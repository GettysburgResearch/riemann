# HLZ finite moment window and an obstruction to its all-order extrapolation

18 November 2026. The arithmetic results below assume RH and concern the symmetric strict derivative-weighted tail, as in the preceding prime-band reports. Fix \(0<a<b\) and let
\[
 W_Y=\sum_{Y^a<p\le Y^b}\frac{\cos(\gamma\log p)}{\sqrt p},
 \qquad H=\log(b/a),\quad d=b-a,\quad q=\tfrac23(b^3-a^3).
\]
For each fixed nonnegative integer \(r\) with \(rb<1/2\), the limit of the \(r\)-th raw moment exists and is \(r!\) times the coefficient of \(z^r\) in
\[
 {\cal M}(z)=e^{Hz+(H/4)z^2}P(z),\qquad
 P(z)=(1-dz)^4+qz(1-dz).
 \tag{1}
\]
Only the indicated finite set of coefficients is warranted on a fixed band. Formally using the same entire series at every order gives a sequence that cannot be the moments of any probability measure. On \([a,b]=[1/20,1/10]\) there is an explicit, certified negative Hankel quadratic form using formal moments through degree 140. This concerns an extrapolation, not a failure of HLZ or the valid finite moment formulas, and no law for the full arithmetic band follows. Publication priority is unassessed. [HLZ primary source, Theorem 5 and equations (5), (24)](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Uniform aggregate interface](prime70_hlz_cutoff_extension.md) · [Sharp continuous input](prime75_hlz_sharp_aggregate_review.md)

## 1. Distinct-prime polynomial

For \(r\) distinct band primes \(p_i\), put \(x_i=\log p_i/\log T\) at prefix height \(T\ge Y\). The normalized leading HLZ coefficient for the cosine-sign average, apart from \(1/\prod_i p_i\), is
\[
 \begin{split}
 K_r(\mathbf x)=1&+\sum_i(-4x_i+2x_i^3)
 +\sum_{i<j}\big[12x_i x_j-2x_i x_j(x_i^2+x_j^2)\big]\\
 &-24\,e_3(\mathbf x)+24\,e_4(\mathbf x),                         \tag{2}
 \end{split}
\]
where \(e_j\) is the squarefree elementary symmetric polynomial of degree \(j\).

To extract the coefficient from HLZ, use scaled shifts \(\alpha,\beta,c\) in units of \(1/\log T\), on fixed separated Cauchy circles. The \(I\)-term with tuple \((u,v,w,t)\) has time factor tending to \(e^t\) and leading scaled zeta quotient \(v/((u+v)(v+w))\). The leading \(h\)-slot arithmetic factor for a prime is \(e^{-v x_i}\). The leading \(k\)-slot factor is \(e^{-u x_i}+e^{-w x_i}-1\), by the exact \(e=1\) local ratio and geometric tail \(O(1/p_i)\). Consequently the average over independent sign choices has factor
\[
 2^{-r}\prod_i(e^{-v x_i}+e^{-u x_i}+e^{-w x_i}-1).
\]
The tuples are \((\alpha,\beta,c,0)\), \((-\beta,-\alpha,c,-\alpha-\beta)\), and \((\alpha,-c,-\beta,-\beta-c)\), with a second sum reflected in the outer shifts. For \(J\), the two factors are \(2^{-r}\prod_i(e^{-\alpha x_i}+e^{-\beta x_i})\) and \(2^{-r}\prod_i(e^{\alpha x_i}+e^{\beta x_i})\), multiplied by \(1/(\alpha+\beta)\) and \(-e^{-\alpha-\beta}/(\alpha+\beta)\). These are the \(h,k\) monomials in (5) with their two possible sign assignments for each prime. Time integrals and zeta expansions produce uniform normalized \(O_r(1/\log T+\sum_i1/p_i)\) errors, as in the lower orders.

