"""
fetch_transcripts.py
Pull YouTube transcripts via Supadata API and save them as Markdown files
in /research/youtube-transcripts/.

Usage:
    1. Create a `.env` file in this folder with: SUPADATA_API_KEY=sd_yourkey
    2. Add `.env` to your .gitignore (so the key never lands on GitHub).
    3. Install deps:  pip install requests python-dotenv
    4. Run:  python fetch_transcripts.py

The VIDEOS list at the bottom is what you edit when you want to add or
swap content. Each entry has the expert name (used as filename), the
video URL, and a short context note that gets stamped into the markdown.
"""

import os
import sys
import time
from pathlib import Path
from collections import defaultdict

import requests
from dotenv import load_dotenv


# --- Config ---------------------------------------------------------------

load_dotenv()
API_KEY = os.getenv("SUPADATA_API_KEY")
ENDPOINT = "https://api.supadata.ai/v1/youtube/transcript"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "research" / "youtube-transcripts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if not API_KEY:
    sys.exit("Missing SUPADATA_API_KEY. Add it to a .env file in this folder.")


# --- API call -------------------------------------------------------------

def fetch_transcript(url: str, lang: str = "en") -> dict:
    """Hit Supadata and return JSON. Retry on 429/5xx."""
    headers = {"x-api-key": API_KEY}
    params = {"url": url, "lang": lang, "text": "true"}

    for attempt in range(3):
        resp = requests.get(ENDPOINT, headers=headers, params=params, timeout=60)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (429, 500, 502, 503, 504):
            wait = 2 ** attempt
            print(f"  ! {resp.status_code} - retry in {wait}s")
            time.sleep(wait)
            continue
        raise RuntimeError(f"Supadata {resp.status_code}: {resp.text[:200]}")
    raise RuntimeError(f"Failed after 3 attempts: {url}")


# --- Markdown writer ------------------------------------------------------

def slugify(name: str) -> str:
    return name.lower().replace(" ", "-").replace(".", "")


def build_markdown_for_expert(expert: str, videos: list) -> str:
    """Compose one markdown file with all videos for that expert."""
    lines = [
        f"# {expert} - YouTube Transcripts",
        f"**Collected via Supadata API on**: 2026-06-21",
        "",
        "---",
        "",
    ]

    for i, v in enumerate(videos, start=1):
        lines += [
            f"## Video {i} - {v['title']}",
            f"**Source**: {v['url']}",
            f"**Context**: {v['context']}",
            "",
            "### Transcript",
            "",
            v["transcript"].strip(),
            "",
            "### Why I picked this",
            v["why"],
            "",
            "---",
            "",
        ]

    return "\n".join(lines)


# --- Main -----------------------------------------------------------------

def main(videos):
    grouped = defaultdict(list)

    for v in videos:
        print(f"-> {v['expert']} :: {v['title']}")
        try:
            data = fetch_transcript(v["url"])
            # Supadata returns `content` when text=true. Fall back to segments.
            transcript_text = data.get("content") or data.get("transcript") or ""
            if isinstance(transcript_text, list):
                transcript_text = " ".join(seg.get("text", "") for seg in transcript_text)

            grouped[v["expert"]].append({
                "title": v["title"],
                "url": v["url"],
                "context": v["context"],
                "transcript": transcript_text,
                "why": v["why"],
            })
            print(f"   ok ({len(transcript_text)} chars)")
        except Exception as e:
            print(f"   FAILED: {e}")
            grouped[v["expert"]].append({
                "title": v["title"],
                "url": v["url"],
                "context": v["context"],
                "transcript": f"_Transcript fetch failed: {e}_",
                "why": v["why"],
            })

    for expert, vids in grouped.items():
        path = OUTPUT_DIR / f"{slugify(expert)}.md"
        path.write_text(build_markdown_for_expert(expert, vids), encoding="utf-8")
        print(f"wrote {path}")


# --- Edit this list -------------------------------------------------------

VIDEOS = [
    {
        "expert": "David Spinks",
        "title": "The Business of Belonging Launch Party",
        "url": "https://www.youtube.com/watch?v=PZbFC-fokR8",
        "context": "Launch event for his book on community as competitive advantage. Includes reading, AMA, and interview format.",
        "why": "His book is the canonical playbook on community-as-moat for B2B. Launch event captures the core thesis in his own voice plus live Q&A pressure-testing it."
    },
    {
        "expert": "David Spinks",
        "title": "What If Taking Care of Each Other Was Enough (CMX Founder)",
        "url": "https://www.youtube.com/shorts/7ZdteE-06aM",
        "context": "Short-form 2026 take from David questioning the tech-solution-first mindset.",
        "why": "Most recent David Spinks content on YouTube (May 2026). Shows where his thinking has moved post-Bevy."
    },
    {
        "expert": "Erica Kuhl",
        "title": "Uncommon Conversations: Strategy w/ Common Room",
        "url": "https://www.youtube.com/watch?v=gX5EgWQQxok",
        "context": "Deep dive on her Trailblazer playbook: metrics, internal buy-in, where community sits org-wise, V2MOM prioritization.",
        "why": "Single most tactical Erica interview on YouTube. Operator-grade detail on measurement, buy-in, persona work, and team placement."
    },
    {
        "expert": "Joel Primack",
        "title": "The Community-Led Growth Show Ep 02 w/ Nisha Baxi (Gong)",
        "url": "https://www.youtube.com/watch?v=z5ffP8Z04OE",
        "context": "Joel interviews Nisha Baxi on building Gong's community from zero in 8 months.",
        "why": "Joel's interviewing style shows what questions he thinks matter for CLG. Gong is a high-signal B2B SaaS case."
    },
    {
        "expert": "Joel Primack",
        "title": "The Community-Led Growth Show Ep 17 w/ Joe Huber (Sprout Social)",
        "url": "https://www.youtube.com/watch?v=6RzvrNSBw78",
        "context": "Joel interviews Joe Huber on Sprout Social's customer community strategy.",
        "why": "Second Joel episode for triangulation. Sprout Social is mid-market SaaS, closer in scale to typical 100Hires-target companies."
    },
    # Add more below once URLs are confirmed for Lloyed, Brian, Mike
]


if __name__ == "__main__":
    main(VIDEOS)