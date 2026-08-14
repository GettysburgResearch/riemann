# Review handoff — Target-Lorenz vector primal/dual continuation

## Live placement and collision repair

```text
repository:       gfreund123/riemann
existing PR:      #468
branch:           research/gpt56-pro/91381-euler-shell-recovery
original parent:  a41f81466f85d52597c97b41505756a8860698d0
renumber cutoff:  2026-08-14T19:56:18Z
```

The first publication attempt used temporary claim IDs `91685--91687`. While
that packet was being pushed, live descendants PRs #469--#475 appeared and used
those IDs independently. This continuation therefore moves the complete packet
to the collision-free `91720+` namespace and deletes the temporary paths.

The controlling live descendants at the cutoff were:

```text
PR #469  3cf685181bd367b92cdcfeef9249e0b9b542a09e  Hall-free terminal generator
PR #470  89af3206ea1894884613e1188b5ab9a6a4cd74f0  native-capacity separator / SONTR
PR #471  4ac821701177edb67a77fe43e89cc2a7a53af68a  three-route synthesis
PR #473  71d6a859ea741fe035de709e8d10ed37301b778e  factor-67 SONTR proposal
PR #475  6cba90ea10163abd62b051c83c8bfd8cc2f901da  three-route native-root attack
```

Later corrections control. In particular, PR #470's exact native-capacity
separator blocks any raw-current-plus-child interpretation that spends the
finite-Euler rough reservoir twice. This packet retains the PR #468
normalization firewall.

## Durable mathematical contribution

```text
L-91720  exact common-source vector optimizer and explicit Farkas dual;
R-91720  exact refutation of the false global one-scalar cutoff collapse;
L-91721  support-easy Target-Lorenz reduction;
L-91722  sufficient full signed-packet determinant lower bound;
T-91720  conditional Target-Lorenz fallback route, not a claim over later SONTR;
X-91720  exact finite replay plus discovery-only arithmetic reconnaissance.
```

PR #470 independently reaches the leftmost-basis optimality conclusion for the
stopped-leaf LP. `L-91720` records the more general ordered-cone theorem and its
explicit coordinate separators. PR #473 is a newer root-Hall/SONTR candidate
which bypasses the stopped-leaf AVLT gate; this packet is retained as an
independent exact fallback and adversarial dual.

## Replay

```bash
cd experiments/X-91720-target-lorenz-vector-primal-dual
python3 verify.py
python3 recon.py
sha256sum -c SHA256SUMS
python3 -m py_compile verify.py recon.py
```

Expected:

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
PASS_TARGET_LORENZ_STRUCTURED_RECONNAISSANCE
```

The first verdict is an exact finite-algebra replay. The second is explicitly
nonrigorous reconnaissance for the infinite arithmetic sign family.

## Scientific boundary

```text
common-source vector optimization and separation    PROVED EXACT
target cutoff one-scalar collapse                    REFUTED EXACT
Target-Lorenz support/determinant reductions         PROVED EXACT
stopped-leaf AVLT signs                              OPEN ON THIS ROUTE
factor-67 SONTR proposal                             LIVE ON PR #473 / REVIEW
Native-Root Capacity Theorem                         NOT ACCEPTED HERE
Riemann Hypothesis                                   UNPROVEN
```
