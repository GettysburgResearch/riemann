# Uniform derivative-weighted phase moments on logarithmic blocks

17 November 2026. I checked the fixed-polynomial calculations, Heap–Li–Zhao's published Theorem 5 with its original arithmetic local factors, and the coefficient hypotheses in the proof. Under RH the source does give a prescribed growing range: for every fixed \(a>0\), the relative phase asymptotic below is uniform for \(m,n\le(\log Y)^a\). The range concerns the admissible twist indices and the stated covariance consequences. The all-prime supremum fails for every fixed tail cutoff. [Classical63 fixed-polynomial check](prime_array63_hlz_classical_independent.md) · [Derivative-tail check](prime_array63_hlz_derivative_tail.md) · [Prime-torus review](prime_array63_tail_prime_torus_review.md)

## Source uniformity and the padding step

The source is Heap–Li–Zhao, *Algebra & Number Theory* 16(7), 1589–1625 (2022), DOI 10.2140/ant.2022.16.1589. Theorem 5 on p. 1605 gives \(J+I+\overline{I(\bar\beta,\bar\alpha)}\) plus \(O_D(T(\log T)^{-D})\) for every fixed \(D>0\), with sufficiently small complex shifts \(|\alpha|,|\beta|\ll1/\log T\), length \(y=T^\theta\) for fixed \(\theta<1/2\), and coefficients satisfying uniform submultiplicativity and a fixed divisor/log majorant. I use (5), (6), and (24), without passing through the smoothed diagonal of Theorem 4. The proof in §4, pp. 1607–1615, makes the complex shift regime explicit. Propositions 10–11 and their proofs in §§5–6 use the fixed coefficient majorants, with \(C'\) in Proposition 11 explicitly a function of \(r,C\). Fix \(y=T^{1/4}\). Write \(\eta=(\log T)^{C''}\) for the threshold, with \(C''\) chosen large after the desired log saving. The small-modulus bound is \(T\exp(-c\sqrt{\log T})\eta^{3/2+\varepsilon}\). The log-dependent large-modulus term is \(T(\log T)^{C'}\eta^{-1/2+\varepsilon}\). At \(\theta=1/4\) its three power terms in \(T\) have exponents \(3/4+\varepsilon,\,2/3+\varepsilon,\,11/12+5\varepsilon/4\), all less than 1 for \(\varepsilon=1/100\). These dependencies make the error uniform for the bounded coefficient family used below. The printed log-majorant at \(n=1\) uses bounded initial data, as in the source's own arrays with nonzero \(a(1)\). [Published PDF, pp. 1605–1615](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [arXiv v1, Theorem 2](https://arxiv.org/pdf/2003.09368v1)

For \(m,n\le y\) put \(M=\max(m,n)\) and \(P(s)=8\sum_{j\le M}j^{-s}\). For each of the four polynomials \(Q(s)=m^{-s}\pm n^{-s},m^{-s}\pm i n^{-s}\), the coefficients of \(P\) and \(P\pm Q\) have moduli between 6 and 10 at each index \(1\le j\le M\) and vanish above \(M\). If \(uv\le M\), the two input moduli have product at least 36 and the output modulus is at most 10. If \(uv>M\), the output is zero. Each padded input therefore satisfies exact submultiplicativity. For \(j\ge2\), the same bound \(\tau_{16}(j)\log j\ge16\log2>10\) works uniformly. The initial values are uniformly bounded by 10. All these arrays are padded further by zeros to length \(y\), retaining the length hypothesis of the source and its Lemma 7. In particular the size of the support and a possible composite monomial index do not change either coefficient constant.

Apply the source to \(P,P+Q,P-Q\), then subtract the padded expressions by the parallelogram identity. The main term is the diagonal of a sesquilinear expression in the coefficients, including the conjugated \(I\) term. Thus it satisfies the same identity as the original shifted sum. Use complex polarization on the four \(Q\)'s to get a mixed monomial estimate. All these are a fixed finite number of source invocations. The dense padding cancels algebraically before bounding the arithmetic main term. The remaining main expression is the appropriate monomial pair with weight \(1/\operatorname{lcm}(m,n)\). Bounding the dense arrays before cancellation would lose this weight.

## Uniform control of the arithmetic factor

