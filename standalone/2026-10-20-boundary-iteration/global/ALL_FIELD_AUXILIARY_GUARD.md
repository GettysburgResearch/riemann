# A finite-place cubic guard for the all-field direct probe

Status: proposed source-dependent lemma for independent review. This is
new mathematics, not a quoted theorem. It removes the spherical constant
term in the *actual direct probe*, including every selected-prime term,
while preserving the target reciprocal coefficientwise.

Scope: a fixed totally complex field \(F\supset\mu_{12}\), a fixed
unitary Hecke target \(\eta\), fixed balanced infinity type and fixed
finite data. Constants may depend on them and on one auxiliary prime.
There is no conductor-uniform assertion about that auxiliary prime.

## 1. Exact sources and conventions

The starting arithmetic, theta realization, finite Poisson transform,
and frequency decomposition are those of Ope26b, commit
adc7f1241b42e322a6451854ab7e4b4c146bf78a, in
preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/.
The exact files and SHA256 values are:

| File | SHA256 |
|---|---|
| 02-arithmetic.tex | 892ce2d22b787810e4e7dc3dda9ac54877a3b749e5cc87c1e21868c1a72f492b |
| 03-theta.tex | fb55e83219ef28a92f0be4f5fce77207be96c6573c3660e5182eb0f435016587 |
| 04-reflection.tex | d76f23137518b7b6ffb491f86598570ec1a89adf43320775eafed5661ce30407 |
| 05-poisson.tex | bd5e53c2d9436aa1c621dca2d1c423035b610b423f064f7d5b6e19f3d9f31992 |
| 06-zero-free.tex | c565166640d5e8210a2af70f00f6b9072112033a182ec7dede17e1517e76be33 |

The later estimates used are Liu, arXiv:2610.26835v1,
Sections 13.2--13.6 and 14, with the fixed balanced-type adapters
identified in ALL_UNITARY_BOUNDARY.md. In particular this note changes
the physical test, rather than treating a twist of its theta factor
alone as permission to change its Euler product.

Write \(a(y)=\operatorname{diag}(y,1)\), \(\Gamma=U_S^6\),
\({\cal V}_S=F_S^\times/F_S^{\times6}=E_S\oplus B_S\), with \(E_S\)
the S-unit image and \(B_S\) an isotropic complement. The Hilbert
convention in 02-arithmetic gives
\[
 H_{\mathfrak p}(\pi,u)=\chi_{\mathfrak p}(u)^{-1}.
 \tag{1.1}
\]
The row-unit correction in 04-reflection, equations
reflection-moving-twist through reflection-S-character, is
\[
 \lambda_{\varepsilon_m}(y)=H_S(\varepsilon_m,y)^{-1},\qquad
 L_{\upsilon_m}=L_S\lambda_{\varepsilon_m}.
 \tag{1.2}
\]
This correction is sextic. Ignoring it would invalidate a naive
quadratic auxiliary twist.

## 2. An adapted auxiliary prime and class complement

Start with the fixed excluded set \(S_0\). Choose a prime ideal
\(\mathfrak p_*=(\pi)\) outside \(S_0\) in the identity ray class
for a sufficiently deep modulus supported on \(S_0\). Thus
\(\pi\in F_v^{\times6}\) for every finite \(v\in S_0\).
The existence of such a prime is the usual prime theorem in a
fixed ray class (qualitative Chebotarev suffices). The modulus
can additionally avoid the finite conductor of the target and all
bad theta/additive places.

For every old S-unit \(\varepsilon\), reciprocity gives
\[
 \chi_{\mathfrak p_*}(\varepsilon)
 =\prod_{v\in S_0}(\varepsilon,\pi)_{6,v}^{-1}=1.
 \tag{2.1}
\]
At the good prime \(\mathfrak p_*\), principal units are sixth
divisible. Hence every old S-unit is a local sixth power at
\(\mathfrak p_*\). Put \(S=S_0\cup\{\mathfrak p_*\}\). Since
\(\mathfrak p_*\) is principal,
\[
 U_S=U_{S_0}\times\langle\pi\rangle.
 \tag{2.2}
\]
In the local power-class decomposition, the old unit image has
trivial new component, while \(\pi\) has trivial old component and
spans the new valuation line. Consequently we may take
\[
 B_S=B_{S_0}\oplus B_*,
 \tag{2.3}
\]
where \(B_*\) is the entire unit line in
\(F_{\mathfrak p_*}^\times/F_{\mathfrak p_*}^{\times6}\).
Both new lines are isotropic, so this is an actual complementary
isotropic subgroup, not a projection that modifies the old cutoff.

