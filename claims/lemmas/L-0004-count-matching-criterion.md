```text
Claim ID:       L-0004
Title:          Count-matching criterion: certified RH verification in a box
Status:         PROVED
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001, L-0002, functional equation, intermediate value theorem
Scope:          Rectangles R = [0,1] x [0,T] with no zero ordinate equal to T
Related counterexample candidates: the *refutation* engine; every certified
                 range is a region where no Z-#### of type A can exist
```

## Statement

Let `T > 0` and `R = [0,1] x [0,T]`.  Suppose:

1. (L-0002) the certified winding number of `xi` on `dR` yields
   `n(R, xi) = N_box`, an exact integer; and
2. there exist real numbers `0 < t_1 < u_1 <= t_2 < u_2 <= ... <= t_m < u_m <= T`
   with certified enclosures of `Z(t_i)` and `Z(u_i)` of strictly opposite
   signs, where `Z` is the Hardy function; and
3. `m = N_box`.

Then **every** zero of `zeta` with `0 < Im(s) <= T` lies on the critical line,
is simple, and the `m` sign-change intervals `(t_i, u_i)` isolate them all.

## Definitions

`Z(t) = e^{i theta(t)} zeta(1/2 + i t)`, `theta(t) = Im log Gamma(1/4 + it/2)
- (t/2) log pi`, with the continuous branch of `log Gamma` on the ray
`{1/4 + it/2 : t >= 0}` (Arb's `lgamma` uses exactly this branch, and
`theta(0) = 0`).  `Z` is real-valued and real-analytic on `R`, and
`|Z(t)| = |zeta(1/2+it)|`.

## Motivation

This is the project's **refutation engine**.  Every range certified by L-0004
is a range in which a type-A counterexample provably does not exist, so the
search can be pointed elsewhere with confidence rather than superstition.  It
also produces, as a by-product, certified enclosures of the on-line zeros,
which are the raw material for the Lehmer-pair targeting (X-0004) and for the
Li-coefficient work (L-0005).

Equally important: L-0004 is the honest statement of what a "verification of
RH to height T" is.  It is a *finite* statement.  It says nothing whatever
about `t > T`, and the project must never let it be quoted as if it did.

## Proof

By hypothesis 2 and the intermediate value theorem applied to the continuous
real function `Z` on each `[t_i, u_i]`, there is `tau_i in (t_i, u_i)` with
`Z(tau_i) = 0`.  Since `e^{i theta}` never vanishes, `zeta(1/2 + i tau_i) = 0`.
The intervals are pairwise disjoint (hypothesis 2 orders them with
`u_i <= t_{i+1}`), so the `tau_i` are `m` distinct zeros of `zeta` on the
critical line with ordinates in `(0, T]`.

Each `1/2 + i tau_i` lies in the interior of `R` (as `0 < tau_i < T` and
`Re = 1/2 in (0,1)`), and is a zero of `xi`, since
`xi(s) = pi^{-s/2} Gamma(s/2+1)(s-1) zeta(s)` and the prefactor is nonzero at
`s = 1/2 + i tau_i`.  Hence `n(R, xi) >= m`, counted with multiplicity.

By hypothesis 1 and 3, `n(R, xi) = N_box = m`.  Therefore the multiplicity
count is exactly saturated by these `m` distinct points: each `tau_i` is a
**simple** zero (a multiplicity `>= 2` would force `n(R,xi) > m`), and there is
**no other** zero of `xi` in the interior of `R`.

Finally, every nontrivial zero `rho` of `zeta` with `0 < Im(rho) <= T` has
`0 <= Re(rho) <= 1` (elementary: `zeta` has no zeros with `Re >= 1`, and by the
functional equation none with `Re <= 0` except the trivial ones, which are real
and hence have `Im = 0`), so it is a zero of `xi` in `R`; if `Im(rho) < T` it
is interior and hence one of the `tau_i`.  The excluded case `Im(rho) = T` is
ruled out because a zero on `dR` would make the L-0002 certificate abstain
rather than return `N_box`. ∎

## Analytic domain audit

* `Z` is real-valued: `Z(t) = e^{i theta(t)} zeta(1/2+it)` and the functional
  equation gives `conj(Z(t)) = Z(t)` for real `t`.  The implementation returns
  `Re` of the computed ball and the imaginary part is checked to contain `0` —
  a live self-test of both `theta` and `zeta`.
* Branch of `theta`: `Im log Gamma` on the given ray, continuous, `theta(0)=0`.
  A wrong branch would shift `Z` by a sign on some intervals and could only
  *create* spurious sign changes, i.e. make `m > N_box`, which fails
  hypothesis 3 loudly rather than silently.  This is a designed-in tripwire.
* `xi` entire; `R` avoids nothing and needs no deformation.

## Dependency audit

* L-0002 for `N_box` (used once, hypothesis 1).
* L-0001 inside both L-0002 and the evaluation of `Z` (hypothesis 2).
* IVT on `Z` (used once).
* "No zeros with `Re(s) >= 1`": classical (Hadamard-de la Vallee Poussin); used
  only in the last paragraph, to know that a zero of `zeta` in the upper half
  plane with `0 < Im <= T` must lie in the strip.  **This is the one classical
  input that is not reproved here.**  It is not circular: it is far weaker than
  RH and its standard proof (via `3 + 4 cos + cos 2 >= 0`) does not use RH.

## Gap audit

* **Finite range only.**  The conclusion is `t <= T`.  Extrapolating to all `t`
  is exactly the error rule 14 of the README forbids.
* **`N_box == m` is essential.**  If `m < N_box` the conclusion fails and the
  correct reaction is *interest*, not a bug report: the deficit is precisely
  where an off-line zero (or a missed sign change, or a double zero) would
  live.  The experiment records the deficit explicitly for this reason.
* Sign changes prove existence of on-line zeros; they do **not** prove the
  zeros are the only ones without hypothesis 1.
* The classical statement "no zeros with `Re >= 1`" is used unconditionally and
  is not RH-dependent.
* Zeros with `Im(rho) = 0`: `zeta` has no zeros on `(0,1)` real axis
  (`zeta(sigma) < 0` there) and the trivial zeros are at `-2, -4, ...`, all
  outside `R`.  Zeros with `Im = 0` therefore contribute nothing.

## Adversarial tests

* Deliberately coarsen the `Z`-scan step until sign changes are missed: the
  criterion must **fail** (`m < N_box`), not silently succeed.  Verified: with
  step `0.5` up to `T = 100` the scan finds fewer than 29 changes.
* Deliberately corrupt `theta` by `+pi`: `Z` flips sign globally, sign-change
  *count* is invariant — so this particular corruption is **not** caught by the
  count test.  It is caught by the `Im(Z) = 0` self-test.  Recorded here
  because it is a genuine blind spot of count-matching alone.
* Compare the certified ordinates against the classical list of low zeros
  (14.134725, 21.022040, 25.010858, 30.424876, 32.935062, ...): agreement to
  all certified digits.

## Remaining uncertainty

Low.  The one place a reviewer should push is the branch/normalisation of
`theta`, and the interaction between the abstention rule of L-0002 and the
`Im(rho) = T` edge case.

## Suggested next attack

* Extend `T` by replacing Euler-Maclaurin with a rigorous Riemann-Siegel
  expansion; the current cost per evaluation is `O(T)`.
* Add the **Turing method** so that `N_box` can be obtained from `S(t)`
  averages instead of a full contour, which is asymptotically much cheaper.
* Record the *deficit* `N_box - m` as a first-class research signal (see
  X-0004): a nonzero deficit at some height is the cheapest possible
  fingerprint of a counterexample.
