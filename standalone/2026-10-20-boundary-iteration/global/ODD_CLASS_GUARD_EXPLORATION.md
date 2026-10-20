# Exploration: an untwisted odd-class guard and its unavoidable leakage

Status: the local six-class calculation and identities below are exact.
The resulting simpler fixed-prime guard is a proposed source-dependent
alternative, not an input to the frozen boundary theorem. No varying-prime
estimate or improved numerical boundary follows from this note.

## 1. The full local matrix

Use the local normalization and adapted auxiliary prime of
ALL_FIELD_AUXILIARY_GUARD.md, but put
\(W_{0,*}=\mathbf1_{\mathcal O_*^\times}\), insert no character
\(\lambda\) and no auxiliary ideal twist \(\psi\), and restrict the
norm-one probe to \(v_*(t_0)\equiv r\pmod6\), where \(r\) is odd.
Keep the source signed archimedean test, so the global
\(\widehat W_0(0)\) is still zero.

The exact local Fourier transform is
\[
 \widehat{\mathbf1_{\mathcal O^\times}}(y)=
 \begin{cases}
  1-q^{-1},&v(y)\ge0,\\
  -q^{-1},&v(y)=-1,\\
  0,&v(y)<-1.
 \end{cases}                                                    \tag{1.1}
\]
Normalize unit multiplicative measure to one; other normalizations give
one common scalar. For \(b\in\mathbb Z/6\mathbb Z\), define
\[
 L_b(z)=\int_{v(y)\equiv b\ (6)}
          \widehat{\mathbf1_{\mathcal O^\times}}(y)|y|^z\,d^\times y.
\]
For \(\Re z>0\), summing the geometric progression gives
\[
 L_b(z)=\frac{(1-q^{-1})q^{-bz}}{1-q^{-6z}}
       \quad(0\le b\le4),\qquad
 L_5(z)=\frac{q^{-5z}(1-q^{6z-1})}{1-q^{-6z}}.                  \tag{1.2}
\]
At the principal point, put \(x=q^{-1/6}\). Then
\[
       (L_0,L_1,L_2,L_3,L_4,L_5)(1/6)=(1,x,x^2,x^3,x^4,0).
                                                                    \tag{1.3}
\]

The Poisson substitution in the frozen guard's equations (5.1)--(5.3)
now has no character multiplier. For a frequency with
\(v_*(h)\equiv j\pmod6\), its local Mellin multiplier is exactly
\(L_{j+r}(z)\). For the three odd physical row classes, the matrix at
the principal point, with columns \(j=0,\ldots,5\), is
\[
 \begin{pmatrix}
 x&x^2&x^3&x^4&0&1\\
 x^3&x^4&0&1&x&x^2\\
 0&1&x&x^2&x^3&x^4
 \end{pmatrix}.                                                   \tag{1.4}
\]
In particular class \(r=1\) retains the principal frequency with
multiplier \(q^{-1/6}\); class \(r=3\) gives \(q^{-1/2}\); class
\(r=5\) kills it by exact cancellation between the negative Fourier
shell and the infinite positive tail. Counting only the negative
shell would miss that cancellation.

## 2. Why this is a plausible simpler fixed-prime guard

The physical row has \(v_*(m)\equiv r\). The original fixed theta
character is unramified on the new unit line, including its reconstructed
Gauss/Weil character, by the frozen guard's Section 4 calculation.
The source row-unit correction is \(\chi_*^r\), an odd character.
It is minus one on a suitable cube unit, whereas both ordinary Jacquet
constituents, including the central scalar in the Weyl commutation,
are one there. The same actual weighted-sheet argument therefore
annihilates both constants. Exterior rescalings and selected primes
preserve this valuation class.

On the high side there are no inserted character twists to cancel:
every exterior Euler coefficient already contains the original target.
The source high sum is partitioned into its six existing frequency
valuation classes, with the common Mellin multiplier replaced by
the six multipliers \(L_{j+1}(z)\) times the unchanged factors from
the other places. These multipliers are holomorphic in \(\Re z>0\)
and bounded on each closed positive vertical strip, and the unchanged
archimedean factor supplies arbitrary vertical decay. The contour
strips used at the present boundary lie in that half-plane.
The \(u=1\) principal row survives by (1.3).

For one fixed auxiliary prime, the source positive high estimates
can be applied separately to these six fixed classes. On the low side
there is just a positive row restriction and the original auxiliary
ideal polynomial. Thus this construction appears to give the same
fixed-prime theorem with fewer inserted twists. This note does not
replace the reviewed cubic guard or claim uniformity as \(q\) varies.

## 3. Exact leakage identity for every odd-selector combination

