# Actual-Xi statement fidelity: fresh reading and repair contract

Source: main `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Status: source-level contradiction and repair requirements; no Lean compilation performed.

## Exact source and naming correction

The full shared dependency `formal/comparator/ChallengeDeps/RiemannComparatorChallengeDeps/XiPickOrderThreeConditional.lean`, blob `7d3dd6c98fd453d1810d80b0e1a39e2e4fbc7ab5`, was read in three consecutive ranges. Its field is named `diagonalPositive`, not the `strictDiagonalPositive` spelling in the old PR prose. The existing pass2 regression already uses the correct field; the spelling correction does not repair or invalidate its mathematical contradiction.

The definitions are

    riemannXi(s) = (1/2) s (s-1) completedRiemannZeta(s)
    centeredXi(z) = riemannXi(1/2+z)
    actualXiNodeP(x) = Re(deriv centeredXi(x)/(x centeredXi(x))).

These are total complex operations. At s=1 the raw product is zero, regardless of the assigned total value of the completed zeta function. Hence centeredXi(1/2)=0 and actualXiNodeP(1/2)=0, since division by zero in this field is zero. An input supplies `inputs.diagonalPositive inputs.grouped (1/2)` with positive argument; it requires that same value to be strictly positive. No derivative calculation is needed.

Thus the stated input package has no inhabitant. A conditional theorem quantified over it can be a valid Lean theorem but does not establish the intended actual-Xi claim. This is not kernel inconsistency, an RH counterexample, or a refutation of the informal positivity theorem.

## An independent enumeration error

`GroupedActualXiC2Expansion` requires an injective map Nat -> ReflectedOffLineOrbit. Evaluation at zero already forces an off-line orbit; injectivity forces infinitely many. Empty or finite off-line spectra are excluded, independently of removable-point normalization. Its completeness field only compares the selected orbit list with another enumeration; replacing the function type alone must not silently lose full source coverage or multiplicity accounting.

## Consumer reading

The complete `XiOrderThree.lean`, blob `8a57d165e4d585232d8976858871b99a0d39101e`, and `XiExternalInputs.lean`, blob `78cab4bfee35fbbffac52737da083eb187b01b13`, were read. Their field projections, polynomial energy-limit argument and repeated-node reductions do not construct the missing input. The citation equality proved by rfl is metadata equality, not the external finite-height theorem. `actualXiInputs_have_concrete_dependencies` returns consequences of an input, not Nonempty of the headline input type.

Lines 500 through the end of `XiSourceSpecific.lean`, blob `da684227de5443511b60d1fafa0b1ccafa1883ee`, were read for the reserve constructor only. That constructor assumes the grouped expansion and tail inputs; this limited reading is not a fresh audit of its earlier analytic/algebraic lemmas.

## Required repair, without weakening the claimed theorem silently

1. Define the intended entire xi, including the removable values xi(0)=xi(1)=1/2. Prove agreement with the raw product off the exceptional points and the analytic/derivative facts needed at the half-node. An arbitrary assignment to `actualXiNodeP(1/2)` is not such a proof.
2. Use an arbitrary countable actual-orbit index with finite exhaustion, or explicit optional zero-padding. Allow empty, finite and infinite off-line spectra. Retain completeness, analytic multiplicity, uniqueness, selected reserve and one-use accounting.
3. Keep the existing C2 expansion domain t>1/4 distinct from the conclusion for every x>0. Any domain extension is a separate analytic input/proof. Restricting the theorem to x>1/2 would change the statement and needs a new disposition.
4. Repair the shared challenge definitions, solution, source consumers, hashes and catalog together. Rebuild the relevant Lean and comparator targets and recheck statement fidelity. Do not treat successful self-comparison or metadata projection as a nonvacuity proof.

The five affected catalog entries remain held: OPERATOR.XI.PICK_ORDER2; OPERATOR.XI.PICK_ORDER3.TP_CURVATURE; OPERATOR.XI.RECIPROCAL_CONCAVITY.ACTUAL; OPERATOR.XI.PICK_ORDER3; OPERATOR.XI.LOEWNER_LOW_ORDER. Independent finite algebra is not automatically invalidated.

`../pass2/lean/XiInputNonvacuity.lean` remains a NOT-COMPILED regression candidate outside trusted imports. This retry changes no formal source and supplies no compiled repair.
