# Marked-place signed-descent Gate 0

Status: **exact partition-reconciliation theorem and exact scoped no-go after
the invariant projector, polynomial Möbius restriction, and literal Wick
deletion; the complete signed pushforward remains undecided**

Scope: odd characteristic for the symbolic support theorem; exact
dependency-free controls at `q=3,5`; no sheaf construction, uniform trace
estimate, principal binding, RH, or GRH theorem.

Exact replay:
[`ffps_marked_place_signed_descent_gate0.py`](ffps_marked_place_signed_descent_gate0.py).
Canonical output:
[`ffps_marked_place_signed_descent_gate0.json`](ffps_marked_place_signed_descent_gate0.json).
Source lock:
[`ffps_marked_place_signed_descent_gate0.sources.json`](ffps_marked_place_signed_descent_gate0.sources.json).

## 0. Verdict

PR #760 and PR #758 make statements in different tensor partitions.

At fixed marked labels, the native bilateral phase is an external product in
the **coefficient partition**

\[
 (P,c)\mid(Q,d).
\tag{0.1}
\]

PR #760 correctly externalizes that trace algebra, polynomial coprimality,
and the literal Wick diagonal. Closed-point Adams extraction, however,
requires the **marked-place partition**

\[
 (\ell,h,Y,Y')\mid(\rho,k,X,X'),
 \qquad
 X=Pc^2\bmod\rho,
 \quad
 Y=Qd^2\bmod\ell.
\tag{0.2}
\]

In (0.2), the selector `ell=P^-(c)` places `ell` and `c` on opposite
blocks, while `c` is evaluated in the `rho` block. The same crossing occurs
for `rho=P^-(d)`. Thus rank one in (0.1) does not establish commuting
partial Frobenii in (0.2).

This packet proves more than the raw-source obstruction in PR #758, but less
than a global categorical impossibility theorem:

> On a clean degree-one nonresonant bilateral chart with two retained source
> labels, the crossed generic support survives `Pi_0`, the exact polynomial
> Möbius coprimality restriction, and literal Wick deletion with coefficient
> one. That labelled class is stable under total Frobenius but not under
> either marked-place partial Frobenius. Consequently those three cleanup
> operations do not, by themselves, promote PR #760's trace externality to
> `RELPARTFROB`.

Other native strata, cleanup cones, or the final signed pushforward could
still cancel or identify the obstructing support. No theorem here excludes
that possibility. The **complete signed pushforward remains undecided**.

## 1. Frozen sources and exact native labels

The machine source lock authenticates thirteen Git blobs. The load-bearing
ones are:

| role | commit | blob | exact content used |
|---|---|---|---|
| corrected marked axes | `d79692ece0b7604ad309c459f565b24e9926f5c5` | `a04eaa8a1fd5838f7bbe605dc9c8099e0f033511` | marked-place blocks, crossed-core trilemma, raw no-lift boundary |
| graph-support module | same | `4ee3c50f3cce3e7aa2dbd901b93fd50b713ea4bb` | faithful generic-support and Frobenius-graph distinction |
| relative-first Adams | `3a595dda92ef827a41e50d2395309692a93748ad` | `aba88795dd1c95cb320d45c1dc367cd71d73e1d5` | subtract before Adams; only the relative class needs descent |
| fixed-label phase externality | same | `68e99e25539de79955ef11534056b9e82b57cb60` | coefficient-partition factorization |
| trace tensor closure | same | `37647db8c43b983dc64bfc71a0c112539119a98a` | trace-level Möbius/Wick externalization and `ONEPLACEWEIL` boundary |
| native bilateral source | `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b` | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | `L-106120`, especially the labels and equations (1), (2), and (5) |
| literal Wick identity | same | `37722c3f36ec7d1681f34d4329a3795e5028f7ae` | `L-106131`, especially the bilateral coordinates and off-atomic kernel |
| centered source correlation | same | `85c4ef92ead7d8b235f9c195c3c0acd16d16030f` | `L-106191`, including the dangerous `c=ell,d=rho` chart |
| principal frontier | same | `d5be8e376c88b63de0be19e0d9e8791624e99ae2` | `T-106140` and the exact principal-binding normalization |
| invariant projector | `b870366141fe8d5f43d5b81f6e50a67d2a888070` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | honest `C-S=Pi_0` endomorphism |

