# Prime dilations on rational labels and the cost of representing a real wave

Consider a proposed way to prove positivity of Weil's prime form. Replace dilation by prime powers on the real line by exact shifts on rational labels. The label \(m/n\) in lowest terms has logarithmic height \(\log(mn)=\sum_p |v_p(m/n)|\log p\). This construction has a sharp, uniform spectral gap, but transmitting the real dilation data to it can cost much more than the actual archimedean term.

For a finite set of primes \(S\), use the regular representation on \(\ell^2(\mathbb Z^S)\), unit vectors \(a\), coordinate shifts \(T_p\), and valuation coordinates \(j_p\). Define
\[
 \mathcal E_S(a)=\sum_{p\in S}\log p\left(
   \langle |j_p|a,a\rangle+\frac2{p-1}
   -2\sum_{m\ge1}p^{-m/2}\Re\langle T_p^m a,a\rangle\right).       \tag{1}
\]
The prime-power coefficient agrees with the actual Riemann explicit formula. The added height and scalar are part of the proposed comparison. Burnol's local conductor operator is a separate operator, defined with physical and additive Fourier variables over one local field. [Burnol](https://arxiv.org/abs/math/9902080)

## Exact local gap

Set \(r=p^{-1/2}\), \(c_p=(1+r^2)/(1-r^2)\). In the Fourier representation on the circle with probability Haar measure, the operator in parentheses is
\[
 |D|+c_p-P_r(\theta),\qquad P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]
Its ground eigenvalue is zero, with Fourier coefficients proportional to \(r^{|j|}\). Indeed the convolution of the coefficients of \(P_r-1\) with \(r^{|j|}\) equals \((|j|+2r^2/(1-r^2))r^{|j|}\). The orthogonal complement of this ground state has spectral bottom exactly \(c_p\).

For the latter assertion take the disk automorphism \(b(z)=(z-r)/(1-rz)\). Its boundary phase derivative is \(P_r\). Writing \(f=g\circ b\) preserves the Dirichlet energy of its harmonic extension to the disk by conformal invariance. In the boundary normalization this is \(\langle |D|f,f\rangle=\langle |D|g,g\rangle\). Substitution gives \(\int P_r|f|^2=\int |g|^2\). Orthogonality to \(P_r\) means \(g\) has zero mean, so its Fourier series gives \(\langle |D|g,g\rangle\ge\|g\|^2\). Equality holds for \(g(z)=z\) or its conjugate. Density extends the result to the form domain. The same proof works with any Hilbert space as coefficient space. Tensorization shows that the finite-prime sum has the product ground state and exact first gap \(\min_{p\in S} c_p\log p\). In particular the gap is uniformly at least \(3\log 2\), since \(((u+1)/(u-1))\log u\) is increasing for \(u>1\).

Let \(\Pi_p\) project onto the ground state in coordinate \(p\) alone. Its first-shift expectation is \(2r/(1+r^2)\). The difference between the shift expectation for \(a\) and for \(\Pi_p a\) has magnitude at most \(2\|(1-\Pi_p)a\|\). Consequently even for correlated vectors
\[
 \mathcal E_S(a)\ge \tfrac14\sum_{p\in S}c_p\log p
   \big(|\langle T_pa,a\rangle|-2\sqrt p/(p+1)\big)_+^2 .          \tag{2}
\]

## A sharp cost for the actual dilation correlations

Take the normalized physical test \(g(u)=L^{-1/2}\mathbf1_{[0,L]}(u)e^{itu}\) in logarithmic coordinates. The indicator is permissible for the translation correlations and its Fourier transform also has finite logarithmic gamma energy. For every prime and power its dilation correlation has phase \(e^{itm\log p}\) up to convention and modulus \((1-m\log p/L)_+\). Let \(x=e^L\), \(S=\{p\le x\}\). Among all unit vectors in (1) having **all** these prescribed prime-power expectations, and even allowing arbitrary correlations among prime coordinates, the minimum energy in the sense of an infimum is
\[
                (1+o(1))\frac{x}{(\log x)^2},                       \tag{3}
\]
uniformly in every real carrier \(t\). The same leading lower bound holds if only the magnitudes of the first prime shifts are prescribed.

