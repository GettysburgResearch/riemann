# T-90505 — Odd Wiener–Hopf–Hankel equivalences for RH

Claim ID: `T-90505`  
Status: **FULL EXACT EQUIVALENCE PROPOSAL — HALF-LINE SIGN THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90505`, `L-90507`, `L-90510`; Xi-cardinal capture on PR #365

Fix `1/2<a<c` and let `A_(a,c)^odd` be the trace-class coefficient operator for the pole-free Weil form restricted to odd tests. Then

\[
 \boxed{
 \begin{aligned}
 \mathrm{RH}
 &\iff A_{a,c}^{\rm odd}\succeq0\\
 &\iff \det(I+tA_{a,c}^{\rm odd})>0\quad(t>0)\\
 &\iff \operatorname{tr}(e^{-\beta A_{a,c}^{\rm odd}}-I)\le0
       \quad(\beta>0)\\
 &\iff
 \bigl(\operatorname{tr}[(A_{a,c}^{\rm odd})^{i+j+1}]\bigr)_{0\le i,j\le d}
 \succeq0\quad(d\ge0).
 \end{aligned}}
 \tag{T-90505.1}
\]

On `L^2(0,infinity)` the quadratic form is explicitly the Lévy continuum expression from (L-90510.6), the negative constant mass, and the all-prime Wiener–Hopf–Hankel series (L-90510.7).

This is the smallest current unconstrained target:

```text
one parity sector;
no pole term;
no pole-null moment constraints;
no external finite-rank projection;
one explicit half-line Wiener–Hopf–Hankel operator.
```

No unconditional half-line positivity theorem is claimed.
