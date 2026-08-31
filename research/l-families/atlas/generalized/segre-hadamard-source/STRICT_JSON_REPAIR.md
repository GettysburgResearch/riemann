# Strict JSON acceptance repair after the first source freeze

The scientific source at6c376a481f73957ecad764a81281206862bb6750 remains
reachable and unchanged in Git. Its exact arithmetic and recorded Tor data
are not retracted. Root's independent code review found an acceptance bug:
the final checker compared parsed Python dictionaries, which treats1,True
and1.0 as equal. A changed count could therefore pass with the original
stored proof-object digest, because the candidate digest was not separately
recomputed before that equality test.

This repair replaces the final comparison with canonical serialized JSON,
which preserves those distinctions and rejects nonfinite numbers. Three
regression tests cover the actual historical trap, nonfinite counterfeits,
and legitimate object-key reordering. The mathematical proof, source maps,
input pins, and exact arithmetic algorithms do not change. The producer and
test hashes, and consequently the enclosing fixture digest, receive a new
identity after regeneration. No historical source commit is rewritten.

Earlier dependent packets authenticate the original immutable Git blobs and
independently reconstruct their own claimed data. They must not describe the
old dictionary comparison as enforcing strict JSON types. This note records
the limitation explicitly. Validation and the repaired freeze will be listed
in the six-hour checkpoint ledger once the memory-gated runs complete.
