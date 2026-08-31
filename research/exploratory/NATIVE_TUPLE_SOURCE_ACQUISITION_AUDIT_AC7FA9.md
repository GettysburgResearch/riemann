# Independent frozen audit: native tuple source acquisition

Audited source: **ac7fa9af27c3fbcb3314f3ed58c8eed35b318052**.
Authoring base: 1904d20cdb76ecd26e0e63472625da930075303e.
Review date: 2026-08-31. This is a non-author, read-only mathematical and
finite-replay audit. The five scientific source files were not edited.
The source author's earlier cosmetic repair is preserved, not amended.

Verdict: **PASS for the stated diagnostic mathematics and exact controls;
arithmetic release metadata needs a small, separate cleanup.**
This is not acceptance of a complete native source decoder, a principal
moment estimate, or any RH implication.

## 1. Exact review scope

All five frozen files were read in full:

- research/exploratory/NATIVE_TUPLE_SOURCE_ACQUISITION.md
- research/exploratory/native_tuple_source_acquisition.py
- research/exploratory/native_tuple_source_acquisition.json
- research/exploratory/native_tuple_source_acquisition.sources.json
- tests/test_native_tuple_source_acquisition.py

All eleven manifest source notes were read at their literal commit:path
identities, including the complete AMPLIFIER, TARGET, SOURCE_FIRST,
OBSERVATION_GAP and ACQUISITION definitions. Source hashes were independently
checked by resolving the Git blob with git rev-parse, reading it with
git cat-file blob, and hashing LF-normalized bytes without the producer's
hash helper. All eleven Git object pins, eleven source hashes, four artifact
hashes, and the payload seal matched.

Frozen artifact LF SHA-256 values:

| artifact | SHA-256 |
|---|---|
| proof | dd8294e3a6284a58e5c2866e28403186a236f0581f43741ffd7cf4ffb297e0f9 |
| producer | 011d3240c4bd9c02d2d3c9c044d165ce83967334441e3ffbff90519ef4585334 |
| manifest | 6308ca557eecfb50fa851f1f87d80b402fdd3c4b4f64a74aa92e4c05d8a83805 |
| tests | 916eca907f8ccb41b9c4906e435aed0da958d1d3108e2080fe413a45cbd3c46f |

Payload SHA-256:
a7725c08d2f00751b9c673ada4c0f4fb3e1ba2c3abb5903347f6e69ef81bc88c.

## 2. Mathematical reconstruction

The rough-support formula is correct. At cutoff U, if every label exceeds U,
the only U-small subset of a nonempty support is the empty subset.
Therefore a_U(empty)=0 and a_U(A)=-1 on every nonempty rough support.
A nonzero history assigns every label to R, S or M, with R and S nonempty
and sign (-1)^|M|.

For j=3 there are six positive histories (M empty, R and S nonempty)
and six negative histories (one label in each of R,S,M).
For j=2 the two histories both have positive sign. The exact bilateral
owner shares 1/10 and 1/6 consequently give twelve +1/60 and twelve -1/60,
zero total coefficient and literal diagonal 24/3600=1/150.
The fixed physical factor is common only for the canonical coefficient
presentation; the proof does not assert that it exhausts the actual gamma
weights.

The independent half-source calculation is also correct:
f_j=-[(1/2)^j-(-1/2)^j], including f_0=0 by separate evaluation.
Its Boolean convolution square gives b_j=1+(-1)^j for j>=1.
L-106133.9--12 then gives the actual density
2 b_j theta^j(1-theta)dtheta and the integrated owner share
b_j/binom(j+2,2). At j=2 this is 1/3; at j=3 it is zero.

SOURCE_FIRST equations (3)--(7) first take the squarefree quotient, then
apply Boolean owner completion. They give tau^(j+2) times the completed
coefficient, with owner/core derivative proportions 2/(j+2) and j/(j+2).
This is not the raw mixed-monomial path of EULER equations (3)--(5).
The latter is (-1)^j tau^2(1-tau)^j, with owner/core integrals
(-1)^j/binom(j+2,2) and its negative. Thus the signs -1/10,+1/10 and
+1/6,-1/6 in the diagnostic refer to the right, explicitly different map.
The report does not exchange theta and tau measures.

For a permutation with a odd cycles and b even cycles, a fixed signed
three-colouring contributes product_cycles(2+(-1)^length)=3^b.
Subtracting the R-empty and S-empty colourings contributes
-2 times product_cycles(1+(-1)^length), which equals
-2*1_(a=0)*2^b. Restoring the all-M colouring contributes (-1)^a.
This proves the displayed character formula for every j>=1, not merely
the enumerated j<=7 panel.

