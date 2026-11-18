# Independent reconstruction of the Proposition 22 far-field term

Reviewer rt_repair_62, 2026-11-17. Primary source **PAPER-S004**, [Rodgers–Tao, arXiv:1801.05914v5](https://arxiv.org/pdf/1801.05914v5), cached at sources/spectral/rodgerstao.pdf. This checks the fixed-time \(X_4\) estimate on pp. 49–50 and its classical counterpart on p. 50. The source inputs are (43)–(44) on p. 21, Corollary 10 (50) on p. 23, the principal value in Theorem 11 (56) on p. 27, renormalization (62)–(63) on p. 39, and the weight and nearby relation on pp. 41–42. I visually checked the formulas on pp. 46 and 49–50.

## Available energy bound

Write \(L=\log T\), \(N=TL\), \(w(k)=(1+|k|/N)^{-100}\), and \(k\sim i\) for \(0<|k-i|<(T^2+|k|+|i|)^{1/10}\). All indices range over \(\mathbb Z^*\). The points \(x_k\) are strictly increasing and odd, and \(x_k-\xi_k=O(\log(2+|k|))\) by (50), uniformly in the source time range. The classical configuration satisfies the same hypotheses. Set \(M=TL^3+\widetilde E_T\).

For \(a=|x_k-x_j|\), \(b=|\xi_k-\xi_j|\), \(r=a/b\), (62) and nonnegativity give \(r^{-2}\ll1+V(r)\) by considering \(r\le1/2\) and \(r>1/2\). Thus \(a^{-2}\ll b^{-2}+\widetilde E_{jk}\). From (43)–(44), \(\sum_{j\ne k} b^{-2}\ll\log^2(2+|k|)\). Indeed, for \(|j|\le2|k|\) sum \(\log^2(2+|k|)/|j-k|^2\), and for \(|j|>2|k|\) sum \(\log^2(2+|j|)/j^2\). Since \(\sum_k w(k)\log^2(2+|k|)\ll NL^2\) by dyadic summation,
\[
 S_2=\sum_{j\ne k}w(j)w(k)(x_k-x_j)^{-2}\ll M.
\]
This uses the defining energy directly. The discussion after (67) gives finite energy almost everywhere, as required for the application.

## Uniform bounds and principal values

Put \(A_k=\sum_{i\ne k,\ i\not\sim k}'(x_k-x_i)^{-1}\). For a far pair, write \(U=T^2+|i|+|k|\), \(H=\log(2+|i|+|k|)\). By (44) and (50) the displacement error relative to the classical separation is \(O(H^2/|i-k|)=O(\log^2 U/U^{1/10})=o_T(1)\) uniformly. Hence
\[
 |x_k-x_i|\asymp |i-k|/H,\qquad
 \left|\frac1{x_k-x_i}-\frac1{\xi_k-\xi_i}\right|
 \ll H^3/|i-k|^2. \tag{1}
\]
The reciprocal difference is absolutely summable for fixed \(T,k\).

Let \(D_k=(T^2+|k|)^{1/10}\). A nearby distance \(d=|i-k|\) satisfies \(d^{10}<T^2+2|k|+d\), so \(d\ll D_k\) by absorbing \(d\) on the left for \(d\ge2\). With a sufficiently large fixed \(C\), set \(H_k=C(|k|+D_k)\). Both signs of all indices above \(H_k\) in absolute value are far. Equations (43), (50) imply \(|x_k|/|x_i|\le 1/2\) there, since the comparison ratio for \(q=|i|/|k|\ge C\) is \(O((1+\log q)/q)\). Pairing \(i\) and \(-i\) in the tail gives \(2x_k/(x_k^2-x_i^2)\), with absolutely summable bound \(O(|x_k|\sum_{i>H_k}\log^2(2+i)/i^2)=O(\log^2(2+H_k))\). The finite portion has the same bound by the harmonic sum and (1). Thus
\[
 |A_k|\ll\log^2(2+T+|k|). \tag{2}
\]
Symmetric zero-height cutoffs give the same ordering of pairs by oddness. A cutoff symmetric about fixed \(k\) gives the same limit because it changes at most \(O(|k|)\) terms at the distant endpoints. The argument uses the symmetric principal value.

## Classical bulk constant

Take \(T^{7/10}\le k\le T^{11/10}\) and \(R=\lfloor T^{1/5}\rfloor\). The actual cutoff differs from \(0<|i-k|\le R\) by at most a bounded number of indices with \(|i-k|\asymp R\). All nearby distances are \(O(T^{1/5})\) here, and on that range the threshold is \(T^{1/5}+O(T^{-7/10})\). The rounding error in the classical far sum is \(O(L/R)\).

Write \(\xi(u)=\Psi^{-1}(u)\) on the increasing branch \([4\pi e,\infty)\), \(x=\xi(k)\), \(f(u)=1/(x-\xi(u))\), \(g(u)=1/(x+\xi(u))\), \(p=f+g\). The symmetric-cutoff classical sum equals
\[
 \sum_{n\ge1,\ |n-k|>R}p(n)+\sum_{n\ge1,\ |n-k|\le R}g(n).
\]
The second sum retains the negative partners of the omitted positive indices. The paired kernel \(p\) is increasing separately on either side of \(k\), since \(p'=\xi'((x-\xi)^{-2}-(x+\xi)^{-2})>0\). Its tail is integrable. The outside sums differ from the integrals on \([0,k-R]\) and \([k+R,\infty)\) by endpoint values of size \(O(L/R+1/x)\), by monotonicity. The inside sum of \(g\) differs from its integral by \(O(1/x)\). Together these integrals equal \(\operatorname{PV}\int_0^\infty p(u)\,du-\operatorname{PV}\int_{k-R}^{k+R} f(u)\,du\). From \(\xi'=4\pi/\log(\xi/(4\pi))\), one gets \(\xi''=O(1/(k\log^2 k))\) in the window. Taylor expansion gives \(f(u)=-1/(\xi'(k)(u-k))+O(1/k)\), so the subtracted principal value is \(O(R/k)\).

In the full integral use \(y=\xi(u)\). The ratio of the two excised \(y\)-lengths at the pole tends to one, so the \(u\) and \(y\) principal values agree. The density is \(\log(y/(4\pi))/(4\pi)\) on \([4\pi e,\infty)\). Extending to zero costs \(O(1/x)\) since the additional density is integrable and the kernel on that interval is \(O(1/x)\). Scaling \(y=xv\) yields
\[
 \frac1{2\pi}\operatorname{PV}\int_0^\infty
 \frac{\log(x/(4\pi))+\log v}{1-v^2}\,dv=-\frac{\pi}{8}.
\]
The constant-numerator integral vanishes by the antiderivative \(\frac12\log|(1+v)/(1-v)|\). The log-numerator has a removable singularity at one. Substituting \(v\mapsto1/v\) above one gives a second copy of \(\int_0^1\log v/(1-v^2)\,dv=-\pi^2/8\) by geometric expansion.

For the actual points, sum (1) over \(|i|\le2k\) and \(|i-k|\ge T^{1/5}\) for \(O(L^3/R)\). The remaining tail \(|i|>2k\) is \(O(\log^3(2+k)/k)\) by integral comparison. Using \(1/x\ll L/k\), \(R/k\ll T^{-1/2}\), and oddness to include the negative side,
\[
 A_k=-\frac{\pi}{8}\operatorname{sgn}(k)+O(L^3T^{-1/5})
 \qquad(T^{7/10}\le |k|\le T^{11/10}). \tag{3}
\]

## Pair cancellation and boundary estimates

For \(|k|\le T^2\), neighboring distances are \(O(T^{1/5})=o(N)\). For \(|k|>T^2\) they are \(O(|k|^{1/10})=o(|k|)\). Thus \(w(j)\asymp w(k)\) on the nearby domain, and by dyadic summation
\[
 Q=\sum_{j\sim k}w(j)w(k)\ll\sum_k D_kw(k)^2
 \ll T^{1/5}N+N^{11/10}\ll T^{6/5}L.
\]
The same summation gives \(\sum_k D_kw(k)^2\log^4(2+T+|k|)<\infty\) for fixed \(T\). Equations (2) and the \(S_2\) bound then give absolute convergence of the outer \(X_4\) sum with the inner principal values taken first.

On the symmetric domain where both indices lie in the bulk, nearby indices have the same sign. The constant term in (3) cancels exactly by exchange \(j\leftrightarrow k\) in the ordered-pair sum. Cauchy–Schwarz bounds the remainder by \(O(L^3T^{-1/5}\sqrt{S_2Q})=O(T^{-1/10}L^2M)\). With an index below \(T^{7/10}\), both are at most \(2T^{7/10}\) and there are \(O(T^{9/10})\) ordered pairs. Equation (2) and Cauchy–Schwarz give \(O(L^2T^{9/20}\sqrt M)=O(T^{-1/20}L^{1/2}M)\).

With an index above \(B=T^{11/10}\), both are at least \(B/2\). The required weighted square sum, including the logarithms of (2), is at most a constant times
\[
 \sum_{|k|\ge B/2}(N/|k|)^{200}
    (T^{1/5}+|k|^{1/10})\log^4(2+T+|k|)
 \ll (N/B)^{200} B(T^{1/5}+B^{1/10})L^4
 =O(T^{-18.7}L^{204}).
\]
Its square root times \(\sqrt{S_2}\) is \(o(M)\). These estimates include boundary-crossing pairs. Therefore \(X_4=o(M)\) uniformly at times where the energy is finite, and in the classical calculation \(X_4=o(TL^3)\).

## Scale check and scope

At \(x=\xi\) the renormalized energy vanishes. Nearby pairs with \(N\le j\le 2N\) and \(k=j+r\), \(1\le r\le cT^{1/5}\), have weights bounded below, gaps comparable to \(r/L\), and contribute \(\gg TL^3\) to the unsigned inverse-distance sum. Thus restricting that positive sum to nearby pairs preserves the obstruction to the extra logarithm in the displayed Lemma 21(ii) bound. The signed estimate survives this control and supports the advocate reconstruction. This note uses neither the author's positive inverse-distance bound nor an assertion about the rest of Proposition 22 or Theorem 1. The other Lemma 21(ii) uses on p. 52 lie outside this check.
