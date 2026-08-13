# O-91402 — Hazard/curvature synthesis after the P61 row closure

**Status:** PROPOSED — pending independent review.

The retained theorem on this branch closes strict positivity of every inherited `P_61` component row. The next all-prime problem is not another fixed-prime sign check; it is an infinite hidden-mass envelope.

Let `M_n` be hidden mass before the currently least unobserved rough prime `p_n`, `C_n` safely captured mass, and `B_n` genuinely new boundary debt. Suppose

\[
M_{n+1}\le M_n-C_n,
\qquad
C_n\ge \frac{c}{p_n}M_n,
\qquad
B_n\le \frac{C}{p_n^2}M_n.
\]

Then

\[
M_K\le M_N\exp\!\left(-c\sum_{n=N}^{K-1}\frac1{p_n}\right),
\]

and

\[
\sum_{n\ge N}B_n\le \frac{C}{c\,p_N}M_N.
\]

Hence the divergent Euler hazard exhausts the hidden mass, while quadratic leakage is `o(M_N)`. No uniform contraction constant is required.

Two local mechanisms can supply the hypotheses.

1. If there are `p_n` causal phases and every source atom is safe in at least `q` phases, averaging gives a phase with

\[
C_n\ge \frac{q}{p_n}M_n.
\]

This is distribution-free and does not assume residue equidistribution.

2. If the new signed boundary packet has support radius `R`, zero total mass, zero first displacement moment, and half-total-variation at most `A M_n`, then

\[
|\langle f_n,\nu_n\rangle|
\le R(R+1)A M_n\|\Delta^2f_n\|_\infty.
\]

Thus a physical score-curvature bound

\[
\|\Delta^2f_n\|_\infty\le K/p_n^2
\]

gives quadratic leakage with constant `C=R(R+1)AK`. For displacement radius eight, `R(R+1)=72`.

The exact native frontier is therefore:

- construct the causal phase cover inside the same parent support;
- prove safe-cover multiplicity at least one;
- identify the genuinely new boundary packet after inherited reserve subtraction;
- prove zero mass and zero first moment;
- prove uniform radius/variation control;
- prove the `O(p^-2)` score-curvature estimate.

These statements would combine with the existing substochastic packet consumer to close the infinite rough-prime envelope. They are not proved by the fixed `P_61` certificate, and RH remains unproved.