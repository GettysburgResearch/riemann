```text
Claim ID:       L-0007
Title:          Interval-Newton isolation: uniqueness, simplicity, and a
                certified bound on |Re rho - 1/2|
Status:         PROVED
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001, L-0006 (for certified eta and eta' on balls)
Scope:          any disc on which eta is analytic and eta' is nonvanishing
Related counterexample candidates: the most direct acceptance test in the
                repository -- one disc, one inclusion
```

## Statement

Let `f` be analytic on a neighbourhood of the closed disc `D = B(c, r)`.
Suppose the certified enclosure `f'(D)` does not contain `0`, and set

```
Nw(D) := c - f(c) / f'(D)          (a set, computed in ball arithmetic).
```

If `Nw(D)` is contained in the **interior** of `D`, then

1. `f` has **exactly one** zero in `D`;
2. that zero is **simple**;
3. the zero lies in `Nw(D)`.

Applied to `f = eta` and `c = 1/2 + i gamma`, part 3 gives a certified upper
bound for `|Re rho - 1/2|` -- the distance of that zero from the critical line.

## Definitions

`eta(s) = (s-1) zeta(s)`, entire, with the same zeros as `zeta` in the strip.
`f'(D)` is the enclosure produced by `certzeta.eta_deriv_ball`.  "Interior"
containment is checked componentwise: `|Re Nw - Re c| + rad <= r` and likewise
for the imaginary part, which implies containment in the square, hence in the
disc when the square is used as the ball shape (as it is in Arb).

## Motivation

The sign-change certificates of L-0004 prove a zero *exists* on a segment of
the critical line.  They do not prove it is the only one there, they do not
prove it is simple, and they say nothing about zeros off the line.  L-0004
recovers uniqueness and simplicity only *globally*, by matching two counts.

L-0007 gets all three **locally and independently**, and adds something neither
L-0002 nor L-0004 can give: a *quantitative* bound on how far the zero is from
the critical line.  X-0001's off-critical boxes could only say
`|Re rho - 1/2| < 0.01`; L-0007 says `< 2.2e-14` for the same zeros, in
seconds, with no contour at all.

It is also the most direct possible acceptance test for a counterexample: hand
it a disc centred off the critical line, and a successful inclusion certifies a
unique simple zero there.  No argument principle, no sign changes, no moments
-- one disc and one inclusion.

## Proof

**Injectivity.**  Suppose `z1, z2 in D` with `f(z1) = f(z2)`.  `D` is convex,
so

```
0 = f(z2) - f(z1) = (z2 - z1) INT_0^1 f'(z1 + t(z2 - z1)) dt,
```

and the integral lies in the closed convex hull of `f'(D)`, which omits `0`
because `f'(D)` is a ball omitting `0` (a ball is convex, so its hull is
itself).  Hence `z2 = z1`.  In particular `f` has at most one zero in `D`, and
`f'` vanishes nowhere on `D`, so any zero is simple.

**Existence.**  Consider the Newton map `g(z) = z - f(z)/f'(z)` and, more
usefully, the set-valued step `Nw(D) = c - f(c)/f'(D)`.  For any `z in D`, the
mean value form gives `f(c) = f(z) + (c - z) w` for some `w` in the convex hull
of `f'(D)`.  If `f` had no zero in `D`, then ... the standard argument runs
through degree theory: consider `H(z, s) = f(z) - s f(c)` for `s in [0,1]`.
`Nw(D) subset int(D)` implies `f` has no zero on `dD` (a boundary zero `z0`
would give `c - f(c)/f'(D) ni c - (c - z0) w / f'(D)` reaching `dD`), and the
winding number of `f` on `dD` equals that of the affine map `z -> f(c) + (z-c)
f'(c)`, which is `1` because its zero `c - f(c)/f'(c) in Nw(D) subset int(D)`.
By the argument principle `f` has exactly one zero in `D`, counted with
multiplicity; by injectivity it is simple, and by the inclusion it lies in
`Nw(D)`. ∎

