# Concrete Segre--Chow change-of-rings comparison

Status: proposed source-bound finite theorem, awaiting independent frozen review.
Scope: characteristic-zero finite graded algebra, not a spectral determinant,
automorphic construction, or RH statement. This packet extends the proposed
proof-only PR782 interface by computing maps. It does not alter its sources.

Authoring base: `17c7624a0bd56c5356d00278b2a846d2efdbdccc`.
Frozen comparison sources: PR782 at
`552fe0b78fd96b02fe5836269e6795a992c935be`; PR769 at
`f36576faf7853a56bd1f64edd29c4df662cae849`; accepted ambient bridge at
`4a317ea5c9d7aa016fba58a1d74746e437329ec7`, independently reviewed at
`acd91a621244872d49e0e4dfde76775879eadfc1`.

## 1. The literal source and comparison

Let V=Q^d, E=V^(tensor m), W=Sym^m(V), and
R_r=(Sym^r V)^(tensor m), with coordinatewise monomial multiplication.
For each content orbit of words in E, take its orbit sum as a W generator.
Choose the lexicographically first word in that orbit, and take every other
word minus that first word as a basis for C=ker(averaging:E->W). This is a
marked basis of the canonical equivariant complement, not a preferred basis.

The bicomplex is

    K_(p,q)=Lambda^p C tensor Lambda^q W tensor R,
    d=d_C+(-1)^p d_W.

All multiplications are performed in R before quotienting. First taking
W-homology gives E1_(p,q)=Lambda^p C tensor B_q, where
B_q=Tor_q^(Sym W)(R,Q) has its induced Sym(C)-module structure. Taking the
actual induced C differential gives

    E2_(p,q)=Tor_p^(Sym C)(B_q,Q).

The total complex computes ambient Tor over Sym(E). An Euler-polynomial
comparison alone cannot determine either the C action or higher differentials.

## 2. Fixed finite panel and predictions, before computation

Primary panel: (d,m)=(3,3), all diagonal-torus weight blocks in internal
degrees 0,1,2,3. Compute actual W differentials, homology representatives,
quotient coordinates, and the C action. Verify every image as a cycle and
every boundary compatibility, then construct the horizontal complexes.

The inherited comparison targets are the full Chow Tor characters from
PR769 and ambient quadratic/cubic dimensions 162 and 1720 from the accepted
ambient bridge. These are comparison targets, never assigned matrix ranks.

In degree two the expected filtration pieces have dimensions 142 and 20.
In degree three write a for the actual rank of

    C tensor B_(1,2) -> B_(1,3).

The preregistered, falsifiable prediction is a=65 and hence zero d2 in this
internal degree. If a<65, the missing actual transgression must be computed;
the prediction will be recorded as failed, not replaced retroactively.
The other predicted horizontal rank is 187 for
Lambda^2 C tensor B_(0,1) -> C tensor B_(0,2). This would leave a
1445-dimensional E2_(2,0) before any higher differential. Neither rank is
to be inferred from the known final ambient dimensions.

For full character checks use diagonal GL_d torus weights and all factor
permutation conjugacy classes. For m=3 take representatives
identity, (01), (012). Quotient class traces must be calculated from actual
induced matrices, not assigned by dimensions. Summed E-infinity characters
must agree with a separately constructed ambient Koszul complex.

Held-out source panel: (d,m)=(3,4), internal degrees through two, all weights
and S4 representatives identity, (01), (01)(23), (012), (0123).
The predicted ambient quadratic traces, in that order, are

    (2025, 189, 45, 9, 3).

These follow independently from Sym^2(E)-R_2 and are not predictions of the
individual Chow homology ranks. The all-weight target uses the corresponding
tensor-cycle character formula, not these five total numbers alone.

## 3. Acceptance and workload plan

Use sparse exact rational linear algebra with complete weight blocks and
fixed deterministic pivots. Retain maps, ranks, homology/quotient coordinates
and character records or their independently replayable constructions.
Integer numerator and denominator bit lengths are capped. All rank results
must come from literal columns and exact reduction; no numerical tolerance,
modular-only rank, or rank inferred from an Euler numerator is accepted.

