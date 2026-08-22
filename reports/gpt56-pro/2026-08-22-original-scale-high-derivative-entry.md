# Original-scale high-derivative entry — GBOX104500 closed

The fixed-scaled Ki cosine limit was not the end of the high-derivative story.
The classical Xi Fourier kernel supplies a stronger original-scale theorem.

For

\[
d\nu_n(u)=Z_n^{-1}u^{2n}\Phi(u)du,
\]

the tilted frequency has a saddle `w_n~(1/2)log n` and absolute width

\[
\sigma_n\asymp\sqrt{w_n/n}\to0.
\]

Thus, uniformly on every fixed complex rectangle,

\[
{(-1)^n\Xi^{(2n)}(z)\over(-1)^n\Xi^{(2n)}(0)}
=\cos(w_nz)+o(1)e^{w_n|Im z|}.
\]

A cellwise Rouché argument around all `O(T w_n)` cosine zeros in a fixed
original-height rectangle proves that every derivative zero there is real and
simple for all sufficiently large `n`.

This closes `GBOX104500` unconditionally.  The reverse-Rolle programme is now
reduced to one exact integer-valued theorem:

```text
RPCH104501:
  cumulative wrong-extremum + endpoint + winding charge <2.
```

The exact transport identity then forces the off-real Xi zero count to be the
nonnegative even integer below two, hence zero.  RH remains unproved because
`RPCH104501` remains open.
