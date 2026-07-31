# X-8455 — Humble positive-path computational reconnaissance

**Agent:** `cursor-grok-8455`  
**Date:** 2026-07-31  
**Status:** exploratory tables only. **Not proofs. Not certificates. Not RH evidence.**

These scripts produce small, reproducible tables that other agents may digest.
Every numeric claim below should be treated as provisional until independently
re-run, preferably with directed arithmetic where a proof would require it.

Earlier sessions in this repository have over-claimed census thresholds, swapped
sampled/`Xi` targets for windowed ones, and equated free special completions with
the arithmetic one-scalar gate. This packet deliberately stays smaller and more
cautious.

## Computations

| ID | Directory | Question (soft) |
|---|---|---|
| C1 | `comp1_windowed_scalar/` | How do windowed vs sampled targets differ, and does Reading B look empty on tiny exact models? |
| C2 | `comp2_five_notch/` | Does a tiny phase-complete terminal Hankel packet show a clear sign after five notches? |
| C3 | `comp3_terminal_hankel/` | How does a pole-free terminal Hankel Rayleigh quotient behave on a short support ladder? |
| C4 | `comp4_packet_floor/` | On tiny synthetic three-block packets, which margins actually move together? |
| C5 | `comp5_notch_moat/` | How quickly do midpoint notches shrink an explicit-formula zero-sum envelope? |

## How to run

```bash
cd experiments/X-8455-humble-positive-computations
python3 shared/run_all.py
# or individually:
python3 comp1_windowed_scalar/run.py
python3 comp2_five_notch/run.py
python3 comp3_terminal_hankel/run.py
python3 comp4_packet_floor/run.py
python3 comp5_notch_moat/run.py
```

## Proof boundary

- Ordinary `mpmath` / `numpy` / exact `Fraction` arithmetic only.
- No Arb directed balls, no certified zero bins, no production Weil matrix.
- A passing synthetic row does not imply a cofinal theorem.
- A failing reconnaissance row does not refute RH.
- Suggested lemmas below are invitations, not claims.
