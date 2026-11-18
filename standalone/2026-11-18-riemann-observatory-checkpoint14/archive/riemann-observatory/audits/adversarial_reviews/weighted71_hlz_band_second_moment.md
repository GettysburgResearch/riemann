# Second moments on power-scale prime bands

Assume RH, and use the strict two-sided derivative-weighted tail law. Fix \(0<a<b<1/4\), put \(L=\log Y\), and define
\[
 W_Y=\sum_{Y^a<p\le Y^b}p^{-1/2}\cos(\gamma\log p).
\]
The expectation tends to \(M_{a,b}=\log(b/a)-4(b-a)+\frac23(b^3-a^3)\). The limiting variance is
\[
 \boxed{\ \frac12\log(b/a)-4(b-a)^2
      +4(b-a)(b^3-a^3)-\frac49(b^3-a^3)^2\ }.
\]
It is strictly below the independent Poisson-phase variance \(\frac12\log(b/a)\). The difference arises from off-diagonal covariance between distinct primes. This is a second-moment result. [HLZ original, Theorems 4–5](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Cutoff and aggregate remainder audit](weighted70_hlz_cutoff_review.md)

## Local kernels

For a prefix ending at \(T\ge Y\), put \(L_T=\log T\), \(x=\log p/L_T\), and \(y=\log q/L_T\). Consider distinct primes \(p,q\). In HLZ (24) use Cauchy shifts scaled by \(1/L_T\), and denote the scaled shifts in an ordered residue by \((u,v,w)\). Set
\[
 A(x;u,w)=e^{-ux}+e^{-wx}-1.
\]
A prime in reduced index \(h\) contributes \(e^{-vx}\). A prime in reduced index \(k\) to first power contributes \(A(x;u,w)+O(1/p)\). Indeed the exact quotient is
\[
 V+(U-1)\frac{1-Vz}{1-z}
 = V+U-1+\frac{(U-1)(1-V)z}{1-z},
 \qquad U=e^{-ux},\quad V=e^{-wx},\quad z=p^{-1-v/L_T}.
\]
The error can be bounded by \(O(x^2/p)\) on these fixed scaled circles. All other factors are bounded uniformly for \(x,y\le b\). Polarization averages the two orders of the reduced index pair. The resulting ordered-factor averages for the ratio \(p/q\) and product \(pq\) are respectively
\[
 \frac{e^{-vx}A(y;u,w)+e^{-vy}A(x;u,w)}2,\qquad
 \frac{e^{-v(x+y)}+A(x;u,w)A(y;u,w)}2.
\]
Each has an error \(O(1/p+1/q)\). These are distinct arithmetic cases in (24). Quotients with repeated primes, needed only in the product diagonal, use the exact prime-power formula in the previous audit.

For clarity, let \(H,K\) be the ordered lists of scaled prime logs in the reduced indices, with sums \(X,Z\). In (5) the two ordered contributions and their real polarization give the leading scaled kernel
\[
 \frac{e^{-\beta X-\alpha Z}+e^{-\beta Z-\alpha X}
    -e^{-\alpha-\beta+\alpha X+\beta Z}
    -e^{-\alpha-\beta+\alpha Z+\beta X}}{2(\alpha+\beta)}.
\]
In (24) a term with scaled tuple \((u,v,w,\lambda)\) gives the leading kernel
\[
 \frac{v e^\lambda}{(u+v)(v+w)}
 \frac{e^{-vX}\prod_{z\in K}A(z;u,w)
       +e^{-vZ}\prod_{z\in H}A(z;u,w)}2.
\]
The three tuples are \((\alpha,\beta,\xi,0)\), \((-\beta,-\alpha,\xi,-\alpha-\beta)\), and \((\alpha,-\xi,-\beta,-\beta-\xi)\), plus the reflected set with \(\alpha,\beta\) exchanged. The scaling factors before differentiation are \(TL_T^2/(2\pi)\) in (5) and \(TL_T/(2\pi)\) in (24), together with the arithmetic factor \(1/\operatorname{lcm}(m,n)\). Dividing each time integral by \(T\) replaces the scaled time power by \(e^\lambda+O(1/L_T)\), because its exact integral is \(e^\lambda (2\pi)^{-\lambda/L_T}/(1+\lambda/L_T)\). The (5) logarithm supplies an additional factor \(L_T(1+O(1/L_T))\) already included in the scaling. Laurent expansion of the zeta quotient is uniform on the separated Cauchy tori. The derivative scaling then gives \(TL_T^4/(2\pi)\) in both cases. On the ratio and product pairs the error in this leading per-pair kernel is \(O(L_T^{-1}+p^{-1}+q^{-1})\) relative to that scaling with the arithmetic factor retained.

