# Community-Led Growth for B2B SaaS

Research portfolio on **Community-Led Growth (CLG) for B2B SaaS**. 
Built as a deliverable for the Junior Growth Marketing Specialist role 
at 100Hires (AI-native, remote), but written to be portable: the 
methodology, source list, and frameworks apply to any growth role in 
B2B SaaS where community matters as a long-term moat.

I picked CLG as the topic because in an AI-saturated market, community 
is the hardest moat for competitors to replicate. Most landing pages, 
ad copy, and content can be generated in minutes now. A community of 
engaged users cannot.

---

## What's In This Repo

- **10 community operators** I studied (LinkedIn, YouTube, podcasts)
- **30 LinkedIn posts**, 3 per expert, verbatim with engagement metrics
- **10 YouTube transcripts**, fetched programmatically via Supadata API
- **Critical reading notes** on operator credibility and where to be 
  skeptical per expert (in `sources.md`)
- **Synthesis** covering patterns, tensions, and what's missing in their 
  advice (in `patterns-and-tensions.md`)
- **Applied** layer with execution plays (using 100Hires as working example) 
  (in `applied-case-study.md`)

---

## How To Navigate

If you only have 5 minutes, read these in order:
1. [`sources.md`](research/sources.md): who I studied and why
2. [`patterns-and-tensions.md`](research/patterns-and-tensions.md): what I learned
3. [`applied-case-study.md`](research/applied-case-study.md): how I'd execute on it

The raw collection is in [`/research/linkedin-posts/`](research/linkedin-posts/) and 
[`/research/youtube-transcripts/`](research/youtube-transcripts/) if you want to verify any claim.

Repository structure:

    research/
    ├── linkedin-posts/        # 10 files, 30 posts total
    ├── youtube-transcripts/   # 6 files, 10 transcripts total
    ├── other/                 # blogs, newsletters, critiques
    ├── sources.md             # expert list + credibility notes
    ├── patterns-and-tensions.md   # synthesis
    └── applied-case-study.md     # execution plays
    scripts/
    └── fetch_transcripts.py   # Python + Supadata API automation

---

## How I Worked

I treated this like a real growth marketing brief. Start with a topic 
hypothesis, gather operator-grade signal, find the patterns, then apply 
them to a specific business context. Three decisions matter here.

**1. Topic narrowing.**  
Started broad (growth marketing for SaaS), narrowed to community-led 
growth specifically. Reasoning: CLG forces longer-term thinking, has 
clearer differentiation than "content marketing" or "SEO," and is harder 
to fake with AI.

**2. Expert selection.**  
Started with around 25 names from initial search. Cut to 10 using three 
filters: operator credibility (did they actually build a community?), 
practice what they teach (is their own LinkedIn or YouTube a CLG case 
study?), and tactical specificity (do they share numbers and playbooks, 
or just frameworks?). Full notes in [`sources.md`](research/sources.md) including who I dropped 
and why.

**3. Collection method.**  
LinkedIn posts collected manually because LinkedIn data quality is too 
context-dependent for scraping. YouTube transcripts collected via Python 
script using the Supadata API. Defendable, reusable, auditable. The 
script is in [`/scripts/fetch_transcripts.py`](scripts/fetch_transcripts.py) 
and runs from a `VIDEOS` list, so adding more sources is one config change 
away.

I deliberately did not chase volume. 10 high-signal transcripts beat 50 
generic ones. Same logic for LinkedIn. 3 posts per expert was enough to 
identify pattern. More would have been content padding.

---
## The 10 Experts and Why

The full credibility breakdown and skepticism notes for each are in 
[`sources.md`](research/sources.md). One-liner reasoning here:

**Tier A — Active operators currently running plays**

1. **Rosie Sherry** (Rosieland, ex-Ministry of Testing). Built and sold 
   a community, currently runs another. Publishes pricing, member counts, 
   and workflow experiments openly. Operator showing her work.

2. **Joel Primack** (Salesforce, host of Community-Led Growth Show). 
   Currently in-role practitioner. His 51-episode podcast interviewing 
   community ops leaders is one of the best curated CLG corpora I found.

3. **Lloyed Lobo** (Boast.AI, Traction). Verifiable exit. Bootstrapped 
   to $10M ARR through community. Highest match to early-stage scrappy 
   reality.

4. **Mike Rizzo** (MarketingOps.com). Rare case of community-first, 
   product-second. Reframes CLG as building a product, not running 
   campaigns. Most underrated thinker in the set.

**Tier B — Active practitioner-writers**

5. **Brian Oblinger** (Community Strategy Academy). 20+ years across 
   multiple brands. His CMX Summit talk on community ROI is the single 
   best content I found for defending community budget to a CFO.

6. **Noele Flowers** (Articulate, ex-Commsor). Currently in-role. Her 
   "participate as a model member, not admin" framing counter-intuitive 
   and actionable.

7. **Christina Garnett** (ex-HubSpot, customer trust theorist). HubSpot 
   tenure for B2B SaaS scale. Brings sociology grounding most operators 
   lack.

**Tier C — Foundational operator-veterans**

8. **David Spinks** (CMX, author of *Business of Belonging*). Built the 
   reference community for the entire industry. His book is cited by 
   almost every other expert in this list.

9. **Erica Kuhl** (Gainsight, ex-Salesforce). Built Trailblazer from 0 
   to 3M members over 17 years. Highest-credential community operator 
   in B2B SaaS history.

10. **Mac Reddin** (Commsor). Builds tooling for community operators. 
    Has to understand the practice deeply. Commsor pivoted multiple 
    times, showing his own learning loop.

The selection trades off recency, tactical specificity, and operator 
credibility. Some experts (David Spinks, Erica Kuhl) are foundational 
but their tactical playbooks are pre-2022. Others (Joel Primack, Noele 
Flowers) are currently in-role but less battle-tested. The mix is 
intentional.

---

## What I Did Not Do (And Why)

- **Did not use scraping tools for LinkedIn.** Manual collection forced me 
  to actually read what I was saving. Output quality came from curation, 
  not volume.
- **Did not include every famous community name.** Several "Top 10 community 
  builder" regulars whose recent content is pure thought leadership got 
cut. See [`sources.md`](research/sources.md).
- **Did not write a "framework."** I am not in a position to define a CLG 
  framework. David Spinks, Erica Kuhl, and Lloyed Lobo already have. 
  Instead I documented where they agree, where they disagree, and what 
  their playbooks are missing.

---

## Tools Used

- **Claude Code** (via Cursor IDE) for drafting, code review, search 
  coordination, and structure feedback
- **Supadata API** for YouTube transcript extraction
- **Python** (`requests`, `python-dotenv`) for the automation script
- **Git + GitHub** for version control and public deliverable

---

## Contact

Steven Njosaputera  
Surabaya, Indonesia  
[LinkedIn](https://www.linkedin.com/in/stevennjo/) · [steven.nyo@gmail.com](mailto:steven.nyo@gmail.com)