# Physical-mask sheaf/amplifier successor: research map

Status: **active exploratory successor to frozen PR #756; no RH or GRH
claim**.

Base object: PR #756 at exact head
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`.

Owning branch: `codex/l-function-sheaf-amplifier`.

## Central question

Can one choose a source-faithful hard restriction on the physical variables

\[
X=Pc^2,\qquad Y=Qd^2
\]

which simultaneously

1. improves the restricted inverse-Gram principal leverage;
2. removes every geometrically constant selected-mode constituent;
3. has conductor/Betti complexity small enough that geometric cancellation
   survives the growing-family limit; and
4. preserves, and eventually individualizes, the response of the principal
   member to a hypothetical off-critical-line zero?

The conjunction is deliberate.  A gain in item 1 which is lost to item 2 or
3 is not an arithmetic amplifier.  A family estimate satisfying items 1--3
without item 4 is not an RH mechanism.

## Work lanes

### Route A: ternary cyclic sheaf gate

Start with the smallest leverage-improving source-realized mask from PR #756:

\[
(\ell,\rho,k,t)=(7,13,3,2),\qquad L_{\rm hard}=27/49.
\]

Express its two selected Kummer modes as trace functions on an explicit
configuration space, remove diagonal/equal-product/geometrically constant
strata, and audit invariant constituents.  Fixed-complexity square-root
cancellation and conductor-uniform `CYSEL` are separate targets.

### Route B: mask/amplifier co-design

Optimize the physical support and dual weights with three ledgers retained:

\[
(\text{principal leverage},\ \text{invariant multiplicity},\
\text{geometric complexity}).
\]

The target is either a certified Pareto-improving mask or an exact dual
no-go theorem.  Complete-frame soft weighting is not a substitute for hard
restriction.

### Route C: principal anomaly transfer

Propagate a symbolic hypothetical principal zero through the native source,
the hard restriction, and the exact

\[
(C,S,R)\mapsto(C+T,S+T,R-T)
\]

invisible direction.  Record the smallest positivity, rigidity, inversion,
or amplifier statement that would turn the surviving response into a
family-wide contradiction.

### Route D: independent arithmetic moonshots

Two bounded structural attacks run in parallel:

- resolve or further reduce the genus-two `Sym^12` defect
  `Epsilon_Eis-Genuine` without fitting more unrelated primes;
- determine whether the first odd-notch trace-zero boundary contributes a
  second `c_q/M` term to the raw family-correlation zero density.

These are independent mathematics tracks, not substitutes for Routes A--C.

## Proof and computation contract

- Exact, exact-finite, imported, formal-model, conditional, and conjectural
  statements are labelled separately.
- A trace-sheaf description is not called `CYSEL` unless the bound is uniform
  in the growing conductor parameter with its Betti/conductor cost included.
- A raw family-correlation zero is never called a zero of an individual
  L-function.
- Local spectral or trace-function equality is never promoted to a motive,
  compatible system, global Euler product, RH, or GRH statement.
- Computation is limited to small exact cyclotomic, matrix, residue, and
  recurrence controls.  No broad finite-field, conductor, curve, or zero
  sweep is authorized by this packet.

## Initial dependency path

Read, in order:

1. `RESIDUAL_MECHANISMS_RESEARCH_MAP.md`;
2. `function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md`;
3. `function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md`;
4. `function_field/FFPS_CYCLIC_CLOSURE_BUDGET.md`;
5. the new Route A--D packets indexed here as they are committed.

## Completion standard for this pass

The pass succeeds only if it leaves auditable movement on the coupled central
question, not merely additional small examples.  At minimum it must leave:

- an explicit selected-mode geometric adapter or a rigorous obstruction to
  forming one;
- an exact co-design optimization or dual certificate which includes a
  complexity charge;
- an end-to-end conditional principal-anomaly statement or a precise no-go;
- bounded, proof-graded records for both arithmetic moonshots;
- replay commands, a release audit, and a five-minute handoff.