Every allowed exterior generator has
\(v_*(A)\equiv0\pmod6\). Multiplying by a power of \(\pi^6\)
lets us choose it with \(v_*(A)=0\). Product generators retain
this property. The remaining balancing is by \(U_{S_0}^6\);
the slice with new valuation zero is compact modulo that lattice.
In particular all exterior ideal sums and their source counting
estimates retain the same exponents.

Let \(\chi_*=\chi_{\mathfrak p_*}\) on units and extend
\[
 \lambda_*(\pi^e u)=\chi_*(u)^2,\qquad
 \lambda(y)=\lambda_*(y_*).
 \tag{2.4}
\]
This has order three. Equations (2.1)--(2.2) imply that \(\lambda\)
is trivial on \(U_S\). It is trivial on the norm section
\(\ell_T\), whose finite coordinates are one. On allowed exterior
ideals define
\[
 \psi(\mathfrak A)=\lambda(A)=\chi_*(A)^2
                  =\chi_{\mathfrak A}(\pi)^2.
 \tag{2.5}
\]
This is the cubic Kummer Hecke character unramified outside \(S\).
The equality fixes its orientation.

## 3. The modified physical probe

Let \(\vartheta=\overline\Lambda\,\overline G\,\eta\) be the
original coefficient in the source completed theta sum. Define
\[
 B_m^\psi(Z)=
 \sum_{\mathfrak c\ {\rm squarefree},\,\mathfrak n}
 \frac{\gamma_2(\mathfrak c)\vartheta(\mathfrak A)
       \psi(\mathfrak A)^{-1}}
      {q_{\mathfrak c}^{1/2}q_{\mathfrak n}}
 \chi_{\mathfrak A}(m)P_G(q_{\mathfrak A}/Z),
 \qquad \mathfrak A=\mathfrak c\mathfrak n^3.
 \tag{3.1}
\]
All primes in these ideals are exterior to the enlarged fixed \(S\).
Use the local test
\[
                 W_{0,*}(x)=\lambda_*(x)\mathbf1_{\mathcal O_*^\times}(x).
 \tag{3.2}
\]
At the other places use fixed smooth/Schwartz annular tests as in
05-poisson. Their Mellin pairings at \(1/6\) are nonzero.
The new local test already has additive integral zero, so
\(\widehat W_0(0)=0\); one may retain the source's signed archimedean
test as well.

For \(t_0\in F_S^1/\Gamma\), put
\[
 e_{-1}(t_0)=\mathbf1_{\{v_*(t_0)\equiv-1\pmod6\}}.
 \tag{3.3}
\]
This is a well-defined locally constant function on the actual
compact quotient. Define
\[
 \begin{split}
 I^\psi(X,Y,Z)=\int_{F_S^1/\Gamma}
 &e_{-1}(t_0)\lambda(t_0)\frac1Y
 \sum_{\mathfrak s}\psi(\mathfrak s)^{-1}W_1(q_{\mathfrak s}/Y)\\
 &\times\frac1{\sqrt{q_{\mathfrak s}X}}\sum_{m\in R}
 q_{\mathfrak s}^{-1/2}g_{\mathfrak s}(-m)
 W_0\!\left(\frac m{t_0\ell_{q_{\mathfrak s}X}}\right)
 B_m^\psi(Z)\,dt_0 .
 \end{split}
 \tag{3.4}
\]
All factors descend under \(\Gamma\), and the original row sum is
finite on compact representatives as before.

The two local supports in (3.2)--(3.3) force
\[
                         v_*(m)\equiv-1\pmod6
 \tag{3.5}
\]
for every physical row of the probe. This congruence is essential.
It is preserved under all auxiliary rescalings and selected-prime
operations, whose primes are exterior to \(S\).

## 4. Both constant terms vanish on the actual weighted sheets

