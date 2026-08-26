# Genus-two Sym12 `S5` Eisenstein defect audit

Status: **STABLE CHANNEL CLOSED; DIFFERENTIAL-INDEPENDENT FORMAL EISENSTEIN
PROJECTION; EISENSTEIN GALOIS REFINEMENT CAVEATED**

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
Galois-cohomology theorem.  Independently, the corrected modular-zero adapter
now proves `G=0` for the positive semisimplified form-attached channel.  Thus
the conditional Shmakov branch simplifies to

\[
\widehat H_{12}=\mathbb L-\mathbb Lf_-.
\]

It still does not prove
the previously observed finite formula
`Hhat_12(p)=-p*a_p(f_-)` for every `p`.

The strongest unconditional result is instead finite: the full `S_5`-fixed
pre-holomorphic covariant space has dimension `66`, and the corrected
two-orientation valuation matrix has rank `66`.  Thus its holomorphic—and,
because the `Phi` target has odd weight, cuspidal—subspace is exactly zero.
This proves absence of the natural marked modular channel without any broad
finite-field computation.  The source audit in
[`GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md`](GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md)
closes the remaining adapter: Roesner's arbitrary-weight stable direct-sum
theorem identifies the stable Galois multiplicities with the holomorphic
general-type multiplicities, including at `m=0`.  Endoscopic and Eisenstein
terms remain separate.

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
(3).  The exact stable adapter proves `G=0`, so the following two assertions
cannot both be promoted to all-`q` theorems:

1. `Hhat_12=-L*f_-`;
2. Shmakov's formal `2-4L` expression realizes the actual Galois Euler class
   on the project ambient stack;

This audit verifies the stack, group action, Tate convention, and
differential-independent formal projection behind item 2, but not its missing
Galois realization.  The former formal escape `G=L` is no longer available:
`G` is a positive form-attached stable channel, not an arbitrary residual
Euler symbol.

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
therefore only conditional corroboration of the independently proved `G=0`.
In particular, it neither proves nor disproves the Galois-caveated Shmakov
formal specialization.

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
channel zero without using the conditional `k=3` dimension formula. BFG's
form-attached channel definition, Bergstrom--Clery's general/Yoshida direct
sum, and Roesner's arbitrary-weight Corollary 5.20 then imply

\[
\boxed{G=0}
\]

as a semisimplified `S_5`-fixed Galois representation. This implication does
not realize the Eisenstein associated graded as an actual Galois Euler class.

## 8. Finite rows and same-characteristic recurrences

The existing exact finite rows are

| `p` | `Hhat_12(p)` | `a_p(f_-)` | Shmakov-formal prediction with `G=0` | discrepancy |
|---:|---:|---:|---:|---:|
| 3 | -3,708 | 1,236 | -3,705 | `+3` |
| 5 | 287,250 | -57,450 | 287,255 | `+5` |
| 7 | -449,624 | 64,232 | -449,617 | `+7` |

Thus the formal `2-4L` branch misses each stored row by exactly `+p` after the
exact stable closure. The rows are finite corroboration of the `2-5L` branch,
not a proof of its Galois realization or of any fourth prime. A
same-characteristic row can no longer discriminate the stable channel, which
is zero; the remaining target is the Eisenstein Galois class itself. No broad
point count is justified for that source-normalization question.

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
  in (8), independently checked in two finite characteristics;
- the theorem-grade form-to-stable adapter and hence `G=0` for the positive
  semisimplified `S_5`-fixed general channel.

The companion replays check the branching carriers, the three-term
Eisenstein projection, the lift/nonlift totals, (7), and the corrected
holomorphy kernel using exact arithmetic. The stable adapter is a
primary-source theorem chain rather than a new numerical replay; none of the
replays realizes the Eisenstein Galois class.

### Conditional or source-caveated

- realization of the formal `2-4L` expression as the actual compact-support
  `S_5 x Gal` Eisenstein Euler class, hence as Frobenius trace `2-4q`;
- `epsilon_Eis=L` and the branch (3) as identities of actual Galois/trace
  channels;
- the official `k=3` row decomposition, which is no longer needed to prove
  that the channel `G` vanishes;
- interpreting the three finite equalities as an all-prime formula;

### Open

- an independent Galois realization of the formal Eisenstein Euler class;
- an all-`q` formula for `Hhat_12`.

## 10. Bounded next attack

The covariant surgery and the stable adapter are closed. The next useful work
is not another point count, valuation rank, or `S_6` decomposition. It is an
independent boundary-geometric or trace-formula justification of the
Eisenstein Tate labels on the natural marked quotient. Connecting-morphism
rank calculations alone cannot supply the missing Galois action.

## 11. Primary sources and novelty boundary

- Bergstrom, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917): form-attached rank-four
  channel, regular Eisenstein theorem, and explicitly expected `m=0`
  continuation.
- Roesner,
  [*Parahoric Restriction for GSp(4) and the Cohomology of Siegel Modular
  Varieties*](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf),
  especially pp. 95--99, Theorem 5.13, Corollary 5.20, and the natural
  six-Weierstrass-point action.
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
  degree two and level two*](https://arxiv.org/abs/2309.04388), equation (3),
  Theorem 5.3, and Remark 5.4.
- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
  the marked quotient, covariant map, and Criterion 7.4.
- [Official `(12,3)` data query](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0),
  used only to audit the conditional row classification.

No claim is made that Shmakov's theorem, the branching rule, or the covariant
framework is externally new.  The project-level contribution of this note is
the hypothesis audit, the differential-independent formal projection and its
conditional defect branch (3), the lift/nonlift correction, the exact
66-dimensional marked zero, and the source-locked stable adapter. Nothing here
proves RH or GRH, constructs a new motive, or promotes a local trace equality
to a compatible global system.
