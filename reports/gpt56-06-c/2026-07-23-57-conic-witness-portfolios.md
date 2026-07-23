# Session report — Issue #57 exact conic witness portfolios

Agent: `gpt56-06-c`  
Issue: #57  
Branch: `agent/gpt56-06-c/57-conic-witness-portfolios`  
Date: 2026-07-23  
Status: proposed proof infrastructure; no RH counterexample candidate

## Starting hypothesis

A finite witness need not be one scalar inequality or one matrix eigenvector.
The active project has many RH-valid constraints on the same finite primitive
data. Their nonnegative dual cone may contain a separator that survives shared
uncertainty even when every individual row is inconclusive.

## Existing work audited

The contribution builds above, rather than duplicates:

- PR #50's uncertainty-closed witness semantics and support-function checker;
- PR #38's scalar and Pick passivity constraints;
- PR #43's differential and Stieltjes localizers;
- PR #48's derivative-free secants and Loewner minors;
- PR #52's two-channel and barycentric localizers;
- PR #56's developing proof-grade Arb feature producer;
- PRs #44, #49, #51 and Issue #55's carrier fixed-vector certification work.

## Main result 1 — finite RH-valid data form a conic system

D-5701 encodes exact affine scalar rows and affine PSD matrix pencils over one
canonical primitive feature table. Under RH, every nonnegative scalar
combination and every exact PSD trace multiplier remains nonnegative.

The decisive proof object is an exact dual portfolio, not a floating solver
optimum. PSD multipliers are represented by rational or dyadic Gram vectors.

## Main result 2 — portfolios can certify what every row misses

For

\[
q_1=-2/5+u,
\qquad q_2=-2/5-u,
\qquad |u|\le1,
\]

each row separately has robust upper `3/5`. The exact portfolio has upper
`-4/5`; the shared primitive coefficient cancels exactly. If the two appearances
of `u` are widened independently, the certificate disappears.

The matrix analogue uses

\[
K(u)=\operatorname{diag}(-1/2+u,-1/2-u).
\]

Each coordinate vector is inconclusive, while the exact PSD multiplier `I`
gives `trace(K)=-1` for every admitted `u`.

## Main result 3 — normalized repair distance

Raw score margin is arbitrary under positive rescaling. L-5702 proves that an
affine portfolio with moat `mu` and feature coefficient `c` gives

\[
\operatorname{dist}(C,K_{RH})\ge\mu/\|c\|_*.
\]

This scale-invariant lower bound measures how much extra primitive-data movement
would be required before the witness could become consistent with all imported
finite RH-valid constraints.

## X-5701

A compact standard-library checker uses exact `Fraction` arithmetic. It supports:

1. affine portfolios over shared interval features;
2. exact Gram portfolios against affine symmetric matrix pencils.

It contracts coefficients before widening, verifies exact feature and gate
manifests, and rejects negative weights, malformed matrices, hidden features,
blocking gates, false endpoints, and zero-touching results.

Local validation:

```bash
python verify.py --self-test
python verify.py certificates/affine-shared-cancellation.json
python verify.py certificates/psd-gram-cancellation.json
```

The self-test reports three exact controls passed. All controls are synthetic;
no zeta or xi value is present.

## Cross-disciplinary connection

The architecture combines robust optimization and SDP duality with
proof-carrying exact replay. A high-performance solver can search a large dual
cone, but soundness requires only exact nonnegative weights, exact Gram factors,
one support-function upper bound, and a strict sign.

## Failed or deferred approaches

- Trusting a floating negative SDP dual was rejected.
- Comparing raw score margins across differently scaled portfolios was rejected.
- Independent intervalization of repeated primitives was rejected when shared
  dependence is available.
- A general exact SDP checker was deferred; low-rank Gram certificates cover the
  first practical use cases and keep the trusted kernel small.
- Full rational-polytope support is inherited from X-4501 after portfolio
  contraction rather than duplicated here.

## Main risks

1. An imported row may have a sign or normalization error.
2. Large portfolio coefficients can amplify ball radii.
3. A solver may nominate a multiplier too close to a proper PSD face for stable
   rationalization.
4. A finite row library may simply lack a separating direction.
5. A positive feature-repair moat does not address unknown semantic omissions or
   correlated software bugs.

## Recommended next actions

1. Issue #39 should export one canonical Arb primitive-feature table rather than
   separate row intervals.
2. Build scalar, secant, two-channel, barycentric, Pick, Stieltjes, and Loewner
   rows over that table.
3. Search normalized portfolios against actual ball radii.
4. Rationalize and replay the best exact portfolio.
5. For carrier work, permit exact higher-rank Gram multipliers over the complete
   fixed-vector matrix pencil.
6. Require independent primitive evaluation for any strict real-data result.

## Files added

- D-5701, L-5701, L-5702, M-5701;
- X-5701 checker, controls, and README;
- source ledger;
- integration patch;
- this report.

No `Z-####` candidate is allocated.