Initial caps: d=3; m in {3,4}; internal degree <=3 for m=3 and <=2 for m=4;
each block <=1024 rows and <=2048 columns; at most 100000 total basis cells;
rational numerator/denominator <=4096 bits; JSON depth <=48 and bytes <=8MiB.
A resource refusal is retained and requires a separately identified design
amendment before any cap increase. The proof is not bounded by finite caps.

The source/fixture contract will authenticate exact Git blobs plus LF hashes,
the producer, this note, tests and typed manifest. Normal and optimized modes
must reject malformed types, duplicate keys, altered maps and source drift.
The release will state which inherited eliminations were rerun and which
source theorems were imported. Canonical arithmetic taxonomy: MIXED with
EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE; rounding: none.

## 4. Intended boundary

This does not claim a general closed formula for individual Chow Tor groups,
degeneration in every degree, a canonical printed equivariant resolution,
or an identification of spectral collisions with source-module rank drops.
The action of g specializes a character of a fixed module; its reduced
recurrence order can change without any change in those Tor spaces.

The top Hessian comparison is secondary and is not part of this initial
finite panel. Classical Koszul/change-of-rings machinery, the Chow module,
canonical duality and the known ambient syzygy characters retain their
primary-source attribution. No external novelty is asserted by this design.

## 5. Separate degree-four design amendment

After completion of the degree-three panel (rank a=65) and the held-out
degree-two m=4 panel, but before computing degree four, extend only the
(d,m)=(3,3) Chow bicomplex to internal degree four. Keep all other caps.
The new falsifiable prediction is that the horizontal map
Lambda^2 C tensor B_(1,2) -> C tensor B_(1,3) has rank 1105, and that
the actual transgression d2:E2_(2,1),4 -> E2_(0,2),4 has rank 65.
This predicts non-degeneration, not degeneration, of this comparison.
Neither statement follows merely from the Euler characteristic: a later
d3 from E3_(3,0),4 could in principle affect the same target.

Compute the transgression by lifting each horizontal cycle to literal
W-Koszul chains, solving its C-image as a W boundary, and applying C again.
Retain the actual sparse transgression matrices and at least one full
nonzero zigzag. Check every chain identity exactly. Any failed prediction,
resource refusal, or new design change will remain in the history.

### Resource refusal and bounded amendment

The first degree-four run stopped at the unchanged 1024-row cap while
constructing E1_(3,0),4; it did not compute a transgression. A subsequent
allocation-only count from the pinned Chow characters gives maximum 1126
rows and 23401 total E1 cells (31609 W-chain cells). Before retrying, raise
only the row cap to 1152. Keep the 2048-column, 100000-cell, bit and byte
caps, all predictions, and the complete weight coverage unchanged.

## 6. Native proof and finite certificate semantics

The orbit-sum inclusion identifies W with the invariant tensors E^(S_m).
The averaging idempotent is characteristic-zero equivariant for GL(V) and
S_m. Its kernel C gives E=W direct-sum C. The displayed word differences
span exactly this kernel: their sum of coefficients on every content orbit
is zero, and they are independent by their unique non-anchor coordinates.
The orbit sum is not in their span. Thus these marked coordinates do not
change the canonical splitting or the underlying equivariant objects.

For an increasing list w_1,...,w_q of W basis indices, the literal map is

    d_W((w_1 wedge ... wedge w_q) tensor r)
      = sum_a (-1)^(a-1) (w_1 wedge ... omit w_a ... wedge w_q)
          tensor (w_a r).

Here w_a r means the sum of its distinct words multiplied factorwise into
the m monomials of r. Commutativity cancels every pair in d_W^2. The same
formula defines d_C. They commute before the total-complex sign; hence
d_C+(-1)^p d_W squares to zero. The Koszul resolution of Q over Sym(E)
therefore identifies the total homology with ambient Tor. Filtering by C
degree, with fixed finite internal grade, is a bounded filtration. Taking
W homology and then C homology gives precisely E1 and E2 above; the higher
maps have bidegree (-r,r-1). This construction proves convergence without
any degeneration assumption or freeness of B_q over Sym(C).

