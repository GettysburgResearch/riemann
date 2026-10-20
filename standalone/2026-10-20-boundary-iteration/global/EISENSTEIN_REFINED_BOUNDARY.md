# Removing the resonant unitary exception over the Eisenstein field

Status: proposed source-dependent analytic theorem, for independent
review. The upstream moment, contour, and scalar-certificate inputs
are identified below. This is not a claim that those complete
preprints have been independently certified, or a proof of RH.

Let \(E=\mathbb Q(\omega)\), \(\omega^3=1\), and let \(\alpha\) be the
unitary primary-generator character in the pinned Eisenstein source.
The new conclusion is
\[
 \boxed{\quad L_E(s,\eta)\ne0
 \quad\text{for every unitary Hecke character }\eta,\qquad
 \Re s>B_\flat=0.874886647039964\ldots .\quad}             \tag{1}
\]
Principal poles are allowed; the boundary line is not included.
The numerical boundary is unchanged from the inherited nonresonant
result. The advance is the inclusion of the formerly missing types
\(\alpha\xi N^{it}\) and \(\alpha^{-1}\xi N^{it}\).
All constants may depend on the fixed character and its angular
degree. No growing-angular-degree uniformity is asserted.

The argument does not substitute \(E\) into a theorem requiring a
field containing \(\mu_{12}\). It uses native Eisenstein analytic
inputs and imports only field-independent scalar inequalities from
the later cyclotomic paper.

## 1. Sources and the exact interfaces

Ope26a means commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a,
file preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3.
Line numbers below refer to that immutable file, not this note.

| Interface | Native source and new work |
|---|---|
| Completed theta reflection | Ope26a proposition completed-reflection, with the spherical version proved in EISENSTEIN_SPHERICAL_REFLECTION.md and fixed higher pure derivatives in EISENSTEIN_UNITARY_INVERSE.md |
| Raw and selected inverse moments, sixth-power amplification | Ope26a canonical marked recursion and initialization, lines 9290–12529; the new angular orbit and weighted residue terminal are proved in EISENSTEIN_UNITARY_INVERSE.md |
| Two ordinary factors and full prime annuli | Ope26a lemma plain and its complete proof, lines 12531–14974; the fixed angular changes are specified in Section 3 below |
| Extension to \(13/18\le\kappa\le1\) | Liu, arXiv:2610.12234v2, Proposition 28.1; independently XS, arXiv:2610.15291v2, Lemma 2.1 and Appendix A |
| Physical compensated probe and its high Euler identity | Ope26a probe, scalar-Euler, and local-compensation sections; AUXILIARY_PRIME_RESIDUE_REMOVAL.md proves that the allowed auxiliary character kills every direct spherical residue |
| Refined low bound and native Eisenstein numerator average | XS, arXiv:2610.15291v2, Proposition 3.1, Proposition 5.1, Lemma 6.2 and Appendix C |
| Scalar endpoint and tangent family | Liu, arXiv:2610.26835v1, equations (14.3)–(14.10), Lemmas 14.8–14.10 and their exact certificates; only their real-variable statements are imported |

The inherited ANGULAR_PRODUCT_MOMENT.md gives the detailed fixed-angular
coefficient changes for the corresponding ordinary induction. Section 3
below explains why the same proof changes apply to the native E
induction; its theorem's stated \(\mu_{12}\) field hypothesis is not
invoked here.

## 2. One closed family and an unconditional-in-the-bootstrap base

Use the full analytic family
\[
 {\cal A}_E=\{\alpha^m\xi:m\in\mathbb Z,\ 
                  \xi\text{ finite order of arbitrary conductor}\}.
                                                               \tag{2.1}
\]
Let \(\beta\) be the supremum of real parts of its nontrivial zeros.
Every unitary Hecke character of this imaginary quadratic field is
one of (2.1), times a norm twist: after removing its integer angular
type using \(\alpha\), the remaining norm-free character has trivial
infinity type and factors through a finite ray class group.
Norm twists translate the imaginary coordinate and do not change
the family boundary.

The inverse theorem in EISENSTEIN_UNITARY_INVERSE.md gives
\[
                       \beta\le 11/12.                  \tag{2.2}
\]
This step uses no preceding angular zero-free hypothesis.
It bounds the raw and selected inverse moments by retaining the
spherical residues as a sparse weighted row contribution; it does
not discard them. The strict canonical margins absorb their energy.
Sixth-power row amplification then bounds smooth Möbius sums, and a
smooth dyadic partition continues the reciprocal holomorphically.
Ordinary unsmoothed Dirichlet-series convergence is not required.

