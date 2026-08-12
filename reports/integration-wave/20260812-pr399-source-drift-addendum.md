# PR #399 source-drift addendum

## Drift census

```text
initial theorem-review cutoff UTC:  2026-08-12T17:28:13Z
initial live head reviewed:          59b1d1773b0f1d98712d58b66f41202e5f221717
later drift census UTC:              2026-08-12T17:36:23Z
newer source head observed:          8d32d9b6353e8b18ec1786ad939803d4d606bf2c
relation:                            5 commits ahead, 0 behind
```

The five-commit delta adds only:

```text
claims/lemmas/L-91328-p61-forcing-has-a-uniform-one-rough-prime-margin.md
experiments/X-91117-p61-one-rough-prime-margin/README.md
experiments/X-91117-p61-one-rough-prime-margin/SHA256SUMS
experiments/X-91117-p61-one-rough-prime-margin/results/verification.json
experiments/X-91117-p61-one-rough-prime-margin/verify.py
```

No file containing the submitted transport-disintegration proof, the completed two-state matrices, the exact cascade counterexample, `L-91326`, or `L-91327` changed in this delta.

## Review of `L-91328`

### Statement

For the complete finite Boolean forcing through prime `61`, the theorem proposes directed exact normalized corridors

\[
F_1(x)>\frac3{40}\sqrt{x},
\qquad
F_2(x)>\frac9{100}\sqrt{x}
\qquad(x\ge67),
\]

and then proves that after one new least rough prime `p>=67`,

\[
F_{a;p}(x)>\frac3{50}\sqrt{x}
\qquad(a=1,2;\ x\ge p).
\]

### Verdict

```text
mathematical type:  ROUTE INFRASTRUCTURE / DIRECTED FINITE-BLOCK THEOREM
review verdict:     VERIFIED WITH FIXES
surviving scope:    one new least rough prime in one reset generation
```

The analytic reduction from the two normalized corridors to the `3/50` one-prime margin is exact:

\[
F_{a;p}(x)=F_a(x)-p^{-1/2}F_a(x/p),
\]

and the global upper corridor `F_a(y)<a\sqrt y` yields the loss `a\sqrt{x}/p`. The worst case `p=67` gives the displayed rational margins.

The retained checker uses exact integer/Fraction arithmetic and directed fixed-denominator inverse-square-root enclosures. It checks both endpoints of every activation cell meeting `x>=67`; the last unbounded cell is controlled by its finite endpoint and limiting coefficient. This is an appropriate proof object for the stated finite-block corridor. The checker was inspected but not rerun.

The qualification “WITH FIXES” reflects integration scope and proof provenance, not a detected sign error: the million-case directed certificate remains a retained external proof object and should be bound by its checksum and exact interpreter/environment in canonical extraction.

## Materiality to the full-proof verdict

The drift is **not material** to the decisive review verdict.

`L-91328` expressly states:

```text
distinct-prime scalar tensorization              NOT CLAIMED / REFUTED ELSEWHERE
positive four-state multiprime state             AVAILABLE
all-generation parity/endpoint ledger            OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```

It supplies useful one-prime margin inside one reset. It does not repair:

1. the exact false completed-cascade identity at `4981bcd...`;
2. the missing positive native source partition;
3. the real-column terminal proof gap;
4. the explicit recursive four-state parity/endpoint projection; or
5. the coefficient-one bounded-debt score recurrence.

Therefore the final dispositions remain:

```text
4981bcd... full proof proposal    FALSE AS SUBMITTED
8d32d9b... live descendant        UNPROVEN / GAP
L-91328 one-prime margin           VERIFIED WITH FIXES at stated scope
Riemann Hypothesis                 UNPROVEN
```