Simultaneous rotation of the scaled Cauchy circles keeps numerator degrees three in \(J\) and four in \(I\) before auxiliary differentiation. Hence \(K_r\) is a symmetric polynomial of total frequency degree at most four. Setting a frequency to zero removes that factor from both sign products, because its normalized constant is one. The monomials supported on at most three indices can therefore be extracted from the symbolic cases \(r=0,1,2,3\); those exact coefficient computations reproduce the constant, single, pair, and triple terms of (2). This is consistent with earlier lower-order derivations. The only possible monomial on four distinct indices is their squarefree product. There is no contribution to it from \(J\), of frequency degree at most three. In an \(I\) tuple the product consumes all four numerator degrees by selecting the linear term \(-(u+v+w)x_i/2\) from each factor. Its remaining coefficient is
\[
 \frac{v(u+v+w)^4}{16(u+v)(v+w)} .
\]
Sum this expression over the three tuples and their reflection, and differentiate with respect to \(c\) at zero. The result simplifies to \(2\alpha\beta\). Dividing the resulting \(\alpha\beta\)-coefficient by the untwisted \(1/12\) gives 24. No monomial can involve more than four distinct indices. Thus (2) holds in every fixed order for the formal leading coefficient. The code checks all deductions involving exact polynomial coefficient extraction. [Symbolic coefficient and witness program](../../scripts/prime79_hlz_formal_moment_obstruction.py)

## 2. Coincident primes and integration in the valid range

To obtain an arithmetic moment from the kernel, put \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\). Expand
\[
 (\Re D)^r=2^{-r}\sum_{j=0}^{r}\binom rj D^j\overline D^{\,r-j}.
\]
The coefficients of each power are bounded by \(r!\), and the longest polynomial has length \(Y^{rb}\). For \(rb<1/2\) choose a fixed declared length \(T^\delta\) with \(rb<\delta<1/2\). Pair complex conjugate terms, use the uniform bounded divisor-closed padding and four-sign polarization, and apply HLZ to the entire polynomial pair. The source remainder is an aggregate normalized \(o(1)\). It is never multiplied by the number of terms in the expansion of \(D^j\overline D^{\,r-j}\).

At a prime repeated in the ordered word, let \(u,v\) be its counts in the two sides of the signed expansion. The lcm denominator contains \(p^{\max(u,v)}\) and the remaining scaled main factor is bounded uniformly by the fixed-order local quotient estimates. If some prime has \(\max(u,v)\ge2\), its total summed contribution is negligible, by \(\sum_{p>Y^a}p^{-2}=o(1)\) and bounded band harmonic sums for the other primes. There are only finitely many equality and sign patterns for fixed \(r\). Thus all surviving non-singletons are exactly pairs with \(u=v=1\). Such a pair occurs with probability \(1/2\) among its sign assignments, contributes \(1/p\), and disappears from the reduced \(h,k\) arithmetic factors. If there are \(j\) pairs, there are \(r!/(2^j j!(r-2j)!)\) ways to pair the selected positions. Summing the paired primes supplies \((H/2)^j\), including the sign probability. Disallowing collisions between different assigned primes costs \(o(1)\), again by \(\sum p^{-2}\). These are the precise Gaussian pairing terms with variance \(H/2\), before multiplying the remaining distinct-singleton kernel.

Define \(B_\ell=\int_{[a,b]^\ell}K_\ell(\mathbf x)\prod_i dx_i/x_i\), with \(B_0=1\). The prime weighted measures converge to \(dx/x\) by Mertens on fixed bands. In the strict tail, first fix the frequencies at \(T=Y\). On prefixes the difference caused by \(\log T\) instead of \(\log Y\) is \(O_r(\log(T/Y)/\log Y)\) after summing, by bounded derivatives of the polynomials and bounded harmonic sums. Its Stieltjes contribution against the inverse-quadratic weight is \(O_r(1/\log Y)\) after normalization. The denominator uses the ordinary derivative prefix asymptotic. The same Stieltjes argument transfers the normalized aggregate \(o(1)\) errors and handles the inclusive prefix at the strict boundary. Thus the limiting \(r\)-th moment is the finite sum
\[
 \sum_{j=0}^{\lfloor r/2\rfloor}
     \frac{r!}{2^j j!(r-2j)!}(H/2)^j B_{r-2j}.
 \tag{3}
\]

