# L-106134 — The common mother is a differential Wick self-convolution, and an ordinary self-convolution modulo closed contractions

Claim ID: `L-106134`  
Programme aliases: `LFAM1.SAME_FIELD_COMMON_MOTHER`, `LFAM2.WICK_ANALYTIC_SQUARE`, `STRESS.REFLECTION_SIGNATURE_CURRENT`  
Status: **CORRECTED EXACT SOURCE/KERNEL FACTORIZATION; ORDINARY REFLECTION FORM VALID MODULO THE INHERITED CLOSED CONTRACTION LEDGER**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106133`; binding `R-106150`; parent `L-102500`, `L-102701`, `L-102740`, `L-102880`, `L-102885`, `T-102990`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Apply the compact common mother to the exact equal-pair Boolean source square
of `L-106133`. Because that source square uses disjoint-support convolution,
its exact same-field image is a Wick--Mellin self-convolution. Ordinary Mellin
self-convolution differs by repeated-label contractions; those contractions
belong to the parent’s already-closed squared/higher-prime-power ledger.

## 1. One owner--core half-field

For a labelled source sequence `Gamma`, with all literal arithmetic weights
included, write

\[
\mathcal O_K[\Gamma](X)
=\sum_\alpha\Gamma(\alpha)K(X/n_\alpha).
\tag{L-106134.1}
\]

Let `A` be the positive ratio-four spline of `L-102701`, and put

\[
A_-=(D-1/2)A,
\qquad
\Phi_*=2A_-*_M A.
\tag{L-106134.2}
\]

For the combined owner--core half-source of `L-106133`, define

\[
\boxed{
F_{U,\theta}(X)
=\mathcal O_A[\mathfrak G_{U,\theta}](X).
}
\tag{L-106134.3}
\]

The prime-label support of every coefficient remains attached to the field.

## 2. Wick--Mellin convolution

For two labelled fields built from the same kernel `A`, define

\[
\begin{aligned}
(F\diamond_MG)(X)
={}&
\sum_{\substack{\alpha,\beta\\
 \operatorname{supp}\alpha\cap
 \operatorname{supp}\beta=\varnothing}}
 c_\alpha d_\beta
 (A*_MA)(X/(n_\alpha m_\beta)).
\end{aligned}
\tag{L-106134.4}
\]

This is ordinary Mellin convolution followed by the exact Boolean/Wick
projection to disjoint source supports.

Put

\[
\boxed{
\mathcal J_U^{\diamond}(X)
=
\int_0^1(1-\theta)
(F_{U,\theta}\diamond_MF_{U,\theta})(X)
\,d\theta.
}
\tag{L-106134.5}
\]

On a finite labelled horizon the integral is only a compact notation for the
rational Beta coefficients of `L-106133`.

## 3. Exact common-mother identity

Boolean source convolution and Wick--Mellin kernel convolution commute by
finite Fubini. Using `L-106133.12` and (L-106134.2),

\[
\begin{aligned}
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
={}&2\int_0^1(1-\theta)
\bigl((D-1/2)F_{U,\theta}\bigr)
\diamond_MF_{U,\theta}\,d\theta.
\end{aligned}
\tag{L-106134.6}
\]

Differentiation commutes with the Wick support projection and, on each Mellin
kernel pair,

\[
D(f*_Mg)=(Df)*_Mg=f*_M(Dg).
\tag{L-106134.7}
\]

Therefore

\[
2\bigl((D-1/2)F\bigr)\diamond_MF
=(2D-1)(F\diamond_MF),
\]

and hence

\[
\boxed{
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U^{\diamond}.
}
\tag{L-106134.8}
\]

The factor is `2D-1`, not `D-1`: differentiation of a convolution equals the
derivative on either one factor, not a product-rule sum of both factors.

## 4. Ordinary completion and the contraction field

Define the ordinary self-convolution

\[
\boxed{
\mathcal J_U(X)
=
\int_0^1(1-\theta)
(F_{U,\theta}*_MF_{U,\theta})(X)
\,d\theta.
}
\tag{L-106134.9}
\]

By `R-106150`,

\[
\boxed{
\mathcal J_U
=
\mathcal J_U^{\diamond}+\mathcal C_U,
}
\tag{L-106134.10}
\]

where `mathcal C_U` is the sum of half-source pairs sharing at least one
literal prime label.

Every shared label has exponent `2`, `3`, or `4` in the resulting physical
source product, according as it is owner/owner, owner/core, or core/core.
Thus `mathcal C_U` belongs to the repeated-label and higher-prime-power source
ledger which `T-102990` records as already closed in the fixed derivative and
outer observations.

Consequently every exact formula below has two versions:

```text
with J_U^diamond: exact coefficientwise source identity;
with J_U:          the same identity modulo a subpower closed field.
```

## 5. CV, XD, outer and derivative-outer coordinates

The parent common-mother channels satisfy

\[
K_{\rm CV}=D\Phi_*,
\qquad
K_{\rm XD}=\frac12(D+3/2)\Phi_*.
\]

Therefore, exactly,

\[
\boxed{
\mathcal O_{K_{\rm CV}}[\mathfrak B_U^{\rm eq}]
=D(2D-1)\mathcal J_U^{\diamond},
}
\tag{L-106134.11}
\]

\[
\boxed{
\mathcal O_{K_{\rm XD}}[\mathfrak B_U^{\rm eq}]
=\frac12(D+3/2)(2D-1)\mathcal J_U^{\diamond}.
}
\tag{L-106134.12}

For the centered outer kernel, `L-102740` gives

\[
R_L=\frac12(D-1)(5D+3/2)\Phi_*
\]

at observation level, and `K_L=DR_L`. Hence

\[
\boxed{
\mathcal O_{R_L}[\mathfrak B_U^{\rm eq}]
=\frac12(D-1)(5D+3/2)(2D-1)
\mathcal J_U^{\diamond},
}
\tag{L-106134.13}
\]

\[
\boxed{
\mathcal O_{K_L}[\mathfrak B_U^{\rm eq}]
=\frac12D(D-1)(5D+3/2)(2D-1)
\mathcal J_U^{\diamond}.
}
\tag{L-106134.14}

Replacing `mathcal J_U^diamond` by the ordinary `mathcal J_U` changes the
right sides only by the inherited closed contraction field.

Equation (L-106134.14) is compatible with the stable same-`K1` relation of
`L-102885`.

## 6. Normal-ordered analytic square in Mellin space

For every initially convergent Mellin parameter, define Boolean normal ordering
by deleting coefficient pairs with intersecting prime-label supports. Then

\[
\boxed{
\widehat{\mathcal J_U^{\diamond}}(s)
=
\int_0^1(1-\theta)
:\!\widehat F_{U,\theta}(s)^2\!:_B
\,d\theta.
}
\tag{L-106134.15}
\]

Equivalently,

\[
:\!\widehat F^2\!:_B
=\widehat F^2-\widehat{\operatorname{Contr}(F)}.
\]

The square remains analytic and has no complex conjugation. Multiplicative
character twisting preserves the normal-ordered form and the literal physical
character `chi(p a^2)=chi(p)chi(a)^2`.

## 7. Reflection signature for the ordinary completion

For the real principal field, write

\[
f_\theta(u)=F_{U,\theta}(e^u),
\qquad
(R_xf)(u)=f(x-u).
\]

`R_x` is a unitary involution. With

\[
E_x=\frac12(I+R_x),
\qquad
O_x=\frac12(I-R_x),
\]

one has exactly

\[
\boxed{
(F_{U,\theta}*_MF_{U,\theta})(e^x)
=\|E_xf_\theta\|_2^2
-\|O_xf_\theta\|_2^2.
}
\tag{L-106134.16}
\]

This identity belongs to the ordinary completion `mathcal J_U`; it is not a
termwise identity for the Wick projection. Since the difference
`mathcal C_U` is already closed after the fixed differential observation, the
reflection signature remains a valid sufficient coordinate for the live
Boolean source.

## Scope

The lemma proves the exact Wick source factorization and the ordinary
reflection reduction modulo inherited closed contractions. It does not prove a
one-sided estimate for either differential image. Those gates are stated in
the corrected `T-106150`.
