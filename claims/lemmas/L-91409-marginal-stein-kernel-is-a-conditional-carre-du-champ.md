# L-91409 — The completed Brownian marginal Stein kernel is a conditional carré du champ of one tilted Jacobi Poisson solution

Claim ID: `L-91409`  
Status: **EXACT REVERSIBLE-DIFFUSION / CONDITIONAL-STEIN THEOREM**  
Created: 2026-08-12  
Depends on: PR #401 `L-91107/L-91319`; `R-91402`  
RH status: **unproved**

## 1. Abstract reversible theorem

Let `(Omega,mu,L,Gamma)` be a reversible diffusion with

\[
 -\langle f,Lg\rangle_\mu
 =\langle\Gamma(f,g)\rangle_\mu.
\]

Let `Z` be a real square-integrable observable, `m=E_mu Z`, and let `h` be the mean-zero Poisson solution

\[
 -Lh=Z-m.
\tag{L-91409.1}
\]

For every smooth scalar test `phi`, reversibility and the diffusion chain rule give

\[
\begin{aligned}
 \mathbb E[(Z-m)\phi(Z)]
 &=\mathbb E[(-Lh)\phi(Z)]\\
 &=\mathbb E[\Gamma(h,\phi(Z))]\\
 &=\mathbb E[\phi'(Z)\Gamma(h,Z)].
\end{aligned}
\tag{L-91409.2}
\]

Consequently

\[
 \boxed{
 \tau_Z(z)
 =\mathbb E[\Gamma(h,Z)\mid Z=z]
 }
\tag{L-91409.3}
\]

is a Stein kernel of the marginal law of `Z`.

Taking `phi(z)=z` gives

\[
 \boxed{
 \mathbb E\tau_Z(Z)=\operatorname{Var}(Z).
 }
\tag{L-91409.4}
\]

Conditional Jensen gives the exact variability bound

\[
 \boxed{
 \operatorname{Var}(\tau_Z(Z))
 \le
 \mathbb E\left[
  (\Gamma(h,Z)-\operatorname{Var}Z)^2
 \right].
 }
\tag{L-91409.5}
\]

Positivity of `tau_Z` is not automatic from positivity of the coordinate carré du champ; it requires a sign or structural theorem for `Gamma(h,Z)` after conditioning.

## 2. Tilted Gamma–Beta reservoir

Condition on finitely many Gamma variables in the BPY two-copy representation. Put

\[
 A=\sum_n c_nG_n,
 \qquad
 D=\sum_n c_nG_nV_n,
\]

with `V_n` having the transformed Beta(2,2) reference density

\[
 \rho(v)=\frac34(1-v^2)\mathbf1_{(-1,1)}(v).
\]

The completed two-copy tilt is

\[
 H_G(V)=(A^2-D^2)^{1/4}.
\]

Let `mu_G` be the probability measure proportional to

\[
 H_G(V)\prod_n\rho(V_n)dV_n.
\]

Its canonical reversible generator has divergence form

\[
 \mathcal L_Gf
 =\frac1{H_G\prod\rho}
  \sum_n\frac14\partial_{V_n}
  \left[
   H_G\prod\rho\,(1-V_n^2)\partial_{V_n}f
  \right],
\tag{L-91409.6}
\]

and carré du champ

\[
 \boxed{
 \Gamma_G(f,g)
 =\frac14\sum_n
  (1-V_n^2)\partial_{V_n}f\,\partial_{V_n}g.
 }
\tag{L-91409.7}
\]

The tilt changes the drift but not the positive quadratic form.

## 3. Exact sum–difference gradients

With an irrelevant additive constant `C`, define

\[
 Z_+=\frac12\log(A+D)+C,
 \qquad
 Z_- =\frac12\log(A-D)+C,
\]

\[
 S=Z_++Z_-
 =\frac12\log(A^2-D^2)+2C,
\]

\[
 \Delta=Z_+-Z_-
 =\operatorname{artanh}(D/A).
\]

Then

\[
 \boxed{
 \partial_{V_n}S
 =-\frac{c_nG_nD}{A^2-D^2},
 \qquad
 \partial_{V_n}\Delta
 =\frac{c_nG_nA}{A^2-D^2}.
 }
\tag{L-91409.8
}

For the Poisson solutions

\[
 -\mathcal L_Gh_S=S-\mathbb E_GS,
 \qquad
 -\mathcal L_Gh_\Delta=\Delta-\mathbb E_G\Delta,
\]

the marginal Stein kernels are therefore

\[
 \boxed{
 \tau_S(S)
 =\mathbb E_G\left[
  -\frac{D}{4(A^2-D^2)}
  \sum_n c_nG_n(1-V_n^2)
  \partial_{V_n}h_S
  \ \middle|\ S
 \right],
 }
\tag{L-91409.9}
\]

and

\[
 \boxed{
 \tau_\Delta(\Delta)
 =\mathbb E_G\left[
  \frac{A}{4(A^2-D^2)}
  \sum_n c_nG_n(1-V_n^2)
  \partial_{V_n}h_\Delta
  \ \middle|\ \Delta
 \right].
 }
\tag{L-91409.10}
\]

These formulas retain every beta coordinate and the exact completed tilt.

## 4. Correct constructive target

The coordinate Hahn/Jacobi theorems `L-91405`–`L-91408` provide finite positive approximations, exact spectral gaps, and explicit low-mode currents for the reference coordinate generator. They do not solve (L-91409.1) for the nonlinear completed observables.

The Brownian/theta route can now be formulated constructively:

1. solve the finite tilted Hahn-product Poisson equation for `S` or the exact reflection observable;
2. identify the conditional carré-du-champ port in the finite chain;
3. prove a cutoff-uniform positive Schur/Green identity with the theta variance square;
4. pass to the Gamma–Beta limit using the uniform spectral and tail estimates.

This is the exact finite-to-continuum DtN problem. No coordinate-level low-rank shortcut is assumed.
