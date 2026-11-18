# Independent adversarial check of absolute sampling at the critical logarithmic endpoint

The random-sign construction works. There exists a real smooth value-decaying test with finite whole-strip norm at \(p=3\) and divergent absolute evaluation on the actual zeta zeros. In fact divergence occurs almost surely for the specified independent signs. This proves failure of the unconditional absolute-sampling assertion at that endpoint. It gives no conclusion about the raw **signed** symmetric height limit or the validity of an endpoint explicit formula with that limit. [Construction audited](weighted138_critical_endpoint_campaign.md) · [Sufficient critical class](analytic135_critical_log_mellin_repair.md)

## Deterministic test and whole-strip norm

Use \(-1/4\le\beta\le5/4\), and fix nonnegative \(\psi\in C_c^\infty((-1/8,1/8))\) with integral one. Take disjoint dyadic-exponent ranges \([L_j,U_j]\) with \(L_{j+1}\ge U_j+3\) and
\[
 S_j=\sum_{r=L_j}^{U_j}\frac1r\ge e^{4j}.
\]
For any lower limit, a finite upper limit exists by harmonic divergence. The carrier set is the finite integer interval \(\mathcal C_j=[2^{L_j},2^{U_j+1}]\cap\mathbb Z\). With \(\lambda_j=e^{j/2}/S_j\), put
\[
 a_{j,n}=\frac{\lambda_j}{n(\log n)^2},\qquad
 F(u)=\sum_j\psi(u-j)\sum_{n\in\mathcal C_j}\varepsilon_{j,n}a_{j,n}\cos(nu),
 \qquad f(x)=x^{-1/2}F(\log x).
\]
For any choices of signs the support translates are locally finite and each inner sum is finite. Thus \(f\) is real and smooth on the open positive half-line. Summability of \(1/(n\log^2 n)\) gives a physical packet envelope \(O(\lambda_j)=O(e^{-7j/2})\). Multiplying by \(e^{-u/2}\) yields \(f(x)=O(x^{-4})\) at infinity. The function vanishes near zero and one. In particular it satisfies the manuscript's literal (A)–(B) and the Mellin integral defines the transform throughout the closed excess strip. Derivatives need only be locally bounded and may grow on distant packets.

Let \(w(t)=\langle t\rangle\log^3(e+|t|)\), \(m=w^{1/2}\), and \(J_\beta(v)=\int\psi(u)e^{(\beta-1/2)u}e^{ivu}du\). Compact support and integration by parts give Schwartz decay uniformly in the entire real strip of \(\beta\). Moderation gives
\[
 m(t)|J_\beta(t-\nu)|\le C_A m(\nu)(1+|t-\nu|)^{-A}.
\]
For any finite sequence \(b_\nu\) indexed by integers, let \(g(t)=(1+|t|)^{-A}\) for \(A>1\). The square of the sum of the absolute translated envelopes is at most
\[
 \left(\sum_\nu g(t-\nu)\right)
 \left(\sum_\nu |b_\nu|^2m(\nu)^2 g(t-\nu)\right).
\]
The first factor is uniformly bounded and the second integrates to \(\|g\|_1\sum_\nu |b_\nu|^2w(\nu)\). This is a deterministic bound, uniform in the size and position of a carrier block, the modulation signs, and the harmless phases of the physical shift. Apply it to the two distinct signed carriers \(\nu=\pm n\) for every \(n\in\mathcal C_j\). It accounts for their paired use without supposing the two signs of one cosine to be independent.

For each \(j\), \(\sum_{n\in\mathcal C_j} w(n)a_{j,n}^2\ll\lambda_j^2 S_j\). This follows shell by shell from \(w(n)\asymp n\log^3 n\) and \(\sum_{2^r\le n<2^{r+1}}1/(n\log n)\ll 1/r\). The single extra upper-end carrier costs no more than the last shell. The physical translation contributes at most \(e^{3j/4}\) over the entire strip, so the weighted whole-strip packet norm is bounded by
\[
 C e^{3j/4}\lambda_j\sqrt{S_j}
 = C e^{5j/4}/\sqrt{S_j}\le C e^{-3j/4}.
\]
The sum of these norms is finite. Triangle inequality across the blocks suffices and needs no interblock orthogonality. The Mellin series itself is absolutely convergent uniformly for \(\beta\) in the strip and \(t\in\mathbb R\), since the physical factor is bounded by \(e^{3j/4}\) and \(\sum_n a_{j,n}\ll\lambda_j\). Therefore the weighted \(L^2\) limit agrees with the Mellin integral, including at every specific zero. There is no assumption about an exceptional or generic vertical trace.

