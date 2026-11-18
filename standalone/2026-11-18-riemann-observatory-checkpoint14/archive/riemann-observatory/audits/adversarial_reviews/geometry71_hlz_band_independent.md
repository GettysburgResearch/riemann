# Independent check of polynomial-band moments under HLZ

18 November 2026. I recover the proposed mean and variance under RH for fixed \(0<a<b<1/4\). The remainder needed for the second moment is an aggregate estimate for \(D\) and \(D^2\), not a pointwise estimate summed over primes. The finite-prime and repeated-index terms vanish off the covariance diagonal, and the surviving covariance operator has a strict positive lower bound. These two moments give no Gaussian limit for this fixed band.

## Source and uniform application

I used Heap–Li–Zhao, journal PDF SHA-256 6162632530cbeee8c1664d7ea53e844cffa9dbc53fe00a8cd8270e2d713b6a82, pp. 1592, 1605, and §§4–6, principally Theorem 5, (5), (24), and Propositions 10–11. The arXiv cache SHA-256 73c78d922741658678023e73bd0684c1003261906ccc97b48f2e727f5874f6f6 gives the corresponding shifted principal-character formula in Theorem 2. The calculation uses the explicit formula (24) without passing through the smoothed replacement in Lemma 6. [Journal PDF](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [ArXiv PDF](../../sources/classical63_derivative_moments/hlz2022.pdf)

Let \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), fix \(2b<\delta<1/2\), and declare source length \(y=T^\delta\) for every \(T\ge Y\). The real quantity \(W=\Re D(\rho)\) is even in the ordinate on RH. The ordered polynomial pairs required are \((D,1)\), \((D,D)\), and \((D^2,1)\), with coefficients bounded in absolute value by 2. For any one pair \(U,V\), put a constant baseline \(A=20\) on the union of the divisor closures of their supports and zero elsewhere. All four \(Q_{\sigma,\tau}=A\,\mathbf1_{\mathrm{support}}+\sigma U+\tau V\) have coefficient moduli between 16 and 24 on this set. A supported product has both factors supported, so 24 is bounded by the product of their lower bounds. The coefficient bounds of Theorem 5 and Propositions 10–11 thus hold with fixed constants, using the usual separate interpretation at \(n=1\). The four weighted sums with coefficients \(\sigma\tau/8\) recover the real sesquilinear pair on the left and the ordered-pair average on the right. Under RH, after the mixed \(\alpha,\beta\) derivative, the left side is the real derivative-weighted moment. The reflection to negative ordinates doubles numerator and denominator for these observables. All padding cancels from the main terms before the \(\operatorname{lcm}(m,n)^{-1}\)-weighted sum is estimated. [Prime cutoff review](prime70_hlz_cutoff_extension.md) · [Weighted cutoff review](weighted70_hlz_cutoff_review.md)

