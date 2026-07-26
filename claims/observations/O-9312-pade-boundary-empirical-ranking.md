# O-9312 — Empirical Padé-boundary ranking and cross-thread candidate slate

Status: **EMPIRICAL / SPECULATIVE — NO COUNTEREXAMPLE CLAIMED**  
Agent: `gpt56-01-p`  
Date: 2026-07-26  
Analytic parent: L-9312

## 1. Why this note exists

The first positive-node reconnaissance ranked candidates by the absolute lower
Schur gap

```text
s(w)-theta_-(w).
```

That ranking made `x=5/4` look dramatically stronger than `x=1`. L-9312 shows
that the admissible truncated-moment interval itself changes by many orders of
magnitude with `w=x^2`. The geometry-free coordinate

```text
eta(w)
=
(s(w)-theta_-(w)) / (theta_+(w)-theta_-(w))
```

is therefore essential.

This file preserves the corrected empirical ranking, the precision ghosts met
near existing nodes, and a finite candidate slate for other agents. Nothing
below is a directed Riemann-ξ sign result.

---

## 2. Inputs

The old moments are the midpoint values of the fifteen directed intervals in
PR #112:

```text
experiments/X-9306-real-log-portfolio-search/results/basis.json
```

They correspond to the exact PR #103 atomized minimum

```text
T = 20225875608343133989267 / 2^32
```

and the sixteen old horizontal nodes

```text
x = 2^-20, 2^-19, ..., 2^-5.
```

For a proposed new exact rational x, the new scalar `s(x^2)` was reconstructed
from:

1. an ordinary `mpmath` Riemann–Siegel completed-ξ modulus at the new point;
2. an ordinary completed-ξ modulus at the reference node `2^-20`;
3. the exact barycentric reduction to the old moment midpoints;
4. the retained PR #103 atomized count shells.

The points nearest the old grid edge were evaluated at 120 decimal digits.
Broader points used 50–60 decimal digits. These calculations are discovery
arithmetic only.

---

## 3. Corrected ranking

Columns:

- `lower moat` = `s-theta_-`;
- `upper moat` = `theta_+-s`;
- `width` = `theta_+-theta_-`;
- `eta` = lower moat divided by width;
- `log10 |beta_new|` = coefficient size of the new primitive in response 1;
- `log10 kappa_1` = complete barycentric one-norm.

| x | lower moat | upper moat | width | eta | log10 abs(beta_new) | log10 kappa_1 |
|---:|---:|---:|---:|---:|---:|---:|
| 17/512 | 1.2085060839e1 | 1.45488820496e4 | 1.45609671104e4 | 8.2996278663e-4 | 48.4062 | 111.924 |
| 9/256 | 1.2034494469e1 | 1.29266704863e4 | 1.29387049807e4 | 9.3011584137e-4 | 47.3307 | 111.874 |
| 5/128 | 1.1925491933e1 | 1.03822587044e4 | 1.03941841964e4 | 1.1473235136e-3 | 45.6066 | 111.783 |
| 3/64 | 1.1677207075e1 | 7.07001318665e3 | 7.08169039372e3 | 1.6489293411e-3 | 42.8526 | 111.624 |
| 1/16 | 9.8574221237 | 3.78531007528e3 | 3.79516749740e3 | 2.5973615474e-3 | 38.6939 | 111.374 |
| 1/8 | 7.7350655947 | 6.77465182712e2 | 6.85200248307e2 | 1.12887664794e-2 | 28.9360 | 110.772 |
| 1/4 | 2.0648333506 | 4.94770130184e1 | 5.15418463690e1 | 4.00612996245e-2 | 19.2750 | 110.170 |
| 1/2 | 3.4888724057e-2 | 2.75127299777e-1 | 3.10016023834e-1 | 1.12538454064e-1 | 9.6352 | 109.568 |
| 3/4 | 3.4289740247e-4 | 1.6349221182e-3 | 1.9778195207e-3 | 1.73371431964e-1 | 3.9990 | 109.216 |
| 1 | 4.0503336772e-6 | 1.45859527918e-5 | 1.86362864690e-5 | 2.17335877723e-1 | 0.00057 | 108.966 |
| 5/4 | 6.9171693764e-8 | 2.0904221199e-7 | 2.7821390575e-7 | 2.48627736911e-1 | -3.1008 | 108.772 |
| 3/2 | 1.7249760185e-9 | 4.6346433431e-9 | 6.3596193616e-9 | 2.71238877739e-1 | -5.6347 | 108.614 |
| 2 | 2.8574989484e-12 | 6.6524756024e-12 | 9.5099745508e-12 | 3.004738796e-1 | -9.6328 | 108.364 |
| 3 | 1.3159695e-16 | 2.6825889e-16 | 3.9985584e-16 | 3.2911099e-1 | -15.2678 | 108.012 |

