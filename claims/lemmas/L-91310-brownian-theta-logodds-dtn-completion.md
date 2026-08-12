# L-91310 — Brownian–theta Dirichlet-to-Neumann completion through an exact log-odds Sturm–Liouville cell

Claim ID: `L-91310`  
Status: **NEW EXACT LOCAL CELL + FULL SOURCE-SPECIFIC DtN PROGRAMME; GLOBAL BOUNDARY IDENTITY OPEN**  
Created: 2026-08-12  
RH status: **unproved**

## 1. The Xi impedance in the BPY coordinate

Let `Z` be the symmetric Brownian/BPY logarithmic variable normalized by

\[
M(r)=\mathbb E e^{rZ}
=\frac{\xi(\frac12+r)}{\xi(\frac12)}.
\tag{L-91310.1}
\]

For `a>0`,

\[
d_a(r)=\frac{M(r-a)}{M(r+a)},
\qquad
\ell_a(r)=\frac{1-d_a(r)}{1+d_a(r)}.
\tag{L-91310.2}
\]

Writing the numerator and denominator symmetrically,

\[
\boxed{
\ell_a(r)
=
\frac{
\mathbb E[e^{rZ}\sinh(aZ)]
}{
\mathbb E[e^{rZ}\cosh(aZ)]
}.
}
\tag{L-91310.3}
\]

This exact probability representation does not by itself prove positive-real
behavior; the `r`-dependent tilt is load-bearing.

## 2. New exact local log-odds cell

Put

\[
v=\tanh z\in(-1,1),
\qquad z=\operatorname{artanh}v,
\]

and

\[
u_{a,\pm}(v)
=
e^{\pm az}
=
\left(\frac{1+v}{1-v}\right)^{\pm a/2}.
\tag{L-91310.4}
\]

A direct differentiation gives

\[
\boxed{
-\frac d{dv}
\left((1-v^2)\frac d{dv}u_{a,\pm}\right)
+
\frac{a^2}{1-v^2}u_{a,\pm}
=0.
}
\tag{L-91310.5}
\]

The differential expression

\[
\mathcal S_a
=
-\frac d{dv}(1-v^2)\frac d{dv}
+
\frac{a^2}{1-v^2}
\tag{L-91310.6}
\]

is positive on compactly supported smooth functions:

\[
\langle f,\mathcal S_af\rangle
=
\int_{-1}^{1}
\left[
(1-v^2)|f'(v)|^2
+
\frac{a^2}{1-v^2}|f(v)|^2
\right]dv
\ge0.
\tag{L-91310.7}
\]

Let

\[
c_a(v)=\cosh(a\operatorname{artanh}v),
\qquad
s_a(v)=\sinh(a\operatorname{artanh}v).
\tag{L-91310.8}
\]

Then

\[
(1-v^2)c_a'(v)=a\,s_a(v),
\qquad
(1-v^2)s_a'(v)=a\,c_a(v),
\tag{L-91310.9}
\]

and

\[
\boxed{
\frac{s_a(v)}{c_a(v)}
=
\tanh(a\operatorname{artanh}v).
}
\tag{L-91310.10}
\]

Thus the bounded regression `tanh(aZ)` is not merely a pointwise contraction:
it is the odd/even boundary transfer of an explicit positive Sturm–Liouville
cell.

## 3. Gamma(4)–Beta(2,2) reservoir

Pair the two BPY Gamma(2) coordinates mode by mode:

\[
G_n=X_n^++X_n^-\sim\Gamma(4),
\qquad
V_n=\frac{X_n^+-X_n^-}{X_n^++X_n^-}\in(-1,1),
\tag{L-91310.11}
\]

where `V_n` has the Beta(2,2) image density and is independent of `G_n`.
With the deterministic BPY weights `c_n>0`,

\[
A=\sum_n c_nG_n,
\qquad
D=\sum_n c_nG_nV_n,
\qquad
Z=\operatorname{artanh}(D/A).
\tag{L-91310.12}
\]

The reservoir carries the positive Jacobi energy

\[
\mathcal E_\beta(F)
=
\frac14\sum_n
\mathbb E\left[
(1-V_n^2)|\partial_{V_n}F|^2
\right].
\tag{L-91310.13}
\]

