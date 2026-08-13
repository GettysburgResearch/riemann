# X-91631 — five-level weighted quarter cascade by endpoint/critical-point certification

This standard-library replay certifies the scalar inequality

\[
\sum_{j=0}^{4}2^{-j}D(4^j x)<0
\qquad(1\le x\le67),
\]

where, on `n=floor(x)`,

\[
D(x)=5\sqrt{x}\sum_{m\le n}\frac{\mu(m)}m
-3\sum_{m\le n}\frac{\mu(m)}{\sqrt m}
-\log x\sum_{m\le n}\frac{\Lambda(m)}{\sqrt m}
+\sum_{m\le n}\frac{\Lambda(m)\log m}{\sqrt m}.
\]

On every common cell with endpoints in `4^-4 Z`, the cascade is

\[
\alpha\sqrt{x}+\beta\log x+\gamma.
\]

The checker proves `beta<0` on every cell. Hence any interior critical point is a minimum, so a rigorous upper bound needs only the two one-sided endpoint values. Activated knot values are checked separately. All arithmetic is outward:

- Möbius and prime-power prefixes are exact;
- square roots use integer `isqrt` enclosures;
- logarithms use the `atanh` series with an explicit positive tail;
- fixed-point multiplication and division round outward.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay certifies only the scalar inequality. It does not prove that the weighted cascade is a one-use positive physical endpoint packing, and it does not prove RH.
