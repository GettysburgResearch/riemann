# Independent exact primitive synthesis review: the Taylor8 inventory

Status: **ACCEPT for the bounded codimension8 branch of the frozen exact
primitive transform, source indexing, constants and both fresh runtime
replays.** Reviewer: arithmetic agent, independent of the operator producer.
Date: 2026-10-10 UTC. The scope remains complex native tests on every
0<L<=1, under the inherited source binding O1--O4. No second complete
continuum integration is performed here.

The general S1--S4 primitive formulas were already independently derived
in EXACT_PRIMITIVE_SYNTHESIS_CROSS_REVIEW.md. I reread the helper's removed=5
branch, the original basis/coefficient constructor, the quantitative
extractor and the separate Taylor weighted checker. The exact inventory
has108 rows and8 columns: rows0..4 are sin(n*pi*t), n=1..5; rows5..7
are exp(t/2), exp(-t/2), cosh(3t/2); rows8..107 are the complete100
high sines n=6..105. In the helper, n=row+1 on the low block and
n=6+row-8 on the high block. Thus the six soft coefficients and every
cosine1..105 represent precisely the same exact z_i. No coefficient,
projection correction or high sine is dropped. Every soft-soft and
soft-cosine product is enclosed, and cosine orthogonality pays the full
diagonal. The complex Hilbert-space synthesis trace bound uses the same
real exact tests and holds for arbitrary complex synthesis coefficients.

The frozen extractor first invokes the full Taylor weighted replay. The
separate weighted checker validates exact literal-slab coverage, endpoint
and quadrature budgets, the completed R receipt, frozen Taylor gamma
helper, trial/source hashes and coefficient identities, the full positive
inverse-weight tail, all finite cosine corrections and shifted LDL reserve.
It reconstructs the source moment receipt before any new synthesis is read.
Its continuum R enclosure is an explicitly imported independently reviewed
completed input. I do not claim to recompute that integral here.

The independently reconstructed python-flint0.9 weighted input is immutable
at SHA-256 cd2178a404167b9cf47aef2e64141d37f9fa01e35fce2a4b66df1c7f6fc9efc9.
I ran, from /workspace/riemann, both modes with that same input:

```bash
nice -n 19 /workspace/.riemann-tools/python/bin/python3 -B \
  research/exploratory/2026-10-10-four-hour-wave/operators/enclose_exact_primitive_synthesis.py \
  /tmp/review-native-taylor8-weighted-normal.json \
  research/exploratory/2026-10-10-four-hour-wave/operators/directed_residual_codim8_trial100_taylor.json \
  --out /tmp/exact-taylor8-independent-arithmetic.normal.json
# Repeat with -O and the optimized temporary output path.
```

Both exit0. Their JSON bytes agree at SHA-256
7d26a1f5992ce5d345deb62341bd1d914f45ab1e170949881c0e1f8a4198ee8e.
Frozen copies are results/exact-taylor8-synthesis-independent.normal.json
and .optimized.json. Every owner receipt field agrees exactly except
the expected baseline weighted-input hash for the independently rebuilt
backend input; the trace and every individual primitive norm are identical.

The complete trace ball is
[0.50573861248819862602169460372551125211009170493217 +/- 2.72e-17],
so K=1 is valid. This inventory retains M=1, epsilon=10^-11,
kappa=1/6 and theta=1/200000000001. Therefore the exact accepted scalar is

    delta=min(epsilon/6,theta/12)=1/2400000000012.

This is the codimension8 deduction from the general S1--S4 transform,
rather than the codimension14 numerical S5 constant. At L=1 it pays both
the projected E norm and the native primitive norm; native zero extension
retains q_L(h,h)>=delta||G_L h||_2^2 for every0<L<=1. The primitive is
injective. No native L2 gap, sign atL>1, global zero conclusion or RH follows.

| Frozen source | SHA-256 |
|---|---|
| enclose_exact_primitive_synthesis.py | 009ae7df8ef5acdea2be122602d8c239eb0a36ac56563bf76640469926b8a011 |
| enclose_primitive_norm.py | a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0 |
| enclose_weighted_lower_taylor.py | 0ba57657eef0ea728134e846c2861f778793715c5d091c3c47090cc87f003f25 |
| directed_residual_codim8_trial100_taylor.json | cba3fb5f17e71678b115c03813b97dda37ec45c19c24604bd302fd8baaf2ed19 |
| directed_exact_synthesis_codim8_trial100_taylor.json | 7aa239a063f4253eb3bfe94d04ad0d121d4525354e3013a95d922e35b5106d3e |
