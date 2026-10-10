# An exact two-variable Dirichlet representation of the negative Ramanujan branch

Status: exact identities in an absolute-convergence region. This supplies a concrete analytic object for the remaining branch; it does not assert an unproved continuation, reciprocal bound, contour saving, or moment theorem.

Dependencies: the coupled scalar and standard infinity-cusp coefficient in `COUPLED_THETA_COMPLETION.md`, and the defining completed Dirichlet series in October 5 `paper2.tex` immediately before `eq:theta-mellin-inversion` (around lines 3286–3301), at OpenAI commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Character factors retain the literal zeros at every excluded prime. This file is a separate proposed object and leaves all previous packets unchanged.

## 1. The remaining coefficient has an infinity type

In the all-negative allocation of the coupled reflection, a=g and e=f=1. Its local Ramanujan product is exactly

\[
\prod_{p\mid g}-(Np)^{-1/2}=\frac{\mu_K(g)}{\sqrt{Ng}}.
\tag{1.1}
\]

It imposes no coprimality between g and the theta index. The outer coefficient after the scalar cancellation is, up to a fixed ray factor,

\[
\mu_K(g)\overline{\alpha(g)}^{3}\chi_k(g)^3.
\tag{1.2}
\]

Thus the difficult coefficient is a Möbius coefficient of a Hecke character with fixed infinity type -3. It is not the finite-order character family of the preceding moment packet. Fixing the infinity type does not make it finite order, and it cannot be hidden in a fixed ray character.

The standard cusp coefficient includes

\[
\vartheta(n):=\overline{\chi_n(\lambda)^2},
\qquad \vartheta^3=1
\]

on ideals outside the fixed bad set. This is a fixed ray character there. Additional fixed-ray indicators and the additive phase at the fixed bad modulus can be expanded in the finitely many multiplicative characters of its unit group. The latter is valid because this standard face excludes the fixed bad primes. Consequently it suffices to keep two fixed ray characters eta and rho in the formulas below. The finite expansion may have complex coefficients; no positivity is inferred from it.

## 2. A literal product identity

For squarefree k outside S, define characters, with zero extension at S and at primes of k,

\[
\chi^-_{k,\eta}(g)=\eta(g)\overline{\alpha(g)}^{3}\chi_k(g)^3,
\qquad
\Psi^+_{k,\rho}(n)=\rho(n)\vartheta(n)\alpha(n)^2\chi_k(n)^3.
\tag{2.1}
\]

Let L_S(s,chi) denote the Euler product with exactly those literal zero factors. The coefficients use the chosen primary generators, so alpha is multiplicative on these ideals. With its fixed ray convention, (2.1) defines Hecke characters of fixed infinity types -3 and +2, respectively.

For Re(w)>1 and Re(s)>1, set

\[
\begin{aligned}
\mathcal Z_k(w,s;\eta,\rho)
={}&\sum_{g\ \mathrm{squarefree}}\mu_K(g)\chi^-_{k,\eta}(g)(Ng)^{-w}\\
&\quad\times\sum_{n\ \mathrm{squarefree}}
 \overline{\alpha(n)}\gamma_2(n)\Psi^+_{k,\rho}(n)(Nn)^{-s}\\
&\quad\times\sum_b
 \overline{\alpha(b)}^{3}\Psi^+_{k,\rho}(b)^3
 (Nb)^{-3s+1/2}.
\end{aligned}
\tag{2.2}
\]

All three series converge absolutely there. The first two use squarefree indices; b is unrestricted. There is no pairwise-coprimality condition among g,n,b. In particular this is the correct class for the negative term, including overlaps of g with n or b.

### Proposition 2.1

In that absolute-convergence region,

\[
\boxed{\mathcal Z_k(w,s;\eta,\rho)
 =\frac{\mathcal T(s,\Psi^+_{k,\rho})}
 {L_S(w,\chi^-_{k,\eta})}.}
\tag{2.3}
\]

Here mathcal T is exactly the formal completed Dirichlet series defined by the source, not an assumed finite-order specialization of its analytic reflection theorem.

**Proof.** Unique factorization and the literal zero convention give

\[
\sum_g\mu_K(g)\chi^-_{k,\eta}(g)(Ng)^{-w}
 =\prod_p\left(1-\chi^-_{k,\eta}(p)(Np)^{-w}\right)
 =L_S(w,\chi^-_{k,\eta})^{-1}.
\]

The product of the second and third series is the displayed definition of mathcal T. Absolute convergence permits all rearrangements. No functional equation is used. \(\square\)

In particular, because vartheta^3=1 and chi_k^9=chi_k^3 including its zeros,

\[
\mathcal T(s,\Psi^+_{k,\rho})
 =G_k(s;\rho)\,
 L_S\!\left(3s-\tfrac12,
       \rho^3\alpha^3\chi_k^3\right),
\tag{2.4}
\]

