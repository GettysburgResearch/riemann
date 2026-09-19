# BCP26 — executed Sylvester-inspired cutoff-boundary research

**Proposed mathematics + reproducible finite checks. RH and GRH remain open.**

This is a substantive continuation of PR #903, stacked on the Newton
programme #848. It audits the earlier sketch, provides the previously
undefined energy kernel, tests the native source, proves that a tempting
positive-block estimate cannot work, and adds a concrete L-family adapter.
It does not claim that a new native upper bound has been proved.

## What changed

The earlier packet focused on `mu*e*e`. That error is identically zero on
the reconstructed square stage. The energy-bearing correction is `g*e`.
Splitting e by its least prime p and using the **actual inverse mu** gives
an exact cancellation:

```text
mu * e_p = -delta_p * b_(Y,p) * mu_<p,
b_(Y,p)(d) = mu(d) 1_(Y/p<d<=Y, every prime of d > p).
```

On the useful stage `g*e_p=mu*e_p`. Every output squarefree integer has a
unique cutoff-crossing prime pivot. Each channel has exactly the native
coefficient on its disjoint support; every nonsquarefree coefficient cancels.
This uses much more than balance, a coefficient cap, or an antichain.

The resulting cumulative functions are **not orthogonal**. Their complete
Gram and signed mean now feed exactly the existing completed Newton state,
with no omitted collar, integer endpoint, or mean-square price.

A proposed all-scale lower bound shows that the raw pivot diagonal is at
least order `Y/log^3 Y`, and its positive cross mass at least order
`Y^2/log^4 Y`, on the literal Möbius source. Even coprime semiprime pairs
supply such a positive sector. The earlier positive-excess programme
therefore needs a genuinely signed regrouping before applying bounds.
Mean-centering the individual rows does not remove this obstruction.

This is not a faster route to the answer by positive matrices. It is a
precise source-specific cancellation mechanism and a proof that one
natural subsequent inequality is the wrong one.

## Finite execution

Six full stages: Y=3,7,15,31,63,255. The largest includes every output
coefficient through 65,535, all 65,280 annular cells, 56 declared rows,
and all 1,596 upper-triangle Gram entries. Across all stages, 70,986
coefficient checks (overlaps counted) and 1,964 Gram entries are checked.

At Y=255, the raw-pivot decomposition gives approximately

```text
separate diagonal                 14.49227268648233
ordered cross covariance         -14.31242068297896
complete annular energy            0.17985200350337
positive ordered cross mass       29.81348728077207
negative ordered cross mass      -44.12590796375103
completed input A                   1.44418175180936
completed output A                  1.58757981507573
```

The JSON contains directed rational enclosures, not floating acceptance.
This raw diagonal is WORSE than the existing NSR26 prime-bank regrouping.
The finite experiments do not suggest advertising it as a norm improvement.
Its value is exposing the exact support and indispensable cancellation.

## L-family result

`LFAMILY.md` gives a rank-deflation adapter for #738, with the paper's CM
cubic-twist analytic-rank-one theorem explicitly imported. For a function
with known central order r, its negative-log-derivative Pick matrix obeys

```text
K_deflated = K_raw - r v v*,       v_i=1/z_i.
```

A synthetic exact test has raw value 4/3 but deflated value -8/3. The
central zero can mask a negative direction. The auxiliary-prime and
projector fixtures are checked exactly; no elliptic L-value or zero
computation is claimed.

## Reading and replay

1. `AUDIT.md`: why this replaces the earlier sketch rather than certifying it.
2. `PROOF.md`: full component proofs and the remaining signed estimate.
3. `EXPERIMENTS.md`: numerical results, controls and their interpretation.
4. `LFAMILY.md`: imported analytic theorem versus locally proved finite algebra.
5. `SOURCES.json` and `VALIDATION.md`: precise provenance and execution scope.

Run from this directory (Python standard library only):

```bash
python -S -B boundary.py --check result.json
python -S -B verify.py result.json
python -S -B lfamily.py --check lfamily_result.json
python -S -B -m unittest -v test_boundary
```

Repeat with `-O` as recorded in VALIDATION.md. The accepting checks do not
rely on Python assert statements. The verifier does not import the producer
or repository code. Both implementations and these proofs have one author;
this is not independent mathematical acceptance or Lean verification.

## Publication status

This packet was prepared in a session with working GitHub reads but no
available GitHub write action, and failed direct Git connectivity. It is
therefore delivered as an add-only repository patch, not represented as
already pushed. See `PUBLISH.md` in this directory for the exact target,
concurrency handling and proposed PR/issue comments. Existing PR #903's
remote head must not be confused with this new work.
