# X-19802 — Green compression counterexample

This exact `fractions.Fraction` regression tests the proposed implication

```text
Green Euler orthogonality
+ positivity on the trace kernel
+ strict pointwise lifted multiplier contraction
+ CE = I
=> ||CKE|| <= 1.
```

The implication is false.

The retained rational model has

```text
Q = diag(-5/4, 5/4),
K = diag(9/10, -9/10),
CE = I,
||K|| = 9/10,
||CKE|| = 3/2.
```

The first coordinate is the exact Green minimizer in every trace fibre; the
second coordinate is the positive trace-kernel direction. Thus Euler
orthogonality and fibre minimality both hold exactly.

Run:

```bash
python verify.py certificates/synthetic.json
python -m unittest discover -s tests -v
```

The verifier uses only integers and `fractions.Fraction`. Eight fail-closed
mutations are retained in `results/tests.txt`.

The corrected operator theorem is `L-19815`: the observed transfer is the Cayley
transform of the Green moment operator, and contractivity is equivalent to
accretivity of its theta-Hankel anticommutator. Pointwise `K^*K<=I` does not
survive a noncommuting Volterra compression automatically.
