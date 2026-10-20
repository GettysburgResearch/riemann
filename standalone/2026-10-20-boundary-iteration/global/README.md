# Resonant theta residues and the missing unitary family

Status: proposed source-dependent mathematics, under review.
RH remains unsolved. No finite checker here authenticates an analytic
zero-free theorem.

The primary result of this subpacket is a proposed removal of the
resonant exception from the full unitary Hecke family over every
number field. The new spherical theta reflection retains and bounds
its constant residue, and the inverse recursion absorbs that residue
with a strict existing margin. A cubic auxiliary character, an exact
finite-place row restriction, and a weighted norm-one probe then kill
both direct constant terms while preserving the original target
reciprocal coefficientwise.

[ALL_UNITARY_REFINED_BOUNDARY.md](ALL_UNITARY_REFINED_BOUNDARY.md)
assembles the all-field inverse base, fixed balanced-type ordinary
moments, the guarded physical probe, and the source residue-averaged
comparison. Its proposed conclusion covers every unitary Hecke
character over every number field for real part greater than
\(B_\flat=0.874886647039964\ldots\).
This extends the family at the inherited boundary; it does not
decrease that number or improve the already covered zeta boundary.

The native Eisenstein proof is independently presented in
[EISENSTEIN_REFINED_BOUNDARY.md](EISENSTEIN_REFINED_BOUNDARY.md).
It uses native E analytic inputs and does not specialize a theorem
whose field hypothesis requires \(\mu_{12}\).

The proof route is:

1. [RESONANT_RESIDUE_MEAN.md](RESONANT_RESIDUE_MEAN.md):
   exact Eisenstein squarefree residue, full-index mark weight,
   coherent Möbius saving, and sparse row exponents.
2. [RESIDUE_INDUCTION_INTERFACE.md](RESIDUE_INDUCTION_INTERFACE.md):
   uniform shifted-label residue row bound and canonical margin.
3. [EISENSTEIN_SPHERICAL_REFLECTION.md](EISENSTEIN_SPHERICAL_REFLECTION.md):
   native finite Fourier and cusp calculation, every finite mask
   retained, plus the exact spherical gamma multiplier.
4. [EISENSTEIN_UNITARY_INVERSE.md](EISENSTEIN_UNITARY_INVERSE.md):
   actual angular coefficient orbit through both Poisson steps,
   selected inverse moments, and the preliminary \(11/12\) boundary.
5. [AUXILIARY_PRIME_RESIDUE_REMOVAL.md](AUXILIARY_PRIME_RESIDUE_REMOVAL.md):
   the digit-three auxiliary choice and coefficientwise cancellation.
6. [EISENSTEIN_REFINED_BOUNDARY.md](EISENSTEIN_REFINED_BOUNDARY.md):
   native E product/numerator bridge and \(7/8\) to \(B_\flat\)
   closure without specializing a \(\mu_{12}\)-field theorem at E.

[ALL_FIELD_SPHERICAL_RESIDUE.md](ALL_FIELD_SPHERICAL_RESIDUE.md)
extends the spherical-residue interface in Liu's stated field setup.
It proves the moving-prime weight by
rational torus transport with the actual finite class cutoff, and
uses the original bounded-row terminal before completion. It is
being reviewed separately; the E theorem does not depend on it.
[ALL_UNITARY_BOUNDARY.md](ALL_UNITARY_BOUNDARY.md) gives the full-family
\(11/12\) base from this inverse terminal.
[ALL_FIELD_AUXILIARY_GUARD.md](ALL_FIELD_AUXILIARY_GUARD.md) supplies
the missing direct comparison: adapted finite class complement,
the exact local Fourier transform, constant-term cancellation, and
coefficientwise preservation of the target. The refinement is then
assembled in the primary theorem linked above.
[ALL_FIELD_CONSTANT_TERM_DRAFT.md](ALL_FIELD_CONSTANT_TERM_DRAFT.md)
records the earlier unproved draft and is not a theorem dependency.

The smallest new load-bearing statements are the spherical local
constant calculation and its uniform finite-profile transport.
The native E calculation is explicit in the cusp formulas; the
all-field extension relies on the source's Jacquet exponents and
ordinary metaplectic torus section. If either corresponding
calculation fails, that branch's inverse extension fails. The
native E guard uses the source's permitted primitive cubic auxiliary
character. The all-field guard instead constructs the finite-S test,
row restriction and two cancelling ideal twists explicitly. Its
principal local Fourier multiplier is checked to be nonzero, and
the actual finite class selector is retained.

Run the standard-library checker with isolated Python:

    python -I -S -B check_residue_algebra.py

[residue_check_results.json](residue_check_results.json) records
2,366 named exact finite checks and binds the checker SHA256.
They check phases, local residue and selected factors, auxiliary
character cancellation, finite inclusion-exclusion, shifted row
majorants, exponent bookkeeping, and the tame guard Fourier transform
in exact cyclotomic arithmetic modulo \(7^2\) and \(13^2\).
Two negative controls reject the wrong quadratic/principal selector
and an even theta digit. Acceptance uses explicit exceptions and
remains active under Python's optimization flag.
They do not prove Mellin
continuation, the upstream recursive moment, the contour assembly,
or the imported continuous scalar certificates. Source pins and
the exact review boundary are in [SOURCES.json](SOURCES.json).
