# Finite algebra validation

`verify.py` passed under both isolated ordinary and optimized Python:

```sh
python -I -S -B verify.py --output CHECKS.json
python -I -S -B -O verify.py --output CHECKS.optimized.json
```

The two JSON files are byte-identical. The retained receipt is `CHECKS.json`.
The script SHA-256 is
`d53793f80b4495ccbb766a05751a524f59be2f1138ab737b340c4bb3e8040267`.

There are 9,816 exact predicates over six finite fields and both sextic
orientations. Every predicate uses integers in an explicit cyclotomic basis;
there are no tolerance comparisons. The field model, multiplicative generator,
kernel digest and per-family counts are recorded for each case. Checks remain
active under `-O` because failure uses explicit exceptions.

The negative controls verify that a missing nonunit zero, reversed Gram
character, and erased local shift axis violate the expected identities. They
are finite counterexamples to the deliberately wrong formulas, not mutations
of the mathematical proof or an external library.

These checks certify only the finite instances described in `LOCAL_KERNEL.md`.
The all-field identities have written elementary proofs. FKMS, hypergeometric
monodromy, conductor facts, and native arithmetic asymptotics are not proved by
the checker. No global inverse-moment improvement is claimed.