The subsequent use of \(\kappa<1\) always assumes the bound
\[
                        \beta\le(1+\kappa)/2             \tag{2.3}
\]
for this whole family, including arbitrary moving finite conductors.
It is never replaced by a hypothesis only on finite-order characters.

## 3. The ordinary product moment over E

Fix a finite set of initial angular exponents \(J\), a finite group
\(\Theta_0\) of fixed finite characters containing all required
reciprocity phases and conjugates, and a finite basis of prime
coefficients in
\[
 {\cal C}=\{\alpha^j\theta:j\in\mathbb Z,\ \theta\in\Theta_0\}.
                                                               \tag{3.1}
\]
Every member of \({\cal C}\) is unramified outside the chosen fixed
set \(S\); moving Kummer factors retain their full original radical
width even if they cancel in the primitive inducing character.
The prime coefficients are fixed finite combinations of this basis.
Arbitrary bounded coefficients and arbitrary prime subsets are not
being introduced.

For the source centrally normalized ordinary factors and full
prime-annulus product, the same estimate is
\[
 \sum_{Nk\ll Z^m}|S_k(n_1)S_k(n_2)Q_k|^2
                         \ll Z^{M+\epsilon},\qquad M=m+q.        \tag{3.2}
\]
For \(z>0\), exclude inducing characters in \({\cal C}\), retain
the original slot mesh and natural zeros, and assume
\[
 n_1+n_2+6\kappa z\le M,\qquad13/18\le\kappa\le1.          \tag{3.3}
\]
Condition (2.3) is required if \(\kappa<1\).
For \(z=0\), only principal inducing characters are excluded, and
bounded nonnegative ordinary lengths are arbitrary.

Here is the source proof transport, including the points at which
finite order could otherwise be used improperly.

1. First and second finite Fourier transforms act on the row's
   finite Kummer characters. The fixed angular factor is evaluated
   on the whole column product and is independent of the summation
   row. It therefore remains outside the finite Gauss sums.
   Multiplicativity extracts only unitary scalars from gcd factors.
   A whole-side conjugation changes \(j\) to \(-j\); no column
   splitting raises \(j\) to the number of factors. The realized
   angular types are contained in \(J\cup(-J)\).
2. An exceptional character in \({\cal C}\) with realized angular
   type \(j\) must be \(\alpha^j\theta\) for
   \(\theta\in\Theta_0\). Thus only the finite list
   \(\{\alpha^{\pm j}\theta:j\in J,\theta\in\Theta_0\}\)
   is used in fixed-character maxima. The infinite group
   \({\cal C}\) is a closure device, not a finite summation index.
3. For each fixed member of that finite list, Mellin inversion and
   the ordinary Hecke functional equation give the same smooth
   mean, with a main term only for the trivial character.
   On any fixed \(\Re s=a>0\), deleted coprimality factors satisfy
   \(\prod_{p\mid R}(1+(Np)^{-a})\ll (NR)^\epsilon\).
   This uses unit modulus. The equal-product-scale two-rectangle
   main terms cancel exactly; nontrivial angular means have no
   main term to begin with.
4. Ordinary reflection changes its gamma quotient to
   \[
     \frac{\Gamma(s+|j|/2)}{\Gamma(1-s+|j|/2)}.           \tag{3.4}
   \]
   Its numerator poles are at \(-|j|/2-\mathbb Z_{\ge0}\).
   Hence the small-norm reflected profile is no worse than the
   original bounded/logarithmic profile, while the other end is
   rapidly decreasing. The finite fixed list supplies simultaneous
   seminorm bounds. Every moving conductor and redundant radical
   remains charged exactly as in the original reflection.
5. If a row is outside \({\cal C}\), multiplying by any allowed
   prime-coefficient basis character gives a nonprincipal member
   of \({\cal A}_E\). Hypothesis (2.3), the logarithmic-derivative
   contour, and fixed angular gamma factors give
   \(|Q_k|^2\ll Z^{\kappa z+\epsilon}\) with the original height
   budgets. At \(\kappa=1\) absolute counting suffices.
