# The spherical residue in the all-field inverse terminal

Status: proposed source-dependent analytic lemma, submitted for
independent review. This replaces the two unresolved interfaces of
ALL_FIELD_CONSTANT_TERM_DRAFT.md: rational torus transport is tracked
with the actual finite class weights, and an existing bounded-row
terminal removes the need to propagate an artificial fixed puncture.
It does not by itself assert a zero-free theorem.

Work in the field and theta setup of Liu,
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Sections 3–5, initially \(F\supset\mu_{12}\), and in its allowed-generator
and ordinary-section conventions. Extension beyond that source field
scope requires the separately stated field adapter. The inputs are
its Proposition 4.1, the exact cocycle and digit identities in Lemma
5.1, and the archimedean Jacquet powers explicitly stated in that proof.
The earlier packet records the immutable PDF SHA256
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5.

## 1. Statement in the form used by the recursion

Replace the first angular derivative at every complex place by the
spherical vector, whose Whittaker function is
\[
           |y_v|_v^{1/2}K_{1/3}(c_v|y_v|_v^{1/2}).
                                                               \tag{1.1}
\]
Keep the fixed finite test, the actual class weight, the fixed finite
character, and every zero-extended exterior mask. Let \(j_p\pmod6\)
be the displayed digit at an exterior prime, including an explicit
digit zero when the prime is a puncture. A prime is not deleted from
this presentation merely because its digit is zero.

For any presentation containing at least one such exterior prime,
the radial functional equation is the original nonconstant reflected
identity, with spherical gamma multiplier, plus a finite sum
\[
       X^{1/3}\sum_{j=0}^{J} c_{m,j}(\log X)^j.           \tag{1.2}
\]
The fixed integer \(J\), profile family and seminorm orders are
independent of the moving row. The coefficients vanish unless every
displayed digit belongs to \(\{0,4\}\). If \(r\) is the product of
the digit-four primes, then
\[
 |c_{m,j}|\ll_{\epsilon,F,S,\mathrm{fixed}}
             (Nr)^{-1/6}(Nm)^\epsilon.                 \tag{1.3}
\]
Whole conjugation permits \(\{0,2\}\) instead.
At a fresh full-index selected prime \(p\), each coefficient polynomial
is multiplied exactly by \(1/Np\); a full-index coprimality mask
multiplies it by \(1-1/Np\).

For a completely unmasked unit presentation an additional term
\(X^{-1/3}\) times a fixed logarithmic polynomial may occur.
It is not assigned the \(1/Np\) selected law. Section 6 explains why
the inverse argument never needs a marked estimate of that term.

## 2. Weighted constant terms before Mellin transformation

Write \(\Gamma=U_S^6\) as in the source. For the actual digit-averaged
automorphic functions \(\mathscr D_m^\pm\) of Lemma 5.1, let
\(C_m^\pm(l)\) be their constant terms integrated on
\(\Omega_l=X_l/\Gamma\) against
\[
                  1_{B_S}([y])L_\upsilon(y)^{-1}.
                                                               \tag{2.1}
\]
The balanced resonant case has zero angular degree in this weight.
Fixed global norm twists have been moved to the radial test.
All finite-order phases in \(L_\upsilon\) are retained.

The source proves \(\Gamma\)-invariance of both digit averages,
their constant terms, and (2.1). Rational diagonal conjugation
preserves the constant-term integral because its adelic modulus is
one. The exact automorphic equality, with constants restored, is
\[
       T_m(l)+C_m^+(l)=T_m^\vee(l)+C_m^-(l),             \tag{2.2}
\]
where the two \(T\)'s contain only nonconstant Fourier terms.

The absolute convergence proof in Lemma 5.1 is still valid.
Its exterior Euler majorant is
\[
       \zeta_F^S(\sigma+1/2)\zeta_F^S(3\sigma+1).
                                                               \tag{2.3}
\]
The spherical archimedean Mellin factors converge on a larger
positive half-plane than is needed here, since their small argument
order is \(x^{1/3}\). The finite local factors are unchanged.
Thus, for each fixed row and every \(\sigma>1/2\),
\[
       T_m(l)=O_{m,\sigma}(l^{-\sigma}),\qquad
       T_m^\vee(l)=O_{m,\sigma}(l^\sigma).               \tag{2.4}
\]
These constants are not used as uniform row bounds.

