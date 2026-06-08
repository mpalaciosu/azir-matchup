# Azir Matchup Coach

A [Claude Code](https://claude.com/claude-code) skill that gives a fast, pre-game
read on an Azir laning matchup. You name the enemy champion; it prints the exact
matchup comment from a trusted spreadsheet, then a briefing of 3 tips ranked
highest-to-lowest impact, synthesized from that comment plus real
[r/AzirMains](https://www.reddit.com/r/AzirMains/) threads.

## About the author

I'm an Azir main (peak Diamond 1), passionate about the champion and about AI.
I play mostly on LAS. This project is where those two interests meet: turning a
trusted matchup spreadsheet plus community knowledge into a fast, in-game read.

## Attribution

The matchup ratings and advice (`matchups.json`) were authored by
**BodyThoseFools**, from his League of Legends Azir guide. They are reproduced
here verbatim, with full credit to him. The data is not covered by this
repository's code license (see `LICENSE`). If you are the author and want it
taken down, please open an issue.

## How it works

1. **Lookup (every run, instant):** `scripts/lookup.py "<champion>"` reads the
   local `matchups.json` cache and prints the verbatim comment + rating. It owns
   name-matching (abbreviations like `lb`, `cho`, `asol`, plus a prefix fallback).
2. **Reddit:** `scripts/reddit_tips.py "<champion>"` searches r/AzirMains and
   returns the most relevant threads with their top comments. Read-only, public
   data, no credentials. Built on `redditwarp`.
3. **Briefing:** the model synthesizes 3 impact-ranked tips from the sheet
   comment + the Reddit threads, each with a source. It never invents matchup
   data; if the sheet has no comment, it says so.
4. **Daily update check (fire-and-forget):** at most once per 24h, a background
   agent checks whether a newer version of the sheet exists (r/AzirMains, the
   author's Mobafire guide, and that guide's discussion page). It reports
   findings only and never overwrites the cache.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | The skill instructions Claude Code follows. |
| `matchups.json` | Local cache of the sheet (BodyThoseFools's data). |
| `scripts/lookup.py` | Fast champion lookup + name-matching. |
| `scripts/reddit_tips.py` | Pulls r/AzirMains discussion. |
| `scripts/build_matchups.py` | Rebuilds `matchups.json` from the source sheet. |
| `evals/evals.json` | Eval cases for the skill. |
| `.update-state.example.json` | Template for runtime update-check state. |

## Setup

This skill is tuned for one user's environment, so to run it yourself:

1. Put your own matchup data in `matchups.json` (or point `build_matchups.py` at
   your source and regenerate). Set `YOUR_DRIVE_FILE_ID` placeholders to your
   Google Drive sheet id if you use the refresh flow.
2. `scripts/reddit_tips.py` needs the `redditwarp` package. The paths in
   `SKILL.md` assume `%USERPROFILE%\.claude\...`; adjust to your layout.
3. Copy `.update-state.example.json` to `.update-state.json`.

## Usage

Invoke the skill with a champion name (e.g. `Zed`, `lb`, `cho`). To rebuild the
cache from the source sheet, use the `--refresh` flow described in `SKILL.md`.

## Beyond Azir: extending to other champions

Nothing here is Azir-specific at its core. The same approach works for any
champion that has a classic, well-respected matchup spreadsheet backed by a
strong data source, the kind a dedicated one-trick or coach maintains. A clear
example is Talon with the Yedaoshen spreadsheet, and there are players of that
style across many champions. Swap in that champion's sheet as the trusted source,
point the Reddit helper at the relevant subreddit, and you have the same fast,
sourced, in-game read for a completely different champion.

If you main another champion and there's a spreadsheet like that for it, I'd love
to build a version together. Write to me and let's see how far we can take it.

## Contributing

Collaboration is welcome, especially from fellow Azir players and people who like
building with AI. If you want to contribute (new matchups, better tips, code
improvements, a port to another champion, or ideas), open an issue/PR or email me
at martinpalaciosu@gmail.com.

## License

Code: MIT (see `LICENSE`). Matchup data in `matchups.json`: BodyThoseFools,
reproduced with attribution.