At odd j>=3 the identity character is zero while a transposition has
character two. Hence the two permutation modules are not isomorphic and
the signed virtual representation is nonzero. At j=3, the positive set
is two natural three-point orbits and the negative set is the regular
S_3-set, so the virtual character is precisely 1-sgn. This does not
obstruct the equivariant signed-sum map, whose value on constant input
can be zero. The proof explicitly makes no permutation-symmetry claim
for physical primes, native measures, or retained amplitudes.

## 3. The source-interface gap is accurately located

At the pinned 86cac1 source:

- L-106026.8 retains literal coefficients omega_i in a supplied finite
  source-owned collection. Plancherel transports those coefficients;
  it does not assign their values.
- L-106093 defines complete A_alpha(t), including shell, carrier,
  marked-prime and renewal labels, and keeps anchor-dependent masks
  inside the opposite sum before the family square.
- T-106140.1 and .7 retain the complete atomic diagonal and principal
  readout under the original conductor weights and Fourier measure.

At b79aa2, SOURCE_FIRST permits additional labels as spectators only
when their measure and weights are transported unchanged. Its section 7
expressly distinguishes its record-diagonal bound from the family readout.
OBSERVATION_GAP section 2 writes the separate coefficient, native atom,
tuple aggregation, and family-square objects. ACQUISITION expressly stops
when a regional occurrence or literal measure has not been supplied.

Consequently the questioned equality in diagnostic lines 102--116 is
indeed the first unproved substitution for this proposed decoder:
the complete native tuple aggregate is not yet identified with
q_a(t) B_U(c)B_U(d). Here g=1 and B_U includes the canonical equal-pair
share, as the pinned DIAGNOSTIC and OBSERVATION_GAP define.

A physical-only mask commutes with aggregation, but that algebra does not
supply the aggregate's value. An unchanged gauge or source endpoint does
not by itself identify the original Wick atomization. A zero canonical
sum does not erase its diagonal or establish the actual weighted sum.
The diagnostic correctly refuses arbitrary reweightings as native
counterexamples, and does not assert repository-wide nonexistence of
a future decoder. Its narrower source-audit statement passes.

## 4. Finite replay and additional hostile controls

Fresh review worktree:
isolated/native-acquisition-independent-review-pass3,
initially at the exact audited source.

The 32 original tests passed in both modes:

- normal Python: 32 tests in 6.093 seconds;
- optimized Python: 32 tests in 6.079 seconds.

Both --check runs passed. Both --emit outputs matched the fixture
byte for byte after CRLF-to-LF normalization; both --emit-sources outputs
likewise matched the manifest. Ruff check and format --check passed.
The full authoring-base-to-ac7fa9 diff passed git diff --check and contained
exactly the five advertised new scientific files.

Additional independent in-memory audit controls, also normal and -O:

- Exhausted all 153 permutations in degrees one through five, using a
  separate disjoint-subset R,S enumeration rather than three-colour
  assignments, and compared the signed fixed count with the formula.
- Exhausted all 22 cycle types in degree eight, extending the five
  depth-eight held-out types in the original tests.
- Independently authenticated all source/object/artifact/payload seals
  and both producer/manifest emission modes as described above.

No floating point or numerical integration is used. In particular n/point
in the support test has a Fraction denominator and remains exact rational.
All source claims about indefinitely growing j are justified by the written
cycle-colouring proof, not by these finite checks. The original tests reject
resealed completion, measure, character and literal-diagonal changes;
boolean-as-integer and type/cap attacks remain rejected under -O.

## 5. Release-contract cleanup, distinct from mathematical acceptance

The producer's CONTRACT at line 116 and the manifest at line 4 use the
descriptive arithmetic string "exact integer coverage and exact rational".
This accurately describes the computation, but omits an explicit rounding
contract and is not the resident programme's canonical MIXED classification
with EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE components.

The prior frozen generalized-programme audit
UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION_AUDIT_330C6F8B.md, section 2,
at G7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e records this taxonomy rule.
AGENTS also requires an arithmetic class and rounding contract for
proof-producing computation.

Recommended bounded repair: a new identity adding the canonical class,
the two components and explicit no-rounding metadata, with a resealed
fixture/manifest and tests for that contract. This is release cleanup,
not a rejection of the diagnostic's equations, character theorem or
source-interface conclusion. Do not amend ac7fa9 or silently change its
source pins. This audit makes no scientific-source edits.

The unresolved native task remains a source-defined occurrence, complete
coefficient density and unchanged-measure transport into the actual
principal member, preserving the literal diagonal. Neither this audit nor
the reviewed packet supplies native signed cancellation or an RH estimate.
