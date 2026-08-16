# X-93300 — Exact cubic-shell and balanced-dispersion regression

Run from the repository root:

```bash
cd experiments/X-93300-cubic-shell-dispersion
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_CUBIC_SHELL_BALANCED_DISPERSION_REDUCTION
283634ae3674d2a5059c79528c1b02a37bdb7d43b8b3210fd20f3aeb2e5835dd
```

The checker uses only Python's standard library and exact `Fraction` arithmetic.

It verifies:

- the scale-four cubic source reorganization;
- exact prime-block reconstruction;
- the large-prime single-power shell;
- all four discrete grid residue formulas through \(M=512\);
- the exact Vaughan identity on eight formal arithmetic fixtures;
- the grouped Type-II coefficient \(a_U\);
- the separate four-adic gauge;
- the First-Hermite Fourier-symbol algebra;
- fail-closed mutations of the source, factor four, Vaughan sign, and divisor threshold.

It does **not** prove BCD or RH, run a prime-distribution campaign, inspect zeta zeros,
or import the First-Hermite one-carrier exclusion.
