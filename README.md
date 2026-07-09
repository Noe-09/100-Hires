— What tools you installed
Cursor IDE.
Git & GitHub Desktop (I actually already had these installed and set up. I've been learning and playing around with building web demos recently, so I already have an active GitHub account with a few different repos created).

— What steps you completed
Installed Cursor and logged in.
Created a brand new public repository specifically for this project in GitHub Desktop
Opened the repository in Cursor.
Created a new file and named it README.md
Drafted this README.md file.
Committed the changes and pushed them to GitHub.

— What issues you ran into and how you solved them
The issue: At first I was new to this app so I got a bit stuck at the extensions step. The instructions said to install the "Claude Code" and "Codex" add-ons from the Extensions tab. I spent some time looking for them, but my Cursor interface looked a bit different (Extensions seem to be merged into Plugins now), and I couldn't find those specific standalone extensions in the search.
The solution: Instead of getting stuck or downloading older versions, I did a quick search online to see how Cursor handles AI models now. I realized that Cursor is already built as an AI-first IDE, meaning Claude and Codex are directly integrated into the software's core features (like the Composer and Agent tools). So, I realized I didn't need to install external add-ons anymore. I just went straight to using the built-in AI features that are already set up inside the app.
# AI-Powered SEO Content Production for B2B SaaS

This repository is part of a portfolio project for a Junior Growth Marketing Specialist application.

The chosen topic is:

**AI-powered SEO content production for B2B SaaS**

---

## Overview

This project is a research collection about how B2B SaaS companies can use AI in their SEO content workflow.

I chose this topic because SEO and content are important growth channels for many SaaS companies. AI can support research, outlines, drafting, editing, optimization, transcript analysis, and content repurposing. However, I do not see AI content as simply “generate more articles faster.” The more important question is how AI can improve the content process while still keeping quality, accuracy, and usefulness.

The goal of this repository is not to create a final playbook yet. The goal is to collect and organize strong source material from people who actually work in SEO, content marketing, AI search, AEO/GEO, content distribution, and B2B growth.

---

## Why I Chose This Topic

100Hires operates in a content-heavy B2B SaaS category. Topics such as applicant tracking systems, hiring workflows, recruiting automation, sourcing, interview processes, ATS comparisons, and HR software can all be supported by useful SEO content.

Because of that, I thought **AI-powered SEO content production** would be a relevant topic to research. It connects growth marketing, SEO, content operations, AI tools, technical workflows, and B2B customer acquisition.

I also wanted to avoid generic AI content advice. I focused on experts who show practical thinking around SEO systems, AI search visibility, answer engines, content quality, distribution, and workflow design.

---

## What I Collected

This repository includes:

- A list of 10 selected experts with profile links and brief annotations
- LinkedIn posts organized by author
- YouTube transcripts organized by video
- Supporting materials such as articles, checklists, webinars, podcast pages, and blog posts
- Notes on why each source is useful for a future playbook

---

## Selected Experts

The final expert list includes:

1. Julian Goldie
2. Matt Diggity
3. Gael Breton
4. Nathan Gotch
5. Aleyda Solis
6. Michael King / Mike King
7. Andy Crestodina
8. Ross Simmonds
9. Bernard Huang
10. Michal Suski

I selected a mix of AI SEO practitioners, SEO testing operators, technical SEO experts, content distribution specialists, B2B content strategists, and founders connected to SEO content optimization tools.

---

## Repository Structure

```text
research/
  sources.md
  methodology.md
  linkedin-posts/
    julian-goldie/
    matt-diggity/
    gael-breton/
    nathan-gotch/
    aleyda-solis/
    michael-king/
    andy-crestodina/
    ross-simmonds/
    bernard-huang/
    michal-suski/
  youtube-transcripts/
    julian-goldie/
    matt-diggity/
    gael-breton/
    nathan-gotch/
    aleyda-solis/
    michael-king/
    andy-crestodina/
    ross-simmonds/
    bernard-huang/
    michal-suski/
  other/
    julian-goldie/
    matt-diggity/
    gael-breton/
    nathan-gotch/
    aleyda-solis/
    michael-king/
    andy-crestodina/
    ross-simmonds/
    bernard-huang/
    michal-suski/

scripts/
  videos.csv
  fetch_youtube_transcripts.py
  format_transcript.py
  normalize_markdown.py

README.md
requirements.txt
.env.example
```

---

## Source Organization

The research materials are organized into four main parts:

### `research/sources.md`

This file lists the 10 selected experts, their profile links, access dates, and brief annotations explaining why each expert was selected.

### `research/linkedin-posts/`

This folder contains LinkedIn posts organized by author.

Each author folder includes collected posts related to:

- AI SEO
- AI Search
- Content production
- AEO / GEO
- Content distribution
- B2B content strategy

### `research/youtube-transcripts/`

This folder contains YouTube transcripts organized by video.

The transcripts are used as long-form source material for understanding how each expert explains their process, frameworks, and practical examples.

### `research/other/`

This folder contains supporting materials such as:

- Articles
- Checklists
- Webinar pages
- Podcast pages
- Blog posts
- Official resource pages

---

## Collection Method

I used a mix of manual collection and lightweight automation.

- LinkedIn posts were collected manually because LinkedIn access is limited and source quality required manual review.
- YouTube transcripts were collected through transcript tools or manually when needed.
- Some transcript formatting was normalized with local Python scripts so timestamps were easier to read in Markdown.
- Supporting materials were collected from official websites, blogs, webinars, resource pages, or podcast pages.

I prioritized fewer high-signal sources over collecting a large volume of generic content.

---

## Tools Used

For the initial setup and research collection, I used:

- **Cursor IDE** for editing the repository and working with project files
- **GitHub Desktop** for creating the repository, committing changes, and pushing to GitHub
- **Git / GitHub** for version control and public portfolio hosting
- **Python** for transcript formatting and cleanup
- **Markdown** for organizing research notes and source files
- **Cursor built-in AI tools** for code support, structure review, and workflow guidance

I also created lightweight local scripts to help with transcript collection and formatting:

- `scripts/videos.csv` - tracks selected YouTube videos
- `scripts/fetch_youtube_transcripts.py` - supports transcript collection
- `scripts/format_transcript.py` - cleans transcript timestamps
- `scripts/normalize_markdown.py` - helps normalize Markdown formatting

---

## Current Status

The first version of the research collection is complete.

The repository now contains:

- 10 selected experts
- Expert profile links and brief annotations
- LinkedIn post collections organized by author
- YouTube transcript files organized by video
- Supporting materials organized by expert
- Scripts used during transcript collection and formatting
- A documented methodology for expert selection and source organization

This research can be used later to build a practical playbook on AI-powered SEO content production for B2B SaaS.
## Methodology

The full research methodology is documented in `research/methodology.md`.

It explains how I selected experts, what types of sources I collected, how I reviewed source quality, and what limitations this research has.