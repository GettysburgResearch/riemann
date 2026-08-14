# L-92206 — Adjacent log-convexity controls every two-by-two principal Hankel minor

Claim ID: `L-92206`  
Status: **PROVED ELEMENTARY SEQUENCE LEMMA**  
Created: 2026-08-14  
Depends on: none  
RH status: **unproved**

Let `a_1,...,a_M` be positive and suppose

\[
 a_k a_{k+2}\ge a_{k+1}^2
 \qquad(1\le k\le M-2).
\]

Then the ratios

\[
 r_k=\frac{a_{k+1}}{a_k}
\]

are nondecreasing.  Consequently, for every `i<j`,

\[
\boxed{
 a_i a_{2j-i}\ge a_j^2
 }
\]

whenever the displayed indices are available.  More generally, every
`2x2` minor of the Hankel sequence with ordered row and column indices has
the sign forced by ratio monotonicity.

For the third-order Xi Hankel matrix

\[
 \begin{pmatrix}
 A_1&A_2&A_3\\
 A_2&A_3&A_4\\
 A_3&A_4&A_5
 \end{pmatrix},
\]

positivity of the adjacent minors at `m=1,2,3` implies

\[
 A_1A_5-A_3^2\ge0.
\]

Thus `L-92203` supplies every proper principal minor required by
`T-92202`; only the full determinant remains.
