# Independent review: the S3 closure and two elliptic maps

Reviewed scientific commit: `567ae7aec00f6ee6d3e01bdde2004e76fec8ff6f`.

The six reviewed files are `GALOIS_CLOSURE_AND_TWO_ELLIPTIC_MAPS.md`, `closure_replay.py`, `test_closure_replay.py`, `closure_source.json`, `closure_artifact.json`, and `closure_provenance.json` under `research/l-families/atlas/generalized/global-s3-prym`. Frozen proof SHA-256: `eff3ef741e8151f719e920979a91014446ea626d04796739dd9de691aa259348`. Frozen artifact SHA-256: `04054e8e0c0899c7d110175383f1856543f03589574c827289d22adcd1a23a88`.

The reviewer independently read the complete proof, producer and all 12 test definitions, checked the frozen inventory/provenance, and independently derived the two source-map formulas. No test or producer computation was run by the reviewer. The main agent reports focused Ruff, write/check/optimized-check and all 12 tests in each Python mode passing at this freeze.

## Geometric assessment

No blocking issue found under the stated hypotheses `p>3`, `A!=0`, and nonzero cubic discriminant. The quadratic polynomial `g=-3x^2-4A` is squarefree and coprime to the cubic `f`; the latter assertion fails exactly at the excluded discriminant locus. Its four simple zeros on E give the geometrically connected genus-three double cover Z. The equations exhibit the actual degree-six cubic splitting field, and both S3 deck generators are defined over the base field. Thus the Frobenius action on the representation multiplicity spaces has no unaccounted constant-field twist.

The sign quotient is the quartic genus-one curve D with the displayed Vandermonde coordinate. The two decompositions of `H1(Z)`, from its biquadratic action and its S3 action, are compatible with Frobenius. Their comparison yields `P_H=P_E P_D` over every permitted finite base field. This is a quotient/cohomology theorem, not an isogeny inferred from sample point counts.

The first map `H->E` is genuinely source-defined: on Z it is the group-law difference between the two other cubic-root points on E. It gives exactly `X=(x^3+4B)/g` and `Y=w(x^3+4Ax-8B)/g^2`. The displayed integer polynomial identity has the correct powers and signs. The coordinate numerator and denominator are coprime, so the degree comparison proves a degree-three map. Its two geometric points over `g=0` and its infinity point account for the fibre over the elliptic origin.

The second map `H->D2` is `U=f(x), S=w(3x^2+A)` and likewise has degree three. The map `D->D2`, `U=u^2,S=us`, is the quotient by the fixed-point-free involution `(u,s)->(-u,-s)`. It is etale of degree two and induces the asserted isogeny of Jacobians. The note correctly distinguishes that statement from an origin-preserving map on a quartic without a chosen origin. The independent quadratic-character proof uses discriminant `-432A^3` and verifies `P_D=P_D2` over every extension.

All infinity terms check: E, H and D2 have one rational point; Z, D and the conic have `1+chi(-3)`, which may be zero. At finite double-root fibres the normalized closure has three points, not six root orderings with multiplicity. The sign and standard stalk traces and both complete count identities agree with those local descriptions. The cyclic `A=0` specialization genuinely changes connectedness/smoothness and is correctly excluded.

## Producer and falsification assessment

The declared five source panels are counted over all four extension degrees, using the unchanged field cap 2401. The producer counts the primitive equations of E, H, D, D2, Z and the conic, every finite base fibre, every rational affine deck point and every rational affine H point in both maps. The projective denominator-zero images and the complete arithmetic infinity terms are retained.

The tests independently verify the two polynomial identities over the integer coefficient ring, include a wrong-coefficient falsifier, and compare prime-field equation enumeration with the square-root-table implementation. They test the normalized branch fibre, both deck relations without cube roots of unity in the base field, the degree-two quotient, changed infinity counts under extension, cyclic/singular rejection, field caps and counterfeit source data.

The genus-two polynomial uses four independent complete counts. The elliptic factors use two and predict two held-out extensions. The degree-six closure polynomial uses the proved source decomposition and is checked against four counted traces; the artifact explicitly does not call that an independent six-count reconstruction. The frozen helper is authenticated before import, with the existing source-authentication chain retained.

## Limits

The result supplies actual covers, arithmetic stalks and two separable degree-three maps. This freeze deliberately does not assert a polarized `(3,3)` Jacobian isogeny, an anti-isometry on torsion, or a particular isogeny kernel; those require an additional argument. Classical quotient, Jacobian, trace and curve-weight principles are not claimed as new. There is no integer-carrier transport or RH conclusion. This is an independent proof/code audit, not an independent execution or formal verification.