The complete list, including the physical-squareclass adapter, partial-
Frobenius verdict, and external-plus-diagonal Adams theorem, is in the source
lock. The replay calls `git rev-parse COMMIT:PATH` and compares every blob;
it does not merely trust a digest copied into its own output.

A fresh shallow clone of this branch may omit the sibling PR objects. Fetch
the four exact source commits without merging either sibling history:

```text
git fetch --no-tags origin d79692ece0b7604ad309c459f565b24e9926f5c5 3a595dda92ef827a41e50d2395309692a93748ad 86cac1d64364015ec2cc0f8fbb6fc75dc041c12b b870366141fe8d5f43d5b81f6e50a67d2a888070
```

The replay fails closed with a missing-object diagnostic if an exact
`COMMIT:PATH` is unavailable; it never merges those histories.

The native bilateral fibre label is

\[
 \iota=(g,\ell,\rho,\sigma,\tau),
 \qquad \ell\ne\rho,
\tag{1.1}
\]

with additive labels `1<=h<ell`, `1<=k<rho`, reduced cores
`ell=P^-(c)`, `rho=P^-(d)`, and physical coordinates

\[
 X=Pc^2\bmod\rho,
 \qquad
 Y=Qd^2\bmod\ell.
\tag{1.2}
\]

These labels are retained rather than reconstructed from a fitted matrix.

## 2. The clean nonresonant bilateral chart

Let $q$ be an odd prime power. Let
$\mathcal C_1=\mathbf A^1_{\mathbf F_q}$ be the universal coefficient space
of monic linear polynomials `T-A`, and base-change it to
$K=\overline{\mathbf F}_q$. Write $\lambda,\rho\in K$ for geometric
coefficient coordinates and work on

\[
 U=\{(\lambda,\rho)\in\mathbf A_K^2:\lambda\ne\rho\}.
\tag{2.1}
\]

Take the monic degree-one reduced cores

\[
 c_\lambda(T)=T-\lambda,
 \qquad
 d_\rho(T)=T-\rho.
\tag{2.2}
\]

On the universal monic-linear incidence chart, write $\ell_\lambda$ and
$\rho_\rho$ for the marked geometric roots paired with $c_\lambda$ and
$d_\rho$. At an $\mathbf F_q$-rational specialization these are exactly the
native selectors $P^-(c)=\ell$ and $P^-(d)=\rho$. Moreover
$(c_\lambda,d_\rho)=1$ on $U$. Freeze $g,\sigma,\tau,h,k$ and the two opposite
owner residues to one. This last normalization is a local residue chart; it
does **not** assert that the complete owner, shell, Boolean, carrier, renewal,
and endpoint source has already been constructed geometrically.

Only `lambda,rho in F_q` specialize to actual affine degree-one closed
places over the base field. General `K`-points belong to the universal
coefficient-space graph. This distinction is load-bearing: base-field trace
rows fix every rational coefficient and cannot see the partial-Frobenius
support shift, whereas an independent extension tower must retain the
universal geometric support.

Put

\[
 B_L=\mathbf A^2_{\lambda,Y},
 \qquad
 B_R=\mathbf A^2_{\rho,X},
\tag{2.3}
\]

and define the crossed graph

\[
 \begin{aligned}
 \iota:U&\longrightarrow B_L\times B_R,\\
 (\lambda,\rho)&\longmapsto
 \left(
  (\lambda,(\lambda-\rho)^2),
  (\rho,(\rho-\lambda)^2)
 \right).
 \end{aligned}
\tag{2.4}
\]

Write $Z=\iota(U)$. Because `lambda,rho` remain coordinates, `iota` is a
graph embedding and $Z$ is irreducible. It is the smallest chart retaining
both load-bearing facts from the native source:

```text
the marked place selecting a core lies on one marked block;
the same core is evaluated on the opposite marked block.
```

No claim is made that this chart, by itself, carries the complete native
amplitude or its global multiplicity.

## 3. MPD-G0.1 — fixed-label trace externality

Fix distinct `ell,rho`. The phase in `L-106120` is

\[
 e_\rho(kPc^2)e_\ell(-hQd^2)
 =\Phi_{\rho,k}(P,c)\Psi_{\ell,h}(Q,d).
\tag{3.1}
\]

This is rank one in the coefficient partition (0.1). For the degree-one
selector in the bounded replay, the fixed-label matrix is

