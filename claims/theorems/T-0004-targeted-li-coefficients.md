```text
Claim ID:       T-0004
Title:          Targeted Li coefficients, and their collapse at n = 1 to a
                one-point Herglotz test
Status:         PROVED (the algebra and the identity) / EMPIRICAL (the values)
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   T-0003 (classical Li), L-0006 (certified Taylor model of eta),
                L-0001
Scope:          lambda_n^(alpha) for n <= 16 at twelve centres alpha; the
                identity at n = 1 is exact and unconditional
Answers:        Q-0012
Related counterexample candidates: Z-0006
```

## Statement

**Part 1 (the family).**  The classical Li coefficients use the Mobius map
`s = 1/(1-z)`, which carries the unit disc onto `Re s > 1/2` with `z = 0` at
`s = 1`.  That choice of base point is arbitrary.  For any `alpha` with
`Re alpha > 1/2`, writing `a = alpha - 1/2`, the map

```
    s  =  1/2 + (a + conj(a) z)/(1 - z) ,          z = phi_alpha(s)
```

is also a bijection of the unit disc onto `Re s > 1/2`, now with `z = 0` at
`s = alpha`.  Its inverse is

```
    phi_alpha(s)  =  (w - a)/(w + conj(a)) ,       w = s - 1/2 .
```

Defining

```
    log xi(s(z))  =  log xi(alpha) + sum_{n>=1} (lambda_n^(alpha)/n) z^n
```

gives, for each admissible `alpha`, a criterion equivalent to RH:

```
    lambda_n^(alpha) >= 0  for all n >= 1     <==>     every zero has Re rho >= 1/2.
```

`alpha = 1` recovers the classical coefficients.

**Part 2 (the amplification law).**  A zero at `rho = 1/2 - delta + i gamma`
is carried to a point of modulus

```
    |phi_alpha(rho)|  =  sqrt( (u+delta)^2 + (gamma-v)^2 )
                       / sqrt( (u-delta)^2 + (gamma-v)^2 ) ,
                                                   alpha = 1/2 + u + i v ,
```

and it contributes `-|phi|^n` (times a bounded phase) to `lambda_n^(alpha)`.
For the classical choice `(u,v) = (1/2,0)` this modulus is `1 + O(delta/gamma^2)`
-- which is precisely why the classical criterion needs `n ~ gamma^2/delta`
before an off-critical zero becomes visible.  Aimed at the zero (`v = gamma`)
the modulus is `(u+delta)/|u-delta|`, which is **unbounded** as `u -> delta`.

**Part 3 (the collapse at n = 1).**  Because `z = 0` sits at `s = alpha` and
`ds/dz|_{z=0} = 2u`,

```
    lambda_1^(alpha)  =  2u * Re( xi'(alpha) / xi(alpha) ) .            (*)
```

So the first targeted Li coefficient is not a series computation at all: it is
**two point evaluations**.  Combining (*) with Part 1 at `n = 1` gives a
statement that needs no Taylor expansion anywhere:

```
    RH   <==>   Re( xi'/xi )(s) >= 0  for every s with Re s > 1/2,
```

i.e. RH is exactly the assertion that `xi'/xi` is a Herglotz (Nevanlinna)
function of the half-plane `Re s > 1/2`.

## Why this is the answer to Q-0012

Q-0012 asked whether there is a criterion whose witness is small *for a zero
that is only slightly off the line*.  Every criterion previously in this
repository answers "no" in the same way: the classical `lambda_n` needs
`n ~ gamma^2/delta`; the Weil quadratic form needs a test function of bandwidth
`~ 1/delta` and hence `~ exp(c/delta)` prime powers (X-0006); the winding number
needs a contour that separates `1/2 - delta` from `1/2`.  T-0004 breaks that for
the *verification* step: given a candidate `(gamma, delta)`, choosing
`alpha = 1/2 + u + i gamma` with `u` comparable to `delta` produces a negative
coefficient at `n = 2` -- or, via (*), at `n = 1`.

Measured on a synthetic zero set with a planted off-line zero at
`delta = 0.01`, `gamma = 14.134725` (X-0010 part 1):

```
    alpha = 1                          |phi| = 1.00005    no negative lambda_n
                                                          up to n = 100000
    alpha = 1/2 + 4.0 delta + i gamma  |phi| = 1.6667     lambda_2 < 0
    alpha = 1/2 + 2.0 delta + i gamma  |phi| = 3.0000     lambda_2 < 0
    alpha = 1/2 + 1.5 delta + i gamma  |phi| = 5.0000     lambda_2 < 0
    alpha = 1/2 + 1.1 delta + i gamma  |phi| = 21.000     lambda_2 < 0
```

The measured moduli reproduce `(u+delta)/(u-delta)` to every printed digit
(`5/3, 3, 5, 21`), so the amplification law is confirmed as an identity and not
merely as an asymptotic.  Classically the same counterexample would need
`n ~ gamma^2/delta = 19979`.

