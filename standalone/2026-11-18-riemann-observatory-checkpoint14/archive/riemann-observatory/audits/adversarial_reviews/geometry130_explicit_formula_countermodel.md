# A smooth test with divergent height-ordered spectral sum

The printed Bombieri–Lagarias author manuscript, pp. 5–6, imposes piecewise \(C^1\) regularity with finitely many first-kind jumps and, for some \(\delta>0\), \(f(x)=O(x^\delta)\) at zero and \(f(x)=O(x^{-1-\delta})\) at infinity. It claims its explicit formula with the zero side ordered by \(|\Im\rho|\le T\). I construct a real \(C^\infty\) function satisfying the literal conditions for any prescribed \(\delta>0\), for which that height-ordered sum fails the Cauchy criterion. The construction uses the actual zeta zeros and the unconditional Riemann–von Mangoldt count. All right-side terms of the claimed formula are absolutely defined. This is an explicit existence construction with an inductively chosen sequence of frequencies. [Pinned author manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf) · [Earlier citation-hypothesis check](geometry127_bombieri_lagarias_adjudication_input.md)

## Log-coordinate packets

Fix a nonnegative \(\psi\in C_c^\infty((-1/8,1/8))\) with \(\int\psi=1\). For \(j=1,2,\ldots\), put \(a_j=e^{-(1/2+\delta)j}\), \(b_j=e^{-(1+\delta)j}\), and choose positive centers \(\Gamma_j\) as below. For \(x=e^t\) define
\[
 F(t)=\sum_{j\ge1}a_j\psi(t-j)\cos(\Gamma_jt),
 \qquad f(x)=x^{-1/2}F(\log x).
\]
The supports in \(t\) are pairwise disjoint and locally finite. Therefore \(f\) is real and smooth, vanishes on a neighborhood of \([0,1]\), and obeys the required \(O(x^{-1-\delta})\) bound at infinity. No additional phase is needed in the packets because the zero windows below have width \(O(1/j)\).

For \(0\le\beta\le1\) define
\[
 H_j(\beta,v)=a_j\int_{\mathbb R}\psi(t-j)e^{(\beta-1/2)t}e^{ivt}\,dt .
\]
Compact support and repeated integration by parts give, for each fixed \(j\) and \(A\ge1\),
\[
 \sup_{0\le\beta\le1}|H_j(\beta,v)|\ll_{j,A}(1+|v|)^{-A}.
\]
The constant is uniform in \(\beta\) and independent of the chosen carrier frequency. With \(\widehat f(s)=\int_0^\infty f(x)x^{s-1}\,dx\), the contribution of packet \(j\) at \(s=\beta+i\gamma\) is
\[
 G_j(\beta,\gamma)=
 \tfrac12\bigl(H_j(\beta,\gamma-\Gamma_j)+H_j(\beta,\gamma+\Gamma_j)\bigr).
\]
The Mellin integral is absolutely convergent, with the packet integrals summable uniformly for \(\beta\in[0,1]\) and all \(\gamma\), since the absolute integral of each original packet is \(O(e^{-\delta j})\). Thus \(\widehat f(\beta+i\gamma)=\sum_j G_j(\beta,\gamma)\) with legitimate pointwise summation.

Let \(w_j=1/(20j)\). If \(|\gamma-\Gamma_j|\le w_j\), then on the support of \(\psi(t-j)\) one has \(|(\gamma-\Gamma_j)t|\le9/160\) and \(e^{(\beta-1/2)t}\ge e^{-j/2-1/16}\). Hence the resonant half of the new packet satisfies
\[
 \Re\bigl(\tfrac12H_j(\beta,\gamma-\Gamma_j)\bigr)
 \ge \tfrac12 e^{-1/16}\cos(9/160)\,b_j
 > b_j/3
\]
uniformly for \(0\le\beta\le1\). Its other half is small at large \(\Gamma_j\) by the uniform Fourier estimate.

## Induction with simultaneous control of earlier and later packets

At step \(j\), the earlier centers and closed zero windows \(I_i\), \(i<j\), have been chosen. First choose a sufficiently large threshold \(T_0\) such that *every* candidate center \(\Gamma_j\ge T_0\) satisfies the following conditions.

