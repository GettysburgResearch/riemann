# X-12201 — Moving-anchor two-Schur certificates

Status: exact finite synthetic checker plus ordinary PR #103 reconnaissance  
Agent: `gpt56-05-j`  
Issue: #122  
Claims: L-12201, T-12202, L-12203, L-12204, M-12201

## Purpose

Draft PR #117 shows that adjoining the critical-line node `t=0` raises the maximum response degree while introducing one new moment. X-12201 generalizes this to every exact positive node.

For an old degree-`2m` moment table and a new anchor `t>0`, all new shifted moments except `c_0` are inherited. The complete degree-`2m+1` half-line cone is decided by

```text
theta_0 <= c_0 <= U_t.
```

A lower violation gives an explicit square response; an upper violation gives an explicit `(z-t)`-times-square response.

## Exact synthetic certificate

The committed rational control uses old moments

```text
(3, 7, 21, 73, 273)
```

and anchor

```text
t = 2.
```

These are the first five moments of three unit atoms at `y=1,2,4`. The shifted moments are

```text
(3, 13, 61, 307, 1633).
```

The checker reconstructs

```text
theta_0 = 101/135,
theta_1 = 539/360,
U_t     = 541/720,
width   = 7/2160.
```

The exact witness polynomials are

```text
q_0(z) = 1 - (64/135) z + (7/135) z^2,
q_1(z) = 1 - (329/720) z + (7/144) z^2.
```

The five cases demonstrate:

- a strict interior point `c_0=3/4`;
- a lower square violation at `c_0=7/10`;
- an upper shifted-square violation at `c_0=4/5`;
- both fail-closed boundary cases.

The lower and upper witness values are reconstructed from the full moment matrices, not merely asserted from threshold subtraction.

## Width regression

The checker constructs

```text
P_t(z)=t q_0(z)^2+(z-t)q_1(z)^2.
```

It verifies `P_t(0)=0`, divides by `z`, shifts back to `y`, and evaluates the resulting old degree-four polynomial. The exact value is

```text
7/1080 = t*(U_t-theta_0).
```

This is the finite regression for L-12203.

## Files

- `verify.py` — exact integer/Fraction checker;
- `certificates/synthetic-two-schur.json` — exact control data;
- `results/synthetic-verification.json` — retained exact output;
- `tests/test_verify.py` — adversarial unit tests.

## Reproduction

```bash
python verify.py certificates/synthetic-two-schur.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

An independent exact notebook reconstruction checked all committed thresholds, both explicit negative witness values, both boundary zeros, and the width identity before publication. The repository unittest file additionally checks schema mutations and fail-closed behavior.

## PR #103 reconnaissance

O-12201 records ordinary midpoint calculations at the exact PR #103 atomized-minimum ordinate. All tested anchors lie inside the Schur interval. The dimensionless interval coordinate moves from approximately

```text
rho_1       = 0.2173
rho_256     = 0.5132
rho_1048576 = 0.9826.
```

Large anchors approach the upper wall, but L-12203 shows that the entire inherited interval is simultaneously contracting. No candidate is inferred from tiny raw large-anchor gaps.

The recommended first proof-producing control is `t=4`: the new point lies at `Re(s)=5/2`, supports an independent directed Euler-product implementation, and has ordinary two-sided slacks around `10^-12`.

## Production certificate sketch

A production object should contain:

```text
schema
old node / ordinate / normalization / deflation fingerprints
exact t
old directed moment intervals
new direct-xi rectangle
reference point and reduced polynomial
full c_0 interval from both reconstructions
rationalized q_0 and q_1
fixed-polynomial interval contractions
width-polynomial consistency interval
verdict
producer fingerprints and SHA-256 ledger
```

The final checker should not trust supplied Schur thresholds or a floating linear solve. It reconstructs exact rationalized witness coefficients and checks their direct interval contractions.

## Proof boundary

X-12201's committed signs are synthetic rational controls. O-12201 is ordinary reconnaissance. No Riemann-xi moving-anchor interval has been certified, no counterexample has been found, and no `Z-####` candidate is allocated.