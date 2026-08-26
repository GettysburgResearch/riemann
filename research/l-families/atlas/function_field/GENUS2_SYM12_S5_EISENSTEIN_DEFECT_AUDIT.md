# Genus-two Sym12 `S5` Eisenstein defect audit

Status: **DIFFERENTIAL-INDEPENDENT FORMAL EULER PROJECTION; GALOIS REFINEMENT CAVEATED**

Scope: the `(j,k)=(12,3)` channel on the marked ambient stack
`A_2(w^1)=A_2[2]/S_5`

Computation: finite character and weight algebra only; no point counts or family
enumeration

Exact replay:
[`genus2_sym12_s5_eisenstein_defect_audit.py`](genus2_sym12_s5_eisenstein_defect_audit.py)

## 1. Outcome

The one-Tate Eisenstein ambiguity in the existing Sym12 packet has a preferred
later-literature branch, but it is not unconditionally resolved as a Galois
Euler class.  Bergström--Faber--van der Geer's `m=0` formula is explicitly an
**expected** continuation of their regular Eisenstein theorem.  Shmakov's later
Theorems 4.6.6--4.6.8 include the nonregular highest weight `(12,0)`, use the
natural `GSp_4(F_2) \cong S_6` action, and use

\[
\mathbb L=\mathbf Q_\ell(-1),
\qquad
\operatorname{Tr}(F_q\mid\mathbb L)=q.
\]

They are nevertheless stated under assumptions on connecting morphisms, and
the dissertation separately records an incomplete treatment of the Galois
action on Eisenstein cohomology.  Taking invariants under the standard `S_5`
fixing one of the six level-two labels gives the exact finite projection of
Shmakov's displayed associated-graded terms

\[
\boxed{
e_{c,\mathrm{Eis}}^{\mathrm{Shm,formal}}
 (\mathcal A_2[2],\mathbb V_{12,0})^{S_5}
=2-4\mathbb L.
}
\tag{1}
\]

In the notation of
[`GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md`](GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md),
accepting Shmakov's displayed Galois/Tate refinement therefore gives

\[
\varepsilon_{\rm Eis}
=e_{\rm Eis}^{S_5}-(2-5\mathbb L)
=\mathbb L.
\tag{2}
\]

Consequently the source-relative master identity has the conditional Shmakov
branch

\[
\boxed{
\widehat H_{12}=\mathbb L-\mathbb L f_- -G.
}
\tag{3}
\]

Here `G` is the stable/general `S_5`-invariant Galois channel.  Equation (3) is
an exact implication of the displayed Shmakov refinement, not an unconditional
Galois-cohomology theorem.  It does **not** prove `G=0`, and it does not prove
the previously observed finite formula
`Hhat_12(p)=-p*a_p(f_-)` for every `p`.

The strongest unconditional result is instead finite: the full `S_5`-fixed
pre-holomorphic covariant space has dimension `66`, and the corrected
two-orientation valuation matrix has rank `66`.  Thus its holomorphic—and,
because the `Phi` target has odd weight, cuspidal—subspace is exactly zero.
This proves absence of the natural marked modular channel without any broad
finite-field computation.  Calling the corresponding formal cohomological
term `G=0` still requires the separately source-caveated Galois/cohomological
adapter; the finite kernel does not construct that realization.

## 2. Normalizations and the outer-automorphism check

Three identifications are load-bearing.

1. Clery--van der Geer identify the marked-Weierstrass stack as
   `A_2[w]=A_2[2]/S_5`, where `S_5` is the stabilizer of one of the six
   Weierstrass labels.
2. Roesner constructs the level-two action from the same six labelled
   Weierstrass points.  Shmakov specializes the same level-two moduli action
   and labels its irreducibles by the BFG partitions of six.  Thus the
   geometric subgroup is the standard point stabilizer, not an `S_6` subgroup
   transported through the exceptional outer automorphism.
3. Shmakov defines the Lefschetz motive on printed page 24 as
   `L=Q_l(-1)` and immediately records that its Frobenius trace is `q`.

These facts remove the two convention escapes that could otherwise turn a
single missing `[5,1] tensor L` into an apparent discrepancy.

Because `S_5` is finite and the coefficient field has characteristic zero,
taking `S_5` invariants is exact and commutes with the alternating compactly
supported Euler characteristic.

### Exact effect of the connecting-morphism assumptions

Shmakov's dissertation summary explicitly qualifies Theorems 4.6.6--4.6.8 as
being under the same assumptions on the behavior of connecting morphisms used
in the Eisenstein calculation.  The same summary then makes the narrower
statement that the computations of **Euler characteristics are unaffected**
by these issues.

That narrower statement follows from exact algebra.  For an equivariant long
exact sequence, or more generally a finite equivariant spectral sequence,

\[
\sum_i(-1)^i[H^i]
\]

