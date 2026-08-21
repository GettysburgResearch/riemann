# L-19831 — Relative local Weyl forces source injectivity and quantitative conditioning

Claim ID: `L-19831`  
Status: **PROVED FINITE OPERATOR NECESSITY THEOREM**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: exact source-to-finite congruence; positive tail Gram  
Scope: adversarial dependency correction between review items 1 and 4

## 1. Purpose

The independent review listed as separate obligations:

1. a quantitative complete source frame;
2. a relative operator local-Weyl theorem.

They are not independent. If the finite localized Weil matrix is the pullback of
the finite CCM matrix through the projected source map, then a relative
local-Weyl lower bound on a positive tail Gram automatically forces the source
map to be injective. It also gives a quantitative lower singular-value bound.

Thus a proof of the fourth theorem on the complete packet already proves the
qualitative part of the first. Conversely, an exact source-kernel direction is
an immediate counterexample to the fourth theorem.

## 2. Exact setup

Let

\[
 T:S\longrightarrow V
 \tag{L-19831.1}
\]

be the projected finite source map. Let `H_V` and `H_S` be positive metrics. Let
`A_V` be the exact finite localized Weil matrix on `V` and put

\[
 A_S=T^*A_VT.
 \tag{L-19831.2}
\]

Let

\[
 D_S\succ0
 \tag{L-19831.3}
\]

be the ordinary omitted-tail Gram on the declared source packet.

Assume that for some `a>0` and `0<=eta<1`,

\[
 \boxed{
 \left\|
 D_S^{-1/2}(A_S-aD_S)D_S^{-1/2}
 \right\|\le\eta a.}
 \tag{L-19831.4}
\]

Equivalently,

\[
 (1-\eta)aD_S
 \preceq A_S
 \preceq(1+\eta)aD_S.
 \tag{L-19831.5}
\]

## 3. Injectivity is automatic

If `x in ker T`, then (L-19831.2) gives

\[
 A_S[x]=0.
\]

But (L-19831.5) gives

\[
 0=A_S[x]
 \ge(1-\eta)aD_S[x].
\]

Since `D_S` is positive definite, `x=0`. Therefore

\[
 \boxed{\ker T=\{0\}.}
 \tag{L-19831.6}
\]

When `dim S=dim V`, the complete projected source map is bijective. No separate
generic-determinant theorem is needed once the relative local-Weyl estimate has
been proved on the complete packet.

## 4. Quantitative singular-value consequence

Assume

\[
 D_S\succeq d_{\min}H_S
 \tag{L-19831.7}
\]

and

\[
 A_V\preceq M_AH_V
 \tag{L-19831.8}
\]

in operator order. Then for every `x in S`,

\[
\begin{aligned}
 M_A\|Tx\|_{H_V}^2
 &\ge A_V[Tx]\\
 &=A_S[x]\\
 &\ge(1-\eta)a d_{\min}\|x\|_{H_S}^2.
\end{aligned}
\]

Hence

\[
 \boxed{
 \sigma_{\min}(T;H_S,H_V)
 \ge
 \sqrt{{(1-\eta)a d_{\min}\over M_A}}.}
 \tag{L-19831.9}
\]

This floor is typically superexponentially smaller than a power of
`1/log lambda`, because `d_min` is a prolate leakage scale. It is nevertheless
the exact conditioning forced by local Weyl.

## 5. Near-kernel supports are exactly local-Weyl bad supports

For a unit source vector `x`,

\[
 A_S[x]\le M_A\|Tx\|_{H_V}^2.
\]

Therefore

\[
 {A_S[x]\over D_S[x]}
 \le {M_A\|Tx\|_{H_V}^2\over D_S[x]}.
 \tag{L-19831.10}
\]

If the projected source map has a near-kernel direction with

\[
 \|Tx\|_{H_V}^2=o(aD_S[x]),
\]

then the relative local-Weyl estimate fails in that direction. Thus supports
near a zeta cycle or a source-frame degeneracy cannot be removed from the proof
merely by declaring the source range qualitatively onto; they must appear in
the bad-support ledger of the support-average theorem.

## 6. Consequence for the four-theorem frontier

The corrected dependency graph is

```text
complete branch/alias estimates
       |
       v
relative local-Weyl on a positive tail Gram
       |
       +--> complete source injectivity and a quantitative floor
       |
       v
signed d4/d6 finite ground transfer.
```

Therefore:

- the review was correct that qualitative density alone is insufficient;
- the requested fixed polylogarithmic singular-value theorem is false by
  `R-19806`;
- a complete proof of the relative local-Weyl theorem automatically supplies
  the source injectivity actually needed;
- items 1 and 4 must not be counted as independent solved gates.

## 7. Audit implication for `L-19828`

Any proof of `L-19828` must exhibit its good-support set before assuming a
complete source inverse. At those good supports, `L-19831` then derives
injectivity. If a step of the proof of `L-19828` uses source injectivity or a
right inverse to establish its own oscillatory estimates, that step is circular.

The branchwise proof in `L-19827/L-19829` is formulated entirely in source-tail
coordinates and does not invoke a source inverse. The final support selection in
`L-19828` is therefore the point at which injectivity is earned rather than
assumed.

## 8. Proof boundary

This is exact finite linear algebra. It does not prove that the good-support set
of `L-19828` is nonempty; it proves what follows if the declared relative
local-Weyl estimate holds there. No RH conclusion follows from this lemma alone.
