# R-90211 — The unsmoothed broad-policy renewal/zeta transfer is not completely monotone

Claim ID: `R-90211`  
Status: **PROPOSED COMPLETE EXACT REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `L-90209/L-90210`; Bernstein's theorem for completely monotone functions  
Scope: refutes one tempting positive-mixture shortcut; does not refute OBH or the smoothed hinge occupation

## 1. The tempting transfer factor

Normalize the continuum hinge occupation by one power of the size variable.
The positive divisor identity behind Möbius inversion gives a manifestly
positive reference solution, and the broad Markov Green solution differs from
it by the scalar factor

\[
 \boxed{
 H(s)=\frac1{\zeta(1+s)[1-\phi(s)]},
 \qquad s>0,
 }
\tag{R-90211.1}
\]

where

\[
 \phi(s)=\mathbb E[V^s]
 =\frac4{s+2}
 \left[\left(\frac34\right)^{s+2}
       -\left(\frac14\right)^{s+2}\right].
\tag{R-90211.2}
\]

Numerically, many low derivatives of `H` have the alternating signs of a
completely monotone function.  If `H` were completely monotone, Bernstein's
theorem would represent it as a positive scale mixture and would give an
extremely short positivity route.

That shortcut is false.

## 2. Renewal-measure representation

Let

\[
 Y=-\log V.
\]

The law of `Y` is absolutely continuous on the compact interval

\[
 [\log(4/3),\log4].
\]

Since `0<phi(s)<1` for real `s>0`,

\[
 \frac1{1-\phi(s)}
 =\sum_{r\ge0}\phi(s)^r
\tag{R-90211.3}
\]

is the Laplace transform of the renewal measure

\[
 \boxed{
 \mathcal R
 =\delta_0+\sum_{r\ge1}\mathcal L(Y_1+\cdots+Y_r).
 }
\tag{R-90211.4}
\]

The `r=0` term is the atom `delta_0`; every `r>=1` term is absolutely
continuous because `Y` has a density.

On the arithmetic side, for `s>0`, absolute convergence gives

\[
 \boxed{
 \frac1{\zeta(1+s)}
 =\sum_{n\ge1}\frac{\mu(n)}n e^{-s\log n}.
 }
\tag{R-90211.5}
\]

Thus the inverse Laplace measure of `H` is the signed convolution

\[
 \boxed{
 \nu_H
 =\left(\sum_{n\ge1}\frac{\mu(n)}n\delta_{\log n}\right)
  *\mathcal R.
 }
\tag{R-90211.6}
\]

## 3. An unavoidable negative atom

Convolution with the atomic `delta_0` part of `mathcal R` preserves every
Möbius atom:

\[
 \sum_{n\ge1}\frac{\mu(n)}n\delta_{\log n}.
\tag{R-90211.7}
\]

Every other component of (R-90211.6) convolves a discrete measure with an
absolutely continuous density and is therefore absolutely continuous.  It
cannot cancel any point mass.

At `n=2`, the atomic coefficient is

\[
 \boxed{
 \frac{\mu(2)}2=-\frac12.
 }
\tag{R-90211.8}
\]

Hence

\[
 \boxed{
 \nu_H(\{\log2\})=-\frac12<0.
 }
\tag{R-90211.9}
\]

The inverse Laplace measure of `H` is intrinsically signed.

## 4. Complete monotonicity is impossible

Bernstein's theorem states that a function on `(0,infinity)` is completely
monotone iff it is the Laplace transform of a positive measure.
The Laplace transform is injective on the locally finite measures appearing
here.  Because the unique inverse measure (R-90211.6) has the negative atom
(R-90211.9),

\[
 \boxed{
 H(s)\text{ is not completely monotone on }(0,\infty).
 }
\tag{R-90211.10}
\]

Therefore some derivative/order and some positive `s` must eventually violate

\[
 (-1)^kH^{(k)}(s)\ge0,
\]

even though low-order numerical tests can look exceptionally convincing.

This is a fail-closed explanation for why low derivative scans are unsafe here.

## 5. Why the hinge route is not refuted

The actual normalized hinge occupation has one additional Riesz factor:

\[
 \boxed{
 \widehat p(s)
 =\frac{H(s)}{2(s+1/2)}.
 }
\tag{R-90211.11}
\]

Multiplication by `(s+1/2)^(-1)` convolves `nu_H` with the positive exponential
density

\[
 e^{-y/2}\mathbf1_{y\ge0}dy.
\]

In particular it **smears every Möbius atom into a continuous tail**.  The
negative atom obstruction of Section 3 disappears at exactly this first Riesz
smoothing level.

Thus

```text
unsmoothed transfer H                         NOT completely monotone;
actual one-Riesz-smoothed hinge transfer       still open;
logarithmic critical target (two Riesz levels) even smoother.
```

This aligns with the finite reconnaissance: generic unsmoothed/step targets can
fail immediately (`O-90209`), while square-root hinges remain positive in every
retained test.

## 6. Exact divisor identity behind the comparison

For completeness, let

\[
 a(x)=\frac1{2\sqrt x}
 \sum_{k\le x}\frac{\mu(k)}{\sqrt k}.
\]

Möbius inversion gives, away from the harmless integer knots,

\[
 \boxed{
 \sum_{d\le x}\frac1d a(x/d)=\frac1{2\sqrt x}.
 }
\tag{R-90211.12}
\]

Indeed the left side has Mellin multiplier `zeta(1+s)` and cancels the
`1/zeta(1+s)` in the transform of `a`.

The broad Markov Green differs from this positive divisor solution exactly by
`H(s)`.  Sections 2--4 prove that this comparison cannot be upgraded to a
positive **unsmoothed** mixing measure.

## 7. Proof boundary

Proved exactly:

- the renewal-measure inverse of `1/(1-phi)`;
- the Möbius atomic inverse of `1/zeta(1+s)`;
- the negative `-1/2` atom at `log2` in the combined transfer;
- failure of complete monotonicity of the unsmoothed transfer.

Still open:

- complete monotonicity / direct positivity of the once-smoothed hinge symbol;
- OBH;
- the critical logarithmic occupation;
- RH.