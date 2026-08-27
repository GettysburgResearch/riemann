# L-105400 — Finitely many signed tail moments control the complete fixed-order matrix error

Claim ID: `L-105400`  
Status: **PROVED EXACT FINITE-DIMENSIONAL PERTURBATION THEOREM**  
Created: 2026-08-23  
Depends on: `L-105370`, `L-105390`  
RH status: **not assumed**

## 1. Moment matrices of a signed measure

Let `sigma` be a finite signed Borel measure on `[0,infinity)` with moments
through order `2k-1`. Put

\[
v_k(s)=(1,s,\ldots,s^{k-1})^T
\]

and, for `a in {0,1}`, define

\[
\boxed{
\mathsf M_{k}^{(a)}(\sigma)
=
\int_{[0,\infty)}
 s^a v_k(s)v_k(s)^T\,d\sigma(s).
}
\tag{L-105400.1}
\]

Its entries are

\[
\boxed{
\left(\mathsf M_k^{(a)}(\sigma)\right)_{ij}
=
\Delta_{i+j+a}(\sigma),
\qquad
\Delta_n(\sigma)=\int s^n\,d\sigma(s).
}
\tag{L-105400.2}
\]

## 2. Finite-moment operator bound

Let

\[
D_{k,a}(\sigma)
=
\max_{0\le n\le2k-2+a}
|\Delta_n(\sigma)|.
\tag{L-105400.3}
\]

Every row of `M_k^(a)(sigma)` has absolute row sum at most `k D_(k,a)`. Hence

\[
\boxed{
\left\|
\mathsf M_k^{(a)}(\sigma)
\right\|_{\rm op}
\le
kD_{k,a}(\sigma).
}
\tag{L-105400.4}
\]

Equivalently, at order `k` the complete ordinary and shifted matrix errors use
only the scalar moments

\[
\Delta_0,\ldots,\Delta_{2k-1}.
\]

No control of higher moments is required.

## 3. Weighted total variation bound

The Rayleigh quotient also gives

\[
\begin{aligned}
|x^T\mathsf M_k^{(a)}(\sigma)x|
&\le
\int s^a|x^Tv_k(s)|^2\,d|\sigma|(s)\\
&\le
\|x\|_2^2
\int s^a\|v_k(s)\|_2^2\,d|\sigma|(s).
\end{aligned}
\]

Therefore

\[
\boxed{
\left\|
\mathsf M_k^{(a)}(\sigma)
\right\|_{\rm op}
\le
\int s^a
\left(1+s^2+\cdots+s^{2k-2}\right)
\,d|\sigma|(s).
}
\tag{L-105400.5}
\]

If the support lies in `[0,1]`, this is at most

\[
k\,|\sigma|([0,1]).
\tag{L-105400.6}
\]

For a remote reciprocal-square tail, the support is eventually contained in a
small interval near zero, so weighted total variation is a convenient strong
sufficient coordinate.

## 4. Perturbation of a positive reserve

Let `R` be a real symmetric matrix with

\[
R\succeq\eta I_k,
\qquad \eta>0,
\]

and let `E` be symmetric. If

\[
\|E\|_{\rm op}<\eta,
\]

then

\[
\boxed{R+E\succ0.}
\tag{L-105400.7}
\]

Combining this elementary Weyl bound with (L-105400.4), it is enough that

\[
\boxed{
kD_{k,a}(\sigma)<\eta}
\tag{L-105400.8}
\]

for the signed tail perturbation not to destroy the reserve.

## 5. Scope

The theorem is finite-dimensional linear algebra. It supplies no Xi tail
moment estimate and no positivity of the signed measure. Moment closeness is a
sufficient perturbative coordinate; it is not necessary for matrix
domination. RH is not involved.
