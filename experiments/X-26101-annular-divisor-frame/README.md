# X-26101 — Annular divisor-gradient frame

This directory contains two deliberately separate layers.

## Exact finite algebra

Run

```bash
python verify.py --self-test --output results/exact-verification.json
```

The checker uses only Python integers and `fractions.Fraction`. It verifies:

- cumulative divisor-comb flow equals the negative divisor-gradient sum;
- every prime-power constraint update equals the rectangular Gram action;
- the formal von-Mangoldt identity for `log(m/(m-1))`;
- exact minimum-norm projection on a rational toy annulus;
- exact halving of the active residuals;
- the pseudoinverse energy identity;
- complete-period orthogonality across different prime bases;
- same-base prime-power covariance controls;
- one rational annular slack/cost ledger;
- seven central and mutation tests.

Retained verdict:

```text
PASS_EXACT_ANNULAR_DIVISOR_FRAME_ALGEBRA
```

Proof-object SHA-256:

```text
8f9bae3c146f304704a9350977aecd8300b050766c32d2d6a7808d60a118dd44
```

This is synthetic finite algebra. It does not verify `SAF` or RH.

## Floating discovery

Run, for example,

```bash
python recon.py 2000 0.45 0.80
```

This script imports NumPy and uses ordinary floating least squares. It emits frame floors, residual contraction, flow norms, objective cost, and feasibility diagnostics for the active-set iteration.

Its output is classified

```text
FLOATING_RECONNAISSANCE_ONLY
```

and is excluded from the exact proof object.

## Proof boundary

```text
exact divisor-gradient and projection algebra   checked
complete-period chain model                     checked
all-X source-specific SAF theorem               open
annular repair -> prime ramp -> RH               conditional
Riemann Hypothesis                              unproved
```
