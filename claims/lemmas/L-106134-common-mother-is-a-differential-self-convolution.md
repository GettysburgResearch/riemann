# L-106134 — The common mother and derivative outer detector are finite differential images of one self-convolution field

Claim ID: `L-106134`  
Programme aliases: `LFAM1.SAME_FIELD_COMMON_MOTHER`, `LFAM2.ANALYTIC_SQUARE_NORMAL_FORM`, `STRESS.REFLECTION_SIGNATURE_CURRENT`  
Status: **PROVED EXACT SOURCE/KERNEL FACTORIZATION**  
Created: 2026-08-25  
Depends on: `L-106133`; parent `L-102500`, `L-102701`, `L-102740`, `L-102880`, `L-102885`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Apply the compact common mother to the exact equal-pair source square of
`L-106133`. The resulting conclusion-bearing field is a finite differential
image of one same-field Mellin self-convolution.

## 1. One owner–core half-field

For a source sequence `Gamma` whose literal arithmetic weights are already
included, write

\[
\mathcal O_K[\Gamma](X)
=\sum_n\Gamma(n)K(X/n).
\tag{L-106134.1}
\]

Let `A` be the positive ratio-four spline of `L-102701`, and put

\[
A_-=(D-1/2)A,
\qquad
\Phi_*=2A_-*_M A.
\tag{L-106134.2}
\]

For the combined owner–core half-source of `L-106133`, define

\[
\boxed{
F_{U,\theta}(X)
=\mathcal O_A[\mathfrak G_{U,\theta}](X).
}
\tag{L-106134.3}
\]

On a finite physical horizon every source sum and every Mellin convolution is
compact because `supp(A) subset [1,4]`.

Put

\[
\boxed{
\mathcal J_U(X)
=\int_0^1(1-\theta)
\bigl(F_{U,\theta}*_M F_{U,\theta}\bigr)(X)
\,d\theta.
}
\tag{L-106134.4}
\]

## 2. Exact common-mother identity

Multiplicative source convolution and Mellin kernel convolution commute by
finite Fubini. Using `L-106133.12` and (L-106134.2),

\[
\begin{aligned}
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
={}&2\int_0^1(1-\theta)
\bigl((D-1/2)F_{U,\theta}\bigr)*_M
F_{U,\theta}\,d\theta.
\end{aligned}
\tag{L-106134.5}
\]

For Mellin convolution,

\[
D(f*_M g)=(Df)*_M g=f*_M(Dg).
\tag{L-106134.6}
\]

Therefore

\[
2\bigl((D-1/2)F\bigr)*_M F
=(2D-1)(F*_M F),
\]

and hence

\[
\boxed{
\mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
=(2D-1)\mathcal J_U.
}
\tag{L-106134.7}
\]

The factor is `2D-1`, not `D-1`: differentiation of a convolution equals the
derivative on either factor, not the sum of the two derivatives.

## 3. CV, XD, outer and derivative-outer coordinates

The parent common-mother channels satisfy

\[
K_{\rm CV}=D\Phi_*,
\qquad
K_{\rm XD}=\frac12(D+3/2)\Phi_*.
\]

Thus

\[
\boxed{
\mathcal O_{K_{\rm CV}}[\mathfrak B_U^{\rm eq}]
=D(2D-1)\mathcal J_U,
}
\tag{L-106134.8}
\]

\[
\boxed{
\mathcal O_{K_{\rm XD}}[\mathfrak B_U^{\rm eq}]
=\frac12(D+3/2)(2D-1)\mathcal J_U.
}
\tag{L-106134.9}
\]

For the centered outer kernel, `L-102740` gives

\[
R_L
=\frac12(D-1)(5D+3/2)\Phi_*
\]

at the observation level. Since `K_L=DR_L`,

\[
\boxed{
\mathcal O_{R_L}[\mathfrak B_U^{\rm eq}]
=\frac12(D-1)(5D+3/2)(2D-1)\mathcal J_U,
}
\tag{L-106134.10}
\]

and

\[
\boxed{
\mathcal O_{K_L}[\mathfrak B_U^{\rm eq}]
=\frac12D(D-1)(5D+3/2)(2D-1)\mathcal J_U.
}
\tag{L-106134.11}
\]

Equation (L-106134.11) is the live derivative/ratio-eight observation used in
`T-102990`, modulo the already-closed squared, repeated-label, Type-I and
terminal fields.

It is compatible with the stable same-`K1` identity of `L-102885`:

\[
(D+3/2)K_L
=D(D-1)(5D+3/2)K_{\rm XD}.
\]

## 4. Analytic square in Mellin space

For every initially convergent Mellin parameter,

\[
\boxed{
\widehat{\mathcal J_U}(s)
=\int_0^1(1-\theta)
\widehat F_{U,\theta}(s)^2\,d\theta.
}
\tag{L-106134.12}
\]

The square is analytic and has no complex conjugation. Consequently it is not
a positive family energy and must not be replaced by
`|widehat F_(U,theta)(s)|^2`.

Multiplicative character twisting preserves the form:

\[
\widehat{\mathcal J_{U,\chi}}(s)
=\int_0^1(1-\theta)
\widehat F_{U,\theta,\chi}(s)^2\,d\theta,
\tag{L-106134.13}
\]

because characters are multiplicative on the two half-source factors. This is
the one-field L-family coordinate associated with the physical-squareclass
families of `T-106140`.

## 5. Reflection signature on the real line

For the real principal field, write

\[
f_\theta(u)=F_{U,\theta}(e^u)
\]

and let

\[
(R_xf)(u)=f(x-u).
\]

`R_x` is a unitary involution. With

\[
E_xf=\frac12(I+R_x)f,
\qquad
O_xf=\frac12(I-R_x)f,
\]

one has exactly

\[
\boxed{
(F_{U,\theta}*_M F_{U,\theta})(e^x)
=\|E_xf_\theta\|_2^2
-\|O_xf_\theta\|_2^2.
}
\tag{L-106134.14}
\]

Thus the self-convolution is an indefinite reflection signature: its negative
part is carried by reflection-odd energy, not by an unexplained four-owner
coherence term.

## Scope

The lemma is an exact source and multiplier compression. It does not prove a
one-sided bound for the differential image in (L-106134.11). Controlling that
image is the same-field frontier `T-106150`; the Wick-centered additive and
Kummer split remains `T-106140`.
