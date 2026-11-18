# Independent review of the formal all-order prime-band obstruction

Assume RH for the arithmetic tail moments. For a fixed band \(0<a<b<1/2\), the proposed distinct-prime kernel and repeated-prime combinatorics agree with the primary HLZ residues in their admissible range \(rb<1/2\) at moment order \(r\). The resulting formula extends algebraically to a sequence of numbers indexed by every order. That formal sequence is not a probability moment sequence. Its explicit Gaussian-polynomial inverse is signed, and its formal moment-generating function vanishes at a real argument. Neither obstruction occurs within the genuine source moment window. [HLZ (5), (24), and Theorem 5](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Aggregate cutoff proof](weighted70_hlz_cutoff_review.md) · [Sharp \(J\) audit](weighted75_sharp_aggregate_review.md)

## Primary kernel and allocation average

Write \(\alpha,\beta,\xi\) for the three scaled Cauchy variables, \(x_i=\log p_i/\log T\) for distinct primes, and \(u,v,w,\lambda\) for a residue's scaled shifts and time exponent. In a signed expansion of a cosine product, every \(p_i\) is assigned independently to one of the reduced indices \(h\) or \(k\). In (24), a prime of \(h\) gives \(e^{-v x_i}\), and a prime of \(k\) gives \(e^{-u x_i}+e^{-w x_i}-1+O(1/p_i)\) by the exact quotient. The \(2^{-r}\) signed averaging therefore gives the factor
\[
 \prod_{i=1}^r \frac{e^{-v x_i}+e^{-u x_i}+e^{-w x_i}-1}{2}.
\]
The bounded fixed-shift errors here retain the aggregate \(1/\operatorname{lcm}\) weight. In (5), the analogous product is \(\prod_i(e^{-\alpha x_i}+e^{-\beta x_i})/2\), with reflected signs for its second residue. Averaging all allocations makes an additional reversal of the two indices redundant. The time exponents and the reflected set are the three tuples \((\alpha,\beta,\xi,0)\), \((-\beta,-\alpha,\xi,-\alpha-\beta)\), \((\alpha,-\xi,-\beta,-\beta-\xi)\) and the \(\alpha,\beta\)-exchange. The leading pre-derivative factor in (24) is \(v/((u+v)(v+w))\). In (5), use the difference of the two time-weighted products divided by \(\alpha+\beta\).

The surviving exponential numerator degree is three in (5) and four in (24), by simultaneous rotation of the separated Cauchy coordinates. Thus the normalized kernel depends on at most four distinct variables in any monomial. Lower interactions are determined by setting all other \(x_i\) to zero. The empty coefficient is one and the one- and two-variable interactions are the previously checked expressions \(-4x+2x^3\) and \(12xy-2xy(x^2+y^2)\). To check the remaining cases directly, let \(S=u+v+w\), \(Q=u^2+v^2+w^2\). For three variables with one power each the quartic numerator in (24) is \(-\lambda S^3/8\). With one squared variable it is \(QS^2/16\). For four variables with one power each it is \(S^4/16\). Insert each into the three residues and their reflection, differentiate in \(\xi\) and extract \(\alpha\beta\). Their unnormalized coefficients are \(-3/2,0,2\), respectively. The three-linear term from (5) is \(-1/2\), from dividing \(-(\alpha+\beta)^3/4\) by \(\alpha+\beta\) and taking its mixed coefficient. Its other interactions with at least three variables vanish by degree. The untwisted coefficient is \(1/12\). Thus the full normalized distinct-prime kernel is
\[
 K_r=1+\sum_i(-4x_i+2x_i^3)
       +\sum_{i<j}[12x_ix_j-2x_ix_j(x_i^2+x_j^2)]
       -24e_3(x_1,\ldots,x_r)+24e_4(x_1,\ldots,x_r).
\]
These checks recover the cubic interaction without presuming it from the preceding three-prime calculation. [Independent symbolic coefficient check](../../scripts/weighted79_formal_band_kernel_checks.py) · [Prior one- and two-prime kernels](weighted71_hlz_band_second_moment.md)

## Which arithmetic moments this evaluates

For every fixed \(r\) with \(rb<1/2\), use the aggregate evaluation of \(D^u\overline D^{\,v}\), \(u+v=r\), and the fixed-envelope divisor-closed pads, where \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\). Supports through \(Y^{rb}\) fit inside a fixed declared exponent strictly below \(1/2\), uniformly over prefixes \(T\ge Y\). First use the source remainder on the whole aggregate, and only then expand its explicit main term. This order matters when classifying collisions. The source is not charged a separate remainder for each sign choice and tuple of primes.

If a prime occurs \(m\) times, with \(u_p,v_p\) on the two signs, its weight including the arithmetic \(\operatorname{lcm}\) factor is \(p^{-\max(u_p,v_p)}\). Any multiplicity at least three, or a same-sign multiplicity two, therefore has summable weight \(p^{-2}\) or smaller. Its contribution tends to zero as the band's lower cutoff grows, since all other prime sums are bounded in reciprocal mass and the normalized local factors are uniformly bounded at the fixed order. An opposite-sign pair has weight \(1/p\) and disappears from the reduced ratio exactly. Among its four sign choices, two are opposite. Summation produces the factor \(H/2\), where \(H=\log(b/a)\). Thus the only surviving nonsingletons are Wick pairs. Counting partitions with \(l\) pairs and \(r-2l\) singletons gives \(r!/(2^l l!(r-2l)!)\). Collisions among those prime positions can be dropped from the limiting product measure since any equality adds a factor \(p^{-2}\) as a repeated reciprocal weight.

