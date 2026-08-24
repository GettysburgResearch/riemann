# T-105415 — Fixed-width moving-saddle endpoint for the Xi reverse-Rolle programme

Claim ID: `T-105415`  
Status: **PROPOSED COMPLETE HIGH-DERIVATIVE ENDPOINT; LOW-ORDER DESCENT OPEN**  
Created: 2026-08-24  
Depends on: `L-105413--L-105415`, `T-105410`  
RH status: **unproved**

The explicit first theta orbit makes the real part of the exact action strictly concave on the complete translated moving-saddle ray. This supplies the global relative-dominance inequality left open by `M-105331`, including the origin and infinity connectors.

Consequently the exact moving-saddle model is relatively accurate on

\[
|\Re z|\le cM/\log M,
\qquad
|\Im z|\le H,
\]

uniformly for every `m>=M`. The exact analytic phase then gives a proposed complete proof that every `Xi^(m)` in the high tail is real-rooted and simple in the common fixed-width box, with negative critical residues. The terminal derivative order is

\[
\boxed{r(T)=O_H(T\log T).}
\]

This genuinely complements `T-105410`:

```text
T105410  much larger unconditional real-axis prefix at shrinking width;
T105415  fixed physical width from the moving-saddle contour proof.
```

The conclusion-facing chain is now

```text
explicit Xi-kernel shifted-ray concavity
-> fixed-width high derivative real-rooted endpoint
-> exact derivative-ladder telescope
-> low-order PRES105220 AND BRP105220
-> RH.
```

Only the first two arrows are addressed here. The last low-order descent remains open and RH is unproved.

```text
global moving-saddle dominance             PROPOSED COMPLETE / REVIEW REQUIRED
relative fixed-width saddle asymptotic      PROPOSED COMPLETE / REVIEW REQUIRED
O(T log T) real-rooted terminal derivative  PROPOSED COMPLETE / REVIEW REQUIRED
low-order derivative-ladder budget          OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```
