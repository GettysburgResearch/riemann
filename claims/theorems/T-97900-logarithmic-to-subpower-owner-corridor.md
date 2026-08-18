# T-97900 — Only the logarithmic-to-subpower owner corridor remains

Claim ID: `T-97900`  
Status: **UNCONDITIONAL REDUCTION; ONE STRICTLY LOCALIZED ROOT ESTIMATE OPEN**  
Created: 2026-08-18  
Depends on: `L-97900`--`L-97902`; PR #594 root zero-hinge map; the frozen annular Mellin--Landau consumer  
RH status: **unproved**

Use

\[
 \delta_X=(\log\log X)^{-1/4},
 \qquad
 P_X=(1-2\delta_X)\log X,
\]

\[
 K_X=\lfloor(\log\log X)^{1/4}\rfloor,
 \qquad
 H_X=X^{1/(K_X+2)}.
 \tag{T-97900.1}
\]

Let `U_(P_X,<p)` be the exact state obtained by adjoining every rough prime in
`(P_X,p)`, and let `U_(P_X)` be the complete logarithmic cube.
Split the exact largest-prime Bellman budget into

\[
 \mathfrak C_X=
 \sum_{P_X<p<H_X}\frac1pU_{P_X,<p}(X/p)
 \tag{T-97900.2}
\]

and

\[
 \mathfrak H_X=
 \sum_{H_X\le p\le X/2}\frac1pU_{P_X,<p}(X/p).
 \tag{T-97900.3}
\]

Then the native normalized root scalar satisfies exactly

\[
 \boxed{
 U_{\rm full}(X)=U_{P_X}(X)-\mathfrak C_X-\mathfrak H_X.
 }
 \tag{T-97900.4}
\]

The preceding lemmas prove

\[
 U_{P_X}(X)\asymp(\log\log X)^{-1}>0
 \tag{T-97900.5}
\]

and, for every fixed `A`,

\[
 |\mathfrak H_X|\ll_A(\log\log X)^{-A}.
 \tag{T-97900.6}
\]

Thus every owner below almost `log X` has been resummed positively and every
owner above `X^{o(1)}` is PNT-negligible.

## Exact remaining correlation

Expanding the state in (T-97900.2) by its literal largest-prime history gives

\[
 \boxed{
 \mathfrak C_X=
 \sum_{P_X<p<H_X}\frac1p
 \sum_{\substack{v\ {m squarefree}\\
                  P_X<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v
 U_{P_X}(X/(pv)).
 }
 \tag{T-97900.7}
\]

All endpoints and owner constraints are exact. This is a one-sided
prime-versus-Mobius Type-II correlation, but its owner prime is now restricted
to

\[
 \boxed{
 (1-o(1))\log X<p<X^{1/(\log\log X)^{1/4}+o(1)}=X^{o(1)}.
 }
 \tag{T-97900.8}
\]

No fixed-power prime sector remains.

## Minimal and quantitative closure statements

The exact root criterion is

> **Logarithmic-to-Subpower Corridor Bellman (`LSCB67`).**
> \[
> \boxed{
> \mathfrak C_X\le U_{P_X}(X)-\mathfrak H_X
> }
> \]
> for every sufficiently large real root endpoint `X`.

By (T-97900.4), `LSCB67` is exactly equivalent to eventual nonnegativity of
the native root scalar. It is not asserted state-wise and does not include the
stronger nonzero Lorenz hinges.

A more convenient strictly sufficient estimate is

> **Margin form `LSCB67+`.**
> \[
> \boxed{
> \mathfrak C_X
> \le U_{P_X}(X)-(\log\log X)^{-2}.
> }
> \tag{T-97900.9}
> \]

Equation (T-97900.6) makes the high-owner error smaller than half of this margin
for all sufficiently large `X`. Therefore

\[
 \mathrm{LSCB67+}
 \Longrightarrow U_{\rm full}(X)>0
 \Longrightarrow\mathrm{RH}.
 \tag{T-97900.10}
\]

The final implication is the already reconstructed zero-safe annular
Mellin--Landau theorem.

## What this pass removes

```text
largest owner <= (1-o(1)) log X       CLOSED by complete cube positivity
largest owner >= X^(1/K_X)            CLOSED by top completion + PNT
all fixed-power owner sectors          CLOSED
activation boundary of high owners    CLOSED with reciprocal-prime interval mass
state-wise Bellman requirement         NOT NEEDED by the root consumer
nonzero Lorenz hinges                  NOT NEEDED by the root consumer
logarithmic-to-subpower corridor       OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```

The remaining theorem cannot be discharged by another fixed count depth: PR
#594 proves all subcritical count-depth currents eventually negative. A valid
continuation must exploit the signed correlation in (T-97900.7) inside the
subpower critical corridor.