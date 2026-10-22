# X-23801 — Carry sandwich exact interfaces and reconnaissance

This experiment has two deliberately separated scopes.

## Exact standard-library checks

`verify.py` checks:

1. the exact floor-sum formula for `beta_(nq)`;
2. the average Legendre/Kummer carry identity through a finite range;
3. the exact Möbius adjoint formula
   ```text
   sum_(k<=n/m) mu(k) beta_(n,mk)=(2m-n-1)/(n+1);
   ```
4. nonnegative feasibility of the canonical descending greedy packing at small
   endpoints;
5. deterministic proof-object replay and mutation rejection.

Run:

```bash
python verify.py results/exact-verification.json
python -m unittest discover -s tests -v
```

Retained exact-interface digest:

```text
44b2b584775278a14324650f7709a59b81a9aa4b61c1cab682135b587cfac8bd
```

## Discovery-only reconnaissance

`recon.py` uses ordinary double precision to scan larger finite endpoints. The
retained run through `X=5000` found:

- no off-diagonal greedy saturation;
- no negative diagonal inverse coefficient;
- signed half-`n` mass approaching `4 sqrt(X)`;
- binomial-entropy deficit consistent numerically with a logarithmic, rather
  than power-scale, loss.

These observations nominate the Carry Obstacle theorem. They are **not**
directed certificates and make no RH inference.

Run:

```bash
python recon.py --output results/recon-5000.json
```

## Proof boundary

The exact files validate algebra and finite code paths only. Neither the
subpolynomial carry sandwich nor the quotient-layer obstacle theorem is proved
by this experiment.