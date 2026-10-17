# Connected theta moments and a decreasing ferromagnetic edge response

**Proposed finite component theorems. Independent review is required. RH
remains open, and degree 18 is not realized by this packet.**

The exact theta source is preserved. The packet adds two results to the
Lee--Yang moment-realization route:

| Result | Certified statement | Boundary |
|---|---|---|
| T16C | A 281-spin, 280-edge connected ferromagnetic tree exactly matches the original theta moments through degree 16; every edge has coupling strictly between 1/200000 and 1/4 | The standardized 18th-moment defect lies strictly in (0.034, 0.035) |
| CER | At the original PR #886 degree-16 source root, an edge between two dimer roots has compensated standardized raw-18 derivative in (-0.785, -0.784), while all lower 16 moments remain fixed | A local analytic germ; no interval reaching the degree-18 target is claimed |

The previously constructed D16 box had next-moment defect in (0.169, 0.170).
The new tree has a certified smaller defect and quantitatively positive
connections between the old components. Its two large dimer observables
have covariance greater than 1/60000. The hidden hub has zero observable
weight; the proof gives the positive-weight approximation and Hurwitz
argument needed to retain the Lee--Yang conclusion.

## Read and reproduce

Read `PROOF.md` for the exact graph, normalization, theorem quantifiers,
full source remainders, contraction argument, and edge-response formula.
`EXPLORATION.md` records unsuccessful degree-18 searches with their
appropriate numerical scope.

With standard Python 3, run in this directory:

```sh
sha256sum --check SHA256SUMS
python3 certify_tree.py --check tree_certificate.json
python3 certify_edge.py --check edge_certificate.json
```

No third-party numerical package, network access, special-function oracle,
or stored target-moment input is needed. Each checker freshly evaluates all
98 source integration cells and all time and index tails. The tree checker
also compares its moment map with exact enumeration of all 128 states of
a seven-spin test instance, through every moment of order 18.

The proof-producing mode is `--emit OUTPUT.json`; the checking mode is
`--check RECEIPT.json`. Both reconstruct the entire calculation. Terminating
rational parameter centers are inputs to an existence proof, not asserted
approximate roots. Every acceptance comparison uses directed integer
intervals and exact rational arithmetic. The decimal values printed at the
end are diagnostics only.

The inherited arithmetic primitives and original D16 parameters are frozen
to PR #886 at commit `d998605c0718e332ac503baf078704b862f8250e` and verified by
SHA-256. The six-index source extension uses that same arithmetic backend;
its new tail bounds are rederived in `PROOF.md`. Exact source references are
listed in `SOURCES.json`.

## Remaining mathematical task

A full proof by this route still needs admissible finite ferromagnets
reaching the original theta moment targets at unbounded orders, with the
associated convergence and source-identification argument. The immediate
next finite milestone is a complete degree-18 target root with certified
positive parameters. The derivative sign and the connected degree-16 box
do not establish that milestone or a global continuation theorem.
