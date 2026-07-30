# L-15103 — Exact two-sign prolate repair of both Weil-radical constraints

Claim ID: `L-15103`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: finite Fourier eigenfunction algebra; fixed-mode prolate-to-Hermite convergence from Connes--Consani--Moscovici; elementary constraint-preserving smoothing  
Scope: repair the source-side gap in the finite prolate target without changing its limit  
Related counterexample candidates: none

## 1. Abstract finite Fourier data

Fix a support parameter `lambda`. Let `e_0,e_2` be real even finite prolate
modes, normalized in any fixed common convention, and suppose

\[
 \mathcal F_\lambda e_j=\theta_j e_j,
 \qquad j\in\{0,2\},
 \tag{L-15103.1}
\]

where the signed compressed-Fourier eigenvalues satisfy

\[
 \theta_0\ne\theta_2.
\]

Put

\[
 a_j=e_j(0).
 \tag{L-15103.2}
\]

Assume `a_0 a_2 != 0`. Evaluation of (L-15103.1) at zero gives, up to the one
common Fourier-normalization factor `kappa_lambda`,

\[
 \int e_j(x)\,dx
 =\kappa_\lambda\theta_j a_j.
 \tag{L-15103.3}
\]

The common factor will cancel below.

Let `h_lambda` be any real even finite-support source satisfying

\[
 \int h_\lambda(x)\,dx=0,
 \qquad
 \varepsilon_\lambda=h_\lambda(0).
 \tag{L-15103.4}
\]

The current two-mode CCM prolate target has exactly this structure: its integral
constraint is exact, while its value at zero is only asymptotically small.

## 2. Exact two-constraint correction

Define

\[
 \boxed{
 \alpha_\lambda
 =\frac{\varepsilon_\lambda\theta_2}
       {a_0(\theta_0-\theta_2)},
 \qquad
 \beta_\lambda
 =-\frac{\varepsilon_\lambda\theta_0}
       {a_2(\theta_0-\theta_2)}.}
 \tag{L-15103.5}
\]

Put

\[
 \widetilde h_\lambda
 =h_\lambda+\alpha_\lambda e_0+\beta_\lambda e_2.
 \tag{L-15103.6}
\]

Then both Weil-radical source constraints hold **exactly**:

\[
 \boxed{
 \widetilde h_\lambda(0)=0,
 \qquad
 \int\widetilde h_\lambda(x)\,dx=0.}
 \tag{L-15103.7}
\]

### Proof

The value correction is

\[
 \alpha_\lambda a_0+\beta_\lambda a_2
 =\varepsilon_\lambda
   \frac{\theta_2-\theta_0}{\theta_0-\theta_2}
 =-\varepsilon_\lambda.
\]

For the integral, (L-15103.3) gives

\[
 \begin{aligned}
 \int(\alpha_\lambda e_0+\beta_\lambda e_2)
 &=\kappa_\lambda
   (\alpha_\lambda\theta_0a_0
    +\beta_\lambda\theta_2a_2)\\
 &=0.
 \end{aligned}
\]

Together with (L-15103.4), this proves (L-15103.7). QED.

## 3. Stable asymptotic regime

Suppose, as `lambda -> infinity`,

\[
 \theta_0\to+1,
 \qquad
 \theta_2\to-1,
 \tag{L-15103.8}
\]

and `a_0,a_2` converge to nonzero Hermite values. Suppose further that, in a
chosen source norm `X`,

\[
 \|h_\lambda-h\|_X=O(r_\lambda),
 \qquad
 |\varepsilon_\lambda|=O(r_\lambda),
 \tag{L-15103.9}
\]

and `e_0,e_2` remain uniformly bounded in `X`. Then

\[
 \boxed{
 |\alpha_\lambda|+|\beta_\lambda|=O(r_\lambda),
 \qquad
 \|\widetilde h_\lambda-h\|_X=O(r_\lambda).}
 \tag{L-15103.10}
\]

For the fixed prolate modes in the source paper, the reported convergence rate
is `r_lambda=lambda^-2`. The key stability point is

\[
 \theta_0-\theta_2\longrightarrow2,
\]

so the repair does **not** divide by the exponentially small difference between
two same-sign concentration eigenvalues.

This is preferable to correcting with modes `0` and `4`, whose signed Fourier
eigenvalues both approach `+1` and whose difference can be extremely small.

## 4. Constraint-preserving admissible smoothing

Finite prolate functions are naturally considered on a compact interval and
may not, after zero extension, belong literally to the Schwartz source class
used in the global radical theorem. The following elementary density statement
separates that domain issue from the exact algebra.

Let `f` be an even `L2` function on `[-lambda,lambda]`, continuous near zero,
with

\[
 f(0)=0,
 \qquad
 \int_{-\lambda}^{\lambda}f=0.
 \tag{L-15103.11}
\]

Then there are even functions

\[
 f_m\in C_c^\infty(-\lambda,\lambda)
\]

such that

\[
 f_m(0)=0,
 \qquad
 \int f_m=0,
 \qquad
 \|f_m-f\|_2\to0.
 \tag{L-15103.12}
\]

### Construction

Choose even smooth cutoffs `chi_m` that equal one near zero and converge to one
pointwise away from the endpoints. Let

\[
 \delta_m=\int\chi_m f.
\]

Then `delta_m -> 0`. Choose one fixed even bump

\[
 b\in C_c^\infty(-\lambda,\lambda),
 \qquad
 b(0)=0,
 \qquad
 \int b=1,
\]

and put

\[
 f_m=\chi_mf-\delta_mb.
 \tag{L-15103.13}
\]

The two constraints are exact and `L2` convergence follows from dominated
convergence on the finite interval.

Thus every repaired prolate source can be approximated arbitrarily closely by
literal admissible radical sources without sacrificing either linear
constraint. A production theorem must additionally propagate this source error
through the `E`-map and the selected Weil form norm; that continuity gate is not
silently assumed here.

## 5. Relationship to the exact Hermite target

`L-15101` already supplies the exact global Hermite source and therefore avoids
all finite-source domain issues. The repaired prolate target remains useful for
a different reason: it is adapted to the time/frequency concentration operator
and may yield a much better localized leakage-to-gap ratio.

The two targets should therefore be compared by the same audited quantity:

\[
 \frac{\text{localized form-dual leakage}}
      {\text{even-complement coercivity}}.
\]

Neither target should be ranked by raw Rayleigh value alone.

## Gap audit

- Equation (L-15103.3) must be checked in the exact finite Fourier convention;
  a common normalization factor is harmless, but mode-dependent factors are not.
- Nonvanishing of `a_0,a_2` and separation of `theta_0,theta_2` must be certified
  at every finite production level.
- Exact source constraints imply membership in the global radical only after
  the source lies in the theorem's admissible class. The smoothing result gives
  density, not an unqualified endpoint theorem.
- Source convergence does not by itself prove the `E`-images converge in the
  Hardy or Weil form norms. That operator-continuity budget must be explicit.
- This lemma repairs a source-side obstruction; it does not prove the localized
  ground-state gap or RH.