6. Exterior inertia is unchanged. Exceptional row valuations still
   occupy prescribed classes modulo six; in the equal multiplicity
   one nonunit case, \(2+v_p(h')\equiv0\pmod6\).
   The same sparse count and signed centered mean apply before
   the positive row enlargement. The diagonal has angular factor
   \(\alpha^j(U)\overline{\alpha^j(U)}=1\).

These facts are precisely the changed inputs of the source
ordinary induction. Its row widths, common supports, two rectangles,
finite Gauss identities, and positive-measure recurrence are the
native E ones. The extension below three quarters checks only the
same inequalities
\[
 6\kappa-1\ge10/3,\quad
 z<M/20\text{ in the centered range},\quad
 A_{\rm comp}+(6\kappa-1)z<14M/15+\epsilon;
                                                               \tag{3.5}
\]
see Liu Proposition 28.1 or XS Appendix A. The source rank order and
mesh-before-slot-count quantifiers are unchanged. This proves (3.2)
in its stated scope directly over E.

## 4. The guarded direct probe and its reciprocal signal

For each fixed target choose a good prime \(p_*\in1_T\), outside
all old fixed data, add it to \(S\), and take the auxiliary primitive
residue character to have local component
\(\xi_{p_*}=\chi_{p_*}^{\,2}\). The source factor
\(\Xi(a)=\xi(a)\chi_a(b_*)\) then gives the theta row digit three
at \(p_*\), since reciprocity has trivial \(T\)-phase there.

Every physical row is a \(p_*\)-unit because of the factor
\(\xi(m_{\rm row})\). Its other finite factors have no conductor at
\(p_*\). The completed theta constant permits only local digits four
(or two after conjugation), and therefore vanishes. The same zero
holds separately in every compensated divisibility/rescaling term,
since selected primes lie outside \(S\). The proof is in
AUXILIARY_PRIME_RESIDUE_REMOVAL.md.

This modification is legal in the exact physical identity.
Ope26a lines 3331–3378 choose \(T\) independently of the target,
allow enlarging \(S\) without changing \(T\), and allow every local
nonprincipal auxiliary character of order dividing six.
Lines 3941–3951 show that the \(b_*\)-factor is
\[
 \sqrt{Nb_*}\tau\,\xi(A)\overline{\xi(H/s)},\qquad H=ua^6,
                                                               \tag{4.1}
\]
and that all the auxiliary factors cancel coefficientwise.
The equality \(\overline{\xi(H/s)}=\overline{\xi(u)}\xi(s)\)
uses only \(\xi^6=1\). The remaining outside unitary phase is one
at the principal row \(u=1\). Lines 16336–16341 explicitly allow
further target-dependent excluded primes without changing the
pretarget \(T\) or slot windows.

Consequently the principal Mellin quotient is still
\[
 e^{(s-5/6)^2}\frac{H_\eta(s)}{L_E^S(s,\eta)},\qquad
 H_\eta(s)=L_E^S(6s-3,(\bar\alpha\eta)^6)\,K_\eta(s),
                                                               \tag{4.2}
\]
where \(K_\eta\) is a holomorphic unit for \(\Re s>1/2\).
In particular \(H_\eta\) is holomorphic and nonzero on
\(\Re s>2/3\), directly from the ordinary Euler region.
This protection uses no conclusion being bootstrapped.

The fixed excluded Euler factors do not change a positive-real-part
zero-free region. The scalar \(c_S\) remains positive, and the
identity-ray prime normalizer is target-free and eventually nonzero.
Its reciprocal costs \(Z^\epsilon\). Its definition does not ask an
infinite-order target to be one on the selected primes.

The residue-free nonconstant theta reflection retains the source
radial exponents and fixed seminorm bounds. Thus the additive Gram,
marked completion, and hybrid sieve calculation gives exactly the
native compensated low estimate, including XS Proposition 3.1's
external decay:
\[
 |J_\eta(Z)|\ll Z^{C(B(\ell))+\epsilon},\quad
 B(\ell)=11/12-\ell/4,\quad C(s)=s-(4+b)/6.              \tag{4.3}
\]
The assumptions on the lengths are the original
\(\ell\le1/5,\ b\ge0,\ l_y\ge11b/6,\ l_x>\ell\), with
\(l_x=(1-b-\ell)/2,\ l_y=(1+b-\ell)/2\).

## 5. First close the family at seven eighths

If \(\Delta=\beta-7/8>0\), take the source geometry
\[
 (b,\ell,l_x,l_y,h)=(1/8,1/6,17/48,23/48,13/16),\qquad
 \kappa=2\beta-1.
                                                               \tag{5.1}
\]
By (2.2), \(3/4<\kappa\le5/6\), and (2.3) holds with equality.
The raw/selected inverse moments, (3.2), and the guarded theta
estimate now supply all analytic inputs of the native E final
comparison, Ope26a lines 15505–16461.

The detector's moving denominator is a finite Kummer twist of a
fixed member of \({\cal A}_E\), so it belongs to the same full family.
Changing to its coefficient presentation inserts only allowed
fixed angular coefficients in the physical prime factors. No finite
character is substituted for the angular target. The reflected
numerator remains the original finite-order \(L_E(w,\chi_u)\).
The local Euler calculations depend polynomially on \(\eta(p)\);
their absolute bounds require only \(|\eta(p)|=1\).

Thus the original direct estimate, continuation criterion and
nonprincipal endpoint inequalities hold with this family supremum.
For example, the moderate endpoint relative to \(C(\beta)\) has
the strict upper bound
\[
       -49/440640-(1-h/4)\Delta<0.                      \tag{5.2}
\]
All other source row ranges keep their strict margins. For every
fixed target they continue (4.2) to a common half-plane left of
\(\beta\), contradicting its definition. Therefore
\[
                              \beta\le7/8.             \tag{5.3}
\]

## 6. Refined numerator over E and the scalar endpoint

For a detected nonprincipal physical row class of size \(U=Z^d\),
write \(\delta=2a-1,\ g=\delta x,\ 0\le x\le1/2\).
The native count has the source rational form
\[
 \begin{split}
 c_\kappa&=1/(3\kappa),\quad
 D_\kappa=3-(1+2c_\kappa)x,\quad
 P_\kappa=(2-2c_\kappa x)(1-x),\\
 {\cal J}_\kappa&=(5/6-\delta)D_\kappa+\delta P_\kappa,\\
 R_\kappa&=1-\delta+
     \frac{(5/6-\delta)\delta P_\kappa}{2{\cal J}_\kappa}.
 \end{split}                                                   \tag{6.1}
\]
This is XS Proposition 4.1, using precisely the moments already
extended above. In particular \(1-\delta\le R_\kappa\le1-2\delta/3\).

XS Proposition 5.1 is already over E. Its proof uses (3.2) on two
copies of each ordinary block, selected physical prime amplitudes,
Hölder, and the ordinary approximate functional equation. The
numerator character remains finite order; the angular target enters
only through the permitted coefficient presentation and detector.
With \({\cal K}=(3R_\kappa+1)/4\), it gives a reflected first moment
of size \(U^{{\cal K}-\theta/2+\epsilon}\), where
\[
 \theta=
 \begin{cases}
 g\min\{\ell/d,1/(6\kappa)\},&0<\delta<1/8,\\
 g/(6\kappa),&\delta\ge1/8.
 \end{cases}                                                   \tag{6.2}
\]
The supply condition for the second case is verified below.

The native local estimate XS Lemma 6.2 and Appendix C keeps the
reflected value inside the row sum: functional equation and all
local conductor deficits together cost \(U^\theta\). The outside
factor contributes \(Y^{-\theta}\). Their net shift cost is
therefore \(Z^{\theta(d/2-l_y)}\), not a pointwise convexity cost.
Its exponent relative to the low target is
\[
 {\cal E}(d;\delta,x)=
 a-B(\ell)-l_y(1/2+\theta)+h(z_0-1/6)-\ell/2+\ell g
       +d({\cal K}+\theta/2-z_0),\quad z_0=17/50.        \tag{6.3}
\]
Here \(h=(1+b+3\ell)/2=l_y+2\ell\). At \(d=h,\delta\ge1/8\),
\[
 \begin{split}
 E_{b,\ell,\kappa}(\delta,x)
 &=C_0+\delta/2+
 \delta x\{\ell+c_\kappa(h/4-l_y/2)\}
       -(3h/4)(1-R_\kappa),\\
 C_0&=-1/4+b/6+5\ell/4. 
 \end{split}                                                   \tag{6.4}
\]
These are scalar identities, identical to Liu (14.7)–(14.9).

For clarity the transport uses the admissibility inequalities of
Liu Remark 14.1, not the restricted two rational stages of XS:
\[
 \begin{gathered}
 b>0,\quad1/6\le\ell\le1/5,\quad7497/10000\le\kappa\le3/4,\\
 B(\ell)>437/500,\quad l_x>\ell,\quad l_y-\ell>11b/6,\\
 6\kappa\ell>3/4,\quad21/100<\ell/h<1/(6\kappa),
                       \quad h/2<l_y<1/2,\\
 E_{b,\ell,\kappa}<0
               \quad\text{on }[1/8,5/6]\times[0,1/2].
 \end{gathered}                                                   \tag{6.5}
\]
Also impose its three strict small/floor/short-row inequalities
(14.10). These are real-variable conditions.

The analytic use of the slightly lower \(\kappa\) is valid already
in XS Proposition 5.1, whose range starts at \(13/18\).
For \(\delta\ge1/8\), the supply check in its case (2) improves to
the explicit positive bound
\[
 (6\kappa-2g)\frac{\ell}{d}-R_\kappa
 \ \ge\ \frac{21}{100}(6\kappa-\delta)
                         -(1-2\delta/3)
 \ \ge\ \frac{1279}{750000}>0                          \tag{6.6}
\]
when \(d\le h+\zeta\) and \(\ell/(h+\zeta)>21/100\).
The shift always satisfies
\(0\le\theta\le\min\{a-1/2,1/10\}\).
Thus the E contour and local estimates remain within their actual
stated boxes; no new analytic continuation strip is postulated.

For each fixed row, first partition by its prime amplitudes on the
fixed \(z\)-line, move its entire numerator in \(w\), and only then
truncate heights and move the buffered denominator segment.
The amplitude class is independent of \(s,w\), and
\(\Re(s+w)>1\) on the connecting box. The correction is holomorphic
there by the native E local calculation. Finite row sums and
retained height boxes justify Fubini. No subsequent \(z\)-contour
passes through an amplitude partition.

The row exponent (6.3) increases with \(d\). In the two regimes
its derivative is respectively
\({\cal K}-z_0+g/(12\kappa)\) and
\({\cal K}-z_0+g\ell l_y/d^2\), between \(7/200\) and one
under (6.5). The scalar inequalities therefore give strict margins
for every intermediate row. The floor, small, far and principal
rows use the original native E estimates and (14.10).
The resulting remainder and (4.3) imply:
\[
 \text{if (6.5), (14.10), and (2.3) hold, then }
                              \beta\le B(\ell).         \tag{6.7}
\]
Indeed if \(\beta>B(\ell)\), both bounds continue (4.2) into a
common half-plane \(\Re s>\sigma_{\rm cont}\) with
\(\sigma_{\rm cont}<\beta\). The numerator factor in (4.2) is a
unit there. This contradicts the supremum defining \(\beta\).

## 7. Closing at the quartic without a field-domain shortcut

Let \(B_\flat\) be the unique root in \((0.8748,0.8750)\) of
\[
 133488B^4-376596B^3+384534B^2-167541B+26231=0.           \tag{7.1}
\]
The exact scalar statements of Liu Lemmas 14.9–14.10 give, for
\(\kappa_\flat=2B_\flat-1<\kappa\le3/4\), tangent parameters
\(b^*(\kappa),\ell^*(\kappa)\) with
\[
 11/12-\ell^*(\kappa)/4<(1+\kappa)/2,                   \tag{7.2}
\]
and every sufficiently close \(\ell<\ell^*(\kappa)\) makes (6.5)
and (14.10) strict. Their certificate covers the closed endpoint
\(\kappa=3/4\).

Suppose \(\beta>B_\flat\). By (5.3),
\[
       \kappa=2\beta-1\in(\kappa_\flat,3/4].
                                                               \tag{7.3}
\]
Condition (2.3) holds with equality. Choose
\(\ell<\ell^*(\kappa)\) so close that \(B(\ell)<\beta\).
Equation (6.7) gives \(\beta\le B(\ell)<\beta\), a contradiction.
This proves (1). The intermediate pointwise boundary
\(B_\infty\) is not needed: the tangent lemma includes the endpoint
licensed by seven eighths.

The numerical comparison gap, mesh and prime-slot count are chosen
before the fixed target. Each target then chooses its finite data,
the auxiliary prime, finitely many angular degrees, derivative
orders, and a sufficiently small height cutoff power. Its constants
and onset can depend on these choices; the continuation boundary
depends only on the numerical gap. Thus the supremum need not be
attained and no uniformity in growing angular weights is used.

## 8. Scope and remaining work

This removes the resonant exception over E at the inherited
\(B_\flat\). It supplies no numerical improvement of that boundary,
and no implication of the full Riemann hypothesis. In particular,
optimizing the same scalar comparison cannot by itself reach one
half; a stronger moment or different coupled estimate is needed.

The proof depends on the full upstream E recursion, contour
identities, XS numerator argument and Liu scalar certificates.
The local checker in this directory checks finite algebra only.
It does not certify those analytic inputs. An extension of the
spherical residue argument to arbitrary fields requires its own
global constant-term analysis; nothing in this note asserts it.
