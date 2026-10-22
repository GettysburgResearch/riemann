# Audit of `L-91843` — positive source stages versus physical comparison stages

Frozen PR: `#488` at `9acd381fa168db02a03646ab16851daebbf4d0fd`  
Reviewed claim: `L-91843`  
Verdict: **UNPROVEN / GAP**

## Issue

`L-91843` asserts that each of fourteen stages supplies disjoint positive packets

\[
 \Sigma_{i-1}=C_i+\sum_bP_{i,b}+U_i+\Sigma_i,
\]

and that observing this positive source telescope yields

\[
 \Omega_X
 =\Xi(d_X^{\rm cur})+r_X
 +\sum_b\beta_bU_b^{(1)}\Omega(P_b),
 \qquad r_X\ge0.
\]

The frozen inputs do not establish that source statement. Several of the listed stages are genuine positive source operations, while several others are physical response comparisons or signed defects.

## Stage-by-stage type audit

| Stage | Operation | Correct mathematical type | Positive source split established? |
|---:|---|---|---:|
| 1 | native/full-Möbius source typing | signed arithmetic identity | No; native row is signed |
| 2 | inner-versus-outer scale split | exact source decomposition if explicitly supplied | Conditional |
| 3 | bottom omission | positive restriction / unused source | Yes |
| 4 | top omission | positive restriction / unused source | Yes |
| 5 | whole-cell support selection | positive restriction of endpoint measure | Yes |
| 6 | deterministic root Hall | positive residual plus positive row bonus reproducing a signed row | Yes at row/fibre scope; common endpoint source still imported |
| 7 | first-owner rough partition | disjoint support projection | Yes |
| 8 | causal current/internal-child split | positive realized identity on a positive packet | Yes on typed positive inputs |
| 9 | endpoint integration | positive linear pushforward | Yes, conditional on the fibre packet |
| 10 | same-cell refinement | positive Markov pushforward | Yes where used |
| 11 | martingale quantizer | positive linear pushforward plus a physical collar | Quantizer yes; collar is not a source partition of native capacity |
| 12 | scalar thinning | positive retained/unused split | Yes |
| 13 | mismatch/collar/taper/base comparison | signed error and capacity comparison | **No** |
| 14 | port completion | PSD capacity coordinate, or absent in the preferred route | Conditional / not source measure |

## The decisive type mismatch

The finite/continuum discrepancy is explicitly a signed defect:

\[
 E_X=b_X^\star-\overline b_X^\star.
\]

The retained-cell theorem controls its adjacent signed increments and their ordinary/detail responses. It does not turn `E_X` into a nonnegative source packet.

Likewise, the capacity proof uses inequalities of the form

\[
 |\mathcal D_4v_q(C_X-E_X^I)|
 \le \text{explicit bound},
\]

then spends positive reserve from a common thinning or omission. This proves a physical inequality. It is not a positive source equality

\[
 \Sigma_{12}=C_{13}+U_{13}+\Sigma_{13}.
\]

A positive source telescope could be obtained only after supplying an explicit positive realization of both signs of every defect and proving its ownership in every typed coordinate. No such realization appears in `L-91843` or its locked inputs.

## Consequence for the native identity

The one-shot route does not need the stronger source claim. Once the final row is independently shown detail-feasible, one may define

\[
 r_X=\Omega_X-\Xi(d_X)\ge0.
\]

That is an exact capacity identity, and the endpoint consumer accepts it. It is, however, a complement after a physical inequality—the operation which `L-91843.4` expressly says it is avoiding.

Therefore:

```text
physical inequality Xi(d_X)<=Omega_X
    may imply a valid one-shot slack identity;

fourteen positive source stages
    are not proved by the submitted ledger;

observing the alleged source telescope
    does not independently establish the native packet identity.
```

## Exact review disposition

`L-91843` is not shown false as a possible theorem after additional construction. Its submitted proof has a load-bearing type gap.

```text
operation order                              useful and explicit
positive ownership at omissions/thinning     verified
first-owner and causal source partitions     verified conditionally
signed mismatch as positive source stage     unproved
port as source-measure stage                 category mismatch
source-derived native root identity          unproved
one-shot complement after feasibility        valid alternative
```

## Minimal repair

For the preferred one-shot route, delete the claim that stages 11–14 are positive source partitions and prove only the following concrete theorem:

1. define the positive endpoint measure and final row `d_X` explicitly;
2. prove `d_X>=0`;
3. prove `Xi(d_X)<=Omega_X` on every physical column;
4. define `r_X=Omega_X-Xi(d_X)`;
5. price `r_X` directly by `Y_4` using the absolute error and omission estimates.

For a genuinely source-derived recursive route, retain `L-91843` only after constructing positive source packets for every signed comparison and every port class.
