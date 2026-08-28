# Native beta Nyquist compression — research reset

## Executive result

A new fixed compact smoother built from widths

\[
a_j\asymp\frac1{j\log^2(ej)}
\]

has a zero-free right-half-plane Laplace product and Fourier decay

\[
\exp\{-c|t|/\log^2(e+|t|)\}.
\]

Convolving it with the source-locked beta band preserves the individual-zeta
RH criterion. The exterior energy beyond

\[
T_A(X)\asymp
\log X\,(\log\log X)^2
\]

is \(O_A(X^{-A})\) without any Möbius cancellation.

Because the physical log-scale field is compactly supported in an interval
of length \(\log X+O(1)\), Fourier-series Parseval samples the complete energy
exactly on one lattice of spacing \(2\pi/(\log X+O(1))\). Truncation leaves only

\[
O_A((\log X)^2(\log\log X)^2)
\]

samples.

## New proof DAG

```text
native individual-zeta beta source
  -> fixed logarithmic box cascade
  -> near-exponential spectral tail
  -> exact Paley-Wiener/Nyquist lattice
  -> almost-quadratic finite-rank beta vector NBV107000
  -> fixed Mellin-Landau consumer
  -> RH.
```

Everything except the norm estimate `NBV107000` is unconditional.

## Why this is not another completion route

The coefficient remains

\[
\beta(n)=\mu(n)-1_{67|n}\mu(n/67).
\]

There is no square lift, Euler--Beta owner allocation, family average, Wick
completion, or principal-member argument. The QPTI semiprime obstruction is
therefore absent by construction.

## Review-sensitive points

1. The box widths must sum to a fixed finite support.
2. The Fourier product must be shown zero-free in the open right half-plane.
3. The near-exponential envelope must be uniform beyond one fixed threshold.
4. The sampling interval must strictly contain the whole physical support.
5. The tail of the discrete lattice, not only the continuous integral, must
   be paid.
6. The low rank must not be promoted to an arithmetic norm estimate.
