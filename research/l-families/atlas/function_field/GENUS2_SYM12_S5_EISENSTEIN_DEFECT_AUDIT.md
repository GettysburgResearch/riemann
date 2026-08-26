# Genus-two Sym12 `S5` Eisenstein defect audit

Status: **THEOREM-SUPPORTED EISENSTEIN RESOLUTION; ONE STABLE CHANNEL OPEN**  
Scope: the `(j,k)=(12,3)` channel on the marked ambient stack
`A_2(w^1)=A_2[2]/S_5`  
Computation: finite character and weight algebra only; no point counts or family
enumeration

## 1. Outcome

The one-Tate Eisenstein ambiguity in the existing Sym12 packet is not an open
choice between two equally supported continuations.  Bergström--Faber--van der
Geer's `m=0` formula is explicitly an **expected** continuation of their regular
Eisenstein theorem.  Shmakov's later Theorems 4.6.6--4.6.8 are unconditional
level-two Eisenstein-cohomology formulas, include the nonregular highest weight
`(12,0)`, use the natural `GSp_4(F_2) \cong S_6` action, and use

\[
\mathbb L=\mathbf Q_\ell(-1),
\qquad
\operatorname{Tr}(F_q\mid\mathbb L)=q.
\]

Taking invariants under the standard `S_5` fixing one of the six level-two
labels gives

\[
\boxed{
e_{c,\mathrm{Eis}}
 (\mathcal A_2[2],\mathbb V_{12,0})^{S_5}
=2-4\mathbb L.
}
\tag{1}
\]

In the notation of
[`GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md`](GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md),

\[
\varepsilon_{\rm Eis}
=e_{\rm Eis}^{S_5}-(2-5\mathbb L)
=\mathbb L.
\tag{2}
\]

Consequently its source-relative master identity is sharpened from two open
channels to one:

\[
\boxed{
\widehat H_{12}=\mathbb L-\mathbb L f_- -G.
}
\tag{3}
\]

Here `G` is the stable/general `S_5`-invariant Galois channel.  Equation (3) is
the strongest conclusion of this audit.  It does **not** prove `G=0`, and it
does not prove the previously observed finite formula
`Hhat_12(p)=-p*a_p(f_-)` for every `p`.

There is also a new finite structural target for `G`: the full
`S_5`-invariant pre-holomorphic covariant space at this weight has dimension
exactly `66`.  Proving that its holomorphy-valuation subspace is zero would
settle the stronger assertion that there is no `S_5`-invariant cusp form at
weight `(12,3)`, hence in particular `G=0`.  No broad finite-field computation
is needed for that target.

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

The Klingen terms request elliptic weights `2` and `15` and vanish.  The
surviving invariant cohomology is therefore

| boundary piece | invariant degree data | alternating contribution |
|---|---|---:|
| Siegel `P_1` | `H_c^2 = 2*1`, `H_c^3 = 2*L` | `2-2L` |
| Klingen `P_2` | zero | `0` |
| Borel `P_0` | `H_c^3 = 2*L` | `-2L` |

This proves (1).  More explicitly:

- the two degree-two copies come from the `[5,1]` summand tensored with the
  two-dimensional weight-14 level-two newspace;
- the two degree-three Siegel copies are the `[5,1]` and `[6]` channels
  tensored with the unique level-one weight-16 form;
- the Borel degree-three term contains one `[6]` and one `[5,1]` copy, each
  with one Tate twist.

No assumption about connecting morphisms can change this Euler
characteristic.  Shmakov states these as `GSp_4(F_2) x Gal` modules, so the
Galois/Tate information is not being reconstructed from dimensions alone.

### Why the BFG branch no longer has equal status

BFG prove their Eisenstein formula for regular highest weight.  At `m=0` they
say that the displayed continuation is expected and impose the formal
convention

\[
S[\Gamma(2),2]:=-\mathbb L-1.
\]

That continuation gives `2-5L`.  Bergstrom--Clery likewise state their
`k=3,j>0` isotypical extension only conditional on the BFG nonregular
Eisenstein conjecture.  Shmakov's later nonregular theorem therefore selects
`2-4L`; it is not merely a second empirical normalization.

