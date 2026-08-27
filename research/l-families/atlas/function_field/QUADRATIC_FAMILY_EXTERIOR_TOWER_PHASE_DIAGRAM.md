# The degree-five marked family has an exact exterior-tower phase diagram

Status: **exact all-mark extension-field identity, exact primitive-exterior
collapse, exact low-mark and stable weight phase diagram, recurrence bounds,
and a formal universal-filter no-go; no finite-field enumeration, arithmetic
equidistribution, new sheaf decomposition, zero theorem, RH, or GRH claim**

Bounded replay:
[quadratic_family_exterior_tower_phase_diagram.py](quadratic_family_exterior_tower_phase_diagram.py).
Canonical summary:
[quadratic_family_exterior_tower_phase_diagram.json](quadratic_family_exterior_tower_phase_diagram.json).

Frozen source: the exact multi-place \(L\)-function identity at commit
`c94466e28a48ec429150f63de6d334d4c4f60110`.  The packet imports its
all-field degree-five coefficient formula and exact curve/infinity adapter.
It does not import any later two-, three-, four-, or six-place extension
packet.

## 0. Outcome

Fix an odd prime \(p\), an integer \(1\le m\le p\), and a set
\(A\subset\mathbf F_p\) of \(m\) distinct finite rational places.  At every
extension degree \(n\ge1\), embed the same set \(A\) in
\(\mathbf F_{p^n}\), and define

\[
 S_A(n)=
 \sum_{D\in\mathcal H_5(p^n)}\prod_{a\in A}\chi_{p^n}(D(a)).
\tag{0.1}
\]

Let \(V_A\) be the finite Dirichlet Frobenius representation supplied by
the locked character adapter, let \(F\) be its base Frobenius, and put

\[
 E_j(n)=\operatorname{Tr}
 \left(F^n\mid\bigwedge^jV_A\right).
\tag{0.2}
\]

Its dimension is \(m-1\).  More precisely, for the source-convention curve

\[
 C_A:y^2=\prod_{a\in A}(a-z),
 \qquad H=H^1(C_{A,\overline{\mathbf F}_p},\mathbf Q_\ell),
\tag{0.3}
\]

the exact parity adapter is

\[
 \boxed{
 V_A=
 \begin{cases}
 H,&m\text{ odd},\\
 \mathbf 1\oplus H,&m\text{ even}.
 \end{cases}}
\tag{0.4}
\]

Write \(C_m=\binom{m+1}{2}\).  Then the complete extension tower is

\[
\boxed{
 S_A(n)=
 (mp^n-C_m)E_1(n)+(p^n-m)E_3(n)-E_5(n).}
\tag{0.5}
\]

If \(\Lambda_j\) is the Frobenius eigenvalue multiset on
\(\bigwedge^jV_A\), (0.5) is equivalently the virtual root ledger

\[
\boxed{
\begin{aligned}
 S_A(n)={}&
 \sum_{\lambda\in\Lambda_1}
 \bigl(m(p\lambda)^n-C_m\lambda^n\bigr)\\
 &+\sum_{\mu\in\Lambda_3}
 \bigl((p\mu)^n-m\mu^n\bigr)
 -\sum_{\nu\in\Lambda_5}\nu^n.
\end{aligned}}
\tag{0.6}
\]

This already proves that the raw tower is a finite constant-coefficient
recurrence.  The main result is that symplectic exterior algebra collapses
(0.6) much further and reveals a sharp nonmonotone weight phase.

## 1. Derivation from the locked coefficient identity

Over \(\mathbf F_{p^n}\), put \(q=p^n\).  If

\[
 L_{A,n}(u)=\det(1-F^nu\mid V_A)
 =\sum_j\ell_j(n)u^j,
\tag{1.1}
\]

then

\[
 \ell_j(n)=(-1)^jE_j(n).
\tag{1.2}
\]

The locked degree-five extraction is

