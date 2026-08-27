# Boolean Frobenius tomography has an exact universal-filter trilemma

Status: **exact all-curve Boolean channel diagonalization, unconditional
member-adaptive Frobenius-filter minimality, exact finite-family universal
filter trilemma, and exact residue/energy signature; no modulus census,
owner theorem, number-field transfer, RH, or GRH theorem**

Bounded exact replay:
[function_field_boolean_frobenius_tomography.py](function_field_boolean_frobenius_tomography.py).
Canonical summary:
[function_field_boolean_frobenius_tomography.json](function_field_boolean_frobenius_tomography.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `FUNCTION_FIELD_BETA_BOOLEAN_EVALUATION_BANDPASS.md` | `7a54822cb9b20f331edb6f40b2276618c496c1cb` | `0306cfa06c68375dd62472073698aaae0ace0ff9` | literal beta source, Boolean split, unit-circle numerator nonvanishing, and energy law |
| `function_field_beta_boolean_evaluation_bandpass.py` | `7a54822cb9b20f331edb6f40b2276618c496c1cb` | `5ab6b5845838495362bb37883386b640e6a8900d` | exact recurrence and finite control |
| `FUNCTION_FIELD_FROBENIUS_CHANNEL_FILTER_CALCULUS.md` | `8192514ed68f50b8e2a9cff9e1bedab2478bb5c1` | `182fee0619e3a78b9e8d9435d921293328c37668` | stable-submultiset filter calculus and generic family lcm theorem |
| `function_field_frobenius_channel_filter_calculus.py` | `8192514ed68f50b8e2a9cff9e1bedab2478bb5c1` | `f349df947adecf99dec4558a99741d1b26641934` | bounded symbolic filter replay |

## 0. Outcome

The earlier Frobenius filter calculus proved a generic minimal-depth theorem:
after excluding accidental numerator cancellation, complementary Frobenius
factors are the unique primitive filters. The literal beta/Boolean source
removes that genericity caveat.

Indeed, at every normalized weight-one Frobenius root,

\[
 \left|\chi(P)q^{-e/2}z^e\right|=q^{-e/2}<1
 \qquad (|z|=1),
\tag{0.1}
\]

so the beta numerator

\[
 1-\chi(P)q^{-e/2}z^e
\tag{0.2}
\]

never vanishes there. The pole order after any finite degree filter is
therefore determined exactly by the filter's orbitwise vanishing orders.
There are no exceptional curves or conductors hidden behind a formal
"generic numerator" clause.

This gives three new exact conclusions.

1. **Member-adaptive tomography.** After a fixed prefilter, every
   coefficient-field Galois-stable submultiset of the surviving character
   Frobenius roots can be retained by one unique primitive additional
   filter. Its degree is exactly the deleted Frobenius multiplicity, counted
   with orbit degrees.
2. **Universal-filter trilemma.** Across a finite family, every Galois orbit
   is in exactly one of three states: pure deletion has the usual lcm/max
   order; compatible positive-retention requests force one exact common
   order; incompatible requests admit no member-blind scalar filter at all.
3. **Energy tomography.** Every retained orbit has a nonzero exact principal
   part and therefore a positive polynomial energy signature. Coherent
   \(+\)/\(-\) recombination can isolate or erase the entire character channel,
   while positive class-energy assembly retains one half of it exactly.

The second point is sharper than a family lcm lower bound. An lcm always
deletes a union of channels. It cannot in general make conflicting
memberwise choices about a shared Frobenius orbit.

## 1. The all-curve Boolean Hadamard split

Let \(C/\mathbf F_q\) be a fixed smooth projective geometrically connected
curve, let \(U\subset C\) be a nonempty open curve, and let \(P\in|U|\) have
degree \(e\). Let \(\chi\) be a nontrivial quadratic divisor or ray-class
character on \(U\), after removing its ramified places. For an effective
divisor \(D\), use the literal beta source

\[
 \beta_P(D)=\mu(D)-\mathbf 1_{P\le D}\mu(D-P)
\tag{1.1}
\]

and the two Boolean classes

\[
 \delta_{\sigma,\chi}(D)={1+\sigma\chi(D)\over2},
 \qquad \sigma\in\{+1,-1\}.
\tag{1.2}
\]

Let \(\mathcal G(z)\) be any fixed nonzero finite degree-lattice prefilter
over the coefficient field used below. The frozen Euler identity gives

\[
 \mathcal H_{\sigma,\chi}(z)
 ={1\over2}\left(\mathcal T_\chi(z)
     +\sigma\mathcal C_\chi(z)\right),
\tag{1.3}
\]

where

\[
 \begin{aligned}
 \mathcal T_\chi(z)
 &=\mathcal G(z)
   {1-q^{-e/2}z^e\over Z_U(z/\sqrt q)},\\
 \mathcal C_\chi(z)
 &=\mathcal G(z)
   {1-\chi(P)q^{-e/2}z^e\over L_U(z/\sqrt q,\chi)}.
 \end{aligned}
\tag{1.4}
\]

Thus the Boolean class coordinate has the exact Hadamard diagonalization

\[
 \boxed{
 \mathcal H_{+,\chi}+\mathcal H_{-,\chi}=\mathcal T_\chi,
 \qquad
 \mathcal H_{+,\chi}-\mathcal H_{-,\chi}=\mathcal C_\chi.}
\tag{1.5}
\]

The antisymmetric coordinate is the character tomography channel. This
remains true on positive-genus curves even when a zeta root and a character
\(L\)-root coincide. Such a coincidence may cancel in one individual class,
but it cannot contaminate the coherent contrast (1.5).

On \(\mathbf A^1\) with one deleted conductor \(Q\), the trivial channel is
analytic on \(|z|<\sqrt q\). There an uncanceled unit-circle character pole
also survives in each individual Boolean class.

## 2. Coefficient field and normalized Frobenius orbits

Fix a characteristic-zero coefficient field \(K\) containing \(\sqrt q\)
and the coefficients of the normalized weight-one factor, and require
\(\mathcal G\in K[z]\setminus\{0\}\). Write

\[
 L_U(z/\sqrt q,\chi)=A_\chi(z)P_\chi(z),
\tag{2.1}
\]

where \(A_\chi\) is regular and nonzero at every point of \(|z|=1\), and

\[
 P_\chi(z)=\prod_{\pi\in\mathcal O_K}\pi(z)^{m_{\chi,\pi}}.
\tag{2.2}
\]

Here the monic irreducible factors \(\pi\in K[z]\) are precisely the
\(K\)-Galois orbits of normalized weight-one roots. Function-field RH/Weil is
used only to put those roots on the unit circle. It supplies no
number-field statement.

Put

\[
 b_\pi=\operatorname {ord}_\pi\mathcal G,
 \qquad
 s_{\chi,\pi}=\max(m_{\chi,\pi}-b_\pi,0).
\tag{2.3}
\]

Thus \(s_{\chi,\pi}\) is the pole multiplicity which survived the prefilter.
For an additional polynomial filter \(F\in K[z]\), put

\[
 a_\pi=\operatorname {ord}_\pi F.
\tag{2.4}
\]

By (0.1), (2.1), and exact local cancellation, the final pole multiplicity
is not merely bounded by but equals

\[
 \boxed{
 r_{\chi,\pi}^{\rm out}
 =\max(s_{\chi,\pi}-a_\pi,0).}
\tag{2.5}
\]

This valuation identity is the engine of the packet.

The local selection and minimality theorems below need only this
nonvanishing on the circle. For the global coefficient/energy expansion in
Section 5, impose the additional analytic-gap hypothesis

\[
 A_\chi(z)^{-1}\text{ is holomorphic on }|z|<R_0
 \quad\text{for some }R_0>1.
\tag{2.6}
\]

This holds for the affine quadratic evaluation characters in the frozen
packet and for the geometrically nontrivial weight-one situation after all
lower-weight factors are put into \(A_\chi\). A geometrically constant
character with an interior normalized pole must first have that channel
deflated; otherwise (2.5) remains a correct local weight-one statement but
the total energy can be dominated by the interior pole.

### Descent boundary

Over a splitting field, one may choose individual roots. Over \(K\), the
chosen multiplicity must be constant on every \(K\)-Galois orbit, so the
smallest selectable unit is one irreducible factor \(\pi\).

If a smaller field \(K_0\) does not contain \(\sqrt q\), stability of an
unscaled factor in the \(u\)-variable is insufficient. The actual degree
filter is a polynomial in \(z\), so the scaled factor itself must descend to
\(K_0[z]\). Every theorem below is stated over a field in which the displayed
normalized factors exist. It cannot be pushed to a smaller coefficient field
by naming a non-descending root orbit.

## 3. Exact member-adaptive minimality

Choose a desired retained profile

\[
 0\le r_{\chi,\pi}\le s_{\chi,\pi}
\tag{3.1}
\]

which is \(K\)-Galois stable. Define

\[
 \boxed{
 F_{\chi,r}(z)
 =\prod_\pi\pi(z)^{s_{\chi,\pi}-r_{\chi,\pi}}.}
\tag{3.2}
\]

Then (2.5) proves that \(F_{\chi,r}\mathcal C_\chi\) retains exactly the
profile \(r\).

More is true.

### Theorem 3.1: unconditional primitive minimality

Among polynomial filters over \(K\) which retain exactly \(r\), (3.2) has
minimum degree. Its valuations at every Frobenius factor are forced, and it
is unique up to a nonzero scalar among filters of minimum degree. In
particular,

\[
 \boxed{
 \deg F_{\chi,r}
 =\sum_\pi
 (s_{\chi,\pi}-r_{\chi,\pi})\deg\pi.}
\tag{3.3}
\]

**Proof.** If \(r_{\chi,\pi}>0\), equation (2.5) forces

\[
 a_\pi=s_{\chi,\pi}-r_{\chi,\pi}.
\tag{3.4}
\]

If \(r_{\chi,\pi}=0\), it forces

\[
 a_\pi\ge s_{\chi,\pi}.
\tag{3.5}
\]

The least allowed order is again \(s_{\chi,\pi}-r_{\chi,\pi}\). Multiplying
the orbitwise requirements proves divisibility by (3.2). Any further factor
increases degree, while a nonzero scalar does not. \(\square\)

Unlike the predecessor's general curve filter theorem, this proof has no
formal no-accident hypothesis. Equation (0.1) excludes every unit-circle
beta-numerator accident for the literal source.

The prefilter cannot be undone. If it already leaves
\(s_{\chi,\pi}<r_{\chi,\pi}\), no polynomial additional filter can resurrect
the requested pole. Tomography deletes or retains surviving modes; it is not
an inverse to prior deletion.

## 4. A finite-family universal-filter trilemma

Now take a finite family \(\chi_1,\ldots,\chi_N\) over one fixed \(q\), one
coefficient field \(K\), and one common normalized degree variable. Factor
all normalized weight-one polynomials over \(K\), and let
\(s_{j,\pi}\) be the multiplicity surviving the common prefilter. Prescribe
desired retained multiplicities

\[
 0\le r_{j,\pi}\le s_{j,\pi}.
\tag{4.1}
\]

We ask for one **member-blind scalar polynomial** \(F\) realizing every
profile simultaneously. Put \(a_\pi=\operatorname {ord}_\pi F\). For each
orbit \(\pi\), define

\[
 E_\pi
 =\{s_{j,\pi}-r_{j,\pi}:r_{j,\pi}>0\},
 \qquad
 D_\pi=\max_{r_{j,\pi}=0}s_{j,\pi},
\tag{4.2}
\]

where the maximum of an empty set is zero.

### Theorem 4.1: orbitwise universal-filter trilemma

Exactly one of the following holds for each \(\pi\).

1. **Pure deletion.** \(E_\pi=\varnothing\). The unique minimum order is

   \[
    a_\pi=D_\pi=\max_j s_{j,\pi}.
   \tag{4.3}
   \]

   This is the usual lcm/max-multiplicity rule.
2. **Compatible retention.** \(E_\pi=\{a_\pi^*\}\) is a singleton and
   \(a_\pi^*\ge D_\pi\). The unique possible order is

   \[
    a_\pi=a_\pi^*.
   \tag{4.4}
   \]

3. **Scalar-filter obstruction.** Either \(E_\pi\) contains two different
   exact orders, or its unique order is smaller than \(D_\pi\). No scalar
   universal filter exists.

**Proof.** A member retaining a positive multiplicity forces the equality
\(a_\pi=s_{j,\pi}-r_{j,\pi}\). A member deleting the orbit forces the
inequality \(a_\pi\ge s_{j,\pi}\). Intersect these equalities and half-lines.
The three displayed cases exhaust the possibilities. Distinct irreducible
orbits are coprime, so their conditions combine independently. \(\square\)

When every member requests complete deletion, Theorem 4.1 gives the exact
corollary

\[
 \boxed{
 F_{\rm full}(z)
 =\operatorname {lcm}_j
   \left(\prod_\pi\pi(z)^{s_{j,\pi}}\right).}
\tag{4.5}
\]

This lcm theorem is unconditional for the beta/Boolean contrast, not a
generic formal-numerator statement.

The obstruction case is more informative. If one member wants to retain an
orbit with its full surviving multiplicity, it forces \(a_\pi=0\). If any
other member wants to delete the same orbit, it forces \(a_\pi>0\). No
member-blind scalar polynomial can do both. Likewise, two members can retain
different multiplicities only when the required deleted multiplicities
\(s_{j,\pi}-r_{j,\pi}\) agree.

This is a genuine family-design boundary. To violate it one must add a
member label, use a vector- or representation-valued filter, or coherently
mix family members before specialization. A longer scalar polynomial does
not help.

## 5. Exact residue and energy signature

Assume the analytic gap (2.6). Let \(F\) be any allowed filter, and write

\[
 \mathcal C_{\chi,F}(z)=F(z)\mathcal C_\chi(z).
\tag{5.1}
\]

For a normalized root \(\lambda\) with final pole multiplicity
\(r_\lambda>0\), define

\[
 A_\lambda
 =\lim_{z\to\lambda^{-1}}
  (1-\lambda z)^{r_\lambda}\mathcal C_{\chi,F}(z).
\tag{5.2}
\]

Equation (0.1), regularity of \(A_\chi\), and the exact filter valuations
show that

\[
 \boxed{A_\lambda\ne0.}
\tag{5.3}
\]

Put \(M=\max_\lambda r_\lambda\). Partial fractions give

\[
 [z^n]\mathcal C_{\chi,F}(z)
 =\sum_{r_\lambda>0}Q_\lambda(n)\lambda^n+O(R^{-n}),
 \qquad \deg Q_\lambda=r_\lambda-1,
\tag{5.4}
\]

for some \(R>1\), with leading coefficient

\[
 {A_\lambda\over(r_\lambda-1)!}.
\tag{5.5}
\]

Consequently,

\[
 \boxed{
 \sum_{n=0}^H
 \left|[z^n]\mathcal C_{\chi,F}\right|^2
 ={H^{2M-1}\over
 (2M-1)((M-1)!)^2}
 \sum_{r_\lambda=M}|A_\lambda|^2
 +O(H^{2M-2}).}
\tag{5.6}
\]

Every nonempty selected profile therefore has a strictly positive leading
energy signature. If the retained profile is empty, the character contrast
has no weight-one pole and its coefficients decay exponentially up to the
next analytic boundary.

Different adaptive filters can isolate different \(K\)-Galois orbits. Their
pole order, oscillatory coefficient packet, and leading energy constant form
an exact Frobenius tomography ledger. Energy alone records squared residue
mass; the coherent coefficient sequence retains the phases.

## 6. Coherent recombination versus positive energy

Apply the same filter \(F\) to both Boolean classes and write their
coefficient sequences as \(h_{+,F}(n)\) and \(h_{-,F}(n)\). Let \(t_F(n)\)
and \(c_F(n)\) be the filtered trivial and character sequences. Equation
(1.5) gives, coefficientwise,

\[
 \boxed{
 h_{+,F}+h_{-,F}=t_F,
 \qquad
 h_{+,F}-h_{-,F}=c_F.}
\tag{6.1}
\]

Thus a coherent signed recombination can completely remove either channel.
Positive energy cannot:

\[
 \boxed{
 |h_{+,F}(n)|^2+|h_{-,F}(n)|^2
 ={\,|t_F(n)|^2+|c_F(n)|^2\over2}.}
\tag{6.2}
\]

After summing through \(H\), one half of the character tomography energy is
retained exactly, with no cross term available for cancellation.

On the affine evaluation family the trivial channel is exponentially
decaying. Combining (5.6) and (6.2) gives

\[
 \boxed{
 \sum_{n=0}^H
 \left(|h_{+,F}(n)|^2+|h_{-,F}(n)|^2\right)
 ={H^{2M-1}\over
 2(2M-1)((M-1)!)^2}
 \sum_{r_\lambda=M}|A_\lambda|^2
 +O(H^{2M-2}).}
\tag{6.3}
\]

On a positive-genus curve the trivial channel may have its own unit-circle
energy. Formula (6.2), rather than a claimed absence of those poles, is the
safe theorem: the two nonnegative channel energies add separately.

## 7. Bounded exact control

The replay uses one formal normalized character polynomial for a
degree-five conductor over \(\mathbf F_9\):

\[
 P_\chi(z)=(1+z)^2(1+z^2),
 \qquad e=1,
 \qquad \chi(P)=-1.
\tag{7.1}
\]

The adaptive filter

\[
 F(z)=1+z^2
\tag{7.2}
\]

deletes the conjugate pair \(\{i,-i\}\) and retains the double root
\(\lambda=-1\). The character contrast becomes

\[
 \mathcal C_F(z)={1+z/3\over(1+z)^2}.
\tag{7.3}
\]

Its coefficients are

\[
 c_F(0)=1,
 \qquad
 c_F(n)=(-1)^n\left({2n\over3}+1\right)\quad(n\ge1),
\tag{7.4}
\]

and hence exactly

\[
 \boxed{
 \sum_{n=0}^H|c_F(n)|^2
 ={4\over27}H^3+{8\over9}H^2+{47\over27}H+1.}
\tag{7.5}
\]

The positive two-class aggregate has leading coefficient \(2/27\), one half
of the character coefficient, because the filtered trivial channel is
exponentially decaying.

The replay also checks a two-member orbit profile. One member has
\(a^2b\) and retains \(a\); the other has \(a^3c\) and retains \(a^2\), with

\[
 \deg a=1,\qquad \deg b=\deg c=2.
\]

Both positive requests force one copy of \(a\) into the filter. Deleting
\(b,c\) gives the compatible primitive universal filter \(abc\), of degree
five. Complete deletion instead gives \(a^3bc\), of degree seven. Asking the
second member to delete \(a\), or asking it to retain only one of its three
copies, triggers the two distinct obstruction cases of Theorem 4.1.

The polynomial (7.1) is a formal Weil-circle control. No claim is made that
a particular degree-five modulus realizes it.

## 8. What is genuinely new here

This packet is not just the juxtaposition of the two frozen inputs.

- The general filter calculus needed a generic no-accident hypothesis. The
  literal beta numerator removes it and makes minimality exact for every
  conductor/curve channel in scope.
- The predecessor's finite-family result treated complete nulling by an lcm.
  Theorem 4.1 solves arbitrary retained multiplicities and identifies when a
  universal scalar filter does not exist at any degree.
- The Boolean Hadamard coordinate makes this exact even when zeta and
  character roots coincide on a positive-genus curve.
- The selected profile is tied to a nonzero residue and energy law, so the
  filter output has an exact auditable spectral signature rather than only a
  divisibility certificate.

The result is still a function-field calibration theorem. Function-field RH
supplies the Frobenius circle; nothing here transfers a filter, estimate, or
zero statement to the integer zeta function. The Boolean restriction is an
evaluation character, not largest-prime ownership. No WAVEPRIMCAR, owner,
CYSEL, RH, or GRH claim is made.

## 9. Proof and scope ledger

| statement | grade |
|---|---|
| literal beta/Boolean Hadamard split (1.3)--(1.5) | **IMPORTED EXACT ALL-CURVE IDENTITY** |
| beta numerator nonvanishing (0.1) | **IMPORTED EXACT ON THE UNIT CIRCLE** |
| exact output multiplicity (2.5) | **PROVED BY LOCAL VALUATIONS** |
| member-adaptive primitive filter (3.2)--(3.3) | **PROVED EXACT WITHOUT GENERICITY** |
| coefficient-field Galois-orbit criterion | **PROVED BY FACTORIZATION; SCALED DESCENT REQUIRED** |
| finite-family universal-filter trilemma | **PROVED EXACT ORBITWISE** |
| full-deletion lcm corollary | **PROVED EXACT WITHOUT GENERICITY** |
| nonzero selected residues and energy law (5.2)--(5.6) | **PROVED BY NONVANISHING AND PARTIAL FRACTIONS UNDER (2.6)** |
| coherent/positive assembly firewall (6.1)--(6.3) | **PROVED EXACT** |
| formal double-root energy \(4/27\) | **REPLAYED EXACT; NO MODULUS REALIZATION CLAIM** |
| owner or incomplete WAVEPRIMCAR theorem | **NOT INCLUDED** |
| number-field transfer | **NOT CLAIMED** |
| RH or GRH | **NOT PROVED** |

## 10. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/function_field_boolean_frobenius_tomography.py --check
python -B -O research/l-families/atlas/function_field/function_field_boolean_frobenius_tomography.py --check
python -B -m unittest tests.test_function_field_boolean_frobenius_tomography
python -B -O -m unittest tests.test_function_field_boolean_frobenius_tomography
python -B -m ruff check research/l-families/atlas/function_field/function_field_boolean_frobenius_tomography.py tests/test_function_field_boolean_frobenius_tomography.py
python -B -m ruff format --check research/l-families/atlas/function_field/function_field_boolean_frobenius_tomography.py tests/test_function_field_boolean_frobenius_tomography.py
~~~

The replay uses rational polynomial arithmetic, three orbit labels, two
family members, and a formal coefficient recurrence through degree \(40\).
It enumerates no finite-field element, modulus, point, closed point, curve,
\(L\)-function, or zero.
