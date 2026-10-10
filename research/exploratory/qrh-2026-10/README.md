# QRH research wave (October 2026)

```text
Status: EXPLORATORY (PROPOSED analysis + IMPORTED external claims); no RH claim
Scope: external zero-free half-plane manuscripts; their exponent architecture; conditional consequences
Exact sources or dependencies: see INTAKE.md (OpenAI 7/8 manuscript, Kintali 47/48 manuscript)
What was actually run: scripts listed below (exact ledger, exact LP certificates, exponent model)
Smallest remaining gap: RH itself (sup Re rho = 1/2) is untouched by everything here
```

RH remains unproved. This folder studies the October 2026 *quasi*-RH manuscripts as an imported
object and as a source of mechanisms. The manuscripts claim a zero-free half-plane `Re s > 7/8`;
they are unreviewed.

## Headline findings (PROPOSED; conditional on the manuscript's stated lemma outputs)

1. **The arithmetic checks out.** The rational arithmetic and polynomial identities turning the
   lemmas into margins pass: 53/53 exact checks (`scripts/ledger_check.py`).
2. **7/8 is set by the low (reflection) estimate**, via `σ0 = 1 − lx/2 − h/6 + θ_low`. The high
   side is tight to `2.3·10⁻⁴`, on rows with mid-depth zeros (`a ≈ 0.69`).
3. **7/8 is effectively optimal for the manuscript's own lemmas.** Re-optimizing the geometry gains
   only `4·10⁻⁵`. Iterating the bootstrap from `β* ≤ 7/8` gains nothing.
4. **Barriers, with exact rational certificates:**
   * the low estimate can never certify below **13/15** in any geometry;
   * zero-free rows, which can only be counted trivially, force **≥ 167/192** at the manuscript's
     detector floor for *any* row-counting input, and → **13/15** as the floor → 1/2;
   * the probe family has a hard floor of **5/6**.
5. **The only escape routes** are cancellation across zero-free rows, beating the large-sieve
   diagonal on the reflected side, or a new probe.
6. **For this repository,** every RH-equivalent subpower premise moves from the trivial exponent
   1/2 to 3/8 under the imported claim. RH needs exponent 0.

| File | Content |
|---|---|
| [SYNTHESIS.md](SYNTHESIS.md) | **start here**: the two architectures, what is new, where a breakthrough would have to come from |
| [AGENDA.md](AGENDA.md) | bounded open problems with payoffs (moment ladder, 7/8 escape routes, verification, repo bridges) |
| [INTAKE.md](INTAKE.md) | exact claimed statements, architecture, dependencies, what was verified |
| [FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md) | the fourth-moment rung (to 17/24) has cubic GL(3)-metaplectic shape; nesting identity (a2/) |
| [BRIDGE_MELLIN.md](BRIDGE_MELLIN.md) | QRH continuation vs the repo's Mellin–Landau premise; graded NRC32 identity; family-relative step |
| [reports/REPO_RECENT_WORK.md](reports/REPO_RECENT_WORK.md) | digest of prior QRH work in PRs 908–910 and branches (read before extending) |
| [FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md) | zero-free rows on the Poisson side: payoff of cross-row cancellation θ (σ = max(13/15, (167−225θ)/(192−225θ)) with DH counts) |
| [ALT_PROBES.md](ALT_PROBES.md) | other metaplectic probes: parity/budget heuristic, cubic minimum 5/6, any theta-type probe ≥ 2/3 (HEURISTIC) |
| [reviews/KINTALI_REVIEW.md](reviews/KINTALI_REVIEW.md) | bounded review of the 47/48 paper: no error found; first unverified step Lemma 3 / App. B; density input identified |
| [numerics/](numerics/README.md) | finite checks: Lemma 7.1 local identity, Kintali eq. (1) phases, joint-moment and Patterson-sum reconnaissance |
| [THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md) | the exponent model, barriers 13/15, 167/192 and 5/6, experiments |
| [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md) | graded Mellin lemma (PROPOSED), conditional corollaries, non-improvements, repo hooks |
| [scripts/ledger_check.py](scripts/ledger_check.py) | 53 exact-rational checks of the manuscripts' stated arithmetic |
| [scripts/threshold_calculus.py](scripts/threshold_calculus.py) | exponent model (exact piecewise-affine row counts; self-tests) |
| [scripts/barrier_lp.py](scripts/barrier_lp.py) | exact LP barrier certificates (output in results/barrier_lp.txt) |
| [scripts/energy_lp.py](scripts/energy_lp.py), [energy_lp_validate.py](scripts/energy_lp_validate.py) | LP supremum of the reflected-energy exponent (14.14) vs closed form |
| [scripts/sensitivity.py](scripts/sensitivity.py), [results/](results/) | scenario optimizations |
| [scripts/SOURCES.txt](scripts/SOURCES.txt) | sha256 of the fetched PDFs |
