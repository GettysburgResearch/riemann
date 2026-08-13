# L-91414 — The finite forcing diagonal modes match the two rough renewal kernels

Claim ID: `L-91414`  
Status: **PROVED EXACT RENEWAL INTERFACE**  
Created: 2026-08-13  
RH status: **unproved**

Retain

\[
U_2=L=2X-Y,
\qquad
U_1=R=X-Y.
\]

The exact delayed renewal of `L-91113` is

\[
F_a^{(53)}(x)=\sum_{m\in\mathcal M_{59}}m^{-1/2}U_a(x/m),
\qquad a=1,2.
\]

Subtracting gives

\[
\boxed{
F_2^{(53)}-F_1^{(53)}
=\sum_m m^{-1/2}X(x/m).
}
\]

Taking `F_2-2F_1` gives

\[
\boxed{
F_2^{(53)}-2F_1^{(53)}
=\sum_m m^{-1/2}Y(x/m).
}
\]

Because `X(x)=sqrt(x)B(x)`, the effective rough kernel in the first identity is
`m^-1`; the second kernel is `m^-1/2`. Their Euler survival factors are exactly

\[
1-p^{-1},
\qquad
1-p^{-1/2}.
\]

These are the two mode laws used by `L-91335/L-91336` and coupled in
`L-91411`. Thus the regeneration mechanism is the normalized Euler
decomposition of the actual delayed renewal, not an unrelated state model.

```text
finite forcing renewal                 EXACT
mode kernels m^-1 and m^-1/2           EXACT
Euler survival factors                 EXACT
coupling interface                     EXACT
finite physical producer               SEPARATE
Riemann Hypothesis                      UNPROVED
```
