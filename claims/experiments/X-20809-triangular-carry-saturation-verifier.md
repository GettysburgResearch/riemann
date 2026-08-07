# X-20809 — Triangular carry-saturation verifier

Experiment ID: `X-20809`  
Title: Exact averaged-carry algebra and ordinary canonical-coefficient reconnaissance  
Status: `EXACT SYNTHETIC ALGEBRA VERIFIED; RIEMANN POSITIVITY RECONNAISSANCE ONLY`  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `L-20815`; `L-20816`; `R-20805`; `T-20805`

## Exact retained verdict

The standard-library `Fraction` layer verifies:

```text
PASS_EXACT_AVERAGED_CARRY_AND_ADJOINT_RECONSTRUCTION
```

at a frozen rational synthetic level `X=14`. It exhaustively compares the
closed averaged-carry formula with direct floor counting and reconstructs the
same positive rational coefficient vector through both:

1. the backward triangular recurrence; and
2. the Möbius-adjoint factorization.

Retained exact values:

```text
coefficient count       13
minimum coefficient     13/210
target-sum digest        1995724207/662547600
```

## Ordinary actual-target result

At the retained actual target `X=10000`:

```text
negative coefficients below -1e-12    0
minimum positive coefficient            1.0003000695973407e-6
endpoint coefficient                     0
lead minus 4 sqrt(X)                      0.907762463298809
binomial objective                        371.5124154811048
complete von Mangoldt ramp                371.5124154811006
identity difference                       4.21e-12
```

The ordinary classification is

```text
ORDINARY_RECONNAISSANCE_NOT_A_CERTIFICATE
```

`O-20808` records separate in-session runs through `X=10^6`.

## Files

```text
experiments/X-20809-triangular-carry/
  verify.py
  README.md
  results/recon-10000.json
```

## Proof boundary

The exact layer authenticates all finite algebra used to define the Carry
Saturation Lemma. It does not prove that the actual logarithmic target emits
nonnegative coefficients for every cutoff. No finite result is promoted to RH.