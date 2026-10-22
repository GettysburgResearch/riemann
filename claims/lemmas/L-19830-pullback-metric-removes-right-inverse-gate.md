# L-19830 — Pullback min--max removes the quantitative right-inverse gate

Claim ID: `L-19830`  
Status: **PROVED FINITE OPERATOR THEOREM; QUALITATIVE COMPLETE SOURCE SUBSPACE STILL REQUIRED**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: qualitative finite surjectivity `L-16211`; signed source hierarchy `L-19823/L-19826`; Rayleigh transfer `T-15103`  
Scope: corrected replacement for the false complete singular-value theorem

## 1. Purpose

The rejected review frontier asked for a lower singular-value bound on the source
map. That is stronger than the finite ground-state argument needs.

Let

\[
 T_R:S_R\longrightarrow V_R
 \tag{L-19830.1}
\]

be any **bijective** finite source realization of the complete CCM space. Instead
of comparing source coordinates with the output metric through
`||T_R^-1||`, pull the physical metric back:

\[
 G_R=T_R^*H_RT_R,
 \tag{L-19830.2}
\]

where `H_R` is the ordinary finite CCM metric. Congruence by `T_R` identifies
all generalized eigenvalues exactly. A small singular value of `T_R` makes
`G_R` small in that source direction; it does not create a small generalized
energy. Only an **upper** bound for `T_R` enters the min--max lower estimate.

This lemma formalizes that observation.

## 2. Abstract min--max theorem

Let `S` and `V` have equal finite dimension, let

\[
 T:S\to V
\]

be invertible, and let `H_V` and `H_S` be positive metrics. Put

\[
 G=T^*H_VT.
 \tag{L-19830.3}
\]

Let `D` be a positive source form and assume

\[
 \lambda_1(D,H_S)\le C_4d_4,
 \qquad
 \lambda_2(D,H_S)\ge c_6d_6.
 \tag{L-19830.4}
\]

Suppose

\[
 \boxed{G\preceq K H_S.}
 \tag{L-19830.5}
\]

Then min--max gives

\[
 \boxed{
 \lambda_2(D,G)
 \ge {c_6d_6\over K}.}
 \tag{L-19830.6}
\]

Indeed, for every two-dimensional subspace `W`,

\[
 \sup_{0\ne x\in W}{D[x]\over G[x]}
 \ge {1\over K}
 \sup_{0\ne x\in W}{D[x]\over H_S[x]},
\]

and taking the min over `W` proves (L-19830.6).

Let `p` be an `H_S`-normalized target satisfying

\[
 D[p]\le C_4d_4,
 \qquad
 G[p]\ge c_p>0.
 \tag{L-19830.7}
\]

Then its generalized Rayleigh value obeys

\[
 \boxed{
 \mu_D={D[p]\over G[p]}
 \le {C_4\over c_p}d_4.}
 \tag{L-19830.8}
\]

Consequently, if

\[
 \boxed{K{d_4\over d_6}\longrightarrow0,}
 \tag{L-19830.9}
\]

the target lies below the second generalized eigenvalue by a relative factor
tending to zero. No lower singular value of `T` occurs.

## 3. Arithmetic-tail version

Let the complete arithmetic tail form `D_ar` satisfy the transfer inequalities
of `L-19826`:

\[
 (1-\epsilon_R)D
 \preceq D_{\rm ar}
 \preceq(1+\epsilon_R+B_R)D,
 \tag{L-19830.10}
\]

with `epsilon_R->0`. Then

\[
 \lambda_2(D_{\rm ar},G)
 \ge{(1-\epsilon_R)c_6d_6\over K},
 \tag{L-19830.11}
\]

and

\[
 \mu_{D_{\rm ar}}
 \le{(1+\epsilon_R+B_R)C_4d_4\over c_p}.
 \tag{L-19830.12}
\]

Thus the exact condition is

\[
 \boxed{
 K(1+B_R){d_4\over d_6}\longrightarrow0.}
 \tag{L-19830.13}
\]

A polylogarithmic alias upper budget leaves a very large reserve.

## 4. Exact congruence with the finite CCM problem

Let `A_V` be the exact finite localized Weil matrix on `V`. Pull it back to

