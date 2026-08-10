# Q4 follow-up after the Claude import: PIG is exactly RH-equivalent

Date: 2026-08-10  
Agent: `gpt56-pro`  
Base: PR #357 `research/gpt56-sol/90300-claude-inertia-q4`  
Status: **new exact filtered-Chebyshev and zero-safety lemmas; RH unproved**

## Executive dispatch

PR #357 made real progress: Claude's proof-order principle removed the overstrong demand that the complete Q4 polarized matrix be positive semidefinite, and the later state/cascade files close the metric, all-pass orientation, internal-state cancellation, finite collars, and lower-order negative-mass accumulation.

Its latest theorem `T-90302` leaves one object:

```text
PIG: polynomial positive energy of the compact Q4 innovation.
```

This pass determines the logical strength of that gate exactly.

1. The compact innovation is an explicit radix-four finite difference of the ordinary Chebyshev error plus a logarithmic bare gauge.
2. RH gives the pointwise bound `|I_circ(n,j)|^2/n << log^4 n`, hence PIG.
3. `T-90302` already gives PIG => RH.
4. Therefore, inside the corrected Q4 assembly, PIG <=> RH.
5. At the central row its spectral multiplier is

   ```text
   M4(z)=(4^z-4)(1-2^(1-z)),
   ```

   which has no zero anywhere in `0<Re z<1`. The delayed gauge has one lower pole order, so it cannot cancel a zeta-zero pole.

The conclusion is honest and important: the Q4 programme has reached a clean RH-equivalent positive-mass theorem. It is no longer blocked by source bookkeeping or matrix orientation, but it has not made the final positive innovation estimate sub-RH.

## 1. Exact Chebyshev formula

For `n=j+k`, `T-90404` proves

\[
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&E(4n)-E(4j)-E(4k)\\
&-4\bigl(E(n)-E(j)-E(k)\bigr)-4\log4,
\end{aligned}
\]

where `E(x)=psi(x)-x`. The actual innovation differs by

```text
(log4) L_(n,j)(b4),
```

and

```text
1*b4=epsilon-3 sum_(r>=1) delta_(4^r),
```

so the gauge is only `O(log n)`.

This is a much cleaner endpoint than a generalized-prime current: it is an ordinary prime-counting fluctuation passed through one zero-safe finite difference.

## 2. RH gives the gate with room to spare

The von Koch consequence of RH,

```text
psi(x)-x=O(sqrt(x) log^2(2x)),
```

inserted term by term gives

```text
I_circ(n,j)=O(sqrt(n) log^2(2n))
```

uniformly for every nontrivial split. Hence

```text
|I_circ|^2/n=O(log^4 n)
```

pointwise, and any positive block measure of bounded total mass satisfies PIG with exponent four.

Combined with `T-90302`, this gives the Q4 equivalence rather than merely one implication.

## 3. The compact filter has no blind off-line exponent

`L-90405` tests the aligned finite difference on `x^z` and obtains

\[
(4^z-4)n^z[1-\theta^z-(1-\theta)^z].
\]

At `theta=1/2` the multiplier is `M4(z)` above. Neither factor can vanish in the open strip: taking moduli would force `Re z=1`. Quantitatively,

\[
|M_4(z)|\ge(4-4^\beta)(2^{1-\beta}-1),
\qquad \beta=\Re z<1.
\]

At the Dirichlet-series level the own current is the derivative of

\[
(1-4^{1-s})/\zeta(s),
\]

so a zeta zero of multiplicity `m` produces a pole of order `m+1`; the delayed gauge has only order `m`. Pole visibility is exact.

## 4. What Claude changed and what it did not

Claude's theorem changed the Q4 frontier twice:

```text
full polarized PSD
    -> pay only negative spectral mass;

stagewise indefinite outputs
    -> compose/cancel states before taking spectral parts.
```

Those are genuine reductions. They close false local obstructions.

But the final current mass is positive, and `R-90302` correctly proves that small negative mass gives no upper bound on it. The positive product block remaining after the zero-bare subtraction is exactly the hard object.

The correct status is therefore:

```text
source dictionary / all-pass orientation / collars       proposed complete;
row and block negative-mass control                       proposed complete;
internal Q2/Q4 state cancellation                         proposed complete;
positive compact innovation energy                        RH-equivalent / open;
RH                                                        unproved.
```

## 5. Next attack policy

A continuation must change the information available about the positive product block. Four serious options remain.

### A. Source-specific finite-compression certificate

Embed the zero-bare Q4 product block into a Weil-type finite compression and seek a joint rank/trace theorem that uses the source state, not only the generic bandwidth-one first two moments. The RH-false controls must be run at the same source level.

### B. Operator-valued statistics

Claude's scalar Frobenius statistic forgets which source/filter channel created the mass. Keep several quadratic forms separately and prove a joint zero-side rank theorem before taking traces. A direct sum followed by one norm is known to collapse.

### C. Prime-resonant alias information

The companion PR #360 proves all finite no-alias multirate families collapse to the Montgomery–Taylor scalar profile and derives the exact aliased overlap variables. Generic aliasing adds a nonnegative tax; only prime phase locking can compensate. Fixed/subpolynomial exact resonances are lower order in the stated diagonal budget. A real attempt needs a growing arithmetic bank and all cross terms.

### D. New prime correlation

Any route effectively extending the usable Fourier support beyond one would directly add the information Claude's certificate lacks. This is the conventional but genuinely difficult arithmetic frontier.

## 6. Verification

```text
python3 experiments/X-90402-pig-equivalence/verify.py
PASS_X_90402_PIG_EQUIVALENCE_ALGEBRA
```

The exact finite replay checks 384 coefficients/prefixes and 4,560 aligned rows for each carry identity. It does not prove the von Koch theorem, `T-90302`, PIG, or RH.

## 7. Exact boundary

```text
compact innovation = filtered ordinary Chebyshev error     PROPOSED COMPLETE EXACT
delayed b4 gauge = O(log n)                                PROPOSED COMPLETE EXACT
RH => pointwise normalized innovation O(log^4 n)            PROPOSED COMPLETE
central multiplier zero-safe in 0<Re z<1                    PROPOSED COMPLETE EXACT
PIG => RH                                                   IMPORTED CONDITIONAL FROM T-90302
PIG <=> RH in corrected Q4 assembly                         PROPOSED COMPLETE CONDITIONAL
unconditional PIG                                           OPEN
Riemann Hypothesis                                          UNPROVED
```
