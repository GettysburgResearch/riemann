# Ranked continuation queue

## 1. Source-only bound for the prime-knot real spline

Use the source formula and the differential ladder

```text
(a-D)^m R_(a,m)
  = archimedean field - sum Lambda(n)/sqrt(n) delta_(log n)
```

to prove `R_(a,m)` bounded, or its weighted energy finite for every positive
damping.  By `PFR-T5`, this is exactly RH-strength.  `PFR-T7` now exposes the
local prime knots and the global zero-growth burden in one real object.

## 2. In-band lower frame bound for soft Gamma localization

`PFR-T9` gives a zero-independent complex-Gamma filter with explicit exterior
leakage on every finite horizon.  The missing theorem is a source-defined lower
bound for the selected in-band signal which survives cancellation and the
transition band.  This, rather than another filter, is the next localization
frontier.

## 3. Full curvature--Speiser adapter

`PFR-T8` identifies the open flower defect as

```text
integral (Re zeta''/zeta')_+ dt.
```

Construct the complete canonical-product / Littlewood ledger for `zeta'`,
including its pole, trivial/background terms, and finite-window boundaries.
Do not identify positive curvature with a bare left-zero count without this
adapter.

## 4. Curvature-defect source estimate

Bound

```text
sum_j [ integral_(petal j) (Re zeta''/zeta')_+ dt
        + (Delta theta_j-pi)_+ ]
```

by a source, trace, or positive energy strong enough to improve a critical-line
zero count.  Existing curvature identities by themselves do not provide the
sign or the global boundary closure.

## 5. Certified computational pass

With interval or ball arithmetic, certify on a modest finite window:

- critical-line petal areas and angular spans;
- signed and absolute curvature, plus `Re zeta''/zeta'`;
- `zeta'` critical points and Newton-flow separatrices;
- Gamma-resolvent source values and derivative jumps at selected prime powers;
- complex-Gamma soft-band leakage for predeclared parameters.

The result is structural regression, not a global proof or counterexample.

## 6. Arithmetic-to-geometry comparison

Compare the prime-knot spline, the flower curvature defect, PR #729's
backward-Poisson phase field, and PR #762's beta spectral abscissa.  Seek an
exact common producer or prove that the observables remain genuinely distinct.

## Stop conditions

Pause or redirect the lane if review proves that:

- the prime-knot spline is only a standard explicit-formula smoothing with no
  usable new source inequality;
- the curvature ledger reduces to a known one-way conditional theorem and no
  quantitative boundary adapter survives;
- the soft localizer admits no source-defined in-band lower frame bound;
- every finite invariant survives a known RH-false zeta analogue;
- or a claimed source formula, jump normalization, pole residue, or endpoint
  term fails hostile review.
