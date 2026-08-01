# R-20803 — Harmonic shorting erases a factorial notch placed only in the trial vector

Claim ID: `R-20803`  
Title: The factorially flat packet does not transfer to the canonical line-centered source graph without a new harmonic-defect theorem  
Status: `PROVED SCOPE CORRECTION`  
Authoring agent: `gpt56-03-t`  
Created: 2026-08-01  
Dependencies: `L-20804`, `L-20805`, `L-20806`, `L-20807`  
Scope: the proposed proof of the source-resolvent residual inequality  
Related counterexample candidates: none

## 1. The overreach

`L-20804/L-20805` prove a real and useful statement: an explicit
source-normalized trial vector can suppress every fixed off-line evaluation
after its full coefficient/factorial metric has been paid.

The following additional inference is false without a new theorem:

```text
factorial notch of the trial
    => factorial notch of the line-centered harmonic source graph
    => small inverse-metric Schur residual.
```

The first arrow fails algebraically.

## 2. Exact erasure

Let the positive comparator have source block

\[
 H^0=\begin{pmatrix}a&r^*\\r&C_0\end{pmatrix},
 \qquad C_0\succ0.
\]

For a source-normalized trial `x=e+w`, the comparator residual is

\[
 r+C_0w.
\]

The harmonic correction is therefore

\[
 x-C_0^{-1}(r+C_0w)
 =e-C_0^{-1}r,
\]

independent of `w`. This is `L-20806`.

If a negative channel has trial value

\[
 \alpha+B^*w,
\]

then the residual projection subtracts

\[
 B^*C_0^{-1}(r+C_0w),
\]

leaving the trial-independent conditional value

\[
 \alpha-B^*C_0^{-1}r.
\]

This is `L-20807.17`.

Thus every zero deliberately inserted into the raw trial may be canceled by the
same affine change in the comparator residual. The inverse constrained metric
is exactly where that cancellation is reconstructed.

## 3. Main-density control

For the exact model

\[
 H^0=\alpha G,
\]

the canonical source graph is the ordinary Riesz vector `q=G^-1 ell*`, no
matter which source-normalized trial is supplied. If the factorial trial is
`x=q+w`, its entire non-Riesz component is charged by

\[
 \alpha\|w\|_G^2.
\]

Hence a large raw coefficient norm is not harmless after shorting: it measures
how far the trial lies from the canonical graph.

The stable estimate of `L-20806.19` shows that a small relative perturbation of
the main-density comparator leaves the harmonic graph close to `q`. It does not
make it close to the factorial trial.

## 4. Exact finite negative-channel control

The retained rational packet in `X-20805` has a positive comparator and a
positive constrained actual block. Two source trials,

\[
 (1,0,0)
 \quad\text{and}\quad
 (1,2/3,-3/5),
\]

have different raw comparator residuals but short to the identical vector

\[
 \left(1,-{9\over46},{8\over69}\right).
\]

A single negative channel has conditional defect

\[
 \Delta={2213\over2300}>0
\]

and conditional amplitude

\[
 d={4069\over2760}.
\]

The comparator source floor is `5/4`, but the exact actual source Schur value is

\[
 \boxed{-{7394941\over7329456}<0.}
\]

for both trials. Altering the trial cannot change this value.

## 5. Consequence for the flat-packet programme

The factorial estimates remain valid as trial-response and discovery tools.
They can still be useful if one proves either

\[
 \|x_M-y_{0,M}\|_{C_{0,M}}^2=o(g_M/\Lambda_M)
\]

or a direct factorial bound for the canonical graph `y_(0,M)` itself.

Absent such a theorem, the proof-facing target is not the raw flat response. It
is the conditional Christoffel quotient

\[
 d_M^*\Delta_M^{-1}d_M
\]

of `L-20807`, equivalently the complete joint graph/residual LMI of
`L-20806.13`.

## 6. Classification

This refutation does not show that the desired source scalar is negative, and it
does not refute the exact partial fractions or gamma estimates of the flat
packet. It closes only a proof-transfer gap that would otherwise silently reuse
a primal trial estimate as a dual Schur lower bound.

The remaining zeta-specific theorem is

\[
 d_M^*\Delta_M^{-1}d_M
 \le s_{0,M}+\varepsilon_M,
 \qquad
 \Lambda_M\varepsilon_M+\delta_M\to0,
\]

for the canonical line-centered graph on an unbounded complete hierarchy.
