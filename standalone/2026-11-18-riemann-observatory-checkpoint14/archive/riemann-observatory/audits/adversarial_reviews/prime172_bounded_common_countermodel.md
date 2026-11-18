# Prime172 — Bounded and integer-valued common-sequence counterexamples

## Statement

Fix \(1/2<\theta<2/3\), \(K\asymp T^\theta\), and an integer \(P\asymp KT\). Use a short band of primes \(\mathcal P\subset[X,(1+\eta)X]\), with \(X=K^{1/4}\), fixed \(0<\eta<2^{1/4}-1\), and \(|\mathcal P|\asymp X/\log X\), for instance the full prime interval. Let \(\mathcal S\) be the full support of \(D_{\mathcal P}^4\) and let \(c_k\) be its coefficients. By the full-support result in Prime161, \(\mathcal S\subset[K,2K)\), \(1\le c_k\le24\), and \(S=|\mathcal S|\asymp K/\log^4 K\). On \(J=[P,2P)\cap\mathbb Z\) define
\[
 h_k(n)=\mathbf1_{(n,k)=1}\big(\cos(2\pi n/k)-\mu(k)/\varphi(k)\big),\qquad
 W(n)=\sum_{k\in\mathcal S}(c_k/k)h_k(n).
\]
There are two common nonnegative sequences of mass \(P\) supported on \(J\). The first lies in \([1/2,3/2]\) on \(J\), and the second takes values in \(\{0,1,2\}\). Each satisfies
\[
 \sum_{k\le2K}\sum_{u\bmod k}
   \left|\sum_{n\equiv u\bmod k}b(n)-P/k\right|^2\ll PK,\qquad
 \sum_{k\le2K}\max_{u\bmod k}
   \left|\sum_{n\equiv u\bmod k}b(n)-P/k\right|\ll K\sqrt P.
\]
The same upper bounds apply on units about their induced unit mean. Each sequence also satisfies
\[
 \sum_n b(n)W(n)\gg S\sqrt T\asymp K\sqrt T/\log^4 T.
\]
In particular this is larger than \(T\log^4 T\) by a factor tending to infinity. The rows are compatible because they arise from one sequence. The reference values are ordinary all-residue or induced-unit means. The result imposes no prime or rough support and uses no prime-model baseline \(P/\varphi(k)\).

## Bounded real sequence

