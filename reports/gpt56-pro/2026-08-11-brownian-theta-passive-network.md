# Radical continuation: Brownian–theta passive network

Date: 2026-08-11  
Agent: `gpt56-pro`  
Status: exact reductions and a new construction programme; **RH remains unproved**

## Executive result

PR #398 proved that separate positivity of the zeta Jordan channel, the completed one-Green channel, the horizontal cocycle, and moving-boundary unitarity does not imply the target Pick kernel. The missing ingredient is exact coupling.

This continuation replaces the final matrix inequality by a constructive Hilbert-space target:

```text
Xi horizontal shift ratio
 -> Cayley impedance ell_a
 -> Brownian two-copy reflection form
 -> Gamma(4)-Beta(2,2) shadow reservoir
 -> supersymmetric theta bulk Q_theta*Q_theta
 -> exact Dirichlet-to-Neumann identification
 -> positive-real Pick kernel
 -> RH.
```

The first four arrows are exact. The Dirichlet-to-Neumann identification is open.

## 1. Exact Cayley reduction

For

\[
 d_a(r)=\frac{\xi(1/2+r-a)}{\xi(1/2+r+a)},
 \qquad
 \ell_a(r)=\frac{1-d_a(r)}{1+d_a(r)},
\]

and a finite Cauchy packet

\[
 C_{ij}=\frac1{r_i+r_j},
\]

one has exactly

\[
 C-DCD
 =2(I+L)^{-1}(LC+CL)(I+L)^{-1}.
\]

Hence the final safe Pick problem is the positive-real kernel

\[
 \left(\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}\right)_{ij}.
\]

This is the same noncommutative anticommutator that blocked the old CKE/Green route on PR #202.

## 2. Brownian two-copy reflection form

Under the BPY half-size-biased law, `Z=log Y` is symmetric and

\[
 M(r)=E e^{rZ}=\xi(1/2+r)/\xi(1/2).
\]

The impedance is

\[
 \ell_a(r)
 =\frac{E[e^{rZ}\sinh(aZ)]}{E[e^{rZ}\cosh(aZ)]}
 =E_{r,a}[\tanh(aZ)].
\]

After cross multiplication, every finite Pick quadratic becomes

\[
 E\left[
  \sinh(aS)
  \int_{-S/2}^{S/2}
   \overline{F(x+\Delta/2)}F(x-\Delta/2)dx
 \right],
\]

where `S=Z_1+Z_2`, `Delta=Z_1-Z_2`, and `F` is an exponential polynomial. Thus the exact theorem is a reflection-positivity statement for the specific Brownian log-range law.

## 3. Gamma shadow reservoir

Pairing the two BPY gamma sums mode by mode gives

\[
 X_n^++X_n^-=G_n\sim\Gamma(4),
 \qquad
 X_n^+/(X_n^++X_n^-)=U_n\sim\operatorname{Beta}(2,2),
\]

with independence. Writing `V_n=2U_n-1`,

\[
 \Sigma_2^+=A+D,
 \qquad
 \Sigma_2^-=A-D,
\]

where `D` is a weighted martingale sum of independent bounded beta coordinates. The two-copy half-size bias is exactly `(A^2-D^2)^(1/4)`.

The beta variables carry the positive Jacobi energy

\[
 \frac14\sum_nE[(1-V_n^2)|\partial_{V_n}f|^2].
\]

After the exact half-size tilt this remains a positive reversible Dirichlet form. PR #399's adjacent martingale butterflies are its finite shadow-transport basis.

## 4. Theta supersymmetry

For the full theta Gibbs ensemble,

\[
 \mu=4a^2-4a'-1/4
\]

and therefore

\[
 -4\partial_v^2+\mu+1/4
 =4(-\partial_v+a)(\partial_v+a)\succeq0.
\]

The pairwise theta-mode variance is an explicit square and cannot be discarded. The Xi impedance is the ratio of the odd and even theta ports

\[
 \ell_a(r)=
 \frac{\int\Phi(t)\sinh(rt)\sinh(at)dt}
      {\int\Phi(t)\cosh(rt)\cosh(at)dt}.
\]

## 5. New exact production theorem

Construct a boundary triple for the positive supersymmetric theta bulk, or equivalently a Gamma-shadow boundary square, whose Weyl function is exactly `ell_a`.

This is an identity target rather than a positivity estimate. Once it is established, Green's identity factors every finite positive-real matrix; the Cayley congruence gives every target Pick matrix; PR #398 performs the analytic continuation; and RH follows.

## 6. Why this route is different

It does not:

- ask finite Brownian approximants to be globally real-rooted;
- infer observed contraction from `|tanh(aZ)|<1`;
- continue one-Green positivity abstractly;
- take absolute values of a prime sum;
- require a fixed nonlinear moment degree at high carrier.

It keeps the infinite Gamma tail as a state reservoir and preserves all theta cross-mode variance channels before taking a scalar boundary ratio.

## 7. Failure tests

The proposed identification must fail on PR #398's planted factor `F_y xi`, even though that control retains the actual zeta Jordan factor and positive completed one-Green measure. It must also retain the half-size tilt and cannot use zero-freeness to define the boundary map.

## Verification

```text
PASS_BROWNIAN_THETA_PASSIVE_NETWORK
checks: 197
```

The replay is exact `Fraction` arithmetic. It proves no Riemann-data sign.
