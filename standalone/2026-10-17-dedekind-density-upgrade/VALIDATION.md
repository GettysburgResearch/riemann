# Validation and review limits

## What was proved on paper

PROOF.md gives a proposed unconditional composition using the cited CT, DF
and BGL results: exact family identification with a finite S-unit-twist list;
stability of the needed zero-detector inputs under those twists; the arbitrary
fixed support-scale transfer; all contour sectors; and the Mellin/descent step.
No RH-strength native covariance is inserted as a hypothesis.

The strongest claim is a proposed zero-free region Re(s)>23/24 for every
Dedekind zeta function and finite-order Hecke L-function, with the stated pole
exception. This is not independently refereed. Mathematical correctness of the
analytic adapters cannot be inferred from the parameter certificate.

## What actually ran

* verify.py and python -O verify.py produced byte-identical CHECKS.json.
* Eight unittest methods passed in ordinary Python and optimized Python.
* The direct density calculation checks all ten norm-exponent terms, not merely
  the simplified rational answer, and its height exponents symbolically in the
  field degree. It obtains 2563/4267 and 1+9d/68.
* Thirteen contour vertices satisfy 143 strict linear inequalities. Convexity
  proves whole-segment inclusion on paper; 63 separate rational sample points
  in the tests only cross-check the implementation, not substitute for that proof.
* All seven new margins are compared with separately entered exact values.
  The same exponent implementation reproduces all seven entries of CT v2's
  original Table 1. New normalization 13/20 is checked against the scale monomial.
* Six separately executed corrupted optimized processes are rejected: deleting
  density savings, retaining the old good line, retaining the old normalization,
  closing the large-frequency gap, violating the correction domain, and claiming
  an unpaid larger saving. Duplicate JSON keys and floating-point inputs are
  rejected as well. No numerical zero search or native ideal census was run.

An initial combined container command completed the ordinary suite but hit
its wall-time limit during the second suite. The optimized suite was then
rerun on its own and completed with all eight tests passing. This was an
execution timeout, not a failing mathematical assertion. No failed output
was recorded as a successful optimized replay.

The exploratory floating-point optimization used to scout parameters is not
part of the proof or acceptance rule. The published witness uses only rational
inputs and a fixed positive slack. No optimality claim is made for 23/24.

## Publication and integrity

The source base is #955 at 6d3d69c7896e3a5d61d1f67e4627125257398ec7. Publication
adds this one standalone directory only. MANIFEST.json records the exact
SHA-256, Git blob identity and length of every other payload. The manifest
is an integrity record, not a mathematical certificate or independent review.
The external papers are linked at their versions, not included as newly
verified library source. No main or integrated-scientific-status change is made.

The final publication receipt, branch and head are provided separately with
the download and PR. Remote blob read-back and a ZIP-extraction replay are
reported there only after they actually complete.

## Priority review targets

1. The entire finite S-unit-twist family, including zero masks and the equality
   between full sixth-power-free index norm and CT's q_u.
2. PROOF Section 3's complete-column central mean and use of the BGL detector:
   check fixed twists, conductor bounds, all powerful terms, and the primitive
   versus omitted-Euler-factor convention.
3. Whether CT's Section 9 rescaling really applies at M=213/200 with unchanged
   weights. The proof relies on the explicit arbitrary-fixed-M>1 statement.
4. Contour movement within the full correction domain, the simultaneous height
   cutoffs, and the changed Mellin normalization 13/20.
5. The distinction between an all-field 23/24 refinement and a stronger ordinary
   Riemann-zeta result. This packet does not improve the reported 7/8 bound.

No independent referee, Lean build, remote CI run, or full-repository validator
was performed. The intended review is substantive mathematical review of a
claimed boundary improvement, not acceptance based on a large check count.
