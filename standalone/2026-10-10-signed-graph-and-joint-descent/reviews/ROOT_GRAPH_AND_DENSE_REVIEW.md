# Independent review of the shared-incidence graph theorem

Reviewer: root, independently reviewing the `signed_sector` manuscript.
Date: 2026-10-10 UTC. Scope: analytic deductions from the explicitly
stated `NM2` and `PW_b` premises, exact finite algebra, and graph
inequalities. This is an AI-agent review, not human peer review or a
proof-assistant certificate.

## Frozen targets

| File | SHA-256 |
| --- | --- |
| `ARBITRARY_GRAPH_SECTORS.md` | `ef3704340d3af629a6bbd97d575d35bb5570474e8973a99c600c76bf096c9f13` |
| `check_graph_charges.py` | `9b7e752cf98a3d3fd0f40fe89b1cacdf497a56249025cd7ff48c8827bc48e671` |
| `graph_charge_checks.json` | `54e7e19ed2aa739a9877b9340a3bfb39ab70c3533fa8fcef8d866fa4387fd569` |

The dense continuation was authored by root and was independently
reviewed by `signed_sector`; its report is separate. This report does
not label root's own dense theorem as independently reviewed by root.

## Mathematical review

**Verdict: pass within the stated conditional scope.** I read all eight
sections and checked the following load-bearing steps against the
stated sources and by direct algebra.

1. The prime-by-prime incidence decomposition is bijective. Its exterior
   coefficient includes the Möbius multiplicity, every conjugation, and
   the principal nonunit mask when the two side multiplicities agree.
   Fixing every shared ideal makes an arbitrary shared-incidence
   selector independent of the singleton core. It does not do so for a
   selector involving an unfrozen singleton or residual conductor.
2. The finite forward correction has local numerator `1-sum z_v` and
   denominator `prod(1-z_v)`. Its unmasked coefficients have no
   one-axis terms; at a frozen-mask prime the inverse product is exact.
   The identities retain zero-extended characters. Finite support
   permits critical weights `1/2`, by moving every weight right by a
   fixed positive amount and then paying an arbitrarily small power of
   `D`. No infinite endpoint Euler convergence is claimed.
3. The two native averaged axes may be on the same Hermitian side:
   Cauchy bounds the absolute row product after the exact correction.
   The remaining axes use the stated pointwise premise. The test on
   each independent axis remains the same original smooth test at a
   shorter scale, so no unstated arbitrary-coefficient version of
   `NM2` or `PW_b` is used.
4. The induced-subset charge constraint leaves each shared-ideal norm
   with exponent at least one. Harmonic ideal sums are taken only
   after the complete signed singleton estimate. The number of shared
   subsets and labeled graphs depends on fixed `k`; the proof does not
   promise useful constants uniform in growing `k`.
5. For each nontrivial induced tree component, the slack equals
   `1+sum(deg(v)-1)(1-gamma_v)`. Isolated vertices have weight at least
   `1/2`. I independently derived the discounted edge charges at the
   two native vertices and the rank/isolate statistic. A full matching
   only has `k-1` effective charges; no false extra charge is counted.
6. A deterministic partition by the entire labeled graph preserves
   all its omitted edges and nonedges as a shared selector. This is
   why the union theorem is valid for a signed sum. It does not rely
   on monotonicity under deletion of arbitrary tuple contributions.
7. The cycle charges satisfy both proper induced-path constraints and
   the full-cycle constraint. I checked the exact cycle gain, the
   four-cycle plus matching exponent, and its cutoff. The fourth-
   moment union bound keeps the same power throughout `1<=R<=D`.
8. At `R=D`, threshold one makes every cross edge automatic. The
   corrected limitation section handles that endpoint explicitly.
   Combining a complete signed graph bound with a controlled
   conductor complement can add back `O(HD^(k+epsilon))`; this cost is
   explicitly retained even when the original graph bound is smaller.

## Diagnostic review and independent execution

I read the producer's finite phase model, independent incidence
reconstruction, complete graph enumeration, subset-charge checker,
dense corner arithmetic, explicit negative controls and acceptance
gates. Its gates raise `RuntimeError`, so optimization cannot remove
them. The formal two-prime phase model is not represented as an
enumeration of genuine global Hecke characters.

I independently reran the producer with a different output destination.
It passed 964,909 declared finite predicates. The resulting JSON was
byte-identical to the author's report, with the SHA-256 recorded above.
The very large count of labeled dense subsets represented by symmetry
classes is a combinatorial coverage annotation; it is not the number
of individually executed predicates and is not evidence for an
infinite theorem.

The all-order proofs are the symbolic arguments in the manuscript.
These finite diagnostics do not verify `NM2`, `PW_b`, an infinite
moment bound, an external theta theorem, `17/24`, or RH. The simplest
remaining unproved input for the requested goal is cancellation in the
far-separated singleton sector beyond its linear-in-`k` pointwise
excess.
