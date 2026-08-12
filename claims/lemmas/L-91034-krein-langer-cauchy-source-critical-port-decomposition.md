# L-91034 — Exact Kreĭn–Langer decomposition into source, critical Cauchy, stable, and zero ports

Claim ID: `L-91034`  
Status: **EXACT MEROMORPHIC-INNER KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: the symmetric Hadamard product for `xi`; `L-91010`; `L-91020`; standard half-plane Blaschke/model-space algebra  
RH status: **unproved**

## 1. Shifted half-plane and the completed scattering ratio

Work in the right half-plane

\[
 \mathbb H=\{z:\Re z>0\},
 \qquad s=\frac12+z.
\]

For `a>0`, define

\[
 \boxed{
 \Theta_a(z)
 =\frac{\xi(\frac12-a+z)}{\xi(\frac12+a+z)}.
 }
 \tag{L-91034.1}
\]

The functional equation and reality of `xi` give

\[
 |\Theta_a(iu)|=1
 \qquad(u\in\mathbb R)
 \tag{L-91034.2}
\]

wherever the quotient is finite.

For a meromorphic scalar function `F`, put

\[
 \boxed{
 K_F(z,w)
 =\frac{1-F(z)\overline{F(w)}}{z+\overline w}.
 }
 \tag{L-91034.3}
\]

The elementary product rule is

\[
 \boxed{
 K_{FG}(z,w)
 =K_F(z,w)
 +F(z)\overline{F(w)}K_G(z,w).
 }
 \tag{L-91034.4}
\]

It is an algebraic identity wherever all terms are defined.

## 2. Deterministic Cauchy inner factor

Let

\[
 b_p(z)=\frac{z-p}{z+\overline p},
 \qquad p\in\mathbb H.
 \tag{L-91034.5}
\]

Then `b_p` is a right-half-plane Blaschke factor.

The first stored Cauchy residual has the stable spectral factor

\[
 \boxed{
 P_a(z)
 =\sqrt{378}\,a^3
 \frac{z(z+\sqrt\alpha a)(z+\sqrt\beta a)}
 {(z+a)^2(z+2a)^2(z+4a)^2},
 }
 \tag{L-91034.6}
\]

where

\[
 \alpha+\beta=\frac{163}{14},
 \qquad \alpha\beta=16.
\]

On the boundary `z=iu`,

\[
 |P_a(iu)|^2
 =D_a^{(0)}(u)-\frac1{16}D_{2a}^{(0)}(u)
 \tag{L-91034.7}
\]

by `L-91020`.

Introduce the deterministic inner factor

\[
 \boxed{
 \Delta_a(z)
 =b_a(z)^2b_{2a}(z)^2b_{4a}(z)^2.
 }
 \tag{L-91034.8}
\]

Its six-dimensional model space is the finite stable-state port associated with the repeated Cauchy poles at `-a,-2a,-4a`.

## 3. The zero-pole Blaschke factor

A denominator zero

\[
 \rho=\frac12+d+i\gamma
\]

of `Theta_a` produces the pole

\[
 p_{\rho,a}=d-a+i\gamma.
 \tag{L-91034.9}
\]

It lies in `H` exactly when `d>a`. Cancel common numerator/denominator zeros first, and let `P_a^zero` be the resulting pole multiset in `H`, with net multiplicities.

The Riemann--von Mangoldt bound implies the Blaschke condition

\[
 \sum_{p\in P_a^{\rm zero}}
 \frac{\Re p}{1+|p|^2}<\infty.
 \tag{L-91034.10}
\]

Define the convergent Blaschke product

\[
 \boxed{
 B_a(z)
 =\prod_{p\in P_a^{\rm zero}}b_p(z)^{m(p)}.
 }
 \tag{L-91034.11}
\]

If a pole lies on the boundary, all formulas below are understood first away from that exceptional scale and then by a one-sided limit.

## 4. The pole-removed quotient is inner

