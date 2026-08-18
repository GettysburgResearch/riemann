# R-98911 — Weyl translation does not preserve the parity observable

Claim ID: `R-98911`  
Status: **PROVED EXACT OPERATOR FIREWALL**  
Created: 2026-08-18  
Frozen target: `L-98703`, Section 3

Let `Pi=(-1)^N` be bosonic parity and `W(h)` a Weyl displacement. Since

\[
 \Pi W(h)\Pi=W(-h),
\]

one obtains

\[
\boxed{W(h)^*\Pi W(h)=W(-2h)\Pi}
\tag{R-98911.1}
\]

up to the conventional scalar Weyl phase; for a real one-mode displacement the
phase is one. This is not equal to `Pi` unless `h=0`.

For the vacuum,

\[
 \langle0|\Pi|0\rangle=1,
 \qquad
 \langle0|W(h)^*\Pi W(h)|0\rangle=e^{-2|h|^2}.
 \tag{R-98911.2}
\]

Thus the statement in `L-98703` that the pole carrier may be removed by a
unitary Weyl translation without changing the trace-free parity matrix
coefficient is false. A valid centering must conjugate and retain the displaced
observable, or subtract an explicitly identified branch contribution. Either
operation changes the object whose heat energy is being bounded.
