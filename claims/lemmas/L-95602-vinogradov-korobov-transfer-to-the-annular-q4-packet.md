# L-95602 — The classical Vinogradov–Korobov bound transfers exactly to the annular Q4 packet

Claim ID: `L-95602`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TRANSFER — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: exact ten-band kernels of PR #580

Use the classical consequence of the Vinogradov–Korobov zero-free region

\[
M(x)
\ll
x\exp\!\left[
-c(\log x)^{3/5}(\log\log x)^{-1/5}
\right].
\tag{L-95602.1}
\]

The exact identity

\[
M_o(x)=\sum_{j\ge0}M(x/2^j)
\]

gives the same form for the odd Mertens state, with a possibly smaller
constant.

Applying bandwise partial summation with the exact bounds

\[
|G_X(t)|\ll\frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\ll\frac{\log(2X)}{X^{3/2}},
\]

yields

\[
\boxed{
|\mathcal A(X)|
\ll
\sqrt X\,\log(2X)
\exp\!\left[
-c_1(\log X)^{3/5}(\log\log X)^{-1/5}
\right].
}
\tag{L-95602.2}
\]

Consequently

\[
\boxed{
\mathcal S_H(X)
\ll_B
X\log^2(2X)
\exp\!\left[
-2c_1(\log X)^{3/5}(\log\log X)^{-1/5}
\right]
+
\log^{B+2}(2X).
}
\tag{L-95602.3}
\]

This is a genuine unconditional improvement over a source-blind
\(O(X\,\mathrm{polylog}\,X)\) estimate. It remains \(X^{1-o(1)}\), not
\(X^{o(1)}\), and therefore does not prove UOSACF or RH.


---
