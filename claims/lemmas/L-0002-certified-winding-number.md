```text
Claim ID:       L-0002
Title:          Certified winding-number zero counting from ball enclosures
Status:         PROVED
Authoring agent: claude-01
Reviewing agents: claude-02 (2026-07-26) -- the counting layer was
                reimplemented independently from this statement (winding2.py:
                convex-cone principal-difference rule, different subdivision)
                and cross-validated on 8 boxes including two Lehmer pairs and
                two adversarial near-edge cases; full agreement, X-0017.  The
                evaluator half of Q-0003 (independent Euler-Maclaurin)
                remains open.
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001 (for f = zeta or xi), argument principle
Scope:          Any f analytic on a neighbourhood of a closed rectangle R,
                nonvanishing on the boundary dR
Related counterexample candidates: the acceptance test for any Z-#### of
                type A (direct off-critical zero)
```

## Statement

Let `f` be analytic on an open set containing the closed rectangle `R`, and let
`dR` be its positively oriented boundary.  Suppose `dR` is written as a
concatenation of arcs `g_1, ..., g_m` with `g_j` running from `a_j` to `b_j`
(`b_j = a_{j+1}`, `b_m = a_1`).  Suppose for each `j` we have a closed ball
`B_j` with `g_j subset B_j`, `B_j` inside the domain of analyticity, and a
ball enclosure `Z_j` with

```
f(B_j) subset Z_j    and    0 not in Z_j.                                (W1)
```

Then `f` has no zero on `dR`, and the number of zeros of `f` inside `R`,
counted with multiplicity, equals

```
n(R, f) = (1/(2 pi)) * sum_{j=1}^{m} Arg( f(b_j) / f(a_j) ),              (W2)
```

where `Arg` denotes the **principal** value in `(-pi, pi]`.

Consequently, if certified enclosures of the right-hand side of (W2) determine
an interval of length `< 1` containing exactly one integer `k`, then
`n(R, f) = k` exactly.

## Definitions

`n(R, f)` is the number of zeros of `f` in the *interior* of `R` counted with
multiplicity.  All balls are closed discs in `C`.  "Certified enclosure" means
a set guaranteed by ball arithmetic to contain the true value.

## Motivation

This is the acceptance test for a direct counterexample.  A candidate
off-critical zero is only a candidate until some rigorous procedure proves a
zero *exists* inside a region that is *disjoint from the critical line*.  (W2)
does exactly that, and it does it with a finite, replayable certificate: the
list of arc endpoints and the enclosures `Z_j`.  A verifier need not rerun the
search — only re-evaluate `f` on the listed balls.

The same machinery run with the answer `0` produces certified **zero-free**
rectangles, which is how this project rules regions out and narrows the hunt.

## Proof

*No zeros on the boundary.*  Each point of `dR` lies on some `g_j subset B_j`,
so its image lies in `Z_j`, which by (W1) omits `0`.

*Argument principle.*  Since `f` is analytic on a neighbourhood of `R` and
nonvanishing on `dR`,

```
n(R, f) = (1/(2 pi i)) INT_{dR} f'(z)/f(z) dz = (1/(2 pi)) * Var_{dR} arg f,
```

where `Var` is the total continuous variation of a continuous branch of
`arg f` along the closed contour.  This is standard.

*Localisation of each arc's contribution.*  Fix `j`.  The set `Z_j` is a
closed disc with `0 not in Z_j`.  A disc not containing the origin is contained
in an open half plane `H_j = { w : Re(w e^{-i phi_j}) > 0 }` for a suitable
`phi_j`: indeed, if `Z_j` has centre `c` and radius `rho` then `|c| > rho`, and
`H_j` with `phi_j = arg c` works, since for `w in Z_j`,
`Re(w e^{-i phi_j}) >= |c| - rho > 0`.

On `H_j` the principal branch of `arg(w e^{-i phi_j})` is continuous with values
in `(-pi/2, pi/2)`.  Therefore, along `g_j`, a continuous branch of `arg f`
changes by

```
Var_{g_j} arg f = arg(f(b_j) e^{-i phi_j}) - arg(f(a_j) e^{-i phi_j})
                 in (-pi, pi).
```

Since the variation lies in `(-pi, pi)` and `Var_{g_j} arg f` is congruent mod
`2 pi` to `Arg(f(b_j)/f(a_j)) in (-pi, pi]`, the two are equal (two numbers in
`(-pi, pi]` that differ by a multiple of `2 pi` are equal, and the value `pi`
is excluded for the variation because the variation is `< pi` strictly).

Summing over `j` and using additivity of the continuous variation along the
concatenation gives (W2). ∎

## Implementation and certificate semantics

`scripts/winding.py`:

* `g_j` are straight segments; `B_j` is the axis-aligned ball covering the
  segment (a rectangle-shaped `acb` ball, which contains the segment).
* If the computed `Z_j` contains `0`, the arc is **bisected** and the test
  retried, to a bounded depth.  Exhausting the depth returns `ok = False` — it
  never returns a count.  This is the only failure mode and it is *safe*: a
  zero on or extremely close to the contour makes the procedure abstain, not
  lie.
