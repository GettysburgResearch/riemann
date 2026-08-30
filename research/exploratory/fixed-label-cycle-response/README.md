# Fixed-label cycle response beyond commutative shadows

Status: proposed exact finite-model theorem, awaiting frozen-source review.
Scope: finite colored directed graphs and fixed-label matrix/voltage lifts;
loops and immediate returns are allowed. This is not undirected Ihara zeta.
Sources: classical directed-cycle determinant and graph-cover constructions;
see [MATHEMATICS.md](MATHEMATICS.md) for exact comparisons and proofs.
What was run: see [verification.json](verification.json) and the replay below.
Smallest remaining gap: independent mathematical review of the precise
fixed-label information-loss statement. No number-field transfer is supplied.

This is a contrasting model for programmes [#763](https://github.com/gfreund123/riemann/issues/763)
and [#764](https://github.com/gfreund123/riemann/issues/764). Its parent is defined
from vertices, colored edges, and declared label matrices before any spectrum
or zero set is calculated.

The packet proves that two sources with the **same entire commutative
multivariable determinant** can have different fixed-label three-sheet cover
responses. For unitary label matrices, the first distinguishing trace is an
exact nonnegative commutator energy. Three is the smallest permutation-sheet
degree for this pair; two-dimensional orthogonal matrix labels already suffice.

The labels use a fixed identification of sheet spaces. The response is not
asserted to be invariant under independent changes of basis at each vertex.
The three-sheet examples may have cyclic based-loop monodromy: noncommuting
edge labels must not be renamed a nonabelian deck group.

Replay (Python standard library only):

```text
python -B research/exploratory/fixed-label-cycle-response/cycle_response.py --check
python -B -O research/exploratory/fixed-label-cycle-response/cycle_response.py --check
python -B -m unittest discover -s research/exploratory/fixed-label-cycle-response/tests -v
```

The computation checks exact rational fixtures and independently enumerates
closed walks and primitive cycles. The all-size theorems are proved in prose,
not inferred from the fixtures. RH and GRH remain unproved; no new arithmetic
L-function, critical-line theorem, or external priority claim is made.
