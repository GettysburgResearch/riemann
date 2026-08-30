# Live shared-fibre collisions survive Boolean and one-sided product aggregation

Status: **exact live-source support witnesses and fixed source variance;
native coefficient-family nonfactorization remains open**

Scope: the canonical equal-pair Boolean source of the locked L-106120 and
T-106140, at explicitly frozen finite horizons. Two exact owner panels prove
that the live residue map need not be injective, even after single-side
equal-product aggregation. This is not a full occupancy census, a bound for
the complete signed source, a geometric descent theorem, or a proof of RH.
RH and GRH remain unproved.

Exact source lock:
[ffps_live_shared_fibre_collisions.sources.json](ffps_live_shared_fibre_collisions.sources.json).

Bounded producer:
[ffps_live_shared_fibre_collisions.py](ffps_live_shared_fibre_collisions.py).

Canonical output:
[ffps_live_shared_fibre_collisions.json](ffps_live_shared_fibre_collisions.json).

What was actually run: two locked owner panels, two locked history controls,
source authentication, and 21 unit tests in normal and optimized Python.

Smallest remaining gap: specify an admissible native coefficient family and
produce two members with the same residue aggregate and different literal
diagonal energy.

## 0. What changes

The predecessor left two genuinely separate questions open:

1. can a complete live shared fibre contain distinct literal atoms in one
   physical residue cell?
2. do the admissible native coefficient vectors have enough freedom to make
   the Wick scalar fail to factor through their residue aggregate?

This packet answers the first **yes**. It does not answer the second.

At each of two frozen horizons there are four different arithmetic
interactions in one cell. Their left physical products are distinct, their
right physical products are distinct, and all eight owner labels are
different. Hence this collision is not an artifact of leaving two equal
Boolean histories uncombined. At the literal ordered-history resolution,
the same panel contains at least sixteen atoms in that cell.

Consequently the corresponding live-support occupancy map has a nontrivial
kernel. The fixed-fibre operator has a genuine `-d` eigenspace on that
kernel. These are statements about the operator on its live support, not
about the sign or cancellation of the one native coefficient vector.

A second calculation gives a nonconstant native history vector with exact
within-cell variance. It is explicitly a fixed source variance calculation,
not a pair of admissible native inputs with equal aggregate and different
diagonal energy.

## 1. Frozen source contract

The replay authenticates eleven exact Git blobs.

| source | commit | blob | content used |
|---|---|---|---|
| L-102883 | `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc` | `b8a6eed2c8dda7d0ed28a8dd18fc57387e4c2e7b` | ordered balanced histories and single-side equal-product collapse |
| L-102887, horizon-safe pair gauge | same | `383aa27fee269645e45c26c12fbd4a97a6b337a8` | squarefree owner kernel, clean completion, unique physical product |
| L-102958 | same | `3b72653ea5f05405c587be165faf7ab2c52c3f2b` | ratio-eight physical support |
| L-102962 | same | `d8f4557df6dc37e6b605b1821c5b8ab028136398` | canonical equal-pair allocation |
| L-106080 | `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b` | `346cc52420ec65457c2a5accc045d4a85635cc24` | exact Boolean Vaughan coefficient |
| L-106120 | same | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | complete shared fibre and all source labels |
| L-106131 | same | `37722c3f36ec7d1681f34d4329a3795e5028f7ae` | literal Wick diagonal before collapse |
| L-106191 | same | `85c4ef92ead7d8b235f9c195c3c0acd16d16030f` | source-dual rescaling and centered incidence |
| T-106140 | same | `d5be8e376c88b63de0be19e0d9e8791624e99ae2` | full owner/source recombination and native coefficient firewall |
| frozen-source terminal audit | `99163530fdd311f42e138e33851a94e26c6b0f32` | `5540f451b41c234066d024d577de50701cf715c7` | exact cutoff and active `[Y/8,2Y]` source window |
| shared-fibre occupancy theorem | `6675c19f20760301d8c91dedc4a7836170003512` | `3e7fff53f5cdbb3a660b24b2e765f4ac35c434c3` | `B_R=R* S R-dI` and the distinction between support and coefficient freedom |

The atom resolution is declared, not changed mid-proof. The literal
resolution retains ordered Boolean factorization slots. The coarser
resolution first combines all histories of each one-sided physical product.
Both resolutions retain the complete owner sums before the family square.
Their diagonal-energy conventions differ; no equality of their Wick
normalizations is asserted.

## 2. Two-prime Boolean cores are nonzero live source coordinates

On one squarefree support, let

\[
 a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf},
 \qquad b_U=a_U\star a_U\star\mu_{\rm sf},
 \qquad U=\lfloor Y^{1/6}\rfloor.
