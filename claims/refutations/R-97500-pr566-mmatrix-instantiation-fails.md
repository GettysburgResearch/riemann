# R-97500 — PR #566 does not instantiate its exact M-matrix lemma

Claim ID: `R-97500`  
Status: **EXACT STATEMENT-TO-USE REFUTATION; ABSTRACT L-96652 SURVIVES**  
Created: 2026-08-17  
Inputs: PR #566 `L-96651/L-96652`; PR #568 `R-97010`; PR #576  
RH status: **unproved**

`L-96652` is an exact theorem: for positive nilpotent `T`,

\[
 F+TF=g,
 \qquad g\ge Tg
 \quad\Longrightarrow\quad F\ge0.
\]

The proposal has two possible interpretations of `T`.

## 1. Natural least-prime interpretation

If `T=R` is the actual least-prime parity operator, the source equation is

\[
 (I+R)F=b,
\]

so `g=b`. By `L-97500`,

\[
 g-Rg=(I-R^2)F.
\]

The right side is exactly the signed current obtained by retaining rough
histories of lengths zero and one and exporting the even two-step frontier.
PR #561/#568 prove that every fixed even-depth current is eventually negative.
The retained directed endpoint gives the scalar witness

\[
 \boxed{
 5B_{2,200000}(2)+3B_{2,200000}(3)
 <-62.7181678185658877324<0.
 }
\]

Therefore the natural-operator premise `g>=Rg` is false.

## 2. Contractive factor-67 interpretation

If `T=A` has the contractive coefficients `alpha`, it is not the natural source
operator. The consumed equation

\[
 (I+A)F=g_A
\]

requires

\[
 \boxed{g_A=b-(R-A)F.}
\]

Thus `g_A` contains the complete signed residual of every unexported child
subtree. Injecting `A F_w` into a disjoint reserve proves a fact about that
reserve; it does not identify the Hall complement with `b-(R-A)F` and does not
prove

\[
 g_A\ge A g_A.
\]

PR #576's scalar fixture already separates reserve domination from Hall-current
domination. `L-97500.5` gives the exact source coefficient missing behind that
fixture.

```text
L-96652 abstract operator lemma        VERIFIED
T=natural least-prime operator         PREMISE FALSE
T=contractive alpha operator           SOURCE EQUATION NOT DERIVED
PR #566 complete composition           UNPROVEN / FIRST ARROW BROKEN
```
