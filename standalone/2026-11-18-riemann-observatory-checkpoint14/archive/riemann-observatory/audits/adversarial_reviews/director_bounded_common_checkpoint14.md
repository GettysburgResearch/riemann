# Checkpoint 14 — Bounded common-sequence phase obstruction

Fix \(1/2<\theta<2/3\), \(K\asymp T^\theta\), and an integer \(P\asymp KT\). Set \(X=K^{1/4}\) and fix \(0<\eta<2^{1/4}-1\). The fourth power of the prime polynomial with primes in \([X,(1+\eta)X]\) has support \(\mathcal S\subset[K,2K)\) consisting of all products of four band primes, including repetitions. If \(M\) counts the band primes, unique factorization gives \(S=|\mathcal S|=\binom{M+3}{4}\asymp K/\log^4 K\) by the prime number theorem. Its coefficient \(c_k\) is the number of ordered tuples with product \(k\), so \(1\le c_k\le24\).

On \(J=[P,2P)\cap\mathbb Z\) there exist a real sequence \(b\) in \([1/2,3/2]\) and an integer sequence \(b\) in \(\{0,1,2\}\), each zero off \(J\) and each of exact mass \(P\). Writing \(B_{k,u}=\sum_{n\equiv u\bmod k}b(n)\), each obeys
\[
 \sum_{k\le2K}\sum_{u\bmod k}|B_{k,u}-P/k|^2\ll PK,\qquad
 \sum_{k\le2K}\max_{u\bmod k}|B_{k,u}-P/k|\ll K\sqrt P.
\]
On unit residues the same bounds hold with the induced unit mean \(\varphi(k)^{-1}\sum_{(u,k)=1}B_{k,u}\). The maximum-error budget is \(O_A(P/\log^A T)\) for every fixed \(A\). For both sequences the real projection is positive and satisfies
\[
 \sum_n b(n)W(n)\gg S\sqrt T\asymp K\sqrt T/\log^4 T,\qquad
 W(n)=\sum_{k\in\mathcal S}\frac{c_k}{k}h_k(n),\quad
 h_k(n)=\mathbf1_{(n,k)=1}\left(\cos(2\pi n/k)-\frac{\mu(k)}{\varphi(k)}\right).
\]
This exceeds \(T\log^4 T\) by a factor tending to infinity.

## Bounded construction and progression budgets

Use \(e(x)=e^{2\pi ix}\). Put \(L=\lfloor K/100\rfloor\), \(I=[P+L,2P-L)\cap\mathbb Z\), and let \(\psi\) be the uniform probability on \([-L,L]\cap\mathbb Z\). The shifted interior stays in \(J\), since its extreme possible integers are \(P\) and \(2P-1\). At a nonzero reduced fraction \(v/q\), the geometric series gives \(|\widehat\psi(v/q)|\ll\min(1,q/K)\). At \(\pm1/k\) for \(k\in\mathcal S\), the multiplier is real and bounded below by \(\cos(2\pi/100)>0\).

