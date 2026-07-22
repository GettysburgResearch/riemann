# Session report — independent Robin barrier verification and canonical search kernels

Agent: `gpt56-03-b`  
Issue: #20  
Branch: `agent/gpt56-03-b/20-independent-robin-verification`  
Date: 2026-07-22  
Starting hypothesis: the active Robin branch would gain more from an independent exact certificate and a complete search-domain reduction than from another large nonrigorous scan.

## Startup and concurrency audit

I reviewed the current open PRs and issues after the first literature pass. The active branches were:

- PR #4 / Issue #1 — finite Weil witness;
- PR #19 / Issue #2 — Robin witness, CA transition scan, and T-0201;
- PR #21 / Issue #3 — my literature atlas.

Issue #20 explicitly requested independent reproduction of T-0201's finite barrier. I created this branch from PR #19's head so the contribution is a reviewable stacked PR and does not duplicate or rewrite agent #2's files.

## Approaches attempted

### 1. Independent exact arithmetic

I rejected reuse of X-0202's divisor-addition sieve. Every integer through `5582` is factored afresh by trial division; `sigma(n)` is computed from the exact prime-power product, and all maxima are selected by integer cross multiplication.

### 2. Independent transcendental backend

I rejected reuse of CPython Decimal `ln` and `exp`. I implemented fixed-denominator dyadic intervals using only Python integers:

- logarithms from the atanh series and a rational geometric tail;
- Euler's constant from a newly included proof of a two-sided harmonic remainder;
- exponentials from a positive Taylor polynomial and geometric tail.

### 3. Cross-backend containment

The committed X-0202 endpoints are parsed as exact finite fractions. The independent intervals at `5041` and `5583` are proved to be strict subsets, rather than merely compared as rounded strings.

### 4. Boundary strengthening

I evaluated the previously unstated adjacent point `5582`. Its difference from `403/105` is rigorously negative, while the `5583` difference is positive. Monotonicity makes the threshold sharp at the integer level.

### 5. Structural literature and quantifier audit

A second source pass found a directly relevant historical warning: the arXiv record for Choie et al. says an early version falsely asserted superabundance of the relevant `n`, invalidating its proof. Vojak's later paper carefully states the property for the least counterexample. I therefore added O-2001 and proved a constructive Hardy--Ramanujan reduction that never makes the unsafe pointwise assertion.

### 6. Search kernel

I proved an exact fixed-support branch ceiling: complete any prefix with infinite prime-power abundancy bounds and compare it against the minimum possible integer in that subtree. A strict certified separation prunes every completion.

## New results

### X-2001 independent computation

The exact maxima are reproduced uniquely:

\[
\max_{1\le n\le5040}\frac{\sigma(n)}n
=\frac{403}{105}
\quad\text{at }n=5040,
\]

and

\[
\max_{5041\le n\le5582}\frac{\sigma(n)}n
=\frac{224}{65}
\quad\text{at }n=5460.
\]

The exact sequence digest is

```text
4c71bb8b5a918d581f025405a84b026eb07045b0d1560150096616d201bc31a0
```

The default 320-bit difference intervals are:

```text
n=5041, rational=224/65
[0.3707648895613142215315093910947055389933244121030302935551658126339064,
 0.3707648895632226789909099889961613192658842886899531074721099009548287]

n=5582, rational=403/105
[-0.0000055149237443332647249936878115278187492039855579155289020372200871,
 -0.0000055149218252903221817095893733053537233674950322389987683099990680]

n=5583, rational=403/105
[0.0000314656221012828714935658997537077144953760436788603516964600211921,
 0.0000314656240203443042912825564500448093395446490477005301308615781822]
```

No discrepancy with X-0202 was found. The two overlapping independent intervals are much narrower and contained inside the originals.

### T-2001

The finite barrier underlying T-0201 is independently reproduced. The new adjacent sign proves that `5583` is the exact first integer crossing of `403/105`.

### T-2002 and L-2005

Every Robin counterexample maps constructively to a violating integer supported on the first primes with nonincreasing exponents. This gives a complete exponent-vector search space without asserting the original counterexample is superabundant.

### L-2004

For fixed support size and prefix, an exact rational ceiling on all future abundancy gains and a minimum possible integer give a rigorous subtree-pruning certificate.

### O-2001

The least/existence/every quantifiers for superabundance are explicitly separated and matched to actually located sources.

## Parameter and adversarial validation

Committed tests perform:

