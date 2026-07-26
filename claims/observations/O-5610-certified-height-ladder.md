# O-5610 — A certified height ladder: `D = 0` at `10^{13}` and `10^{14}`

Claim ID: O-5610
Title: Unconditional `D = N - N_0 = 0` certificates at `t = 10^{13}` (999 units,
4467 zeros) and `t = 10^{14}` (50 units, 242 zeros), at `~0.3` s per zero
Status: CERTIFIED-COMPUTATION
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-26
Last updated: 2026-07-26
Dependencies: X-5604; FLINT/Arb as an external implementation, audited in
`O-5611`
Scope: the slabs listed below
Related counterexample candidates: none — this is a capability result

## What was done

`O-5608` closed one `40`-unit window at `4.7\times10^{12}`.  This claim reports
the same predicate run as a *ladder*, to establish how high it reaches and what
it costs.

```text
t          slab                                    span   N     N_0   D   time
1e13       (10000000000000.5, 10000000000999.5)     999   4467  4467  0   21 min
1e14       (100000000000000.5, 100000000000050.5)    50    242   242  0   10 min
```

Both are **unconditional**: `N` from Arb's `zeta_nzeros` as a ball of radius
zero; `N_0` from certified sign changes of `Z`, every sign an Arb ball strictly
on one side of zero; `0` undecided samples in either run.  No bound on
`\int S`, no conjecture, no floating-point sign decision, no Riemann–Siegel
remainder estimate.

Every zero in those slabs is on the critical line **and simple** — `N` counts
with multiplicity, and simple sign changes exhaust it.

## The honest framing, which matters here

These are **spot certificates at great height, not an extension of the verified
frontier.**  Platt–Trudgian verified RH *exhaustively* up to
`3.0000175\times10^{12}`; below `10^{15}` there are of order `10^{16}` zeros, and
nothing here touches all of them.  What the ladder shows is that a *specific*
stretch of the critical line, arbitrarily far up, can be certified cheaply and
unconditionally — which is a different and much weaker statement than extending
the exhaustive frontier, and must not be confused with it.

That said, the two heights above are `3.3` and `33` times the exhaustive
frontier, and the counting primitive alone reaches further:

```text
N(1e13) = 43124192297102       20.3 s
N(1e14) = 467888702914983      39.9 s
N(1e15) = 5045354828589535    173.3 s
```

so `333\times` the frontier for the count.  Counting is cheap; the sign pass is
what sets the practical limit.

## Cost model

```text
             N (both endpoints)   sign pass          per zero
t = 1e13     50 s                 4468 samples       0.281 s
t = 1e14     90 s                  454 samples       1.1 s
t = 1e15     443 s                    -              -
```

The sign pass dominates and scales like `\sqrt{t}`, because each `Z` evaluation
costs a Riemann–Siegel main sum of `\sqrt{t/2\pi}` terms.  Two engineering
choices carried it:

1. **Adaptive precision.**  All `4468` samples at `t = 10^{13}` decided at `64`
   bits; the escalation ladder never fired, because `|Z|` is `O(1)` while the
   `64`-bit ball radius is `~3\times10^{-3}`.  Against `192` bits throughout,
   that is `0.281` s per sample instead of `0.61`.
2. **Gram placement.**  `certify_gram.py` needs no scanner at all: samples go at
   Gram points, and where Gram's law fails the interval is bisected adaptively.
   At `t = 10^{14}` Gram's law delivered `171` of `242` zeros (`71\%`) and one
   refinement round closed the rest.  Nothing about Gram's law is assumed — it
   chooses where to look, and a failure costs evaluations, never correctness.

A design question settled by measurement, recorded so it is not re-run: getting
`N_0` from a library zero-finder instead is **56 times slower**.
`acb.zeta_zeros` at index `4.3\times10^{13}` costs `32.2` s for one zero and
`79.1` s for four — `15.7` s marginal — because it isolates each ordinate to
high precision, when a *sign* is all the predicate needs.

## A precision trap, found the hard way

The first `t = 10^{15}` attempt returned `N_0 \ge 43` against `N = 52` and
stalled.  The cause was that sample positions were being routed through
binary64, and at `10^{15}` a `double` has `ulp = 0.125` against a mean zero
spacing of `0.188` — so the refinement's new points collapsed onto the old ones.

This is the *same* defect an external review had already found in `rs_zeta.c`'s
zero emitter (see the correction in `O-5604`), reappearing in different code.
Sample placement is now exact-rational end to end.

Two further notes, because the failure mode is instructive:

- **Correctness was never at risk.**  A coarse sample position is not a wrong
  answer; the sign certified *at* that position is still certified.  The run
  reported `D \le 9`, not `D = 0`, and refused to conclude.  That is the
  fail-closed design working as intended.
- Fixing the placement then exposed a second bug: an exact dyadic at
  `t = 10^{15}` with `24` fractional bits needs `74` bits to represent, above
  the first ladder rung, and the code returned "not exact" instead of escalating.
  The starting precision is now derived from the sample's bit length.

## Limitations

1. **Spot certificates, not exhaustive verification.**  See above.  The claim is
   about specific slabs.
2. `N` rests on Arb's `zeta_nzeros`, an external implementation.  `O-5611`
   audits it against an independent route.
3. The `t = 10^{14}` certificate was produced before the placement fix, with
   coarser sample positions.  It stands — `0` samples were undecided and `242`
   alternations were certified — but it would be reproduced with different
   sample points today.
4. Slab endpoints are half-integers, chosen to be exactly representable and
   unlikely to sit near a zero.  Endpoints *near* a zero are dramatically more
   expensive; see the cost anomaly in `O-5608`.

## Reproduction

```bash
cd experiments/X-5604-exact-slab-discrepancy
python3 certify_height.py --t0 10000000000000     --span 999 --tag 1e13
python3 certify_height.py --t0 100000000000000    --span 50  --tag 1e14
```

## Suggested next attack

The sign pass costs `\sqrt{t}` per zero and that is the whole story.  Arb's
Platt entry points (`acb_dirichlet_platt_local_hardy_z_zeros` and friends) are
all exported from the bundled `libflint` and reachable by `ctypes`; they
evaluate `Z` on a whole block by FFT rather than one point at a time, which is
the only known way to beat the per-point cost.  Whether that beats `0.28` s per
zero in practice is untested — the one measurement made here, of the *zero
finder* built on it, went the wrong way by `56\times`.
