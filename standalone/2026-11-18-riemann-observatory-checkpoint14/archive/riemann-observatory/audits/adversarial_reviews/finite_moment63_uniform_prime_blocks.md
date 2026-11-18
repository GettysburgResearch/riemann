# Uniform derivative-weighted tail covariances for growing prime blocks

17 November 2026. Assume RH. Let \(\mathcal T_Y(U,V)=\sum_{|\gamma|>Y}|\zeta'(\rho)|^2U(\rho)\overline{V(\rho)}/|\rho|^2\), let \(B_Y=\mathcal T_Y(1,1)\), and put \(e_m(s)=m^{-s}\), \(Q_k=k e_k-e_1\). Zeros may be counted with multiplicity, since the derivative vanishes at multiple zeros. The untwisted normalization is \(B_Y\sim (\log Y)^4/(12\pi Y)\), with both signs of the ordinate. This follows by Stieltjes integration from the one-sided untwisted moment \(T(\log T)^4/(24\pi)\). [Gonek, Corollary 1, p. 124](../../sources/classical63_lfunctions/gonek1984.pdf) · [Tail normalization and fixed-character phase law](prime_array63_tail_prime_torus_review.md)

## Uniform entry estimates

For fixed \(D,B>0\), uniformly over integers \(1\le m,n\le(\log Y)^D\), put \(g=\gcd(m,n)\). The estimate is

\[
 \frac{mn\,\mathcal T_Y(e_m,e_n)}{B_Y}
 =g+O_{D,B}\!\left(\frac{g\log(mn/g^2)}{\log Y}+(\log Y)^{-B}\right). \tag{1}
\]

For \(m=n\), the left side is exactly \(m\), since \(|e_m(1/2+i\gamma)|^2=m^{-1}\). No zeta error appears in this identity. In particular the normalized tail Fourier coefficient at \(\log(m/n)\) has absolute error \(O_D(1/\log Y)\) about \(g/\sqrt{mn}\) in this whole range. To see this, divide (1) by \(\sqrt{mn}\) and use \(x^{-1/2}\log x\le 2/e\) for \(x=mn/g^2\ge1\), with \(B=1\).

Expanding \(Q_k,Q_l\) gives, for \(k,l\le P\le(\log Y)^D\),

\[
 \frac{\mathcal T_Y(Q_k,Q_l)}{B_Y}
 =\gcd(k,l)-1+O_{D,B}\!\left(
 \frac{\gcd(k,l)\log(kl/\gcd(k,l)^2)+\log k+\log l}{\log Y}
       +(\log Y)^{-B}\right). \tag{2}
\]

For prime indices the error is \(O_D(\log(2P)/\log Y)\) uniformly, including the diagonal, by (1) and the exact diagonal identity. This gives uniform absolute convergence for prime indices up to every fixed power of \(\log Y\). Over all integer indices the error is \(O_D(P/\log Y)\) upon taking \(B=1\): use \(g\log(kl/g^2)\le 2g\log(P/g)\le 2P/e\). Thus one can take any \(P=o(\log Y)\), for example \(P=(\log Y)^{1-\varepsilon}\) with fixed \(0<\varepsilon<1\), for uniform absolute convergence over all integer pairs. The centering by the tail means leads to the same estimates, since \(\mathcal T_Y(Q_k,1)/B_Y=O_D(\log(2P)/\log Y)\) uniformly by (1).

If prime variables are scaled by their limiting standard deviations \(\sqrt{p-1}\), the covariance matrix converges to the identity in operator norm for every fixed polylogarithmic prime block. In fact (2) bounds the error in its \((p,q)\) entry by \(C_D\log(2P)/(\log Y\sqrt{(p-1)(q-1)})\). Cauchy–Schwarz then gives operator norm at most \(C_D\log(2P)\sum_{p\le P}(p-1)^{-1}/\log Y\). Even summing over all integers instead of primes yields \(O_D((\log(2P))^2/\log Y)=o(1)\). This is a covariance statement. It does not control unrestricted characters on a growing torus.

## Applying the published shifted theorem to a uniform family

Use Heap–Li–Zhao (HLZ), Theorem 5, §4, p. 1605, with main terms (5) and (24), and declared length \(y=T^{1/4}\). Theorem 4 rewrites the latter expression with a smoothing integral, which is unnecessary here. The shifts are complex and sufficiently small of size \(1/\log T\), as specified at the opening of the proof on p. 1607. For each pair \(m,n\le (\log T)^D\) let \(D_{m,n}=\{d:d\mid m\text{ or }d\mid n\}\). Use four polynomials with real coefficients

\[
 a_{\sigma,\tau}(d)=8\mathbf 1_{d\in D_{m,n}}
       +\sigma\mathbf 1_{d=m}+\tau\mathbf 1_{d=n},
 \qquad \sigma,\tau\in\{-1,1\}.
\]

All coefficients on that divisor-closed support lie in \([6,10]\), including when \(m=n\). Thus \(|a(uv)|\le |a(u)a(v)|\) with constant 1. If \(a(uv)\ne0\), both input coefficients are at least 6. All four arrays obey a common divisor/log majorant, for instance \(\tau_{16}(d)\log d\) for \(d\ge2\), and have bounded initial coefficient \(a(1)\le10\). Here the source's \((\log d)^C\) convention at \(d=1\) is the bounded initial value. The proofs only use this upper bound in divisor sums, so one can write \(\tau_{16}(d)\log(2d)\) to include the initial value. All other declared coefficients up to \(y\) are zero. This construction uses unit monomials, with the factors \(k,l\) in \(Q_k,Q_l\) applied only after the shifted theorem. Padding the coefficients of \(Q_k\) directly by a baseline depending on \(k\) would not give this fixed envelope.

Here is where uniformity of the published \(O(T(\log T)^{-A})\), for any fixed \(A>0\), enters. These are coefficient envelopes in the proof, with \(\theta=1/4\), fixed complex-shift radii, exact submultiplicativity and the preceding fixed divisor/log bound. The initial contour and §4.1 estimates use the uniform pointwise bound on the coefficients, including the first, general coefficient case of Pratt–Robles, Theorem 1.1, in the specialization to the interval given by HLZ. The errors displayed there are powers smaller than \(T\), with this \(\theta\). In §4.2, Lemma 7 bounds the error with fixed envelopes for \(a\) and the shifted convolution \(b\) in (28), the latter bounded by the corresponding divisor convolution as in the source. In §4.3 the error estimates after Perron inversion and the contour shift depend on divisor-majorant sums such as \(\sum_{h\le y}|a(h)|/h\); the printed p. 1612–1613 bounds are \(T\) times an exponential saving in \(\sqrt{\log T}\), allowing any fixed power of \(\log T\) from these sums. No support-size parameter enters these bounds except the common declared length.

For §4.4 take \(\eta=(\log T)^{D+1}\). In its error sum, a term indexed by conductor \(q\) contains \(a(kq)\), hence is zero for \(q>(\log T)^D\). The large-modulus part \(E_2\) is therefore empty for this family. Proposition 10 applies to \(E_1\) with the common coefficient bounds and this fixed power cutoff. Its \(T\exp(-c\sqrt{\log T})\eta^{3/2+\varepsilon}\) bound is uniform across the four arrays. The coefficient dependence in its proof, including Lemma 12, is through the exact submultiplicativity or upper bounds by absolute coefficient divisor sums. Siegel's theorem enters here, so these citations do not give numerical thresholds. The proof of Proposition 11 is not needed for polylogarithmic support. This tracks the uniformity of the published estimate specialized to these arrays. It does not use a constant from a fixed-polynomial asymptotic whose dependence on the polynomial is unspecified. [HLZ journal, Theorem 5, §4.1–4.4 and Proposition 10](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Pratt–Robles, arXiv v3, §1.1–1.2 and Theorem 1.1](../../sources/finite_moment63_uniform/pratt_robles_1706.04593v3.pdf)

For every quadratic expression in the real coefficients in the shifted theorem, apply \(\tfrac18\sum_{\sigma,\tau}\sigma\tau\) to its values at the four arrays. The common padding cancels exactly and the result is the symmetric bilinear expression on \(e_m,e_n\). This applies to the **full** arithmetic main term, before an error is estimated termwise. The four error terms stay uniformly \(O_{A,D}(T(\log T)^{-A})\). On RH, after the two zeta shifts are differentiated, the zero sum on this symmetric pair is \(\sum |\zeta'(\rho)|^2\Re(e_m(\rho)\overline{e_n(\rho)})\). Real coefficients suffice because the desired two-sided zero sum is twice this positive-ordinate real part.

## Uniform arithmetic estimates on the Cauchy circles

Write \(L=\log T\), \(h=m/g\), \(j=n/g\), so the monomial pair selected by polarization has arithmetic weight \(1/(ghj)=1/\operatorname{lcm}(m,n)\), with indices \((h,j)\) and \((j,h)\) averaged. Compare its arithmetic kernel to \((h,j)=(1,1)\), retaining its prefactor \(1/\operatorname{lcm}(m,n)\). Use \(|\alpha|=2c/L\), \(|\beta|=3c/L\), and auxiliary \(|\eta'|=c/L\) for a fixed sufficiently small \(c>0\). Here \(\eta'\) is the source's auxiliary shift, distinct from the conductor cutoff. The polar denominators in the three versions of \(Z\) in (24) are separated from zero by a fixed multiple of \(1/L\), and the auxiliary Cauchy disk contains no such pole. The argument is the same for the interchanged or conjugated shifts, since the bounds depend only on absolute shift sizes and separated radii.

In (5), the factors \(h^{-\beta}j^{-\alpha}\) and \(h^{\alpha}j^{\beta}\) differ from 1 by \(O(\log(hj)/L)\) uniformly. The ordinary Laurent pole factors are \(O(L)\), and for each shift \(u=O(1/L)\),

\[
 \int_0^T (1+|\log(t/(2\pi))|)^a |(t/(2\pi))^u|\,dt\ll T L^a,
 \qquad a=0,1.
\]

The integral at zero converges since \(|\Re u|\) is small. The resulting change of the \(J\)-kernel, before the prefactor, is \(O(TL\log(hj))\).

For (24) there is a uniform local-factor estimate. Let \(\delta\) bound the moduli of all three shifts, so \(\delta=O(1/L)\). For a prime \(p\) denote \(A=p^{-u}\), \(C=p^{-w}\), \(x=p^{-1-v}\). The source's function \(f_{u,w}\) satisfies

\[
 \sum_{b\ge0} f_{u,w}(p^b)t^b=\frac{1-t}{(1-At)(1-Ct)},\qquad
 |f_{u,w}(p^b)-1|\le 2b\,\delta\log p\,p^{b\delta}.
\]

The inequality follows by writing the coefficient as \(A^b+(C-1)\sum_{a=0}^{b-1}A^a C^{b-1-a}\), and bounding each difference from 1 by the exponential integral inequality. The denominator of the local ratio in (24) is \((1-x)/((1-Ax)(1-Cx))\) and its reciprocal is bounded by an absolute constant for \(\delta\le1/8\). For \(e\ge1\), the difference of the local numerator and denominator is bounded by

\[
 \sum_{b\ge0}|f_{u,w}(p^{b+e})-f_{u,w}(p^b)|,|x|^b
 \ll \delta\log p\,p^{e\delta}\sum_{b\ge0}(2b+e)(p^{-1+2\delta})^b
 \ll \delta e\log p\,p^{e\delta}.
\]

For \(p^e\mid j\le L^D\), \(p^{e\delta}\) is uniformly bounded, and the sum of the bounds over \(p^e\parallel j\) is \(O(\delta\log j)\). The Euler product thus differs from 1 by \(O(\delta\log j)\), using \(|\prod(1+r_p)-1|\le\exp(\sum|r_p|)-1\). Including \(h^{-v}\) gives total arithmetic factor \(1+O(\log(hj)/L)\). The remaining factor \(\zeta(1+u+v)\zeta(1+v+w)/\zeta(1+v)\) is \(O(L)\) on these circles. Accordingly the integrand change is \(O(\log(hj))\) times the explicit integrable shift powers. The auxiliary Cauchy derivative costs \(O(L)\) and makes the net change in each \(I\)-kernel \(O(TL\log(hj))\), before the common prefactor. This handles primes of any size in the asserted range, and composite reduced indices as well.

The sum of all main-term comparisons is therefore \(O(TL\log(hj)/\operatorname{lcm}(m,n))\) on the outer Cauchy circles. Apply outer Cauchy directly to the difference between the polarized finite shifted sum and \(1/\operatorname{lcm}(m,n)\) times the untwisted finite shifted sum, both holomorphic. This uses the main-term comparison only where the polar pieces are regular, and costs \(O(L^2)\). The resulting positive-ordinate real cross sum \(A_{m,n}(T)\) satisfies

\[
 A_{m,n}(T)=\frac{A_{1,1}(T)}{\operatorname{lcm}(m,n)}
 + O_{A,D}\!\left(\frac{T L^3\log(mn/g^2)}{\operatorname{lcm}(m,n)}+T L^{2-A}\right). \tag{3}
\]

If a permitted contour height within bounded distance of \(T\) is used, moving back to an arbitrary endpoint changes the polarized sum by \(O(T^{7/8}\log T)\) under RH. Indeed the monomial products have modulus at most 1, the interval's multiplicity is \(O(\log T)\), and the analytic derivative bound is \(O(T^{7/16})\) uniformly. The error is below \(T L^{2-A}\) for each fixed \(A\). This extension also allows real \(T\) at or between zeros, with the right-continuous cumulative sum. [HLZ, formulas (5) and (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Independent unit-window and pointwise derivations](prime_array63_effective_bound_skeptic.md)

For \(T\ge Y\), every \(m,n\le(\log Y)^D\) also lies below \((\log T)^D\). Apply Stieltjes integration against \((T^2+1/4)^{-1}\) to the difference in (3), using its value at \(Y\) for the strict-tail lower endpoint. The boundary term and the integral both preserve the orders \((\log Y)^3/(Y\operatorname{lcm}(m,n))\) and \((\log Y)^{2-A}/Y\), with their displayed factors. This follows from \(\int_Y^\infty t^{-2}(\log t)^u dt\ll_u Y^{-1}(\log Y)^u\) for each fixed real \(u\). The symmetric numerator doubles the positive-ordinate real sum and the untwisted tail doubles by the same factor. Multiply by \(mn/B_Y\) and take \(A>2D+B+2\) to absorb the source remainder. This proves (1).

## An obstruction to uniformity over every prime

For fixed \(Y\) with \(B_Y>0\), the normalized weighted Fourier function \(\phi_Y(t)=B_Y^{-1}\int_{|\gamma|>Y}e^{-it\gamma}\,d\nu(\gamma)\) is continuous at 0 with \(\phi_Y(0)=1\), by dominated convergence. There are arbitrarily large consecutive primes with ratio tending to 1: an eventual lower bound \(1+\varepsilon\) on every consecutive prime ratio would give geometric growth and a convergent reciprocal-prime sum, contrary to Euler. Along such pairs \(p,q\), \(\phi_Y(\log(p/q))\to1\) and \(1/\sqrt{pq}\to0\). Thus the supremum absolute Fourier error over distinct prime pairs is at least 1 for each fixed \(Y\). For the covariance, the same pair sequence gives

\[
 \frac{\mathcal T_Y(Q_p,Q_q)}{B_Y\sqrt{pq}}
 =\phi_Y(\log(p/q))
  -\frac{\phi_Y(\log p)}{\sqrt q}
  -\frac{\phi_Y(\log q)}{\sqrt p}+\frac1{\sqrt{pq}}\ \longrightarrow\ 1,
\]

using symmetry and \(|\phi_Y|\le1\). The prediction for distinct primes is 0, so the supremum error after this variance-scale normalization is at least 1 and the unscaled covariance error has infinite supremum at each such \(Y\). The growing-range estimates above take \(Y\) to infinity while restricting the indices and are compatible with this fixed-\(Y\) obstruction.

The specialization uses the published shifted-moment theorem and the stated RH conversion. It gives asymptotic uniform ranges and makes no publication priority claim. The Pratt–Robles v3 file was inspected for the general coefficient case in §1.1–1.2 and Theorem 1.1. Its SHA-256 is `8f50206351f40b193fb49535fe9839023632731e621f4c625bfff4ce53f35d2e`. [Pratt–Robles v3](https://arxiv.org/pdf/1706.04593v3) · [HLZ journal DOI](https://doi.org/10.2140/ant.2022.16.1589)