Fix one row satisfying (3.5). Its allowed ideal generator \(m_0\)
has \(v_*(m_0)=0\); write \(m=\varepsilon_m m_0\).
Equations (2.1)--(2.2) and (3.5) show, on local units, that
\[
 \lambda_{\varepsilon_m,*}(u)
       =\chi_*(u)^{-1}.
 \tag{4.1}
\]
The original fixed theta coefficient is unramified on units at the new
prime, including the Gauss-phase character reconstructed after the
enlargement of \(S\). Here is the local check. In 02-arithmetic,
lines 523--573, its quadratic contribution is the character
\([a]\mapsto\mathfrak w_S(a^{-1})^{-1}\) on \(B_S\), combined with
the fixed Kummer factor contributed by \(4\). At a good odd place of
additive conductor zero, the normalized quadratic Weil index
\(\mathfrak w_*(u)\) is one for every unit \(u\) (line 539).
The new part of \(B_S\) is the unit line, so this Weil character is
trivial there. The Kummer factor for \(4\), the old \(\Lambda\), and
the target are unramified at \(\mathfrak p_*\) by its choice.
Thus the reconstructed \(\overline\Lambda\,\overline G\,\eta\)
has trivial new unit character. This does not assume that every
old chosen generator remains unchanged after the enlargement.
After the twist in (3.1), the actual S-character is therefore
\[
 L_{\upsilon_m,*}(u)=\chi_*(u)^{-2}\chi_*(u)^{-1}
                   =\chi_*(u)^3.
 \tag{4.2}
\]
This is nontrivial quadratic on units for every such row, including
every row-unit class and every direct selected-prime term.

Choose a unit \(b\in\mathcal O_*^\times\) which is a cube and
has \(\chi_*(b)^3=-1\), and put it in the new coordinate of
\(F_S^\times\), with all other coordinates one. Then
\(|b|_S=1\) and \([b]\in B_*\subset B_S\). Translation by \(b\)
preserves the sheet, its quotient measure, and the exact class
cutoff \(\mathbf1_{B_S}([y])\).

The ordinary Jacquet module of the unramified cubic theta
representation has trivial action by \(a(b)\) for a cube unit \(b\).
For the exact normalization this follows from Liu Section 4's
inducing law on diagonal cubes and Lemma 5.1: the two possible
absolute-value characters have exponents \(1/3\) and \(2/3\);
both are one on units, and the cover cocycle is one on cubes.
An extension between them cannot introduce a nontrivial unipotent
action of this compact unit group: a fixed smooth vector factors
through a finite quotient, whose complex representations are
semisimple. This statement concerns the Jacquet action and holds
for the source finite cutoff vector as well as the spherical vector.

It follows that the direct constant term is unchanged by
\(y\mapsto by\). For the reflected constant term use
\(w a(b)=bI\cdot a(b^{-1})w\), with no cube cocycle.
The scalar \(bI\) has trivial action by the same inducing law on
central cube units, so this constant term too is unchanged.
On the other hand the weight \(L_{\upsilon_m}(y)^{-1}\) changes
sign by (4.2). The actual weighted constant terms thus equal their
negatives and are zero:
\[
                     C_m^+(l)=C_m^-(l)=0 .
 \tag{4.3}
\]
No unweighted-theta integral was substituted here. The finite
selector, the row-unit correction, and the source local cutoff are
all retained. In particular there is no need to replace the local
Whittaker function \(\mathbf1_U\) by a different projector.

The same argument applies if the source reflection has nonzero
balanced angular/radial type. For spherical types it supplies the
missing cancellation. All nonconstant reflection formulas and
their fixed-profile bounds are unchanged except for the finite
character data.

## 5. Exact Poisson cancellation and the principal frequency

