# Agent continuation report — FIR screw cone and adaptive zero deflation

Agent: `gpt56-08`  
Issue: #95  
Pull request: #98  
Branch: `agent/gpt56-08/95-screw-prime-knot`  
Date: 2026-07-26  
Classification: two proposed proof units, one directed positive control, and empirical search guidance; no counterexample claimed

## Executive result

The scalar prime-knot route has expanded into a complete arithmetic-progression
filter cone.

> **EUREKA 1 — the zeta screw matrix is an FIR energy table.**  Under RH, every
> exact zero-sum coefficient vector `c` satisfies
> \[
> -\sum_{i,j}c_i\overline{c_j}\Psi((i-j)h)
> =\sum_\gamma\frac{|P_c(e^{i\gamma h})|^2}{\gamma^2}\ge0.
> \]
> Equally spaced screw witnesses are therefore finite impulse-response filters
> acting on the zero-ordinate spectrum.

> **EUREKA 2 — one increment Toeplitz matrix parameterizes the whole cone.**
> Writing `P_c(z)=(1-z)B(z)` converts every zero-sum filter uniquely into one
> vector `b`, with RH consequence
> \[
> b^*H^{(n)}(h)b\ge0,
> \quad
> H_{ij}=\Psi((i-j+1)h)+\Psi((i-j-1)h)-2\Psi((i-j)h).
> \]
> A negative exact Rayleigh contraction would be a finite RH counterexample.

> **EUREKA 3 — exact resonance ranking needs no `Psi` values.**  At
> `h=log(p)/d`, the derivative jump of any frozen filter is
> \[
> 2d\log p\sum_r r p^{-r/2}\operatorname{Re}\rho_{dr}(c),
> \]
> where `rho_k` are exact coefficient autocorrelations.  Candidate prime-power
> events can be ranked before any directed special-function work.

The first full Toeplitz search found a binary64 margin around `1.9e-5`.  I
froze the mode to exact 24-bit dyadics and completed a 128/192/256-bit directed
MPFR replay over every required prime power.  The result is strictly positive,
so that exact mode is excluded.

The same matrix was then decomposed heuristically over the first 600 critical-
line zero pairs.  Reoptimizing after subtraction lowered the residual minimum
to approximately `5.06e-6`.  The contribution is highly concentrated: only
five nonconsecutive zero pairs account for about `44.3%` of the raw frozen-mode
energy.  This motivates adaptive certified zero-bin deflation rather than a
long consecutive zero prefix.

## New proof units

### L-9504 — arithmetic-progression FIR filter cone

This claim proves:

1. the finite FIR spectral identity;
2. the exact increment-Toeplitz parameterization of every zero-sum vector;
3. the RH-conditional Gram expansion of the Toeplitz matrix;
4. a general exact prime-resonance derivative-jump formula;
5. the normalized binomial family `P=(1-z)^m` and its even-denominator cusp
   susceptibility.

The trusted checker interface is especially small.  Given exact `b`, it
reconstructs

```text
c_0 = b_0
c_j = b_j-b_(j-1)
c_n = -b_(n-1)
```

and contracts

```text
-2 sum_k rho_k(c) Psi(kh).
```

No eigenvalue routine is part of a certificate.

### L-9505 — zero-bin deflation and tail box

For the zero Gram vector

\[
 u_\gamma(h)
 =\frac{1-e^{i\gamma h}}\gamma
  (1,e^{i\gamma h},\ldots,e^{i(n-1)\gamma h})^T,
\]

a certified bin gives both:

- a repaired matrix lower block
  \[
  u_\gamma u_\gamma^*\succeq u_cu_c^*-(2G+\eta)\eta I;
  \]
- a sharper fixed-vector lower contribution
  \[
  |v^*u_\gamma|^2
  \ge\max(0,|v^*u_c|-\|v\|\eta)^2.
  \]

If exact bins cover all zeros through `T` and a rigorous reciprocal-square
tail bound is available, the repaired residual obeys the two-sided box

\[
 0\preceq R_{\rm low}\preceq(4nS_T+2E)I.
\]

This creates two disproof modes: residual negativity and residual excess above
the RH tail ceiling.

The proof is self-contained.  Draft PR #90 contains a parallel generic Pick
zero-bin theorem, but L-9505 does not import that unmerged result.

## Reconnaissance progression

### Binomial filters

The normalized filters

\[
 \mathcal B_m(h)
 =\frac{2}{\binom{2m}{m}}
  \sum_{k=1}^m(-1)^{k+1}\binom{2m}{m-k}\Psi(kh)
\]

were scanned first.  At `h=log(2)/2`, the margin decreased from approximately
`0.01318` at order `16` to

```text
B_59(log(2)/2) = 0.006175701225849269
```

at order `59`.  The order-59 derivative jump was approximately

```text
7.217872195781672,
```

with negative left slope and positive right slope in the binary64 evaluation.
This is a genuine exact resonance structure but not a negative witness.

### Full Toeplitz optimization

The full matrix search improved substantially on the binomial family.  A broad
binary64 grid found persistent minima near `log(2)/2` and `log(2)/3`.

The exact case chosen for proof replay was

```text
h = log(2)/3
n = 53.
```

It has three operational advantages:

1. every row threshold is exactly `q^3<=2^k`;
2. the final cutoff is only `208063`;
3. the complete manifest contains only `18778` prime powers.

The frozen discovery values were

```text
binary64 minimum eigenvalue      1.9285536855e-05
24-bit frozen-vector Rayleigh    1.9285536220e-05
24-bit frozen-vector norm^2      0.9999999669.
```

