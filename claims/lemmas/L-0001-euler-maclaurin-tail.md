```text
Claim ID:       L-0001
Title:          Explicit Euler-Maclaurin remainder bound for zeta on balls
Status:         PROVED
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   D-0001 (notation), classical Euler-Maclaurin summation
Scope:          All s with Re(s) + 2M + 1 > 0, s != 1; uniform over balls
Related counterexample candidates: prerequisite for every certified enclosure
                 used in Z-#### candidate files
```

## Statement

Let `M >= 0` and `N >= 1` be integers, let `B_k` denote the Bernoulli numbers
(`B_1 = -1/2`) and let `(s)_j = s(s+1)...(s+j-1)` be the rising factorial.
Write `sigma = Re(s)`.  For every `s != 1` with `sigma + 2M + 1 > 0`,

```
zeta(s) = sum_{n=1}^{N-1} n^{-s}
        + (1/2) N^{-s}
        + N^{1-s}/(s-1)
        + sum_{k=1}^{M} ( B_{2k} / (2k)! ) (s)_{2k-1} N^{-s-2k+1}
        + E_{M,N}(s),
```

and the remainder satisfies the explicit bound

```
|E_{M,N}(s)|  <=  |(s)_{2M+1}| * |B_{2M+2}|/(2M+2)! * N^{-sigma-2M-1}
                  * ( 1 + |s + 2M + 1| / (sigma + 2M + 1) ).            (L1)
```

**Uniform (ball) form.** Let `B = B(c, r)` be a closed complex ball with
`sigma_lo := Re(c) - r` and `sigma_lo + 2M + 1 > 0`. Then for every `s in B`,

```
|E_{M,N}(s)| <= P * |B_{2M+2}|/(2M+2)! * N^{-sigma_lo-2M-1} * (1 + A/(sigma_lo+2M+1))
```

where `P = prod_{j=0}^{2M} sup_{s in B} |s + j|` and
`A = sup_{s in B} |s + 2M + 1|`, both of which are bounded above by
`prod (|c+j| + r)` and `|c + 2M + 1| + r` respectively.

## Definitions

`zeta(s)` is the analytic continuation of `sum n^{-s}` (`Re s > 1`), with its
single simple pole at `s = 1` of residue `1`.  `B~_m(x) := B_m(x - floor(x))`
is the `m`-th periodic Bernoulli function.  A *ball* `B(c,r)` is the closed set
`{s : |s - c| <= r}`; enclosures are in the sense of Arb's `acb` type.

## Motivation

Every certified statement in this project — a certified zero count, a certified
zero-free rectangle, a certified sign of `Z(t)`, a certified enclosure of a
candidate off-critical zero — ultimately rests on being able to *bound*
`zeta(s)` over a *set*, not merely to evaluate it at a point.  (L1) is the
primitive that makes that possible without trusting any library's `zeta`.
It is deliberately proved here from scratch so that the project's rigorous
computations do not have a black box at the bottom.

## Proof

Apply Euler-Maclaurin summation to `f(x) = x^{-s}` on `[N, X]`, `X -> infinity`,
for `Re(s) > 1`; all terms below continue analytically to `sigma + 2M+1 > 0`,
`s != 1`, so the identity persists there by uniqueness of analytic
continuation (both sides are analytic in that region, the left by definition of
the continuation, the right because each displayed term is).

For `Re(s) > 1`, summation by parts / repeated integration by parts gives the
classical identity

```
sum_{n=N}^{infinity} n^{-s} = (1/2) N^{-s} + N^{1-s}/(s-1)
   + sum_{k=1}^{M} (B_{2k}/(2k)!) (s)_{2k-1} N^{-s-2k+1} + E_{M,N}(s),
```

with the exact remainder in integral form

```
E_{M,N}(s) = - ( (s)_{2M+1} / (2M+1)! ) * INT_N^infinity B~_{2M+1}(x) x^{-s-2M-1} dx.
                                                                        (L2)
```

(This is Euler-Maclaurin with the remainder taken after `2M+1` steps; see e.g.
Edwards, *Riemann's Zeta Function*, §6.4.  A self-contained derivation is:
repeatedly use `B~_{m}'(x) = m B~_{m-1}(x)` and integrate by parts, the boundary
terms at integers producing the `B_{2k}` sum because `B~_m(n) = B_m` and
`B_{2k+1} = 0` for `k >= 1`.)

It remains to bound (L2).  Integrate by parts once more, using
`B~_{2M+1}(x) = (1/(2M+2)) d/dx B~_{2M+2}(x)`:

```
INT_N^inf B~_{2M+1}(x) x^{-s-2M-1} dx
  = [ B~_{2M+2}(x) x^{-s-2M-1} / (2M+2) ]_{x=N}^{infinity}
    + ((s+2M+1)/(2M+2)) INT_N^inf B~_{2M+2}(x) x^{-s-2M-2} dx.
```

