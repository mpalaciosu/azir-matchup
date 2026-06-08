# Porting this skill to another champion

The skill is not really Azir-specific. If your champion has a classic, trusted
matchup spreadsheet (the kind a dedicated one-trick or coach maintains, like the
Yedaoshen sheet for Talon), you can stand up the same fast, sourced, in-game read
in a few steps.

## What you need

- A trusted matchup spreadsheet for the champion, laid out as a table with at
  least: champion name, a difficulty/rating, and a matchup comment.
- The champion's main subreddit (e.g. `r/TalonMains`) for the community pull.
- Python 3, and `redditwarp` for the Reddit step (`pip install -r requirements.txt`).

## Steps

1. **Swap the data.** Replace `matchups.json` with your champion's matchups. Keep
   the same shape:
   ```json
   {
     "_meta": { "source_author": "<sheet author>", "attribution": "..." },
     "champions": {
       "zed": { "name": "Zed", "rating": "...", "advice": "...", "runes": "" }
     }
   }
   ```
   Keys are the normalized opponent name (lowercase, no spaces/punctuation). If you
   have the sheet as a markdown table, `scripts/build_matchups.py <file>` builds the
   JSON for you.

2. **Point the Reddit helper at the right subreddit.** In
   `scripts/reddit_tips.py`, change `SUBREDDIT = "azirmains"` to your champion's
   subreddit (without the `r/`).

3. **Update name aliases if needed.** In `scripts/lookup.py`, the `ALIASES` map
   handles abbreviations (`lb` -> LeBlanc, etc.). Add any that matter for your
   matchup pool. The prefix fallback covers most cases.

4. **Rewrite `SKILL.md` for your champion.** Replace "Azir" with your champion and
   adjust the briefing guidance (what a tip should capture: key cooldowns, level-6
   counterplay, must-dodge abilities). Keep the rules that make it trustworthy:
   print the comment verbatim, never invent data, cite each tip's source.

5. **Credit the sheet author.** Keep an Attribution section and a takedown note.
   The matchup data is the author's work; reproduce it with clear credit.

6. **(Optional) Refresh flow.** If the sheet lives in Google Drive, set your file
   id in place of `YOUR_DRIVE_FILE_ID` and wire the `--refresh` path as in
   `SKILL.md`.

## Want to do this together?

I'm happy to help port it to your champion and figure out the workflow with you.
Open an issue or email martinpalaciosu@gmail.com.
