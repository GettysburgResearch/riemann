# Fractional Julia heat candidate: pole-branch audit and corrected frontier

This add-only packet audits PR #613 at exact head
`f28aa51a6d6740067202611d8ebda4be2ef0a1c9`.

It proves that the uniform heat-energy estimate asserted in `L-98703` is false
for every sufficiently small fractional intensity. The obstruction is
unconditional and deterministic: the fractional zero of
`B_diamond(s)^theta` at the zeta pole `s=1` is a branch point, and its
Selberg--Delange contribution has Gaussian heat energy of exponential rate
`1/2`, independent of `theta`.

It also records the exact Weyl/parity conjugation identity showing that a Weyl
translation cannot remove this carrier while leaving the parity matrix
coefficient unchanged.

The exact algebraic positive-chaos theorem and atomwise Tao source labels are
not refuted. A corrected fractional route needs a defined centered observable,
an exact source realization of that observable, and a center-localized heat
bound after the `s=1` branch has been retained or subtracted.

A cleaner repair is positive-carrier pole centering:

\[
\widetilde B_\theta(s)=\left(\frac{s}{s-1}B_\diamond(s)\right)^\theta,
\qquad
\log\frac{s}{s-1}=\int_0^\infty e^{-st}\frac{e^t-1}{t}\,dt.
\]

The carrier is positive and parity-neutral, removes the pole branch, and does
not cancel any nontrivial-zero branch. The resulting mixed
Tao/continuum heat theorem `PCFHE` remains open.

```text
fractional positive chaos                 retained exact
atomwise Tao source labels                retained exact
uniform L-98703 theta-rate                refuted
Weyl-invariance claim                     refuted
positive continuum pole carrier          proved exact
pole-centered heat estimate PCFHE         open / RH-bearing
T-98700 RH conclusion                     unproved
```