\[
 S_{\ell,\rho}(c,d)
 =\mathbf1_{c=\ell}\mathbf1_{d=\rho}
 =u_\ell(c)v_\rho(d),
\tag{3.2}
\]

and therefore has rank one over $\mathbf Q$.

Likewise, the exact finite-horizon polynomial identity

\[
 \mathbf1_{(c,d)=1}=\sum_{m\mid c,\,m\mid d}\mu(m)
\tag{3.3}
\]

and its squared version give finite signed sums of coefficient-side tensor
products. Literal Wick subtraction is external minus the same-atom diagonal.
These are the exact trace-algebra conclusions of PR #760. This packet does
not refute or weaken them.

## 4. MPD-G0.2 — clean marked-support shift

Let the left partial Frobenius act on the whole left marked block and fix the
right block:

\[
 \varphi_L:
 (\lambda,Y;\rho,X)
 \longmapsto
 (\lambda^q,Y^q;\rho,X).
\tag{4.1}
\]

Define $\varphi_R$ symmetrically. Total Frobenius is
$\varphi_L\varphi_R$.

### Theorem MPD-G0.2

For every odd $q$, the reduced support $Z$ is stable under total
Frobenius and is not stable under either partial Frobenius.

### Proof

The equations of $Z$ are defined over $\mathbf F_q$, so raising all four
coordinates to their `q`-th powers preserves the reduced graph.

If the left partial Frobenius preserved $Z$, then on its coordinate ring
one would have both

\[
 X=(\rho-\lambda)^2
 \quad\text{and}\quad
 X=(\rho-\lambda^q)^2.
\]

Their difference is

\[
 (\rho-\lambda)^2-(\rho-\lambda^q)^2
 =(\lambda^q-\lambda)
  (2\rho-\lambda-\lambda^q).
\tag{4.2}
\]

Equation (4.2) is not the zero polynomial in
$K[\lambda,\rho,(\lambda-\rho)^{-1}]$. Hence the two generic supports are
different. The right-hand statement is symmetric. $\square$

This proof concerns simultaneous Frobenius of each complete marked block.
It does not reuse the narrower and inapplicable obstruction obtained by
moving only `h` or only `Y` inside one block.

## 5. MPD-G0.3 — post-cleanup generic-support survival

Work in a support-faithful characteristic-zero group, for example the free
$\mathbf Q$-module on irreducible generic supports, or a constructible-
function/sheaf $K_0$ equipped with a faithful map to that module. Retain
two disjoint literal source labels `0,1` before physical collapse.

### Projector

The imported honest identity is

\[
 C-S=\Pi_0,
 \qquad
 \operatorname{im}\Pi_0\simeq E.
\tag{5.1}
\]

On the invariant deck line, `Pi_0` has coefficient one. It changes the deck
factor but does not change the geometric support $Z$.

### Möbius restriction

For the distinct linear cores (2.2), the only common monic divisor is one.
Thus (3.3) equals one on all of $U$. No nontrivial Möbius term shares this
generic chart with opposite coefficient.

### Literal Wick deletion

Normal ordering deletes same-label pairs. It retains the two ordered
off-atomic orientations

\[
 (0,1),\qquad(1,0).
\tag{5.2}
\]

On the labelled source cover their generic supports $Z_{01}$ and
$Z_{10}$ are distinct from the deleted same-label diagonals. For normalized
unit coefficients, each retained orientation has coefficient

\[
 1_{\Pi_0}\cdot1_{(c,d)=1}\cdot1_{0\ne1}=1.
\tag{5.3}
\]

### Theorem MPD-G0.3 — post-cleanup generic-support survival

After `Pi_0`, polynomial Möbius coprimality, and literal labelled Wick
deletion, each ordered off-atomic clean chart has nonzero generic-support
coefficient. By MPD-G0.2 its support is moved by either partial Frobenius.
Consequently this cleaned labelled chart does not descend to a bivariate Weil
class with the required commuting partial Frobenii in any category where an
isomorphism preserves generic support.

The labels and the order of operations are load-bearing. If a later
pushforward forgets labels, identifies supports, or supplies another stratum
with the same support and opposite coefficient, (5.3) need not survive. This
theorem therefore closes the shortcut

```text
Pi_0 + Wick + Moebius automatically imply RELPARTFROB
```

and nothing stronger.

## 6. MPD-G0.4 — the partition rank tax

Let

\[
 \mathcal I_q=\{(a,b)\in\mathbf F_q^2:a\ne b\}.
\tag{6.1}
\]

