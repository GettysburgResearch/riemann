# Positive loops instead of another averaged residual bound

**Status: PROPOSED finite/local component mathematics, with a directed full-source
certificate; independent mathematical review required. RH, exact degree-20
matching and unbounded-order feasibility remain open.**

Base: #981, `cf41f3f94a0f1df2bb503d22ab384bfc69288f33`.
No inherited source or integrated mathematical status is edited.

The new operation adds a positive Ising edge between existing component roots,
then retunes nine old coordinates so the first eighteen theta moments remain
EXACT. It leaves the class covered by Lee--Yang intact and removes the tree-only
restriction. It does not claim that arbitrary positive correlations improve the
next moment.

## Results

- At ANY fixed matching order with an invertible lower moment Jacobian, an exact
  local continuation preserves lower moments. Its next-moment derivative is the
  explicitly compensated edge covariance in PROOF (2). Opposite signs on two
  missing edges give two-sided LOCAL reachability, with no all-order guarantee.
- At the TRUE degree-18 theta solution of #981, a positive edge between roots
  7 and 9 has compensated raw degree-20 derivative in (-3.423,-3.421); the edge
  (2,7) has derivative in (0.107,0.109). These are rigorous interval certificates,
  not numerical slopes at a fitted center.
- An independently certified endpoint at edge bias q=1/10000 has 282 spins and
  282 edges, matches theta moments 2 through 18 exactly, and has degree-20 excess
  in (0.4737,0.4738), reduced by more than 0.0004 from the #981 excess in
  (0.474,0.475). This is a SMALL finite improvement, not degree-20 matching.
- The new #988 tree has a different excess in (0.450,0.451), already smaller.
  This packet does not claim the smallest residual across architectures. Its
  contribution is the source-certified two-sided response and loop operation.

Read PROOF.md before interpreting the finite checks. The approximation criterion
in #981 COFINAL_COMPACTNESS.md remains an implication with an OPEN premise.

## Reproduce

From this directory in the parent repository:

    python replay.py

Only the Python standard library and the two SHA-pinned inherited files
`interval_source.py` and `parameters.json` are needed. Every accepting run
reconstructs the infinite theta source through degree 20, all its tails, both
old response certificates and the new positive-loop root. No cached moments,
solver, network or external L-value/zero data are used.

The source primitive is inherited, not independent. The checker/proof have one
author; the complete seven-spin control independently assembles the finite
probability law but is not a referee or second transcendental backend.
