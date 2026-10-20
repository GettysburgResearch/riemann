# Fixed radial parameters in the angular theta and inverse argument

Date: 20 October 2026. Status: separate proof addendum for independent
review. It does not modify the frozen pure-angular packet.

This addendum uses exactly the exceptional representation, constant-term
Jacquet description, and norm-sheet formulas in Baiying Liu,
[arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Section 5,
especially equations (5.2), (5.4), and Lemma 5.1, pp. 31--34. The higher
angular vectors and finite coefficient transformations are already
proved in ANGULAR_THETA_AND_INVERSE.md. The proposed extension below
does not assume a new inverse-moment estimate.

## 1. Balance the common norm component first

Fix a totally complex field \(F\supseteq\mu_{12}\), and use the
ideal-weight convention

\[
 L_{\Omega,S}=\prod_{v\in S}\Omega_v^{-1},\qquad
 L_{\Omega,S}(y_v)=
 (y_v/|y_v|)^{a_v}|y_v|_v^{i\gamma_v},
 \quad a_v\in\mathbb Z,\quad\gamma_v\in\mathbb R.
 \tag{1.1}
\]

Here \(\Omega\) is an actual global unitary Hecke character, not an
arbitrary prescribed tuple. The normalized complex absolute value is
\(|y_v|_v=|y_v|^2\).

Let \(r=[F:\mathbb Q]/2\). In the ideal convention, the norm character
\(N^{it}\) has value \((N\mathfrak a)^{it}\) and local weight
\(|y_v|_v^{it}\). Dividing by this character with
\(t=r^{-1}\sum_v\gamma_v\) replaces every radial parameter by
\(\gamma_v-t\). Its Hecke function is only translated in the imaginary
variable. We can therefore assume

\[
 \sum_{v\mid\infty}\gamma_v=0.
 \tag{1.2}
\]

Write \(\lambda_v\in\{1,-1\}\) for the angular vector of the
Eisenstein character \(\Lambda\) in the same convention. The joint
nonresonance condition is

\[
 \boxed{(\boldsymbol a,\boldsymbol\gamma)
       \notin\{(\boldsymbol\lambda,0),
                 (-\boldsymbol\lambda,0)\}.}
 \tag{1.3}
\]

### Proposed inverse theorem

For every fixed integer \(h\), finite-order \(\xi\), and
\(\nu=\Omega^h\xi\), the inverse moment, general-row long inverse
count, and selected inverse moment in ANGULAR_THETA_AND_INVERSE.md
remain valid. Their norm exponents and length margins are unchanged.
Their constants and finite orders can depend on the fixed radial
parameters, as they already depend on the fixed angular parameters.
Consequently

\[
 L_F(s,\Omega^h\xi)\ne0\qquad(\operatorname{Re}s>11/12).
 \tag{1.4}
\]

The finite-order or principal cases are included, with a principal pole
permitted. A common norm twist translates any such pole in the usual
way and does not change a real zero-free boundary.

## 2. The exact direct and reflected Mellin transforms

For the coefficient \(\nu\), the theta local weight has angular degree
\(m_v=ha_v-\lambda_v\) and radial parameter \(h\gamma_v\). Write
\(g_v=h\gamma_v\). Use the same actual root-derivative vector of
degree \(m_v\), including the original spherical vector when
\(m_v=0\):

\[
 W_{m_v}(a(y))=
 x^{(|m_v|+1)/2}\omega_{m_v}(y)K_{1/3}(c_v\sqrt x),
 \qquad x=|y|_v.
 \tag{2.1}
\]

Its Weyl rotation reverses the angular degree and preserves the radial
Bessel factor up to the already computed unit-modulus constant. No
radial derivative or new representation is introduced.

Put

\[
 A_v=(|m_v|+1)/2-1/6,\qquad
 B_v=(|m_v|+1)/2+1/6.
\]

The source direct sheet integral contains \(L_S(y)^{-1}W_m(a(y))\),
so after angular cancellation its Mellin transform is a nonzero
constant times

\[
 \prod_v 2^{2(t-ig_v)+|m_v|}
 c_v^{-2(t-ig_v)-|m_v|-1}
 \Gamma(A_v+t-ig_v)\Gamma(B_v+t-ig_v).
 \tag{2.2}
\]

This is the Bessel Mellin integral from the pure-angular proof with
\(t\) replaced by \(t-ig_v\). It converges in the same real half-plane.
The direct finite-place transform is still the positive measure of
the chosen common unit neighborhood, since that neighborhood lies
in every required finite local kernel.

The source reflected sheet integral instead contains
\(L_S(y)W_{w,m}(a(y))\). Thus its archimedean gamma factors are

\[
 \prod_v\Gamma(A_v+t+ig_v)\Gamma(B_v+t+ig_v).
 \tag{2.3}
\]

All finite tensor coefficients and the fixed Weyl phases are retained
in the source finite profile factor. Dividing (2.3) by the direct
transform (2.2) at \(-t\), the exact multiplier has the form

\[
 \mathfrak m_{\upsilon,\alpha}(t)
 =E_{\upsilon,\alpha}(t)C^t
 \prod_v
 \frac{\Gamma(A_v+t+ig_v)\Gamma(B_v+t+ig_v)}
      {\Gamma(A_v-t-ig_v)\Gamma(B_v-t-ig_v)}.
 \tag{2.4}
\]

The Bessel powers in the ratio contribute the positive constant
\(C^t\); any remaining fixed phase is absorbed in \(E\).
Their exact local ratio is
\((2/c_v)^{4t+4ig_v}\). The factor
\((2/c_v)^{4ig_v}\) is fixed and has modulus one, so it is
included in \(E\); the \(t\)-dependent factor is the stated
positive-base exponential.

At \(t=\sigma+iT\), a numerator and denominator in (2.4) have
imaginary parts \(T+g_v\) and \(-T-g_v\). Their exponential Stirling
factors cancel exactly. Their real parts differ by \(2\sigma\).
Thus the two gamma ratios at a place contribute
\((1+|T+g_v|)^{4\sigma}\). Since \(g_v\) is fixed, this is bounded
by a fixed multiple of \((1+|T|)^{4\sigma}\), also when
\(\sigma<0\). The total height exponent remains \(4r\sigma\).

The numerator poles have real part \(-A_v-n\) or \(-B_v-n\).
They are at or to the left of \(-1/3\); reciprocal gamma factors
add no poles. The source finite-place strip is therefore still
available for every \(\operatorname{Re}t>-\delta\),
\(\delta<1/3\). The direct Mellin transform has no zero.
All profile derivatives satisfy the same bound

\[
 |(x\partial_x)^j\Phi_W(x)|
 \ll p_J(W)\min\{x^{a_0},x^{-A}\},
 \quad 0<a_0<1/3,
 \tag{2.5}
\]

with the original finite seminorm and polynomial incoming norm-height
costs. Only constants and fixed orders change.

## 3. Constant terms with a surviving angular degree

If at least one \(m_v\ne0\), the original compact-circle argument
applies without change. Radial factors are constant under this circle
action. The weighted constant-term integral transforms by a nontrivial
angular character, so it is zero.

All unit compatibility remains global. Construct \(L_S\) from the
inverse S-restriction of the actual global theta character; its product
is trivial on S-units. A common finite open unit kernel exists for the
finite realized coefficient list. Multiplying the finite and infinite
profiles by radial phases of modulus one does not change their absolute
sheet majorants or any exterior digit table.

## 4. Constant terms when every angular degree is zero

The remaining case is \(h\boldsymbol a=\boldsymbol\lambda\).
Because all \(a_v\) are integers and every \(\lambda_v\) is plus
or minus one, this forces \(h=1\) or \(h=-1\). Condition (1.3)
then gives \(\boldsymbol g=h\boldsymbol\gamma\ne0\), with
\(\sum_v g_v=0\).

Let \(A_\infty^1\) be the positive archimedean norm-one torus.
Its logarithmic coordinates are vectors
\(t=(t_v)\in\mathbb R^r\) with \(\sum_vt_v=0\).
They act by multiplication on the compact quotient
\(F_S^1/U_S^6\), preserving its Haar measure. The finite class
cutoff is unchanged under this action: the complex sixth-power
quotient is trivial.

The relevant representation input is the actual one in source
Proposition 4.1, pp. 25 and 28: at a complex place the cover is
split and the local representation is the ordinary spherical
principal series with normalized inducing exponents
\(\pm1/6\). The two rank-one Bruhat cells give its possible
unnormalized torus characters
\(|y|_v^{1/2-1/6}\) and \(|y|_v^{1/2+1/6}\). Source
Lemma 5.1, p. 32, states these as the constant-term Jacquet
powers 1/3 and 2/3, with a missing constituent assigned
coefficient zero. These are exponents of the fixed inducing
representation, not a claim inferred from a Bessel asymptotic.
The global theta function is the automorphic residue identified
in Proposition 4.1, p. 26; its constant-term map is equivariant
for these local torus actions and therefore has this finite
spectral support. Changing a vector within the representation
does not introduce a new inducing exponent. In the present
all-zero-angular case, every complex vector is in fact the
original spherical vector, fixed by the Weyl element.

Tensoring the finite sets of local exponents, and retaining
the finite digit averages, shows that the constant-term function lies
in a finite sum of generalized eigenspaces for \(A_\infty^1\), with real
exponents \(A_j(t)\). It is not necessary for every \(A_j\) to
be a multiple of the total norm.

These components descend individually to the required quotient.
To see this without making a choice of fundamental domain, group
the finitely many equal restricted real characters. Choose one
torus element separating the remaining characters. The spectral
projection onto each generalized character space is a polynomial
in its translation operator on the finite translation span:
the Chinese remainder theorem constructs these projections from
the relatively prime powers of its distinct linear factors.
Translations commute with the sixth-power unit action,
so these projections preserve the source's unit invariance.
Multiplication by \(L_S^{-1}\) preserves descent, by its global
unit compatibility.

The corresponding weighted constant-term component has generalized
translation eigenvalue

\[
 \exp\{A_j(t)-i\boldsymbol g\cdot t\}.
 \tag{4.1}
\]

Because \(\boldsymbol g\) is nonzero and perpendicular to the
all-ones vector, some norm-one vector \(t\) has
\(\boldsymbol g\cdot t\ne0\). Scale it sufficiently small that
this value is not an integer multiple of \(2\pi\). The real
quantity \(A_j(t)\) cannot cancel this nontrivial phase, so the
eigenvalue in (4.1) is different from one. If \(T_t\) denotes
this translation and \(f_j\) is the weighted component, a
fixed positive integer \(N_j\) satisfies

\[
 (T_t-\lambda_j(t))^{N_j}f_j=0,
 \qquad \lambda_j(t)=e^{A_j(t)-i\boldsymbol g\cdot t}.
\]

Integrating and using Haar invariance gives
\((1-\lambda_j(t))^{N_j}\int f_j=0\), so the integral is
zero. Summing the finitely many components annihilates the
whole constant term. In the semisimple case this is the
ordinary one-step eigencharacter orthogonality identity.

Equivalently, the full weighted constant term can be treated
without resolving its individual components. On its finite
translation span, the polynomial

\[
 P(X)=\prod_j(X-\lambda_j(t))^{N_j}
\]

annihilates the translation operator applied to that term.
Every factor \(1-\lambda_j(t)\) is nonzero, so \(P(1)\ne0\).
Haar invariance gives
\(0=\int P(T_t)f=P(1)\int f\), proving the same vanishing.
The translation and its polynomial preserve exact unit
invariance and the finite digit/class cutoffs, since all
these torus actions commute. This formulation includes all
possible logarithmic generalized-eigenvector terms directly.

There is no such nonzero balanced radial vector when \(r=1\).
Then this extra case is empty, as it should be.

## 5. Closing the inverse recursion

The preceding sections prove the same actual unsmoothed theta
reflection as the pure-angular note, with the modified profiles.
The direct and reflected Fourier-series exchanges remain absolute:
all newly inserted radial factors have modulus one. The local
archimedean vectors themselves have exactly the same absolute
Bessel majorants already checked in the pure-angular note.

For each fixed \(h,\xi\), the coefficient set is still

\[
 \{\Omega^h\theta,\Omega^{-h}\theta:\theta\in\Theta_0\}.
\]

Its radial parameters are drawn from the fixed finite set
\(\{h\boldsymbol\gamma,-h\boldsymbol\gamma\}\).
The cube coefficient \(\nu(b)^3\), the terminal factors
\(L(R)^2L(n)^{-1}L(b)^{-3}\), and the selected factors
\(L(P)^2\) retain their exact multiplicative separation.
The two residual characters are still
\(\nu G_0\xi_1\) and then \(\nu\xi_1\xi_2\).
No radial parameter is moved into a periodic Kummer row character.

Thus every inverse terminal bound, finite-depth margin,
initialization, selected-prime restoration, and sixth-power
amplification in Sections 5--7 of the pure-angular note applies
with (2.5). This proves the proposed inverse theorem and (1.4),
under the same identified upstream analytic inputs.

## 6. The precise product-moment interface for a separate review

The fixed radial extension of the ordinary Hecke functional equation
is classical; see Molin--Page,
[Computing groups of Hecke characters](https://webusers.imj-prg.fr/~pascal.molin/pdf/hecke.pdf),
Section 2.4. In the local-weight convention (1.1), an ordinary
character with degree \(ha_v\) and radial parameter \(h\gamma_v\)
has gamma factor

\[
 \prod_v\Gamma(s+|ha_v|/2-ih\gamma_v).
\]

Its ordinary reflection kernel consequently replaces equation (4.1)
of ANGULAR_PRODUCT_MOMENT.md by

\[
 \widehat W(1-s)
 \prod_v\frac{\Gamma(s+|ha_v|/2+ih\gamma_v)}
                 {\Gamma(1-s+|ha_v|/2-ih\gamma_v)}.
 \tag{6.1}
\]

The same paired imaginary parts give the old height exponent.
Its poles are \(s=-|ha_v|/2-ih\gamma_v-n\). In Mellin inversion,
the small-argument residues are
\(x^{|ha_v|/2+n+ih\gamma_v}\) times polynomials in \(\log x\).
Their absolute size is no worse than the original logarithmic
kernel bound; the fixed oscillations do not add a power of x.

Balancing (1.2) is essential for the simple fixed-character mean
statement. If \((\boldsymbol a,\boldsymbol\gamma)\ne0\), its
integer multiples are distinct infinity types, so the exception
orbit remains finite. Moreover no nonzero power, even after a
finite-order twist, can be a pure norm character: equality would
force \(h\boldsymbol a=0\) and every \(h\gamma_v\) equal, and
their sum zero forces all of them zero. Hence every nontrivial
member in the finite exceptional set has an entire Hecke function;
the only pole in the balanced family is the principal pole at one.

These facts supply the changed analytic interfaces for a radial
product-moment adapter. The inverse result above is proved
independently of that adapter; no refined angular boundary is
assumed in deriving it.