\[
 S_{5,m}=(C_m-mq)\ell_1+(m-q)\ell_3+\ell_5.
\tag{1.3}
\]

All three indices are odd, so substituting (1.2) into (1.3) proves
(0.5).  Multiplying a power sum by \(p^n\) dilates each recurrence root by
\(p\), which proves (0.6).

The even-parity summand \(\mathbf1\) in (0.4) is the split-infinity factor
\((1-u)\).  It is not an optional normalization.  For odd \(m\), the curve
in (0.3) is also not silently replaceable by the monic polynomial
\(\prod_a(z-a)\): that replacement multiplies the right side by \(-1\) and
is the nontrivial quadratic twist when \(-1\) is nonsquare.  Along the
extension tower the twist sign is raised to the \(n\)-th power.

## 2. Primitive symplectic coordinates

Put \(g=\lfloor(m-1)/2\rfloor\).  For

\[
 h_j(n)=\operatorname{Tr}(F^n\mid\bigwedge^jH),
\tag{2.1}
\]

define the primitive exterior trace, for \(0\le j\le g\), by

\[
 \Phi_j(n)=h_j(n)-p^nh_{j-2}(n),
 \qquad \Phi_0(n)=1,
\tag{2.2}
\]

with negative indices zero.  Symplectic Lefschetz decomposition and
reciprocity give

\[
 h_j=\Phi_j+p^nh_{j-2}\quad(j\le g),
 \qquad
 h_j=p^{n(j-g)}h_{2g-j}\quad(j>g).
\tag{2.3}
\]

Every eigenvalue contributing to \(\Phi_j\) has absolute value
\(p^{j/2}\).  Thus \(\Phi_j\) is a pure Weil-weight-\(j\) row.  For even
\(m\), (0.4) also gives

\[
 E_j=h_j+h_{j-1};
\tag{2.4}
\]

for odd \(m\), \(E_j=h_j\).

## 3. The complete low-mark ladder

Equations (0.5) and (2.3)--(2.4) give the following exact table.  Here and
below \(q=p^n\), so each displayed equality is an equality of complete
extension sequences, not a one-field interpolation.

\[
\boxed{
\begin{array}{c|l|l}
m& S_A(n)&\text{Weil weights present}\\ \hline
1&0&\varnothing\\
2&2q-3&2,0\\
3&3(q-2)\Phi_1&3,1\\
4&q^2-10+(4q-10)\Phi_1&4,3,1,0\\
5&(q^2-15)\Phi_1&5,1\\
6&(q^2-21)\Phi_1+(q-6)\Phi_2-21&5,4,2,1,0\\
7&(q-7)\Phi_3-28\Phi_1&5,3,1\\
8&(q-8)\Phi_3-8\Phi_2-36\Phi_1-36&5,3,2,1,0\\
9&-9\Phi_3-45\Phi_1&3,1\\
10&-\Phi_4-10\Phi_3-10\Phi_2-55\Phi_1-55&4,3,2,1,0.
\end{array}}
\tag{3.1}
\]

The rows at \(m=1,\ldots,6\) recover the locked one- through six-place raw
formulas after the standard conversions between \(h_1,h_2\) and the curve
coefficients.  The table is derived directly from the all-\(m\) source,
not from those later packets.

## 4. Stable collapse and the unique weight-five notch

For odd \(m\ge9\), put \(g=(m-1)/2\).  At \(g=4\), reciprocity says
\(h_5=p^nh_3\); write \(\Phi_5=0\) in that boundary row.  For \(g\ge5\),
\(\Phi_5=h_5-p^nh_3\) is the genuine fifth primitive exterior trace.  In
both cases the exact stable formula is

\[
\boxed{
 S_A(n)=-\Phi_5(n)-m\Phi_3(n)-C_m\Phi_1(n),
 \qquad m\ge9\text{ odd}.}
\tag{4.1}
\]

For even \(m\ge10\), put \(g=(m-2)/2\), with the same boundary convention
\(\Phi_5=0\) at \(g=4\).  Then

