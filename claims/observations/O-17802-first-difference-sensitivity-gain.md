# O-17802 — First-difference and hybrid notch reconnaissance

Claim ID: `O-17802`  
Status: `EMPIRICAL / SCHEDULING ONLY`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Dependencies: `L-17802`; ordinary high-precision first-100-zero evaluation  
Counterexample status: none

## Motivation

The original five box-square notches in PR #165 drove the known-line background
to the numerical floor, but `L-17802` shows that they also impose ten powers of
high-frequency decay. Since any undiscovered off-line zero must lie beyond the
verified critical-line frontier, that is the wrong optimization target once the
known phases are modeled explicitly.

## Ordinary first-100-zero RMS

For the universal smooth pole-free base window, using midpoint values of the
first 100 zeta zeros and 60-decimal arithmetic, the RH zero-side RMS values are:

```text
base, no critical-zero notch             5.388903995843091e-3
five box-square notches                  2.911441577923176e-16
five normalized first differences        2.256771542808316e-7
```

Replacing exactly one old notch by a normalized first difference gives:

```text
zero 1   RMS 7.077460570813262e-14   rigorous frontier gain >3.6004e23
zero 2   RMS 5.194886992711982e-14   rigorous frontier gain >1.6737e23
zero 3   RMS 8.233937665275407e-15   rigorous frontier gain >1.1983e23
zero 4   RMS 6.139515169133129e-15   rigorous frontier gain >8.4297e22
zero 5   RMS 7.331719653539385e-15   rigorous frontier gain >7.4388e22
```

Thus:

- the fourth-zero hybrid has the smallest ordinary first-100 RMS;
- the third-zero hybrid has the best guaranteed sensitivity gain among the three
  lowest-RMS hybrids;
- the all-difference filter sacrifices line-background suppression but gains more
  than `4.5e115` in guaranteed response relative to the all-box filter at the
  verified frontier.

## Candidate queue

1. **Conservative candidate:** replace the fourth box-square notch only.
2. **Sensitivity candidate:** replace the third box-square notch only.
3. **Maximum-frontier candidate:** use all five normalized differences and retain
   the first 100 or more critical-zero phases exactly.
4. Repeat the same ladder on the exact triangular base of `L-15409`, eliminating
   the infinite-window evaluator entirely.

Every number above is ordinary high precision. None is a directed prime value,
a bound violation, or evidence against RH.
