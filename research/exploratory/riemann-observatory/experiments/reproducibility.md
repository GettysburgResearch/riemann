# Reproducibility register

Every computation in the Observatory is listed here with its command, environment and output hash. "Rigorous" means Arb ball arithmetic with certified enclosures; anything else is labelled non-rigorous. Campaign-specific computations are additionally documented in `proposals/independent_campaigns/<campaign>/FINAL.md`.

Environment (session of 2026-11-17): Linux x86-64, 4 vCPU, 15 GB RAM; Python 3 with python-flint 0.9.0 (Arb), mpmath 1.3.0, sympy 1.14.0, numpy, scipy 1.18.1, networkx 3.7.

## EXP-0001 — first 100,000 nontrivial zeta zeros (rigorous)

* Code: `experiments/code/zeros_arb.py` (calls `flint.acb.zeta_zeros`, i.e. Arb's `acb_dirichlet_zeta_zeros`, which isolates zeros on the critical line and certifies the count via Turing's method).
* Commands: `python3 zeros_arb.py 1 50000 zeros_1_50000.tsv` and `python3 zeros_arb.py 50001 50000 zeros_50001_100000.tsv` (working precision 96 bits); runtimes 1059 s and 1283 s.
* Output: `experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz` (columns: index n, midpoint of γ_n to 25 significant digits, radius bound), sha256 `4d364a6ba8043e878409fe7d2ce89d2e9c6a29ba48dc1446b54c468579715603`.
* Range: γ_1 = 14.1347251417346937904572…, γ_100000 = 74920.8274989941867938492…; maximum ball radius 1.7·10⁻²⁴.
* Status: NUMERICAL-RIGOROUS for the stated enclosures, conditional on the correctness of Arb/FLINT. Note the midpoint is printed to 25 significant digits, so for γ < 10⁵ the printing adds an absolute rounding error of at most 5·10⁻²¹; the radius column bounds only the Arb ball. A certified enclosure of γ_n from this file is therefore [mid − rad − 5·10⁻²¹, mid + rad + 5·10⁻²¹]. These data are used by the campaigns; they are not new mathematics (RH is verified far beyond this height, Platt–Trudgian 2021).

## EXP-0002 … EXP-0006 — research campaigns C1–C5

Each campaign directory contains the investigator's code (`experiments/code/<campaign>/`), the skeptic's and adjudicator's independent re-implementations (subfolders `skeptic/`, `adjudicator/` where present) and outputs (`experiments/results/<campaign>/`). The adjudicated statement of what each computation establishes, its rigor label, and rerun commands are in `proposals/independent_campaigns/<campaign>/FINAL.md` and the corresponding `REPORT.md`/`SKEPTIC_REVIEW.md`.

| ID | Campaign | Main computations | Rigor |
|---|---|---|---|
| EXP-0002 | C1 detection horizons | Li-coefficient single-defect grid (63 cases), de Bruijn–Newman collision ODE (54 cases), exact Jensen-polynomial root counts (Arb), Nicolas grid, horizon tables at T₀ | mixed: Arb-certified thresholds; model predictions non-rigorous |
| EXP-0003 | C2 countermodel zoo | certified off-line zeros of Davenport–Heilbronn, Epstein zeta, F_c(s)=ζ(s)(1+c2^{-s}+2·4^{-s}); de Bruijn–Newman H_t for t<0; Chowla–Selberg evaluation refuting a published conjecture; Li thresholds with corrected boundary term | Arb/Rouché certificates where stated; Li thresholds non-rigorous (two independent codes) |
| EXP-0004 | C3 failure anatomy | de Branges/Conrey–Li condition counts over 100,000 zeros (three implementations) and 1000-zero blocks to n=10¹⁰; Cheng–Graham counterexample certificate; Micheas counterexample; Mertens/Liouville checks | Arb-certified counts and certificates |
| EXP-0005 | C4 Weil window locality | Galerkin λ_min(L) profiles (upper bounds), single-defect detection margins (Arb point certificates at T up to 10¹⁰⁰⁰), eight exact-rational negative witnesses, arithmetic-side vs zero-side cross-checks | Arb certificates for margins/witnesses; Galerkin values are upper bounds (non-rigorous) |
| EXP-0006 | C5 function-field transfer | sharp window theorem tests over 𝔽_q for 24 (q,g), window-positivity decay data | computations exact over finite fields where stated |

## EXP-0007 … EXP-0009 — audits

| ID | Audit | Computations |
|---|---|---|
| EXP-0007 | Quasi-RH 11/12 (`audits/quasi_rh/`) | ~100 checks of residue-symbol, Gauss-sum, reciprocity, Gauss–Jacobi and cubic-theta identities in ℤ[ω]; code in `experiments/code/quasi_rh/` and `audits/quasi_rh/architecture_checks/` |
| EXP-0008 | 2026 claims (`audits/claims_2026/`) | Alpöge–Furman Prop. 4.2 witnesses on actual zeros (T ≤ 3·10⁴); Landau–Siegel constants, prime-sum inequalities (Arb, x ≤ 10⁷), L(σ,χ_d)>0 certificates for |d| ≤ 5000; code in `experiments/code/claims_2026/` |
| EXP-0009 | Level-2 flag audits (`audits/L2_flag_audits/`) | Bellotti–Trudgian–Yang trigonometric polynomial and Table 1 (Arb branch-and-bound, root isolation), Farmer thresholds, Yakaboylu witnesses; code referenced inside each audit file |

All computations ran in the session environment listed at the top of this file. No code from external repositories (including the OpenAI release) was executed.
