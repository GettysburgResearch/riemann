# L-106434 — Endpoint residues are weighted samples of the actual Xi Turán current

Claim ID: `L-106434`  
Status: **PROVED EXACT FOR FINITE REGULAR ENDPOINT QUOTIENTS; CONFLUENT FORM BY JETS**  
Created: 2026-08-25  
Depends on: `L-106400--L-106401`; `L-106433`  
RH status: **not assumed**

Let `F` be a real entire function or a finite canonical-product truncation on
a regular window.  Put

\[
N=(F-i\lambda F')(F''+i\lambda F'''),
\]

\[
D=(F+i\lambda F')(F''-i\lambda F'''),
\qquad
U=N/D,
\]

and reduce all common factors.  Define the endpoint Turán current

\[
\mathcal T_F=FF'''-F'F''.
\]

The exact endpoint cancellation is

\[
\boxed{N-D=2i\lambda\mathcal T_F.}
\tag{L-106434.1}
\]

## 1. Simple-pole residue identity

Let `b` be a simple upper-half-plane zero of the reduced denominator `D`.
Then `N(b)` is nonzero and

\[
\boxed{
\operatorname{Res}_{z=b}U(z)
 ={N(b)\over D'(b)}
 ={2i\lambda\mathcal T_F(b)\over D'(b)}.
}
\tag{L-106434.2}
\]

Use the Fourier convention

\[
\widehat f(\omega)
 ={1\over2\pi}\int_{\mathbb R}f(t)e^{-i\omega t}dt.
\]

For `xi>0`, closing the contour in the upper half-plane gives

\[
\boxed{
\widehat U(-\xi)
 =i\sum_{b\in\mathcal P_+(U)}
  \operatorname{Res}(U,b)e^{ib\xi}
 =-2\lambda\sum_b
  {\mathcal T_F(b)\over D'(b)}e^{ib\xi}.
}
\tag{L-106434.3}
\]

The constant boundary value of `U` contributes only at frequency zero and is
irrelevant to every Hankel trace.

## 2. Literal visible Xi sampling Gram

Write `b_j=a_j+i y_j` and

\[
\alpha_{jk}=y_j+y_k-i(a_j-a_k).
\]

Substitution of (L-106434.3) into `L-106433` gives

\[
\boxed{
V_H^-(U)
 =4\lambda^2
 \sum_{j,k}
 {\mathcal T_F(b_j)\over D'(b_j)}
 {\overline{\mathcal T_F(b_k)}\over\overline{D'(b_k)}}
 {1-e^{-H\alpha_{jk}}\over\alpha_{jk}^2}.
}
\tag{L-106434.4}
\]

The adverse unobserved Gram is

\[
\boxed{
C_H^-(U)
 =4\lambda^2
 \sum_{j,k}
 {\mathcal T_F(b_j)\over D'(b_j)}
 {\overline{\mathcal T_F(b_k)}\over\overline{D'(b_k)}}
 {e^{-H\alpha_{jk}}\over\alpha_{jk}^2}.
}
\tag{L-106434.5}
\]

Both matrices are positive semidefinite.  The favorable orientation is the
corresponding Gram at the lower denominator divisor, or equivalently the
upper divisor of the reflected quotient, and is subtracted in the signed
tail before taking a positive part.

For `F=Xi`, `L-106401` gives

\[
\widehat{\mathcal T_\Xi}(\xi)
 =-i\xi\Lambda_\Xi(\xi),
\qquad
\Lambda_\Xi\ge0.
\]

Thus every numerator sample in (L-106434.4)--(L-106434.5) is an evaluation of
the explicit actual-Xi exterior-square source.  The only remaining weights are
the literal companion-pole interpolation factors `1/D'(b_j)` and the positive
Cauchy/exponential kernel.

## 3. Confluent blocks

If `b` is a pole of order `r`, the partial fraction coefficients are linear
combinations of the jets

\[
\partial_z^q
 \left({2i\lambda\mathcal T_F(z)\over D(z)/(z-b)^r}ight)_{z=b},
\qquad 0\le q<r.
\]

The hard-band Gram is obtained by applying the corresponding derivatives to
`(1-exp(-H alpha))/alpha^2`; the complement uses
`exp(-H alpha)/alpha^2`.  Hence multiplicity and collision conditioning are
fully explicit and cannot be hidden in a scalar source ratio.

## 4. Correct surviving interpolation target

The actual visible `1/600` row would follow from the Xi-specific inequality

\[
4\lambda_T^2
 \sum_{j,k}
 {\mathcal T_\Xi(b_j)\over D_T'(b_j)}
 {\overline{\mathcal T_\Xi(b_k)}\over\overline{D_T'(b_k)}}
 {1-e^{-H_T\alpha_{jk}}\over\alpha_{jk}^2}
 <\left({1\over600}+o(1)\right)N(T,2T).
\]

This is a precise weighted sampling theorem at the adverse endpoint companion
zeros.  It is not proved here.  The source hierarchy controls the numerator
function; a lower-frame or cancellation theorem for the denominator-derivative
weights remains necessary.
