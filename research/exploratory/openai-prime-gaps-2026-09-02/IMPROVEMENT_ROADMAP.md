# Improvement roadmap

```text
Status: PROPOSED EXECUTION PROGRAM
Ordering principle: eliminate trust gaps first; optimize only through modular interfaces
RH status: unproved
```

## 0. Ranked priorities

1. **Delete the physical-integral axiom from `PrimeGaps186`.** It is finite, explicit, and already has an external checker.
2. **Independently review `LongGapsBetweenPrimes.long_gap_theorem`.** It is the nearest source to a promotable unconditional theorem.
3. **Extract the common prime-gap library.** Definitions and elementary bridges should not remain duplicated in monoliths.
4. **Parameterize both proofs before optimizing them.** Constants should be fields in theorem inputs, not hard-coded throughout generated code.
5. **Attack the two Kloosterman inputs as standalone finite-field formalization projects.** They are the deepest trust gap in the 186 theorem.
6. **Build the explicit-formula/RH bridge separately.** No gap endpoint should be relabeled as an RH criterion.

## 1. Track A — close the bounded-gap trust boundary

### A1. Physical-certificate kernelization

**Target theorem**

```lean
 theorem physical_integral_bounds_of_certificate
   (cert : PhysicalCertificate fixedTrialData)
   (hcert : CheckPhysicalCertificate cert = true) :
   PrimeGap186.physical_integral_bounds
```

**Design**

- replace the 152-clause opaque conjunction with a typed record indexed by the exact outer rows, inner rows, and scalar caps;
- use rational endpoints for every mesh cell and every claimed enclosure;
- separate optimizer output from checker input;
- provide analytic lemmas for exponential, polynomial, rational-profile, measure, and integral enclosures;
- make the final checker small enough for line-by-line review;
- combine per-row theorems automatically and remove the global axiom.

**Soundness rule**

The checker may use generated rational data, but no floating-point comparison may occur in the trusted path. Transcendentals require proved rational enclosures with explicit remainders or monotonicity bounds.

**Success criterion**

`#print axioms PrimeGap186.primeGapLiminf_le_186` no longer lists `physical_integral_bounds`.

### A2. Clean-room numerical replay

Run the upstream Python certificate in two independent environments:

- the documented NumPy/python-flint/FLINT stack;
- a second implementation using a different arbitrary-precision interval engine.

Compare every row by a canonical JSON key, not by aggregate pass/fail. Deposit:

```text
input hash
software lock
all 152 lower/upper margins
rounding mode
checker transcript
output hash
```

This does not replace A1, but it catches transcription and library-patch errors before proof-object work.

### A3. Rank-three Kloosterman theorem

**Target abstraction**

```lean
 theorem normalized_hyperKloosterman3_bound
   (p : Nat) [Fact p.Prime] (c : ZMod p) (hc : c != 0) :
   norm (normalizedKloosterman3 p c) <= 3
```

**Subprojects**

1. identify the exact classical hyper-Kloosterman theorem and normalization;
2. prove equivalence between its finite-field character notation and the source's nested `ZMod` sum;
3. isolate the geometric/cohomological input behind a narrow audited interface;
4. handle all small-prime cases directly;
5. prove the stated constant after normalization.

A bibliographic wrapper axiom is useful documentation but is not final closure. Full removal likely requires a serious finite-field cohomology or equivalent trace-formula library.

### A4. Kloosterman correlation theorem

**Target abstraction**

```lean
 theorem kloosterman2_shifted_correlation_bound ... :
   norm correlation <= 8 * p * sqrt p
```

**Required theorem analysis**

- rewrite the sum as a correlation of trace functions under two rational maps;
- compute conductors and singular loci;
- classify geometric isomorphism or duality exceptions;
- prove the source assumptions on `A,B` exclude every exceptional case, or add the missing exclusions;
- derive the exact constant 8, not only an unspecified `O(p^(3/2))`;
- discharge `p=2,3` separately if the geometric theorem assumes larger characteristic.

This is the most technically difficult bounded-gap closure task. It should remain independent from trial-function optimization.

### A5. Toolchain stabilization and modular extraction

Port reviewed theorem modules to the stable Riemann generation or retain an explicit multi-toolchain package. Proposed module split:

