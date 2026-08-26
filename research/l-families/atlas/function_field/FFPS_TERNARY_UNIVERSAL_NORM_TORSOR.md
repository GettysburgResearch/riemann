# Universal norm-torsor normal form for the ternary physical mask

Status: **exact varying-place degree-shell trace-complex and exact generic
invariant/conductor normal form for the minimal ternary mask; no full FFPS
owner/Boolean adapter, uniform pushed-forward Betti bound, `CYSEL`, RH, or
GRH theorem**

Bounded exact replay:
[`ffps_ternary_universal_norm_torsor.py`](ffps_ternary_universal_norm_torsor.py).
Canonical summary:
[`ffps_ternary_universal_norm_torsor.json`](ffps_ternary_universal_norm_torsor.json).

Frozen dependencies:

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_CYCLIC_SHEAF_INVARIANT_AUDIT.md` | `8b4559a54` | `d531ef36d314549072052cc5b1ae1762c11d00e2` | fixed-fibre physical Kummer adapter |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | honest cyclic endomorphism identity |
| `FFPS_RELATIVE_BOUNDARY_TRACE_TOWER_GATE.md` | `961603fd0` | `cc8b649848a2e7425989a553628d9c830f56f6d1` | universal cycle selector |
| `FFPS_EXACT_CYCLE_SELECTOR_MASS_NO_GO.md` | `691166b8c` | `d136159ea9f0fa41600e673dc2c6ef1a2ad2f10f` | forced exact-selector mass |

## 0. Outcome

Fix a prime power

\[
 q\equiv1\pmod 6
\tag{0.1}
\]

and two positive place degrees \(a,b\).  The minimal \(k=3,t=2\) physical
mask admits one exact trace-complex while the two closed places vary over
their entire squarefree degree shells.

The construction has four layers.

1. The universal degree-\(d\) etale algebra supplies a norm map.  Composing
   one fixed exact-order-six character of \(\mathbf F_q^\times\) with that
   norm gives the canonical exact-order-six character on every irreducible
   residue field \(\mathbf F_{q^d}\).
2. Four scalar norm-orientation double covers impose the four physical
   quadratic sectors.  Their total degree is \(16\), independent of \(a,b\).
3. On that cover, one cubic torsor carries the two faithful selected modes.
   Its regular pushforward has rank three.  Hence the full physical torsor
   package has rank \(48\), again independent of \(a,b\).
4. Tensoring with the exact rational \(a\)- and \(b\)-cycle selectors makes
   the trace vanish away from pairs of irreducible place polynomials.

At an irreducible pair this complex has exactly the ternary hard and selected
physical traces, with the physical coordinates \(Pc^2,Qd^2\), not owner
labels.  Thus the previously missing phrase “one varying-closed-place physical
torsor” can be replaced, **for one degree pair and the clean local
mask**, by the explicit norm-torsor below.

There is also a sharp complexity split:

\[
 \boxed{
 \begin{array}{c|c}
 \text{physical norm/Kummer layer}&
   \text{rank }48,\ \text{tame boundary support }6(a+b)\\
 \text{exact irreducibility layer}&
   \text{absolute rank mass }
   \displaystyle {2^{a+b-2}\over ab}.
 \end{array}}
\tag{0.2}
\]

So the Kummer geometry itself has bounded rank and only linear toric
ramification.  The exact full-\(S_a\times S_b\) cycle projector is the
exponential termwise bottleneck.  A scalable proof must keep that projector
assembled through a joint cancellation, replace it by a source-specific
selector, or avoid it through a prime-polynomial trace formula.  Expanding
the exact selector into hooks and estimating them separately cannot work.

This is not the full FFPS complex.  Owners, both native Boolean sums, the
source-selected Artin--Schreier phases, shared incidence, Wick cleanup, and
the final signed conductor recombination have not been transported to this
base.

## 1. Universal closed-place algebra and canonical norm lift

Let

\[
 B_d=\operatorname{Spec}
 \mathbf F_q[c_1,\ldots,c_d,\Delta^{-1}]
\tag{1.1}
\]

parameterize monic squarefree polynomials

\[
 F_d(T)=T^d+c_1T^{d-1}+\cdots+c_d.
\]

The universal root algebra

\[
 A_d=\mathcal O_{B_d}[T]/(F_d)
\tag{1.2}
\]

is finite etale of degree \(d\).  Put

\[
 \mathcal T_d=\operatorname{Res}_{A_d/B_d}\mathbf G_m,
 \qquad
 N_d:\mathcal T_d\longrightarrow\mathbf G_m.
\tag{1.3}
\]

Choose an exact-order-six character

\[
 \xi:\mathbf F_q^\times\longrightarrow\mu_6,
 \qquad \theta=\xi^2.
\tag{1.4}
\]

For an irreducible \(F_d\), its fibre is \(k_F=\mathbf F_{q^d}\), and

\[
 \xi_d=\xi\circ N_{k_F/\mathbf F_q}
\tag{1.5}
\]

has exact order six because the norm is surjective.  If a physical value is
in a fixed quadratic sector,

\[
 X/u=s^2,
\]

then

\[
 \boxed{
 \xi_d(X/u)
 =\xi(N(s)^2)
 =\theta(N(s)).}
\tag{1.6}
\]

This is precisely the root-orientation identity used by the ternary mask.
It is canonical over the varying degree shell: no abstract identification
of different residue-field character groups is required.

When \(a=b\), remove the resultant diagonal from \(B_a\times B_b\); more
generally remove the common-root resultant.  Denote the resulting clean
place-pair base by \(B_{a,b}^{\circ}\).  This ensures that the two universal
etale algebras represent distinct coprime place polynomials.  It does not
force either polynomial to be irreducible; that is the separate Frobenius
cycle condition in Section 4.

## 2. A degree-16 norm-orientation cover

Over \(B_{a,b}^{\circ}\), take two sector-anchor unit coordinates and four
physical unit coordinates

\[
 u_X\in\mathcal T_a,\qquad u_Y\in\mathcal T_b,
 \qquad
 X_1,X_2\in\mathcal T_a,
 \qquad
 Y_1,Y_2\in\mathcal T_b.
\tag{2.1}
\]

The labels stand for the actual physical values \(Pc^2\) and \(Qd^2\) in
the two atoms of the quadratic covariance.  The anchors \(u_X,u_Y\) are
variables, not silently chosen nonsquare constants in \(\mathbf F_q\).  This
distinction is necessary in even extension degree, when a base-field
nonsquare becomes a square in the residue field.  A native source adapter
must supply these anchors from its sector decomposition; this packet does not
identify them with owner labels.

Define the norm-orientation cover \(p:\widetilde{\mathcal P}
\to\mathcal P\) by

\[
 \begin{aligned}
 h_{X,1}^2&=N_a(X_1/u_X),&
 h_{X,2}^2&=N_a(X_2/u_X),\\
 h_{Y,1}^2&=N_b(Y_1/u_Y),&
 h_{Y,2}^2&=N_b(Y_2/u_Y).
 \end{aligned}
\tag{2.2}
\]

On the unit torus this is finite etale of degree \(2^4=16\), regardless of
the place degrees.

At an irreducible \(\mathbf F_q\)-point, the quadratic character on
\(\mathbf F_{q^d}^\times\) is exactly the norm lift of the quadratic
character on \(\mathbf F_q^\times\):

\[
 \eta_q(N_d(x))
 =(N_d(x))^{(q-1)/2}
 =x^{(q^d-1)/2}
 =\eta_{q^d}(x),
\]

Thus \(X/u\) is a square in \(\mathbf F_{q^d}\) exactly when
\(N_d(X/u)\) is a square in \(\mathbf F_q\), and the normalized trace of the
four covers in (2.2) is

\[
 {1\over16}\operatorname{Tr}(p_*\mathbf 1)
 =\prod_{Z\in\{X_1,X_2,Y_1,Y_2\}}
   \mathbf1_{Z\text{ lies in its prescribed quadratic sector}}.
\tag{2.3}
\]

Equation (2.3) is only asserted after the irreducibility selector.  On a
reducible etale algebra, “total norm square” need not mean square in every
factor.  That causes no trace error: the exact cycle selector makes every
such rational fibre contribute zero.

This scalar norm cover is much smaller than adjoining a square root in each
of the geometric root coordinates.  It is allowed because the cubic
orientation is insensitive to the sign of a square root and depends only on
its norm, as (1.6) proves.

## 3. The universal ternary torsor and relative projector

Choose a relative alignment \(\varepsilon\in\{+1,-1\}\) and put

\[
 U=
 {h_{X,1}\over h_{X,2}}
 \left({h_{Y,1}\over h_{Y,2}}\right)^\varepsilon.
\tag{3.1}
\]

Form the cubic Kummer torsor

\[
 \pi:\mathcal Z\longrightarrow\widetilde{\mathcal P},
 \qquad z^3=U,
\tag{3.2}
\]

and let \(\mathcal H=\pi_*E\), where the coefficient field contains
\(\mu_3\).  If \(\Pi_0,\Pi_1,\Pi_2\) are its three deck idempotents, the
two-point ternary mask has

\[
 \boxed{
 \mathsf C=\Pi_0+{1\over4}(\Pi_1+\Pi_2),
 \qquad
 \mathsf S={1\over4}(\Pi_1+\Pi_2),
 \qquad
 \mathsf C-\mathsf S=\Pi_0.}
\tag{3.3}
\]

The coefficient \(1/4\) is the forced value
\(|\gamma_1|^2=|\gamma_2|^2\) for every retained two-subset of \(\mu_3\).
These are honest endomorphisms of \(\mathcal H\), not fractional object
multiplicities.

Normalize the finite pushforward by \(1/16\), and tensor every term with the
same place selector and the same later source complex.  Additivity gives

\[
 \boxed{
 {1\over16}Rp_!(\mathcal H,\mathsf C)
 -{1\over16}Rp_!(\mathcal H,\mathsf S)
 ={1\over16}Rp_!(\operatorname{im}\Pi_0).}
\tag{3.4}
\]

At an irreducible rational place pair, the right side is exactly the
principal local trace restricted to the same four physical sectors.  The
left side is the ternary hard current minus its selected Kummer modes.  Thus
all selected constant resonances cancel before an absolute value is taken.

Equation (3.4) is an exact **degree-shell local physical adapter**.  It is not
yet the native FFPS identity \(P=C-S\), because the source coefficients and
all cleanups listed in Section 7 have not been realized as one common
equivariant functor on this base.

## 4. Exact irreducible-place selection

The etale root cover of \(B_d\) has geometric monodromy \(S_d\).  Let
\(\mathrm{Std}_d\) be its standard local system and put

\[
 \mathcal Q_d={1\over d}\Lambda_{-1}(\mathrm{Std}_d)
 \quad\text{in }K_0\otimes\mathbf Q.
\tag{4.1}
\]

Its Frobenius trace is one on \(d\)-cycles and zero on every other cycle
type.  Consequently

\[
 \mathcal Q_{a,b}=\mathcal Q_a\boxtimes\mathcal Q_b
\tag{4.2}
\]

selects exactly pairs of irreducible place polynomials.  Tensor (3.4) with
the pullback of (4.2).  Equations (2.3), (3.3), and (4.1) then prove the
claimed trace identity on every \(\mathbf F_q\)-point of the full
squarefree degree-shell base: reducible place rows vanish, wrong physical
sectors vanish, and the remaining trace is the exact ternary local mask.

The price is binding.  The unique hook expansion gives

\[
 \|\mathcal Q_d\|_{\rm rank}={2^{d-1}\over d},
\]

so the canonical product selector has

\[
 \boxed{
 \|\mathcal Q_{a,b}\|_{\rm rank}
 ={2^{a+b-2}\over ab}.}
\tag{4.3}
\]

The physical package before this tensor has ranks

\[
 \boxed{
 \operatorname{rank}p_*\mathcal H=48,
 \quad
 \operatorname{rank}p_*(\operatorname{im}\Pi_1\oplus
                         \operatorname{im}\Pi_2)=32,
 \quad
 \operatorname{rank}p_*(\operatorname{im}\Pi_0)=16.}
\tag{4.4}
\]

These product masses are forced inside the universal local package, not just
costs of one presentation.  At the generic point the four square classes in
(2.2) are independent: a physical-coordinate boundary valuation detects
each one separately.  After adjoining their roots, the valuation of \(U\)
at such a boundary is \(\pm1\), so the cubic cover is still nontrivial.  The
physical deck group is therefore

\[
 G_{\rm phys}=C_2^4\times C_3,
 \qquad |G_{\rm phys}|=48.
\tag{4.5}
\]

A sign change in the four \(h\)-coordinates multiplies \(U\) by a sign and
lifts by the same sign on \(z\), while \(C_3\) multiplies \(z\) by a cubic
root.  These actions commute.  The norm equations are symmetric in the
universal roots, so \(S_a\times S_b\) acts trivially on
\(G_{\rm phys}\).  Conversely, the physical deck group is generated by
loops inside a geometric fibre of the place base, and the identity section
\(X_i=u_X,Y_i=u_Y\), with \(h_i=z=1\), splits the root monodromy from it.
Thus the generic finite-monodromy quotient is the direct product

\[
 \boxed{(S_a\times S_b)\times G_{\rm phys}.}
\tag{4.6}
\]

Irreducible characters of a direct product are external tensor products.
Hence tensoring the unique hook expansion of \(\mathcal Q_{a,b}\) with an
honest \(G_{\rm phys}\)-representation \(W\) forces absolute rank mass

\[
 \boxed{
 \|\mathcal Q_{a,b}\boxtimes W\|_{\rm rank}
 ={2^{a+b-2}\over ab}\dim W.}
\tag{4.7}
\]

Taking \(W\) to be the regular, selected, or relative physical
representation gives exactly the three masses obtained from (4.3) and
(4.4).  Therefore no cancellation internal to the bounded norm/Kummer layer
can make the exact cycle selector affordable.

Here (4.7) is the support/semisimple rank mass of the **unnormalized honest**
representation (W). The factors (1/16) in (3.4) and (1/4) in (3.3)
are trace normalizations and endomorphism weights, not claims of fractional
object multiplicity.

This local direct-product no-go does **not** rule out cancellation after
tensoring with the complete owner/Boolean/incidence FFPS source complex.  Such
a complex need not be an honest positive \(G_{\rm phys}\)-representation,
may impose additional relations, and is not constructed here.  Nor does the
argument rule out a weaker or source-specific place selector.

## 5. Exact invariant criterion

Let \(Z\) be a geometrically integral source stratum of
\(\widetilde{\mathcal P}\) on which \(U\) is a unit.  The two selected lines
are the faithful cubic Kummer systems attached to \(U\) and \(U^2\).
Therefore

\[
 \boxed{
 \dim(\mathcal M_1\oplus\mathcal M_2)^{
   \pi_1^{\rm geom}(Z)}
 =
 \begin{cases}
 2,&U\in K(Z)^{\times3},\\
 0,&U\notin K(Z)^{\times3}.
 \end{cases}}
\tag{5.1}
\]

Over a geometric splitting cover of the two universal etale algebras,

\[
 N_a(X_1/X_2)N_b(Y_1/Y_2)^\varepsilon
 =\prod_{i=1}^a{x_{1,i}\over x_{2,i}}
  \prod_{j=1}^b
   \left({y_{1,j}\over y_{2,j}}\right)^\varepsilon.
\tag{5.2}
\]

Each exponent is \(\pm1\).  A boundary valuation of \(U\) is therefore
\(\pm1\) on the normalized orientation cover, so \(U\) is not a cube in the
generic function field.  The generic selected invariant multiplicity is
zero for every \(a,b\).

The criterion is exactly the old fixed-fibre criterion, now on the
universal norm cover.  It also explains a useful descent refinement.  If one
forgets the square orientation and writes

\[
 F=U^2=N_a(X_1/X_2)N_b(Y_1/Y_2)^\varepsilon,
\]

then the two descended physical lines have characters \(\xi(F)\) and
\(\xi^2(F)\).  On an arbitrary physical stratum their invariant multiplicity
is

\[
 \boxed{
 \mathbf1_{F\in K(Z)^{\times6}}
 +\mathbf1_{F\in K(Z)^{\times3}}.}
\tag{5.3}
\]

It can equal one on a cube-but-not-sixth-power stratum.  On the physical
quadratic-sector cover, \(F=U^2\); since squaring is invertible modulo cubes,
“\(F\) is a cube” is equivalent to “\(U\) is a cube,” which then makes
\(F\) a sixth power.  Hence (5.3) collapses back to the \(0/2\) law (5.1).
This separates physical descent from sector-conditioned geometry without
changing the source trace.

For a connected monomial stratum, (5.1) is again finite linear algebra: the
exponent row of \(U\) must lie in the relation-row span modulo three.  No
monodromy classification is required.

## 6. Conductor normal form

After geometric splitting, compactify each of the
\(3a+3b\) multiplicative root coordinates (four physical variables and two
sector anchors) by \(\mathbf P^1\).  The reduced
toric boundary has

\[
 \boxed{2(3a+3b)=6(a+b)}
\tag{6.1}
\]

geometric divisors.  The four norm-orientation equations have odd valuation
along every physical boundary and along the relevant anchor boundaries.  The
cubic ratio itself cancels the anchor exponents, but the sector projector
still carries their quadratic ramification.  All orientation and cubic
ramification is tame, so every Swan conductor is zero, and there is no
ramification away from this boundary and the already removed
discriminant/resultant loci.

The physical torsor rank is bounded by (4.4).  A safe total tame-conductor
bound for the rank-48 regular package on the split toric compactification is

\[
 \boxed{
 \operatorname{cond}_{\rm toric}(p_*\mathcal H)
 \le48\cdot6(a+b)=288(a+b).}
\tag{6.2}
\]

This is deliberately a rank-times-support bound, not an assertion that every
constituent ramifies maximally.  It proves the needed qualitative normal
form:

\[
 \boxed{
 \text{bounded physical rank, tame Swan zero, linear degree-shell
 boundary support}.}
\tag{6.3}
\]

The discriminant and resultant opens add their own boundary under a global
compactification of \(B_{a,b}^{\circ}\).  Their degrees grow polynomially in
\(a,b\), and their pushed-forward Betti contribution is not bounded here.
Most importantly, tensoring with \(\mathcal Q_{a,b}\) reintroduces the
exponential absolute rank mass (4.3) if its hook constituents are estimated
separately.  Formula (6.2) must not be quoted as the conductor of the entire
irreducibility-selected FFPS complex.

## 7. Exact remaining gate

The construction closes the following local geometric chain:

```text
varying squarefree place polynomials of fixed degrees (a,b)
  -> universal finite etale algebras
  -> canonical norm-lifted order-six physical characters
  -> degree-16 norm-orientation cover
  -> one rank-three cubic torsor
  -> exact hard-selected relative projector
  -> exact rational irreducible-place selector.