\[
 A_S=T^*A_VT.
 \tag{L-19830.14}
\]

Then

\[
 \lambda_j(A_V,H_V)=\lambda_j(A_S,G)
 \tag{L-19830.15}
\]

for every `j`, including multiplicity. The finite ground vector in `V` is the
image under `T` of the generalized ground vector in `(S,G)`. Therefore use of
the pullback metric changes no finite CCM eigenstate and no finite real-zero
conclusion.

If `L-19828` gives

\[
 A_S=(\log R)D_{\rm ar}+E_R,
 \qquad
 \|D_{\rm ar}^{-1/2}E_RD_{\rm ar}^{-1/2}\|
 =o(\log R),
 \tag{L-19830.16}
\]

the same target/second-eigenvalue comparison transfers to the exact finite
matrix.

## 5. Upper bound for the projected source map

The upper bound (L-19830.5) is elementary on the quadratic-log packet. Put

\[
 L=2\log\lambda,
 \qquad
 t_k={2\pi k\over L},
 \qquad
 |k|\le N=O(L^2).
\]

For an exact source `f` with `f(0)=0`, split its Mellin transform:

\[
 |M_f(t)|
 \le\int_0^1|f(x)|x^{-1/2}dx
    +\int_1^\lambda|f(x)|x^{-1/2}dx.
 \tag{L-19830.17}
\]

The first term is at most `||f'||_(L2(0,1))` because

\[
 |f(x)|\le x^{1/2}\|f'\|_{L^2(0,1)}.
\]

The second is at most

\[
 (\log\lambda)^{1/2}\|f\|_2.
\]

On the polylogarithmic prolate/Hermite mode window, the oscillator energy bound
gives

\[
 \|f'\|_2\le C(\log R)^C\|f\|_2.
 \tag{L-19830.18}
\]

Hence

\[
 \boxed{
 |M_f(t_k)|
 \le C(\log R)^C\|f\|_2.}
 \tag{L-19830.19}
\]

The exact Fourier factorization `L-19825` and a standard polynomial upper bound
for zeta on `|t|=O(log R)` give

\[
 \boxed{
 \|T_Rf\|_{H_V}^2
 \le C(\log R)^C\|f\|_2^2.}
 \tag{L-19830.20}
\]

Thus one may take

\[
 K_R=(\log R)^C
 \tag{L-19830.21}
\]

for the ordinary metric.

For the moving-Hardy metric with `tau_R<1/2`, support in
`[lambda^-1,lambda]` gives

\[
 M_R\preceq2\lambda^{2\tau_R}H_V.
\]

Therefore

\[
 \boxed{
 K_R^{\rm Hardy}
 \le C R^{\tau_R}(\log R)^C
 \le C R^{1/2}(\log R)^C.}
 \tag{L-19830.22}
\]

Since the signed fixed-mode hierarchy has

\[
 {d_4\over d_6}=\Theta(R^{-2}),
\]

both (L-19830.21) and (L-19830.22) satisfy

\[
 K_R^{\rm Hardy}(1+B_R){d_4\over d_6}	o0
 \tag{L-19830.23}
\]

for every polylogarithmic `B_R`.

## 6. What remains of the source theorem

The quantitative lower singular-value theorem is neither true nor needed. The
source obligation is reduced to the qualitative statement:

```text
choose, at one nonexceptional support in each large block, a finite exact
source subspace S_R carrying the signed d4,d6 tail hierarchy such that
T_R:S_R->V_R is bijective.
```

Once such a subspace is present, all metric losses required by the finite
Rayleigh/Hurwitz transfer are controlled by the upper estimate proved here.
Near-zeta-cycle ill-conditioning is harmless in the pullback metric.

`L-16211` proves surjectivity of the **full** exact source range. It does not by
itself prove that the particular complete prolate packet is bijective. That is
now the sole source-frame question; no quantitative right inverse remains.

## 7. Proof boundary

- The pullback min--max theorem, congruence, and upper source-map estimates are
  proved.
- The theorem explicitly does not infer bijectivity of the complete prolate
  packet from density of the full source range.
- A mixed or adaptive exact source subspace is allowed, provided the signed tail
  hierarchy and branch theorem are proved on it.
- No RH conclusion follows until that qualitative source-subspace construction
  is supplied.
