# L-94022 — The `P_61` finite forcing has explicit nonduplicating terminal-prime weights

Claim ID: `L-94022`
Status: **PROVED EXACT CAUSAL-PARENT ALLOCATION; NATIVE CANCELLATION EXCLUDED**
Created: 2026-08-16
Depends on: `L-91650`, `L-93602`, `L-93783`
Replay: `X-94020-live-endpoint-source`
RH status: **unproved**

Fix one finite-forcing packet at endpoint `x>67` and list the primes

\[
 p_1<\cdots<p_k,
 \qquad
 p_i>x/67.
\tag{L-94022.1}
\]

Every associated child parameter

\[
 y_i=x/p_i
\]

lies in the complete Target–Lorenz range `1<=y_i<67`.

Put

\[
 r_i=p_i^{-1/2},
 \quad
 s=\prod_i(1-r_i),
 \quad
 \lambda_i=r_i\prod_{h<i}(1-r_h),
 \quad
 \alpha_i=r_i\lambda_i.
\tag{L-94022.2}
\]

Since `sum lambda_i=1-s`, moving the survival copy to the left gives the exact
normalized identity

\[
 \boxed{
 P_x
 =\sum_i\beta_i
  (P_x-r_iA_{p_i}P_{y_i})
 +\sum_i\gamma_iA_{p_i}P_{y_i},
 }
\tag{L-94022.3}
\]

where

\[
 \beta_i=\frac{\lambda_i}{1-s},
 \qquad
 \gamma_i=\frac{\alpha_i}{1-s}=r_i\beta_i.
\tag{L-94022.4}
\]

Hence

\[
 \sum_i\beta_i=1,
 \qquad
 \sum_i\gamma_i<67^{-1/2}<1/8.
\tag{L-94022.5}
\]

The `beta_i` are the real, nonduplicating parent path weights missing from a
collection of independently instantiated leaves.  At `(p,y)=(67,13)` the
corresponding terminal causal block contains exactly 229 active `P_61`
divisors, nine of which have an active child term.  Its atom is

\[
 \frac{
  \mu(d)
 }{\sqrt d}
 \left[
 Q_{py/d}-p^{-1/2}Q_{y/d}
 \right].
\tag{L-94022.6}
\]

The complete directed AVLT makes each **finite-forcing causal block** positive
under the same Target–Lorenz coefficient vector.

Scope is load-bearing: (L-94022.3) allocates the `P_61` finite forcing.  It does
not cancel the actual oriented rough-child marginal of the native paired source.
That marginal is strictly negative at `q=2` by `R-94020`; inserting it as a
separate positive child would invalidate the native normalization.
