# O-32701 — The actual critical half-binary/half-ternary producer develops negative rows at large finite endpoints

Claim ID: `O-32701`  
Status: **HIGH-PRECISION / COMPENSATED FLOATING RECONNAISSANCE — NOT AN EXACT REFUTATION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Scope: the frozen half-binary/half-ternary producer used by the first-entrance/GFEP programme; no RH conclusion

## 1. Target and producer

The tested source is the actual critical target

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

Its exact multiple-Möbius divergence is formed first and then propagated by the frozen equal-weight binary/ternary descending recurrence. This is the source-specific producer itself, not an Abel-prefix surrogate.

## 2. Discovery

Compensated binary64 reconstruction gives the following minimum coefficients.

| `X` | number of negative producer rows | minimum coefficient | representative minimizing row |
|---:|---:|---:|---:|
| 20,000,000 | 0 | nonnegative at displayed precision | — |
| 25,000,000 | 1 | about `-5.98133e-4` | `107` |
| 30,000,000 | 4 | about `-4.16259e-3` | `43` |
| 40,000,000 | 11 | about `-1.16595e-2` | `29` |
| 50,000,000 | 21 | about `-1.93381e-2` | `36` |
| 60,000,000 | 28 | about `-2.12210e-2` | `43` |
| 80,000,000 | 40 | about `-4.17806e-2` | `29` |
| 100,000,000 | 53 | about `-5.68090e-2` | `24` |

The computation was independently repeated with Kahan-compensated accumulation in both the multiple-Möbius source and descending renewal; the displayed negative values were stable far beyond the last shown decimal places relevant to the sign.

This is strong reconnaissance, but it is **not** promoted to an exact counterexample because the complete computation includes floating evaluations of square roots and logarithms over a very large source manifest and has not yet been converted into a directed interval proof object.

## 3. Negative debt remains small

The capacity-weighted negative debt of the same producer remains tiny compared with the endpoint scale. Representative floating values were approximately

```text
X=25,000,000     0.0062
X=30,000,000     0.0448
X=40,000,000     0.264
X=50,000,000     0.404
X=60,000,000     0.804
X=80,000,000     1.45
X=100,000,000    2.27
```

Thus the experiment points in opposite directions for two formerly conflated targets:

```text
pointwise producer positivity       likely false;
subpower weighted negative debt     still plausible.
```

## 4. Consequence for review strategy

GFEP implies pointwise positivity of this producer. Therefore a proof of GFEP should not be prioritized until the large-scale sign mutation has either been reproduced by a directed proof object or explained by a numerical failure.

The weaker BTF/Cycle-Debt route is not contradicted; indeed the observed debt is much smaller than the pointwise defect suggests.

## 5. Required next assurance step

A proof-grade refutation should freeze one endpoint with a comfortable negative moat (for example a large endpoint from the table), emit the exact linear source kernel for the selected row, and evaluate the square-root/log target by directed rational or MPFR intervals. Until that artifact exists, this file remains discovery-only.
