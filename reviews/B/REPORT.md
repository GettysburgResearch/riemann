# Reviewer B — incomplete working review

**Disposition: NOT READY FOR INTEGRATION. No review PR or new source census has been verified in this run.**

## Assignment and independence

Reviewer B owns programmes #736–#741, #763 and #764. The intended baseline is the post–22 August 2026 integration. Other reviewers' unpublished work is not a dependency. Their outstanding dispositions are pending integrator reconciliation, not failed reviews and not accepted claims.

This file preserves useful historical source leads and mathematical audit questions. It is **not** a completed independent review: the current attempt did not receive readable tool results sufficient to inspect the release manifest, issue discussions, current source files, or publication receipt. Accordingly no historical source summary below is promoted to an accepted scientific disposition. No execution, directed computation, formal build, or exact-SHA fresh proof review is claimed.

## Historical source leads, not a newly verified census

The following identities occur in earlier inspected project material. Revalidate both object existence and file contents before importing a claim. The current heads may differ.

| PR | Historical checkpoint | Why B must inspect it |
|---|---|---|
| #766 | `17c7624a0bd56c5356d00278b2a846d2efdbdccc` | Modular source quotients, coefficient flags, Poincare/Hecke constructions, representation calculations. |
| #769 | `f36576faf7853a56bd1f64edd29c4df662cae849` | Ternary Chow/Segre source, syzygies, computation artifacts. |
| #770 | `9421846721cd788ab01615c8b6d459d9de849df7` | Source observation, inverse and tail conditions. |
| #781 | `ea282c4e73ecd2d8cad44587da5ffa135df67e98`; later historical head `83dca1a6b750feeffe9f446656bb01694131d74a` | #763/#764 corpus, representation identities, finite torsion and graph classifications, Epstein certificates. These versions must not be conflated. |
| #782 | `737bf85ec9f36213cfe02b7edc178181545167f7` | Segre–Chow synthesis, transferred higher differentials, degree-six frontier. |
| #783 | `48d556561125cba3859a4c6d6747bcb44c1a7fc1` | Source-normalized Poincare frames, Hecke scale, renewal transition; Xi portions require reviewer A reconciliation. |
| #774 | `abe712bdeca0968167f6decc2fbc0651fdd73592` | Native rectangular source factorization and primitive splitting. |
| #776 | `b7acc73075f7f8da4ebc783a449d2b68ce4aad63` | Occupancy/Hodge/centered-current finite identities. |
| #778 | `8db2752fa046a9fc686f3a4a5606beb2da3e7176` | Closed, unmerged principal-mode obstruction with surviving local geometry. Prior prose contained a different apparent head; reconcile against Git objects. |

The historical main checkpoint is `6dda8b5125457ed936330229f8c9eb6491728e76`. The actual previous release manifest and inclusion/exclusion boundary have **not** been revalidated in this run. These leads are not proof that coverage is exhaustive.

## Mathematical distinctions that the final audit must preserve

### Hilbert series, recurrence numerator and equivariant K-polynomial

For a two-dimensional vector space in characteristic zero, the degree-r part of the Segre coordinate ring is `(Sym^r V)^{tensor m}`. Its character is therefore `h_r(A)^m`. This explains the Hilbert-series identity but not every proposed geometric or arithmetic interpretation.

For generic eigenvalues alpha,beta, the ambient polynomial denominator has factors `(1-alpha^(m-k) beta^k T)^{binom(m,k)}`. A distinct-weight recurrence denominator has one copy of each factor. Therefore its numerator and the full equivariant K-polynomial differ by the product with exponents `binom(m,k)-1`. A proof that calls these numerators identical without the excess factors is not correct. Degenerate eigenvalues require a polynomial-identity or confluent continuation argument; the generic minimal recurrence need not stay minimal after specialization.

The additive alternating character of Tor is not by itself an ordinary positive character, a polarized space, an automorphic object or a Fredholm/superdeterminant realization. Every one of those promotions needs a separate construction.

### Recurrence degree statements

The formula `deg N = deg Q - nu`, with top coefficient `-q_D phi(-nu)`, follows from a Laurent expansion at infinity only under the precise two-sided recurrence/invertibility and proper-rational-function assumptions that justify that expansion. Exceptional specializations, canceled denominators and finite polynomial parts must be treated explicitly. No universal degree claim is approved here without reading those hypotheses in the source.

### Finite atlases versus uniform theorems

The reported torsion threshold has a forward all-order statement and a converse certified only through a finite m range. A finite exhaustive cyclotomic candidate list can establish the finite converse but cannot supply its unbounded extension. The odd-degree multiplicity formula has separate finite corroboration and a conditional transversality theorem; even-degree boundary behavior was reported unresolved. The claim ledger must keep those assertions separate.

Graph census minimality applies to the enumerated class and size range, not to arbitrary graphs. A complete infinite family theorem is a different row from its experimental discovery.

### Automorphic and source hypotheses

A source quotient must be constructed in the source space before Mellin observation if that is the claim. Equality of the observed scalar functions does not establish equality of source objects. For Hecke/Poincare constructions record the exact Petersson normalization, Gram matrix, rank dependence, uniformity in selected vectors and required symmetric-square input.

Weak interlacing with equality caused by a zero Schur coupling must not become strict interlacing. A critical renewal asymptotic valid away from zeros of its limiting coupling polynomial says nothing by itself about exact finite-weight cancellation at a resonance.

### Family averages and the principal member

In a finite character space, adding an arbitrary constant changes the principal coefficient without changing any nonprincipal coefficient. Thus nonprincipal variance or purity cannot alone bound the principal member. A source-specific theorem can overcome this separation, but only by proving an additional binding estimate. #778 must be retained as a closed research disposition, not discarded because it is closed and not merged. Its exact countermodel and surviving local trace identities require fresh inspection.

### Certified Epstein zeros

A proof-grade rectangle certificate must authenticate the function and modulus, complex-domain remainder bounds, a nonvanishing boundary, complete oriented edge coverage, and the integer winding inference. Ordinary high precision is not directed arithmetic. Reflected copies must be counted with distinctness checked. Epstein zeros outside a critical line are not zeta/RH counterexamples without the required Euler-product and completion hypotheses.

## Ownership handoff

B: recurrence and representation algebra; literal modular/source constructions; automorphic uniformity; finite-field hypotheses; finite classifications; Epstein certificate semantics; exact local/principal separation.

A, pending integrator reconciliation: Xi-specific innerness, Stieltjes/Pick and negative-square endpoints, literal Xi radial transport, RH implications of principal arithmetic estimates. B must audit the premise and object transfer; A must independently audit the terminal Xi/RH implication. Neither review is assumed accepted here.

## Required completion work and omissions

1. Read the actual previous release manifest and repository integration/review rules at a frozen baseline.
2. Read bodies and all discussions for each of the eight assigned programme issues. Their six L-family titles and mappings are not guessed here.
3. Establish an exhaustive execution/successor graph, including closed and superseded PRs. The historical leads above are not that graph.
4. Inspect and hash the actual proof files and primitive computational artifacts at each chosen source SHA; split versions when changes alter claims.
5. Independently check the all-order algebraic proofs and the uniform analytic estimates; execute selected authenticated exact or interval verifiers with their full dependencies.
6. Replace the provisional extraction targets by concrete baseline-consistent paths and attach dependencies, fixes and source identities to every accepted row.
7. Publish on a separate review branch, open a review PR and read back its exact head and file identities.

Until these actions are completed, no row in the accompanying TSV is an integration acceptance. Outstanding scientific dispositions are pending integrator reconciliation or fresh B inspection as indicated, never default acceptance.
