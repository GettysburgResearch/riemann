# X-9502 — Screw FIR/Toeplitz reconnaissance and directed control

Claim ID: X-9502  
Title: Prime-resonant FIR filters, a 53-dimensional screw Toeplitz mode, and directed positive replay  
Status: EMPIRICAL  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: D-9501, L-9503, L-9504; L-9505 for the proposed next-stage deflation  
Scope: finite arithmetic-progression zeta-screw search  
Related counterexample candidates: none

## Statement

A new arithmetic-progression search over the zeta screw function produced a
small positive `L-9504` increment-Toeplitz mode.  The mode was frozen to exact
24-bit dyadic coordinates and replayed with directed MPFR arithmetic at 128,
192, and 256 bits.

The final result is strictly positive.  It therefore excludes this exact
finite mode and is **not** a counterexample to RH.

The exact directed case is

```text
h                         = log(2)/3
matrix size               = 53
maximum sampled argument  = 53 log(2)/3
prime-power cutoff        = 208063
threshold at row k        = q^3 <= 2^k
prime count               = 18640
prime-power count         = 18778
vector denominator        = 2^24
manifest SHA-256          = 18224939cfbd3d221695e8883e7eabf2d4201697ef6b154c0260b1b9e7cff0d2
```

The 256-bit producer enclosure is

\[
\begin{aligned}
 b^*H^{(53)}(\log2/3)b\in[
 &1.928553622308640188310963997625878557364125578418042806481204260290997513959522403925111843
 \times10^{-5},\\
 &1.928553622308640188310963997625878557364125578418042806481204260291025054537139777586645641
 \times10^{-5}].
\end{aligned}
\tag{X-9502.1}
\]

An independent standard-library checker reconstructed the zero-sum FIR vector,
all integer autocorrelations, the complete manifest digest, and the Rayleigh
contraction from serialized primitive intervals.  Its exact rational lower
endpoint was also strictly positive.

## Route discovered

### Binomial FIR filters

The first search specialized `L-9504` to

\[
 P(z)=(1-z)^m.
\]

At the exact resonance `h=log(2)/2`, the normalized binary64 value decreased
steadily with order, reaching approximately

\[
 \mathcal B_{59}(\log2/2)=0.006175701225849269.
\]

The one-sided derivative jump from `L-9504.16` was approximately

\[
 7.217872195781672
\]

at order `59`; the separately computed one-sided slopes had opposite signs.
This identified exact prime-power resonances as search locations but did not
produce a negative nomination.

These values are reconnaissance observations.  They were not used in the
directed certificate (X-9502.1).

### Full increment-Toeplitz cone

Optimizing the whole `L-9504.5` matrix, rather than one binomial vector,
reduced the binary64 margins by orders of magnitude.  A broad scan showed two
persistent basins near

```text
h = log(2)/2
h = log(2)/3.
```

The exact `log(2)/3` resonance was selected because every prime inclusion can
be decided by integers and its complete proof replay needs only `18,778`
prime-power rows.

The binary64 eigensolver gave

```text
minimum eigenvalue       1.9285536855e-05
frozen-vector Rayleigh   1.9285536220e-05
frozen-vector norm^2     0.9999999669
```

The 53 exact vector numerators are committed in every directed certificate and
are reconstructed independently by the checker.

## Directed producer

The producer

```text
experiments/screw_toeplitz_mpfr.c
```

performs the following steps.

1. It checks exactly that
   \[
   208063^3\le2^{53}<208064^3.
   \]
2. It enumerates every prime and prime power through `208063`.
3. It assigns a prime power `q` to the first sampled row satisfying
   `q^3<=2^k`, without a floating comparison.
4. It evaluates `log(p)`, `sqrt(q)`, the elementary smooth series, its explicit
   positive tail, and every prefix sum with outward MPFR rounding.
5. It reconstructs the difference vector `c=(1-z)b` and its autocorrelations
   from the frozen integers at runtime.
6. It contracts
   \[
   -2\sum_{k=1}^{53}\rho_k(c)\Psi(kh)
   \]
   with coefficient-aware directed endpoints.

The observed local runtimes were machine-dependent but small:

```text
128 bits: 0.16 s, about 5.2 MB RSS
192 bits: 0.20 s, about 5.3 MB RSS
256 bits: 0.25 s, about 5.4 MB RSS
```

## Independent checker

The standard-library checker

```text
experiments/verify_screw_toeplitz_certificate.py
```

uses no NumPy, MPFR, FLINT, or special-function library.  It:

1. reconstructs the exact zero-sum difference vector;
2. recomputes every lag autocorrelation with Python integers;
3. contracts all outward decimal `Psi` intervals with exact `Fraction`
   arithmetic;
4. independently sieves the manifest and recomputes its canonical SHA-256;
5. requires overlap between the producer and serialized-primitives
   enclosures;
6. requires strict positivity and nesting at every precision;
7. checks the symbolic cutoff identity from `h=log(2)/3`.

The verification artifact records

```text
status   PASS
verdict  STRICTLY_POSITIVE_EXACT_SERIALIZED_CONTRACTION
scope    excludes only the committed exact finite vector
```

The producer and serialized contractions need not contain each other in a
fixed direction.  MPFR accumulation rounding can widen the producer result,
while outward decimal serialization can widen the exact primitive-row
contraction.  The checker correctly requires overlap, positivity, and separate
cross-precision nesting.

