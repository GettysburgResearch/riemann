# Heap–Li–Zhao and the derivative-weighted prime-array tail

Date 2026-11-17. I checked the shifted mean value in Heap–Li–Zhao arXiv v1, Theorem 2 and equations (5)–(9), and in the journal, Theorem 4 with (4)–(6) and Theorem 5 with (24). For the fixed twist \(Q_k(s)=k^{1-s}-1\), their formula gives the differentiated mixed moment unconditionally. On RH its absolute-square form is
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2|Q_k(\rho)|^2
  =\frac{k-1}{24\pi}\,T(\log T)^4+O_k(T(\log T)^3).
 \tag{1}
\]
Consequently the two-sided ordinate tail in the factorial-array constant is
\[
 \sum_{|\gamma|>Y}
       \frac{|\zeta'(\rho)|^2|Q_k(\rho)|^2}{|\rho|^2}
  =\frac{k-1}{12\pi}\,\frac{(\log Y)^4}{Y}
       +O_k\!\left(\frac{(\log Y)^3}{Y}\right).
 \tag{2}
\]
In particular the factor in (2) for \(k=2\) is \(1/(12\pi)\). The audit reproduces the specialization at fixed polynomial length and does not establish independent error constants for the general mean-value theorem. [Author v1, pp. 3–5](https://arxiv.org/pdf/2003.09368v1) · [Journal, pp. 1592–1593 and 1605–1607](https://doi.org/10.2140/ant.2022.16.1589) · [Factorial-array error constant](jump_factorial_prime_array63_proponent.md)

## Hypotheses, shifts, and differentiation

The inspected primary PDF hashes are \(\texttt{73c78d922741658678023e73bd0684c1003261906ccc97b48f2e727f5874f6f6}\) for the arXiv v1 and \(\texttt{6162632530cbeee8c1664d7ea53e844cffa9dbc53fe00a8cd8270e2d713b6a82}\) for the journal. The arXiv statement uses \(I(\alpha,\beta,T)+\overline{I(\bar\beta,\bar\alpha,T)}+J(\alpha,\beta,T)\) in (9), with the same conjugation in the journal. The conjugation bars are visible in the page images and matter for arbitrary complex coefficients. In print Theorem 5 is in §4, on p. 1605, with the same \(I\) in (24) and \(J\) in (5) on p. 1592. Theorem 4 rewrites \(I\) in terms of the smoothed diagonal expression \(L\). Formula (24) is the convenient one here, so no auxiliary smoothed-diagonal cutoff \(w\) or choice of its \(H\) needs to be differentiated. [Local v1](../../sources/classical63_derivative_moments/hlz2022.pdf) · [Local journal](../../sources/classical63_derivative_moments/hlz2022print.pdf)

The source assumes \(|a(mn)|\ll |a(m)a(n)|\) and \(|a(n)|\ll\tau_r(n)(\log n)^C\), with fixed \(r,C>0\), in a Dirichlet polynomial up to \(y=T^\theta\), fixed \(\theta<1/2\). The two-point coefficients \(a(1)=-1\), \(a(2)=2\) satisfy the submultiplicative bound with constant 1. For composite \(k\) the two-point coefficients of \(Q_k\) fail that bound when \(mn=k\) and \(m,n>1\). The parallelogram reduction below handles this and other fixed coefficient patterns using admissible inputs. The divisor/log bound holds for \(n\ge2\) with fixed coefficients, and the source itself uses arrays with nonzero \(a(1)\), so its log-bound notation uses the usual convention of a bounded initial value at that index. Taking \(\theta=1/4\) and padding by zeros puts any fixed support in the required interval for all sufficiently large \(T\).

The two-shift theorem for the stated coefficient class is unconditional. On p. 1593 the authors explicitly distinguish the earlier GLH-dependent method and their separate GRH variant for more general coefficients. The negative-moment Theorem 1 assumes RH and simplicity. Those hypotheses are unrelated to applying Theorem 5 to \(Q_2\). The proof on p. 1607 describes the shifts as complex and small \(\ll1/\log T\). Its residue contour contains
\[
 \frac{\zeta'(s)}{\zeta(s)}
       \zeta(s+\alpha)\zeta(1-s+\beta)Q(s)\overline Q(1-s),
\]
where \(\overline Q\) conjugates coefficients. The residue of \(\zeta'/\zeta\) is the zero multiplicity, so the mean value is over zeros counted with multiplicity. The polynomial arguments are unshifted. This verifies the positions of the twists and shows why no derivative of the polynomial is taken. [Journal, remarks on p. 1593 and contour on p. 1607](https://doi.org/10.2140/ant.2022.16.1589)

Write \(\mathcal F_Q(\alpha,\beta;T)\) for the finite shifted sum, and \(M_Q=J_Q+I_Q(\alpha,\beta,T)+\overline{I_Q(\bar\beta,\bar\alpha,T)}\) for Theorem 5's main term. For each large \(T\), the finite sum is holomorphic in a neighborhood of \((0,0)\). Put \(\ell=\log T\). Choose a sufficiently small fixed \(c>0\) within the source's uniform shift range and take \(|\alpha|=c/\ell\), \(|\beta|=2c/\ell\). These distinct radii keep \(\alpha,\beta,\alpha+\beta\) away from zero. The exact two-variable Cauchy identity gives
\[
 \partial_\alpha\partial_\beta\mathcal F_Q(0,0;T)
  =\frac{1}{(2\pi i)^2}
     \iint\frac{M_Q(\alpha,\beta;T)}{\alpha^2\beta^2}\,d\alpha\,d\beta
      +O_A(T\ell^{-A+2}).
 \tag{3}
\]
The two inverse radii account for the \(+2\). This contour version uses the main expression only at regular shifts and avoids any need to separately differentiate its apparent poles. The differentiated finite sum is exactly
\[
 \sum_{0<\gamma\le T}
       \zeta'(\rho)\zeta'(1-\rho)Q(\rho)\overline Q(1-\rho).
 \tag{4}
\]
With a convention in which \(Q\) were shifted together with its zeta factor, \((\zeta Q)'(\rho)=\zeta'(\rho)Q(\rho)\) would still hold by \(\zeta(\rho)=0\), and analogously at \(1-\rho\). Under RH, \(1-\rho=\bar\rho\), so (4) is \(\sum|\zeta'(\rho)|^2|Q(\rho)|^2\). Multiple zeros have zero contribution. The Cauchy differentiation in (3)–(4) does not require RH, GLH, or simplicity.

## Leading factor for the fixed polynomial

First take a fixed coefficient array satisfying the source hypotheses. One can extract the leading term by comparing the main expressions for \(Q\) and for \(Q=1\), avoiding evaluation of the universal shifted kernel. Keep the two nested circles above and write \(\eta\) for the auxiliary shift denoted \(\gamma\) in the arithmetic main term. Take \(|\eta|=c/(4\ell)\) when computing its derivative in (24). Each pair sum occurring in the zeta poles of the three terms
\[
 Z_{\alpha,\beta,\eta;h,j},\qquad
 Z_{-\beta,-\alpha,\eta;h,j},\qquad
 Z_{\alpha,-\eta,-\beta;h,j}
\]
has modulus bounded below by a fixed multiple of \(1/\ell\). For fixed \(\alpha,\beta\) on their circles those pole arguments do not meet zero inside the small \(\eta\) circle either. The reciprocal denominator factor \(1/\zeta(1+v)\) in the global ratio is holomorphic at \(v=0\), with a zero there. Thus the auxiliary derivative is an ordinary Cauchy derivative. For these specific fixed coefficients no further prime factors become singular at the origin.

The finitely many pairs \((h,j)\) in (5) and (24) are obtained by writing \(m=gh\), \(n=gj\), \((h,j)=1\), with \(m,n\in\operatorname{supp}a\). Their common weight is \(a(m)\overline{a(n)}/(ghj)=a(m)\overline{a(n)}/\operatorname{lcm}(m,n)\). Define
\[
 C(Q)=\sum_{m,n}\frac{a(m)\overline{a(n)}}{\operatorname{lcm}(m,n)}.
\]
The factors \(h^{-\beta}j^{-\alpha}\) and \(h^\alpha j^\beta\) in \(J_Q\) equal \(1+O_Q(\ell^{-1})\) uniformly on the circles. The zeta poles are \(O(\ell)\), and the integral of
\(\big|\log(t/(2\pi))(t/(2\pi))^u\big|\) over \(0<t<T\) is \(O(T\ell)\) uniformly for \(u=O(\ell^{-1})\). This uses direct integration at \(0<t<1\) and the bound \(\big|(t/(2\pi))^u\big|\ll1\) on \(1\le t\le T\). Thus
\[
 J_Q-C(Q)J_1=O_Q(T\ell).
 \tag{5}
\]

For \(I_Q\), the \(h,j\)-dependence of \(Z_{u,v,w;h,j}\) in (24) is a factor \(h^{-v}\) and finitely many local ratios. At \((u,v,w)=(0,0,0)\) each local ratio is 1. Indeed \(f_{0,0}=\mu*1*1=1\), so the numerator with exponent \(m+j_p\) and the denominator with \(m\) both sum \(\sum_{m\ge0}p^{-m}\). The local series converge uniformly in a small fixed polydisk, and their denominators are nonzero near its center by this value. Therefore the total \(h,j\)-dependent factor is \(1+O_Q(\ell^{-1})\) on the three small contours. The \(h=j=1\) ratio
\[
 Z_{u,v,w;1,1}
   =\frac{\zeta(1+u+v)\zeta(1+v+w)}{\zeta(1+v)}
\]
is \(O(\ell)\) there, with two numerator factors of order at most \(\ell\) and the reciprocal of order at most \(1/\ell\). Consequently replacing the local factors by 1 makes \(O_Q(1)\) error in each \(Z\) before the auxiliary derivative. The factors \((t/(2\pi))^u\), \(u=O(\ell^{-1})\), are uniformly integrable with integral \(O(T)\). Cauchy's derivative in \(\eta\) then makes the total error \(O_Q(T\ell)\), for each order of the two main shifts. The same estimate holds with conjugated shifts and outer conjugation. The common diagonal factor \(C(Q)\) is real by symmetry in \(m,n\), so the outer conjugation preserves that factor. In particular
\[
 M_Q-C(Q)M_1=O_Q(T\ell)
\]
on the two main contours. Using Theorem 5 for \(Q\) and \(1\), and applying the \(\alpha,\beta\) Cauchy formulas to the difference, proves that (4) equals \(C(Q)\) times the unweighted mixed derivative moment, up to \(O_Q(T\ell^3)\). The comparison uses fixed support throughout, so it does not assert the same leading factor for a growing twist. The choice of a nearby good contour height in the proof of the source theorem is harmless here. Under RH the change over a bounded displacement of the endpoint contributes at most \(O_Q(T^{7/8}\log T)\), by the unit-window count and the critical-line derivative bound in the effective array proof. [Source equations (5), (6), (24)](https://doi.org/10.2140/ant.2022.16.1589) · [Explicit critical-line derivative and zero-count bounds](prime_array63_effective_bound.md)

An arbitrary fixed Dirichlet polynomial \(Q\) can be recovered from admissible inputs. Fix \(M\) containing its support, and take \(P(s)=B\sum_{n\le M}n^{-s}\) for \(B\ge4\) with \(\max_n|a(n)|\le B/4\). The nonzero coefficients of \(P\) and \(P\pm Q\) have moduli between \(3B/4\) and \(5B/4\), and all indices \(1\le n\le M\) occur. For \(mn\le M\) the product of the two input moduli is at least \((3B/4)^2\ge5B/4\). For \(mn>M\) the output is zero. This gives even the exact submultiplicative inequality used in the proof of the source theorem. The divisor/log bound is automatic on this fixed support. At every shift the diagonal quadratic expressions for \(P+Q\) and \(P-Q\), minus twice the expression for \(P\), give twice the expression for \(Q\). The same parallelogram identity holds for \(C\). Hence the asymptotic comparison extends to arbitrary fixed \(Q\) with constants allowed to depend on its coefficients and support. In particular the four summands for \(Q_k=k\,k^{-s}-1\) are \(1,-1,-1,k\), so \(C(Q_k)=k-1\) for every fixed \(k\ge2\).

## Gonek's exponent and the tail

I inspected the page image of Gonek's Corollary 1, p. 124, equations (5)–(6), SHA-256 \(\texttt{dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3}\). At \(\mu=1\), \(\alpha=0\), the coefficient in (6) is \(1/3-2(1/8)=1/12\) relative to \(T/(2\pi)\). The printed logarithmic power is \(2\mu+2=4\), with error power \(2\mu+1=3\). Thus on RH
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2
   =\frac{T(\log T)^4}{24\pi}+O(T(\log T)^3).
\]
The \(1/12\) times \((\log T)^3\) scale is for the average after division by the zero count. The exponent 3 for the raw moment in the preceding derivative-moment notes is one power too small. Combining Gonek's stated raw asymptotic and the comparison proves (1) for every fixed \(k\ge2\). [Gonek, pp. 123–124](https://doi.org/10.1007/BF01403094) · [Local p. 124 scan](../../sources/classical63_lfunctions/gonek1984.pdf#page=2)

Let \(A_Q(t)\) denote the one-sided accumulated moment in (1). For \(Y\) large, Stieltjes integration by parts with the lower endpoint included in \(A_Q(Y)\) gives the strict tail
\[
 \sum_{\gamma>Y}
       \frac{|\zeta'(\rho)|^2|Q(\rho)|^2}{1/4+\gamma^2}
 =
 -\frac{A_Q(Y)}{Y^2+1/4}
 +\int_Y^\infty\frac{2t A_Q(t)}{(t^2+1/4)^2}\,dt.
\]
If \(c_Q=(k-1)/(24\pi)\), the boundary term is
\(-c_Q(\log Y)^4/Y+O_k((\log Y)^3/Y)\). The integral is
\(2c_Q(\log Y)^4/Y+O_k((\log Y)^3/Y)\), using
\(\int_Y^\infty(\log t)^4t^{-2}dt=(\log Y)^4/Y+O((\log Y)^3/Y)\).
The equal negative-ordinate tail doubles the leading term, proving (2). Any multiple zero can be included with its multiplicity because the summand vanishes. Gonek's untwisted theorem and the bound \(|Q_k(\rho)|\le1+\sqrt k\) already suffice for an order-of-magnitude \(O_k((\log Y)^4/Y)\). The asymptotic constants here do not replace the elementary explicit all-\(N\) error bound for the prime array.

## Polarization and the rational phase limit

For fixed \(Q(s)=\sum a_m m^{-s}\) and \(R(s)=\sum b_n n^{-s}\), define
\[
 C(Q,R)=\sum_{m,n}
       \frac{a_m\overline{b_n}}{\operatorname{lcm}(m,n)}.
\]
On RH the derivative-weighted moment is a sesquilinear form, linear in \(Q\). Its value on \((Q,R)\) is one quarter of the difference of its diagonal evaluations at \(Q+R,Q-R\), plus \(i/4\) times the difference at \(Q+iR,Q-iR\). Apply the already proved fixed-polynomial diagonal estimates to these four polynomials. The result is
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2 Q(\rho)\overline{R(\rho)}
   =\frac{C(Q,R)}{24\pi}T(\log T)^4
       +O_{Q,R}(T(\log T)^3).
\]
Stieltjes integration gives the corresponding positive-ordinate tail with leading constant \(C(Q,R)/(24\pi)\). For complex coefficients the negative-ordinate tail is the conjugate of the positive-ordinate tail for \((\overline Q,\overline R)\), where bars on polynomials conjugate coefficients. Its leading constant is also \(C(Q,R)/(24\pi)\). Thus the full signed tail has expansion
\[
 \mathcal T_Y(Q,R):=
 \sum_{|\gamma|>Y}\frac{|\zeta'(\rho)|^2 Q(\rho)\overline{R(\rho)}}{|\rho|^2}
 =
 \frac{C(Q,R)}{12\pi}\frac{(\log Y)^4}{Y}
      +O_{Q,R}\!\left(\frac{(\log Y)^3}{Y}\right).
 \tag{6}
\]

The common factor is a divisor-sum form. Since
\(\operatorname{lcm}(m,n)^{-1}=\gcd(m,n)/(mn)\) and
\(\gcd(m,n)=\sum_{d\mid m,\ d\mid n}\varphi(d)\),
\[
 C(Q,R)=\sum_d\varphi(d)
       \left(\sum_{d\mid m}\frac{a_m}{m}\right)
       \overline{\left(\sum_{d\mid n}\frac{b_n}{n}\right)}.
\]
For \(Q_k=k\,k^{-s}-1\), its inner divisor sum is zero at \(d=1\), one at \(d>1\) dividing \(k\), and zero otherwise. Hence \(C(Q_k,Q_l)=\gcd(k,l)-1\). In particular, for distinct fixed primes the mixed tail is \(O_{k,l}((\log Y)^3/Y)\), whereas the two diagonal tails have positive \((\log Y)^4/Y\) leading constants. Their inner product divided by the product of their tail norms tends to zero.

Let \(B_Y=\mathcal T_Y(1,1)\) and, for real \(u\), set
\[
 F_Y(u)=\sum_{|\gamma|>Y}
    \frac{|\zeta'(\rho)|^2}{|\rho|^2}e^{i\gamma u}.
\]
For fixed positive integers \(m,n\), take \(Q(s)=n^{-s}\), \(R(s)=m^{-s}\) in (6). The left side is \(F_Y(\log(m/n))/\sqrt{mn}\). Dividing by the untwisted tail yields
\[
 \lim_{Y\to\infty}\frac{F_Y(\log(m/n))}{B_Y}
   =\frac{\gcd(m,n)}{\sqrt{mn}}
   =\prod_{p}p^{-|v_p(m/n)|/2}.
 \tag{7}
\]
The ratio depends only on the reduced rational number. This statement fixes \(m,n\) before passing to the limit.

There is a probability limit on the compact group of prime angles. Map an ordinate \(\gamma\) to \((e^{i\gamma\log p})_p\), with probability weights proportional to \(|\zeta'(\rho)|^2/|\rho|^2\) in the tail. The character indexed by \(r\in\mathbb Q_{>0}^{\times}\) is the finite product of the coordinate powers \(v_p(r)\). Formula (7) gives all its limiting moments. They are those of the product over primes of the normalized Poisson kernel laws
\[
 \frac{1-p^{-1}}{1-2p^{-1/2}\cos\theta+p^{-1}}\,
     \frac{d\theta}{2\pi}.
\]
Each one-coordinate Fourier coefficient is \(p^{-|j|/2}\). The finite-coordinate trigonometric polynomials are uniformly dense in the continuous functions on the compact product by Stone–Weierstrass. Thus the prime-angle measures converge weakly to that product law. Equivalently this is the compact dual of the positive rationals with the discrete multiplicative topology.

In the ordinary real topology the limiting values specified by (7) are discontinuous at \(u=0\). For \(r_m=(m+1)/m\), \(\log r_m\to0\) and the value is \(1/\sqrt{m(m+1)}\to0\), while the value at zero is 1. In the real ordinate variable the probabilities used above escape to infinity, since their support is outside \([-Y,Y]\). The product limit on prime angles therefore gives no weak probability limit on the real ordinate axis.
