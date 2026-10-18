# Isolated formal component

`NativeMaskFinite.lean` proves six scoped lemmas:

1. `divisor_double_count`: the complete finite f=1*g double sum, with every
   related pair retained.
2. `average_mask_bound`: a nonnegative divisor expansion and a supplied
   counting bound imply the finite linear average estimate.
3. `moment_transfer`: a supplied literal pointwise bound implies the
   complete finite even-moment bound.
4. `cofinal_exponent`: an unbounded set of fixed orders and sublinear excess
   make the family-height/excess exponent arbitrarily small.
5. `cofinal_fixed_order_extraction`: an upward-closed growth property follows
   at every exponent above 1/2. Each fixed-order premise may include its own
   arbitrary constant, threshold and positive epsilon loss.
6. `geometric_exponent_bootstrap`: an upward-closed property, a starting
   exponent of one, and a supplied recurrence theta -> max(a,r theta),
   with a>0 and r<1, reach a after finitely many steps. The intended
   prime-replica application has 0<=r<1.

For the two abstract growth lemmas, the intended paper interpretation is
`P(t) := there exist C,D0 such that |A_fixed_row(D)|<=C D^t for D>=D0`.
The file deliberately leaves P abstract. It verifies the order of the
quantifiers, and does not claim a Lean construction of that native function
or of the Mellin implication to a zero-free half-plane.

The exact toolchain is Lean 4.35.0-rc3, with Mathlib commit
`0493595ecd5da8ef14742febab99728f98e948e8`. The accompanying `lean-toolchain`
and `lakefile.toml` pin this separate project. With that toolchain installed,
the standalone reproduction is

```sh
lake update
lake exe cache get
lake build
```

The actual session first checked the five earlier lemmas directly in the
pinned primary CT Lake environment. The complete six-lemma project was
then copied into a fresh directory, resolved from its own lakefile, obtained
the Mathlib cache and built with `lake build`. It imports only the specific
tactics used, rather than the complete tactic bundle. This standalone
check uses no CT library, theorem or custom axiom.

`FORMAL_RECEIPT.json` pins the tested source, command, toolchain and printed
axiom closures. The source contains no `sorry` or project axiom. Its six
printed closures use only `propext`, `Classical.choice`, and `Quot.sound`.

This file is outside the repository's historical formal-v0.1 project and
does not alter its trusted targets, toolchain or actual-xi status. It does
not formalize the Hecke source, the infinite Euler-product bound, the
Gaussian transform, a critical native estimate, field RH or ordinary RH.
The analytic prime-row inequality in Theorem B1, which supplies the
geometric recurrence, remains a paper proof. The sixth lemma verifies
the finite logical bootstrap once that recurrence is supplied.
The separate CT build receipt concerns an EXTERNAL imported theorem and
must not be read as formalization of the new analytic deductions here.
