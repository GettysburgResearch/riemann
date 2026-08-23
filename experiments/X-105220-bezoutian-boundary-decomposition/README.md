# X-105220 — Bezoutian and boundary-decomposition replay

This lightweight standard-library replay authenticates the finite exact scope
of `R-105202`, `L-105213`, and the algebraic chord identity in `L-105216`.

Run:

```bash
python -B experiments/X-105220-bezoutian-boundary-decomposition/verify.py \
  --output experiments/X-105220-bezoutian-boundary-decomposition/results/verification.json
```

Expected verdict:

```text
PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION
```

The checker uses exact `Fraction` arithmetic and a complete-real-line Sturm
count. It verifies:

- the Bezoutian residue factorization on four polynomial packets;
- exact diagonalization on their critical points;
- the five-real-root counterexample to subunit residue coherence;
- the exact pairwise residue-dispersion identity;
- the differential chord-polarization identity at rational fixtures.

It does **not** authenticate the entire-function Cauchy exhaustion, positivity
of the boundary Loewner kernel, `PRES105220`, `BRP105220`, or RH.
