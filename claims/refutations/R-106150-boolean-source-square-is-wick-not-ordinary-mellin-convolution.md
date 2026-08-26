# R-106150 — A Boolean source square is a Wick convolution, not an ordinary Mellin self-convolution

Claim ID: `R-106150`  
Programme aliases: `LFAM1.BOOLEAN_WICK_FIREWALL`, `LFAM2.SHARED_LABEL_CONTRACTION`, `STRESS.HALF_SOURCE_SELF_SQUARE_AUDIT`  
Status: **PROVED EXACT SOURCE-ALGEBRA FIREWALL; THE FIRST SCALAR SELF-CONVOLUTION FORM OF `L-106134` IS CORRECTED**  
Created: 2026-08-25  
Depends on: `L-106132--L-106134`; parent `T-102990` and its closed repeated/higher-prime-power ledger  
Programme issues: #743, #736, #737  
RH status: **unproved**

`L-106133` proves an exact square in the squarefree Boolean algebra:

\[
\mathfrak B_U^{\rm eq}
=
\int_0^1(1-\theta)
\mathfrak G_{U,\theta}\star
\mathfrak G_{U,\theta}\,d\theta.
\]

The symbol `star` requires disjoint prime-label supports. The first version of
`L-106134` silently replaced it by ordinary source convolution when passing to
Mellin self-convolution. That replacement is false before shared-label
contractions are removed.

## 1. Finite counterfixture

Let one source field consist of a single labelled owner atom `x_p`. Then

\[
x_p\star x_p=0
\]

in the Boolean algebra, because the two factors share the label `p`.
Ordinary multiplication instead contains

\[
x_p^2=p^{-1}U_{p^2}\ne0.
\]

With two atoms `x_p+x_q`,

\[
(x_p+x_q)^2
=x_p^2+2x_px_q+x_q^2,
\]

whereas

\[
(x_p+x_q)\star(x_p+x_q)=2x_px_q.
\]

Thus ordinary Mellin self-convolution contains source terms which are absent
from the canonical squarefree equal-pair source.

## 2. Exact Wick/ordinary decomposition

Let the labelled half-source field be

\[
F(X)=\sum_\alpha c_\alpha A(X/n_\alpha),
\]

where `supp(alpha)` is the prime-label support of the atom. Define the
Wick--Mellin convolution

\[
\boxed{
(F\diamond_M F)(X)
=
\sum_{\substack{\alpha,\beta\\
                 \operatorname{supp}\alpha\cap
                 \operatorname{supp}\beta=\varnothing}}
 c_\alpha c_\beta
 (A*_M A)(X/(n_\alpha n_\beta)).
}
\tag{R-106150.1}
\]

The ordinary Mellin convolution splits exactly as

\[
\boxed{
F*_MF
=F\diamond_MF+\operatorname{Contr}(F),
}
\tag{R-106150.2}
\]

where `Contr(F)` is the sum over pairs sharing at least one literal label.

## 3. Every contraction is a repeated/higher-power source field

One atom of the owner--core half-source has physical form

\[
p a^2,
\qquad(p,a)=1.
\]

If two half-source atoms share a label `r`, then inside their ordinary product
that label occurs as one of:

```text
owner / owner:  r^2;
owner / core:   r^3;
core / core:    r^4.
```

Multiple shared labels only increase these exponents. Therefore every term of
`Contr(F)` belongs to the repeated-label or higher-prime-power source ledger.

The parent `T-102990` records these fields as already closed at subpower cost
in the fixed derivative/outer observation. Hence the contraction is not zero,
but its complete observed contribution may be moved into the inherited closed
remainder.

## 4. Correct common-mother statement

The exact source identity is

\[
\boxed{
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U^{\diamond},
}
\tag{R-106150.3}
\]

where

\[
\mathcal J_U^{\diamond}
=
\int_0^1(1-\theta)
(F_{U,\theta}\diamond_MF_{U,\theta})\,d\theta.
\]

If

\[
\mathcal J_U
=
\int_0^1(1-\theta)
(F_{U,\theta}*_MF_{U,\theta})\,d\theta,
\]

then

\[
\mathcal J_U
=
\mathcal J_U^{\diamond}+\mathcal C_U
\]

with `mathcal C_U` in the closed repeated/higher-power ledger. Consequently
the ordinary self-convolution may still be used in a conclusion theorem only
**modulo this explicit closed contraction field**.

## 5. Reflection and Mellin consequences

The reflection-signature identity

\[
(F*_MF)(e^x)
=\|E_xf\|_2^2-\|O_xf\|_2^2
\]

is an identity for the ordinary self-convolution. It does not hold termwise for
the Wick projection. It remains a valid sufficient coordinate because the
difference is the inherited closed contraction field.

Likewise, the exact Mellin coordinate of the Boolean source is the
normal-ordered analytic square

\[
\widehat{\mathcal J_U^{\diamond}}(s)
=
\int_0^1(1-\theta)
:\!\widehat F_{U,\theta}(s)^2\!:_B\,d\theta,
\]

not the unqualified ordinary square. The Boolean normal-ordering symbol removes
all shared-label contractions and introduces no complex conjugation.

## Binding consequence

```text
L-106133 Boolean/Beta half-source square             RETAINED EXACT
first L-106134 ordinary exact self-convolution       CORRECTED
exact Wick self-convolution                          PROVED EXACT
ordinary self-convolution modulo closed contractions VALID
reflection signature modulo closed contractions      VALID SUFFICIENT COORDINATE
T-106150                                              CORRECTED
Riemann Hypothesis                                    UNPROVED
```

The corrected statements are in `L-106134` and `T-106150`.
