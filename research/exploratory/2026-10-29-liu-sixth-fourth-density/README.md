# Sixth-order density from Liu's ordinary fourth moment

**Superseded by the same source’s inverse moment.** Liu Theorem 10.4 and Lemma 10.6 additionally claim `Σ|M_r|²≪X^[max(1,(1+5r)/6)+ε]` on the same sixth-free rows. Combining that bound with Liu’s z=0 fourth moment yields the stronger rate `R=(15−16δ)/(15−6δ)` for `0<δ<5/6`: at σ=4/5 it is 9/19≈.473684, and at θ it is 3795224/13141959≈.288787. Thus the weaker Θ₆–Liu rate below is **not a new improvement over Liu** when the respective source-family bridges hold. The full-rate source and bridge also remain unverified here; [the Liu source minimax note](../2026-10-29-liu-source-minimax-barrier.md) gives the exact moment obstruction and an unproved local mixed-correlation target.

**Status: conditional source synthesis; arithmetic matching is not closed.** The deduction below combines de Faveri's n-free-row Θ₆ sieve and the [long detector proof](../2026-10-29-direct-nfree-density/UNIFORM-DETECTOR-PROOF.md) with the recently claimed ordinary fourth moment in [Liu, Theorem 12.14 and Remark 12.16](https://arxiv.org/html/2610.26835v1#S12.Thmtheorem14). That source theorem and its induction are not independently verified here. A bridge identifying its allowed-generator rows with the precise ideal-index FHL family of the Θ₆ source, including finite ray/unit sectors, original zero masks and fixed-height profile seminorms, is an additional explicit hypothesis. Liu's Part II assumes fixed cyclotomic F containing μ₁₂; its Part III claims a general F⊃μ₁₂ extension. Neither statement directly covers Q(ω), which does not contain μ₄. No individual zero-free half-plane is proved.

Assume the following for one fixed field F⊃μ₁₂ and fixed S and sextic data:

* The exact good sixth-free ideal characters used by the detector obey de Faveri's Θ₆ estimate with arbitrary common squarefree columns, finite sectors and original masks, as in [the direct theorem](../2026-10-29-direct-nfree-density/README.md).
* For the same nonprincipal inducing rows and common fixed profiles, Liu's z=0 assertion supplies

      Σ_{u sixth-free; Nu≤X} |S_m(u;β,h)|⁴
           ≪ X^(1+ε)(1+|h|)^A,       0≤m≤1/2+o(1).          (1)

  The estimate holds for the fixed derivative orders and β in the detector Sobolev step; profiles, finite classes and the one global height allowance are fixed before the requested small power loss. Liu's z=0 statement itself excludes only principal inducing rows and imposes no β*(F) hypothesis. Principal presentations contribute at most an individually counted fixed row. The source also requires verifying the allowed-generator / FHL bridge, not merely comparing conductor sizes.
* The fixed-field Hecke/FHL conductor and mask inputs used by the long detector are available, so the simultaneous inverse and ordinary witnesses have `r≤t`, `m≤1/2`, and `r+m≥t`, up to arbitrarily small fixed losses, with their respective squared thresholds `X^(δr)` and `X^(δm)`.

For every fixed `1/3<δ=2σ−1<5/6`, the following density statement then holds for the matched sextic family:

    Σ_{u sixth-free; Nu≤X} N(σ,X^τ;χ_u)
          ≪ X^(R+ε)                                           (2)

for every ε>0 and some sufficiently small τ>0, with R defined by (4). In particular,

    σ=4/5: R=181/298≈0.607383,
    σ=θ:   R=19615469784638/44055542392319≈0.445244.

At 4/5 the earlier direct Θ₆ witness gives 137/222≈0.617117, so the exact gain is `161/16539`. At θ the earlier direct exponent is `22061549/48851754≈0.451602`, so the gain is `13683402696154287079/2152190519286139277526≈0.006358`. No all-height or all-number-field conclusion follows from (2).

