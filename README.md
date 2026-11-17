# tiny-chess-01 — 4 KB chess engine

A tiny, original, fully deterministic chess engine in one 4,077-byte
`main.py` (Python 3.13 stdlib only). Board: 0x88. Search: negamax with
alpha-beta, a move-only transposition table, quiescence search (captures,
plus all evasions when in check), futility pruning at depth 1, and MVV move
ordering, over a fixed 100,000-node budget (no clock, no randomness — every
replay is identical).
Eval: material plus arithmetic centralization. Move generation is
perft-verified against python-chess (8 standard positions, depths 1–3, all
exact), including underpromotions, en passant and castling.

Practice trial-1 (make.fun kit scorer, 8 games): Elo 1,464 — 2 wins, 5 draws,
1 loss, no time losses (max ~3.7 s/move, limit 10 s). Practice mean over
trials 0–2: Elo 1,235 (1,253 / 1,464 / 989), vs 1,165 for the previous version.
Built with AI assistance; the build log and test notes live in the
accompanying work directory (not part of this repository).
