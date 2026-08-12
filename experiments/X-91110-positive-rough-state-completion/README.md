# X-91110 — Positive SHARP-preserving rough-state completion

Companion replay for `L-91319`.

```bash
python3 experiments/X-91110-positive-rough-state-completion/verify.py
sha256sum -c experiments/X-91110-positive-rough-state-completion/SHA256SUMS
```

Expected verdict:

```text
PASS_POSITIVE_SHARP_PRESERVING_ROUGH_STATE_COMPLETION
```

The checker performs exact arithmetic in
`Q[r]/(r^2-1/p)` for representative primes. It verifies:

- the signed rough Euler matrix;
- its minimal entrywise-positive completion;
- exact preservation of the SHARP functional `(1,2)`;
- strict improvement of the endpoint-score functional `(2,1)`;
- positivity of the completed matrix for `p>=5`.

The replay proves finite algebra only. It does not solve the remaining
colored-to-uncolored physical-column projection or prove RH.
