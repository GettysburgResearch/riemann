# L-14305 — Weighted Fourier-tail elimination by cofinal diagonal extraction

Claim ID: L-14305  
Title: The prolate projection tail is never a structural blocker in the finite diagonal RH criterion  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: Parseval, density of trigonometric polynomials, T-14301, audited L-14302/L-14303  
Scope: remove the weighted target-tail limit from the global positive-route blocker  
Related counterexample candidates: none

## Statement

Fix `lambda>1` and put

\[
 \ell=\log\lambda.
\]

Let `P_N` be the ordinary `L2([-ell,ell])` orthogonal projection onto

\[
 E_N=\operatorname{span}\{\phi_n:|n|\leq N\},
 \qquad
 \phi_n(t)=(2\ell)^{-1/2}e^{i\pi nt/\ell}.
 \tag{L-14305.1}
\]

For `0<tau<1/2`, define

\[
 \|f\|_{\lambda,\tau}^2
 =\int_{-\ell}^{\ell}
 |f(t)|^2\bigl(e^{2\tau t}+e^{-2\tau t}\bigr)\,dt.
 \tag{L-14305.2}
\]

Then every `f in L2([-ell,ell])` satisfies

\[
 \boxed{
 \|(I-P_N)f\|_{\lambda,\tau}
 \leq
 \sqrt2\,\lambda^\tau\|(I-P_N)f\|_2
 \longrightarrow0.}
 \tag{L-14305.3}
\]

If

\[
 f=\sum_{n\in\mathbb Z}c_n\phi_n,
\]

then the explicit coefficient form is

\[
 \boxed{
 \|(I-P_N)f\|_{\lambda,\tau}^2
 \leq
 2\lambda^{2\tau}
 \sum_{|n|>N}|c_n|^2.}
 \tag{L-14305.4}
\]

Consequently, for every sequence

\[
 \lambda_j>1,
 \qquad 0<\tau_j<\frac12,
 \qquad \varepsilon_j>0,
 \tag{L-14305.5}
\]

and every sequence of targets

\[
 k_j\in L^2([-\log\lambda_j,\log\lambda_j]),
\]

there are integers `M_j`, which may be chosen strictly increasing, such that

\[
 \boxed{
 N\geq M_j
 \quad\Longrightarrow\quad
 \|(I-P_N)k_j\|_{\lambda_j,\tau_j}\leq\varepsilon_j.}
 \tag{L-14305.6}
\]

### Cofinal reciprocal-residual criterion

Assume

\[
 \lambda_j\to\infty,
 \qquad
 \tau_j\nearrow\frac12,
 \qquad
 \varepsilon_j\downarrow0,
 \tag{L-14305.7}
\]

and let `k_j=k_{lambda_j}` be the CCM prolate target. For every `j,N`, put

\[
 p_{j,N}=P_Nk_j.
 \tag{L-14305.8}
\]

Suppose that, for each `j`, there are arbitrarily large `N` for which the exact
finite CCM matrix `QW_{lambda_j}^N` passes the audited L-14302 global
simple-even gates and the L-14303 reciprocal-Hardy correction obeys

\[
 \frac{\mathcal R_{j,N}}{h_{j,N}}\leq\varepsilon_j.
 \tag{L-14305.9}
\]

Then one can choose a strictly increasing diagonal sequence `N_j` such that

\[
 \inf_{c\ne0}
 \|c\xi_{j,N_j}-k_j\|_{\lambda_j,\tau_j}
 \leq2\varepsilon_j,
 \tag{L-14305.10}
\]

where `xi_{j,N_j}` is the exact finite global ground state. Therefore T-14301
implies the Riemann hypothesis.

Equivalently, the positive route no longer requires a separate asymptotic proof
that the weighted projection tail tends to zero. It is enough to prove the
**cofinal** finite-dimensional condition

\[
 \boxed{
 \lim_{j\to\infty}
 \inf_{\substack{N\geq M_j\\N\ {m passes}}}
 \frac{\mathcal R_{j,N}}{h_{j,N}}=0,}
 \tag{L-14305.11}
\]

where `M_j` is any certified tail threshold satisfying (L-14305.6).

## Applicability to the CCM target

For fixed `lambda`, the function

\[
 k_\lambda(u)=E(h_\lambda)(u),
 \qquad \lambda^{-1}\leq u\leq\lambda,
\]

belongs to `L2(d*u)`. Indeed, extending `h_lambda` by zero outside
`[-lambda,lambda]`, the defining sum is finite and, with

\[
 H_\lambda=\|h_\lambda\|_\infty,
\]

one has for `u in [lambda^-1,lambda]`

\[
 |k_\lambda(u)|
 \leq u^{1/2}\left\lfloor\frac\lambda u\right\rfloor H_\lambda
 \leq\lambda H_\lambda u^{-1/2}.
 \tag{L-14305.12}
\]