Here the `q` labels are the affine monic degree-one places `T-a`. They are
not the `q+1` closed degree-one points of the complete curve
\(\mathbf P^1_{\mathbf F_q}\); the place at infinity is outside this affine
source chart.

Thus the finite matrix panel uses the actual `F_q`-rational degree-one
specializations. It authenticates the partition-rank statement, not the
geometric support-shift theorem. The latter is proved symbolically on the
universal coefficient space and receives separate $\mathbf F_{q^2}$ witnesses.

Rows of the source-faithful labelled allocation are indexed by
`(ell,d) in I_q` and columns by `(rho,c) in I_q`. The retained `d` and `c`
are source-cover labels feeding the physical coordinates, not extra
coordinates on the collapsed marked-place base. Define

\[
 M_q[(\ell,d),(\rho,c)]
 =\mathbf1_{c=\ell}\mathbf1_{d=\rho}.
\tag{6.2}
\]

For every row `(ell,d)`, the unique nonzero column is `(d,ell)`. Hence
$M_q$ is the swap permutation matrix and

\[
 \boxed{\operatorname{rank}_{\mathbf Q}M_q=q(q-1).}
\tag{6.3}
\]

The same rank holds over every characteristic-zero field, including
$\mathbf C$. In contrast, every fixed-`(ell,rho)` coefficient slice (3.2)
has rank one. Universalizing a family of fixed-label factorizations changes
the tensor partition and incurs a source-cardinality rank.

After literal Wick deletion, the two retained ordered label orientations
live on disjoint labelled supports. Their flattening is

\[
 M_q\oplus M_q,
\]

so

\[
 \boxed{\operatorname{rank}_{\mathbf Q}(M_q\oplus M_q)=2q(q-1).}
\tag{6.4}
\]

Equation (6.4) is a statement on the retained labelled source cover. If the
two ordered orientations are forgotten before flattening, their matrices add
to `2M_q`, whose rank is only `q(q-1)`. Such label forgetting is exactly a
later pushforward at which cancellation or identification must be audited;
it is not literal pre-collapse Wick normal ordering.

The exact controls give ranks `6,12` at `q=3` and `20,40` at `q=5`.
Equation (6.3), not those two instances, is the theorem.

This is a presentation lower bound for any external-product expansion that
retains this complete labelled panel. It is not a Betti lower bound for an
unknown derived pushforward and not a live-source occupancy theorem.

## 7. Positive and counterfeit controls

The replay contains two deliberately different rank-one controls.

1. A nonzero external product on the same finite row and column sets has
   rank one. It models the clean separable Kummer/norm situation and confirms
   that the rank checker does not manufacture an obstruction.
2. Dropping both crossed selectors leaves a source-blind phase-only all-ones
   matrix of rank one. Reinstating the literal selectors produces (6.2) and
   full rank. This is the counterfeit-rejection control: phase
   factorization without source incidence is insufficient.

For support, the replay uses

\[
 \mathbf F_q[t]/(t^2-2),
 \qquad q\in\{3,5\},
 \qquad \lambda=t,\quad\rho=1.
\tag{7.1}
\]

In both fields, `2` is nonsquare and `t^q=-t`. The original and total-
Frobenius points lie on $Z$; the two partial-Frobenius points do not. These
extension-field points authenticate that base-field trace agreement does not
identify the universal geometric supports. They are exact witnesses for the
bounded controls, not evidence from which the all-odd-$q$ theorem is
inferred.

## 8. Reconciliation with PR #758 and PR #760

The conclusions now fit without contradiction.

| statement | status after Gate 0 |
|---|---|
| fixed-label phase factors in `(P,c)|(Q,d)` | **EXACT; RETAINED FROM #760** |
| polynomial coprimality and literal Wick have signed trace-tensor formulas | **EXACT; RETAINED FROM #760** |
| raw natural universal source has crossed marked-place incidence | **EXACT; RETAINED FROM #758** |
| local Artin--Schreier/incidence pieces are Weil under simultaneous marked-block Frobenius | **EXACT; RETAINED FROM #758** |
| clean crossed support survives `Pi_0` + Möbius + labelled Wick | **PROVED HERE, SCOPED TO THE CLEAN CHART** |
| trace externality implies marked-place partial Frobenius | **REFUTED AS AN AUTOMATIC INFERENCE** |
| complete signed native pushforward has no bifrobenius descent | **NOT PROVED** |
| a correspondence category can repair the descent | **OPEN** |

