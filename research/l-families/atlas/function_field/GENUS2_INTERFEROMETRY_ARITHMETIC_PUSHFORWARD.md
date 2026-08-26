# Genus-two Frobenius-interferometry arithmetic pushforward

**Status:** exact bounded transform of source-locked complete histograms.

**Scope:** the member-uniform monic squarefree quintic families over exactly
`q=3,5,7`, transformed through the rational coefficient adapter for the three
compact-group selectors `P,D,S`. No finite field, polynomial, curve, root, or
family member is enumerated. Nothing below is an all-`q` law, an
equidistribution estimate, a monodromy classification, or an RH/GRH result.

## 1. Frozen sources and refusal contract

The arithmetic source is the complete joint `(a_D,b_D)` law in
`balanced_control_family_scan.json`. Its required LF-normalized SHA-256 is
`c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e`
and its required canonical payload hash is
`50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c`.
The producer also pins:

- the histogram producer at
  `7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b`;
- its primitive coefficient arithmetic at
  `f595dbf52d4265cfe2ea6888255f53df887fed77e204103f2b0dfd95e961f935`;
- its affine action at
  `32e440750b2832ec4cc84473187b4b1aa6396eda87c64f5ac845b2a96dc88f08`;
  and
- the selector producer at
  `48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7`.

The three required complete-member ledger hashes are respectively
`e38543c4526e6b330f012274398a258f2d021ddae18442d2f0094d42ec229790`,
`69fe496e1cca2090ca62bf7622ff34c3ab3aef1b9268dfb41c4df94d380a9d0a`,
and `c1d4ca30f45341de53af20ab4e4ca3f9bff79542146f1ac2230169eec9669655`.
Every digest is checked before the histogram is parsed or the selector module
is executed. Schema, coverage status, field ladder, atom counts, member mass,
and embedded primitive locks are then checked. A self-consistent replacement
with a different payload is rejected.

There are `32+81+138=251` source atoms, representing `162`, `2500`, and
`14406` members. The producer preflights the complete count and refuses above
the inclusive `4096`-atom cap. It performs one exact adapter visit per source
atom.

## 2. Normalization and exact adapter

For

\[
 T^4+a_DT^3+b_DT^2+qa_DT+q^2,
\]

the normalized selector quartic is

\[
 Z^4-e_1Z^3+e_2Z^2-e_1Z+1,
 \qquad e_1=-a_D/\sqrt q,\quad e_2=b_D/q.
\]

All three selectors are even in `e1`, so the locked packet's root-free adapter
is evaluated entirely in rational arithmetic at

\[
 A=e_1^2=a_D^2/q,\qquad e_2=b_D/q.
\]

With `I_(r,s)=p_r p_s-p_(r+s)`, the definitions are

\[
 P=I_{2,2}-I_{4,4},\qquad
 D=-I_{1,1}+2I_{1,5}+I_{4,4},\qquad
 S=-2I_{2,8}.
\]

The compact theorem gives ambient `USp(4)` mean zero for each and named
subgroup Haar signatures `(2,0,0)`, `(0,2,0)`, and `(0,0,2)`. Those are
compact probability integrals, not expected values asserted for these three
finite arithmetic families.

## 3. Exact frozen member-weight laws

The exact means, in selector order `P,D,S`, are:

| `q` | `mean(P)` | `mean(D)` | `mean(S)` |
|---:|---:|---:|---:|
| 3 | `-2584/2187` | `232/2187` | `8/6561` |
| 5 | `-57468/78125` | `16148/78125` | `7152/390625` |
| 7 | `-441712/823543` | `156896/823543` | `-2952/5764801` |

Thus `P` has a negative mean at all three fields, `D` a positive mean, and
`S` is much closer to zero and changes sign between `q=5` and `q=7`. This is
an exact three-field census, not a trend claim. The JSON freezes the complete
joint law, all three marginals, raw second moments, and the full covariance
matrix, retaining the covariance warning from the selector theorem.

The exact negative/zero/positive member counts are:

| `q` | `P: -/0/+` | `D: -/0/+` | `S: -/0/+` |
|---:|---:|---:|---:|
| 3 | `96 / 6 / 60` | `102 / 0 / 60` | `45 / 36 / 81` |
| 5 | `1410 / 30 / 1060` | `1464 / 0 / 1036` | `1211 / 250 / 1039` |
| 7 | `8484 / 42 / 5880` | `8820 / 0 / 5586` | `6552 / 1092 / 6762` |

