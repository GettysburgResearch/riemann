# Concrete Segre--Chow change-of-rings comparison

Status: preregistered exact source computation; results not yet obtained.
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
