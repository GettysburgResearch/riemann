# L-105624 — Even log-concave sources have a monotone current–Turán contraction profile

Claim ID: `L-105624`  
Status: **PROVED ABSTRACT LOG-CONCAVE-SOURCE THEOREM; XI LOG-CONCAVITY IS A SEPARATE INPUT**  
Created: 2026-08-25  
Depends on: `L-105620--L-105623`  
RH status: **not assumed**

## 1. Statement

Let

\[
\Phi:\mathbb R\to(0,\infty)
\]

be even and log-concave, with sufficient smoothness and decay. Use the
exterior-square/current notation

\[
\Lambda_2(\xi)
={1\over2}\int(2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du,
\]

\[
j_h(\xi)
=\widehat J_h(\xi),
\qquad h>0.
\]

For `xi>=0`, define

\[
\boxed{
r_h(\xi)
={h e^{-h\xi}\Lambda_2(\xi)\over j_h(\xi)}.
}
\tag{L-105624.1}
\]

`L-105620` gives `0<r_h<=1`. The new conclusion is

\[
\boxed{
r_h(\xi)\text{ is nonincreasing on }[0,\infty).
}
\tag{L-105624.2}
\]

The same statement holds by approximation for nonsmooth log-concave sources
for which the displayed quantities are finite.

## 2. Exterior-square conditional law

Write

\[
\Phi=e^{-\psi},
\]

where `psi` is even and convex. Put `s=xi` and, for `x>0`, define

\[
q_s(x)
={1\over Z_s}
 x^2
 \Phi\!\left({s\over2}+x\right)
 \Phi\!\left({s\over2}-x\right).
\tag{L-105624.3}
\]

This is the normalized difference law of the positive exterior-square source
conditioned on the sum frequency `s`.

Its potential is

\[
V(s,x)
=-2\log x
+\psi\!\left({s\over2}+x\right)
+\psi\!\left({s\over2}-x\right).
\tag{L-105624.4}
\]

One has

\[
V_{xx}
={2\over x^2}
+\psi''(s/2+x)+\psi''(s/2-x)>0,
\tag{L-105624.5}
\]

and

\[
V_{sx}
={1\over2}
\left[
\psi''(s/2+x)-\psi''(s/2-x)
\right].
\tag{L-105624.6}
\]

Convexity gives the pointwise curvature bound

\[
\boxed{
|V_{sx}|\le {1\over2}V_{xx}.
}
\tag{L-105624.7}
\]

## 3. Quantile transport moves each endpoint forward

Let

\[
F_s(x)=\int_0^xq_s(t)\,dt
\]

and define the infinitesimal monotone-transport velocity

\[
v_s(x)=-{\partial_sF_s(x)\over q_s(x)}.
\tag{L-105624.8}
\]

The continuity equation is

\[
\partial_sq_s+\partial_x(q_sv_s)=0.
\]

Differentiating its first-order form gives

\[
\boxed{
v_s''-V_xv_s'-V_{xx}v_s=V_{sx}.
}
\tag{L-105624.9}
\]

At an interior positive maximum of `v_s`, equations
(L-105624.7)--(L-105624.9) exclude `v_s>1/2`. At an interior negative minimum
they exclude `v_s<-1/2`. The natural endpoint limits are obtained by
truncation and then sending the truncation to `0` and `infinity`. Therefore

\[
\boxed{|v_s(x)|\le {1\over2}.}
\tag{L-105624.10}
\]

Under the monotone coupling of the conditional laws, put

\[
U_s={s\over2}+X_s,
\qquad
V_s={s\over2}-X_s.
\]

Equation (L-105624.10) gives

\[
{dU_s\over ds}={1\over2}+v_s(X_s)\ge0,
\qquad
{dV_s\over ds}={1\over2}-v_s(X_s)\ge0.
\tag{L-105624.11}
\]

Both ordered endpoints move to the right as the sum frequency increases.

## 4. Divided-difference monotonicity

Define the positive exponential divided difference

\[
\boxed{
H_h(u,v)
={e^{2hu}-e^{2hv}\over2h(u-v)}
={1\over u-v}\int_v^ue^{2ht}\,dt,
\qquad u>v.
}
\tag{L-105624.12}
\]

It is nondecreasing in each endpoint. Hence (L-105624.11) gives

\[
s\longmapsto
\mathbb E_{q_s}H_h(U_s,V_s)
\quad\text{nondecreasing}.
\tag{L-105624.13}
\]

The current/exterior-square formulas identify this expectation exactly:

\[
\boxed{
\mathbb E_{q_s}H_h(U_s,V_s)
=e^{hs}{j_h(s)\over h\Lambda_2(s)}.
}
\tag{L-105624.14}
\]

Taking reciprocals proves (L-105624.2).

## 5. Consequence for the phase-collision profile

For a log-concave source, the canonical diagonal contraction `r_h` is a
monotone causal weight. Thus any physical all-pass phase which acts as a causal
isometry in the one-sided source coordinate can only move energy toward
smaller values of `r_h`; `L-105625` gives the exact operator statement.

This converts the arbitrary-profile commutator of `PCC105623` into one scalar
source property plus the inner/causal physical identification.

## 6. Xi boundary

The theorem does not assert in this file that the standard Xi Fourier kernel
is log-concave. That is a separate source theorem and must be independently
source-locked and reviewed before consumption. Nor does log-concavity alone
imply RH: it is only a second-order source property.

Even after the Xi log-concavity input, one must verify that the exact
cofinal two-trace physical map is the causal inner action covered by
`L-105625`, including boundary zeros and finite-window seams.
