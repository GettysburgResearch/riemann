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
| `T-16001` | Gate is satisfiable via freely prescribable real zeros; satisfiability **equivalent to RH**; explicit zero-matched sequence | `PROPOSED` | elementary proof + classical LP import; exact Sturm verification | `L-15108`, `O-16001`, Laguerre–Pólya |
| `R-16001` | Sampled-`Xi` target cannot satisfy `T-15104`'s hypotheses: scale obstruction | `PARTIAL` — see its ERRATUM | census `CERTIFIED-COMPUTATIONAL` for the sampled family; constant `alpha_c` and mechanism (e) **corrected**; conclusion (f) survives for both targets | `O-16001`, `L-16003`, `L-15108` |
| `X-16001` | Exact rational verifier for the cone-collapse propositions | `PROPOSED` | all propositions pass; certificate sha256 `2eacce19f8a8…` | — |
| `X-16002` | Certified real-root census of the sampled target, with controls | `PROPOSED` | 150-digit eval, 100-digit rationalization, exact Sturm, stable at 20/30/40/50/60 | — |
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
