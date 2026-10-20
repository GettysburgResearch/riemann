# Conditional hybrid sectors for unequal Type-I lengths

20 October 2026. **Proposed conditional consumer of the hybrid
cubic mean.** The common unitary Hecke zero-free premise is an
explicit input; this note does not improve that boundary.

Inputs:

* HYBRID_ANGULAR_MEAN.md, SHA256
  dcf9f71ae9d828f71741ae255be7d41323b9ea3ca7ab184b1c9fbeb31de82ae8;
* CONDITIONAL_ANGULAR_SECTORS.md, SHA256
  313bb31cf85a967533490ccea53d696d02db968717db194682d61a3ee63945a3;
* the uniform actual-family reciprocal theorem and exact reflected
  cubic family cited in those notes.

## 1. Reflect all three terms before stripping the cube factor

Assume a common zero-free half-plane with boundary
\(\beta\in[1/2,1)\) for the actual unitary Hecke characters in
the cube factors. A common theorem for the entire unitary family
is sufficient. Choose a fixed
\[
             \frac{2\beta+1}{6}<p<\frac12,
       \qquad \delta=\frac12-p\in(0,1/6).
\tag{CH1}
\]
For \(\ell\ne0\), put \(L=1+|\ell|+|t|\).
The exact reflected inequality (U7), partial summation, and
the three terms of the hybrid mean (H2) give
\[
 \begin{split}
 \sum_{Nr\le B}^{*}\|\mathbf Q_r^{[\ell]}(p+it)\|^2
 \ll (BL)^\epsilon\{&
       B^{2-2p}L^{4-8p}\\
       &+B^{1-p}L^{4-4p}
        +B^{3/2-p}L^{10/3-4p}\}.
 \end{split}
\tag{CH2}
\]
Indeed the reflection multiplies the right-line normalization
by \(B^{2\delta}L^{8\delta}\).
Every right-line row exponent is greater than \(2\delta\),
so its weighted partial summation is legitimate.
Substituting \(\delta=1/2-p\) gives precisely the displayed
three pairs of exponents.

The ordinary Hecke factor in the cube completion is evaluated
at \(3p-1/2+3it\), strictly to the right of \(\beta\).
Its fixed finite conductor and angular conductor
\(O((1+|\ell|+|t|)^2)\), together with the common-family
reciprocal bound, permit its removal at a cost
\((BL)^\epsilon\).
All deleted Euler factors and natural common-prime zeros remain.
There is no moving quadratic conductor.

For the same actual free-column Type-I form as in (S6), Mellin
inversion and Cauchy over its \(B\) outer rows therefore give
\[
 \begin{split}
 |T_\ell(A,B)|\ll
 (AB(1+|\ell|))^\epsilon A^p\{&
 B^{3/2-p}(1+|\ell|)^{2-4p}\\
 &+B^{1-p/2}(1+|\ell|)^{2-2p}\\
 &+B^{5/4-p/2}(1+|\ell|)^{5/3-2p}\}.
 \end{split}
\tag{CH3}
\]
The radial seminorm order is fixed, independent of \(\ell\);
the contour gap and its constants are fixed before taking
any length or angular limit.
Arbitrary bounded outer coefficients are allowed, but a prime
restriction or arbitrary arithmetic multiplier in the free
inner column is not inserted.

## 2. Fourier localization and the exact limiting widths

Use the fixed periodized smooth bump
\(\phi_{\Delta,\theta_0}\), \(0<\Delta\le1\), with the same
outer coefficient in every Fourier mode.
Absolute Fourier summation in (CH3) gives the error
\[
 \begin{split}
 \left|T_{\phi_{\Delta,\theta_0}}
          -\Delta\!\left(\int\phi\right)T_0\right|
 \ll (AB)^\epsilon A^p\{&
 B^{3/2-p}\Delta^{-2+4p-\epsilon}\\
 &+B^{1-p/2}\Delta^{-2+2p-\epsilon}\\
 &+B^{5/4-p/2}\Delta^{-5/3+2p-\epsilon}\}.
 \end{split}
\tag{CH4}
\]
The zero-angular term is kept exactly. Its possible spherical
main term has not been suppressed.

