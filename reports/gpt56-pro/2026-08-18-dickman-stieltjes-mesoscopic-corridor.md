# Research report: complete-base Stieltjes transfer and a mesoscopic Dickman corridor

## Verdict

The centered-boundary audit is binding: the positive finite-Euler main is
cancelled at the almost-full-product boundary, so uncentered boundary
positivity is false. The correct next move is to recombine the complete
`P_61` base before comparing the rough-prime measure to its continuous model.

The exact identity

\[
\mathcal F(Y,z)/\sqrt Y=\int A_z(Y/x)\,dh(x)
\]

achieves that recombination. The normalized base `h=b/sqrt(x)` has finite
exponentially weighted variation and total signed mass `a_*>0`. Its continuous
Dickman transport is therefore `a_*rho(u)(1+o(1))` whenever
`log z >> log u`.

PR #603 used a coarse prime-reciprocal discrepancy `O(1/log z)` and treated the
bounded base remainder separately. The exact transfer leaves only one
prime-measure discrepancy. At Vinogradov--Korobov strength this is

\[
O\bigl(u\exp[-c(\log z)^{3/5}(\log\log z)^{-1/5}]\bigr).
\]

Comparison with de Bruijn's lower bound for `rho` proves positivity through

\[
u\le c_0(\log Y)^{3/8}(\log\log Y)^{-3/4}.
\]

This is a genuine unconditional advance but not the full producer. The fixed
or very small least-prime root remains open and retains the reciprocal-zeta
sign obstruction.

## Strategic next step

The remaining attack should not return to an absolute bounded remainder. It
should seek either:

1. a signed prime-measure discrepancy estimate after the completed small-prime
   Euler operator;
2. a future-prime Bellman barrier whose base is the Stieltjes profile; or
3. a centered Type-II estimate for the exact zero hinge.