For singleton variables replace \(L_T\) by \(L_Y\) on \(Y\le T\le Ye^{\sqrt{\log Y}}\), changing the polynomial by \(o(1)\) uniformly. At larger \(T\), the uniformly bounded normalized prefixes suffice because the far strict-tail integral is negligible after normalization. This is the same Abel summation as for the previous two- and three-prime computations. Prime reciprocal measure on the band converges to \(dx/x\) under this scale. Put \(d=b-a\), \(q=2(b^3-a^3)/3\). The integrals of one-label, two-label, three-label and four-label interactions are, respectively,
\[
 -4d+q,\qquad 12d^2-2dq,\qquad -24d^3,\qquad 24d^4 .
\]
Each untouched singleton contributes \(H\). The exponential generating series for the singleton sum is consequently \(e^{Hz}[(1-dz)^4+qz(1-dz)]\), using the binomial choices of up to four labels. Summing Wick pairs contributes \(e^{Hz^2/4}\). The true moments at the admissible orders therefore agree term by term with
\[
 M_{\rm form}(z)=e^{Hz+Hz^2/4}\bigl[(1-dz)^4+qz(1-dz)\bigr].
\]
This equation defines formal coefficients at all other orders. It does not evaluate the corresponding arithmetic moments at those orders. For example the full \(D^r\) arm really has length as large as \(Y^{rb}\), and the fact that only four formal interactions survive does not shorten its source input.

## Signed inverse, all-moment obstruction, and finite positivity

For formal rescaling \(y=(W-H)/\sigma\), \(\sigma=\sqrt{H/2}\), set \(s=d/\sigma>0\) and \(q'=q/\sigma>0\). The Gaussian-polynomial signed density is \(\phi(y)R(y)\) with standard normal \(\phi\) and
\[
 R(y)=(1-sy)^4-6s^2(1-sy)^2+3s^4+q'[y-s(y^2-1)].
\]
To verify the inverse, apply the identity \(\int e^{ty}\phi(y)\mathrm{He}_j(y)\,dy=t^j e^{t^2/2}\) for probabilists' Hermite polynomials. The polynomial coefficients across these five Hermite degrees are \(1,-4s+q',6s^2-sq',-4s^3,s^4\). At \(y=1/s+\sqrt3\) the density factor is \(-6s^4-q'(\sqrt3+2s)<0\).

There is an even shorter all-moment contradiction. Suppose a positive probability \(\mu\) shares every formal moment, in the original \(W\) coordinate, with the signed Gaussian-polynomial inverse \(\nu\). Because the even moment coefficients of \(\mu\) are nonnegative, monotone convergence applied to the Taylor series of \(\cosh(tW)\) gives
\[
 \int \cosh(tW)\,d\mu
 =\sum_{n\ge0}\frac{t^{2n}}{(2n)!}\int W^{2n}\,d\mu
 =\int\cosh(tW)\,d\nu <\infty.
\]
The last series exchange is absolute by Gaussian-polynomial domination, equivalently bounded by the corresponding integral against \(|\nu|\). Thus \(\mu\) has every real exponential moment. Its convergent exponential expansion must give exactly \(M_{\rm form}(t)\). At \(t=1/d\) this vanishes, whereas \(\int e^{tW}\,d\mu>0\). Alternatively the equal exponential moments imply equality of Fourier transforms and hence equality to the signed inverse, contradicting its open negative-density interval. This avoids invoking a moment-determinacy theorem without checking its hypotheses.

A finite failing Hankel test also follows abstractly. Take \(dt=1+\delta\) with \(\delta^3=q/(8d)>0\). Then the polynomial factor of \(M_{\rm form}(t)\) is \(\delta^4-(q/d)\delta(1+\delta)<0\). Square the degree-\(n\) Taylor polynomial of \(e^{tW/2}\). These squares converge to \(e^{tW}\) and are dominated by \(e^{|tW|}\) against \(|\nu|\). Their integrals are negative for some finite \(n\). This gives a polynomial-square witness without asserting a numerical degree bound.

All genuine source Hankel tests \(2nb<1/2\) must be positive semidefinite by actual moment convergence. They are in fact strictly positive by a direct check of the signed inverse on polynomials of degree at most \(n\). Here \(s^2=2d^2/H\le d(a+b)\le b^2\), from \(H\ge2d/(a+b)\), and \(q'\le2b^2s\). At \(n=0\) the mass is 1. For \(n=1\), the normalized variance computed from the formal first two moments is \(1-4s^2+6sq'-(q')^2>0\) because \(b<1/4\). For \(n\ge2\) with \(b<1/(4n)\), let \(f\) have \(\int f^2\phi=1\), degree at most \(n\). Multiplication by \(y\) has norm at most \(C_n=\sqrt n+\sqrt{n+1}\) on this degree space by the normalized Hermite recurrence. Then \(sC_n<2/5\) and \(s^2\le1/64\). In the positive probability \(f^2\phi\,dy\), put \(m_2=\mathbb E(1-sy)^2\ge9/25\) by the reverse triangle inequality. Jensen bounds the fourth power from below by \(m_2^2\). Thus
\[
 \int f^2R\phi \ge
 m_2(m_2-6s^2)-2b^2\bigl(sC_n+s^2 C_n^2+s^2\bigr)>0 .
\]
For the last inequality the first term is at least \((9/25)(9/25-3/32)\), and the subtracted upper bound is \((1/32)(2/5+4/25+1/64)\). The first exceeds the second. This directly rules out using the negative-density witness to refute a moment order that the source actually supplies.

The contradiction applies precisely to promoting the same formal formula to *all* moments on one fixed positive band. It neither rejects the finite-window arithmetic formulas nor rules out an actual band limit with different higher moments. No canonical theorem record was changed.
