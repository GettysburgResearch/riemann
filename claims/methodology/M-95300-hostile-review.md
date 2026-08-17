# M-95300 — Hostile review protocol for the carry root-port correction

Review in this order:

1. `R-95300`: recompute \(1*b_2\), the interior annihilator and the radical
   noncancellation.
2. `L-95300`: check multiples Möbius inversion, size conservation, the
   six-node relation and the root edge \(\gamma=\chi_{3,1}\).
3. `L-95301`: check the endpoint increment and deleted-column-one Mellin term.
4. `T-95300`: ensure no one-channel positivity is inferred from the signed or
   two-channel constructions.

Immediate falsifiers:

```text
one interior edge with nonzero b2 response;
one T>=7 with rho_T=0;
an incorrect q=1 physical column;
a root-port coefficient different from -rho(w);
a claim that rho_T has an unconditional eventual sign;
a claim that two-channel positivity proves one-channel PICR.
```
