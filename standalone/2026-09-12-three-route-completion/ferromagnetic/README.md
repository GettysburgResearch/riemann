# Exact constrained ferromagnetic graft directions

**Proposed component work. No sixteenth-moment crossing, all-order realization,
or RH proof.** Read [PROOF.md](PROOF.md) for the complete mathematics and exact
scope. This packet does not change or promote its predecessor sources.

The new general formula expresses the compensated first unmatched cumulant
after a graph deformation using a component polynomial, without a full
Jacobian inverse. It includes an exact determinant criterion for the lower
moment map. Applied to one-edge mergers at PR #863's stated native root, it
certifies two positive-edge directions that strictly reduce the actual
sixteenth-moment excess while preserving all seven even moments through14.
The correlated component grows from two spins to three. Four other permitted
edge directions give the opposite sign.

The application is CONDITIONAL on ICR1, PR #863 at
`0640c9c59be0bf20c18258460a7517fb09728e82`. The new arithmetic authenticates
that root box and encloses every possible point in it; it does not replay
the native theta integration that establishes the root's existence.

Standard-library accepting commands, from the repository root:

```text
python -I -B standalone/2026-09-12-three-route-completion/ferromagnetic/certify_graft.py
python -I -B -O standalone/2026-09-12-three-route-completion/ferromagnetic/certify_graft.py
python -B standalone/2026-09-12-three-route-completion/ferromagnetic/test_graft.py
python -B -O standalone/2026-09-12-three-route-completion/ferromagnetic/test_graft.py
```

The first two reconstruct `graft-certificate.json` entirely and compare it.
`--emit` writes a proposed output and is not an accepting replay. Normal and
optimized execution use one arithmetic implementation. The tests separately
compare the complete eight configurations of three spins with the formal quotient,
and exact rational linear solves with the annihilator formula at six orders.

Optional non-directed exploration (requires mpmath and the recorded Git objects):

```text
python -B standalone/2026-09-12-three-route-completion/ferromagnetic/scout.py --continue
python -B standalone/2026-09-12-three-route-completion/ferromagnetic/star_scout.py --minnorm
```

The first uses midpoints of #863's stored moment intervals as scouting targets.
The second uses the new #867 weight-adapted star at
`4c7898432546814812b2be8c72fc199e294354d1`. Neither script enters acceptance.
Neither produced a new moment16 root. Their retained JSON records have an
explicit non-directed status. An opposite-sign star seed is useful motivation,
but does not prove that the two seeds are connected inside the lower-moment
fiber. Convex mixtures are not used as ferromagnetic realizations.

The next missing theorem is a target-containing positive-parameter continuation,
with lower-moment preservation and conditioning controlled over the entire
path. A strict initial derivative is not that theorem.
