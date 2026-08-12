# L-91034 — Exact Kreĭn–Langer source/critical/stable/zero-port decomposition

Claim ID: `L-91034`  
Status: **EXACT MEROMORPHIC-INNER KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Corrected: 2026-08-12 — separated the de Branges–Rovnyak kernel identity from the still-open arithmetic-Hankel/Cauchy-Weil intertwiner  
Depends on: the symmetric Hadamard product for `xi`; `L-91010`; standard half-plane Blaschke/model-space algebra  
RH status: **unproved**

## 1. Shifted half-plane and completed scattering ratio

Work in

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

The load-bearing algebra is the product rule

\[
 \boxed{
 K_{FG}(z,w)
 =K_F(z,w)
 +F(z)\overline{F(w)}K_G(z,w).
 }
 \tag{L-91034.4}
\]

## 2. Deterministic stable inner factor

For `p in H`, let

\[
 b_p(z)=\frac{z-p}{z+\overline p}.
 \tag{L-91034.5}
\]

The first stored Cauchy Hardy factor has repeated stable poles at
`-a,-2a,-4a`. The corresponding deterministic inner factor is

\[
 \boxed{
 \Delta_a(z)=b_a(z)^2b_{2a}(z)^2b_{4a}(z)^2.
 }
 \tag{L-91034.6}
\]

Its model space has dimension six and is the canonical finite stable-port
space. The exact stored Cauchy transfer itself is

\[
 P_a(z)=\sqrt{378}\,a^3
 \frac{z(z+\sqrt\alpha a)(z+\sqrt\beta a)}
 {(z+a)^2(z+2a)^2(z+4a)^2},
 \qquad
 \alpha+\beta=\frac{163}{14},\quad\alpha\beta=16,
 \tag{L-91034.7}
\]

but no pointwise multiplication by `P_a` is used in the unfiltered kernel
identity below.

## 3. Crossed xi-zero Blaschke factor

A denominator zero

\[
 \rho=\frac12+d+i\gamma
\]

of `Theta_a` produces the pole

\[
 p_{\rho,a}=d-a+i\gamma.
 \tag{L-91034.8}
\]

It lies in `H` exactly when `d>a`. Cancel common numerator/denominator factors
first. Let `P_a^zero` be the resulting pole multiset, with net multiplicities.
The zero count gives

\[
 \sum_{p\in P_a^{\rm zero}}
 \frac{\Re p}{1+|p|^2}<\infty.
 \tag{L-91034.9}
\]

Define

\[
 \boxed{
 B_a(z)=\prod_{p\in P_a^{\rm zero}}b_p(z)^{m(p)}.
 }
 \tag{L-91034.10}
\]

Boundary-pole scales are handled by one-sided limits.

## 4. Pole removal and inner factorization

The symmetric Hadamard product of `xi`, after reindexing numerator zeros by
functional-equation reflection, gives

\[
 \Theta_a(z)
 =e^{i\vartheta_a}
 \prod_{\lambda}^{\rm sym}
 \frac{z+\overline\lambda}{z-\lambda},
 \qquad
 \lambda=\rho-\frac12-a.
 \tag{L-91034.11}
\]

For `Re(lambda)>0`, the factor is `b_lambda^{-1}` and is cancelled by `B_a`.
For `Re(lambda)<0`, it is a Blaschke factor after putting
`p=-conj(lambda)`. A boundary factor cancels identically. The symmetric product
and (L-91034.9) converge.

Consequently

\[
 \boxed{A_a(z):=B_a(z)\Theta_a(z)}
 \tag{L-91034.12}
\]

is analytic inner in `H`. Stirling asymptotics show that no adverse exponential
outer factor occurs. Therefore

\[
 \boxed{
 I_a(z):=\Delta_a(z)B_a(z)\Theta_a(z)
 =\Delta_a(z)A_a(z)
 }
 \tag{L-91034.13}
\]

is inner.

## 5. Exact unfiltered four-term identity

At points avoiding the pole sets, define

\[
 \boxed{
 \begin{aligned}
 \mathcal K_a^{\rm src}(z,w)
 &:={K_{I_a}(z,w)\over
 \Delta_a(z)B_a(z)
 \overline{\Delta_a(w)B_a(w)}},\\[1mm]
 \mathcal K_a^{\rm crit}(z,w)
 &:=K_{\Theta_a}(z,w),\\[1mm]
 \mathcal K_a^{\rm st}(z,w)
 &:={K_{\Delta_a}(z,w)\over
 \Delta_a(z)B_a(z)
 \overline{\Delta_a(w)B_a(w)}},\\[1mm]
 \mathcal K_a^{\rm hyp}(z,w)
 &:={K_{B_a}(z,w)\over
 B_a(z)\overline{B_a(w)}}.
 \end{aligned}
 }
 \tag{L-91034.14}
\]