For the formal series of the \(B_\ell\), integrate (2) by the number of selected indices. Each unselected index supplies \(H\). An index selected in a single term integrates to \(-4d+q\), an unordered pair term to \(12d^2-2dq\), a triple term to \(-24d^3\), and a four-index term to \(24d^4\). Therefore the formal generating series \(\sum B_\ell z^\ell/\ell!\) is \(e^{Hz}\) times
\[
 1+(-4d+q)z+(6d^2-dq)z^2-4d^3 z^3+d^4 z^4=P(z).
\]
The Wick pairs in (3) multiply by \(e^{Hz^2/4}\), giving (1). At \([1/20,1/10]\) the proved arithmetic moments in this argument are orders \(0,\ldots,4\). The formal coefficients above that window are not obtained from the source theorem. No uniformity in growing \(r\), or simultaneous all-order convergence on a fixed positive band, has been used.

## 3. Formal inversion and the probability obstruction

Write \(\sigma=\sqrt{H/2}\), \(s=d/\sigma\), \(q'=q/\sigma\) and standardize \(y=(W-H)/\sigma\), using the Gaussian factor's mean \(H\), rather than the true first coefficient \(H-4d+q\). For a standard real Gaussian \(G\) with density \(\phi\), write \({\rm He}_k\) for probabilists' Hermite polynomials. The identity
\[
 E[{\rm He}_k(G)e^{tG}]=t^k e^{t^2/2}
\]
gives the unique explicit signed Gaussian-polynomial inverse of the entire formal expression in standardized coordinates. Its density is \(R(y)\phi(y)\), where
\[
 R(y)=1+(-4s+q'){\rm He}_1(y)+(6s^2-sq'){\rm He}_2(y)
        -4s^3{\rm He}_3(y)+s^4{\rm He}_4(y)
     =(1-sy)^4-6s^2(1-sy)^2+3s^4+q'[y-s(y^2-1)] .
\]
In particular \(R(1/s+\sqrt3)=-6s^4-q'(\sqrt3+2s)<0\). This proves negative density on a nonempty open interval.

To justify that the same formal moments cannot belong to a different positive probability, suppose a probability has all of them. Its even moments are bounded above by the moments of the absolutely weighted Gaussian polynomial \(|R(y)|\phi(y)\). By monotone convergence of the cosh series, it has finite exponential moments at every real argument. Dominated convergence gives its moment generating function by the entire Taylor series. Undo the affine transformation to conclude that its moment generating function equals \({\cal M}\). But \(P(1/d)=0\) and hence \({\cal M}(1/d)=0\), whereas a positive probability with finite exponential moment has a strictly positive moment generating function at every real point. Equivalently, Fourier uniqueness would identify it with the signed density above, which is impossible.

## 4. Finite Hankel witness

For \([a,b]=[1/20,1/10]\), take the degree-70 polynomial
\[
 Q_{70}(y)=\sum_{j=0}^{70}\frac{(13/2)^j}{j!}{\rm He}_j(y).
\]
The formal normalized squared expectation is
\[
 \frac{E[R(G)Q_{70}(G)^2]}{E[Q_{70}(G)^2]}
   =-0.0011820826117612421070700877231385\ldots< -0.00118 .
\]
This is a finite certificate of failure of positive semidefiniteness in the degree-70 moment Gram matrix, or equivalently in the ordinary monomial Hankel matrix after an invertible basis change. It uses moments only through order 140. To check it, expand the numerator in the five Hermite polynomials of \(R\). The integrals \(E[{\rm He}_i(G){\rm He}_j(G){\rm He}_k(G)]\) vanish unless \(A=(i+j-k)/2\), \(B=(i+k-j)/2\), \(C=(j+k-i)/2\) are nonnegative integers, and otherwise equal \(i!j!k!/(A!B!C!)\). This follows by extracting coefficients in the Gaussian generating product \(\exp(uv+uw+vw)\). Consequently the five integrals involving \(Q_{70}^2\) are exact rationals. Only the five coefficients of \(R\), depending on \(\sqrt{\log 2/2}\), require Arb intervals. At 160 bits the quoted normalized value is enclosed with radius \(6.53\cdot10^{-46}\), and the code asserts the strict threshold above. The same witness construction at degrees 30, 40, 50, and 60 gives positive values and is recorded as such. There is no minimal-degree assertion. [Recorded Arb and exact algebra checks](../../experiments/results/prime79_hlz_formal_moment_obstruction.json)

To replay, run `python scripts/prime79_hlz_formal_moment_obstruction.py` from the repository root with SymPy and python-flint. The saved JSON records the FLINT version and includes both the successful and positive witness evaluations.
