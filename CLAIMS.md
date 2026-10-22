# CLAIMS.md — claim index

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31.

**Scope warning.** This index is complete only for the `16xxx` claims created on 2026-07-31. The `14xxx` and
`15xxx` rows are transcribed from branch reading and are provided so the graph is usable; their statuses are as
recorded by their authoring agents and have **not** been independently re-verified here except where noted. The
integrator should extend and correct this file; it is not authoritative for other agents' work.

Statuses per README §7: `IDEA`, `EMPIRICAL`, `PARTIAL`, `PROPOSED`, `PROVED`, `INDEPENDENTLY_VERIFIED`,
`REFUTED`, `SUPERSEDED`.

---

## 16xxx — 2026-07-31, `claude-fable-01` (branch `claude/agentic-polymath-riemann-jjj23a`)

| ID | Title | Status | Evidence level | Depends on |
|---|---|---|---|---|
| `L-16001` | Radical target is Pólya's `Phi`; `hat k = Xi/4`, not `Xi` | `PROPOSED` | analytic proof + 32–40 digit check | none (self-contained) |
| `L-16002` | One-signed target ⇒ `B_p` PSD by Cauchy–Schwarz ⇒ isotropic cone empty ⇒ feasible `c` for every special `Q` | `PROPOSED` | elementary proof + exact verification | `L-15107` (notation only) |
| `L-16003` | Gap parity: `#real >= #same-sign adjacent pairs`; equality and interlacing forced when one-signed | `PROPOSED` | elementary proof; bound held 26/26 | `L-15108`, `O-16001` |
| `L-16004` | Special completion in closed form = Loewner matrix of `-P'/P`; positivity ⇔ real-rootedness; **parity automatic** | `PROPOSED` | elementary proof + exact verification | `O-16001` |
| `O-16001` | CvS coordinates are Fourier **coefficients**; target is `xi_j = (-1)^j Xi(2 pi alpha j)`; documents the positivity trap | `PROPOSED` | quoted from arXiv:2511.23257 + derivation | `L-16001` |
| `O-16002` | Jensen-polynomial counterexample window is **empty**, not merely finite | `PROPOSED` | literature (GORZ 2019; GORTTW 2022) | — |
| `L-16005` | Hard-window artifact dominance: exact error relation, rigorous $\varepsilon(T)$ bound, certification boundary $\alpha\lesssim0.4$. **See the ERRATUM to (iii): on this lemma's own lattice $\omega_jT=\pi j$, so the sharp decay is $O(j^{-2})$ with an alternating sign, not $O(1/j)$ — contradicted by the lemma's own table. All three downstream conclusions stand** | `PROPOSED` — (iii) superseded | bounds `PROVED`; tables `EMPIRICAL`, reproduced to 0.11% | `L-16001`, `O-16001` |
| `T-16001` | Gate is satisfiable via freely prescribable real zeros; satisfiability **equivalent to RH**; explicit zero-matched sequence | `PROPOSED` | elementary proof + classical LP import; exact Sturm verification | `L-15108`, `O-16001`, Laguerre–Pólya |
| `R-16001` | Sampled-`Xi` scale obstruction | `PARTIAL` — see ERRATUM and ERRATUM 2; conclusion **downgraded to OPEN** | census `CERTIFIED-COMPUTATIONAL` for the sampled family; constant `alpha_c` and mechanism (e) **corrected**; conclusion (f) survives for both targets | `O-16001`, `L-16003`, `L-15108` |
| `X-16001` | Exact rational verifier for the cone-collapse propositions | `PROPOSED` | all propositions pass; certificate sha256 `2eacce19f8a8…` | — |
| `X-16002` | Certified real-root census of the sampled target, with controls | `PROPOSED` | 150-digit eval, 100-digit rationalization, exact Sturm, stable at 20/30/40/50/60 | — |
| `O-16003` | Source atlas: the repo's Weil matrices are Loewner forms of explicit sources; (L0)/(L1)/(L2) screen | `PROPOSED` — exploratory | high-precision float; precision-tracking defects | CvS Prop 4.1, `L-16004` |
| `O-16004` | The arithmetic Weil form nominates its own target `xi = Q_W^{-1} eta / (eta^T Q_W^{-1} eta)` | `PROPOSED` — **headline downgraded, see its §6** | exact congruence for the inertia; high-precision float elsewhere | `O-16003`, CvS Thm 5.6 |
| `L-16006` | CvS gate = orthogonal-polynomial extremal problem: `t* = min{ &#124;&#124;P&#124;&#124;^2 : P monic, deg 2N }`, `P_xi` = the monic OP; for a pole-sum source it is a **pole detector**; contains an explicit failed prediction | `PROPOSED` | (a)–(c) short exact proofs, checked to working precision; (d) measurement | `T-16001`, `L-16004`, CvS Thm 5.6 |
| `O-16005` | Positive-definiteness **and** zeta-zero recovery independently select `D-0001`'s block sign pattern `(+pole, -arch, -prime)`; contains a correction to `L-16006` | `PROPOSED` | high-precision float, 2 points, 8 sign patterns each | `D-0001`, `L-16006`, `O-16004` |
| `O-16006` | Resolution is set by `N`, **not** by the prime cutoff (flat over `c = 50..20000`); `t* ~ 0.088/(N log c)`, but the `1/N` half is **universal** (a Pick control is flatter), so only the `1/log c` is arithmetic | `PROPOSED` | high-precision float, every row recomputed at 2x dps | `L-16006`, `O-16004` |
| `O-16007` | Residue law `a(gamma) = (log c/pi^2) sin^2(gamma log c/2)`, measured to 8 digits across a 685x swing. **`PARTIAL`: the identity is now DERIVED as `T-16002`; the "blind cutoffs" conclusion is REFUTED and withdrawn** | `PARTIAL` | high-precision float | `T-16002`, `L-16006` |
| `T-16002` | **The cardinal residue identity, derived**: `g_u(z) = (L/pi^2) sin^2(pi mu) <u,ell(mu)>^2`. The resonance at integer `gamma*Delta` is **removable inside the node band** (`g_u = L u_k^2`) and, outside it, an on-line notch whose off-line continuation is `-sinh^2(pi y) < 0` — the most favourable case for detection, not blindness | `PROPOSED` — derived, conditional on `D-0001` | derivation from review + 8-digit check; corrected experiment | `D-0001` (load-bearing), `L-16004`, `L-16006` |
| `O-16008` | Detectability. **See its ERRATUM: half the headline was wrong.** The blind band does widen monotonically (`8.9e4` at `N=8` to `3.7e32` at `N=24`) so locating the exact threshold in fixed precision is hopeless; but absolute float64 sensitivity **improves** with `N` (`8.7e-2` to `6.8e-9`) once the pole enters the node band, which my `N<=14` range had hidden. Needs `~4.0N+10` digits. Also **corrects the scope of `L-16004`(ii)** | `PROPOSED` — synthetic caricature | high-precision float, dps doubled at `N=8,14,22,24`; constants NOT converged in `M` | `L-16004`, `O-16004` |
| `O-16009` | The pole-detector's budget is `floor(N/2)`: error depends on the margin `m = N-2k` alone, not on `N` or pole height. **Predicts `O-16004`'s `N=10` cutoff to within a factor 1-3.** Truncation bias is one-signed and saturates in `K`, but `t*` does NOT -- the norm depends on the whole zero set | `PROPOSED` | high-precision float; residuals `1e-62..1e-112`, dps re-runs | `L-16006`, `O-16004`, `O-16007` |
| `M-16001`–`M-16005` | Organizational proposals | `PROPOSED` | see `ORGANIZATIONAL_PROPOSALS.md` | — |

