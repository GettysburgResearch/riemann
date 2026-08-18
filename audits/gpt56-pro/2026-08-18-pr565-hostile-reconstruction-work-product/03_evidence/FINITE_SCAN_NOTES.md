# Corrected finite scan

`code/scan_p61_bias_corrected.cpp` is the corrected scanner retained for this packet.

Important implementation point: the exploratory scanner first written during the pass generated all `2^18` divisors in signed 64-bit integers. The complete product of primes through 61 exceeds 64-bit range. The corrected scanner recursively generates only divisors `d <= N/2`, using the cutoff before multiplication, so no overflowing irrelevant products enter the list.

The coefficient reduction is

\[
F(x)=\sum_{n\le x}\frac{f_n}{\sqrt n}H_x(n),
\qquad
M(x)=\sum_{n\le x}\frac{m_n}{\sqrt n}H_x(n),
\]

where

\[
f_n=\sum_{d m=n,\ d\mid P_{61}}\mu(d)q_\star(m),
\qquad
m_n=\sum_{d m=n,\ d\mid P_{61}}q_\star(m).
\]

For a fixed open interval between consecutive integer knots, the active and saturated index sets are constant, so every linear margin `aF+bM` is affine in `log(x)`. Its minimum on that interval occurs at an endpoint. Therefore the integer-knot scan covers the real continuum on the finite range, modulo the floating-point enclosure issue.

Retained command:

```bash
g++ -O3 -std=c++17 code/scan_p61_bias_corrected.cpp -o scan_p61
./scan_p61 12300000
```

The result is diagnostic rather than directed interval arithmetic. Its margins are large enough to make it valuable reconnaissance, but the archive does not relabel it a universal certificate.
