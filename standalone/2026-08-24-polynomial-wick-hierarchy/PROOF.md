# Square-root polynomial Wick hierarchy

This standalone proof packet contains the exact algebraic and analytic-model
advance T-105250.

## The central identity

Let
\[
P_K(x)=1-\sum_{j=1}^K
\frac{\binom{2j}{j}}{4^j(2j-1)}x^j.
\]
Because this is the degree-`K` truncation of `sqrt(1-x)`, its omitted tail has
positive absolute coefficients. Hence
\[
\frac{P_K(x)^2}{1-x}
=\left(1+
 \frac{P_K(x)-\sqrt{1-x}}{\sqrt{1-x}}\right)^2
\]
has nonnegative coefficients and no terms of degree `1,...,K`.

The coefficient tail is bounded by
\[
0\le q_{K,m}\le
\left(\frac{\binom{2K}{K}}{4^K}\right)^2,
\]
and becomes equal to the right side for `m>=2K`.

## Stable source coordinate change

For a contraction `x` in any Banach algebra,
\[
\|1-P_K(x)\|\le1-c_K,\qquad
c_K=\binom{2K}{K}4^{-K}.
\]
Thus
\[
\|P_K(x)^{-1}\|\le c_K^{-1}\asymp\sqrt{\pi K}.
\]
The hierarchy is polynomially conditioned, not exponentially conditioned.

## Frozen energy

The prime-simplex degree-`m` energy is `m!/(2m)!`. Therefore
\[
\mathcal D_K
=\sum_{m>K}q_{K,m}^2\frac{m!}{(2m)!}
\le
c_K^4\frac{(K+1)!}{(2K+2)!}
\frac{4K+6}{4K+5}.
\]
This tends to zero superfactorially.

## Proportion consequences

If actual/model trace and HS factors are `tau` and `upsilon`, the exact
full-signature consumer gives
\[
\liminf N_0/N
\ge
\frac{2(\tau/\upsilon)^2}{1+2\mathcal D_K}-1.
\]
At `K=2` and `tau/upsilon=99/101`, this is at least
\[
4997295529/5425779287
=0.9210281628\ldots.
\]

If the transfer is asymptotically lossless for every fixed `K`, then the
right side tends to one as `K` tends to infinity. Hence almost all zeros lie
on the line.

The actual-Xi transfer is not proved in this packet.
