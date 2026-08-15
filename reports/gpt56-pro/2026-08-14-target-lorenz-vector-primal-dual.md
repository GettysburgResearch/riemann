# Target-Lorenz common-source vector primal/dual report

## Freeze and live movement

```text
repository:       gfreund123/riemann
origin PR:        #468
origin parent:    a41f81466f85d52597c97b41505756a8860698d0
renumber cutoff:  2026-08-14T19:56:18Z
report date:      2026-08-14
```

The packet was first published under temporary IDs `91685--91687`. During the
publication, PRs #469--#475 appeared and independently occupied those IDs. The
complete packet is therefore renumbered to `91720+`; the temporary files are
deleted rather than left as ambiguous duplicate claim IDs.

The most material descendants are PR #470, which proves an exact native
capacity separator and introduces SONTR, and PR #473, which presents a newer
factor-67 root-Hall/SONTR proposal. The present packet is an independent exact
Target-Lorenz optimization/duality result and fallback producer route. It does
not supersede those descendants and does not claim RH.

## Main theorem

The Target-Lorenz removal is the exact optimizer of the complete common-source
submeasure problem. The retained causal profiles have opposite monotonicities:
row per target decreases with divisor order, while score per target increases.
Therefore one leftmost target removal simultaneously:

```text
maximizes every component row;
minimizes score;
preserves exact target;
uses one common source coefficient.
```

If it passes all row and score demands, it is a primal certificate. If one row
fails, the cutoff ratio gives an explicit dual upper bound proving that every
exact-target submeasure of the same even source fails that row. This upgrades
the Target-Lorenz frontier from an ansatz to a complete primal-or-dual decision
theorem for its source cone.

PR #470 independently obtained the leftmost-basis optimality statement for the
live stopped-leaf LP. `L-91720` packages the general ordered-cone theorem and
the exact dual separator applicable beyond that one finite instance.

## Scope correction

A proposed collapse of the target cutoff to the single scalar
`sqrt(y)(sqrt(p)+1)` is false across the child-activation boundary. `R-91720`
gives a same-scalar algebraic counterexample and replaces it with the correct
piecewise `(A,u)=(sqrt(py),sqrt(y))` cell form.

## Full signed determinant reduction

`L-91722` bounds every Lorenz row margin below by the complete signed causal
row minus the cutoff row-per-target ratio times the complete signed target.
Thus it is sufficient to certify one full signed-packet determinant per row and
cutoff, rather than the original signed prefix determinant. The condition is
not claimed necessary.

## Support reduction

`L-91721` proves that whenever the target cutoff satisfies `c>=py/j`, the
Lorenz row margin is exactly the complete signed causal row. On the retained
Green/canonical row inputs, this closes that entire regime and restricts the
new arithmetic campaign to `c<py/j`.

## Arithmetic evidence

The discovery-only replay checks the structured grid

```text
p in {67,71,83,127};
y in {1,...,66};
j in {2,...,66}.
```

It finds no negative Target-Lorenz row margin. The minimum is

```text
p=67, y=1, j=66,
cutoff=35,
margin=0.001907989661226... .
```

This is the first quotient cell, already covered by the exact theorem
`py<2j`. Floating-point reconnaissance does not certify the remaining real
parameter cells.

## Relation to the newer SONTR route

`T-91720` remains a valid conditional implication for the stopped-leaf
Target-Lorenz route:

```text
AVLT + live one-use native ledger -> NRCT -> endpoint deficit o(log^2 X).
```

It is no longer presented as the only live endgame. PR #473 instead moves the
Hall operation to the strict root window `x<67` and proposes explicit finite
realization reserves. That route must be reconstructed against PR #470's
native-capacity separator and all frozen endpoint-frame inputs.

## Replay

```bash
cd experiments/X-91720-target-lorenz-vector-primal-dual
python3 verify.py
python3 recon.py
sha256sum -c SHA256SUMS
```

Expected exact theorem verdict:

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
```

Expected discovery verdict:

```text
PASS_TARGET_LORENZ_STRUCTURED_RECONNAISSANCE
```

## Honest status

```text
common-source vector primal/dual theorem       PROVED EXACT
one-scalar cutoff collapse                     REFUTED EXACT
support and determinant reductions             PROVED EXACT
structured arithmetic reconnaissance           POSITIVE / NOT A PROOF
stopped-leaf AVLT                               OPEN ON THIS ROUTE
factor-67 SONTR                                 CANDIDATE / REVIEW REQUIRED
Native-Root Capacity Theorem                    NOT ACCEPTED HERE
Riemann Hypothesis                              UNPROVEN
```
