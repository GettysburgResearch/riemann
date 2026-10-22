# L-91411 — The Brownian–theta Pick problem has an infinitesimal Stieltjes–Herglotz gate

Claim ID: `L-91411`  
Status: **EXACT KERNEL/FEATURE REDUCTION; POSITIVE SPECTRAL DATA CONSTRUCTION OPEN**  
Created: 2026-08-12; normalization corrected 2026-08-12  
Authoring agent: `gpt56-pro`  
Depends on: PR #401 at `82fe81e52d8c221c8649376d759aa8d0ee64c0c7`, especially `L-91105/L-91106` and `L-91310/L-91319`  
RH status: **unproved**

## 1. Xi transport and its Cayley impedance

Put

\[
M(r)=\frac{\xi(\frac12+r)}{\xi(\frac12)},
\qquad
 g(r)=\log M(r),
\]

and, for `0<a<1/2`,

\[
d_a(r)=\frac{M(r-a)}{M(r+a)},
\qquad
\ell_a(r)=\frac{1-d_a(r)}{1+d_a(r)}.
\tag{L-91411.1}
\]

For positive nodes `r_i`, let

\[
C_{ij}=\frac1{r_i+r_j},
\qquad
D_a=\operatorname{diag}(d_a(r_i)).
\]

PR #401 proves the exact Cayley congruence

\[
C-D_aCD_a\succeq0
\iff
\left[
\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}
\right]_{i,j}\succeq0.
\tag{L-91411.2}
\]

## 2. Exact differential flow

Define

\[
\boxed{
 h_a(r)=g'(r-a)+g'(r+a).
}
\tag{L-91411.3}
\]

Then

\[
\partial_a\log d_a(r)=-h_a(r),
\qquad
\partial_aD_a=-H_aD_a,
\]

where `H_a=diag(h_a(r_i))`. Therefore

\[
\boxed{
\partial_a(C-D_aCD_a)
=D_a(H_aC+CH_a)D_a.
}
\tag{L-91411.4}
\]

Since `D_0=I`,

\[
\boxed{
C-D_aCD_a
=\int_0^a
 D_u(H_uC+CH_u)D_u\,du.
}
\tag{L-91411.5}
\]

Thus the finite horizontal Pick problem is solved if, for every `u`,

\[
\boxed{
\left[
\frac{h_u(r_i)+h_u(r_j)}{r_i+r_j}
\right]_{i,j}\succeq0.
}
\tag{L-91411.6}
\]

The full finite-shift problem has become an infinitesimal positive-real problem.
No matrix-valued integration ambiguity remains because each integrand in
(L-91411.5) is conjugated by a positive diagonal matrix.

## 3. Correct Stieltjes–Herglotz feature representation

The first version of this lemma omitted the possible nonnegative linear term.
That omission made the proposed class too small: even a centered Gaussian law
has `h_a(r)` proportional to `r`. The corrected sufficient representation is as
follows.

Let `h:(0,infinity)->R`. Suppose there are a constant `beta>=0` and a positive
measure `mu` on `[0,infinity)` satisfying the necessary integrability such that

\[
\boxed{
 h(r)=\beta r
 +r\int_0^\infty\frac{d\mu(t)}{r^2+t}.
}
\tag{L-91411.7}
\]

Then

\[
\boxed{
\begin{aligned}
\frac{h(r)+h(s)}{r+s}
={}&\beta\\
&+\int_0^\infty
 \left[
  \frac r{r^2+t}\frac s{s^2+t}
  +\frac{\sqrt t}{r^2+t}
   \frac{\sqrt t}{s^2+t}
 \right]d\mu(t).
\end{aligned}}
\tag{L-91411.8}
\]

Hence the kernel is a literal Gram with one constant feature and one
continuous two-channel feature:

\[
\boxed{
\Phi_r
=\sqrt\beta
\oplus
\left(
 \frac r{r^2+t},
 \frac{\sqrt t}{r^2+t}
\right)_{t\ge0}.
}
\tag{L-91411.9}
\]

The integral part also allows an atom at `t=0`, which produces a `1/r` term.
Thus (L-91411.7) is the natural odd Herglotz/Stieltjes form with both the linear
and reciprocal boundary channels visible.

This proves the following sufficient theorem.

> **Infinitesimal Stieltjes–Herglotz Gate (`ISHG_a`).** For each `0<=u<=a`,
> construct `beta_u>=0` and a positive measure `mu_u` such that
> \[
> h_u(r)=\beta_ur
> +r\int_0^\infty\frac{d\mu_u(t)}{r^2+t}.
> \]

