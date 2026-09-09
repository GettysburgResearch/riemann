# Adversarial verification wave — verdicts and disposition (2026-08-30)

Six skeptic agents (math + code lenses) reviewed the frozen claims.
Full verdicts: workflow wf_755727c9-97d journal. Disposition:

## Applied (code + proofs fixed, batteries re-run green)

- T-108002 FATAL: degree-2 purity completeness missing the trace-zero
  branch — FIXED in core/reconstruct.py; counterexample rows B10 added;
  claim + failure ledger updated (F-108002-2).
- T-108002 majors: traces mode inoperative (improper numerators) — FIXED
  in core/exact.minimal_rational_form + rows B11; A5 provably redundant —
  REDESIGNED (A1 certifies prefix, A5 predicts tail), B6 tightened;
  Ext^2 branch dead code — FIXED; A6 crash on high degree — FIXED.
- L-108001 majors: properness hypotheses added to (i)/(ii) with the
  refuting example recorded; (iii) parenthetical corrected.
- T-108500 major: Theorem 2's character-ring-exit inference repaired with
  the splitting-field argument (sqrt(a^2-b) not in Q(a,b)(sqrt(a^2-4b)));
  overclaim "odd powers >= 3 exit" reduced to the proved m=3 statement
  (m >= 4 conjectural); garbled draft fragments cleaned.
- T-108501 major: quaternionic slice paragraph corrected (C[s] is
  isomorphic to C x C inside M_2(C); the series lies in R[s]; spectrum
  defined via the minimal polynomial in the noncommutative case).
- X-108002 B3: the original "structureless" row was eventually periodic
  (genuinely finite-rank — correctly certified by the improved detector);
  replaced by the primes, lesson recorded.

## Minors — APPLIED in the 2026-08-31 continuation pass (every item below
   is now fixed in place; list retained as the record of what changed)

- T-108500 Lemma 4: state Zariski-density of the distinct-nonzero-roots
  locus explicitly and either weaken the degenerate-case conclusion to the
  degree bound or add the coefficient-level Zariski argument for the
  divisibility clause (the claim-file summary already asserts only the
  degree bound, so nothing downstream is affected).
- PROOF.md Theorem 3 parenthetical: reword "recorded in matrix/defects.json
  runs" to claim only the (0,7) instantiation checks (explicit higher-m
  degeneration rows are not emitted).
- defect_powers_run.py: restrict the symbolic series check to the
  tail-vanishing part (the head comparison is definitional); delete dead
  e_list code; align "m <= 5"/"m <= 6" wording and statement numbering.
- T-108501/X-108501 C4: replace the vacuous floating corroboration with a
  genuine dual-number-arithmetic path (or delete C4); add the one-sentence
  continuation-uniqueness remark to consequence (3); soften Definition 1's
  "every hypercomplex zeta" remark to "every series/functional-calculus
  hypercomplex zeta".
- X-108505 V4: strengthen the palindromicity refutation to the any-scale
  test (the any-scale statement is true — j=1 forces scale 6 while j=3
  forces scale^3 = 81 — but the deposited check tests one scale).
- X-108506 W4/W5: make W4 compute the pure-case modulus from N_3's
  coefficients per prime; derive W5's m=2 defect from the actual squared
  series (both facts are true and independently re-derived by the skeptic;
  the deposited checks are weaker than the prose).
- O-108506 wording: align the Sato-Tate label between Status and Reading
  (it is a theorem for non-CM curves, used as a labelled external input);
  "the prime set" -> "the set of good primes".
- T-108002: the checkpoint report's "10 exact checks" is now 14.

RH status: unproved; nothing in this ledger bears on it.