## The actual-zero lower bound is probabilistic, not pointwise cancellation control

For a zero \(\rho=\beta+i\gamma\) in a shell \(2^r<\gamma\le2^{r+1}\) with \(r\in[L_j,U_j]\), take the integer \(n\) nearest to \(\gamma\). Then \(n\in\mathcal C_j\) even at the upper shell boundary, and \(|\gamma-n|\le1/2\). In the Mellin coefficient of this unsigned single carrier, the resonant term is
\[
 \frac12 a_{j,n}e^{(\beta-1/2)j}
      e^{i(\gamma-n)j}J_\beta(\gamma-n).
\]
The real part of \(J_\beta(v)\) is bounded below by a fixed positive constant on \(|v|\le1/2\), uniformly on \(0\le\beta\le1\), since the real cosine is uniformly positive on the bump. The external factor \(e^{i(\gamma-n)j}\) need not be close to 1. Only the **modulus** is lower bounded, which is sufficient. The second term of the same carrier has factor \(J_\beta(\gamma+n)=O_A((\gamma+n)^{-A})\), so the difference estimate for moduli is uniform even after the shift phase. By taking all initial exponents large the resulting unsigned coefficient satisfies
\[
 |b_{j,n}(\rho)|\gg e^{-j/2}\lambda_j/(2^r r^2).
\]
No dominance is required against the other carriers, and \(\beta\) may vary with every zero.

On the countable product of independent symmetric signs, set \(Z_\rho=\sum_{j,n}\varepsilon_{j,n}b_{j,n}(\rho)\) and \(V_\rho=\sum_{j,n}|b_{j,n}(\rho)|^2\). For a finite complex Rademacher series, exact pairing yields
\[
 \mathbb E|Z_\rho|^2=V_\rho,qquad
 \mathbb E|Z_\rho|^4
 =2V_\rho^2+\left|\sum b_{j,n}(\rho)^2\right|^2-2\sum|b_{j,n}(\rho)|^4
 \le3V_\rho^2.
\]
The infinite-series identities follow by the deterministic absolute bound from the physical envelope. Hölder, or Paley–Zygmund for \(|Z_\rho|^2\), gives \(\mathbb E|Z_\rho|\gg\sqrt{V_\rho}\). Hence one matching coefficient suffices in each shell. Riemann–von Mangoldt gives \(\gg2^r r\) zeros in the whole shell with multiplicities. Summing the individual expectations over it yields \(\gg e^{-j/2}\lambda_j/r\). Summing the shells of the block costs \(S_j\), giving expectation bounded below by a positive constant on every block. This argument uses no short-window count or information about the real parts.

## From expectation to an actual divergent trace

For the finite nonnegative height sum \(X_T=\sum_{0<\Im\rho\le T}|Z_\rho|\), each evaluation is a measurable limit of finite signed sums and is bounded by the deterministic envelope. Thus \(X_T\) has finite second moment. Minkowski and the preceding per-zero estimates give
\[
 \|X_T\|_2\le\sum_{0<\Im\rho\le T}\sqrt{V_\rho}
 \le C\mathbb E X_T
\]
with a common constant. Paley–Zygmund gives \(\mathbb P(X_T\ge\mathbb E X_T/2)\ge c>0\) when the mean is positive. The expected finite sums tend to infinity as the disjoint successive blocks are included. Given any threshold \(B\), choose a finite \(T\) with \(\mathbb E X_T>2B\). Monotonicity yields \(\mathbb P(X_\infty>B)\ge c\), and continuity of probability on decreasing threshold events gives \(\mathbb P(X_\infty=\infty)\ge c\). This is an actual existence conclusion. Infinite expectation alone would not have sufficed.

In fact the divergence event is unchanged by changing finitely many signs. Such a change adds finitely many smooth compact log profiles with rapidly decreasing Mellin transforms on \(0\le\Re s\le1\), and hence finite absolute trace by the unit-height count. Enumerate all signs in a sequence. For any finite initial segment, replace its signs by fixed constants, obtaining a tail-dependent measurable version of the same event. The event belongs to the tail sigma-field, so Kolmogorov's zero–one law gives probability one. The original construction needs only positive probability.

All ordinary arithmetic terms are finite for every realization by value decay and vanishing near 1. The counterexample therefore establishes genuine failure of absolute sampling at \(p=3\) rather than just a divergent Cauchy–Schwarz majorant. It makes no inference about cancellation among signed conjugate-height increments, an endpoint Dini theorem for general tests, or publication priority. No canonical files were changed.
