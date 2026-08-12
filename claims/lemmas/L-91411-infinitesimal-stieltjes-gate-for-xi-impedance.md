# L-91411 — The Brownian–theta Pick problem has an infinitesimal Stieltjes gate

Claim ID: `L-91411`  
Status: **EXACT KERNEL/FEATURE REDUCTION; STIELTJES MEASURE CONSTRUCTION OPEN**  
Created: 2026-08-12  
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

## 3. A Stieltjes representation gives an explicit two-channel feature map

Let `h:(0,infinity)->R`. Suppose a positive measure `mu` on `[0,infinity)`
satisfies the necessary integrability and

\[
\boxed{
 h(r)=r\int_0^\infty\frac{d\mu(t)}{r^2+t}.
}
\tag{L-91411.7
}

Then

\[
\begin{aligned}
\frac{h(r)+h(s)}{r+s}
&=\int_0^\infty
 \frac{rs+t}{(r^2+t)(s^2+t)}\,d\mu(t)\\
&=\int_0^\infty
 \left[
  \frac r{r^2+t}\frac s{s^2+t}
  +\frac{\sqrt t}{r^2+t}
   \frac{\sqrt t}{s^2+t}
 \right]d\mu(t).
\end{aligned}
\tag{L-91411.8}
\]

Hence the kernel is a literal Gram with feature vector

\[
\boxed{
\Phi_r(t)=
\left(
 \frac r{r^2+t},
 \frac{\sqrt t}{r^2+t}
\right).
}
\tag{L-91411.9}
\]

This proves the following sufficient theorem.

> **Infinitesimal Stieltjes Gate (`ISG_a`).** For each `0<=u<=a`, construct a
> positive measure `mu_u` such that
> \[
> h_u(r)=r\int_0^\infty\frac{d\mu_u(t)}{r^2+t}.
> \]

Then every matrix in (L-91411.6) is PSD; (L-91411.5) gives every Xi Pick
matrix; the safe continuation theorem on PR #398 yields the zero-free
half-plane and hence RH along a cofinal sequence `a->0`.

This is a constructive realization target: `mu_u` is precisely the spectral
measure that a theta Dirichlet-to-Neumann model would have to produce.

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

The source in `ISG_a` is consequently a symmetrized Fisher response. PR #401's
Stein decomposition says that its constant-Stein part already has a positive
rank-two feature and that all non-Gaussian difficulty is the variability of the
canonical Stein kernel. In the present coordinate, that remaining task is:

\[
\boxed{
\text{convert the theta/Gamma--Beta Fisher response }h_a(r)
\text{ into the Stieltjes spectral measure }\mu_a.
}
\tag{L-91411.13}
\]

## 5. Exact two-point frontier

The first nontrivial Pick test has a particularly simple scalar form. Put

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

The first term is the Gaussian two-channel feature. `ISG_a` asserts that the
complete covariance, including `D_u`, is still representable by the two-channel
continuum (L-91411.9) after enlarging the spectral parameter `t`. Thus the
Stieltjes measure is a precise target for absorbing the Stein variability; it
is not another generic positivity slogan.

## 7. Proof boundary

```text
finite-shift Pick defect as integral of infinitesimal kernels   EXACT
Stieltjes feature factorization                                 EXACT
Brownian Fisher expression for h_a                              EXACT
monotonicity of ell_a                                           EXACT
2-point determinant reduction                                   EXACT
construction of mu_a from theta/Gamma--Beta bulk                OPEN / RH-BEARING
all-size Xi Pick positivity                                     OPEN
Riemann Hypothesis                                               UNPROVED
```
