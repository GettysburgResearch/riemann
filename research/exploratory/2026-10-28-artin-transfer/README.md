# Brauer transfer from Hecke zero-free regions to Artin L-functions

**Status:** Proposed classical transfer, conditional on the imported family-wide Hecke nonvanishing theorem; not a new proof of the Hecke theorem and not a claim of external novelty.

**Source input:** Baiying Liu, [*Zero-free half-planes for Hecke L-functions over number fields*](https://arxiv.org/abs/2610.26835), v1, 19 October 2026 (examined PDF SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`), claims a common boundary `B_flat = 0.874886647039964...`, specified there as a root of a quartic, for finite-order Hecke L-functions over every number field. Its Corollary 19.2 explicitly records monomial Artin representations; this note extracts a broader consequence using Brauer induction. We do not independently verify Liu's analytic theorem or claim priority for the corollary.

## Conditional proposition

Let `B` be real with `0<B<1`. Suppose that, for **every** number field `F` and **every** finite-order Hecke character `chi` of `F`, the full uncompleted `L_F(s,chi)` is holomorphic and nonzero on `Re(s)>B`, except that the trivial character has a simple pole at `s=1`. Let `L/K` be a finite Galois extension of number fields with group `G`, and let `rho` be any finite-dimensional complex representation of `G`. Then its full Artin L-function is holomorphic and nonzero in `Re(s)>B`, with a pole at `s=1` of order exactly `dim(rho^G)` when this integer is positive. In particular, for a nontrivial irreducible representation, it is holomorphic and nonzero everywhere on that half-plane.

The same conclusion, with the pole shifted from `s=1` to `s=1-it`, applies to `L(s+it,rho)` for every real `t`. It does not claim such a bound for arbitrary unitary Hecke or Weil characters with nontrivial archimedean type.

## Proof

Brauer's induction theorem expresses the character of `rho` as an **integer** linear combination

    chi_rho = sum_j n_j Ind_{H_j}^G theta_j,

where each `H_j` is a subgroup of `G`, each `theta_j` is a one-dimensional character of `H_j`, and `n_j` may be negative. For the fixed field `F_j=L^{H_j}`, class field theory associates to `theta_j` a finite-order Hecke character `eta_j`. Artin formalism, including induction and the local factors at ramified primes, gives the meromorphic identity

    L_K(s,rho) = product_j L_{F_j}(s,eta_j)^{n_j}.

The equality is initially valid in a right half-plane and then by meromorphic continuation. By the stated hypothesis, every factor and its reciprocal is holomorphic and nonzero on the target half-plane away from `s=1`; the finite product is consequently holomorphic and nonzero there, with no cancellation assumption.

At `s=1`, the nontrivial factors are holomorphic and nonzero; each trivial factor has a simple pole. The order of the product's pole is

    sum_{j: theta_j=1} n_j
      = <chi_rho, 1_G>
      = dim(rho^G),

where Frobenius reciprocity gives `<Ind_{H_j}^G theta_j,1_G> = <theta_j,1_{H_j}>`. This proves the assertion at `s=1` as well. Norm twists are the same statement after replacing `s` by `s+it`.

If Liu's stated all-number-field Hecke result is correct, take `B=B_flat`; this yields that strict half-plane for every finite-image Artin L-function, not just the monomial cases explicitly listed in the cited corollary. The Hecke hypothesis must apply over all intermediate fields, not just over the Eisenstein field or to Dirichlet characters. For comparison, Boyang Hu's [preprint](https://hexagonmath.org/2610.00216v1) claims `Re(s)>7/8` for the substantially broader class of unitary Weil L-functions; neither preprint was independently checked here.

**What was run:** A proof-level derivation from standard Brauer induction, class field theory and full local Artin formalism; no computational test or independent audit of Liu's theorem. The scope and exact classical references should receive independent mathematical review.

**Smallest remaining gap:** Independently audit the imported all-field Hecke theorem and this use of the full ramified Artin formalism; separately search for an earlier explicit statement of the same consequence. No new zero-free theorem for zeta is established by the transfer alone.
