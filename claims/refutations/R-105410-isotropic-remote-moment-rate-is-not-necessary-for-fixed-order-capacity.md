# R-105410 — The isotropic remote-moment rate is not necessary at fixed matrix order

Claim ID: `R-105410`  
Status: **PROVED EXACT SCOPE SEPARATOR**  
Created: 2026-08-24  
Depends on: `L-105400`, `L-105411`  
RH status: **not assumed**

`RTMH105400(k)` used the sufficient condition

\[
\max_{0\le n\le2k-1}|\Delta_n|
=o(J^{-d_k}),
\qquad
d_k=3k(k-1)+4.
\]

This common rate is not the natural fixed-order condition.

Choose `1<B<d_k` and put

\[
\sigma_J
=J^{-B}\delta_{J^{-2B}}.
\]

Then

\[
\Delta_n(\sigma_J)
=J^{-B(2n+1)}.
\]

The zeroth moment violates the old rate:

\[
J^{d_k}\Delta_0
=J^{d_k-B}\longrightarrow\infty.
\]

But every naturally graded moment from `L-105411` vanishes:

\[
\boxed{
J^{2n+1}\Delta_n
=
J^{-(B-1)(2n+1)}
\longrightarrow0.
}
\]

Equivalently, after the exact tail congruence the complete moment-matrix perturbation tends to zero.

Thus

```text
old common J^(-d_k) rate       sufficient but overstrong;
graded J^(-(2n+1)) rate        scale invariant;
complete Xi tail               may also be handled by endpoint compactness.
```

This is an abstract signed-measure separator. It does not prove the Xi tail estimate or any residue sign.
