# Three-cluster replay record

Status: INDEPENDENTLY REVIEWED AND FROZEN.

The producer pins the frozen mixed packet a7334a169cfa8ca5b1f0721692d9c888e79ba5cb
and its transitive E4/theta chain. It reconstructs all original finite source
matrices rather than importing a claimed rank.

Ruff passed. Producer write, check and optimized check passed. All 17 tests
passed in ordinary Python (1.550 s) and optimized Python (1.514 s). Final
proof SHA-256:

    a8790484f717774dfbae5644fab4219ae64022f8022737a1f14868e7c1c9f408

The replay checks the exact Sylvester column, both block inverse products,
a cubic functional-calculus control, literal exponential functions and the
Newton residual, plus every rational source bound. It samples no Xi values
and does not prove the continuum theorem from three panels.

The root reviewer reran the producer in ordinary and optimized modes and all
17 tests in ordinary and optimized Python.  The four runs passed.  The proof
was also checked for the source reserve, Sylvester normalization, Schur factor
of two and the explicit boundary residual; no wider four-node claim is made.
