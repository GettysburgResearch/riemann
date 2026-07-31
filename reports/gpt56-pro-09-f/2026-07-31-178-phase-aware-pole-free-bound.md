# Phase-aware pole-free prime-error bound

Agent: `gpt56-pro-09-f`  
Date: 2026-07-31  
Issue: #178  
Stack: PR #177

## Result

The qualitative pole-free criterion of PR #165 has been converted into a finite
phase-aware interval theorem.

For one fixed raw prime-power window, retain selected certified critical-line
zeros with their exact phases.  Bound only the unselected zeros through:

1. finite shell count upper bounds and transform suprema;
2. an explicit high-zero moment derived from the Bellotti--Wong zero-count
   majorant;
3. an exponentially decaying trivial-zero tail.

Under RH,

```text
|complete prime sum - selected phase model - trivial model| <= B.
```

A directed interval outside this band proves an off-line zero exists.  For a
real endpoint-profile packet, the same argument gives a Loewner matrix band and
a frozen-vector disproof test.

## New candidate

The five-notch universal window at

```text
x = 8578244975439 / 549755813888
```

contains only 64,542 prime-power terms in the ordinary finite manifest.
Reconnaissance gives:

```text
raw prime midpoint       +4.183986431348427e-9
100-zero + trivial model +6.270779861476257e-11
ordinary discrepancy     +4.121278632733664e-9
```

The planning high-zero tail after the first 100 zeros is about `5.6e-26`.
The current prime discrepancy is almost certainly dominated by FFT/window
interpolation error, but the exact directed calculation is cheap enough to
settle.

## Mathematical boundary

The new band is conditional on RH.  It is a disproof interface, not the missing
positive proof of the terminal norm.  False RH forces eventual violation because
the window transform is nonzero at every shifted right-half-plane zero.

## Exact finite layer

`X-15605` uses only integer and Fraction arithmetic.  Eight adversarial tests
pass.  The synthetic proof-object digest is

```text
8ecafb5da1d9f31c2cfe638a7067ce25ab00b9d65dc5df90bfc62e60114ed774
```

## Immediate handoff

Build a directed evaluator for the exact infinite-convolution/notched window,
certify the first 100 zero phases, enumerate the 64,542 prime powers, and run the
finite checker.  Preserve either a strict band violation or a proof-grade
numerical-floor diagnosis.
