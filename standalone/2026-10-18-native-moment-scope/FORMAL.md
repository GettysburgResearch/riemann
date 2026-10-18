# Isolated formal component

`NativeMaskFinite.lean` proves five scoped lemmas:

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

For the last lemma, the intended paper interpretation is
`P(t) := there exist C,D0 such that |A_fixed_row(D)|<=C D^t for D>=D0`.
The file deliberately leaves P abstract. It verifies the order of the
quantifiers, and does not claim a Lean construction of that native function
or of the Mellin implication to a zero-free half-plane.

The exact toolchain is Lean 4.35.0-rc3, with Mathlib commit
`0493595ecd5da8ef14742febab99728f98e948e8`. The accompanying `lean-toolchain`
and `lakefile.toml` pin this separate project. With that toolchain installed,
the intended standalone reproduction is

```sh
lake update
lake exe cache get
lake build
```

The actual session also checked the file directly in the pinned primary CT
project's Lake environment, using exactly that Mathlib revision:

```text
lake env lean --root=<this-directory> <this-directory>/NativeMaskFinite.lean
```

`FORMAL_RECEIPT.json` pins the tested source, command, toolchain and printed
axiom closures. The source contains no `sorry` or project axiom. Its five
printed closures use only `propext`, `Classical.choice`, and `Quot.sound`.

This file is outside the repository's historical formal-v0.1 project and
does not alter its trusted targets, toolchain or actual-xi status. It does
not formalize the Hecke source, the infinite Euler-product bound, the
Gaussian transform, a critical native estimate, field RH or ordinary RH.
The separate CT build receipt concerns an EXTERNAL imported theorem and
must not be read as formalization of the new analytic deductions here.
