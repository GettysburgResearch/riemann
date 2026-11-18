# A directly weighted critical-line series bound

18 November 2026. The director reconstructed both vector variation proofs, inspected the complete finite certificate implementation, and replayed the centered-moment, exact symbolic, finite-through-1000 and sharper weighted-tail checks. The unconditional conclusion is

```text
0.61649875288731141829 < C2 < 2.35771,
C2 = sum_(distinct critical-line rho, both signs)
       |zeta'(rho)|^2 |2^(1-rho)-1|^2 / |rho|^2.
```

Multiple zeros contribute zero. No RH, simplicity assumption or zero separation is used for this series bound. Under RH it is the previously identified tapered-array limiting constant. The conditional quartic splice near 0.65339 is not used in this enclosure.

## The analytic improvement

First, the centered Hardy-phase main-term proof improves the earlier scalar Cauchy bound: use Euler truncation M=ceil(T/2), subtract half log M from the frequencies, and apply the weighted Montgomery–Vaughan Hilbert inequality. Local phase bounds are |theta'-half log M|<=0.67 and |theta''|<=1/T for the specified expanded intervals at T>=400. The polynomial moment, disk remainder, two-sided cubic cutoff and dyadic tail formulas were independently checked, including all rounded constants. Their tail at 400 is 83.0427344..., and with earlier interval blocks gives C2<87.66. This is retained as an intermediate validated bound, not the current best value.

For the sharper result put G(t)=Z(t)Q2(1/2+it). Its real and imaginary components vanish at every selected critical zero. Rolle points for the two components need not agree. Variation of each squared first derivative, with zero endpoint derivatives, yields sum |G'(gamma)|^2<=integral |f'||f''|<=||f'||_2||f''||_2 for f=phi G. Reflection costs two. Replacing |Q2|^2 by its maximum would lose a factor up to six and is avoided.

The product Q2*P has coefficients -1 on odd n<=M, +1 on even n<=M, and 2 on even M<n<=2M. Its squared coefficients through M therefore preserve the unweighted leading logarithmic moments. Tail even frequencies have gap at least 2/(n+2), except the first when M is odd; that one costs an additional absolute 2 in the Hilbert correction. Both independent proofs retain this exception. The sharper proof keeps the literal tail harmonic bound 2(log2+2/M) and differentiates Q2 times the original Hardy remainder on the real axis. The product-rule norms are 1+sqrt2, sqrt2 log2 and sqrt2(log2)^2. Their normalization supplies each required additional log denominator. All coefficient bounds decrease at the declared lower height, so the final infinite dyadic remainder uses a valid common coefficient.

The director read the exact formulas in the independent note and replayed its Arb script: the complete analytic tail beyond 10000 is less than 1.741202. The finite certificate at 160 bits has complete positive count 10142 and partial in (0.61649875288731141829,0.61649875288731141830). Adding the upper endpoint gives the stated strict 2.35771 bound. The director independently replayed all shared partial heights at 192 bits. The other reviewer replayed the full 160-bit 10000 run byte for byte. The FLINT all-zero multiplicity count is a different routine from its critical-line zero isolation; the script exhausts the former with disjoint simple critical zeros. Thus this finite census is unconditional, rather than an assumption that an isolated list contains all zeros.

## Asymptotic control and limits

For a fixed relative block length eta and fixed outer margin delta, only the leading diagonal length changes to eta+2delta. All cutoff and Hilbert corrections are lower order at large height. Sum blocks in ratio 1+eta, take Y to infinity first, then delta to zero and eta to zero. This proves the unconditional bound limsup Y*tail(Y)/log^4Y<=2/sqrt960=1/(4sqrt15). The order of these limits is explicit. The RH-conditional exact coefficient 1/(12pi) is smaller and consistent.

A one-percent series enclosure would follow, for example, from a complete derivative-sum certificate through 10^7 of width below 0.00025, using the independently checked tail below 0.005901712. That larger census was not run. New global weighted-cutoff optimizations remain candidates until separately reviewed. These analytic coefficient tails must not be substituted for the near-function tail in the finite-length prime-array remainder, which is a different estimate.

[Centered proof](prime64_main_term_moments.md) · [First vector proof](prime65_q2_vector_rolle.md) · [Independent sharper proof](positivity65_q2_weighted_rolle_skeptic.md) · [Finite certificates](prime64_q2_partial_tail_observation.md) · [Director replay](../../experiments/results/director65_weighted_rolle_checks.json)
