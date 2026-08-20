# Parabolic Vaughan correction and composite-owner frontier

Date: 2026-08-21
Branch base: PR #691 head `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`
Scientific status: **RH unproved**

This packet records four conclusions.

1. The positive compact cubic B-spline construction is exact, but its half-order moment is strictly positive. It therefore does not inherit the zero-moment Type-I decay of `L-100310`.
2. The balanced Vaughan remainder admits an exact large-divisor Hankel form. With `U=floor(X^(1/3))`, its outer divisor pair is asymptotically parabolic: after ordering, `e<d^2`.
3. On squarefree support, writing `d=ga`, `e=gb`, `(a,b)=1`, removes the gcd sign exactly: `mu(ga)mu(gb)=mu(a)mu(b)`. The cutoff remains coupled, so no fictitious independent SCGR/PCWD split is claimed.
4. The live prime-interval result is `L-100615`, not the weaker exponent-two corollary: every `q<=p^A`, `A<exp(3/4)`, is eventually positive.

The corrected implication matrix keeps the signed zero-moment kernel for Vaughan/Type-I and the positive B-spline only as an independent structural compact probe. The sole terminal arithmetic task remains the composite-owner lifting / large-divisor Hankel negative-mass estimate `CPL102000`, which is exactly the balanced Vaughan gate in a more localized coordinate system.

No proof of `CPL102000` or RH is claimed.