# Executed validation and its exact scope

The paper arguments remain PROPOSED and require independent mathematical
review. This document reports finite source replays, directed arithmetic,
and a small isolated Lean component. None certifies an infinite native
moment bound or RH.

## Exact primitive ideal and character checks

| Report | Complete declared coverage |
|---|---|
| CHECKS.json | All 155 integral Eisenstein ideals through norm 256; all 77 exterior columns; all 19 exterior masking ideals through norm 64 |
| EXTENDED_CHECKS.json | All 2,474 integral ideals through norm 4,096; all 1,241 exterior columns; all 157 exterior masking ideals through norm 512 |
| KUMMER_CHECKS.json | All 19 explicit Kummer rows through norm 64 and all 77 exterior columns through norm 256; every residue of all 52 exterior prime-ideal residue fields in that cap |
| FAST_SOURCE_CHECKS.json | Every integer coefficient through norm 4,194,304, in all ten principal mask arrays, matches the original independent local-factor producer byte for byte |

The HNF enumeration and ideal factorization retain actual ideals of equal
norm separately. Their complete norm counts are compared with the independent
scalar formula from zeta(s)L(s,chi_-3). Mobius/character norm coefficients
are compared with a separate rational Euler algorithm. Every factorization
reconstructs the ideal itself, not merely its norm. Split, inert, ramified,
nonunit, common-prime and repeated-prime cases are explicit.

`test_exact.py` runs the deposited checks in ordinary and optimized Python,
tests four deliberately wrong exact models at their intended gates, and
compares the fast Euler-deletion recurrence against independent local
factors at all norms <=8192 for all 66 mask signatures through norm 512.
The fast recurrence never changes the original primitive array.

The original #976 packet was separately authenticated against all twelve
Git blobs at its exact frozen commit. Its 12,040-predicate report reproduced
in both Python modes, its sealed payload verifier passed, and its eight
separately executed corruptions failed at their original gates. This is
recorded in BASELINE_REPLAY.json. No inherited file or historical report
was modified.

## Directed Gaussian replays

Both experiments use the fixed weight W(y)=y^-4 exp[-log(y)^2/4]/sqrt(4pi),
with tau=1. They do not use the reflected theta source.

| Experiment | Rows and scales | Complete norm cutoff | Longer replay |
|---|---|---|---|
| GAUSSIAN.json | Every principal row u=b^6 with Nb<=64, including all 19 ideal multiplicities; 11 scales D=2^j, 0<=j<=10 | 4096D, up to 4,194,304 | 8192D, up to 8,388,608; 384 rather than 256 bits |
| NATIVE_GAUSSIAN.json | Every ideal row Nu<=64 in the explicitly specified sextic Kummer family; all 19 complex rows; 9 scales D=2^j, 0<=j<=8 | 4096D, up to 1,048,576 | 8192D, up to 2,097,152; 384 rather than 256 bits |

There is no lower truncation. Every omitted upper ideal column is covered
by the proved absolute tail majorant (G2), evaluated with directed Arb
operations. Exact norm-coefficient arrays are regenerated from the
primitive field, source and local factors, with portable signed-int32 hashes.
Actual ideal rows, generators and mask multiplicities are authenticated.

The deposited principal enclosures contain all 165 corresponding longer
row/moment enclosures. Twenty low-scale comparisons use individual HNF
ideal sums. The native experiment passes 558 longer real/imaginary/square/
moment containment checks and 38 individual-ideal comparisons. The two
different coefficient producers give exactly the same principal-row
enclosure on all nine common scales.

`test_gaussian.py` rejects a missing infinite tail, the same wrong split-prime
mask in both producer and replay, and a self-consistent omission of a conjugate
masking ideal. The independent source/coverage or longer-tail gate rejects
each model. It also checks the decreasing-profile premise and directed
integer powers across zero and on negative balls. Generic analytic Arb
exponentiation is not used to square zero-crossing intervals.

The interval implementation is python-flint 0.9.0 / FLINT 3.6.0. Its directed
arithmetic contract is an assumption. The longer replay is a fresh execution
of the published producer, not a second implementation of Arb or an
independent mathematical referee. The ideal-by-ideal checks have their
specified smaller caps. No large zero census, statistical exponent fit or
infinite sign is inferred from the values.

## Formal component

The five lemmas in NativeMaskFinite.lean typechecked with Lean 4.35.0-rc3
and pinned Mathlib `0493595ecd5da8ef14742febab99728f98e948e8`, with no warnings
in the final run. Each printed axiom closure is exactly `propext`,
`Classical.choice`, `Quot.sound`. The source hash and command are in
FORMAL_RECEIPT.json; FORMAL.md states the finite and logical scope.

This is not a Lean proof of the infinite mask-average theorem, native
Gaussian estimate, Hecke zero-free equivalence, growth-abscissa theorem,
CT-input corollary, or RH. The repository's existing formal-v0.1 tree is
unchanged. The separate CT_BUILD_RECEIPT.json records the external build
attempt and must be read for its actual completion status.

## Primary-source and artifact authentication

CT_SOURCE_AUDIT.json authenticates the actual 142,663-byte primary CT v2
TeX source, including nine located theorem/formula blocks. It was compared
with #976's exact source interface as described in CT_INTERFACE_REVIEW.md.
Source authentication does not prove the imported representation theory.

`replay.py --intervals --ct-source <downloaded-primary-TeX>` is the combined
finite reproduction entrypoint. Its completed execution record is deposited
as VALIDATION_RECORD.json. `verify_manifest.py` separately checks every
sealed payload and the complete top-level inventory. The manifest is
authenticated by the frozen Git commit, not by a self-reference.

No repository-wide validator, remote CI verdict, independent referee
acceptance, integrated mathematical status or stronger zero-free boundary
is claimed. PROOF.md §8 explicitly adopts the external printed CT-31/32
theorem; its native power improvement is a deduction from that input.