Put \(L=\log T\), \(g=(m,n)\), \(h=m/g\), \(j=n/g\). Take small fixed \(c>0\) and two Cauchy circles \(|\alpha|=c/L\), \(|\beta|=2c/L\). For the auxiliary derivative in (24), use \(|\eta|=c/(4L)\). The zeta poles of the three \(Z\) terms are off those contours and outside the auxiliary circle, since the required pair sums have modulus at least a fixed multiple of \(1/L\). On the circles the \(Z\) factor for \(h=j=1\) is \(O(L)\): it is two numerator zeta factors of size \(O(L)\) and one reciprocal zeta factor with a zero at the origin, of size \(O(1/L)\). The multiplier from (24) is \(h^{-v}\) times one local ratio for each \(p^e\Vert j\), for the appropriate small shifts \(u,v,w\). In the reflected term the roles of \(h,j\) may switch.

For exactness, (6) defines \(f_{u,w}=\mu*(n\mapsto n^{-u})*(n\mapsto n^{-w})\), with the Möbius factor unshifted. Set \(U=p^{-u}\), \(V=p^{-w}\), and \(z=p^{-1-v}\). Then
\[
 f_{u,w}(p^r)=V^r+(U-1)\sum_{b=0}^{r-1}U^bV^{r-1-b},\qquad
 \sum_{r\ge0}f_{u,w}(p^r)z^r=\frac{1-z}{(1-Uz)(1-Vz)}.
\]
Writing \(f_r=f_{u,w}(p^r)\), the local ratio in (24) is exactly
\[
 \frac{\sum_{r\ge0} f_{r+e}z^r}{\sum_{r\ge0}f_rz^r}
 =V^e+(U-1)\left(\sum_{b=0}^{e-1}U^bV^{e-1-b}\right)\frac{1-Vz}{1-z}.
\]
The last quotient is uniformly bounded, since \(|z|\le p^{-1+O(1/L)}\) and \(|Vz|\le p^{-1+O(1/L)}\). The first term differs from 1 by \(O((e\log p/L)\exp(O(e\log p/L)))\). The second term has the same bound by \(|U-1|\ll(\log p/L)p^{O(1/L)}\) and the elementary bound on its finite geometric sum. Since \(e\log p\le\log j\le\frac14 L\), the exponentials are bounded independently of the pair. Summing departures over \(p^e\Vert j\) gives \(O(\log j/L)\), and taking the product preserves that estimate by \(\left|\prod (1+x_p)-1\right|\le e^{\sum|x_p|}-1\). Including \(h^{-v}\) gives
\[
 h^{-v}\prod_{p^e\Vert j}
 \frac{\sum_{r\ge0}f_{r+e}z^r}{\sum_{r\ge0}f_rz^r}
   =1+O\!\left(\frac{\log(hj)}{L}\right).
\]
The factors \(h^{-\beta}j^{-\alpha}\) and \(h^\alpha j^\beta\) in \(J\) obey the same estimate directly.

Consequently the per-pair \(J\) term differs from its \(h=j=1\) counterpart by \(O(TL\log(hj))\), before the weight \(1/\operatorname{lcm}(m,n)\). This uses the \(O(L)\) zeta pole bound and the \(O(TL)\) integral bound with one \(\log(t/(2\pi))\) factor. The \(I\) term has the same bound: the \(Z\) perturbation is \(O(\log(hj))\), the integral of the small powers of \(t/(2\pi)\) is \(O(T)\), and the auxiliary Cauchy derivative contributes \(O(L)\). These integral bounds follow by integrating the small power directly on \((0,1]\), and using \(|(t/(2\pi))^{O(1/L)}|\ll1\) for \(1\le t\le T\). The outer \(\alpha,\beta\) differentiation brings another \(O(L^2)\). Comparing with Theorem 5 for the constant polynomial gives, under RH,
\[
 \begin{split}
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2
      m^{-\rho}n^{-\bar\rho}
 &=\frac{1}{\operatorname{lcm}(m,n)}\sum_{0<\gamma\le T}|\zeta'(\rho)|^2\\
 &\quad+O\!\left(\frac{TL^3\log(hj)}{\operatorname{lcm}(m,n)}
                        +T L^{-D+2}\right).
 \end{split}
\]
The derivative applies to the two zeta factors, which are the shifted factors. The weight \(Q(\rho)\overline R(1-\rho)\) is unshifted. Neither the source nor the differentiation needs simplicity. RH is used here to set \(1-\rho=\bar\rho\). If the rectangle is first taken at a good height within a bounded distance of the stated endpoint, the unit-window zero count and the critical-line derivative convexity bound give a power-saving change on RH for these logarithmic lengths.

## Explicit tail range and covariance

