# Factor-67 compact-reserve closure packet

This packet is the successor to the initial factor-67 SONTR proposal on PR
#473.  It closes the proposal's remaining compact reserve obligation by proving
that target Hall is exact in the total physical equality row and by replacing
all abstract approximation constants with explicit strict native-capacity
margins.

Normative files:

```text
claims/lemmas/L-91692-target-hall-is-row-transparent-and-the-factor67-reserve-is-explicit.md
claims/theorems/T-91661-factor67-compact-reserve-closes-the-sontr-producer-gate.md
claims/observations/O-91692-factor67-reserve-closure-frontier.md
experiments/X-91692-factor67-reserve-closure/
reports/gpt56-pro/2026-08-14-factor67-compact-reserve-proof.md
```

Core exact constants:

```text
Hall total-row error             0
159/500 < L(x)                  <183/100<2
C67                              <19
interior reserve                 41 Omega/[32(K+178)]
terminal reserve                 581 X^(-3/2)
P61/67 port                      one aggregate port
recursive coefficient mass      <1/8
```

The packet proves the compact reserve obligation on frozen interfaces.  It does
not independently reprove every frozen dependency and does not claim RH.
