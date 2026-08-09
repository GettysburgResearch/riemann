# Positive occupancy-source normal form for the prime endpoint

Date: 2026-08-09  
Branch: `research/gpt56-pro/353-positive-occupancy-source`  
Base: PR #352 head `0de05ce56350efbd63bce475dc95a55c9435a55d`  
Status: exact new structural theorems; RH unproved

## 1. Why this continuation

PR #352 reduces the live project to the eventual sign of

\[
 A(X)=\sum_{p\le X}(\log p)r_X(p).
\]

It also isolates a globally negative prime-power moat and shows that the derivative gate is a stronger critical weighted-Chebyshev problem. The present continuation asks a different question:

> Is the undifferenced endpoint itself the output of a positive causal state whose geometry is simpler than the prime sum?

The answer is yes.

## 2. Individual columns

For every carry column `q`, define the unit-occupancy set

\[
 \mathcal U_q=\bigcup_{k\ge1}[kq,kq+1]
\]

and its cumulative occupancy deficit

\[
 \Delta_q(x)=x/q-|\mathcal U_q\cap[q,x]|.
\]

It is an explicit positive sawtooth with

\[
 q^{-1}\le\Delta_q\le1.
\]

For the normalized residual

\[
 f_q(t)=\sqrt q\,r_{qe^t}(q),
\]

put

\[
 Q_q(t)=e^{-t/2}\Delta_q(qe^t)>0.
\]

Then exactly

\[
 -f_q(t)
 =\int_0^t\left(1-{t-u\over2}\right)Q_q(u)\,du.
\]

Equivalently,

\[
 f_q(t)
 ={A_q(t)\over2}[t-2-\bar u_q(t)].
\]

This proves two seemingly opposite facts:

```text
every positive-real Mellin moment of r_X(q) is strictly negative;

every fixed column r_X(q) is eventually positive as X/q -> infinity.
```

Thus no componentwise pointwise-negative proof of the endpoint is available. The moving prime boundary is essential.

## 3. Aggregate prime source

For any nonnegative arithmetic weight `lambda`, the column sources combine without a square-root loss:

\[
 \mathcal Q_\lambda(t)
 =e^{-t/2}\sum_{q\le e^t}
  \lambda(q)\Delta_q(e^t)\ge0.
\]

The aggregate residual is

\[
 -F_\lambda(e^t)
 =\int_0^t\left(1-{t-u\over2}\right)
  \mathcal Q_\lambda(u)\,du.
\]

For the prime weight this is the exact endpoint `A`. If

\[
 M_0(t)=\int_0^t\mathcal Q_{\mathbb P}(u)du,
 \qquad
 M_1(t)=\int_0^t(t-u)\mathcal Q_{\mathbb P}(u)du,
\]

then

\[
 A(e^t)=\frac12[M_1(t)-2M_0(t)].
\]

Consequently

\[
\boxed{
 \mathrm{RH}
 \iff
 {M_1(t)\over M_0(t)}<2
 \quad\text{eventually}.
}
\]

This is merely an exact reformulation of PR #352's endpoint criterion, but it replaces an oscillatory prime sum by one positive source and one fixed one-sign-change Green kernel.

## 4. Fractional endpoint unification

The complete fractional family of `T-90010` uses the same source. For `1<sigma<=2`,

\[
 -\mathscr A_\sigma(t)
 =\int_0^t
 {a^{\sigma-2}\over\Gamma(\sigma-1)}
 \left(1-{a\over2(\sigma-1)}\right)
 \mathcal Q_{\mathbb P}(t-a)\,da.
\]

Thus the critical age threshold is exactly

\[
 2(\sigma-1).
\]

The order-two endpoint has threshold two; the order-one monotonicity boundary is the limit in which the positive age window collapses.

## 5. Finite arithmetic state

At integer `N`,

\[
 \mathcal Q_{\mathbb P}(\log N)
 ={1\over\sqrt N}\left[
 N\sum_{p\le N}{\log p\over p}
 -\sum_{m\le N}\log\operatorname{rad}(m)
 +\log\operatorname{rad}(N)
 \right].
\]

On the complete open cell `N<X<N+1`, it has the exact two-exponential form

\[
 \mathcal Q_{\mathbb P}(\log X)
 =\sqrt X[P_1(N)-\ell(N)]
  +X^{-1/2}S_1(N).
\]

The source jumps upward only when a new prime activates:

\[
 \Delta\mathcal Q_{\mathbb P}(\log N)
 =\mathbf1_{N\text{ prime}}\log N/\sqrt N.
\]

The endpoint derivative has the opposite jump, and between integers

\[
 {d^2\over dt^2}A(e^t)=e^{-t/2}S_1(N).
\]

This gives an exact three-state system

\[
 M_1'=M_0,
 \qquad M_0'=\mathcal Q_{\mathbb P},
 \qquad
 \mathcal Q_{\mathbb P}'
 =\frac12\mathcal Q_{\mathbb P}-e^{-t/2}S_1(N),
\]

with explicit prime jumps.

## 6. New proof-facing target

The smallest positive-state closing theorem is now:

> **Prime Occupancy Age Bound.** For all sufficiently large `t`, the backward mean age of `mathcal Q_P` is strictly less than two.

A stronger sufficient theorem is the instantaneous concentration inequality

\[
 M_0(t)\le2\mathcal Q_{\mathbb P}(t),
\]

which is exactly endpoint monotonicity and therefore should not be mistaken for a routine positive-source estimate.

The undifferenced target allows `M_0-2Q` to change sign; only its integral must stay favorable. This is why the mean-age coordinate is strictly weaker and more faithful than the derivative gate.

Potential mechanisms to test next:

1. a source-specific variation-diminishing theorem for the radical/prime jump system;
2. a comparison of `mathcal Q_P` with the complete prime-power source, using the explicit moat before taking an absolute value;
3. a Lyapunov functional involving `(M_0,M_1,Q)` which tolerates local derivative failures;
4. a dyadic or fixed-ratio recurrence for the positive source rather than for `A` itself.

## 7. Exact boundary

```text
column occupancy source                     PROPOSED COMPLETE EXACT
column positive-real Mellin sign             PROPOSED COMPLETE EXACT
fixed-column eventual positivity             PROPOSED COMPLETE EXACT
aggregate positive-source convolution        PROPOSED COMPLETE EXACT
prime endpoint mean-age equivalence           PROPOSED COMPLETE EXACT
fractional one-sign-change kernels            PROPOSED COMPLETE EXACT
integer/two-exponential source state           PROPOSED COMPLETE EXACT
prime jump / radical curvature law            PROPOSED COMPLETE EXACT
finite formal-coefficient replay              PASS
prime occupancy age bound                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVEN
```