where

\[
G_k(s;\rho)=\sum_n^*\gamma_2(n)\rho(n)\vartheta(n)
                  \alpha(n)\chi_k(n)^3(Nn)^{-s}.
\]

The Gauss-coefficient series G_k is not declared an Euler product. Its twisted multiplicativity contains the cubic cross-symbol. Deleting that cross-symbol would change the object.

## 3. Exact Mellin arguments of the two variables

Use the Mellin convention W(x)=(2*pi*i)^(-1) integral W_hat(z)x^(-z) dz. Let Vsharp be the imported reflected weight and let its Mellin transform be Vsharp_hat(t). On the standard face, a fixed branch of the all-negative completed polynomial is a fixed scalar times

\[
\begin{aligned}
\frac1{\sqrt A}\sum_g^*&
 \frac{\mu_K(g)\eta(g)\overline{\alpha(g)}^3\chi_k(g)^3}{\sqrt{Ng}}
 W_1(Ng/A)\\
 &\times\sum_n^*\sum_b
 \frac{\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3
        \rho(b)^3\alpha(b)^3\chi_k(b)^3}
      {\sqrt{Nn}\,Nb}
 V^\sharp\!\left(\frac{c\,Nn\,(Nb)^3B}{(Ng)^2(Nk)^2}\right),
\end{aligned}
\tag{3.1}
\]

with c>0 fixed by the cusp and bad-prime normalization. The finite unit and ray scalars have already been retained by the decomposition above. Formula (3.1) follows directly from the exact scalar cancellation, the standard cusp coefficient including vartheta, and the all-negative choice in the Ramanujan product.

For any Re(t)>1/2 and Re(z)>2Re(t)+1/2, absolute convergence permits Mellin inversion and Proposition 2.1. It yields

\[
\boxed{
\frac1{(2\pi i)^2}
\int_{(z)}\!\int_{(t)}
 \widehat W_1(z)\widehat{V^\sharp}(t)
 A^{z-1/2}\left(\frac{cB}{(Nk)^2}\right)^{-t}
 \frac{\mathcal T(\tfrac12+t,\Psi^+_{k,\rho})}
 {L_S(\tfrac12+z-2t,\chi^-_{k,\eta})}
\,dt\,dz.}
\tag{3.2}
\]

The two linear arguments are therefore

\[
s=\tfrac12+t,
\qquad w=\tfrac12+z-2t.                                 \tag{3.3}
\]

The source's Schwartz estimates for Vsharp at infinity and its positive-power bound at zero justify its Mellin transform on the chosen right-hand line. Its gamma-quotient representation and the original smooth compact support supply the vertical decay needed for this initial double integral. This is an identity on the initial contours only; shifting them requires further analytic bounds with the displayed infinity types and conductor dependence.

## 4. Why the cube Euler factor does not simply cancel the reciprocal

Equations (2.3)–(2.4) display a numerator factor of type +3 at argument 3s-1/2 and a denominator factor of type -3 at the independent argument w. These are distinct Euler factors. Neither an absolute-convergence rearrangement nor complete multiplicativity identifies them.

Even in a primitive character normalization, applying the ordinary Hecke functional equation to the denominator would conjugate its character and replace w by 1-w. For cancellation with the numerator, one would additionally need the corresponding fixed-ray characters to match and

\[
1-w=3s-\tfrac12,
\quad\text{equivalently}\quad w+3s=\tfrac32.
\tag{4.1}
\]

Under the literal Mellin arguments (3.3), this becomes z+t=-1/2. A codimension-one relation between independent Mellin variables is not an identity of the double integral. Imprimitive Euler factors and conductor/gamma multipliers would also have to be retained. No such cancellation is used here.

The precise research object is therefore the joint quotient in (3.2), with angular characters, rather than a scalar theta transform with an arbitrary divisor multiplier. Establishing a bound for this quotient strong enough to survive the average over k remains an analytic problem. A finite-order zero-free theorem alone does not supply the needed inverse-L estimate.

## 5. What this reduction achieves

The all-negative component has been reduced to a literal two-variable product of a reciprocal Hecke L-function and a completed Gauss-coefficient series, in an explicit domain and with the correct Mellin coupling. It explains both why an Euler-factor approach is plausible and why replacing the divisor weight by a finite-order twist is invalid. It preserves every repeated-prime overlap, rather than excising an exceptional subfamily.

A possible next input is a uniform joint estimate for the quotient in (3.2), or a coupled functional equation which keeps its two variables and all fixed-ray components. Such an estimate would need to control the fixed infinity types and moving conductor. No existing multiple-Dirichlet-series theorem has been imported as if its coefficient system were already identical to (2.2).
