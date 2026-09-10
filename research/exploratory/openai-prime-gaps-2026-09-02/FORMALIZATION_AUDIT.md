# Formalization and trust-boundary audit

```text
Status: DESK AUDIT OF EXACT UPSTREAM COMMITS
Independent replay: not performed in this import pass
Promotion status: blocked pending exact-SHA build and semantic review
```

## 1. Audit matrix

| Item | `PrimeGaps186` | `LongGapsBetweenPrimes` |
|---|---|---|
| Exact source | `61340d0b74163003b32756bb16e91d9209a5e330` | `8f5fa88c88b4750028c05b66b081d56a92418054` |
| Source commit | single unsigned root commit | single unsigned root commit |
| Lean toolchain | 4.34.0-rc2 | 4.33.0 |
| Riemann toolchain compatibility | no; isolate or port | yes at major toolchain pin |
| Completed source | `PrimeGaps186.lean` | `LongGapsBetweenPrimes.lean` |
| Comparator scaffold | `Challenge.lean`, intentional `sorry` targets | `Challenge.lean`, intentional `sorry` target |
| Project-specific axioms in endpoint | three | none reported |
| Numerical sidecar | Python/NumPy/python-flint plus documented custom FLINT fix | none required for endpoint |
| Upstream kernel/comparator report | conditional theorem accepted | theorem accepted |
| Independent human semantic review | absent | absent |
| Riemann classification | `IMPORTED / REVIEW_PENDING` | `IMPORTED / REVIEW_PENDING` |

The intentional `sorry` declarations in each `Challenge.lean` are specification placeholders. A raw repository-wide grep is therefore not an adequate theorem audit. The relevant questions are which modules the lake build imports, whether the completed module imports `Challenge`, and what `#print axioms` reports for each exported theorem.

## 2. `PrimeGaps186`: exact trust boundary

### 2.1 What the completed theorem appears to establish

Upstream metadata and source declarations identify the endpoint

```lean
PrimeGap186.primeGapLiminf_le_186
```

as a Lean proof from:

```text
PrimeGap186.kloosterman3_bound
PrimeGap186.kloosterman2_correlation_bound
PrimeGap186.physical_integral_bounds
```

plus standard logical axioms such as `propext`, `Classical.choice`, and `Quot.sound` inherited through mathlib.

A successful kernel check therefore certifies the implication

```text
K3 AND K2C AND PHY  ->  primeGapLiminf <= 186,
```

not the unconditional number-theoretic theorem.

### 2.2 Numerical certificate separation

The upstream numerical program is valuable but currently external to the proof term. Its environment is unusually specific:

```text
Python 3.12.13
NumPy 2.2.6
python-flint 0.9.0
FLINT 3.6.0 with a documented signed-convolution correction
```

Review must answer four independent questions:

1. Does the program recompute every one of the 152 clauses, with no skipped index or duplicated row?
2. Are all transcendental and integral enclosures directed outward rather than rounded heuristically?
3. Does the custom FLINT correction affect only performance or also mathematical soundness?
4. Is there a deterministic proof-object format that Lean can check without trusting Python, NumPy, FLINT, or the optimizer?

Until the fourth question is answered, a passing run is corroboration rather than axiom elimination.

### 2.3 Semantic hazards requiring manual review

- **Kloosterman normalization:** verify the factor `1/p`, additive-character convention, norm, and correspondence to the cited finite-field theorem.
- **Correlation exceptional cases:** verify that `A,B != 0` and the exclusions `t=0,-1` remove every geometric degeneration needed by the intended correlation theorem.
- **Small primes:** inspect `p=2` and any case where `-1=1` or the excluded points collide.
- **Totalized division:** Lean fields define division at zero; the conditional branch must prevent accidental use of those values.
- **Physical-table binding:** every integer table, mesh width, radial/angular coefficient, and cap must be the exact object certified externally.
- **Tuple certificate:** prove cardinality 40, distinctness, minimum 0, maximum 186, and admissibility for every prime.
- **DHL transfer:** confirm that two primes in a translate yield a pair of consecutive primes with no larger separation.
- **Liminf definition:** verify the `EReal` embedding, indexing of `Nat.nth Nat.Prime`, and treatment of initial terms.
- **Generated-file audit:** establish that no auxiliary declaration with a hidden `sorry`, unsafe axiom, or accidental import enters the endpoint.

