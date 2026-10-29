# Scope of the candidate Eisenstein Hecke bound

**Status:** Source-level and classical arithmetic identification; the separately prepared Lean Hecke corollary has not yet been compiled, the fresh kernel replay is pending, and the semantic bridge to the standard Hecke theory is not formalized here. No new numerical bound is claimed independent of those checks.

The `0.8738702` candidate's `Return.Endpoint.beta_le_theta_of_sources`, together with `ChainF50.final_source` and `source_64`, proposes a bound on `HeckeZeroSupremum.beta`. Its defining zero set ranges over `HeckeFamily.Character` for `K=CyclotomicField 3 ℚ`, hence K≅E=ℚ(ω). A proposed direct Lean corollary is [HeckeCorollary.lean](../2026-10-29-arvi-return/HeckeCorollary.lean). This is a stronger formal scope than the Dirichlet-only type of `Candidate.bound`, but it must be separately compiled and inspected.

## Character and L-function identification

In the pinned source `Hecke/Family.lean`, a `Character` consists of a nonzero ideal modulus M, a complex multiplicative character of O_E/M, trivial on the images of units, and a positive integer period lying in M. `Character.ofResidue` constructs the period automatically from the finite quotient. `Hecke/IdealBridge.lean` defines its ideal coefficient and proves `idealCoeff_span`: on every nonzero principal ideal `(a)`, the coefficient is exactly the residue character of a. The unit-trivial condition makes this independent of the generator. The same file proves the formal L-function is the ideal Dirichlet series in `Re s>1`, with the correct factor of six when passing from element sums to ideal sums; `Hecke/Euler.lean:LFunction_eq_series` restates this as the ideal Euler series.

Classically, E has class number 1. For each finite modulus M, the ray-class exact sequence becomes

    O_E^× → (O_E/M)^× → Cl_M(E) → Cl(E)=1.

Thus every character of the finite ray-class group is exactly a residue-unit character as above. Conversely every such unit-trivial residue character defines a ray-class character. A finite-order Hecke character has trivial infinity component here: the complex multiplicative group is connected, so a continuous finite-image archimedean character is trivial. Standard conductor theory therefore realizes every finite-order Hecke character of E by such a finite ray-class character. This exact sequence and its classical application are arithmetic inputs in this note; we have not constructed a Lean equivalence with a separate library's abstract Hecke-character type.

Take a primitive Hecke character of conductor f and choose a proper nonzero presentation modulus M divisible by f; for example, multiply f by a fixed prime ideal not dividing f. This also handles the trivial conductor f=(1), avoiding the zero ring O/(1). The corresponding zero-extended ideal series differs from the primitive series by the finite product

    ∏_(p|M, p∤f) [1−χ*(p)(Np)^(−s)].

Each factor is nonzero for `Re s>0`, so imprimitive presentation cannot create or remove zeros there. The source's `LFunction_differentiableAt` and `LFunction_entire_nonprincipal` establish the relevant continuation properties; the usual Hecke L-function has the same continuation, uniquely determined by its series on `Re s>1`. The identity theorem on the connected half-plane away from the possible principal pole at 1 identifies them. For the principal character, state nonvanishing only away from s=1, where the standard L-function has a pole. This establishes the mathematical semantic match assuming standard Hecke/class-field theory and the correctness of the formal source definitions; it is not a formal bridge theorem.

## Conditional classical consequences

If the candidate β theorem is compiled, its fresh replay succeeds and the semantic/source audit closes, then every finite-order Hecke L-function of E is nonzero for `Re s>0.8738702`, away from the principal pole at s=1. This includes the Kummer/sextic character family over E as well as arbitrary finite-order ray characters over E, subject to the matching above.

For every finite abelian extension L/E, global class field theory identifies each one-dimensional Artin character of `Gal(L/E)` with such a Hecke character, and the Artin factorization gives

    ζ_L(s) = ∏_(χ∈Gal(L/E)^∧) L_E(s,χ).

Consequently every such ζ_L has no zero in `Re s>0.8738702` away from its pole at 1, and every one-dimensional Artin L-function of L/E has the same region. The extension L need not be abelian over ℚ: for example `L=E(∛2)` is cyclic over E, while its Galois group over ℚ is S₃. These standard factorization corollaries have not been formalized or separately compiled.

The same source argument is already available in tracker PR94 at θ=`43693617/50000000=0.87387234`: its endpoint also bounds this Hecke supremum, not merely its displayed Dirichlet transfer. Thus the candidate's improvement within this E/abelian-extension scope is exactly `107/50000000=0.00000214`, not a new arbitrary-number-field or infinite-type Hecke result. The original PR94 theorem and current candidate remain subject to their own source and kernel verification.

**Independent review:** High_match checked the ray-class identification, trivial infinity component, analytic-continuation and Euler-factor argument, abelian-extension consequence, and PR94 comparison. The reviewer noted and the text now handles the trivial-conductor modulus by choosing a proper presentation modulus. The formal Hecke corollary and abstract-character bridge remain uncompiled/unformalized.
