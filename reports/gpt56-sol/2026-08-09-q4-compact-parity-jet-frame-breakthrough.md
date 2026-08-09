# Q=4 compact-innovation parity synthesis and jet-frame breakthrough

Date: 2026-08-09  
Agent: `gpt56-sol`  
Branch: `research/gpt56-sol/344-q4-compact-parity-synthesis`  
Base: PR #342 at `0ecb814f3f1d376ef28ab77ada6710c07e58f6d9`  
Status: **TWO NEW EXACT FINITE-FILTER THEOREMS; RH REMAINS UNPROVEN**

## Executive result

The live Q=4 route had reduced the RH-bearing step to the balanced compact one-step current innovation. This continuation removes two more ambiguities.

First, the compact source

```text
B_circ=(1-4^(1-s))/zeta(s)
```

admits an exact finite reconstruction from the parity pair whose complete current-scale synthesis charge is below `2/5` of the fixed parity-frame coefficient reserve. A strengthened cycle certificate forces the entire derivative gauge to factor through a strictly delayed ordinary Möbius boundary source.

Second, and more strongly, the compact current itself satisfies the uniform critical-line jet-frame inequality

```text
2 |q_circ|^2
 <= |q_+|^2+|q_-|^2+|B_+|^2+|B_-|^2.
```

This is proved by an exact `2 x 2` Hermitian polynomial certificate. Its first principal minor is a positive quartic and its determinant is a positive degree-eight polynomial. Exact Bernstein coefficients on six rational subintervals certify positivity with no floating step.

Thus the compact Q=4 innovation no longer needs a new current-space source map: it is already a strict component of the existing parity **jet** frame.

## 1. Exact compact-source synthesis

With

```text
z=2^-s,
p(z)=(1-z)(1-2z)(1-sqrt(2)z)^2,
T(z)=(1-z)(1-4z^2),
```

and the positive cubic Bezout polynomial `U` from PR #263, every polynomial `H` gives

```text
W_+=T U + H p(-z),
W_-=T U(-z)-H p(z),
W_+ p(z)+W_- p(-z)=T.
```

The exact cycle

```text
H(z)=(123+296z-387z^2+117z^3-14z^4+62z^5+303z^6)/1000
```

has `H(1)=1/2` and critical current-synthesis charge

```text
q_W=(14014874005-9814156296 sqrt(2))/32000000
    <9/2.
```

Since the parity analysis reserve is `45/4`,

```text
q_W/(45/4)<2/5.
```

Differentiation produces the gauge polynomial

```text
G_H=z[W_+'p+W_-'p(-z)].
```

The identity

```text
G_H(1)=3-6H(1)=0
```

and the explicit factor `z` give

```text
G_H=z(z-1)R_H.
```

Because `(1-z)O=1/zeta`, the complete gauge is only

```text
(log 2) z R_H(z) / zeta(s),
```

a finite strictly delayed ordinary Möbius boundary source. No new current-scale source species appears.

## 2. Uniform compact-current jet frame

For an arbitrary differentiable carrier `F`, set

```text
B_+=p(z)F,
B_-=p(-z)F,
B_circ=T(z)F,
```

and differentiate in `s`.

Writing

```text
u=F',
v=(log 2)F,
```

gives

```text
q_+=p u-zp' v,
q_-=p(-z)u+z p'(-z)v,
q_circ=T u-zT'v.
```

On `Re(s)=1/2`, `|z|=1/sqrt(2)` and `(log2)^2<1/2`. The theorem proves the stronger algebraic form

```text
2|q_circ|^2
 <= |q_+|^2+|q_-|^2
    +2(|p|^2+|p(-z)|^2)|v|^2,
```

which implies

```text
2|q_circ|^2
 <= |q_+|^2+|q_-|^2+|B_+|^2+|B_-|^2.
```

The Hermitian difference matrix has first principal minor

```text
Q1(x)=32x^4-16sqrt(2)x^3+(92+96sqrt(2))x^2+18sqrt(2)x+9
```

and determinant `8 Q2(x)`, where

```text
Q2(x)=256x^8-128sqrt(2)x^7
      +(976+1344sqrt(2))x^6
      -(960+224sqrt(2))x^5
      +(7912+4776sqrt(2))x^4
      +(1560+552sqrt(2))x^3
      +(-420+78sqrt(2))x^2
      +(-216+72sqrt(2))x
      +(117+54sqrt(2)).
```

`Q1` has strictly positive Bernstein coefficients on `[-1,0]` and `[0,1]`. `Q2` has strictly positive Bernstein coefficients on

```text
[-1,-1/2], [-1/2,0], [0,1/2], [1/2,1].
```

Hence the Hermitian symbol is positive definite on the full critical circle.

Because the symbol is finite trigonometric polynomial, Toeplitz compression gives the corresponding finite-support Hilbert inequality. Causal finite prefixes incur only a fixed-width terminal collar.

## 3. Exact replay

The retained standard-library exact checks are

```text
X-34401 ... /verify.py
X-34401 ... /verify_jet_frame.py
```

with result digests

```text
compact synthesis:
05fbc3e49a729957d3253593d566e131f100964d1ac80144b4ae423c47ffd65e

jet frame:
4a4c3cffc2b803827776066aaab27bb8d058a31ad0bac3fe41e1f3b8654982b6
```

The checks prove no delayed recurrence and no RH conclusion.

## 4. What this closes in the live Q=4 graph

Before this pass, the balanced compact innovation was still described as requiring a new current-space domination theorem.

That is no longer accurate.

The exact source classification is now

```text
compact Q4 current
 -> uniform parity current+bare jet frame, coefficient 1/2;

alternative finite source synthesis
 -> current-scale parity synthesis <2/5 frame budget;
 -> all derivative gauge = strictly delayed ordinary Mobius boundary;

actual Q4 innovation
 -> compact current
    + one explicit log4-delayed bare Q4 gauge.
```

PR #334 already closes the fully synthesized ordinary Möbius carry boundary cofinally except the fixed row `n=3`. PR #341 closes the Q=4 terminal scattering-state curvature sign. PR #342 closes the critical reserve increment, second-current cross term, and product-source absorption.

## 5. Honest remaining obstruction

The remaining theorem is not another source-map problem. It is the final **source-convolved two-frequency no-double-spend composition**:

```text
parity current+bare jet energy
+ paired Selberg forcing
+ reconstructed Mobius boundary
+ Q4 delayed bare gauge
+ neutral terminal state
 -> coefficient-one finite-delay recurrence.
```

PR #337 closes the corresponding untwisted carry-row Selberg–Kummer inequality cofinally, but the independent-frequency physical product block still carries the RH information. The new jet-frame theorem embeds the compact innovation into that existing block; it does not independently bound the block.

Thus this branch materially narrows the live frontier without relabeling the last Hermitian estimate as routine.

## Exact status

```text
compact Q4 source finite parity reconstruction       PROPOSED COMPLETE EXACT
current-scale synthesis charge <2/5                  PROPOSED COMPLETE EXACT
derivative gauge -> delayed ordinary Mobius source   PROPOSED COMPLETE EXACT
uniform compact-current parity jet frame             PROPOSED COMPLETE EXACT
finite Toeplitz/Hilbert consequence                   PROPOSED COMPLETE
source-convolved reflected no-double-spend recurrence UNPROVEN / RH-bearing
Riemann Hypothesis                                    UNPROVEN
```
