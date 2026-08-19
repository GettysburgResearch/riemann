# T-99710 — Adaptive Poisson-owner Carleson frontier

Claim ID: `T-99710`  
Status: **UNCONDITIONAL REDUCTIONS; ONE PHASE-SENSITIVE EMBEDDING OPEN**  
Created: 2026-08-20  
Base: PR #655 at `7946f2979a69392e5275be90f023dfb34009d4d9`  
RH status: **unproved**

Let

\[
h(x)=H_{67}^{\rm sharp}(x)
\]

be the exact scalar SHARP Harnack defect of PR #647, and define the finite
phase packet

\[
\mathscr H_x(w)
=
\sum_{n\le x}{\beta(n)\over\sqrt n}T(x/n)n^{-w}.
\tag{T-99710.1}
\]

For `x>=e^e`, put

\[
\tau_x={1\over\log\log x}
\]

and define its adaptive Poisson square function

\[
\boxed{
\mathscr S(x)
=
\left(
\int_{\mathbb R}
 {\tau_x\over\pi(\tau_x^2+\gamma^2)}
 |\mathscr H_x(-\tau_x+i\gamma)|^2\,d\gamma
\right)^{1/2}.
}
\tag{T-99710.2}
\]

`L-99711` proves pointwise

\[
|h(x)|\le\mathscr S(x).
\tag{T-99710.3}
\]

Consequently the following single theorem is conclusion-complete.

> **Adaptive Poisson-Owner Carleson estimate (`APOC99710`).**  For every
> `epsilon>0`,
> \[
> \int_{e^e}^{X}\mathscr S(x){dx\over x}
> \ll_\epsilon X^\epsilon.
> \tag{T-99710.4}
> \]

Indeed, (T-99710.3) gives

\[
\int_1^X h_-(x){dx\over x}=X^{o(1)}.
\tag{T-99710.5}
\]

PR #653 proves that subpower logarithmic negative mass of `h` makes the
negative-part Mellin transform holomorphic in every half-plane `Re s>epsilon`.
Landau applied to the remaining nonnegative part, together with the exact
zero-safe scalar transform, excludes every zeta zero with real part greater
than `1/2+epsilon`.  Letting `epsilon` tend to zero and using the functional
equation gives RH.

Thus

\[
\boxed{\mathrm{APOC99710}\Longrightarrow\mathrm{RH}.}
\tag{T-99710.6}
\]

## Why this target is structurally different

PR #655 shows that every fixed logarithmic owner order has a negative
coefficient and that the untwisted martingale variance vanishes on the
principal parity sector.  `L-99710` removes both obstructions:

1. Cauchy–Poisson averaging gives the exact gap
   \[
   \overline V_{\tau_x}(n)
   \ge {1\over\log\log x}|a(n)|^2;
   \]
2. the left strip costs only
   \[
   x^{\tau_x}
   =\exp(\log x/\log\log x)=x^{o(1)}.
   \]

So the unresolved estimate has a genuine martingale spectral gap and exactly
the amount of analytic slack permitted by the negative-mass conclusion.

## Source-specific proof contract

A valid proof of (T-99710.4) must perform the owner quadratic-variation
embedding before the source index is collapsed.  It may use:

```text
the exact logarithmic-owner probabilities P_n(q);
the Cauchy-averaged gap L-99710;
the SHARP activation weight T(x/n);
the positive RN endpoint cocycle of PR #652;
the source-complete sequential first-owner Euler identity.
```

It may not use:

```text
source-blind prefix Cauchy-Schwarz;
a fixed strip width;
a finite logarithmic owner order;
the contracted alpha-child operator as the native Euler operator;
coefficientwise positivity of the real-u completion as a Landau witness.
```

## Continuous-order cross-check

`L-99712` proves that the exponential mixture of all fixed owner orders becomes
coefficientwise positive at the sharp order `u*=log(2)/log(67)`.  `R-99710`
proves why this cannot directly close Landau: it introduces a genuine positive
real pole, and its pole-subtracting derivative has negative activation atoms.
This cross-check leaves the adaptive phase square, not real-order positivity,
as the conclusion-facing mechanism.

```text
Cauchy-Poisson owner gap                    PROVED EXACT
adaptive strip evaluation                  PROVED EXACT
subpower phase/strip tradeoff               PROVED EXACT
continuous all-order positive completion    PROVED EXACT
real-order direct Landau promotion          REFUTED
APOC99710 source Carleson embedding          OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```