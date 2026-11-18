# A density-one sign change in Zhao's integrated quadratic prime bias

Assume GRH for primitive quadratic Dirichlet L-functions. Write
\[
 I_D(Y)=\frac{\log Y}{Y^{3/2}}\int_2^Y\sum_{p\le t}\chi_D(p)\,dt .
\]
For each fixed \(A>0\), the proportion of fundamental discriminants with
\[
 \limsup_{Y\to\infty} I_D(Y)>A,\qquad
 \liminf_{Y\to\infty} I_D(Y)<-A
\]
tends to one. This holds separately for positive and negative discriminants. In particular the discriminants exhibiting the eventual negative sign of Zhao's question 2 in §8 have relative density zero. For each fixed discriminant the normalized function is bounded. The quantifier on \(A\) comes before the density limit.

## A probabilistic witness

At every prime let \(B_p\) independently take values \(1,-1,0\) with probabilities \(p/(2(p+1)),p/(2(p+1)),1/(p+1)\). Extend completely multiplicatively. For fixed \(x\ge 2\) use the random variable
\[
 T(x)=\sqrt{x}\sum_{n>x}\frac{\Lambda(n)B_n}{n}(1-x/n).
\]
The first powers converge in mean square and almost surely by independence and summable variances. The contribution of higher powers is bounded by an absolute constant uniformly in \(x\), by partial summation from \(\sum_{p^k\le t,k\ge2}\log p\ll\sqrt t\). The latter estimate follows from Chebyshev's bound for squares and \(O(t^{1/3}\log t)\) for the remaining exponents.

Set \(x_j=\exp(2^j)\). The prime blocks \(x_j<p\le x_j^2\) are disjoint. With weight \(w_x(p)=\sqrt x(\log p)(1-x/p)/p\), their variances are
\[
 \sum_{x<p\le x^2} w_x(p)^2\frac p{p+1}\sim\frac{\log x}{3}.
\]
Indeed the prime number theorem and partial summation give the constant \(\int_1^\infty(1-1/v)^2dv/v^2=1/3\). To pass from bounded \(v=p/x\) to infinity, the contribution for \(p>B x\) is \(O(\log(Bx)/B)\) by Chebyshev and partial summation. Each summand is bounded in magnitude by \(O(\log x/\sqrt x)\), so the independent triangular-array central limit theorem applies. Each sign of a fluctuation exceeding one standard deviation has probability bounded below independently of large \(j\). By independence and Borel–Cantelli each occurs infinitely often almost surely. The remaining first powers \(p>x_j^2\) have total variance \(O(\log x_j/x_j)\), summable over \(j\). Their contribution tends to zero almost surely. Thus the sampled \(T(x_j)\) is unbounded above and below almost surely.

## Transfer to fundamental discriminants

Define \(T_D(x)\) by replacing \(B_n\) with \(\chi_D(n)\). For any fixed finite tuple of \(x\)'s the corresponding vector converges in law to the model vector as \(Q<|D|\le 2Q\) tends to infinity. Here are details retaining uniform control of the nonabsolute arithmetic series.

* For finitely many primes their character values converge jointly to the independent local model, by the Chinese remainder theorem and squarefree counting. For odd primes, among the \(p^2-1\) allowed classes modulo \(p^2\), exactly \(p-1\) are divisible by \(p\), and the two nonzero signs have equal counts. At 2, split \(D=d\) for squarefree \(d\equiv1\pmod4\) and \(D=4d\) for squarefree \(d\equiv2,3\pmod4\). The odd fundamental discriminants have proportion \(2/3\), equally split modulo 8 between 1 and 5. The same count applies in a one-sided dyadic interval of either sign.
* With \(L=(\log Q)^6\), truncate at \(n\le L\). The GRH bound \(\psi(t,\chi_D)\ll \sqrt t\log^2(2Qt)\) and partial summation give tail \(O_x(L^{-1/2}\log^2(2QL))=o(1)\). For fixed \(K>\max x\), higher powers above \(K\) contribute \(O_x(K^{-1/2})\) absolutely.
* For distinct odd primes \(p,q\le L\), the mean of \(\chi_D(pq)\) has absolute value \(O((pq)^2/\sqrt Q)\). To see this, split the fundamental discriminant types as above, and sum over allowed residue classes modulo \(8p^2q^2\). Squarefree counting in each class has absolute error \(O(\sqrt Q)\), uniformly in the modulus: insert \(\mu^2(n)=\sum_{h^2\mid n}\mu(h)\), count a single residue class modulo the least common multiple when compatible, and extend the main sum past \(\sqrt{2Q}\) with error \(O(\sqrt Q)\) using \(1/\operatorname{lcm}(m,h^2)\le h^{-2}\). The main densities for invertible classes at \(p,q\) are equal, giving total character sum zero there. The diagonal mean is at most one. Consequently the mean square of the prime sum over \(K<p\le L\) is \(\ll_x\sum_{p>K}(\log p/p)^2+O_x(L^4(\log L)^4/\sqrt Q)\).
* The model truncation converges in probability. The same tail bound in the arithmetic family, first taking \(Q\to\infty\), then \(K\to\infty\), proves joint weak convergence by testing bounded Lipschitz functions and the union bound over the finite tuple.

For any \(A,\epsilon>0\), choose finitely many \(x_j\) such that with probability greater than \(1-\epsilon\) the maximum of the corresponding model coordinates exceeds \(A+C\) and their minimum is below \(-A-C\). Here \(C\) is an absolute bound exceeding \(2/3\) plus the archimedean correction in the [prime-tail identity](zhao-bias-kernel-nov18.md). This strict event is open, so weak convergence gives an arithmetic lower density at least \(1-\epsilon\) on dyadic intervals. For each discriminant counted, uniform almost periodicity transfers the two strict witnesses at negative logarithmic times to arbitrarily large positive times, and the normalized integrated bias differs from the resulting profile by \(o_D(1)\). Let \(\epsilon\downarrow0\). Summing dyadic intervals yields the stated natural relative density.

Source of the question: [T. Zhao, Research in Number Theory (2025), §8(2)](https://doi.org/10.1007/s40993-025-00640-y).
