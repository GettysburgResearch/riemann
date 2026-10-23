# Review scope and frozen source

**Status: standalone research contribution. No new zero-free boundary is established or proposed for integration.**

## Exact source

- Mathematical source commit: `193c3d79f0522f08f62afc5c24c29f139d889080`.
- Source tree: `1e71897b46a6b7b75fe8694c48b7d08911260276`.
- Parent and preceding published research head: `e87c5f669f81fe6371af926917d1c5b21023bce8`.
- Source directory: `standalone/2026-10-22-quartic-full-sieve/`.

The follow-up publication commit adds only this record, the manifest, and review reports. It leaves all eight files in the frozen mathematical source byte-for-byte unchanged. The manifest records their SHA-256 hashes and Git blob identities. Hashes authenticate the reviewed bytes; they do not certify mathematical truth.

## Independent internal checks

| Report | Reviewer | Scope |
|---|---|---|
| [Tail and principal target](REVIEW_TAIL_AND_PRINCIPAL.md) | `alternative_major`, separate from their author | Full local tail proof, complete-row large sieve, divisor Cauchy, conditional principal amplifier, smooth-profile and Euler-factor scope |
| [Quartic completion and correction](REVIEW_QUARTIC_COMPLETION.md) | `full_inverse`, separate from their author | High numerator valuations, all-row completion, exact scale shifts, corrected split/inert Gauss-square identity and norm-five counterexample |
| [Reflected energy and spectral interface](REVIEW_SPECTRAL.md) | `full_inverse`, separate from their author | Native changes to pinned source induction, powerful-row count, angular Bessel reconstruction, ordinary level identities, and remaining spectral gaps |
| [Additional source review](REVIEW_EXACT_SOURCE.md) | `spectral_route`, separate from the quartic authors | Exact-source check of the full-row tail, Gauss-square correction, completion, and README scope |

Each reviewer identifies the exact source revision and the actual checked claims. These are separate-agent internal reviews, not independent human peer review, a formal proof, or integration approval. Agreement among agents does not replace the displayed mathematical arguments.

## Claim boundaries

1. **Native quartic tail.** The packet supplies a complete proof of the estimate
   $$\sum_{0<Nk\le K}|T_R(k,D)|^2\ll_\varepsilon (KD)^\varepsilon(K/R+D^2/R^4).$$
   It uses exact local Gauss identities and the ordinary complete multiplicative large sieve. Every nonzero row is included. The zero row is excluded. The simplification to `K/R` at `K=D^2/H` requires `R^3>=H`.
2. **Exact quartic identities.** The all-row completion and corrected coefficient identity are algebraic deductions from the stated local formulas. The correction is to the inherited repository formula; this packet does not assert that an uninspected earlier version of a cited paper was wrong.
3. **Source-dependent reflected estimates.** The marked inverse and powerful-row notes assume the specified statements of the pinned quasi-RH source, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, source SHA-256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`. The reviews inspect the native changes and their source use sites. They do not independently rebuild that entire analytic source.
4. **Conditional consumer.** The principal amplifier proves the stated implication from a full raw moment bound with its common smooth-profile uniformity. The input needed for the `17/20` half-plane is unproved here. The implication is not an achieved boundary.
5. **Spectral interface.** Exact local and archimedean identities are separated from the unproved global centered estimate. Neither ordinary level identities, a positive full-series mean, nor a small vector norm establishes scalar evaluation with the needed uniformity.

## Smallest unresolved mathematical step

The quartic route still needs the full retained low-divisor centered quadratic estimate, with its finite arithmetic diagonal, all physical row masks and punctures, both angular input columns and their cross term, common reconstruction kernel, every cusp, and the actual finite-cover evaluation cost. A tail estimate cannot supply an assumed bound for the vector to which the tail is attached.

The packet therefore leaves the inherited source-qualified boundary unchanged. It does not promote the improved but inactive second marked constraint, a low-side-only exponent, or a guessed level dependence into a zero-free result.

## What was checked mechanically

- The frozen source commit was fetched from GitHub; its parent and tree were checked against the prepared local tree.
- Reviewers used `git show` at the exact source SHA and recomputed the relevant file hashes.
- The source and report bytes were scanned for unintended control characters; two TeX escaping defects in the marked note were repaired before the source freeze, and one review formatting defect was repaired before publication.
- Staged whitespace checks, Git tree comparisons, and a final remote readback check the integrity of the publication.

No numerical experiment, finite zero search, or automatically accepting mathematical checker is offered as proof of an infinite analytic claim. The explicit norm-five calculation is a counterexample to the old sign, supported by a separate all-modulus proof of the corrected identity.

## Preservation

The new branch descends from the exact published head of [PR #1015](https://github.com/GettysburgResearch/riemann/pull/1015). Publication uses a new branch and a draft PR. No previous proof file is edited, no history is rewritten, and this packet does not change `main`.