The right side is square-integrable against `d*u` on this compact interval.
Thus the density conclusion applies without importing any unproved asymptotic
regularity of the prolate functions.

## Proof

For `|t|<=ell`,

\[
 e^{2\tau t}+e^{-2\tau t}
 \leq2e^{2\tau\ell}
 =2\lambda^{2\tau}.
\]

Therefore

\[
 \|g\|_{\lambda,\tau}^2
 \leq2\lambda^{2\tau}\|g\|_2^2
 \tag{L-14305.13}
\]

for every `g`. Taking `g=(I-P_N)f` proves the first inequality in
(L-14305.3). Ordinary Fourier completeness gives

\[
 \|(I-P_N)f\|_2\to0.
\]

Parseval gives

\[
 \|(I-P_N)f\|_2^2
 =\sum_{|n|>N}|c_n|^2,
\]

which proves (L-14305.4).

For each `j`, convergence gives a finite threshold `M_j^0` after which the
weighted tail is at most `epsilon_j`. Replace recursively

\[
 M_j^0\quad\hbox{by}\quad
 M_j=\max(M_j^0,M_{j-1}+1)
\]

to obtain increasing thresholds, proving (L-14305.6).

By the cofinal hypothesis, choose a passing

\[
 N_j\geq\max(M_j,N_{j-1}+1)
\]

with `mathcal R_{j,N_j}/h_{j,N_j}<=epsilon_j`. Audited L-14302 and L-14303 give

\[
 \inf_{c\ne0}
 \|c\xi_{j,N_j}-k_j\|_{\lambda_j,\tau_j}
 \leq
 \underbrace{\|(I-P_{N_j})k_j\|_{\lambda_j,\tau_j}}
             _{\leq\varepsilon_j}
 +\underbrace{\mathcal R_{j,N_j}/h_{j,N_j}}
             _{\leq\varepsilon_j},
\]

which proves (L-14305.10). Since `2 epsilon_j->0`, T-14301 applies. QED.

## Why this changes the critical path

Earlier versions of the positive-route report listed two asymptotic tasks:

```text
weighted projection tail -> 0,
reciprocal residual / coercivity -> 0.
```

The first task is automatic under cofinal truncation. It needs finite
certification at each chosen level, but no new global theorem about zeta,
prolate functions, or the Weil operator. The sole structural question is now:

> Does the reciprocal-Hardy residual/coercivity ratio become small at
> arbitrarily large finite truncations along a support sequence tending to
> infinity?

This formulation is weaker than requiring an all-large-`N` estimate and is
exactly matched to a proof-producing search.

## Constructive tail certificates

Equation (L-14305.4) is exact but contains an infinite coefficient tail. Any of
the following finite interfaces is sufficient:

1. a directed Sobolev/variation bound implying a Fourier-tail majorant;
2. interval quadrature of the finite coefficient prefix plus a proved analytic
   remainder;
3. a direct weighted approximation certificate by a rational trigonometric
   polynomial;
4. a stronger explicit bound derived from the piecewise formula for
   `E(h_lambda)`.

Discovery code may simply increase `N` until a nonrigorous estimate is small;
promotion still requires one of these directed certificates.

## Gap audit

- The convergence is for each fixed `lambda,tau`; no uniform rate in `lambda`
  is asserted.
- Arbitrarily large passing truncations are essential. One isolated good small
  `N` cannot automatically be enlarged because the ground state and coercivity
  change with `N`.
- `P_N` is the ordinary Fourier projection, not the weighted projection. The
  bounded-weight comparison is why ordinary density still suffices.
- The result removes the tail as a structural theorem, not as a finite
  proof-engineering obligation.
- Bound (L-14305.12) is deliberately crude and is used only to establish
  membership in `L2`.
- The cofinal residual condition remains unproved; this lemma does not resolve
  RH by itself.

## Adversarial checks

1. Let `lambda_j` grow extremely fast. The required `M_j` may also grow
   extremely fast, but existence is unchanged.
2. A sequence with a good residual ratio only at one fixed `N` per support does
   not satisfy the cofinal hypothesis.
3. Since `W_tau>=2`, weighted convergence implies ordinary convergence, but the
   proof requires the opposite direction and uses the finite-support upper
   bound.
4. Choosing `tau_j` close to `1/2` enlarges the finite comparison factor; it
   does not invalidate density.
5. If the target were not in `L2`, Fourier density would be unavailable; the
   explicit finite-sum bound verifies this hypothesis for `k_lambda`.

## Remaining uncertainty

The lemma is elementary and complete-looking but remains `PROPOSED` pending an
independent review. The cofinal passing condition (L-14305.9) is now the central
unproved analytic/spectral statement.
