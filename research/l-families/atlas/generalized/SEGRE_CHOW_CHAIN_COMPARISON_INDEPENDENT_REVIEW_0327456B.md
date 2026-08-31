# Independent review of the Segre--Chow chain comparison

Verdict: **PASS**, with the finite scope and interpretation boundaries in the
science note retained.

Reviewed science: `0327456b384a89ccc6bfdeaa76578689703d7ecb`.
Preregistration lineage: `28c6d95ccf6842ec415c440c77a8036a187f176c`,
`6416a3c301c22fb674ef12947568da0ad341f801`, and the preserved bounded-cap
amendment `e3a9b2c56029fa41e4cbceb1fbf64de4e20c75b4`.

## Proof audit

The orbit-sum splitting `E=W direct-sum C` is literal and equivariant in
characteristic zero.  The producer forms the W-Koszul complex before taking
homology, transports the actual C action to chosen homology representatives,
and constructs the horizontal Koszul complex from those induced maps.  The
degree-four `d2` is not inferred from an Euler coefficient: each horizontal
cycle is lifted to W chains, its first C image is solved as a W boundary, and
the second C image is reduced in `B_(2,4)`.  The stored checks enforce every
boundary equation and target-cycle condition.

The spectral-sequence indexing is consistent.  The rank-65 map from
`E2_(2,1),4` to the 65-dimensional `E2_(0,2),4` kills the latter and leaves
1550 dimensions in the former.  Together with `E2_(3,0),4` of dimension
7684 and the absence of other grade-four terms, this gives ambient
`Tor_(3,4)` dimension 9234 and `Tor_(2,4)=0`.  The separate coefficient check

\[
 [T^4](1-T)^{27}\sum_{r\ge0}{r+2\choose2}^3T^r=-9234
\]

agrees but is not used to construct the differential.  The nonzero `d2`
correctly proves non-formality only as an internally graded Sym(C)-module
complex; the note does not overstate plain-vector-space formality.

## Independent finite checks

The exact science gates report 36/36 tests in both normal and optimized
Python, both producer checks, identical source emissions, and clean lint and
base-diff checks.  A clean detached replay at the exact science SHA repeated
all 36 tests normally (649.407s) and with `-O` (644.278s), both producer
checks with the identical sealed payload, Ruff, and the full base diff.
Independently of the producer's rational rank routine, I
loaded the frozen fixture and recomputed every stored transgression block over
`F_1009`.  All 46 weight blocks were present; their source dimensions sum to
1615, target dimensions to 65, and modular ranks to 65, matching every stored
rank.  Nineteen blocks are nonzero and the stored chain zigzag has a nonzero
target class.  The four resident artifact seals and the payload seal also
recompute exactly.

## Boundaries

This is a finite `(d,m)=(3,3)` chain-map theorem plus the declared `(3,4)`
held-out low-degree comparison.  It does not provide a general strand
formula, a canonical basis or scalar-unique differential, an automorphic
object, a superdeterminant, purity, or an RH/GRH implication.  The nonzero
higher differential is precisely evidence that alternating characters alone
discard load-bearing chain data.