The exterior finite transform is unchanged: it is precisely
05-poisson, equations finite-Poisson-factor and
finite-Poisson-transform. Its Fourier argument remains
\[
       t_0\ell_{q_{\mathfrak s}X}\frac h{sA},
       \qquad
       \left|\ell_{q_{\mathfrak s}X}\frac h{sA}\right|_S
                   =T=\frac{Xq_h}{q_{\mathfrak A}} .
 \tag{5.1}
\]
After unfolding the nonzero \(h\)-orbits under \(\Gamma\), put
\[
 c=\ell_{q_{\mathfrak s}X}\frac h{sA}\ell_T^{-1},\qquad
 t=t_0c .
 \tag{5.2}
\]
This substitution preserves the norm-one measure. Since
\(\lambda(\ell_T)=1\), it gives the exact factors
\[
 \lambda(t_0)=\lambda(t)
       \frac{\psi(\mathfrak s)\psi(\mathfrak A)}{\lambda(h)},
 \qquad
 e_{-1}(t_0)=
 \mathbf1_{\{v_*(t)\equiv v_*(h)-1\pmod6\}}.
 \tag{5.3}
\]
Thus the two auxiliary ideal twists in (3.1) and (3.4) cancel
*coefficientwise*, before forming any Euler product.

For \(j\in\mathbb Z/6\mathbb Z\), define
\[
 V_j^\lambda(T)=
 \int_{F_S^1}\mathbf1_{\{v_*(t)\equiv j-1\pmod6\}}
          \lambda(t)\widehat W_0(t\ell_T)\,dt .
 \tag{5.4}
\]
The local Fourier transform of (3.2), for the self-dual additive
measure of conductor \(\mathcal O_*\), is
\[
 \widehat W_{0,*}(\pi^{-1}u)
       =q_*^{-1}\tau(\lambda_*)\lambda_*(u)^{-1},
 \qquad
 |\tau(\lambda_*)|=q_*^{1/2},
 \tag{5.5}
\]
and is zero at all other valuations. The sign in the Gauss sum
is the fixed Fourier sign and has no effect on nonvanishing.
This is the complete local Fourier calculation, not a generic
appeal to nonvanishing of a test.

Consequently \(V_j^\lambda=0\) unless \(j=0\).
For \(j=0\), its Mellin transform is
\[
 M_\lambda(z)=
 \int_{F_S^\times}\lambda(y)\widehat W_0(y)|y|_S^z\,d^\times y,
 \tag{5.6}
\]
whose new local factor is a fixed nonzero scalar times \(q_*^z\).
Thus \(M_\lambda(1/6)\ne0\); its holomorphy and vertical decay
on the needed strips follow from the unchanged archimedean
factors. Absolute unfolding and Mellin inversion use exactly
the source majorants, since the new weights have modulus at most one.

Write \(h=ur^6\) with the source frequency representatives and an
allowed exterior \(r\). Then
\[
 \lambda(h)=\lambda(u),\qquad v_*(h)\equiv v_*(u)\pmod6.
 \tag{5.7}
\]
The exact high-side identity is therefore the source one with
\[
 \sum_{u\in{\cal U}}q_u^{-z}{\cal F}_{u,\eta}
 \quad\hbox{replaced by}\quad
 \sum_{\substack{u\in{\cal U}\\v_*(u)\equiv0\ (6)}}
       \lambda(u)^{-1}q_u^{-z}{\cal F}_{u,\eta},
 \qquad M(z)\ \hbox{replaced by}\ M_\lambda(z).
 \tag{5.8}
\]
Crucially \({\cal F}_{u,\eta}\) has the original target \(\eta\),
not \(\eta\psi^{-1}\). Every exterior local Euler coefficient
is identical to the source coefficient after (5.3).
The principal frequency \(u=1\) belongs to the restricted set,
has phase one, and retains its nonzero Mellin multiplier.
All other changes in (5.8) are fixed finite-class restrictions and
unitary row phases.

## 6. Low bounds, selected primes, and high bounds

The theta factor is evaluated only on rows satisfying (3.5), where
(4.3) removes both constants. The source nonconstant reflected
theta estimate therefore applies with the same exponents.
Its proof partitions the finite S-unit classes first, so retaining
this congruence is a restriction of the original positive row sums.
Finite local characters and profiles remain in a fixed finite list.

