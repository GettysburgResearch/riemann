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
