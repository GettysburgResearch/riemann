# Independent check of the common-sequence phase obstruction

I reconstructed the finite Fourier and Gram argument in [Prime161](prime161_common_sequence_phase_campaign.md). It gives the stated common nonnegative weighted sequence. The displayed construction takes real values at integer arguments. If integer **values** are desired, an additional sampling argument below gives them with exact mass \(P\) and the same bounds. The comparison is to all-residue uniform centering or the induced unit mean. It does not test the prime-model unit baseline.

## Interval, support and phase normalization

Fix \(1/2<\theta<2/3\), \(K\asymp T^\theta\), and positive integer \(P\asymp KT\). The half-open interval \(J=[P,2P)\cap\mathbb Z\) has exactly \(P\) elements. With \(L=\lfloor K/100\rfloor\), the half-open interval \(I=[P+L,2P-L)\cap\mathbb Z\) has \(P-2L\) elements and \(I+[-L,L]\subset J\) on integers, including at the upper endpoint. Both lengths are \(\asymp P\). The argument uses \(P/(K^2\log K)\to\infty\) and \(K/\sqrt P\to0\), which hold throughout the stated range. Four distinct primes in a fixed narrow relative window \([X,(1+\eta)X]\), with \((1+\eta)^4<2\) and \(K=X^4\), give \(\binom{\pi((1+\eta)X)-\pi(X)}4\asymp K/\log^4K\) different products by unique factorization and the prime number theorem. At a preassigned band edge the shifted lower-start shell in Prime161 keeps every such product in one shell. All moduli are odd for large \(T\).

For any integer \(r\), reduction of \(e(rn/k)\) on \(k\)-residues gives a reduced frequency of denominator \(q=k/(r,k)\). The average on unit residues is \(c_k^{\mathrm{Ram}}(r)/\varphi(k)=\mu(q)/\varphi(q)\), since unit reduction to \(q\) is onto with equal fibers and the reduced numerator permutes units. Reflection \(r\mapsto-r\) leaves this real mean unchanged. At \(r=\pm1\) the centered real test is therefore exactly \(h_k(n)={\bf1}_{(n,k)=1}(\cos(2\pi n/k)-\mu(k)/\varphi(k))\). It has zero all-row mean. At \(1/k\) its Fourier coefficient, in the convention \(k^{-1}\sum_{u\bmod k}h_k(u)e(-u/k)\), is
\[
\frac{\varphi(k)+c_k^{\rm Ram}(2)}{2k}
-\frac{\mu(k)c_k^{\rm Ram}(1)}{k\varphi(k)}
=\frac{\varphi(k)+\mu(k)}{2k}-\frac{1}{k\varphi(k)}.
\]
Here \(k\) is odd and squarefree with four primes tending uniformly to infinity, so \(\mu(k)=1\), \(\varphi(k)/k\to1\), and the coefficient tends uniformly to \(1/2\). Reflection gives the same result at \(-1/k\). Only the \(k\)-summand can contribute at either reduced frequency because two integers in \([K,2K)\) with one divisible by the other coincide.

For the uniform positive kernel on \([-L,L]\), its symmetric transform is the mean of cosines, each bounded below by \(\cos(2\pi L/k)>c>0\) at \(\pm1/k\). The full geometric-series bound at reduced \(a/q\ne0\) is \(\min(1,[(2L+1)|\sin(\pi a/q)|]^{-1})\ll\min(1,q/K)\), since the circular distance from \(a/q\) to 0 is at least \(1/q\). Thus \(G=\psi*H\), \(H=\sum_{k\in\mathcal S}(Kc_k/k)h_k\), has at least \(|\mathcal S|\) reduced frequencies with coefficient bounded below in absolute value. The target real projection is against \(W=H/K\), with no further factor of \(P\), \(K\) or \(\varphi(k)\).

## Gram bound and discrepancy

Include each distinct reduced frequency of denominator \(\le2K\) only once. The minimal circular spacing is \(1/(4K^2)\). A geometric sum over an interval of \(N\) integers has each off-diagonal Gram entry \(\ll\min(N,\|\alpha-\beta\|^{-1})\). Starting from any fixed row, the \(j\)-th neighbor in either orientation is at distance at least \(j/(4K^2)\) until the half-circle. There are \(O(K^2)\) distinct frequencies. The absolute row sum off the diagonal is therefore \(O(K^2\log(2K))\). The diagonal is exactly \(N\). The bound on the Hermitian error's operator norm follows from the row and column sums. This proves the lower Gram estimate on \(I\) and the upper estimate for the adjoint transform of vectors supported on \(I\). Hence \(M=\|G{\bf1}_I\|_2\gg\sqrt{P|\mathcal S|}\).

