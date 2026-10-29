# Mixed inverse/plain moment and its scalar limitation

**Status:** Source-conditional calculation. The moment below imports the [rectangular squarefree-column sieve](../2026-10-29-conjugate-conductor-sieve/README.md), and its application to row-varying detector witnesses requires the common-profile Sobolev and fixed-field detector inputs of the [short-detector note](../2026-10-29-short-cubic-conductor-detector/README.md). It does not give a new density exponent by itself and is not an individual zero-free region.

For the conductor-ordered cubic family, or the restricted fixed-order family `g=a b^(n−1)` under the general-n sieve replay, take centrally normalized inverse and plain polynomials M_r and S_m with common row character and lengths D=X^r and L=X^m. For bounded nonnegative r,m and fixed common smooth annular profiles, the source sieve gives

    Σ_g |M_r(g) S_m(g)|² ≪ X^ε (X+X^(1/2+r+m)).                   (1)

The sum is over the conductor-ordered family, retaining the original noncoprime zero masks. The bound also holds with finitely many fixed differentiated profiles and the usual fixed polynomial height cost. To see this, multiply the two sums and use the exact multiplicativity of the original zero-extended character. The product is a polynomial in h, supported on `Nh≍DL`, with coefficients `λ_h` satisfying

    |λ_h| ≪ τ_K(h)/(DL)^(1/2),

where τ_K is the ideal divisor function. For each h write h=qv² with q squarefree. Fix v; the factor χ_g(v²) is outside the q-sum and has modulus at most one. The squared mass of the q-coefficients is `≪X^ε/(Nv)²` by the ideal count and a divisor bound, since `Nq≪DL/(Nv)²`. Partition q into logarithmically many dyadic ranges and apply the squarefree-column bound at length Q≪DL/(Nv)². Minkowski over v gives a row L² norm at most

    X^ε Σ_{Nv≪sqrt(DL)} (Nv)^(−1)
       [X+X^(1/2)DL/(Nv)²]^(1/2)
      ≪ X^ε [X^(1/2)+X^(1/4)(DL)^(1/2)],

because Σ_(Nv≤Y)(Nv)^−1≪log(2Y) and Σ_v(Nv)^−2 converges. Squaring proves (1). Fixed ray-class reciprocity phases, ν and all zero masks are as in the cited sieve note. A fixed bounded tuple of profile/real-part/frequency parameters is handled by differentiated coefficient vectors and Sobolev as in the cited detector note; the factor χ_g(v²) can be dropped at each parameter value before taking the supremum. The exact detector uses one selected character and its simultaneous witnesses; arbitrary two-witness applications would additionally need a common presentation and profile uniformity.

## Exact minimax

Suppose simultaneous saturation gives `r≤t`, `m≤1/2`, `r+m≥t`, and `|M_r|²≥X^{δr−o(1)}`, `|S_m|²≥X^{δm−o(1)}`, with fixed 0<δ<1. Dropping small preliminary losses, the two individual moments and (1) give the minimum of

    I(r) = max(1,1/2+r) − δr,
    P(m) = 1 − δm,
    J(r,m) = max(1,1/2+r+m) − δ(r+m).                               (2)

Let `t₀=1/(2−δ)` and `R=1−δ/[2(2−δ)]`. Over all t>0, with r,m≥0 and the constraints above,

    inf_t sup_(r,m) min{I(r),P(m),J(r,m)} = R.                       (3)

For `t₀/2≤t≤t₀`, the feasible point `r=m=t₀/2` gives `I=P=J=R`: here r≤1/2 and r+m=t₀≥1/2. For `0<t<t₀/2`, take r=t,m=0; then I=J=1−δt>R and P=1. For t≥t₀, take r=t,m=0; then I=J=1/2+(1−δ)t≥R and P=1, so the minimum is at least R. These cases establish the lower bound on the minimax. The upper bound is attained at t=t₀ using only I and P, by the two-branch optimization in the cited short-detector note. Thus even the exact additional mixed moment (1) leaves its exponent unchanged. The lower-bound witnesses are feasible points in the scalar relaxation, not constructions of actual Hecke rows.

This also explains why a product estimate solely of the form (1) cannot overcome the balanced bottleneck: at r=m=t₀/2 its exponent equals both individual-moment exponents. A sharper estimate would have to exploit structure beyond arbitrary convolution coefficients, supply an independent constraint excluding those simultaneous witness lengths, or prove a genuinely stronger joint moment. No conclusion is drawn about such stronger inputs.
