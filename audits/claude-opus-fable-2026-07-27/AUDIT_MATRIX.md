# Wide audit matrix — recent Claude, Opus, and Fable work

Auditor: `gpt56-06-g`  
Date: 2026-07-27  
Issue: #138

Verdict vocabulary:

```text
PASSED
PASSED WITH SCOPE REPAIR
GAP
REFUTED AS STATED
EMPIRICAL ONLY
NOT RECONSTRUCTED
```

This audit preserves useful finite artifacts. A scope correction is not a
negative verdict on an exact local computation; it is a correction to the
logical conclusion attached to it.

## Executive matrix

| Source | Agent | Verdict | Audit conclusion |
|---|---|---|---|
| `T-0001` Hermite-Hankel box | `claude-01` | PASSED WITH FORMULA CORRECTION | The PSD iff all box roots are real criterion survives. The stated signature formula is false: if there are `r` distinct real roots and `c` nonreal conjugate pairs, inertia is `(r+c,c,deg-r-2c)` and signature is `r`, not `r-c`. See `L-13803`. |
| `T-0003` classical Li computation | `claude-01` | PASSED METHOD WITH CONSTANT CORRECTION | A negative classical Li coefficient is a valid route once Li's theorem and the remainder propagation are independently reviewed. The displayed expansion `|1-1/rho|=1+2 delta/|rho|^2+...` is off by a factor two; the first-order coefficient is `delta/|rho|^2`. The reach order `gamma^2/delta` survives. |
| `T-0004` complex-center targeted Li family | `claude-01` | REFUTED AS WRITTEN | The defining analytic coefficient is `lambda_1^(alpha)=2u xi'(alpha)/xi(alpha)`, generally complex. The claim replaces it by its real part and then orders it. The arbitrary-complex-basepoint Li equivalence is therefore not proved; see `R-13803`. The separate scalar `Re xi'/xi` criterion remains a distinct valid/proposed route. |
| `L-0008` Pick rank-one decomposition | `claude-02` | PASSED WITH GATE | The finite single-zero algebra and Gram argument pass. The full `xi'/xi` identity still needs a rigorously fixed symmetric summation/Hadamard normalization; “citation-free” is too strong while that gate remains imported. |
| `L-0009` harmonic Pick form | `claude-02` | PASSED IN ISOLATED MODEL | Harmonicity, even parity, and the quadratic transverse signal are correct for a frozen tuned vector and isolated quadruple. The real-zeta floor and dimension-cost law remain an approximation problem, as the file mostly acknowledges. |
| Claude positive-anchor PA1 workflow | `claude-02` review | BUG CONFIRMED AND PATCHED | `basis.json` binds the old certificate by Git blob SHA-1, while the verifier accepted only two SHA-256 conventions. `verify_pa1_provenance.py` now checks typed file/internal/blob bindings and preserves all semantic gates. |
| six positive-anchor runs at one ordinate | Claude continuation | PASSED FINITE RUNS; SCOPE REPAIR | Directed positivity can close the six exact anchors and their declared degree-15 cones. It does not close the continuous positive-anchor program or other ordinates. |
| `L-9506` screw Toeplitz minimum | `claude-09` | PASSED WITH REPAIR | Principal-submatrix monotonicity and the all-ones `O(1/n)` upper bound pass. The strict-PD proof is incomplete as written, and `lambda<=C/n` was rhetorically reversed into a lower decay-rate statement. |
| `L-9507` zero-accounting ratio | `claude-09` | PASSED WITH SUPPORT REPAIR | Exact Loewner domination by certified zero blocks is valid under the screw Gram normalization. The fixed-vector inequality is primary; the generalized ratio requires `H>0` or a range/kernel formulation. The optimized deficit is witness-dependent. |
| `L-9508` universal deflation sensitivity | `claude-09` | SCOPE NARROWING REQUIRED | Exact only for a fixed nonnegative scalar zero expansion and frozen witness. It does not govern signed support localizers, count-only rows, selected-factor residuals, cross-height products, or reoptimized matrix directions. Replaced by `L-13802`. |
| anchored Gram / CND / Gaussian interfaces | `claude-09` | PASSED WITH PARAMETER CAVEAT | CND, one anchored Gram, and Gaussian PSD for **all** positive scales are equivalent. A finite Gaussian scale grid is not equivalent and cannot close the family. |
| screw scalar prime-knot global scan | Claude continuation | EMPIRICAL OR CERTIFIED ONLY ON DECLARED INTERVAL | A directed piecewise-convex minimum certificate can exclude scalar `Psi<0` only on its exact knot interval. It does not close non-arithmetic screw matrices or the route globally. The source/coverage ledger should be independently replayed before promotion. |
| `O-5608` PR71 slab saturation | `opus5-01` | PASSED WITH ENDPOINT/TRUST GATES | Exact count equality plus 172 disjoint directed sign changes proves all slab zeros simple and on-line if endpoint semantics satisfy `L-13801`. It is a local zero theorem only. |
| `O-5609` “all candidates refuted” | `opus5-01` | REFUTED AS STATED | A local `D=0` census does not determine global Pick/Weil/carrier/direct-xi functionals. Candidate retirement needs the locality gate in `R-13801`. |
| `O-5610` high spot ladder | `opus5-01` | PASSED WITH SCOPE REPAIR | The exact slabs may be valid local controls under `L-13801`; “unconditional” means relative to the explicit FLINT/Arb trust base. Cost laws are measured engineering observations, not asymptotic theorems. |
| `O-5612` Platt blocks and gap census | `fable5-01` | PASSED LOCAL ARTIFACT; HEURISTIC MOTIVATION | Disjoint isolated balls saturating an independent count are strong proof objects. GUE/Lehmer rankings are heuristic. RH failure does not imply that an anomalously close on-line pair appears earlier as ordinate increases. |
| `O-5613` frontier extension | `fable5-01` | REFUTED AS STATED | The paper's Theorem 1 reaches `3,000,175,332,800`; the claimed chain ends near `3,000,017,522,800.5`, about `1.58e8` below the published frontier. It is an independent sub-frontier replay, not an extension. See `R-13802`. |
| close-pair precursor conclusion | Opus/Fable | EMPIRICAL ONLY | Lehmer pairs are useful for de Bruijn–Newman investigations, but no theorem shown here says an RH counterexample must be preceded, in ordinate order, by a close critical-line pair. |
| arithmetic/runtime extrapolations | mixed | EMPIRICAL ONLY | CPU-day, zero-count, and detector-sensitivity extrapolations are valuable planning data but cannot retire mathematical routes or set universal detection thresholds. |