The local constant-term Jacquet characters at a complex place have
real powers \(1/3\) and \(2/3\), as stated in the source proof.
The tensor constant term consequently has a finite translation span.
Allow generalized eigenspaces, hence fixed powers of logarithms;
no semisimplicity assumption is needed.

The integrated constant term retains only equal real exponents at
all complex places. One can check this directly using the ordinary
unit subgroup: its sixth powers lie in \(\Gamma\), their logarithms
span the archimedean norm-one hyperplane. If needed pass to the
finite-index subgroup whose finite components fix the finitely many
smooth finite vectors and finite characters; the logarithms still
span that hyperplane. A distinct real character cannot be invariant
under that lattice. Projection onto a
generalized character is a polynomial in a separating translation
operator, so it preserves \(\Gamma\)-invariance. Equivalently, Haar
integration on the compact norm sheet kills the nontrivial restricted
real characters. The finite class weight is unchanged by positive
archimedean norm-one translation; it therefore does not invalidate
this projection argument.

After choosing a fixed norm section, the possible integrated forms are
\[
 C_m^+(l)=l^{1/3}P_{m,+,1}(\log l)
                    +l^{2/3}P_{m,+,2}(\log l),
\]
\[
 C_m^-(l)=l^{-1/3}P_{m,-,1}(\log l)
                    +l^{-2/3}P_{m,-,2}(\log l).         \tag{2.5}
\]
All polynomial degrees are bounded in the fixed finite profile family.

Take \(1/2<\sigma<2/3\) in (2.4). In (2.2), as \(l\to0\),
the \(l^{-2/3}\) polynomial cannot be canceled by any other displayed
term. Therefore \(P_{m,-,2}=0\). The same argument at \(l\to\infty\)
gives \(P_{m,+,2}=0\). This is an absolute-growth exclusion; it does
not assert absence of the second character from the local Jacquet
module.

## 3. The direct constant vanishes on every nonunit presentation

For every digit, including zero, source (5.3) gives
\[
               \sum_{z\bmod p}\alpha_{p,j}(z)=0.         \tag{3.1}
\]
This is the exact additive transform at the zero argument, with the
source's natural zero even at exponent zero.

The automorphic constant term is invariant under left \(N(\mathbb A)\).
For the direct term, right translation by \(n(z/p)\) becomes such
a left translation after passing the diagonal. Thus its value is
independent of \(z\). Any explicit exterior prime factor therefore
annihilates the direct constant by (3.1):
\[
                         C_m^+(l)=0.                  \tag{3.2}
\]
This includes redundant sixth-power factors and pure coprimality
punctures. Cancellation of a primitive character does not remove the
displayed local zero.

Only a presentation without any exterior prime mask can have a
direct \(l^{1/3}\) term. This exceptional finite-profile case is kept
separate; no artificial puncture is inserted in the recursion.

## 4. Rational torus transport with finite class weights

Fix a local active choice \(z_p\ne0\). The exact lifted Bruhat identity
is source (5.7):
\[
 wn(z_p/p)=(z_p/p)I\,n(-p/z_p)a(p^2z_p^{-2})\bar n(p/z_p).
                                                               \tag{4.1}
\]
The split central scalar is trivial, the left unipotent does not
change the constant term, and the final compact factor fixes the
good spherical vector.

The unit-phase assertion here does not use a Whittaker-functional
identity at zero. It follows from the ordinary torus cocycle and
right compact invariance, exactly the last calculation below source
(5.8). For a unit \(u\), any linear functional on the same spherical
vector has
\[
 \ell\bigl(\pi(a(p^e u))v_p^\circ\bigr)
       =\chi_p(u)^{2e}
                       \ell\bigl(\pi(a(p^e))v_p^\circ\bigr).
                                                               \tag{4.2}
\]
Indeed the factor is the cocycle between \(a(p^e)\) and the compact
torus element \(a(u)\); it is independent of the chosen functional.
For \(e=2,\ u=z_p^{-2}\), this factor is
\(\chi_p(z_p)^{-8}=\chi_p(z_p)^4\).