```text
PrimeGaps186/FiniteField.lean
PrimeGaps186/SieveAbstract.lean
PrimeGaps186/TrialData.lean
PrimeGaps186/PhysicalCertificate.lean
PrimeGaps186/DHL.lean
PrimeGaps186/AdmissibleTuple186.lean
PrimeGaps186/Main.lean
```

Generated tables should live in data modules; conceptual proofs should remain readable.

## 2. Track B — improve the number 186

### B1. Separate the `(k,D)` frontier

Create a machine-readable frontier:

```text
k
best known certified admissible diameter D
sieve positivity margin for DHL[k,2]
certificate hash
formal theorem status
```

The final theorem constructor should accept any certified row. This makes it possible to improve the bound without editing the analytic core.

### B2. Search for a tighter admissible 40-tuple

Run an exact branch-and-bound or SAT/ILP search for forty distinct shifts in `[0,D]`, beginning with `D=185` and descending only after a certificate is found. Admissibility can be checked finitely:

- for primes `p<=40`, verify the tuple does not occupy all residue classes;
- for `p>40`, cardinality alone prevents full coverage.

Emit the tuple and residue omissions as a Lean-checkable finite certificate. A successful `D<186` result improves the endpoint without changing the analytic theorem.

Do not assume such a tuple exists; the search can instead certify nonexistence inside a declared search class.

### B3. Sensitivity analysis of the 152 inequalities

For each clause record:

```text
certified margin
contribution to the final sieve inequality
derivative/sensitivity with respect to trial coefficients
rounding loss
mesh-discretization loss
```

The clauses with the smallest normalized slack identify which angular signatures, radial coefficients, or caps deserve re-optimization. This is more informative than globally rerunning the optimizer.

### B4. Parameterized trial-function optimization

Replace the fixed coefficient table by a finite-dimensional rational family with:

- symmetry constraints enforced algebraically;
- exact objective and constraint maps;
- a floating optimizer used only to nominate candidates;
- rational reconstruction;
- interval proof of feasibility and objective margin;
- deterministic Lean certificate generation.

Candidate improvements include a larger radial basis, alternative two-pole profiles, adaptive rather than uniform mesh cells, and direct optimization of the final positivity margin.

### B5. Move from `k=40` to a better sieve threshold

Attempt the theorem-sized targets in order:

```text
DHL[39,2]
DHL[38,2]
...
```

For each `k`, pair the analytic margin with the best exact admissible-tuple diameter. A lower `k` is useful only when the tuple frontier actually improves the final `D`.

The proof search should expose which input is limiting:

- physical trial function;
- Kloosterman correlation constant;
- a Cauchy-Schwarz or dispersion loss;
- a combinatorial sieve coefficient;
- a rounding/certificate loss.

### B6. Stronger distribution input

Investigate whether a sharper trace-function correlation theorem, a broader bilinear estimate, or a better decomposition raises the effective distribution level. This is a genuine analytic-number-theory project, not a numerical retuning. Any new input must be stated as a standalone theorem and tested against the same parameterized sieve API.

## 3. Track C — certify and sharpen long gaps

### C1. Independent theorem audit

Review in dependency order:

```text
random-sieve probability space
collision and covariance lemmas
L2/L3 concentration and tail bounds
short_translates_with_sieveDelta
small_primes_residue_choice
full-cover assembly
prime_gap_from_full_cover
asymptotic conversion
long_gap_theorem
```

The first deliverable is a frozen statement-equivalence report and exact `#print axioms` transcript, not a refactor.

### C2. Abstract `ShortTranslates`

Turn the current predicate into a theorem parameterized by:

```text
sparsity delta
height H
base scale x
allowed translation range T(x)
prime bands
success probability/moment constants
```

Prove the current theorem by instantiation. This exposes the true interface consumed by the Erdos-Rankin reduction and allows stronger future sieve inputs to drop in.

### C3. Constant ledger

Replace anonymous inequalities by a ledger carrying every loss:

```text
small-prime uncovered-set constant
short-translates sparsity constant
medium-prime allocation loss
large-prime cleanup loss
coverEta
location exponent 8
cover-to-gap factor 16
X-scale factor 128
```

Prove monotonicity of the final constant with respect to ledger fields. Optimize the ledger only after the original proof is reviewed.

### C4. Explicit thresholds

The current eventual proof can be strengthened to return a computable `X0` from explicit parameter inequalities. The resulting value may be enormous; its purpose is auditability and executable testing, not practical prime-gap discovery.

### C5. Deterministic short-translates certificates

