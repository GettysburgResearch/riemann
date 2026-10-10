# Validation and evidence boundaries

**Status:** proposed research packet, 2026-10-10. The small constant improvement is a conditional deduction from the explicitly listed imported analytic machinery. The stronger fourth moment and the height-local off-diagonal estimate are open.

## Mathematical review

The [review report](REVIEW.md) identifies the reviewed files by SHA-256 and states its precise coverage. A separate research agent checked the changed geometry against the source, including the compensated physical expression, the enlarged principal Euler region, the fixed plain-moment parameter, common exponent margins and the final continuation criterion. It also reviewed the exact envelope obstruction, the causal inverse, the native zero adapter and local energy, and the gcd reduction for the fourth-moment target.

This was an independent AI-agent review within this research pass. It is not an external referee's acceptance or an independent verification of the complete upstream analytic proof. The Euler/tail author is the reviewer for other components; that author's own contribution is distinguished in the report.

A second agent checked the completed-transform height normalization and higher-moment extraction and reviewed the final overview's claims. The overview was then tightened to state the proved mean-square domain and the critical-strip range of the zero adapter explicitly. No theorem file bound in the review was changed by those editorial corrections.

The complete conditional proof is in [GEOMETRY_PERTURBATION.md](GEOMETRY_PERTURBATION.md). Its frozen SHA-256 is 6e3befcc15b92536dd80f376a87384d5fa4688a938c11d949be7924d4a4c1e12. The smallest global dependency whose failure would invalidate its conclusion is the validity of its listed imported analytic inputs in the stated coefficient classes and uniformities. The proof introduces no hypothetical new moment input.

## Reproducible exact checks

Run the following from this packet's directory using Python 3:

    python checks/check_native_height.py
    python checks/check_tail_euler.py
    python checks/check_research_algebra.py

Repeat with python -O to check that interpreter optimization does not remove the acceptance gates. All checkers use explicit failures rather than relying on removable assertions for their counted predicates.

| Checker | Exact predicates per run | Coverage |
|---|---:|---|
| Native height | 29,785 | Finite Newton identities, coherent completely multiplicative phases, compressed block and detail-energy arithmetic, and the full finite inverse/plain defect |
| Tail and Euler | 83 | Exact sparse local polynomial identities and rational affine-envelope inequalities, including the enlarged principal domain |
| Research algebra | 148 | Original and perturbed rational certificates, the exact quadratic-field geometry obstruction, finite causal inverse compositions, conditional moment exponents, and 90 weighted gcd-decomposition panels |
| **Total** | **30,016** | Exact finite algebra and declared rational inequalities |

Each checker passed in ordinary and optimized Python. For each checker, stdout was byte-identical between modes and matched its recorded results file. The reviewer independently replayed the 83- and 148-predicate checkers in both modes. The native checker was executed by the authoring/root workflow and is not included in that reviewer's independent computation claim.

Results are recorded in [native](results/check_native_height.json), [Euler](results/check_tail_euler.json) and [research algebra](results/check_research_algebra.json). The [provenance manifest](PROVENANCE.json) binds all three checker sources and result files.

### Arithmetic and coverage contract

The native checker uses integer, rational and Gaussian-rational arithmetic. Its nontrivial model character has chi(2)=i, chi(3)=(3+4i)/5 and chi(5)=-1, with the other prime values equal to 1. It is a structural completely multiplicative phase, not a numerical evaluation of n to the power -it at a physical height. The Newton panels use Y in {1,2,3,5,7,15,31}; the largest native index is 1023. Product-defect panels cover each integer Y from 1 through 31.

The Euler checker uses exact rational polynomial arithmetic. It partitions each piecewise affine envelope at every rational crossing before checking the entire specified interval. These are exact envelope comparisons, not a floating-point sample of an interval.

The research checker represents the geometry obstruction in Q(sqrt(921)). Its decimal enclosure is derived from rational bounds on the radical. The causal tests include horizons on both sides of sixth powers. The 90 gcd panels use five integer scales and eighteen row labels, with completely multiplicative model phases in {+1,-1} and the actual nonunit zero-extension pattern. They test the full weighted identity; they do not compute actual Eisenstein sextic symbols or prove their arithmetic cancellation.

All arithmetic used by these checkers is exact. No floating-point tolerance, ordinary high-precision calculation or fitted extrapolation is used as a proof gate. The symbolic proofs establish the general identities; the finite examples check the implementation and selected source algebra.

## What was not established or run

- No fresh Lean kernel build or Comparator build was run. The new mathematics has not been formalized.
- No complete independent reconstruction of the imported analytic proof was performed.
- No zero census, certified physical-height computation, or numerical proof of a zero-free region was performed.
- No new infinite fourth or higher moment was proved.
- No pointwise native off-diagonal estimate sufficient for a shrinking zero-free band was proved.
- No result in this packet establishes RH or promotes a claim into the repository's integrated record.

The exact distinction matters: the zero-to-polynomial adapter, local energy threshold and shrinking diagonal are proved component results. Their combination excludes a zero only after the missing off-diagonal estimate is supplied.

## Source and repository preservation

The packet is based on the published import commit 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, on the import branch underlying draft PR #908. The imported source pin is adc7f1241b42e322a6451854ab7e4b4c146bf78a. The relevant quasi-Riemann manuscripts, companion Siegel manuscript, documentation and Lean directories were checked against upstream fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb and were unchanged.

Publication adds this proposed packet and a navigation entry in the root README. It preserves the October 7 import and existing integrated research. The follow-up PR is stacked on the import branch so that its review diff contains only this new work.
