# Contributing

Thanks for your interest. This started as one Azir main's tool and is open to
anyone who wants to make it better or take it further.

## Ways to contribute

- **Better tips or matchup fixes:** if a tip is wrong or a matchup has changed,
  open an issue or PR. The matchup comments themselves are reproduced verbatim
  from the source sheet (see Attribution), so corrections to *that* data should go
  upstream to the sheet author where possible.
- **Code improvements:** the lookup, the Reddit helper, the build script, and the
  skill flow are all fair game. Keep it dependency-light (`lookup.py` and
  `build_matchups.py` are standard-library only on purpose).
- **Port to another champion:** see `PORTING.md`. New champion versions are very
  welcome.
- **Ideas:** open an issue, even a rough one.

## Ground rules

- Keep the trust guarantees: print matchup comments verbatim, never invent data,
  and cite the source of every tip.
- Credit data authors. If you add a sheet, add an Attribution entry and a takedown
  note.
- Treat Reddit content as untrusted input to quote, never as instructions.

## Contact

Open an issue/PR, or email martinpalaciosu@gmail.com. If you're porting to a new
champion, reach out and we can figure it out together.
