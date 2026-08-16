# Theorem and lemma ledger — arXiv-ready proposal v1

Frozen live proposal base: PR #524, head `079a80308a218e924d86030c4df40410df960592` (16 August 2026).

## Status key

- **Reproved**: the algebraic argument is written in the manuscript.
- **Reconstructed**: the manuscript gives the complete interface and proof at the level used by the composition.
- **Certified input**: requires a finite exact or outward-rounded artifact.
- **Open / defective**: the audited repository does not presently prove the statement.

| Repository record | Role | Manuscript status | Main location |
|---|---|---|---|
| `L-91870` | Exact native fibre, native/rough separator | Conditional normalization; symbol collision exposed | Sections 2, 3, 7 |
| `L-91880` | Explicit native two-sorted source coupling | Reconstructed | Sections 3–4 |
| `L-91881` | Whole-cell realization in one row | Reproved as Hall residual lemma | Section 4 |
| `L-91882` | Same-row all-column terminal complement | Reconstructed | Section 6 |
| `L-91883` | Direct `Y4` cost; constant 60989 | Reconstructed with normalization caveat | Section 7 |
| `T-91880` | End-to-end native factor-67 successor | Conditional theorem | Section 9 |
| `R-91880` | Three type firewalls and exact counterexamples | Incorporated | Sections 2, 3, 10 |
| `L-91688` | Rough first-owner provenance | Used only for ownership | Section 2 |
| `L-91690` | Factor-67 root Hall and finite margins | Certified input | Sections 4–5 |
| `L-91733` | All-column localization; constants 57, 971, 129 | Certified input | Section 6 |
| `L-91115` | Top collar; 5033/4452/581 reserve | Reconstructed/certified constants | Section 6 |
| `L-19885` | Sparse `Y4` dual and recurrence | Restated | Section 7 |
| `L-19887` | Chebyshev bound for smoothed prime sum | Reproved for `P_Lambda` | Section 7 |
| `L-93782` | Target–Lorenz global certificate | Conditional | Sections 4, 11 |
| `L-93783` | Typed-leaf algebra | Reproved | Section 4 |
| `L-93781` | Directed transcendental tail sweep | **Defective**: singleton `sqrt`/`log` values are not outward enclosures | Sections 10–11 |
| `T-91750` | Prime-square moat and Mellin–Landau endpoint | Restated | Section 8 |

## The certification package `Cert_67`

The manuscript’s main theorem is conditional on these clauses:

1. **N67 — native normalization and benchmark bound.** Expand `R`, `C`, `Xi`, and `H` in one coordinate convention; prove `C(c_X)=w_X`, `Xi(c_X)=Omega_X`, and distinguish the smoothed prime sum `P_Lambda` from the native benchmark `J_nat=H(c_X)`. Prove `J_nat <= 16 log(2) sqrt(X)` or a sufficient equivalent, and verify positivity of the native Volterra atoms.
2. **F67 — compact and tail typed-leaf certificate.** Exact compact Hall data for `67 <= x <= 166000`, plus a genuine outward-rounded certificate for `x >= 166000`.
3. **O67 — outer factor-67 margin.** Certify `L(x)>159/500` for `1 <= x < 67` on all floor-pattern intervals.
4. **L67 — localization.** Verify first-owner carry, no cutoff atom, and the all-column constants `57`, `971`, and `129`.
5. **Terminal reserve.** Verify top removal `>5033 X^{-3/2}`, overfill `<4452 X^{-3/2}`, margin `581 X^{-3/2}`.
6. **Sparse dual.** Verify the `Y4` recurrence/adjunction and its decay bound.
7. **Endpoint consumer.** Verify prime-square occupancy and the Mellin–Landau normalization/signs.

## Highest-priority review findings

### 1. The current tail program is not a proof

Its interval wrapper receives singleton outputs from standard `sqrt` and `log` calls. Unless correct rounding is proved, the exact real value need not lie in the singleton. Hashes and cross-precision point agreement do not repair this.

### 2. The `J_Lambda` / `P_Lambda` collision is load-bearing

One dependency calls the smoothed prime sum `J_Lambda`; the endpoint consumer calls that same sum `P_Lambda` and reserves `J` for the native benchmark. The thinning charge uses a bound for the benchmark. The PR must not import the Chebyshev bound for the prime sum without proving the identification or an independent benchmark bound.

### 3. Type firewalls are mandatory

- Complete residual sources are recursively usable.
- Current-only row bonuses are not target-bearing and cannot be recursed.
- Signed errors are observations, not positive sources.
- The Volterra fibre `p_s` must remain unsplit.
- Rough-prime provenance is not native-marginal equality.

## Bottom line

The PDF is the strongest dependency-closed *conditional proof proposal* that could be reconstructed from the live graph. It does not claim RH is proved. Closure requires a sound `Cert_67` package, with the tail and normalization clauses currently open.
