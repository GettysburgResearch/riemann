# L-106432 — Exact hard-band visible and signed-tail trace formulas

Claim ID: `L-106432`  
Status: **PROVED EXACT FOURIER/HANKEL IDENTITY**  
Created: 2026-08-25  
Depends on: `L-105290`; `L-106431`  
RH status: **not assumed**

This lemma computes the literal compressed Hankel terms in the signed-index
frontier.  It contains no source-density or denominator-cancellation
promotion.

## 1. Circle form

Let

\[
U(e^{it})=\sum_{n\in\mathbb Z}u_ne^{int}
\]

be scalar and unimodular, with `U in H^(1/2)`.  Let `P_d` be the projection of
`H^2` onto

\[
\operatorname{span}\{1,z,\ldots,z^{d-1}\}.
\]

The Hankel matrix of `H_U` has entry `u_{-(j+k+1)}`.  Counting the pairs
`0<=k<d`, `j>=0` with `j+k+1=m` gives

\[
\boxed{
\|H_UP_d\|_{\mathcal S_2}^2
 =\sum_{m\ge1}\min(d,m)|u_{-m}|^2.
}
\tag{L-106432.1}
\]

The complementary domain projection satisfies

\[
\boxed{
\|H_UP_d^\perp\|_{\mathcal S_2}^2
 =\sum_{m>d}(m-d)|u_{-m}|^2.
}
\tag{L-106432.2}
\]

Replacing `U` by `bar U` gives the same formulas with `u_m` in place of
`u_{-m}`.  Therefore the signed complement of `L-106431` is exactly

\[
\boxed{
\Delta_d(U)
 =\sum_{m>d}(m-d)
   \bigl(|u_{-m}|^2-|u_m|^2\bigr).
}
\tag{L-106432.3}
\]

No model-space coverage estimate occurs in these identities.

## 2. Upper-half-plane form

Use the unitary Fourier transform under which `H^2(C_+)` is
`L^2(0,infinity)`.  For `H>0`, let `P_[0,H]` be multiplication by
`1_[0,H]` in positive-frequency coordinates.  Write `u_hat` for the boundary
Fourier transform of `U`.

For negative output frequency `-x`, `x>0`, the Hankel kernel is

\[
K_-(x,s)=\widehat U(-x-s),
\qquad s>0.
\]

Fubini and the change of variables `xi=x+s` give

\[
\boxed{
V_H^-(U):=\|H_UP_{[0,H]}\|_{\mathcal S_2}^2
 =\int_0^\infty
   \min(H,\xi)|\widehat U(-\xi)|^2\,d\xi.
}
\tag{L-106432.4}
\]

Likewise

\[
\boxed{
C_H^-(U):=\|H_UP_{[0,H]}^\perp\|_{\mathcal S_2}^2
 =\int_H^\infty
   (\xi-H)|\widehat U(-\xi)|^2\,d\xi.
}
\tag{L-106432.5}
\]

For the favorable orientation,

\[
V_H^+(U)
 =\int_0^\infty
   \min(H,\xi)|\widehat U(\xi)|^2\,d\xi,
\]

\[
C_H^+(U)
 =\int_H^\infty
   (\xi-H)|\widehat U(\xi)|^2\,d\xi.
\]

Consequently

\[
\boxed{
\Delta_H(U)=C_H^-(U)-C_H^+(U)
 =\int_H^\infty(\xi-H)
  \bigl(|\widehat U(-\xi)|^2-|\widehat U(\xi)|^2\bigr)d\xi.
}
\tag{L-106432.6}
\]

The full signed index splits as

\[
\boxed{
-\operatorname{wind}U
 =\bigl(V_H^-(U)-V_H^+(U)\bigr)+\Delta_H(U).
}
\tag{L-106432.7}
\]

In particular,

\[
\boxed{
-\operatorname{wind}U
 \le V_H^-(U)+(\Delta_H(U))_+.
}
\tag{L-106432.8}
\]

## 3. Exact tail flow

Whenever differentiation under the integral is justified,

\[
\boxed{
\Delta_H'(U)
 =-\int_H^\infty
  \bigl(|\widehat U(-\xi)|^2-|\widehat U(\xi)|^2\bigr)d\xi,
}
\tag{L-106432.9}
\]

and

\[
\boxed{
\Delta_H''(U)
 =|\widehat U(-H)|^2-|\widehat U(H)|^2.
}
\tag{L-106432.10}
\]

Thus the surviving endpoint problem is a literal signed spectral-tail flow.
A pointwise inequality between analytic numerator and denominator source
densities does not substitute for (L-106432.4) or (L-106432.6).

## 4. Scope

The formulas are exact for finite rational symbols and extend by monotone or
trace-class approximation at `H^(1/2)` scope.  They do not estimate the Xi
endpoint quotient.  Their purpose is to replace the unsupported visible
`1/600` promotion by the exact conclusion-facing quantities.
