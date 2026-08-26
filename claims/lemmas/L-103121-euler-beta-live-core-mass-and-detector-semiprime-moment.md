# L-103121 — The Euler–Beta live-core mass is positive and the bounded detector has a negative semiprime moment

Claim ID: `L-103121`  
Status: **PROVED EXACT SIGN THEOREM**  
Created: 2026-08-26  
Depends on: `L-103120`; corrected bounded-detector symbol `L-105490`; the literal live-core convention `omega(c)>=2` used in `R-103120`  
RH status: **not assumed**

The previous QPTI pass proved an exact finite Euler–Beta identity but did not
examine its first global arithmetic mode.  That mode has a fixed sign.

## 1. The live-core Euler mass

For a squarefree core `c`, put

\[
 d(c)=\frac{\mu(c)}{\binom{\omega(c)+2}{2}c^2}.
\]

The root and first-chaos core layers have `omega(c)=0,1`.  The literal live
core used in `R-103120` begins at `omega(c)=2`.  Define

\[
\boxed{
 D_{\ge2}
 =\sum_{\substack{c\ge1\\\mu^2(c)=1\\\omega(c)\ge2}}
 d(c).
}
\tag{L-103121.1}
\]

This series converges absolutely.  Let

\[
 P_2=\sum_p\frac1{p^2},
 \qquad
 \mathcal P_\theta=\prod_p\left(1-\frac{\theta}{p^2}\right).
\]

Expanding the Euler product and using

\[
 \frac1{\binom{k+2}{2}}
 =2\int_0^1(1-\theta)\theta^k\,d\theta
\]

gives

\[
\boxed{
 D_{\ge2}
 =2\int_0^1(1-\theta)
 \left(\mathcal P_\theta-1+\theta P_2\right)d\theta.
}
\tag{L-103121.2}
\]

For every finite prime set and `0<=theta<=1`,

\[
 \prod_p\left(1-\frac\theta{p^2}\right)
 \ge 1-\theta\sum_p\frac1{p^2}.
\]

This follows inductively from
`(1-a)(1-b)=1-a-b+ab>=1-a-b`.  Passage to the infinite product is justified
by absolute convergence.  The inequality is strict for `theta>0`, because at
least two prime factors are present.  Therefore

\[
\boxed{D_{\ge2}>0.}
\tag{L-103121.3}
\]

The committed exact finite-prime certificate gives

\[
 D_{\ge2}=0.010265\ldots,
\]

but only strict positivity is used below.

## 2. The detector moment at the semiprime density

The corrected Mellin symbol of the bounded derivative-outer kernel is

\[
 \widehat K_L(s)
 =\frac{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})}
 {s(s-1/2)}.
\]

At `s=1/2`, the final numerator factor and the denominator vanish to first
order.  Since

\[
 \lim_{s\to1/2}
 \frac{1-\sqrt2\,2^{-s}}{s-1/2}=\log2,
\]

direct substitution in the remaining factors gives

\[
\boxed{
 \widehat K_L(1/2)
 =\int_1^8K_L(y)y^{-3/2}\,dy
 =-(2-\sqrt2)^2\log2<0.
}
\tag{L-103121.4}
\]

Thus the first squarefree-semiprime density mode of the live Euler–Beta source
has coefficient

\[
\boxed{
 C_{\rm EB}
 :=D_{\ge2}\widehat K_L(1/2)<0.
}
\tag{L-103121.5}
\]

Numerically, `C_EB=-0.0024415...`.

## Scope

This lemma is an exact sign calculation.  It does not use RH and does not by
itself invoke an asymptotic counting theorem.  The semiprime transfer and the
resulting refutation of `EBD103120` are `R-103121`.
