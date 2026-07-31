# L-18501 — Exact right-inverse gap for selected-zero counts

Claim ID: `L-18501`  
Title: An exact evaluation right inverse bounds every non-kernel generalized eigenvalue from below  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-m`  
Created: 2026-07-31  
Dependencies: finite-dimensional min--max; exact selected-zero evaluation maps; positive metric Gram  
Scope: the generalized count requested in Issue #185

## 1. Abstract setting

Let `U` be a finite-dimensional real or complex Hilbert space. Let

\[
G\succ0
\]

be a declared metric form. Let

\[
V:U\longrightarrow\mathbb C^m
\]

be surjective, and let

\[
C:\mathbb C^m\longrightarrow U,
\qquad VC=I_m,
\tag{L-18501.1}
\]

be any exact right inverse. Put

\[
R=\ker V,
\qquad d=\dim R=\dim U-m,
\tag{L-18501.2}
\]

and define the selected-coordinate Gram

\[
K_Z=V^*V.
\tag{L-18501.3}
\]

Let

\[
\Lambda\ge\lambda_{\max}(C^*GC).
\tag{L-18501.4}
\]

The supplied right inverse need not be metric-orthogonal to `R`; arbitrary
kernel components only make `Lambda` a looser, still valid bound.

## 2. Right-inverse spectral-gap theorem

On the metric orthogonal complement

\[
R^{\perp_G}
\]

one has

\[
\boxed{
K_Z\succeq\Lambda^{-1}G.
}
\tag{L-18501.5}
\]

Equivalently, if

\[
A_Z=G^{-1/2}K_ZG^{-1/2},
\tag{L-18501.6}
\]

then `A_Z` has exactly `d` zero eigenvalues and every other eigenvalue is at
least `1/Lambda`.

Consequently, for every

\[
0<\tau<\Lambda^{-1},
\tag{L-18501.7}
\]

\[
\boxed{
N_{A_Z}(\tau)=d,
}
\tag{L-18501.8}
\]

where `N_A(tau)` counts eigenvalues strictly below `tau`, with multiplicity.

### Proof

Let `P_R^G` be the `G`-orthogonal projection onto `R` and put

\[
C_0=(I-P_R^G)C.
\tag{L-18501.9}
\]

Since `V` vanishes on `R`,

\[
VC_0=VC=I_m.
\tag{L-18501.10}
\]

Metric projection is contractive, hence

\[
C_0^*GC_0\preceq C^*GC\preceq\Lambda I_m.
\tag{L-18501.11}
\]

The map `V` restricts to an isomorphism

\[
V:R^{\perp_G}\longrightarrow\mathbb C^m.
\]

Indeed it is injective because its kernel intersects `R^(perp_G)` trivially,
and the dimensions agree. Its inverse is exactly `C_0`: for
`u in R^(perp_G)`, the vector `u-C_0Vu` lies both in `R` and in
`R^(perp_G)`, hence vanishes.

Thus every `u in R^(perp_G)` has the form `u=C_0a`, where `a=Vu`, and

\[
\begin{aligned}
\langle Gu,u\rangle
&=\langle C_0^*GC_0a,a\rangle\\
&\le\Lambda\|a\|_2^2
 =\Lambda\|Vu\|_2^2
 =\Lambda\langle K_Zu,u\rangle.
\end{aligned}
\]

This proves (L-18501.5). On `R`, `K_Z` is identically zero, including all cross
terms. The generalized spectral statement and (L-18501.8) follow. QED.

## 3. Domination by a larger certified-zero block

Let `K_T` be any positive form satisfying

\[
\boxed{K_T\succeq K_Z.}
\tag{L-18501.12}
\]

For the zeta application, `K_T` may be the complete Gram of every certified
critical-line zero through height `T`, with multiplicities, while `K_Z` uses
only a selected subset with unit weights.

Min--max gives

\[
\boxed{
N_{G^{-1/2}K_TG^{-1/2}}(\tau)
\le d
\qquad(0<\tau<\Lambda^{-1}).
}
\tag{L-18501.13}
\]

Adding more certified positive zero coordinates can only raise generalized
eigenvalues; it can never create an additional low evaluation direction.

## 4. Direct Schur-floor corollary

Suppose a Hermitian finite form `S` satisfies the certified-zero lower bound

\[
S\succeq K_T-B_TG,
\qquad B_T\ge0.
\tag{L-18501.14}
\]

If `beta>0` and

\[
\boxed{
B_T+\beta<\Lambda^{-1},
}
\tag{L-18501.15}
\]

then, on `R^(perp_G)`,

\[
\boxed{
S\succeq\beta G.
}
\tag{L-18501.16}
\]

Indeed `K_T>=K_Z>=Lambda^-1 G` there. Thus the count inequality and the positive
visible floor are two consequences of the same right-inverse gap.

## 5. Weighted selected coordinates

If the selected certified zeros carry a positive diagonal multiplicity matrix
`W>=mu I`, replace `K_Z` by

\[
K_Z^{(W)}=V^*WV.
\]

Then every occurrence of `Lambda^-1` above improves to `mu Lambda^-1`.
For actual zero multiplicities, `mu>=1`, so the unit-weight theorem is always a
safe lower bound.

## 6. Proof-producing data

A finite rational or directed certificate needs only:

1. a positive metric Gram `G`;
2. an exact selected evaluation matrix `V`;
3. an exact right inverse `C` with `VC=I`;
4. a basis of `ker V` and an exact rank check;
5. a rational `Lambda` with `C_0^*GC_0<=Lambda I`, where `C_0` is the
   metric-orthogonalized right inverse;
6. a Loewner certificate `K_T>=V^*V`;
7. the strict rational comparison `(B_T+beta)Lambda<1`.

No numerical eigensolver is required.

## 7. Proof boundary

- The finite theorem is exact linear algebra.
- Selected zero ordinates, multiplicities, evaluation normalization, the full
  certified-zero Gram, and the high-zero tail budget are external source gates.
- The theorem proves the requested count on any packet carrying an exact selected
  evaluation right inverse.
- It does not show that this packet is the complete dangerous low-spectral
  hierarchy. That capture question remains separate and is classified by
  `T-14307`.
