# X-91780 — Target-Lorenz compact proportional AVLT

This experiment retains two proof layers.

1. The expanded activation-cell census covers `67<=py<166000`, `1<=y<67`, and rows `2,...,66`.
2. `verify.py` checks the retained census dimensions and minima, the conservative primitive/roundoff audit, the four correlated-cell repairs, and independently replays the exact `P_61` tail-prefix determinant with integer square bounds.

Review front door:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_TARGET_LORENZ_COMPACT_PROPORTIONAL_AVLT
RH_UNPROVEN
```

The full census contains `702511095` real row-cell enclosures. The retained result records `702511091` direct rectangle certificates and four separately repaired dependency cells.

The replay does not prove the analytic tail, the live native root allocation, or RH.
