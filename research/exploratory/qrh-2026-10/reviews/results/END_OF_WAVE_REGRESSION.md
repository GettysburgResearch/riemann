# End-of-wave regression rerun (10 Oct 2026, 22:20-22:30 UTC)

```text
Status: TOOLING record. No mathematical claim beyond "these scripts still produce their recorded
  verdicts at this commit".
Scope: the exact-check scripts added in the last part of the wave, rerun at HEAD after all
  red-team edits. paper.tex was re-extracted from ref 31c706bb (sha256 prefix 42a5ee0febca59fd).
Exact sources or dependencies: the scripts listed below, at the commit containing this file
What was actually run: each script with `python3 -I`; outputs went to session scratch, so the
  committed results files were not changed (two that the scripts rewrite were restored with git)
Smallest remaining gap: none of these reruns is independent of the scripts' own authors; they
  only show that the recorded verdicts reproduce
```

| script | recorded verdict | rerun | time |
|---|---|---|---|
| reviews/part1_free_checks.py (with `--replay-junction`) | 32/32 gates, 10/10 controls | 32/32, 10/10; J1 fails only P2 as designed | 65 s |
| proposed/PART1_FREE_7_8/remark_19_3_checks.py (without `--lean`) | 43/43 with the Lean group | 39/39 gates, 13/13 controls; Lean group skipped | 1 s |
| reviews/cubic_allocation_loss.py | 56/56 | 56/56 | 10 s |
| reviews/cubic_hb_checks.py | 27/27 | exit 0, all PASS | 1 s |
| proposed/CUBIC_FOURTH_MOMENT/lemmas_4bcd_gh_checks.py | 18/18 | 18/18 | 59 s |
| proposed/CUBIC_FOURTH_MOMENT/lf_theta_third_checks.py | 14/14 | 14/14 | 1 s |
| proposed/CUBIC_FOURTH_MOMENT/a4_checks.py | 5/5 | exit 0, all PASS | 1 s |
| proposed/CUBIC_FOURTH_MOMENT/lemma_4i_checks.py | 6/6 | exit 0, all PASS | 2 s |
| proposed/CUBIC_FOURTH_MOMENT/lemma_4k_checks.py | 10/10 | 10/10 | 44 s |
| scripts/detector_density.py | 21/21 gates, 5/5 controls | 21/21, 5/5 | 48 s |
| scripts/explicit_pnt_7_8.py (without `--zeros`) | constants as in EXPLICIT_PNT_7_8.md | same constants; the optional float zero sum section omitted | 15 s |
| reviews/cubic_profile_uniformity.py | 26/27 (one explained FAIL) | 26/27 | 18 s |
| reviews/theta_row_ledger.py | 19/19 | 19/19 | 18 s |
| reviews/hecke_lean_fidelity.py | reading cross-checks | exit 0; trivial-character residue matches the class number formula | 6 s |
| reviews/sep30_l42_44_checks.py | 65/65 | 65/65 | 49 s |

Separately, every relative link in the folder's markdown files resolves: 376 links. One
regex hit, at SEP30_SEC4_REVIEW.md:137, is a formula, not a link.

Lean provenance check (22:28 UTC):
* `lean/*.lean` and the two strip challenges are byte-identical to the copies that were built and
  comparator-checked.
* The explicit-Siegel challenge differed only by a docstring caveat added after its first run.
  It was copied over and re-run with both kernels: accepted, 1188s.
* `checks/CorollaryAxioms.lean` re-run at HEAD: all seven `#print axioms` lines show only
  `[propext, Classical.choice, Quot.sound]`.
