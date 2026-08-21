# L-95051 — The positive scale-four majorant has sharp square-root times logarithm cost

Claim ID: `L-95051`  
Status: **PROPOSED COMPLETE EXACT/ASYMPTOTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-95050`; the signed reciprocal coefficients `a_4` from PR #474  
Scope: coefficientwise stability and weighted total variation; no claim about a cancellation-sensitive physical norm

## 1. Triangular nonlinear reconstruction

Let

\[
A_4(s)=\frac1{G_4(s)}
=\sum_{n\ge1}{a_4(n)\over n^s},
\qquad a_4(1)=1.
\]

Since

\[
{A_4'\over A_4}=-{G_4'\over G_4}
=\sum_n{\Lambda_4(n)\over n^s},
\]

coefficient comparison gives, for `n>=2`,

\[
\boxed{
a_4(n)\log n
=-\sum_{\substack{d\mid n\\d>1}}
 \Lambda_4(d)a_4(n/d).}
\tag{L-95051.1}
\]

Thus the log derivative determines the reciprocal coefficients only after the boundary value `a_4(1)=1` is supplied.

## 2. Positive majorant

Induction using `L-95050.6` gives

\[
\boxed{|a_4(n)|\le g_4(n)\qquad(n\ge1).}
\tag{L-95051.2}
\]

Indeed, assuming the inequality below `n`,

\[
|a_4(n)|\log n
\le\sum_{d\mid n,d>1}\Lambda_4(d)g_4(n/d)
=g_4(n)\log n.
\]

The positive divisor compiler is therefore a fail-closed total-variation majorant for the signed scale-four reciprocal state.

## 3. Exact growth scale of the majorant

Put

\[
V_4(X)=\sum_{n\le X}{g_4(n)\over\sqrt n}.
\]

Write `n=2^em` with `m` odd. For `e=2k`,

\[
{g_4(2^{2k}m)\over\sqrt{2^{2k}m}}
={2^k\over\sqrt m},
\]

while the allowed odd `m` satisfy `m<=X/4^k`. Each even dyadic level therefore contributes a fixed positive multiple of `sqrt X`. Odd levels do the same with a factor `1/sqrt2`.

There are `Theta(log X)` nonempty dyadic levels. Elementary integral comparison yields constants `0<c<C` such that

\[
\boxed{
c\sqrt X\log(2X)
\le V_4(X)
\le C\sqrt X\log(2X).}
\tag{L-95051.3}
\]

Hence the straightforward positive reconstruction has macroscopic weighted cost

\[
\boxed{V_4(X)=\Theta(\sqrt X\log X).}
\tag{L-95051.4}
\]

It cannot by itself supply a polylogarithmic Cycle-Debt or Q4 endpoint bound.

## 4. Interpretation

The scale-four logarithmic derivative does possess a positive, coefficient-one multiplicative realization. What fails is not source positivity but **capacity scale**: absolute reconstruction pays one square-root unit at every dyadic depth.

A closing theorem must retain signed/Hermitian cancellation between depths. Replacing the reciprocal state by the positive majorant destroys exactly the information needed for RH.

## 5. Proof boundary

Established:

1. exact boundary-dependent coefficient recursion;
2. coefficientwise positive majorization;
3. sharp `Theta(sqrt X log X)` weighted cost.

Open:

1. a cancellation-faithful quadratic or passive transfer;
2. the Q4 mean estimate;
3. RH.
