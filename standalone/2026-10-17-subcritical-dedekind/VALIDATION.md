# Validation boundary and reproducibility

**Proposed analytic composition; same-author proof and checker; independent mathematical review remains necessary.** Finite checks cannot certify an L-function theorem. No accepted 91/100 theorem, actual zero census, Lean build, external referee, upstream metaplectic reconstruction, repository-wide validator or remote CI is claimed.

## What was executed

The complete `verify.py` ran under ordinary Python and `python -O`, producing byte-identical CHECKS.json. All failures use explicit exceptions, not Python assertions. Syntax compilation passed. The polynomial utility is adapted from #961 and credited; the new data, estimates and checks are not advertised as an independent reviewer.

There are 1,394 finite predicates. The largest groups are 483 density checks (including 210 norm and 210 height monomials), 561 correction-domain guards, 84 reciprocal-disk guards, 60 middle-coefficient checks, and the full 22-class budgets. Other groups include normalization identities, dyadic-cone fixtures, complete nested-set patterns, powerful-radical fixtures and local-majorant identities. Repeated guards count as predicates, not independent analytic cases.

Every e-polynomial budget is certified by rational Bernstein coefficients on the ENTIRE interval [0,10^(-6)]; analytic applications use 0<e<=10^(-6). The limiting endpoint zero is used only to compare polynomial constants, not to apply an analytic estimate. The proof separately establishes the infinite summation and contour arguments.

The local beta tests use Q=r^2 for r=5,7,13,17, so both finite geometric sums and exact tail formulas are rational. These are local-formula fixtures, not a computed global number-field model. The small-effective-length control tests the positive profile ENVELOPE, not actual Whittaker values. The dyadic-cone grid illustrates the algebra; PROOF Sections 2.2--2.3 give the uniform argument instead of extrapolating from samples.

`run_mutations.py` launched seven separate optimized processes, all failing at the intended gates:

- delete the diagonal term when M<1;
- replace the good numerator mean by individual convexity;
- count a middle class at its upper rather than lower zero threshold;
- retain an old Mellin shift;
- use zero gap at the large-frequency cutoff;
- delete the subunit-effective-length envelope;
- corrupt the local beta coefficient.

MUTATIONS.json contains the actual failure messages. These are corrupted finite models, not proof-assistant modifications of a formal analytic proof.

The source thresholds were first explored with rational/float scripts outside the packet. They are now fixed explicit fractions. No optimizer, floating-point approximation, or sampled asymptotic is used by the final checker or proof.

## What the new argument must still withstand

The decisive step is PROOF (10)--(15), not the predicate count: uniform finite profiles for every balanced physical row; all c,n,a_f sums; the T<1 profile regime; local beta sums with the correct q_f and square-root weights; and use of the quadratic sieve BEFORE absolute auxiliary summation. The statement is reconstructed from CT's unrestricted reflection and is not a substitution of M<1 into its M>1 corollary.

Next review the exact fixed S-unit character adapter, complete AFE and density-detector columns, zero-selected subset mean, fixed exceptional sets before subsequent tiny losses, principal residue, every contour/tail and the changed Mellin normalization. None is certified by the rational checker. No critical native covariance theorem is inferred.

## Prior-publication check

Live #961 was already open at 7bd275b44261fff93bb565a9342c44b7c66526f6. All thirteen archive file blob hashes and sizes match its live tree, and the reconstructed subtree is exactly 916580e58acc72b87df6931b4e688543501c95ab. Its FULL verifier outputs in ordinary and optimized Python reproduce its archived CHECKS.json, and its twelve-payload-file manifest passes. This pass did not create that recovery, rerun its old mutations, or overwrite its historical qualifications.

## Publication semantics

Only a new standalone directory is added on #961. No inherited file or integrated scientific-status statement is edited. The outer publication receipt records the actual resulting commit, branch, PR, subtree and file identity comparisons. The manifest binds source bytes, not theorem validity. A fresh ZIP replay and remote read-back are reported only after their actual execution in that outer receipt.
