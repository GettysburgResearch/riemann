# Phase-flow / real-only Gate-0 packet

This exploratory packet studies:

1. the flower/petal geometry of `zeta(1/2+it)`;
2. real-only phase and explicit-formula representations of zero displacement.

Start with [`MATHEMATICS.md`](MATHEMATICS.md), then read the
[`continuation index`](CONTINUATION_108260.md),
[`flower theorem`](FLOWER_CURVATURE_108260.md),
[`actual-Xi resolvent theorem`](XI_GAMMA_RESOLVENT_108260.md), and
[`localization firewall`](LOCALIZATION_FIREWALL_108260.md).

## Principal results

### Initial Gate 0

- `PFR-T1`: exact Hardy-flower area, speed, curvature, weighted Wirtinger,
  and participation-count identities;
- `PFR-T2`: the centered-Xi flower phase velocity above the zero strip is an
  absolutely convergent real prime cosine signal on `Re(s)>1`;
- `PFR-T3`: for every finite real zero model, inverse Poisson evolution gives
  a real response whose weighted-energy abscissa is exactly the maximal
  off-axis zero height;
- `PFR-T4`: the same de-Poissonization is the critical-weight explicit formula
  for actual Xi, in distributional form;
- `PFR-R1`: an Xi-symmetric off-axis quartet can have only real derivative
  critical points, closing any generic one-quartet/one-Speiser-branch rule.

### Continuation 108260

- `PFR-T5`: for every `a>1/2` and integer `m>=2`, one entirely real,
  prime-defined actual-Xi Gamma-resolvent has a safe logarithmic-derivative
  Taylor-remainder transform, and its weighted-`L2` abscissa and pointwise
  exponential type are exactly the supremal off-critical zero displacement;
  RH is equivalent to boundedness of this function;
- `PFR-T6`: a fixed-sign Hardy petal is simple exactly up to angular span
  `2*pi`, its open signed turn is `-(span+pi)`, and an explicit normalized
  negative-curvature integral plus the origin corner exactly accounts for the
  total curvature defect that pays for missing petal count;
- `PFR-R2`: a zero-independent holomorphic exponential-mode multiplier
  cannot produce an exact hard ordinate window; any viable localization must
  quantify leakage or use additional non-holomorphic/global structure;
- `PFR-C2`: exact height localization of the resolvent remains open under that
  firewall;
- `PFR-C3`: transferring the curvature-defect ledger into a new zero count
  remains open.

## Replay

```bash
python3 code/verify_phase_real.py
python3 code/verify_phase_resolvent.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected terminal markers include:

```text
PASS_PFR_PHASE_REAL_TRANSDUCER
PASS_PFR_T5_T6_CONTINUATION
RH_UNPROVEN
```

The replays authenticate finite algebra and floating-reconnaissance regressions only.
The analytic proofs are in the manuscripts and require ordinary mathematical
review.

## Scope

No zero is newly located. No zero proportion is improved. No RH or GRH claim is
made. External novelty and priority are explicitly unreviewed.
