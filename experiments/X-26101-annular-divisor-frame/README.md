# X-26101 — Annular divisor-gradient frame

This directory contains exact finite algebra and separately classified floating discovery.

## Exact divisor-gradient algebra

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
- the projection energy identity;
- complete-period orthogonality across different prime bases;
- same-base prime-power covariance controls;
- one rational annular slack/cost ledger;
- seven central and mutation tests.

Retained verdict and digest:

```text
PASS_EXACT_ANNULAR_DIVISOR_FRAME_ALGEBRA
8f9bae3c146f304704a9350977aecd8300b050766c32d2d6a7808d60a118dd44
```

## Exact Hilbert–Farkas and recursive-potential algebra

Run

```bash
python verify_dual.py --self-test --output results/exact-dual-verification.json
```

This checker verifies:

- equality of the finite primal minimum radius and the homogeneous dual ratio;
- a positive KKT dual control;
- the projected-dual update with an exact safe step;
- quantitative monotonicity of the concave dual energy;
- the additive-function second-difference identity;
- five central and mutation tests.

Retained verdict and digest:

```text
PASS_EXACT_ANNULAR_HILBERT_FARKAS_AND_POTENTIAL
02fa7f37eeac8ff06d389e6f8f71b5c24e953ebbfe028d2aaabbbaea87919e1b
```

Both exact objects are synthetic finite algebra. They do not verify `ADF` or RH.

## Floating discovery

Run, for example,

```bash
python recon.py 2000 0.45 0.80
```

This script imports NumPy and uses ordinary floating least squares. It emits frame floors, residual behavior, flow norms, objective cost, and feasibility diagnostics for the active-set iteration.

Its output is classified

```text
FLOATING_RECONNAISSANCE_ONLY
```

and is excluded from both exact proof objects. In particular, the runs show that the total positive-residual norm can increase on individual active half-steps; that overstrong invariant has been withdrawn in `L-26103/L-26106`.

## Proof boundary

```text
exact divisor-gradient and projection algebra   checked
Hilbert-Farkas duality and monotone potential    checked
complete-period chain model                     checked
initial residual L2 budget                      proposed complete
Annular Dual Frame inequality                   open
annular repair -> prime ramp -> RH               conditional
Riemann Hypothesis                              unproved
```