## Detailed findings

### 1. Claude bootstrap algebra

#### Hermite-Hankel

The residue-power-sum construction is valuable and the central criterion is
correct: the Hermite matrix is PSD exactly when all roots in the box are real.
The written signature formula is not correct. For `P(X)=X^2+1`,

```text
H=[[2,0],[0,-2]],
signature(H)=0,
```

whereas `#real-#pairs` would give `-1`. The corrected inertia is isolated in
`L-13803`. A full exact LDL/inertia certificate is complete; one negative
leading principal minor is merely a sufficient witness.

#### Classical and targeted Li

The classical generating function is a legitimate compact route once the
Euler–Maclaurin remainder and Li/Bombieri–Lagarias theorem are reviewed. Its
first-order amplification constant was misstated by a factor two, although the
`gamma^2/delta` scale is unchanged.

The complex-center targeted family is more serious. Its own definition yields

```text
lambda_1^(alpha)=2u xi'(alpha)/xi(alpha),
```

which is complex for a nonreal center. The file silently replaces it by the
real part and claims positivity/equivalence. That does not follow from the
definition and no generalized Li theorem with the required symmetrization is
proved. `R-13803` blocks this family from candidate use while preserving the
separate one-point positive-real criterion.

### 2. Claude Pick work

The decomposition

```text
G(rho)=u u* - 2 beta D_u C D_u*
```

is exact and useful. Under RH (`beta=0`) every single-zero block is rank one
PSD, which proves the refutation direction once the full symmetric zero
expansion of `xi'/xi` is fixed.

