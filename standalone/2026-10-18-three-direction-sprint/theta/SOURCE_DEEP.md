# Isolated complete theta source for higher finite orders

**Status: PROPOSED directed arithmetic source enclosure.** This changes
precision and quadrature parameters in separate files. It does not alter
the already executed degree22,24 or26 certificate identities, and it is
not an independent arithmetic implementation.

primitive512.py is the pinned #994 integer interval primitive, whose
ancestor SHA256 is
`2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55`.
Only the executable constants change: `BITS=512` and `DEGREE=180`.
The same exact Machin arctangent enclosure, positive exponential series
with explicit remainder, repeated interval squaring, integer outward
rounding and Taylor coefficient recurrence are used. The unchanged96-term
arctangent and exponential remainders remain included at the new precision;
they are never silently replaced by512-bit accuracy claims.

source_deep.py uses seven explicit theta indices, cell half-width`1/32`,
and cell counts

```text
(36,24,16,12,8,6,4),
```

so the respective cutoffs are `(9/4,3/2,1,3/4,1/2,3/8,1/4)` and there are
106 cells. Each requested moment list is finite; the implementation
accepts even maximum degrees through64. The proof below applies to each
such list. It retains the entire time range and all theta indices.

## Uniform Taylor remainder

The `n`th half-line density summand is

\[
 g_n(t)=(4q_n^2 e^{9t/2}-6q_n e^{5t/2})e^{-q_ne^{2t}},
 \qquad q_n=\pi n^2.
\]

On a complex circle of radius`1/8` about any cell center, one has
`|Im t|<=1/8` and `Re t<=75/32`. Thus
`Re(e^(2t))=e^(2Re t) cos(2Im t)>0`; the last exponential has modulus
at most1. For `n<=7`, `q_n<196`, so `e<3` gives

\[
 |g_n(t)|\le4\cdot196^2\cdot3^{11}
                  +6\cdot196\cdot3^6<10^{11}. \tag{1}
\]

The strict exponent bounds used here are
`(9/2)(75/32)=675/64<11` and `(5/2)(75/32)<6`.
The cell radius ratio is`(1/32)/(1/8)=1/4`. Cauchy's formula therefore
bounds the density Taylor remainder after degree180, uniformly on the
real cell, by `10^11 4^(-181)/(1-1/4)`.

For the `j`th raw moment, `0<=t<=9/4` supplies multiplier`(9/4)^j`.
Twice the sum of all positive integration lengths is`53/4<16`. Hence the
complete two-sided Taylor error is bounded by

\[
 E_j=\frac{16\cdot10^{11}(9/4)^j}{4^{181}(3/4)}. \tag{2}
\]

The exact finite polynomial product with`t^j` is integrated through its
full degree; it is not truncated again at180.

## Complete positive time and index tails

Every `g_n(t)` is positive on`t>=0`, since `q_n>3`. Dropping its negative
prefactor term and using `e^(2(U+x))>=e^(2U)(1+2x)` gives, with
`lambda_n=2q_n e^(2U)-9/2>0`,

\[
 2\int_U^\infty t^j g_n(t)\,dt
 \le8q_n^2e^{9U/2-q_ne^{2U}}
    \sum_{k=0}^j\binom jk U^{j-k}\frac{k!}{\lambda_n^{k+1}}. \tag{3}
\]

This is applied at each of the seven actual cutoffs, with directed
exponential evaluations.

For all omitted indices`n>=8`, the same exponential inequality at`U=0`
gives a bound involving
`8pi^2 n^4 e^(-pi n^2) j!/(2pi n^2-9/2)^(j+1)`.
The ratio of consecutive terms is at most

\[
 (9/8)^4e^{-17\pi}<(9/8)^4e^{-51}<1/2,
\]

and the denominator only decreases that ratio further. Summing the
geometric majorant therefore gives the **full** omitted-index bound

\[
 16\pi^2 8^4e^{-64\pi}
       \frac{j!}{(128\pi-9/2)^{j+1}}. \tag{4}
\]

The checker subtracts (2) from the finite cell sum for the lower endpoint,
and adds (2)--(4) for the upper endpoint. It then divides by its freshly
enclosed positive normalization and standardizes by its freshly enclosed
positive variance. Moment/cumulant operations use the same outward
interval arithmetic at every stage. Each remainder component is retained
in the source receipt.

This source receipt is a reusable enclosure, not a proof of any finite
model's feasibility. A final existence verifier must reconstruct it
afresh or independently verify all of its input enclosures and tails.

```text
python standalone/2026-10-18-three-direction-sprint/theta/source_deep.py --degree 32 --emit standalone/2026-10-18-three-direction-sprint/theta/source_deep32.json
```

The executed degree32 reconstruction completed in52.0984 seconds. Its
canonical JSON with one LF newline SHA256 is
`db7bdbfea207f37a4baca6cad03df0c0f51052caa6ef5f47e00e07e37b41711e`;
its actual Windows CRLF file-byte SHA256 is
`89903a63d27cd7fac0e023edfc685ef409f8172379e57f4b75082490c93850d3`.
Input-file hashes recorded inside the receipt use actual file bytes.
