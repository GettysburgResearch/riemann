# X-4101 — Exact synthetic controls for xi differential/Stieltjes witnesses

Status: exact finite-zero-model regression only. This experiment does **not**
evaluate the Riemann xi function and cannot produce an RH counterexample.

## Purpose

This experiment tests the algebraic kernels of `L-4101` and `L-4102` before an
Arb producer exists.

For a finite synthetic zero multiset `Z`, define

\[
 F_Z(s)=\sum_{\rho\in Z}\frac1{s-\rho}.
\]

All zero coordinates and evaluation points are rational. The implementation
uses exact Gaussian-rational arithmetic based on `fractions.Fraction`.

It checks two proposed RH witness mechanisms:

1. the one-point differential localizer

   \[
   \mathcal D(s)=\operatorname{Re}F'(s)
   +\frac{1}{x}\operatorname{Re}F(s),
   \qquad s=1/2+x+iT;
   \]

2. the shifted-Stieltjes moments

   \[
   m_n=\frac{(-1)^n}{n!}\frac{d^n}{du^n}
   \left[\frac1{\sqrt u}
   \operatorname{Re}F(1/2+\sqrt u+iT)\right],
   \qquad u=x^2,
   \]

   and their Hankel/localizing matrices.

## Files

- `synthetic.py` — exact finite-zero jet, moment conversion, matrices, fixed
  quadratic forms, and synthetic certificate checker;
- `certificates/synthetic-offline-quartet.json` — exact right-side witness
  control;
- `tests/test_synthetic.py` — exact sign, moment, matrix, and mutation tests;
- `results/tests.txt` — recorded independent exact reconstruction checks.

## Right-side off-line quartet control

The committed zero multiset is

\[
 \left\{\frac12\pm\frac1{10}\pm20i\right\}.
\]

At

\[
 s=\frac12+\frac{11}{100}+20i=0.61+20i,
\]

the exact finite model gives

\[
 \operatorname{Re}F_Z(s)
 =\frac{563216297601940400}{5376148512009261}
 \approx104.7620422583>0,
\]

while

\[
 \mathcal D_Z(s)
 =-\frac{262158411401971496699725715848000000}
 {28902972823179391166739349766121}
 \approx-9070.2922846652<0.
\]

The one-by-one localizer is exactly

\[
 (B_0)_{00}=\frac12\mathcal D_Z(s)<0.
\]

This control demonstrates the geometric distinction from the scalar
`Re F<0` criterion: the evaluation lies to the **right** of the off-line pole,
so the scalar real part is strongly positive while the differential localizer
is strongly negative.

These numbers are properties of the finite synthetic model only.

## Exact moment conversion

For a finite jet `A_k=Re F_Z^(k)(s)`, the implementation reconstructs

\[
 m_n=
 \sum_{k=0}^{n}
 (-1)^k
 \frac{(2n-k)!}
 {2^{2n-k}n!k!(n-k)!}
 \frac{A_k}{x^{2n-k+1}}.
\]

For synthetic critical-line zeros it independently computes

\[
 m_n=\sum_\gamma
 \frac1{(x^2+(T-\gamma)^2)^{n+1}}
\]

and requires exact equality.

For a vector `c`, it also compares the matrix quadratic forms with the direct
positive sums

\[
 c^{\mathsf T}A_Nc
 =\sum_\gamma a_\gamma
 \left(\sum_jc_ja_\gamma^j\right)^2
\]

and

\[
 c^{\mathsf T}B_Nc
 =\sum_\gamma (T-\gamma)^2a_\gamma^2
 \left(\sum_jc_ja_\gamma^j\right)^2.
\]

No numerical eigenvalue enters these checks.

## Commands

From this directory:

```bash
python synthetic.py certificates/synthetic-offline-quartet.json
python -m unittest discover -s tests -v
python -m compileall -q synthetic.py tests
```

Expected certificate status:

```text
SYNTHETIC_RIGHT_SIDE_DIFFERENTIAL_NEGATIVE
```

## Validation performed in this session

An independent exact reconstruction of the committed formulas checked:

1. positive `Re F_Z` and negative `D_Z` for the off-line quartet;
2. exact `B00=D/2`;
3. equality of direct and finite-jet moments through order seven;
4. equality of order-three Hankel quadratic forms with direct positive sums;
5. equality of order-three localizing quadratic forms with direct positive
   sums;
6. the essential localizer orientation;
7. strengthening negative divergence as the evaluation approaches the pole from
   the right;
8. exact agreement with all rational endpoints stored in the JSON control.

All checks succeeded using exact `Fraction` arithmetic. The committed unittest
file packages the same regressions for independent rerun.

## Proof boundary

The following are **not** supplied here:

- an `xi`, `zeta`, gamma, or polygamma evaluation;
- ball arithmetic;
- a high-height scan;
- a genuine negative xi-jet certificate;
- a `Z-####` candidate.

Issue #39 remains responsible for an Arb producer and independent checker. Any
real candidate must use exact dyadic points, prove the `xi` denominator excludes
zero, enclose the required logarithmic-derivative jet, freeze a dyadic vector,
and leave the final quadratic interval strictly below zero.

## Suggested Arb progression

1. Reproduce the synthetic controls with complex balls.
2. Calibrate `D>=0` and the moment matrices on known critical-line zeros.
3. Evaluate scalar and differential signs together at paired horizontal offsets.
4. Add `2 x 2` and `3 x 3` localizers only after the one-point jet is stable.
5. Use fitted Stieltjes or Padé models only to nominate exact points and vectors;
   reevaluate every proof value directly.