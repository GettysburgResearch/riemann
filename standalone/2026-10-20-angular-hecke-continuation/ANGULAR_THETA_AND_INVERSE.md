# Angular inverse moments from the actual exceptional-theta representation

Date: 2026-10-20.

Status: proposed source-dependent analytic proof, with scoped independent
reviews recorded separately. The new work is
the extension of the source's inverse-moment derivation to an explicit
infinite-order angular family. This is not an assumption of an angular
moment theorem or an application of the finite-order zero-free theorem
to an infinite-order character.

The fixed external source is Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), especially
Proposition 4.1, Lemma 4.2, Sections 5--10, and Theorem 18.2.
Its PDF SHA-256 is
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5.
We use its exceptional representation, exterior Whittaker table,
Gauss identities, Kummer sieve inputs, and explicitly specified norm
bookkeeping. Those upstream inputs have the same status as in the
original finite-order argument. We do not certify the whole preprint.

## 1. Statement

Fix a number field \(F\supseteq\mu_{12}\). Let \(\Lambda\) be the
unitary Eisenstein character of source Lemma 4.2, obtained by norm
pullback from \(\mathbb Q(\omega)\). Its complex angular exponents are
\(\epsilon_v\in\{1,-1\}\), with no radial exponent.

Fix an integer \(d\ge2\), \(j\in\mathbb Z\), and a finite-order Hecke
character \(\xi\) of \(F\).
Put

\[
 \nu=\Lambda^{dj}\xi.
 \tag{1.1}
\]

Choose the final finite set \(S\) as in source Section 3, including all
fixed conductors and enough primes to make \(\mathcal O_{F,S}\)
principal. Exterior ideals are coprime to \(S\); all Kummer symbols
retain their natural zero extensions.

### Theorem A: angular inverse moment

For every \(c,\varepsilon>0\), \(C_0>0\), and
\(W\in C_c^\infty((0,\infty))\),

\[
 \sum_{0<N u\le C_0H}
 \left|D^{-1/2}\sum_{\mathfrak a}
       \mu_F(\mathfrak a)\nu(\mathfrak a)
       \chi_{\mathfrak a}(u)
       W(N\mathfrak a/D)\right|^2
 \ll_{F,S,\nu,c,\varepsilon,C_0,W} H(HD)^\varepsilon,
 \qquad
 H\ge\max\{2,D^{1+c}\}.
 \tag{1.2}
\]

The row convention includes the finite unit sectors of the source.
Both common Kummer orientations are permitted. The bound has finite
test-seminorm and polynomial norm-twist orders, as needed for the
scale argument below. No uniformity as \(d,|j|,F\), or the conductor
of \(\xi\) grows is claimed.

### Theorem B: a new angular zero-free family

Under the same upstream inputs,

\[
 \boxed{
 L_F(s,\Lambda^{dj}\xi)\ne0
 \quad\text{for }\operatorname{Re}s>11/12.}
 \tag{1.3}
\]

The pole at one in the principal case \(j=0,\xi=1\) is permitted.
For \(j\ne0\), the character has nonzero infinity type and its
Hecke function is entire.

Varying \(d\ge2\) shows that this covers every
\(\Lambda^m\xi\) with integer \(m\notin\{-1,1\}\).
The integer \(d\) is unrelated to the sextic Kummer row parameter:
the cube completion and sixth-power amplification below keep their
original powers three and six. The fixed coefficient character
requires multiplicativity and the nonresonant angular type, not
an order-dividing-six condition.

### Principal-residue consequence

For the principal correction in the first packet, the extracted
character is

\[
 \nu_\eta=(\overline\Lambda\eta)^6
          =\Lambda^{-6}\eta^6,
\]

where \(\eta\) is finite order. Thus (1.3) applies with \(d=6,j=-1\).
Since the residual factor \(K_\eta\) is a holomorphic unit on
\(\operatorname{Re}s>1/2\), the exact identity

\[
 H_\eta(s)=L_F^S(6s-3,\nu_\eta)K_\eta(s)
\]

gives the strictly stronger principal-protection region

\[
 \boxed{H_\eta(s)\ne0\quad
       (\operatorname{Re}s>47/72),\qquad 47/72=0.652777\ldots .}
 \tag{1.4}
\]

This improves the earlier Euler-product threshold \(2/3\) by \(1/72\).
It does not, by itself, move the final target zero-free boundary:
the other contour terms still require their estimates.

## 2. Higher angular vectors in the same representation

This step uses the actual spherical vector of source Proposition 4.1
and the Lie calculation printed on source p. 33. It is not a change
of the exceptional representation or a conjectured higher-weight
Whittaker model.

At a complex place, regard \(\mathfrak{sl}_2(\mathbb C)\) as a real
Lie algebra, then complexify its action on the smooth representation.
Write