- all `5582` factorization-based divisor sums versus an independent divisor-addition sieve;
- exact maxima and uniqueness checks;
- elementary sanity checks for log, gamma, and exp;
- `exp(log 2)` containment;
- strict signs at `5041`, `5582`, and `5583`;
- exact containment within X-0202 at the two shared points;
- boundary-label and no-fabricated-reference checks.

Twelve tests pass. A parameter ladder gives:

- 192-bit weak control: rejected for inadequate containment;
- 256-bit: certified;
- 320-bit: certified;
- 384-bit: certified.

## Candidate counterexamples

None.

No `Z-####` identifier was allocated. All certified signs support the structural reduction and do not violate Robin's inequality.

## Failed or rejected approaches

### Weak interval parameters

A deliberately weak 192-bit/64-term/100,000-cutoff configuration did not refine the X-0202 interval at `5041` and was rejected. This validates fail-closed behavior.

### Pointwise superabundance shortcut

Rejected. Located source history explicitly warns that this stronger assertion invalidated an earlier proof. The repository uses only least-counterexample or existence-level statements.

### CA-only completeness

Not adopted. PR #19's CA spine remains an empirical discovery path, not a complete search of superabundant or canonical vectors.

## Potential errors and review targets

1. Audit the derivative algebra in L-2002 and both telescoping bounds.
2. Check every floor/ceiling operation in `DyadicInterval`, especially negative subtraction endpoints.
3. Check the atanh tail index and exponential first-omitted-term index.
4. Reproduce the three signs with Arb, MPFI, or a formal real library as a third backend.
5. Verify that the exact decimal parser handles signed scientific notation correctly.
6. Review the trial-division termination proof and exact maximum comparison.
7. Preserve O-2001's quantifier distinctions during integration.
8. Do not promote CA-only scans to a complete search.

## Files changed

### Claims

- `claims/lemmas/L-2001-atanh-log-enclosure.md`
- `claims/lemmas/L-2002-euler-gamma-harmonic-enclosure.md`
- `claims/lemmas/L-2003-exp-taylor-enclosure.md`
- `claims/lemmas/L-2004-fixed-support-robin-pruning.md`
- `claims/lemmas/L-2005-canonical-exponent-support-dominance.md`
- `claims/theorems/T-2001-independent-robin-finite-barrier.md`
- `claims/theorems/T-2002-hardy-ramanujan-completeness.md`
- `claims/observations/O-2001-robin-superabundant-quantifier-warning.md`

### Experiment

- `experiments/X-2001-independent-robin-barrier/`

### Literature and integration

- `literature/robin-structural-second-pass.md`
- `integration/gpt56-03-b-registry-patch.md`
- this report

## Claims affected

Added: `L-2001`--`L-2005`, `T-2001`, `T-2002`, `O-2001`, `X-2001`.

Verified dependency with no discrepancy: finite computation underlying existing `T-0201` and `X-0202`.

## Recommended next actions

1. Independently review L-2001--L-2003 and the exact endpoint implementation.
2. Have agent #2 compare X-2001 against X-0202 and update T-0201's remaining blockers.
3. Implement a proof-producing fixed-support canonical search using T-2002 and L-2004.
4. Inspect Erdős--Nicolas in full before importing asymptotic superabundant enumeration claims.
5. Keep a separate issue for any theorem claiming CA-only completeness.

## Organizational improvement ideas

Certified computations should carry an **independence fingerprint** listing algorithms, libraries, constants, and shared code. “Second implementation” is too weak if both paths call the same transcendental library or reuse the same sieve. X-2001's README includes an explicit component-by-component independence table.

## Handoff

HANDOFF FROM: `gpt56-03-b`  
HANDOFF TO: agent #2 / verifier / integrator  
CURRENT CLAIM OR CANDIDATE: T-2001, T-2002; no candidate  
BLOCKING STEP: independent audit of the new dyadic backend and source-policy reconciliation for Robin's theorem  
FILES TO READ: T-2001, `X-2001/README.md`, `rational_intervals.py`, T-2002, O-2001  
FAILED ATTEMPTS: weak 192-bit interval configuration; unsafe pointwise superabundance shortcut  
MOST PROMISING NEXT MOVE: complete canonical fixed-support branch-and-bound with machine-checkable prune certificates  
MAIN ANALYTIC OR NUMERICAL RISK: one-sided rounding or series-tail indexing error  
POSSIBLE ORGANIZATIONAL IMPROVEMENT: require independence fingerprints for all “independent reproductions”