The checker forms each W chain space in complete diagonal weight blocks.
Its sparse rational echelon method retains the original independent image
columns. On each dependent column it records a kernel vector with a unique
new leading column index. These kernel vectors are independent, span the
kernel, and give the matching rank upper bound. Extending the boundary
span by these cycles produces a basis for actual homology. Every incoming
column is checked to be an outgoing cycle. For multiplication by each C
basis vector, every independent boundary column is checked by the literal
identity C(d_W u)=d_W(Cu); every chosen homology cycle is multiplied in R,
tested as a cycle, and reduced modulo the actual boundary image. Thus the
Sym(C) action is not an arbitrary action assigned to the known Tor table.

Applying the horizontal Koszul formula to those induced maps gives the
second exact complexes, again checking every consecutive composition. The
producer retains the complete C tensor B_(1,2) matrix, horizontal matrices
in the named grades, homology representatives, and the degree-four
transgression matrices. Their zero-based basis indices have the literal
combinations/product ordering in the producer; the W and C generators are
also printed in the fixture. Full W matrices are freshly reconstructed
and their complete canonical digest is retained. No old producer is
imported, no source matrix rank is copied, and no numerical tolerance is
used. The test suite additionally verifies all stored horizontal and d2
ranks by independent dense elimination over F_1009. This supplies an
independent lower bound matching the rational upper/kernel certificate;
finite-field ranks alone would not certify rational rank upper bounds.

Factor permutations act on the literal R monomials and on C wedge terms.
They fix W pointwise. The ambient comparison instead acts on the E wedge
terms as well. Reducing these actual actions gives every diagonal GL3
weight and every factor-permutation class trace. The separate comparison
with the Chow Schur table uses interlacing patterns, not these maps:
for partition (a,b,c), enumerate a>=x>=b>=y>=c and x>=z>=y with weight
(z,x+y-z,a+b+c-x-y). Complete torus characters in every S_m class determine
the characteristic-zero GL3 x S_m representation. Traces at identity alone
would not do so.

## 7. Results through internal degree three

For the ternary cube, the only nonzero E2 terms through degree three are:

| (p,q), internal grade | Dimension | S3 class traces (1,(01),(012)) |
| --- | ---: | --- |
| (0,0), 0 | 1 | (1,1,1) |
| (0,1), 2 | 20 | (20,0,-10) |
| (1,0), 2 | 142 | (142,18,10) |
| (1,1), 3 | 275 | (275,25,35) |
| (2,0), 3 | 1445 | (1445,-9,-43) |

The actual ranks 65 and 187 in the original preregistration both pass.
There is no possible nonzero higher differential among this support at a
fixed internal grade. Thus E2=E-infinity in these grades, giving ambient
Tor_(1,2) of dimension 162 with traces (162,18,0), and Tor_(2,3) of
dimension 1720 with traces (1720,16,-8). These total traces are only a
compact display: the fixture and checker compare every weight/class with
a second literal ambient Koszul construction using all 27 E generators.
That comparison does not infer individual Tor from an Euler sum.
The tests also build the complete expected ambient weight/class characters
without any Koszul elimination: they enumerate fixed words for chi_E,
apply the exact Sym^2 and Sym^3 cycle formulas, and subtract the literal
R_2 and R_3 characters. Agreement in every weight is therefore checked by
both a second chain complex and this independent character formula.

For the held-out fourth power of a three-dimensional V, the degree-two
pieces have dimensions 63 and 1962. Their S4 class traces are respectively
(63,21,-21,0,-21) and (1962,168,66,9,24). Their sum is the preregistered
(2025,189,45,9,3). The checker compares their full weight characters with
the literal ambient Koszul complex on all 81 generators. No higher-power
pattern is inferred from these two examples.

## 8. The degree-four transgression construction

For x in ker(d1:Lambda^2 C tensor B_(1,2)->C tensor B_(1,3)), choose
the stored W-cycle representatives and lift x to X in Lambda^2 C tensor
K_W,1,2. Write d_C X=sum_c c tensor Z_c. Horizontal closedness says every
Z_c is a W boundary; solve d_W Y_c=Z_c with the retained exact preimages.
Set Y=sum_c c tensor Y_c. Then d_C X-d_W Y=0, and the remaining total
boundary is d_C Y. It is a W cycle because d_W d_C Y=d_C d_W Y=d_C^2 X=0.
Its class in B_(2,4) is d2(x), with the total-sign convention above.

