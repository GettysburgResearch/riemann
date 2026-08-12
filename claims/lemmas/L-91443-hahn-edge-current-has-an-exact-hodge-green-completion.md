# L-91443 — Every finite Hahn edge current has an exact Hodge–Green completion with unit-gap control

Claim ID: `L-91443`  
Status: **EXACT FINITE REVERSIBLE-CHAIN THEOREM; XI/THETA SOURCE IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91403/L-91404`, PR #409 `L-91422/L-91431`  
RH status: **unproved**

## 1. The Beta-binomial Hahn chain

For `0<=k<=N`, put

\[
 \pi_N(k)=\frac{6(k+1)(N-k+1)}{(N+1)(N+2)(N+3)},
\]

\[
 \lambda_k=(k+2)(N-k),
 \qquad
 \mu_k=k(N-k+2).
\]

The generator is

\[
 (\mathcal L_Nf)(k)
 =\frac14\left[
 \lambda_k(f(k+1)-f(k))
 +\mu_k(f(k-1)-f(k))
 \right].
\tag{L-91443.1}
\]

Detailed balance gives the edge conductances

\[
\boxed{
 c_k=\frac14\pi_N(k)\lambda_k
    =\frac14\pi_N(k+1)\mu_{k+1}>0,
 \qquad0\le k<N.
}
\tag{L-91443.2}
\]

The Dirichlet form is

\[
 \mathcal E_N(f,g)
 =\sum_{k=0}^{N-1}
  c_k[f(k+1)-f(k)]
  \overline{[g(k+1)-g(k)]}.
\tag{L-91443.3}
\]

## 2. Edge current and divergence

Let `J=(J_0,...,J_(N-1))` be an arbitrary complex edge current and set

\[
 J_{-1}=J_N=0.
\]

Define its vertex divergence by

\[
\boxed{
 (\operatorname{div}_\pi J)(k)
 =\frac{J_{k-1}-J_k}{\pi_N(k)}.
}
\tag{L-91443.4}
\]

Then

\[
 \sum_{k=0}^{N}\pi_N(k)\operatorname{div}_\pi J(k)=0,
\]

and discrete summation by parts gives

\[
\boxed{
 \left\langle\operatorname{div}_\pi J,f\right\rangle_{\pi_N}
 =\sum_{k=0}^{N-1}
  J_k\overline{[f(k+1)-f(k)]}.
}
\tag{L-91443.5}
\]

## 3. Exact Hodge potential

Define `P_J` up to an additive constant by

\[
\boxed{
 P_J(k+1)-P_J(k)=\frac{J_k}{c_k}.
}
\tag{L-91443.6}
\]

Then

\[
\boxed{
 -\mathcal L_NP_J
 =\operatorname{div}_\pi J,
}
\tag{L-91443.7}
\]

and, for every `f`,

\[
\boxed{
 \sum_{k=0}^{N-1}J_k\overline{\Delta f_k}
 =\mathcal E_N(P_J,f).
}
\tag{L-91443.8}
\]

The exact resistance energy is

\[
\boxed{
 \mathcal R_N(J)
 :=\mathcal E_N(P_J,P_J)
 =\sum_{k=0}^{N-1}\frac{|J_k|^2}{c_k}.
}
\tag{L-91443.9}
\]

Because the state graph is a path, there is no cycle current and no hidden Hodge component: every edge current has this unique gradient representation.

## 4. Sharp Green completion

Young's square identity gives

\[
\boxed{
 \operatorname{Re}
 \sum_{k=0}^{N-1}J_k\overline{\Delta f_k}
 \ge
 -\frac12\mathcal R_N(J)
 -\frac12\mathcal E_N(f,f).
}
\tag{L-91443.10}
\]

Indeed the difference is

\[
 \frac12\sum_{k=0}^{N-1}
 c_k\left|
 \Delta f_k+\frac{J_k}{c_k}
 \right|^2.
\]

The coefficients `1/2` are sharp.

This is the exact finite analogue of the Beta-current completion in PR #409, but it requires no abstract Poisson solver and loses no endpoint term.

## 5. Unit spectral-gap alternative

`L-91404` proves that the nonzero spectrum of `-L_N` is

\[
 \frac{j(j+3)}4,
 \qquad j=1,...,N,
\]

so the spectral gap is exactly one. Put

\[
 g=\operatorname{div}_\pi J.
\]

Since `g` has mean zero,

\[
\boxed{
 \mathcal R_N(J)
 =\langle g,(-\mathcal L_N)^{-1}g\rangle_{\pi_N}
 \le\|g\|_{L^2(\pi_N)}^2.
}
\tag{L-91443.11}
\]

Consequently

\[
\boxed{
 \operatorname{Re}
 \sum_kJ_k\overline{\Delta f_k}
 \ge
 -\frac12\|\operatorname{div}_\pi J\|_{L^2(\pi_N)}^2
 -\frac12\mathcal E_N(f,f).
}
\tag{L-91443.12}
\]

This replaces a pointwise inverse-conductance estimate by one vertex-space norm whenever the divergence is easier to identify.

## 6. Brownian/theta interpretation

At a finite shadow level, the non-Gaussian Brownian current of PR #409 has the form

\[
 \sum_kJ_{u,N}(k)\Delta\mathcal A_{F,N}(k).
\]

Equation (L-91443.10) says that the native Hahn/Jacobi bulk pays exactly one half of the test energy. The sole remaining charge is

\[
 \frac12\mathcal R_N(J_{u,N})
\]

plus the sharp endpoint reserve of `L-91431`.

Therefore the finite source-specific closing target is

\[
\boxed{
 \mathfrak R_{\theta,N}(F)
 \ge
 \frac12\mathcal R_N(J_{u,N})
 +\frac14\mathbb E[c_{\tau,u}\mathcal D_F].
}
\tag{L-91443.13}

Alternatively, by (L-91443.11), it suffices to dominate half the squared divergence norm.

The conductances, resistance and endpoint coefficient are all explicit. A finite SDP or exact sum-of-squares search can therefore test the boundary identity without discretizing a possibly unstable Brownian zero producer.

## 7. Continuum limit

Under `V_N=(2K-N)/N`, the Hahn forms converge to the Beta(2,2) Jacobi form. If the finite currents converge in resistance norm and their divergences are uniformly square integrable, (L-91443.8)--(L-91443.12) pass to the Jacobi limit by lower semicontinuity.

This is the correct stable limiting topology for the Brownian current. Pointwise convergence of current coefficients alone is insufficient.

## 8. Boundary

```text
finite Hahn conductance network                 EXACT
edge-current divergence identity                EXACT
unique Hodge potential on the path              EXACT
sharp resistance completion                     EXACT
unit-gap divergence bound                       EXACT
finite theta-reserve inequality                 OPEN / EXPLICIT
resistance-norm continuum passage               OPEN ANALYTIC
Brownian reflection / Pick positivity           OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