in the relevant Grothendieck group is independent of the ranks of the
connecting maps/differentials.  Thus the connecting-morphism assumptions are
needed to place the displayed constituents in individual cohomological
degrees, but not to take their alternating formal Euler class.  In particular,
the projection `2-4L` below is differential-independent once the displayed
associated-graded constituents and Tate labels are accepted.

There is a separate caveat.  Shmakov also says that the thesis falls short of
a satisfactory treatment of the **Galois action** on Eisenstein cohomology and
points to the missing trace-formula/weighted-intersection-cohomology bridge.
Therefore:

- `2-4L` is exact as the `S_5` projection of Shmakov's formal Tate-labelled
  associated-graded Euler expression;
- the ranks of connecting maps cannot change it;
- its realization as the actual compact-support `S_5 x Gal` Euler class, and
  hence the Frobenius formula `2-4q`, remains source-caveated rather than
  unconditional in this audit.

Forgetting the Galois/Tate refinement sends `L` to its one-dimensional class
and gives virtual invariant dimension `2-4=-2`; the one-Tate distinction is
visible only in the stronger Galois-refined statement needed by the project.

## 3. Exact `S_6 -> S_5` projection

For the standard point stabilizer,

\[
\operatorname{Res}^{S_6}_{S_5}s[\lambda]
=\sum_{\mu\nearrow\lambda}s[\mu],
\]

where one removable corner is deleted.  A fixed vector is a copy of `s[5]`,
so

\[
\dim s[\lambda]^{S_5}
=
\begin{cases}
1,&\lambda=[6]\text{ or }[5,1],\\
0,&\text{otherwise}.
\end{cases}
\tag{4}
\]

Thus no full `S_6` character calculation is required.  Every invariant
projection below keeps only `[6]` and `[5,1]`.

## 4. Re-derivation of the Eisenstein term

Insert `(lambda_1,lambda_2)=(12,0)` into Shmakov's Theorems 4.6.6--4.6.8 and
then apply (4).  Only the following classical elliptic dimensions enter:

\[
\begin{aligned}
\dim S_{14}(\mathrm{SL}_2(\mathbf Z))&=0,\\
\dim S_{14}^{\rm new}(\Gamma_0(2))&=2,\\
\dim S_{16}(\mathrm{SL}_2(\mathbf Z))&=1,\\
\dim S_{16}^{\rm new,-}(\Gamma_0(2))&=0.
\end{aligned}
\tag{5}
\]

The Klingen terms request elliptic weights `2` and `15` and vanish.  Shmakov's
displayed degree-by-degree cohomology (conditional on the connecting-morphism
assumptions) has the following surviving invariant terms; their alternating
formal class is independent of those assumptions.

| boundary piece | displayed invariant degree data | formal Euler contribution |
|---|---|---:|
| Siegel `P_1` | `H_c^2 = 2*1`, `H_c^3 = 2*L` | `2-2L` |
| Klingen `P_2` | zero | `0` |
| Borel `P_0` | `H_c^3 = 2*L` | `-2L` |

This proves the finite formal projection (1).  More explicitly:

- the two degree-two copies come from the `[5,1]` summand tensored with the
  two-dimensional weight-14 level-two newspace;
- the two degree-three Siegel copies are the `[5,1]` and `[6]` channels
  tensored with the unique level-one weight-16 form;
- the Borel degree-three term contains one `[6]` and one `[5,1]` copy, each
  with one Tate twist.

No assumption about connecting morphisms can change this alternating Euler
expression.  Shmakov displays the terms as `GSp_4(F_2) x Gal` modules, so the
Tate labels are not reconstructed from dimensions alone; nevertheless, his
separate caveat about establishing the Galois action prevents this audit from
promoting the displayed refinement to an unconditional Galois Euler class.

### Why the BFG branch no longer has equal status

BFG prove their Eisenstein formula for regular highest weight.  At `m=0` they
say that the displayed continuation is expected and impose the formal
convention

\[
S[\Gamma(2),2]:=-\mathbb L-1.
\]

That continuation gives `2-5L`.  Bergstrom--Clery likewise state their
`k=3,j>0` isotypical extension only conditional on the BFG nonregular
Eisenstein conjecture.  Shmakov's later calculation therefore makes `2-4L`
the preferred formal associated-graded branch.  It is stronger evidence than
a second empirical normalization, but the Galois-refined equality remains
caveated as explained above.

This is a source reconciliation, not a claim that the Shmakov formula or its
specialization is new mathematics.

## 5. Consequence for the Sym12 defect

The earlier packet established, relative to its exact ambient adapter and the
theorem-supported endoscopic term,

\[
\widehat H_{12}
=-\mathbb L f_-+\varepsilon_{\rm Eis}-G.
\]

