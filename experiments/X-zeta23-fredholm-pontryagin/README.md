# Final-strike research packet

This packet contains two complementary results.

1. **`FREDHOLM_PONTRYAGIN_COMPLETION.md`** constructs a Gaussian-confined trace-class global compression of Weil's form. It turns RH into positivity of one Fredholm determinant on the positive real axis, equivalently positivity of every shifted moment Hankel matrix or exterior coefficient. It proves that false RH produces a negative coefficient at a finite exterior degree and finite prime cutoff.
2. **`INNER_PHASE_BANK_STRIP_NORM_FIREWALL.md`** proves that powered inner/all-pass channels pay exponential cost in every strip/form norm controlling off-line evaluation. Critical-line unitary norm and a polynomial derivative gauge do not imply the missing full arithmetic bound.

The executable regression is `verify.py`. It checks finite-dimensional algebra, the quantitative finite-degree bound, the exact Gaussian overlap law, phase-bank multiplier growth, exterior-power amplification, Hankel detection, truncation stability, and noncommutative word expansion.

Run:

```bash
python3 verify.py --json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_FREDHOLM_PONTRYAGIN_FINAL_STRIKE
```

**RH is not claimed proved.** The remaining theorem is all-order prime-side positivity of the Fredholm determinant or shifted Hankel matrices.
