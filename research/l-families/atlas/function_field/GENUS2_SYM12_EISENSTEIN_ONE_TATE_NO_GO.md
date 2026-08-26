# Genus-two `Sym^12`: Eisenstein one-Tate convention no-go

Status: **EXACT FINITE LOCALIZATION; `epsilon_Eis=0` RULED OUT AT THE
DISPLAYED EULER-CLASS LEVEL; GALOIS REALIZATION STILL SOURCE-CAVEATED**

Scope: `(j,k)=(12,3)`, equivalently
`(lambda_1,lambda_2)=(12,0)`, on
`A_2(w^1)=A_2[2]/S_5` for the natural point-stabilizer `S_5`.

Resource bound: finite constituent bookkeeping only. No point counts,
Fourier fitting, or large linear algebra.

Exact replay:
[`genus2_sym12_eisenstein_one_tate_no_go.py`](genus2_sym12_eisenstein_one_tate_no_go.py).
Canonical output:
[`genus2_sym12_eisenstein_one_tate_no_go.json`](genus2_sym12_eisenstein_one_tate_no_go.json).

## 1. Outcome

The remaining discrepancy is not an undifferentiated boundary-normalization
choice. It is one explicitly named local class.

Bergstrom--Faber--van der Geer's expected nonregular continuation gives

\[
e_{c,\mathrm{Eis}}^{S_5}=2-5\mathbb L,
\tag{1}
\]

whereas the exact natural-`S_5` projection of the constituents displayed in
Shmakov's Theorems 4.6.6--4.6.8 is

\[
e_{c,\mathrm{Eis}}^{S_5,\mathrm{Shm}}=2-4\mathbb L.
\tag{2}
\]

Every term in (1) and (2) agrees except the contribution of the unique
Fricke-positive weight-16 newform of level two. The decomposition in BFG's
Theorem 4.4, when used in their expected `m=0` continuation, assigns its
degree-three Tate block

\[
B'\otimes\mathbb L
=([5,1]\oplus[4,2]\oplus[3,2,1])\otimes\mathbb L,
\tag{3}
\]

while Shmakov assigns

\[
([4,2]\oplus[3,2,1])\otimes\mathbb L.
\tag{4}
\]

Only `[5,1]` has a fixed vector under the natural point-stabilizer `S_5`.
Thus (3)--(4) is exactly one `[5,1] tensor L` copy, and

\[
\boxed{
(2-4\mathbb L)-(2-5\mathbb L)=\mathbb L.
}
\tag{5}
\]

No exceptional-outer-automorphism choice and no sign twist changes (2) into
(1). The four possible selector totals are

\[
2-4\mathbb L,\qquad
1-3\mathbb L,\qquad
0,\qquad
1-\mathbb L.
\tag{6}
\]

The first is the geometric natural/trivial convention. The other three are
counterfactual convention checks.

Consequently, **`epsilon_Eis=0` is incompatible with Shmakov's displayed
Euler constituents even after every `S_6 -> S_5` convention escape is
allowed**. At the formal Tate-labelled level the exact answer is

\[
\boxed{\varepsilon_{\rm Eis}=\mathbb L.}
\tag{7}
\]

The remaining caveat is narrower than before: Shmakov explicitly says that
the thesis does not provide a fully satisfactory justification of the Galois
action on Eisenstein cohomology. Therefore (7) is theorem-supported as the
displayed Tate-labelled branch and is forced after forgetting Galois to the
topological Euler class, but this packet does not independently realize (7)
inside the Grothendieck group of actual `Gal(Qbar/Q)` representations.

## 2. The BFG specialization

BFG define compactly supported Eisenstein cohomology as the kernel of the
forget-supports map. Shmakov's Definition 2.1.4 defines
`H_c,Eis` as the image of the boundary connecting map, equivalently the same
kernel of `H_c -> H`. Thus (1) and (2) are not ordinary-versus-compact or
full-versus-kernel normalizations. BFG's Corollary 4.5 gives, for regular
`(l,m)`,

\[
\dim S_{l-m+2}(\Gamma_0(2))
-\dim S_{l+m+4}(\Gamma_0(2))\mathbb L^{m+1}
+2(S[m+2]+1)
\tag{8}
\]

when `m` is even. Theorem 4.2 says that for `m=0` this is only an
**expected** continuation, using

\[
S[2]:=-\mathbb L-1.
\tag{9}
\]

At `(l,m)=(12,0)`,

\[
\dim S_{14}(\Gamma_0(2))=2,
\qquad
\dim S_{16}(\Gamma_0(2))=3,
\]

