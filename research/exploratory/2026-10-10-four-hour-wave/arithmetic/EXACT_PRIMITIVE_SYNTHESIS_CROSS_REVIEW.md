# Independent exact primitive synthesis review

Status: **ACCEPT for S1--S5, the source transform and both fresh runtime replays.**
Reviewer: arithmetic agent, independent of the operator producer.
Review date:2026-10-10 UTC. The native conclusion remains0<L<=1.

I read the full new proof and checker, the primitive extractor, weighted
replay helper, original basis/coefficient constructor, and quantitative
completion proof. These load-bearing files are frozen at:

| Source | SHA-256 |
|---|---|
| `EXACT_PRIMITIVE_SYNTHESIS.md` | `1e1cd511a477cf5120b0b7ca0a9ebb36ce5b115d8c3faa063e76b6870733aac9` |
| `enclose_exact_primitive_synthesis.py` | `009ae7df8ef5acdea2be122602d8c239eb0a36ac56563bf76640469926b8a011` |
| `enclose_primitive_norm.py` | `a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0` |
| `enclose_analytic_upper.py` | `b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b` |
| `directed_residual_codim14_trial100.json` | `9213accb90caa99e17172f620c3946ab638542eaf0523dfba89ab8f870d2016a` |
| `directed_exact_synthesis_codim14_trial100.json` | `df598c783ec412941cfd13f3c07cb3054ae3ad32a613320318a5915ffcbe3551` |

All four closed G formulas were independently reconstructed by convolution
or Laplace partial fractions. The six soft coefficient transformations
match the source inventory: low sines1..11, exp(+t/2), exp(-t/2),
cosh(3t/2), and all high sines12..111. The projection/energy corrections
are already folded into the complete source coefficient rows; none is
dropped. The same exact real z_i are used. Pointwise Cauchy--Schwarz and
integration give the stated synthesis trace bound for arbitrary complex
coefficients. No real-only native test restriction is introduced.

The removable F/F-prime/F-double-prime formulas and exact zero rates are
correct. Every soft-soft product uses the sum rate and sum polynomial
power; every mixed cosine term is paid with factor2; exact positive
frequency cosine orthogonality gives diagonal1/2. Directed coefficient
balls preserve cancellation without midpoint substitution.

The checker invokes the frozen primitive extractor first. That extractor
freshly reconstructs the entire weighted receipt, checks semantic equality,
all source/trial/helper hashes, full continuum coverage and weighted
reserve, before the new synthesis reads the authenticated coefficients.
This is a complete fresh matrix/source replay. The complete continuum R
integral remains an accepted previously produced input; it is not repeated.

My initial optimized attempt supplied the owner python-flint0.8 receipt
to the0.9 backend and exited1 at the strict full-fresh semantic guard.
The guard was preserved. Corrected normal and optimized runs used the
independently rebuilt0.9 weighted input, SHA-256
`eab5e0bd7f683de7c185e3795be5f2e039a0d7f0f08a38a15a7249995322e4ce`.

The successful commands, from `/workspace/riemann`, were:

```bash
nice -n 19 /workspace/.riemann-tools/python/bin/python3 -B \
  research/exploratory/2026-10-10-four-hour-wave/operators/enclose_exact_primitive_synthesis.py \
  /tmp/review-native-weighted-normal.json \
  research/exploratory/2026-10-10-four-hour-wave/operators/directed_residual_codim14_trial100.json \
  --out /tmp/exact-primitive-synthesis-independent-arithmetic.normal.json
# Repeat with -O and the optimized temporary output path.
```

Both exit0. Their JSON bytes are identical at SHA-256
`1e6eb716fc49da8860b69950304a52b7c86cea3521f906d2149ef56e045c851e`. Permanent copies are in
`results/exact-primitive-synthesis-independent.normal.json` and `.optimized.json`.
Every owner output field agrees exactly except the expected baseline
weighted-receipt hash for the independently rebuilt backend input. The
complete trace ball and every individual norm ball agree exactly.

The synthesis trace is
`[0.51327163928409972066385135858719195985933514973386 +/- 1.00e-15]`,
so K=1 is valid. With epsilon10^-11,M1,kappa6/5 and the stated theta,
delta=min(epsilon/6,theta*kappa/2)=1/600000000000 exactly.
The same native zero extension retains the full primitive bound at every
0<L<=1, and atL1 it also pays the projected E norm. No native L2 gap,
sign atL>1, source adapter beyond the reviewed binding, or RH result
is inferred. The complete unknown source tail is retained in the baseline
weighted replay; the finite primitive synthesis does not replace it.