\tag{2.1}
\]

If `r,s` are distinct primes greater than `U`, then

\[
 a_U(r)=a_U(s)=-1.
\]

There are exactly two nonzero ordered balanced histories on `{r,s}`:

\[
 (r,s,1),\qquad(s,r,1),
\]

each with coefficient `+1`. Thus

\[
 \boxed{b_U(rs)=2.}
\tag{2.2}
\]

With two distinct owner labels, the full occurrence has depth four. Its
canonical equal-pair share is `1/binom(4,2)=1/6` per history and `1/3`
after these two histories are combined. Neither is zero.

This uses the canonical equal-pair gauge, not an extra minimum-owner
restriction. L-102962 permits every unordered pair on the active cofinal
source. In the witnesses below the owner products also satisfy the native
owner/core size inequalities directly.

The producer checks (2.2) twice: by enumerating the ordered balanced
histories and independently through the Vaughan identity

\[
 b_U=\mu_{\rm sf}-2\mu_U+
 \mu_U\star\mu_U\star\mathbf1_{\rm sf}.
\tag{2.3}
\]

## 3. LIVEOCC-1: an arithmetic collision after history aggregation

Take

\[
 Y=2^{30},\quad U=32,\quad
 g=37,\quad \ell=43,\quad\rho=47,\quad c=\ell,\ d=\rho.
\tag{3.1}
\]

Use the two left and two right owner pairs

| side | owner labels | product | physical product |
|---|---|---:|---:|
| left 0 | `(5,31)` | `P_0=155` | `N_0=392348555` |
| left 1 | `(2,101)` | `P_1=202` | `N_1=511318762` |
| right 0 | `(3,137)` | `Q_0=411` | `M_0=1242913731` |
| right 1 | `(7,71)` | `Q_1=497` | `M_1=1502988137` |

Here `N_i=P_i(37*43)^2` and `M_j=Q_j(37*47)^2`.
Every one of the four ordered interactions `(N_i,M_j)` is clean:

- all eight owner labels are distinct, avoid `67`, and avoid `37,43,47`;
- the full squarefree cores have gcd `37`, leaving reduced cores `43,47`;
- both full cores consist of two primes greater than `U`, so (2.2) applies;
- every physical product lies strictly inside `[Y/8,2Y]`;
- every cross interaction has `1/8<N_i/M_j<8`;
- the left owner products share one dyadic block, as do the right products;
  the two `N_i` share one physical dyadic block, as do the two `M_j`;
- all labels satisfy the horizon-safe completion bound;
- `ell|N_i`, `ell` does not divide `M_j`, `rho|M_j`, and `rho` does not
  divide `N_i`.

The fixed owner congruences are exact:

\[
 P_1-P_0=47=\rho,
 \qquad Q_1-Q_0=86=2\ell.
\tag{3.2}
\]

Therefore the shared-fibre physical map gives, for all four atoms,

\[
 \begin{aligned}
 x_{ij}&=-\rho^2Q_j\pmod\ell=3,\\
 y_{ij}&=\ell^2P_i\pmod\rho=36,\\
 \sigma&=\kappa_{43}(Q_j)=+1,
 \qquad\tau=\kappa_{47}(P_i)=+1.
 \end{aligned}
\tag{3.3}
\]

Thus all four lie in the same genuine fibre

\[
 \iota=(37,43,47,+1,+1)
\]

and the same residue cell `(3,36)`.

### Why the collision survives the source-authorized aggregation

L-102887 identifies the one-sided owner product as the squarefree kernel of
`N=P a^2`; its owner pair and core are unique. Since `P_0!=P_1`, the left
physical products remain distinct after single-side equal-product
aggregation. The right products are likewise distinct.

Consequently all four pairs `(N_i,M_j)` remain different after both
one-sided aggregations. Their physical ratios, pair products, and
differences are also pairwise distinct in this fixture. No unspecified
further complete-output quotient is being identified with these maps.

At the literal ordered-history resolution, each of the four arithmetic
pairs has `2*2=4` nonzero histories. Hence there are at least sixteen
distinct literal atoms in the same cell. The full fibre can contain more
atoms; the proof does not require listing them.

## 4. Independent held-out conductors

The same checks are repeated at different marked conductors and a different
nonperfect-sixth-power dyadic cutoff:

\[
 Y=2^{33},\quad U=45,\quad
 g=53,\quad\ell=59,\quad\rho=61.
\tag{4.1}
\]

The owner products are

\[
 P_0=7\cdot19=133,\quad P_1=2\cdot97=194,
 \qquad
 Q_0=5\cdot103=515,\quad Q_1=3\cdot211=633.
\tag{4.2}
\]