Let \(F(n)=\sum_{K\le l<2K}\cos(2\pi n/l)\) with integer \(l\). Let \(L=\lfloor K/100\rfloor\), \(\psi\) be the symmetric probability kernel on \([-L,L]\cap\mathbb Z\), and \(I=[P+L,2P-L)\cap\mathbb Z\). For fixed \(n\in I\), the real phase \(f_n(x)=n/x\) on \([K,2K]\) has \(f_n''(x)=2n/x^3\asymp T/K^2\). Graham and Kolesnik, *Van der Corput's Method of Exponential Sums*, London Mathematical Society Lecture Note Series 126 (Cambridge, 1991), Theorem 2.2, p. 8, states that for real twice continuously differentiable \(f\) with \(\lambda\le |f''|\le A\lambda\) on an interval, the sum of \(e(f(l))\) over its integers is \(O(A|I_x|\sqrt\lambda+\lambda^{-1/2})\). Endpoint choices change the sum by \(O(1)\). Thus uniformly for \(n\in I\),
\[
 |F(n)|\ll\sqrt T+K/\sqrt T\ll\sqrt T.
\]
[Cambridge primary excerpt](https://assets.cambridge.org/97805213/39278/excerpt/9780521339278_excerpt.pdf)

Put \(a(n)=\delta(F(n)-\langle F\rangle_I)\mathbf1_I(n)\), \(\delta=d/\sqrt T\) with a fixed sufficiently small \(d>0\), and \(b=\mathbf1_J+\psi*a\). This gives zero mean for \(a\), exact mass \(P\) for \(b\), the claimed support and pointwise real cap. The interval Gram bound in Prime161 gives \(\|F\mathbf1_I\|_2^2\ll(P+K^2\log(2K))K\), since the rational Fourier series for \(F\) has \(O(K)\) coefficients of uniformly bounded magnitude. Orthogonal removal of the mean yields \(\|a\|_2^2\ll K^2\). The Prime161 residue Parseval calculation applies unchanged. More explicitly, at reduced \(v/q\ne0\), the weight over \(k\le2K\) is \(\sum_{k\le2K:q\mid k}1/k\ll q^{-1}\log(e\,2K/q)\). Multiplication by \(|\widehat\psi(v/q)|^2\ll\min(1,q^2/K^2)\) makes the weight \(O(1/K)\) uniformly. The adjoint Gram upper bound then yields pooled variance \(O(PK)\). The baseline \(\mathbf1_J\) has variance \(O(K^2)\). Cauchy–Schwarz gives the stated maximum bound, and least squares and the triangle inequality give the two induced-unit bounds.

For the signal define \(G=\psi*h_k\) individually for each \(k\). In the interval pairing of \(F\) and \(G\), the diagonal frequency overlap is exactly at \(\pm1/k\). If \(1/l\) or \(-1/l\) is in the period-\(k\) Fourier support, then \(l\mid k\), forcing \(l=k\) in the half-open dyadic shell. The coefficient of \(h_k\) at \(1/k\) is \(1/2+O(X^{-1})\) for the full support by Prime161. The multiplier at \(1/k\) is uniformly bounded below by a positive constant, so the diagonal part is \(\gg P\) with positive sign. The off-diagonal Gram operator norm is \(O(K^2\log(2K))\). Parseval on the single period gives \(\|\widehat G\|_{\ell^2}\le\|h_k\|_\infty\ll1\), where the hat here denotes normalized periodic coefficients. Consequently the cross error is \(O(K^{5/2}\log(2K))=o(P)\) uniformly in \(k\). This is exactly where \(\theta<2/3\) is used, and requires no global coefficient-energy bound for \(\sum_k c_k h_k/k\).

For the constant subtraction, each cosine in \(F\) has interval sum \(O(l)\), giving \(\sum_I F=O(K^2)\). The function \(\psi*h_k\) is bounded and periodic of mean zero, so \(\sum_I G=O(K)\). The subtraction is \(O(K^3/P)=o(P)\) per \(k\). Hence by symmetry of \(\psi\),
\[
 \sum_n(\psi*a)(n)W(n)
 =\delta\sum_{k\in\mathcal S}\frac{c_k}{k}
       \sum_{n\in I}(F(n)-\langle F\rangle_I)(\psi*h_k)(n)
 \gg \delta P S/K \asymp S\sqrt T.
\]
The contribution from \(\mathbf1_J\) has absolute value \(O(S)\) by period cancellation. This establishes the bounded real example.

## Integer sequence and exact mass

Independently round each \(b(n)\) on \(J\) to an adjacent integer \(B(n)\) using probabilities that give mean \(b(n)\). Then \(B(n)\in\{0,1,2\}\), and \(\xi_n=B(n)-b(n)\) are independent, centered and have variance at most \(1/4\). The expected pooled squared progression noise is at most \(\sum_{k\le2K}\sum_{n\in J}\mathbb E|\xi_n|^2=O(PK)\). The total-mass noise has variance at most \(P/4\), and the weighted projection noise has variance at most \(P\|W\|_\infty^2/4=O(P(S/K)^2)\). The latter divided by the square of the real-example signal is \(O(1/K)\). By Markov and Chebyshev there is an outcome with pooled progression noise \(O(PK)\), total-mass error \(O(\sqrt P)\), and projection noise less than half the real-example lower bound for large \(T\). For instance choose the constants in the first two bounds so their exceptional probabilities are each at most \(1/4\). The third exceptional probability tends to zero.

Make at most \(O(\sqrt P)\) single-unit edits to restore mass \(P\), keeping the range \(\{0,1,2\}\) on \(J\). The total occupancy and total remaining capacity are both \(P+O(\sqrt P)\), so the required edits are available. A unit edit changes the pooled progression vector by Euclidean norm at most \(\sqrt{\lfloor 2K\rfloor}\), one entry per modulus. The total edit norm is therefore \(O(\sqrt{PK})\). The projection costs \(O(\sqrt P S/K)=o(S\sqrt T)\). The triangle inequality recovers variance \(O(PK)\) and the same signal lower bound. The maximum and induced-unit bounds then follow as before.

This proof strengthens the common-sequence obstruction in Prime161 to a uniform pointwise cap and to an integer-valued example. It remains a statement about ordinary integer centering on one interval. Additional sieve support, prime-density normalization and genuinely prime-specific constraints can still change the arithmetic problem.
