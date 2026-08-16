# Hardened four-adic annular chain: normalization repair and a two-row direct consumer

## Executive result

The \(J_\Lambda/P_\Lambda/F_\Lambda\) distinction in PR #541 is fatal to the
endpoint consumer used in PR #535. Exact native saturation gives
\(\mathcal H=P_\Lambda\), not \(J_\Lambda\); it leaves the complete arithmetic
gap \(F_\Lambda\) untouched.

The annular construction nevertheless has a stronger direct consumer. For a
fixed component row,

\[
\int_1^\infty [c_X(j)-c_{X/4}(j)]X^{-s-1}dX
=(1-4^{-s})\left[
\frac{C_j}{s^2}+
\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
\right].
\]

The annular factor is nonzero in \(\Re s>0\). Moreover the two explicit
kernels \(P_2,P_3\) have no common zero in the open strip: simultaneous
vanishing forces \(2^{-z}\in\{1,2\}\), hence \(\Re z\in\{0,-1\}\).

Therefore eventual positivity of only the two component rows \(j=2,3\)
already implies RH by Landau. The full annular telescope, all-row SHARP,
endpoint deficits, prime-square moat, and large-\(j\) asymptotics are unnecessary.

## Adversarial producer verdict

The old four-block Peano display is not a reconstructible proof. Its cut set
and edge terms are not defined and the Möbius cancellation is asserted rather
than expanded. This packet does not silently import it.

The exact surviving producer target is

\[
\int_{X/4}^{X}S_2(t)\frac{dt}{t}\ge0,
\qquad
\int_{X/4}^{X}S_3(t)\frac{dt}{t}\ge0,
\]

with the completely explicit Möbius kernels in `L-96012`. The functions are
affine in \(\log X\) on every unit cell, so integer knots are exhaustive for
falsification.

## Extended computation

```json
{
  "N": 10000000,
  "elapsed_sec": 4.5382750034332275,
  "formula": "log4*S[floor(X/4)] + logX*(S[X]-S[floor(X/4)]) - (T[X]-T[floor(X/4)])",
  "rows": {
    "2": {
      "X": 3,
      "minimum": 0.860121382433459,
      "negative_count_below_-1e-10": 0
    },
    "3": {
      "X": 4,
      "minimum": 0.33218664394213004,
      "negative_count_below_-1e-10": 0
    }
  }
}
```

The scan is evidence only. It neither supplies the missing infinite producer
proof nor changes the status of RH.

## Status

```text
normalization correction                 proved
annular Mellin transform                 proved
two-row noncancellation                  proved
two-row -> RH implication                proved
two-row annular positivity               open / RH-bearing
complete unconditional RH proof          not obtained
Riemann Hypothesis                       unproved
```
