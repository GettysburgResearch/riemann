# FFPS graph Kummer character spectrum

Status: **exact finite graph/Fourier theorem and bounded replay; not an FFPS
source realization or varying-conductor estimate**

Replay:
[`ffps_graph_kummer_character_spectrum.py`](ffps_graph_kummer_character_spectrum.py)

## 0. Outcome

The graph construction in the checkerboard curve model has a complete
character spectrum, not only a distinguished top character.

Let `Gamma=(V,E)` be a finite simple graph without isolated vertices.  Attach
a distinct monic irreducible `P_v` of one common degree `e` to every vertex,
orient each edge, and put

\[
f_{uv}=P_u/P_v.
\]

An edge subset `x in F_2^E` indexes the formal tensor character

\[
\mathcal L_x
=\bigotimes_{a\in x}\mathcal L_\kappa(f_a).
\]

Its geometric branch divisor is controlled by the binary incidence boundary

\[
\partial:\mathbf F_2^E\longrightarrow\mathbf F_2^V.
\]

The exact sequence

\[
0\longrightarrow Z_1(\Gamma;\mathbf F_2)
\longrightarrow\mathbf F_2^E
\xrightarrow{\partial}
\operatorname{im}\partial
\longrightarrow0
\tag{0.1}
\]

gives

\[
\boxed{
\dim\ker\partial
=\beta(\Gamma)
=|E|-|V|+c(\Gamma).}
\tag{0.2}
\]

Every admissible branch pattern has exactly `2^beta` edge-subset preimages.
In particular,