The full stated length matters. In §4 the contour and continuous estimates use the fixed coefficient envelope, with the cited perturbed-moment errors including \(T^{3/20}y^{33/20}\), and the oscillatory cutoff has cost bounded by \(T^{1/2+\epsilon}y(\log T)^C\). Principal Perron uses \(x=Tk/(2\pi h)\) with \(\log x\asymp\log T\) on the declared length and has fixed-divisor bounds; complex shifts contribute \(n^{O(1/\log T)}\) on the absolute series and are bounded on finite ranges of polynomial size. For the nonprincipal terms choose \(\eta=(\log T)^K\). Proposition 11's three length-dependent errors are
\[
yT^{1/2+\epsilon},\qquad y^{4/3}T^{1/3+\epsilon},\qquad
y^{1/3+\epsilon}T^{5/6+\epsilon},
\]
all power savings for small enough \(\epsilon\) when \(\delta<1/2\). Its remaining piece \(T(\log T)^C\eta^{-1/2+\epsilon}\) allows any fixed log saving. The expansion and summation in Proposition 10 involve the same divisor/submultiplicative envelope, polylogarithmic \(\eta\), and the qualitative Siegel step. No further Dirichlet GRH is needed here. A bound \(\sum_{m\le y}m^{-\sigma}\ll y^{(1-\sigma)_+}\log(2y)\) on the finite factor in its shifted Perron integral costs only \(y^\Delta\) on \(\sigma=1-\Delta\), leaving \((y/x)^\Delta\) in the decay since in that nonprincipal formula \(x=Tkq/(2\pi d)\gg T\) with \(d\mid kq\). The coefficient envelope and harmonic/divisor sums, rather than the cardinality of the support, are the sources of these uniform bounds. The proof uses the possibly ineffective unremoved-prime result. If one chose the effective deletion proof instead, every prime in this fixed band tends to infinity and the removed summand is \(O(Y^{-a/2})\) uniformly, but no deletion is required. The quoted theorem concerns arbitrary large \(T\); if working from a good-ordinate intermediate contour, the bounded-distance change inserts \(O(\log T)\) zeros. On RH the shifted zeta and its derivative satisfy \(O_{\epsilon}(T^\epsilon)\) on the needed shrinking strips, and the padded quadratic factors have \(O_M(y)\) bounds, so the endpoint cost is a power saving. The \(\alpha,\beta\) Cauchy derivatives cost two powers of \(\log T\), absorbed by choosing the original save exponent larger.

## Local kernels and differentiated residues

Set \(L_T=\log T\), \(x=\log p/L_T\), \(z=\log r/L_T\) for two *distinct* primes. For reduced ordered twist \((h,k)\), the leading local multiplier of \(Z_{u,v,w,h,k}\), in scaled variables, is \(e^{-v\sum_{p\mid h}x_p}\) times the product over \(p\mid k\) of \(e^{-ux_p}+e^{-wx_p}-1\) for squarefree \(k\). The sole repeated prime needed is for \(p^2\), with bounded multiplier from the exact factor. To check the squarefree approximation, sum the generating function of \(f_{u,w}(p^j)\) with \(U=e^{-ux_p}\), \(V=e^{-wx_p}\), \(s=p^{-1-v/L_T}\). The exact one-step quotient is \(V+(U-1)(1-Vs)/(1-s)\); its difference from \(U+V-1\) is \((U-1)(1-V)s/(1-s)=O(p^{-1})\), uniformly on the fixed scaled contours. For any of our twists the same boundedness extends to exponent two by the generating-function coefficient calculation. Thus the ignored terms on this moving band have an additional \(O(Y^{-a})\) factor.

For the principal parts use the leading Laurent coefficient of each zeta function. In (5) the summand is the difference of direct and dual exponentials divided by the scaled \(A+B\), with a common \(L_T^2\) multiplier after integrating the time logarithm. In (24) the Laurent prefactor is \(L_T\,v/((u+v)(v+w))\). The three tuples \((u,v,w,\lambda)\) are \((A,B,c,0),(-B,-A,c,-A-B),(A,-c,-B,-B-c)\), with their outer \(A,B\) reflection. Replacing the time integral by \(T e^\lambda\) incurs a relative-scale additive \(O(L_T^{-1})\) on fixed contours, since
\[
T^{-1}\int_0^T(t/(2\pi))^{\lambda/L_T}\,dt
=e^\lambda(2\pi)^{-\lambda/L_T}/(1+\lambda/L_T).
\]
The integral with the extra logarithm has leading term \(L_T e^\lambda\) and a uniformly bounded remainder after division by \(T\). This argument also excludes a missing \(t=0\) endpoint contribution.

