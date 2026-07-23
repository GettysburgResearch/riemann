# Cross-disciplinary source ledger — conic witness portfolios

Agent: `gpt56-06-c`  
Issue: #57  
Snapshot: 2026-07-23

The repository proofs D-5701 and L-5701 are elementary. The sources below
supply theorem shapes and algorithmic context, not hidden RH dependencies.

| Source | Inspection | Theorem shape transferred | Repository use |
|---|---|---|---|
| Vandenberghe and Boyd, *Semidefinite Programming*, SIAM Review 38 (1996) | author-hosted full PDF | PSD cones, trace duality, primal/dual SDP certificates | exact Gram multipliers for matrix witness portfolios |
| Ben-Tal and Nemirovski, *Robust Convex Optimization*, Mathematics of Operations Research 23 (1998) | author-hosted full PDF | universal feasibility over uncertainty sets and tractable robust counterparts | optimize the worst-case portfolio, not a midpoint score |
| Peyrl and Parrilo, *Computing Sum of Squares Decompositions with Rational Coefficients*, Theoretical Computer Science 409 (2008) | author-hosted manuscript | numerical nomination followed by rounding/projection to exact rational certificates | rationalize Gram/PSD nominations before proof replay |
| Liu and Pataki, *Exact duality in semidefinite programming based on elementary reformulations*, SIAM Journal on Optimization 25 (2015) | arXiv full text | exact certificates and pathology-aware SDP reformulation | warning that opaque floating SDP duals are not proof objects |
| Magron et al., *Formal Proofs for Nonlinear Optimization*, Journal of Automated Reasoning 64 (2020) | author/arXiv full text | untrusted numerical optimization plus small formally checkable certificates | trusted-base reduction for future exact portfolio checkers |

## Operational conclusions

1. Solvers nominate; exact rational replay proves.
2. PSD status should be carried by an explicit Gram factor where practical.
3. Robustness is a universal statement over one joint uncertainty set.
4. Weak duality is enough for soundness; optimizer optimality is unnecessary.
5. Near-degenerate SDP output requires special caution during rationalization.
