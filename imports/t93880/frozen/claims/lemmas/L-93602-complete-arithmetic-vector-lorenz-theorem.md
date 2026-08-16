# L-93602 — Complete Arithmetic Vector-Lorenz Theorem

Claim ID: `L-93602`  
Status: **PROPOSED COMPLETE ALL-PARAMETER THEOREM ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91720`, `L-91780`, `L-91781`, `L-93601`  
RH status: **unproved**

For every

\[
p\ge67,
\qquad1\le y<67,
\qquad2\le j\le66,
\]

the leftmost Target-Lorenz common-source removal `U_(p,y)` satisfies

\[
\boxed{
\mathfrak L_j(p,y)
=R_j(U_{p,y})-O_R^{(j)}(p,y)\ge0.
}
\tag{L-93602.1}
\]

Indeed `L-91780` gives

\[
\mathfrak L_j(p,y)\ge\frac{\Theta_j(p,y)}{E_T(p,y)}.
\]

The compact directed theorem `L-91781` proves `Theta_j>0` for `py<166000`.
`L-93601` proves `Theta_j>26` for `py>=166000`. The two domains meet exactly,
with no omitted boundary cell.

By the exact ordered-cone theorem `L-91720`, the same coefficient vector:

```text
matches target exactly;
minimizes declared score cost;
maximizes every component row simultaneously;
returns an explicit coordinate separator if a row fails.
```

Thus the arithmetic common-source row gate is closed on the complete real
domain. Rows beyond `66`, where the stopped child is inactive, remain governed
by the frozen canonical/frontier row theorem and are not inferred by extending
the `2..66` certificate silently.