Again the eight owner labels are distinct and clean, and

\[
 P_1-P_0=61=\rho,
 \qquad Q_1-Q_0=118=2\ell.
\tag{4.3}
\]

Both original cores are two primes above the frozen cutoff. All four
interactions lie in the active source window and ratio-eight support, with
common one-sided dyadic blocks. The exact output records the resulting
classes, cell, and physical products. Tests also reverse the left/right
orientation while retaining the correct sign in the `x` coordinate.

This is a held-out finite witness, not a claim about the density of
collisions in an asymptotic conductor family.

## 5. Exact live-support operator consequence

Write

\[
 d=(1-1/\ell)(1-1/\rho)>0.
\]

On any `n` distinct literal atoms in one cell, the principal submatrix of
the predecessor's exact Wick operator is

\[
 B_{\rm cell}=d(J_n-I_n).
\tag{5.1}
\]

Every vector supported on those atoms with coordinate sum zero lies in the
kernel of the full residue aggregation `R`, even when the full fibre has
additional atoms. Hence

\[
 B_Rh=-dh.
\tag{5.2}
\]

The arithmetic panels therefore force at least a three-dimensional
residue-kernel after Boolean histories have been combined; the declared
literal-history resolution forces at least a fifteen-dimensional kernel.
At that literal resolution, the sixteen-point principal submatrix has
eigenvalues `15d` once and `-d` fifteen times. The full live-support operator
is indefinite: the all-ones vector on the panel has positive Rayleigh
quotient, and a within-cell difference has negative Rayleigh quotient.

This closes a support gate that the ambient-envelope theorem could not
close. It also makes the predecessor's arbitrary-coefficient forgetting
criterion applicable to actual live support: an adapter required to work
for **every coefficient vector on this support** cannot retain only `Rz`.

It does **not** prove that every such coefficient vector is native. In the
two-by-two owner panel, the native entries have the constrained form

\[
 z_{ij}(t)=\overline{A_i(t)}B_j(t),
\tag{5.3}
\]

with their literal arithmetic weights and source parameters. Those four
entries are not declared independent knobs.

## 6. Fixed native history variance is a separate exact diagnostic

First, the small calibration shows why collisions alone do not imply native
variance. At

\[
 Y=2^{24},\ U=16,\ g=17,\ \ell=43,\rho=47,
 \quad P=2\cdot3,\ Q=5\cdot7,
\]

the active physical products are `3206166` and `22344035`, and the cell is
`(42,2)`. The four ordered histories have equal coefficient ratios
`(1,1,1,1)`. Their native vector has zero projection to the within-cell
sum-zero space, despite the noninjective support map.

For a nonconstant native control, take

\[
 \begin{gathered}
 Y=2^{54},\quad U=512,\quad
 G=\{11,13,17,19\},\quad g=46189,\\
 \ell=1031,\quad\rho=521,\quad
 P=2\cdot3,\quad Q=5\cdot7.
 \end{gathered}
\tag{6.1}
\]

The full cores are `g*ell` and `g*rho`. Their physical products are
`13606477271387286` and `20268453388818635`, both strictly inside the
active window with ratio-eight overlap. The common core is below
`Y^(1/3)=262144`; this is not forced into the very-large-common-core regime.

Every two-element product from `G` is at most `323<U`, while every
three-element product is at least `2431>U`. Also `ell,rho>U`. The subset
formula

\[
 a_U(S)=-\sum_{D\subseteq S,\ \prod D\le U}(-1)^{|D|}
\tag{6.2}
\]

therefore gives exactly ten nonzero balanced histories on `G union {ell}`:

- `(ell,G,1)` and its ordered swap have coefficient `3`;
- for each `p in G`, `(ell,G minus {p},p)` and its swap have coefficient
  `-1`.

The right core has the identical coefficient pattern with `rho` in place
of `ell`. In particular each complete balanced coefficient is `-2`, not
zero. Each one-sided occurrence has seven labels and equal-pair weight
`1/binom(7,2)=1/21`.

Factor out the common non-Boolean source multiplier, physical reciprocal
weight, Mellin phase, and bilateral owner share `1/441`, calling their
product `w`. At the literal ordered-history resolution, the hundred
bilateral coefficient ratios are:

| coefficient ratio | multiplicity |
|---:|---:|
| `9` | `4` |
| `-3` | `32` |
| `1` | `64` |

All hundred histories have the same arithmetic pair and residue cell.
Exactly,

\[
 \sum z_\omega=4w,\qquad
 D=676|w|^2,
\tag{6.3}
\]

and their within-cell source variance is

