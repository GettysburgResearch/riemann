# M-91302 — Hostile verification plan for the three-route completion

Methodology ID: `M-91302`  
Status: **EXECUTABLE REVIEW PLAN**  
Created: 2026-08-12

## Review A — canonical system

1. Re-derive the Mellin and Fourier conventions.
2. Verify the local `p=2` factor and every zero of that factor.
3. Prove the regularized Hankel truncations are trace class.
4. Check the Fredholm determinant normalization against Suzuki's canonical
   coordinate.
5. Search for a hidden use of innerness in injectivity of `I+/-K`.
6. Run the bad self-dual mask control.

## Review B — Fock colligation

1. Re-derive the one-particle inner product and Fock overlap.
2. Check the scale product system.
3. Verify both Hardy orientations and the bridge.
4. Keep all cross kernels; prohibit diagonal-only proofs.
5. Derive the proposed source/output Gram equality term by term.
6. Run the PR #398 Jordan-preserving control.

## Review C — Brownian/theta DtN

1. Re-derive the BPY normalization of `M(r)`.
2. Verify the Gamma(4)-Beta(2,2) decomposition.
3. Verify the log-odds Sturm–Liouville cell.
4. Verify the theta supersymmetric factorization and the boundary trace.
5. Close the form sum and its boundary triple.
6. Prove the Weyl function equals the Xi impedance, not merely a function with
   similar symmetry.
7. Run the historical Green-stationarity counterexample.

## Blind synthesis review

A fourth reviewer receives only the statement of `AOT_a` and the exact source
definitions. The reviewer must independently derive all three realizations or
find the first missing equality.

## Promotion rule

The proposal may be promoted to a claimed proof only after:

```text
AOT_a is proved for every rational a in one sequence a_j -> 0;
all three hostile reviews pass;
the two RH-false controls fail at the declared boundary-identification joint;
the canonical, colligation, and DtN transfer functions agree exactly;
no sorry, numerical assumption, or target-kernel square root remains.
```
