# Arithmetic cancellation versus graph coercivity

Status: proposed component proofs and bounded exact checks; independent review required.
**RH is not proved. No fixed-power or subpower residual bound is proved.**

This is a synthesis-led research continuation of #803 after reading the newer
prime-power divisor work and the post-integration review. It keeps the actual
Möbius prefix and the original physical residual metric.

## New results

1. **An explicit centered, two-jet completion.** At every integer Y>=2, a
   prescribed three-block polynomial has the exact Möbius prefix, p(1)=0,
   p'(1)=1, p(0)=-2, support below 8Y, coefficients bounded by 84, and
   coefficient norm S<1924+log Y. This is not a bound on its physical energy.
2. **A native unconditional energy improvement.** Classical Mertens estimates
   and a complete frequency calculation give E(p_Y^c)=O(Y exp(-c Phi(log Y))),
   Phi(v)=v^(3/5)(log v)^(-1/5). Thus E=o(Y), and any fixed logarithmic saving
   from Y holds. This is an application of classical estimates, not a new
   Mertens bound, a fixed power saving, or an RH completion. Constants are not
   numerically certified. The same bound applies to the old two-endpoint family.
3. **A sharp missing norm adapter.** On balanced fixed-ratio tail blocks,
   graph-to-physical norm comparison costs order Y/log Y. This remains true
   after preserving both safe jets and centering. The explicit variation
   Q_Y(s)(1-2^(1-s))^2(1-2^(-s)) has R>=Y/24 but G=O(log Y).
   For ANY fixed number of the indicated jets, an analogous family exists.
4. **A full analytic limit for the explicit variation.** R/Y tends to a
   positive constant C_*, independently enclosed in
   [1.704219450036,1.704219498544]. All 4095 rational integral cells through
   4096 and the complete tail are accounted for. It is not a native-zeta
   error norm or a newly optimized minimum.

## Why the proposed closure stops

The divisor gaps control their own prime-power form. They do not provide a
subpower comparison with the physical residual. The new centered completion
and its plus/minus variations all preserve the actual prefix, both jets,
centering and logarithmic coefficient energy. At least one varied completion
has physical energy Omega(Y), while its graph energy is only O(log^2 Y).
This does not refute a special estimate for a chosen native minimizer.

The native stretched-exponential saving remains Y^(1-o(1)); the hypothetical-
zero lower bound requires an upper bound Y^o(1) on an unbounded sequence.
No such bound, sparse-sign saving, or unbounded Weil positivity is supplied.
Do not submit the packet as a claimed complete RH proof.

## Read and replay

Read PROOF.md, then SYNTHESIS.md for source-by-source distinctions and the
remaining full-proof obligation. SOURCES.json records exact repository heads,
file objects and the scoped reading depth. It is not an exhaustive integration
census or a source-code audit of those branches.

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py --part 1
    python -I -S -B test_rejections.py --part 2

Add --optimized to the last two commands for optimized subprocess checks.
See VALIDATION.md for actual executions and their limits. General Hardy,
Poincare, convolution and asymptotic ingredients are credited; no external
novelty or independent referee acceptance is claimed.