\[
\boxed{
\#\{\text{nonzero invariant edge modes}\}=2^\beta-1.}
\tag{0.3}
\]

For a connected graph on `v` vertices, all even vertex subsets are
admissible.  Therefore the number of modes ramified at `2r` degree-`e`
vertices is

\[
\boxed{
N_{2r}=2^\beta\binom{v}{2r},
\qquad 0\le r\le\lfloor v/2\rfloor.}
\tag{0.4}
\]

This spectrum depends only on `v` and `|E|`, not on graph topology.  For a
tree, `beta=0`, so `partial` is a bijection from edge subsets to even vertex
subsets.  Changing the tree only relocates the distinguished top mode
`x=E`: it maps to the odd-degree vertex set of that tree.  A path places this
mode in the smallest nonconstant stratum `2r=2`; another tree generally
places it higher.  The complete multiset (0.4) is unchanged.

Finally, for any selected Fourier subspace `W <= F_2^E`,

\[
\boxed{
\#\{0\ne w\in W:\mathcal L_w\text{ invariant}\}
=2^{\dim(W\cap Z_1)}-1.}
\tag{0.5}
\]

Thus a selected mask has no invariant mode exactly when

\[
\boxed{
W\cap Z_1=0
\quad\Longleftrightarrow\quad
\partial|_W\text{ is injective}.}
\tag{0.6}
\]

Equation (0.6) is the graph **mask transversality criterion**.

## 1. Formal Fourier modes versus geometric lines

The word `mode` is load-bearing.  The `2^|E|` edge subsets are characters of
the formal product of the edgewise quadratic pushforwards.  If the edge
squareclasses are dependent, several formal modes pull back to the same
geometric Kummer line.

In particular, a nonzero cycle `z in ker partial` is a nontrivial Fourier
label but

\[
\prod_{a\in z} f_a
\in\overline{\mathbf F}_q(T)^{\times2}.
\]

For the present monic equal-degree model the product is already a square in
`F_q(T)`: every vertex exponent and the infinity exponent are even, and the
leading constant is one.  The corresponding geometric line is trivial.
It contributes an invariant/main-term channel; it is not a square-root
cancellation mode.

This distinction explains both (0.3) and why cyclic graphs are unsuitable if
all formal edge characters are retained without a transverse mask.

## 2. Incidence boundary and uniform fibers

Write `iota_a in F_2^V` for the unoriented incidence column of an edge
`a=uv`; it has ones at `u` and `v`.  Orientation disappears modulo two.  For
an edge subset `x`, multiplication gives

\[
\prod_{a\in x}f_a
\equiv
\prod_{v:(\partial x)_v=1}P_v
\pmod{\overline{\mathbf F}_q(T)^{\times2}},
\qquad
\partial x=\sum_{a\in x}\iota_a.
\tag{2.1}
\]

The kernel consists exactly of subgraphs in which every vertex has even
degree: the binary cycle space `Z_1(Gamma;F_2)`.  The standard incidence-rank
identity is

\[
\operatorname{rank}\partial=|V|-c(\Gamma).
\tag{2.2}
\]

Rank-nullity proves (0.2).

A vertex pattern `b in F_2^V` belongs to `im partial` exactly when its parity
is even on each connected component:

\[
\sum_{v\in C}b_v=0
\qquad\text{for every component }C.
\tag{2.3}
\]

Every nonempty fiber of a linear map is a coset of its kernel.  Equations
(0.2) and (2.3) therefore prove the uniform fiber law

\[
\#\partial^{-1}(b)=2^\beta
\qquad(b\text{ admissible}).
\tag{2.4}
\]

Taking `b=0` gives `2^beta` invariant modes, one of which is the empty/trivial
Fourier label.  Removing it proves (0.3).

## 3. Connected branch and Betti spectrum

Assume from here that `Gamma` is connected, put

\[
v=|V|,\qquad m=|E|,\qquad\beta=m-v+1,
\]

and keep all vertex primes at common degree `e`.  The admissible patterns are
all even vertex subsets.  There are `binom(v,2r)` patterns of size `2r`, and
each has `2^beta` preimages.  This proves (0.4).

For `r>=1`, the corresponding Kummer line is nonconstant and has

\[
b_r=2er,
\qquad
\dim H_c^1(\text{maximal lisse open},\mathcal L_x)=2er-2,
\qquad H_c^2=0.
\tag{3.1}
\]

For `r=0`, there are `2^beta` invariant modes.  On the maximal extension
`P^1`, each is constant and has

\[
\dim H_c^0=1,
\qquad \dim H_c^1=0,
\qquad \dim H_c^2=1.
\tag{3.2}
\]

Thus the full branch/Betti spectrum is

| branch vertices | geometric branch points | multiplicity | maximal `H_c^1` per mode | maximal `H_c^2` per mode |
|---:|---:|---:|---:|---:|
| `0` | `0` | `2^beta` | `0` | `1` |
| `2r>0` | `2er` | `2^beta binom(v,2r)` | `2er-2` | `0` |

The invariant row is deliberately separate.  Applying the nonconstant
formula `b-2` at `b=0` would erase the main-term obstruction and produce a
nonsensical negative Betti number.

### 3.1 Closed totals

The even-binomial identities

\[
\sum_r\binom v{2r}=2^{v-1},
\qquad
\sum_r 2r\binom v{2r}=v2^{v-2}
\tag{3.3}
\]

give the following exact totals across all formal modes:

\[
\begin{aligned}
\sum_x1
 &=2^\beta2^{v-1}=2^m,\\
\sum_x b(x)
 &=ev\,2^{m-1},\\
\sum_x\dim H_c^1(U_{x,\max},\mathcal L_x)
 &=ev\,2^{m-1}-2^{m+1}+2^{\beta+1},\\
\sum_x\dim H_c^2(U_{x,\max},\mathcal L_x)
 &=2^\beta.
\end{aligned}
\tag{3.4}
\]

On the common graph-torsor open, all `ev` vertex roots are removed.  A
nonconstant mode has `H_c^1=ev-2`; an invariant mode has `H_c^1=ev-1` and
`H_c^2=1`.  Hence

\[
\sum_x\dim H_c^1(U_{\rm all},\mathcal L_x)
=2^m(ev-2)+2^\beta.
\tag{3.5}
\]

The total removable-puncture tax over **nonconstant modes only** is

\[
\boxed{
ev\left(2^{m-1}-2^\beta\right).}
\tag{3.6}
\]

Invariant modes are excluded from (3.6): their common-to-maximal change also
crosses the compact-support `H_c^0/H_c^2` main-term regime, so it is not the
same cancellation tax.

## 4. Tree spectral universality and top-mode relocation

For a connected tree, `m=v-1` and `beta=0`.  Therefore

\[
\partial:\mathbf F_2^E
\xrightarrow{\sim}
\{b\in\mathbf F_2^V:|b|\equiv0\pmod2\}.
\tag{4.1}
\]

Every even branch pattern occurs exactly once, for every tree topology.  In
particular the multiplicity spectrum is simply

\[
N_{2r}=\binom v{2r}.
\tag{4.2}
\]

What topology controls is the location of the specifically distinguished
all-edge mode:

\[
\partial(\mathbf 1_E)
=\{v:\deg_\Gamma(v)\text{ is odd}\}.
\tag{4.3}
\]

For a path this is its two endpoints.  Conversely, a tree whose all-edge
mode has only two branch vertices has exactly two odd vertices.  Its leaves
already supply two odd vertices; the leaf identity then rules out every
degree at least three, so the tree is a path.

Therefore tree topology only relocates the distinguished top mode within the
universal spectrum (4.2), and the path uniquely places it in the smallest
nonconstant stratum.

This statement is spectral, not a canonical edge-by-edge identification:
changing topology can change the branch pattern attached to many individual
edge subsets.  What remains fixed is the complete multiset, while the
project's singled-out all-edge character moves between its strata.

## 5. Mask transversality

Let `W <= F_2^E` be a linear selected Fourier subspace.  Its invariant modes
form the kernel of the restricted boundary map:

\[
\ker(\partial|_W)
=W\cap\ker\partial
=W\cap Z_1(\Gamma;\mathbf F_2).
\tag{5.1}
\]

If

\[
t=\dim(W\cap Z_1),
\]

then this kernel contains `2^t` elements.  Removing the zero Fourier label
proves (0.5).  The following conditions are equivalent:

1. `W` contains no nonzero invariant selected mode;
2. `W cap Z_1=0`;
3. `dim partial(W)=dim W`;
4. `partial|W` is injective.

This is an exact inverse-design rule.  One may retain cycles in the ambient
graph while choosing a transverse `W`, as the replay's cycle-broken mask
does.  Conversely, any selected subspace meeting the cycle space contains a
forced invariant channel before any arithmetic cancellation is considered.

Mask transversality is a representation/source firewall, not a
varying-conductor trace estimate.  It removes geometrically constant modes;
it does not bound the remaining nonconstant traces, preserve a physical
hard mask, or individualize a principal member.

## 6. Bounded replay

The producer checks all `771` connected labelled simple graphs on two
through five vertices.  Across them it evaluates `55,894` edge subsets.  It
verifies:

- incidence rank and cycle dimension;
- admissibility component by component;
- uniform `2^beta` fibers;
- the full connected spectrum (0.4);
- the tree/path top-mode criterion;
- path versus star spectral equality;
- a full cycle mask with one invariant nonzero mode;
- a cycle-broken transverse mask with none.

The controls use bit arithmetic only.  They enumerate no finite field,
polynomial, curve, cohomology group, or `L`-function zero.

Run:

```text
python research/l-families/atlas/function_field/ffps_graph_kummer_character_spectrum.py --check
pytest -q tests/test_ffps_graph_kummer_character_spectrum.py
```

## 7. Proof ledger

### Proved exactly

- incidence-boundary identity (2.1);
- cycle-space kernel and dimension (0.2);
- componentwise admissibility and uniform fiber law (2.4);
- invariant-mode count (0.3);
- connected branch/Betti spectrum (0.4), (3.1), and (3.2);
- closed totals (3.4)--(3.6);
- tree spectral universality and top-mode relocation;
- Mask transversality (0.5)--(0.6).

### Imported

- the tame rank-one Kummer-sheaf interpretation;
- Grothendieck--Ogg--Shafarevich and duality for the Betti entries.

### Not proved here

- that a graph or mask is the exact physical FFPS source adapter;
- legal filling of source punctures;
- cancellation for any remaining nonconstant mode;
- a varying-conductor selected trace estimate;
- principal-member individualization;
- CYSEL, WCADD, WCKUM, RH, or GRH.

## 8. Novelty boundary

The cycle-space exact sequence, incidence rank, and even-subset spectrum are
elementary graph theory and linear algebra.  The project contribution is
their source-aware packaging as a Kummer-character spectrum and the mask
transversality design rule.  No external novelty or priority claim is made.
