# L-100163 — The critical activation endpoint is exactly the factor-67 half-order Harnack sequence

Status: **PROVED EXACT FINITE IDENTITY**  
Created: 2026-08-20  
RH status: **unproved**

Let

\[
M_{1/2}(X)=\sum_{n\le X}{\mu(n)\over\sqrt n}
\]

and

\[
B_\beta(X)=\sum_{n\le X}{\beta(n)\over\sqrt n},
\qquad
\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67).
\]

Reindexing the second term gives exactly

\[
\boxed{
B_\beta(X)
=M_{1/2}(X)-67^{-1/2}M_{1/2}(X/67).
}
\tag{L-100163.1}
\]

Thus the unique half-order endpoint residue isolated by the logarithmic coarea theorem `L-100162` is not a new object. It is precisely the factor-67 Harnack difference of the ordinary half-order Möbius prefix.

Consequently the remaining activation-boundary theorem may be stated discretely: control the one-sided cumulative debt of the sequence `B_beta(N)` at integer activation endpoints strongly enough to imply subpower logarithmic negative mass for the critical centered remainder.

No continuum interpolation, owner graph, Hardy square, or positive completion is hidden in (L-100163.1).