## Approximate zero-spectrum attribution

To determine whether zero deflation could materially strengthen the route, the
same binary64 Toeplitz matrix was decomposed heuristically using the first 600
positive `mpmath.zetazero` ordinates and their negative conjugates.

This is not a certified zero computation.  It is search guidance only.

The reoptimized residual minima were

```text
positive zero pairs removed    residual minimum eigenvalue
100                            1.4040520291e-05
200                            1.0250490189e-05
300                            7.3563467701e-06
400                            5.6911716974e-06
500                            5.3793535436e-06
600                            5.0628217378e-06
```

For the original raw eigenvector, the most influential pair among those 600
was positive zero #121, near ordinate

```text
271.494055641645
```

with contribution approximately

```text
2.9609433374e-06
```

or `15.35%` of the raw Rayleigh value.  The five largest pair contributions
accounted for approximately `44.3%`, and the twenty largest accounted for
approximately `63.5%`.  This supports adaptive bin certification rather than
certifying zero ordinates merely in increasing order.

## Reproduction artifacts

```text
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

## Verification performed

1. The reconnaissance script independently reproduced the manifest counts and
   hash used by the C producer.
2. The binary64 script and directed C producer froze the same 24-bit vector.
3. All `Psi(kh)` rows nested from 128 to 192 to 256 bits.
4. Both producer Rayleigh intervals and exact serialized contractions nested
   across the three precisions.
5. The standard-library checker independently regenerated all `18,778`
   prime-power rows and the exact manifest digest.
6. The exact integer filter digest was identical at all precisions.
7. The 256-bit directed lower endpoint was strictly positive by a very large
   enclosure-width margin.
8. JSON parsing and SHA-256 checks passed for every preserved artifact.

## Analytic domain audit

All `Psi` arguments are positive real multiples of `log(2)`.  Prime threshold
comparisons are exact integer inequalities.  Every logarithm has a positive
integer argument; every square root is the positive real root.  The smooth
series is used only at positive arguments and has an explicit positive
geometric tail.  No complex logarithm, contour, or division by `xi` occurs.

The interpretation of a negative Toeplitz Rayleigh value as an RH
counterexample still depends on the independently reviewed `D-9501` Suzuki
normalization and `L-9504` FIR theorem.

## Dependency audit

- `D-9501` fixes the explicit `Psi` normalization.
- `L-9503` supplies the elementary smooth series and prime-prefix formula.
- `L-9504` proves the RH-valid FIR/Toeplitz cone and exact contraction.
- `L-9505` is not used to certify (X-9502.1); it formalizes the next zero-bin
  deflation stage.
- The approximate zero-attribution result is not a dependency of any directed
  statement.

## Gap audit

- The result is positive and excludes one vector only.
- Positive finite Toeplitz matrices do not prove RH.
- Small minimum eigenvalues may be ordinary FIR suppression of a discrete
  positive spectrum rather than evidence of an off-line zero.
- The C producer and Python exact checker are independent only after the
  primitive `Psi` rows.  A future negative result requires a second directed
  special-function implementation.
- The MPFR-header fallback is documented for the project container but should
  not replace the official `mpfr.h` in a production review build.
- Approximate mpmath zeros are not certified bins and were never subtracted in
  the directed artifact.
- Deflation must include the `L-9505` bin-width repair.  Subtracting midpoint
  rank-one blocks directly would be unsound.
- The current vector was optimized before zero deflation.  The residual cone
  must be reoptimized after each certified subtraction stage.
- The large-order binomial observations were binary64 reconnaissance and are
  not promoted to directed finite exclusions.

## Adversarial tests

1. Change the symbolic denominator from `3` to `2` without changing the cutoff
   and require the checker to reject the exact cutoff identity.
2. Delete the prime power `2^17` and require the manifest digest and primitive
   rows to change.
3. Reverse one directed `Psi` endpoint and require immediate rejection.
4. Mutate one frozen numerator and require the filter digest and exact
   contraction to change.
5. Contract the matrix by direct dense multiplication and by FIR
   autocorrelations and compare at high precision.
6. Rebuild with official MPFR headers and compare every serialized interval.
7. Recompute the zero-attribution ranking with an independent zero table; do
   not require identical ordering for nearly tied small contributions.
8. Certify bins around zero indices `121`, `60`, `207`, `105`, and `244`
   before spending effort on a long consecutive prefix.

## Remaining uncertainty

No negative nomination has been found.  The principal research uncertainty is
whether critical-line-zero deflation exposes a genuinely negative residual or
merely drives a positive singular-spectrum Toeplitz mode closer to zero.  The
principal certification uncertainty is the cost of obtaining narrow,
independently reproduced bins around the most influential nonconsecutive zero
indices.

## Suggested next attack

Use `L-9505.10` to obtain sharp fixed-vector lower subtractions for certified
bins around zero indices `121`, `60`, `207`, `105`, and `244`; then form the
full repaired matrix blocks, reoptimize the deflated Toeplitz cone, freeze the
new mode, and replay the same 53 primitive `Psi` intervals.  Only after the
residual optimization should the search enlarge `n`, vary the resonance, or
certify hundreds of additional zeros.
