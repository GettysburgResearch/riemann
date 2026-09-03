# Placement inside the Riemann repository

```text
Riemann base inspected: main@6dda8b5125457ed936330229f8c9eb6491728e76
Import class: exploratory external source
Trusted-spine changes: none
```

## 1. Repository-level assessment

Riemann's trusted release and formal-v0.1 spine intentionally distinguish:

```text
external source
-> exploratory import
-> exact-SHA review
-> extracted integrated packet
-> formal/canonical promotion, when justified.
```

The prime-gap repositories enter at the second stage only. This PR does not modify:

```text
canonical/
claims/
formal-v0.1 or the reviewed formal spine
research/integrated/
production experiment paths
```

The sources remain independently pinned under `research/exploratory/imports/`, while the readable analysis lives in the sibling dossier directory.

## 2. Why submodules are the correct import form

`PrimeGaps186` contains a generated Lean source of roughly ten megabytes, a numerical program, comparator data, and a PDF artifact. Copying selected files would obscure the exact upstream tree and license; copying all files would create a divergent vendor snapshot. Exact gitlinks preserve:

- upstream commit identity;
- upstream directory layout;
- toolchain and lake locks;
- license files;
- numerical and comparator artifacts;
- clean future source-delta review.

The moving upstream branch names are recorded only for context. The gitlink commits are the source of truth.

## 3. Formal placement

### Current state

```text
research/exploratory/imports/openai-prime-gaps-2026-09-02/
  PrimeGaps186                 gitlink
  LongGapsBetweenPrimes       gitlink

research/exploratory/openai-prime-gaps-2026-09-02/
  source lock, digest, audit, roadmap, RH bridge
```

### Future state after review

Only modular theorem extractions should move into Riemann-owned source. A sensible experimental layout is:

```text
formal/Experimental/PrimeGaps/Common/
formal/Experimental/PrimeGaps/LongGaps/
formal/Experimental/PrimeGaps/BoundedGaps/
formal/Experimental/FiniteFields/Kloosterman/
formal/Experimental/Certificates/Intervals/
```

Each extraction must name the upstream SHA and retain a statement-equivalence file. The monolithic upstream files should remain source references rather than being made root imports.

## 4. Interaction with current RH research

The gap imports touch three existing research themes without closing them.

### Arithmetic source and explicit formula

Riemann needs one canonical von-Mangoldt/Chebyshev source contract. Prime-gap consequences can become endpoint theorems once that contract supplies explicit short-interval estimates. The imports offer definitions and tests, not the source theorem itself.

### Mobius and coefficient-extraction gates

Live PR #786 identifies RH-equivalent or stronger signed Mobius gates; live PR #785 isolates a coefficientwise theta-lattice sign. These are qualitatively stronger than extremal gap statements. The imported sieve machinery should not be used to weaken their quantifiers silently.

### Finite-field/L-function machinery

The two Kloosterman assumptions suggest a tractable interface between finite-field spectral bounds and analytic sieve estimates. This can connect to L-function/Frobenius research in the repository, but only after the exact finite-field theorem and normalization are pinned.

## 5. Proposed extraction order

1. `LongGapsBetweenPrimes` statement and axiom audit.
2. Common `ConsecutivePrimes`, gap, iterated-log, primorial, and residue-cover definitions.
3. Full-cover-to-gap theorem.
4. Abstract `ShortTranslates` theorem.
5. Bounded-gap admissible-tuple-to-liminf bridge.
6. Physical certificate checker and fixed trial data.
7. Abstract `DHL[40,2]` theorem.
8. Kloosterman theorem interfaces, followed eventually by proofs.

This order maximizes unconditional reusable content while keeping the deepest assumptions visible.

## 6. Claim and registry policy

No new RH claim ID is allocated by this import. A future reviewed extraction may receive theorem identities for:

- the unconditional long-gap theorem;
- the conditional `K3 + K2C + PHY -> liminf gap <=186` theorem;
- the physical-certificate elimination theorem;
- common elementary prime-gap bridges.

The unconditional 186 endpoint must not be registered until all three project assumptions are discharged. The long-gap theorem must not be marked reviewed until an independent exact-SHA semantic audit is deposited.

## 7. Merge posture

This packet is add-only except for import-index documentation. It can be reviewed in three independent slices:

```text
source locks and gitlinks
mathematical/formal audit
research roadmap and RH boundary
```

A reviewer can accept the provenance import while requesting changes to interpretation without altering the upstream commits.
