# IMR26: realize theta moments by ferromagnetic spin systems

**Proposed component proofs; independent review required. RH and all-order
Ising realization remain unproved.** This is a new research direction, not a
continuation of the divisor-gap calculation or a solved arithmetic norm bound.

The intended chain is

    exact full theta moments -> finite nonnegative-coupling spin models
    -> Lee–Yang + uniform complex moment convergence -> RH.

Read [PROOF.md](PROOF.md) for the complete transfer, actual finite construction,
analytic domains, and coupling-reserve theorem. Read [PROGRAMME.md](PROGRAMME.md)
for the open all-order realization and a concrete finite search specification.
[SOURCES.json](SOURCES.json) retains exact source versions and reading scope.

What is supplied:

- A specialization of classical Lee–Yang closure with an explicit finite-moment
  error bound paying every complex direction. Bounded variance is enough once
  the moment-matching ferromagnets exist; their existence is the open step.
- An exact 28-spin law matching the UNCHANGED theta source through moment order
  eight, with all theta indices and time tails enclosed. Its tenth-moment
  mismatch is certified, not concealed. The finite moment point is interior;
  strictly positive equal-coupling realizations nearby follow analytically.
- A necessary condition for any successful family: its removable rank-one
  complete-graph coupling reserve must tend to zero, by Rodgers–Tao. This is
  not a statement that all individual couplings tend to zero.
- An exact grouped-spin moment evaluator and a source-derived seed certificate.

This does not claim the Ising route is externally new. Lee–Yang, Newman–Wu,
Rodgers–Tao, and earlier Xi/partition-function proposals are credited explicitly.
We do not assert that RH implies the particular ferromagnetic realization target.

Replay (standard library only):

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B -O test_rejections.py
```

`--emit` is producer-only and does NOT authenticate the package. The accepting
commands regenerate all six raw moments (including normalization) on 84 cells,
pay every omitted theta/time tail, and prove root signs. They do not verify the
infinite Lee–Yang theorem, Rodgers–Tao theorem, or the open moment extension.
The finite tests are not independent mathematical acceptance.
