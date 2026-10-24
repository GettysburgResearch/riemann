# A signed sixth-moment reduction using the sextic root number

24 October 2026. Research status: exact finite and functional-equation
reductions, with an identified remaining analytic estimate. This note does
**not** prove a sixth-moment exponent, and does not change a zero-free
boundary. The squarefree row case is separated from the general row case.

## 1. Sources and the quantitative target

The arithmetic identities and the fourth-moment argument are from
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`.
The local copy `arithmetic_lane/ope26a_source.tex` has SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
Relevant labels are `lem:fixed-gauss-phase`, `lem:hecke-strip-growth`,
`lem:plain`, `old-eq:2.12`, and `old-eq:2.1h`.

The primitive sextic root-number normalization is independently visible
in Gao--Zhao, *Moments and one level density of sextic Hecke L-functions*,
[arXiv:2201.01885v2](https://arxiv.org/pdf/2201.01885), Section 2.4,
equation (2.8): on its squarefree class congruent to one modulo 36 the
root number is the sextic Gauss sum divided by the square root of the
conductor norm. Its additive character uses the same different as the
source convention. The finite ray partition above extends this
normalization to the fixed twists under consideration.

For comparison, de Faveri, *Optimal large sieve for fixed order
characters*, [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
Sections 1.3.2--1.3.3 and 8, treats root-number coupling and a second
moment of cubic characters parameterized by their conductor. That second
moment is not a sixth moment of the sextic family considered here.

Write a proposed central sixth-moment bound as

\[
 \sum_{Nu\asymp U}|L(1/2+it,\psi_u)|^6
 \ll U^{1+\delta_6+\epsilon}(1+|t|)^C.                 \tag{1}
\]

At the root agent's current limiting class, the parameters are

\[
\begin{split}
 R&=0.59033235352635579359,\\
 \theta&=0.05216519695620035706,\\
 \ell_y&=0.45970744037451584266,\\
 h&=0.79394759738813612843.
\end{split}
\]

Unamplified Holder gives selected-row exponent
\((5R+1+\delta_6)/6\). Against an unamplified fourth moment the sufficient
inequality is

\[
 \delta_6<(1-R)/2=0.204833823236822103205.
\]

The current fourth-moment consumer already includes an amplification
shift. Its effective numerator exponent is

\[
 E_4=\frac{3R+1}{4}+\frac\theta2-\theta\frac{\ell_y}{h}
 =0.68862744049940498104.
\]

Consequently an **unamplified** replacement (1), with the amplifier
parameter reset to zero, must satisfy the stricter scalar condition

\[
 \boxed{\quad
 \delta_6<\frac{1-R}{2}
       -6\theta\left(\frac{\ell_y}{h}-\frac12\right)
 =0.18010287536465091825.
 \quad}                                                     \tag{2}
\]

These are consumer calibrations, not a claim that (1), or its full moving
mask and row uniformity, has been established.

## 2. The squarefree sextic root-number cube

Use the source's primary generators in the Eisenstein ring, put
\(\alpha(c)=c/|c|\), and retain zero extensions at nonunits. For a good
squarefree primary ideal \(c\), the source proves

\[
 \gamma_2(c)^3=\mu(c)\alpha(c),\qquad
 \gamma_1(c)=G(c)\gamma_2(c)^2.
\]

Here \(G\) is a fixed finite ray function, with its quadratic-refinement
law retained. It follows exactly that

\[
 \boxed{\gamma_1(c)^3=G(c)^3\alpha(c)^2.}             \tag{3}
\]

In particular the cubic power has neither a remaining Gauss factor nor a
Möbius factor. A finite ray function may be expanded in a fixed finite
character basis; it need not itself be treated as one character.

Fix the finite-order twist of the family, and partition the squarefree
row \(u\) into finitely many fixed ray classes, away from its fixed bad
prime support. On each class, the primitive conductor is
\(\mathfrak f_0(u)\) with norm \(Q_u=c_0Nu\), where the bad conductor
part \(\mathfrak f_0\) is fixed on that class. The finite primitive Gauss
sum factors by CRT into the good Gauss sum \(\gamma_1(u)\), the fixed
bad-prime Gauss sum, and cross-character evaluations on the fixed bad
modulus. The latter evaluations are fixed ray functions of \(u\).
The different and primary-generator conventions likewise change only
this fixed ray data. Hence the primitive root number has the form

\[
 \varepsilon(\psi_u)=\xi(u)\gamma_1(u),
 \qquad |\xi(u)|=1,
\]

with \(\xi\) a fixed finite ray function on the class. Thus

\[
 \varepsilon(\psi_u)^3=\rho(u)\alpha(u)^2,
 \qquad \rho(u)=\xi(u)^3G(u)^3.                    \tag{4}
\]

The same assertion holds for the source's displayed orientation
\(\psi_u(n)=\tau(n)\chi_n(u)\): sextic reciprocity first transfers it
to \(\chi_u(n)\) on a fixed row ray class, changing the fixed finite
twist. If the whole family is conjugated, the angular exponent and all
Gauss orientations in (3)--(4) must be conjugated together.

## 3. Apply the approximate functional equation to the sixth power

In this section the primitive inducing character is nonprincipal. A
nonunit good squarefree row has a prime with local character of exact
order six, so this holds after the fixed-prime exclusions above. Any
bounded unit/principal exceptions are separated first; their usual
polar terms are not included in formula (6).

Let

\[
 C_u=\frac{3Q_u}{(2\pi)^2},\qquad s=\frac12+it,
 \qquad
 E_u(t)=\varepsilon(\psi_u)C_u^{-it}
             \frac{\Gamma(1/2-it)}{\Gamma(1/2+it)}.
\]

The primitive functional equation gives
\(L(s,\psi_u)=E_u(t)\overline{L(s,\psi_u)}\), and \(|E_u(t)|=1\).
Therefore, including a vanishing central value,

\[
 |L(s,\psi_u)|^6=E_u(t)^{-3}L(s,\psi_u)^6.           \tag{5}
\]

Choose a real even entire rapidly decreasing AFE test. Apply the
functional equation to the degree-six power itself. The two AFE sums
are conjugate after multiplication by \(E_u(t)^{-3}\), so

\[
 |L(s,\psi_u)|^6
 =2\Re\left\{
 E_u(t)^{-3}\sum_{\mathfrak n}
 \frac{d_6(\mathfrak n)\psi_u(\mathfrak n)}
      {(N\mathfrak n)^{1/2+it}}
 V_t\left(\frac{N\mathfrak n}{C_u^3}\right)
 \right\}.                                                   \tag{6}
\]

Here \(d_6\) is the sixfold ideal divisor function; one possible test is

\[
 V_t(x)=\frac1{2\pi i}\int_{(a)}
 H(z)\frac{\Gamma(1/2+it+z)^6}
            {\Gamma(1/2+it)^6}x^{-z}\frac{dz}{z},
 \qquad a>0.
\]

This identity avoids an expansion into 64 independently estimated
one-factor AFE branches. In the bounded-height conductor aspect its
natural total column length is \(N\mathfrak n\asymp U^3\). At general
height the archimedean scale and profile seminorms must also be retained.

By (4), the row-dependent factor in (6) is a fixed ray function times
\(\alpha(u)^{-2}(Nu)^{3it}\). The other factors in \(E_u(t)^{-3}\)
are fixed on a ray class or depend only on \(t\). On a dyadic column
block, the radial dependence of \(V_t(N\mathfrak n/C_u^3)\) is a
coupled smooth function of \(Nu/U\) and \(N\mathfrak n/U^3\).
It can be separated by the source's common Mellin calculus, keeping
its derivative and height bounds. It is not replaced by an unrelated
row cutoff for every column.

## 4. Exact angular row Poisson, including the squarefree sieve

After fixed-ray expansion and reciprocity, a radial row block has the
form

\[
 \sum_{u\ {\rm primary}}\mu^2(u)\eta(u)\chi_n(u)
       \alpha(u)^{-2}\Phi_n(Nu/U),                  \tag{7}
\]

where all fixed punctures are included in the periodic zero extension
and \(\eta\) is one of finitely many fixed ray characters.
Insert the exact identity \(\mu^2(u)=\sum_{d^2\mid u}\mu(d)\).
For each \(d\), write

\[
 Y=U/(Nd)^2.
\]

The scalar outside the residual row sum is
\(\mu(d)\eta(d^2)\chi_n(d^2)\alpha(d)^{-4}\). In particular it is
zero if a prescribed natural zero forces it to be zero.

Choose a period \(m\) for the remaining periodic row function
\(T_n(v)\). It includes the fixed ray and primary congruences and every
prime dividing \(n\); \(m=m_0\operatorname{rad}(n)\) is admissible
after enlarging the fixed modulus. Define the literal finite sum

\[
 \mathfrak g_n(h;m)=\sum_{a\bmod m}T_n(a)e(ha/m).
\]

For the source's self-dual plane measure and Fourier pairing, define
\(\mathcal H_2\) by

\[
 \widehat{\alpha(z)^{-2}\Phi(Nz)}(y)
       =\alpha(y)^2\mathcal H_2\Phi(Ny),\qquad y\ne0.
\]

This convention includes the harmless constant phase in the angular
Hankel transform. Plane Poisson gives the exact formula

\[
 \sum_v T_n(v)\alpha(v)^{-2}\Phi_n(Nv/Y)
 =\frac{Y}{Nm}\sum_{h\ne0}
      \mathfrak g_n(h;m)\,
      \alpha(h)^2\alpha(m)^{-2}
      \mathcal H_2\Phi_n\left(\frac{YNh}{Nm}\right).          \tag{8}
\]

The omitted term \(h=0\) is **exactly zero**: the plane integral of a
radial function times \(\alpha(z)^{-2}\) vanishes. Also
\(\mathcal H_2\Phi(x)=O(x)\) at zero and has arbitrary decay at
infinity for compact smooth annular \(\Phi\). The nonzero terms in
(8) cannot be discarded; (6) is a positive moment despite its signed
representation.

Formula (8), summed with the exact \(d\)-scalars, retains the whole
squarefree sieve. Its natural frequency scale is

\[
 H\asymp Nm/Y=Nm\,(Nd)^2/U.                          \tag{9}
\]

For squarefree good \(n\), fixed-prime decomposition of
\(\mathfrak g_n\) leaves the good factor
\(\sqrt{Nn}\gamma_1(n)\overline{\chi_n(h)}\), with all fixed
factors and their natural zeros kept. In the principal sieve branch
\(d=1\), the generic critical scales are therefore

\[
 \boxed{Nn\asymp U^3,\qquad Nh\asymp U^2,\qquad
  \text{prefactor per normalized column }U/(Nn).}             \tag{10}
\]

The complete generic summand includes

\[
 U\,\frac{d_6(n)}{Nn}\,
       \gamma_1(n)\alpha(n)^{-2}
       \overline{\chi_n(h)}\alpha(h)^2,
                                                               \tag{11}
\]

times the retained fixed ray factors and the coupled Hankel profile.
In a branch \(d\ne1\), the coefficient \(U\) in (11) is replaced
by \(U/(Nd)^2\), and the frequency range grows as in (9). This
growth must be paid when bounding the whole sieve tail.

## 5. A second exact simplification: the Möbius cubic Gauss factor

For good squarefree \(n\), (3) gives a more useful linear identity:

\[
 \boxed{\quad
 \gamma_1(n)\alpha(n)^{-2}
   =\mu(n)G(n)\alpha(n)^{-1}\overline{\gamma_2(n)}.
 \quad}                                                        \tag{12}
\]

Indeed \(\gamma_2(n)^2=\mu(n)\alpha(n)
\overline{\gamma_2(n)}\). Thus the generic transformed sixth moment
contains a Möbius-weighted **cubic** Gauss coefficient.

There are two material differences from the proved third-pass cubic
moment:

1. The character in (11) remains the **sextic**
   \(\overline{\chi_n(h)}\), with unrestricted \(h\), not a cubic
   character on an ordinary row of the same scale.
2. Its coefficient includes \(d_6(n)\), and the full expansion includes
   nonsquarefree \(n\). The third-pass moment proved a particular
   Möbius coefficient class; a divisor bound on \(d_6\) does not
   justify replacing that structured class by this one.

For example, writing \(h=ab^2\), with squarefree \(a\), leaves a
moving sextic twist from \(a\) and a cubic twist from \(b\). The
companion `MOVING_SEXTIC_TWIST_EXTENSION.md` now supplies a proposed,
independently reviewed extension for such a twist of conductor norm
\(T\), in its stated \(A\ge B\) cubic moment and \(T\le B^{2/3}\)
range. Its rectangular version has the stricter shortened-column
condition \(T\le(B/C)^{2/3}\), with
\(C\asymp(B/A)^{1/3}\). These are quantified hypotheses, not
unrestricted uniformity in the new moving twist. They do not yet
cover the entire signed form (11): the \(d_6\) coefficient requires
its own structured adaptation, the displayed cubic row range must
match, and the nonsquarefree column and sieve branches remain.

## 6. Why the existing coupling theorem does not close (11)

In the coprime squarefree sector, Gauss multiplicativity is

\[
 \gamma_1(ab)=\gamma_1(a)\gamma_1(b)
                   \chi_a(b)\chi_b(a).
\]

After a finite ray partition, the cross factor is the cubic symbol
\(\chi_a(b)^2\), up to a fixed unit phase. Consequently the
six-variable sum grouped into three variables on each side has the
nonseparable factor

\[
 \chi_a(b)^2\overline{\chi_a(h)}
 =\overline{\chi_a(hb^4)}                         \tag{13}
\]

on its actual coprime support. The exponent four in (13) cannot be
changed to two for a sextic character. This is a different coupling
from the cubic conductor identity in de Faveri Section 8, where an
outer variable combines multiplicatively with a Poisson frequency
after a conjugation particular to order three.

As a size check, put \(Na,Nb\asymp U^{3/2}\), and normalize each
group coefficient by its square root of norm. The ordinary cubic
large sieve bounds the resulting bilinear form for a fixed \(h\) by
\(U^{1+\epsilon}\). The scalar outside it is
\(U/\sqrt{NaNb}\asymp U^{-1/2}\). Summing this estimate absolutely
over \(Nh\ll U^2\) costs \(U^{5/2+\epsilon}\). This is worse than
the existing fourth-moment route; it is only a diagnostic of that
particular use of the coupling, not an impossibility result.

## 7. The positive three-factor induction has a separate diagonal cost

Simply replacing the two plain factors in the source's `lem:plain`
by three does not prove a useful sixth moment. After individual full
reflection, the source gives each length at most \(M/2+o(1)\), but
the total is now allowed to be \(A=3M/2+o(1)\), instead of
\(A\le M+o(1)\).

In the clean balanced sector \(n_1=n_2=n_3=M/2\), with all common
supports trivial, the first transformed row width is
\(K_0=2A-M=2M\). The positive Gauss norm used in the second transform
has a genuine zero-frequency diagonal. Source equation
`old-eq:2.12` measures its excess as

\[
 A-M=M/2.                                             \tag{14}
\]

Centering equal-product-scale boxes removes the exceptional fixed
character volume term in the source induction; it does not remove
this positive diagonal. Before Cauchy and enlargement, the original
coprime bilinear form would make that diagonal force \(a=b=1\).
Retaining the signed coprimality through a width-reducing argument
would be an additional analytic step. Taking two exact Poisson
transforms without that width change merely returns the original
sum.

Thus (14) is an exact obstruction to the **unchanged positive
induction**, not an assertion that a sixth-moment estimate is false.
The signed root-number formulation (6)--(13) avoids declaring that
positive diagonal a main term, but has not yet bounded its remaining
nonzero-frequency form.

## 8. General row powers and full completion remain necessary

The argument in Sections 2--6 concerns squarefree good row conductors.
It must not be promoted to every displayed sextic row by positivity.
For a local exponent \(e=2\), for example, the primitive cubic root
factor obeys \(\gamma_2(p)^3=-\alpha(p)\), whereas \(e=1\) gives
\(\gamma_1(p)^3=G(p)^3\alpha(p)^2\). Mixed exponent blocks also
retain cross-character factors: cubing a CRT cross factor for local
exponents \(e,f\) gives, up to a fixed ray phase, the quadratic
symbol \(\chi_p(q)^{3(e+f)}\). This need not disappear when
\(e+f\) is odd.

Likewise, in (8) a prime with column exponent \(j\not\equiv0\pmod6\)
has its primitive local Gauss factor of character exponent \(j\),
whereas \(j\equiv0\pmod6\) gives the Ramanujan sum of the retained
nonunit mask. The corresponding local frequency is not represented
by (12). These are explicit remaining sectors, not zero terms.

A usable inverse consumer would require a bound for the entire form
(6)--(9), all these local sectors, the prescribed profile and height
class, and whatever moving row masks the consumer needs. The
numerical requirement is (2) for an unamplified replacement, or a new
compatible amplified sixth-moment estimate with its own proved
capacity. No such bound is asserted here.

## 9. Addendum, 24 October 2026: the coefficient adapter and orientation

The subsequent `MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md`, frozen at
SHA256 `8d2b8e49149008a4541b8d6e8b993254252f124c2259241d24d65f4d6ce1bb7d`,
now supplies the structured extension for
\(a_K(n)=\mu(n)d_K(n)\) for every fixed positive integer \(K\).
Its exceptional coefficient argument and full-moment handoff were
independently reviewed. At \(K=6\) this resolves the **squarefree
coefficient-class requirement** identified in Section 5, within the
following stated cubic moment scope.

Under its explicit all-finite-character \(\mathrm{ZF}_\beta\)
hypothesis and pinned source estimates, the adapter gives some
existential \(\eta_6>0\) for the moment with coefficient
\(\mu d_6\,\theta_R G\) and cubic row character
\(\overline{\chi_3}\). It permits a common moving natural
presentation, charging its entire radical \(R\), including redundant
zeros. Its full-moment range is \(A\ge B\), \(NR\le B^{2/3}\);
the rectangular consequence requires
\(NR\le(B/C)^{2/3}\), \(C\asymp(B/A)^{1/3}\). It does not
give unrestricted moving-twist uniformity or a numerical size of
\(\eta_6\). The earlier derivation (3)--(12) is unchanged.

There is also an orientation restriction when trying to apply this
new result to (11). That expression has the factor

\[
 \overline{\gamma_2(n)}\,
       \overline{\chi_{6,n}(h)}.
\]

If \(h=t b^2\), with squarefree \(t\), it becomes, apart from the
moving twist from \(t\),

\[
 \overline{\gamma_2(n)}\,
       \overline{\chi_{3,n}(b)}.                         \tag{15}
\]

The proved cubic moment has orientation
\(\gamma_2\overline{\chi_3}\), or, after conjugating the whole
polynomial, \(\overline{\gamma_2}\chi_3\). Formula (15) has
neither orientation. Conjugating only the Gauss coefficient or only
the row character is not justified. A fourth-power parametrization
\(h=t b^4\) matches the latter orientation, but introduces a sparse
parametrization and a larger residual core; it is not an ordinary
row average of the same size.

Accordingly the coefficient extension is a new usable input, while
the full sextic frequency coupling, this opposite square-frequency
orientation, nonsquarefree column sectors, and the complete
squarefree-row sieve and profiles still require estimates. No sixth
moment satisfying (2), and no smaller zero-free boundary, follows
from this addendum.
