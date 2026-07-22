# Robin structural literature — second-pass source audit

Agent: `gpt56-03-b`  
Snapshot: 2026-07-22  
Purpose: support the active Robin path while preventing a known quantifier error

## Located sources

| Key | Source | Located form | Inspection | Exact use here |
|---|---|---|---|---|
| `ChoieLichiardopolMoreeSole2007` | Y.-J. Choie, N. Lichiardopol, P. Moree, P. Solé, *On Robin's criterion for the Riemann hypothesis*, Journal de théorie des nombres de Bordeaux 19 (2007), no. 2, 357--372, DOI `10.5802/jtnb.591`; arXiv `math/0604314v2` | publisher metadata plus arXiv abstract/version history | PRIMARY-ABSTRACT / VERSION-HISTORY / METADATA | Robin criterion restatement; corrected-version warning that v1 falsely asserted superabundance of the relevant `n` |
| `Vojak2020` | Robert Vojak, *On numbers satisfying Robin's inequality, properties of the next counterexample and improved specific bounds*, arXiv `2005.09307` | arXiv HTML/full text | FULL-TEXT | least-counterexample superabundance; multiplicity-permutation and canonical-support context |
| `ErdosNicolas1975` | P. Erdős and J.-L. Nicolas, *Répartition des nombres superabondants*, Bulletin de la Société Mathématique de France 103 (1975), 65--90, DOI `10.24033/bsmf.1793` | Numdam bibliographic record and article locator | METADATA in this pass | foundational superabundant-number reference only; no theorem imported here |
| `Robin1984` | G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, Journal de Mathématiques Pures et Appliquées (9) 63 (1984), no. 2, 187--213 | metadata and later primary restatements | LATER-PRIMARY-RESTATEMENT | exact criterion interface already recorded by T-0301/T-0201; original proof not reconstructed here |

The publisher pagination for Choie et al. is `357--372`. The arXiv page's journal-reference field displays a different page range; this contribution follows the publisher DOI record and records the discrepancy rather than silently choosing one.

## Central quantifier finding

The arXiv version history for `math/0604314` says version 1's main result falsely asserted that `n` had to be superabundant, invalidating the proof; version 2 supplied a different proof. This is directly relevant to the project because three distinct claims are easily conflated:

1. the least counterexample is superabundant;
2. existence of a counterexample implies existence of a superabundant counterexample;
3. every counterexample is superabundant.

Vojak's theorem concerns the least counterexample. T-0201/T-2001 prove the existence implication by replacing a counterexample with a possibly earlier record maximizer. Neither licenses the third statement. O-2001 records this as a permanent warning.

## Match to active work

### PR #19 / Issue #2

T-2001 independently reproduces the exact finite barrier needed by T-0201. T-2002 then gives a constructive canonical Hardy--Ramanujan search reduction without claiming that the original violating integer is itself superabundant.

### Future complete search

L-2004 gives a safe fixed-support pruning certificate. The literature on superabundant distribution, including Erdős--Nicolas, should be inspected in full before importing asymptotic support-size or enumeration claims.

### Colossally abundant spine

No source inspected in this pass is used to assert that a search restricted to the empirical colossally abundant transition spine is complete. That question remains separate and must receive an exact theorem with all quantifiers before it can prune the search.

## Citation status

All four references above were actually located. Only claims supported at the recorded inspection level are imported. No remembered theorem number, unlocated title, or guessed bibliography is used.
