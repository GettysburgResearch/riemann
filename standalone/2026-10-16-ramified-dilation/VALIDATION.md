# Verification, limitations and publication state

Status: proposed written proofs and exact finite checks; NOT PUSHED.
Proof and checker have the same author. No independent mathematical review.

## Executed checks

`python verify.py` and `python -O verify.py` reproduce results.json byte
for byte. The final script has 3,679 explicit finite predicates, including
repeated/setup checks, not 3,679 independent asymptotic cases. Nine named
negative controls reject concrete incorrect substitutions.

Local Gauss verification compares a DIRECT sum over all unit residues
with a separate residue-fiber formula, using exact cyclotomic polynomial
reduction over Q(omega). Complete row-residue coverage is:

- split rational primes: (7,e=1,2,3), (13,e=1,2);
- the inert Eisenstein prime above 5, norm 25: e=1,2;
- exponent six at the norm-7 prime: six explicitly listed rows only,
  each evaluated by a direct sum modulo 7^6.

The direct finite-field Gauss norm is also checked. No OCR, floating-point
phase comparisons or statistical sampling enter these checks.

The physical row fixtures use four named Eisenstein prime ideals with
norms (7,7,25,13), keeping the norm-7 conjugates distinct. Five denominator
patterns are tested. The source has all 54 seeds of norm at most 13 and
specified shell translates; its amplitude is an explicitly artificial
rational function of scale. Dilation columns are the stated finite prime
boxes. All their output rows are included, and complete sparse arrays are
compared before any moment is taken.

This is NOT a census of all native ideal columns or all physical rows under
the large reported norm caps. Some norms are enormous solely because of
sixth powers. At most 892 nonzero output rows occur in the declared cases.
The checker does not evaluate the actual theta B, its infinite Gaussian
expansion, the source's S-arithmetic Haar integrals, or its comparison
residual. Written proofs, not these fixtures, justify the all-scale claims.

## Adversarial controls

The nine controls cover neutral-prime support, zero-extension of principal
characters, equal-norm conjugate ideal aliasing, neutral-shell overlap,
the D^3 prefactor, moving column scale, divided row index, divergent ray
endpoint budget, and the false universal operator power saving.

Tests do not demonstrate every possible failure mode. There is no automatic
mutation-generation claim, no independent arithmetic backend, and no
computer-assisted asymptotic certificate.

## Parent and source authentication

The two complete parent proof files read locally and the inspected parent
checker were matched to live Git blob identities. SOURCES.md lists those
identities and the two freshly read upstream formal definition files.
The preceding #950 checker and the #951 checker were NOT newly replayed.
No Lean build, comparator, full-repository validation or remote CI was run.

## Packaging checks

All Python files were syntax-compiled. The payload manifest binds every
other file by byte length, SHA-256 and Git blob ID. Its own bytes are bound
by the supplied add-only patch and ZIP, not by a circular self-hash.
The patch was applied to a fresh local EMPTY Git fixture and its resulting
files were compared byte-for-byte with the packet. A fresh ZIP extraction
was separately checked. This is not a clean clone or full-repository test.

## Remote publication limitation

Live GitHub reads succeeded, including parent and newer sibling metadata.
The current GitHub tool discovery returned 48 read/search functions and no
create/update/commit/PR functions. Searching available plugins returned the
installed hybrid connector. The runtime has no `gh`, and a direct public
network request failed with a DNS resolution error. No credentials were
searched for, no permissions were changed, and no write was sent through
an unsupported GET route.

No new remote branch, commit, PR or comment exists from this pass. The
suggested branch name is a handoff only. The parent and main remain
unchanged. The add-only patch is prepared against the stated frozen #950
base; a receiving agent must perform the actual authenticated publication
and then record its real SHA/PR and remote byte read-back.

## Priority review targets

RAMIFIED_DILATION.md: local zero-extension and support in Lemma 1; quotient
and Haar unfolding hypotheses in Section 2; the row normalization in
(12), including the surviving (Na)^(-6); neutral overlap in (14); and the
explicit separation of raywise versus same-height norms. Finally review
the sharpness construction and the fact that the critical coprime input
and full scalar Gaussian bound are still open.