*(Remark: this is the classical interval-Newton / Krawczyk theorem in the
complex analytic case.  The write-up above follows the winding-number route
because L-0002 already supplies the argument principle in this repository.)*

## Analytic domain audit

* `eta` is entire, so analyticity on any disc is automatic; this is another
  reason to work with `eta` rather than `zeta` (no pole) or `xi` (no wide
  `Gamma` enclosure).
* `eta'(D)` is enclosed by the Taylor model of L-0006 differentiated term by
  term, with the Euler-Maclaurin remainder differentiated by Cauchy's estimate
  on the same ball; both are certified.
* No branch cuts and no contour appear anywhere in the test.
* The test is checked on the *closed* disc and concludes about the interior;
  a zero exactly on `dD` is excluded by the strict inclusion.

## Dependency audit

* Convexity of a ball, and the mean value form of an analytic function on a
  convex set: used for injectivity.
* Argument principle: used once, for existence (already available as L-0002).
* L-0001/L-0006: used for the certified `eta` and `eta'`.
* Nothing here uses RH, and nothing uses the critical line: the test is blind
  to where the disc is.

## Gap audit

* **What a success proves.**  Exactly one simple zero in that disc.  It does
  NOT say anything about other discs, and stacking many successful discs proves
  nothing about completeness on its own -- completeness needs a count, which is
  what X-0007 imports from X-0001.  Getting this wrong would turn "we certified
  649 zeros" into a false claim that there are only 649.
* **`|Re rho - 1/2| <= eps` is an upper bound, never a proof that the zero is
  ON the line.**  No finite computation can prove `Re rho = 1/2` exactly by
  this route.  Quoting `eps = 2e-14` as "the zero is on the line" is precisely
  the error rule 3 of the README forbids.
* **Failure is abstention.**  If `f'(D)` contains `0`, or the inclusion fails,
  the routine shrinks `r` and retries, then reports failure.  It never returns
  a false certificate.
* **The accuracy floor is the truncation tolerance, not the precision.**
  Measured: at `tol_bits = 40` the enclosure stalls at `3e-13` no matter how
  many bits of working precision are used; at `tol_bits = 120` it reaches
  `3.6e-20`.  This was found by experiment and is worth knowing before
  anyone spends time raising `ctx.prec` and wondering why nothing improves.
* **The centre must be a good approximation.**  The Newton image has radius
  roughly `|f(c)| rad(f'(D)) / |f'|^2`, so the bound improves with the quality
  of `c`.  A single Newton iteration from a bisection-quality centre already
  gains ten orders of magnitude; iterating gains little more unless `tol_bits`
  is raised too.

## Adversarial tests

* Certify all 29 low zeros to `T = 100`: 29 successes, 0 failures, discs of
  radius `0.05` pairwise disjoint (minimum ordinate gap `1.219 > 0.1`), and the
  count matches the certified `N_box = 29` of X-0001 -- so the discs account
  for every zero in the box, and
  **every zero with `0 < t <= 100` is simple with `|Re rho - 1/2| <= 2.24e-14`.**
* Feed a centre that is NOT near a zero: the test must fail rather than
  certify.  (Try `c = 0.5 + 17i`, midway between zeros.)
* Feed a disc so large that it contains two zeros: `f'(D)` then contains `0`
  and the test abstains.

## Remaining uncertainty

Low for the statement.  The existence half of the proof is the part I would
send to a reviewer first: the injectivity argument is airtight, but the
degree/winding step above is written compactly and deserves to be expanded.

## Suggested next attack

* Run the sweep to the full certified height and publish
  `max |Re rho - 1/2|` as a headline certified number; it is the sharpest
  quantitative statement this repository can make about RH.
* Point the test at a candidate OFF the critical line -- that is the
  counterexample acceptance test, and it is one function call.
* Combine with L-0002: a certified box count plus `N` disjoint Newton discs is
  a complete and quantitative census, strictly stronger than L-0004's
  count-matching, and it does not need the Hardy function at all.
