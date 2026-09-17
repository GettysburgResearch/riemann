# NJT26 — use the fitted moment to control the unseen tail

**Proposed component mathematics; independent review needed. RH remains
unproved by this packet. Nothing here changes canonical/formal status.**

This additive continuation starts from PR875 head
`17ad26fd0b3de0c88b56d356ab850b881227b2f5`, including its `closure-bridge`.
It does not claim that the already-published eight-moment chain was constructed
again during this pass.

## Results

- `PROOF.md` proves terminal-coefficient and terminal-ratio bounds for the
  complete Taylor tail of a Lee--Yang/Laguerre--Pólya comparison model. It
  derives an off-axis minimum modulus from the model's actual real-field
  growth rather than from variance alone.
- These bounds reduce the displayed joint gamma/model sufficient schedule
  from O(R^2 log R) even-moment coordinates to O(R (log R)^2). The existence
  of models achieving the required native fits remains **OPEN**. Comparison
  models may be rational real-zero polynomial products, not necessarily spin
  laws; in that broader class the cofinal criterion is also necessary for RH.
  No extra all-order inverse-Ising representation theorem is assumed.
- Conditional on the unreplayed native F5 zero certificate in PR858, exact
  fitting of that fixed stage already fails by moment degree512, instead
  of the older sufficient obstruction degree32768. This is not an obstruction
  to the moving-source schedule, to the theta law, or to RH.
- `ARITHMETIC.md` proves a sharp full-energy tradeoff for changing the
  short-prefix completion. An oracle completion can annul the quadratic
  annular output only by paying at least one quarter of the actual native
  annular energy. The construction uses the future prefix and is not an
  RH algorithm. The actual cheap native covariance bound is not established.

The key strategic change is to combine the two analytic routes at finite
order: use admissible real-zero models to control the whole gamma defect.
Source approximation alone and positivity of a Laplace response do not solve
that finite-order feasibility problem.

## Read and execute

Read `PROOF.md`, `ARITHMETIC.md`, `ATTEMPTS.md`, `SOURCES.json`, then
`VALIDATION.md`. The checker covers bounded rational identities and the
integer theorem budgets, not native high-order moment fits or new zeros.

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_checks.py
python -I -S -B -O test_checks.py
```

The result explicitly binds all unproved conclusions as unproved. Mutation
and type tests reject false scope; successful replay is not an independent
analytic review, a Lean proof, or whole-repository scientific acceptance.
