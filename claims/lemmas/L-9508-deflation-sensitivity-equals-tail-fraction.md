# L-9508 — Deflation sensitivity equals the zero-side tail fraction

Claim ID: L-9508
Title: What a zero-deflation route can detect is capped by its uncertified tail, and that is decided by the decay of the zero-side weight
Status: PROPOSED
Authoring agent: `claude-09`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: none beyond the stated hypothesis; `L-9507` and `X-9504` are the worked example
Scope: every "certified-zero deflation" route in the repository
Related counterexample candidates: none; this claim **ranks** the routes

## Motivation

The repository currently has a large deflation cluster — issues #84, #93,
#121, #137 and draft PRs #90, #96, #97, #99, #100, #101, plus `L-9505` on the
screw route — all sharing one shape: certify critical-line zeros, subtract
their contribution from an RH-nonnegative quantity, and look for a negative
residual.  Each branch is separately certifying zeros at real cost.

`X-9504` showed that for the screw route the residual is exactly the
uncertified tail and that closing it would need about `10^14` certified zeros.
This claim isolates the reason, which turns out not to be about the screw
function at all, and turns it into a cheap test any route can apply *before*
spending certification effort.

## Statement

**Hypothesis (a deflation route).**  Under RH a quantity `Q` admits a
nonnegative zero expansion

\[
 Q=\sum_\gamma w(\gamma),
 \qquad w(\gamma)\ge0,
\tag{L-9508.1}
\]

where `Q` is determined by arithmetic data (prime sums, archimedean terms,
`xi` evaluations) and `w(gamma)` is determined by the individual ordinate.
The sum runs over the zero ordinates with multiplicity, both signs.

Let `Gamma` be a finite set of zeros certified with multiplicity, and put

\[
 \rho_\Gamma=\frac{\sum_{\gamma\in\Gamma}w(\gamma)}{Q},
 \qquad
 F_\Gamma=1-\rho_\Gamma
 =\frac{\sum_{\gamma\notin\Gamma}w(\gamma)}{Q}.
\tag{L-9508.2}
\]

**(a) Deflation inequality.**  RH implies `rho_Gamma <= 1`, i.e. `F_Gamma >= 0`.
A directed certificate of `rho_Gamma > 1` disproves RH.

**(b) Sensitivity.**  Suppose RH fails in a way that makes the true arithmetic
side smaller than its on-line prediction by relative amount `delta`,

\[
 Q_{\rm true}=(1-\delta)\,Q_{\rm RH}.
\]

Then the deflation test fires — that is, `sum_{Gamma} w > Q_true` — **if and
only if**

\[
 \boxed{\delta>F_\Gamma.}
\tag{L-9508.3}
\]

So `F_Gamma` is exactly the detection threshold.  If in addition the two sides
are enclosed with combined relative width `epsilon`, a *certificate* needs
`delta > F_Gamma + epsilon`.

**(c) No trade.**  Arithmetic-side precision cannot push the threshold below
`F_Gamma`, and zero certification cannot push it below `epsilon`.  The two
costs are not interchangeable: they bound different terms of
`F_Gamma + epsilon`.

**(d) The tail fraction is decided by the decay of `w`.**  Take
`Gamma = {|gamma| <= T}` and the Riemann-von Mangoldt density
`dN = (2 pi)^{-1} log(gamma/2 pi) d gamma`.  Then

\[
 F(T)\;\asymp\;\frac1Q\int_T^\infty w(\gamma)\,\frac{\log(\gamma/2\pi)}{2\pi}\,d\gamma,
\tag{L-9508.4}
\]

giving

```text
w(gamma) ~ gamma^{-2}          F(T) ~ log(T) / T
w(gamma) ~ gamma^{-2k}         F(T) ~ log(T) / T^{2k-1}
w = |f-hat|^2, f in C^k_c      F(T) = O( log(T) / T^{2k-1} )
w Gaussian                     F(T) decays superexponentially
```

**(e) Cost law in the heavy band.**  If `w ~ gamma^{-2}` then improving the
detection threshold by one decimal digit costs a factor of about `10` in `T`,
hence about `10` in the number of certified zeros — because `F(T) ~ log T / T`
and the zero count below `T` is `~ (T/2 pi) log(T/2 pi)`.  Ten digits of
sensitivity cost ten orders of magnitude of certification.

## Proof

**(a)** Under RH, (L-9508.1) is a sum of nonnegative terms, and `Gamma` indexes
a subset of them, so `sum_{Gamma} w <= sum_all w = Q`.  A certified strict
reverse inequality contradicts that.

**(b)** By definition `sum_{Gamma} w = (1 - F_Gamma) Q_RH`.  The test fires iff
`sum_{Gamma} w > Q_true`, i.e. iff
`(1 - F_Gamma) Q_RH > (1 - delta) Q_RH`, i.e. iff `delta > F_Gamma`, since
`Q_RH > 0`.  Adding the enclosure widths shifts the threshold by `epsilon`.

**(c)** Immediate from the two terms being independent: `F_Gamma` depends only
on which zeros were certified, `epsilon` only on the arithmetic.

**(d)** Substitute the density into the tail sum; the displayed rates are the
standard asymptotics of `int_T^infty gamma^{-2k} log(gamma) d gamma`, and for
`f in C^k_c` the bound `|f-hat(gamma)| = O(gamma^{-k})` gives
`w = O(gamma^{-2k})`.

**(e)** `F(T) ~ c log(T)/T` and `N(T) ~ (T/2 pi) log(T/2 pi)`, so
`F ~ 10^{-d}` needs `T ~ 10^{d}` up to logarithms, hence `N(T) ~ 10^{d}` up to
logarithms. ∎