Take \(F(n)=\sum_{K\le l<2K,\ l\in\mathbb Z}\cos(2\pi n/l)\). Use the same half-open shell for \(F\) and \(\mathcal S\), which includes a possible support point at \(K\). For \(n\in I\), the second derivative of \(f_n(x)=n/x\) on \([K,2K]\) is \(2n/x^3\asymp T/K^2\). The van der Corput second-derivative estimate \(\sum_l e(f_n(l))=O(K\sqrt{\lambda}+\lambda^{-1/2})\) for \(|f_n''|\asymp\lambda\) gives \(F(n)=O(\sqrt T+K/\sqrt T)=O(\sqrt T)\), uniformly on \(I\). An endpoint convention in this estimate changes the sum by \(O(1)\). [Graham and Kolesnik, Theorem 2.2, p. 8](https://assets.cambridge.org/97805213/39278/excerpt/9780521339278_excerpt.pdf)

For an interval of \(N\) integers, the Gram matrix of exponentials at distinct reduced frequencies of denominator at most \(2K\) is \(N\mathrm{Id}+E\), with \(\|E\|\ll K^2\log(2K)\). Indeed the circular separation is at least \(1/(4K^2)\), the geometric-series bound on an off-diagonal entry is \(O(\|\alpha-\beta\|^{-1})\), and summing by increasing distance on either side gives the harmonic row bound. The adjoint has the same squared operator norm as the synthesis operator. Since \(P\gg K^2\log(2K)\) asymptotically, the \(O(K)\) coefficients \(1/2\) of \(F\) give \(\|F\mathbf1_I\|_2^2\ll PK\).

With \(\delta=d/\sqrt T\) for a sufficiently small fixed \(d>0\), set
\[
 a=\delta(F-\langle F\rangle_I)\mathbf1_I,\qquad b=\mathbf1_J+\psi*a.
\]
Then \(a\) has zero mass, \(\|a\|_\infty\le1/2\), and \(\|a\|_2^2\ll\delta^2 PK\ll K^2\) by orthogonal centering. Positive convolution preserves the cap, and the interval inclusion gives the required support and exact mass.

For \(g=\psi*a\), finite residue Parseval gives row variance \(k^{-1}\sum_{r=1}^{k-1}|\widehat g(r/k)|^2\) since the zero mode vanishes. After gathering equal reduced fractions, the weight on \(|\widehat a(v/q)|^2\) is at most
\[
 C\min(1,q^2/K^2)\frac{\log(e\,2K/q)}q\ll K^{-1}.
\]
Here the factor before smoothing comes from \(\sum_{k\le2K,\ q\mid k}1/k\). The adjoint Gram bound on \(I\) gives total perturbation variance \(O((P/K)\|a\|_2^2)=O(PK)\). The interval baseline has row discrepancies of absolute value at most one, hence variance \(O(K^2)\). The square triangle inequality gives the asserted cumulative variance. Cauchy–Schwarz over moduli gives the sum of maxima, and \(K/\sqrt P\asymp T^{(\theta-1)/2}\) gives the logarithmic savings. The induced unit mean minimizes the unit-row quadratic error and shifts the reference value by at most the all-row maximum error, so the unit-row maximum increases by at most a factor two.

## Positive projection on the whole shell support

Each \(h_k\) is real, bounded and of period mean zero. All \(k\) are odd for large \(T\). The Ramanujan sums at \(1,2\) equal \(\mu(k)\), giving the normalized Fourier coefficient at each of \(\pm1/k\) as
\[
 \frac{\varphi(k)+\mu(k)}{2k}-\frac{\mu(k)^2}{k\varphi(k)}
 =\frac12+O(X^{-1}).
\]
This formula covers repeated primes via \(\mu(k)=0\). The only common frequencies of \(F\) and \(G_k=\psi*h_k\) can be \(\pm1/k\), since \(l\mid k\) for a frequency \(\pm1/l\) of period \(k\) and both indices lie in \([K,2K)\). These two coefficients give a positive diagonal contribution \(\gg P\) to \(\sum_I F G_k\). By period Parseval the coefficient norm of \(G_k\) is \(O(1)\). The finite-interval off-diagonal pairing therefore contributes \(O(K^{5/2}\log(2K))=o(P)\), uniformly in \(k\), since \(K^{3/2}\log(2K)/T\to0\) for \(\theta<2/3\).

By boundedness and zero period means, one partial period per summand gives \(\sum_I F=O(K^2)\) and \(\sum_I G_k=O(K)\). Centering costs \(O(K^3/P)=o(P)\) per \(k\). The symmetry of \(\psi\) yields
\[
 \sum_n(\psi*a)(n)W(n)
 =\delta\sum_{k\in\mathcal S}\frac{c_k}{k}\sum_{n\in I}(F(n)-\langle F\rangle_I)G_k(n)
 \gg \delta PS/K\asymp S\sqrt T.
\]
The baseline \(\mathbf1_J\) contributes \(O(S)\) by the same period cancellation. This establishes the signed bound, including the repeated-factor contributions.

## Cap-preserving integerization

Round independently at each site of \(J\) to one of the neighboring integers with expectation \(b(n)\). The errors have mean zero and variance at most \(1/4\). By independence, the expected cumulative squared residue error is \(O(PK)\), the mass error has variance \(O(P)\), and the projection error has variance \(O(P(S/K)^2)\) since \(\|W\|_\infty\ll S/K\). Its ratio to the squared real signal is \(O(1/K)\). Markov's and Chebyshev's inequalities give a joint outcome with squared residue error \(O(PK)\), mass error \(m=O(\sqrt P)\) in absolute value, and loss at most half the positive real lower bound.

If mass must be removed, at least \((P-m)/2\) sites are positive. If mass must be added, at least \(P-(P+m)/2\) sites are below two. Thus \(m\) distinct eligible sites can each be changed by one in the required direction, preserving the integer cap and restoring exact mass. In each modulus the edits all have the same sign and absolute row mass \(m\), so their squared row norm is at most \(m^2\). They cost \(O(PK)\) in cumulative squared norm and \(O(\sqrt P S/K)=o(S\sqrt T)\) in projection. The triangle inequality and the earlier maximum and centering arguments give all integer conclusions.

## Scope and provenance

Full residue rows and their deviations from \(P/k\) have exact compatible marginals modulo common divisors because each row comes from the same sequence. Unit-restricted rows use modulus-dependent masses. For instance the odd row modulo two has mass \(P/2+o(P)\), while prime-model centering gives \(P\). The construction concerns a single integer interval, ordinary all-residue or induced-unit centering, and the exact unit-centered moving phase on the entire specified narrow-band support. Prime or rough support, the prime reference \(P/\varphi(k)\), and estimates for the genuine prime sum or full smoothed \(C_*\) remain outside this result. Publication priority has not been established.

The per-modulus argument above follows the bounded construction and gives a direct check of the finite-interval error. The independent bounded review also verifies the signal by controlling the full combined kernel's coefficient energy, including proper denominators. The earlier round established the common-sequence construction with nonnegative weights and a larger absolute signal, with no uniform cap in that construction. [Bounded construction](prime172_bounded_common_countermodel.md) · [Independent bounded review](analytic172_bounded_common_skeptic.md) · [Earlier director review](director_common_sequence_round17.md) · [Earlier construction](prime161_common_sequence_phase_campaign.md) · [Analytic review](analytic163_common_sequence_review.md) · [Geometric review](geometry163_common_sequence_skeptic.md)
