# L-92913 — The reconstructed one-shot native deficit is below 55000

Claim ID: `L-92913`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM — REVIEW REQUIRED**  
RH status: **unproved**

Let
\[
r_X(q)=\Omega_X(q)-\Xi(d_X)(q)\ge0,
\qquad
\delta_X=\sum_qY_4(q)r_X(q).
\]
The exact radix-four dual gives \(\delta_X=J_\Lambda(X)-\mathcal H(d_X)\).

## 1. Elementary benchmark bound

Chebyshev's binomial argument gives \(\psi(t)\le2(\log2)t\): the central binomial coefficient bounds \(\psi(2u)-\psi(u)\le2u\log2\), and summing the resulting dyadic intervals gives the global estimate. For
\[
f_X(t)=t^{-1/2}\log(X/t),
\]
Stieltjes integration by parts yields
\[
J_\Lambda(X)=\int_{1^-}^X f_X(t)d\psi(t)
\le2\log2\int_1^Xt^{-1/2}
\left(1+\frac12\log\frac Xt\right)dt
<8(\log2)\sqrt X.
\]
Since \(1-\tau_K<130/\sqrt K\), \(K>X/67\), \(\sqrt{67}<33/4\), and \(\log2<7/10\),
\[
\boxed{(1-\tau_K)J_\Lambda(X)<6006.}
\]

## 2. Sparse dual sums

The exact recurrence
\[
Y_4(q)-2\mathbf1_{4\mid q}Y_4(q/4)=\Lambda(q)
\]
implies that \(Y_4\) is supported only on powers of two and numbers \(4^vp^a\) with \(p\) odd prime. Elementary summation gives
\[
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11,
\]
and, with \(L=\log(2X)\),
\[
\sum_{q\le X}\frac{Y_4(q)}q\le3+2L+2L^2.
\]
Consequently the nonterminal comparison costs less than four for \(X\ge10^{12}\), while the terminal comparison costs less than
\[
4452\cdot11=48972.
\]
The bottom width-two and fixed top omission have total literal score below one at \(X\ge10^{12}\). The quantizer is score-favorable.

## 3. No port or base term

Every Hall residual, bonus, causal current and internal child is already a direct nonnegative row. Mismatch is paid by scalar capacity reserve; omissions remove positive source. No colored state completion or Schur complement is invoked, so the actual auxiliary matrix demand is exactly zero. There is no large-endpoint base insertion.

Therefore
\[
\boxed{0\le\delta_X<6006+4+48972+1=54983<55000}
\]
for every integer \(X\ge10^{12}\). No estimate of \(J_\Lambda(X)-4\sqrt X\) is used.
