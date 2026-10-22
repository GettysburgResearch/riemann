# Phase-real continuation 108260

## Status

Claims: `PFR-T5`, `PFR-T6`, `PFR-R2`; refined targets `PFR-C1--C3`.

Status: **AUTHOR-PROVED EXACT THEOREMS / REVIEW PENDING / EXTERNAL NOVELTY UNESTABLISHED**

This continuation advances both original lanes.

- [`FLOWER_CURVATURE_108260.md`](FLOWER_CURVATURE_108260.md) proves the exact self-intersection, turning, and normalized curvature-defect ledger for Hardy petals.
- [`XI_GAMMA_RESOLVENT_108260.md`](XI_GAMMA_RESOLVENT_108260.md) constructs a prime-defined actual-Xi real response whose weighted-energy abscissa and pointwise exponential type are exactly the supremal off-critical zero displacement. Its Laplace transform is a safe Taylor remainder of `xi'/xi`.
- [`LOCALIZATION_FIREWALL_108260.md`](LOCALIZATION_FIREWALL_108260.md) proves that no zero-independent holomorphic mode multiplier can create an exact hard ordinate window.

No zero is newly located, no zero proportion is improved, and RH/GRH remain unproved.

---

## Relationship to the existing project frontiers

### PR #762

PR #762 gives a different source-faithful beta harmonic whose squared growth
exponent is `2 Theta-1`.  `PFR-T5` gives the unsquared exponent

\[
B_\xi=\Theta-\frac12
\]

for a real explicit-formula resolvent.  This is a parallel observable, not an
improvement claim.

### Issue #39

Issue #39 studies pointwise passivity and Pick matrices for `Re xi'/xi` in a
safe half-plane.  PFR-T5 instead applies a Fourier de-Poissonization followed
by a future Gamma resolvent and reads the zero abscissa from real-time growth.

### PR #729 / Programme #744

PR #729 identifies backward-Poisson amplification in derivative-ratio
Herglotz fields.  Here the raw logarithmic phase field is de-Poissonized and
then regularized by a one-sided Gamma resolvent.  The two operators are related
but act on different source objects and have different consumers.

### Programme #763

PFR-T5 is a concrete example of a real transducer in the Riemann Structures
search: a harmless safe phase field is transformed into a real signal whose
stability exponent is exactly the hidden zero displacement.

---

## Computation

The bounded replay verifies:

- the universal open and closed turning formulas;
- the `2 pi` simplicity threshold and forced full-turn lag classes;
- the curvature-defect count algebra;
- the real Hardy convexity coordinate change;
- the finite resolvent Cauchy energy;
- four floating-reconnaissance actual-Xi source/zero regressions at
  `a=2`, `m=3`, `t in {1/4,1/2,1,3/2}`, using prime powers through `10^6`
  and the first twenty verified critical-line zero pairs.

Current replay:

```text
PASS_PFR_T5_T6_CONTINUATION
checks=8
proof_object=c29b66ffdb29e5eb2eedef66ded096be38af2e1d9d52219cecd830645dcfb2d8
8 focused tests pass
RH_UNPROVEN
```

The numerical comparison is ordinary double precision and authenticates only
a regression.  It does not prove the analytic theorem or a zero-free region.

---

## Exact next burdens

### PFR-G6 — height-localized source resolvent

Construct a source-defined localization in zero ordinate whose energy abscissa
is the maximal off-critical displacement in a chosen height window.  The
localizer must not be fitted from zero positions and must retain a controlled
prime-side formula.

### PFR-G7 — curvature-defect estimate

Control the exact defect

\[
\sum_j\left[
\int_{\gamma_j}^{\gamma_{j+1}}
\frac{\vartheta'(t)(\mathfrak C_H(t))_-}
{\vartheta'(t)^2Z(t)^2+Z'(t)^2}\,dt
+(L_j-\pi)_+
\right]
\]

strongly enough to turn (3.12) into a new critical-line zero count.

### PFR-G8 — boundary closure

Combine the flower curvature ledger with the exact Riemann--von Mangoldt
boundary term, multiplicities, and Turing-style endpoint accounting.  Main
term saturation is not enough for RH.

### PFR-G9 — prime-side stability mechanism

Prove boundedness or every-positive-damping `L^2` integrability of (5.4)
directly from the prime source.  This is an RH-strength cancellation theorem;
the present pass identifies the exact real function but does not prove its
stability.

---

## Scope firewall

```text
petal simple iff angular span <= 2*pi                 PROVED EXACT
open-petal signed turn = -(span+pi)                  PROVED EXACT
absolute-curvature excess pays angular excess         PROVED EXACT
flower curvature-defect zero-count ledger             PROVED EXACT
actual-Xi prime-defined Gamma-resolvent formula        PROVED EXACT
resolvent L2 abscissa = supremal off-line distance     PROVED EXACT
resolvent pointwise exponent = same distance           PROVED EXACT
analytic hard-window multiplier                        REFUTED GENERICALLY
height-localized actual-Xi theorem                     OPEN
prime-side boundedness                                 OPEN / RH-EQUIVALENT
new critical-line zero proportion                      NONE
Riemann Hypothesis                                     UNPROVEN
```
