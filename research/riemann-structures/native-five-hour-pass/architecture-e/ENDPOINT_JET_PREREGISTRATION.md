# Endpoint four-jet preregistration

Declared before the endpoint acquisition.  This packet has two sharply
separated parts.

1. Exact rational polynomial algebra reconstructs the signed confluent
   matrix (J4.2), expands its four leading determinants, and compares them
   with the declared odd/even factors (J4.3)--(J4.4).  It also checks the
   reflection factorization of the orthonormal Toeplitz form (J4.5).
2. A fixed 100-decimal-digit reconnaissance evaluates the regular expansion
   (J4.6), records `F^(0)..F^(7)` at `1/2`, the four ordinary eigenvalues of
   the orthonormal repeated-node matrix, and both reflection factors.

The numerical stage uses `mpmath` with the eta-regularized removable value at
one.  It is a scout, not interval arithmetic.  Acceptance therefore records
`endpoint_signs_interval_certified=false`, `local_neighborhood=false`, and
`continuum_four_node_theorem=false`.  No adaptive precision, node search, or
fit is allowed.  The fixed precision is 100 digits and the Taylor order is 8.

Owned files are `ENDPOINT_FOUR_JET_FACTORIZATION.md`, this preregistration,
`endpoint_jet_replay.py`, `ENDPOINT_JET_REPLAY.md`, and
`tests/test_architecture_e_pass_endpoint_jet.py`.  The JSON fixture is typed,
rejects duplicate keys, floats and nonfinite tokens, and binds all owned
source bytes.  Expected resources are below 64 MiB and ten seconds.

