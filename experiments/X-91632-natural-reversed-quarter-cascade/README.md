# X-91632 — natural parent-to-child five-level quarter cascade

This exact directed replay certifies

\[
D(256x)+\frac12D(64x)+\frac14D(16x)+\frac18D(4x)+\frac1{16}D(x)<0
\]

for every `1<=x<=67`. Equivalently,

\[
\sum_{j=0}^{4}2^{j-4}D(4^jx)<0.
\]

This orientation matches four successive factor-four affine lifts: a row at scale `4^j x` lifted to the top scale `256x` carries coefficient `2^{j-4}`.

The arithmetic and interval method are identical to `X-91631`:

- exact Möbius and prime-power prefixes;
- integer-isqrt square-root enclosures;
- atanh logarithm series with explicit positive tail;
- outward fixed-point arithmetic;
- both one-sided endpoints of every common cell and all activated knots.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay certifies only the scalar sign. It does not by itself prove that all five rows can be embedded into one physical parent capacity without duplication, and it does not prove RH.