Consequently the active digit sum is exactly
\[
 \sum_{z_p\ne0}\alpha_{p,j}(z_p)\chi_p(z_p)^4
  =\begin{cases}
       (q_p-1)/\tau_{p,4},&j=4,\\
       0,&j\ne4.
    \end{cases}                                          \tag{4.3}
\]
Its magnitude is \(q_p^{1/2}(1-q_p^{-1})\).
For \(j=0\), the inactive branch \(z_p=0\) has coefficient
\(1-q_p^{-1}\), and its active sum vanishes. For \(j\ne0\)
there is no inactive branch. Thus only the digit-four primes are
active in a surviving constant term.

Let \(r\) be their allowed product generator. Before integrating,
the exterior active diagonals are \(a(p^2)\). Left multiplication
by the rational matrix \(a(r^{-2})\) transports them to \(S\):
at an active exterior prime its product with \(a(p^2)\) is a unit
torus element; at the other exterior primes it is already a unit
torus element. Their compact actions can be removed. All ordinary
section cocycle factors have modulus one.

At \(S\), the resulting torus variable is \(r^{-2}y^{-1}\).
The cocycle is a product of the same Hilbert symbols
\(H_S([\cdot],[\cdot])^2\) as in source (5.4).
It depends only on \([r]\) and \([y]\) in the finite group
\(\mathcal V_S=F_S^\times/F_S^{\times6}\).
Set \(v=r^2y\). Then
\[
 |v|_S=q_r^2l,\qquad
 [y]=[r]^{-2}[v],\qquad
 L_\upsilon(y)^{-1}
            =L_\upsilon(r)^2L_\upsilon(v)^{-1}.          \tag{4.4}
\]
The last scalar has modulus one. Multiplicative sheet measure has
Jacobian one, and \(\Omega_l\) is transported to a fundamental
set on the new sheet. Thus the actual class cutoff becomes
\(1_{B_S}([r]^{-2}[v])\), accompanied by an explicit finite Hilbert
phase. Both belong to a finite family indexed by \([r]\).
They are not replaced by a row-dependent arbitrary function.

It follows that the reflected constant term has the form
\[
 C_m^-(l)=\epsilon_m
 \prod_{j_p=4}\frac{q_p-1}{\tau_{p,4}}
 \prod_{j_p=0}(1-q_p^{-1})\,
        B_{\upsilon,[r]}((q_r^2l)^{-1}),               \tag{4.5}
\]
where \(|\epsilon_m|=1\) or a bounded fixed finite linear combination
of such phases, and \(B_{\upsilon,[r]}\) ranges over a fixed finite
family of actual weighted constant functions. Every component
retains the transported cutoff and cocycle just described.

For every profile class that actually occurs, choose one realizing
row with digit four at its active primes. Its nonzero scalar in
(4.5) shows that Section 2's exclusion of the second exponent
applies to that profile. Classes never realized by a row need not
be included. Thus every retained profile's surviving part is
\(x^{1/3}\) times a fixed logarithmic polynomial. Consequently
(4.5) is
\[
 l^{-1/3}q_r^{-1/6}
 \prod_{p\mid m}(1-q_p^{-1})
       \widetilde P_{\upsilon,[r]}(\log l+2\log q_r),
                                                               \tag{4.6}
\]
up to unitary phases and fixed normalizations. The finite family
makes its coefficients uniformly bounded; the translated logarithms
cost \(q_m^\epsilon\). This proves the claimed moving-row bound
without using the nonuniform constants in (2.4).

## 5. Mellin reflection and selected full-index marks

The spherical norm-sheet Mellin factor is
\[
 \widehat V_0(t)=c_{F,S}A^t
       \bigl[\Gamma(t+1/3)\Gamma(t+2/3)\bigr]^{r_F},
                  \qquad r_F=[F:\mathbb Q]/2.            \tag{5.1}
\]
It is nonzero near \(t=1/3\). Equations (2.2), (3.2), and (4.6)
give a meromorphic continuation with only the indicated finite-order
pole at \(t=1/3\), for nonunit presentations. Dividing by (5.1)
and shifting a compact-test Mellin integral gives (1.2).
Derivatives of the fixed gamma factor change only the fixed
coefficient polynomial and its degree.

