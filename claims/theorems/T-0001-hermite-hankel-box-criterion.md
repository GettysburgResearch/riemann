```text
Claim ID:       T-0001
Title:          Hermite-Hankel box criterion: a finite algebraic witness for an
                off-critical zero
Status:         PROVED  (mathematics)  /  EMPIRICAL (the numerical sensitivity claims)
Authoring agent: claude-01
Reviewing agents: (none yet -- this is exactly the kind of claim the README says
                 must not be trusted until independently reconstructed)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001, L-0006 (Taylor-model enclosures), argument principle,
                Hermite's theorem on Hankel forms of a real polynomial
Scope:          Any rectangle D symmetric about the critical line with
                xi (equivalently eta) nonvanishing on dD
Related counterexample candidates: provides the acceptance test for a whole
                CLASS of candidates: "an off-critical zero somewhere in D",
                without needing to localise it first
```

## Statement

Let `D = [1/2 - a, 1/2 + a] x [c - r, c + r]` with `a, r > 0` and `c > r > 0`,
and let `eta(s) = (s-1) zeta(s)`.  Assume `eta` has no zero on `dD`.  Let
`rho_1, ..., rho_N` be the zeros of `eta` in the interior of `D`, listed with
multiplicity, and set

```
w_j = (rho_j - 1/2 - i c) / (i r) ,        q_k = sum_{j=1}^{N} w_j^k .
```

Then:

**(a)  Computability.**  For every `k >= 0`,

```
q_k = (1/(2 pi i)) INT_{dD} ((s - 1/2 - i c)/(i r))^k (eta'/eta)(s) ds ,
```

so all `q_k` are computable by certified quadrature from `eta` and `eta'` on
`dD` alone -- no knowledge of the zeros is needed.

**(b)  Reality.**  Every `q_k` is real.

**(c)  Criterion.**  Let `H_m = (q_{i+j})_{0 <= i,j <= m-1}` for `m >= N`
(entries `q_0, ..., q_{2m-2}`; note `q_0 = N`).  Then

```
every zero of zeta in D lies on the critical line
        <==>   H_N is positive semidefinite.
```

**(d)  Witness.**  Consequently, a certified **negative** leading principal
minor of `H_N` is a finite, machine-checkable proof that `zeta` has a zero in
`D` off the critical line -- i.e. a counterexample to the Riemann hypothesis.
Symmetrically, a certified positive definite `H_N` proves RH inside `D`.

**(e)  Discriminant form.**  If the `N` zeros are distinct then

```
det H_N = prod_{i<j} (w_i - w_j)^2 = discriminant of prod_j (X - w_j),
```

so `det H_N < 0` already witnesses an *odd* number of off-critical conjugate
pairs in `D`.  This is the cheapest single-number version of (d).

## Definitions

`w(s) = (s - 1/2 - ic)/(ir)` is the affine map sending the critical-line
segment `{1/2 + it : |t - c| <= r}` onto the real interval `[-1, 1]`, and
sending `D` onto the rectangle `[-1,1] x [-a/r, a/r]` in the `w`-plane.  All
matrices are real symmetric; "positive semidefinite" is meant in the usual
sense.  A "certified" minor is an interval enclosure not containing `0` and of
known sign.

## Motivation

Both existing certified tools in this repository need the counterexample to be
*already localised*:

* L-0002 (winding number) can only certify a zero off the line if you hand it a
  rectangle that is **disjoint from the critical line**, so it can only see
  displacements larger than the rectangle's separation;
* L-0004 (count matching) detects a failure only as a *deficit* between two
  counts, and then tells you nothing about where or how big it is.

T-0001 removes that restriction.  Its box **straddles** the critical line, so
an off-line zero at any displacement `delta > 0` -- however small -- is inside
the box, and the criterion is exact for every `delta > 0`.  What degrades as
`delta -> 0` is not the criterion but the *numerical effort* needed to resolve
its verdict: by (e) the signal scales like `(delta/r)^2`.  That is a much
gentler failure mode than "the method cannot see it at all", and it converts
the counterexample hunt into a question about quadrature accuracy, which is a
resource question rather than a structural one.

## Proof

**(a)** `eta` is entire (the pole of `zeta` at `s=1` is cancelled), and
`eta'/eta` is meromorphic with simple poles exactly at the zeros of `eta`, the
residue at a zero of multiplicity `m` being `m`.  The map `s -> w(s)` is affine
hence holomorphic, so `w(s)^k eta'(s)/eta(s)` is meromorphic on a neighbourhood
of `D` with poles only at the `rho_j`, and the residue at `rho_j` is
`w(rho_j)^k = w_j^k`.  Since `eta` has no zero on `dD`, the residue theorem
applies and gives (a).  (A zero of multiplicity `m` contributes `m` equal terms,
matching the "with multiplicity" convention.)

