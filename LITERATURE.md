# Literature and Reproducibility Anchors

Snapshot date: 2026-07-22.  Entries are primary sources or source repositories.
Their inclusion is not an endorsement of every claim.

## Finite Weil-matrix route

1. A. Groskin, *A finite Guinand--Weil dictionary and archimedean tail order for
   the truncated Weil quadratic form*, arXiv:2607.02828 (2026).
   Primary role: exact finite zero-source dictionary, admissibility, finite
   source quotient, pole-neutral family, tail-order theorem, and two-sided
   certification rule.

2. A. Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated
   Weil Form*, arXiv:2605.20224 (2026).
   Primary role: empirical matrix construction and high-precision experiments;
   not a proof of RH or its negation.

3. A. Groskin, *A matrix-valued von Mangoldt measure in the finite
   Connes--van Suijlekom path*, Zenodo DOI 10.5281/zenodo.21242028 (2026), arXiv
   pending at this snapshot.
   Primary role: exact prime-threshold derivative structure and finite
   source-to-jet rigidity.

4. A. Connes and W. van Suijlekom, *Quadratic forms, real zeros and echoes of the
   spectral action*, arXiv:2511.23257.

5. A. Connes, C. Consani, and H. Moscovici, *Zeta spectral triples*,
   arXiv:2511.22755.

6. M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.

## Source-code anchor used for X-0001

The formulas were independently transcribed and tested from the public
`akivag613/connes-cvs-` reproducibility repository, especially
`papers/2_guinand_weil_dictionary_tail_order/scripts/arb_ldlt_certify.py` and
the accompanying LaTeX source.  The source file snapshots inspected on
2026-07-22 had blob SHAs:

- paper source: `5982b1aac01ed7a1bc5f3c6afb5383fb8804636a`;
- Arb inertia script: `16ab9ced90b517d4d616f97962a95b949fa9fac4`.

X-0001 shares formulas, not a numerical backend: its discovery implementation
uses mpmath and its certificate checker uses exact Python fractions.  This is
still not a fully independent analytic derivation; Q-0004 exists for that
purpose.