Write \(\kappa(m,n)=g/\sqrt{mn}\). For \(m,n\le L^a\) choose \(D>2a+8\). Multiplying the last estimate by \(\sqrt{mn}\) makes the source error at most \(T L^{-D+2}\sqrt{mn}\), which is absorbed by \(\kappa(m,n) T L^3\) uniformly since \(mn/g\le L^{2a}\). Use the RH untwisted moment \(T L^4/(24\pi)+O(TL^3)\) from Gonek as in the fixed-polynomial check. The phase sum is then
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2e^{-i\gamma\log(m/n)}
 =\frac{\kappa(m,n)}{24\pi}T L^4
    +O_a\!\big(\kappa(m,n) T L^3(1+\log(hj))\big).
\]
Count both signs by adding the reflected sum, which conjugates the phase. For \(|\gamma|>Y\) with \(m,n\le(\log Y)^a\), the same pair is within the uniform range at each \(t\ge Y\). Stieltjes integration against \((1/4+t^2)^{-1}\) with the endpoint \(-A(Y)/(1/4+Y^2)\) retained for the strict tail therefore gives
\[
 \Phi_Y(\log(m/n))
 =\kappa(m,n)\left[1+O_a\!\left(\frac{1+\log(hj)}{\log Y}\right)\right] ,
 \qquad m,n\le(\log Y)^a .
\]
Here \(\Phi_Y\) is the characteristic function of the normalized two-sided derivative tail. The normalization uses the untwisted strict tail, of size \((\log Y)^4/(12\pi Y)\). The error is relative to \(\kappa(m,n)>0\), and in the claimed range it is \(O_a((1+\log\log Y)/\log Y)\). This specifies the growth range. The source small-modulus proof uses Siegel’s theorem, so this calculation provides no numerical threshold for \(Y\).

For \(q_k(\gamma)=\sqrt{k}e^{-i\gamma\log k}-1\), substitution gives uniformly for \(k,l\le K=(\log Y)^a\)
\[
 \mathbb E_Y q_k\overline q_l
  =(k,l)-1+O_a\!\left(\frac{((k,l)+2)(1+\log(kl))}{\log Y}\right).
\]
For the growing prime block \(p\le K\), set \(Z_p=q_p/\sqrt{p-1}\). The diagonal second-moment discrepancies from the identity are \(O_a((1+\log K)/\log Y)\). The off-diagonal discrepancies are bounded by \(C_a(1+\log K)/[\log Y\sqrt{(p-1)(q-1)}]\). The nonnegative rank-one majorant of the off-diagonal matrix has norm bounded by that prefactor times \(\sum_{p\le K}1/(p-1)\ll1+\log K\). The full second-moment matrix thus differs from the identity by \(O_a((1+\log K)^2/\log Y)=o(1)\) in operator norm. The means also have squared Euclidean norm \(O_a((1+\log K)^3/(\log Y)^2)\), so centering preserves covariance convergence. This controls a growing block of second moments. For higher Fourier characters the stated range applies when the reduced numerator and denominator of the prime-power character are each at most \((\log Y)^a\).

## Obstruction to uniformity over all primes

The derivative-weighted measure \(\nu\) has finite mass by the untwisted derivative moment and dyadic summation with the \(1/|\rho|^2\) weight. The same positive main term forces infinitely many positive weights at unbounded heights. Thus each finite tail cutoff \(Y\) has positive mass \(B_Y\). Its normalized restriction \(\nu_Y\) is a probability, and at this fixed \(Y\) dominated convergence gives \(\Phi_Y(t)=\int e^{-it\gamma}\,d\nu_Y(\gamma)\to1\) as \(t\to0\).

There are distinct prime pairs with \(q>p\to\infty\) and \(q/p\to1\). In fact an eventual multiplicative gap \(p_{j+1}/p_j\ge1+\delta\) for some fixed \(\delta>0\) would make the reciprocal primes have summable geometric tails, contrary to Euler's divergence. Along pairs with ratios tending to 1, \(\Phi_Y(\log(p/q))\to1\) for this fixed \(Y\), whereas \(\kappa(p,q)=1/\sqrt{pq}\to0\). Hence
\[
 \sup_{p\ne q\ \mathrm{prime}}
       |\Phi_Y(\log(p/q))-1/\sqrt{pq}|\ge1
\]
for every fixed \(Y\). The primes in this obstruction run beyond any fixed block. For fixed finite sets of primes and fixed exponent vectors, the reduced rational is fixed and the phase formula gives its Poisson Fourier coefficient. These fixed-character limits imply weak convergence on the compact prime torus by Stone–Weierstrass. The all-pairs supremum asks for a different order of quantifiers, so its failure is consistent with that weak convergence.
