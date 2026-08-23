# X-105220 — Bezoutian and boundary-decomposition replays

These lightweight standard-library replays authenticate the finite exact scope
of `R-105202--R-105203`, `L-105213`, `L-105216`, and `L-105218`.

Run:

```bash
python -B experiments/X-105220-bezoutian-boundary-decomposition/verify.py \
  --output experiments/X-105220-bezoutian-boundary-decomposition/results/verification.json

python -B experiments/X-105220-bezoutian-boundary-decomposition/verify_inertia_split.py \
  --output experiments/X-105220-bezoutian-boundary-decomposition/results/inertia_split_verification.json
```

Expected verdicts:

```text
PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION
PASS_X_105218_CRITICAL_NODE_INERTIA_SPLIT
```

The first checker uses exact `Fraction` arithmetic and a complete-real-line
Sturm count. It verifies:

- the Bezoutian residue factorization on four polynomial packets;
- exact diagonalization on their critical points;
- the five-real-root counterexample to subunit residue coherence;
- the exact pairwise residue-dispersion identity;
- the differential chord-polarization identity at rational fixtures.

The second checker verifies:

- exact block congruence of the critical-node packet to
  `(-H D H) direct_sum R`;
- exact recovery of the boundary matrix as the Schur complement;
- the four-point separator showing order-three packet positivity does not
  bootstrap to all packet sizes.

The combined retained result contains 237 exact rational/Sturm/block checks.
Neither checker authenticates the entire-function Cauchy exhaustion,
positivity of the boundary Loewner kernel, `PRES105220`, `BRP105220`, or RH.
