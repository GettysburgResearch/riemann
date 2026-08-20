# L-99942 — Critical negative mass is exactly the weighted downward variation of the positive quadratic normalization

Claim ID: `L-99942`  
Status: **PROVED EXACT MEASURE IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99940`  
RH status: **not assumed**

Write `G_2^ac` for the absolutely continuous part of `G_2`. From
`L-99940`,

\[
dG_2^{ac}(u)=3e^{-u}\mathfrak H_1(e^u)\,du.
\]

Therefore, for every `X>=1`,

\[
\boxed{
3\int_1^X(\mathfrak H_1(x))_-\frac{dx}{x}
=\int_{[0,\log X]}e^u\,d(-G_2^{ac})_+(u).
}
\tag{L-99942.1}
\]

This is an equality, not a comparison.

The right side is a **critically weighted** downward variation. Ordinary total
variation of `G_2` does not control it, because the weight is `e^u`.