### Errata raised against existing claims

| Target | Issue | Raised in |
|---|---|---|
| `L-15101.7` | asserts `hat k = Xi`; correct identity is `hat k = Xi/4` | `L-16001`(c) |
| `L-15108` §5/§8.3 | flags parity as something to be arranged; it is **automatic** | `L-16004`(iv) |
| any leading-minor PSD gate | leading principal minors do not certify semidefiniteness for singular matrices | `L-16004` adversarial tests |

### Confirmed, not weakened, by this session

`L-15107` (Lemma 4.2 corner case, and the CvS Appendix B.1 cross-check), `L-15108` (independently re-derived
against CvS Lemmas 5.2/5.3/5.8/5.9 and found correct), `L-15109`, `T-15103`, `T-15104`, and the working note's
Theorem 3.1 — all stand as correct implications. What `R-16001` shows is that `T-15102`/`T-15104` have hypotheses
that the repository's current target sequence cannot jointly satisfy, not that the theorems are wrong.

---

## 15xxx — transcribed, not re-verified here

| ID | Title | Status as recorded | Branch |
|---|---|---|---|
| `L-15101` | Exact Hermite source, global Weil radical, Gaussian localization tail | `PROPOSED` | `agent/gpt56-pro-10/151-radical-hermite-bridge` |
| `L-15102` | Radical compression and leakage residual | `PROPOSED` | same |
| `L-15103` | Two-sign prolate radical repair (*"two-sign" refers to Fourier eigenvalue signs, not to the target's sign pattern* — clarified this session) | `PROPOSED` | same |
| `L-15104` | Screw kernel leakage bound | `PROPOSED` | same |
| `L-15105` | Sharp boundary resolvent real-zero family | `PROPOSED` | same |
| `L-15106` | Radical cluster obstruction | `PROPOSED` | same |
| `L-15107` | Exact Finsler target-completion criterion | `PROPOSED` | `agent/gpt56-04-f/151-finsler-target-completion` |
| `L-15108` | Special positive completion ⇔ real-diagonalizable quotient | `PROPOSED` | same |
| `L-15109` | Bézoutian root-threshold diagonalization | `PROPOSED` | same |
| `T-15101` | Form-core ground-state transfer | `PROPOSED` | `agent/gpt56-pro-10/151-radical-hermite-bridge` |
| `T-15102` | Reduced positive RH criterion from exact radical leakage | `PROPOSED` | same |
| `T-15103` | Target-pinned diagonal completion | `PROPOSED` | `agent/gpt56-04-f/151-finsler-target-completion` |
| `T-15104` | Finsler–Hermite cofinal criterion implying RH | `PROPOSED` | same |
| `R-15101` | Graph-separator incompleteness | `PROPOSED` | same |
| `X-15103` | Exact Finsler target-completion checker | `PROPOSED` | same |
| `T-14301` | Finite diagonal prolate–Weil criterion | `PROPOSED` | `agent/gpt56-09/143-finite-diagonal-prolate` |
| `L-14301`–`L-14307` | prolate / resolvent / Hardy-basis lemma stack | `PROPOSED` | same |

Earlier claim families (`93xx`, `98xx`, and below) are not indexed here; see the branch reports.
