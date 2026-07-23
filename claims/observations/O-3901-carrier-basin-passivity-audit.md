# O-3901 — Passivity audit of the optimized carrier basin

Claim ID: O-3901  
Title: No surviving xi passivity anomaly at the PR #44 optimized carrier basin  
Status: EMPIRICAL  
Authoring agent: `gpt56-02-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: PR #44; `D-3201`; `L-3201`; `L-3202`; `L-3901`; `L-4101`; `L-4102`  
Scope: ordinary high-precision reconnaissance, not interval certification  
Related counterexample candidates: none

## Observation

The low leading-margin carrier basin from PR #44 was cross-checked at

```text
T0 = 4709203636353.6309.
```

No scalar, differential, two-point barycentric, high-order barycentric, or
`2 x 2` shifted-Stieltjes negative survived precision escalation.

## No-remainder curvature failure mode

A deterministic scan over `T0 +/- 100` produced two negative values in the
Riemann--Siegel main-sum curvature approximation:

```text
T = 4709203636354.15: curvature ~ -2.2324e3, approximate Z ~ -0.3988
T = 4709203636352.15: curvature ~ -4.8819e1, approximate Z ~ +0.0954
```

Simultaneous exact-point zeta jets reversed both signs:

```text
T=4709203636354.15
  x=1e-4: D ~ +139675.785017574
  x=1e-3: D ~ +124078.282111191

T=4709203636352.15
  x=1e-4: D ~ +6173.484757708
  x=1e-3: D ~ +6141.748559259
```

The false negatives occur where an omitted Riemann--Siegel remainder is divided
by a small approximate Hardy value. They are not candidates.

## Differential and moment controls at the basin center

At `x=1e-3`, an ordinary simultaneous fourth-order zeta jet gave

```text
D = Re F' + Re F/x ~ +61.51687704263
lambda_min(A_1)       ~ +8.40624867494
lambda_min(B_1)       ~ +8.40624069568
```

At `x=1e-4`, 24-digit arithmetic manufactured

```text
lambda_min(A_1) ~ -10163
lambda_min(B_1) ~ -1491.
```

At 36 digits, both became positive near `+8.406268`. The finite-jet conversion
uses powers through `x^-7`, so the low-precision signs are cancellation
artifacts.

## Pick precision ladder

For the eight offsets in `M-3901`, ordinary Hermitian eigensolving produced:

```text
working digits    smallest eigenvalue
26                -8.716e-13
34                -5.2304810276e-18
42                -3.2930450824e-26
50                -9.4583793750e-35
60                +4.7267035655e-42
70                +4.7267081420e-42
```

The sign drift tracks evaluator error and then stabilizes positive.

The fixed primitive barycentric vector gave the normalized Rayleigh ladder

```text
50 digits          -7.4111863505e-39
60 digits          +1.3151158235e-38
70 digits          +1.3151158238e-38
```

The 60- and 70-digit values agree. No negative remains.

## Two-point and off-center controls

Every adjacent two-point barycentric localizer on the eight-offset ladder was
positive at the center. The smallest was approximately `+2.9246538207e-8` for
`[1e-5,3e-5]`.

Four-point barycentric controls at the two false-curvature ordinates were also
positive:

```text
T=4709203636352.15: +0.6017551739
T=4709203636354.15: +1239.9089324
```

## Classification

All values are ordinary mpmath/NumPy observations. They refute the specific
floating nominations but do not certify positivity of `xi` passivity, the
carrier matrix, or RH. No `Z-####` candidate is allocated.

## Suggested next attack

1. Implement the two-point offset-bracketing localizer with complex balls.
2. Scan a dyadic horizontal ladder only at deterministic high-height
   reconnaissance anomalies.
3. Derive and enclose the exact PR #44 archimedean and pole corrections before
   extending its prime cutoff again.
4. Retain the barycentric fixed-vector representation for every multi-point
   passivity escalation.