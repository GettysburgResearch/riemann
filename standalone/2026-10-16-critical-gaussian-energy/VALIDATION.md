# Validation and limitations

## Historical recovery

The saved factorization ZIP was extracted; all payloads passed their original
manifest. Its ordinary and optimized checker outputs reproduce RESULTS.json
(49,777 predicates). The local Git tree b627f8da787a9857d60a29f1e637e6e5b22b979a
matches the connected GitHub recursive read-back, including the manifest.
Recovery commit: bf55bad693d147747bdb8074fc555d408b60782e, draft PR #952.
Old NOT PUSHED labels are preserved as historical text, not current status.

## New exact checks

`chks/check_energy.py` checks 375 rational square-completion identities, 27
critical-energy Jacobians and degree-uniform exponent bookkeeping. It also
covers EVERY rational ideal norm n<=40,000 in the specified 0/1/m support with
2 and 3 excluded, at m=2,4,6,8. This is a complete rational-prefix MAJORANT
count, not an Eisenstein high-moment computation or a Gaussian experiment.

The reported 210,357 predicates include 160,000 prefix guards and 49,651
support reconstructions; the count is not independent research evidence.
Seven finite false-substitution checks are included. Separate `python -O`
processes with a wrong CDF shift, energy Jacobian and root embedding were
executed and rejected; see MUTATIONS.json. Ordinary/optimized EXACT.json
outputs agree byte for byte. The analytic inequalities are proved in the
note, not by these finite counts.

## Separate, non-certified numerical check

At 60 decimal digits, direct logarithmic-scale quadrature and the explicit
pair kernel agree to relative tolerance 1e-45 on eight finite Eisenstein
polynomials: m=2 or 6, four stated rows, and all 27 occupancy patterns at the
three prime ideals of norms 7,7,25. Original character zeros remain. This is
NOT all native ideals, an infinite Gaussian source, directed interval
arithmetic, or an asymptotic estimate. Results are in NUMERICAL.json.
Ordinary and optimized runs reproduce all rounded reported fields exactly.

The first numerical adapter mistakenly interpreted the helper's zeta_6 basis
as its separate omega basis. Both energy assemblies shared that adapter, so
their mutual agreement alone did not detect it. Inspection of the unchanged
primitive helper exposed the issue. The adapter was corrected; independent
unit-root, multiplication and direct exponential character checks were added,
and both complete numerical runs were repeated. Only the corrected results
are published. The wrong-root process mutation now fails before quadrature.
The mathematical square-completion and all exact prefix checks were unaffected.

## Review boundaries

All proofs/code have one author; no independent agent or human referee, Lean
build, imported theta reconstruction, or full-repository/remote CI was run.
The helper is recovered #936 source, not an independent arithmetic backend.
The current external paper landing page was checked; no PDF was analyzed in
this continuation. #950/#951 overlap is credited at the stated reading scope.

The principal source's critical off-diagonal estimate is OPEN. No complete RH
proof, numerical zero-free improvement, or generalized full native moment is
asserted. The actual accomplishment is publication of the prior work and the
energy kernel/diagonal/truncation/transfer statements at their stated scope.