**(b)** The zero multiset of `eta` inside `D` is invariant under the reflection
`s -> 1 - conj(s)` across the critical line: this is the functional equation
`xi(s) = xi(1-s)` combined with `xi(conj s) = conj(xi(s))`, plus the fact that
`D` is symmetric about the critical line and lies in the upper half plane, so
the reflection maps `D` onto itself.  In the `w` coordinate the reflection is
`w -> conj(w)`:  writing `s = 1/2 + i c + i r w`, we get
`1 - conj(s) = 1/2 + i c + i r conj(w)`.  Hence the multiset `{w_j}` is closed
under conjugation, so each power sum `q_k = sum_j w_j^k` is invariant under
conjugation and therefore real.

**(c)** By (b) the monic polynomial `P(X) = prod_j (X - w_j)` has real
coefficients (its coefficients are, up to sign, the elementary symmetric
functions of a conjugation-closed multiset).  Hermite's theorem for a real
polynomial `P` of degree `N` with power sums `q_k` states that the real
symmetric Hankel form `H_N = (q_{i+j})` has

```
rank H_N      = number of DISTINCT roots of P,
signature H_N = (#distinct real roots) - (#distinct non-real conjugate pairs).
```

If every zero of `zeta` in `D` is on the critical line then every `w_j` is
real, so writing `v_j = (1, w_j, ..., w_j^{N-1})^T in R^N` we get
`H_N = sum_j v_j v_j^T`, manifestly positive semidefinite.

Conversely suppose some zero is off the critical line, i.e. some `w_j` is
non-real.  Then `P` has at least one non-real conjugate pair among its distinct
roots, so `signature H_N < rank H_N`, which forces `H_N` to have at least one
negative eigenvalue; hence `H_N` is not positive semidefinite.  This proves the
equivalence.

**(d)** Immediate from (c): a symmetric matrix with a negative leading
principal minor is not positive semidefinite, and every step of the computation
is an interval enclosure, so a certified negative minor is a proof.  (The
existence of the zeros themselves is part of (a): `q_0 = N` counts them.)

**(e)** For distinct `w_j`, `H_N = V^T V` with `V` the Vandermonde matrix
`V_{kj} = w_j^k`, so `det H_N = (det V)^2 = prod_{i<j}(w_i - w_j)^2`, the
discriminant.  For real `w_j` every factor is a positive real; for a single
non-real conjugate pair `w = alpha +- i beta` the corresponding factor is
`(2 i beta)^2 = -4 beta^2 < 0` while all other factors pair up into positive
reals (a factor `(w_i - w_j)` and its conjugate partner multiply to a modulus
squared).  Hence one pair flips the sign; an even number of pairs does not. ∎

## Analytic domain audit

* `eta(s) = (s-1) zeta(s)` is entire.  Using `eta` instead of `xi` deliberately
  avoids `Gamma(s/2+1)`: the Gamma factor is zero-free and so changes nothing in
  the criterion, but its ball enclosure is the widest ingredient of `xi` and it
  would dominate the numerical error.  `pi^{-s/2}` likewise.
* `eta'/eta` has poles exactly at the zeros of `eta`.  In the closed strip with
  `Im s > 0`, the zeros of `eta` are exactly the nontrivial zeros of `zeta`
  (`s = 1` is not a zero: `eta(1) = 1`).  So no trivial zero and no pole can
  enter `D`, which is required for the residue count to mean what we claim.
* No branch cuts: the integrand uses no logarithm and no fractional power.
  `w(s)^k` is a polynomial in `s`.  This is a real advantage over the winding
  number of L-0002, whose correctness argument is entirely about branches.
* The contour is `dD`, traversed positively; no deformation is performed.
* The residue theorem needs `eta` nonvanishing on `dD`; the implementation
  certifies this by enclosing `eta` on balls covering `dD` and checking
  `0` is excluded, and **abstains** otherwise.

## Dependency audit

* Residue theorem: used in (a).
* Functional equation `xi(s) = xi(1-s)` and the reflection principle
  `xi(conj s) = conj(xi(s))`: used in (b) only, to get reality of `q_k`.
  Neither is RH-dependent.
* Hermite's theorem on Hankel forms of a real polynomial: used in (c).  This is
  the one classical input not reproved here.  It is a statement of real
  algebra, entirely independent of zeta.
* Vandermonde/discriminant identity: used in (e).
* L-0001/L-0006 for the certified enclosures of `eta`, `eta'`.

## Gap audit

Deliberate search for the standard failure modes:

* **Approximate zero vs. proved zero.**  Not applicable in the dangerous
  direction: the witness in (d) is a *sign*, and a sign certified by interval
  arithmetic is a proof.  But note carefully what (d) proves: it proves that
  **some** zero in `D` is off the line.  It does **not** localise it, does not
  bound `delta`, and does not prove the zero is simple.  A candidate file
  claiming more than that is overclaiming.
* **Nontriviality.**  Automatic: `D` lies in `0 < Re s < 1`, `Im s > 0`, where
  every zero of `eta` is a nontrivial zero of `zeta`.  This must be re-checked
  if anyone ever runs the criterion on a box reaching outside the strip.