To see the lower bound, put \(e_p=\langle |j_p|a,a\rangle\). Split the sum for the first shift into the two edges incident at index zero and all the other edges. Vector Cauchy–Schwarz on the first two and the inequality \(2uv\le u^2+v^2\) on the others give
\[
 v_p:=|\langle T_pa,a\rangle|\le\sqrt{2e_p}+e_p .
\]
Thus for small \(v_p\), \(e_p\ge v_p^2/2-O(v_p^3)\). In (1) the entire bounded prime potential costs at most \(2\sum_{p\le x}(\log p)/(\sqrt p-1)=O(\sqrt x\log x)\). On \([x^{3/4},x]\) take \(v_p=1-\log p/L\); enlarging the absolute constant in the cubic error covers this whole range. For each fixed positive integer \(j\),
\[
 \sum_{p\le x}\log p\,(1-\log p/L)^j\sim j!\,x/L^j .
\]
This follows by partial summation from the prime number theorem, or by substituting \(y=\log(x/p)\) and integrating \(y^j e^{-y}\). Primes below \(x^{3/4}\) make a negligible contribution to these asymptotics. This proves the lower bound in (3).

For the matching construction use a product of unit circle functions with prescribed squared moduli. If \(p\ge x^{3/4}\), the required density, after rotating the phase, is exactly \(1+2v_p\cos\theta\), with \(0\le v_p\le1/4\). Use its positive square root. Its constant and linear Taylor terms are \(1+v_p\cos\theta\), and the remainder is \(O(v_p^2)\) in the circle Sobolev norm \(H^1\), by differentiation. Its \(|D|\) energy is therefore \(v_p^2/2+O(v_p^3)\). For a smaller prime put \(h=L/\log p\). The sequence \((1-|m|/h)_+\) is positive definite, being the correlation of a normalized interval under integer translations. Its trigonometric polynomial is nonnegative by Fourier inversion (equivalently it is a convex combination of the adjacent integral-length Fejér kernels). Fejér–Riesz factorization gives its required squared modulus using a polynomial of degree at most \(\lfloor h\rfloor\), with unit norm. Its energy is at most \(h\), so the cost from these smaller primes is \(O(x^{3/4}L)\). Rotate each factor by \(t\log p\). The height term has the asserted leading asymptotic; both the prime potential and the scalar term are negligible there. This proves (3).

For comparison, the physical gamma integral of the test itself is \(O(\log(2+|t|)+1)\) for \(L\ge1\), from the logarithmic bound on the digamma multiplier and the squared sinc tail after changing variables to \(L(\xi-t)\). The separate explicit-formula pole term can be large at small carrier and must be retained in any transfer to the full form. Even at arbitrarily high carriers, once \(e^L/L^2\) greatly exceeds \(\log(2+|t|)\) the arithmetic height required to match all the prime correlations individually exceeds this gamma budget. A successful transfer would have to use their weighted signed sum or a compensating term; individual preservation plus the local graph gaps cannot supply it.

The pole contribution can also be made negligible in this comparison. Each pole pairs the two integrals of $g(u)e^{\pm u/2}$; their product in modulus is $O(e^{L/2}/[L(t^2+1/4)])$, by explicitly integrating the two exponentials. Take $L=2\log\log |t|$ and let $|t|\to\infty$. The physical gamma term and the absolute pole contribution together are $O(\log |t|)$, whereas (3) forces graph energy asymptotic to $(\log |t|)^2/[4(\log\log |t|)^2]$. Thus the pole budget cannot supply the missing factor for this explicit family.
