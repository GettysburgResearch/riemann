# Independent complete native heat-point review

Status: full analytic/source/code ACCEPT, and independent native normal and
optimized replay PASS with byte-identical owner receipts.
Scope: complete actual-Xi heat trace at exactly `u=1/64`, derivative order
zero. One strict inequality; no all-time or higher-derivative coverage.
Exact sources: [NATIVE_HEAT_POINT_V2.md](../NATIVE_HEAT_POINT_V2.md), SHA256
`7834f3510f252f1ea75c3e63a244af0679fcdb2be5e99fe107813ce2153306e2`;
[check_native_heat_point_v2.py](../check_native_heat_point_v2.py), SHA256
`ff2502372b3c6e79d68a1477daa111162ff6bc2d3ed5d00347cb1a71f8e08ac7`;
and [COMPLETE_PRIME_HEAT_TRACE.md](../COMPLETE_PRIME_HEAT_TRACE.md), SHA256
`d48987c9143620d6b433163c080a89f3bc4966764d0880a83666a671fda3fb29`.
The complete infinite formula is separately accepted in
[ARCHIMEDEAN_HEAT_SOURCE_REVIEW.md](ARCHIMEDEAN_HEAT_SOURCE_REVIEW.md).
What was actually run: the frozen native checker, normal and optimized,
with separate outputs under `/tmp`, followed by byte equality and source
authentication. Both completed successfully in less than one second.
Smallest remaining gap: signs at every positive heat time and every
derivative order, or a separate strict negative derivative certificate.

## Complete analytic and code gate

At the fixed heat time the exact Gamma integrand is
`(exp(-q)-exp(-q/4-4q^2))/(1-exp(-q))`. Writing
`h=q*(3/4-4q)` and `H(z)=expm1(z)/z` gives exactly
`-exp(-q)*(3/4-4q)*H(h)/H(-q)`. The value at zero is `-3/4`.
The hypergeometric representation `H=1F1(1;2;z)` is entire and regularizes
the removable zero. Its denominator detects the remaining nonreal poles.

Where the argument ball has real part greater than `1/4`, the code uses
`exp(-q)*expm1(h)/expm1(-q)`, which is algebraically the same meromorphic
function. The two evaluation formulas have no analytic branch discrepancy.
Near zero the entire regularization is retained. Ball division and the
finite-integral gate enforce the native holomorphy/enclosure contract;
uncertainty or a pole intersection does not produce an accepted finite
integral by an unchecked decimal evaluation.

The four certified integration segments partition `[0,100]` exactly. Every
returned complex enclosure must be finite and contain zero in its imaginary
projection. All real intervals are summed. For the remaining q range,
`1-exp(-q)>1/2`, and
`integral_(100)^infinity |I(q)|dq<=2 exp(-100)+8 exp(-25-40000)`.
The checker adds the complete symmetric tail radius, not a zero remainder.
Euler's constant, pi, exponentials and the prefactor are also native balls.

Integer trial division authenticates all 18 primes through 64 and repeated
integer multiplication all 27 prime powers. Every power uses its literal
von Mangoldt weight `log p`. The omitted prime CONTRIBUTION TO K is bounded
by `2 sqrt(u)/sqrt(pi)*exp(-log^2(64)/(8u))`, as obtained from the complete
HT12 derivative-zero bound. The exact domain checks `log64>2` and
`log64>4u` satisfy that bound's hypotheses. The remainder enters K with a
minus sign; the checker subtracts the entire interval `[0,tail_upper]`.

The final strict predicate is applied to the full K ball after the complete
Gamma and prime tails, all 27 literal finite terms and native uncertainties.
The source contains no assertions whose removal would weaken optimized
acceptance. It calls no root-list, root-count or logarithmic-jet routine.
The backend and finite integration budgets are fixed explicitly. The
primitive directed integration uses python-flint 0.9.0 / FLINT 3.6.0 at
320 bits; this same-backend replay is not a distinct integration library.

## Independent executed receipts

The independent outputs are retained here as
[native_heat_point_normal.json](native_heat_point_normal.json) and
[native_heat_point_optimized.json](native_heat_point_optimized.json).
Both are byte-identical to the owner's `native_heat_point_v2.json`, with
SHA256 `89bec61baaa916c846575922661442b7d8432dc838c216e98782d9b7b55a87fe`.
Every direct proof/checker source hash matches the currently frozen bytes.
The complete positive interval has midpoint approximately
`0.04514116080116654`, width approximately `1.6790938029784357e-43`, and a
strictly positive exact rational lower endpoint. Its full rational endpoints,
each native integral segment and every finite prime term are in the receipt.

The older all-hypergeometric attempt exhausted its finite time budget and
has no accepted receipt. This review binds version two only. The accepted
result is one literal complete-source inequality, `K(1/64)>0`; it supplies
neither the universal complete-monotonicity signs nor RH or its refutation.
