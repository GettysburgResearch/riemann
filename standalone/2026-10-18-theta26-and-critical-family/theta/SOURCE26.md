# A complete directed theta source through moment 26

This file justifies the new source producer `source26.py`. It does not assume
the Riemann hypothesis, a zero-free strip, a table of zeta zeros, or an external
table of theta moments. The integer interval backend is imported unchanged
from the pinned source in PR #994:

`c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`standalone/2026-10-18-theta20-and-native-cancellation/theta/pr886_primitive.py`,
Git blob `c32015f110d10186538ffabcb4689ba5bbc060d0`.

The producer authenticates that exact blob before loading it. It configures the
backend for 512 fractional bits and Taylor degree 220; the inherited file is
not edited. Arithmetic endpoints are signed integers in units of `2^-512`.
All divisions, multiplications, square roots, and elementary exponential
enclosures are directed in that backend. The construction uses the same exact
96-term Machin formula and the same argument-reduced exponential routine;
their analytically bounded remainders remain included at the new precision.

## 1. Actual Xi normalization

For real `t >= 0`, let

\[
 \Phi(t)=\sum_{n\ge1}\left(4q_n^2e^{9t/2}-6q_ne^{5t/2}\right)
                 e^{-q_ne^{2t}},\qquad q_n=\pi n^2,
\]

and extend this density evenly to the line. The source's theta identity is

\[
 \frac{\int_{\mathbb R}e^{izt}\Phi(t)\,dt}
      {\int_{\mathbb R}\Phi(t)\,dt}
 =\frac{\xi(1/2+iz)}{\xi(1/2)}.
\]

Every summand is positive on the nonnegative real axis: its prefactor is
`2q_n e^(5t/2)(2q_n e^(2t)-3)>0`. Write `T` for the probability variable
obtained by normalization, and `v = E[T^2]`. The computed moment sequence is
that of `T/sqrt(v)`, which has variance one. Fourier bands in this standardized
variable must therefore be divided by `sqrt(v)` to obtain the physical Xi
band. There is no unrecorded rescaling.

## 2. Finite integration and its Taylor remainder

For indices `n=1,...,11`, the producer integrates from zero to `U_n=c_n/16`,
where

\[
 (c_1,\ldots,c_{11})=(40,29,23,18,14,12,9,7,5,3,2).
\]

There are 162 cells of width `1/16`, with centers `(2k+1)/32` and halfwidth
`1/32`. On each cell the complete density summand is expanded to degree 220.
The exact interval polynomial is then multiplied by `t^j` and integrated
exactly, for every even `j` from zero through 26. The factor two for the full
line is included in `integrate_moment`.

The Cauchy circle around a cell center has radius `1/8`. On every such circle,

\[
 q_n<484,\quad \Re t<21/8,\quad |\Im t|\le1/8.
\]

Because `cos(2 Im t)>0`, the exponential `exp(-q_n exp(2t))` has modulus at
most one. The remaining prefactor has modulus less than `10^16`. This last
bound is deliberately generous: using `e<3`, its first term is at most
`4*484^2*3^12`, and its second at most `6*484*3^7`; their sum is already below
`10^12`.

The ratio of the cell halfwidth to the Cauchy radius is `1/4`, so the Taylor
remainder is at most `10^16 * 4^-221/(1-1/4)`. The total full-line length of all
explicit intervals is `2*162/16=81/4<32`, and `0<=t<=5/2` on them. Consequently
the complete absolute integration error for raw moment `j` is at most

\[
 E_j=\frac{32\cdot10^{16}(5/2)^j}{4^{221}(3/4)}.
\]

This bound is added to both endpoints of the computed raw moment interval.
There is no assumption that the tails of the alternating Taylor coefficients
are numerically small.

## 3. Every omitted time interval

For one retained index, put `U=U_n`, `q=pi*n^2`, `E=exp(2U)`, and
`lambda=2qE-9/2>0`. For `t=U+x`, `x>=0`, positivity and
`exp(2x)>=1+2x` give the full-line tail bound

\[
 2\int_U^\infty t^j\Phi_n(t)\,dt
 \le 8q^2e^{9U/2-qE}
       \sum_{k=0}^{j}\binom jk
       \frac{U^{j-k}k!}{\lambda^{k+1}}.
\]

The producer evaluates and adds all eleven of these bounds, with outward
interval rounding. It checks that every denominator is strictly positive.
Dropping the negative prefactor term is valid because an upper bound on the
positive density is being taken.

## 4. Every omitted theta index

For `n>=12`, the same bound with `U=0` yields

\[
 2\int_0^\infty t^j\Phi_n(t)\,dt
 \le \frac{8\pi^2n^4e^{-\pi n^2}j!}{(2\pi n^2-9/2)^{j+1}}.
\]

The denominator increases with `n`. Consecutive numerators have ratio

\[
 (1+1/n)^4e^{-\pi(2n+1)}<\tfrac12\qquad(n\ge12).
\]

For example `(1+1/n)^4<2`, `pi>3`, and `2n+1>=25` make this inequality
immediate. Summing the geometric majorant gives the complete omitted-index
bound

\[
 \frac{16\pi^2 12^4e^{-144\pi}j!}{(288\pi-9/2)^{j+1}}.
\]

Both time and index tails are nonnegative and therefore enlarge only the
upper raw-moment endpoint.

## 5. Normalization, cumulants, and output

The normalization interval is checked to have a strictly positive lower
endpoint. The producer divides the even raw moments by that normalization,
then divides moment `2r` by `v^r`. Odd moments are exactly zero. Cumulants are
computed by the finite identity

\[
 \kappa_n=\mu_n-
 \sum_{j=1}^{n-1}\binom{n-1}{j-1}\kappa_j\mu_{n-j}.
\]

The recorded cumulant ratios are
`kappa_(2r)(T/sqrt(v))/kappa_(2r)(epsilon)`, where `epsilon` is a fair sign.
Its cumulants are exact integers obtained from its exact moment sequence.
These ratios are just convenient finite coordinates; no infinite-product
representation is assumed.

The output `theta26_source.json` contains all raw moments, variance, normalized
moments, cumulant ratios, and every analytic remainder bound. The first replay
produced SHA-256
`c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf`.
Its thirteen ratio widths run from less than `4.12e-113` to less than
`5.91e-106`. These are directed enclosures of the complete source, rather than
ordinary-precision error estimates.

The backend is inherited, so a replay with it is not independent arithmetic.
The increased index range, time intervals, Taylor degree, all remainder
constants, and the normalization used here are explicit new choices and can
be checked without trusting a source-moment receipt.

## Reproduce

From a checkout containing the pinned inherited source:

```bash
python source26.py --source /path/to/pinned/theta --output theta26_source.json
```

This regenerates the full source. A parameter producer may use midpoint
values to find a candidate; any existence certificate must use the full
intervals instead of those midpoints.