Write \(A=X^a\), \(B=X^{1-a}\), \(0\le a\le1\).
Compare each term with \(X\Delta\), and let \(p\) approach
\((2\beta+1)/6\) from the right, with a fixed positive buffer.
The resulting three width exponents are
\[
 \begin{split}
 \xi_1(a,\beta)&=\frac a2-\frac{1-\beta}{7-4\beta},\\
 \xi_2(a,\beta)&=
 \frac{2\beta+1+3(3-2\beta)a}{8(4-\beta)},\\
 \xi_3(a,\beta)&=
 \frac{\beta-1+3(2-\beta)a}{2(7-2\beta)}.
 \end{split}
\tag{CH5}
\]
Put \(\Xi_\beta(a)=\min(\xi_1,\xi_2,\xi_3)\).
Whenever \(\Xi_\beta(a)>\eta>0\), the exact discrepancy in
(CH4) is smaller than \(X\Delta\) by a fixed power for
\[
                       \Delta\ge X^{-\Xi_\beta(a)+\eta}.
\tag{CH6}
\]
To obtain this statement choose \(p\) in (CH1) sufficiently
close to its lower endpoint, then allocate all small losses
inside the fixed \(\eta\).
No endpoint reciprocal bound or constant uniform as the gap
vanishes is asserted. If \(\Xi_\beta(a)\le0\), this particular
conditional expression supplies no shrinking-sector conclusion.

## 3. A strict unequal-length improvement over the new hybrid bound

For \(a\ge5/9\), the first exponent in (CH5) is no smaller
than the third. Their difference has positive denominator and
numerator
\[
       a(1+\beta)(7-4\beta)-7(1-\beta)>0.
\tag{CH7}
\]
For clarity this numerator increases with \(a\); at
\(a=5/9\) it increases with \(\beta\in[1/2,1)\) and is already
positive at \(\beta=1/2\).
The other two cross at
\[
              a_c=\frac{23-8\beta}{3(11-4\beta)},
          \qquad \frac59<a_c<\frac57.
\tag{CH8}
\]
Consequently, on this range, \(\Xi_\beta=\xi_3\) below
\(a_c\), and \(\Xi_\beta=\xi_2\) above \(a_c\).

Compare this with the unconditional hybrid exponent
\[
       \xi_{\rm hyb}(a)=
                \min\left\{\frac{1+a}{8},\frac{3a}{10}\right\}.
\]
For \(5/9\le a\le a_c\), the difference is
\[
 \Xi_\beta(a)-\xi_{\rm hyb}(a)
       =\frac{(1-\beta)(9a-5)}{10(7-2\beta)}.
\tag{CH9}
\]
For \(a_c\le a\le5/7\), its positive numerator, over
\(40(4-\beta)\), is
\[
                      5+10\beta-3(1+6\beta)a;
\]
this decreases in \(a\), and at \(5/7\) equals
\(20(1-\beta)/7>0\).
For \(5/7\le a\le1\), the difference is
\[
 \Xi_\beta(a)-\xi_{\rm hyb}(a)
           =\frac{(1-\beta)(5a-3)}{8(4-\beta)}>0.
\tag{CH10}
\]
Thus the conditional hybrid consumer is strictly stronger for
every \(a>5/9\), and agrees at \(a=5/9\).
This includes a substantially larger range than the earlier
coarse conditional consumer.

The positive-displacement refinements in Section 4 of the
unconditional hybrid note do not further improve
\(\xi_{\rm hyb}\) when \(a\ge5/9\).
Indeed, for \(5/9\le a\le5/7\), the third fixed-displacement
threshold has derivative proportional to \(5-9a\le0\).
For \(a\ge5/7\), the middle threshold before \(1/6\) has
derivative proportional to \(3-5a<0\).
After \(1/6\), its enlarged-normalization threshold is at
most \(1/5\), below \((1+a)/8\ge3/14\).
Hence (CH9)--(CH10) compare with the best of those displayed
right-line bounds in this unequal-length range, not merely
with a deliberately coarsened bound.

At balance \(a=1/2\), retain the stronger unconditional
width \((\sqrt{73}-1)/48\) from the hybrid note.
For other ratios one can always take the best applicable
unconditional and conditional expressions.
At \(a=1\), (CH5) reduces to the earlier conditional
\((5-2\beta)/(4(4-\beta))\), approximately \(0.2600\)
at the proposed common boundary.

All statements remain smooth weighted discrepancies from
the exact zero-angular average of the actual free-column
Gauss form. They do not supply a prime-sector theorem or
a new zero-free boundary, and make no assertion about the
quadratic/sextic marked detector.
