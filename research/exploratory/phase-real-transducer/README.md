# Phase-flow and real-response Gate 0

Status: `PROPOSED / EXACT FINITE / EXACT ANALYTIC / NON_DIRECTED_HIGH_PRECISION`  
Scope: finite models plus source-defined actual-Xi transforms; RH unproved  
Base: current `main` lineage, continued on draft PR #768  
Programmes: issue #763; overlaps issue #17, issue #39, issue #744 / PR #729, PR #762, and Weil/Suzuki positivity

## Scientific map

```text
PFR-T1   Hardy flower area, curvature, and participation bounds
PFR-T2   safe centered-Xi phase velocity = real prime cosine field
PFR-T3   finite inverse-Poisson response energy detects off-axis height
PFR-T4   critical explicit formula in phase/de-Poissonized form
PFR-R1   local quartet -> local Speiser critical point is false
PFR-T5   actual-Xi Gamma resolvent has exact zero-displacement abscissa
PFR-T6   petal turn, self-intersection, and curvature-defect ledger
PFR-R2   exact holomorphic hard ordinate window is impossible
PFR-T7   the actual-Xi resolvent is a real prime-knot spline
PFR-T8   flower curvature defect = positive zeta-prime phase variation
PFR-R3   nonvanishing filters preserve the infinite-time abscissa
PFR-T9   complex Gamma filters give finite-horizon soft localization
PFR-T10  symmetric resolvent = prime-knot + Bochner + Pick structure
PFR-T11  flower--Speiser Gauss law and harmonic screening ledger
PFR-R4   mirror critical points can screen flower curvature perfectly
```

The latest continuation is [`CONTINUATION_108420.md`](CONTINUATION_108420.md).
It adds two major bridges and one firewall:

1. a source-defined symmetric Xi resolvent whose local derivative jumps recover
   `Lambda(n)/sqrt(n)`, whose global growth records `Theta-1/2`, and which is
   positive definite / positive real / Pick-positive exactly under RH;
2. an exact finite-rectangle Gauss law converting the flower's positive
   `zeta'` phase variation into a Speiser zero count plus explicit screening
   and boundary flux;
3. an exact mirror-screening countermodel showing that curvature cannot count
   left critical points without controlling right-side harmonic measure.

## Replay

```bash
python3 research/exploratory/phase-real-transducer/code/verify_phase_real.py
python3 research/exploratory/phase-real-transducer/code/verify_phase_resolvent.py
python3 research/exploratory/phase-real-transducer/code/verify_flower_curvature.py
python3 research/exploratory/phase-real-transducer/code/verify_phase_speiser_localization.py
python3 research/exploratory/phase-real-transducer/code/verify_phase_positive_screening.py
python3 -m unittest discover \
  -s research/exploratory/phase-real-transducer/tests \
  -p 'test_*.py' -v
```

Latest marker:

```text
PASS_PFR_SYMMETRIC_POSITIVITY_AND_SPEISER_SCREENING
checks=10
proof_object=eec2e381e3efc29ebe85bfe406027a6e54117db2cc833e2130a75458ab65498e
RH_UNPROVEN
```

The replays authenticate finite formulas and bounded non-directed regressions.
They do not machine-prove the analytic manuscripts or external novelty.

## Claims and open gates

- `PFR-T1`--`PFR-T11`: exact statements with explicit imported/project-native boundaries.
- `PFR-R1`--`PFR-R4`: reusable structural firewalls.
- `PFR-C1`: prove symmetric or one-sided source positivity/boundedness; RH-strength and open.
- `PFR-C2`: exact hard height localization closed by `PFR-R2/PFR-R3`.
- `PFR-C3`: control the flower--Speiser screening and finite-window boundary flux; open.
- `PFR-C4`: source-defined in-band lower frame bound for the soft finite-horizon localizer; open.

No new critical-line zero proportion, off-line zero, `zeta'` zero, RH theorem,
or external priority claim is made.
