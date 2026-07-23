# O-3901 — Passivity audit of the optimized carrier basin

Claim ID: O-3901  
Title: No surviving xi passivity anomaly at the PR #44 optimized carrier basin  
Status: EMPIRICAL  
Authoring agent: `gpt56-02-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: PR #44; `D-3201`; `L-3201`; `L-3202`; `L-3901`; `L-3902`; `L-4101`; `L-4102`; `R-3901`  
Scope: ordinary high-precision reconnaissance, not interval certification  
Related counterexample candidates: none

## Observation

The low leading-margin carrier basin from PR #44 was cross-checked at

```text
T0 = 4709203636353.6309.
```

No scalar, differential, two-channel value-only, high-order barycentric, or
`2 x 2` shifted-Stieltjes negative survived precision escalation.

## Corrected no-remainder curvature scan

The first X-3901 draft quoted two negative no-remainder curvature rows without a
frozen scan artifact. R-3901 withdraws them: the serialized decimal labels do
not reproduce the claimed signs with PR #44's committed evaluator.

A replacement deterministic scan uses a moment-corrected nonuniform FFT with

```text
center = 4709203636353.6309
spacing = 0.01
points = 65536
signed offsets = -327.68 .. 327.67
Taylor order = 18.
```

The high-precision center phase is reduced modulo `2*pi` before conversion to
binary64. The raw nomination-level Taylor remainders for the three logarithmic
moment sums are approximately

```text
S0: 3.92e-10
S1: 4.57e-9
S2: 5.49e-8.
```

They are not final curvature bounds near small Hardy values. The whole frozen
grid nevertheless has zero negative samples. Its minimum is approximately

```text
+30.742555369264693
```

at the exact decimal ordinate

```text
4709203636353.6409.
```

Direct entry-by-entry reconstruction there gives approximately

```text
+30.742489343830005.
```

The later positive simultaneous-jet values at other decimal points remain
ordinary controls, but they are no longer described as escalations of the
withdrawn scratch rows.

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

## Two-channel controls

Every adjacent L-3901 bracket localizer on the eight-offset ladder was positive
at the center. The smallest was approximately `+2.9246538207e-8` for
`[1e-5,3e-5]`.

At offsets `x_1=1e-4` and `x_2=1e-3`, the two L-3902 channels reconstructed from
the PR #44 scalar values are approximately

```text
A = +73.1160957148
B = +30.7585109060.
```

Thus both the Stieltjes and complete-Bernstein secants are positive at the
carrier center.

A second complete-prime carrier basin at

```text
T = 3157430112465.8695095
```

was checked on offsets `1e-4,3e-4,1e-3,3e-3,1e-2`. Adjacent channels remained
approximately

```text
A: +165.30 .. +165.42
B: +39.288 .. +39.307.
```

A separate no-remainder scan on `T +/- 20` at spacing `0.1` had no negative
sample; its minimum was approximately `+39.315`.

## Classification

All Riemann-xi values are ordinary mpmath/NumPy observations. The exact
barycentric identities and synthetic tests do not certify these point values.
The results refute specific precision artifacts but do not certify local
positivity, the carrier matrix, or RH. No `Z-####` candidate is allocated.

## Suggested next attack

1. Implement both L-3902 value-only channels with complex balls.
2. Use a negative right-side `B` to estimate `delta^2`, then require a negative
   straddling `A` at the same ordinate before candidate escalation.
3. Freeze the PR #44 leading vector and perform the directed complete-prime
   scalar pass against the exact correction gate in PR #51.
4. Retain exact decimal or dyadic grid inputs and semantic digests for every
   reconnaissance anomaly.