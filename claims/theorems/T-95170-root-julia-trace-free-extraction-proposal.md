# T-95170 — Trace-free root-Julia extraction would close the carry route

Claim ID: `T-95170`  
Status: **CONDITIONAL CLOSURE THEOREM — EXTRACTION HYPOTHESIS OPEN; RH UNPROVED**  
Created: 2026-08-17  
Depends on: `L-95040/L-95041`, `L-95171/L-95172`, and the reviewed Cycle-Debt-to-prime-ramp/Mellin–Landau consumer  
Scope: names the exact remaining matrix-to-carry interface; it does not assert that interface

## 1. The extraction theorem

For each endpoint `X`, let `Sigma_2(q)` be the positive two-channel source of `L-95171`, and let

\[
\mathcal J_2(e)=\sum_q\chi_e(q)\Sigma_2(q)
\]

be its positive carry current.

**Trace-free Schur extraction (`TFSE`).** Construct, source coefficient by source coefficient, a finite balanced split/auxiliary-current system whose scalar off-diagonal output is the complete critical root/carry source and whose negative capacity cost is bounded by

\[
C\left(
1+\sum_{n\le X}{b_2(n)^2\over g_2(n)n}
\right)\log^A(2X),
\tag{T-95170.1}
\]

for fixed `A,C`, while the positive trace is returned to the auxiliary environment rather than charged as scalar debt.

The construction must preserve:

1. the coefficient-one channel swap;
2. the unit/root boundary;
3. every carry column before scalar observation;
4. the off-diagonal sign;
5. source ownership through all Pascal cycles.

## 2. Conditional consequence

By `L-95172`, the parenthesis in (T-95170.1) is `O(log X)`. Thus TFSE gives polylogarithmic optimized Cycle Debt. The existing exact elementary spine then gives

\[
\text{polylog Cycle Debt}
\Longrightarrow
\text{complete prime ramp }4\sqrt X+\operatorname{polylog}(X)
\Longrightarrow
\mathrm{RH}.
\]

Hence

\[
\boxed{\mathrm{TFSE}\Longrightarrow\mathrm{RH}.}
\tag{T-95170.2}
\]

## 3. Automatic rejection conditions

TFSE is not established by any of the following:

```text
root neutrality alone;
signed interior span alone;
entrywise positivity of Sigma_2 alone;
replacing b_2 by |b_2| or g_2;
charging the full trace as scalar capacity;
a source-free Schur complement;
a finite experiment without an all-X map.
```

## 4. Boundary

```text
positive two-channel root state         PROVED / L-95171
logarithmic channel energy              PROVED / L-95172
trace-free Schur extraction             OPEN / RH-BEARING
TFSE -> Cycle Debt -> RH                CONDITIONAL COMPLETE
Riemann Hypothesis                      UNPROVED
```
