# Validation, review, and exact scope

## Accepted mathematical statement

The new claim is the rational-parameter corollary in
[UNIFORM_BOUNDARY.md](correlated/UNIFORM_BOUNDARY.md), with boundary
\(43744333/50000000\). Its hypotheses are the analytic inputs expressly
stipulated by Xu--Sang, arXiv:2610.15291v2. Its global consumer is their
general Lemma 8.1, with the moment parameter licensed by their first stage.
The computation proves that the new tuple satisfies every numerical
hypothesis of that consumer.

The source version and normalization are fixed in the proof and JSON
receipt. The endpoint is equation (28), with the row exponent of equation
(21); the complete scalar list is Section 6.2. We do not substitute an
isolated numerator estimate for the full remainder proposition.

## Arithmetic and coverage

- Every accepting operation uses arbitrary-size integers and rational
  arithmetic through Python's standard-library Fraction class.
- The positivity certificate covers the whole rectangle
  \(0\le\delta\le5/6,\ 0\le x\le1/2\). It uses a polynomial identity and
  positive coefficients, not sampling, interpolation, or an estimated
  Lipschitz constant.
- All 21 strict scalar margins and three inclusive margins are
  reconstructed. The exact stage-zero license is checked separately from
  the candidate conclusion.
- The principal polynomial implementation expands in one variable. The
  independent implementation constructs a bivariate rational ring and
  clears the denominator directly. It imports no parent code or
  coefficient table.
- Both implementations remain active under Python optimization.

## Replays

From this packet directory:

    python -S -B verify_packet.py --replay

This checks the exhaustive file manifest and then copies the verified
sources into a fresh temporary directory. It runs the parent and
independent reconstruction in both ordinary and optimized Python. All
four resulting receipts must match their frozen counterparts byte for
byte, and the two distinct receipt formats must agree on all parameters,
scalar margins, and coefficient arrays.

The verifier also runs one negative mathematical control: keeping the
same \(b,\kappa,g\) while requesting boundary \(0.87488664\) must reject at
the discriminant positivity predicate. An unrelated error is not accepted
as that rejection. The exact fixed-\(\kappa\) limit is a separate
mathematical theorem; failure of this sufficient certificate alone would
not prove impossibility.

The checks require no numerical libraries, network access, zero tables,
or external executables. Exploratory floating-point searches were used to
locate candidate parameters during development; they are not part of the
proof or accepting payload.

## Independent reviews

The following reports bind the reviewed mathematical objects by SHA-256:

- [Final boundary review](review/UNIFORM_BOUNDARY_FINAL_REVIEW.md) checks
  the frozen proof, both parent code files, the parent receipt, the
  independent code and receipt, and their exact agreement.
- [Analytic interface review](review/XU_ANALYTIC_INTERFACE_REVIEW.md)
  checks the complete numerical interface, the preceding-stage license,
  all-target saving and all-height closure.
- [Independent parameter derivation](review/XU_PARAMETER_INDEPENDENT_REVIEW.md)
  records the separately reconstructed positivity proof.
- [Joint numerator review](review/JOINT_NUMERATOR_INDEPENDENT_REVIEW.md)
  audits the proposed mixed-moment and contour comparison.
- [Principal and quartic review](review/PRINCIPAL_QUARTIC_REVIEW.md)
  audits the coupled Mellin residue, full quartic Möbius encoding,
  signed tensor normalization and the precise scope of the period
  obstruction.
- [Coordinating mathematical review](review/COORDINATOR_MATHEMATICAL_REVIEW.md)
  records direct checks of the native crossing calculation,
  direct-estimate floor, principal/quartic identities and theta arguments.

The coordinating agent also read the native, quadratic, theta, and heat
arguments. The native balance bound was corrected before publication:
its constant bound applies only on the specified crossing set. The new
whole-prefix crossing calculation was then checked with the actual
Mellin normalization, its complete frequency error, and the literal
physical window.

These are independent agents in one AI session, not external human
referees, proof-assistant verification, or a new independent reconstruction
of the upstream analytic manuscripts.

## What is and is not authenticated

The manifest and Git blob identities authenticate the published payload.
The two algebra implementations authenticate the new rational parameter
calculation against the named source formulas. The mathematical reviews
check the explicit application of the imported consumer.

They do not authenticate the original cubic-theta reflection, inverse
moment, plain fourth moment, all-family \(7/8\) theorem, or all analytic
extensions proved in Xu--Sang. The new global corollary retains these
dependencies visibly. No RH resolution, effective numerical height
threshold, or repository-wide test/CI result is asserted.

The other attack notes have their own scopes and source qualifications.
A lower limit for an upper-bound recipe is not a lower bound on the actual
arithmetic expression. A counterexample in a broader Fourier-kernel class
does not change the actual modular theta kernel. Those distinctions are
part of the statements being reviewed.
