# The complete ternary-cube Chow-base Tor character table

Status: proposed exact source computation with a classical duality completion.
Frozen primitive source: `a895f47628b0bc7c7ee5e0392df2f79c24166f92`.
This concerns the Chow polynomial base Sym(Sym^3 V), not Sym(V tensor V tensor V).

## 1. Source, conventions, and what is computed

Let dim V=3 over a characteristic-zero field. Put

    R_r=(Sym^r V) tensor (Sym^r V) tensor (Sym^r V),
    W=Sym^3 V,     S'=Sym W,
    B_(i,j)=Tor_i^(S')(R,k)_j.

The multiplication W -> R_1 is the literal orbit-sum inclusion. GL(V)
acts diagonally, and S3 permutes the three factors. Write [lambda] for
the polynomial GL3 Schur module of partition lambda, padded to length
three. Write 1, epsilon, sigma for the trivial, sign, and standard
representations of this factor-permutation S3. This S3 is not an
arithmetic monodromy group introduced by a new cover.

The frozen exact Koszul calculation gives every torus-weight space and
all three S3 class traces in internal degrees 1,2,3. The chain dimensions
are respectively (27,10), (216,270,45), and (1000,2160,1215,120).
Every differential comes from actual W multiplication, and d^2=0 is
checked on every column. Rational elimination is performed in complete
weight blocks. This source computation, not a signed Hilbert numerator,
supplies the low-degree homology below.

The classical Chow-module theorem gives projective dimension 3 and
duality

    B_(3-i,7-j) = B_(i,j)^* tensor (det V)^7.                (1.1)

The factor-permutation sign twist is trivial because dim V-1=2. The
canonical degree-zero row is B_(0,0)=k and B_(i,0)=0 for i>0. Negative
internal degrees vanish. Thus (1.1) determines every remaining grade
from grades zero through three; grades above seven vanish. This completes
the Tor characters, not explicit matrices for a minimal free resolution.

## 2. Complete table

All nonzero entries are as follows; every omitted B_(i,j) is zero.

| i | j | GL3 x S3 representation | Dimension |
| --- | --- | --- | --- |
| 0 | 0 | [000] tensor 1 | 1 |
| 0 | 1 | [210] tensor sigma + [111] tensor epsilon | 17 |
| 0 | 2 | [222] tensor 1 + [330] tensor epsilon | 11 |
| 1 | 2 | [411] tensor sigma | 20 |
| 1 | 3 | [522] tensor (1+sigma) + ([531]+[432]) tensor epsilon | 65 |
| 2 | 4 | [552] tensor (1+sigma) + ([642]+[543]) tensor epsilon | 65 |
| 2 | 5 | [663] tensor sigma | 20 |
| 3 | 5 | [555] tensor 1 + [744] tensor epsilon | 11 |
| 3 | 6 | [765] tensor sigma + [666] tensor epsilon | 17 |
| 3 | 7 | [777] tensor 1 | 1 |

The total free ranks are (29,85,85,29). Their alternating characters give
the expected identity specialization

    N(I,T)=1+17T-9T^2-65T^3+65T^4+9T^5-17T^6-T^7.        (2.1)

In particular -9 in degree two means 11 generators minus 20 relations,
not nine relations and no generators. The trivial S3 sector already
contains the [222] generator. Its presence is essential even though it
is hidden by the negative total scalar coefficient.

For a compact independent check, the low-degree class traces in the
order (identity, transposition, three-cycle) are

    B_(0,1): (17,-1,-7),
    B_(0,2): (11,-9,11),
    B_(1,2): (20, 0,-10),
    B_(1,3): (65,-25,35).                                 (2.2)

These total traces alone do not identify the GL3 representations.
The separate replay compares every weight and class with the table.
For each Schur module it enumerates the interlacing patterns

    lambda1 >= mu1 >= lambda2 >= mu2 >= lambda3,
    mu1 >= nu >= mu2,

with weight (nu,mu1+mu2-nu,|lambda|-mu1-mu2). This is the usual
semistandard-tableau branching rule and gives its complete character.
The source and character routes are independent: the former uses
Koszul differentials; the latter uses these finite Schur patterns.
Equality of torus characters in each S3 isotypic sector identifies the
representations, since characteristic-zero representations are semisimple.

For grades at least four, [a,b,c]^* tensor det^7=[7-c,7-b,7-a].
This explicitly gives all the upper rows in the table from the lower
ones. No extra large chain calculation or assumed Betti symmetry is used.

## 3. Classical comparison and the precise added information

The finite Chow module, its duality, and related syzygy constructions
are classical; see Raicu--Sam--Weyman,
[On some modules supported in the Chow variety](https://arxiv.org/pdf/2108.10910),
Proposition 2.7, (3.2)--(3.5), and Example 4.5. In particular Example 4.5
already supplies the S3-invariant normalization component. Projecting this
table onto the trivial factor-permutation sector recovers exactly

    F0: [000] in degree0, [222] in degree2;
    F1: [522] in degree3;
    F2: [552] in degree4;
    F3: [555] in degree5, [777] in degree7.                  (3.1)

No novelty is claimed for that prior component or for the abstract
duality theorem. The repository result is a source-bound complete
GL3 x S3 character computation over the smaller Chow base, including
the other factor-permutation sectors and an authenticated replay of
the actual low-degree multiplication. It explains concretely why the
recurrence numerator is an Euler character rather than a Betti table.

The table supplies the free modules in an equivariant minimal resolution
up to isomorphism. It does not choose its differentials or a preferred
splitting, nor does it identify the Euler character with a finite
superdeterminant. Restricting these representations to inertia and taking
invariants of whole tensor terms remains necessary; projecting each factor
separately is not justified by this character computation.

## 4. Replay and falsifiers

The producer authenticates the frozen proof, primitive producer, and full
artifact before reading its three complete ternary-cube weight records.
It does not execute the old producer or repeat its rational eliminations.
It checks all rows against independent Schur patterns, the classical
normalization sector, the dual table, and the universal character Euler
identity at several declared diagonal matrices, including collisions.

Deleting the [222] generator, replacing 11-minus-20 by zero-minus-9,
or twisting the duality by a factor-permutation sign changes actual
weight/class data and is rejected. The full table is a consequence of
the finite exact source calculation plus (1.1), not an extrapolation
from scalar samples. The initial rank3/power3 case is an acknowledged
comparison case, not advertised as an untouched held-out example.
