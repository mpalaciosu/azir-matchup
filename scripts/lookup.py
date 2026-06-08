#!/usr/bin/env python3
"""Look up a champion's Azir matchup from matchups.json.

Usage:
    lookup.py "<champion or abbreviation>"

Prints one of:
  - a matched entry:
        NAME: <display name>
        RATING: <rating>
        ADVICE: <verbatim advice text>
        RUNES: <runes>
  - EMPTY  (row exists but the advice cell is blank; treat as "not in the sheet")
  - NOT_FOUND  (no such champion in the sheet)
  - AMBIGUOUS: a, b, c  (short input matched more than one champion)

Owns the name-matching so the model doesn't have to: case-insensitive, ignores
spaces/apostrophes/periods, plus common abbreviations. Exit code is always 0;
read the first printed token to branch.
"""
import io
import json
import os
import sys

# Abbreviations and nicknames -> normalized canonical key.
ALIASES = {
    "lb": "leblanc",
    "cho": "chogath",
    "asol": "aurelionsol",
    "tf": "twistedfate",
    "mundo": "drmundo",
    "kog": "kogmaw",
    "vel": "velkoz",
    "velkoz": "velkoz",
    "gp": "gangplank",
    "ksante": "ksante",
    "yi": "masteryi",
    "kass": "kassadin",
    "ww": "warwick",
    "morde": "mordekaiser",
    "akshan": "akshan",
}


def _norm(name):
    return "".join(ch for ch in name.lower() if ch.isalnum())


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("NOT_FOUND")
        return 0
    query_raw = " ".join(sys.argv[1:]).strip()
    key = _norm(query_raw)

    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(skill_dir, "matchups.json")
    if not os.path.exists(path):
        print("NOT_FOUND")
        return 0
    data = json.loads(io.open(path, encoding="utf-8").read())
    champs = data.get("champions", {})

    key = ALIASES.get(key, key)

    entry = champs.get(key)

    # Fall back to prefix match if no exact hit (e.g. "kata" -> "katarina").
    if entry is None:
        prefix = [k for k in champs if k.startswith(key)]
        if len(prefix) == 1:
            entry = champs[prefix[0]]
        elif len(prefix) > 1:
            print("AMBIGUOUS: " + ", ".join(champs[k]["name"] for k in sorted(prefix)))
            return 0

    if entry is None:
        print("NOT_FOUND")
        return 0
    if not entry.get("advice", "").strip():
        print("EMPTY")
        print("NAME: " + entry["name"])
        return 0

    print("NAME: " + entry["name"])
    print("RATING: " + (entry.get("rating") or "").strip())
    print("ADVICE: " + entry["advice"])
    print("RUNES: " + (entry.get("runes") or "").strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