```

What remains is not another fixed-fibre Kummer calculation.  A native FFPS
theorem must construct a single common pushforward carrying:

1. both complete Boolean source sums;
2. the owner/core factorization and the actual \(Pc^2,Qd^2\) maps;
3. both source-selected Artin--Schreier phases before squaring;
4. common removal of literal atoms, equal products, roots, shared incidence,
   and every constant/resonant subquotient;
5. the cycle selector without paying (4.3) term by term;
6. the signed varying-conductor recombination before the outer absolute
   value.

The most economical next target is therefore an equality in the
Grothendieck group **after** tensoring the full source complex with
\(\mathcal Q_{a,b}\), followed by simplification before any Betti norm is
taken.  Failing that, use a prime-polynomial explicit formula or a
source-specific factorization-type quotient.  The exact full-cycle
semisimple selector has already been optimized and is exponentially too
large.

Even if that categorical adapter is built, Deligne gives only a trace bound
with the resulting total Betti number.  A uniform subpower estimate, the
number-field analogue, and principal individualization are independent
analytic gates.

## 8. Proof ledger

| statement | grade |
|---|---|
| universal squarefree algebra and norm map (1.1)--(1.3) | **STANDARD EXACT CONSTRUCTION** |
| canonical order-six norm lift and physical identity (1.5)--(1.6) | **PROVED EXACT** |
| degree-16 norm-sector cover and irreducible-fibre trace (2.2)--(2.3) | **PROVED EXACT** |
| universal cubic torsor and endomorphism identity (3.2)--(3.4) | **PROVED EXACT** |
| exact irreducible-place trace selection (4.1)--(4.2) | **PROVED EXACT IN `K_0 tensor Q`** |
| bounded physical ranks (4.4) | **PROVED EXACT** |
| invariant criteria (5.1), (5.3) | **PROVED BY KUMMER THEORY** |
| generic invariant multiplicity zero | **PROVED BY A BOUNDARY VALUATION** |
| tame linear toric support and bound (6.1)--(6.2) | **PROVED FOR THE PHYSICAL TORSOR PACKAGE** |
| exact selector termwise mass (4.3) | **PROVED / IMPORTED FROM THE LOCKED NO-GO** |
| direct-product monodromy and forced local product mass (4.5)--(4.7) | **PROVED FOR THE UNIVERSAL NORM-TORSOR PACKAGE** |
| one universal clean local degree-shell mask complex | **CONSTRUCTED EXACTLY** |
| full owner/Boolean/phase FFPS source adapter | **NOT CONSTRUCTED** |
| cancellation of selector mass after the full source tensor | **OPEN / CENTRAL** |
| uniform pushed-forward Betti or signed trace estimate | **OPEN** |
| `CYSEL`, `WCADD106140`, `WCKUM106140`, RH, or GRH | **NOT PROVED** |

No external novelty or priority claim is made for universal norms, Kummer
torsors, or cycle selectors separately.  The project contribution is the
source-aware composition: it replaces the vague varying-place torsor gate by
an explicit bounded-rank object and isolates the exact-cycle projector as the
first unavoidable exponential term in the naive global assembly.

## 9. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_ternary_universal_norm_torsor.py --check
python -B -O research/l-families/atlas/function_field/ffps_ternary_universal_norm_torsor.py --check
python -B -m unittest tests.test_ffps_ternary_universal_norm_torsor
python -B -O -m unittest tests.test_ffps_ternary_universal_norm_torsor
python -B -m ruff check research/l-families/atlas/function_field/ffps_ternary_universal_norm_torsor.py tests/test_ffps_ternary_universal_norm_torsor.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_ternary_universal_norm_torsor.py tests/test_ffps_ternary_universal_norm_torsor.py
```

The replay checks exact rank, boundary, selector-mass, and character-exponent
normal forms for \(1\le a,b\le8\), plus prime-power base-field guards.  It
enumerates no finite field, polynomial, place, curve, source atom,
\(L\)-function, or zero.
