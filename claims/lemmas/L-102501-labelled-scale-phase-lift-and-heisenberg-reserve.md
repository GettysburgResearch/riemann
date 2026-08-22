# L-102501 — Labelled scale–phase lift and the covariant Heisenberg reserve

Claim ID: `L-102501`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Depends on: `L-102500`  
RH status: **not assumed**

Let `L` be a finite labelled prime multiset. The two copies of `67` are
distinct labels even though their prime values agree. For a label `ell`, put

\[
p_\ell=\text{its prime value},\qquad
r_\ell=p_\ell^{-1/2},\qquad
\lambda_\ell=\log p_\ell.
\]

Let

\[
(U_\ell f)(u)=f(u-\lambda_\ell)
\]

and write `vartheta=(vartheta_ell)` on the labelled torus. With
`phi(u)=Phi_*(e^u)`, define

\[
\boxed{
\mathcal F_{\mathcal L}(u,\vartheta)=
\prod_{\ell\in\mathcal L}
\left(I-r_\ell e^{-i\vartheta_\ell}U_\ell\right)\phi(u).
}
\tag{L-102501.1}
\]

At `vartheta=0` this is the exact physical finite Euler source. Keeping the two
`67` coordinates separate preserves the labelled source before equal-product
collapse.

## 1. Relative phase coordinate

Define

\[
\Lambda=i\sum_{\ell\in\mathcal L}
\lambda_\ell\partial_{\vartheta_\ell},
\qquad Q=u-\Lambda,
\qquad P=-i\partial_u.
\tag{L-102501.2}
\]

On the character indexed by a labelled subset `S`, `Lambda` has eigenvalue

\[
\lambda_S=\sum_{\ell\in S}\log p_\ell.
\]

Therefore

\[
\boxed{
Q[\phi(u-\lambda_S)e^{-i\vartheta_S}]
=(u-\lambda_S)\phi(u-\lambda_S)e^{-i\vartheta_S}.
}
\tag{L-102501.3}
\]

The absolute `log(n)` carrier has disappeared. Only the relative coordinate in
the fixed compact mother remains. Since `supp(phi) subset [0,log 16]`, every
labelled atom has `0 <= u-lambda_S <= log 16` on its support.

## 2. Canonical commutator

On the compactly supported finite Euler domain,

\[
\boxed{[P,Q]=-iI.}
\tag{L-102501.4}
\]

This is unaffected by the number of labels, duplicate `67`, or equal physical
products.

## 3. Strict determinant reserve

Use

\[
\mathscr H_{\mathcal L}=L^2(\mathbb R_u\times\mathbb T^{\mathcal L}_\vartheta).
\]

For `F` in the finite labelled domain define

\[
\mathsf S(F)=
\begin{pmatrix}
\|PF\|^2&\Re\langle PF,QF\rangle\\
\Re\langle PF,QF\rangle&\|QF\|^2
\end{pmatrix}.
\]

The commutator gives

\[
2i\,\Im\langle PF,QF\rangle
=\langle F,[P,Q]F\rangle=-i\|F\|^2.
\]

Cauchy–Schwarz therefore yields

\[
\boxed{\det\mathsf S(F)\ge\frac14\|F\|^4.}
\tag{L-102501.5}
\]

This is a uniform strict determinant reserve. It is not obtained by spending
one positive diagonal reserve twice.

## 4. Why covariance is necessary

The ordinary phase derivative has eigenvalue `log(n)`, which is unbounded and
contains the deterministic carrier. The covariant coordinate `Q=u-Lambda`
replaces it by the bounded relative activation coordinate. This is the correct
source-level scale–phase tensor for the programme.
