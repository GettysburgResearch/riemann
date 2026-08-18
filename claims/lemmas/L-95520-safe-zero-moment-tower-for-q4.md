# L-95520 — A polylog-stable zero-moment tower for the annular Q4 packet

Claim ID: `L-95520`  
Status: **PROVED EXACT OPERATOR THEOREM**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400`  
RH status: **not assumed**

Let

\[
 (SF)(X)=F(X/2)
\]

and let `mathcal A` be the factor-1024 annular Q4 observation of PR #580. For
an integer `M>=1`, define

\[
 \boxed{\mathcal A^{[M]}=(I-S)^M\mathcal A.}
\tag{L-95520.1}
\]

## Mellin safety

Endpoint halving has Mellin multiplier `2^{-z}`. Therefore

\[
 \widehat{\mathcal A^{[M]}}(z)
 =(1-2^{-z})^M\widehat{\mathcal A}(z).
\tag{L-95520.2}
\]

Every added zero lies on `Re z=0`; no conclusion-producing pole in `Re z>0`
is cancelled.

## Exact inverse and polylog equivalence

On endpoint functions extended by zero below `1`,

\[
 \boxed{
 (I-S)^{-M}=
 \sum_{j\ge0}\binom{M+j-1}{M-1}S^j.
 }
\tag{L-95520.3}
\]

At a fixed endpoint `X`, the sum terminates at `j<=log_2 X`. Hence its total
coefficient mass is

\[
 \sum_{j\le\log_2X}\binom{M+j-1}{M-1}
 =\binom{M+\lfloor\log_2X\rfloor}{M}
 =O_M((\log X)^M).
\tag{L-95520.4}
\]

Consequently

\[
 \boxed{
 \mathcal A^{[M]}(X)=O((\log X)^C)
 \iff
 \mathcal A(X)=O((\log X)^{C'})
 }
\tag{L-95520.5}
\]

for some fixed exponents `C,C'` differing by at most `M`.

## Moment cancellation

If `phi(u)=J(e^{-u})` is either logarithmic-coordinate annular kernel, then
`(I-S)^M` multiplies its Mellin transform by a function with a zero of order
`M` at `z=0`. Therefore the transformed kernel satisfies

\[
 \boxed{
 \int u^k\phi^{[M]}(u)\,du=0,
 \qquad 0\le k<M.
 }
\tag{L-95520.6}
\]

Thus the Q4 route admits arbitrarily many exact low-frequency moments without
changing its conclusion-producing strength, at only a fixed polylogarithmic
inverse cost.
