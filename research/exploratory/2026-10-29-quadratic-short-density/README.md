# A detector density bound for positive quadratic Dirichlet characters

**Status:** A proposed derivation from the classical quadratic large sieve and standard Dirichlet L-function analytic facts, using the source detector proof replay described below. It is weaker than the known quadratic-family zero-density theorem cited at the end and does not improve the literature. This is a family zero-density estimate, not an individual zero-free region. The detector replay requires independent verification; no novelty claim is made.

Let d range over positive odd squarefree integers with d≡1 mod4, and let χ_d be the primitive quadratic Dirichlet character of conductor d. Write `N_d(σ,T)` for the number of zeros of `L(s,χ_d)`, counted with multiplicity, in `Re s≥σ`, `|Im s|≤T`. Put δ=2σ−1. The proposed estimate is: for every fixed `1/2<σ<1` and ε>0 there is τ>0 such that

    Σ_{d≤X, d sf, d≡1 (4)} N_d(σ,X^τ)
       ≪_{σ,ε} X^{1−δ/2−δ²/2+ε}.                             (1)

The d=1 principal character is separately harmless. The exponent is strictly below 1; since this family has `(2/π²+o(1))X` members, all but a power-saving fraction have no zero in the displayed rectangle. At σ=4/5 the exponent is `13/25`. The same bound holds for dyadic d≈X; applying the same dyadic proof at global upper base X and summing logarithmically many boxes gives the displayed cumulative form. The zero-free rectangles have height X^τ and need not hold for every individual character.

## Classical arithmetic moments

For odd squarefree columns b and odd squarefree rows d, [Heath-Brown's quadratic large sieve, Theorem 1](https://doi.org/10.4064/aa-72-3-235-275), states

    Σ_{d≤CX, d odd sf} |Σ_{b≤CQ, b odd sf} λ_b (b/d)|²
       ≪_ε (XQ)^ε (X+Q) Σ_b|λ_b|².                           (2)

For d≡1 mod4, quadratic reciprocity gives `(b/d)=(d/b)=χ_d(b)`, including the common zero when (b,d)>1. Hence a normalized smooth inverse block of length Q=X^r, including any common norm twist and its finitely many parameter derivatives, has squared coefficient mass O(1) and satisfies

    Σ_{d≤X} |M_r(d)|² ≪ X^{max(1,r)+ε}.                        (3)

Here and below sums are over the indicated d family and X-powers absorb bounded endpoint constants.

For a normalized plain block of length N=X^m, write each odd column uniquely as n=qv² with q squarefree. No coprimality between q and v is imposed. Multiplicativity with original zeros gives χ_d(n)=χ_d(q)χ_d(v²), and the outer factor has modulus at most one. For fixed v, the squarefree q coefficient vector has squared mass `≪v^(−2)` and length `≪N/v²`. Apply (2), then Minkowski and `Σ_{v≪√N}1/v≪log(2N)`. For `m≤1/2+η` this yields

    Σ_{d≤X} |S_m(d)|² ≪ X^{1+O(η)+ε}.                          (4)

A common smooth annular profile with row-dependent zero real part and norm-twist height is handled via the [finite-dimensional Sobolev lemma](../2026-10-29-detector-profile-sobolev/README.md): after grouping dyads, each fixed parameter and its first/mixed derivatives give one coefficient vector shared by all d. Derivatives insert bounded powers of log on the annulus, and integrating over height `O(X^τ)` costs a fixed polynomial in X^τ. The qv² decomposition and χ_d(v²) multiplier are unchanged by this reduction.

## Detector replay over Q

Remove d=1 and fix a floor `1/2<σ_f<σ`. Each χ_d has even fixed archimedean type, conductor at most X and entire primitive L-function. Work with the odd Euler product `L_odd(s,χ_d)=(1−χ_d(2)2^(−s))L(s,χ_d)`; the deleted factor is nonzero for Re s>0. Standard Dirichlet L continuation, Euler products, the functional equation, fixed-type strip growth and individual zero count provide the Q-version of [the fixed-field proof packet](../2026-10-29-cubic-short-detector-proof/README.md). The same argument applies with Γ_R rather than Γ_C and a fixed deleted factor at 2:

* For each d, nested maxima over χ_d and its conjugate at heights up to fixed multiples of X^τ give a bin endpoint a≥σ−e and a buffered zero-free rectangle. Borel–Carathéodory and three-circles control L_odd and its reciprocal there by X^η. The functional equation and that buffer give the reflected bound with conductor factor at most `X^(a−1/2+O(e))` and a fixed polynomial in X^τ.
* For bounded dyadic lengths `D=X^r`, `N=X^m`, partial Mellin shifts, with all Fourier frequencies sharing one height allowance, give `|M_r|²≪X^{(2a−1)r+η}` and `|S_m|²≪X^{(2a−1)min(m,1−m)+η}`. Absolute-line tails are removed with external smoothness orders selected after τ.
* For fixed `t∈[1,3/2]`, a Möbius inverse cutoff `D*=X^t` and a Gamma integral at a selected zero give, after cancellation of all nonunit coefficients through D* and dyadic/Fourier separation, two witnesses using the same character and common frequency:

      r≤t+o(1),  m≤1/2+O(η),  r+m≥t−o(1),
      |M_r|²≥X^{(2a−1)r−η},  |S_m|²≥X^{(2a−1)m−η}.          (5)

  Here e,η>0 are fixed preliminary losses, and τ is chosen afterward so all fixed polynomial height costs are smaller than the final ε. The whole real-line detector replay, including the single frequency budget and differentiated profiles, is a source-qualified proof obligation; it is not an assumption of an all-height zero-free boundary.

## The detector minimax

Let δ₀=2σ−1 and choose the fixed cutoff `t=1+δ₀/2∈[1,3/2]`. Group the finitely many bins and logarithmically many dyadic choices. A zero with real part at least σ gives a≥σ−e, so replacing 2a−1 by δ₀ costs O(e+η). By (3)–(5) and Chebyshev the row count is controlled by the smaller of

    max(1,r)−δ₀r,    1−δ₀m.

Because `r∈[t−1/2,t]`, `m≥t−r` and `m≤1/2`, for r≤1 this minimum is at most `1−δ₀(t−1/2)`; for r≥1 it is at most `(1−δ₀)t`. Their maximum is

    max{1−δ₀(t−1/2),(1−δ₀)t}
       =1−δ₀/2−δ₀²/2.

The two values are equal by the chosen t. Small range overflows cost O(e+η), and the finite bins, logarithmic dyads, Sobolev height factor, and standard individual zero count `O((X^τ+1)log X)` fit into ε after the preliminary losses and τ are fixed in that order. This yields (1), contingent only on the verified source detector replay and the cited classical inputs. □

## Comparison with a stronger known theorem

[Corrigan–Zhao, Theorem 1.4](https://arxiv.org/abs/2211.00260), state for all primitive quadratic characters of conductor at most Q an estimate of the form

    (QT)^ε min{(Q³T⁴)^[(1−σ)/(2−σ)],
                (QT)^[3(1−σ)/σ]}.

Their family contains every χ_d counted above. At fixed height the first branch has exponent `3(1−σ)/(2−σ)`, strictly below our `(1−σ)(2σ+1)` for every `1/2<σ<1`, since their difference is

    (1−σ)²(2σ−1)/(2−σ)>0.

For a sufficiently small fixed power height T=X^τ, the gap remains after including the displayed T-power and small losses. At σ=4/5 the known Q exponent is 1/2, compared with 13/25 here. Thus (1) does not provide a literature improvement; it only checks the classical quadratic sieve and the saturated-detector minimax in this family.