The exact local cell (L-91310.5) is therefore compatible with the native
Beta-coordinate geometry rather than being imposed from outside.

## 4. Positive theta bulk

Let `B(v)>0` be the theta ground state and

\[
Q_\theta=\partial_v+a_\theta(v),
\qquad
H_\theta=4Q_\theta^*Q_\theta
=-4\partial_v^2+\mu(v)+\frac14
\succeq0.
\tag{L-91310.14}
\]

The complete theta variance is an explicit sum of pairwise squares. Let
`A` be the positive phase-locked five-shift operator and put

\[
f_*=\mathscr AB.
\tag{L-91310.15}
\]

The phase-filtered source satisfies the exact transmutation

\[
\boxed{
\Phi_*^{\rm ph}
=
\mu f_*-H_\theta f_*
=
\left(4\partial_v^2-\frac14\right)f_*.
}
\tag{L-91310.16}
\]

Its half-line even and odd transforms obey

\[
E_\Phi(r)
=
\left(r^2-\frac14\right)E_f(r),
\tag{L-91310.17}
\]

\[
O_\Phi(r)
=
\left(r^2-\frac14\right)O_f(r)
+
2r f_*(0).
\tag{L-91310.18}
\]

There is exactly one boundary trace.

## 5. Proposed positive bulk

Define the form sum

\[
\mathbb H_a
=
H_\theta
\boxplus
\mathcal S_a^{(\beta)}
\boxplus
\mathcal N_{\rm Pois}
\boxplus
\mathcal D_2,
\tag{L-91310.19}
\]

where

- `H_theta` is the supersymmetric theta bulk;
- `S_a^(beta)` is the tensor/direct-integral assembly of the positive log-odds
  cells through the Gamma–Beta shadow coordinates;
- `N_Pois` is the nonnegative Poisson/Fock number-difference form;
- `D_2` is the positive radial `p=2` Riesz defect operator.

Every summand is positive on its natural core.

Define boundary maps `(Gamma_0,Gamma_1)` by the even and odd traces in
(L-91310.17)–(L-91310.18), with the `p=2` port carrying the known local factor.

## 6. Theta–Brownian DtN identification

The route-III closing theorem is:

> **Theta–Brownian DtN Identification (`TBDI_a`).**  
> The closed positive form `H_a` with the declared boundary maps has Weyl
> function
> \[
> m_a(r)
> =
> \Gamma_1(\mathbb H_a+r)^{-1}\Gamma_0^*
> =
> \ell_a(r)
> \tag{L-91310.20}
> \]
> after exact elimination of the local `p=2` factor.

Equivalently, the historical missing square becomes

\[
\boxed{
2\mathcal T^*L_R\mathcal T
+
\{L_X,\mathcal T^*\mathcal T\}
+
\mathcal E_\beta
+
\mathcal E_{\rm Pois}
+
\mathcal E_2
=
4\mathcal J_a^*\mathcal J_a.
}
\tag{L-91310.21}
\]

This strengthens the old unsupported identity by displaying the three
previously omitted positive reservoirs.

## 7. Why `TBDI_a` closes route III

Green's identity for `H_a>=0` gives

\[
\frac{
\ell_a(r)+\overline{\ell_a(s)}
}{
r+\bar s
}
\succeq0.
\tag{L-91310.22}
\]

The exact Cayley congruence of `L-91307` gives the target Schur-Pick kernel,
hence innerness of `Theta_a`.

## 8. The exact remaining calculation

The local cell, theta transmutation, Poisson/Fock source, and `p=2` port are
explicit. What remains is to prove that their Green boundary ledger has no
additional signed same-scale port and that its scalar Weyl ratio is exactly
(L-91310.3).

This is a source-specific equality of two analytic functions. A proof may be
organized by showing that the proposed bulk numerator and denominator:

1. have the same safe-half-plane Laplace transforms as the Xi odd/even
   functions;
2. obey the same functional equation and boundary normalization;
3. have an identically zero difference by analytic uniqueness.

No appeal to assumed Pick positivity is allowed.