For finite parameter instances, derandomize the translate choice or emit a witness residue assignment. This supplies regression tests for the abstract probabilistic proof and can reveal hidden endpoint errors.

### C6. Improve the asymptotic scale

A genuine order-of-magnitude improvement requires a stronger covering/sieve theorem, not only constant cleanup. Keep the reduction parameterized so that any improved sparse-set covering input immediately yields a new `gapScale` theorem. State the new input first; do not bury it inside asymptotic arithmetic.

## 4. Track D — common formal analytic-number-theory infrastructure

### D1. Prime-gap definitions

Create one reviewed definition set for:

- `ConsecutivePrimes`;
- `primeGap n`;
- `primeGapLiminf`;
- `MaxPrimeGapBelow X`;
- finite and eventual gap predicates;
- conversion between nth-prime and existential-consecutive-prime formulations.

### D2. Admissibility and covering duality

Bounded-gap admissibility says a tuple omits at least one residue class modulo each prime. Long-gap covering deliberately chooses residue classes whose union covers an interval. Formalizing both in one residue-incidence language may yield reusable duality lemmas, certificate formats, and search code even though the analytic goals are opposite.

### D3. Exact arithmetic certificates

Build a generic certificate layer for:

- finite tuples and residue omissions;
- residue covers and CRT witnesses;
- rational inequalities;
- interval enclosures;
- table cardinality and index completeness.

The trusted checker should be independent of optimization/search programs.

### D4. Asymptotic calculus

Extract robust lemmas for iterated logarithms, eventual positivity, substitutions `x=a log X`, and comparison of explicit scales. This is useful throughout the Riemann repository and reduces semantic risk from totalized logarithms.

## 5. Track E — RH-directed research, with the gap firewall intact

The gap packages can support an RH program only after a signed prime-distribution interface is installed. The target architecture is

```text
von Mangoldt/Chebyshev source
        -> exact Mellin transform and explicit formula
        -> all-test-function signed discrepancy or Weil quadratic form
        -> source-admissible canonical system / coefficient extraction
        -> RH.
```

The imported theorems become consequences or stress tests of this source theory; they are not reverse arrows.

### E1. Formal RH-to-upper-gap consequence

From a reviewed explicit-formula theorem, derive an explicit Chebyshev error under RH and then an upper bound for prime-free intervals. This creates a formally verified forward arrow

```text
RH -> square-root-scale upper bound on all sufficiently large prime gaps.
```

It does not use or prove the imported liminf/limsup bounds, but it places them on the same interface.

### E2. Gap-cell decomposition of the prime source

Proposed research theorem: partition the logarithmic prime axis into cells between consecutive primes and derive an exact identity expressing the centered Chebyshev/von-Mangoldt distribution as

```text
local cell boundary terms + local mass defects + prime-power correction.
```

Then seek a Poincare/Wirtinger-type bound converting cell geometry into a quadratic source estimate. The imported small- and long-gap theorems constrain extreme cells. The decisive missing input will still be a uniform signed defect estimate; this project is valuable precisely because it will expose whether gap geometry can contribute anything nontrivial to that estimate.

### E3. Beurling-prime firewall

Attempt to construct generalized-prime systems exhibiting both qualitative bounded-gap and long-gap behavior while their associated zeta functions have off-critical zeros. Such a countermodel would rigorously show that the two extremal gap properties, even together, do not encode RH-level signed cancellation. This is a proposed theorem program, not a result of this packet.

### E4. Finite-field trace-function transfer

The two Kloosterman assumptions are finite-field RH-type inputs. Formalizing them can seed a reusable trace-function library and clarify how geometric RH over finite fields yields cancellation in sieve problems. The classical zeta RH does not follow, but the formal technology—characters, transforms, conductors, correlations, and positivity—may transfer to the repository's L-function programs.

## 6. Definition of completion

The prime-gap import program is complete only when all of the following are separately true:

```text
Long-gap theorem independently reviewed at exact SHA
Physical-integral axiom deleted by a kernel-checked certificate
Both Kloosterman axioms discharged or explicitly retained as named external theorems
Common definitions extracted without changing statements
Every improvement has a parameter/certificate record and exact replay
No gap theorem is registered as an RH implication
```

A complete solution of RH would additionally require closure of the explicit-formula positivity/cancellation gate described in `RH_BRIDGE.md`; none of the tasks above silently supplies it.
