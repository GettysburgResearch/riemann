# L-107300 — Native rectangular shared-fibre panels factor into two one-sided forms

Claim ID: `L-107300`  
Status: **PROVED EXACT FINITE SOURCE THEOREM**  
Created: 2026-08-30  
Depends on: the shared-fibre map and arbitrary-occupancy identity on PR #765  
RH/GRH status: **not assumed**

Fix one shared marked fibre

\[
\iota=(g,\ell,\rho,\sigma,\tau),
\qquad
\ell\ne\rho
\]

with distinct odd prime conductors.  Let \(X\) be a finite left source set and
\(Y\) a finite right source set.  Suppose the literal arithmetic panel is the
full rectangle

\[
\Omega=X\times Y.
\tag{L-107300.1}
\]

Assume the physical residue map has the source-faithful product form

\[
r(i,j)=\bigl(r_R(j),r_L(i)\bigr)
\in\mathcal A_\ell\times\mathcal A_\rho.
\tag{L-107300.2}
\]

This is exactly the form of the marked-place map on PR #765: the
\(\ell\)-coordinate is determined by the right owner/cofactor variables and
the \(\rho\)-coordinate by the left variables.

Let

\[
P_L:\mathbb C^X\to\mathbb C^{\mathcal A_\rho},
\qquad
(P_La)_y=\sum_{r_L(i)=y}a_i,
\]

\[
P_R:\mathbb C^Y\to\mathbb C^{\mathcal A_\ell},
\qquad
(P_Rb)_x=\sum_{r_R(j)=x}b_j.
\tag{L-107300.3}
\]

Let

\[
H_q=I-\frac1qJ,
\qquad
S_{\ell,\rho}=H_\ell\otimes H_\rho,
\qquad
d_{\ell,\rho}
=
\left(1-\frac1\ell\right)
\left(1-\frac1\rho\right).
\tag{L-107300.4}
\]

## 1. Native rank-one coefficient family

Suppose the literal coefficient vector on \(\Omega\) factors as

\[
\boxed{
z_{ij}=\overline{a_i}\,b_j.
}
\tag{L-107300.5}
\]

This is the native form identified in the live owner panels on PR #765; the
entries are constrained, not independent knobs.

Let \(R_\iota\) be residue aggregation on \(\Omega\).  Then

\[
\boxed{
R_\iota z
=
P_Rb\otimes\overline{P_La}
}
\tag{L-107300.6}
\]

up to the harmless ordering convention of the two residue coordinates.
Indeed, in one cell \((x,y)\),

\[
\sum_{\substack{r_R(j)=x\\r_L(i)=y}}
\overline{a_i}b_j
=
\overline{\sum_{r_L(i)=y}a_i}
\left(\sum_{r_R(j)=x}b_j\right).
\]

Moreover,

\[
\boxed{
\sum_{i,j}|z_{ij}|^2
=
\|a\|^2\|b\|^2.
}
\tag{L-107300.7}
\]

## 2. Exact fixed-fibre Wick factorization

The PR #765 arbitrary-occupancy identity is

\[
\mathscr W_\iota(z)
=
(R_\iota z)^*S_{\ell,\rho}(R_\iota z)
-
d_{\ell,\rho}\|z\|^2.
\tag{L-107300.8}
\]

Using (L-107300.6), the tensor-product rule for quadratic forms gives

\[
\boxed{
\begin{aligned}
\mathscr W_\iota(a,b)
={}&
\bigl(a^*P_L^*H_\rho P_La\bigr)
\bigl(b^*P_R^*H_\ell P_Rb\bigr)\\
&-
d_{\ell,\rho}\|a\|^2\|b\|^2.
\end{aligned}
}
\tag{L-107300.9}
\]

Define the one-sided normalized source responses

\[
\lambda_L(a)
=
\frac{a^*P_L^*H_\rho P_La}{\|a\|^2},
\qquad
\lambda_R(b)
=
\frac{b^*P_R^*H_\ell P_Rb}{\|b\|^2}.
\tag{L-107300.10}
\]

For nonzero \(a,b\),

\[
\boxed{
\mathscr W_\iota(a,b)
=
\|a\|^2\|b\|^2
\left(
\lambda_L(a)\lambda_R(b)-d_{\ell,\rho}
\right).
}
\tag{L-107300.11}
\]

Thus the complete native rectangular panel is determined by two one-sided
quadratic responses and two norms.  The faithful-algebra rank tax of the
arbitrary-coefficient theorem is not required for this rank-one native
coefficient class.

## 3. Single-cell specialization

If every left atom and every right atom maps to one common physical cell,
then

\[
a^*P_L^*H_\rho P_La
=
\left(1-\frac1\rho\right)\left|\sum_i a_i\right|^2,
\]

\[
b^*P_R^*H_\ell P_Rb
=
\left(1-\frac1\ell\right)\left|\sum_j b_j\right|^2.
\]

Hence

\[
\boxed{
\mathscr W_\iota(a,b)
=
d_{\ell,\rho}
\left(
\left|\sum_i a_i\right|^2
\left|\sum_j b_j\right|^2
-
\|a\|^2\|b\|^2
\right).
}
\tag{L-107300.12}
\]

This may have either sign.  Support collision alone does not determine the
native value.

## 4. Rectangular completion defect

For a source-authorized subset \(\Omega_0\subsetneq X\times Y\), extend the
coefficient vector by zero to the full rectangle.  Equations
(L-107300.8) and (L-107300.9) remain exact for the extended vector, but the
rank-one identity (L-107300.5) is broken precisely on the omitted pairs.

Writing

\[
z^{\rm full}_{ij}=\overline{a_i}b_j,
\qquad
e=z^{\rm full}-z^{\Omega_0},
\]

gives the exact defect

\[
\boxed{
\mathscr W(z^{\Omega_0})
=
\mathscr W(z^{\rm full})
-2\Re\langle B_\iota z^{\rm full},e\rangle
+\langle B_\iota e,e\rangle.
}
\tag{L-107300.13}
\]

Thus nonrectangular live occupancy is a named signed boundary problem, not an
untyped failure of the factorization.

## Scope

The theorem proves a finite native source compression.  It does not prove
that the complete cofinal source is a disjoint union of rectangles with a
small boundary defect, nor any signed trace estimate or principal binding.
