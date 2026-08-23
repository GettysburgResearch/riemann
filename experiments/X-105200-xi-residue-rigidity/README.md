# X-105200 — light residue-rigidity replay

This standard-library replay checks only the finite algebra after the analytic
saddle theorem:

- the exact sign and common scale of the trigonometric-model residues;
- the exact coherence/variance identity;
- the integration-constant firewall;
- the natural-window adjacent-phase scaling surrogate;
- fail-closed status flags.

It does **not** replay the Xi Fourier saddle, Rouché argument, or any heavy
zero computation.

```bash
python -B experiments/X-105200-xi-residue-rigidity/verify.py \
  --output experiments/X-105200-xi-residue-rigidity/results/verification.json
python -B -m unittest discover \
  -s experiments/X-105200-xi-residue-rigidity/tests -p 'test_*.py' -v
```