so (8)--(9) give

\[
2-3\mathbb L+2(-\mathbb L)=2-5\mathbb L.
\]

The source grade matters: (1) is BFG's expected nonregular continuation, not
their regular theorem.

## 3. The Shmakov specialization

Shmakov's elliptic dimension table on printed page 356 gives

| weight | level-4 new | level-2 new `+` | level-2 new `-` | level 1 |
|---:|---:|---:|---:|---:|
| 14 | 1 | 1 | 1 | 0 |
| 16 | 1 | 1 | 0 | 1 |

Both sources use the geometric Tate class `L=Q_l(-1)`, with Frobenius trace
`q`; a Tate inversion cannot account for the discrepancy.

Insert `(lambda_1,lambda_2)=(12,0)` into Theorems 4.6.6--4.6.8 and keep only
the natural invariant carriers `[6]` and `[5,1]`.

### Siegel boundary

In degree two, the two level-two weight-14 newforms each carry

\[
[4,2]\oplus[5,1]\oplus[3,2,1],
\]

so the marked quotient keeps two constants. The level-4 block has no natural
fixed vector.

In degree three at weight 16:

- the unique level-4 newform has no natural fixed vector;
- the unique Fricke-positive level-2 newform carries (4), hence has no
  natural fixed vector;
- the unique level-one form contributes one `[5,1]` and one `[6]`, hence
  `2L`.

Thus the Siegel contribution is

\[
2-2\mathbb L.
\tag{10}
\]

### Klingen boundary

The relevant elliptic weights are 2 and 15. The corresponding cusp spaces
vanish, so the Klingen Euler contribution is zero.

### Borel boundary

The surviving modules are

\[
H_c^2=[4,2]\oplus[2^3]\oplus[3,2,1],
\]

and

\[
H_c^3=([6]\oplus[4,2]\oplus[5,1])\otimes\mathbb L.
\]

The first has no natural fixed vector and the second has two. Hence the
Borel contribution is

\[
-2\mathbb L.
\tag{11}
\]

Equations (10)--(11) give (2).

## 4. Exact localization against BFG

It is useful to compare source blocks rather than only the totals.

| block | BFG expected marked contribution | Shmakov marked contribution | difference `Shm-BFG` |
|---|---:|---:|---:|
| weight-14 level two | `2` | `2` | `0` |
| weight-16 level one oldspace | `-2L` | `-2L` | `0` |
| formal weight-two/Borel block | `-2L` | `-2L` | `0` |
| weight-16 Fricke-positive level-two newform | `-L` | `0` | `+L` |

Thus the nonregular convention (9) is **not itself** the disputed term: its
`-2L` contribution agrees exactly with Shmakov's Borel calculation. The
discrepancy lies in the regular-weight-16 Siegel block, specifically in
whether the Fricke-positive local representation contains `[5,1]`.

Shmakov's proof makes the local mechanism explicit. For a level-two newform,
parahoric restriction starts from

\[
[4,2]\oplus[5,1]\oplus[3,2,1].
\]

The kernel selected by the normalized induction/intertwining map is `[4,2]`
for the Fricke-positive unramified-quadratic Steinberg twist and `[5,1]` for
the Fricke-negative Steinberg representation. At weight 16 the source table
has one positive and no negative newform. This is precisely why the natural
marked quotient sees no level-two new contribution in (2).

## 5. Outer and sign conventions cannot repair it

The exact convention packet proves that the only four selectors obtained from
the natural/outer `S_5` and an optional sign twist are

| convention | selected irreducibles | Shmakov Euler projection |
|---|---|---:|
| natural, trivial | `[6]`, `[5,1]` | `2-4L` |
| outer, trivial | `[6]`, `[2^3]` | `1-3L` |
| natural, sign | `[1^6]`, `[2,1^4]` | `0` |
| outer, sign | `[1^6]`, `[3^2]` | `1-L` |

None is `2-5L`. Moreover, the split-root and official modular-form
conventions are already known to lie in the same inner class, so only the
first row is geometrically relevant. Equation (6) is a no-go, not an invitation
to relabel the marked quotient.

## 6. The rank obstruction

Apply the forgetful rank realization `L -> 1`. Equations (1) and (2) have
virtual ranks

\[
-3\quad\text{and}\quad-2.
\]

Connecting maps or extensions cannot change an alternating Euler class.
Therefore a missing differential cannot turn Shmakov's displayed associated
graded into BFG's expected branch. Any reconciliation must change an input
constituent—exactly the `[5,1] tensor L` block isolated above—not merely the
placement of constituents in cohomological degrees.

