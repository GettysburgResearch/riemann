# X-15613 — Joint profile-soft direct-short verifier

This standard-library-only checker replays the finite core of `L-15632`.
It verifies:

- positivity of the joint main profile Gram;
- the actual soft-profile threshold;
- both sides of the relative joint remainder LMI;
- positivity of the ambient block;
- the exact main-profile harmonic solve;
- the `L-18512` direct-short identity;
- the explicit negative-part bound

  ```text
  4 (epsilon + 4 epsilon^2) log(R) tau.
  ```

The retained control deliberately has a negative exact shorted value:

```text
S = -1201/100000,
```

while the theorem bound is

```text
3/25.
```

Run:

```bash
python verify.py certificates/synthetic.json \
  --json-out results/synthetic-verification.json
python -m unittest discover -s tests -v
```

The artifact checks finite operator algebra only. It does not contain a
production Suzuki profile Gram, prime manifest or cofinal support sequence.
