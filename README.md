# tiny-chess-01 — 4 KB chess engine

A tiny, original, fully deterministic chess engine in one 4,051-byte
`main.py` (Python 3.13 stdlib only). Board: 0x88. Search: negamax with
alpha-beta, a move-only transposition table, quiescence search (captures,
plus all evasions when in check) and MVV move ordering, over a fixed
100,000-node budget (no clock, no randomness — every replay is identical).
Eval: material plus arithmetic centralization. Move generation is
perft-verified against python-chess (8 standard positions, depths 1–3, all
exact), including underpromotions, en passant and castling.

Practice trial-1 (make.fun kit scorer, 8 games): Elo 1,253 — 2 wins, 2 draws,
4 losses, no time losses (max ~3.6 s/move, limit 10 s).
Built with AI assistance; the build log and test notes live in the
accompanying work directory (not part of this repository).
