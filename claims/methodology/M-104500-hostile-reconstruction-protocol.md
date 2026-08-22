# M-104500 — Hostile reconstruction protocol for the Xi reverse-Rolle cascade

## Review order

1. `R-104500` — verify both counterexamples and the missing factor two.
2. `L-104500` — reconstruct the adjacent-critical-value identity and every
   boundary convention.
3. `L-104501` — reconstruct the argument-principle winding and the iterated
   off-real-zero ledger on one common domain.
4. `L-104502` — verify the Riccati recursion, residue sign and Pick-kernel
   diagonal.
5. `L-104503` — check that local uniform cosine convergence plus Rouche and
   conjugation symmetry really gives one simple real zero in every disk.
6. `T-104500` — verify the even-integer rigidity and the precise two open gates.
7. Run `experiments/X-104500-reverse-rolle/verify.py` and compare its retained
   result byte-for-byte.

## Immediate falsifiers

Reject or narrow the packet at the first occurrence of:

- coefficient one instead of coefficient two for a wrong extremum;
- ignoring the adjacent critical value on either side of an extremum;
- deleting `B_-`, `B_+`, or `W-1` on a finite domain;
- counting a multiple critical point as a generic simple one;
- claiming that diagonal Pick signs imply a full Pick kernel;
- using the actual-Xi order-three reserve at several derivative levels;
- turning compact cosine convergence into an expanding-box theorem without a
  quantitative uniform estimate;
- inferring zero exceptional count from a proportion without multiplying by
  the total zero count;
- changing the derivative order after observing a hypothetical zero without a
  uniform order-height theorem;
- claiming RH from the finite exact replay.

## Mutation suite

Mandatory controls include:

```text
p(x)=x^4-2x^2+2;
f(z)=2+cos z;
polynomials whose derivatives have nonreal zeros;
intervals with each of the four endpoint-defect patterns;
contours with nontrivial W(F,F';Omega);
finite Pick matrices with positive diagonals but negative determinant.
```

## Status discipline

The exact reverse-Rolle laws and fixed-scaled-box theorem are unconditional.
`GBOX104500` and `RPCH104500` are open.  RH remains unproved until both are
proved on one common growing rectangle with one nonduplicated defect ledger.