The nonconstant reflection retains every original local coefficient
and moving scale. Its multiplier is the source finite factor times
\[
        A_1^t\left[
          \frac{\Gamma(1/3+t)\Gamma(2/3+t)}
               {\Gamma(1/3-t)\Gamma(2/3-t)}
                    \right]^{r_F}.                    \tag{5.2}
\]
The nearest numerator poles are at \(-1/3\). Thus all source compact
profile estimates with \(0<a_0<1/3\), including \(a_0=1/4\), remain
available with finite seminorms and polynomial norm-height costs.

At a fresh full-index coprimality prime \(p\), insert explicit
digit zero in (4.3). Its active branch is zero and its inactive
branch contributes precisely \(1-q_p^{-1}\). There is no torus
translation, no class-weight shift, and no logarithmic change.
Hence every positive-pole coefficient polynomial has this exact
multiplier. Subtracting the coprimality mask from the unrestricted
full index gives the divisibility multiplier \(q_p^{-1}\).
Products of fresh selected primes iterate this rule coefficientwise.
Shared-prime zeros must be allocated before this fresh-prime rule,
just as in the source marked completion.

## 6. Why the unit presentation does not obstruct marked inverse moments

A direct constant can survive only when there is no explicit exterior
prime in the complete presentation. In the canonical moment
\(\chi_n(k)\chi_n(f)^4\rho(n)\), this forces both exterior ideals
\((k)_S\) and \(f\) to be units and \(\rho\) to have no exterior
puncture. In particular the relevant row is bounded.

Treat all bounded rows in the original squarefree column sum before
cube completion or theta reflection. This is the existing terminal
in Liu Section 10.2, paragraph immediately after (10.4):
absolute column counting and the label count give
\(\mathcal E\ll Z^{N+\epsilon}\le Z^{N+V+\epsilon}\).
The marked version is identical. Ope26a at the immutable pin above,
lines 7303–7315 (equation old-eq:4.2), defines
\[
 \mathfrak d(A)=\sum_{\text{selected tuples}}
                   \prod_i a_i(p_i)1_{p_i\mid A}
 \quad\text{and proves}\quad
                  |\mathfrak d(A)|\ll_\epsilon q_A^\epsilon
                                                               \tag{6.1}
\]
for a fixed slot count. Therefore the original normalized column
sum on each bounded row has square \(\ll Z^{N+\epsilon}\).
The factor \(Z^{-V}\), the label count and divisor-bounded label
weights give the same canonical bound. No selected-prime length
factor is charged a second time.

This bound is taken before inserting the completed index. It avoids
isolating a negative-pole residue whose selected multiplier would be
one rather than \(1/q_p\). All remaining theta terminals have an
explicit exterior row prime and hence (3.2). Every reflected
positive-pole residue used by that terminal obeys Section 5's mark
law. No new fixed puncture has to survive either Poisson transform.

## 7. The canonical residue energy

Apply RESIDUE_INDUCTION_INTERFACE.md to the surviving positive pole.
The shifted row digit is \(v_p(k)+4v_p(f)\pmod6\). The squared
residue factor costs \(q_p^{-1/3}\) on digits two/four and is zero
on odd digits. Its uniform row sum is
\[
 \sum_{Nk\ll Z^M}|{\mathfrak r}_{k,f}|^2
                    \ll Z^{M/3+\epsilon}(Nf)^\epsilon.
                                                               \tag{7.1}
\]
The finite logarithmic polynomials in (1.2) are absorbed in
\(Z^\epsilon\). Cube completion contributes
\(q_h^{-1}(Z^N/q_h^3)^{1/3}=Z^{N/3}q_h^{-2}\), which is summable.
Fresh selected primes contribute \(1/q_p\); assignments to the
extracted cube factor use the source divisor allocation.

Thus the residue part of a canonical energy is
\[
                           \ll Z^{(2N+M)/3+\epsilon}.
                                                               \tag{7.2}
\]
With \(F=N+V\) and the original strict margin
\(F-M-Q-z_0\ge c>0\),
\[
 F-\frac{2N+M}{3}
       =\frac{2V+Q+z_0+c'}3\ge c/3,\qquad
             c'=F-M-Q-z_0\ge c.                         \tag{7.3}
\]
The existing recursion absorbs this terminal contribution. All
nonconstant transforms, child widths and fixed coefficient orbits
are unchanged. This proves the spherical-residue interface needed
by an all-field resonant inverse adapter, under the stated source
inputs; the adapter and final comparison must still be stated in
their own field and character scope.
