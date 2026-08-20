# Native normalization, collar reconstruction, and Hardy-tail factorization

**Scientific status:** exact hostile correction and reduction. **RH remains
unproved.**

## 1. Why the latest collar simplification must be corrected

For the source-aligned logarithmic box, let `W` be the unnormalized kernel and
`phi=W/sqrt(.)`. Then

\[
\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\sum_n\frac{\beta(n)}n\phi(X/n).
\]

Thus the native local Euler factor on `phi` is `I-p^{-1}U_p`. The factor
`I-p^{-1/2}U_p` is correct on `W`, not on `phi`. Moving it unchanged across the
normalization changes every rough child coefficient.

In the deep region `phi=A-By^{-1/2}`. The nonnative factor kills the
half-order term; the native factor leaves

\[
A(1-p^{-1})-B(1-p^{-1/2})y^{-1/2}.
\]

This is the first broken arrow in PR #664's conclusion-facing composition.

## 2. Correct collar source

For a finite labelled prime set, the native normalized coefficient of a subset
with product `n` is `mu(n)/n`. A collar occurrence contributes

\[
\frac{\mu(n)}n
\left[8+(-8-3\log(y/n))(y/n)^{-1/2}\right].
\]

The coefficient of `log(y)y^{-1/2}` is therefore `-3 mu(n)/sqrt(n)`. After
combining the duplicate `67` labels, the complete coefficient is

\[
-3\sum_{y/67<n\le y}\frac{\beta(n)}{\sqrt n}.
\]

Its Mellin multiplier is

\[
\frac{(1-67^{-s})(1-67^{-(s+1/2)})}
{s\zeta(s+1/2)},
\]

so subpower logarithmic negative mass is equivalent to RH.

## 3. Exact opening of the Poisson square

For any finite packet,

\[
Q_\tau
=\int\left|\sum_nc_nn^{\tau-i\gamma}\right|^2P_\tau(\gamma)d\gamma
=\sum_{m,n}c_m\overline{c_n}\min(m,n)^{2\tau}.
\]

The kernel is Brownian covariance. Therefore

\[
Q_\tau
=\left|\sum_nc_n\right|^2
+2\tau\int_1^\infty
\left|\sum_{n\ge v}c_n\right|^2v^{2\tau-1}dv.
\]

This is the exact off-diagonal object hidden by the phase notation in GPMOC.
The remaining theorem must control these nested arithmetic tails before source
collapse. The coefficientwise owner gap does not do so by itself.

## 4. Final verdict

```text
old paired stopping-line proposal              superseded by native-source audit
PR #664 normalized half-order operator         nonnative
canonical normalized operator                  exact: p^(-1)
native pair positivity                         exact
native all-prime collar window                  half-order beta window
Poisson owner packet                            exact Hardy tail square
required tail/window negative-mass estimate     RH-equivalent / open
Riemann Hypothesis                              unproved
```
