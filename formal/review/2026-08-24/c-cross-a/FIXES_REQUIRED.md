# Fixes required

## P0 — required before reconciliation

1. **Repair the trusted build.** Restore the compatibility theorem `RiemannFormal.Upstream.zeta23_bridge_preserves_RH`, or remove/update every trusted `#print axioms` reference and the expected audit set consistently.

2. **Restate `MellinLandauBoundarySingularity` exactly.** Use the reviewed tail transform from 1 to infinity with kernel `x^(-s-1)`, or prove the exact inversion/indicator adapter into Mathlib's standard Mellin transform. Positivity and nonzero hypotheses must apply to the actual support controlling the convergence boundary.

3. **Restate `SubpowerNegativeMassHolomorphy` exactly.** Zero-extend below one or use a tail transform; the logarithmic negative-mass bound on `[1,X]` cannot control arbitrary behavior on `(0,1)`.

4. **Add the strongest honest conditional consumer.** One declaration must expose every open premise:
   * exact fixed detector/source Mellin identity;
   * initial convergence half-plane;
   * fixed nonvanishing multiplier;
   * fixed holomorphic defect;
   * exact Landau boundary theorem;
   * exact negative-mass holomorphy theorem where used;
   * reciprocal-zeta noncancellation/order;
   * right-half-plane zero exclusion and functional-equation reflection.
   Its formal status must be `PROVED_CONDITIONAL`.

## P1 — formal completeness and trust QA

5. Add the analytic-order/meromorphic-order adapter at `ρ≠1`, and state the reciprocal pole multiplicity in the same convention as Zeta23 `zeroMult`.

6. Either formalize an arbitrary finite Mellin linear-combination theorem or rename the delivered API as two-term.

7. Formalize the actual logarithmic-box transform and `K_A(s)=(1-A^(-s))/s ≠ 0` for `A>1`, `Re(s)>0`.

8. Make `check_axioms.sh` discover and compile all trusted axiom-print modules, including `Analysis/AxiomAudit.lean` and `PrintAxioms/MellinAPI.lean`.

9. Extend machine source locks to the new scientific heads and exact paths. String constants in `SourceLocks.lean` are not sufficient if `verify_source_locks.py` never reads them.

10. Run the complete exact-head command suite and attach the logs/status to the repaired Reviewer A head.

## P2 — documentation alignment

11. Update `A.tsv`, the blueprint, and the report after the proposition repairs; do not retain `PROVED_CONDITIONAL` against the current overbroad statements.

12. Keep the generic `MellinAPI` comparator as a useful local API test, but add or rename a comparator topic so it does not imply that the final conditional consumer has been checked.