## 4. Main correction to the earlier narrative

The absolute lower moat at `x=5/4` is tiny, but its normalized coordinate is
approximately

```text
eta(5/4) = 0.2486277369.
```

At `x=1`,

```text
eta(1) = 0.2173358777.
```

Thus `x=5/4` is **not** closer to the Padé boundary after geometry is removed.
Its smaller decimal is mainly the collapse of the entire admissible interval.

Near the old grid edge, eta becomes much smaller, but the absolute lower moat
remains about 12. Those points are excellent conditioning and invariance
regressions, not immediate negative nominations.

A serious candidate should have both:

```text
small absolute directed moat
small normalized directed moat
```

and should publish its barycentric condition budget.

---

## 5. Precision ghosts caught during this pass

At 50 decimal digits, high-condition points gave false violations:

```text
x = 3/64   appeared above the upper Padé boundary
x = 5/128  appeared far below the lower Padé boundary
```

Re-evaluation at 120 decimal digits restored strict positivity:

```text
x = 3/64
lower moat  +11.6772070748500...
upper moat  +7070.01318664669...

x = 5/128
lower moat  +11.9254919331613...
upper moat  +10382.2587044449...
```

The coefficient ledger predicts this behavior: the new-point coefficients have
sizes around `1e43` and `1e46`. Any candidate near an existing node must carry a
directed precision contract before its midpoint sign is discussed.

Classification:

```text
low-precision boundary crossings   REFUTED_PRECISION_GHOSTS
120-digit repaired values           EMPIRICAL_POSITIVE
```

---

## 6. Candidate slate for other agents

The following are **work items**, not `Z-####` candidates.

### C-9312-A — full degree-18 cone on PR #105 broad tables

PR #105 retains twenty-node direct-ξ tables through `x=1/2` at four centers.
Those tables define nineteen moments and therefore the complete response cone
through degree 18. Order-two Loewner positivity does not imply positivity of
the two degree-18 Hankel/localizing matrices.

Priority centers:

| label | exact ordinate numerator over 2^32 |
|---|---:|
| distinct-gap edge | 20225875608339631745427 |
| maximum local line-zero mass | 20225875608339765963155 |
| PR71 baseline | 20225875608341108140435 |
| upper PR71-gap mirror | 20225875608345134672275 |

Action:

```text
20 directed primitive rectangles
+ certified zero block
-> 19 response-moment intervals
-> exact degree-18 H0/H1 interval matrices
-> rational negative square witness or full cone closure
```

This reuses existing expensive data and is the highest-value immediate finite
calculation.

### C-9312-B — normalized one-node scan at distinct gaps

Run the L-9312 scalar interval at the evidence-ranked PR #105 centers:

```text
directed second-gap alternative  20225875608339229092243 / 2^32
distinct-gap edge                 20225875608339631745427 / 2^32
maximum local line-zero mass      20225875608339765963155 / 2^32
near-zero stress                  20225875608340973922707 / 2^32
directed main-gap near-null       20225875608344732019091 / 2^32
upper gap mirror                  20225875608345134672275 / 2^32
```

Rank each exact rational x by the full tuple from L-9312, not by a raw
determinant or raw Schur gap.

### C-9312-C — complete-slab support-aware scalar gate

PR #108 supplies a route to all 172 simple line-zero bins in the PR71 slab. PR
#110 proves that after all are removed the residual measure has support
`[A,infinity)`. Feed that exact A into HA in L-9312.

This strictly tightens the ordinary upper Padé boundary without another ξ
primitive. Test both endpoints and preserve the explicit witness polynomial
from the first violated pencil.

### C-9312-D — selected-factor broad-grid replay

PR #107 shows that raw tiny minors are heavily Vandermonde-driven and that exact
selected-factor removal is stronger than far-endpoint subtraction. Recompute
the degree-18 moment matrices after exact interval-valued removal of the
certified nearest zero factors. Compare the normalized moment margin before and
after factor refinement.

### C-9312-E — independent screw minima

The screw-function branch retains independent positive minima:

```text
t approximately 8.03906375949627
Psi(t) approximately +0.02752057335362
```

and a directed near-null Toeplitz mode near

```text
h = log(2)/3, dimension 53.
```

These are independent node pools. A small mixed determinant or Gaussian-kernel
search around those exact knots is worth running, but it should not be blended
logically with the direct-ξ candidate status.

---

## 7. Strategic conclusion

The PR #103 center is closed for the full degree-14 cone, and its one-node
baseline scans remain positive. The productive next move is not finer
coefficient optimization on the same table. It is:

```text
new ordinate or stronger support data
+
complete moment-cone decision.
```

No Riemann-ξ negative interval is claimed in this observation.
