# Independent arithmetic-lane review of the heat-trace argument

Reviewed file: `swarm/heat_trace/report.md`, as read on 30 October 2026, with threshold t₀=10⁻⁶ and endpoint floor(U²/(8·10⁶)).

**Verdict: the displayed theorem follows from its three stated inputs. No blocking mathematical error found.** This review checks the derivation; it does not independently certify the external finite-height computation or the provenance of the stated counting bound. It also does not certify global novelty.

## Definition and quantifiers

The coordinate λ=(γ−iδ)² is correct for the xi zero corresponding to ρ=1/2+δ+iγ. Functional-equation symmetry pairs δ with −δ at fixed positive γ, so the complete upper-zero sum is real. Multiplicity is retained. The counting law and Gaussian factor justify local absolute convergence and termwise differentiation at each fixed derivative order and positive time. No uniform-in-order differentiation interchange is needed.

The theorem's very large finite endpoint is not an all-order statement. Complete monotonicity on a short time interval does not alone imply complete monotonicity on the whole positive axis; even 1−t is locally completely monotone on (0,1). Thus there is no hidden automatic RH conclusion from the small-time lemma.

## Low-order argument

- Both bt and nφ have the same sign; when their magnitudes are at most π/2 their difference has magnitude at most π/2. Since n|φ|≤n/γ≤2/5, a negative real contribution requires |b|t>π/2. The bound |b|≤γ gives the stated necessary inequality t>π/(2γ).
- With η∈(U/4,U/3], a−q≥(7/8)γ² and r/q≤16(γ²+1/4)/U² hold for the stated U. The first inequality has a positive margin: 8/9−7/8=1/72, larger than 1/(4U²).
- The logarithmic derivative of γ²(r/q)ⁿe^(−7πγ/16) is at most 2(n+1)/γ−7π/16<0 throughout γ≥U and n≤2U/5.
- The final exponent uses 3·(2U/5)−21U/16=−9U/80 correctly. U²exp(−9U/80)<1 for U≥1000.

This covers all n<400 under the final theorem's U≥10⁶ assumption.

## Small-time, all-order argument

The central cancellation of phase is correct:

ψ=2u(y−n/y)+2n(u/y−arctan(u/y)).

On |y−√n|≤10 and n≥400, y≥√n/2 and |(y+√n)/y|≤3. This gives the displayed 6|u||y−√n| term. The cubic remainder is negligible under |u|≤1/2000. The phase is strictly below 1/2 in magnitude, so the whole broad interval contributes nonnegatively.

For y=√n(1+z), |y−√n|≤1/2 implies 3nz²≤3/4. The logarithm estimate yields y^(2n)e^(−y²)≥e^(−3/4)nⁿe^(−n). The complex modulus is at least this real-axis modulus. The claimed 1/8 factor is conservative.

For the central count, A≥39X/40 and A/(2π)>X/7 give M(B)−M(A)≥L log X/(4π)>L log X/13. The two error terms are bounded by (1/4)log(2X)+8<2log X. The final inequality L/13−2≥L/20 holds already when L≥520/7, well inside L≥1000.

The Gaussian-envelope inequality is exact: after setting v=√(y²+u²), it reduces to log(v/√n)≤v/√n−1. Since |v−y|≤|u|<1, every k-th shell is bounded by 2Pₙe^(−(k−1)²).

The short-interval zero count follows from the supplied global count even for an interval whose lower endpoint is zero: M is continuous there and its derivative is integrable. One may make the shell logarithm step explicit as follows: the upper endpoint satisfies b+2≤X(k+2), and k+2≤Xᵏ for X≥20000, k≥10; hence log(b+2)≤(k+1)log X. The displayed shell count follows.

Finally,

Σ_{k≥10}(k+1)e^(−(k−1)²)≤2⁻⁷¹Σ_{k≥10}(k+1)2⁻ᵏ=3/2⁷⁸.

Thus the negative tail is far smaller than half the positive central lower bound. This controls the entire infinite tail and uses no RH input.

## Large-time argument and coverage

The bound log(17x)≤3x follows from log17<3 and log x≤x−1. Combining n≤t₀U²/8 with t≥t₀ yields the stated exponent −t₀γ²/2. The function γ²exp(−t₀γ²/2) is decreasing once γ²≥2/t₀, satisfied by U≥10⁶. The reciprocal-square tail then gives a total relative tail less than 1.

There is no gap between cases: n<400 is covered for all times; n≥400 is covered for 0<t≤t₀; every allowed n is covered for t≥t₀. The endpoint arithmetic at U=3·10¹² is correct: U²/(8·10⁶)=1.125·10¹⁸.

## Optional strengthening with the same proof

The constants actually support t₀=10⁻⁴ without changing the argument's structure:

- L≥100, |u|≤1/200 and X≥2000.
- The broad-interval phase is at most 0.30000004<1/2.
- The central counting error remains <2log X, and L/13−2≥L/20 still holds.
- The shell count remains valid for L≥100; the same tail series bound applies.
- The large-time estimate has the stronger exponential decay and permits n≤U²/80000.

At U=3·10¹² this would give endpoint 112,500,000,000,000,000,000 = 1.125·10²⁰. This improvement is optional; the originally stated theorem already passes review. If adopted, update every threshold consistently and bind the final reviewed file hash.

## Remaining limitation

No step proves the signs for arbitrarily high orders at times bounded away from zero. The moment-kernel peak has width about t⁻¹/² in ordinate, and the small-time proof benefits from that broad averaging. It should not be described as all-order Hankel positivity, a new individual zero-free region, or an RH proof.