\[
 E(z)=\begin{pmatrix}0&z\\0&0\end{pmatrix},\qquad
 F(z)=\begin{pmatrix}0&0\\z&0\end{pmatrix},\qquad
 w=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Let \(v^\circ\) be its compact-invariant spherical vector. With the
outer scalar \(i\) belonging to the complexification, define

\[
 E_\pm=\tfrac12\{E(1)\mp iE(i)\},\qquad
 F_\pm=\tfrac12\{F(1)\mp iF(i)\}.
 \tag{2.1}
\]

One must not identify this complexification with a single complex
matrix algebra: it is the direct sum of the holomorphic and
antiholomorphic factors. The bracket identities below can also be
checked directly from the real matrix brackets.

Because \(E(z)-F(\bar z)\in\mathfrak{su}(2)\), compact invariance gives

\[
 E_+v^\circ=F_-v^\circ,\qquad
 E_-v^\circ=F_+v^\circ.
 \tag{2.2}
\]

Moreover

\[
 [E_+,F_-]=[E_-,F_+]=0.
 \tag{2.3}
\]

For example the first bracket is one quarter of
\(H(1)+iH(i)-iH(i)+H(-1)=0\).
Equations (2.2)--(2.3), by induction, imply

\[
 E_+^m v^\circ=F_-^m v^\circ,\qquad
 E_-^m v^\circ=F_+^m v^\circ\qquad(m\ge0).
\]

The ordinary Weyl element belongs to the compact group and
\(\operatorname{Ad}(w)E_\pm=-F_\pm\). Consequently

\[
 \pi(w)E_+^m v^\circ=(-1)^m E_-^m v^\circ,\qquad
 \pi(w)E_-^m v^\circ=(-1)^m E_+^m v^\circ.
 \tag{2.4}
\]

These are identities in the same local representation. Its cubic
cover does not change the Lie algebra; at the complex place the
Hilbert-symbol factors in the displayed ordinary sections are
trivial. The original source already uses precisely these sections
and this compact-invariant vector.

For completeness, write its additive character as
\(\psi(z)=\exp(2\pi i\operatorname{Re}(\tau z))\), \(\tau\ne0\).
Whittaker equivariance and
\(a(y)n(z)=n(yz)a(y)\) give

\[
 W_{E_+v}(a(y))=\pi i\tau\,y\,W_v(a(y)),\qquad
 W_{E_-v}(a(y))=\pi i\bar\tau\,\bar y\,W_v(a(y)).
 \tag{2.5}
\]

Here \(\pi i\) means the numerical constant, not the representation.
The source's first-derivative formula therefore determines, after
one fixed nonzero normalization,

\[
 W_{v^\circ}(a(y))
   =x^{1/2}K_{1/3}(c_v\sqrt x),\qquad x=|y|_v=|y|^2.
\]

Normalize
\(v_m=(\pi i\tau)^{-m}E_+^m v^\circ\) and
\(v_{-m}=(\pi i\bar\tau)^{-m}E_-^m v^\circ\) for \(m\ge1\).
The exact higher-angular formula is

\[
 \boxed{
 W_{v_m}(a(y))
 =x^{(|m|+1)/2}\omega_m(y)K_{1/3}(c_v\sqrt x),
 \quad \omega_m(y)=(y/|y|)^m.}
 \tag{2.6}
\]

They are nonzero smooth vectors, indeed compact-finite vectors since
they are obtained by a finite enveloping-algebra action on
\(v^\circ\). Equation (2.4) shows that their Weyl rotations have the
same radial profile with angular sign reversed, up to the fixed
phase \((-\bar\tau/\tau)^m\). That phase has modulus one.

## 3. The angular character on the \(S\)-unit quotient

Let \(\Theta_0\) be the finite group generated by \(\xi,G_0\), the
finite unit characters \(\Upsilon_S\), and their conjugates. The
coefficient set used in the proof is the finite set

\[
 \mathcal C_{d,j}=
 \{\Lambda^{dj}\theta,\Lambda^{-dj}\theta:\theta\in\Theta_0\}.
 \tag{3.1}
\]

It need not be a group. Finiteness and closure under the specific
transformations in Section 5 are what the induction uses.

For \(\nu'\in\mathcal C_{d,j}\), the theta ideal character appearing in
cube completion is \(\vartheta=\overline\Lambda\nu'\) times one of
the fixed finite corrections. Its angular exponents have absolute
values \(|dj-1|\) or \(|-dj-1|\), never zero because \(d\ge2\).

There is an exact global construction of the required local
character. Write \(\vartheta=\prod_v\vartheta_v\) as an idelic Hecke
character, trivial on \(F^\times\), and use the usual ideal convention
outside \(S\). Define

\[
 L_S(y)=\prod_{v\in S}\vartheta_v(y_v)^{-1}.
 \tag{3.2}
\]

For every \(A\in F^\times\),

\[
 L_S(A)=\vartheta((A)_S),\qquad L_S(\epsilon)=1
       \quad(\epsilon\in U_S).
 \tag{3.3}
\]

The second identity follows because an \(S\)-unit has trivial exterior
ideal. This is why a nontrivial infinity type does not obstruct
periodization. Its infinite and finite local phases are not discarded
separately; their product is trivial on \(U_S\).

For the row-unit class \(\upsilon\), multiply \(L_S\) by the source
finite Hilbert-symbol character. Its restriction to \(U_S^6\) remains
trivial. The source digit-average automorphy proof now gives
\(\Gamma=U_S^6\)-invariance unchanged: the exterior compact factors
still act on the original spherical vectors, the \(S\)-component
of the auxiliary compact element is the identity, and the Kummer
digit functions are unchanged on sixth powers. Changing the
archimedean vector does not affect any of these statements.

At a finite place, a continuous unitary character has an open kernel
on the unit group. One proof is to choose an open subgroup whose
image lies in a short arc about one; a subgroup of the circle
contained in such an arc is trivial. Because (3.1) and the row-unit
classes are finite, one can choose one compact open neighborhood

\[
 U\subseteq\prod_{v\in S_f}F_v^{\times6}
\]

contained in every required local unit kernel and in the original
source cutoffs. No triviality on the finite valuation group is
needed. Valuation phases in the rotated finite profiles have
modulus one; the fixed finite-place support and small-norm bounds
remain those of the actual local vectors.

Use at each complex place the vector (2.6) matching the actual
angular exponent of \(L_S\). The sign depends on the ideal/local
convention, but the absolute values above are exact. Multiplication
by finite-order characters and row-unit characters cannot change them.

## 4. Norm-sheet reflection with the same decay exponents

Pair the direct Whittaker function with \(L_S^{-1}\), and the Weyl
rotation with the reversed angular weight, exactly as in source
Lemma 5.1. Each complex angular integral cancels the matching phase.
The representation's constant-term Jacquet characters are pure
norm characters. Since the matching angular exponent is nonzero,
the weighted constant terms vanish. Thus no new constant term is
being omitted.

The exterior coefficient and digit tables are unchanged. Consequently
the unsmoothed theta identity has exactly the same coefficients
and norm scales as source (5.6); only its fixed radial profiles change.
The proof of orbit unfolding uses (3.3), and its absolute convergence
uses the same exterior coefficient majorant. The higher fixed
archimedean powers improve small-norm integrability and retain
exponential decay at infinity.

For \(m\in\mathbb Z\setminus\{0\}\), put

\[
 a_m=(|m|+1)/2-1/6,\qquad b_m=(|m|+1)/2+1/6.
\]

Direct Mellin integration gives

\[
 \int_0^\infty
 x^{(|m|+1)/2}K_{1/3}(c\sqrt x)x^t\,\frac{dx}{x}
 =
 2^{2t+|m|}c^{-2t-|m|-1}
 \Gamma(a_m+t)\Gamma(b_m+t).
 \tag{4.1}
\]

The integral is absolutely convergent for
\(\operatorname{Re}t>-a_m\), with \(a_m\ge5/6\).
It follows by setting \(u=c\sqrt x\) in the usual Bessel Mellin
integral; for \(|m|=1\) it is exactly the source's formula.

The direct Mellin profile is a nonzero constant times the product
of these gamma factors. Weyl reversal (2.4) gives the same radial
factors on the reflected side. The normalized multiplier is therefore

\[
 {\mathfrak m}_{\upsilon,\alpha}(t)
 =E_{\upsilon,\alpha}(t)A^t
   \prod_{v\mid\infty}
   \frac{\Gamma(a_{m_v}+t)\Gamma(b_{m_v}+t)}
        {\Gamma(a_{m_v}-t)\Gamma(b_{m_v}-t)}.
 \tag{4.2}
\]

The fixed phase factors are included in \(E\). Source finite-place
bounds imply that \(E\) is holomorphic and bounded on closed strips
inside \(\operatorname{Re}t>-\delta\), for any fixed \(\delta<1/3\).
The gamma numerator poles lie farther left, and reciprocal gamma
functions introduce no poles. On each fixed vertical strip,
Stirling's formula gives

\[
 |{\mathfrak m}_{\upsilon,\alpha}(\sigma+iT)|
 \ll_{\sigma,F,S,d,j,\Theta_0}(1+|T|)^{4r_F\sigma},
 \qquad r_F=[F:\mathbb Q]/2.
 \tag{4.3}
\]

The exponent is independent of the angular degree. Constants may
depend on that fixed degree. In particular, the finite-place strip
\(\operatorname{Re}t>-1/3\) remains the limiting strip; higher
angular degree does not improve it.

Repeating the Mellin inversion in source Proposition 5.2 now proves,
for \(W\in C_c^\infty(I)\), any \(A>0\), derivative order \(\ell\), and
\(0<a_0<1/3\),

\[
 |(x\partial_x)^\ell\Phi_{W,\upsilon,\alpha}(x)|
 \ll \|W\|_{C^J(I)}\min\{x^{a_0},x^{-A}\}.
 \tag{4.4}
\]

The constants and finite derivative order are simultaneous over
the fixed finite coefficient/profile family. Norm modes \(x^{iT}\)
cost a polynomial in \(1+|T|\) in the test seminorm. We have thus
proved the actual radial input needed by the inverse recursion,
including its uniformity in the varying row.

## 5. Exact closure of the inverse recursion

We now check the coefficient transformations and the analytic
estimates of source Section 10. Finite order is not replaced by
an arbitrary bounded residual column coefficient.

### 5.1. Cube completion

The theta coefficient identity is
\(a_0(n)=\overline\Lambda(n)\gamma_2(n)\) on squarefree columns.
For a multiplicative zero-extended presentation
\(\Psi_u(n)=\nu'(n)\rho(n)\chi_n(u)\chi_n(f)^4\),
the cube-Möbius completion uses

\[
 \mu(h)\overline\Lambda(h)^3\Psi_u(h)^3.
\]

After combining its divisor with the theta cube variable
\(b=hb_0\), multiplicativity gives exactly

\[
 \Psi_u(h)^3\Psi_u(cb_0^3)
 =
 \nu_f(c)\nu_f(b)^3\chi_c(u)\chi_u(b)^3,
 \quad \nu_f(n)=\nu'(n)\rho(n)\chi_n(f)^4.
 \tag{5.1}
\]

Thus \(\overline\Lambda(b)^3\nu_f(b)^3\) belongs entirely to the
cube/label coefficient, independent of the residual column and
current row. Its modulus is at most one before the existing divisor
weight. The variable character is still the same finite-order
quadratic Kummer matrix \(\chi_u(b)^3\). No power \((\nu')^3\)
is passed as a new residual column character.

### 5.2. The terminal reflection

In source Lemma 10.2 the reflected coefficient splits into

\[
 \Omega\,\rho_0(R)\,\beta(n,b)
       \frac{\chi_R(nb)^3}{\sqrt{Nn}\,Nb},
 \tag{5.2}
\]

where the \(L_S\)-dependence is explicitly
\(L_S(R)^2\) in the row factor and
\(L_S(n)^{-1}L_S(b)^{-3}\) in the tuple factor, with a frozen scalar
from the supported numerator. Those formulas use only
multiplicativity and unit modulus. All the finite unit, Gauss,
coprimality and residue-class factors stay in their original places.
The tuple coefficient is independent of \(R\).

Consequently the quadratic--cubic estimate of source Lemma 7.1
applies to exactly the same finite Kummer families. Its arbitrary
bounded *separate* coefficients permit (5.2). No angular phase
is inserted into a varying opposite sieve index. The reflected
profile has (4.4), so source Lemma 10.3 retains its energy bound

\[
 Z^\varepsilon
 \{Z^M+Z^{2M-O/2+Q+V-N_*}\}.
 \tag{5.3}
\]

The local numerator-valuation sums and all norm exponents in that
bound are exterior computations, untouched by the infinity type.

### 5.3. Both Poisson transforms

The row characters entering orbit Poisson are products of Kummer
symbols of order dividing six. The fixed \(\nu'\) is a column
coefficient, not part of the periodic row character. Hence the
order-six requirement in source Proposition 8.1 remains satisfied.

The source Gauss identities, multiplied by \(\nu'\), give the first
and second residual column coefficients

\[
 \begin{split}
  \mu(n)\nu_1(n),&\qquad
    \nu_1=\nu'G_0\xi_{\epsilon_1},
       &&\text{source (10.11)},\\
  a_0(n)\nu_2(n),&\qquad
    \nu_2=\nu_1\overline G_0\xi_{\epsilon_2}
          =\nu'\xi_{\epsilon_1}\xi_{\epsilon_2},
       &&\text{source (10.12)}.
 \end{split}
 \tag{5.4}
\]

Every character on the right belongs to the fixed finite set
\(\mathcal C_{d,j}\). Conjugating a complete side also preserves this
set. Equations (5.1) and (5.4) enumerate every occurrence of a power
or transformation of the fixed character in the recursion: powers
on extracted common factors remain frozen outer phases, while the
residual character changes only by the displayed finite factors.

All shared-prime zeros agree in these identities. The second
Möbius extraction gives the same row and label as in the source,
\(u'=d_kd_2u''\), \(f'=JCd_2v'\), with the same coprimality modulus.
The common-factor coefficient has modulus at most one and remains
outside the column norm. Principal origins and signed restoration
identities are unchanged: the same fixed character occurs on both
conjugate sides, and its common-factor products cancel or have
unit modulus. There is no new projection count.

### 5.4. Closing the finite-depth norm induction

The remaining operations concern norms, finite classes, and
positive separate coefficients. The row lift, its compact dual
support, and its logarithmic kernel bound are unchanged. Formula
(4.4) supplies every column-reflection tail and seminorm estimate.
The common Fourier measure of source (10.2) can therefore be
chosen before the arithmetic indices exactly as there. Increasing
the fixed angular degree changes constants and finite seminorm
orders, not a power of the scale \(Z\).

For clarity, the scalar induction being used is the source
normalized \(a_0\nu'\) energy with \(F=N+V\). Its margin is
\(F-M-Q\ge c>0\). In the terminal range, (5.3) gives the two
exponents bounded by \(F-c\) and \(F-2c+10d_0\), where
\(d_0\) is the small terminal cutoff, unrelated to the angular
integer \(d\ge2\). In a nonterminal
two-transform step the exact normalization is

\[
 \kappa_i+\lambda_c+C_c+2F_c=F,
\]

and, with its prescribed fine-scale allowances,

\[
 M'\le M-2(V+\ell)+32\eta,\qquad
 F'\le F+32\eta.
\]

Each margin loses at most \(128\eta\); the norm estimate and
principal-restoration allowance are covered by the source's
\(256\eta+\tau+\pi+\varepsilon'\) edge allowance.
Choosing \(d_0<c/400\), a fixed depth larger than
\((M_{\max}+2)/d_0\), and then the source small mesh closes the
induction. The finite supremum is taken over \(\mathcal C_{d,j}\)
and its finite profile family. No group law beyond (5.4) is
used in this supremum.

The initialization of source Theorem 10.4 uses the same Gauss
conversion and hence the same set (3.1). Its two margins are
the unchanged \(m-r\) and \(3m-2r\), up to the listed small
initial losses. This proves (1.2), including its test and
norm-twist uniformity. The numerical induction is not being
improved; its newly justified angular input is what extends
its family.

## 6. Sixth-power amplification and zero-freeness

Here the proof can be given without any further theta argument.
For the fixed character \(\nu\) in (1.1), set

\[
 M_u(T)=T^{-1/2}
   \sum_{\mathfrak a}\mu_F(\mathfrak a)\nu(\mathfrak a)
          \chi_{\mathfrak a}(u)W(N\mathfrak a/T).
\]

The logarithmic derivative in scale replaces \(W\) by
\(-W/2-yW'\). Applying (1.2) to these two tests and using
Sobolev on unit logarithmic intervals yields

\[
 \sum_{Nu\le H}\sup_{T_0\le T\le D}|M_u(T)|^2
 \ll H(HD)^\delta,
 \qquad H=D^{1+c},
 \tag{6.1}
\]

for any fixed \(c,\delta>0\), after increasing the threshold.
The relative gap \(c/2\) handles all \(T\le eD\); bounded
scales are finite sums.

For every exterior ideal \(\mathfrak b\), Euler multiplication
gives

\[
 M_1(D)=
 \sum_{\mathfrak d\mid\operatorname{rad}\mathfrak b}
 \mu_F(\mathfrak d)\nu(\mathfrak d)
 (N\mathfrak d)^{-1/2}
 M_{\mathfrak b^6}(D/N\mathfrak d).
 \tag{6.2}
\]

Indeed \(\chi_{\mathfrak a}(\mathfrak b^6)\) is precisely
the coprimality indicator \((\mathfrak a,\mathfrak b)=1\).
This identity is valid for every unitary Hecke character;
finite order is irrelevant.

The absolute divisor mass in (6.2) is
\(\prod_{\mathfrak p\mid\mathfrak b}(1+(N\mathfrak p)^{-1/2})
\ll (N\mathfrak b)^\delta\). There are
\(\gg_{F,S}H^{1/6}\) exterior ideals of norm at most \(H^{1/6}\),
with distinct sixth powers. Averaging (6.2) over them and using
(6.1) gives

\[
 |M_1(D)|^2\ll H^{5/6}(HD)^\delta.
\]

Taking \(c,\delta\) sufficiently small for each prescribed
\(\varepsilon>0\) proves

\[
 \sum_{\mathfrak a}\mu_F(\mathfrak a)\nu(\mathfrak a)
        W(N\mathfrak a/D)
 \ll D^{11/12+\varepsilon}.
 \tag{6.3}
\]

A smooth dyadic partition and the tests \(W(y)y^{-s}\)
make the corresponding reciprocal Dirichlet series locally
uniformly convergent on \(\operatorname{Re}s>11/12\).
It agrees with \(1/L_F^S(s,\nu)\) on \(\operatorname{Re}s>1\).
The identity theorem for its meromorphic Hecke continuation
therefore gives \(L_F^S(s,\nu)G_\nu(s)=1\). A zero of the
Hecke function in this half-plane would contradict this
identity. Finite omitted factors have zeros only on
\(\operatorname{Re}s=0\), because their phases are unitary.
This proves Theorem B and (1.4).

## 7. General-row amplification and the selected inverse moment

The bootstrap also needs the two versions of the inverse estimate
used in source Section 13.4. Both extend to this angular family.

### 7.1. The long inverse count

For sixth-power-free \(u\), retain the exact identity

\[
 M_u(D)=\sum_{\mathfrak d\mid\operatorname{rad}\mathfrak b}
 \mu_F(\mathfrak d)\nu(\mathfrak d)\chi_{\mathfrak d}(u)
 (N\mathfrak d)^{-1/2}M_{u\mathfrak b^6}(D/N\mathfrak d).
 \tag{7.1}
\]

At a prime dividing \(u\), the natural zero makes both local
factors one; at the remaining primes this is ordinary Euler
multiplication. The fixed character is unchanged. Average over
\(N\mathfrak b\ll(H/U)^{1/6}\), for \(Nu\asymp U\), and use
the injectivity of \((u,\mathfrak b)\mapsto u\mathfrak b^6\),
with the finite unit sectors retained. Equation (6.1) gives

\[
 \sum_{Nu\asymp U}^{(6)}|M_u(D)|^2
 \ll U^{1/6}H^{5/6}(HD)^\delta,
 \qquad H\asymp\max\{U,D^{1+c}\}.
\]

For \(D=U^r\) and bounded \(r\), choose \(c,\delta\) small.
This proves the angular form of source Lemma 10.6:

\[
 \sum_{Nu\asymp U}^{(6)}|M_u(U^r)|^2
 \ll U^{e(r)+\varepsilon},
 \qquad e(r)=\max\{1,(1+5r)/6\}.
 \tag{7.2}
\]

The same common profile and height bounds apply.

### 7.2. Statement with selected prime factors

Let the prime lists \(\mathcal P_i\) be disjoint and contained
in fixed-ratio annuli of length \(P_i=Z^{z_i}\). Their bounded
coefficients \(b_i(\mathfrak p)\) are independent of the row and
other columns. Set \(z=\sum_i z_i\), and form

\[
 Q_k=\prod_i P_i^{-1/2}
 \sum_{\mathfrak p\in\mathcal P_i}
 b_i(\mathfrak p)\nu(\mathfrak p)\chi_{\mathfrak p}(k)
 W_i(N\mathfrak p/P_i).
\]

For fixed positive margins

\[
 r+2z<m,\qquad 2r+8z<3m,
 \tag{7.3}
\]

the angular counterpart of source Theorem 11.2 is

\[
 \sum_{0<Nk\le CZ^m}|M_k(Z^r)Q_k|^2
 \ll Z^{m+\varepsilon}.
 \tag{7.4}
\]

Its natural zeros, fixed common coprimality, surviving sublists,
both whole orientations, and finite seminorm and polynomial
height bounds are retained. The number of prime positions is
fixed before \(Z\). As in the source, an initial coprimality
modulus growing with \(Z\) must retain its original exponent
in the initialization; it is not made free by (7.4).

### 7.3. The selected coefficient remains separated

Before a positive estimate, use the exact priority partition

\[
 1_{p\mid D_1\cdots D_t n}
 =\sum_{j=1}^{t}1_{p\mid D_j}\prod_{a<j}1_{p\nmid D_a}
  +1_{p\mid n}\prod_{a\le t}1_{p\nmid D_a}.
 \tag{7.5}
\]

This identity changes no character. Assigned primes stay in
outer factors; surviving primes keep their original list and
coefficient. If a surviving prime meets a transformed row,
label, or coprimality support, its column divisibility mark
forces a natural zero. Restoring its full original list is
therefore an identity of signed polynomials before taking
norms, exactly as in source Section 11.1.

The cube identity remains \(d(h^3nb^3)=d(n(hb)^3)\).
The angular factor \(\nu(hb)^3\) is frozen in the combined cube
variable. In the terminal reflection the full local character
factor separates exactly as

\[
 L_S((RP)^2/(nb^3))
 =L_S(R)^2L_S(P)^2L_S(n)^{-1}L_S(b)^{-3}.
 \tag{7.6}
\]

Here \(R\) is the valuation-one row and \(P\) the active prime
tuple. After their finite power classes are fixed, the residual
finite profile depends only on \(n,b\). Thus the actual terminal
polynomial has the form

\[
 A(R)\sum_P\frac{a(P)}{\sqrt{NP}}1_{(R,P)=1}
 \sum_{n,b}\beta(n,b)\chi_R(nb)^3\chi_P(n)^{-2}1_{(P,b)=1},
 \tag{7.7}
\]

with \(a\) independent of \(R,n,b\) and \(\beta\) independent
of \(R,P\). Formula (7.6), which is the retained character in
source Lemma 11.1, is valid for any multiplicative unitary
\(L_S\). It proves the needed angular independence, rather
than replacing the finite Kummer sieve characters by angular
characters. The local symbol exponents remain \(3,-2,0\)
with their unit indicators.

### 7.4. The selected terminal estimate and induction

The hybrid sieve now applies to precisely (7.7), with the
same separate coefficients. For the source terminal norms
\(K=Z^{H_0},L=Z^{z_a},X=Z^{N_*}\), its scale
\(Y=K^2(ND)^2L^2/(XNa_D)\), and dyads \(U,B\), the bound is

\[
 \|S_{a_D;U,B}\|_2^2
 \ll Z^\varepsilon\frac{K+UB}{UB}
       \{U+L+(UL)^{2/3}\}\,
       m(UB^3/Y)^2,
 \quad m(x)=\min\{x^{1/4},x^{-J}\}.
 \tag{7.8}
\]

Equation (4.4) supplies this same radial majorant, including
derivatives, before separating the common Fourier profile.
Neither the exterior Weyl coefficients nor their valuation
sums change. The three terminal exponents of source Section
11.2 therefore remain

\[
 M+z_a,\quad
 2M-O/2+Q+V-N_*+2z_a,\quad
 M+(Q+V-N_*)/2+2z_a.
\]

Under its two normalized margins
\(F-M-Q-z_0\ge c\), \(4F-3M-6z_0\ge c\), and
\(z_a\le z_0\), with the terminal branch conditions
\(V,\ell_h<2d_0\), their respective upper bounds are
\(F-c\), \(F-2c+10d_0\), and
\(F-M/4-3c/4+5d_0\). Take \(d_0<c/400\).
Inactive marked primes retain their convergent \(Np^{-1}\)
mass. This closes every terminal branch.

For nonterminal children, (7.5) either assigns a prime
position or retains its old scale, so \(z'\le z_0\).
The exact source margin relations give

\[
 F'-M'-Q'-z'\ge c-15\eta_0,\qquad
 4F'-3M'-6z'\ge c-44\eta_0,
\]

and \(M'\le M-2(V+\ell)+32\eta_0\).
The fixed finite character set is still (3.1), by (5.4).
Thus the same finite-depth argument as in Section 5.4 closes
both margins with the retained edge losses.

Finally, initialize from \(M_kQ_k\) itself. For the selected
prime tuple \(P\), assign \(j_0=(n,P)\) of nominal length
\(G\), write \(n=j_0n_0,P=j_0P_0\), and use the squarefree
residual column \(c_0=n_0P_0\). Its length is
\(D'=r+z-2G\), the active cap is \(z_0=z-G\), and

\[
 \psi_k(n)\psi_k(P)=\psi_k(j_0)^2\psi_k(c_0),\qquad
 Z^{-(r+z)/2}=Z^{-G}Z^{-D'/2}.
\]

The contraction \(\psi_k(j_0)^2\) is outside the column norm.
The assigned-tuple count cancels \(Z^{-G}\). Applying the
inverse initialization with the actual coprimality charge
of \(j_0\), the two source margins are

\[
 m-r-2z+2G,\qquad 3m-2r-8z+10G+2P_1.
\]

They are positive by (7.3), with all initial losses chosen
inside those margins. Fixed-ratio windows keep the resulting
profiles uniformly smooth at the actual declared scales.
This proves (7.4). No finite-order assumption on the fixed
angular coefficient enters this initialization or the selected
recursion.

## 8. Limits and the role of the companion proof

The finite-order theorem at \(B_\flat\) is not used in the
angular deduction. The new exponent \(11/12\) comes from the
inverse moment and sixth-power amplification.

The selected product moment of source Section 12 is proved
in the separate ANGULAR_PRODUCT_MOMENT.md adapter. Its
full-annulus prime coefficients, ordinary centering, and
exceptional inducing characters require that separate proof.
The subsequent argument reaching \(B_\flat\) is in
ANGULAR_BOOTSTRAP.md. The present note provides its independent
preliminary \(11/12\) bound, its long inverse count, and its
selected inverse input; it does not assume the bootstrap's
conclusion or import an angular zero-free theorem from a
finite-order one.


## Appendix A. General angular types and finite base change

The same local construction gives a larger family. The following
argument also checks zero local angular degrees, which the initial
power-of-Lambda statement did not need.

### A.1. The criterion

Fix \(F\supseteq\mu_{12}\) and an actual unitary Hecke character
\(\Omega\) of \(F\) with pure angular infinity type and no radial
component. The word “actual” matters: an arbitrary list of angular
integers need not satisfy the global unit condition.

Use the following consistent local convention. For a global Hecke
character \(\chi=\prod_v\chi_v\), put
\(L_{\chi,S}=\prod_{v\in S}\chi_v^{-1}\). At a complex place write

\[
 L_{\Omega,S}(z)=(z/|z|)^{a_v},\qquad
 L_{\Lambda,S}(z)=(z/|z|)^{\lambda_v},
 \quad a_v\in\mathbb Z,\quad\lambda_v\in\{1,-1\}.
\]

Thus \(L_{\chi,S}(A)=\chi((A)_S)\) on global elements, in the
same ideal convention as the inverse-moment proof. Assume

\[
 \boxed{\boldsymbol a\ne\boldsymbol\lambda
        \quad\hbox{and}\quad
        \boldsymbol a\ne-\boldsymbol\lambda.}
 \tag{A.1.1}
\]

#### General inverse theorem

For every integer \(h\) and finite-order Hecke character \(\xi\),
the inverse-moment bound (1.2) of Sections 1--7 above holds
with the following character; the long inverse count (7.2)
and selected inverse moment (7.4) of that note hold as well:

\[
 \nu=\Omega^h\xi.
 \tag{A.1.2}
\]

Consequently

\[
 \boxed{L_F(s,\Omega^h\xi)\ne0
        \qquad(\operatorname{Re}s>11/12),}
 \tag{A.1.3}
\]

with a principal pole at one permitted. Constants may depend on
the fixed field, character, exponent, and finite tests.

To see the relevant nonresonance, suppose an integer \(h\) satisfies
\(h\boldsymbol a=\pm\boldsymbol\lambda\). Every component of the
right side is \(1\) or \(-1\). Since the \(a_v\) are integers,
\(h\) divides one, so \(h=1\) or \(h=-1\). This contradicts
(A.1.1). In particular the theta angular vector

\[
 \boldsymbol m=h\boldsymbol a-\boldsymbol\lambda
 \tag{A.1.4}
\]

is nonzero for every \(h\). Its individual components can be zero.
The same statement holds for the conjugate coefficient orbit.

### A.2. Zero angular degree at some places is permitted

The core proof already constructs every nonzero integer angular
vector by pure root derivatives. At a place with \(m_v=0\), use
the original spherical vector itself:

\[
 W_0(a(y))=x^{1/2}K_{1/3}(c_v\sqrt x),
 \qquad x=|y|_v.
 \tag{A.2.1}
\]

It is fixed by the Weyl element. There is no derivative
normalization to divide by at that place. Its Mellin transform is

\[
 \int_0^\infty x^{1/2}K_{1/3}(c\sqrt x)x^t\frac{dx}{x}
 =2^{2t}c^{-2t-1}\Gamma(1/3+t)\Gamma(2/3+t).
 \tag{A.2.2}
\]

The first gamma pole is at \(t=-1/3\). Therefore this factor,
and the complete multiplier, are holomorphic on every required
strip \(\operatorname{Re}t>-\delta\) with \(\delta<1/3\).
The finite-place estimate already imposed that same strict
restriction. No contour used by the inverse proof crosses this
new pole.

For arbitrary \(m_v\in\mathbb Z\), the uniform form of the local
shifts is

\[
 a_{m_v}=(|m_v|+1)/2-1/6,\qquad
 b_{m_v}=(|m_v|+1)/2+1/6.
\]

Each gamma quotient still contributes
\((1+|T|)^{4\sigma}\) to the fixed-strip estimate. Some zero
degrees consequently change neither the total
\(4r_F\sigma\) exponent nor the finite test-seminorm statement.
The direct Mellin product has no zero, and reciprocal gamma
factors introduce zeros rather than poles.

Absolute sheet integration is also preserved. Near zero,
\(W_0(a(y))=O(x^{1/3})\), while the higher-angular vectors have
still better small-norm powers. At infinity every one of them
has exponential Bessel decay times a fixed power. Thus all
positive-line absolute majorants used in source Lemma 5.1
remain valid.

### A.3. One nonzero component kills the global constant terms

The source Jacquet characters are pure norm characters at every
complex place. The finite class weight is unchanged by complex
rotation because \(\mathbb C^\times/\mathbb C^{\times6}\) is
trivial.

The weighted constant-term function descends to the compact
norm-one quotient \(F_S^1/U_S^6\): this follows from the global
idelic construction of \(L_S\), not from any assertion that
the infinite and finite phases are separately trivial on units.
The compact angular circle at each complex place acts on that
quotient and preserves its measure. At a place where \(m_v\ne0\),
the weighted constant term transforms by the nontrivial
character \(e^{-im_v\theta}\).

Averaging that circle action shows that its integral is zero.
This argument needs only one nonzero component. It does not
assume a product-shaped fundamental domain for the unit lattice.
The Whittaker term, in contrast, has the matching angular
character and survives. By (A.1.4) there is always a place that
kills the constant terms.

Consequently the same unsmoothed reflection, the multiplier with
the shifts above, and the radial decay estimate follow. No
additional constant-term residue has been removed informally.

### A.4. The coefficient recursion needs no further change

For each fixed \(h,\xi\), use the finite coefficient set

\[
 \{\Omega^h\theta,\Omega^{-h}\theta:\theta\in\Theta_0\},
\]

where \(\Theta_0\) contains the fixed finite corrections and
unit characters. All common finite-place kernels exist exactly
as in the core proof. The two residual transformations remain

\[
 \nu_1=\nu G_0\xi_{\epsilon_1},\qquad
 \nu_2=\nu_1\overline G_0\xi_{\epsilon_2}.
\]

The cube factor contains only the frozen phase \(\nu(b)^3\);
the terminal reflection separates the same unitary row and
tuple factors. Nothing in those identities requires that
\(\Omega\) be a power of \(\Lambda\).

Sections 2--3 above supply the only additional local case.
All norm inequalities and finite-depth induction therefore
apply, proving the inverse moment for (A.1.2). The complete
sixth-power amplification and dyadic continuation in Section 6
of the core note then prove (A.1.3). Its Section 7 applies verbatim:
the extra active-prime phase is \(L_S(P)^2\), separate from
the row and the residual columns, and changes no norm margin.

### A.5. Descent by finite base change retains the angular type

Let \(K\) be a number field, \(F=K(\zeta_{12})\), and
\(\Omega_K\) a unitary Hecke character of \(K\) with nonzero
pure angular infinity type. Its norm pullback is
\(\Omega_F=\Omega_K\circ N_{F/K}\).
Suppose its infinity vector over \(F\) satisfies (A.1.1).
Then

\[
 L_K(s,\Omega_K)\ne0\qquad(\operatorname{Re}s>11/12).
 \tag{A.5.1}
\]

Here is a direct justification that does not try to cut out a
finite class field from the kernel of an infinite-order
character. The extension \(F/K\) is finite abelian, with group
\(G\). Exclude a fixed finite set of primes containing all
ramification and conductors. At an unramified prime
\(\mathfrak p\) of \(K\), write \(f\) for the order of its
Frobenius and \(g=|G|/f\). Its \(g\) primes above have norm
\((N\mathfrak p)^f\) and pulled-back character value
\(\Omega_K(\mathfrak p)^f\). On the other side, the values
\(\tau(\operatorname{Frob}_{\mathfrak p})\), for
\(\tau\in\widehat G\), consist of every \(f\)-th root of unity
with multiplicity \(g\). Therefore their local products agree,
and

\[
 L_F^{S_F}(s,\Omega_F)
 =\prod_{\tau\in\widehat G}
     L_K^{S_K}(s,\Omega_K\tau)
 \tag{A.5.2}
\]

first in the absolute-convergence half-plane and then by
meromorphic continuation. The finite characters \(\tau\) have
the class-field interpretation, but \(\Omega_K\) is never
declared finite order.

The left side is zero-free by (A.1.3). Every factor on the right
has the same nonzero infinity type as \(\Omega_K\), hence is
entire. A zero of any one of them would make the product zero.
The omitted Euler polynomials are nonzero on
\(\operatorname{Re}s>0\), since the characters are unitary.
This proves (A.5.1).

### A.6. Imaginary quadratic consequence, including weight two

Let \(K\) be an imaginary quadratic field distinct from
\(E=\mathbb Q(\sqrt{-3})\), and let \(\Omega_K\) be a unitary
Hecke character of nonzero angular degree \(a\in\mathbb Z\).
Take \(F=K(\zeta_{12})\).

Across the complex places of \(F\), the angular vector of
its norm pullback has the sign pattern \(a\epsilon_K\);
the Eisenstein character has the sign pattern \(\epsilon_E\).
Their ratio is the nontrivial quadratic character
\(\epsilon_K/\epsilon_E\) on
\(\operatorname{Gal}(F/\mathbb Q)\). It takes both signs.
It is unchanged by complex conjugation, since both numerator
and denominator change sign, so both values occur on complex
places, not merely on the two representatives of one place.

Thus \(a\epsilon_K\) cannot equal either
\(\epsilon_E\) or \(-\epsilon_E\). This holds even when
\(|a|=1\). Equations (A.1.3) and (A.5.1) prove

\[
 \boxed{
 L_K(s,\Omega_K)\ne0\quad
 (\operatorname{Re}s>11/12),
 \quad K\ne\mathbb Q(\sqrt{-3}).}
 \tag{A.6.1}
\]

Finite-order twists are included throughout. For \(K=E\),
the earlier core proof covers every integer angular degree
other than \(1,-1\). The resonant degree-one types over \(E\)
are not covered by this argument.

For the corresponding dihedral holomorphic automorphic
inductions over \(\mathbb Q\), (A.6.1) is a statement about the
**unitarily normalized** \(L\)-function. Angular degree
\(|a|=1\) corresponds to holomorphic weight two. Thus this
criterion reaches weight-two CM forms over the non-Eisenstein
imaginary quadratic fields. The analytic claim is the Hecke
statement (A.6.1); the automorphic interpretation does not
replace its proof.

For the classical normalization used here, see Molin--Page,
[Computing groups of Hecke characters](https://webusers.imj-prg.fr/~pascal.molin/pdf/hecke.pdf),
19 October 2022, Lemma 4 and Sections 2.5.2 and 5.3.1,
especially Theorem 37. Algebraic type \((k-1,0)\) has unitary
angular degree \(1-k\), up to conjugation; its Hecke series
is a CM newform of weight \(k\), and
\(L_{\mathrm{alg}}(s)=L_{\mathrm{unit}}(s-(k-1)/2)\).
The broader field descent and the final proposed boundary
are developed in FAMILY_DESCENT.md and ANGULAR_BOOTSTRAP.md.
