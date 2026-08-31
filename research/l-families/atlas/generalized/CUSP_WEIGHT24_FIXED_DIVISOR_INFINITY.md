# Fixed-weight zeros and poles of the original cusp-period quotient

Status: proposed theorem, frozen-source review required before integration.
Scope: the actual completed first-coefficient quotient at weight **24**, dimension
two. No weight limit is taken. The zero and pole counts below count distinct
points separately, not just a signed difference.
Authoring base: `eaa8e8263bb34b8b669f911580c9dd9e55766ba2`.

Arithmetic taxonomy: **MIXED: EXACT_RATIONAL / CERTIFIED_INTEGER_COVERAGE**.
The finite checker uses integers and reduced rational numbers, with no rounding,
and covers every coefficient through its declared cutoff. The analytic theorem,
automorphic imports, prime phases, contour radii and counting constants are proved
or imported in this note; they are **not machine-certified numerical data**.

## 1. Statement and literal source

Put \(q=e^{2\pi iz}\), and use the canonical coefficient basis of
\(V=S_{24}(\mathrm{SL}_2(\mathbb Z))\):

\[
 g=\Delta E_4^3-696\Delta^2=q+O(q^3),\qquad
 b=\Delta^2=q^2+O(q^3),\qquad W=\mathbb Cb.                 \tag{FI1}
\]

With the full fundamental domain, invariant measure \(d\mu=dx\,dy/y^2\),
and the literal completed Eisenstein series
\(E^*(z,s)=\pi^{-s}\Gamma(s)\zeta(2s)
\sum_{\Gamma_\infty\backslash\mathrm{SL}_2(\mathbb Z)}\Im(\gamma z)^s\),
where \(\Gamma_\infty\) includes \(-I\), let

\[
 I_s(u,v)=\int_{\mathcal F}y^{24}\overline{u(z)}v(z)E^*(z,s)d\mu,
 \qquad Q_1(s)=\frac{\det I_s|_{(g,b)}}{I_s(b,b)}.           \tag{FI2}
\]

The quotient is continued meromorphically, including across zeros of the
denominator. It is the original quotient associated to \(a_1\), not an eigenline
period and not a new flag chosen to suit the proof. The frozen RQ and CF sources
give continuation and \(Q_1(s)=Q_1(1-s)\), with real conjugation symmetry.

**Theorem FI.** There exists \(\eta>0\) such that for every fixed pair
\(1<\sigma_1<\sigma_2\le1+\eta\), there are constants
\(c_Z,c_P>0\) and \(T_0\), depending on the pair, for which

\[
 \#\{s:\sigma_1\le\Re s\le\sigma_2,\ 0<\Im s\le T,
                 \ Q_1\text{ has a genuine zero at }s\}\ge c_ZT,
\]
\[
 \#\{s:\sigma_1\le\Re s\le\sigma_2,\ 0<\Im s\le T,
                 \ Q_1\text{ has a genuine pole at }s\}\ge c_PT
 \qquad(T\ge T_0).                                      \tag{FI3}
\]

In particular, the original quotient has infinitely many uncancelled zeros and
infinitely many uncancelled poles at this one fixed weight. Its reflection and
conjugation symmetries give the corresponding assertions in the reflected strip
\(1-\sigma_2\le\Re s\le1-\sigma_1<0\).

No value of \(\eta,c_Z,c_P,T_0\), first divisor location, simplicity, exact unsigned
asymptotic, critical-line assertion, RH statement, or new automorphic
representation is claimed. This is a source-specific application of classical
automorphic lifting and prime-twist value theory. There is no global-priority
claim. In particular, a fixed-depth, growing-weight ladder is not used to infer
FI3.

## 2. Exact eigenform reduction, with all cross periods retained

The exact Hecke action is

\[
 T_2|_{(g,b)}=\begin{pmatrix}0&1\\20468736&1080\end{pmatrix}.
\]

These are its actual Fourier pivots: the modular forms involved are determined
by their first two coefficients. The finite checker also checks held-out
coefficients. Set

\[
 d_0=144169,\quad \alpha_\pm=540\pm12\sqrt{d_0},\quad
 f_\pm=g+\alpha_\pm b,\quad \delta=\alpha_+-\alpha_-=24\sqrt{d_0}.
                                                               \tag{FI4}
\]

The eigenvalues are distinct, so the commuting Hecke operators preserve both
one-dimensional eigenspaces. Thus \(f_\pm\) are normalized level-one simultaneous
Hecke eigenforms, not merely eigenvectors for an unrelated finite matrix.
Their coefficients are real and \(b=(f_+-f_-)/\delta\).
Write \(\lambda_\pm(n)=a_{f_\pm}(n)n^{-23/2}\), and define unitary-normalized
finite-part Euler products continued from \(\Re s>1\):

