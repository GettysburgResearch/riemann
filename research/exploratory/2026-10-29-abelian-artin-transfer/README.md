# Fixed Dirichlet strips for abelian Dedekind zeta and Artin L-functions

**Status.** This is the classical Artin–Dirichlet factorization applied to an assumed fixed Dirichlet strip. It does not supply an independent zero-free theorem, a new proof of the source strip, or a priority claim. The staged θ=4369351/5000000 Lean candidate in [the return audit](../2026-10-29-arvi-return/README.md) has compiled and its imported constants have passed `leanchecker --fresh` using the same Lean kernel. Its conventional Dirichlet and Riemann L-function interpretation, external verification and tracker admission remain separate gates. Nothing below asserts a fresh Lean formalization of the transfers.

## Transfer statement

Let `0<θ<1`. Assume that ζ(s) is zero-free for `Re s>θ`, apart from its simple pole at 1, and that every primitive nonprincipal Dirichlet L-function is zero-free there. Let K/Q be any finite abelian Galois extension and let ρ be a finite-dimensional complex representation of `G=Gal(K/Q)`.

Then the Dedekind zeta function `ζ_K(s)` has no zeros in `Re s>θ` and has its simple pole at s=1. The Artin L-function `L(s,ρ,K/Q)` also has no zeros in that half-plane; its only pole there is at s=1, with order equal to the multiplicity of the trivial representation in ρ. If that multiplicity is zero, it is entire. The statements hold simultaneously for every such K and ρ, with the same θ. They are qualitative and claim no uniform lower bound for the absolute values.

The standard completed functional equations reflect nontrivial zeros across `Re s=1/2`, with the contragredient representation on the Artin side. Since its irreducible factors are also covered by the same Dirichlet hypothesis, there are likewise no zeros in `0<Re s<1−θ`. Thus every nontrivial zero in the critical strip lies in `1−θ≤Re s≤θ`. These mirrored statements concern the open critical strip and do not exclude the usual trivial zeros outside it.

## Proof and local factors

Every irreducible complex representation of finite abelian G is a one-dimensional character. Write

    ρ ≅ ⊕_{χ∈Ĝ} m_χ χ,       m_χ∈Z_{≥0}.

By Kronecker–Weber and Artin reciprocity, each χ corresponds to a unique primitive Dirichlet character `χ*` (up to the harmless reciprocity convention of inversion), and its one-dimensional Artin L-function agrees with `L(s,χ*)`. At a ramified prime the Artin factor is defined using inertia invariants: for a ramified one-dimensional χ these invariants are zero and the factor is 1, exactly as for its primitive Dirichlet character. At an unramified prime the Frobenius eigenvalue supplies the usual Euler factor. Thus, initially for `Re s>1` and then by meromorphic continuation,

    L(s,ρ,K/Q) = ∏_{χ∈Ĝ} L(s,χ*)^{m_χ},
    ζ_K(s)     = ∏_{χ∈Ĝ} L(s,χ*).                            (1)

The second line is the regular-representation factorization; its trivial-character factor is ζ(s), and every other factor is a nonprincipal primitive Dirichlet L-function. Their assumed nonvanishing and entireness, together with ζ's simple pole and absence of zeros in the region, give the claims. The order of the pole in the first line is exactly m_triv, because all the nontrivial factors are nonzero at 1 under the hypothesis. □

Using a character induced modulo a nonminimal modulus does not introduce zeros in `Re s>0`: the imprimitive L-function differs from its primitive L-function by finitely many factors `(1−χ*(p)p^(−s))`, each nonzero there. For the principal character the primitive L-function is ζ; finite Euler deletions preserve its simple pole at 1. One must nevertheless use the primitive factors in (1) to obtain the **exact** complete Artin and Dedekind Euler products.

Under the staged candidate's intended all-Dirichlet interpretation, take `θ=4369351/5000000=0.8738702`. This gives the displayed common region for every individual abelian K and abelian Artin representation, subject to the verification gates in the status paragraph. The already reported 7/8 Dirichlet theorem implies the same statement with θ=7/8 by the same standard factorization, so only the small change of θ is inherited from the candidate. No claim is made here about nonabelian Artin representations, Hecke characters over a general base field, or their zero-free regions.

**Independent review.** High_match checked the primitive and ramified Euler factors, pole orders, zero-free imprimitive corrections, contragredient functional-equation reflection, and source qualifications; no substantive defect was found.
