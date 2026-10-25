# Independent internal review: the restricted inverse estimate

Reviewer: root research agent. Author: fractional_native agent. This is
an internal mathematical review, not external peer review or formal
verification of the imported analytic framework.

Reviewed mathematical file: `SHORT_INVERSE.md`, SHA256
`95c31d1af71ea7e7895eb61dbf6d1407eba1f93bf232041243a4e3498b130a9f`.
The author separately supplies `check_short_inverse.py`; its finite
checks do not replace the analytic review below.

## Verdict

Pass for the explicitly restricted, source-dependent theorem. The paper
does not yield a new zero-free half-plane or a new local excluded zero
sector, and it correctly proves why its particular density feedback
cannot do so. No unresolved mathematical issue was found in that scope.

## Claims examined

I read the complete note and its preceding buffered-moment input
`../second-pass/CAPPED_NATIVE_MOMENT.md`. The source inputs are the
pinned all-finite-order cap, Xu--Sang's polynomial-height buffered bins,
and Liu's amplitude-sensitive count with its fixed prime system. The
following restrictions are material to the review verdict:

- The amplitude and the detected inverse/plain witnesses belong to the
  same fixed presentation after the source's finite splitting. A maximum
  over different ray twists does not transfer amplitudes between them.
- The prime-supply, disjointness and mesh hypotheses remain in force.
  An arbitrary externally selected row subset does not acquire the count.
- Additional bounded-power punctures alter natural zeros, not primitive
  zeros. Their polynomial modulus cost enters the buffered logarithm
  argument; it is not silently declared conductor-independent.
- The relevant cap is for the finite-order Eisenstein family, not only
  for ordinary zeta. Nonzero angular characters are not included in this
  cap-based estimate.
- The exceptional principal presentations remain governed by the source
  decomposition. The theorem applies to the specified nonprincipal rows.

I checked the monotonicity calculation in (7) and the positive derivative
of the rational count with respect to `C`. Thus replacing an actual
amplitude `G>=g` by the threshold `g` weakens the class count in the
correct direction. The inequality `delta>=2g` follows from the source's
pointwise prime-amplitude ceiling. The floor class is avoided by the
strict threshold, rather than incorrectly receiving a high-amplitude
count.

The per-bin inverse estimate is genuinely for the coefficient
`mu_E(n) psi_u(n)`, obtained by a finite-height reciprocal contour inside
the buffered zero-free rectangle. The argument does not replace this
coefficient by a Gauss sum or by an arbitrary-coefficient operator norm.
Combining its square with the compatible row count gives precisely
`R_g(delta)+r delta`, so the maximum in (5) has the correct direction.
The old moment may also be restricted to the same nonnegative row set,
which justifies the minimum of the two upper bounds in (6).

For the rational example, `C<=1/2` and `A>=1/12` imply
`C/(A+C)<=6/7`. Dropping the nonnegative `A^2 C'` term therefore gives
the derivative lower bound `r-1-18/49`; at `r=7/5` it is `8/245>0`.
Consequently the endpoint evaluation at `delta=3/4` is a proved maximum,
not merely a sampled largest value. The displayed saving is
`4861/4651680`, and the crossing `107567/77528` lies above the range
where the derivative argument becomes valid and below `7/5`.

## The detector conclusion is also checked

The decisive feature is that the target class itself occurs in the
moment envelope. At its old crossing `t_0`,
`R_0+delta_0 t_0=e_0(t_0)`. For larger cutoffs both candidate long
counts remain at least `R_0`; for smaller cutoffs the short count is at
least `R_0`. Equality is attained at the crossing. This proves the exact
minimax identity (19) without requiring monotonicity of the entire
envelope. It also explains why repeated independent density feedback
cannot make a strict first improvement.

The actual averaged-numerator critical class has amplitude about
`0.23467`, well below the new example's threshold `0.37`. The note does
not transfer the restricted gain to this class or claim that a smaller
family cap removes it. The simultaneous-witness Holder estimate is a
convex combination of already available marginal count exponents; it
cannot improve their minimum. This conclusion is limited to that use of
the marginal estimates and does not rule out a new joint moment.

Finally, the rough-prime coefficient discussion distinguishes a bound
for one value of a Hilbert-valued polynomial from bounds for its
homogeneous components or its values on a circle. The first rough-prime
term correctly displays the cost in the particular positive convolution
transfer. It is not asserted to be a lower bound for the true arithmetic
moment. The finite-mark and full parity ranges are not conflated.

## Limits of this review

The global cap and the buffered/arithmetic source theorems are explicit
premises. This review does not certify their entire proofs. The new
restricted exponent is a useful intermediate estimate, but it supplies
neither the critical all-row inverse saving nor the missing relation
between simultaneous detector witnesses.
