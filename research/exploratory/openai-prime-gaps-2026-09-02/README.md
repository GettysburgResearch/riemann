# OpenAI prime-gap imports: exact source locks and research front door

```text
Status: IMPORTED / REVIEW_PENDING
Scope: one conditional bounded-gap theorem; one unconditional long-gap theorem
Riemann Hypothesis: UNPROVED; neither imported theorem implies RH
Riemann base: main@6dda8b5125457ed936330229f8c9eb6491728e76
Initial import date: 2026-09-03
Paper-link update: 2026-09-04
```

This packet imports and audits the two OpenAI prime-gap repositories published
on 2026-09-02. The upstream repositories are present as exact gitlinks rather
than copied or silently normalized source trees. Their own licenses, histories,
toolchains, numerical artifacts, and trust boundaries remain visible.

The subsequent publication of **Improved Long Gaps Between Primes** fits this
same packet. The already-imported long-gap proof commit is retained as the
authoritative gitlink, while the later documentation commit that adds the paper
URL is source-locked separately.

## Exact imports

| Upstream | Exact proof commit | Upstream ref | Lean toolchain | Local gitlink |
|---|---|---|---|---|
| `openai/PrimeGaps186` | `61340d0b74163003b32756bb16e91d9209a5e330` | `main` | `leanprover/lean4:v4.34.0-rc2` | `research/exploratory/imports/openai-prime-gaps-2026-09-02/PrimeGaps186` |
| `openai/LongGapsBetweenPrimes` | `8f5fa88c88b4750028c05b66b081d56a92418054` | `master` | `leanprover/lean4:v4.33.0` | `research/exploratory/imports/openai-prime-gaps-2026-09-02/LongGapsBetweenPrimes` |

Both upstream repositories declare Apache-2.0. The exact machine-readable lock
is in [`SOURCE_LOCK.json`](SOURCE_LOCK.json).

Initialize the imports with:

```bash
git submodule update --init --recursive \
  research/exploratory/imports/openai-prime-gaps-2026-09-02/PrimeGaps186 \
  research/exploratory/imports/openai-prime-gaps-2026-09-02/LongGapsBetweenPrimes
```

The gitlinks, not the moving upstream branch names, are authoritative.

## Long-gaps paper publication lock

The paper is:

```text
OpenAI
Improved Long Gaps Between Primes
source location: Theorem 1.1 and Proposition 1.2
```

The public source URL and theorem alignment were added upstream at:

```text
03a1190d0bc5502d9f54eeb60ad3e45e22b0df0b
```

That commit is the direct child of the imported proof commit and changes only:

```text
README.md
formalization.yaml
```

The main Lean source remains blob:

```text
14467e08a1848a43c374b43001f172eab2a71d3c
```

Accordingly, this packet does not move the gitlink merely to acquire a paper
link. It records the proof commit and publication metadata commit separately.

The paper CDN could not be rendered or downloaded in this environment. No PDF
hash or page-level audit is claimed. The exact source and retrieval boundary
are in `LONG_GAPS_PAPER_SOURCE_LOCK.json`.

## The two mathematical endpoints

### Bounded gaps at 186

The exported `PrimeGaps186` endpoint is the conditional statement

```text
primeGapLiminf <= 186.
```

Its architecture is

```text
rank-3 Kloosterman bound
+ rank-2 Kloosterman correlation bound
+ 152 physical-integral inequalities
        -> DHL[40,2]
        -> admissible 40-tuple of diameter 186
        -> infinitely many prime gaps at most 186.
```

The final Lean declaration is conditional on the three named project axioms. A
separate Python/FLINT certificate recomputes the physical inequalities, but the
upstream README explicitly states that running it does not discharge the Lean
axiom.

### Long gaps

The exported `LongGapsBetweenPrimes` endpoint proves that for some `c > 0` and
all sufficiently large `X`, there are consecutive primes `p < q <= X` with

```text
q - p >= c * log X * (log log X)^2 * log log log log X
                  / (log log log X)^2.
```

The paper's scale improves the previous explicit
Ford-Green-Konyagin-Maynard-Tao scale by the unbounded factor

```text
log_2 X / log_3 X.
```

Its central Proposition 1.2 is the formal `ShortTranslates` theorem: every
sufficiently sparse set of offsets in `[1,H]`, with
`H <= x (log x)^2`, can be made simultaneously composite by one translate of a
primorial progression with translating parameter at most `exp(x)`.

The final proof is an Erdos-Rankin residue cover driven by:

```text
exact mean-zero signed divisor weights
+ local residue factors with negative distinct-root covariance
+ weak Mertens/Euler-product estimates
+ a second-moment simultaneous-root argument
+ small/intermediate/large-prime covering
+ CRT and consecutive-prime extraction.
```

Upstream metadata reports a full formalization of Theorem 1.1 and Proposition
1.2 with zero `sorry` and only ordinary Lean/mathlib axioms. Independent
semantic review is still absent.

## Repository decision

These sources are deliberately **not** installed in `formal-v0.1`,
`canonical/`, `claims/`, or `research/integrated/`.

Reasons:

1. `PrimeGaps186` retains three theorem-bearing project axioms, including a
   large numerical conjunction.
2. `LongGapsBetweenPrimes` is substantially closer to an auditable
   unconditional formal theorem, but its review is upstream self-assessment
   rather than independent exact-SHA review.
3. The two upstream packages use different Lean generations; only the
   long-gap package matches Riemann's current Lean 4.33 toolchain.
4. Extremal prime-gap statements are not RH criteria. Treating them as such
   would violate the repository's finite-to-global and implication-boundary
   policies.

## Packet map

- [`MATHEMATICAL_DIGEST.md`](MATHEMATICAL_DIGEST.md): theorem dependency maps and mathematical content.
- [`LONG_GAPS_PAPER_DIGEST.md`](LONG_GAPS_PAPER_DIGEST.md): theorem significance, proof mechanism, paper/formal alignment, Riemann relevance, and improvement program.
- [`LONG_GAPS_PAPER_SOURCE_LOCK.json`](LONG_GAPS_PAPER_SOURCE_LOCK.json): proof-versus-publication commit split and PDF retrieval boundary.
- [`FORMALIZATION_AUDIT.md`](FORMALIZATION_AUDIT.md): trust boundaries, version compatibility, and semantic hazards.
- [`IMPROVEMENT_ROADMAP.md`](IMPROVEMENT_ROADMAP.md): prioritized theorem-sized projects for certification and sharper gap results.
- [`RH_BRIDGE.md`](RH_BRIDGE.md): what an honest bridge from prime distribution to RH would have to prove.
- [`RIEMANN_INTEGRATION_MAP.md`](RIEMANN_INTEGRATION_MAP.md): placement relative to the live repository.
- [`REVIEW_CHECKLIST.md`](REVIEW_CHECKLIST.md): exact-SHA promotion checklist.
- [`REPRODUCE.md`](REPRODUCE.md): checkout and audit commands.

## First recommended execution

The fastest high-value path is three parallel tasks:

1. turn the 152 physical inequalities in `PrimeGaps186` into a small,
   kernel-checked certificate format, thereby deleting one project axiom
   without touching the deep exponential-sum inputs;
2. independently replay and audit
   `LongGapsBetweenPrimes.long_gap_theorem` and
   `LongGapsBetweenPrimes.short_translates`;
3. parameterize the long-gap proof's `kappa=1/8`, cutoff, survivor, and
   location constants, keeping a formal ledger that separates changes to the
   implicit constant from changes to the iterated-log order.

Only after these steps should either source be considered for exact reviewed
extraction into `research/integrated/` or `formal/Experimental/`.
