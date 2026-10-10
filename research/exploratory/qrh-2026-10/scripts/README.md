# Scripts for the QRH wave: what each one does and how to run it

All scripts are self-contained Python 3. Dependencies: `numpy`, `scipy`, `sympy`; `mpmath` for some
companions. Run them from this directory unless noted. Runtimes are for one core of a shared
4-core machine.

| Script | Purpose | Arithmetic class | Run | Time |
|---|---|---|---|---|
| `ledger_check.py` | 53 checks of the 7/8 and 47/48 manuscripts' stated rational arithmetic and polynomial identities | EXACT_RATIONAL | `python3 ledger_check.py` | seconds |
| `threshold_calculus.py` | exponent model of the 7/8 architecture; self-tests reproduce 7/8, 11/12 and the Lemma 20.2 margin | FLOATING_RECONNAISSANCE (row counts exact piecewise-affine) | `python3 threshold_calculus.py` | ~5 s |
| `energy_lp.py`, `energy_lp_validate.py` | LP supremum of the reflected-energy exponent (14.14) vs the closed form `max(M', (2M'+1+3l')/4, 2M'+l'-1)` | LP (floating) | `python3 energy_lp_validate.py` | ~30 s |
| `barrier_lp.py` | exact rational LP certificates: 13/15 (low side), 167/192 (floor bin), floor-dependence | EXACT_RATIONAL certificates | `python3 barrier_lp.py` | seconds |
| `sensitivity.py <scenario>` | Nelder–Mead geometry optimization for one scenario (see `SCENARIOS`); writes `../results/<scenario>.json` | FLOATING_RECONNAISSANCE | `python3 sensitivity.py A_paper_bp11_12` | 1–10 min |
| `floor_lp.py`, `floor_theta.py` | floor-bin cancellation payoff, exact LP and model (FLOOR_BIN_BARRIER.md) | EXACT / FLOATING | see file headers | minutes |
| `make_ladder_svg.py` | the barrier-ladder figure (`../figures/barrier_ladder.svg`) | n/a | `python3 make_ladder_svg.py` | seconds |
| `explicit_pnt_7_8.py` | explicit psi/theta/pi-li/short-interval bounds and the explicit Robin envelope under H(7/8) (EXPLICIT_PNT_7_8.md); writes `../results/explicit_pnt_7_8.{txt,json}` | INTERVAL (mpmath.iv, outward rounding); `--zeros` adds a FLOATING sanity check | `python3 -I explicit_pnt_7_8.py [--zeros]` | ~17 s (45 s with `--zeros`) |
| `zd_*.py` | ANTEDB-based zero-density runs (ZERO_DENSITY_CONDITIONAL.md); needs a sandboxed ANTEDB checkout, see that file | EXACT (ANTEDB rationals) / float grid | see file headers | minutes |

Companion folders, each with its own README or header:

* `../a2/`: exact-symbol Eisenstein-integer code for the fourth-moment structure.
  * `check_twisted_mult.py 200`: twisted multiplicativity.
  * `check_nesting.py 120`: the nesting identity.
  * `dual_offdiag.py X:HD ...`: dual off-diagonal reconnaissance.
* `../numerics/`: Lemma 7.1 local identity, Kintali phases, joint moment, Patterson sums.
* `../moments/`: fourth and sixth moments of the sextic Möbius family.
* `../reviews/`, `../falsification/`: review replays and tests.

Reproducibility caveats:

* Optimizations are local (Nelder–Mead from several starts). The exact LP certificates, not the
  optimizers, are the authoritative barrier statements.
* `pdftotext` drops complex-conjugation bars. Formulas were taken from the TeX source in
  PR 908's import or from rendered PDF pages.
