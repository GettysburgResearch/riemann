# The cubic power bottleneck for cyclic sextic fields

**Status.** A source-qualified family-density calculation, not an individual zero-free theorem or priority claim. It imports the sextic inverse and unmarked ordinary fourth moments, the source FHL power-character matching, de Faveri's cubic sieve, the quadratic sieve/detector and their common-height/profile replays. The stronger Eisenstein cubic bound additionally uses the claimed Theorem 1 of [rStation paper 52 v5](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5). For full-zeta statements at the candidate boundary it also assumes admission and the conventional Dirichlet interpretation of the separately staged candidate. None of these recent analytical claims is independently established here.

Let F be either Q(ω), using the cited Eisenstein sextic moments, or Q(ζ₁₂), using Liu Theorem 12.14, Remark 12.16 and the corresponding inverse moment. Fix compatible sextic/cubic/quadratic FHL source presentations and good S, and let χ_u range over exact-order-six characters with good sixth-free labels Nu≤X. Their cyclic sextic class fields L_u/F have ≫X distinct members, already from squarefree labels, because the good local conductor determines each squarefree label and a field has only two order-six character generators.

For each fixed σ and ε, choose the detector, moment losses and then a common small τ>0. At σ=4/5 the cited sextic moments give the order-six factor exponent 9/19; at `θ=4369347/5000000` they give `3795224/13141959≈0.288787`. The cubic and quadratic powers must also be counted. From the source bounds and the multiplicity calculation below, the **full relative quotient** is controlled by

    σ=4/5:  O(X^(2/3+ε)) for F=Q(ω),  O(X^(8/11+ε)) for F=Q(ζ₁₂),
    σ=θ:    O(X^(1/2+ε)) for F=Q(ω),  O(X^(6306530/11891959+ε)) for F=Q(ζ₁₂).  (1)

These bounds apply in `Re s≥σ`, `|Im s|≤X^τ`. At θ the quadratic factor controls the all-label Eisenstein estimate, while the cubic factor controls the Q(ζ₁₂) estimate. The cubic exponent improves on the latter's former inverse-only value. No optimality or exhaustive priority claim is made.

## Retaining all three orders

Artin factorization gives `ζ_L/ζ_F=∏_{j=1}⁵ L_F(s,(χ_u^j)^*)`, with primitive all-place factors. The source's zero-extended S-good presentations can omit additional fixed-S Euler factors, but those factors do not vanish for Re s>0 and therefore have the same zeros there. The faithful factors j=1,5 have identical symmetric zero counts. Decompose each sixth-free label uniquely as `u=v b³`, with v cube-free and no coprimality requirement. With original zero extensions,

    χ_u²(a)=χ_v²(a)·1_((a,b)=1).                             (2)

The extra Euler deletion has no zeros for Re s>0. The compatible powered-family construction identifies the primitive χ_v² with a cubic FHL character up to the fixed allowed embedding; this matching, including its S-unit sectors, is an explicit source input. Every v admits at most `O((X/Nv)^(1/3+ε))` b choices. If cubic density for Nv≤V is `O(V^(D+ε))`, a small-label height split and partial summation give

    # {u≤X with a cubic-power zero} ≪ X^[max{1/3,D}+ε].       (3)

For instance, split Nv≤X^η trivially at `X^(1/3+η+ε)`; on larger dyads choose the common X-height below the local V-power allowance, and sum `(X/Nv)^(1/3)` against the density count. At σ=4/5, de Faveri gives D=8/11 for fixed F. For F=Q(ω), rStation paper 52 v5 Theorem 5.7 claims the sharper D=2/3 at σ=4/5 for the compatible principal cubic family, so (1)'s first exponent improves to 2/3 in that case; it is a separate unverified source input.

At θ, the direct cubic n-free sieve plus the source-qualified **long-cutoff** detector gives the Q(ζ₁₂) exponent in (1). Put `h=2(1−θ)=630653/2500000`, `δ=1−h`, `t=10/(4+3h)=25000000/11891959`, and `L=4t/5`. The exact Θ₃ count exponent is

    f(r)=max{1−δr, (1−δ)r, 2/3+(2/3−δ)r}.

On `[L,t]` the last face decreases until r=2 and the second increases after r=2; the first is dominated there. Their endpoint values at L and t agree at

    R₃=10h/(4+3h)=6306530/11891959.                            (3a)