\[
 Z=\zeta(s),\quad S_\pm=L(s,\operatorname{sym}^2 f_\pm),\quad
 C=L(s,f_+\times f_-),\qquad
 A(s)=\pi^{-s}\Gamma(s)(4\pi)^{-s-23}\Gamma(s+23).           \tag{FI5}
\]

Here “finite” refers to nonarchimedean factors, not a truncation of the primes.
At a prime, let the Satake parameters of \(f_+\) be \(u,u^{-1}\) and those of
\(f_-\) be \(v,v^{-1}\). The parameters for \(S_+\) are \(u^2,1,u^{-2}\),
and for \(C\) they are \(uv,u/v,v/u,(uv)^{-1}\). The elementary local identity

\[
 \sum_{a\ge0}\lambda_+(p^a)\lambda_-(p^a)X^a
 =\frac{1-X^2}{\prod_{\epsilon,\epsilon'\in\{1,-1\}}
                       (1-u^\epsilon v^{\epsilon'}X)}       \tag{FI6}
\]

follows from the two Hecke recurrences (or multiplication of the rational
generating functions). With equal forms it yields the diagonal identity.
Consequently literal unfolding gives, with no missing \(\zeta(2s)\) factor,

\[
 X:=I_s(f_+,f_+)=AZS_+,\quad Y:=I_s(f_-,f_-)=AZS_-,\quad
 T:=I_s(f_+,f_-)=AC.                                      \tag{FI7}
\]

Indeed every unfolded entry is \(A\zeta(2s)\sum_n
\lambda_i(n)\lambda_j(n)n^{-s}\). Both cross entries agree, first by this series
and then meromorphically. They are not zero: their normalized first coefficient
is one. A Hecke eigenbasis does **not** diagonalize this period matrix.

The basis change has determinant \(-\delta\), while
\(I_s(b,b)=(X+Y-2T)/\delta^2\). Its factors cancel exactly in FI2:

\[
 Q_1(s)=A(s)\frac{N(s)}{H(s)},\qquad
 H=Z(S_++S_-)-2C,\quad N=Z^2S_+S_--C^2.                  \tag{FI8}
\]

This identity is meromorphic, not just formal. On \(\Re s>1\), \(A\) is
holomorphic and nowhere zero: neither gamma argument meets a pole, gamma has
no zeros, and the exponential factors never vanish.

For clarity about cancellation, put \(H_c=X+Y-2T\),
\(J_c=X-Y\), \(K_c=X+Y+2T\). Then

\[
 Q_1=\tfrac14(K_c-J_c^2/H_c).                              \tag{FI9}
\]

At an ordinary point with \(\operatorname{ord}H_c=m>0\) and
\(\operatorname{ord}J_c=r\), the pole order is \(\max(m-2r,0)\).
Thus a pole of \(J_c/H_c\), or a denominator zero count alone, is not enough.
The proof below pays the stronger condition \(H=0,N\ne0\) directly.

## 3. The four primitive automorphic inputs

The application uses the four representations attached to
\((Z,S_+,S_-,C)\), of degrees \((1,3,3,4)\). The following verifies every
cuspidality, distinction and Ramanujan hypothesis of the value theorem.

First, the level-one \(\mathrm{GL}_2\) representations \(\pi_\pm\) are unitary
cuspidal with trivial central character and are unramified at every finite prime.
If either had a self-twist by a character \(\chi\), central characters would force
\(\chi^2=1\). A ramified \(\chi_p\) cannot preserve an unramified representation:
its unramified two-dimensional local parameter is trivial on inertia, while its
twist has inertia acting by the nontrivial scalar \(\chi_p\). Hence \(\chi\)
would be unramified at all finite primes. A quadratic idele class character of
\(\mathbb Q\) with this property is trivial (equivalently, a nontrivial quadratic
extension has discriminant of absolute value greater than one). This also rules
out induction from a character of a quadratic extension, since such an induction
has the associated nontrivial quadratic self-twist; see Ramakrishnan,
Proposition 2.3.1(2), pp.53-54.

Gelbart--Jacquet, Theorem 9.3(3), p.534, therefore supplies cuspidal \(\mathrm{GL}_3\)
lifts. Their lift is the adjoint lift; the central characters here are trivial,
so it is exactly the symmetric-square normalization in FI5.

The pair \(\pi_+,\pi_-\) is not twist equivalent either. Such a twist would
again be quadratic and unramified, hence trivial, whereas \(\alpha_+\ne\alpha_-\).
Alternatively already at \(p=2\) a quadratic twist requires equal squares, but

\[
 \alpha_+^2-\alpha_-^2=25920\sqrt{144169}\ne0.              \tag{FI10}
\]

Ramakrishnan's Theorem M, p.54, now supplies the cuspidal \(\mathrm{GL}_4\)
tensor product, with the local factors in FI6. Its published one-page correction
changes a running-header spelling only, not this theorem.

The two symmetric squares are not isomorphic: their coefficient at two is
\(\lambda_\pm(2)^2-1\), different by FI10 divided by \(2^{23}\). The other
degrees differ. All four representations are thus pairwise nonisomorphic.
The trivial \(\mathrm{GL}_1\) representation giving \(\zeta\) is included;
cuspidality for degree one has no proper-parabolic condition. Their central
characters are unitary, and the cuspidal lifts are taken in unitary normalization.
Deligne's theorem gives \(|u|=|v|=1\) at every finite prime. The displayed
Satake products show the required Ramanujan bound for both lifts as well.
No unproved general \(\mathrm{GL}_4\) Ramanujan conjecture is invoked.

## 4. Correction-aware simultaneous prime twists

We use **Booker--Thorne, Proposition 3.1**, p.2034: for the above pairwise
nonisomorphic unitary cuspidal inputs satisfying finite-place Ramanujan, given
\(y,R>1\) there is \(\eta>0\) such that, for every
\(1<\sigma\le1+\eta\), their common prime-wise phase twists over \(p>y\)
jointly attain every tuple whose coordinates have moduli between \(R^{-1}\)
and \(R\). This is a value statement for absolutely convergent products, not a
claim that an arbitrary twist is automorphic.

Their 2018 correction replaces an incorrect uniform error term in Lemma 2.1 by
\(O(1/\log(2/(\sigma-1)))\); it still tends to zero and leaves Proposition 3.1
and the main conclusions intact. We use no quantitative rate from the original
incorrect estimate.

Take \(y=3/2\) and \(R=4\). Every prime is greater than \(y\), so no finite
Euler factors have been dropped or silently retuned. One \(\eta\) works for
both of the following exact targets:

| purpose | \((Z,S_+,S_-,C)\) | \(H\) | \(N\) |
| --- | --- | --- | --- |
| pole | \((1,1,4,5/2)\) | \(0\) | \(-9/4\) |
| zero | \((1,1,4,2)\) | \(1\) | \(0\) |

For any chosen \(\sigma\), let \(\chi(p)=p^{-it_p}\) be the phases supplied
for one target, extended completely multiplicatively. They are common to all
four Euler products. The corresponding \(H_\chi,N_\chi\) are analytic on
\(\Re s>1\). Because the polynomial coefficients in FI8 are constants, their
Dirichlet coefficients are exactly \(h_n\chi(n),n_n\chi(n)\).

Both constant coefficients vanish, and both coefficients at \(n=2\) equal

\[
 h_2=n_2=(\lambda_+(2)-\lambda_-(2))^2
 =\frac{83041344}{2^{23}}=\frac{1297521}{131072}>0.          \tag{FI11}
\]

Consequently neither twisted function is identically zero: its leading
Dirichlet coefficient is \(\chi(2)h_2\ne0\). More explicitly, multiplying its
series on the positive real axis by \(2^s\) and letting \(s\to\infty\)
recovers this coefficient by absolute convergence. This is the necessary
nonconstant analytic-function check; a single attained value alone would not
justify Rouché.

## 5. Complete tails, simultaneous contours, and distinct-point counts

Let \(d_r(n)\) count ordered factorizations into \(r\) positive integers.
Unit-modulus local parameters give the coefficient majorants

\[
 |h_n|\le4d_4(n),\qquad |n_n|\le2d_8(n).                  \tag{FI12}
\]

For example \(ZS_\pm\) and \(C\) each have degree four, while
\(Z^2S_+S_-\) and \(C^2\) each have degree eight. Products of their coefficient
majorants use Dirichlet convolution, not pointwise multiplication.
Thus both series converge absolutely and locally uniformly on \(\Re s>1\),
uniformly in all prime twists. This pays the entire omitted tail, not just a
finite prime prefix. An explicit optional tail majorant, for \(M\ge1,a>1\), is

\[
 \sum_{n>M}d_r(n)n^{-a}\le
 aM^{1-a}\sum_{j=0}^{r-1}\binom{r-1}{j}
 (1+\log M)^{r-1-j}\frac{j!}{(a-1)^{j+1}}.               \tag{FI13}
\]

Indeed \(\sum_{n\le x}d_r(n)\le x(1+\log x)^{r-1}\), by summing the last
factor and bounding the other harmonic sums. Partial summation, discarding the
nonpositive endpoint term, gives the integral of this bound; expanding after
\(x=Me^u\) gives FI13. For fixed \(a>1,r\), it tends to zero as \(M\to\infty\).

Fix \(1<\sigma_1<\sigma_2\le1+\eta\) and their midpoint \(\sigma\). For the
pole target, \(H_\chi(\sigma)=0\) and \(N_\chi(\sigma)\ne0\). Choose a closed
disk \(D=\{|s-\sigma|\le\rho\}\) strictly inside the strip, small enough that
\(N_\chi\) is nonzero throughout \(D\), and with \(H_\chi\) nonzero on its
boundary. Such a radius exists because the former condition is open and zeros
of the latter nonzero analytic function are isolated. Write
\(\gamma=\min_{\partial D}|H_\chi|>0\) and
\(\nu=\min_D|N_\chi|>0\).

Choose a finite coefficient cutoff whose **two** absolute tails on
\(\Re s\ge\sigma_1\) are less than one quarter of their respective margins.
For the finitely many primes in that prefix, simultaneous approximation of
\(p^{-it}\) to \(\chi(p)\), with sufficiently small tolerance, makes

\[
 \sup_D|H(s+it)-H_\chi(s)|<\gamma,\qquad
 \sup_D|N(s+it)-N_\chi(s)|<\nu.                           \tag{FI14}
\]

The omitted untwisted and twisted tails each use FI12, so no assumption about
uncontrolled phases remains. The first inequality on \(\partial D\) and
Rouché give at least one zero of \(H(s+it)\) in \(D\), counted with its positive
analytic multiplicity. The second inequality ensures that \(N(s+it)\) has no
zero anywhere in \(D\). FI8 and the nonvanishing of \(A\) therefore make every
such denominator zero an actual pole of \(Q_1\).

For the zero target, interchange the roles: choose the disk with \(H_\chi\)
nonzero throughout and \(N_\chi\) nonzero on the boundary, then approximate
both functions with the corresponding margins. This gives a numerator zero
with no denominator cancellation and hence an actual zero of \(Q_1\).

For completeness, the good shifts in each construction have positive lower
Lebesgue density on the **positive** real axis. Distinct prime logarithms are
rationally independent: an integer relation exponentiates to a forbidden prime
factorization of one. For every nonzero integer vector, the time average of
\(e^{-it\sum m_p\log p}\) tends to zero. Approximating continuous functions
on the finite torus by trigonometric polynomials proves equidistribution of the
one-parameter flow; a continuous nonnegative bump supported in the open phase
box and positive somewhere gives a positive lower density of good shifts.
This is also the approximation mechanism in Booker--Thorne, pp.2040-2041.

Restrict those shifts to \(\rho<t<T-\rho\). Every good shift has a divisor in
the translated disk, hence with imaginary part in \((0,T)\). A fixed divisor
can account for shifts in an interval of length at most \(2\rho\). The union
of these intervals covers the good shifts, whose measure is at least a fixed
positive multiple of \(T\) for sufficiently large \(T\). Dividing by
\(2\rho\) proves the **distinct-point** lower bound in FI3. No simplicity or
uniform bound on multiplicity is assumed. This proves the theorem.

## 6. Exact finite replay and what it does not certify

The companion producer reconstructs \(E_4,\Delta,g,b\) through \(q^{64}\),
the \(T_2\) pivots and held-out action, the quadratic eigenvalue data, and every
ordinary Dirichlet coefficient of \(H,N\) through \(n=64\). It compares the
eigenform determinant with a second coefficient-basis Gram determinant,
retaining all square-divisor contributions from \(\zeta(2s)\).
Prime-power recurrences test the local tensor Euler factors. Exact rational
target and valuation controls catch the distinction between a denominator zero
and a genuine pole. Independent tests reconstruct the q-prefix by the Euler
product for \(\Delta\), and the Dirichlet coefficients by explicit divisor
sums, rather than calling the same producer recursively.

All untrusted JSON is size/depth/node/type bounded; duplicate keys, bools,
floats, nonfinite values, nulls, extra fields and resealed altered payloads are
rejected. Validation reconstructs the entire expected fixture and authenticates
frozen Git blobs with replace objects disabled, LF SHA256 identities and all
four non-fixture artifact hashes. Assertions are not acceptance gates, so
optimized Python has the same rejection contract. This does not independently
prove the imported analytic theorems or produce \(\chi,\rho,\eta,T_0\).

Primary imports, read in their published normalization:

- [Booker--Thorne](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf),
  Theorem 1.2 hypotheses, Proposition 3.1 and pp.2040-2041;
  [their correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf), both pages.
- [Gelbart--Jacquet](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf),
  Theorem 9.3(3), p.534, with the adjoint normalization on p.472.
- [Ramakrishnan](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf),
  Proposition 2.3.1(2), Theorem M, pp.53-54;
  [running-header correction](https://emis.muni.cz/journals/Annals/152_3/correction.pdf).
- [Holowinsky--Soundararajan](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p18-p.pdf),
  section 2, the unitary Hecke normalization and Deligne bounds.

The smallest load-bearing imported step is the correction-aware joint
prime-twist surjectivity for the four verified primitive inputs. Replacing it
by a theorem asserting denominator zeros alone would not prove this result.
