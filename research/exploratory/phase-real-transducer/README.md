# Phase-flow and real-response Gate 0

Status: `PROPOSED / EXACT FINITE / EXACT ANALYTIC / NON_DIRECTED_HIGH_PRECISION`  
Scope: finite models plus source-defined actual-Xi transforms; RH unproved  
Base: current `main` lineage, continued on draft PR #768  
Programmes: issue #763; overlaps issue #17, issue #39, issue #744 / PR #729, and PR #762

## Scientific map

```text
PFR-T1  Hardy flower area, curvature, and participation bounds
PFR-T2  safe centered-Xi phase velocity = real prime cosine field
PFR-T3  finite inverse-Poisson response energy detects off-axis height
PFR-T4  critical explicit formula in phase/de-Poissonized form
PFR-R1  local quartet -> local Speiser critical point is false
PFR-T5  actual-Xi Gamma resolvent has exact zero-displacement abscissa
PFR-T6  petal turn, self-intersection, and curvature-defect ledger
PFR-R2  exact holomorphic hard ordinate window is impossible
PFR-T7  the actual-Xi resolvent is a real prime-knot spline
PFR-T8  flower curvature defect = positive zeta-prime phase variation
PFR-R3  nonvanishing filters preserve the infinite-time abscissa
PFR-T9  complex Gamma filters give finite-horizon soft localization
```

The latest continuation is `CONTINUATION_108320.md`.  It adds three structural
advances:

1. the real Gamma resolvent recovers `Lambda(n)/sqrt(n)` as universal derivative
   jumps at `t=log n`, while its global growth still records `Theta-1/2`;
2. the petal-curvature defect is exactly the positive variation of
   `arg zeta'(1/2+it)`, with a finite signed-Poisson critical-point model;
3. hard and infinite-time height localization are closed at a no-go boundary,
   while finite-horizon complex-Gamma localization has an explicit leakage
   estimate.

## Replay

```bash
python3 research/exploratory/phase-real-transducer/code/verify_phase_real.py
python3 research/exploratory/phase-real-transducer/code/verify_phase_resolvent.py
python3 research/exploratory/phase-real-transducer/code/verify_flower_curvature.py
python3 research/exploratory/phase-real-transducer/code/verify_phase_speiser_localization.py
python3 -m unittest discover \
  -s research/exploratory/phase-real-transducer/tests \
  -p 'test_*.py' -v
```

The replays authenticate finite formulas and bounded non-directed regressions.
They do not machine-prove the analytic manuscripts or external novelty.

## Claims

- `PFR-T1` -- `PFR-T9`: exact statements with distinct imported/project-native boundaries.
- `PFR-R1` -- `PFR-R3`: reusable structural firewalls.
- `PFR-C1`: source-only boundedness of the global real spline, equivalent to RH and open.
- `PFR-C2`: exact hard height localization closed by `PFR-R2`/`PFR-R3`.
- `PFR-C3`: full curvature-defect plus Riemann--von Mangoldt boundary closure, open.
- `PFR-C4`: source-defined in-band lower frame bound for the soft finite-horizon localizer, open.

No new critical-line zero proportion, off-line zero, `zeta'` zero, RH theorem,
or external priority claim is made.
