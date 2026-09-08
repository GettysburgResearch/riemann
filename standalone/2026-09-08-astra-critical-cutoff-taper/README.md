# Critical cutoff taper and the finite-energy boundary

**No RH completion is claimed.** This packet supplies an endpoint-safe causal
taper, a conditional exact-critical-line convergence theorem, and a direct
finite-energy-to-RH argument. The arithmetic energy bound remains unproved.
All results are author-proposed components awaiting independent review.

Parent: PR811 at `946dedfa3f6ec2d74f3f0f00f9ca511abf9652d7`.
All predecessor files, main, review records, and formal sources are unchanged.

Start with [PROOF.md](PROOF.md), then [ATTEMPT.md](ATTEMPT.md).

For the literal weighted prime discrepancy

    R(x)=sum_(p<=x)sqrt(p)-integral_2^x sqrt(u)/log u du,
    J=integral_2^infinity R(x)^2/x^3 dx,

this packet proves `RH <=> J<infinity`. The reverse implication constructs an
analytic logarithm; the forward implication explicitly imports the classical
RH-conditional Cramer mean-square theorem. It is not an unconditional bound.

Replace the sharp logarithmic cutoff by its fixed width-one average,
`Cbar_X=integral_0^1 C_(X exp u)du`. It preserves the exact source horizon.
If J is finite, its complete norm error is at most

    ||Cbar_X-C_infinity||^2 <=6 integral_(log X)^infinity |v(t)|^2dt,
    v(t)=exp(-t)R(exp t).

On RH that right side is O(1/log X). Taking the GEOMETRIC average of the
same forward Euler completions produces outer finite approximants whose
complete complex logarithms converge in weighted L2 with norm error
O(1/sqrt(log X)). Their entropies converge as well. No convergence of the exponentials in L2 is claimed.

This is sharper conditional endpoint control than the old growing norm bound,
not a new estimate proving RH. In particular the Cramer input cannot be used
as an unconditional final lemma. ATTEMPT.md identifies that failed inference.

The bounded checker reconstructs finite physical Grams and entire stopped
futures with rational arithmetic. It does not machine-prove CM, the analytic
limits, or an all-cutoff prime discrepancy estimate. See VALIDATION.md.
