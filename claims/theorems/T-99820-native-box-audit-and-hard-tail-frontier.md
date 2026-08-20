# T-99820 — Native box audit and exact Hardy-tail closure frontier

Claim ID: `T-99820`  
Status: **UNCONDITIONAL CORRECTION AND REDUCTION; FINAL RH-EQUIVALENT ESTIMATE OPEN**  
Created: 2026-08-20  
Frozen base: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
Compared: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`; PR #662 at `7af71708570b9621c08b6598efacada7abe84bf2`  
RH status: **unproved**

## Binding correction

The conclusion-facing box is

\[
(\mathcal S_{67}h)(X)/\sqrt X
 =\sum_n\beta(n)n^{-1}\phi(X/n).
\]

Therefore its native prime operator is `I-p^(-1)U_p`. The
`I-p^(-1/2)U_p` operator used on the normalized potential in PR #664 is not the
native source. Its half-order annihilation and unweighted Mertens-window
collar slope cannot be used to prove the canonical scalar sign.

## What survives after repair

- the normalized box potential is nonnegative and increasing;
- every native one-prime step is nonnegative;
- every native two-prime block is positive;
- pairwise positivity still does not supply all-prime composition;
- the exact native collar coefficient is the half-order duplicate-67 window
  `D_67^beta`, not an unweighted Mertens window;
- PR #659's Poisson square is exactly a Hardy square of nested native tails.

## Correct conclusion-facing chain

```text
native normalized box source
 -> p^(-1) Euler factors
 -> half-order duplicate-67 collar window D_67^beta
 -> subpower logarithmic negative mass
 -> zero-free Mellin factor + Landau
 -> RH.
```

By `L-99823`, the displayed negative-mass estimate is equivalent to RH. By
`L-99822`, the GPMOC route is an equivalent nested-tail square formulation of
the same cross-source burden.

## Exact boundary

```text
native box normalization                    PROVED
PR #664 normalized p^(-1/2) operator        NONNATIVE
native one-/two-prime positivity            PROVED
native all-prime composition                OPEN
native collar window                        PROVED EXACT
Hardy tail-square factorization             PROVED EXACT
subpower native-window negative mass        OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