The symmetric Hadamard product of `xi`, after reindexing the numerator zeros by functional-equation reflection, gives

\[
 \Theta_a(z)
 =e^{i\vartheta_a}
 \prod_{\lambda}^{\rm sym}
 \frac{z+\overline\lambda}{z-\lambda},
 \qquad
 \lambda=\rho-\frac12-a.
 \tag{L-91034.12}
\]

For `Re(lambda)>0`, the factor in (L-91034.12) is `b_lambda^{-1}` and is cancelled by `B_a`. For `Re(lambda)<0`, put `p=-conj(lambda)`; the same factor is `b_p`. A boundary factor cancels identically. The symmetric ordering and (L-91034.10) give a convergent product.

Consequently

\[
 \boxed{
 A_a(z):=B_a(z)\Theta_a(z)
 }
 \tag{L-91034.13}
\]

is an analytic inner function in `H`. A possible singular inner factor at infinity is harmless; Stirling asymptotics show its exponential mean type is zero.

Therefore

\[
 \boxed{
 I_a(z):=\Delta_a(z)A_a(z)
 =\Delta_a(z)B_a(z)\Theta_a(z)
 }
 \tag{L-91034.14}
\]

is also inner, and `K_(I_a)`, `K_(Delta_a)`, and `K_(B_a)` are positive semidefinite kernels.

## 5. The four kernels

At points avoiding the pole sets, define

\[
 \boxed{
 \begin{aligned}
 \mathcal G_a^{\rm src}(z,w)
 &:=
 \frac{P_a(z)\overline{P_a(w)}}
 {\Delta_a(z)B_a(z)
  \overline{\Delta_a(w)B_a(w)}}
 K_{I_a}(z,w),\\[1mm]
 \mathcal G_a^{\rm crit}(z,w)
 &:=P_a(z)\overline{P_a(w)}K_{\Theta_a}(z,w),\\[1mm]
 \mathcal G_a^{\rm st}(z,w)
 &:=
 \frac{P_a(z)\overline{P_a(w)}}
 {\Delta_a(z)B_a(z)
  \overline{\Delta_a(w)B_a(w)}}
 K_{\Delta_a}(z,w),\\[1mm]
 \mathcal G_a^{\rm hyp}(z,w)
 &:=
 \frac{P_a(z)\overline{P_a(w)}}
 {B_a(z)\overline{B_a(w)}}
 K_{B_a}(z,w).
 \end{aligned}
 }
 \tag{L-91034.15}
\]

The first kernel is the canonical pole-removed safe scattering Gram. The second is the critical Cauchy/Clark kernel filtered by the exact stored Cauchy factor. The third contains only the six deterministic stable states. The fourth contains exactly the crossed xi-zero poles.

## 6. Exact source/critical/port identity

Apply (L-91034.4) twice:

\[
 \begin{aligned}
 K_{I_a}
 &=K_{\Delta_a B_a\Theta_a}\\
 &=K_{\Delta_a}
  +\Delta_a(z)\overline{\Delta_a(w)}K_{B_a}
  +\Delta_a(z)B_a(z)
   \overline{\Delta_a(w)B_a(w)}K_{\Theta_a}.
 \end{aligned}
 \tag{L-91034.16}
\]

Multiplication by

\[
 \frac{P_a(z)\overline{P_a(w)}}
 {\Delta_a(z)B_a(z)
  \overline{\Delta_a(w)B_a(w)}}
\]

gives the promised identity:

\[
 \boxed{
 \mathcal G_a^{\rm src}
 =\mathcal G_a^{\rm crit}
  +\mathcal G_a^{\rm st}
  +\mathcal G_a^{\rm hyp}.
 }
 \tag{L-91034.17}
\]

This is exact, with no contour remainder and no sign estimate.

For every finite packet `(z_j)` and coefficients `(c_j)`,

\[
 \sum_{j,k}\overline{c_j}c_k
 \mathcal G_a^{\rm src}(z_j,z_k)\ge0,
 \tag{L-91034.18}
\]

