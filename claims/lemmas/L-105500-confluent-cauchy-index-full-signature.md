# L-105500 — Confluent Cauchy-index full signature

Claim ID: `L-105500`  
Status: **PROVED EXACT AT REGULAR FINITE-WINDOW SCOPE**  
Created: 2026-08-24  
Depends on: `L-105303`, `L-105310`; elementary Cauchy-index reciprocity  
RH status: **not assumed**

## 1. Setup and reduced critical quotient

Let `F` be holomorphic in a neighbourhood of a bounded
conjugation-invariant rectangle `Omega`, real on

\[
I=(a,b)=\Omega\cap\mathbb R.
\]

Assume

\[
F(a)F'(a)F(b)F'(b)\ne0
\]

and that the boundary of `Omega` contains no pole of the meromorphic quotient

\[
R(z)=\frac{F(z)}{F'(z)}.
\tag{L-105500.1}
\]

No coprimality or simplicity assumption is imposed.  At a zero of `F` of
multiplicity `mu`, the common factor in `F'` cancels and

\[
R(z)=\frac{z-c}{\mu}+O((z-c)^2).
\tag{L-105500.2}
\]

Thus the poles of `R` are exactly the non-root critical points, with their
literal pole orders.  Let

\[
M=\sum_{c\in\Omega}\operatorname{ord}_c^-(R)
\tag{L-105500.3}
\]

be the total pole-order dimension.

For a source-fixed finite family of holomorphic real-symmetric observations
`phi_1,...,phi_d`, define

\[
C_{ij}=-\frac1{2\pi i}
\int_{\partial\Omega}R(z)\phi_i(z)\phi_j(z)\,dz.
\tag{L-105500.4}
\]

The complete pole-jet observation map identifies `C` as a congruence of a
nondegenerate `M`-dimensional Hermite residue form `H_Omega`.

## 2. Exact local signatures

At a real pole `c` of order `m`, write

\[
R(z)=\sum_{r=1}^{m}a_{c,r}(z-c)^{-r}+O(1),
\qquad a_{c,m}\ne0.
\]

In the normalized pole-jet basis, the local block is the anti-triangular
Hankel matrix from `L-105310`.  Symmetric elimination is a congruence and gives

\[
H_c\sim -a_{c,m}J_m,
\tag{L-105500.5}
\]

where `J_m` is the reversal matrix.  Consequently

\[
\operatorname{sig}H_c=
\begin{cases}
-\operatorname{sgn}(a_{c,m}),&m\text{ odd},\\
0,&m\text{ even}.
\end{cases}
\tag{L-105500.6}
\]

A nonreal pole and its conjugate, each of order `m`, give a block

\[
\begin{pmatrix}0&B\\B^*&0\end{pmatrix}
\tag{L-105500.7}
\]

with `B` anti-triangular and invertible.  It has exactly `m` positive and `m`
negative eigenvalues, hence zero signature.

Define the real Cauchy index so that a jump from `-infinity` on the left to
`+infinity` on the right has index `+1`.  Then a real pole with leading term
`a_m(x-c)^(-m)` has local index `sgn(a_m)` for odd `m` and zero for even `m`.
Equations (L-105500.6)--(L-105500.7) therefore give the exact identity

\[
\boxed{
\operatorname{sig}H_\Omega=-\operatorname{Ind}_{a}^{b}(F/F').
}
\tag{L-105500.8}
\]

This is the point at which every nonreal and every even confluent block
cancels automatically.  No positive-index nuisance charge is paid.

## 3. Reciprocal Cauchy-index identity

For a regular real point `x`, put

\[
V_x(F,F')=
\begin{cases}
1,&F(x)F'(x)<0,\\
0,&F(x)F'(x)>0.
\end{cases}
\tag{L-105500.9}
\]

Partition `(a,b)` at the zeros of `F F'`.  At a distinct real zero `r` of `F`
of arbitrary multiplicity `mu`,

\[
\frac{F'}F(x)=\frac{\mu}{x-r}+O(1),
\]

so its local Cauchy index is `+1`; moreover `V` drops from one to zero.
At a zero of `F'` which is not a zero of `F`, the local change of `V` is
exactly the local Cauchy index of `F/F'`.  Summing the local changes yields

\[
\boxed{
\operatorname{Ind}_{a}^{b}(F'/F)
+
\operatorname{Ind}_{a}^{b}(F/F')
=V_a(F,F')-V_b(F,F').
}
\tag{L-105500.10}
\]

Every distinct real zero of `F` contributes one to the first index, regardless
of multiplicity.  If `Z_dist(F;I)` denotes their number, then

\[
\operatorname{Ind}_{a}^{b}(F'/F)=Z_{\rm dist}(F;I).
\tag{L-105500.11}
\]

Combining (L-105500.8)--(L-105500.11) gives the exact confluent reverse-Rolle
formula

\[
\boxed{
Z_{\rm dist}(F;I)
=
\operatorname{sig}H_\Omega
+V_a(F,F')-V_b(F,F').
}
\tag{L-105500.12}
\]

The endpoint correction belongs to `{-1,0,1}` and is retained literally.

## 4. Compression inequality without a nuisance penalty

Because `H_Omega` is nondegenerate of dimension `M`,

\[
\operatorname{sig}H_\Omega=2\nu_+(H_\Omega)-M.
\tag{L-105500.13}
\]

Congruence cannot increase positive index, while the Hermitian rank--trace
inequality gives

\[
\nu_+(H_\Omega)\ge\nu_+(C)
\ge
\frac{(\operatorname{tr}C)_+^2}{\|C\|_{\rm HS}^2}.
\tag{L-105500.14}
\]

Hence

\[
\boxed{
Z_{\rm dist}(F;I)
\ge
2\frac{(\operatorname{tr}C)_+^2}{\|C\|_{\rm HS}^2}
-M+V_a(F,F')-V_b(F,F').
}
\tag{L-105500.15}
\]

In particular the right side may be weakened by only one, not by a positive
density of multiplicity or nonreal blocks.

## 5. Xi consequence

Take `F=Xi` in a regular dyadic window and let `N_1(T,2T)` count all zeros of
`Xi'` in the corresponding rectangle with multiplicity.  Common `Xi/Xi'`
factors are already cancelled in (L-105500.1), so

\[
M_T\le N_1(T,2T).
\tag{L-105500.16}
\]

If a source-owned compression satisfies

\[
\eta_T=
\frac{(\operatorname{tr}C_T)_+^2}
{N_1(T,2T)\|C_T\|_{\rm HS}^2},
\tag{L-105500.17}
\]

then (L-105500.15), the standard adjacent zero-count asymptotic
`N_1(T,2T)/N(T,2T)->1`, and the fact that distinct real Xi zeros are a subset
of critical-line zeros counted with multiplicity give

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
\ge 2\liminf_{T\to\infty}\eta_T-1.
}
\tag{L-105500.18}
\]

This removes both the `821/5000` nuisance subtraction and the separate
common-zero/simple-window hypothesis from the conclusion-facing inequality.
It does not estimate the Xi contour matrix.

## 6. Scope

The local block algebra, Cauchy-index identity, endpoint ledger, and
compression inequality are exact.  The passage to an asymptotic Xi proportion
still requires a source-owned family with the stated trace and
Hilbert--Schmidt estimates and `o(N_1)` contour/transfer errors.
