# O-7501 — High-carrier direct-xi modulus reconnaissance

Claim ID: O-7501  
Title: The first direct-xi horizontal block is increasing and convex in ordinary high precision  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-g`  
Created: 2026-07-25  
Dependencies: L-7501 for interpretation only  
Scope: one exact dyadic ordinate and nine exact offsets  
Related counterexample candidates: none

## Parameters

The ordinate is the exact dyadic

\[
 T=\frac{20225875608343121406355}{2^{32}}
 =4709203636353.630899999989\ldots,
\]

and the horizontal offsets are

\[
 x\in\{2^{-20},2^{-18},2^{-16},2^{-14},2^{-12},
       2^{-10},2^{-8},2^{-6},2^{-5}\}.
\]

Ordinary 50-decimal reconnaissance used `mpmath`'s simultaneous
Riemann--Siegel evaluation.  To avoid underflow from the completed gamma factor,
it computed

\[
 \log|\xi(s)|
 =\log\left|\frac{s(s-1)}2\right|
 -\frac{\operatorname{Re}s}{2}\log\pi
 +\operatorname{Re}\log\Gamma(s/2)
 +\log|\zeta(s)|.
\]

This arithmetic is not directed and is not a certificate.

## Results

Normalize the modulus-square values by the positive common factor

\[
 \widetilde H(x^2)
 =\frac{|\xi(1/2+x+iT)|^2}
 {|\xi(1/2+2^{-20}+iT)|^2}.
\]

The resulting ordinary values are:

| `x` | `log(tilde H)` | `tilde H` |
|---:|---:|---:|
| `2^-20` | `0` | `1` |
| `2^-18` | `4.196215479997513e-10` | `1.0000000004196215481` |
| `2^-16` | `7.133566314145072e-9` | `1.0000000071335663396` |
| `2^-14` | `1.145566820986908e-7` | `1.0000001145566886603` |
| `2^-12` | `1.833326413363901e-6` | `1.0000018333280939078` |
| `2^-10` | `2.933361106406871e-5` | `1.0000293340412986445` |
| `2^-8` | `4.693302170671883e-4` | `1.0004694403697254975` |
| `2^-6` | `7.507242241002376e-3` | `1.0075354922329645557` |
| `2^-5` | `3.000289245701233e-2` | `1.0304575145032700303` |

Every adjacent modulus difference is positive. The adjacent secant slopes of
`log H` with respect to `u=x^2` decrease from approximately

```text
30.7585847527394
```

to

```text
30.7140610949256,
```

consistent with the L-7502 concavity requirement.

Every adjacent second divided difference of the normalized `H` values is also
positive. The smallest is approximately

```text
+436.4870960634164.
```

## Interpretation

No midpoint nomination survives in this exact horizontal block. The smallest
ordinary monotonicity moat is the first pair, with relative log-modulus-square
increase about `4.20e-10`; that row still merits directed evaluation because its
scale is much smaller than the later rows, but the block is not presently a
counterexample candidate.

The result is consistent with the existing directed `Re(xi'/xi)` grid, whose
smallest scalar value at the central ordinate was positive.

## Proof boundary

- The special-function values are ordinary `mpmath`, not Arb intervals.
- The normalized values share an ordinary computed denominator.
- Positivity on these nodes says nothing about other ordinates or inserted
  horizontal points.
- No `Z-####` identifier is allocated.

## Suggested next attack

1. Complete the 192/256-bit Riemann--Siegel Arb replay of this block.
2. If it is certified nonnegative, preserve the primitive direct-xi rectangles.
3. Search distinct exact ordinates rather than merely adding precision here.
4. Use the first adjacent pair as a low-width regression control for future
direct-xi producers.