Under the displayed Shmakov Galois/Tate refinement, substitution of (2) gives
(3).  It follows that the following three assertions cannot all be promoted to
all-`q` theorems:

1. `Hhat_12=-L*f_-`;
2. Shmakov's formal `2-4L` expression realizes the actual Galois Euler class
   on the project ambient stack;
3. `G=0`.

This audit verifies the stack, group action, Tate convention, and
differential-independent formal projection behind item 2, but not its missing
Galois realization.  Conditional on item 2, an all-`q` proof of item 1 would
instead force

\[
G=\mathbb L
\]

in the relevant Grothendieck/trace channel.  That would be highly
non-generic for a genuine stable Siegel-cusp contribution and should be
treated as a diagnostic of the remaining adapter/channel decomposition, not
as a conjecture inferred from three primes.

## 6. The official-data rows: useful, but not independent

The official query for `(j,k,l)=(12,3,0)` returns five `S_6` rows.  Their lift
classification matters:

| partition | Specht dimension | `dimLift` | `dimNonLift` | `S5` fixed dimension |
|---|---:|---:|---:|---:|
| `[3,1^3]` | 10 | 0 | 1 | 0 |
| `[2^3]` | 5 | 1 | 0 | 0 |
| `[2^2,1^2]` | 9 | 0 | 1 | 0 |
| `[2,1^4]` | 5 | 1 | 0 | 0 |
| `[1^6]` | 1 | 1 | 0 | 0 |

Thus the nonlift/general part has total dimension `19`, while the three lift
rows have total dimension `11`.  The older packet's description of all five
rows as stable/general is incorrect.  Its invariant conclusion survives:
neither the full list nor the two nonlift rows contain `[6]` or `[5,1]`.

However, the implemented `k=3` decomposition is based on the same conditional
nonregular continuation discussed by Bergstrom--Clery, Remark 5.4.  It is
therefore conditional evidence for `G=0`, not an independent resolution of
the Eisenstein defect.  In particular, it neither proves nor disproves the
preferred but Galois-caveated Shmakov formal specialization.

## 7. An unconditional finite covariant target

Clery--van der Geer's covariant construction sends a marked binary-sextic
covariant `C'_{d,b}` to Siegel weight

\[
(j,k)=(b,d-b/2).
\]

Hence `(j,k)=(12,3)` corresponds to `(d,b)=(9,12)`.  Before imposing their
holomorphy valuations, the `S_5`-invariant covariant multiplicity is

\[
\dim\operatorname{Hom}_{\mathrm{SL}_2}
\left(
 \operatorname{Sym}^{12},
 \operatorname{Sym}^{5}(\operatorname{Sym}^{9})
 \mathbin\otimes \operatorname{Sym}^{9}
\right).
\tag{6}
\]

This dimension is exactly `66`.  A small coefficient calculation proves it.
Let

\[
F(t,z)=\prod_{r=-9,-7,\ldots,9}(1-tz^r)^{-1},
\qquad
A_w=[t^5z^w]F(t,z),
\]

and let

\[
B_w=\sum_{r=-9,-7,\ldots,9}A_{w-r}.
\]

Then `B_w` is the weight-`w` multiplicity in the tensor product in (6).
For an `SL_2` module, the multiplicity of highest weight `12` is
`B_12-B_14`; exact expansion gives

\[
B_{12}=752,
\qquad
B_{14}=686,
\qquad
B_{12}-B_{14}=66.
\tag{7}
\]

This is not yet a modular-form dimension. Criterion 7.4 of
Clery--van der Geer imposes boundary valuations on these covariants. The
corrected companion valuation packet now resolves that finite problem:

\[
\boxed{
\dim\ker J_{(9,12)}=0.
}
\tag{8}
\]

The ten **unordered** `3+3` boundary partitions form a single orbit under the
standard `S_5`: represent a partition by the two other labels sharing the
block with the fixed label, and `S_5` is transitive on those two-subsets. One
representative divisor therefore suffices, but the substitution displayed in
Definition 7.1 has two block orientations. The former replay kept only the
block containing the marked root and falsely obtained nullity `15`. Exact
controls at weights `(6,1)`, `(4,5)`, and `(2,11)` show that both oriented
blocks must be imposed in the conservative marked implementation. The
corrected `9902 x 66` matrix has rank `66` over `Q` and modulo two audit
primes.

Finally, the Siegel `Phi` target at `(12,3)` has odd elliptic weight `15` and
vanishes. Thus every holomorphic `S_5`-invariant form at this weight is
already cuspidal. Equation (8) therefore proves the natural marked modular
channel zero without using the conditional `k=3` dimension formula. Calling
the corresponding term in the formal cohomological defect `G=0` still
requires the independently source-caveated Galois/cohomological realization;
the finite kernel does not supply that adapter.

## 8. Finite rows and same-characteristic recurrences