## Directed replay

### Exact input

```text
matrix size                53
step                       log(2)/3
vector denominator         2^24
prime cutoff               208063
prime count                18640
prime-power count          18778
manifest SHA-256           18224939cfbd3d221695e8883e7eabf2d4201697ef6b154c0260b1b9e7cff0d2
```

The producer checks

```text
208063^3 <= 2^53 < 208064^3
```

before performing any special-function work.

### Numerical result

The three producer intervals nest.  The 256-bit result is

```text
[1.928553622308640188310963997625878557364125578418042806481204260290997513959522403925111843e-05,
 1.928553622308640188310963997625878557364125578418042806481204260291025054537139777586645641e-05].
```

The exact standard-library contraction of serialized primitive rows also
nests and has a strictly positive lower endpoint.

### Independent checks

The checker independently reconstructs:

- the zero-sum difference vector;
- all 53 integer autocorrelations;
- the exact rational Rayleigh interval;
- every prime and prime power through the cutoff;
- the canonical manifest hash;
- cross-precision primitive and Rayleigh nesting.

Its verdict is

```text
STRICTLY_POSITIVE_EXACT_SERIALIZED_CONTRACTION.
```

This is a finite exclusion, not an RH proof.

## Zero-spectrum attribution

Using approximate `mpmath.zetazero` ordinates solely for discovery, the first
600 positive zeros and their negative conjugates were subtracted from the
binary64 Toeplitz matrix.

```text
pairs   reoptimized residual minimum
100     1.4040520291e-05
200     1.0250490189e-05
300     7.3563467701e-06
400     5.6911716974e-06
500     5.3793535436e-06
600     5.0628217378e-06
```

The five largest contributions to the original mode were approximately:

```text
zero index    ordinate             pair contribution
121           271.494055641645     2.9609433374e-06
60            163.030709687182     2.6023676805e-06
207           407.581460386896     1.3791694008e-06
105           244.070898497078     8.2574108604e-07
244           462.065367274883     7.8131107291e-07
```

Together they account for roughly `44.3%` of the raw frozen-mode value.  The
top twenty account for roughly `63.5%`.

These are not certified ordinates.  Their only role is to choose the first Arb
bins requested from the zero-deflation infrastructure.

## Cross-route handoff

Draft PR #90 / Issue #84 already contains:

- a certified extremely narrow first-zero bin;
- exact slab counts from `arb.zeta_nzeros`;
- generic scalar and matrix zero-deflation logic for Pick kernels.

The most valuable integration is not to deflate zero #1 from the screw matrix;
it contributes very little to the current mode.  Instead, request narrow Arb
bins for indices

```text
121, 60, 207, 105, 244
```

and apply the fixed-vector bound in L-9505 before building full matrix repairs.
This ordering is expected to produce most of the available deflation moat with
only five special-function certificates.

## Files added in this continuation

```text
claims/lemmas/L-9504-arithmetic-progression-fir-filter-cone.md
claims/lemmas/L-9505-screw-zero-bin-deflation-and-tail-box.md
claims/experiments/X-9502-screw-fir-toeplitz-and-directed-control.md
experiments/screw_fir_toeplitz_recon.py
experiments/screw_toeplitz_mpfr.c
experiments/verify_screw_toeplitz_certificate.py
experiments/results/X-9502-screw-toeplitz/README.md
experiments/results/X-9502-screw-toeplitz/recon.json
experiments/results/X-9502-screw-toeplitz/p128.json
experiments/results/X-9502-screw-toeplitz/p192.json
experiments/results/X-9502-screw-toeplitz/p256.json
experiments/results/X-9502-screw-toeplitz/verification.json
experiments/results/X-9502-screw-toeplitz/zero-attribution-600.json
experiments/results/X-9502-screw-toeplitz/SHA256SUMS
```

## Highest-priority review targets

1. The sign and factor conventions in `L-9504.4`, `L-9504.11`, and the
   resonance jump `L-9504.13`.
2. The claim that the increment parameterization is onto the full zero-sum
   arithmetic-progression cone.
3. The factor `2E` and complete-coverage hypotheses in the `L-9505` upper box.
4. The smooth-series lower tail in the C producer.
5. The exact threshold bucket `ceil(log_2(q^3))` and final cutoff identity.
6. The checker rule that producer and serialized contractions need overlap,
   not a fixed containment direction.
7. Rebuilding with official `mpfr.h` rather than the documented project-
   container ABI fallback.

## What has not been proved

- No Toeplitz matrix or FIR witness has been shown negative.
- No approximate zero used in attribution has been certified by this branch.
- No finite positive scan proves RH.
- No claim is made that the decreasing eigenvalues must eventually cross zero.
- No independent special-function implementation has reproduced the MPFR
  primitive rows.
- The Suzuki normalization remains pending independent repository review.

## Immediate continuation

1. Obtain rigorous bins for zero indices `121`, `60`, `207`, `105`, and `244`.
2. Apply the sharp fixed-vector lower subtraction from L-9505.
3. Form the repaired whole-matrix blocks and reoptimize the residual.
4. Freeze the new mode to dyadics and reuse the already directed 53-row `Psi`
   table.
5. If the residual remains positive, rank new exact `log(p)/d` resonances by
   L-9504.13 before evaluating any larger prime cutoff.
6. In parallel, derive a rigorous reciprocal-square zero-tail bound so that
   complete low-zero coverage eventually yields the two-sided excess-positive
   test in L-9505.15.