\[
\boxed{
\begin{aligned}
 S_A(n)={}&-\Phi_5(n)-\Phi_4(n)
 -m\bigl(\Phi_3(n)+\Phi_2(n)\bigr)\\
 &-C_m\bigl(\Phi_1(n)+1\bigr),
 \qquad m\ge10\text{ even}.
\end{aligned}}
\tag{4.2}
\]

All explicit factors \(p^n\) have disappeared.  This yields the complete
top-weight phase:

\[
\boxed{
\begin{array}{c|c|c}
\text{mark counts}&\text{weight-five carrier}&\text{coefficient}\\ \hline
5,6&p^{2n}\Phi_1&+1\\
7,8&p^n\Phi_3&+1\\
9,10&\text{none}&0\\
m\ge11&\Phi_5&-1.
\end{array}}
\tag{4.3}
\]

Thus \(m=9,10\) is the unique interior mark-count notch for the degree-five
top channel.  It is not a monotone loss of exterior support: the channel
returns at \(m=11\) as a new primitive representation and then has the
rigid coefficient \(-1\) forever.

There is also a sharp formal no-go.  On a generic symplectic torus with
coordinates \(x_1,\ldots,x_g\), a weight of \(\Phi_5\) has recurrence root

\[
 p^{5/2}x_1x_2x_3x_4x_5.
\tag{4.4}
\]

If a polynomial \(Q(T)\in\mathbf Q(p)[T]\), independent of the marked
configuration, annihilated the entire moving \(\Phi_5\) row for every
formal torus point, then

\[
 Q(p^{5/2}x_1x_2x_3x_4x_5)=0
\tag{4.5}
\]

as a Laurent identity.  Hence \(Q=0\).  No nonzero finite-degree universal
extension-shift filter can recreate the \(m=9,10\) cancellation in the
stable formal symplectic family.  This is a representation-theoretic
statement; it does not assume or assert Zariski density for the arithmetic
branch-point family at a fixed prime.

## 5. Exact recurrence bounds and memberwise ranks

Let

\[
 R_j(T)=\det(T-F\mid\operatorname{Prim}^jH),
 \qquad
 d_j=\deg R_j=
 \binom{2g}{j}-\binom{2g}{j-2}.
\tag{5.1}
\]

Unavailable primitive indices have degree zero.  Equations (4.1)--(4.2)
show that stable annihilators are

\[
 \boxed{R_1R_3R_5\quad(m\ge9\text{ odd})}
\tag{5.2}
\]

and

\[
 \boxed{(T-1)R_1R_2R_3R_4R_5
 \quad(m\ge10\text{ even}).}
\tag{5.3}
\]

Their orders telescope exactly:

\[
 d_1+d_3+d_5=\binom{2g}{5},
\tag{5.4}
\]

and

\[
 1+d_1+d_2+d_3+d_4+d_5
 =\binom{2g+1}{5}.
\tag{5.5}
\]

Therefore every stable tower has a recurrence of order at most

\[
\boxed{\binom{m-1}{5}.}
\tag{5.6}
\]

This characteristic-polynomial annihilator does not require a
distinct-root assumption.  For exact *minimal* ranks, use the standard
semisimplicity of Frobenius on \(H^1\) of a curve (equivalently on its
Jacobian), inherited by the exterior representations.  Let \(r_j(A)\) be
the number of distinct eigenvalues of \(F\) on
\(\operatorname{Prim}^jH\).  Weil moduli separate different \(j\)-rows, and
all coefficients in (4.1)--(4.2) are nonzero.  Hence

\[
\boxed{
 \operatorname{rank}_{\min}S_A=
 \begin{cases}
 r_1+r_3+r_5,&m\ge9\text{ odd},\\
 1+r_1+r_2+r_3+r_4+r_5,&m\ge10\text{ even},
 \end{cases}}
\tag{5.7}
\]

again omitting \(r_5\) at \(g=4\).  Repeated roots change their amplitude,
not the order of the exponential basis.