For an auditable tail summary, define the outer absolute one-percent tail to
include all ties at the largest absolute threshold whose retained mass is at
least one percent. Its threshold and tied member count are:

| `q` | `P` threshold; count | `D` threshold; count | `S` threshold; count |
|---:|---:|---:|---:|
| 3 | `728/81; 6` | `1376/81; 9` | `4112/243; 6` |
| 5 | `5872/625; 40` | `10532/625; 40` | `48696/3125; 106` |
| 7 | `23368/2401; 252` | `40468/2401; 168` | `284040/16807; 462` |

The `P` outer tails are entirely negative and the `D` outer tails entirely
positive at all three fields. The `S` outer tails contain both signs at
`q=5,7`. Full tied sign counts and exact marginal atoms are in the JSON.

## 4. Exceptional coefficient strata

The same single pass evaluates three algebraic loci without importing or
enumerating any new family:

1. the formal integral `+q` reciprocal-quadratic split locus;
2. its repeated-factor sublocus `a_D^2-4b_D+8q=0`; and
3. the compact symmetric-cube coefficient curve
   `-q a^4+q a^2 b+q^2 a^2+b^3-2q b^2=0`, separated into the nodal ghost
   `(a,b)=(0,0)` and generic integral-trace candidates.

Their exact member counts are:

| `q` | integral split | repeated split | `Sym^3` curve | nodal ghost | generic integral-trace candidate |
|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 0 | 18 | 12 | 6 |
| 5 | 705 | 15 | 55 | 50 | 5 |
| 7 | 3570 | 84 | 378 | 336 | 42 |

The matched conditionals show a real but non-diagnostic concentration:

- `mean(P | integral split)` is `128/81`, `10112/29375`, and `45376/40817`,
  positive in every field although the full-family `P` means are negative.
- The repeated split locus is empty at `q=3`. At `q=5,7`, its conditional
  `D` means are `12544/1875` and `24812/2401`, far above the corresponding
  full-family means.
- On the generic integral-trace `Sym^3` candidates, `mean(S)` is `0` at
  `q=3` and `24` at both `q=5,7`. The nodal ghost has `S=0`; keeping it in the
  whole coefficient curve dilutes the curve conditional to `0`, `24/11`, and
  `8/3`.

At `q=5,7`, every generic integral-trace candidate and every repeated-split
member lies in the tied outer one-percent `S` tail. But no named exceptional
stratum meets the `P` or `D` outer one-percent tails, and none meets any outer
tail at `q=3`. Large selector values therefore cannot be read memberwise as
subgroup or endomorphism certificates.

The split condition is only a polynomial factorization predicate. The
`Sym^3` condition is only a coefficient-curve or integral-trace predicate.
Neither asserts polarization, arithmetic origin, compatible systems,
monodromy, or motives.

## 5. Uniform affine-orbit law: exact refusal

The source affine action changes `a_D` only by sign and fixes `b_D`, so all
three selectors are orbit-invariant. However, the frozen orbit counts are
aggregated only by the older balanced statistic `B`. That aggregation does
not determine the selector orbit law: at `q=3,5,7`, respectively `3`, `10`,
and `17` `B`-buckets contain multiple selector triples, carrying `66`, `966`,
and `7896` members.

The JSON records the ambiguous buckets and refuses to allocate their aggregate
orbit counts. Consequently every member-weight statement above is exact,
while no uniform-coarse-orbit selector law is claimed.

## 6. Exact/conjectural boundary and replay

Every displayed `q=3,5,7` law, mean, covariance, sign count, tied tail, and
conditional is exact. No all-`q` formula or conjecture is proposed from three
fields. A natural next theorem is to evaluate the exact all-`q` joint moments
required by the three adapter polynomials and then prove an error term before
comparing finite means with compact Haar signatures.

Replay from the repository root with:

```text
python research/l-families/atlas/function_field/genus2_interferometry_arithmetic_pushforward.py --check
python -m unittest tests.test_genus2_interferometry_arithmetic_pushforward -v
python -O -m unittest tests.test_genus2_interferometry_arithmetic_pushforward -v
```