For the additive factor, the norm-one unfolding introduces a
unitary row phase and a fixed S-supported twist
\(\psi(\mathfrak s)^{-1}\) in its auxiliary ideal column.
More explicitly, up to the unchanged common source normalization,
the coefficient is
\[
 \begin{split}
 \widetilde A^\psi_{[k]}
 ={}&\mathbf1_{\{v_*(k)\equiv-1\ (6)\}}\lambda(k)Y^{-1/2}
 \sum_{\mathfrak s}\psi(\mathfrak s)^{-1}q_{\mathfrak s}^{-1}
 g_{\mathfrak s}(-k)W_1(q_{\mathfrak s}/Y)\\
 &\hspace{35mm}\times
 \Omega_\lambda(q_k/(q_{\mathfrak s}X)),\\
 \Omega_\lambda(T)
 ={}&\int_{F_S^1}W_0(t\ell_T)\lambda(t)^{-1}\,dt .
 \end{split}
 \tag{6.1}
\]
Indeed set \(y=k/(t_0\ell_{q_{\mathfrak s}X})\) in the unfolded
norm-one integral. On the support of its new local factor \(v_*(y)=0\);
the congruence becomes the one in (6.1), and
\(\lambda(t_0)=\lambda(k)\lambda(y)^{-1}\).
The local factor of \(W_0\lambda^{-1}\) is simply
\(\mathbf1_{\mathcal O_*^\times}\). Thus its profile is of the
original fixed compact type. The positive row norm is bounded by
dropping the displayed congruence after removing the unitary phase.
The proof of Liu (13.7), Section 13.2,
applies with precisely this twist: after common-support splitting,
the column character is
\(\lambda_{\varepsilon,j}\psi^{-1}\), with the same exterior
conductor/radical bound. The nonprincipal smooth means use the
whole unitary bootstrap family. For the principal exceptions the
source explicitly observes that any fixed S-supported twist
preserves the necessary exterior valuation condition modulo six.
Hence its exceptional count and both exponents in (13.7) are unchanged.
The diagonal term sees only coefficients of modulus one.
This is why the sharper direct estimate (13.8), not just the
coarse additive large sieve, remains available.

Form the same physically compensated selected-prime expression
as Liu Section 13.2, with all selected primes outside the enlarged
fixed \(S\). Every rescaling has local \(v_*=0\); the source's
marked cube/squarefree decompositions preserve (3.5) and (4.2).
Thus (4.3) holds term by term before the marked terms are combined.
The compensation coefficients retain the original \(\eta(p)\).
On the low side their expansion merely enlarges the fixed finite
coefficient group by \(\psi\), which is already included in the
ordinary product-moment family; they are not changed to coefficients
for a different target.
On the high side, (5.3) holds for every coefficient of each
rescaled probe. All selected-prime Euler factors consequently
involve the original target \(\eta\), exactly as in the source.
The surviving frequency restriction and phase in (5.8) are
independent of every selected-prime label.

In the high estimates, absolute and mean-square bounds over the
restricted frequency family are bounded by the original positive
sums. The unitary phase is removed only after those identities have
been formed. Local correction products and local contour assignments
are unchanged, since every exterior coefficient is unchanged.
The principal row remains present and its correction product is the
original nonzero one. The finite number of frequency rows generating
the same character remain distinct as in the source; the new
restriction can only remove some nonprincipal rows.

The low estimate (13.8), the high estimate (13.20), and the
residue-averaged refinement (14.20) therefore have their original
exponents and strict margins for the guarded probe. There is no
claim that an arbitrary twist or arbitrary subfamily may be inserted
in these estimates: (3.4)--(5.8) establish the exact allowed change.

## 7. Consequence and the rejected shortcut

Combined with the full-family \(11/12\) inverse base in
ALL_UNITARY_BOUNDARY.md and the fixed balanced-type ordinary product
adapters, the direct comparison can now be applied to every unitary
target over \(F\supset\mu_{12}\). The same source scalar certificates
first give \(7/8\), then the residue-averaged endpoint
\[
                   B_\flat=0.874886647039964\ldots .
 \tag{7.1}
\]
The complete family closure and descent are stated separately in
ALL_UNITARY_REFINED_BOUNDARY.md. This changes the covered family,
not the numerical value of the inherited endpoint.

For clarity, the initially tempting quadratic guard with physical
rows \(v_*(m)\equiv0\pmod6\) does not work. A tame nontrivial
character on unit-supported \(W_{0,*}\) has Fourier Mellin support
at valuation \(-1\), so that choice kills the principal frequency.
The cubic choice, the physical row congruence \(-1\), and the
resulting local theta digit \(3\) are a single compatible package.