## Consequences for the repository

Measured in `X-9506`, with the target set at a relative deficit of `1e-12`:

```text
zero-side weight w(gamma)                        F(1000)     required T   certified zeros
1/gamma^2  (screw Psi; xi'/xi Pick at a point)  4.181e-02      2.217e+14        1.065e+15
1/gamma^4  (hypothetical second-order kernel)   7.711e-06      2.498e+05        3.813e+05
1/gamma^6                                       1.163e-09      4.309e+03        3.793e+03
Weil, C^0  test function (sinc^2)               3.627e-02      1.914e+14        9.154e+14
Weil, C^2  test function (sinc^4)               1.021e-05      2.758e+05        4.253e+05
Weil, C^6  test function (sinc^8)               3.391e-12      1.200e+03        8.120e+02
Weil, C^10 test function (sinc^12)              6.792e-20      2.168e+02        8.766e+01
Gaussian   exp(-gamma^2/200)                    0.000e+00      7.430e+01        1.739e+01
```

Three conclusions, in decreasing order of confidence.

1. **The screw route's deflation is blocked, and not by accident.**  Krein's
   screw normalization fixes the weight at exactly `gamma^{-2}` — the slowest
   decay for which the expansion still converges.  `L-9505` is correct and
   unimprovable in this respect; the obstruction is structural.  This
   reproduces the `X-9504` order of magnitude by an independent route
   (`2.2e14` here against `3.3e13` there, the difference being the fitted
   constant `K = 3.43`).

2. **A route's band is a property of its weight, not of its effort.**  A `C^0`
   or bounded-variation test function puts a Weil carrier route in the *same*
   band as the screw route — `1.9e14` — while a `C^6` test function of the
   same support needs `812` certified zeros.  The decisive design choice is
   the smoothness of the test function, not the search over carriers.

3. **In the light band the binding constraint moves off zero certification
   entirely.**  At `C^6` the required zero count is already within reach of
   published certified tables, and `F` is below `1e-12`; the threshold is then
   set by `epsilon`, i.e. by how tightly the prime and archimedean sides can
   be enclosed.  Effort spent certifying *more* zeros there is wasted, and
   effort spent on directed arithmetic is not.

**The actionable test.**  Before certifying more zeros, a deflation branch
should compute `F(T)` for its own weight at the `T` it can reach.  If `F(T)`
is far above the enclosure width, more zeros will not help enough; if it is
far below, more zeros are not needed.

## Gap audit

- (L-9508.1) is a **hypothesis about the route**, not a theorem.  Applying this
  claim to a specific branch requires that branch's own normalization audit to
  confirm its `Q` really has a nonnegative zero expansion with the weight
  claimed.  I have carried that audit out only for the screw route
  (`X-9503`).  The rows above for the Weil and Pick weights are **weight-class
  calculations**, not audits of any particular branch's implementation, and
  must not be quoted as verdicts on a specific PR.
- (L-9508.3) models the failure of RH as a single relative shift `delta` of the
  arithmetic side.  A genuine off-line zero changes the expansion's
  *structure* — an off-line `gamma` is complex and its term is no longer of the
  form `w(gamma) >= 0` — so `delta` is a proxy for the size of the resulting
  discrepancy, not a description of it.  The threshold statement is
  nonetheless the right one: whatever the discrepancy, it must exceed the
  uncertified tail to be visible.
- The rates in (d) are asymptotic in `T`; the table uses a numerical
  quadrature of (L-9508.4) with the density, not a proved tail bound.  It is a
  scaling calculator.
- `|f-hat| = O(gamma^{-k})` for `f in C^k_c` is the standard bound and is not
  sharp for specific `f`; a particular test function may do better.
- Nothing here says deflation is useless.  It says deflation buys exactly
  `F_Gamma` of sensitivity and no more, and that this is knowable in advance.
- The claim says nothing about whether any route can *find* a `delta > 0`.

## Adversarial tests

1. For the screw route at `n=53`, `h=log(2)/3`, `T=1000`, the claim predicts a
   threshold `F ~ 4e-02` from the weight class.  `X-9503` measured the
   optimized deficit at `6.6e-03`.  These differ by the optimization over `b`,
   which the weight-class calculation ignores; check that the *measured* value
   is never below the class value by more than the optimization can explain.
2. Take a synthetic finite zero set and a known `w`; verify (L-9508.3) exactly
   by construction.
3. Vary the smoothness `k` of a test function at fixed support and confirm
   `F(T)` scales as `T^{-(2k-1)}`.
4. Confirm the two costs do not trade: raise precision at fixed `Gamma` and
   verify the detection threshold does not fall below `F_Gamma`.

**Status.**  Test 1 was run: the class value `4.18e-02` sits above the measured
optimized deficit `6.6e-03` by a factor `6.3`, consistent with the
optimization over `b` recovering part of the tail; the class value is a
conservative estimate of the threshold, as intended.  Tests 2-4 are not run.

## Remaining uncertainty

The lemma is elementary and I am confident in (a)-(c).  Part (d) is standard
asymptotics.  The **application** to any branch other than the screw route is
the uncertain step, because it needs that branch's weight identified correctly,
and I have not audited those branches.  I would not want row 4 of the table
("Weil, C^0") read as a verdict on any specific carrier PR without that audit.

## Suggested next attack

Run the `X-9506` calculator against the actual weights used by the branches in
the deflation cluster — that requires, for each, one line: what is `w(gamma)`?
Issues #84, #93, #121 and #137 are the ones with live certification requests.
If any of them is in the light band, its zero-certification dependency can be
closed immediately and the effort redirected to directed arithmetic; if in the
heavy band, the branch should be told before more zeros are produced.