## Exact detector optimization

Set `f(x)=max(1−δx,(1−δ)x,5/6+(1/3−δ)x,1/3+(5/6−δ)x)`. By Θ₆ the inverse witness counts at exponent f(r). The fourth-moment hypothesis (1) yields ordinary-witness exponent `1−2δm`. Since `m≥t−r` and `r≤t`, this is at most `h_t(r)=1−2δ(t−r)`.

Throughout `1/3<δ<5/6`, choose

    t = −2(15δ−2)/(18δ²−39δ+5),
    r₀ = −(42δ−5)/[2(18δ²−39δ+5)],
    m₀ = t−r₀ = −3(6δ−1)/[2(18δ²−39δ+5)].                (3)

The exact checker [check.py](check.py) verifies the following identities, which prove `1<t<3/2`, `t−1/2<r₀<1`, and `0<m₀<1/2` throughout the open range. With `A=−18δ²+39δ−5`, the positive quantities are

    t−1=(3δ−1)(6δ−1)/A,
    3/2−t=(−54δ²+57δ−7)/(2A),
    1−r₀=(5−6δ)(6δ−1)/(2A),
    1/2−m₀=(−18δ²+21δ−2)/(2A).

A and the two displayed quadratic numerators are concave and positive at both range endpoints. The admissible inverse range starts at `r≥t−1/2>1/2`. On `[t−1/2,1]`, f equals the decreasing face `f₂(r)=5/6+(1/3−δ)r`, and h_t increases; their minimum is maximized at their intersection r₀. On `[1,t]`, f equals the increasing face `f₃(r)=1/3+(5/6−δ)r`, while h_t increases, so their minimum is at most f₃(t). Algebra gives

    f₂(r₀)=h_t(r₀)=f₃(t)
       = (36δ²−42δ+5)/(18δ²−39δ+5)=R.                      (4)

Thus every saturated detector row has at least one admissible witness count ≤X^(R+ε). The ordinary moment is not applied when its length exceeds 1/2: the detector controls that excess by arbitrarily small fixed losses before the profile and height choices.

At σ=4/5 these parameters simplify to `t=175/149`, `r₀=505/596`, `m₀=195/596`. At θ they are respectively `57600512500000/44055542392319`, `41257858750000/44055542392319` and `16342653750000/44055542392319`.

## Exact continuum comparison

In the same range, the earlier direct full n-free Θ₆ density exponent R₀ and de Faveri's natural-label middle-branch exponent D both exceed (4). Let `B=−18δ²+30δ−5`; A and B are positive on the closed interval by concavity and positive endpoint values. Exact factorization gives

    R₀−R=(3δ−1)(5−6δ)(6δ+1)/[6(11−6δ)A] > 0,
    D−R=3δ(3δ−1)(5−6δ)(6δ−1)/(2AB) > 0.                (5)

For each fixed σ the strict comparison survives sufficiently small positive height powers. The comparisons are conditional on the matched ordinary fourth-moment input and the stated recent source claims; they do not imply priority over every existing theorem.

## Source bridge to be checked

Liu's Lemma 3.3 gives one allowed generator modulo sixth S-unit powers for each exterior ideal, and the remaining unit-sector group is finite. In its equation (6.3) an allowed generator can be compared with an FHL presentation as `k=ε_k x m_E z⁶`, with ε_k in the fixed finite group O_{F,S}×/(O_{F,S}×)⁶. Kummer characters then suggest a partition by ε_k and finite ray data, with a fixed S-supported column twist and one global orientation, matching χ_n(k) to the FHL χ_u(n) on good coprime ideals; sixth-free good ramification matches the shared-prime zero masks. Liu explicitly proves the corresponding cubic-power comparison in (6.3)–(6.4), but this exact **sextic** comparison, the primitive presentation and representative-count transport must still be proved for the chosen Θ₆ data. They are not inferred merely from the printed cubic identity. This is the main gap in applying (1) to the whole natural ideal-index family.
