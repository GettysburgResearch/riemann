# Arithmetic checks on an amplified endpoint comparison

Status: exploratory exact-arithmetic checks. No new zero-free theorem is claimed.

Scope and sources: Yuanda Xu and Hejian Sang, [*Amplified moments and a refinement of the quasi-Riemann hypothesis*, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), equations (10), (21), (28) and the numerical conditions in Section 6. The PDF inspected had SHA-256 `e881519b3d2447ae2afee43650fac5e65a47e73fd52c236e1122823a7b64885f`. We did not check its analytic results or their imported inputs. Baiying Liu, [*Zero-free half-planes for Hecke L-functions over number fields*](https://arxiv.org/abs/2610.26835), reports the stronger boundary `0.874886647039964...` as the infimum of the refined comparison system. Neither paper is independently reviewed here.

## A candidate in the stated admissible range

The first script checks the following rational values against the numerical conditions of Xu–Sang Section 6:

```
b = 17307/200000
ell = 4178001/25000000
kappa = 29991/40000
g = 1/10^9, zeta = 1/10^12, g_star = 1/10^11.
```

The implied boundary is `262465997/300000000 = 0.874886656666...`. The continuous endpoint inequality is checked without sampling: with `y=1/2-x`, `Q=J*(-E-g)` is quadratic in delta, with leading coefficient `A(y)>0` and discriminant expression `4*A(y)*C(y)-B(y)^2>0` for `y>=0`, because every exact rational coefficient in each polynomial is strictly positive. The script checks these coefficients and the remaining scalar inequalities. Substituting this candidate in the cited propositions, subject to all their assumptions and proof correctness, yields a marginally stronger boundary than the `0.8748867` stated in Xu–Sang. It is **weaker than** the boundary stated by Liu and therefore is not a record or a significant improvement. The preceding Xu–Sang stage licenses this same kappa; this calculation does not independently prove that stage.

## One exact obstruction at a more ambitious boundary

At candidate boundary `0.87488664`, define `ell=4*(11/12-B)=1566751/9375000` and use the optimistically licensed `kappa=2*B-1=4686083/6250000`. The second script checks the formal expression (28) at `x=1/2` and two values `delta=46934/100000,46935/100000`. The two expressions have opposite slopes in `b`. Positive rational weights summing to one cancel `b`; their weighted sum is exactly

```
12816494833840121269482852422749 /
419266225701571864005751712694665625000 > 0.
```

Thus at least one of these two endpoint expressions is positive for every real `b`, so the strict negative endpoint screen fails at this particular parameter point. The chosen kappa lies slightly **below** the numerical range specified by Xu–Sang Section 6: this is an algebraic diagnostic for a hypothetical extension of their screen, not an application of their proposition at that kappa. It does not rule out another geometry, a different row bound, or a different proof, and it does not establish failure for any other boundary.

Numerically solving the stationarity equations with `kappa=2*B-1` produces `B=0.874886647039964...`, consistent with Liu's reported value. This numerical observation is not a proof of the global optimum and carries no novelty claim.

## Reproduction

With Python 3 and SymPy 1.14.0, run from the repository root:

```
python research/exploratory/2026-10-28-amplified-endpoint/check_admissible_candidate.py
python research/exploratory/2026-10-28-amplified-endpoint/check_fixed_point_obstruction.py
```

Both scripts use exact rationals for their assertions; printed floating approximations are explanatory. Successful arithmetic does not verify the cited moments, contour moves, analytic continuation, family transfer, or any new L-function zero-free result.