This rank test is independent of the Tate/Galois label. If Shmakov's
topological constituent calculation is accepted, `epsilon_Eis=0` is already
impossible before asking how Frobenius acts.

## 7. Exact logical grade

### Exact finite deductions

- the BFG specialization (1) from Corollary 4.5 plus their stated `m=0`
  convention;
- the natural projection (2) of Shmakov's displayed constituents;
- the four convention totals (6);
- the unique localization (3)--(5);
- the virtual-rank obstruction;
- independence of the alternating Euler class from connecting-map ranks.

### Primary-source theorem support

- Shmakov's Theorem 4.3.12 only invokes its connecting-map assumption when
  `lambda_1=lambda_2`; that does not occur here.
- Theorem 4.3.21 invokes an assumption when `lambda_2=0`, but the present
  Klingen source spaces vanish and its Euler contribution is zero.
- Theorem 4.3.34 says its unresolved assumptions apply only at
  `(lambda_1,lambda_2)=(0,0)`; the present Borel case is not exceptional.
- The dissertation summary explicitly says Euler characteristics are
  unaffected by the connecting-morphism issues.

These points make `2-4L` the source-preferred displayed Euler branch and make
its rank `-2` robust. They do not erase the author's separate Galois caveat.

### Source-caveated

- realization of every displayed Tate label as the actual compact-support
  `S_5 x Gal` Euler class;
- hence `epsilon_Eis=L` as a fully independent theorem in
  `K_0(Rep Gal(Qbar/Q))`;
- the resulting all-`q` Frobenius identity.

### Open, in its smallest form

Independently compute one local-to-global map: the compactly supported Siegel
Eisenstein contribution of the unique Fricke-positive weight-16 level-two
newform. The decisive test is whether its degree-three natural-`S_5` module
contains `[5,1]`.

Shmakov predicts

\[
[3,2,1]\oplus[4,2]
\]

and therefore no marked invariant. BFG's expected continuation inserts one
additional `[5,1]`. A Pink boundary calculation or the single relevant
parabolic term in the stabilized trace formula, including its Tate twist,
would close the Galois realization. More primes, point counts, or
same-characteristic recurrences do not address this map.

## 8. Consequence for the project master identity

The independently closed stable adapter gives `G=0`, so

\[
\widehat H_{12}
=-\mathbb L f_-+\varepsilon_{\rm Eis}.
\]

The source-preferred displayed Shmakov branch is therefore

\[
\widehat H_{12}=\mathbb L-\mathbb L f_-,
\]

not the empirically observed `-L f_-` branch. This packet does not overwrite
that conflict. It proves that the conflict cannot be blamed on an outer
`S_6` convention, a sign twist, the formal weight-two convention, or an
uncomputed connecting-map rank. Either the one local Eisenstein constituent
or another supposedly exact input to the master adapter must be revisited.

## 9. Replay

Run:

```text
python research/l-families/atlas/function_field/genus2_sym12_eisenstein_one_tate_no_go.py --check
pytest -q tests/test_genus2_sym12_eisenstein_one_tate_no_go.py
```

The replay transcribes nine nonzero constituent rows, applies the four exact
selectors, and checks the one-carrier difference. It contains no cohomology
engine and does not promote the source-caveated Galois realization.

## 10. Primary sources and novelty boundary

- Bergstrom, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917), Definition of `e_Eis` on
  printed page 4, Theorem 4.2 on printed page 5, and Theorem 4.4 plus
  Corollary 4.5 on printed page 6. The paragraph immediately after Theorem
  4.2 explicitly marks the `m=0` extension as expected; the paragraph after
  Theorem 4.4 gives the corresponding `C*(-L-1)` isotypical convention.
- Shmakov,
  [*Cohomology of Local Systems on Siegel Threefolds with Square-Free
  Parahoric Level*](https://openscholar.uga.edu/record/1979), especially the
  authorial caveats on printed pages 3--5; the Tate convention on printed
  page 24; Definition 2.1.4 on printed pages 72--73; Theorems 4.3.12,
  4.3.21, and 4.3.34 on printed pages 243, 254, and 276; the elliptic
  dimension table on printed pages 355--356; Theorem 4.6.6 and its explicit
  level-two parahoric-kernel calculation on printed pages 370--373; Theorem
  4.6.7 on printed pages 373--375; and Theorem 4.6.8 on printed pages
  376--378.

No claim is made that the source theorems, the `S_6` branching facts, or the
parahoric restriction are new. The project contribution is the exact
one-class localization, the four-convention no-go, and the sharply reduced
Galois comparison target.
