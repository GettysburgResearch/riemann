# X-zeta23-zero-heat-monotonicity

Finite regression for the first-Hermite Gaussian / zero-heat continuation of PR #375.

The experiment checks only closed-form finite identities and synthetic controls:

- Fourier inversion of the first-Hermite autocorrelation;
- the confluent limit of the PR #375 three-Gaussian residue kernel;
- the exact negative target-pair value;
- the heat-derivative identity;
- the telescoping square budget in the new terminal graph;
- convergence to the target multiplicity on a finite synthetic terminal packet;
- domination of a finite von Mangoldt tail by the all-integer Gaussian envelope.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_FIRST_HERMITE_ZERO_HEAT_MONOTONICITY
```

The replay does **not** prove the abstract infinite-multiset terminal theorem, the Guinand--Weil formula, the all-prime inequality, the corrected-kernel floor, or RH.
