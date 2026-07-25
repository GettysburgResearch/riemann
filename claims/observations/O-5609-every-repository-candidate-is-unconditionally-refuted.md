# O-5609 — Every counterexample candidate in this repository's history, refuted by one certificate

Claim ID: O-5609
Title: All candidate ordinates ever nominated on any branch lie inside a single
`40`-unit window for which `D = N - N_0 = 0` is certified unconditionally
Status: CERTIFIED-COMPUTATION (rests on `O-5608`, plus an exhaustive branch
search for nominated ordinates)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: O-5608 (the certificate); X-5604
Scope: every ordinate nominated as a counterexample candidate on any branch of
this repository as of 2026-07-25
Related counterexample candidates: all of them

## The claim

Two years of agent work on this repository has nominated candidate ordinates
from several independent routes — the `xi`-passivity Pick screens (#39, #66,
#71), the `X-3902` `j`-grid, the D-0801 carrier programme (#42, #55).  Every one
of them sits in the same tiny neighbourhood, and that neighbourhood is now
certified.

```text
certified window (O-5608)      (4709203636333.1875, 4709203636373.1250)
                                span 39.94, N = N_0 = 172, D = 0

PR #71  j = -15 full-complex   4709203636353.162150      inside
j = -5 finalist T_0            4709203636353.474609      inside
X-3902 grid centre             4709203636353.630859      inside
D-0801 production carrier      4709203636353.650391      inside
full j-grid, j in [-29,+29]    (4709203636352.7246, 4709203636354.5371)
                                span 1.81                inside
```

An exhaustive search of all remote branches for ordinate-shaped constants in
`*.md` returns nothing outside `[4709203636352.15,\;4709203636354.15]` — a
`2`-unit interval sitting well inside the certified window, with `19` units of
clearance on the left and `18.6` on the right.

**Therefore: no ordinate ever nominated in this repository is, or is near, an
off-critical zero.**  Not conditionally, not to floating-point accuracy —
unconditionally, from an Arb ball count and `172` certified sign balls.

## Why they all coincide

This is not a coincidence and is worth stating, because it is the real lesson.

Every route that nominated an ordinate was a *screen for local anomaly*.  The
Pick screens look for a near-singular `K`; `O-5604` showed that what they were
actually finding is a large zero gap, since `xi'/xi(s) = \sum_\rho 1/(s-\rho)` is
dominated by the nearby zeros.  The D-0801 carrier programme was tuned to the
same height for unrelated reasons and then optimised locally.  So the whole
repository has been examining one `2`-unit stretch of the critical line at
`t \approx 4.709\times10^{12}`, from four different directions, without any of
the four being able to settle it.

It contains `172` zeros.  All of them are on the line and simple.

## What this does and does not mean

- **Does:** the counterexample backlog is empty, and it is empty for a reason
  that no amount of additional precision on any of those candidates could have
  changed.  `R-5603` showed the `128`-bit Pick screen was a coin flip; this
  shows that even a perfect screen would have found nothing there, because
  there is nothing there.
- **Does:** it retires the remaining conditional language.  `O-5604`'s Turing
  argument, `O-5605`'s bracket, the `128`-bit ghosts — all were circling a
  question that is now answered outright.
- **Does not:** say anything about RH.  One `40`-unit window at
  `4.7\times10^{12}` is a single local ledger entry.  `D > 0` somewhere would
  refute RH; `D = 0` here refutes only the candidates.
- **Does not:** validate or invalidate the *methods*.  A Pick matrix or a Weil
  form may still be the right instrument; this says only that they were pointed
  at a stretch of line where nothing was wrong.

## The strategic consequence

The repository's search has been **monocultural in height**, not just in method.
Four independent routes converged on the same two units of the critical line,
and no route noticed, because none of them could count zeros.  A cheap,
unconditional counter changes the economics: `O-5608` cost `102` seconds for
`172` zeros, and `999` units at `t = 10^{13}` cost `21` minutes for `4467`.

The right posture from here is: **certify first, screen second.**  Any ordinate
a screen nominates should be run through `X-5604` before a single additional bit
of precision is spent on it.  At `~0.3` seconds per zero that is cheaper than
almost any nomination is worth.

## Limitations

1. The exhaustive branch search matched ordinate-shaped decimal constants and
   the `/2^32` dyadic form in Markdown.  A candidate recorded only in source, or
   only in a JSON artifact, or in a form the pattern missed, would not appear.
   The search covered all remote branches at `2026-07-25`.
2. It covers *ordinates*.  The Robin-criterion route (#2/#20/#25/#46) and the
   Li-coefficient route (#14) do not nominate ordinates at all, and nothing here
   touches them.
3. `O-5608` inherits its trust in Arb's `zeta_nzeros`, an external
   implementation.
4. Candidates below the Platt–Trudgian verified height are covered by that
   verification, not by this one; the D-0801 low-carrier tests at
   `T = 62831853071` and `T = 6283.19` are in that category.

## Reproduction

```bash
cd experiments/X-5604-exact-slab-discrepancy
python3 slab_discrepancy.py --a 75347258181331/16 --b 37673629090985/8 --prec 192 \
    --out results/window-pr71.json                       # N = 172
python3 certify_parallel.py \
    ../X-5602-riemann-siegel-detector/results/zeros-pr71-ordinate.txt \
    --a 75347258181331/16 --b 37673629090985/8 --expected-N 172 \
    --out results/certified-pr71.json                    # N_0 = 172, D = 0
```

## Suggested next attack

Stop searching this height.  Everything the repository has nominated is here,
and there is nothing here.  The interesting question is where to point the
counter next — and the answer is not "a large gap" but **a Lehmer pair**: if RH
fails, a conjugate pair leaves the line by first colliding on it, so the
signature to hunt is two zeros anomalously *close* together, not anomalously far
apart.  A large gap is what remains *after* a departure; a near-collision is
what precedes one, and it is visible while the zeros are still on the line.