This is a source reconciliation, not a claim that the Shmakov formula or its
specialization is new mathematics.

## 5. Consequence for the Sym12 defect

The earlier packet established, relative to its exact ambient adapter and the
theorem-supported endoscopic term,

\[
\widehat H_{12}
=-\mathbb L f_-+\varepsilon_{\rm Eis}-G.
\]

Substitution of (2) gives (3).  It follows that the following three assertions
cannot all be promoted to all-`q` theorems:

1. `Hhat_12=-L*f_-`;
2. Shmakov's Eisenstein formula applies to the project ambient stack;
3. `G=0`.

This audit proves item 2 at the level of the cited stack, group action, and
Tate convention.  Hence an all-`q` proof of item 1 would instead force

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
the Eisenstein defect.  In particular, it cannot overrule the unconditional
Shmakov specialization.

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

This is not yet a modular-form dimension.  Criterion 7.4 of
Clery--van der Geer imposes boundary valuations on these covariants.  The
structural vanishing problem is now finite and explicit:

\[
\boxed{
\text{compute the holomorphy-valuation kernel inside this 66-dimensional
space.}
}
\tag{8}
\]

The ten `3+3` boundary partitions form a single orbit under the standard
`S_5`: represent a partition by the two other labels sharing the block with
the fixed label, and `S_5` is transitive on those two-subsets.  Therefore an
`S_5`-invariant covariant has the same valuation on all ten such divisors, and
one representative suffices for that part of Criterion 7.4.

Finally, the Siegel `Phi` target at `(12,3)` has odd elliptic weight `15` and
vanishes.  Thus every holomorphic `S_5`-invariant form at this weight is
already cuspidal.  A zero kernel in (8) would prove the full invariant cusp
space zero and would in particular prove `G=0` without using the conditional
`k=3` dimension formula.

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

under the audited master identity.  They do not imply `G=L`, because three
first-power Frobenius traces do not determine a Galois representation.

A same-characteristic row at `q=p^2` would become genuinely discriminating
only after the dimension/purity/characteristic-polynomial type of `G` is fixed:
it would compare `sum gamma_i^2` with the Tate prediction `p^2`.  No such row
is manufactured here, and no broad point count is justified before the exact
covariant problem (8) and the channel adapter are resolved.

## 9. Proof ledger

### Proved or theorem-supported

- the standard-subgroup branching rule (4);
- Shmakov's Tate convention and applicability to nonregular `(12,0)`;
- the exact invariant Eisenstein value `2-4L` in (1);
- `epsilon_Eis=L` and the one-open-channel defect (3), relative to the existing
  exact ambient/endoscopic identity;
- the correction of the official rows into `19` nonlift and `11` lift
  dimensions;
- the pre-holomorphic covariant dimension `66` in (7);
- transitivity of `S_5` on the ten `3+3` boundary partitions.

### Conditional or corroborative

- the official `k=3` row decomposition as a proof that `G=0`;
- interpreting the three finite equalities as an all-prime formula;
- identifying a representation from the three traces in (9).

### Open

- the valuation-kernel calculation (8);
- the unconditional value of the stable/general invariant channel `G`;
- reconciliation of (9) with the conditional zero-invariant data;
- an all-`q` formula for `Hhat_12`.

## 10. Bounded next attack

The best next pass is exact covariant surgery, not more point counting:

1. construct a rational basis for the 66 covariants in (6), using
   transvectants or exact `SL_2` highest-weight projection;
2. pull one basis through a representative `3+3` degeneration;
3. form the exact valuation/leading-coefficient matrix dictated by Criterion
   7.4;
4. compute its rational kernel and record whether it is zero;
5. only if a nonzero kernel survives, decompose its Hecke/lift type and then
   use one same-characteristic tower as a discriminator.

This route is finite, independently checkable, and attacks the sole remaining
channel in (3).

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
  Parahoric Level*](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf),
  printed page 24 and Theorems 4.6.6--4.6.8, printed pages 371--377.
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
the normalization audit, the resulting exact replacement of the two-gate
defect by (3), the lift/nonlift correction, and the finite 66-dimensional
proof target.  Nothing here proves RH or GRH, constructs a motive, or promotes
a local trace equality to a compatible global system.
