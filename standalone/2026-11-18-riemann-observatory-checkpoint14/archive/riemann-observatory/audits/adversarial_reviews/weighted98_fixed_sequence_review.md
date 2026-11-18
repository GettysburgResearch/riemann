# Differentiated one-sided remainder | Single fixed coefficient sequence

Assume RH for the derivative-weighted zero problem. Set \(\theta=4b\), \(P=D^4=\sum_{k\le Y^\theta}c_k k^{-s}\), \(T\asymp Y\), \(L=\log T\), and \(H=T^\kappa\). In the smoothed contour formulation, the conjectured reduction to one fixed nonnegative coefficient sequence is valid. The lower shifted divisor term has an elementary power-saving estimate, uniformly in the numerator. The resulting estimate needed for the fixed sequence remains open here. [Smooth contour reduction](analytic95_pure_fourth_adjudication.md) · [Saddle verification](weighted96_smooth_saddle_review.md) · [HLZ journal, equations (27)–(29)](../../sources/classical63_derivative_moments/hlz2022print.pdf)

## Differentiate the arithmetic remainder

Let \(B_{\alpha,\beta,\eta}(m)\) be the coefficients of
\[
 B_{\alpha,\beta,\eta}(s)=
     \frac{\zeta(s+\eta)\zeta(s+\alpha)\zeta(s-\beta)}{\zeta(s)} .
\]
After the reparametrization of the reflected saddle, the coefficient in the smoothed sum is \(k^{-1} (k/m)^\beta c_k B_{\alpha,\beta,\eta}(m)\). The weight \(w_T(2\pi m/k)\) is real and independent of the shifts. In particular the intermediate argument \(2\pi m/k+\Im\beta\) has already been replaced with a uniform power-saving error before Cauchy. The smoothed arithmetic sum is finite, and its derivative commutes with all sums.

