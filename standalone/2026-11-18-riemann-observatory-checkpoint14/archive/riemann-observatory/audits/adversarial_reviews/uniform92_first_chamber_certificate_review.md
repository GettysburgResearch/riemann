# Independent review of the first-chamber integral certificate

18 November 2026. Both continuum enclosures pass. I rederived the simplex and full-cube formulas, bounded them with independent rational calculations, checked the Arb conversions, and reproduced the recorded script output. The finite projection matrix calculation is outside this review's independent derivation. [Original certificate](prime89_first_chamber_certificate.md) · [Script](../../scripts/prime89_first_chamber_certificate.py) · [Recorded output](../../experiments/results/prime89_first_chamber_certificate.txt)

## Partial crossing and signed error

The integral is over \(a\le x_i\le b\) and \(\sum_i x_i>1\), with density \(\prod_i dx_i/x_i\) and numerator \(A(s)=2(s^3-2s+1)\), \(s=\sum_i x_i\). Under \(y_i=b-x_i\) the Jacobian has absolute determinant one. The domain becomes \(y_i\in[0,d]\), \(S=\sum_i y_i<L\), where \(d=3/50\) and \(L=3/25=2d\). Two distinct strict caps \(y_i>d, y_j>d\) would force \(S>2d\), so their intersection is empty even before disregarding boundaries. Whether one includes boundary faces does not affect the integral. Shifting a single cap's designated coordinate by \(d\) gives simplex size \(L-d=3/50\), numerator \(A(rb-d-S)\), and denominators \(a-y_i\) on the shifted axis and \(b-y_j\) on the others. Symmetry gives four identical cap integrals. In particular \(q=L/b=3/7\) for the full simplex and \(q=(L-d)/a=3/11\) for a cap. Each pole lies outside its entire simplex.

If \(G_i=(1-y_i/c_i)^{-1}\) and \(T_i=\sum_{j=0}^{64}(y_i/c_i)^j\), all terms are nonnegative, and \(0\le G_i-T_i\le q^{65}/(1-q)\). A telescoping product difference has four summands, each bounded by \(q^{65}(1-q)^{-4}\). Multiplying by \(\prod c_i^{-1}\) restores the denominators. For \(T=L'-S\ge0\), the identity \(A(1+T)=2T+6T^2+2T^3\) proves positivity and the maximum at \(T=L'\). Integrating the resulting constant error bound costs the simplex volume \((L')^4/4!\). With \(J_0,K_0\) the truncated full and single-cap integrals and errors \(e_J,e_K\) as in the certificate, this gives
\[
J_0-4K_0-4e_K\ \le I_4\ \le J_0-4K_0+e_J.
\]
The negative multiplier \(-1/8\) reverses the endpoints. The exact rational width \((e_J+4e_K)/8\) is approximately \(2.623234770786839669\times 10^{-27}\). I evaluated the inequality \((e_J+4e_K)/8<263/10^{29}\) using rational arithmetic.

The radial moment identity follows by setting \(y_i=s u_i\), \(\sum_i u_i=1\), whose Jacobian in \(s,u_1,\ldots,u_{r-1}\) is \(s^{r-1}\). The unit-simplex integral of \(u^\alpha\) is \(\prod_i\alpha_i!/(|\alpha|+r-1)!\) by repeated beta integration. The remaining power integral is \((L')^{|\alpha|+r+j}/(|\alpha|+r+j)\). The code's factor \((|\alpha|+r-1)!\) and the single additional radial power denominator are both correct. The signed coefficients of \(A(u-S)\) are \(A(u),4-6u^2,6u,-2\). The one-sided remainder bound comes from the sign of the full polynomial on the domain.

## Independent rational cross-check

I instead used total-degree truncation at \(D=96\) for the product of geometric series and integrated in the nonnegative slack variable \(T=L'-S\). The needed moments are
\[
\int_{S<L'} y^\alpha (L'-S)^j\,dy
=\frac{\prod_i\alpha_i!\,j!\,(L')^{|\alpha|+r+j}}{(|\alpha|+r+j)!}.
\]
This follows by integrating the radial power against \((L'-s)^j\). The integrand uses the three positive coefficients \(2,6,2\) of \(A(1+T)\). For total degree \(m\), the geometric sum has at most \(\binom{m+r-1}{r-1}\) terms, each at most \(q^m\) after factoring out \(\prod c_i^{-1}\). Beyond \(D\), the ratio of consecutive scalar bounds is at most \(q(D+1+r)/(D+2)<1\). Thus the first omitted bound divided by one minus this ratio bounds the whole omitted sum pointwise. The resulting rational interval for \(-I_4/8\) has width about \(3.39784220436554\times10^{-35}\), lies in the reported interval, and is contained in the outward decimal bracket
\[
[-0.000011160937946221134790658139614142,\quad
 -0.000011160937946221134790658139614107].
\]
The calculation uses exact integers and rational numbers through both comparisons.

## Full-cube identity and rounding

When \(ra\ge1\), the region with \(s\le1\) has measure zero. Set \(H=\int_a^b dx/x\) and \(m_j=\int_a^b x^j dx/x\). In expanding \(s^3\), the \(x_i^3\) terms contribute \(r m_3H^{r-1}\), the \(3x_i^2x_j\) terms contribute \(3r(r-1)m_2m_1H^{r-2}\), and the distinct-coordinate terms contribute \(r(r-1)(r-2)m_1^3H^{r-3}\). The latter coefficient counts ordered triples. Multiplying by two and including the linear and constant parts of \(A\) gives the stated expression. Its distinct-coordinate term is absent for \(r=2\). For \(a=13/50,b=8/25\) I bounded \(H=2\operatorname{atanh}((b-a)/(b+a))\) by summing the first 41 positive terms of its power series and adding a geometric bound for the tail. Evaluating the polynomial in \(H\) with signed rational interval arithmetic gave a width below \(1.18\times10^{-85}\) for the correction and an interval contained in the reported full-cube decimal ball.

I replayed the script with python-flint 0.9.0 and obtained a byte-for-byte match to the recorded output. I converted Arb's internal midpoint and radius to exact dyadic rationals. The partial-crossing internal ball contains both exact endpoints constructed by the script, and the two printed decimal balls contain their respective internal dyadic balls. This check distinguishes the partial-crossing rational width bound \(2.63\times10^{-27}\) from the width of the displayed decimal interval, \(3.74\times10^{-27}\). The outward rounding in the displayed interval has no bearing on the exact width bound.