Then every matrix in (L-91411.6) is PSD; (L-91411.5) gives every Xi Pick
matrix; the safe continuation theorem on PR #398 yields the zero-free
half-plane and hence RH along a cofinal sequence `a->0`.

This is a constructive realization target: `beta_u` is the Gaussian/linear
bulk channel, while `mu_u` is the nontrivial theta Dirichlet-to-Neumann spectral
measure.

## 4. Brownian meaning of the infinitesimal state

Under the BPY half-size-biased law, let `Z=log Y`. Then

\[
M(r)=\mathbb E e^{rZ},
\qquad
 g'(r)=\mathbb E_r Z,
\qquad
 g''(r)=\operatorname{Var}_r(Z).
\tag{L-91411.10}
\]

Therefore

\[
\boxed{
 h_a(r)=\mathbb E_{r-a}Z+\mathbb E_{r+a}Z,
}
\tag{L-91411.11}
\]

and

\[
\boxed{
 h_a'(r)=
 \operatorname{Var}_{r-a}(Z)
 +\operatorname{Var}_{r+a}(Z)>0.
}
\tag{L-91411.12}
\]

The source in `ISHG_a` is consequently a symmetrized Fisher response. PR #401's
Stein decomposition says that its constant-Stein part already has a positive
Gaussian rank-two feature and that all non-Gaussian difficulty is the
variability of the canonical Stein kernel. In the corrected coordinate, the
linear coefficient `beta_a` absorbs precisely such a Gaussian bulk; the
remaining task is

\[
\boxed{
\text{represent the residual theta/Gamma--Beta Fisher response by }\mu_a\ge0.
}
\tag{L-91411.13}
\]

## 5. Exact two-point frontier

Put

\[
q_a(r)=\frac{\ell_a(r)}r.
\]

For `0<r<s`, the determinant of the `2 x 2` impedance kernel is

\[
\boxed{
\det
\begin{pmatrix}
 \ell_a(r)/r&(\ell_a(r)+\ell_a(s))/(r+s)\\
 (\ell_a(r)+\ell_a(s))/(r+s)&\ell_a(s)/s
\end{pmatrix}
=
\frac{[q_a(r)-q_a(s)]
      [s\ell_a(s)-r\ell_a(r)]}
     {(r+s)^2}.
}
\tag{L-91411.14}
\]

The Brownian regression formula

\[
\ell_a(r)=\mathbb E_{r,a}[\tanh(aZ)]
\]

implies that `ell_a` is increasing: its derivative is the covariance of the two
increasing functions `Z` and `tanh(aZ)` under the tilted law. Hence

\[
s\ell_a(s)-r\ell_a(r)>0.
\]

Consequently every two-point Pick matrix is PSD if and only if

\[
\boxed{
 r\longmapsto\frac{\ell_a(r)}r
 \text{ is nonincreasing.}
}
\tag{L-91411.15}
\]

This is a useful low-order attack and a stringent numerical/theoretical audit
for any proposed DtN realization. It is not sufficient for all matrix sizes.

## 6. Relation to the Stein-variability defect

PR #401 gives, for an arbitrary test `F`,

\[
\operatorname{Re}\operatorname{Cov}^{(2)}_u(\mathcal A_F,S)
=V_u\bigl(|\mathbb E_uF(Z)|^2+|\mathbb E_uF(-Z)|^2\bigr)
 +\operatorname{Re}\mathcal D_u(F).
\tag{L-91411.16}
\]

The first term is the finite-dimensional Gaussian feature and should feed the
`beta_u` channel. `ISHG_a` asks that the full covariance, including
`D_u`, be represented after adjoining the positive continuum indexed by `t`.
Thus the corrected Herglotz data give a precise target for absorbing the Stein
variability; they are not another generic positivity slogan.

## 7. Proof boundary

```text
finite-shift Pick defect as integral of infinitesimal kernels   EXACT
linear-plus-Stieltjes feature factorization                     EXACT
Brownian Fisher expression for h_a                              EXACT
monotonicity of ell_a                                           EXACT
2-point determinant reduction                                   EXACT
construction of beta_a,mu_a from theta/Gamma--Beta bulk         OPEN / RH-BEARING
all-size Xi Pick positivity                                     OPEN
Riemann Hypothesis                                               UNPROVED
```
