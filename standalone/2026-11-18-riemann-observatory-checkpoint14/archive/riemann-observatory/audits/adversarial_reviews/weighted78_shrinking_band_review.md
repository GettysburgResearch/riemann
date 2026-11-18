# Independent review of the shrinking-exponent Gaussian band

Assume RH. Let \(L=\log Y\), \(b=b(Y)\to0\), \(a=a(Y)\) with \(a/b\to r\in(0,1)\) and \(aL\to\infty\). On the strict two-sided derivative-weighted tail \(|\gamma|>Y\), define
\[
 A_Y=e^{aL},\qquad B_Y=e^{bL},\qquad
 H_Y=\sum_{A_Y<p\le B_Y}\frac1p,\qquad
 S_Y=\sum_{A_Y<p\le B_Y}p^{-1/2}\cos(\gamma\log p)-H_Y .
\]
Then \(S_Y\) converges in law and in every fixed moment to the centered Gaussian of variance \(\tfrac12\log(1/r)\). No variance normalization is needed. The proof uses the aggregate, bounded-coefficient version of HLZ, so the arbitrary log-saving error is incurred once per aggregate evaluation. [HLZ Theorem 5 and (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Growing-cutoff and uniform coefficient audit](weighted70_hlz_cutoff_review.md) · [Sharp continuous replacement](weighted75_sharp_aggregate_review.md)

## Prime endpoint and independent phase model

Eventually \(0<a<b\), both \(A_Y\) and \(B_Y\) tend to infinity, and the prime reciprocal Mertens formula at the two real endpoints gives
\[
 H_Y=\log\log B_Y-\log\log A_Y+o(1)
     =\log(b/a)+o(1)\longrightarrow\log(1/r).
\]
The difference of reciprocal sums uses the stated open lower and closed upper prime endpoint, also when either real endpoint equals a prime. No monotonicity in \(Y\) is needed. In particular, \(H_Y=O(1)\) and \(\sum_{A_Y<p\le B_Y}p^{-2}\le A_Y^{-1}H_Y=o(1)\).

Use independent circle phases \(\Theta_p\) with Poisson kernel of radius \(p^{-1/2}\), so \(E_\star e^{ij\Theta_p}=p^{-|j|/2}\). The centered variable \(X_p=p^{-1/2}\cos\Theta_p-p^{-1}\) has
\[
 E_\star X_p=0,\qquad E_\star X_p^2=\frac12(p^{-1}-p^{-2}),\qquad |X_p|\le2p^{-1/2}.
\]
Its \(\ell\)-th cumulant for each fixed \(\ell\ge3\) is \(O_\ell(p^{-\ell/2})\) from the finite cumulant polynomial and the supremum bound. Independence gives for their sum a cumulant bound
\[
 O_\ell\!\left(\sum_{A_Y<p\le B_Y}p^{-\ell/2}\right)
 =O_\ell\bigl(A_Y^{-(\ell-2)/2}H_Y\bigr)=o(1).
\]
The first cumulant is zero and the second tends to \(\frac12\log(1/r)>0\). Thus all fixed model moments converge by the moment–cumulant identity. For the uncentered complex sum \(D_\star=\sum_{A_Y<p\le B_Y}p^{-1/2}e^{-i\Theta_p}\), \(E_\star |D_\star|^j=O_j(1)\) for each fixed \(j\). To see this use real and imaginary parts, their bounded means, and the same cumulant argument at an even order at least \(j\). For \(u+v=j\), \(E_\star D_\star^u\overline{D_\star}^{\,v}\) is nonnegative, since its Fourier expansion has nonnegative coefficients and nonnegative character expectations, and is bounded by \(E_\star |D_\star|^j\).

## Arithmetic aggregate comparison on every prefix

For fixed \(Y\) set \(D(s)=\sum_{A_Y<p\le B_Y}p^{-s}\), the same polynomial for every prefix \(T\ge Y\). Its real part at \(1/2+i\gamma\) gives the uncentered cosine statistic. To compare a raw cosine moment of degree \(j\), expand \((\Re D)^j\) into the finitely many \(D^u\overline D^{\,v}\) terms, \(u+v=j\), taking their real combinations. Under RH the conjugate is the same real-coefficient polynomial evaluated at \(1-\rho\). Each power has coefficients bounded by \(j!\) and support length at most \(B_Y^j=Y^{jb(Y)}\). For any fixed declared exponent \(0<\delta<1/2\), \(B_Y^j\le Y^{\delta/2}\) eventually, hence below the declared HLZ length \(T^\delta\) throughout \(T\ge Y\), also after a bounded correction to a good contour height. The onset depends on the fixed degree. There is no inference at a degree growing with \(Y\).

The four padded arrays formed from the divisor-closed union of the two supports have fixed common divisor/log and submultiplicative envelopes. A baseline depending only on \(j\), followed by the four signs, removes the padding in the entire shifted quadratic evaluation. Thus Theorem 5 supplies a single \(O_{j,C}(T(\log T)^{-C})\) remainder in a prescribed aggregate, before the two outer shift differentiations. Apply Cauchy on constant separated radii scaled by \(1/\log T\), as in the inspected source reconstruction. The remainder, normalized by the untwisted derivative moment, is \(O_{j,B}((\log T)^{-B})\) for every fixed \(B\) after increasing \(C\). In particular there is no sum of separate remainder constants over the primes.

For a term indexed by \(m,n\), put \(g=(m,n)\), \(h=m/g\), \(k=n/g\), and \(L_T=\log T\). The exact local quotient in (24), with shifts \(O(1/L_T)\), changes the normalized untwisted kernel by \(O(\log(hk)/L_T)\) relative to the factor \(1/\operatorname{lcm}(m,n)\). This follows at \(p^e\Vert k\) from
\[
 V^e+(U-1)\left(\sum_{i=0}^{e-1}U^iV^{e-1-i}\right)\frac{1-Vz}{1-z}
  =1+O(e\log p/L_T)
\]
with \(U,V=p^{O(1/L_T)}\), \(z=p^{-1+O(1/L_T)}\). Multiply the local errors using the product bound with exponent \(O(\log(hk)/L_T)\), bounded on all the supports in use. The explicit powers in (5) have the same control. Here in fact \(\log(hk)\le(u+v)\log B_Y=j b(Y)L\), so the relative main-term perturbation is \(O_j(b(Y)L/L_T)\) uniformly in \(T\). This comparison is to the exact untwisted prefix, before its large-\(T\) asymptotic is used for normalization. The aggregate weight \(1/\operatorname{lcm}(m,n)\) is exactly the polynomial Dirichlet weight \(1/\sqrt{mn}\) times the model character expectation \(g/\sqrt{mn}\). For the products above the sum of these model weights, including their nonnegative array coefficients, is \(E_\star D_\star^u\overline{D_\star}^{\,v}=O_j(1)\). Thus the aggregate relative error is \(O_j(b(Y)L/L_T)\), and the bounded centering constant \(H_Y\) incurs only fixed-degree binomial factors.

Consequently the positive-prefix probability with masses \(|\zeta'(\rho)|^2\) has
\[
 \left|E_T(S_Y^j)-E_\star\left(\sum X_p\right)^j\right|
 \ll_{j,B} b(Y)L/L_T+L_T^{-B}.
\]
The unmodified source coefficient estimate may have an ineffective threshold. For an effective version the earlier full-length small-conductor split deletes at most one prime \(\ell_T\) for each \(T\), with the deletion made before forming and padding all aggregate powers. A deleted band prime is \(>A_Y\), so the centered term it removes has size at most \(2A_Y^{-1/2}\) pointwise. The same aggregate comparison at even order \(2j\) gives bounded centered prefix and model moments uniformly with that deletion. Restoring it by \(|(x+z)^j-x^j|\le j|z|(|x|+|z|)^{j-1}\) and Hölder costs \(O_j(A_Y^{-1/2})\), uniformly on both sides. This restoration uses the full fixed prime statistic before partial summation, even if \(\ell_T\) changes with \(T\). Effectivity for a limiting band presupposes specified effective rates for its cutoff parameters. [Exceptional-conductor split and restoration](weighted70_hlz_cutoff_review.md)

## Strict-tail transfer

Let \(M(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2\), with \(M(T)\sim T(\log T)^4/(24\pi)\) under RH. For fixed \(Y\) and \(j\), set \(f_Y(\gamma)=S_Y(\gamma)^j\), and \(M_f(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^2f_Y(\gamma)\). The prefix comparison bounds \(M_f(T)-m_{j,Y}M(T)\) by \(M(T)\) times a fixed error tending to zero, uniformly for \(T\ge Y\), where \(m_{j,Y}\) is the full model moment. The boundary at infinity vanishes for this fixed \(Y\), since \(f_Y\) is a bounded finite polynomial and \(M(T)\ll T(\log T)^4\). With \(k(t)=1/(t^2+1/4)\), partial summation gives the strict positive tail as
\[
 -k(Y)M_f(Y)-\int_Y^\infty k'(t)M_f(t)\,dt .
\]
Using the cumulative prefix through \(\gamma=Y\) gives the exact strict cutoff even when \(Y\) is an ordinate. The same identity for the constant statistic and the untwisted asymptotic give tail mass \(\sim(\log Y)^4/(24\pi Y)\). The sum \(k(Y)M(Y)+\int_Y^\infty|k'(t)|M(t)\,dt\) is of that order. Therefore the normalized tail expectation differs from the model by the same vanishing order of error. Cosines are even in \(\gamma\), so conjugation preserves the normalized expectation on the two-sided strict tail. Multiple zeros have zero derivative weight. The resulting moment convergence, with Gaussian moment determinacy and tightness from the bounded second moments, proves the convergence in law. [Gonek untwisted prefix, Corollary 1](../../sources/classical63_lfunctions/gonek1984.pdf) · [Earlier exact cutoff check](uniform64_hlz_third_review.md)

This is a scalar statement. An interval-independent vanishing remainder in a local fourth-moment bound does not itself give a small-scale tightness estimate. For example, a triangular pulse of height one and width \(h\) centered at a uniform random interior point has each fixed increment fourth moment \(O(h)\), even uniformly in the two deterministic times. Yet at shrinking width its continuous paths retain unit oscillations over shrinking intervals. No functional convergence conclusion is drawn from the aggregate comparison here.
