# O-108517 — The two-invariant phase diagram: Cheeger constant and frustration index exactly organize the breach sides

```text
Claim ID: O-108517
Status:   OBSERVATION over PROVED-per-instance certificates (all 45
          corpus rows exact: Sturm verdicts, exhaustive-subset Cheeger
          constants, exhaustive max-cut frustration indices; the
          separation statements are patterns over the stated corpus,
          not theorems)
Created:  2026-08-31 (pass 3 continuation, Lane 3; answers the
          two-invariant question deposited by O-108006/T-108514)
Programme: #763 (graph purity mechanisms)
Machine:  research/exploratory/2026-08-30-two-programme-pass/graphs/
          phase_diagram.py + phase_diagram.json (stdlib + core.exact;
          exact Fractions throughout)
Corpus:   45 graphs, n <= 22: the four capped-ladder families
          (k = 2..6, the O-108006 witness frames), all GP(n,k) with
          5 <= n <= 11, Moebius ladders M8/M10 (verdict spot-checks
          against cap_windows.json and the atlas agree everywhere)
RH status: RH and GRH are unproved; this claim does not address them.
```

## The two invariants (both exact per graph)

- `h(G) = min_{0<|S|<=n/2} e(S, S-bar)/|S|` — the edge-expansion
  (Cheeger) constant, exhaustive over all subsets;
- `f(G) = |E| - maxcut(G)` — the frustration index (minimum edge
  deletions to bipartiteness; f = 0 iff bipartite), exhaustive.

Verdicts RAM / POS / NEG / BOTH are Sturm-exact (cut 283/100 with the
census separation guard; guard-flagged spectra get adaptive rational
cuts — the two flagged cells reproduce the census's 706/707 verdicts).

## The exact corpus facts

1. **The expansion side is an h-dichotomy.** Every graph with a
   positive-end breach (POS or BOTH; 16 of 45) has `h <= 1/4`; every
   graph without one (RAM or NEG; 29 of 45) has `h >= 1/3`. NO corpus
   member has h in the open gap (1/4, 1/3). The positive-end breach
   is exactly the low-expansion stratum of this corpus.
2. **The entry side among breachers is an f-dichotomy.** Every
   non-Ramanujan corpus member with `f = 2` enters at the NEGATIVE
   end (GP(9,1), GP(11,1), M8, M10, crosscap-ladder k=2; and the
   crosscap family stays NEG-first as it goes BOTH), and every one
   with `f = 4` enters at the POSITIVE end (all eight POS rows; the
   708/709/706 families go BOTH only later). Frustration 2 vs 4
   PREDICTS the first breach side in every non-Ramanujan corpus row.
3. **All five NEG-only graphs have f = 2 exactly** — the negative-end
   breachers at small order are precisely two edge-deletions from
   bipartite, and their h stays >= 1/3 (their expansion is healthy;
   the breach is purely frustration-driven). Symmetrically, the
   positive-end families keep f CONSTANT (= 4) while h falls
   (1/3 -> 1/4 -> 1/5) as the corridor grows — the BOTH transition
   arrives not by rising frustration but by falling frustration
   DENSITY f/m (2/15 at entry, 2/33 at both-end), i.e. the corridor
   dilutes the odd cycles toward near-bipartiteness.
4. **Corridor arithmetic**: in the ladder families h is exactly
   2/floor(n/2) once a balanced 2-edge mid-corridor cut exists
   (1/4 at n = 16, 18; 1/5 at n = 20, 22), the discrete geometry
   behind O-108006's "parallel cross-sections" reading.

## Honest calibration against provable inequalities

The easy Cheeger direction for cubic graphs (`3 - lambda_2 <= 2h`)
would force a positive-end breach only at `h < (3 - 2 sqrt 2)/2 ~
0.0858`; the corpus threshold sits at h = 1/4 — three times larger.
So the h-dichotomy above is a corpus PATTERN strictly beyond what the
Cheeger inequality proves, deposited as a target: is there a
cubic-graph theorem "h <= 1/4 and (girth/frustration side condition)
implies lambda_2 > 2 sqrt 2" for a natural graph class? Conversely
the f = 2 vs f = 4 entry-side law is deposited as the sharpest open
pattern: does frustration index 2 FORBID positive-end entry
(equivalently, does every positive-end-only cubic graph need
f >= 3)? A counterexample search beyond this corpus is the next
campaign; the n = 16 census reps could settle it exhaustively at
minimal order.

## Scope caveats

45 graphs, n <= 22, from three structured families plus GP; no claim
of universality. GP(24,2)+ (T-108514's infinite family) is outside
the exhaustive-h range (2^47 subsets); its corridor structure
suggests h -> 0 along the family, consistent with fact 1, but that is
unverified reconnaissance, not a row.
```
