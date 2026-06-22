# Community-Led Growth for B2B SaaS

Research portfolio for the **Junior Growth Marketing Specialist** role 
at 100Hires (AI-native, remote).

I picked Community-Led Growth (CLG) as the topic because in an AI-saturated 
market, community is the hardest moat for competitors to replicate. Most 
landing pages, ad copy, and content can be generated in minutes now. 
A community of engaged users cannot.

---

## What's In This Repo

- **10 community operators** I studied (LinkedIn, YouTube, podcasts)
- **30 LinkedIn posts** — 3 per expert, verbatim with engagement metrics
- **11 YouTube transcripts** — fetched programmatically via Supadata API
- **Critical reading notes** — operator credibility + where to be skeptical 
  per expert (in `sources.md`)
- **Synthesis** — patterns, tensions, and what's missing in their advice 
  (in `patterns-and-tensions.md`)
- **Applied** — what this means for 100Hires specifically 
  (in `applied-to-100hires.md`)

---

## How To Navigate

If you only have 5 minutes, read these in order:
1. `sources.md` — who I studied and why
2. `patterns-and-tensions.md` — what I learned
3. `applied-to-100hires.md` — how I'd execute on it

The raw collection is in `/research/linkedin-posts/` and 
`/research/youtube-transcripts/` if you want to verify any claim.

Repository structure:

    research/
    ├── linkedin-posts/        # 10 files, 30 posts total
    ├── youtube-transcripts/   # 6 files, 11 transcripts total
    ├── other/                 # blogs, newsletters, critiques
    ├── sources.md             # expert list + credibility notes
    ├── patterns-and-tensions.md   # synthesis
    └── applied-to-100hires.md     # execution plays
    scripts/
    └── fetch_transcripts.py   # Python + Supadata API automation

---

## How I Worked

I treated this like a real growth marketing brief: start with a topic 
hypothesis, gather operator-grade signal, find the patterns, then apply 
them to a specific business context. Three decisions matter here.

**1. Topic narrowing.**  
Started broad (growth marketing for SaaS), narrowed to community-led 
growth specifically. Reasoning: CLG forces longer-term thinking, has 
clearer differentiation than "content marketing" or "SEO," and is harder 
to fake with AI.

**2. Expert selection.**  
Started with ~25 names from initial search. Cut to 10 using three filters: 
operator credibility (did they actually build a community?), practice what 
they teach (is their own LinkedIn/YouTube a CLG case study?), and tactical 
specificity (do they share numbers and playbooks, or just frameworks?). 
Full notes in `sources.md` including who I dropped and why.

**3. Collection method.**  
LinkedIn posts collected manually because LinkedIn data quality is too 
context-dependent for scraping. YouTube transcripts collected via Python 
script using the Supadata API — defendable, reusable, auditable. The 
script is in `/scripts/fetch_transcripts.py` and runs from a `VIDEOS` 
list, so adding more sources is one config change away.

I deliberately did not chase volume. 11 high-signal transcripts beat 50 
generic ones. Same logic for LinkedIn — 3 posts per expert was enough to 
identify pattern, more would have been content padding.

---

## What I Did Not Do (And Why)

- **Did not use scraping tools for LinkedIn.** Manual collection forced me 
  to actually read what I was saving. Output quality came from curation, 
  not volume.
- **Did not include every famous community name.** Several "Top 10 community 
  builder" regulars whose recent content is pure thought leadership got 
  cut. See `sources.md`.
- **Did not write a "framework."** I am not in a position to define a CLG 
  framework — David Spinks, Erica Kuhl, and Lloyed Lobo already have. 
  Instead I documented where they agree, where they disagree, and what 
  their playbooks are missing.

---

## Tools Used

- **Claude Code** (via Cursor IDE) — drafting, code review, search 
  coordination, structure feedback
- **Supadata API** — YouTube transcript extraction
- **Python** (`requests`, `python-dotenv`) — automation script
- **Git + GitHub** — version control, public deliverable

---

## Contact

Steven Njosaputera  
Surabaya, Indonesia  
[https://www.linkedin.com/in/stevennjo/]
[steven.nyo@gmail.com]