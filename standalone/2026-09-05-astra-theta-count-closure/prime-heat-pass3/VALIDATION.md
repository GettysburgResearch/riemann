# Execution and publication boundary

The new verify.py was executed in this session in normal Python and under
python -O. Both runs recomputed 17,142 exact rational checks, agreed with the
retained checks.json, and produced byte-identical output.

Four separately corrupted retained results were rejected with nonzero status:
modified total check count, RH flag, global-depth parameter, and machine-proof
flag. The exact executions are recorded in refusal_tests.json. This tests
result-integrity behavior, not mathematical soundness of the analytic proofs.

Checks cover finite Gamma coefficient algebra and majorants, complex contour
moduli, adaptive contour parameters, endpoint removal, two independent Hermite
polynomial reconstructions, exact rational frequency evaluations, the all-scale
mixed-integral normalization, and finite parameter comparisons for depth 10^22.
There is no loop through 10^22 orders. That range follows from the proved
parameter inequalities and the explicitly imported verified zero prefix.

The original parent verify_exact.py was also rerun in both modes: 225 checks
per mode, identical outputs. All 11 original SHA-256 entries passed. During
the first publication, the supplied pass2 verifier was rerun in both modes:
4,104 checks per mode, identical outputs; all 12 pass2 SHA-256 entries passed.
The parent interval low-zero certificate is unchanged but was NOT rerun in
this current session. Its historical execution and mpmath Gamma trust boundary
remain in the parent packet. No full zero verification or new zero census ran.

No proof assistant, external referee, or independent mathematical agent
verified the infinite arguments. No remote CI result or external priority is
claimed. The positive results and the remaining gap are stated in PROOF.md.
The unrestricted mixed inequality and RH remain unproved.

## First publication receipt

The requested prepared 13-file pass2 continuation was published at
401196451ef1b51e5ff4d84dd23bd75bbf9215a1. Its exact subtree is
fc0834a79c6f74f68355b26b3f7357d333d50eef, matching the supplied local files.
Concurrent work at cabc431bdd510205b64be0c829764cb2b7967661 was retained.
An earlier non-fast-forward update was refused, and no force push was used.
The historical no-publication fields inside that immutable supplied packet
refer to the previous authoring session. A PR conversation comment records
the new publication; those historical receipts were not silently rewritten.

The present prime-heat-pass3 packet is a separate add-only continuation.
Its exact publication commit is recorded in the PR conversation after remote
readback, rather than embedded circularly inside its own source files.
