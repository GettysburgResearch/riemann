# Coherent quadratic graded algebra: exact replay

The [proof](COHERENT_QUADRATIC_GRADED_ALGEBRA.md) distinguishes the
fixed-twist module R_n tensor chi from the unital graded algebra
R_n tensor chi^n. The latter uses the actual two-colour multiplication
on the joint S4 times C2 cover and has even-grade principal poles.
Its two positive scalar-resonance weights come from Z_tilde and its
constant quadratic twist, rather than the signed regular trace of the
fixed-twist module.

The runtime authenticates the preceding source adapter at
`c0b197918936d8ad360f462702855020fb26ac67` before importing it. That
adapter authenticates the actual S4 quadratic-cover reconstruction at
`c67d858fc9f7112cf9f0b13049a97d68de0d429b` and its full dependency chain.
No new polynomial reconstruction is fitted here. Primitive recounts
remain at field orders 5, 25, 7 and 49. Only the p=5 panel has the full
degree-ten constituent; the two p=7 panels retain their four-trace limit.

The exact controls compare multiplication colours, cohomological grade
parity, all ramified infinity factors, source-fibre and cohomological
power traces, finite functional equations, independently bounded
determinant logarithms, both scalar weights and positive radial probes.
The grade-zero rational factor is kept separate, including its sign
outside the initial arithmetic Euler disk. The proofs establish the
infinite source and boundary statements; finite probes do not replace
the all-grade or all-root arguments.

From the repository root, using the serialized Python runtime:

```text
python research/l-families/atlas/generalized/koszul-analytic-parent/coherent_quadratic_replay.py --check
python -O research/l-families/atlas/generalized/koszul-analytic-parent/coherent_quadratic_replay.py --check
python -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_coherent_quadratic.py
python -O -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_coherent_quadratic.py
```

The root agent's serialized focused Ruff checks, producer write/check,
optimized producer check and all 24 tests in each Python mode passed.
Independent proof review has completed; runtime and exact-freeze review
are pending. The owned fixture binds
this note, proof, runtime and substantive tests with LF-normalized
SHA-256 digests and validates complete JSON values, including types.
