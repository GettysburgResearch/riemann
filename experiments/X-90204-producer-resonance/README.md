# X-90204 — Certified resonance of the frozen binary–ternary producer

This package supports `L-90207` and `T-90204`.

It targets the **actual sparse producer trace at `n=2`**, not merely one GFEP
exit.  For this trace

```text
G(2)=2,
G(3)=2,
a(2)=2,
a(3)=0,
a(4)=2,
```

and the exact increment recurrence of `L-90205` determines every later
coefficient.

## Run

```bash
python3 verify.py
```

Required dependency:

```text
mpmath
```

A successful run prints

```text
PASS_X_90204_PRODUCER_RESONANCE
```

and rewrites `results/verification.json`.

## What is certified

The script checks the explicit characteristic

```text
Delta(u)=1-1/2[2^(1-u)+3^(-u)+(3/2)^(-u)]
```

near

```text
u_c = 0.94935582067958621159...
      +45.67580547243676992334... i.
```

The certificate has four layers.

### 1. Rouché root enclosure

At 80 digits, with an independent `mpmath.iv` interval evaluation at the
center,

```text
|Delta(u_c)| < 4.4e-60,
|Delta'(u_c)| > 0.6722.
```

An explicit second-derivative bound on the radius `1e-10` disk gives a positive
Rouché margin greater than `6.7e-11`, so exactly one simple characteristic root
lies in the disk.

### 2. Producer-boundary noncancellation

The continued numerator

```text
N(u)=B(u)+1/2 R2(u)+1/2 R3(u)
```

is evaluated through `50,000` recurrence coefficients at 80-digit working
precision.  The finite partial has modulus about `0.0156037`.  The **analytic
infinite-tail bound** from `|a(m)|<=2` is below `0.005827`, and the entire
root-disk variation is below `8.2e-8`.  The retained lower bound is

```text
|N(u_*)| > 0.0097.
```

Thus the characteristic zero is genuinely excited by the sparse producer.

### 3. Zeta noncancellation

The alternating eta series is summed through `10,000` terms.  Pairing
consecutive terms gives an explicit infinite-tail estimate below `0.007673`.
After disk variation,

```text
|eta(u_*)| > 0.6139,
|1-2^(1-u_*)| > 0.2503,
```

so `zeta(u_*) != 0` without importing a numerical zero table.

### 4. Critical-shift pole

Therefore the Mellin transform of

```text
F(X)=2 A_X(2)
```

has a genuine nonreal pole at

```text
s_*=u_*-1/2,
Re(s_*) > 0.4493558205795862.
```

`T-90204` supplies the exact Landau argument transferring this to integer
endpoints and proving polynomial positive and negative oscillations.

## Assurance scope

The recurrence, infinite tails, derivative bounds, integer interpolation, and
Landau consequence are analytic statements in the accompanying markdown
proofs.  This script certifies the finite transcendental inequalities with very
large margins.  The two load-bearing characteristic point evaluations are also
replayed with directed interval arithmetic.

The package does **not** locate the first negative endpoint.  Direct finite
reconnaissance remains positive for a very long range; the theorem is cofinal
and analytic rather than a finite counterexample search.
