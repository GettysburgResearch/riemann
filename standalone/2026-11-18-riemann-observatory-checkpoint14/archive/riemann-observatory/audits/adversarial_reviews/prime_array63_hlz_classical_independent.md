# Fixed Dirichlet-polynomial derivative moments from Heap–Li–Zhao

Theorem 2 and equations (5)–(9) of [Heap–Li–Zhao, arXiv:2003.09368v1](../../sources/classical63_derivative_moments/hlz2022.pdf) give a small-shift discrete second moment unconditionally. The corresponding journal statement is [Theorem 5, equations (5), (6) and (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf), *Algebra & Number Theory* 16(7), 1589–1625, DOI 10.2140/ant.2022.16.1589. The opening of the proof on printed p.1607 explicitly specifies complex shifts. The calculation below uses this theorem for fixed real Dirichlet polynomials and assumes RH when identifying the reflected product with an absolute square.

## Result and polynomial hypotheses

Let \(Q(s)=\sum_m a_m m^{-s}\) with fixed, finitely supported real coefficients, and set
\[
 S(a,b)=\sum_{m,n}\frac{a_m b_n}{\operatorname{lcm}(m,n)},\qquad S(a)=S(a,a).
\]
On RH, with zeros counted with their multiplicities,
\[
 \sum_{0<\gamma\le T}|\zeta'(\rho)|^2|Q(\rho)|^2
   = \frac{S(a)}{24\pi}T(\log T)^4+O_Q(T(\log T)^3).
 \tag{1}
\]
For two such real coefficient vectors, polarization gives the same formula with \(|Q(\rho)|^2\) replaced by \(\Re(Q_a(\rho)\overline{Q_b(\rho)})\) and \(S(a)\) by \(S(a,b)\). Both signs of the ordinates give twice this real cross-moment. A multiple zero makes a zero contribution because it has \(\zeta'(\rho)=0\).

The source theorem uses a length \(y=T^\theta\) with fixed \(\theta<1/2\), \(|a(mn)|\ll |a(m)a(n)|\), and divisor/logarithm-bounded coefficients. The coefficient bound at \(n=1\) is the finite bounded case, equivalently one can write the majorant with \(\log(2n)\). The literal \((\log 1)^C\) would force every nonzero submultiplicative sequence to vanish. A fixed divisor-closed support with no zero coefficients on it meets the multiplicative bound: if \(a_{mn}\ne0\), then \(a_m,a_n\ne0\), and only finitely many relevant pairs occur. The divisor/log bound is immediate on this fixed support. The length can be \(T^{1/4}\) with all unused coefficients set to zero, for all sufficiently large \(T\).

A general fixed \(a\) can be reduced to such vectors without any additional zero hypothesis. Let \(D\) be the finite divisor closure of its support and let \(b\) be its indicator vector. Choose \(M>\max_m|a_m|\) with \(M>0\). The vectors \(a+Mb,a-Mb,Mb\) have nonzero entries on all of \(D\). For either the shifted sum or the final derivative moment, its quadratic functional \(F\) obeys
\[
 F(a)=\tfrac12\{F(a+Mb)+F(a-Mb)\}-F(Mb).
\]
The same identity holds for \(S\). The constants can depend on the fixed vectors. This step matters for \(Q_k(s)=k^{1-s}-1\) when \(k\) is composite, because its bare two-point support misses the proper factors of \(k\).

## Source main terms and complex shift control

Write \(\ell=\log T\), \(x=\alpha\), \(y=\beta\), \(z\) for the auxiliary shift, \(u=x+y\), and \(\tau=\log(t/(2\pi))\). In (24) use \(h,k\) for the fixed coprime indices. The source's \(Z_{x,y,z,h,k}\) consists of
\[
 \frac{\zeta(1+x+y)\zeta(1+y+z)}{\zeta(1+y)}
\]
times \(h^{-y}\) and the finite product over \(p\mid k\) of ratios of the series with \(f_{x,z}(p^{j+v_p(k)})\) and \(f_{x,z}(p^j)\), both weighted by \(p^{-j(1+y)}\). Here \(f_{x,z}=\mu * (n\mapsto n^{-x})*(n\mapsto n^{-z})\), and \(f_{0,0}(n)=1\). For \(p\mid k\) the two series converge normally in a neighborhood of the origin and have the same nonzero value \((1-p^{-1})^{-1}\) at zero. Indeed the prime-power coefficients are sums of at most \(2j+2v_p(k)+1\) monomials bounded by geometric factors with arbitrarily small exponent as the neighborhood shrinks. Thus the whole extra factor is \(1+O_Q(1/\ell)\) on shifts \(O(1/\ell)\).

Take \(|x|=2c/\ell,\ |y|=3c/\ell,\ |z|=c/\ell\) for a sufficiently small fixed \(c>0\). The same estimates apply with \(x\) and \(y\) interchanged. All Laurent denominators in the three source terms are separated from zero by a constant times \(1/\ell\). For fixed outer shifts, the terms are holomorphic in \(z\) on and inside the inner circle. The Laurent expansions of \(\zeta(1+w)\) and \(1/\zeta(1+w)\) give
\[
 Z_{x,y,z,h,k}=\frac{y}{(x+y)(y+z)}+O_Q(1)
\]
on those circles, with the substituted forms obeying the same error bound. The characters \(h^{-y}\) and the local ratios have already been included in the error. The exponential factors in (24) may grow as \(t\downarrow0\), but their absolute values are bounded by \(\exp(O(c|\tau|/\ell))\). For \(j=0,1\),
\[
 \int_0^T (1+|\tau|)^j e^{O(c|\tau|/\ell)}\,dt\ll_j T\ell^j.
\]
This follows from integrability at zero once \(\ell\) is large and from \(|\tau|\ll\ell\) between \(1\) and \(T\).

The \(J\) integrand of (5), including its factor \(\tau\), has leading expression
\[
 J_0(x,y;\tau)=\tau\,\frac{1-e^{-u\tau}}{u}.
\]
The error in its integral is \(O_Q(T\ell)\) on the outer circles, since both \(h,k\) are fixed and their shift powers differ from \(1\) by \(O_Q(1/\ell)\). Under the integral for \(I\), the leading expression prior to differentiation in \(z\) is
\[
 K_0(x,y,z;\tau)=
 \frac{y}{u(y+z)}
 +e^{-u\tau}\frac{x}{u(z-x)}
 +e^{-(y+z)\tau}\frac{z}{(x-z)(y+z)}.
\]
The sign in the second term comes from substituting \((-y,-x,z)\) into \(Z\). The third uses \((x,-z,-y)\) and its associated exponential. The integrated error here before the \(z\) derivative is \(O_Q(T)\). Cauchy's formula on the inner circle then gives \(O_Q(T\ell)\) after that derivative. Directly,
\[
 \partial_z K_0(x,y,0;\tau)
 =-\frac{1}{uy}-\frac{e^{-u\tau}}{ux}+\frac{e^{-y\tau}}{xy}.
\]
Consequently, after including both permutations in the source theorem,
\[
 I_0(x,y;\tau)+I_0(y,x;\tau)
 =-\frac{(1-e^{-x\tau})(1-e^{-y\tau})}{xy}.
\]
This total and \(J_0\) extend holomorphically across the apparent poles. The factor on the main integrals is
\[
 \sum_{g,h,k:\,(h,k)=1}\frac{a_{gh}a_{gk}}{ghk}=S(a),
\]
because \(g=\gcd(gh,gk)\) and \(ghk=\operatorname{lcm}(gh,gk)\).

Let \(F_T(x,y)\) be the source's shifted finite sum and \(H_T(x,y)\) the integral of \(S(a)(J_0+I_0+I_0^{\mathsf T})/(2\pi)\). The calculations give \(F_T-H_T=O_Q(T\ell)+O_{Q,A}(T\ell^{-A})\) on the outer product of circles, where the latter term is the source error. Both \(F_T\) and \(H_T\) are holomorphic inside those circles. The outer double Cauchy formula therefore gives \(O_Q(T\ell^3)\) from the leading-term truncation and \(O_{Q,A}(T\ell^{2-A})\) from the source error for the mixed derivative at zero. This argument only compares the source's polar pieces on their regular torus and uses the explicit holomorphic \(H_T\) when applying the outer formula.

The coefficient of \(xy\) in \(J_0\) is \(\tau^4/3\), from the \(u^2\tau^4/6\) term. The coefficient in \(I_0+I_0^{\mathsf T}\) is \(-\tau^4/4\). Their sum is \(\tau^4/12\), and
\[
 \int_0^T \tau^4\,dt=T(\log T)^4+O(T(\log T)^3).
\]
Meanwhile the derivative of \(F_T\) is the sum of \(\zeta'(\rho)\zeta'(1-\rho)Q(\rho)Q(1-\rho)\). On RH, \(1-\rho=\bar\rho\), so real \(Q\) coefficients identify it with the left side of (1). If using the proof's contour-height convention, select a permitted contour height within \(O(1)\) of \(T\). The unit-interval zero count is \(O(\log T)\) and the pointwise RH bound gives \(\zeta'(\rho)=O_\epsilon(T^\epsilon)\) there, so the change is absorbed by \(O_Q(T\ell^3)\). The derivative bound follows by Cauchy in a radius \(1/\log T\), using Lindelöf on the right and the functional equation on the left. Thus (1) holds for general large real \(T\).

## The factorial weights and the two-sided tail

For \(k,l\ge1\), inserting \(Q_k(s)=k^{1-s}-1\) and \(Q_l(s)=l^{1-s}-1\) gives
\[
 S(Q_k,Q_l)=1-1-1+\frac{kl}{\operatorname{lcm}(k,l)}
 =\gcd(k,l)-1.
\]
This includes \(Q_1=0\) and \(S(Q_k)=k-1\). In particular \(S(Q_2)=1\).

For the positive-ordinate real mixed partial sum \(A(t)=C\,t(\log t)^4+O(t(\log t)^3)\), with \(C=S(a,b)/(24\pi)\), partial summation against \(g(t)=(t^2+1/4)^{-1}\) gives
\[
 -A(Y)g(Y)+\int_Y^\infty A(t)\frac{2t}{(t^2+1/4)^2}\,dt
 =C\frac{(\log Y)^4}{Y}+O\!\left(\frac{(\log Y)^3}{Y}\right).
\]
In particular the boundary term subtracts one copy and the integral supplies two copies of the leading coefficient. Conjugate zeros supply the second copy of the positive-ordinate tail, giving
\[
 \sum_{|\gamma|>Y}
 \frac{|\zeta'(\rho)|^2 Q_a(\rho)\overline{Q_b(\rho)}}{|\rho|^2}
 =\frac{S(a,b)}{12\pi}\frac{(\log Y)^4}{Y}
   +O_{a,b}\!\left(\frac{(\log Y)^3}{Y}\right).
\]
For \(\gcd(k,l)=1\) the leading term vanishes, and the formula retains its absolute error interpretation. Its constants are asymptotic and depend on the fixed polynomial data. It supplies no uniform estimate as \(k,l\) increase and no explicit remainder constants for a numerical enclosure.

## Check against Gonek

[Gonek 1984, Corollary 1, p.124, equation (6)](../../sources/classical63_lfunctions/gonek1984.pdf) gives the unnormalized sum for \(\mu=1,\alpha=0\) with prefactor \(1/3-1/8-1/8=1/12\) times \(T/(2\pi)\) and log-power \(2\mu+2=4\). Its error power is \(2\mu+1=3\). This agrees with (1) for \(Q=1\), \(S=1\). Dividing by \(N(T)\sim T\log T/(2\pi)\) gives the average \((\log T)^3/12\). An earlier draft of the companion reading notes assigned the normalized log-power to the raw sum and its tail. The corrected exponents are recorded there.