If `r≥L`, apply the inverse second moment; otherwise `4m≥4(t−r)>L` and `4m≤2`, so apply the ordinary eighth moment to cover the actual witness range. The detector's `t≤5/2` extension and powered-block profile transfer are explicit source-qualified replays, not the printed t≤3/2 statement. See the [uniform detector proof](2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md) and [scalar analysis](2026-10-29-direct-nfree-density/README.md). This R₃ is smaller than de Faveri's cubic θ exponent `2741281467955/5056830380773` and the Khale et al. fixed-height conductor value `2522612/4369347`, with height losses absorbed by choosing τ small. These named comparisons are not exhaustive.

For F=Q(ω), paper 52 v5 Theorem 1 instead claims the stronger cube-free cubic exponent `D₅₂=1891959/4564490≈0.41449516` at θ, including fixed finite S-supported twists. This improves on (3a) for E but does not automatically transfer to Q(ζ₁₂). Its application assumes that the powered cubic family in (2), including finite ray sectors and primitive factors, matches the source. The theorem is dyadic; split `Nv≤X^η` trivially and, for larger dyads, take the common height exponent below η times the source's local height allowance. Since D₅₂>1/3, (3) then gives `X^(D₅₂+ε)` cubic-power exceptions after choosing η and τ in terms of ε.

Similarly write `u=w c²` with w squarefree, again allowing overlap. Then

    χ_u³(a)=χ_w³(a)·1_((a,c)=1).                             (4)

The quadratic core is an allowed powered FHL family, and there are `O((X/Nw)^(1/2+ε))` c choices. A quadratic core exception exponent Q therefore gives `X^[max{1/2,Q}+ε]` after the same small-label height split. At σ=4/5, `Q=13/25`; at θ, `Q=4332174293591/12500000000000<1/2`. Thus the θ quadratic contribution `X^(1/2+ε)` dominates the Eisenstein cubic contribution, but is smaller than (3a) over Q(ζ₁₂). Conjugate cubic powers share symmetric zero counts. Finite S factors, fixed-sector fibers, divisor bounds and logarithmic dyads contribute only X^ε.

The unmarked sextic count itself uses `t=5/(5−2δ)` and `R₀=(15−16δ)/(15−6δ)`, δ=2σ−1, as derived in [the return-gate note](2026-10-29-sextic-fourth-return-gate.md). The row detector uses the same original χ_u and one global X-height; all moment and profile constants must be uniform under that presentation. For F=Q(ζ₁₂), Liu's allowed-generator family and de Faveri's sextic FHL family must be related through the finite S-unit sectors, including shared-prime zero masks; their matching is not replaced by a conductor-only comparison. For F=Q(ω), use the separately stated Eisenstein source moment and its primary-symbol identification rather than applying Liu's μ₁₂ field hypothesis directly.

## Full zeta and discriminants

At θ, the conditional Dirichlet candidate controls the base factors of both F=Q(ω) and F=Q(ζ₁₂): these Dedekind zetas are finite products of primitive Dirichlet L-functions, with ζ itself as the principal factor. Hence all but the θ-exception count in (1) have full ζ_L zero-free in the **open** rectangle `Re s>θ`, `|Im s|≤X^τ`, with the pole at 1 excluded. At σ=4/5 the candidate boundary is too far right to control ζ_F in the desired closed rectangle; (1) remains a relative-quotient statement there.

For general sixth-free labels, every nontrivial power has conductor norm `≪Nu`, so `|D_L|≪X⁵`. Taking X a fixed small multiple of Y^(1/5) supplies a specified ≫Y^(1/5)-field family below Y and exception exponents `1/10` over E and `1261306/11891959` over Q(ζ₁₂), at θ, up to ε. This is an X-truncated natural-label family, not a count of all cyclic sextic fields with |D_L|≤Y.

For squarefree u the cubic and quadratic cores both have the same good conductor u, so the extra label multiplicities in (3) and (4) disappear. Over E the maximum of the order-six, cubic and quadratic θ exponents is D₅₂; therefore at most `O(X^(1891959/4564490+ε))` of these ≫X fields are exceptional. Here every nontrivial power has good conductor u, so `|D_L|≍(Nu)⁵`. The global-X height and small-label split give the cumulative squarefree-label discriminant bound `O(Y^(1891959/22822450+ε))`, with ≫Y^(1/5) fields and a suitably small Y-power height. Over Q(ζ₁₂), the available cubic bound (3a) still dominates on squarefree labels. In both cases the full-zeta claim is conditional on the open base strip and does not include the line Re s=θ.

**Independent review.** Families checked both power decompositions and masks, multiplicity/height accounting, the field-source distinction, exact θ fractions, field fibers and the squarefree discriminant conversion. The reviewer rechecked the revised E and Q(ζ₁₂) θ bottlenecks and squarefree E discriminant exponent. The reviewer treats the cited analytic estimates and their source matching as inputs and noted the primitive all-place convention in the factorization above.
