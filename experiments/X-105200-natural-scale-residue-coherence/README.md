# X-105200 — Natural-scale Xi residue coherence

This replay authenticates only exact finite algebra used by the packet:

- Sturm-exact factor-two reverse-Rolle conservation on rational polynomial fixtures;
- the residue-coherence defect inequality;
- the exact Gaussian-model critical-residue formula;
- the mean/variance transfer constant.

Run:

```bash
python -B experiments/X-105200-natural-scale-residue-coherence/verify.py \
  --output experiments/X-105200-natural-scale-residue-coherence/results/verification.json
```

Expected verdict:

```text
PASS_X_105200_NATURAL_SCALE_RESIDUE_COHERENCE
```

The replay does **not** authenticate the Laplace saddle estimates for the Xi
Fourier kernel, the uniform natural-height Rouché theorem, the actual-Xi
residue asymptotics, any low-order coherence estimate, boundary winding, or
RH. Those are mathematical proof obligations in the claim files.
