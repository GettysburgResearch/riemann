# R-98901 — Local Tao atoms do not supply the claimed isometric Fock direct limit

Claim ID: `R-98901`  
Status: **PROVED INTERFACE REFUTATION; UNPHASED LOCAL PORT RETAINED**  
Created: 2026-08-18  
Depends on: `L-98901`

The exact arithmetic part of `L-98701` constructs a positive local matrix at
phase zero. `L-98703` then asserts, without a transition formula, that the same
labels form a phase-covariant directed system and that the local diagonal pays
the reflected heat cross block.

`L-98901` gives an exact one-prime counterexample to that inference:

```text
P={3}, x=3, tau=pi/log 3;
unphased Tao diagonal C=8/9;
phased reciprocal off-diagonal A_tau=4/3;
Schur determinant=-80/81.
```

Therefore the obvious phase lift is not positive even before any infinite
cutoff or Stieltjes limit.

There is a second normalization obstruction. At a finite odd-prime cutoff `P`,
the positive fractional-chaos mass contains the Euler factor

\[
\prod_{p\in P}(1-p^{-1/2})^{-\theta},
\]

whose logarithm is at least

\[
\theta\sum_{p\in P}p^{-1/2}
\]

and diverges with the cutoff. The statement “each Tao diagonal is at most one,
therefore the completed Fock source has uniformly bounded trace” does not
follow: tensor/Fock history mass is not the local port diagonal.

Accordingly, weak compactness in `L-98703` cannot be invoked until a separate
heat-regularized, phase-covariant diagonal bound has actually been proved. That
missing bound is the load-bearing theorem, not a consequence of `L-98701`.