The mixed derivative of (5) uses the cubic exponential terms, because division by \(\alpha+\beta\) reduces homogeneous degree by one. In (24) the auxiliary derivative \(\partial_\xi\) is additional, so the quartic terms are needed. No singular denominator invalidates this degree extraction. Simultaneously rotating all Cauchy variables preserves the separated tori, and integrates every nonmatching homogeneous degree to zero. For the surviving term the auxiliary derivative at zero is legitimate first in the disk \(|\xi|<\min(|\alpha|,|\beta|)\), where all relevant denominators avoid zero or cancel. The remaining mixed derivatives after combining the reflected terms are polynomial. Their coefficients from (5) and (24) with reflection are, respectively,
\[
\begin{array}{c|cc}
 &J&I+\text{reflection}\\ \hline
p/q&
 (x+y-1)(x^2-4xy+x+y^2+y-2)/6&
 -(2x^3y+6x^2y^2-6x^2y+2xy^3-6xy^2-2x-2y+3)/12\\
pq&
 (x+y-1)^2(x+y+2)/6&
 -(2x^3y-6x^2y^2+6x^2y+2xy^3+6xy^2-12xy-2x-2y+3)/12 .
\end{array}
\]
The untwisted mixed coefficient is \(1/12\). Thus, defining \(F(x)=1-4x+2x^3\) and \(K_0(x,y)=F(x)+F(y)-1+12xy-2xy(x^2+y^2)\), the normalized leading kernels are
\[
 K_{\rm ratio}(x,y)=K_0(x,y)-6x^2y^2,\qquad
 K_{\rm product}(x,y)=K_0(x,y)+6x^2y^2.
\]
The normalization refers to each coefficient after retaining its arithmetic factor inside the aggregate main term. It does not assert that the source remainder is relatively small for every individual polynomial-size twist. [Independent exact symbolic extraction](../../scripts/weighted71_hlz_covariance_kernels.py)

## Aggregate prefix and tail transfer

Let \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\). Use
\[
 W_Y^2=\tfrac12|D(\rho)|^2+\tfrac12\Re D(\rho)^2 .
\]
Apply the aggregate HLZ formula for \(|D|^2\), to the cross term for \(D^2\) and \(1\), and to the cross term for \(D\) and \(1\) for the mean. The support bound \(Y^{2b}\) permits a fixed declared exponent \(2b<\delta<1/2\) at every \(T\ge Y\). The divisor-closed pads of the prior audit have fixed bounded coefficients, since \(D^2\) has coefficients at most 2. The error \(O_A(TL_T^{-A})\) in HLZ is applied to the aggregate quadratic forms before the Cauchy derivatives. Consequently the normalized error is an arbitrarily small fixed log power without a factor for the number of primes. The comparison here uses HLZ Theorem 5, formula (5), and (24), without the diagonal smoothing lemma. [Primary source, pp. 1592 and 1605](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Bounded coefficient and source uniformity](weighted70_hlz_cutoff_review.md)

For \(|D|^2\), the diagonal \(p=q\) contributes \(p^{-1}\) times the exact untwisted derivative moment, since \(|p^{-\rho}|^2=p^{-1}\) under RH. For \(D^2\), the repeated-prime term has twist \(p^2\) against \(1\), arithmetic factor \(1/p^2\), and a bounded normalized local kernel by the prime-power quotient. Its aggregate main term is \(O(\sum_{p>Y^a}p^{-2})=o(1)\). For distinct primes both ratio and product have arithmetic factor \(1/(pq)\). In the product sum \(D^2\) the two ordered ways to obtain \(pq\) coincide with summing over the two ordered pairs \(p,q\) and \(q,p\). Thus for the weighted prefix expectations
\[
\begin{aligned}
 E_T W_Y
  &=\sum_{Y^a<p\le Y^b}\frac{F(\log p/L_T)}p+o(1),\\
 E_T W_Y^2
  &=\frac12\sum_{Y^a<p\le Y^b}\frac1p+
 \sum_{\substack{Y^a<p,q\le Y^b\\p\ne q}}
  \frac{K_0(\log p/L_T,\log q/L_T)}{pq}+o(1).
\end{aligned}
\]
The errors tend to zero uniformly over \(T\ge Y\). In fact the reciprocal prime mass of the band is bounded, the finite-prime factor errors cost \(O(Y^{-a})\), and the scaled zeta and time-power error costs \(O(1/\log Y)\) times bounded reciprocal mass. The Gonek untwisted prefix asymptotic supplies the exact denominator up to relative \(O(1/L_T)\). The ordinary HLZ version suffices. In the effective variant remove the one exceptional prime before all quadratic evaluations, as in the cutoff audit. If the excluded prime lies in this band it is above \(Y^a\), and the omitted summand has magnitude at most \(Y^{-a/2}\). The omitted term can be restored using bounded second moments, with error \(O(Y^{-a/2})\), so the final statistic is fixed across all prefixes.

