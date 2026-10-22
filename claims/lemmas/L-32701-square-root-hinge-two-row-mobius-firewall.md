# L-32701 — Square-root hinge inverse: two explicit Möbius rows form a zero-safe firewall

Claim ID: `L-32701`  
Title: The first two nontrivial rows of the exact carry inverse for the square-root hinge have explicit finite-filter-over-zeta transforms with no common right-half-plane zero  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Scope: exact finite carry inversion and Mellin source identification; no sign theorem and no RH claim

## 1. The hinge target

Fix an integer endpoint `T>=3` and define

\[
h_T(q)=q^{-1/2}-T^{-1/2},\qquad 2\le q\le T.
\tag{L-32701.1}
\]

Let `c_T(j)` be the unique triangular inverse of the average carry matrix

\[
h_T(q)=\sum_{j=q}^T c_T(j)\,\beta_{jq}.
\tag{L-32701.2}
\]

The target is the square-root hinge appearing in the positive hinge decomposition of the critical logarithmic target on PR #295.

## 2. Exact multiple-Möbius inversion

For a general target `w`, put

\[
u_m=\sum_{k\le T/m}\mu(k)w(mk).
\tag{L-32701.3}
\]

The carry inverse formula gives exactly

\[
\boxed{
 c_T(j)=
 \frac{(j+1)[j u_j-(j-2)u_{j+1}]
      +2\sum_{m=j+2}^T u_m}
      {j(j-1)}.}
\tag{L-32701.4}
\]

Swapping the finite sums, for every column `q>=2` the coefficient of `w(q)` is

\[
K_j(q)=\frac{1}{j(j-1)}\left[
 j(j+1)\mathbf1_{j\mid q}\mu(q/j)
 -(j+1)(j-2)\mathbf1_{j+1\mid q}\mu(q/(j+1))
 +2\!\sum_{\substack{m\mid q\\m\ge j+2}}\mu(q/m)
\right].
\tag{L-32701.5}
\]

Since `sum_(m|q) mu(q/m)=0` for `q>=2`, this is a finite Dirichlet-convolution filter.

Define `f_j` on `1,...,j+1` by

\[
f_j(d)=
\begin{cases}
-2,&1\le d\le j-1,\\
(j+2)(j-1),&d=j,\\
-j(j-1),&d=j+1.
\end{cases}
\tag{L-32701.6}
\]

Then

\[
\boxed{K_j(q)=\frac{(f_j*\mu)(q)}{j(j-1)}\qquad(q\ge2).}
\tag{L-32701.7}
\]

The value at `q=1` is deliberately excluded: the original carry system begins at column two.

## 3. The rows `j=2,3`

For `j=2`,

\[
\boxed{K_2=-\mu+2\,\delta_2*\mu-\delta_3*\mu\quad(q\ge2).}
\tag{L-32701.8}
\]

For `j=3`,

\[
\boxed{K_3=\frac{-2\mu-2\delta_2*\mu+10\delta_3*\mu-6\delta_4*\mu}{6}
\quad(q\ge2).}
\tag{L-32701.9}
\]

Ignoring the harmless missing `q=1` coefficient, their Dirichlet numerators are

\[
E_2(s)=-2+4\,2^{-s}-2\,3^{-s},
\tag{L-32701.10}
\]

and

\[
E_3(s)=-2-2\,2^{-s}+10\,3^{-s}-6\,4^{-s}.
\tag{L-32701.11}
\]

Thus the non-elementary part of each row transform is `E_j(s)/zeta(s)`.

## 4. Exact no-common-zero theorem

The two numerators have no common zero in `Re(s)>0`.

Indeed, write

\[
x=2^{-s},\qquad y=3^{-s}.
\]

If `E_2(s)=0`, then

\[
y=2x-1.
\tag{L-32701.12}
\]

Substitution into `E_3(s)=0` gives

\[
-2-2x+10(2x-1)-6x^2
=-6(x-1)(x-2)=0.
\tag{L-32701.13}
\]

Hence `x=1` or `x=2`. But `Re(s)>0` implies

\[
|x|=2^{-\Re(s)}<1,
\]

which excludes both possibilities. Therefore

\[
\boxed{E_2(s)E_3(s)\text{ cannot vanish simultaneously in }\Re(s)>0.}
\tag{L-32701.14}
\]

## 5. Mellin transform of the hinge rows

For `Re(z)>1/2`, direct integration gives

\[
\int_q^\infty
(q^{-1/2}-T^{-1/2})T^{-z-1}\,dT
=\frac{q^{-z-1/2}}{2z(z+1/2)}.
\tag{L-32701.15}
\]

Consequently

\[
\int_1^\infty c_T(j)T^{-z-1}\,dT
=\frac{1}{2z(z+1/2)}
\sum_{q\ge2}\frac{K_j(q)}{q^{z+1/2}}.
\tag{L-32701.16}
\]

Writing `s=z+1/2`, the sum is

\[
\frac{E_j(s)}{j(j-1)\zeta(s)}
+\frac{2}{j(j-1)},
\tag{L-32701.17}
\]

where the second term is exactly the correction for deleting column `q=1`. It is elementary and cannot cancel a zeta-zero pole.

Thus a hypothetical zero `rho` of zeta with `Re(rho)>1/2` creates an uncancelled nonreal pole in at least one of the two Mellin transforms `j=2` or `j=3`.

## 6. Two-row one-sign criterion

It follows from the standard Mellin-Landau one-sign theorem that

\[
\boxed{
\begin{gathered}
 c_T(2)\ge0\text{ eventually},\\
 c_T(3)\ge0\text{ eventually}
\end{gathered}
\quad\Longrightarrow\quad RH.}
\tag{L-32701.18}
\]

The same conclusion holds if both rows are eventually of a prescribed one sign after an elementary compact correction.

This is not a proof of the signs. It is an exact firewall: the apparently elementary positivity of only two fixed inverse rows already contains the complete off-line zero obstruction.

## 7. Reconnaissance and scope

Independent finite exploration found both hinge rows nonnegative through endpoints far beyond those used in the earlier carry scans, including tests through `T=10^7`. That is discovery only and is not used in the theorem.

The lemma explains why a proof of full square-root-hinge inverse positivity cannot be obtained from a generic monotonicity argument without solving an RH-strength problem: its first two fixed rows already form a zero-safe reciprocal-zeta detector.

## Proof boundary

Established exactly:

- the inverse-row formula;
- the finite convolution kernels for rows two and three;
- their Dirichlet numerators;
- the no-common-zero theorem;
- the Mellin transforms and two-row RH implication.

Open:

- eventual positivity of either row, let alone both;
- full square-root-hinge carry saturation;
- RH.
