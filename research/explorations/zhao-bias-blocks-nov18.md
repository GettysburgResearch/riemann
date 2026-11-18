# A stretched-exponential bound for the exceptional quadratic biases

**Proposed theorem.** Under quadratic GRH there are absolute \(c,c'>0\) such that, in either one-sided family \(Q<|D|\le 2Q\) of fundamental discriminants, all but \(O(Qe^{-c\sqrt{\log Q}})\) satisfy
\[
 \limsup I_D>c'(\log Q)^{1/4},\qquad \liminf I_D<-c'(\log Q)^{1/4}.
\]
Here \(I_D\) is the normalized integrated quadratic prime bias in the [prime-tail identity](zhao-bias-kernel-nov18.md). The following growing-degree polynomial argument complements the [fixed-degree amplitude estimate](zhao-bias-moments-nov18.md).

## Scales and moment transfer

Choose a sufficiently large absolute \(R\ge4\) as specified below. Set \(M=\lfloor\kappa\sqrt{\log Q}\rfloor\) with \(\kappa>0\) sufficiently small in terms of \(R\), \(x_j=R^{M+j}\) for \(1\le j\le M\), and \(N=R^{3M}\). Let \(w_j(p)=\sqrt{x_j}(\log p)(1-x_j/p)/p\) for \(x_j<p\le N\), zero otherwise. Put \(s_j^2=\sum_{x_j<p\le R x_j} w_j(p)^2\). Uniformly in this range,
\[
 c_0\log x_j\le s_j^2\le C_0\log x_j
\]
with absolute constants independent of \(R\ge4\) for sufficiently large \(Q\), using the prime number theorem on \([2x_j,3x_j]\) and Chebyshev's upper bound for the full sum. Split the normalized sum into its block \(U_j\) and remainder \(V_j\),
\[
 U_j=\sum_{x_j<p\le R x_j}\frac{w_j(p)}{s_j}\chi_D(p),\qquad
 V_j=\sum_{Rx_j<p\le N}\frac{w_j(p)}{s_j}\chi_D(p).
\]
Uniformly in the family, the GRH truncation error in the unnormalized prime-power tail is \(O(\sqrt{x_j/N}\log^2(2QN))=o(1)\), and higher powers cost \(O(1)\). Thus \(T_D(x_j)=s_j(U_j+V_j)+O(1)\).

For comparison use independent variables \(B_p\) with probabilities \(p/(2(p+1))\) at each of \(\pm1\) and \(1/(p+1)\) at zero. For any monomial of degree \(d\) with prime variables \(p\le N\), its arithmetic mean differs from its independent-model mean by \(O(N^{2d}Q^{-1/2})\) with an absolute constant, by the [squarefree residue-class estimate](zhao-bias-moments-nov18.md). This bound remains uniform as \(d\) grows. Each of our linear forms has sum of absolute coefficients \(\le C\sqrt N\), by Cauchy–Schwarz, the variance bounds above, and Chebyshev. Every polynomial product used below thus transfers in expectation with absolute error \(O(Q^{-1/4})\): for products of at most \(M\) fixed degree-six factors in distinct forms the upper bound is \(Q^{-1/2}N^{12M}(CN^3)^M\), and for \((\sum V_j^2)^M\) it is \(Q^{-1/2}N^{4M}(CMN)^M\). Take \(50\kappa^2\log R<1/5\). Even summation over \(2^M\) products costs \(o(Q^{-1/5})\).

## Many disjoint blocks of each sign

In the independent model the \(U_j\) are independent, symmetric, uniformly subgaussian with variance \(1-o(1)\): the squared coefficients sum to one and each \(p>x_1\). Let \(P(z)=(z-1/4)(z+1)^2\), so \(\mathbb E P(\pm U_j)\ge1\) for large \(Q\) and \(\mathbb E P(\pm U_j)^2\le C\) absolutely. Choose a sufficiently small constant \(h>0\) and set \(f(z)=(1-hP(z))^2\). Then \(f\ge0\), \(f(z)\ge1\) wherever \(z\le1/4\), and \(\mathbb E f(\pm U_j)\le1-\delta\) for some absolute \(\delta>0\). Choose \(0<\eta<1/4\) sufficiently small that the sum of \(\binom M k(1-\delta)^k\) at \(k=\lceil(1-\eta)M\rceil\) decays exponentially in \(M\), by the binomial entropy bound. If at most \(\lfloor\eta M\rfloor\) blocks exceed \(1/4\) on the chosen side then some \(k\) blocks all fail, and their product of the nonnegative \(f(\pm U_j)\) is at least one. Markov's inequality, independence in the model and the preceding moment transfer show that each such exceptional arithmetic event has probability \(O(e^{-c_1 M})\).

## Controlling the remote part in all blocks

Let \(B=(b_{jp})\) be the matrix of coefficients for the \(V_j\). For \(j\le k\), Chebyshev's estimate gives
\[
 (BB^{\mathsf T})_{jk}\le C\frac{\sqrt{x_j x_k}}{s_j s_k}\frac{\log(Rx_k)}{Rx_k}
 \le \frac{C'}R R^{-(k-j)/2}.
\]
All constants are absolute for sufficiently large \(M\), since the logarithms of all the scales differ by at most a factor of three. Hence \(\|BB^{\mathsf T}\|_{\mathrm{op}}\le C_1/R\) and its trace is at most \(C_1M/R\). Writing \(W=\sum V_j^2\), independence and subgaussianity in the model imply
\[
 \mathbb E e^{tW}\le\det(I-2tBB^{\mathsf T})^{-1/2}\le e^{2tC_1M/R},\qquad t=R/(4C_1).
\]
Indeed average \(\exp(\sqrt{2t}\,G\cdot V)\) over an independent standard Gaussian vector \(G\), then bound the independent prime-variable expectation by \(\exp(t\|B^{\mathsf T}G\|^2)\). The determinant estimate follows by diagonalization. Consequently \(\mathbb E W^M\le(C_2 M/R)^M\). The same arithmetic moment has an additional error \(O(Q^{-1/4})\). Now fix \(R\) large enough in terms of \(\eta,C_2\). Markov gives \(W<\eta M/64\) except on a set of probability \(O(e^{-c_2M})\). Fewer than \(\eta M\) coordinates can then have \(|V_j|\ge1/8\). Together with the block estimate this gives \(U_j+V_j>1/8\) somewhere and \(U_j+V_j<-1/8\) elsewhere. The lower bound on \(s_j\) and the almost periodic transfer from the reflected prime-tail formula prove the theorem.

## One choice of constants

For all sufficiently large \(Q\), the proof permits the specific conclusion
\[
 \#\{D\text{ failing either amplitude bound with }c'=1/250\}
   \ll Q\exp\!\left(-\frac{\sqrt{\log Q}}{10000}\right).
\]
Here are the margins. Take \(R=e^{24}\), \(\kappa=1/100\), \(h=1/32\), \(\delta=1/32\), and \(\eta=1/1024\). The even moments of \(U_j\) of orders two, four and six are at most \(1,3,15\), respectively, by comparison of the even-power coefficients of the product moment-generating function with those of \(e^{t^2/2}\). The variance is at least \(1-o(1)\). Expanding \(P^2\) and using symmetry gives \(\mathbb E P^2\le15+3(65/16)+1/16<28\), whereas \(\mathbb E P\ge1\). Thus \(\mathbb E f\le1-1/32\). The elementary binomial entropy inequality \(H(1/1024)+(1-1/1024)\log(31/32)<-0.02\) gives the block event a saving exceeding \(e^{-0.015M}\) for large \(M\).

For each \(x_j\), the primes between \(2x_j\) and \(3x_j\) contribute \((\log x_j)(\int_2^3(1-1/u)^2du/u^2+o(1))>(\log x_j)/100\) by the prime number theorem. For large \(y\), partial summation and the prime number theorem give \(\sum_{p>y}(\log p)^2/p^2\le 3\log y/y\). In the covariance estimate, \(\log(Rx_k)/\sqrt{\log x_j\log x_k}\le 2\) for large \(M\). Thus the matrix entry bound is \((600/R)R^{-|k-j|/2}\), and \(C_1=3000\) works. The resulting \(C_2\) can be taken as \(20000\), by \(M!\le M^M\) and \(4e^{1/2}C_1<20000\). At the stated \(R\), \(64C_2/(\eta R)<1/10\). Finally \(15 M\log N\le 45\kappa^2\log R\,\log Q=0.108\log Q\) absorbs the arithmetic transfer with room to spare. The available normalized amplitude before bounded errors is \(\sqrt{\log x_j}/80\ge(\sqrt{24}/800-o(1))(\log Q)^{1/4}\). These constants specify the exponents and amplitudes in an asymptotic result; no finite starting conductor has been computed.
