# Suggested review order

Review this companion after, or together with, the frozen core import in
[PR #908](https://github.com/GettysburgResearch/riemann/pull/908). The PR body
records the exact companion commit. Review applies to that head and the stated
scope; a source-integrity pass is not acceptance of the mathematics.

1. **Source scope.** Read `SOURCE_SELECTION.json` and `RELATED_RESULTS.md`.
   Confirm why each family is included. In particular, keep the narrower
   cyclotomic-field strip in 029 distinct from the stronger zeta strip in 003,
   and retain the conditional status of the simultaneous-root paper.
2. **Source fidelity.** Run `checks/source_bundle.py verify --source ...`.
   Confirm the complete selected directories, every byte/blob/mode, canonical
   origin selection and transitive internal imports. The old core is separately
   verified without modification. General metadata updates must not alter the
   old audit record.
3. **Exact arithmetic.** Read `NATIVE_MOBIUS_BRIDGE.md` and rerun its checker.
   Check ideal splitting, the ramified factor at 3, the norm-4 inert factor at 2,
   strict-left/closed-right endpoints, signed coefficients, completion terms,
   and the actual arithmetic measure in every kernel.
4. **Conditional estimates.** Confirm that all uses of 7/8 are explicitly
   conditional on the imported theorem and the classical reciprocal-zeta
   interface. Verify the `3/4 + epsilon` energy exponent and the equivalence up
   to constants of the two completed states. Preserve the inherited failure of
   the MHB32 bootstrap and the restricted meaning of the CAP36 deduction.
5. **Proposed research.** The transfer from smooth ideal sums to moving floor
   kernels is open. Fixed-form logarithmic savings, average family cancellation,
   positivity of a Gram matrix, or a finite identity do not supply its uniform
   bound. No rank, conductor, cutoff or endpoint cost may be dropped.
6. **Formal verification.** Inspect the actual comparator statements and
   solution mappings, then run them in a fresh assembled view if the required
   toolchain is available. The lexical marker inventory does not check theorem
   equivalence or external dependency implementations. The square-difference
   comparator does not certify every later family-182 extension.

## Load-bearing new objects

- The coefficient identity and floor/interval formulas in `NATIVE_MOBIUS_BRIDGE.md`.
- Its full Gram/completion and block-mean identities, including every sign.
- The imported-source and scope map in `RELATED_RESULTS.md`.
- The complete source-set selector, origin checker and assembler in
  `checks/source_bundle.py`.

## Smallest unresolved implication

The selected imported arithmetic estimates must be shown to control the
specified native signed covariance with constants uniform in every active
parameter, including completion and moving-endpoint errors. No theorem in this
companion establishes that implication. Any future strict improvement beyond
the imported 7/8 boundary needs a separately stated and reviewed estimate.
