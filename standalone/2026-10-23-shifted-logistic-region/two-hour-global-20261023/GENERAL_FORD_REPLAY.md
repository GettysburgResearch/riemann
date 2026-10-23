# Exact scalar replay for the weighted Ford and Poisson-tail components

2026-10-23. Author replay, not an independent mathematical review.

The frozen analytic inputs are:

- GENERAL_WEIGHTED_FORD_DETECTOR.md:
  `c52fa826706a26aec19cf0ed448ca4944dd86ad45ec67cc69da106fef5e6bf50`.
- POISSON_KERNEL_ZERO_TAIL.md:
  `c862b1e3087fd4d8e8cf52c7463f9e5786121a3f71cae1dc602bf18948b35c3b`.
- verify_general_ford.py:
  `da64b1b653dfb771773efc530e2ffbe605f665f835251e578891f888c89cfa27`.

Both `python -I -S -B verify_general_ford.py` and
`python -I -S -B -O verify_general_ford.py` completed successfully.
Their captured JSON files are byte-identical, SHA256
`ac0d04a6f5e68b5ef316a17f5e7d99ca0ef44bf18523bbed424f27c89336a039`.
The normal file is GENERAL_FORD_CERTIFICATE.json. All acceptance
conditions use explicit exceptions, so optimized Python retains them.

The key refined endpoint is R=19/4, log-height60, whose rational
interval lower margin is greater than .00007985918. The proof of
monotonicity in the accompanying note turns this endpoint into an
infinite-tail exclusion at the minimizing zero. The finite checker
itself does not prove that analytic step or any imported zeta result.

The checker also verifies six original weighted endpoints, three
other refined endpoints, six negative controls, and the elementary
side conditions for the kernel and monotonicity. In particular it
certifies w0>6, global curvature<70, and c4(R0=139)<1.08, the inputs
needed by the separately authored prime-gain certificate.

The interval engine follows the earlier exact logistic replay's
Fraction and Taylor design. This is not an independent implementation
of that engine. The new scalar expressions, endpoints, and side
conditions are independent work specific to this component. A full
R=19/4 theorem additionally requires the complementary low-height
rectangle and the global minimum argument, with source and human
mathematical review still distinct from these finite computations.