The boundary term at infinity vanishes because `B~_{2M+2}` is bounded and
`sigma + 2M + 1 > 0`.  At `x = N` (an integer) `B~_{2M+2}(N) = B_{2M+2}`.
Using the standard fact that for even index the periodic Bernoulli function
attains its maximum modulus at the integers,

```
|B~_{2M+2}(x)| <= |B_{2M+2}|   for all real x,
```

we obtain

```
| INT_N^inf B~_{2M+1}(x) x^{-s-2M-1} dx |
   <= (|B_{2M+2}|/(2M+2)) * [ N^{-sigma-2M-1}
        + |s+2M+1| * INT_N^inf x^{-sigma-2M-2} dx ]
   =  (|B_{2M+2}|/(2M+2)) * N^{-sigma-2M-1} * ( 1 + |s+2M+1|/(sigma+2M+1) ).
```

Substituting into (L2) and using `(2M+1)! * (2M+2) = (2M+2)!` gives (L1). ∎

The ball form follows because each factor in (L1) is bounded above by the
stated supremum over `B`, and `N >= 1` makes `N^{-sigma-2M-1}` decreasing in
`sigma`.

## Analytic domain audit

* `zeta` is analytic on `C \ {1}`; the representation is used only for
  `s != 1`.  The term `N^{1-s}/(s-1)` carries the pole.
* `N^{-s} := exp(-s log N)` with the **real** logarithm of the positive integer
  `N`; no branch ambiguity arises.  The implementation uses a cached rigorous
  enclosure of `log N` and `acb.exp`, so the branch is fixed by construction.
* No contour deformation is involved.
* The hypothesis `sigma + 2M + 1 > 0` is checked at run time on the *lower*
  bound of `Re(s)` over the ball; the code returns `+inf` (forcing a larger `M`)
  when it cannot be verified.

## Dependency audit

* Euler-Maclaurin summation formula with periodic Bernoulli remainder: used to
  obtain (L2).  Classical.
* `|B~_{2n}(x)| <= |B_{2n}|`: used once, in the final bound.  Classical
  (follows from the Fourier series `B~_{2n}(x) = (-1)^{n+1} 2 (2n)!
  sum_{k>=1} cos(2 pi k x)/(2 pi k)^{2n}`, whose terms are maximised in
  absolute value simultaneously at `x` integral).
* Analytic continuation / uniqueness: used to extend the identity from
  `Re s > 1` to `sigma + 2M + 1 > 0`.

## Gap audit

* **Not** a claim about `zeta'`; a separate bound is needed for the derivative
  (open, see OPEN_PROBLEMS Q-0002).
* The bound is weaker by the additive `1` than Edwards' sharper form; this is
  deliberate, since the sharper form's proof needs an extra estimate.  Using a
  *weaker* certified bound can never invalidate a certificate, only make it
  more expensive.
* Overestimation on wide balls is real: `P` grows like `r^{2M+1}` for large `r`,
  so the scheme must be used with adaptive subdivision (this is exactly what
  L-0002 does).
* The claim says nothing about the *cost* of achieving a given accuracy.
* Catastrophic cancellation: the main sum has `N` terms of comparable size for
  `s` on the critical line; ball arithmetic tracks the resulting precision loss
  automatically, so it cannot silently corrupt a certificate — it can only make
  the returned ball wide.

## Adversarial tests

Implemented in `tests/test_certzeta.py`:

1. Agreement with Arb's *independent* `acb.zeta` implementation (different
   algorithm — Riemann-Siegel / Borwein — and an independently written error
   analysis) at `s = 2, 3, 1/2+14.13i, 1/4+30i, 3/4+100.5i, 1/2+1000.25i,
   0.3-45.7i`: the enclosures must intersect (they do; in fact each contains
   the other's midpoint).
2. Exact special values: `zeta(2) = pi^2/6`, `zeta(4) = pi^4/90`,
   `zeta(-1) = -1/12`, `zeta(0) = -1/2` (the last two test the continuation
   region `sigma < 0`, where `M` must be large enough).
3. Ball input: the enclosure over `B(1/2 + 20i, 0.01)` must contain the point
   values at several interior points.
4. Functional equation `xi(s) = xi(1-s)` at random points — an end-to-end test
   that catches sign, factorial and rising-factorial indexing errors.  (This
   test in fact caught an off-by-one in the exponent `N^{-s-2k+1}` during
   development; see NEGATIVE_RESULTS R-0001.)
5. Monotone refinement: increasing `M` must shrink, never move, the enclosure.

## Remaining uncertainty

Low.  The proof is classical and the implementation is cross-checked against an
independent rigorous library.  The main risk is not the mathematics but a
transcription error in the code; test 4 above is specifically designed to be
sensitive to that class of error, and it was.

## Suggested next attack

* Prove the analogous bound for `zeta'(s)` (needed for interval-Newton /
  Krawczyk certification of *isolated* zeros, which is strictly stronger than
  the winding number: it yields uniqueness and a certified enclosure of the
  zero itself).  See Q-0002.
* Replace the main sum by a Riemann-Siegel expansion with rigorous remainder to
  make height `10^6+` feasible; the current cost is `O(T)` terms per evaluation.
