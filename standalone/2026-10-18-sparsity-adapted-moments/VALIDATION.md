# What was executed, and what was not

## Mathematical review boundary

Both proof notes and the code have ONE author. They received a same-author reconstruction, not a separate agent, human referee, proof-assistant check, or new proof of the imported large sieve. No full-repository validator, upstream Lean build, remote CI, L-value calculation or zero census was performed. Publication does not constitute mathematical acceptance.

The proof's actual gain is the selected mollifier mean. A self-audit found that an initially highlighted U^(9/16) selected first mean is also implied by a full eighth moment. The proof and overview were corrected BEFORE publication; the overlap now has an explicit regression. The old same-order comparison is valid but is not claimed to beat every available bound.

## Exact finite checks

Both `python verify.py` and `python -O verify.py` completed and produced byte-identical CHECKS.json: 25,863 counted predicates, including setup and repeated guards. Main coverage:

- 8,800 comparisons of the selected exponent's closed formula with an independent maximization over every affine breakpoint, for n=3,...,18, eight fixed moment orders and five real lines. The infinite continuous formula is proved in SPARSE_MOMENTS.md; this is only a finite regression.
- Eight formal rational-polynomial identities authenticate the general-n density algebra by exact coefficient equality, not extrapolation from sampled integer n. Additional parameter/budget checks run for n=6,...,128.
- 2,592 actual-conductor exponent checks retain the direction of the negative dual factor; 121 sextic piecewise examples; an explicit eighth-moment overlap check.
- 1,060 abstract root-of-unity/nonunit identities, and 2,560 COMPLETE rational-integer power decompositions through 512 at n=3,4,6,8,10. Root phases are abstract algebra fixtures, not a physical number-field character census.
- Native rational divisor/mollifier coefficient checks retain the unit, annihilation below A and the two-sided exclusion mask.
- 2,210 prefix disjointness and 6,630 dilated square-mass checks retain the interval bookkeeping needed by the maximal polynomial argument. These are repeated finite fixtures, not distinct analytic theorems.

No floating-point arithmetic enters the accepting checker. Exploratory floating optimization suggested directions but supplies no accepted certificate and no optimality assertion.

## Separately executed negative controls

`run_mutations.py` executes eight NEW optimized Python processes. Each fails at its declared gate; MUTATIONS.json records actual outcomes:

wrong crossing; max replacing min; wrong dual conductor sign; erased nonunit mask; false coprimality of c and d; replacement of the selected mollifier by the full-row bound; wrong Holder R-power; duplicated prefix interval.

The full-row replacement is a VALID WEAKER mathematical bound. Its failure means that it cannot certify the NEW 5/7 exponent, not that the previous bound is false. All other controls test the stated exact identities/inequalities at their specified scope. Failed or timed-out runs are not counted as successes.

## Reproduction and publication contract

`verify_manifest.py` checks every manifested payload hash and byte length. The manifest does not hash itself. A new ZIP was extracted into a separate directory; both accepting modes and all eight rejected mutations were replayed there, and the byte manifest matched.

Publication is through connected GitHub write actions, on a new branch from #975. No clean cloned worktree is claimed. The final remote tree and individual blob identities must be compared with the tested local files before reporting success; the exact head is recorded in the PR description, not embedded self-referentially in a manifest.

## Priority adversarial review

1. Check the imported operator really applies on both power-free indices with the specified fixed twists and generators.
2. Check the selected mollifier split Y=min(A,U/R), its four dyadic terms, and all R-dependent exponents.
3. Check the rowwise zero detector: translate the Gamma kernel before summing, retain every dyadic prefix/ordinate maximum, and sum complete-column interval masses in the common l2 space.
4. Check the negative actual-conductor factor for the all-order AFE and the selected envelope formula.
5. Check the Jensen multiplicity conversion and the choice of a fixed positive height exponent only AFTER the required final loss.

The unresolved global RH estimate is not among the predicates claimed passed.
