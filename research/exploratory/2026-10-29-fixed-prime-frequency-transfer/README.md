# A fixed-profile prime mark and the Riemann-zeta barrier

**Status:** A conditional implication, not a proof of RH or of a marked inverse moment. It improves the scope of the [arbitrary-phase transfer](../2026-10-29-full-inverse-marked-transfer/README.md) by using one fixed smooth prime profile and a common frequency. It still requires uniformity over an interval of frequencies and does not handle one fixed phase or a row set that depends on that frequency.

Use the positive odd squarefree `d≡1 (mod 4)`, the fixed nonnegative smooth row weight V, the fixed compact-annular inverse weight W and the full quadratic relative-inverse polynomial `M_d(Y^r)` of the [Riemann quadratic growth identity](../2026-10-29-riemann-quadratic-inverse-growth/README.md). Fix `0<r<1/2` and `z>0`, put `P=Y^z`, and choose one fixed nonnegative smooth prime profile U supported in a compact positive annulus and positive on a smaller annulus. For all rows use the same real frequency t:

    Q_d(t)=P^(−1/2) Σ_(p odd prime) U(p/P) χ_d(p) p^(−it).

The quadratic zero mask at p|d is retained. Let κ≥0 and suppose that for each ε>0 a bound holds uniformly for every `0≤t≤T`, with `T=C P` and a sufficiently large fixed C,

    Σ_d V(d/Y)|M_d(Y^r) Q_d(t)|²
        ≪_(ε,r,z,V,W,U) Y^(1+κ+ε)(1+T)^A,                  (1)

where A≥0 is a fixed height-loss exponent. Then

    Θ_ζ ≤ 1/2 + (κ+A z)/(2r),                               (2)

with `Θ_ζ` the supremum of real parts of nontrivial Riemann-zeta zeros. Thus a proposed fixed-profile marked estimate already implies a zero-free region whenever its height loss and allowed width make the right side less than 1. No such bound is established here.

## Proof

The Montgomery–Vaughan mean value theorem for Dirichlet polynomials gives uniformly in d

    ∫_0^T |Q_d(t)|² dt
       = (T+O(P)) · P^(−1) Σ_p |U(p/P)|² 1_(p∤d).

Here the O(P) constant depends only on the fixed upper endpoint of U's support. Choose C large enough that the left side divided by T is at least half the diagonal. The prime number theorem supplies `≫P/log P` primes in the subannulus where U is bounded below; every `d≪Y` is divisible by at most `O_z(1)` of them. Therefore, uniformly for every row in V's support,

    (1/T)∫_0^T |Q_d(t)|²dt ≫ 1/log P.                       (3)

Multiply (3) by `V(d/Y)|M_d(Y^r)|²`, sum the nonnegative terms, and apply (1) for each t. The unmarked inverse mean is at most `Y^(1+κ+Az+ε)` times a logarithm, which is absorbed into the arbitrarily small loss. The lower/mean half of the quadratic full-inverse argument shows that a ζ zero at β yields an unmarked mean-square Ω of exponent arbitrarily close to `1+2r(β−1/2)`. Thus `2r(β−1/2)≤κ+Az`, proving (2). This implication uses the lower mean, not the quadratic large-sieve upper half of the growth identity. □

If (1) is available for the same fixed r and κ=0 for **arbitrarily small fixed z>0**, with A bounded independently of z, and the admissible frequency window always contains `[0,CP]`, then letting z→0 in (2) would imply RH. The implied constant may depend on z but not on Y or t. If the allowed height is `Y^τ`, one must have `z<τ`; a choice rule with `τ(z)≤z`, or a height exponent A(z) growing like 1/z, does not yield RH by this argument. At any fixed z and A, only the finite boundary (2) follows.

The rational-prime family matters: in a number field, distinct prime ideals may have the same norm, so their coefficients can cancel before the frequency average diagonalizes. A transfer to Eisenstein prime slots requires additional handling of the conjugate-prime fibers and their permissible fixed twists. The result also does not cover detector-selected row sets varying with t, since those weights cannot be pulled outside the integral.

**Independent review:** Families checked the Dirichlet-polynomial mean value, row-uniform prime divisor bound, exponent Az and the width/height choice order. The source quadratic mean theorem and any proposed input (1) remain separate assumptions.
