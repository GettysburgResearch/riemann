# Formalization Reviewer C: operator and QA report

## Freeze

- Repository: `gfreund123/riemann`
- Bootstrap merge: `573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f`
- Branch: `formal/030-xi-operator-qa`
- Research cutoff: PR #707
- RH status: **UNPROVED**

No post-#707 theorem is imported.  The reviewed actual-Xi order-three theorem is
represented as `PROVED_CONDITIONAL`, not as an unconditional formal proof.

## Owned formal modules

- `RiemannFormal.Operator.FiniteMatrix`
- `RiemannFormal.Operator.PickAlgebra`
- `RiemannFormal.Operator.ReciprocalConcavity`
- `RiemannFormal.Operator.XiOrderThree`
- `RiemannFormal.Operator.HeatQ4Finite`
- `RiemannFormal.Refutations.MatrixFirewalls`
- `RiemannFormal.Refutations.HeatQ4Firewalls`

The machine-readable declaration-by-declaration report is
[`C_OPERATOR_QA.tsv`](C_OPERATOR_QA.tsv).  It separately records statement
existence, unconditional proof, conditional proof, source locking, comparator
coverage, and axiom audit status.

## Exact finite algebra

The formal library proves:

1. the two-point Pick determinant identity;
2. the three-node `A*B` determinant decomposition;
3. the reciprocal and companion second-divided-difference factorization;
4. exact two- and three-dimensional LDL congruence identities;
5. PSD and PD principal-minor implications without a PSD-to-PD upgrade;
6. finite positive-sum reciprocal concavity with an exact square certificate;
7. the off-line orbit defect formula and zero-curvature critical orbit;
8. one-orbit absorption, finite reserve allocation, and a finite reciprocal-square budget;
9. finite Hermite recurrences, Q4 filter identities, and the zero-bare Q4 determinant formula.

## Conditional actual-Xi boundary

The following inputs remain explicit propositions or theorem hypotheses:

- corrected published high-zero verification;
- corrected bibliographic/source lock;
- grouped local `C^2` convergence through two derivatives;
- one representative per reflected orbit;
- retention of the `(m0-1)R0` multiplicity residual;
- reciprocal-square zero-tail control;
- repeated-node reduction and packet ordering/congruence.

`actualXiOrderedDistinctPickOrderThree_of_inputs` proves the nontrivial exact
ordered-distinct PSD implication from those inputs and the two scalar curvature
signs.  `actualXiPickOrderThreeConditional` packages the complete size-at-most-
three PSD conclusion while keeping repeated-node and analytic hypotheses visible.
Distinct-node positive definiteness is not stated.

## Formalized firewalls

Kernel-checkable exact witnesses establish:

- `positiveSchurCannotRescue`;
- `coefficientBudgetDoesNotImplyOperatorContraction`;
- `smallNegativeInertiaDoesNotControlCurrent`;
- `hyperbolicPoleBlockNotTwoPositiveSquares`;
- `positiveExcessDoesNotControlSquareRoot`;
- `scalarDiagonalDoesNotDeterminePolarizedGram`.

The finite `parityChangesUnderDisplacement` theorem is intentionally classified
`BLOCKED_MATHEMATICS` for the full heat semantic ID.  It is a regression fixture,
not a formal proof of the analytic Bohr/vertical-limit no-go.

## Comparator topics

Trusted challenge/solution pairs are added for:

- `XiPickThreeNode`;
- `OperatorPositiveSchurRescue`;
- `XiPickOrderThreeConditional`.

The conditional challenge exposes every external proposition in its statement.
The trusted `ChallengeDeps` side imports Mathlib only; the sorry-free solution
side imports the formal library.

## Fail-closed QA

- `check_no_sorry.sh` rejects `sorry`, `admit`, custom `axiom`/`opaque`, and
  unresolved tactic suggestions in trusted modules; it also compiles every
  Reviewer C comparator challenge and solution.
- `check_axioms.sh` discovers every `#print axioms` declaration dynamically and
  permits only `propext`, `Classical.choice`, and `Quot.sound`.
- `verify_declaration_map.py` checks declaration existence and prevents a
  conditional row from being labeled `PROVED` without an explicit blocker.
- `check_statement_sources.py` joins `C.tsv`, the canonical claim registry, and
  `C_OPERATOR_QA.tsv`, requiring exact source SHA/path equality and consistent
  proof/conditional/source/comparator/axiom flags.

No heavy computation, external high-zero verification, broad Q4 scan, or full
Lean build was rerun outside formal CI.
