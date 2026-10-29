# Scalar barrier for Liu's inverse and ordinary moments

**Scope.** Conditional on the stated source inequalities, this is an exact limitation of their positive-moment/detector scalar relaxation, not a counterexample to the actual Hecke family, to a structured mixed moment, or to an individual zero-free region. The source family's arithmetic identification and Liu's recent results remain unverified inputs.

Liu Theorem 10.4 and Lemma 10.6 claim, for the appropriate sextic family over fields containing μ₁₂, the inverse moment exponent `e(r)=max{1,(1+5r)/6}`; Liu Theorem 12.14 at z=0 claims an ordinary fourth moment of exponent 1 for `m≤1/2`, with the stated profile and polynomial-height controls. The z=0 assertion does not itself require a β* premise. The detector supplies simultaneous squared thresholds `X^(δr)` and `X^(δm)`, with `r≤t`, `m≤1/2`, `r+m≥t` up to small fixed losses. For `0<δ<5/6`, put

    t*=5/(5−2δ),  r*=2t*/3,  m*=t*/3,
    R=(15−16δ)/(15−6δ)=1−δr*.                               (1)

The Liu inverse count `e(r)−δr` and ordinary count `1−2δm` attain R at `(r*,m*)`, and the long inverse at `(t*,0)` also attains R. Standard monotonicity gives the upper bound R by choosing t=t*. This is the x=0 source rate in Liu's Proposition 2.7, subject to its source hypotheses; the elementary two-moment derivation uses the unamplified inputs directly and avoids assuming a prime-slot condition. At σ=4/5 it is 9/19; at the tracker θ it is 3795224/13141959≈.288787. This dominates the [generic-Θ₆ plus Liu ordinary-fourth rate](2026-10-29-liu-sixth-fourth-density/README.md) whenever the two estimates apply to the same rows.

## Arbitrary generic mixed monomials

Add the generic de Faveri Θ₆ estimate for every fixed monomial `M^a S^b`, a,b nonnegative integers not both zero. Divisor-bounded convolution, common profiles and squarefree-column extraction put its count exponent at `f(ar+bm)`, where

    f(x)=max{1−δx,(1−δ)x,5/6+(1/3−δ)x,1/3+(5/6−δ)x}.      (2)

When `1≤t≤t*`, the witness `(r,m)=(r*,m*)` is admissible because `r*≤1`, `m*≤1/2` and r*+m*=t*. The two Liu counts equal R. For (a,b)=(0,1), f₀(m*)=1−δm*>R; for (1,0) and (0,2), f₀(r*)=R. Every other nonzero pair has `ar*+bm*≥t*`, so, since δ<5/6,

    f(ar*+bm*) ≥ 1/3+(5/6−δ)t* = R+1/6.                    (3)

For `t*≤t≤3/2`, the witness `(r,m)=(t,0)` is admissible. The Liu inverse count is `1/6+(5/6−δ)t≥R`, the ordinary fourth count is 1, and every generic monomial with a≥1 has `f(at)≥f₃(t*)=R+1/6`; a=0 has f(0)=1. Hence no finite collection of these separate or generic mixed monomial moments lowers the worst-case scalar exponent on this cutoff range.

A positive-data model makes the Hölder limitation concrete. At the first witness, take approximately X^R rows with `|M|²=X^(δr*)`, `|S|²=X^(δm*)` and all other rows zero. It saturates the Liu inverse second and ordinary fourth bounds, while (2)–(3) show that every fixed generic mixed monomial bound is respected up to small powers. Thus Hölder or Cauchy applied only to those positive inequalities cannot rule out this data. The model is not claimed to arise from characters or detector zeros. A genuinely sharper estimate for the actual arithmetic joint correlation, additional detector structure, or another source input could still improve R.

## A local arithmetic input sufficient to improve the source rate

The scalar obstruction does not preclude cancellation for the actual product. Fix `1/3<δ<5/6` and the same field, source and detector hypotheses. Suppose that for some fixed κ,c>0, uniformly in the common profiles and their fixed Sobolev derivative orders, both common character orientations, and `|r−r*|,|m−m*|≤c`, one has the structured mixed estimate

    Σ_{u sixth-free; Nu≤X} |M_r(u) S_m(u)|²
        ≪ X^(1+δm−κ+ε).                                      (4)

Here M is the actual normalized Möbius inverse block and S the actual normalized ordinary block, with original masks, and the fixed polynomial norm-twist-height costs are absorbed by a sufficiently small global height exponent. The exponent `1+δm` is the baseline supplied on buffered detected rows by Liu's inverse second moment and the pointwise bound `|S_m|²≪X^(δm+ε)`; (4) asks for a fixed power saving on the *actual* joint correlation. Stating it as an all-row bound is a strong sufficient hypothesis; a proved version on the buffered detected subfamily with the same profile quantifiers would also suffice. It is not currently proved.

Under (4), the same source-qualified detector gives a density exponent strictly smaller than R. To see this, define `I(r)=e(r)−δr` and `O(m)=1−2δm` on the admissible compact domain `D_t={0≤r≤t, 0≤m≤1/2, r+m≥t}`. At t=t*, the exact equality locus of `min(I(r),O(m))≤R` is

    {(r*,m*)} ∪ {(t*,m): 0≤m≤m*}.                            (5)

Indeed I strictly decreases for r<1 and strictly increases for r>1; its R-levels are r* and t*, and O(m)≥R exactly when m≤m*. The simultaneous constraints force the isolated point for r≤r* and leave the stated vertical segment at r=t*.

Take `t=t*−η>1` for a sufficiently small fixed η. Choose a neighborhood U of `(r*,m*)` contained in the box of (4), small enough that `1−δr−κ≤R−κ/2` throughout U. At t=t*, compactness gives a strict saving away from U and a neighborhood of the vertical segment; the saving persists for t sufficiently close to t*. Inside the vertical neighborhood, r≤t*−η and the increasing long-inverse face gives a fixed saving at least `(5/6−δ)η`. Within U, saturation and (4) yield the count exponent `1+δm−κ−δ(r+m)=1−δr−κ≤R−κ/2`. After a finite dyadic/profile partition, choose all detector losses and the global height power small enough to preserve a positive fraction of the savings. This gives `X^(R−κ'+ε)` for some κ'>0.

The product coefficients in (4) are the normalized restricted Möbius divisor sums of [the mixed-coefficient obstruction](2026-10-29-mixed-witness-coefficient-obstruction.md). At r*=2m*, their squarefree coefficient ℓ² mass is ≫`1/(log D log N)` for the stated nonzero fixed profiles; a power-small coefficient norm cannot establish (4). This does not disprove cancellation in the subsequent Hecke-family correlation.

For comparison, plain Cauchy with Liu's ordinary fourth moment and the generic Θ₆ inverse fourth moment gives at `(r*,m*)` a mixed-moment exponent `1/2 + [1/3+5r*/3]/2`. This exceeds the baseline `1+δm*` by exactly

    (10−9δ)/[9(5−2δ)] > 0.                                  (6)

For example the excess is `23/171` at σ=4/5 and about `0.1037` at θ. Using the buffered pointwise inverse bound with Liu's inverse second moment first gives an inverse fourth bound of exponent `1+δr*`; Cauchy with the ordinary fourth then merely recovers the baseline `1+δr*/2=1+δm*`. It gives no power saving for (4).
