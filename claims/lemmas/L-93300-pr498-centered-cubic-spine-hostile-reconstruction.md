# L-93300 — Hostile reconstruction of the centered cubic Q4 spine

Claim ID: `L-93300`  
Status: **INDEPENDENT EXACT RECONSTRUCTION / VERIFIED WITH FROZEN IMPORTS**  
Created: 2026-08-16  
Frozen target: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
RH status: **unproved**

## 1. Purpose

This lemma reconstructs the complete analytic spine of PR #498 before any new
arithmetic estimate is proposed.  It fixes the normalization, predecessor,
interpolation, Mellin multiplier and pole-survival interfaces.

No estimate equivalent to RH is imported.

## 2. Endpoint and centering normalization

Let

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf1_{4\mid m}\Lambda(m/4)
 +3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r},
\]

\[
 C_\circ(x)=\sum_{m\le x}c_\circ(m),
\]

and, for \(0\le j<N\),

\[
 R_N(j)
 =C_\circ(N)-C_\circ(j)-C_\circ(N-j-1).
\]

The predecessor is \(N-j-1\), not \(N-j\).

Put

\[
 M_N=\frac1N\sum_{j=0}^{N-1}R_N(j)
\]

and

\[
 \mathscr V_\circ(N)
 =\frac1{N^2}\sum_{j=0}^{N-1}|R_N(j)-M_N|^2.
\]

For

\[
 w(\theta)=\theta(1-\theta)-\frac16,
\]

one has

\[
 \int_0^1w=0,
 \qquad
 \int_0^1w^2=\frac1{180}.
\]

Therefore, with

\[
 \mathcal A_\circ(N)
 =\int_0^1w(\theta)Q_{\circ,N}(\theta)\,d\theta,
\]

Cauchy--Schwarz gives exactly

\[
 \boxed{
 |\mathcal A_\circ(N)|^2
 \le \frac N{180}\mathscr V_\circ(N).
 }
\]

The factor \(N\) is forced by the convention
\(\mathscr V_\circ=N^{-1}\int|Q-M|^2\).

## 3. Cubic Riesz identity

Define

\[
 K(x)=2\int_0^xw(u)\,du
 =\frac{x(1-x)(2x-1)}3.
\]

Then \(K(0)=K(1)=0\), \(K(1-x)=-K(x)\), and \(K'=2w\).

Finite summation over the moving prefixes gives

\[
 \boxed{
 \mathcal A_\circ(N)
 =\sum_{m\le N}c_\circ(m)K(m/N).
 }
\]

The endpoint term \(m=N\) vanishes.  The equality fails if the reflected
predecessor is changed from \(N-j-1\) to \(N-j\).

## 4. Mellin multiplier

For \(\Re s>-1\),

\[
 \widehat K(s)
 =\int_0^1K(x)x^{s-1}\,dx
 =\frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

For real \(X\ge1\), define the same Riesz sum with \(m\le X\).  Absolute
convergence in \(\Re s>1\) gives

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty\mathcal A_\circ(X)X^{-s-1}\,dX
 ={}&
 \frac{s-1}{3(s+1)(s+2)(s+3)}
 \\
 &\times
 \left[
 (1-4^{1-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
 +3(\log4)\frac{4^{-s}}{1-4^{-s}}
 \right].
 \end{aligned}
 }
\]

At a nontrivial zero \(\rho\), none of

\[
 \rho-1,\qquad
 1-4^{1-\rho},\qquad
 1-4^{-\rho},\qquad
 (\rho+1)(\rho+2)(\rho+3)
\]

vanishes.  The four-adic term is holomorphic there.  Hence every open-strip
zero survives as a nonremovable pole.

## 5. Integer-to-real interpolation

On \(N\le X<N+1\),

\[
 |K(m/X)-K(m/N)|
 \le \frac{m}{3N^2}.
\]

The elementary Chebyshev bound gives

\[
 \sum_{m\le N}m|c_\circ(m)|\ll N^2.
\]

The new endpoint at \(X=N+1\) carries \(K(1)=0\).  Thus

\[
 \boxed{
 |\mathcal A_\circ(X)-\mathcal A_\circ(N)|\ll1.
 }
\]

An integer estimate with exponent \(\sigma\) therefore extends to the real
Mellin variable with the same exponent.

## 6. Equivalence disposition

The previous sections prove:

\[
 \mathscr V_\circ(N)\ll(\log N)^A
 \Longrightarrow
 \mathcal A_\circ(X)=O_\varepsilon(X^{1/2+\varepsilon})
 \Longrightarrow
 \mathrm{RH}.
\]

Conversely, the classical von Koch estimate under RH gives

\[
 C_\circ(x)\ll\sqrt x\log^2(2x)
\]

and hence

\[
 \mathscr V_\circ(N)\ll\log^4(2N).
\]

Thus `T-93251` is a valid RH-equivalent criterion.

The centered prime-row Fourier decomposition and the frozen diagonal/minor-arc
bounds give, conditionally on those exact finite identities,

\[
 \left|
 \mathscr V_\circ(N)
 -\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)
 \right|
 \ll\log(2N).
\]

Accordingly `T-93253` is a valid equivalent localization, not an independent
upper bound.

Finally,

\[
 \mathcal A_\circ(N)=\sum_pZ_{p,N}
\]

makes `T-93255` an exact criterion.  Its proposed CPBD estimate is the missing
RH-bearing arithmetic theorem, not an established consequence of the diagonal.

## 7. Review verdicts

```text
centered endpoint predecessor                     VERIFIED
mean-zero Bernoulli normalization                 VERIFIED
cubic Riesz identity                              VERIFIED
integer-real interpolation                        VERIFIED
Mellin multiplier                                 VERIFIED
open-strip pole survival                          VERIFIED
centered-energy equivalence                       VERIFIED
mean-free major-arc equivalence                    VERIFIED ON FROZEN FOURIER INPUTS
CPBD estimate                                      OPEN / RH-EQUIVALENT
Riemann Hypothesis                                unproved
```