At zero shifts the generating function is \(\zeta^2\). A single derivative is \(\zeta\zeta'\) for \(\alpha,\eta\), and \(-\zeta\zeta'\) for \(\beta\). A pair of **distinct** derivatives is \(\zeta'^2\) for \(\alpha,\eta\), and \(-\zeta'^2\) for either pair involving \(\beta\). These formulas do not concern repeated derivatives in the same parameter. The triple derivative is
\[
 -\frac{\zeta'^3}{\zeta}
   =\zeta^2\bigl(-\zeta'/\zeta\bigr)^3 .
\]
Define \(A=d_2*\Lambda*\Lambda*\Lambda\) and \(C(m)=\sum_{rs=m}\log r\log s\), the latter the coefficient of \(\zeta'^2\). The three derivatives of the full summand yield exactly
\[
 \frac{c_k}{k}\bigl(A(m)+\log(k/m)C(m)\bigr)w_T(2\pi m/k)
 \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right].
\]
Only the \(\beta\)-derivative can hit the exterior power. Its sign is \(\log k-\log m\). The nonnegative sequence \(A\) is the sole triple-derivative term, with no shifts remaining.

## Keep the denominator fixed when averaging units

For every \(m,k\ge1\), put \(k'=k/(m,k)\). The reduction map \((\mathbb Z/k\mathbb Z)^\times\to(\mathbb Z/k'\mathbb Z)^\times\) is surjective with equal-size fibers, by prime-power reduction and CRT. Multiplication by \(m/(m,k)\) permutes the latter units. Thus
\[
 \frac1{\varphi(k)}\sum_{a\bmod k}^{*} e(-am/k)
   =\frac{\mu(k')}{\varphi(k')}.
\]
This includes \(k'=1\), where the difference vanishes. Apply the additive-twist estimate at each *unit numerator over the original denominator* \(k\), then subtract its average over unit numerators. There is no need for a coprimality cutoff on the summation variable, or a separate shifted divisor formula on each gcd block.

## Uniform shifted divisor estimate by the Hurwitz functional equation

Here is a Mellin proof of the rapid-decay consequence of GL(2) Voronoi needed here. It makes both the polar term and the numerator uniformity explicit. Put
\[
 d_{u,v}(n)=\sum_{rs=n}r^{-u}s^{-v},\qquad
 Z(s;u,v,a,k)=\sum_{n\ge1}d_{u,v}(n)e(-an/k)n^{-s}.
\]
The parameters \(u,v\) are bounded by fixed multiples of \(1/L\), with the variables used later on separated circles if desired. On the absolutely convergent half-plane, and then meromorphically, residue classes give the exact identity
\[
 Z(s;u,v,a,k)=k^{-2s-u-v}\sum_{r,\ell=1}^k
 e(-ar\ell/k)\zeta(s+u,r/k)\zeta(s+v,\ell/k).
\]
For \(u\neq v\), the residues at \(s=1-u\) and \(s=1-v\) are respectively \(k^{-1+u-v}\zeta(1-u+v)\) and \(k^{-1+v-u}\zeta(1+u-v)\). Indeed the summation over the residue class from the Hurwitz pole contributes \(k\) only at the zero class of the other variable, and zero elsewhere. Hence all polar terms are independent of the unit \(a\). The pole coalescence at \(u=v\) is removable in the difference of numerators, as follows directly from the same finite expression.

Use Hurwitz's exact Fourier formula in the region \(\Re z<0\),
\[
 \zeta(z,x)=\frac{2\Gamma(1-z)}{(2\pi)^{1-z}}
           \sum_{n\ge1}n^{z-1}\cos\!\left(\frac{\pi(1-z)}2-2\pi nx\right),
           \qquad 0<x\le1 .
\]
This is the classical Hurwitz functional equation, with absolutely convergent series on each fixed left line. [DLMF equation 25.11.9](https://dlmf.nist.gov/25.11.E9)

Take \(s=-B+it\) for a fixed integer \(B\ge1\). Expanding the two cosines into exponentials, each double finite sum has the form
\[
 \sum_{r,\ell=1}^k e\bigl((-ar\ell+nr+m\ell)/k\bigr),
\]
with possible signs on \(n,m\). It has absolute value exactly \(k\) since the \(r\)-sum selects exactly one \(\ell\). The two remaining Dirichlet series of absolute values converge. Stirling cancels the exponential growth of each cosine factor and gives
\[
 |Z(-B+it;u,v,a,k)|
 \ll_B k^{1+2B+O(1/L)}(1+|t|)^{1+2B+O(1/L)}
\]
uniformly in \(a\). This bound also holds for its unit average and their difference. Using a trivial \(k^2\) bound for the finite sum would obscure this conductor calculation, though a fixed extra polynomial loss could also be absorbed by choosing \(B\) large in this range.

Let \(F_k(x)=w_T(2\pi x/k)\log(k/x)\), \(M=kT\) and \(\delta=H/T\). The test is supported on \(x\asymp M\), and differentiating with respect to \(\log x\) at most \(j\) times costs \(O_j(L\delta^{-j})\). By integration by parts in the Mellin integral,
\[
 |\widetilde F_k(-B+it)|\ll_{B,j}
    L M^{-B}(1+\delta|t|)^{-j}.
\]
Mellin inversion expresses the smoothed divisor sum as the integral of \(Z(s)\widetilde F_k(s)\) on a right line. Subtracting the numerator average cancels the poles exactly, so the contour can move to \(-B\). The shift is justified by the rapid Mellin decay and polynomial growth on fixed strips, from the finite Hurwitz representation and its standard vertical estimates. Integration there yields
\[
 \left|\sum_n d_{u,v}(n)F_k(n)
     \left[e(-an/k)-\frac{\mu(k/(n,k))}{\varphi(k/(n,k))}\right]\right|
 \ll_B L^C k\delta^{-2}
      \left(\frac{k^2}{M\delta^2}\right)^B
 = L^C k\delta^{-2}\left(\frac{kT}{H^2}\right)^B .
\]
Powers \(O(1/L)\) in the prior estimate are harmless since \(k\) and \(\delta^{-1}\) are bounded by fixed powers of \(T\), and one chooses the Mellin decay order larger than \(2B+3\). The shifted coefficients satisfy \(\partial_u\partial_v d_{u,v}(n)|_0=C(n)\). The difference of weighted sums is holomorphic on the shift polydisk, and two Cauchy derivatives add only \(O(L^2)\). Thus the same bound with a fixed additional log power controls the \(C(m)\) term.

For \(\kappa>(1+\theta)/2\), \(kT/H^2\) is at most a fixed negative power of \(T\) uniformly for \(k\le Y^\theta\) on every compact comparable-height block. The total after multiplying by \(|c_k|/k\) is bounded by \(L^C y\delta^{-2}\) times an arbitrarily high power of this saving, since \(c_k\le24\). The term is therefore \(O_N(T^{-N})\) for every fixed \(N\). The equivalent Bessel transition condition is \(kH\gg k\sqrt{kT}\), since \(kH\) is the transition width in \(m\) and \(k\sqrt{kT}\) is the wavelength for the first dual term at \(m\asymp kT\). This uses a fixed power margin. The coarser established saddle bound can be retained by choosing \(\kappa>(2+\theta)/3\), which implies the divisor condition. Use of the optional sharper saddle bound in the previous review also allows \(\kappa>(1+\theta)/2\) for standard two-transition tapers.

## Consequence for the remaining input

A sufficient estimate on each compact comparable-height block is
\[
 \Re\sum_{k\le Y^\theta}\frac{c_k}{k}
   \sum_m (d_2*\Lambda*\Lambda*\Lambda)(m)\,w_T(2\pi m/k)
      \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right]
 =o(T(\log T)^4).
\]
The denominator-\(1\) orientation contributes no nonprincipal term. The compact-to-strict-tail argument uses the earlier positive absolute mixed bound beyond \(RY\) and the short endpoint estimate for \(D^2\). These independently justify the required endpoint and tail passage. This fixed-sequence estimate is a weaker sufficient input than the uniform three-shift bound. The Mellin argument above only removes the weighted shifted-divisor term and gives no bound of the required size for the triple Mangoldt convolution. No canonical record was changed.

## Appendix | Reduction from three Mangoldt factors to one

The fixed sequence \(A\) admits a further exact reduction. Here write \(\mathcal L(s)=\zeta'(s)/\zeta(s)\), and define
\[
 C_*(m)=\bigl(d_2*(\Lambda\log^2)\bigr)(m),
 \qquad (\Lambda\log^2)(n)=\Lambda(n)(\log n)^2 .
\]
This \(C_*\) differs from the earlier divisor coefficient \(C(m)\). On \(\Re s>1\), absolute convergence allows the logarithmic derivative series to be differentiated twice, giving
\[
 \sum_m C_*(m)m^{-s}=-\zeta(s)^2\mathcal L''(s).
\]
Indeed \(\mathcal L=-\sum_n\Lambda(n)n^{-s}\) and the two derivatives of \(n^{-s}\) supply \(+(\log n)^2\). The ordinary derivative identities
\[
 \frac{\zeta''}{\zeta}=\mathcal L'+\mathcal L^2,\qquad
 \frac{\zeta'''}{\zeta}=\mathcal L''+3\mathcal L\mathcal L'+\mathcal L^3
\]
give
\[
 \zeta\zeta'''-3\zeta'\zeta''
     =\zeta^2(\mathcal L''-2\mathcal L^3).
\]
Consequently the exact identity of Dirichlet series is
\[
 \sum_m A(m)m^{-s}=-\zeta^2\mathcal L^3
  =\frac12\left(\sum_m C_*(m)m^{-s}+\zeta\zeta'''-3\zeta'\zeta''\right).
\]
It applies coefficientwise by uniqueness of absolutely convergent Dirichlet series.

For the two derivative products use the same two-shift family \(d_{u,v}(m)\) as above. The coefficient of \(\zeta\zeta'''\) is \(\partial_v^3d_{u,v}(m)|_0=-\sum_{rs=m}(\log s)^3\). The coefficient of \(\zeta'\zeta''\) is \(\partial_u\partial_v^2d_{u,v}(m)|_0=-\sum_{rs=m}\log r(\log s)^2\). The numerator-minus-unit-average difference of the shifted family is holomorphic at \(u=v\), independent of the order of subsequent Cauchy extraction. The previously proved Mellin estimate applies with test \(w_T(2\pi x/k)\) alone. Its proof also permits the same test multiplied by any fixed power of \(\log(k/x)\), with a fixed log loss. Three shift derivatives cost \(O((\log T)^3)\), absorbed by choosing the left Mellin line far enough. For \(\kappa>(1+\theta)/2\) these two derivative-product sums are \(O_N(T^{-N})\) for every fixed \(N\), after summing over \(k\).

To state exactly what this subtracts, let
\[
 E_F=\sum_{k\le Y^\theta}\frac{c_k}{k}
       \sum_m F(m)w_T(2\pi m/k)
       \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right].
\]
The coefficient identity and the smooth divisor estimate give \(E_A=\tfrac12E_{C_*}+O_N(T^{-N})\) before taking real parts. No gcd restriction is introduced. The principal subtraction is the same unit average over the original modulus \(k\) for every term, so the identity does not change the factors \(c_k/k\), the phase convention, or the Ramanujan factor at a noncoprime \(m\). The extra exterior-factor derivative \(\log(k/m)C(m)\) was already removed by the preceding divisor calculation. It follows that the compact-local sufficient estimate can use the single nonnegative sequence \(C_*=d_2*(\Lambda\log^2)\) and asks for \(\Re E_{C_*}=o(T(\log T)^4)\). The reduction does not provide that estimate. The original contour normalization contributes a factor \(1/2\) to this replacement, in addition to the existing \(1/8\) weight of the real pure term in the fourth-power identity.
