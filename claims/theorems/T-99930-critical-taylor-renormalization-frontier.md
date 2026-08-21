# T-99930 — Critical Taylor renormalization and the last native scalar

Claim ID: `T-99930`  
Status: **UNCONDITIONAL SYNTHESIS + CONDITIONAL RH THEOREM**  
Created: 2026-08-20  
Frozen base: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
RH status: **unproved**

The complete current proof spine may be expressed without Hall, Volterra,
score, capacity, terminal, or contracted-child imports.

## Proven spine

1. `L-99930` proves the activation-zero native scalars
   \[
   G_m(X)=\sum_n\beta(n)n^{-1/2}S(X/n)^m
   \]
   are positive for every real `m>=2`.
2. `L-99931` removes, with certified alternating sign, every Euler–Taylor layer
   whose effective prime exponent is larger than one.
3. The first layer not controlled by the convergent prime mass is the explicit
   scalar `C_m` of `L-99932`.
4. Its Mellin transform is holomorphic at every positive real point and retains
   every hypothetical reciprocal-zeta pole with positive real part.

Therefore, for any one fixed integer `m>=2`,

\[
 \boxed{
 \int_1^X(\mathcal C_m(t))_-\frac{dt}{t}=X^{o(1)}
 \quad\Longrightarrow\quad RH.
 }
 \tag{T-99930.1}
\]

Eventual nonnegativity of `C_m` is a stronger sufficient condition.

## Canonical minimal member

The choice `m=2` gives

\[
 \boxed{
 \mathcal C_2(X)=
 16\frac{1-67^{-3/2}}{\zeta(3/2)}X
 -\sum_n\frac{\beta(n)}{\sqrt n}
  \bigl[4(\sqrt{X/n}-1)_+\bigr]^2.
 }
 \tag{T-99930.2}
\]

The second term is globally nonnegative.  The missing inequality is the exact
upper envelope

\[
 \boxed{
 G_2(X)\le
 16\frac{1-67^{-3/2}}{\zeta(3/2)}X
 }
 \tag{T-99930.3}
\]

or merely subpower logarithmic mass of its violations.

## Reconciliation with the live ratio-window frontier

Differentiating the normalized quadratic scalar gives

\[
 \frac{d}{d\log X}\bigl[X^{-1}G_2(X)\bigr]
 =4X^{-1}G_1(X),
 \tag{T-99930.4}
\]

where `G_1` is the critical zero-at-activation carrier.  A final scale
difference is therefore a positive logarithmic B-spline smoothing of `G_1`.
The collar coefficient isolated in PR #664 is the same half-order boundary:
it is the ratio-67 Möbius window after the box normalization.

Thus the newest routes meet at one arithmetic object rather than furnishing
independent missing lemmas.

## Exact boundary

```text
activation-zero power positivity m>=2       PROVED
subcritical Taylor remainders                PROVED POSITIVE
all absolutely convergent Euler layers       REMOVED EXACTLY
critical renormalized kernel                 PROVED EXACT
critical negative-mass criterion -> RH       PROVED CONDITIONAL
critical envelope / negative mass            OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```

No statement in this theorem identifies the open critical envelope with an
already proved supercritical inequality.