\[
 \boxed{
 D-\frac{|\sum z_\omega|^2}{100}
 =\frac{16896}{25}|w|^2.}
\tag{6.4}
\]

The Wick value of this history subpacket is correspondingly

\[
 \boxed{d(16-676)|w|^2=-660d|w|^2.}
\tag{6.5}
\]

This is not the complete native fibre. Other arithmetic tuples and their
cross terms have not been summed. Moreover this particular hundred-history
block becomes one arithmetic pair under one-sided equal-product
aggregation; its representation ledger may be handled by an inherited
closed estimate. It is not an obstruction to that estimate and is not a
global noncancellation theorem.

There is also an internal four-history subset with ratios
`(-3,1,1,1)`, sum zero and diagonal energy `12|w|^2`. Its presence is an
exact combinatorial fact. Selecting that subset changes the source region;
it is not automatically an admissible full native input. Neither it nor
(6.4) is used to claim native coefficient-family nonfactorization.

## 7. What remains open

To prove failure of residue-only reconstruction **on an admissible native
family**, one must exhibit two admissible native inputs on the same
declared atom resolution with

\[
 Rz=Rz',\qquad D(z)\ne D(z').
\tag{7.1}
\]

No such pair is supplied here. The following substitutes do not establish
(7.1): unequal coefficients in one fixed vector; nonzero within-cell
variance; an internal zero-sum subset; replacing a vector by its cell mean;
or comparing diagonal energies before and after changing the atom
resolution.

The exact updated boundary is:

| question | status |
|---|---|
| existence of a live duplicate residue cell | **PROVED BY TWO SOURCE-LOCKED OWNER PANELS** |
| persistence after Boolean-history and single-side equal-product aggregation | **PROVED FOR THOSE PANELS** |
| nontrivial kernel and `-d` eigenspace on live support | **PROVED** |
| fixed native history variance | **PROVED AT THE DECLARED LITERAL RESOLUTION** |
| native coefficient-family nonfactorization | **OPEN** |
| full occupancy, multiplicity growth, and coefficient distribution | **OPEN** |
| complete native fibre sign or global signed cancellation | **OPEN** |
| ONEPLACEWEIL, RELPARTFROB, RELTRACE, WCADD/WCCORR, WCKUM, principal binding | **OPEN** |

The smallest next task is now a coefficient-family typing problem, not
another ambient residue sweep. Declare exactly which source parameters or
linear region maps the intended adapter must respect, keep the horizon,
cutoff, owner gauge, and atom resolution fixed, and test (7.1) within that
declared family. In parallel, the universal atom-plus-diagonal adapter
remains justified for arbitrary coefficient vectors on the now-certified
live noninjective support.

No external novelty claim is made for Boolean convolution, congruence
collisions, or incidence spectra separately. The advance is the exact
source-locked live witness and the separation of support noninjectivity,
fixed source variance, and admissible coefficient freedom.

## 8. Replay boundary

```text
python -B research/l-families/atlas/function_field/ffps_live_shared_fibre_collisions.py --check
python -B -O research/l-families/atlas/function_field/ffps_live_shared_fibre_collisions.py --check
python -B -m unittest tests.test_ffps_live_shared_fibre_collisions
python -B -O -m unittest tests.test_ffps_live_shared_fibre_collisions
python -B -m ruff check research/l-families/atlas/function_field/ffps_live_shared_fibre_collisions.py tests/test_ffps_live_shared_fibre_collisions.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_live_shared_fibre_collisions.py tests/test_ffps_live_shared_fibre_collisions.py
```

The replay authenticates eleven blobs, checks two fixed owner panels and
two fixed history controls, enumerates Boolean assignment cubes of at most
`3^5=243`, and materializes coefficient vectors of length at most `100`.
It uses exact integers and rationals, no floating-point arithmetic, no
conductor-family sweep, and no curve, sheaf, or zero computation.

The arithmetic class is `MIXED`: `CERTIFIED_INTEGER_COVERAGE` for complete
enumeration of each declared finite Boolean assignment cube and exact
integer source predicates, and `EXACT_RATIONAL` for Wick energies. These
coverage claims apply only to the declared finite supports, not to the
complete live fibre. The rounding contract is exact, with no rounding.

The canonical output binds the producer, tests, note, and source manifest by
SHA-256 after CRLF-to-LF normalization. The exact commit binds the canonical
output itself. Acceptance requires equality with a fresh recomputation,
including those hashes, and resolution of every primitive Git blob at its
locked commit. The Vaughan identity is replayed independently of the
ordered-history convolution; the tests recompute normalization, integer
cutoffs, congruences, and rational controls. No independent external
implementation or complete native coefficient family was replayed.

RH and GRH remain unproved.