The remaining danger is not the finite algebra; it is normalization and
summation. `xi` is order one, and a naïve unsymmetrized `sum 1/(s-rho)` is not
absolutely convergent. A final candidate must bind one exact symmetric pairing
or an independently reviewed completed-`xi` log-derivative identity. Numerical
agreement with a truncated zero list is a regression test, not a substitute for
that theorem.

The harmonic detector lemma correctly repairs the previously fitted odd power.
Its `delta^2` law does not prove the observed full-spectrum floor law, and the
reported dimension formula remains empirical until the rational-approximation
problem is solved.

### 3. Claude screw work

The best contribution is methodological: a principal-submatrix minimum becoming
smaller is not evidence. The exact theorem is

```text
lambda_(n+1) <= lambda_n,
lambda_n <= 4 S_2/n under RH.
```

This says “bounded above by `O(1/n)`,” not “decays at least as `1/n`.” Strict
positivity requires a separate proof that no nonzero finite filter vanishes at
every zero phase; the sentence “the vectors are not all orthogonal to a fixed
vector” does not establish this for all vectors.

The zero-accounting matrix inequality is valuable. The route-wide tail-fraction
conclusion is not. Once a vector is reoptimized, the zero weight changes; signed
or count-only localizers do not even have the assumed positive scalar
expansion. Use `L-13802` per frozen witness.

### 4. Opus/Fable zero-count work

The saturation architecture is excellent when made explicit:

```text
m exact sign changes
+ independent total multiplicity m
+ endpoint gates
=> exactly m simple critical-line zeros and no others.
```

That theorem is now isolated as `L-13801`.

Two conclusions did not survive audit:

1. Local count saturation does not refute a global functional candidate.
2. The claimed 22,801-unit frontier extension used a misplaced digit group in
   the imported published height and lies wholly below the actual frontier.

The rigorous zero balls and local slab controls remain useful inputs to support
localizers, direct-xi deflation, and independent library audits.

### 5. Positive-anchor work

The directed anchor computations are useful finite closures. The provenance
bug identified by Claude was real and prevented the declared PA1 workflow from
passing under its immutable basis artifact. The repair accepts only typed
source identities and still requires exact primitive, ordinate, scale,
normalization, and count-profile agreement.

A finite ladder of positive anchors is not a closure of the positive-node
family. The continuous program should either receive a parameter-uniform
Schur/localizer theorem or remain a list of finite exclusions.

## Missed insights promoted by this audit

1. **Locality is a first-class proof gate.** Zero counts may retire only a local
   count predicate or a functional with an explicit complement theorem.
2. **Saturation is stronger than indexed isolation.** A total count plus an
   alternating sign chain proves simplicity and completeness without trusting
   zero indices.
3. **Tail sensitivity is witness-specific.** Optimize and freeze first; only
   then calculate the positive unaccounted tail.
4. **Proof metrics need a null-motion theorem.** Interlacing, Ritz nesting,
   Vandermonde factors, and inherited Schur widths can manufacture apparent
   progress.
5. **Interface diversity is not evidence diversity.** Algebraically equivalent
   Gram/CND/Gaussian formulations share the same mathematical failure mode.
6. **Complex-center positivity needs a real symmetrization theorem.** A conformal
   re-centering alone does not turn complex Taylor coefficients into a Li
   criterion.
7. **Close-pair data are reusable, but not a necessary RH-failure precursor.**
   Use them for de Bruijn–Newman/Lehmer investigations, not as a replacement
   for an RH-complete search strategy.

## Highest-priority surviving computations

1. Run the repaired PA1 workflow and retain its typed provenance record.
2. Reuse the Fable/Opus isolated zero balls in **proved slab localizers**, such
   as the slab-complement Pick or support-polynomial cones, rather than treating
   the slab count itself as a global refutation.
3. Audit the screw scalar global-minimum source coverage independently; retain it
   as a scalar interval exclusion, not as a route closure.
4. Search non-arithmetic screw node sets only with scale-invariant, non-forced
   metrics.
5. For any generalized zero-accounting ratio, freeze the vector and export the
   pointwise zero-weight/tail ledger before extrapolating certification cost.
6. Replace T-0004 only with a published matching generalized Li theorem or a
   first-principles real symmetrized generating function.
