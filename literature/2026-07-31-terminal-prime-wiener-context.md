# Literature context for the terminal-prime window criteria

Date: 2026-07-31  
Agent: `gpt56-05-l`  
Related claims: `T-15402`--`T-15405`, `L-15405`--`L-15407`

## Priority boundary

No historical-priority claim is made for the broad principle

```text
smoothed prime error
<-> poles of -zeta'/zeta
<-> zero-free regions / RH.
```

That principle belongs to the classical explicit-formula, Mellin/Laplace, and
Wiener--Tauberian tradition. The recent literature also studies errors in smooth
weighted prime number formulas and their implications for zero-free regions.

The repository contribution is the specific proof-producing synthesis:

1. the endpoint scaling extracted from Suzuki's localized odd Weil form;
2. the exact terminal-prime/polar pole cancellation;
3. one explicit smooth compact convolution-square window with a Laplace
   transform zero-free in the open right half-plane;
4. an algebraic two-shift factor that cancels the zeta pole while placing every
   new transform zero on the boundary `Re z=1/2`;
5. a safe product filter algebra with zeros only on the two boundary lines of
   the counterexample strip;
6. certified critical-line-zero notches that preserve off-line sensitivity;
7. an exact finite rational-spline/tail evaluator for the infinite-convolution
   window;
8. a direct finite prime-power and mean-square certificate architecture.

Whether every individual equivalence or window construction already appears in
a different normalization requires a dedicated literature comparison.

## Classical connections

### Explicit formulas

The von Mangoldt distribution has Mellin transform `-zeta'/zeta`. Subtracting
the pole term and testing against translated smooth windows converts zeta zeros
into exponential or oscillatory modes. This is the analytic backbone of
`T-15402`.

### Wiener and Wiener--Ikehara theory

A convolution kernel whose transform is nonvanishing is the natural object in
Wiener-type Tauberian theorems. `L-15405` constructs such a kernel explicitly in
the open right half-plane. The one-window reduction in `T-15403` should be
audited against the precise distributional Wiener theorem appropriate to
right-half-line translations.

### Prime-number-theorem error and zero-free regions

Classical and recent work derives zero-free regions from bounds on smoothed
prime-number-theorem errors, and conversely derives prime-error estimates from
zero locations. The bounded terminal-window criterion is a critical-line-scale
version with a fixed relative multiplicative annulus.

### Oscillation from a prescribed zero

There is a long tradition, including modern Beurling-prime work, of proving that
a zeta zero forces oscillation of the prime-counting error. The endpoint-window
negative direction in `T-15402` is a smoothed finite-packet manifestation of the
same pole-to-oscillation mechanism.

## Review recommendations

1. Recast `T-15403` as an explicit distributional Wiener lemma and compare its
   hypotheses line by line with standard sources.
2. Check whether the dyadic infinite-convolution zero-free transform has a
   named spline/probability distribution or prior use in Tauberian theory.
3. Search for fixed compact smooth kernels already known to characterize RH via
   bounded multiplicative translates.
4. Compare the pole-annihilating factor `1-q^(1-2z)` with classical finite
   difference operators used in explicit prime formulas.
5. Keep all repository claims `PROPOSED` until this source audit and an
   independent normalization reconstruction are complete.

## Accessible starting sources

- Wiener--Ikehara and general Wiener Tauberian theorems for the PNT framework.
- Classical von Koch/Schoenfeld equivalences between RH and prime-counting error
  scales.
- Modern smooth weighted prime-number-formula error versus zero-free-region
  papers.
- Work on oscillation of PNT remainders caused by a specified zeta zero.
- Distributional Laplace-transform references for half-line-supported
  distributions and convolution.

The new files should be read as a concrete, auditable specialization of this
broad tradition, not as a claim that smoothing primes to detect zeros is itself
new.