The existing exact finite rows are

| `p` | `Hhat_12(p)` | `a_p(f_-)` | forced `Tr(F_p|G)` from (3) |
|---:|---:|---:|---:|
| 3 | -3,708 | 1,236 | 3 |
| 5 | 287,250 | -57,450 | 5 |
| 7 | -449,624 | 64,232 | 7 |

Thus they impose

\[
\operatorname{Tr}(F_p\mid G)=p
\qquad(p=3,5,7),
\tag{9}
\]

under the conditional Shmakov-refined branch (3).  They do not imply `G=L`,
because three first-power Frobenius traces do not determine a Galois
representation; without the Galois realization of (1), even this forced-trace
interpretation is conditional.

A same-characteristic row at `q=p^2` would become genuinely discriminating
only after the dimension/purity/characteristic-polynomial type of `G` is fixed:
it would compare `sum gamma_i^2` with the Tate prediction `p^2`. No such row
is manufactured here. The covariant problem (8) is now resolved; a broad
point count is still unjustified before the channel adapter is resolved.

## 9. Proof ledger

### Unconditional finite or Euler-formal statements

- the standard-subgroup branching rule (4);
- Shmakov's Tate convention and the fact that the displayed formulas include
  nonregular `(12,0)`, subject to their stated hypotheses;
- independence of the alternating Euler class from the assumed ranks of the
  connecting morphisms;
- the exact `S_5` projection of Shmakov's displayed formal associated-graded
  terms to `2-4L` in (1);
- the correction of the official rows into `19` nonlift and `11` lift
  dimensions;
- the pre-holomorphic covariant dimension `66` in (7);
- transitivity of `S_5` on the ten unordered `3+3` boundary partitions;
- the source-calibrated two-orientation valuation rank `66` and zero kernel
  in (8), independently checked in two finite characteristics.

The two companion replays check the branching carriers, the three-term
Eisenstein projection, the lift/nonlift totals, (7), and the corrected
holomorphy kernel using exact arithmetic. Neither encodes a Galois
realization of the formal cohomological channels.

### Conditional or source-caveated

- realization of the formal `2-4L` expression as the actual compact-support
  `S_5 x Gal` Eisenstein Euler class, hence as Frobenius trace `2-4q`;
- `epsilon_Eis=L` and the branch (3) as identities of actual Galois/trace
  channels;
- the official `k=3` row decomposition as a Galois/cohomological proof that
  the formal channel `G` vanishes;
- interpreting the three finite equalities as an all-prime formula;
- the forced traces in (9), and identifying a representation from them.

### Open

- an independent Galois realization of the formal Eisenstein Euler class;
- transport of the exact modular zero in (8) to the formal stable/general
  Galois channel `G`;
- reconciliation of (9) with the conditional zero-invariant data;
- an all-`q` formula for `Hhat_12`.

## 10. Bounded next attack

The covariant surgery is closed. The next useful work is not another point
count or another valuation rank. It is an exact comparison between the
natural marked modular zero and the compact-support cohomological channel in
the formal defect, together with an independent boundary-geometric or
trace-formula justification of the Eisenstein Tate labels. Only that adapter
can turn the finite zero into an actual Galois/Frobenius identity;
connecting-morphism rank calculations alone cannot supply it.

## 11. Primary sources and novelty boundary

- Bergstrom, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917): regular Eisenstein theorem and
  explicitly expected `m=0` continuation.
- Roesner,
  [*Parahoric Restriction for GSp(4) and the Cohomology of Siegel Modular
  Varieties*](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf),
  especially Theorem 5.13 and the natural six-Weierstrass-point action.
- Shmakov,
  [*Cohomology of Local Systems on Siegel Threefolds with Square-Free
  Parahoric Level*](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0),
  especially the caveats on printed pages 4--5, the Tate convention on printed
  page 24, and Theorems 4.6.6--4.6.8 on printed pages 371--377.  The summary
  both qualifies those theorems by connecting-morphism assumptions and says
  Euler characteristics are unaffected by that issue, while separately
  recording the incomplete Galois-action treatment.
- Bergstrom--Clery,
  [*Dimension formulas for spaces of vector-valued Siegel modular forms of
  degree two and level two*](https://arxiv.org/abs/2309.04388), Theorem 5.3 and
  Remark 5.4.
- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
  the marked quotient, covariant map, and Criterion 7.4.
- [Official `(12,3)` data query](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0),
  used only to audit the conditional row classification.

No claim is made that Shmakov's theorem, the branching rule, or the covariant
framework is externally new.  The project-level contribution of this note is
the hypothesis audit, the differential-independent formal projection and its
conditional defect branch (3), the lift/nonlift correction, and the finite
66-dimensional proof target.  Nothing here proves RH or GRH, constructs a
motive, or promotes a local trace equality to a compatible global system.
