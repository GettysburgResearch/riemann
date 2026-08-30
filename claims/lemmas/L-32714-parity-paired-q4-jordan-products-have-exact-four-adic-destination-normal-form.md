# L-32714 — Parity-paired Q=4 Jordan products have an exact four-adic destination normal form

Claim ID: `L-32714`  
Title: Splitting the positive finite Q=4 Jordan deformation by two-adic parity removes every odd-valuation product destination; every surviving independent-frequency column is exactly a strict four-adic descendant plus one explicit divisor boundary  
Status: **PROPOSED COMPLETE EXACT SOURCE-TYPING/NORMAL-FORM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-32712`; PR #337 `L-32704`; complete multiplicative twisting  
Scope: finite-deformation product destinations and their carry normal form; quantitative boundary absorption and the global coefficient-one recurrence remain separate

## 1. The parity split

Let

\[
 \chi_2(n)=(-1)^{v_2(n)}.
\]

This is completely multiplicative. Retain the positive Q=4 Jordan coefficients `J_tau(n)` of `L-32712` and define

\[
 J_\tau^+(n)=J_\tau(n),
 \qquad
 J_\tau^-(n)=\chi_2(n)J_\tau(n).
 \tag{L-32714.1}
\]

Equivalently, put

\[
 J_\tau^{\rm ev}={J_\tau^++J_\tau^-\over2},
 \qquad
 J_\tau^{\rm odd}={J_\tau^+-J_\tau^-\over2}.
 \tag{L-32714.2}
\]

The first sequence is supported on even `v_2`; the second is supported on odd `v_2`. Both are coefficientwise nonnegative.

At the local generating-function level, with `b=2^tau`, `x=y^2`, the formulas are

\[
 \boxed{
 \sum_{m\ge0}J_\tau(2^{2m})x^m
 =\frac{(1-bx)(1-4x)}{(1-x)(1-4b^2x)},
 }
 \tag{L-32714.3}
\]

and

\[
 \boxed{
 \sum_{m\ge0}J_\tau(2^{2m+1})x^m
 =\frac{(b-1)(1-4x)}{(1-x)(1-4b^2x)}.
 }
 \tag{L-32714.4}
\]

Their coefficientwise nonnegativity is also immediate from the explicit even/odd coefficient formulas of `L-32712`.

## 2. Orthogonality of the two parity channels

For any two coefficient sequences `f,g`, complete multiplicativity gives

\[
 (\chi_2f)*(\chi_2g)=\chi_2(f*g).
 \tag{L-32714.5}
\]

Hence

\[
 \boxed{
 J_\tau^+*J_\tau^+
 +J_\tau^-*J_\tau^-
 =(1+\chi_2)(J_\tau*J_\tau).
 }
 \tag{L-32714.6}
\]

Every coefficient with odd two-adic valuation vanishes. Every coefficient with even valuation is doubled.

The same identity holds with independent twists and with either factor replaced by any logarithmic derivative of the same deformation, because twisting and differentiation commute with the completely multiplicative parity character.

On a Hermitian diagonal, the physical channel energies obey

\[
 \boxed{
 \|F_+\|^2+\|F_-\|^2
 =2\|F_{\rm ev}\|^2+2\|F_{\rm odd}\|^2.
 }
 \tag{L-32714.7}
\]

No even/odd cross term remains.

## 3. Source-convolved finite reflected square

Let `b_4^+=b_4` and `b_4^-=chi_2 b_4`, and define

\[
 K_{\tau}^{\pm}=b_4^{\pm}*J_\tau^{\pm}.
 \]

For independent twists `t,u`, each channel has the exact finite reflected square

\[
 (K_{\tau,t}^{\pm}-b_{4,t}^{\pm})
 *(K_{\tau,-u}^{\pm}-b_{4,-u}^{\pm}).
 \tag{L-32714.8}
\]

Summing the two channels and using (L-32714.5) shows that every coefficient of the complete product-side source has even two-adic valuation.

Thus every surviving destination has the unique form

\[
 \boxed{d=4^r q,
 \qquad r\ge0,
 \qquad q\text{ odd}.}
 \tag{L-32714.9}
\]

This statement is exact before any norm, carry estimate, or logarithmic derivative is taken.

## 4. Four-adic product-carry normal form

Fix a carry row `n=j+k`. For `r>=1`, put

\[
 N_r=\left\lfloor{n\over4^r}\right\rfloor,
 \qquad
 J_r=\left\lfloor{j\over4^r}\right\rfloor,
 \qquad
 c_r=\chi_{n,4^r}(j).
 \]

PR #337 `L-32704` proves for every positive integer `q`

\[
 \boxed{
 \chi_{n,4^rq}(j)
 =\chi_{N_r,q}(J_r)
 +c_r\mathbf1_{q\mid N_r-J_r}.
 }
 \tag{L-32714.10}
\]

Since every non-odd paired destination is of the form (L-32714.9), equation (L-32714.10) applies to the complete product source. Therefore each `r>=1` contribution has the exact decomposition

\[
 \boxed{
 \text{paired product at }4^rq
 =\text{strict descendant at }(N_r,J_r)
 +\text{current-row divisor boundary}.
 }
 \tag{L-32714.11}
\]

The descendant parent satisfies

\[
 N_r\le n/4^r.
 \tag{L-32714.12}
\]

No same-scale residue-class state and no nonprincipal Dirichlet-character channel is introduced.

The `r=0` sector is the odd core at the current row and is retained without alteration.

## 5. Differentiation preserves the normal form

The coefficient identities in Sections 2--4 are finite at each integer destination and analytic in `tau` near zero. They may therefore be differentiated coefficientwise.

At first and second order, the paired product normal form yields exactly:

1. the even-valuation generalized-prime product;
2. the complete paired Selberg forcing;
3. strict `4^{-r}` descendants;
4. the current-row divisor boundaries appearing in `L-32704`;
5. the correctly polarized source currents of `L-32712`.

Thus the Hermitian second variation does not generate any additional odd-valuation or wrong-radix remainder.

## 6. Why this advances the final assembly

The previous Q=4 recurrence still had a typing ambiguity: after finite-deformation polarization, could the product source produce columns not governed by the four-adic storage theorem?

The answer is no after the exact parity pair. The complete destination dictionary is now

```text
current odd core;
strict four-adic descendants;
explicit divisor boundaries;
finite collars.
```

The strict descendants are compatible with the asymptotic reserve storage of `L-32713`. The divisor boundaries are the same source type as the current-row cross terms treated in `L-32704`, rather than a new independent-frequency object.

## 7. Proof boundary

Closed exactly:

1. positive even/odd decomposition of the finite Q=4 Jordan source;
2. complete parity orthogonalization of product coefficients;
3. elimination of every odd-valuation destination;
4. unique `4^r times odd` destination typing;
5. exact strict-descendant plus divisor-boundary carry normal form;
6. preservation of that normal form through the logarithmic second variation.

Still open:

1. one quantitative no-double-spend allocation of all divisor boundaries and descendants in the physical block;
2. composition with the all-pass terminal state into the coefficient-one delayed recurrence;
3. RH.
