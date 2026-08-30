# Independent review: complete closed-point Euler replay

Reviewed commit: `4ba9cf883ecf49fe0034d6b05a878caf2768d263`.
Reviewer: independent `recent_landscape` agent, 2026-08-31.
Scope: `CLOSED_POINT_EULER_REPLAY.md`, `closed_euler.py`,
`test_closed_euler.py`, `closed_artifact.json`, and `closed_provenance.json`
under `research/l-families/atlas/generalized/global-s3-prym/`.

Conclusion: no blocking proof, degree-normalization, residue-character, or
coverage-acceptance defect was found. This is an independent finite Euler
multiplication route for the six frozen curves, through degree four. It does
not itself establish an all-degree theorem or independently reimplement the
finite-field library.

I read the complete proof, producer and eight tests from the exact Git commit.
The proof hash bound by the manifest is
`9ab9da6f7edba679a6702c5172a4017d344026c786d970074a32ae0940935f63`;
the closed artifact hash is
`00bf91d273db50ddc58cea6b0c6504a2909c99cec1ff14d6b751bc1593fa898b`.
Root reports successful Ruff, complete replay, eight ordinary tests and eight
optimized tests. I did not rerun those jobs; my review was independent reading
and derivation, with computation kept serialized by root.

## Closed-place and local-factor audit

The enumeration uses the p-power Frobenius on F_(p^n), retaining orbits of
exact length n. Those are exactly the affine closed points of degree n.
Every element is assigned to a disjoint orbit, and the Möbius count verifies
the number of retained orbits. The minimal polynomial is formed as an actual
product over the orbit in the field. Requiring all coefficients to be encoded
in F_p and checking irreducibility are appropriate independent consistency
checks. Compatible embeddings between different extension models are not
needed because the resulting monic polynomial identifies the base closed place.

The local standard denominator is reconstructed from the cubic over the actual
residue field. Unramified root counts 0, 1 and 3 correctly select three-cycle,
transposition and identity factors. A simple discriminant root contributes
`1-z`; cyclic triple ramification contributes one. The separately included
infinite place has determinant one for both sheaves in this particular packet.

At a nonzero residue t the Kummer twist substitutes its residue-field quadratic
character into z, including the odd coefficients of a ramified local factor.
At zero its invariant space is zero. The dedicated F7 branch example correctly
distinguishes the negative sign over F7 from the positive sign after a quadratic
constant extension. The closed-point algorithm uses exact-degree orbits, so it
does not accidentally count the latter extension value as the original factor.

The substitution `z=T^degree` and the inverse-series recurrence are correct.
Every local denominator has constant term one. Omitting degrees greater than
four changes the formal Euler product only in degree five and above; no analytic
convergence assertion is required. The completed finite product is compared to
the frozen elliptic polynomial padded through degree four and the frozen Prym
polynomial. The multiplication itself uses neither Newton recursion nor
extension trace summation, which makes this a useful second verification route.

## Authentication and adversarial checks

All seven predecessor files are compared with normalized bytes of the exact
`23ad35cc8010f72cf1df54f09eccb4dcba108879` Git objects before importing the
predecessor implementation. The source identity is checked again when building
the payload. The current replay reconstructs the orbits, factors and products;
it does not accept the artifact's self-described coverage as evidence.

The compact census retains factor multiplicities and a digest of the complete
ordered closed-place records. Type-sensitive canonical JSON comparison and
separate file bindings prevent accepting a merely internally consistent edited
artifact. The primitive field implementation remains explicitly shared with
the predecessor, whose independent field-model controls are not rebranded as
new checks here.

The tests directly enumerate irreducible quadratics, check exact-degree counts
and distinct minimal polynomials, verify Kummer sign change and zero/cyclic
stalks, detect a dropped or wrongly graded factor, and reject incomplete degree
coverage, invalid coefficients, caps and numeric-type forgery. No mathematical
acceptance check depends on Python `assert`.

The underlying global source theorem and weight theorem retain their previous
scope and external imports. No new mathematical priority or arithmetic RH
consequence is claimed by this finite replay.
