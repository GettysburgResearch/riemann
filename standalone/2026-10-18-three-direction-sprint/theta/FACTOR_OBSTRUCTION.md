# A degree14 obstruction to independent Gaussian quadratic factors

**Status: PROPOSED, finite computer-assisted obstruction.** This concerns
one simple real-zero approximation architecture. It neither disproves
other Lee--Yang constructions nor makes an RH claim.

Consider characteristic-function factors

\[
 f_{a,s}(z)=e^{-sz^2/2}(1-az^2),\qquad a\ge0,\ s>0.
 \tag{1}
\]

Each has real zeros. Its inverse Fourier density is

\[
 g_s(x)+a g_s''(x)
 =\left(1-\frac as+\frac{a x^2}{s^2}\right)g_s(x),
 \qquad g_s(x)=\frac{e^{-x^2/(2s)}}{\sqrt{2\pi s}}.
\]

Thus (1) is a positive probability law exactly when `a<=s`. This also
follows as a necessary condition from its unique integrable inverse
Fourier transform being nonnegative near0. The `s=0` case only permits
`a=0`, since any other polynomial violates the unit bound on real
characteristic functions.

For a finite independent convolution of such positive factors, optionally
with an extra centered Gaussian, let `S_r=sum_j a_j^r`. Its variance is

\[
 v=s_0+\sum_j(s_j+2a_j)\ge3S_1. \tag{2}
\]

Expanding the logarithm of the moment generating function at zero gives,
for every `r>=2`,

\[
 S_r=\frac{(-1)^{r+1}\kappa_{2r}}{2(2r-1)!}. \tag{3}
\]

In particular, variance1 requires `S_1<=1/3`.

## An explicit power-sum witness

For every `a>=0` and every real polynomial `p`,

\[
 a\ge2a p(a)-a p(a)^2,
\]

because the difference is `a(1-p(a))^2`. Take

\[
 p(a)=116a-2913a^2+17762a^3.
\]

Summing the pointwise inequality over all factors gives

\[
 S_1\ge 2\sum_{i=1}^3 w_i S_{i+1}
          -\sum_{i,j=1}^3w_iw_jS_{i+j+1},
 \quad (w_1,w_2,w_3)=(116,-2913,17762). \tag{4}
\]

The right side uses only cumulants through14. A fresh complete directed
computation for the **actual standardized theta law** encloses it near

\[
 0.3527360817230699>0.35>\frac13. \tag{5}
\]

Equations (2)--(5) prove that no finite convolution of the positive factors
(1), even with an additional Gaussian factor, matches the standardized
theta moments through14. Matching moments implies matching cumulants,
since cumulants of each fixed order are polynomial functions of the
moments through that order.

The witness does not use numerical zeta zeros or a zero-location
assumption. It was suggested by an unsuccessful scout based on Gaussian
smoothing of individual quadratic real-zero factors. Once the fixed
integer witness is selected, all acceptance calculations use fresh source
intervals and exact rational operations.

This obstruction is deliberately scoped. A globally positive density
corresponding to `e^(-sz^2/2) product_j(1-a_jz^2)` need not allocate enough
Gaussian variance to make **each factor individually** positive. Such a
correlated allocation is outside the hypothesis. Connected ferromagnetic
models likewise escape this independent-factor obstruction.

## Replay

```text
python standalone/2026-10-18-three-direction-sprint/theta/certify_factor_obstruction.py --emit standalone/2026-10-18-three-direction-sprint/theta/factor_obstruction14.json
python standalone/2026-10-18-three-direction-sprint/theta/certify_factor_obstruction.py --check standalone/2026-10-18-three-direction-sprint/theta/factor_obstruction14.json
```

The standard-library verifier pins the inherited320-bit outward integer
primitive, reconstructs all theta moments through14 with the complete
Taylor/time/index tails, forms (3), and evaluates (4). It accepts the
strict rational bound above`.35`; saved JSON is accepted only by equality
with a fresh reconstruction. Source provenance and analytic tail formulas
are documented in INHERITED.json and PROOF22.md.