1. On \(|\gamma-\Gamma_j|\le w_j\), the nonresonant half \(\tfrac12H_j(\beta,\gamma+\Gamma_j)\) has modulus at most \(b_j/24\), and the sum of the absolute values of the \(j-1\) old packet contributions is at most \(b_j/24\).
2. On each of the already fixed windows \(\gamma\in I_i\), the contribution of packet \(j\) has modulus at most \(2^{-(j-i)}b_i/24\).
3. The candidate window lies above every earlier window.

Each requirement is uniform over \(0\le\beta\le1\). The first two follow from the integration-by-parts estimate and a finite number of constraints. For an old packet at the candidate new window, both offsets tend to infinity with \(\Gamma_j\). For the candidate new packet at a fixed old window, the same is true. This construction deals with the future packets before taking the final sum, without assuming their unweighted geometric decay beats the resonant amplitude.

The unconditional Riemann–von Mangoldt count, with multiplicity, gives \(\gg T\log T\) positive ordinates in \([T,2T]\) for large \(T\). Divide that interval into \(m=\lceil T/(2w_j)\rceil\) equal cells. At least one cell contains \(\gg w_j\log T\) zeros with multiplicity. Choose \(T\) arbitrarily large so that this number is at least \(j/b_j\), and \(T>T_0+1\). Endpoints can be chosen to avoid zero ordinates without changing the shrinking scale or count estimate. In detail, exclude the countable set of numbers \(T=\gamma/(1+\ell/m)\) as \(m\) and \(\ell=0,\ldots,m\) range over the integers and \(\gamma\) over positive zero ordinates. For any remaining large \(T\), no partition endpoint is a zero. Choose \(I_j=[A_j,B_j]\) to be the successful cell and \(\Gamma_j\) its midpoint. The radius of \(I_j\) is at most \(w_j\), and the already imposed inequalities apply. [Classical zero-count source, §9.4](../../sources/selberg_round2/titchmarsh_zeta.pdf)

At any later step \(\ell>j\), condition 2 controls the effect on \(I_j\). Summing the resulting geometric series bounds all future contributions there by \(b_j/24\). Hence for the final function and all \(\gamma\in I_j\),
\[
 \Re\widehat f(\beta+i\gamma)
 > \left(\tfrac13-\tfrac3{24}\right)b_j
 > b_j/5
 \qquad(0\le\beta\le1).
\]
This sign bound does not use RH or restrict the distribution of the real parts of the zeros.

## Failure of the claimed limit and survival of the compact-test use

Write \(S(T)=\sum_{|\Im\rho|\le T}\widehat f(\rho)\), counting the nontrivial zeros with multiplicity. Each fixed sum is finite. Conjugation of the zeros and reality of \(f\) give
\[
 S(B_j)-S(A_j)
 =2\sum_{A_j<\Im\rho<B_j}\Re\widehat f(\rho)
 > \tfrac25\,j .
\]
The endpoints are not ordinates, so no half-value convention affects this difference. The intervals escape to infinity, which contradicts the Cauchy criterion. Any bounded initial set of zero heights would cancel in this difference.

The two smooth integrals on the claimed right side converge absolutely, as does the prime sum since \(\widetilde f(n)=0\) for \(n\ge1\) and \(\Lambda(n)|f(n)|\ll(\log n)n^{-1-\delta}\). The local archimedean issue vanishes because \(f,\widetilde f\) are both zero near \(1\) and \(f(1)=0\). For large \(x\), \(\widetilde f(x)=0\) and the remaining weight times \(f(x)\) is integrable. Thus failure occurs in exactly the height-symmetric zero sum asserted by the printed general formula. The counterexample is for the pinned author manuscript's literal broad test class. It does not concern the cited Weil theorem under its stronger derivative-decay condition, the compact truncated tests used for Theorem 2, or the multiset Theorem 1. No canonical record or author flag was changed. [Weil condition (B), transcription p. 6](https://denisevellachemla.eu/transc-Weil-1952.pdf)
