# Marked-place bifrobenius gluing gate for the native FFPS source

Status: **exact correction of the Adams factor axes, exact simultaneous-block
Frobenius theorem for the local Artin--Schreier/incidence constituents, and
exact crossed-core obstruction for the natural raw universal source; no full
native bifrobenius complex, absolute no-go after signed pushforward,
correspondence-level Adams theorem, uniform trace estimate, CYSEL, WCADD,
WCKUM, RH, or GRH theorem**

Bounded exact replay:
[ffps_marked_place_bifrobenius_gluing_gate.py](ffps_marked_place_bifrobenius_gluing_gate.py).
Canonical summary:
[ffps_marked_place_bifrobenius_gluing_gate.json](ffps_marked_place_bifrobenius_gluing_gate.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `L-106120` | `98af0db6e` | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | bilateral marked-place factor graph |
| `L-106131` | `98af0db6e` | `37722c3f36ec7d1681f34d4329a3795e5028f7ae` | Wick additive/Kummer decomposition |
| `L-106191` | `98af0db6e` | `85c4ef92ead7d8b235f9c195c3c0acd16d16030f` | centered double-incidence coordinate |
| `T-106140` | `98af0db6e` | `d5be8e376c88b63de0be19e0d9e8791624e99ae2` | signed global recombination discipline |
| `FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md` | `05da4d170` | `c79e52ebf0099fe416bc2c79dcb041cc21e025fb` | exact two-place Adams acceptance criterion |
| `FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md` | `9ced25bef` | `21645bdb609320cf176893aa589af7a17c741d9a` | clean external rank-\(48\) package |
| `FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md` | `e39031369` | `19939eb240ca6b2b6d5221954cec76fe0f5c4f9c` | internal phase-rank and one-axis no-go being scoped here |
| `FFPS_TERNARY_RELATIVE_CORRESPONDENCE_NORMAL_FORM.md` | `8192514ed` | `4ee3c50f3cce3e7aa2dbd901b93fd50b713ea4bb` | graph-shift escape and exact relative kernel |
| `FFPS_FROBENIUS_EXTENSION_TOWER_ALIASING.md` | `9c95eb368` | `3d16de5cf8b099b8348c470befcda6c6050aad9e` | extension-tower fidelity firewall |
| `FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md` | `5c9462064` | `e7cb9133bb6b57ddbb1c7f1e350f1d2d0af7bd1a` | literal physical coordinates and cleanup order |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | honest \(C-S=\Pi_0\) endomorphism |

The first four files are read at their frozen commit paths; they are not
present as live files on this exploration branch.

## 0. Corrected verdict

The clean ternary norm/Kummer package passes the separable two-place gate in
the closed-point Adams packet. The complete native owner/Boolean source does
not currently pass it. The reason, however, is subtler than the earlier
universal phase-rank verdict states.

For closed-point Adams, the two tensor factors are the two **marked places**

\[
 \ell=P^-(c),\qquad \rho=P^-(d),
\tag{0.1}
\]

not the phase variable versus the physical residue, and not the two atom
copies inside one square. Once the coordinates are grouped by marked place,

\[
 \begin{array}{c|c}
 \ell\text{-block}&(\ell,h,Y,Y'),\quad Y=Qd^2\bmod\ell\\
 \rho\text{-block}&(\rho,k,X,X'),\quad X=Pc^2\bmod\rho.
 \end{array}
\tag{0.2}
\]

The local Artin--Schreier line and centered incidence are ordinary Weil
objects under simultaneous Frobenius of the whole appropriate block. Their
large internal matrices do not prove large separation rank across the
\(\ell\mid\rho\) partition.

The real source obstruction is the crossed square

\[
 \boxed{
 \ell=P^-(c),\quad c\longmapsto X\bmod\rho;
 \qquad
 \rho=P^-(d),\quad d\longmapsto Y\bmod\ell.}
\tag{0.3}
\]

Each reduced core is selected on one marked-place side and evaluated on the
other. Common-core, coprimality, Boolean, shell, owner, and cleanup data add
further cross relations. The natural raw universal coefficient-space
construction therefore has no coordinatewise marked-place bifrobenius lift.

This is not an absolute nonexistence theorem for the class obtained **after**
the complete signed source pushforward. A virtual cancellation could erase
the obstructing supports before Adams extraction. No such common pushed-
forward class has been constructed.

## 1. The exact marked-place factor graph

Frozen `L-106120` gives one bilateral member

\[
 \mathcal W_{\ell,\rho;h,k}
 =\sum_{P,Q,c,d}
 \overline {A_{P,c}}B_{Q,d}
 e_\ell(-hQd^2)e_\rho(kPc^2),
\tag{1.1}
\]

with (0.1) and with all common-core, source-shell, Boolean, owner, carrier,
renewal, and coprimality labels retained. Put

\[
 X=Pc^2\bmod\rho,\qquad Y=Qd^2\bmod\ell.
\tag{1.2}
\]

The correct Adams grouping is

~~~text
ell marked-place block                 rho marked-place block
----------------------                 ----------------------
ell, h                                 rho, k
Y=Q d^2 mod ell                        X=P c^2 mod rho
Y,Y' centered incidence                X,X' centered incidence
ell-side orientation/Kummer data       rho-side orientation/Kummer data

        ^ ell=P^-(c) crosses     rho=P^-(d) crosses ^
        |                                           |
        +---- c also feeds X      d also feeds Y ---+
~~~

For fixed source labels the two displayed phases tensor. The failure occurs
when the varying source labels and their selectors are transported to one
universal marked-place base.

## 2. Correction theorem: internal matrix rank is not Adams separation rank

Let \(A,B\) be finite sets and let

\[
 H_A:A\times A\to E,\qquad H_B:B\times B\to E
\]

be nonzero kernels over a characteristic-zero field. Define

\[
 K((a,a'),(b,b'))=H_A(a,a')H_B(b,b').
\tag{2.1}
\]

### Theorem 2.1

Across the marked-block partition

\[
 (A\times A)\mid(B\times B),
\]

the kernel (2.1) has separation rank one, regardless of the two internal
matrix ranks

\[
 \operatorname {rank}(H_A),\qquad\operatorname {rank}(H_B).
\tag{2.2}
\]

**Proof.** Flatten \(H_A\) and \(H_B\) as functions on the two marked-place
blocks. Equation (2.1) is their single outer product. \(\square\)

Apply this to

\[
 H_{Q,m}=QI_m-J_m.
\tag{2.3}
\]

The earlier exact theorem

\[
 \operatorname {rank}H_{Q,m}
 =\begin{cases}m,&m<Q,\\Q-1,&m=Q\end{cases}
\tag{2.4}
\]

remains correct. It measures rank between the two atom-residue coordinates
inside one marked-place block. It does not by itself measure external rank
between the \(\ell\)- and \(\rho\)-blocks.

The replay takes internal matrices of ranks two and three. Their bilateral
marked-block table has separation rank one exactly. Thus the implication

\[
 \text{large internal }QI-J\text{ rank}
 \Longrightarrow
 \text{large marked-place Adams separation rank}
\tag{2.5}
\]

is false.

This correction does not construct the complete source external product.
It identifies which existing calculation cannot refute one.

## 3. Simultaneous marked-block Frobenius

Consider the local Artin--Schreier function \(hY\) on one marked-place
block. Simultaneous \(q\)-Frobenius gives

\[
 (h,Y)\longmapsto(h^q,Y^q),\qquad
 h^qY^q=(hY)^q.
\tag{3.1}
\]

On every finite extension, additive trace is Frobenius invariant:

\[
 \operatorname {Tr}((hY)^q)=\operatorname {Tr}(hY).
\tag{3.2}
\]

Hence \(\mathcal L_\psi(hY)\) has the ordinary Weil structure of the whole
\(\ell\)-block. Likewise \(\mathcal L_\psi(kX)\) has the ordinary Weil
structure of the whole \(\rho\)-block.

The one-axis pullbacks

\[
 hY\longmapsto h^qY,\qquad hY\longmapsto hY^q
\tag{3.3}
\]

need not be geometrically isomorphic to the original line. That exact
predecessor no-go is retained. Equation (3.3), however, is not the
marked-place partial Frobenius required by double Adams, because \(h\) and
\(Y\) belong to the same marked-place block.

The same distinction applies to the centered diagonal. Simultaneous
Frobenius sends

\[
 Y-Y'=0
 \quad\longmapsto\quad
 Y^q-(Y')^q=(Y-Y')^q=0,
\tag{3.4}
\]

so the reduced diagonal support is preserved. Moving \(Y\) alone gives the
distinct graph \(Y^q=Y'\). Again, the latter is a valid one-axis support
calculation but not the Frobenius of the complete \(\ell\)-block.

Therefore:

\[
 \boxed{
 \text{local AS and incidence constituents do not themselves obstruct
 marked-place partial Frobenius.}}
\tag{3.5}
\]

Their source maps still depend on variables crossing the marked-place
partition. Section 4 is where the actual obstruction appears.

## 4. Crossed-core allocation trilemma

Let \(\mathcal C_d\) be the coefficient space of monic degree-\(d\)
polynomials and consider the universal divisor incidence

\[
 \mathcal I_d
 =\{(\alpha,F)\in\mathbf A^1\times\mathcal C_d:F(\alpha)=0\}.
\tag{4.1}
\]

Total Frobenius moves both the root and the coefficients and preserves this
incidence. Root-only Frobenius does not. In degree one, write

\[
 F_A(T)=T-A.
\]

The incidence is the diagonal \(\alpha=A\). Pulling only the root coordinate
by Frobenius changes it to

\[
 \alpha^q=A,
\tag{4.2}
\]

a distinct geometric support. Pulling only the coefficient coordinate gives

\[
 \alpha=A^q,
\tag{4.3}
\]

which is distinct as well. Constructible complexes with distinct generic
supports cannot be isomorphic.

This gives an exact trilemma for the native core \(c\).

### Case 1: \(c\) belongs to the \(\rho\)-block

Then \(X=Pc^2\bmod\rho\) is local to that block, but the condition

\[
 \ell=P^-(c)
\]

contains the universal incidence \(\ell\mid c\) across the blocks.
The \(\ell\)-partial Frobenius moves its support as in (4.2).

### Case 2: \(c\) belongs to the \(\ell\)-block

Then the least-place selector can be local, but evaluation of \(c\) at
\(\rho\) crosses the blocks. The native coprimality conditions include the
corresponding nonincidence \(\rho\nmid c\); its open support is moved by
\(\rho\)-partial Frobenius just as the complement of (4.2) is moved.

### Case 3: duplicate \(c\)

Putting one copy in each block requires the equality

\[
 c_\ell=c_\rho.
\tag{4.4}
\]

This is a diagonal across the marked blocks. One-sided Frobenius moves it to
a Frobenius graph, so it supplies no coordinatewise bifrobenius lift.

The same three cases apply to \(d\), with the roles reversed. The shared
common core \(g\) supplies another equality-diagonal instance. Coprimality,
source shells, Boolean incidence, owner/core overlaps, equal products, and
resonant cleanup add further coupled supports.

Thus:

\[
 \boxed{
 \text{the natural raw universal coefficient-space source has no
 coordinatewise marked-place bifrobenius lift.}}
\tag{4.5}
\]

The adjective **natural raw** is load-bearing. The theorem considers the
literal source graph before a signed derived pushforward. It does not rule
out cancellation of these supports in the final virtual class.

## 5. Frozen-source escape and its cost

At a fixed finite horizon, freeze every source polynomial over
\(\mathbf F_q\) as an individual zero-dimensional label. Frobenius fixes each
label, and the marked-place residue coordinates can then receive their
simultaneous block Frobenii. This supplies a formal source-specific
presentation.

It is not a scalable compression. It contains at least one summand per
retained source label. On the clean prime-core panel

\[
 c=\ell,
\tag{5.1}
\]

the least-place incidence contains an identity submatrix indexed by the
retained degree-\(a\) places. If every degree-\(a\) row is retained, its rank
is

\[
 I_q(a)={1\over a}\sum_{e\mid a}\mu(e)q^{a/e}.
\tag{5.2}
\]

This is exponential in \(a\), up to the factor \(a^{-1}\). The replay records

\[
 I_3(a)=3,3,8,18,48,116
 \qquad(1\le a\le6).
\tag{5.3}
\]

Equation (5.2) is a conditional complexity lower bound for a presentation
retaining the complete identity panel. It is **not** an occupancy theorem
for the final live Boolean/owner image. Proving that the live source retains
all, a positive proportion, or only subpower-many such cells is a separate
source theorem.

The safe dichotomy is:

\[
 \begin{array}{c|c}
 \text{universal geometric coefficients}&
   \text{crossed incidence obstructs the natural partial lift}\\
 \text{frozen }\mathbf F_q\text{ source labels}&
   \text{partial lift exists formally but pays source-cardinality rank}.
 \end{array}
\tag{5.4}
\]

## 6. The minimal bifrobenius gluing datum

The complete source need not be external term by term if its full
pushforward carries a stronger bivariate Weil structure. The minimal object
needed for the exact Adams theorem is a common class

\[
 \mathcal K_{\rm nat}
\tag{6.1}
\]

on the ordered marked-place base, together with the following data.

1. Two commuting partial Frobenius structures

   \[
   \varphi_\ell^*\mathcal K_{\rm nat}\simeq\mathcal K_{\rm nat},
   \qquad
   \varphi_\rho^*\mathcal K_{\rm nat}\simeq\mathcal K_{\rm nat}.
   \tag{6.2}
   \]

2. The cocycle equating their product with ordinary total Frobenius.
3. For every pair of independent extension degrees, equality of the
   bivariate trace with the literal native owner/Boolean/Artin--Schreier
   source, including all normalizations.
4. Common equivariant hard and selected endomorphisms realizing
   \(C-S=\Pi_0\) on this same class.
5. Common equivariant cones for literal atoms, equal products, root pieces,
   owner/core overlap, shared incidence, and every constant or resonant
   constituent.
6. The signed varying-conductor recombination before any norm, triangle
   inequality, or absolute value.
7. Uniform complexity bounds for every partial Adams transform after all
   required pushforwards.

With these data the exact predecessor formula applies:

\[
 abP_{a,b}(\mathcal K_{\rm nat})
 =\sum_{e\mid a}\sum_{f\mid b}
 \mu(e)\mu(f)
 A_{a/e,b/f}
 (\psi_1^e\psi_2^f\mathcal K_{\rm nat}).
\tag{6.3}
\]

No current packet supplies (6.1)--(6.2) for the complete native source.
Base-field trace agreement is not enough: formula (6.3) requires the whole
independent extension tower and the Adams powers of every stalk eigenvalue.

## 7. Conditional signed-pushforward frontier

The crossed-support theorem applies before the complete signed pushforward.
An equality in a Grothendieck group can cancel objects with the same support,
Tate shift, arithmetic Frobenius scalar, and source coefficient. Therefore
the following possibility remains logically open:

\[
 \text{raw crossed source}
 \longrightarrow
 \text{common signed pushforward and cleanup}
 \longrightarrow
 \mathcal K_{\rm nat}\text{ with bifrobenius descent}.
\tag{7.1}
\]

The exact cyclic endomorphism identity

\[
 C-S=\Pi_0
\tag{7.2}
\]

survives every genuinely common equivariant functor. It cannot construct the
functor or prove that the crossed phase, owner, and cleanup constituents
match. The current state is

\[
 \boxed{
 \begin{array}{ll}
 \text{clean norm/Kummer package:}&\text{separable Adams gate passed};\\
 \text{natural raw native source:}&\text{coordinatewise bifrobenius obstructed};\\
 \text{complete signed pushforward:}&\text{unbuilt and undecided}.
 \end{array}}
\tag{7.3}
\]

It would be incorrect either to apply closed-point Adams to the native source
now or to report a categorical impossibility theorem after every possible
signed pushforward.

## 8. Correspondence escape

The natural alternative is not to identify a diagonal with its partial
Frobenius pullback. Retain every resulting graph as a correspondence.
For one residue coordinate, the support orbit begins

\[
 \Gamma_n:\quad y=x^{q^n},\qquad n\ge0.
\tag{8.1}
\]

These supports are distinct at every bounded depth, while a formal divisor
grid contains only

\[
 2^{\omega(a)+\omega(b)}
\tag{8.2}
\]

nonzero Möbius slots. This makes a graph-shift description sparse even when
the point-function matrices have large rank.

Support-symbol sparsity is not yet a closed-point formula. A valid successor
category must provide:

- composition laws for the two graph correspondences;
- trace maps at independent extension levels;
- Adams powering of the complete stalk eigenvalue packets;
- the Tate scalar in every centered background;
- common hard/selected projectors and cleanup cones;
- exact equal-place corrections;
- a uniform Betti/conductor or other trace-complexity ledger.

The extension-tower aliasing packet proves why total graph counts or a few
power traces cannot replace these data. It also shows that a compact
correspondence may exist even when its literal point-function matrix has
exponential dimension. Thus the correspondence route is a real open escape,
not a theorem already supplied by the graph-support notation.

## 9. Consequence for the existing front door

The following predecessor statements remain valid:

- the exact \(QI-J\) internal rank theorem;
- failure of an Artin--Schreier line under Frobenius of only one of its two
  local coordinates;
- failure of a diagonal under Frobenius of only one atom coordinate;
- the clean norm/Kummer Adams compression;
- the graph-support orbit and extension-tower aliasing theorems.

The interpretation requiring correction is:

\[
 \text{those internal/one-axis facts alone refute marked-place Adams}.
\]

They do not. The source-faithful obstruction is the crossed selector and
evaluation graph (0.3), together with the shared native source relations.

Accordingly the safe front-door description is:

> Termwise bounded-rank externalization of the natural complete source is
> obstructed by crossed marked-place/source incidence. The local phase and
> centered-incidence constituents are ordinary Weil objects inside the
> correct marked-place blocks. A bifrobenius structure after the complete
> signed pushforward, or a correspondence-level replacement, remains open.

## 10. Proof ledger

| statement | grade |
|---|---|
| frozen native factor graph (0.1)--(1.2) | **IMPORTED EXACT** |
| internal \(QI-J\) rank | **IMPORTED / RETAINED EXACT** |
| block outer-product correction theorem | **PROVED EXACT** |
| refutation of internal-rank implication (2.5) | **PROVED BY AN EXACT FINITE CONTROL AND THE GENERAL OUTER-PRODUCT IDENTITY** |
| simultaneous marked-block Artin--Schreier Weil structure | **PROVED FORMALLY BY FROBENIUS INVARIANCE OF ADDITIVE TRACE** |
| simultaneous marked-block diagonal preservation | **PROVED BY (3.4)** |
| predecessor one-axis no-go | **RETAINED AT ITS NARROWER AXES** |
| universal divisor-incidence support shift | **PROVED EXACT** |
| crossed-core allocation trilemma | **PROVED FOR THE NATURAL RAW UNIVERSALIZATION** |
| frozen-label finite-horizon escape | **PROVED FORMALLY** |
| identity-panel rank \(I_q(a)\) | **PROVED CONDITIONALLY ON RETAINING THAT PANEL** |
| clean ternary external Adams package | **IMPORTED PROVED EXACT** |
| full native external product | **NOT CONSTRUCTED** |
| full native commuting partial Frobenii | **NOT CONSTRUCTED** |
| absolute no-go after complete signed pushforward | **NOT PROVED** |
| correspondence-level closed-point Adams theorem | **NOT CONSTRUCTED** |
| uniform Betti/conductor or signed trace estimate | **NOT PROVED** |
| CYSEL, WCADD, WCKUM, RH, or GRH | **NOT PROVED** |

No external novelty or priority is claimed for partial Frobenius, universal
divisor incidence, or Adams operations separately. The project-specific
result is the source-axis audit and the exact crossed-core gluing gate.

## 11. Bounded replay

~~~text
python -B research/l-families/atlas/function_field/ffps_marked_place_bifrobenius_gluing_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_marked_place_bifrobenius_gluing_gate.py --check
python -B -m unittest tests.test_ffps_marked_place_bifrobenius_gluing_gate
python -B -O -m unittest tests.test_ffps_marked_place_bifrobenius_gluing_gate
python -B -m ruff check research/l-families/atlas/function_field/ffps_marked_place_bifrobenius_gluing_gate.py tests/test_ffps_marked_place_bifrobenius_gluing_gate.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_marked_place_bifrobenius_gluing_gate.py tests/test_ffps_marked_place_bifrobenius_gluing_gate.py
~~~

The replay performs exact rational elimination only on internal matrices of
sizes two and three and on one \(4\)-by-\(9\) marked-block outer product. It
evaluates the Möbius formula for \(I_3(a)\) through degree six and records six
formal graph-support signatures. It enumerates no finite-field element,
polynomial, closed place, source atom, point, curve, \(L\)-function, or zero.
