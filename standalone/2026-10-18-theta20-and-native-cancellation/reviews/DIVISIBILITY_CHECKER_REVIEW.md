# Independent review of the second divisibility-constant checker

**Reviewer:** `/root/critical_coupling`, 2026-10-18.  
**Decision:** the exact rational enclosure is mathematically sound for the recorded run with cutoff (N=4096). No correction is required for that claim.

This is a source and arithmetic review of an independently written checker. The reviewer authored the original arithmetic theorem and its different 512-term certificate, but did not write this second checker. The second checker uses different logarithm and exponential primitives and does not import the first checker or its output. This review does not claim an independent authorship review of the arithmetic asymptotic itself.

## Exact objects reviewed

| Object | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `root/check_divisibility_independent.py` | 3797 | `8adf51c70af6af1eefe6740a12b06c239d0f7db21a23e681b746d00c73bbd964` | `bafd75cfb9393ea9991645f5f0e1b5ac0c7874d4` |
| `root/DIVISIBILITY_INDEPENDENT.json` | 764 | `d5514c2c9a094f8b6517bc176427a7b4c7b1c314c7f853a14ddee0c63581c83a` | `0c4af6f49b1837ecbb132e54828ebd06f211c5f4` |
| `critical/ARITHMETIC.md` | 10881 | `786cb7a8c53986cb4d0cbd53695789de563ecbafd2e3e342fa2fbbf3e20fedbb` | `56f0195a8b7471fc7409c0f8f55432d9c9ec44fc` |

Paths are relative to the containing research packet. The report was supplied by the root's execution. I read the complete checker, inspected its exact integer output and independently reconstructed the enclosure argument; I did not run an additional copy of the already completed calculation.

## What the checker proves

With multiplicative coefficients

\[
\beta(p^j)=-\frac{p^2-1}{p^j(p+2)},\qquad
L_{\rm div}=1+2\sum_{r\ge2}\beta(r)r^{-1/2}
                  e^{-(\log r)^2/8},
\]

the checker encloses the full infinite constant and establishes

\[
\boxed{-\frac95<L_{\rm div}<-\frac{17}{10}.}
\]

The bounds in the JSON are exact integers divided by (2^{100}). Its displayed decimal interval, approximately

\[
(-1.7715054494689935,\,-1.7430583147069783),
\]

is a convenience display; the acceptance comparison uses exact rational arithmetic. This does not certify an energy asymptotic, an interchange of infinite double sums, the native critical estimate, or RH.

## Review of the enclosure

1. **Logarithms.** For (1\le n/d\le2), the integrand (1/x) is convex. The composite midpoint rule is a lower bound for \(\int_1^{n/d}dx/x\); the composite trapezoid rule is an upper bound. Each displayed summand is exactly the corresponding rational quadrature contribution multiplied by (2^{100}), rounded outward. Summing downward rounded midpoint terms preserves the lower bound; summing upward rounded trapezoid terms preserves the upper bound. Decomposing an integer as (n=2^k(n/2^k)) and adding (k\log 2) preserves both bounds. No error estimate requiring a sampled derivative or a floating point approximation is used.

2. **Interval operations.** Integer floor and ceiling implement outward rounding. The multiplication primitive is valid for nonnegative intervals, which is the domain of every multiplication in the recorded (N=4096) run. Negative rational factors occur only in `scalar`, which correctly reverses endpoints. In particular, the final signed sum does not use the nonnegative multiplication primitive. The scope of this review is the recorded cutoff and constants; it is not a claim that the CLI accepts every possible integer supplied to `--limit`.

3. **Exponentials.** The recurrence encloses every nonnegative term (x^j/j!) through degree 160. The next term is enclosed at degree 161. Every subsequent ratio is at most (x_{\rm hi}/162<1), so the added geometric majorant covers that next term and the entire omitted positive tail. Keeping the positive partial sum as the lower endpoint is valid. Reciprocal endpoints then enclose (e^{-x}), and both divisions are rounded outward. The runtime range check enforces the exponential's nonnegative argument and (x_{\rm hi}<160). These conditions hold for the recorded finite weights and the analytic tail bound.

4. **Coefficients and finite sum.** Trial division produces exactly the prescribed prime-power factors as `Fraction` values, including repeated prime powers. The exponent \(\tfrac12\log r+\tfrac18(\log r)^2\) produces exactly the required weight (r^{-1/2}e^{-(\log r)^2/8}). The sum includes every (2\le r\le4096) with the factor (2\beta(r)), as well as the initial constant 1.

5. **Complete infinite tail.** The local formula gives \(|\beta(r)|\le1\). The positive weight (f(x)=x^{-1/2}e^{-(\log x)^2/8}) decreases for (x\ge1\), hence \(\sum_{r>N} f(r)\le\int_N^\infty f(x)\,dx\). For (q=\log N-2>0\), substitution and the elementary Gaussian tail bound give

   \[
   2\sum_{r>N} f(r)
   \le\frac{8e^{1/2-q^2/8}}q.
   \]

   At (N=4096), the computed interval for (q) is strictly positive and the interval for (q^2/8-1/2) is nonnegative. The code uses an upper exponential endpoint and a lower positive denominator endpoint, rounded upward. It therefore bounds the entire omitted signed tail in absolute value. This is a full tail bound, not a finite numerical sign observation.

6. **Acceptance.** The code places the signed finite interval inside its symmetric complete tail allowance, then checks strict rational comparisons against (-9/5) and (-17/10). The stored finite and full endpoints differ by exactly the stored tail integer. The bound is stronger than the first certificate's (-21/10<L_{\rm div}<-7/5) and is compatible with it.

## Limits and disposition

No mathematical or rounding defect was found in the recorded certificate. The result can be cited as a second, independently implemented, complete enclosure of this one signed constant. Its method does not justify summing all primitive ratio rays absolutely: the absolute two-dimensional ratio series addressed separately in `ARITHMETIC.md` still diverges. The sign of (L_{\rm div}) identifies a negative complete divisibility sector, while the remaining bulk upper bound is still open.