* **Enclosure still intersecting the critical line.**  Not applicable: the
  criterion never needs the region to avoid the line.  This is the point of it.
* **Parity blindness of (e).**  `det H_N < 0` detects an odd number of
  off-critical conjugate pairs.  Two off-line pairs in the same box give a
  positive determinant.  The full PSD test (c) has no such blindness; only the
  cheap determinant shortcut (e) does.  **Any agent using (e) alone must
  subdivide `D` before concluding "no off-line zeros".**
* **Multiplicity/degeneracy.**  If two zeros coincide, `H_N` is singular and
  `rank H_N < N`; the criterion is then PSD-but-not-PD.  The implementation
  reports `UNDECIDED` in that situation rather than guessing.  A repeated zero
  on the critical line is thus indistinguishable, by this test alone, from a
  numerically unresolved pair -- correctly so.
* **Quadrature error.**  Fully accounted: the composite Gauss-2 rule carries a
  certified Cauchy remainder, and the remainder is added into the enclosure of
  every `q_k`.  If the effort is insufficient the pivots straddle zero and the
  verdict is `UNDECIDED`.  There is no configuration in which insufficient
  effort yields a false `PD` or a false `NOT_PSD`.
* **Conditioning.**  `H_N` is a Hankel matrix; these are notoriously
  ill-conditioned as `N` grows, and the normalisation `|w_j| <= ~1` is what
  keeps it usable.  Expect the practical limit to be `N` of order 10-30 per
  box, i.e. boxes of height a few tens near `t ~ 100`.  Subdivide rather than
  enlarge.
* **Circularity.**  None: nothing in the proof uses RH, and the numerics use
  no zero locations as input.
* **"Independent implementations differ" trap.**  Where X-0001 (winding + sign
  changes) and X-0002 (moments) both apply, they must agree; a disagreement is
  a bug hunt, not a discovery.  Both currently agree on every box tested.

## Adversarial tests (all in experiments/X-0002, part 2)

The decisive test of a *detector* is that it fires.  On synthetic polynomials
with deliberately planted off-critical pairs at displacement `delta`, at
quadrature effort `nsub = 32`:

```
planted delta   verdict
--------------  ---------------------------------------------
none            PD          (correct: no false positive)
0.1             NOT_PSD     (correct: certified witness produced)
0.03            UNDECIDED   (honest abstention)
0.01            UNDECIDED
0.003           UNDECIDED
```

The `UNDECIDED` boundary sits where the `(delta/r)^2` signal of (e) drops below
the certified quadrature error, exactly as the theory predicts.  Raising the
effort moves the boundary down; it does not change any verdict from `PD` to
`NOT_PSD` or back.

On `zeta` itself the four boxes tested
(`[0.2,0.8]x[12,23]`, `[0.2,0.8]x[23,29]`, `[0.2,0.8]x[12,35]`,
`[0.25,0.75]x[36,48]`) all return `PD` with `N = 2, 1, 5, 3`, agreeing with the
independent counts of X-0001.

## Remaining uncertainty

* The mathematics of (a)-(e) I regard as solid; the step most worth an
  independent reconstruction is (b), because reality of `q_k` is what licenses
  treating `H_N` as a real symmetric matrix, and it silently uses the fact that
  `D` is symmetric about the critical line.  **If a later agent runs this on a
  box that is not symmetric about the line, (b) fails and the whole criterion
  is void.**  The implementation checks that each `q_k` has an imaginary part
  enclosing `0` and aborts otherwise; that check is a safety net, not a proof.
* The sensitivity claim "signal `~ (delta/r)^2`" is asymptotic and empirical
  here, not proved as a theorem with constants.  See Q-0006.
* I have not searched the literature; the moment step is certainly the
  classical Delves-Lyness method and the algebra is classical Hermite theory.
  The combination may well be known.  Nothing in this file should be described
  as new mathematics.  What is new *to this repository* is that it is
  implemented, certified, and wired to a counterexample search.

## Suggested next attack

1. **Push the sensitivity.**  Quadrature error falls like `nsub^{-4}`, and the
   signal falls like `delta^2`, so the smallest certifiable displacement scales
   like `nsub^{-2}`.  Doubling the effort quarters the detectable `delta`.
   Measure the constant, then decide whether `delta ~ 10^{-6}` is reachable at
   heights where the zeros are well separated.
2. **Use (e), not (c), for a first sweep**: one determinant per box, with
   subdivision to defeat the parity blindness.
3. **Combine with X-0004**: run the criterion on the boxes around the tightest
   Lehmer pairs first.  Those are the boxes where the `w_j` are closest to
   colliding, hence where `det H_N` is smallest, hence where a small
   perturbation off the line is *most* visible relative to the on-line signal.
   That is the natural marriage of the two experiments and it is the single
   most promising concrete next step in this repository.
4. Prove the sensitivity statement of Q-0006 properly, with explicit constants,
   turning "raise the effort" into a computable budget for a target `delta`.
