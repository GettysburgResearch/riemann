# Relative zeta density for sixth-free natural labels

**Status.** A conditional family consequence of the proposed [full-sixth-free 49/78 estimate](../2026-10-29-full-sixthfree-fourth-density/README.md), the cubic natural-index zero density in rStation paper 52 v5 Theorem 5.7, the fixed-field quadratic large sieve and detector replay, and classical class field theory. The growing-twist detector quantifiers have a source-qualified replay in the linked 49/78 note; the short-cutoff transfer, source reciprocity and recent analytic inputs are not independently proved here. It is not an individual zero-free region and makes no exhaustive priority claim.

Let E=ℚ(ω), S the fixed good set including primes over 6, and u range over primary good sixth-power-free elements with `Nu≤X`. For u≠1, the source sextic character χ_u has a nontrivial tame component at each good prime dividing u. Restrict to those u for which χ_u has exact order 6, and let L_u/E be its cyclic sextic class-field extension. Subject to the listed inputs, for each ε>0 there exists τ>0 such that at most

    O_ε(X^(2/3+ε))                                             (1)

of the **distinct fields** L_u have a zero of `ζ_(L_u)/ζ_E` in `Re s≥4/5`, `|Im s|≤X^τ`. There are `≫X` distinct such fields: good squarefree u have primitive conductor `(u)` and order 6, so squarefree ideal counting gives ≫X distinct characters and each cyclic sextic field has exactly two generators. Thus (1) is a density-one relative-zeta rectangle in this natural-label family, with a sufficiently small height power. It is a count by natural label X, not by absolute discriminant. The fixed base ζ_E factor is not covered by (1).

Artin factorization gives five nontrivial primitive all-place factors induced by the indicated original presentations; fixed deleted Euler factors are nonzero in Re s>0. χ_u and χ_u⁵ have the same symmetric-height zero counts; their exceptional-label sum is `O(X^(49/78+ε))` under the proposed full-family input. The remaining powers reduce to lower-order natural families with their original masks:

* Write `(u)=v b³` with v cube-free, no coprimality assumption. Then on good a,

      χ_u(a)² = χ_v(a)² · 1_((a,b)=1).

  With the compatible principal FHL presentation detailed in [the sextic-family note](../2026-10-29-cyclic-sextic-family/README.md), primary cubic reciprocity gives `(v/a)₆²=(v/a)₃=(a/v)₃` on good coprime ideals, with the same zeros. Thus χ_u² and χ_u⁴ induce the conjugate principal cubic primitive characters attached to v. An arbitrary extra fixed ray twist is not covered by source52’s principal-twist theorem. Their zeros on `Re s>0` are unchanged by the deleted Euler factors. Source52 Theorem 5.7 at σ=4/5 gives `O(Y^(2/3+ε))` exceptional cubic labels `Nv≤Y` at a sufficiently small power height, subject to its principal-twist/source identification. Summing b costs

      X^(2/3+ε) Σ_b (Nb)^(−2−3ε) ≪ X^(2/3+ε).               (2)

* Write `(u)=w c²` with w squarefree, again retaining possible overlap. Then

      χ_u(a)³ = χ_w(a)³ · 1_((a,c)=1).

  The fixed-field quadratic Hecke large sieve and its source-qualified detector give `O(Y^(13/25+ε))` exceptional w labels at sufficiently small power height. Summing c costs

      X^(13/25+ε) Σ_c (Nc)^(−26/25−2ε)
         ≪ X^(13/25+ε).                                    (3)

The b,c power factors are good and their Euler deletions are finite and nonzero for `Re s>0`; extra masks at primes already ramified are redundant. Distinct u can share lower-order factors, and the sums above count every such multiplicity rather than ignoring it. A finite union over the five relative factors gives the exponent 2/3.

The source bounds in (2)–(3) are stated at a small power of the **local** label scale Y, while the claim uses one height X^τ. To make this uniform, split off small Y. For cubic `Nv≤X^h`, trivial u counting gives `≪X^(1/3+2h/3+ε)`; choose fixed `h<1/2`. For quadratic `Nw≤X^h`, the analogous bound is `≪X^(1/2+h/2+ε)`; choose `h<1/25`. The individual zero-count cost `X^(O(τ))` is absorbed by taking τ smaller than the resulting gaps. On the remaining dyads choose τ below h times the respective source height exponent, then sum dyads. This avoids silently applying a local-height theorem at the global height.

The fixed base factor has the exact factorization `ζ_E=ζ·L(s,χ_{−3})`. Thus the retuned [all-Dirichlet candidate](../2026-10-29-return-retune-8738694/README.md), conditional on tracker admission and its conventional L-function interpretation, would give ζ_E nonvanishing in `Re s>0.8738694`; no additional Eisenstein-Hecke bridge is required for this particular base field. Combining it with a relative estimate above applies to a **full ζ_(L_u)** rectangle only when its fixed real-part boundary is strictly greater than 0.8738694. The present numerical statement (1) at 4/5 does not meet that condition; a full-zeta corollary needs the corresponding relative density calculation at a larger fixed σ and the smaller common height.

For absolute discriminant, the conductor–discriminant formula gives

    |D_L|=|D_E|⁶ (N f_χ)² (N f_(χ²))² N f_(χ³).

The contributions of a good prime to this exponent are 5, 4, or 3 according as the local order of χ is 6, 3, or 2. These exponents vary with the valuations in u. While squarefree labels give a subfamily with discriminant ≍(Nu)^5, a single power change from the full natural-label count to discriminant ordering is not justified by (1).

**Independent review.** High_match and Families checked the cubic and quadratic power masks, convergent multiplicity sums, small-local-label height split, natural-label field fibers, the corrected Dirichlet base factorization and the discriminant-ordering limitation, conditional on the stated analytical inputs.