The key distinction is between equality of finite trace functions after a
chosen coordinate decomposition and an object carrying independent
extension towers in the marked-place variables.

## 9. MPD-G0.5 — principal-binding and trace ledger

This packet changes the order of the remaining Architecture-B work but does
not close an analytic gate.

| stage | exact status | next burden |
|---|---|---|
| `TRACE-NATREL` | imported exact trace identity | retain all source labels through one common functor |
| clean post-projector support | scoped obstruction proved here | determine whether the complete signed pushforward cancels or relocates it |
| `ONEPLACEWEIL` | **OPEN** | construct complete one-sided amplitudes on fixed closed-point spaces with uniform presentation/conductor data |
| external-plus-diagonal / partial Frobenius | conditional exact formalism | prove it for the complete relative class, not one fixed trace row |
| closed-point Adams--Möbius | imported exact once the object exists | retain every non-deck Adams eigenvalue and equal-place correction |
| `ONEPLACETRACE` / `RELTRACE` | **OPEN** | obtain a uniform signed trace estimate before outer absolute values |
| `PRINCIPAL_BINDING` | **OPEN** | match the trace coefficientwise to `T-106140` at the exact horizon and normalization |
| frozen principal consumer | conditional imported implication | requires all preceding open gates |

Therefore

```text
complete source cancellation/descent
  -> ONEPLACEWEIL
  -> ONEPLACETRACE / RELTRACE
  -> PRINCIPAL_BINDING
  -> frozen consumer
```

remains a conditional programme. This packet supplies neither the first
arrow nor any later estimate.

## 10. Proof and computation ledger

| item | grade |
|---|---|
| exact source commits and blobs | **AUTHENTICATED BY GIT OBJECT LOOKUP** |
| coefficient-versus-marked partition distinction | **PROVED BY DEFINITIONS** |
| MPD-G0.2 total/partial Frobenius theorem | **PROVED SYMBOLICALLY FOR EVERY ODD $q$** |
| `Pi_0` coefficient on invariant line | **IMPORTED EXACT AND REPLAYED** |
| degree-one polynomial Möbius coefficient | **PROVED EXACT** |
| literal two-label Wick coefficient | **PROVED EXACT ON THE LABELLED COVER** |
| MPD-G0.3 cleaned generic-support obstruction | **PROVED IN A SUPPORT-FAITHFUL CATEGORY ON THE CLEAN CHART** |
| MPD-G0.4 rank formulas | **PROVED EXACT FOR EVERY FINITE INDEX SET OF THE STATED FORM** |
| `q=3,5` matrices and extension witnesses | **EXACT FINITE AUTHENTICATION CONTROLS** |
| occupancy of the clean chart in the complete live source | **NOT PROVED** |
| noncancellation after complete signed pushforward | **NOT PROVED** |
| `ONEPLACEWEIL`, `RELTRACE`, principal binding | **NOT PROVED** |
| RH or GRH | **UNPROVED** |

No external novelty or priority claim is made for generic-support
filtrations, Frobenius graphs, permutation-matrix rank, Möbius
inclusion--exclusion, or cyclic projectors separately. The project-specific
result is the exact post-cleanup partition audit.

## 11. Replay and resource boundary

Run from the repository root:

```text
python -B research/l-families/atlas/function_field/ffps_marked_place_signed_descent_gate0.py --check
python -B -O research/l-families/atlas/function_field/ffps_marked_place_signed_descent_gate0.py --check
python -B -m unittest tests.test_ffps_marked_place_signed_descent_gate0
python -B -O -m unittest tests.test_ffps_marked_place_signed_descent_gate0
python -B -m ruff check research/l-families/atlas/function_field/ffps_marked_place_signed_descent_gate0.py tests/test_ffps_marked_place_signed_descent_gate0.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_marked_place_signed_descent_gate0.py tests/test_ffps_marked_place_signed_descent_gate0.py
```

The largest exact matrix has dimension `40`. The replay authenticates
thirteen upstream blobs, performs exact rational elimination, materializes
26 abstract ordered base-field label pairs, and checks eight explicit
quadratic-extension point transforms. It enumerates no source horizon,
polynomial family, closed-place family, curve, sheaf, conductor family,
`L`-function, or zero. **RH and GRH remain unproved.**