For \(Y\le T\le Y e^{\sqrt L}\), the coordinates \(\log p/L_T\) differ uniformly from \(\log p/L\) by \(O(L^{-1/2})\). All kernels are polynomial on a fixed compact box, so this replacement changes the prefix formulas by \(o(1)\). Beyond that point the same prefix formulas give bounded first and second moments. For the strict tail, partial summation of a prefix \(A_f(T)\) against \(k(t)=(t^2+1/4)^{-1}\) gives \(-k(Y)A_f(Y)-\int_Y^\infty k'(t)A_f(t)\,dt\). The far range of the integral carries \(O(e^{-\sqrt L}(L+\sqrt L)^4/Y)\) by the bound \(A_1(T)\ll T\log^4 T\) for the untwisted prefix mass, and is \(o(1)\) after division by the full tail mass. The same is true for differences between any of the preceding moment formulas and the corresponding fixed reciprocal sums. The boundary term at \(Y\) enforces the strict convention. Conjugation yields the same real moment on both sides. [Strict-tail normalization](uniform64_hlz_third_review.md)

## Covariance and positivity

The prime reciprocal measures \(\sum_{Y^a<p\le Y^b}p^{-1}\delta_{\log p/L}\) converge weakly to \(dx/x\) on \([a,b]\), by the prime reciprocal Mertens asymptotic on subintervals. The omitted diagonal mass in tensor-product sums is \(o(1)\). Subtracting the squared mean leaves the ordinary off-diagonal correction
\[
 C(x,y)=K_0(x,y)-F(x)F(y)
       =-4xy+6x^3y+6xy^3-4x^3y^3 .
\]
Integration gives
\[
 \operatorname{Var}W_Y\longrightarrow
 \tfrac12\log(b/a)+\int_a^b\int_a^b C(x,y)\frac{dx\,dy}{xy}.
\]
The independent Poisson-phase variance at finite \(Y\) is \(\tfrac12\sum_{Y^a<p\le Y^b}(1/p-1/p^2)\), tending to its diagonal term. The correction is strictly negative on any nonempty band in this range since \(C=-4xy[1-\frac32(x^2+y^2)+x^2y^2]\) and the bracket is positive.

The same proof applies to fixed bounded, piecewise continuous real test weights \(g\) and \(h\) supported in bands within \([a,b]\), by replacing the prime coefficients by \(g(\log p/L)\) or \(h(\log p/L)\), bounding their absolute values by a common constant, and applying covariance polarization. This gives the bilinear form with local term \(\frac12\int gh\,dx/x\) and correction \(\iint g(x)h(y)C(x,y)\,dx\,dy/(xy)\). As a bilinear form this extends by continuity to \(L^2(dx/x)\), without any arbitrary measurable array claim. The correction has rank at most two, with features \(x,x^3\) and coefficient matrix
\[
 \begin{pmatrix}-4&6\\6&-4\end{pmatrix}.
\]
The correction alone is not positive semidefinite, as seen by a constant test. The full covariance form has lower bound \((\frac12-2b^2)\|g\|_{L^2(dx/x)}^2\). Indeed \(|C(x,y)|\le4xy\) for \(0<x,y\le b\), and \(\int_0^b x^2\,dx/x=b^2/2\). This verifies positive definiteness with a uniform margin throughout the permitted range.

For the corresponding sine statistics the two-sided means and all mixed cosine-sine covariances vanish by reflection. The sine correction is \((K_{\rm ratio}-K_{\rm product})/2=-6x^2y^2\), with the same local diagonal term. Thus its covariance operator is a rank-one negative correction to \(\frac12 I\), bounded below by \((\frac12-\frac32 b^4)I\). These are constraints on first and second moments only.