For arbitrary coefficients \(a_1,a_3,a_5\), let
\[
                 C_j(z)=\sum_{r=1,3,5}a_r L_{j+r}(z).
\]
Substitution of (1.2) gives the exact relation
\[
 \boxed{\quad
 C_0(z)=\frac{q^{-z}C_5(z)-q^{z-1}C_1(z)}{1-q^{-1}}.
 \quad}                                                           \tag{3.1}
\]
For example it is enough to verify this for the three separate rows;
the negative-shell contribution in \(L_5\) is essential in each check.
Consequently
\[
 \max\{|C_1(\sigma+it)|,|C_5(\sigma+it)|\}
 \ge \frac{1-q^{-1}}{q^{-\sigma}+q^{\sigma-1}}
                         |C_0(\sigma+it)|.                        \tag{3.2}
\]
At the principal point this reads
\[
 \max\{|C_1(1/6)|,|C_5(1/6)|\}
 \ge q^{1/6}\frac{1-q^{-1}}{1+q^{-2/3}}|C_0(1/6)|.                \tag{3.3}
\]
Thus no linear combination of the three odd selectors can isolate
the principal valuation class, or even make all the nonprincipal
class multipliers smaller by a power of \(q\) after principal
normalization. This obstruction permits arbitrary complex signs.

Moving the physical test to an annulus \(v(x)=a\) multiplies all
entries by \(q^{-a(1-z)}\) and replaces its selector by the physical
row class \(r=a+v(t_0)\). Summing arbitrary radial annuli therefore
still gives the same three-dimensional space at each \(z\), so
(3.1) continues to hold. It is not an artifact of one annulus.

For principal normalization relative to the sum of physical weighted
absolute norms, (1.3) shows that the best purely unramified odd class
has norm \(q^{-1/6}\), attained at \(r=1\). This is better than the
ramified cubic channel's \(q^{-1/3}\), but it necessarily leaks into
other frequency classes as in (3.3). Adding cubic channels, which
are supported only at frequency valuation zero, cannot cancel that
leakage: exact isolation forces the unramified part's principal
coefficient to be zero by (3.1). The remaining isolated principal
signal therefore pays the sharp cubic cost established in
AUXILIARY_AMPLIFICATION_EXPLORATION.md.

## 4. Remaining varying-prime barrier

For the \(r=1\) probe in a native reciprocal presentation, write
\(m=\pi a\). The theta symbol contributes \(\chi_{\mathfrak A}(\pi)\),
while Gauss dilation contributes \(\chi_{\mathfrak s}(\pi)^{-1}\).
Thus the varying prime probes the coupled ratio
\(\mathfrak A/\mathfrak s\), with its exact sixth-power cases.
The principal local normalization is now \(P^{1/6}\), so a crude
pointwise prime average \(P^{\beta+\epsilon}\) would only yield a
saving against a \(P\)-sized aligned principal average when
\(\beta<5/6\). This is still below the current boundary.

Moreover, the frequency classes in (1.4), their actual theta
conductors, and the norm-one archimedean profiles must all be tracked
uniformly when the auxiliary prime varies. Treating their former
fixed-prime constants as absolute would be invalid. A genuine gain
requires a new coupled-average estimate or another structural input.

There is also an exact reason that a fixed odd guard cannot improve the
arbitrary-coefficient sextic large-sieve operator. On columns prime to
the auxiliary prime,
\(\chi_{\pi^j u}(b)=\chi_\pi(b)^j\chi_u(b)\).
Multiplication of every column coefficient by the fixed phase
\(\chi_\pi(b)^j\) preserves its squared norm. The restricted row family
is therefore unitarily equivalent to the original one. Any improvement
must use coefficient structure or an average in the auxiliary prime.

## 5. Concurrent scoped audits

The independent type-I agent checked the high-side interface against
Ope26b `05-poisson.tex`, lines 309--386: valuation class is invariant
under \(U_S^6\), the decomposition \(h=ur^6\) retains precisely
\(j=v_*(u)\), and splitting the six classes before the contour
estimates leaves every Euler factor unchanged. The actual transform
\(\mathbf1_\mathcal O-q^{-1}\mathbf1_{\pi^{-1}\mathcal O}\),
the principal value, positive-strip holomorphy, and the inherited
archimedean decay were checked separately. That audit found no
fixed-prime high-side obstruction and makes no growing-conductor claim.

The independent boundary agent checked the exceptional \(L_5\) term,
all three rows of (3.1), the annular dilation, and the physical odd
theta digit against the frozen cube-unit argument. No local defect
was found. These scoped concurrent audits do not turn the exploratory
varying-prime discussion into a proved boundary improvement.