There is no incoming horizontal boundary to this source, since B_(1,1)=0,
and no horizontal quotient at the target, since B_(2,3)=0. Changing the
chosen vertical lifts changes the target by a horizontal image from the
zero space C tensor B_(2,3). The ordinary spectral-sequence construction
also proves independence of representatives. The producer checks every
equation d_W Y_c=Z_c and every target cycle exactly, stores all induced d2
columns and a complete first nonzero zigzag, and supplies rank/nullspace
certificates. This is an actual chain-level transgression, not a map
postulated from a dimension discrepancy.

The full finite result is

    dim E2_(2,1),4 = 1615,   dim E2_(0,2),4 = 65,
    rank d2 = 65,            dim E2_(3,0),4 = 7684.

There are no other nonzero E2 terms in internal grade four. All 46 source
weight blocks, including zero-rank blocks, are retained; the map is onto.
Its image is the entire representation

    [552] tensor (1+sigma) + ([642]+[543]) tensor epsilon.

Both degree-four predictions pass. After d2, the only surviving pieces
are E3_(2,1),4 of dimension 1550 and E3_(3,0),4 of dimension 7684. All later
maps have zero source or target, so E3=E-infinity here. Consequently

    Tor_2^(Sym E)(R,Q)_4 = 0,
    dim Tor_3^(Sym E)(R,Q)_4 = 9234.

This 9234 is not the earlier 9019: the latter is Tor_3^R(Q,Q)_3, a
different ring and grading in the accepted ambient bridge. As a secondary
check only, the degree-four coefficient of
(1-T)^27 sum_r binomial(r+2,2)^3 T^r is -9234. That Euler coefficient is
not used to calculate d2 or infer its surjectivity.

**A precise non-formality consequence.** The W-Koszul complex is not
formal as an internally graded Sym(C)-module complex. If it were
quasi-isomorphic, over Sym(C), to the direct sum of its homology B_q in
their homological degrees, derived tensoring over Sym(C) with Q would
have the direct-sum E2 homology. In internal degree four this would retain
the 65-dimensional total-degree-two term B_(2,4). The actual total
complex has zero such homology, by the surjective d2 just computed.
This contradiction rules out that formality. It does not rule out a
splitting as a complex of plain Q-vector spaces; C-linearity is essential.
Thus the missing information is genuinely higher chain compatibility,
not merely a missing scalar trace or an inconvenient basis choice.

## 9. Source, literature, and interpretation boundaries

The source/module construction and duality are classical: see
Raicu--Sam--Weyman, [On some modules supported in the Chow variety](https://arxiv.org/html/2108.10910),
Proposition 2.7, (3.2)--(3.5), and Example 4.5. The frozen PR769 table is a
comparison target; our low-grade eliminations, C action and transgression
are rerun directly. PR782 correctly proposed the comparison and the
cycle-index refinement of the *alternating* character. This packet adds
literal maps to that interface; it does not claim a new general
change-of-rings theorem or external priority for these finite identities.

Keep three objects distinct: the equivariant K-polynomial for the ambient
Segre algebra over Sym(E); the Chow-base alternating Tor polynomial over
Sym(W); and the reduced scalar recurrence numerator after specializing
an operator and cancelling scalar denominator factors. The bicomplex
relates the first two at chain level. A scalar eigenvalue collision does
not change this fixed characteristic-zero source complex or its Betti
spaces. None of the three is automatically a finite superdeterminant of
the natural syzygy complex. Additive Euler identities discard differentials.

The source manifest authenticates ten exact Git note blobs, including the
two prediction freezes and the bounded resource-refusal amendment. It
also authenticates the unchanged resident ambient proof and review. Old
full-resolution matrices are not replayed or imported. Current artifact
seals bind this proof, producer, tests and manifest. Fresh acceptance
reconstructs the complete declared panel before comparing the fixture;
resealing a changed map, omitted weight, scalar type or claim cannot make
it pass. The normal and optimized Python modes have the same semantics.
