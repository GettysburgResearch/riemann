# Sources, credit, and reading limits

## Frozen repository base

GettysburgResearch/riemann, PR #950:
5a6418b021a35c95bbc2c80775353ee33506faee.
Packet: standalone/2026-10-16-critical-geometric-lift/.

MATHEMATICS.md and PRE_POISSON.md were read in full from the conversation's
previously supplied ZIP. Their bytes were freshly matched to the live
GitHub packet tree 107bc2981294979539942e480331cfb7b6651a5e:

- MATHEMATICS.md: blob b786c89c9d910beaf00b61407bb6a253c5de43a5,
  11,684 bytes.
- PRE_POISSON.md: blob 14e0f3af519b54f766127f51275ab65c7b0600bb,
  7,640 bytes.
- verify.py: blob 923a3159f7e9791d8803bcdb6a48db7a5f662614,
  13,255 bytes. Its elementary arithmetic implementation was inspected;
  this pass uses a new standalone checker, not an independently developed
  number-field backend. The old checker was not freshly replayed.

The parent supplied the h(d) coefficient, simultaneous X/Z dilation and
principal/residual warning. Those are prior work, not discoveries here.
The parent source's same-height completion theorem is not silently applied
to this packet's joint-ray envelope.

## Newer sibling

PR #951, aba76e1df38dc438b9f5c5f20b698fb26fb1716e, was read at full PR
metadata scope and its complete ATTACK_STATUS.md was read live:
standalone/2026-10-16-coupled-critical-flow/ATTACK_STATUS.md,
blob 56e23681b35ebb55412ff515f43e100ba503837b.

The sibling reports direct Gaussian transfers and an unproved compensated
signed estimate. Its complete new mathematical proofs were NOT reread in
this pass and are not analytic premises for the new local proofs. Earlier
#946/#944 interfaces are mentioned only at inherited assessment scope.

## Pinned upstream source actually read

AxiomMath/DedekindZetaZeroFree,
09afbb4ce6570c1615d58509dc197fc9f0956b7d:

1. DedekindZetaZeroFree/Moments/Probes/
   PrincipalProbeAndSeparatedMellinSeries.lean
   Blob: 6caa6418e903384af51806f85089e1212f009cb4.
   Read full returned file, through its end (within the requested 210 lines).
   Relevant definitions: gaussRow, integrand, probe,
   exteriorSexticRowCharacter, PrincipalData and its exteriorCharacters.
   These specify the actual Gauss normalization and multiplicative character.

2. DedekindZetaZeroFree/Theta/Profiles/
   ReflectionGaussianAndSixthUnitInvariance.lean
   Blob: d9a1c2de997604f4069d39eb76f6f80978f88428.
   Read full returned file, through its end (within the requested 220 lines).
   Relevant definitions: forwardArithmeticWeight, forwardRowCharacter,
   forwardSummand, forwardB; the SixthUnitCharacterCompatibility input and
   the derived forwardB_sixthTranslate theorem.
   This is sixth-UNIT invariance, not invariance under nonunit sixth powers.

No source file is copied into this packet; formulas and proof interfaces
are paraphrased/derived with attribution. No claim of formal elaboration,
transitive dependency checking, comparator execution, or axiom audit.

The S-arithmetic unfolding theorem explicitly assumes the primitive additive
character, principal S-ring, finite-index unit quotient and Haar data. The
local adapter does not rebuild those upstream data. Classical finite-field
Gauss orthogonality, CRT, S-unit finiteness, Haar unfolding, Minkowski and
geometric-series arguments are not claimed as new general methods.

## Access and freshness

A live open-PR listing identified #951 after the user's preceding #950 pass.
PR #949 metadata was also checked. An attempted guessed file path in #949
returned 404; it was not used. Public web verification located the current
Dedekind paper record, but fresh v1/v2 source-body retrieval failed. No new
manuscript import, new theorem-version comparison, or fresh PDF analysis is
claimed in this pass. In particular no bound is inferred from a webpage
abstract or a search-result fragment.

Repository AGENTS.md was read live at the frozen parent. Only add-only
standalone work is proposed. No historical claim identifier is reused,
no draft branch is described as integrated, and no exhaustive priority
search or review of all repository history is claimed.