With \(F=G{\bf1}_I\), subtracting the interval mean from each of the positive and negative parts \(F^\pm\) is an orthogonal projection on \(\ell^2(I)\). With \(\lambda=K/M\), the vectors \(a^\pm=\lambda(F^\pm-\langle F^\pm\rangle_I{\bf1}_I)\) have zero mass, \(\|a^\pm\|_2\le K\) and pointwise lower bound \(-K/\sqrt{|I|}\). This last inequality uses \(\langle F^\pm\rangle_I\le M/\sqrt{|I|}\). Convolving with the positive kernel preserves the lower bound and keeps support inside \(J\). Consequently \(b^\pm={\bf1}_J+\psi*a^\pm\) are nonnegative and have mass \(P\), without a truncation of negative values.

For \(g=\psi*a^\pm\), finite Parseval gives total variance at modulus \(k\) equal to \(k^{-1}\sum_{r=1}^{k-1}|\widehat g(r/k)|^2\); the zero mode is absent by the exact mass cancellation. The cumulative weight at a reduced frequency \(a/q\), \(q\ge2\), is at most
\[
\left|\widehat\psi(a/q)\right|^2 \sum_{m\le 2K/q}\frac1{qm}
\ll \min(1,q^2/K^2)\frac{\log(e\,2K/q)}q\ll\frac1K.
\]
The final bound for \(q\le K\) uses boundedness of \(x\log(2e/x)\) for \(0<x\le1\). Thus imprimitive appearances are accounted for with their full geometric multiplicities. The adjoint bound above gives summed perturbation variance \(O((P/K)\|a^\pm\|_2^2)=O(PK)\). The baseline \({\bf1}_J\) contributes \(O(K^2)\) because every progression count differs from \(P/k\) by less than 1. Cauchy–Schwarz in the \(O(K)\) moduli gives summed row maxima \(O(K\sqrt P)\). Since \(K/\sqrt P\asymp T^{(\theta-1)/2}\), this supplies every fixed logarithmic saving against \(P\). On restricting to units, the induced mean minimizes the row squared error and its shift from \(P/k\) is at most the row's maximum error. Cross-modulus common-divisor marginals agree exactly by summing the same sequence over the corresponding congruence class. This also holds for the all-residue deviations from \(P/k\), as \(k/d\) copies of \(P/k\) sum to \(P/d\) for \(d\mid k\).

Symmetry of the convolution and the definition of \(F\) give
\[
\sum_n H(n)(b^+(n)-b^-(n))=\lambda(M^2-|I|\,\langle F\rangle_I^2).
\]
The sum \(\sum_IF\) is \(O(K|\mathcal S|)\), as each convolved \(h_k\) is bounded and mean-zero with period \(k\), leaving only a partial period. The ratio of the subtracted term to \(M^2\) is \(O(K^2|\mathcal S|/P^2)=o(1)\). Hence one sign yields absolute projection against \(W\) of size \(\gg M\gg\sqrt{P|\mathcal S|}\asymp K\sqrt T/\log^2 T\). Its ratio to \(T\log^4T\) is \(\asymp K/(\sqrt T\log^6 T)\to\infty\).

## Optional integer values with exact mass

Fix the successful deterministic \(b\). Independently draw \(P\) integers of \(J\) from the probability \(b(n)/P\), and write \(B(n)\) for the occupancies. Each realization has nonnegative integer values, support in \(J\), and mass \(P\). For each modulus the resulting vector of residue counts is multinomial, with mean vector given by \(b\)'s counts. The sum of entry variances is \(P(1-\sum_u p_{k,u}^2)\le P\). Hence the expected total squared error about the deterministic counts over \(k\le2K\) is \(O(PK)\). Markov at a sufficiently large fixed multiple makes failure probability at most \(1/4\). On the complementary event the same \(O(PK)\) bound about \(P/k\) follows by the square triangle inequality, and the maxima and unit-centered consequences follow as before.

The change in the projection \(\sum W(n)B(n)\) has mean zero and variance at most \(P\|W\|_\infty^2\ll P(|\mathcal S|/K)^2\). Its ratio to the square of the deterministic lower bound is \(O(|\mathcal S|/K^2)=o(1)\). Chebyshev shows the projection retains at least half its magnitude with probability \(1-o(1)\). The two events intersect, proving existence of one integer-valued sequence with all bounds at once.

The integer-valued variant still permits repeated draws and mass on nonunits. Its support lies in one fixed interval, with the phase tested on one selected four-prime subfamily. The available reference on units is \(\varphi(k)^{-1}\sum_{(u,k)=1}B_{k,u}\), not \(P/\varphi(k)\). Already modulo 2 the all-residue bound forces odd mass \(P/2+O(\sqrt{PK})=P/2+o(P)\), whereas the prime-model baseline on the sole unit residue is \(P\). The common-divisor marginal identity concerns whole rows. Unit-restricted rows can discard different integers and need not have that equality. Common-sequence consistency leaves prime and sieve support unconstrained, and the result does not estimate the actual long-prime term or full smoothed \(C_*\) sum.
