# Ternary FFPS cyclic sheaf: fixed-fibre construction and invariant audit

Status: **exact fixed-fibre Kummer construction and exact invariant criterion;
varying-closed-place source complex and `CYSEL` remain open**.

## Start here

The minimal \(k=3,t=2\) physical hard mask from PR #756 has an honest
rank-two Kummer interpretation after passing to the quadratic orientation
cover of the physical coordinates. Its two selected modes are the two
faithful cubic characters. On the square-expanded pair space, their kernel is

\[
 \left({\Phi(\omega_1)\over\Phi(\omega_2)}\right)^r,
 \qquad r=1,2.
\tag{0.1}
\]

Fix a relative alignment

\[
 \varepsilon\in\{+1,-1\}
\]

between the two cubic character groups and write

\[
 R_X={X_1\over X_2},\qquad
 R_Y={Y_1\over Y_2},\qquad
 X=Pc^2,\quad Y=Qd^2.
\]

The sharp invariant test is:

\[
 \boxed{
 \mathcal M_r|_Z\text{ is geometrically constant}
 \iff
 R_XR_Y^{\varepsilon}
 \in K(Z)^{\times3},
 \qquad r=1,2.}
\tag{0.2}
\]

Here \(Z\) is any geometrically integral source stratum on which the displayed
units are defined. Consequently the rank-two selected system has geometric
invariant multiplicity

\[
 \boxed{
 \dim \mathcal M_{\rm sel}^{\pi_1^{\rm geom}(Z)}=
 \begin{cases}
 2,&R_XR_Y^\varepsilon\text{ is a cube in }K(Z),\\
 0,&\text{otherwise.}
 \end{cases}}
\tag{0.3}
\]

This passes the invariant test on the generic physical pair torus, but fails
on the aligned compensating resonance

\[
 X_1Y_1^\varepsilon=X_2Y_2^\varepsilon,
\tag{0.4}
\]

and in particular on every double physical collision. Wick normal ordering
removes the literal atomic diagonal only. It does **not** by itself remove all
of (0.4).

There is also no coefficient freedom inside the ternary two-point mask:
every retained two-subset of \(\mu_3\) has

\[
 |\gamma_1|^2=|\gamma_2|^2={1\over4}.
\tag{0.5}
\]

Rotating the hard mask therefore cannot null the resonant invariant channel.
One must prove cancellation on that source ledger, project it out by an exact
signed identity, or move to a richer mask family.

This invariant is an obstruction to a **separate** `CYSEL` estimate, not
automatically to the principal difference. The exact source identity is
\(P=C-S\). A common constant constituent of the hard-current complex \(C\)
and selected complex \(S\) could cancel before any absolute value is taken.
That relative cancellation is not constructed here, but it is a more direct
geometric target than bounding both constituents separately.

This is a useful first sheafification, but not `CYSEL`. At fixed complexity,
absence of a top invariant gives a Deligne bound only with its total compactly
supported Betti number. At fixed base field and growing conductor, the
irreducibility, degree-shell, Boolean-incidence, and varying-place operations
have not yet been assembled into one complex and no uniform Betti bound is
known.

The exact finite companion is
`ffps_cyclic_sheaf_invariant_audit.json`. It uses only
\(\mathbf Q(\zeta_3)\) and two-dimensional linear algebra over
\(\mathbf F_3\); it enumerates no field, place, conductor, curve,
\(L\)-function, or zero.

## 1. Source contract and a necessary characteristic correction