* Two extra guard conditions force subdivision: `|Arg(f(b)/f(a))|` must be
  bounded away from `pi` (default `<= 0.75 pi`) and the enclosure of that `Arg`
  must be narrow.  Neither is required by the proof — both are cheap insurance
  against a wide enclosure straddling the branch cut of `Arg`.
* The returned interval for `(1/2pi) sum Arg(...)` is certified; a count is
  emitted only if that interval pins down a unique integer.

## Analytic domain audit

* Applied to `f = xi` (entire): no poles, no branch cuts, no trivial zeros.
  This is why the implementation counts zeros of `xi`, not of `zeta` — using
  `zeta` on a rectangle whose closure meets `s = 1` would be invalid, and the
  trivial zeros would pollute rectangles reaching `Re(s) < 0`.
* `xi(s) = pi^{-s/2} Gamma(s/2 + 1) (s-1) zeta(s)` is used in the pole-free
  form `(s-1) zeta(s)`, computed by multiplying the Euler-Maclaurin
  representation through by `(s-1)`; the only singular term
  `N^{1-s}/(s-1)` becomes `N^{1-s}`.  Hence the evaluator is valid at `s = 1`
  too, and `xi` is enclosed correctly on rectangles containing `s = 1`.
* `pi^{-s/2} := exp(-(s/2) log pi)` with the real `log pi`: single-valued.
* `Gamma(s/2 + 1)` is analytic for `Re(s) > -2`; every rectangle used lies in
  `Re(s) >= 0`.
* The contour is a rectangle boundary; no deformation is performed.

## Dependency audit

* Argument principle: used once (needs `f` analytic on a neighbourhood of `R`
  and nonvanishing on `dR`; both established above).
* L-0001: used to produce `Z_j`.
* Additivity of continuous argument variation along concatenated arcs:
  elementary.

## Gap audit

* **Existence vs. count.** (W2) certifies a *count*, not a location.  A count
  `>= 1` in a rectangle disjoint from the critical line **would** be a genuine
  counterexample certificate; a count of `0` certifies a zero-free region.  A
  count of `1` does *not* by itself give an enclosure of the zero tighter than
  the rectangle — that is fine, since the rectangle is what must be disjoint
  from the critical line.
* **Multiplicity.** The method counts with multiplicity and cannot distinguish
  a double zero from two simple zeros.  Do not claim simplicity from it.
* **Boundary zeros.** Not an error source: the method abstains.
* **Interior of R.** The count is for the open rectangle; a zero exactly on the
  boundary makes (W1) fail, so this is consistent.
* **Wide-ball overestimation** can make the procedure abstain unnecessarily;
  this costs time, not correctness.
* **The branch-cut trap.** `Arg` is discontinuous across the negative reals.
  The proof avoids it entirely by bounding the variation *before* taking any
  principal value; the guard conditions add a second layer.  This is the single
  most common error in naive implementations of this method and is worth a
  reviewer's attention.

## Adversarial tests

Implemented in `tests/test_winding.py`:

1. Polynomials with known zero counts: `z`, `z^2`, `z^2+1`, `(z-0.3)^5`,
   `z^3 - 1` on rectangles that do and do not contain the zeros.
2. A rectangle whose boundary passes exactly through a zero (`f = z`, `R` a
   square centred at the origin with a corner at 0 — the routine must abstain,
   not return a number).
3. `xi` on `[0,1] x [0,T]` for `T = 30, 50, 100`: counts `3, 10, 29`, matching
   independent knowledge of the ordinates of the low-lying zeros.
4. Symmetry: the count on `[0, 1/2] x [0,T]` must equal the count on
   `[1/2, 1] x [0,T]` (functional equation), for every `T` avoiding a zero
   ordinate... **NOTE:** these two rectangles share the critical line as an
   edge and every known zero lies on it, so both counts *abstain*.  The test is
   therefore run as `[0, 1/2 - d] x [0,T]` vs `[1/2 + d, 1] x [0,T]`, which
   must agree by `xi(s) = xi(1-s)` and `xi(sbar) = conj(xi(s))`.  This is a
   genuine independent check of the whole stack, and it passes with both
   counts `0` for `d = 0.01`, `T = 100`.
5. Additivity: the count over `[0,1] x [0,T]` equals the sum of the counts over
   stacked sub-rectangles (used in production via `count_zeros_rect_split`).

## Remaining uncertainty

Low for the mathematics.  Moderate for the *engineering* claim that the code
implements the proof: the guard constants are heuristic, and an independent
reimplementation is the appropriate check.  Requested: see OPEN_PROBLEMS Q-0003.

## Suggested next attack

* Add a rigorous `zeta'` bound (Q-0002) to upgrade counts to interval-Newton
  *uniqueness* certificates.
* Use the certificate format to make verification cheap: store the arc
  endpoints and let a verifier re-derive (W2) without re-running subdivision.
