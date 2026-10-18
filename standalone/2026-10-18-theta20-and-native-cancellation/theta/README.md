# Original theta moments through degree 20

**Proposed finite theorem, subject to independent mathematical review. RH is
not proved.** The complete original theta law is realized through every moment
of order 20 by a connected finite zero-field ferromagnet. The model has 305
vertices, 304 strictly positive edges, 304 positively weighted observed spins
and one zero-weight hub. It is a new finite target beyond the degree 18
constructions in #981 and #988; no worldwide or exclusive priority is claimed.

The full proof is in `PROOF20.md`. The complete model is the short rational
polynomial in `connected_blocks.py`, with exact parameters in
`parameters20.json`. The source is the literal theta density, freshly
reconstructed through 20 in each accepting run. The transcendental backend
and source protocol are inherited from #988, with their exact byte identities
recorded in `SOURCES.json`.

The root cube has radius 10^-30 in ten stated coordinates. Its directed
displacement bound is below 1.561e-39 and its contraction bound below 1.371e-10.
The existence claim follows from this whole-cube contraction. The saved
certificate is a comparison receipt, not a substitute for reconstruction.

Run from this directory with ordinary Python 3:

```sh
python replay.py
```

This authenticates every manifested payload, reproduces the complete
source/root certificate and independent finite-assembly checks in ordinary
and optimized Python, compares their outputs, and rejects four actually
executed optimized corruption controls. Standard-library Python suffices.
No numerical optimizer or special-function package is needed for acceptance.

For individual replays:

```sh
python certify20.py --check certificate20.json
python check_connected.py --check finite_checks20.json
```

The finite checker independently assembles all 305-spin moments at the
rational center by generating-polynomial multiplication, and enumerates all
128 configurations of a seven-spin fixture. It does not enumerate 2^305 states,
independently reimplement transcendental intervals, or prove the theta
equalities without the separate contraction argument.

`EXPLORATION20.md` describes the successful change of graph and the attempts
that failed. The successful operation repeatedly split a weighted sign into
an almost-aligned unequal dimer, and decomposed a dimer into independent signs
when it reached its zero-coupling face. The boundary distribution identities
are exact; the exploratory path was not interval-certified. Only the final
interior 305-spin model is the accepted finite object of this packet.

The remaining full-proof problem is cofinal feasibility: models whose moments
converge to every fixed theta moment. The classical compactness/Hurwitz
consumer is already available in #981. This one degree 20 result does not
establish that global construction premise.

The optional `produce_center.py` reconstructs the source and refines the
finite starting data in `seed20.json` using ordinary Decimal Newton steps.
Its output is nondirected, and is not an acceptance premise:

```sh
python produce_center.py --emit proposed_parameters.json
```

The rational witness, source, producer, checker and receipts are bound by
`MANIFEST.json`; provenance and inherited byte identities are in `SOURCES.json`.