The apparent poles in the three terms of (24) are removable in their sum. On \(A+B=0\) the first and second tuples match with opposite residue, on \(B+c=0\) the first and third match, and on \(A-c=0\) the second and third match after interchanging \(u,w\). The latter symmetry follows from \(f_{u,w}=f_{w,u}\), and the time factors agree on that plane. The \(A+B=0\) residues in (5) also cancel. Holomorphic divisibility by these linear factors gives the combined germ and permits nested scaled Cauchy circles with separated radii. After retaining only degree two in (5) and degree three before the auxiliary derivative in (24), it suffices to take the cubic and quartic exponential powers, respectively. For an independent arithmetic extraction I evaluated the resulting symmetric homogeneous quadratic in \(A,B\) at \((1,1),(1,2),(1,3)\) by differentiating only the scalar and exponential pieces in \(c\) there. These directions are used on the homogeneous coefficient polynomials, so a subsequent rescaling to small shift radii poses no problem. The third direction checks the reconstruction. The untwisted coefficient is \(1/12\). [Independent exact symbolic replay](../../scripts/geometry71_hlz_band_independent_checks.py)

After dividing by this coefficient, write \(F(x)=1-4x+2x^3\) and
\[
H(x,z)=F(x)+F(z)-1+12xz-2xz(x^2+z^2).
\]
I obtain \(F(x)\) for the one-prime normalized multiplier, \(H(x,z)-6x^2z^2\) for the ratio twist, and \(H(x,z)+6x^2z^2\) for the product twist. These are main-term multipliers attached to the \(1/\operatorname{lcm}\) weights. For distinct \(p,r\) the common weight is \(1/(pr)\). For the second moment of \(\Re D\) take \(\frac12 |D|^2+\frac12\Re(D^2)\), so the \(\pm6x^2z^2\) difference cancels. The diagonal of \(|D|^2\) gives exactly \(1/p\) per prime before the factor \(1/2\), independent of all shifts after normalization. The \(p^2\) term in \(\Re(D^2)\) has \(\operatorname{lcm}(p^2,1)=p^2\) and bounded differentiated multiplier, hence contributes \(O(\sum_{p>Y^a}p^{-2})=o(1)\). Removing the diagonal from an otherwise smooth pair sum or the square of the mean costs the same. The weighted total main-term error is \(O((L_T^{-1}+Y^{-a})(1+\sum_{p\in\mathrm{band}}1/p)^2)\), with the independent \(o(1)\) shifted-theorem error still aggregate. Thus neither ignored local factors nor the repeated-index pair create a missing finite term.

## Strict tail and the limits

Let \(B_0(t)\) be the two-sided derivative-square prefix sum, and \(B_j(t;Y)\) its analogous weighted sum for \(W^j\). Fix the \(Y\)-dependent band through all \(t\ge Y\). Gonek's mean-square asymptotic gives \(B_0(t)\sim t(\log t)^4/(12\pi)\) under RH. With \(w(t)=(t^2+1/4)^{-1}\), strict tail integration satisfies
\[
\int_{(Y,\infty)} w\,dB_j
=-w(Y)B_j(Y;Y)-\int_Y^\infty w'(t) B_j(t;Y)\,dt.
\]
The boundary uses the inclusive prefix, so an atom at \(Y\) is removed. For \(Y\le t\le Y\exp(\sqrt{\log Y})\), \(\log Y/\log t=1+O((\log Y)^{-1/2})\), uniformly. The polynomial kernels and all absolute prime weights are bounded in the required sums, making it valid to freeze their arguments at \(\log p/\log Y\) in this window. The far part of the last integral is \(O((\log Y)^4Y^{-1}e^{-c\sqrt{\log Y}})\) for a fixed \(c>0\), using the uniform bounded prefix moment ratio. The same estimates control \(w(t)B_j(t;Y)\) at infinity. Finally \(\int_{(Y,\infty)}w\,dB_0\sim(\log Y)^4/(12\pi Y)\). Consequently any uniformly \(o(1)\) normalized prefix discrepancy in the window, including its lower boundary term, is an \(o(1)\) strict-tail moment discrepancy. [Gonek source](../../sources/classical63_lfunctions/gonek1984.pdf)