Apply (L-91034.4) twice:

\[
 K_{I_a}
 =K_{\Delta_a}
 +\Delta_a\overline{\Delta_a}K_{B_a}
 +\Delta_a B_a\overline{\Delta_a B_a}K_{\Theta_a}.
 \tag{L-91034.15}
\]

Division by the common inner factors gives

\[
 \boxed{
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}
  +\mathcal K_a^{\rm st}
  +\mathcal K_a^{\rm hyp}.
 }
 \tag{L-91034.16}
\]

The source, stable-port, and hyperbolic-port kernels are positive semidefinite:
`K_(I_a)`, `K_(Delta_a)`, and `K_(B_a)` are positive kernels, and scalar
congruence preserves positivity. The critical kernel may have negative squares.

Equation (L-91034.16) is the exact Kreĭn–Langer/Potapov decomposition. It has
no contour remainder.

## 6. Common filtering preserves the identity

Let `T` be any linear map defined on the four common feature spaces—for
example, a finite rational Hardy filter, a boundary convolution, a carrier
localizer, or a finite packet evaluation map. Apply `T` in the first variable
and its adjoint in the second. Then

\[
 \boxed{
 T\mathcal K_a^{\rm src}T^*
 =T\mathcal K_a^{\rm crit}T^*
  +T\mathcal K_a^{\rm st}T^*
  +T\mathcal K_a^{\rm hyp}T^*.
 }
 \tag{L-91034.17}
\]

All three positive terms remain positive.

Therefore, **once the actual Cauchy Hardy map of `T-91006` is constructed on
this common model-space domain**, (L-91034.17) becomes precisely

\[
 \boxed{
 \begin{aligned}
 \text{safe positive source Gram}
 ={}&\text{critical Cauchy Gram}\\
 &+\text{deterministic stable ports}\\
 &+\text{crossed hyperbolic zero ports}.
 \end{aligned}}
 \tag{L-91034.18}
\]

The italicized domain/intertwining clause is load-bearing. Pointwise
multiplication of `K_(Theta_a)` by `P_a(z)conj(P_a(w))` is not automatically the
translation-invariant Weil/Cauchy filtering of `T-91006`.

## 7. Explicit port vectors

For an ordered Blaschke product `B=prod b_(p_nu)`, the Takenaka--Malmquist
functions

\[
 e_\nu(z)
 =\sqrt{2\Re p_\nu}
 {1\over z+\overline{p_\nu}}
 \prod_{\ell<\nu}b_{p_\ell}(z)
 \tag{L-91034.19}
\]

satisfy

\[
 K_B(z,w)=\sum_\nu e_\nu(z)\overline{e_\nu(w)}.
 \tag{L-91034.20}
\]

Repeated zeros are repeated in the ordering. This supplies six explicit
stable states from `Delta_a` and one explicit state per crossed zero pole from
`B_a`.

For one simple pole `p`,

\[
 \boxed{
 {K_{b_p}(z,w)\over b_p(z)\overline{b_p(w)}}
 ={2\Re p\over(z-p)(\overline w-\overline p)}.
 }
 \tag{L-91034.21}
\]

Thus a crossed xi pole is a positive rank-one output port. Pairing conjugate
poles realifies it into the expanding/contracting two-state hyperbolic block.
In the critical kernel the same square appears with the opposite sign.

## 8. RH is exactly absence of the zero-port factor

Under RH, `Theta_a` has no pole in `H`, so

\[
 B_a\equiv1,
 \qquad
 K_{B_a}\equiv0,
 \qquad
 \mathcal K_a^{\rm hyp}\equiv0.
 \tag{L-91034.22}
\]

Conversely, if an off-line zero has depth `d>0`, choose
`0<a<d` outside the countable set of possible shift cancellations. Then
`B_a` is nonconstant and (L-91034.21) gives a nonzero port. Hence

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal K_a^{\rm hyp}\equiv0
 \text{ for every }a>0.
 }
 \tag{L-91034.23}
\]

A dense countable set of scales is enough.

## 9. Exact limitation

This theorem proves the meromorphic-inner kernel decomposition. It does not
complete the arithmetic CJHI theorem.

In particular:

1. the completely-monotone Hankel kernel of `L-91031` depends only on
   `z+conj(w)`;
2. the pole-removed source kernel in (L-91034.14) is a two-variable
   de Branges--Rovnyak kernel;
3. the translation-invariant Cauchy/Weil filter of `T-91006` is not merely
   pointwise multiplication in the `z` variable.

An explicit coisometry/intertwiner must connect those spaces. Treating them as
identical would assume the missing theorem.

No positivity statement alone deletes `K_(B_a)`: the one-pole control in
`R-91005` shows exact cancellation between a negative critical kernel and a
nonzero positive pole port even when the source kernel is identically zero.
