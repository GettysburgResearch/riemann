# R-97200 — An exact finite Euler overshoot refutes closure from the local Julia state alone

Claim ID: `R-97200`  
Status: **PROVED EXACT DIRECTED COUNTEREXAMPLE TO A PROOF MECHANISM**  
Created: 2026-08-18  
RH status: **the full RJTE statement is not refuted**

Take

\[
P=\{3,5,7,11,13\},\qquad N=26.
\]

The finite inverse is

\[
B_P(z)=(1-2^{-z})^2(1-2^{-z-1})\prod_{p\in P}(1-p^{-z}).
\]

Its normalized boundary is

\[
\begin{aligned}
\mathcal B_P(26)={}&2-\frac{11\sqrt2}{8}
-\frac{2\sqrt3}{3}-\frac{2\sqrt5}{5}
-\frac{\sqrt7}{7}-\frac{\sqrt{11}}{11}-\frac{\sqrt{13}}{13}\\
&+\frac{\sqrt{21}}{21}+\frac{\sqrt{15}}{15}
+\frac{5\sqrt{26}}{52}+\frac{5\sqrt{22}}{44}
+\frac{5\sqrt{14}}{28}+\frac{\sqrt{10}}4
+\frac{11\sqrt6}{24}.
\end{aligned}
\]

A 200-bit dyadic radical enclosure proves

\[
\boxed{\mathcal B_P(26)>1.1306169339746402>1.}
\]

Nevertheless this finite Euler system has:

1. positive reciprocal coefficients `g_P`;
2. `|b_P|<=g_P` and a termwise PSD Julia matrix;
3. a nonnegative generalized-prime source;
4. the exact parity-covariant channel swap;
5. the bounded alternating divisor martingale;
6. finite logarithmic energy;
7. positive moment Hankel matrices.

Thus none of those properties, separately or together without a completion boundary, implies RJTE.

The unit-normalized Schur matrix

\[
\begin{pmatrix}1&\mathcal B_P(26)\\\mathcal B_P(26)&1\end{pmatrix}
\]

has negative determinant, while the genuine cumulative Julia moment matrix remains PSD. This is an exact SDP separation between local passivity and the missing boundary normalization.

The counterexample does **not** show that the completed all-prime boundary exceeds one. It proves that the unprocessed-prime completion port is mathematically load-bearing.