and the same is true separately for the stable and hyperbolic port kernels. Positivity follows because multiplying a positive kernel by `m(z)conj(m(w))` is a Gram congruence.

Thus (L-91034.17) is precisely

\[
 \boxed{
 \begin{aligned}
 \text{safe positive source Gram}
 ={}&\text{critical Cauchy Gram}\\
 &+\text{deterministic stable ports}\\
 &+\text{crossed hyperbolic zero ports}.
 \end{aligned}}
 \tag{L-91034.19}
\]

## 7. Explicit port features

For an ordered Blaschke product `B=prod b_(p_nu)`, the Takenaka--Malmquist functions

\[
 e_\nu(z)
 =\sqrt{2\Re p_\nu}
 \frac1{z+\overline{p_\nu}}
 \prod_{\ell<\nu}b_{p_\ell}(z)
 \tag{L-91034.20}
\]

satisfy

\[
 K_B(z,w)=\sum_\nu e_\nu(z)\overline{e_\nu(w)}.
 \tag{L-91034.21}
\]

Repeated zeros are simply repeated in the ordering. Equations (L-91034.15) therefore give explicit stable and zero-port vectors.

For one simple crossed zero pole `p`,

\[
 \boxed{
 \frac{K_{b_p}(z,w)}
 {b_p(z)\overline{b_p(w)}}
 =\frac{2\Re p}
 {(z-p)(\overline w-\overline p)}.
 }
 \tag{L-91034.22}
\]

Hence its filtered port is the positive rank-one kernel

\[
 \boxed{
 \mathcal P_{a,p}(z,w)
 =\frac{2\Re p\,P_a(z)\overline{P_a(w)}}
 {(z-p)(\overline w-\overline p)}
 }
 \tag{L-91034.23}
\]

up to the preceding inner factors in the chosen model-space ordering.

For

\[
 p=d-a+i\gamma,
\]

the boundary diagonal is proportional to

\[
 \frac{2(d-a)|P_a(ix)|^2}
 {(d-a)^2+(x-\gamma)^2}.
 \tag{L-91034.24}
\]

The conjugate pole realifies with it into the two-state expanding/contracting hyperbolic block of `L-91010/L-91025`. In the critical kernel the corresponding model-space square is subtracted; in (L-91034.17) it is retained as an output port.

## 8. RH and absence of the hyperbolic port

Under RH there is no pole of `Theta_a` in `H` for any `a>0`. Thus

\[
 B_a\equiv1,
 \qquad
 K_{B_a}\equiv0,
 \qquad
 \boxed{\mathcal G_a^{\rm hyp}\equiv0.}
 \tag{L-91034.25}
\]

Conversely, suppose an off-line zero has depth `d>0`. Choose `0<a<d` outside the countable set of possible numerator/denominator cancellation spacings. Then `Theta_a` has a genuine pole in `H`, `B_a` is nonconstant, and (L-91034.23) gives a nonzero hyperbolic port. Therefore

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal G_a^{\rm hyp}\equiv0
 \text{ for every }a>0.
 }
 \tag{L-91034.26}
\]

The implication remains valid if `a` is restricted to any dense countable set.

## 9. Exact limitation

Equation (L-91034.17) proves the structural source/critical/port identity. It does **not** prove that the zero-port term vanishes.

It also does not by itself identify the pole-removed model-space source kernel `G_src` with the scalar completely-monotone Hankel kernel of `L-91031`. Those are different positive realizations: the former is a two-variable de Branges--Rovnyak kernel, while the latter depends only on `z+conj(w)`. A separate source-ordering/coisometry theorem is required to identify or dominate them.

Thus the exact remaining alternatives are:

1. prove `G_hyp=0`, which is RH by (L-91034.26); or
2. construct an arithmetic coisometry from the explicit safe Stinespring space of `L-91031` onto `G_src` and prove that its stable and critical outputs exhaust the source norm, leaving no hyperbolic output.

No positivity statement alone can delete the last term.