### 2.4 Toolchain decision

Riemann main pins Lean 4.33. `PrimeGaps186` pins a 4.34 release candidate. The safe options are:

1. preserve the package as an independently built submodule, as this import does;
2. port a reviewed modular extraction to 4.33 and record every source change;
3. add a multi-toolchain external-import CI job without making Riemann's root package depend on it.

Silently changing the root toolchain is not acceptable.

## 3. `LongGapsBetweenPrimes`: exact trust boundary

### 3.1 What the completed theorem appears to establish

Upstream metadata reports that

```lean
LongGapsBetweenPrimes.long_gap_theorem
```

has no project-specific axioms. The expected `#print axioms` output contains only ordinary Lean/mathlib principles. This is a much stronger formal status than the bounded-gap endpoint, but it is still not an independent semantic audit.

### 3.2 Semantic hazards requiring manual review

- **Theorem equivalence:** compare the completed `LongGapTheorem` predicate, `long_gap_theorem`, and the comparator's nth-prime statement in both directions.
- **Consecutive-prime predicate:** confirm strict ordering, primality, and absence of an intervening prime.
- **Location bound:** track `<X` versus `<=X` and whether the upper prime or both primes are constrained.
- **Iterated logarithms:** verify eventual positivity and every denominator before field simplification; small-`X` totalization must be quarantined behind thresholds.
- **Residue conventions:** check zero, positive representatives, and conversion between `ZMod`, naturals, and divisibility.
- **Primorial conventions:** verify whether the endpoint prime is included and that every selected modulus divides the final modulus.
- **Cover interval endpoints:** audit every `Icc`, `Ioc`, and translated interval for an omitted first or last integer.
- **Composite witness:** ensure a covering prime is strictly smaller than the covered translated integer where required, so divisibility proves composite rather than allowing equality.
- **Random-to-existence step:** check measurability, finite probability spaces, and the strict inequality giving positive success probability.
- **Moment and collision bounds:** inspect diagonal/off-diagonal classifications and all finite-cardinality coercions.
- **Prime extraction:** verify that the first prime after the composite block exists and that the preceding prime gives the claimed consecutive pair.
- **Asymptotic conversion:** independently replay the chain from `coverScale x` and `exp(8*x)` to `gapScale X` and the final constant.

### 3.3 Refactoring risk

The source is a single file of roughly five thousand added lines. Refactoring should occur only after exact-SHA review. The first extraction should preserve theorem statements verbatim and move definitions in dependency order; it should not simultaneously optimize constants or rewrite asymptotic conventions.

## 4. Review levels

### Level A: source and build identity

- exact gitlink and source-tree hash;
- toolchain and `lake-manifest.json` lock;
- clean `lake build` transcript;
- comparator replay;
- confirmation that completed modules do not import `Challenge`.

### Level B: kernel boundary

- `#print axioms` for every exported theorem;
- declaration inventory and `sorryAx` search on the compiled environment;
- unsafe declaration/import audit;
- independent verification of generated file and sidecar hashes.

### Level C: semantic theorem review

- source-paper statement against Lean statement;
- every quantifier, asymptotic threshold, normalization, and endpoint convention;
- edge cases and non-vacuity;
- named assumptions compared to the exact classical theorems they are intended to represent.

### Level D: numerical/certificate review

- clean-room replay in a pinned container;
- independent small checker;
- proof-object generation;
- Lean consumption of the proof object;
- deletion of the corresponding project axiom.

### Level E: Riemann promotion

Promotion requires two separate decisions:

1. whether a theorem is mathematically and formally reviewed;
2. whether it belongs in Riemann's stable formal or integrated spine.

A theorem can pass the first decision and remain an external experimental dependency. Neither import currently passes the full promotion gate.

## 5. Immediate audit verdicts

### `PrimeGaps186`

```text
Conditional implication formalized: strong evidence / kernel-reported upstream
Unconditional <=186 theorem: not established in Lean
Physical numerical premise: externally corroborated, not kernel-bound
Kloosterman premises: open in this package
Independent exact-SHA review: absent
```

### `LongGapsBetweenPrimes`

```text
Completed axiom-light theorem: strong evidence / kernel-reported upstream
Project-specific assumptions: none reported
Semantic statement and constant flow: independent review required
Independent exact-SHA review: absent
```

These verdicts justify exact exploratory import, not canonical promotion.
