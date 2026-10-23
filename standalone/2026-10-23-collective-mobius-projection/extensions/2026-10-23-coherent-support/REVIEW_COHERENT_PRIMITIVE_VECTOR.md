# Review of the assembled coherent primitive vector proof

23 October 2026. Reviewed `../two-hour-boundary-20261023/COHERENT_PRIMITIVE_REMAINDER_VECTOR.md`, final SHA256 `bb321aae05c906187371ea7cd7a01062b19f0c0a2d889b3106c4d6e48eaaeca4`.

This receipt distinguishes authorship from review. I co-derived the ordinary n-prime weights, the common-character identity, the exceptional fifth-power repair and the Euler-denominator closure. I then checked the final written assembly against PR1015's complete local decomposition, the frozen full-vector bounds and the actual projection normalization. This is not an independent second derivation of those co-derived ingredients.

The prior draft `b1177120db3bfb57efdc1a3a7f2631df497829eebcfbebb436fa4bdf8be3aaa7` was **not** accepted: extracting shared fifth-power label primes left a row-dependent coprimality restriction. The final version explicitly repairs that restriction by finite inclusion-exclusion, retaining an unreduced full numerator multiplier `E^6`.

The final interfaces check as follows.

1. The selected local multiplier acts on the whole free product `m R0`. Consequently the two characters use the same actual row `r=c0(ed0)^2 t_out S^6`. The R0 sieve is applied for each frozen selected part before aggregating its restricted inverse-row norms. Divisor-many representations suffice; a unique representation is not asserted. Replacing each restricted norm by the full norm before aggregation would lose the gain and is explicitly avoided.
2. The ordinary n-prime table retains `X=D/(G e f d0 v0)` and the PR1015 weights. The balanced term has weakest exponent `d0^-7/6`; a v0-only prime also lies in k_m. The completed plateau has weights `e^-5/4 f^-23/12 d0^-5/4 v0^-11/12 k_m^-1`, or the weaker but still summable `f^-17/12` if its sixth power remains in the row. These exponents agree with the full local formula, rather than only the squarefree toy case.
3. Ordinary selected-label plateau exponents are exactly `-(10 epsilon+5+6a)/12` outside the modulus and `-(11 epsilon+6+7a)/12` inside it. Their squared weights converge after divisor Cauchy. The balanced term inside the modulus has squared decay at least `S^-3/2`; the outside part uses the restricted-row aggregation just described.
4. In the exceptional fifth-power branch, the exact re-encoding is `R=G^5 E^5 R2`, `n=GEz`, with full numerator `E^6 z R2`. The only remaining puncture in the free coefficient is the fixed `GE`; the remaining label may share primes with z. The full local modulus branches `0,6,7` have ratios `1,1-q^-1,q^-1/2` and preserve the common-character form. The squared balanced weights `G^-7/3 E^-11/6` (or stronger) and all displayed plateau weights are summable. No full continuous-series sixth-power periodicity is used.
5. The row-label denominator is independent of the free n coefficient and is restored only after the numerator family is bounded. Weighted Cauchy and the all-scale extension justify the entire ideal sum, including subunit scales. Smaller internal epsilon handles the scaled norm losses.
6. The retained scalar volume uses the same physical cutoff as the coherent calculation. Its total is `KU`. The partial poles retain their exact local phase collapse and are bounded by the already proved scalar estimates; their sum is `D^(5/6)K^(7/6)+D^(1/2)K^(3/2)`, with the latter subordinate for `K<=D`.
7. The small-scale finite-minus-pole identity and the sixth-free residue-vector estimate justify the stated all-scale use. The whole pole is restored once, in the actual projection consumer, and the PR1013 half-range Gram hypothesis remains explicit.

No further issue was found in the final assembly. At `U=D^(6/7)`, `K=D^(1/12)`, the four projection exponents are exactly `79/84,133/144,67/72,20/21`; the largest is `20/21`. The gain relative to `41/42` is `1/42`.

The conclusion concerns the specified Gauss-vector **projection**. It does not estimate its orthogonal complement, prove a smaller fixed zero-free boundary, or prove RH. The later attempt to improve the volume term is not part of this reviewed file.