This packet consumes the following exact results at frozen PR #756 head
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`:

- `FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md`;
- `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md`;
- `FFPS_CYCLIC_CLOSURE_BUDGET.md`;
- live-source claims `L-106120`, `R-106122`, `R-106123`, `L-106131`, and
  `T-106140`, frozen there at PR #751 head
  `98af0db6ec7f77d6333a77a3dac53c4698852f43`.

The numerical leverage witness

\[
 (\ell,\rho)=(7,13),\qquad L_{\rm hard}=27/49
\]

uses two residue fields of different characteristics. It is **not** itself
one function-field sheaf over a common finite base. A function-field port
retains the mask order \(k=3\), density \(t/k=2/3\), and physical maps, but
replaces \(7,13\) by two distinct closed places of one
\(\mathbf F_q(T)\). Their residue cardinalities \(q^a,q^b\) must satisfy

\[
 6\mid q^a-1,\qquad 6\mid q^b-1.
\tag{1.1}
\]

The restricted-Gram leverage must then be recomputed for those cardinalities.
No statement below promotes the literal number-field value \(27/49\) to that
new panel.

This correction is load-bearing: a product of trace functions in
characteristics \(7\) and \(13\) is finite harmonic algebra, not the trace of
one \(\ell\)-adic complex over a common finite field.

There is nevertheless an exact smallest common-base control. Over
\(\mathbf F_7(T)\), choose two distinct degree-one places. Both physical
sign-pair dimensions are \(3\), and the locked cyclic-mask formula gives

\[
 \boxed{
 L_{\rm hard}={1\over2}
 <
 L_{\rm full}={9\over16}
 <
 L_{\rm soft}={513\over784}.}
\tag{1.2}
\]

The Wick atomic residual is still positive:

\[
 {1\over2}(7-1)^2-\left({3\over2}\right)^2={63\over4}.
\tag{1.3}
\]

Thus the qualitative hard gain, soft loss, and Wick obstruction coexist in
one characteristic. Equations (1.2)--(1.3) are a source-algebra control, not
the varying-place sheaf theorem.

## 2. Exact fixed-fibre Kummer construction

First work over one finite field \(k=\mathbf F_Q\), with \(6\mid Q-1\). The
two physical sides may be regarded as two labelled copies of this field. The
same construction applies after scalar extension to each geometric factor of
a Weil restriction when the two closed-place degrees differ; descent is
discussed separately in Section 6.

Choose exact-order-three characters

\[
 \theta_X,\theta_Y:k^\times\longrightarrow\mu_3
\]

and exact-order-six roots

\[
 \xi_X^2=\theta_X,\qquad \xi_Y^2=\theta_Y.
\]

Choose quadratic-sector representatives \(u_X,u_Y\). For physical points in
those sectors,

\[
 X/u_X=s_X^2,\qquad Y/u_Y=s_Y^2.
\tag{2.1}
\]

The oriented characters from PR #756 are

\[
 \epsilon_X(X)=\xi_X(X/u_X)=\theta_X(s_X),\qquad
 \epsilon_Y(Y)=\xi_Y(Y/u_Y)=\theta_Y(s_Y).
\tag{2.2}
\]

They are independent of \(s_X\mapsto-s_X\) and \(s_Y\mapsto-s_Y\), since
every cubic character is even under (1.1).

Let

\[
 \widetilde{\mathcal T}=\mathbf G_m^2
 \longrightarrow
 \mathcal T=\mathbf G_m^2,\qquad
 (s_X,s_Y)\longmapsto(u_Xs_X^2,u_Ys_Y^2).
\tag{2.3}
\]

This is the degree-four orientation cover for one physical atom. Fixing an
identification between the two abstract cubic value groups gives a relative
alignment \(\varepsilon=+1\) or \(-1\). On the cover put

\[
 \mathcal F_r
 =\mathcal L_{\theta^r(s_Xs_Y^\varepsilon)},
 \qquad r=1,2,
\tag{2.4}
\]

where \(\mathcal L_{\theta(f)}\) denotes the rank-one Kummer local system
attached to \(f\). Equivalently, before identifying the character groups,
(2.4) is the exterior tensor product of their two rank-one Kummer systems.

The trace of \(\mathcal F_r\) is exactly \(\Phi^r\), up to the fixed sector
scalar already recorded in the source-realization packet. Thus this is the
selected \(r\)-th `L-106120` double-nonprincipal member on one fixed clean
fibre.

On two atoms, let

\[
 \widetilde{\mathcal T}^{(2)}
 =\widetilde{\mathcal T}\times\widetilde{\mathcal T},
\]

and define

\[
 \boxed{
 \mathcal M_r
 =\operatorname{pr}_1^*\mathcal F_r
  \otimes
  \operatorname{pr}_2^*\mathcal F_r^\vee.}
\tag{2.5}
\]

Its trace is exactly the kernel in (0.1). Each \(\mathcal M_r\) is rank one,
pure of weight zero, and tamely ramified at the coordinate boundary. The
selected ternary system is

\[
 \boxed{\mathcal M_{\rm sel}=\mathcal M_1\oplus\mathcal M_2.}
\tag{2.6}
\]

It has rank two. The orientation cover on the two-atom physical pair torus
has degree \(4^2=16\), independent of conductor degrees.

### Source-coordinate pullback

On the source torus choose owner roots

\[
 P/u_X=a^2,\qquad Q/u_Y=b^2.
\]

Then

\[
 X=Pc^2=u_X(ac)^2,\qquad
 Y=Qd^2=u_Y(bd)^2,
\tag{2.7}
\]

and (2.4) pulls back to

\[
 \mathcal L_{\theta_X^r(ac)}
 \boxtimes
 \mathcal L_{\theta_Y^{\varepsilon r}(bd)}.
\tag{2.8}
\]

Equation (2.8) is the geometric form of the exact owner/core identity

\[
 \psi(P)\theta(c)=\psi(Pc^2).
\]

It also shows why a sheaf on owner labels alone is the wrong object.

## 3. Exact invariant criterion

Let \(Z\) be a geometrically integral locally closed source stratum inside the
two-atom orientation cover, and assume none of the four physical coordinates
vanishes on \(Z\). In \(K(Z)^\times\), put

\[
 U_Z=
 {s_{X,1}\over s_{X,2}}
 \left({s_{Y,1}\over s_{Y,2}}\right)^\varepsilon.
\tag{3.1}
\]

The restriction of \(\mathcal M_r\) is the cubic Kummer system attached to
\(U_Z^r\). A faithful cubic Kummer system is geometrically trivial exactly
when its defining unit is a cube in the function field. Both \(r=1\) and
\(r=2\) are invertible modulo three, so

\[
 \mathcal M_r|_Z\text{ trivial}
 \iff U_Z\in K(Z)^{\times3}.
\tag{3.2}
\]

But

\[
 U_Z^2=R_XR_Y^\varepsilon.
\tag{3.3}
\]

Squaring is an automorphism of
\(K(Z)^\times/K(Z)^{\times3}\). Therefore (3.2) is equivalent to (0.2).
This proves (0.2)--(0.3).

No external monodromy classification is needed: the statement follows from
the cyclic Kummer cover at the generic point. It is also gauge-stable. A
sector change multiplies \(U_Z\) by a geometric constant, which is a cube
over the algebraic closure. Simultaneous inversion of the primitive cubic
characters exchanges \(\mathcal M_1\) and \(\mathcal M_2\).

### Connected monomial subtori

For a connected monomial subtorus, (0.2) becomes exact linear algebra. Let

\[
 x=[R_X],\qquad y=[R_Y]
\]

be the exponent coordinates in \(\mathbf F_3^2\). If the stratum is cut out
by monomial relation rows \(L\subset\mathbf F_3^2\), then

\[
 \boxed{
 \mathcal M_r|_Z\text{ is constant}
 \iff (1,\varepsilon)\in
 \operatorname{rowspan}_{\mathbf F_3}(L).}
\tag{3.4}
\]

The companion producer verifies (3.4) for the exact strata in the next
section and for both relative alignments.

## 4. Constant, collision, and nonconstant strata

The criterion gives the following exact ledger.

| source stratum | relation | selected invariant multiplicity |
|---|---:|---:|
| generic physical pair torus | none | \(0\) |
| \(X_1=X_2\) only | \(R_X=1\) | \(0\), generically |
| \(Y_1=Y_2\) only | \(R_Y=1\) | \(0\), generically |
| aligned compensating resonance | \(R_XR_Y^\varepsilon=1\) | \(2\) |
| opposite resonance | \(R_XR_Y^{-\varepsilon}=1\) | \(0\), generically |
| double physical collision | \(R_X=R_Y=1\) | \(2\) |
| literal atomic diagonal | \(\omega_1=\omega_2\) | \(2\) |

Three distinctions matter.

1. **Atomic is smaller than constant.** Wick normal ordering subtracts the
   literal source diagonal. Distinct atoms can still have both physical
   squareclasses equal, and the compensating locus (0.4) is larger still.
2. **One collision is not enough.** If \(X_1=X_2\) but \(R_Y\) remains a
   noncube in the stratum function field, the selected system is nonconstant.
   This matches the mixed versus double Kummer split in `L-106131`.
3. **Equal product must be typed.** An equality among the original integer
   or polynomial products is a constant stratum only if it forces the
   residue-field relation (0.4). Conversely, (0.4) can hold without either
   physical coordinate agreeing separately.

More generally, every integral stratum on which

\[
 R_XR_Y^\varepsilon=G^3
\tag{4.1}
\]

for some \(G\in K(Z)^\times\) is resonant. Equation (4.1), not a finite list
of visual diagonals, is the complete geometric test.

This does **not** say that every point satisfying a cubic residue condition
creates a global constant constituent. Geometric triviality concerns the
function field of a whole integral stratum. Nor does a constant restriction
by itself prove a main term: the arithmetic Frobenius scalar and signed
source coefficient still matter. It says exactly which ledgers cannot be
discarded by citing nonprincipality of the ambient characters.

## 5. Ternary rigidity: mask rotation cannot remove the resonance

Let \(\mathscr S\subset\mu_3\) have size two and

\[
 \gamma_r={1\over2}\sum_{s\in\mathscr S}s^{-r},
 \qquad r=1,2.
\]

The missing element of \(\mu_3\) is \(m\). Since all three roots sum to zero,

\[
 \gamma_r=-{m^{-r}\over2},
\]

and hence (0.5) follows. Therefore the selected contribution in `CYSEL` is,
up to the already-recorded common live weights,

\[
 {1\over4}\mathcal M_1\oplus{1\over4}\mathcal M_2
\tag{5.1}
\]

for every rotated two-point hard mask.

The two modes have the same invariant locus, because both are faithful
characters of \(\mu_3\). Positive coefficients in (5.1) do not remove that
locus. The arithmetic traces of the two geometrically constant systems can
sum to \(2\) or to \(-1\), depending on the Frobenius scalar; there is no
universal zero.

Thus the minimal ternary mask has a useful rigidity/no-go:

\[
 \boxed{
 \text{mask rotation changes hard support labels but cannot tune the
 selected-mode invariant multiplicity.}}
\tag{5.2}
\]

Changing the **relative** primitive-character alignment replaces the product
resonance \(R_XR_Y\) by the quotient resonance \(R_X/R_Y\). It moves the
resonant ledger; it does not reduce its rank or local-system complexity.

## 6. Descent across closed places

Let \(\mathfrak l,\mathfrak r\) be distinct closed places of degrees \(a,b\)
over \(\mathbf F_q\). Their unit groups are the rational points of the tori

\[
 T_a=\operatorname{Res}_{\mathbf F_{q^a}/\mathbf F_q}\mathbf G_m,
 \qquad
 T_b=\operatorname{Res}_{\mathbf F_{q^b}/\mathbf F_q}\mathbf G_m.
\tag{6.1}
\]

For a **fixed** pair of places, the local multiplicative characters define
rank-one character sheaves on these tori, and the preceding construction can
be pulled back along the two physical maps. After base change to
\(\overline{\mathbf F}_q\), each Weil restriction splits into Frobenius
conjugate one-dimensional torus factors. The invariant test must hold on
every resulting geometric factor.

The pair of faithful cubic modes is better behaved than either labelled
mode: arithmetic Frobenius may invert \(\mu_3\), but that merely exchanges
\(\mathcal M_1\) and \(\mathcal M_2\). Thus their direct sum is a natural
rank-two descent object once a relative alignment has been fixed. If only one
local primitive character is inverted, the relative alignment changes; that
remains a genuine hard-mask choice.

Varying the places requires substantially more geometry. A plausible base
starts with squarefree-polynomial configuration spaces. A degree-\(a\)
closed place is represented by an \(\mathbf F_q\)-point whose Frobenius
permutation is an \(a\)-cycle; irreducibility is a Frobenius conjugacy
condition, not a Zariski-open condition on polynomial coefficients. One
would need, at minimum,

1. the two configuration spaces and their universal finite etale algebras;
2. the two unit Weil-restriction tori over that base;
3. the rank-two selected Kummer system with its relative alignment;
4. a class-function or cohomological realization of both irreducible-place
   conditions;
5. the Boolean/core/owner incidence complex and its degree restrictions;
6. the literal diagonal and every geometrically constant/resonant subquotient
   removed before the signed conductor recombination.

This universal complex is **not constructed here**. In particular, the
fixed-fibre rank two must not be confused with the rank after all of these
pushforwards.

## 7. What Deligne would and would not give

Let \(Z/\mathbf F_Q\) be a fixed smooth geometrically connected
\(d\)-dimensional stratum and let \(\mathcal M_r\) be lisse and pure of weight
zero on \(Z\). If (0.2) fails, then top compactly supported cohomology has no
invariant contribution. The Grothendieck trace formula and Weil II give the
schematic bound

\[
 \left|
 \sum_{z\in Z(\mathbf F_Q)}
 \operatorname{tr}(\operatorname{Frob}_z|\mathcal M_r)
 \right|
 \le
 B_c(Z,\mathcal M_r)Q^{d-1/2},
\tag{7.1}
\]

where

\[
 B_c(Z,\mathcal M_r)
 =\sum_i\dim H_c^i(Z_{\overline{\mathbf F}_Q},\mathcal M_r).
\]

For a curve, (7.1) is square-root size. In growing dimension it is only one
square-root saving against \(Q^d\); it is not \(Q^{d/2}\). On the complete
generic torus the multiplicative character sum can vanish exactly, but the
actual FFPS source is incomplete and weighted, so that special product
factorization is unavailable without proof.

At the elementary fixed-fibre level:

- each selected mode has rank one;
- the selected sum has rank two;
- Kummer ramification is tame and its Swan conductor is zero;
- the two-atom physical pair torus has dimension four and eight coordinate
  boundary divisors in \((\mathbf P^1)^4\);
- the orientation cover has degree sixteen.

All those costs are conductor-independent. They are not the costs deciding
`CYSEL`. The unproved growing costs include:

| operation | missing uniform ledger |
|---|---|
| varying closed places | rank and Betti growth on the two place-moduli spaces |
| irreducible-place selection | complexity of the Frobenius cycle-class projector |
| prime-owner shells | coherent explicit formula or sheaf realization across moduli |
| Möbius/Vaughan and Boolean incidence | ranks after convolution and compact pushforward |
| collision cleanup | number, degree, and Betti cost of all surviving strata |
| conductor recombination | cancellation before the outer absolute value |

At fixed \(q\), conductor degree grows while the number of conductor fibres
is power-sized. A fixed-fibre estimate, even with perfect local conductor,
does not pay that family; this is exactly the `R-106123` firewall. A valid
geometric `CYSEL` theorem must prove a bound of the form

\[
 \boxed{
 \text{normalized Frobenius trace of the complete selected complex}
 =Y^{o(1)},}
\tag{7.2}
\]

with the total Betti/conductor cost included and the varying-place sum still
signed. Neither (0.3) nor (7.1) proves (7.2).

The standard weight input is Deligne's
[Weil II](https://numdam.org/articles/10.1007/BF02684780/). Katz's
[Gauss Sums, Kloosterman Sums, and Monodromy Groups](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf)
is a primary reference for Kummer/trace-sheaf constructions. Quantitative
conductor control under cohomological transforms is itself a theorem to prove
in each setting; see Fouvry--Kowalski--Michel,
[On the conductor of cohomological transforms](https://arxiv.org/abs/1310.3603).
These references justify the framework, not the missing FFPS complex.

## 8. Consequence for mask/sheaf co-design

The first co-design score for a hard support should be the triple

\[
 \left(
 L_{\rm hard},
 \max_Z\dim\mathcal M_{\rm sel}^{\pi_1^{\rm geom}(Z)},
 B_{\rm normalized}
 \right),
\tag{8.1}
\]

where \(Z\) runs over source strata retained after exact cleanup and
\(B_{\rm normalized}\) is the **post-pushforward** complexity, not local rank.

For the ternary two-point mask, the first entry can improve, the generic
second entry is zero, but the aligned resonance has invariant multiplicity
two and cannot be changed by rotation. Therefore the next exact design
question is not another ternary leverage calculation. It is one of:

1. prove the full FFPS exceptional ledger removes (0.4) with no forbidden
   fibrewise absolute values;
2. construct a signed projector annihilating its contribution while
   preserving the hard inverse-Gram gain;
3. enlarge \(k\) and solve for Fourier coefficients orthogonal to all
   resonance characters, charging resulting rank and conductor;
4. prove a no-go showing every leverage-improving physical support has a
   surviving resonant constant channel.

The third and fourth options are the natural ambitious successors.

### Relative trace-sheaf target for the principal difference

The closure packet gives the exact scalar relations

\[
 P=C-S,\qquad A=C+R,\qquad K=S+R.
\tag{8.2}
\]

The invisible displacement

\[
 (C,S,R)\longmapsto(C+T,S+T,R-T)
\tag{8.3}
\]

changes only the common \(C,S\) background and leaves \(P\) fixed. Thus it
cannot hide a principal anomaly inside \(P\): exactly,

\[
 \max(|C|,|S|)\ge {1\over2}|P|.
\tag{8.4}
\]

It does explain why separate scalar bounds on \(A,K\) do not control either
constituent.

Geometrically, the strongest next object may therefore be a relative class

\[
 [\mathcal C_{\rm hard}]-[\mathcal M_{\rm sel}]
\tag{8.5}
\]

on one common source base, with literal atoms and inherited exceptional
strata already removed. The audit should ask whether the invariant
constituents identified by (0.2) occur in \(\mathcal C_{\rm hard}\) with the
same multiplicity, Tate shift, arithmetic Frobenius scalar, and source
coefficient. Only then may they cancel in (8.5).

At present \(\mathcal M_{\rm sel}\) has the fixed-fibre construction above,
while \(\mathcal C_{\rm hard}\) has only the exact hard-projector trace
identity from PR #756. There is no common derived complex and no morphism
whose cone realizes \(C-S\). Equality or cancellation of numerical traces on
tiny fibres would not supply one.

Accordingly there are two honest geometric routes:

1. **separate route:** excise or control every resonant constituent of
   \(\mathcal M_{\rm sel}\) and prove `CYSEL`;
2. **relative route:** construct (8.5) and prove that common invariants cancel
   before estimating the principal trace.

The second route could be strictly stronger: `CYSEL` is sufficient for
controlling the cyclic pieces, but it is not logically necessary for the
already exact principal extraction \(P=C-S\).

## 9. Exact proof grades

| statement | grade |
|---|---|
| physical orientation cover and fixed-fibre Kummer systems (2.3)--(2.6) | **PROVED EXACT** |
| owner/core pullback (2.7)--(2.8) | **PROVED EXACT FROM LOCKED SOURCE** |
| cube-class invariant criterion (0.2)--(0.3) | **PROVED EXACT** |
| connected monomial-subtorus row-span test (3.4) | **PROVED EXACT FINITE** |
| generic, collision, and aligned-resonance table | **PROVED EXACT AT DECLARED STRATA** |
| ternary Fourier rigidity (0.5) and rotation no-go | **PROVED EXACT** |
| fixed-place rank/tameness/orientation-degree ledger | **PROVED EXACT / STANDARD KUMMER INPUT** |
| rank-two descent under simultaneous cubic inversion | **PROVED FORMALLY** |
| common-base \(\mathbf F_7(T)\) leverage control (1.2)--(1.3) | **PROVED EXACT FROM LOCKED FORMULA** |
| scalar principal extraction \(P=C-S\) and inequality (8.4) | **PROVED EXACT FROM LOCKED SOURCE** |
| common relative complex (8.5) and invariant cancellation | **NOT CONSTRUCTED** |
| universal varying-place source complex | **NOT CONSTRUCTED** |
| absence of invariants after complete FFPS cleanup | **OPEN** |
| uniform Betti/conductor bound | **OPEN** |
| `CYSEL`, `WCADD106140`, or `WCKUM106140` | **OPEN / RH-BEARING** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made.

## 10. Reproduction

The producer performs three two-element cyclotomic sums and small row
reductions in \(\mathbf F_3^2\). The resource cap is 2,000 exact operations
and three seconds. It performs no finite-field or arithmetic-family sweep.

~~~powershell
python research/l-families/atlas/function_field/ffps_cyclic_sheaf_invariant_audit.py --check
python -O research/l-families/atlas/function_field/ffps_cyclic_sheaf_invariant_audit.py --check
python -m pytest -q tests/test_ffps_cyclic_sheaf_invariant_audit.py
python -O -m pytest -q tests/test_ffps_cyclic_sheaf_invariant_audit.py
python -m ruff check research/l-families/atlas/function_field/ffps_cyclic_sheaf_invariant_audit.py tests/test_ffps_cyclic_sheaf_invariant_audit.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_cyclic_sheaf_invariant_audit.py tests/test_ffps_cyclic_sheaf_invariant_audit.py
~~~

Regenerate the canonical JSON only by omitting `--check` from the first
command.