Before the stable range, the same argument gives the exact memberwise
rank ledger

\[
\boxed{
\begin{array}{c|c|c}
m&\operatorname{rank}_{\min}&\text{characteristic-polynomial order bound}\\ \hline
1&0&0\\
2&2&2\\
3&2r_1&2d_1\\
4&2+2r_1&2+2d_1\\
5&2r_1&2d_1\\
6&1+2r_1+2r_2&1+2d_1+2d_2\\
7&r_1+2r_3&d_1+2d_3\\
8&1+r_1+r_2+2r_3&1+d_1+d_2+2d_3.
\end{array}}
\tag{5.8}
\]

The factors of two are literal root dilations by \(p\) or \(p^2\), not
fitted duplicate recurrences.

## 6. Generic torus ranks are not representation dimensions

For a formal generic maximal torus of \(\operatorname{Sp}(2g)\), the
distinct Laurent weights in the fundamental primitive exterior
representation have count

\[
\boxed{
 r_j^{\rm tor}(g)=
 \sum_{\substack{0\le s\le j\\s\equiv j\ ({\rm mod}\ 2)}}
 2^s\binom gs.}
\tag{6.1}
\]

Indeed, a weight has \(s\) nonzero signed coordinates and \(j-s\) even;
all such supports occur.  More precisely, if \(a=(j-s)/2\), its primitive
multiplicity is
\(\binom{g-s}{a}-\binom{g-s}{a-1}>0\) because \(j\le g\).  Those
multiplicities need not equal one.  For example,

\[
 d_3(4)=48,\qquad r_3^{\rm tor}(4)=40,
\tag{6.2}
\]

and

\[
 d_4(4)=42,\qquad r_4^{\rm tor}(4)=41.
\tag{6.3}
\]

Consequently the first formal-generic ranks are

\[
\begin{array}{c|rrrrrrrrrrr}
m&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\operatorname{rank}_{\rm tor}&2&4&6&8&19&34&48&48&115&222&385.
\end{array}
\tag{6.4}
\]

For odd \(m\ge11\), this becomes

\[
 6g+16\binom g3+32\binom g5,
\tag{6.5}
\]

and for even \(m\ge12\),

\[
 3+6g+8\binom g2+16\binom g3
 +16\binom g4+32\binom g5.
\tag{6.6}
\]

These are formal generic-torus ranks.  They are not assertions that the
arithmetic marked family has full monodromy, realizes a generic torus
point, or equidistributes.

## 7. Pure Tate baselines, affine subtraction, and the scalar-notch alias

Primitive even exterior representations have zero weights.  Their exact
zero-weight multiplicities are

\[
 z_{2r}(g)=\binom gr-\binom g{r-1}.
\tag{7.1}
\]

Thus \(z_2=g-1\) and \(z_4=\binom g2-g\).  The pure recurrence roots in the
even low-mark rows are

\[
\begin{array}{c|l|l}
m&\text{pure Tate baseline}&\text{minimal homogeneous root set}\\ \hline
2&2p^n-3&\{1,p\}\\
4&p^{2n}-10&\{1,p^2\}\\
6&p^{2n}-6p^n-21&\{1,p,p^2\}\\
8&-16p^n-36&\{1,p\}.
\end{array}
\tag{7.2}
\]

For every even \(m\ge10\), (4.2) has the exact baseline

\[
\boxed{
 -C_m-m(g-1)p^n-\left(\binom g2-g\right)p^{2n}.}
\tag{7.3}
\]

All three coefficients are nonzero for \(g\ge4\).  Hence the unique monic
minimum-degree homogeneous scalar filter removing those roots termwise is

\[
 (E-1)(E-p)(E-p^2).
\tag{7.4}
\]