Prime Mertens gives weak convergence on the fixed interval \([a,b]\) of \(\sum_{Y^a<p\le Y^b}p^{-1}\delta_{\log p/\log Y}\) to \(dx/x\). In fact the subinterval cumulative functions converge uniformly by the Mertens estimate as \(Y^a\to\infty\), and endpoint inclusion differs by at most \(Y^{-a}\). Tensoring the finite measures gives the pair integrals. Therefore the mean is
\[
\log(b/a)-4(b-a)+\tfrac23(b^3-a^3).
\]
The covariance correction for distinct primes is
\[
C(x,z)=H(x,z)-F(x)F(z)=-4xz+6x^3z+6xz^3-4x^3z^3 .
\]
Integrating \(C/(xz)\) on the square and adding the diagonal term yields
\[
\operatorname{Var}(W)\ \longrightarrow\
\tfrac12\log(b/a)-4(b-a)^2+4(b-a)(b^3-a^3)-\tfrac49(b^3-a^3)^2 .
\]
All assertions here are moment limits under the specified law. The cutoff \(b<1/4\) ensures that the product-polynomial support fits in a fixed declared length below \(T^{1/2}\). The proof makes no endpoint assertion.

## Covariance contradiction attempt

The same computation for finite linear combinations of band indicators has the local covariance \(\frac12\langle f,f\rangle_{dx/x}\) and off-diagonal form \(\langle f,Cf\rangle\). The off-diagonal term is signed, so entrywise positivity would be an inappropriate test. Directly,
\[
C(x,z)=-g(x)g(z)+5x^3z^3,\qquad g(x)=2x-3x^3 .
\]
On \((0,1/4)\), \(\int g(x)^2\,dx/x=931/8192<1/2\). Hence for any real compactly supported band step function the limiting covariance is bounded below by \((1/2-931/8192)\|f\|_{L^2(dx/x)}^2\), by Cauchy–Schwarz, even if the positive second rank-one term is discarded. This also tests all finite cross-band covariance matrices, including overlapping bands. I find no covariance, endpoint or residue obstruction in the specified range.

## Parallel notes and the sine comparison

I compared the two completed reports after the independent extraction. Their formulas, strict boundary convention and aggregate use of \(D^2\) agree with this reconstruction. For the sine statistic \(W_s=-\Im D(\rho)\), the same computation subtracts \(\Re(D^2)/2\) instead of adding it, so the off-diagonal covariance is \(-6x^2 z^2\), the mean and mixed cosine-sine covariance vanish exactly by reflection, and the variance limit is \(\tfrac12\log(b/a)-\tfrac32(b^2-a^2)^2\). Its correction operator has norm at most \(6\int_0^b x^4 dx/x=\tfrac32 b^4\). The independent-phase diagonal prediction for both statistics is \(\tfrac12\log(b/a)\), and the limiting arithmetic variances are strictly smaller while staying positive. [Prime covariance report](prime71_hlz_band_covariance.md) · [Weighted covariance report](weighted71_hlz_band_second_moment.md)

The rooted CUE model in the prime report uses the globally weighted law on pairs \((U,j)\). A separate rule normalizing the index weights inside each Haar matrix would give a different law. With the stated convention, rooting supplies one factor \(\prod|1-z_j|^2\) from the Haar density and another from the square derivative, giving the fourth-power insertion. The free-particle projection is onto \((z-1)^2\) times the polynomial modes \(0,\ldots,N-2\), of codimension two in the \(N+1\) modes \(0,\ldots,N\). The two orthogonal complementary mode vectors are constant and centered linear. Checked that the circle integration identity for a projection process gives the four trace corrections displayed in that report, and that at fixed \(0<y\le x<1/4\) the overlap endpoints are \(0,y,x,1-x,1-y,1\); the roots included deterministically change the cosine mean but no covariance. The signs and the normalization therefore have an independent geometric check. This comparison is at first and second moments.
