# Reproducibility register

Every computation in the Observatory is listed here with its command, environment and output hash. "Rigorous" means Arb ball arithmetic with certified enclosures; anything else is labelled non-rigorous. Campaign-specific computations are additionally documented in `proposals/independent_campaigns/<campaign>/FINAL.md`.

Environment (session of 2026-11-17): Linux x86-64, 4 vCPU, 15 GB RAM; Python 3 with python-flint 0.9.0 (Arb), mpmath 1.3.0, sympy 1.14.0, numpy, scipy 1.18.1, networkx 3.7.

## EXP-0001 — first 100,000 nontrivial zeta zeros (rigorous)

* Code: `experiments/code/zeros_arb.py` (calls `flint.acb.zeta_zeros`, i.e. Arb's `acb_dirichlet_zeta_zeros`, which isolates zeros on the critical line and certifies the count via Turing's method).
* Commands: `python3 zeros_arb.py 1 50000 zeros_1_50000.tsv` and `python3 zeros_arb.py 50001 50000 zeros_50001_100000.tsv` (working precision 96 bits); runtimes 1059 s and 1283 s.
* Output: `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` (columns: index n, midpoint of γ_n to 25 significant digits, radius bound), sha256 `4d364a6ba8043e878409fe7d2ce89d2e9c6a29ba48dc1446b54c468579715603`.
* Range: γ_1 = 14.1347251417346937904572…, γ_100000 = 74920.8274989941867938492…; maximum ball radius 1.7·10⁻²⁴.
* Status: NUMERICAL-RIGOROUS for the stated enclosures, conditional on the correctness of Arb/FLINT. Note the midpoint is printed to 25 significant digits, so for γ < 10⁵ the printing adds an absolute rounding error of at most 5·10⁻²¹; the radius column bounds only the Arb ball. A certified enclosure of γ_n from this file is therefore [mid − rad − 5·10⁻²¹, mid + rad + 5·10⁻²¹]. These data are used by the campaigns; they are not new mathematics (RH is verified far beyond this height, Platt–Trudgian 2021).
