# O-32401 — Literature position of the dyadic prime Riesz criterion

Claim ID: `O-32401`  
Title: The fixed-dyadic criterion `T-32404` lies strictly between Suzuki's weighted Chebyshev sign criterion and his stronger full-monotonicity condition  
Status: **LITERATURE / EXACT ALGEBRAIC ADAPTER**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Primary literature: Masatoshi Suzuki, *On variants of Chebyshev's conjecture*, The Ramanujan Journal 68 (2025), article 95; correction published 2025-12-19  
Scope: prior-art positioning; no new RH claim

## 1. Common weighted prime Riesz mean

Put

\[
 P_\Lambda(X)
 =\sum_{n\le X}{\Lambda(n)\over\sqrt n}\log{X\over n},
 \qquad
 F(X)={P_\Lambda(X)\over\sqrt X}.
\tag{O-32401.1}
\]

Suzuki's Theorem 1 proves the equivalence

\[
\mathrm{RH}
\iff
P_\Lambda(X)-4\sqrt X\le0
\quad\text{eventually}.
\tag{O-32401.2}
\]

The same paper gives under RH the explicit formula

\[
P_\Lambda(X)-4\sqrt X
=-{\zeta'\over\zeta}(1/2)\log X
-\sum_\rho {X^{\rho-1/2}\over(\rho-1/2)^2}
+O(1),
\tag{O-32401.3}
\]

with the zero sum bounded under RH because the denominator is quadratic.

Thus the source and the smoothing order in `T-32404` are classical/known; the new coordinate there is the fixed-dilation pole cancellation.

## 2. The new fixed-dyadic condition

`T-32404` uses

\[
D_\Lambda(X)
=P_\Lambda(X)-\sqrt2P_\Lambda(X/2).
\]

Dividing by `sqrt X`,

\[
\boxed{
{D_\Lambda(X)\over\sqrt X}
=F(X)-F(X/2).
}
\tag{O-32401.4}
\]

Hence its eventual positivity is exactly eventual monotonicity of the normalized Riesz mean along the one fixed dyadic step

\[
X/2\longrightarrow X.
\]

Suzuki's explicit formula (O-32401.3) immediately gives under RH

\[
D_\Lambda(X)
=(\sqrt2-1){\zeta'\over\zeta}(1/2)\log X+O(1),
\]

which agrees with the independent Mellin proof in `T-32404`.

## 3. Suzuki's stronger monotonicity condition

Let

\[
 A(X)=\sum_{n\le X}{\Lambda(n)\over\sqrt n}.
\]

Away from prime-power knots,

\[
 {d\over d\log X}F(X)
 ={2A(X)-P_\Lambda(X)\over2\sqrt X}.
\tag{O-32401.5}
\]

Suzuki's Theorem 2 assumes, after writing his endpoint as `X=xe^2`,

\[
\sum_{n\le X}{\Lambda(n)\over\sqrt n}
[\log(X/n)-2]\le0.
\]

This is exactly

\[
P_\Lambda(X)-2A(X)\le0,
\]

or

\[
\boxed{F'(X)\ge0}
\tag{O-32401.6}
\]

in logarithmic scale. Thus that theorem asks for eventual **full monotonicity** of `F`, not merely one fixed-ratio increment.

The paper explicitly notes that the corresponding limiting assertion requires RH plus an additional zero-sum estimate; it is stronger than RH in that form.

## 4. Exact hierarchy of conditions

The three conditions may therefore be read as

```text
Suzuki Theorem 1:
    F(X) <= 4 eventually
    <=> RH;

T-32404:
    F(X) > F(X/2) eventually
    <=> RH;

Suzuki Theorem 2 hypothesis:
    F is eventually increasing at every infinitesimal scale
    => RH.
```

The dyadic theorem is not a replacement for Suzuki's work; it is a fixed-dilation adapter which cancels the real pole multiplicatively and retains only a bounded critical-line oscillation under RH.

## 5. Research consequence

The literature comparison suggests two proof-facing attacks on `T-32404`:

1. prove only one-scale dyadic monotonicity, avoiding the stronger derivative sign in Suzuki's Theorem 2;
2. exploit the exact coefficient source
   \[
   (\varepsilon-2\delta_2)*\Lambda,
   \]
   whose split image is the dyadic factorial/entropy defect, rather than estimate `P_Lambda` and `A` separately.

Any argument which accidentally proves full monotonicity should be recognized as attacking a condition stronger than the new fixed-dyadic target.
