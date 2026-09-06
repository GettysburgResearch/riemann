# Final-pass validation boundary

The authenticated original X-105659 source (Git blob
`e708af8c5235b71e7382d43220236536fc3f20a8`) fails in ordinary Python 3.13 /
SymPy 1.14.0 and in the completed original-source optimized run. Fixing only
the formal-generator substitution still fails the advertised coefficient
positivity. The separately identified invariant-cone repair passes in ordinary
mode and reconstructs its polynomial certificate and four rational fixtures.
The grouped subsequent optimized attempt was interrupted: no optimized PASS
for the repaired theorem or fresh replay of the old 10,225 controls is claimed.

`replay/verify_small_controls.py` passes in both ordinary and optimized Python
with identical output. Its seven named groups cover the literal quartic
Bezout matrix and characteristic polynomial, critical residues, determinant
factors, the three cone repairs, nineteen finite Beta coefficients, and the
forced unit determinant factor. It is not the infinite analytic proof.
A draft matrix transcription in F01 was corrected after this fresh check;
the two-negative-square conclusion was unchanged.

The package validator passes normally and under `-O`. Seven distinct packet
mutations are rejected in each mode: invalid source SHA, unregistered claim
source, altered proof, float count, duplicate JSON key, changed RH flag, and
changed authenticated author code. These fourteen refusals concern inventory
and integrity, not source theorem truth.

Historical uploader/coordination records outside the delivered packet remain
on the branch and are excluded explicitly from its manifest. The pass-2
packet, validator and replay records are archived verbatim. No research
branch, main, workflow, permission or trusted formal module is modified.