There is a provenance warning.  The roots \(p\) and \(p^2\) in (7.3) are
zero weights inside the irreducible primitive exterior representations;
they are not, merely from this calculation, constructed invariant Tate
subobjects.  On a special Frobenius torus, a nonzero weight can also
specialize to the same root.  Any homogeneous scalar filter containing
\((E-p)\) or \((E-p^2)\) deletes both contributions because a scalar tower
cannot distinguish their provenance after spectral collision.  The
six-place square-polynomial alias is the first low-rank instance of this
general phenomenon.

The known baseline (7.2)--(7.3) suggests a provenance-preserving alternative:
subtract it *affinely* before applying a homogeneous filter.  Such a
subtraction removes the fixed zero-weight amplitude while retaining any
excess amplitude caused by a special geometric collision.  This is an
exact algebraic option, not a cancellation estimate or a sheaf projector.

## 8. What the theorem does and does not say

The extension sequence keeps one base configuration \(A\subset\mathbf F_p\)
and base-changes it.  Choosing an unrelated configuration at every
extension degree does not define this Frobenius recurrence.  Conversely,
the family members \(D\in\mathcal H_5(p^n)\) are newly summed at each
extension; the theorem does not base-change one individual \(D\).

The notation \(E_j(n)\) is
\(\operatorname{Tr}(F^n\mid\bigwedge^jV)\).  It is generally **not**
\(E_j(1)^n\), nor is \(e_j(F^n)\) the \(n\)-th power of \(e_j(F)\).
Similarly, a representation dimension is not automatically a minimal
recurrence rank because distinct torus weights can have multiplicity.

The finite Dirichlet representation and curve adapter are imported from
the locked source.  This packet does not construct a new sheaf realizing
each displayed virtual decomposition, promote the family correlation to an
individual motive, control a family average, isolate a principal member,
or prove a statement about complex zeros.  No RH or GRH implication is
claimed.

## 9. Bounded replay

The producer performs sparse integer algebra in terms
\(q^k\Phi_j\), with \(j\le5\).  It verifies all ten low rows, the stable
collapse through \(m=24\), the exact weight-five support, recurrence-order
telescoping, zero-weight baselines, and bounded generic Weyl-support counts
through genus eight.  It constructs no matrix and enumerates no finite
field, polynomial family, branch set, curve, extension field, prime, or
zero.

~~~text
python -B research/l-families/atlas/function_field/quadratic_family_exterior_tower_phase_diagram.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_exterior_tower_phase_diagram.py --check
python -B -m unittest tests.test_quadratic_family_exterior_tower_phase_diagram
python -B -O -m unittest tests.test_quadratic_family_exterior_tower_phase_diagram
python -B -m ruff check research/l-families/atlas/function_field/quadratic_family_exterior_tower_phase_diagram.py tests/test_quadratic_family_exterior_tower_phase_diagram.py
python -B -m ruff format --check research/l-families/atlas/function_field/quadratic_family_exterior_tower_phase_diagram.py tests/test_quadratic_family_exterior_tower_phase_diagram.py
~~~

## 10. Claim ledger

| statement | grade |
|---|---|
| all-\(m\) exterior formula (0.5)--(0.6) | **PROVED EXACT FROM LOCKED SOURCE** |
| low-mark table (3.1) | **PROVED EXACT** |
| stable primitive collapse (4.1)--(4.2) | **PROVED EXACT** |
| unique \(m=9,10\) top-weight notch | **PROVED EXACT** |
| nonzero universal stable top-row filter | **REFUTED OVER THE FORMAL SYMPLECTIC TORUS** |
| characteristic-polynomial recurrence bounds | **PROVED EXACT** |
| distinct-root memberwise ranks | **PROVED USING STANDARD FROBENIUS SEMISIMPLICITY** |
| generic torus ranks | **FORMAL GENERIC; NO ARITHMETIC EQUIDISTRIBUTION CLAIM** |
| pure Tate baseline and homogeneous-filter alias warning | **PROVED EXACT AT TRACE LEVEL** |
| new sheaf decomposition, family estimate, RH, or GRH | **NOT PROVED** |