## What this is NOT: the delta-resolution wall is not broken

`|phi_alpha(rho)|` is large only when `|v - gamma|` is at most about `delta`.
A blind scan over `v` therefore needs a grid of spacing `~delta`, and the total
work to sweep a height range `[0,T]` is `~ T/delta` probes -- the same
`1/delta` factor that appears in every other criterion here.  The sharp form of
this, from (*): the pair `{1/2 - delta + i gamma, 1/2 + delta + i gamma}`
contributes

```
    (u+delta)/((u+delta)^2 + d^2)  +  (u-delta)/((u-delta)^2 + d^2),   d = v-gamma
```

to `Re(xi'/xi)(alpha)`, and this is negative **exactly when** `d^2 < delta^2 - u^2`.
The detection window in `v` has half-width `sqrt(delta^2 - u^2) < delta`, for
every choice of `u`.  There is no setting of `u` that widens it.

So T-0004 is **not a search**.  It is the last stage of a pipeline: a cheap
screen produces a candidate `(gamma, delta)`; this converts the candidate into
a witness of size `n = 2`, or into a single certified real number via (*).
That is the role Q-0012 was looking for, and it is the role it can have.

The wall itself is worth naming.  Three criteria of completely different type
-- contour integration (L-0002), prime sums (T-0002), and now conformal
re-centring (T-0004) -- all pay exactly `1/delta`.  Whether that exponent is
intrinsic is recorded as a new open problem (Q-0016); it is the sharpest
structural regularity this repository has found.

## Certified results (X-0010 part 2)

`li_general` on real `zeta`, ball arithmetic throughout, `tol_bits = 500`,
16 coefficients at each of twelve centres `alpha = 1/2 + u + i v` with
`u in {0.1, 0.01, 0.001}` and `v` at the midpoint of the tightest zero pairs
this repository has certified:

| target | v | u | positive | negative |
|---|---|---|---|---|
| low zero | 14.1347 | 0.1 / 0.01 / 0.001 | 16/16 | none |
| Lehmer pair 1977 | 1977.2227 | 0.1 / 0.01 / 0.001 | 16/16 | none |
| Lehmer pair 1329 | 1329.1243 | 0.1 / 0.01 / 0.001 | 16/16 | none |
| classical Lehmer pair 7005 | 7005.0817 | 0.1 / 0.01 / 0.001 | 16/16 | none |

Enclosure radii `1e-150` to `1e-180`; total runtime under 4 s.  Every value is
certified positive.  **No counterexample.**  Aimed directly at the four closest
zero pairs known to this repository, with `u` pushed down to `0.001`, the
targeted criterion still sees nothing off the line.

By the window computation above, the `u = 0.001` rows rule out an off-line pair
with `delta > 0.001` whose ordinate lies within `sqrt(delta^2 - u^2)` of the
tested `v` -- a genuinely local statement, and one that no other criterion in
the repository delivers from a single point evaluation.

## Validation

1. **Reduction.**  `li_general(alpha=1, n)` agrees with `li_coefficients(n)` for
   `n = 1..12` to all 30 printed digits, with overlapping enclosures.  The two
   go through different code: `xi_taylor_at` re-centres the Euler-Maclaurin
   Taylor model at an arbitrary complex `alpha`, uses `polygamma` at `alpha/2+1`
   rather than at `3/2`, and rescales the composition by `2u`.  Agreement at
   `alpha = 1` exercises all of that against the path already validated in
   T-0003.
2. **The identity (*).**  `lambda_1^(alpha)` from the series and
   `2u * Re(xi'/xi)(alpha)` from the first two Taylor coefficients agree to 24+
   digits with overlapping enclosures at `(u,v) = (0.5,0), (0.1,14.13),
   (0.01,1977.22), (0.001,7005.08)`.  This is a strong end-to-end check: the
   left side runs through the Mobius composition and a series logarithm, the
   right side does not.
3. **Enclosure honesty.**  `xi_taylor_at` propagates the Euler-Maclaurin
   remainder into every Taylor coefficient by Cauchy on `|s - alpha| = R`,
   including the `|alpha - 1|` factor that the `alpha = 1` case does not need.
   Omitting this was R-0008; the regression test for it is in
   `tests/test_li.py`.

## Reproduce

```
python3 experiments/X-0010-targeted-li/run.py
python3 -m pytest tests/test_li.py -q
```

## Open

- Q-0016: is the `1/delta` cost exponent intrinsic to *every* certified
  criterion, or is it an artefact of the three families tried so far?
- (*) makes `Re(xi'/xi) > 0` checkable at ~1 ms per point.  What is the cheapest
  screen that produces candidates `(gamma, delta)` at a rate this can consume?
  See X-0011.
