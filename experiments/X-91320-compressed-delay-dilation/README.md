# X-91320 — exact compressed-delay dilation regression

This experiment checks the finite polynomial model of `L-91322`.

For the inner function `Theta(z)=z^m`,

```text
K_Theta = span{1,z,...,z^(m-1)}.
```

An integer raw delay multiplies by `z^(-k)`.  It generally leaves the model
space, but it splits uniquely into

```text
nonnegative powers = compressed backward shift;
negative powers    = escaped Hardy prefix.
```

`verify.py` uses exact Gaussian-integer arithmetic to check:

- the pairwise raw Gram equals resident Gram plus leakage Gram for every pair
  in a five-vector packet;
- the full packet Pythagorean identity;
- the compressed-delay semigroup law;
- invariance of the compressed state in `K_(z^m)`;
- a concrete counterexample to raw-delay invariance.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_COMPRESSED_DELAY_DILATION
```

The script is a regression for the algebraic geometry, not evidence for the
remaining arithmetic inequality or for RH.
