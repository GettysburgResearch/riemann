# Quantitative exceptional sets for Zhao's integrated quadratic prime bias

**Proposed theorem.** Assume GRH for primitive quadratic Dirichlet L-functions. For each fixed \(A>0\) there exists \(c_A>0\) such that, among fundamental discriminants of either specified sign with \(Q<|D|\le 2Q\), all but \(O_A(Q/(\log Q)^A)\) satisfy
\[
 \limsup_{Y\to\infty} I_D(Y)>c_A\sqrt{\log Q},\qquad
 \liminf_{Y\to\infty} I_D(Y)<-c_A\sqrt{\log Q},
 \qquad I_D(Y)=\frac{\log Y}{Y^{3/2}}\int_2^Y \sum_{p\le t}\chi_D(p)\,dt .
\]
No hypothesis on relations between zero ordinates is needed. We give the arithmetic high-moment argument. The [reflected prime-tail formula](zhao-bias-kernel-nov18.md) supplies the implication from each strict prime-tail witness to a recurrent limiting value.

## Finite prime sums

Let \(r=\max(1,\lceil A\rceil)\), \(b=1/(100r)\), \(N=Q^b\). Use all dyadic \(x=2^j\) in \([N^{1/4},N^{1/2}]\), whose number \(M\asymp b\log Q\). Write
\[
 w_x(p)=\frac{\sqrt{x}\,\log p}{p}(1-x/p)\mathbf1_{x<p\le N},
 \qquad \sigma_x^2=\sum_p w_x(p)^2,\qquad
 Z_x=\sum_p a_x(p)\chi_D(p),\quad a_x(p)=w_x(p)/\sigma_x .
\]
Throughout this range \(\sigma_x^2\sim (\log x)/3\) uniformly by the prime number theorem and partial summation. In detail, the scaled prime sum out to \(Bx\) contributes \((\log x)(\int_1^B(1-1/u)^2du/u^2+o_B(1))\); the positive remaining sum is \(O(\log(Bx)/B)\) by Chebyshev's bound. The constant at \(B=\infty\) is \(1/3\). For the full prime-power tail in the reflected formula,
\[
 T_D(x)=\sqrt x\sum_{n>x}\frac{\Lambda(n)\chi_D(n)}{n}(1-x/n)
       =\sigma_x Z_x+O(1).
\]
Indeed the GRH bound \(\psi(t,\chi_D)\ll\sqrt t\log^2(2Qt)\) gives a truncation error \(O(\sqrt{x/N}\log^2(2QN))=o(1)\); all powers of exponent at least two cost \(O(1)\) by Chebyshev and partial summation. Every implied constant here is uniform in the discriminant.

## A simultaneous signed witness for independent signs

Temporarily replace the characters by independent Rademacher variables \(\varepsilon_p\), each taking values \(\pm1\) equiprobably. Put \(P(z)=(z-1/4)(z+1)^2\). For either choice of sign the polynomial
\[
 H_\pm=\sum_x P(\pm Z_x)
\]
has expectation \(3M/2\), since each \(Z_x\) is symmetric of variance one. A positive value forces some \(\pm Z_x>1/4\).

We claim \(\operatorname{Var}_\varepsilon H_\pm\ll M\) with an absolute constant. The covariance of two summands is \(O(\sum_p a_x(p)a_y(p))\). Indeed in the orthonormal Walsh expansion, the coefficient at a nonempty set \(S\) of \(P(\pm Z_x)\) has absolute value \(\ll\prod_{p\in S}a_x(p)\) when \(|S|\le3\), and vanishes otherwise. This follows by expanding the powers and using \(\sum_p a_x(p)^2=1\). Summing products of coefficients over sizes one to three and using Cauchy–Schwarz proves the claim about covariance. For \(x\le y\),
\[
 \sum_p a_x(p)a_y(p)\ll
 \frac{\sqrt{xy}}{\sqrt{\log x\log y}}\sum_{p>y}\frac{(\log p)^2}{p^2}
 \ll \sqrt{x/y},
\]
since \(\log x\) and \(\log y\) differ by at most a factor of two. Summing the geometric bound proves the variance estimate. Bonami's hypercontractive inequality on the Boolean cube, \(\|F\|_{2r}\le(2r-1)^{d/2}\|F\|_2\) for real multilinear degree at most \(d\), now gives
\[
 \mathbb E_\varepsilon (H_\pm-3M/2)^{2r}\ll_r M^r .
\]

## Arithmetic moment transfer

Average over fundamental discriminants of the specified sign in the dyadic conductor interval. For a monomial in odd prime characters with product \(n\) and total degree at most \(6r\), squarefree counting gives
\[
 \mathbb E_D\chi_D(n)=
 \mathbf1_{n=\square}\prod_{p\mid n}\frac p{p+1}
 +O(n^2 Q^{-1/2}).
\]
For completeness, split \(D=d\) or \(4d\) according to the squarefree parameter \(d\bmod4\). In each residue class modulo \(8\,\mathrm{rad}(n)^2\), opening \(\mu^2(d)\) gives a density times the interval length with absolute error \(O(\sqrt Q)\), by truncation of the square-divisor sum at \(\sqrt{2Q}\). The tail of the main term is bounded by \(O(Q\sum_{h>\sqrt{2Q}}h^{-2})\). Among the \(p^2-1\) squarefree-allowed local classes at each odd prime the \(p(p-1)\) units split equally by sign. The Chinese remainder theorem and division by the total family size \(\asymp Q\) give the formula.

Expand \((H_\pm-3M/2)^{2r}\) in the prime variables before imposing \(\varepsilon_p^2=1\). Every monomial product is at most \(N^{6r}\). The total absolute coefficient mass is \(O_r(M^{2r}N^{6r})\) because \(\sum_p a_x(p)\le\sqrt{N}\le N\). Hence the summed residue-class error is \(O_r(M^{2r}Q^{-1/2}N^{18r})=o(1)\). For a square monomial, its arithmetic main term differs from the Rademacher value by at most \(6r/N^{1/4}\). The sum of the absolute coefficients on square monomials is \(O_r(M^{2r})\). To see this, take the polynomial formed before expansion by replacing every scalar coefficient by its magnitude, bounding the constant by \(3M/2\). Its Rademacher expectation after raising to \(2r\) majorizes precisely the required square monomials. Minkowski's inequality and the bounded \(6r\)-norm of every normalized Rademacher linear form give \(O_r(M^{2r})\). The summed local correction is therefore also \(o(1)\).

This proves the same \(O_r(M^r)\) centered moment bound in the arithmetic family. Markov's inequality gives probability \(O_r(M^{-r})\) that \(H_+\le0\) or \(H_-\le0\). Outside this set the prime tails have both signs with magnitudes exceeding \(\min_x\sigma_x/4-O(1)\). By the reflected formula and almost periodic recurrence, each witness gives limiting normalized values differing from its prime tail by an absolute bounded quantity. For all sufficiently large \(Q\) we may take \(c_A=\sqrt{b}/40\), giving the theorem.

The result addresses [T. Zhao, Research in Number Theory (2025), §8(2)](https://doi.org/10.1007/s40993-025-00640-y). All analytic assertions about the individual L-functions above assume GRH. The finite arithmetic moment transfer itself is unconditional.
