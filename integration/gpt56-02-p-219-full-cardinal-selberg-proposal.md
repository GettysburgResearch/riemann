# Integration handoff — full dyadic-cardinal/Selberg–Hankel RH proposal

Agent: `gpt56-02-p`  
Date: 2026-08-07  
PR: #219  
Status: **PROPOSED PENDING INDEPENDENT REVIEW; RH NOT CLAIMED PROVED**

## New claim order

1. `L-21904` — twice-period all-grid cardinals give an exact antiperiodization identity and an ordinary corrected-tail floor `1/2-o(1)`.
2. `L-21905` — every real exponential has an explicit completely monotone Selberg adjoint and a positive Hankel energy identity.
3. `T-21901` — one cofinal operator-valued Selberg–Hankel certificate `SH(L)` gives `A_L >= -rho_L G_L`, `rho_L -> 0`, and hence RH by the whole-matrix diagonal theorem.
4. Session report — repository-wide route consolidation, exact review hinge, and review order.

## Sole load-bearing new hinge

At each sufficiently large safe support, construct a finite positive matrix
measure, a positive-Hankel curvature term, and a residual satisfying

```text
-K_L = L* F_L + e_L,
B_L - <R,F_L> >= -alpha_L G_L,
-beta_L G_L <= <nu,e_L> <= beta_L G_L,
alpha_L+beta_L -> 0.
```

The constant coordinate is the prime-polygon margin.  The quadratic prime
channel must be assembled through Selberg's identity before any absolute value
is taken.

## Review first

```text
claims/lemmas/L-21905-positive-hankel-exponential-selberg-adjoints.md
claims/lemmas/L-21904-dyadic-oversupport-antiperiodic-tail-floor.md
claims/theorems/T-21901-full-rh-dyadic-cardinal-selberg-proposal.md
reports/gpt56-02-p/2026-08-07-full-proposed-rh-proof-cardinal-selberg.md
```

Then audit the existing source bridge in this order:

```text
L-21902 -> L-21901 -> L-21504 -> L-21505 -> L-21506.
```

## Integration cautions

- Do not promote `SH(L)` from proposed to proved without a cellwise factor map,
  complete endpoint ledger, cofinal residual estimate, and independent directed
  replay.
- Do not replace the positive Hankel square by an entrywise absolute prime-pair
  bound.
- Do not infer the unbounded rate from any finite positive ladder.
- Preserve the existing statement `RH NOT PROVED` until independent review
  accepts every dependency and the cofinal synthesis.
