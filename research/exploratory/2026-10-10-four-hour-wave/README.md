# Four-hour research wave, 10 October 2026

Status: **PROPOSED / UNDER INDEPENDENT REVIEW**. RH remains open.

Scope: original quantitative lemmas, exact obstruction models, source-qualified
literature adapters, and reproducible experiments motivated by the October 2026
quasi-RH manuscripts. No inherited reviewed claim is promoted or rewritten here.

Exact sources or dependencies: repository base
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`; OpenAI `math` source commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; Liu refinement commit
`7d10420de90efa2f082a06a342fc7accbd57ab37`. Each component specifies its
additional analytic assumptions and arithmetic class.

What was actually run: recorded in the component reports and checkpoint log.
Ordinary high precision is reconnaissance; exact rational checks and directed
interval computations are labeled separately. An imported manuscript theorem
is kept distinct from a theorem independently reconstructed in this wave.

Smallest remaining gap: source-faithful critical cancellation, unrestricted
all-order positivity, or another explicitly identified global RH-facing input.
Local certificates, finite obstruction models, and improved supercritical
estimates do not discharge it.

## Sources

- OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*
  (30 September 2026), official source repository
  <https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb>.
- OpenAI, *The Quasi-Riemann Hypothesis* (5 October 2026), alternate
  `11/12` architecture in the same release.
- Baiying Liu's subsequent explicit improvement near `0.874957069799`;
  exact source and theorem obligations are documented in `literature/`.
- Other release papers are imported only at their precise fixed-source,
  conductor, height, coefficient, and uniformity scopes.

## Workstreams

| Directory | Target |
|---|---|
| `arithmetic/` | Critical negative-mass rates and a lower SHARP positivity threshold |
| `xi/` | Quantitative derivative transport and exact obstruction models |
| `heights/` | Height-versus-order mechanisms and global positivity through 3500 points |
| `operators/` | Source-specific continuum coercivity and effective-matrix bounds |
| `literature/` | Exact new-paper sources, admissibility audit, and exponent optimization |
| `correlations/` | Quantitative correlation-to-arithmetic adapters with explicit uniformity |
| `certificates/` | Directed critical-line endpoint signs and exact anchor intervals |

The scheduled wave runs from 11:59:27 to 15:59:27 UTC (approximately
15:00–19:00 in Jerusalem). Checkpoints are published on
`codex/research-wave-2026-10-10`; acceptance requires review at an exact commit.

Related prior repository research is draft PR
<https://github.com/GettysburgResearch/riemann/pull/910>, inspected at
`670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`. Its geometric perturbation,
same-envelope obstruction, and native height detector are credited in the
component comparisons. Its draft status is preserved; it is not an accepted
source verdict. Publication receipts are recorded in `CHECKPOINTS.md`.

The third checkpoint adds independently reviewed component deductions:
all-real SHARP positivity for m>=7/5, global kernel positivity for every
packet of at most 3500 positive nodes, and a uniform codimension-ten positive
continuum sector for every window through log3. The global kernel result
uses the named classical counting inputs and published finite-height zero
verification. Its L2 polynomial argument improves the earlier maximum-based
orders 320 (classical strip) and 350 (imported 7/8 strip).

The companion theorem proves an all-fixed-order sector beyond a complete
zero strip, with quantitative source-error budgets. A separate critical
residue test exposes the additional hypotheses implicit in pointwise
positivity at power one. The complete finite-census adapter also certifies
the rectangle |T|<=2, 0<=y<=1/2 at order zero and lambda=10, retaining
its imported historical finite-count input. The conditional half-plane
B=0.87495703 assumes
the imported analytic inputs. A further B=0.874956 implication prices a
new, explicitly open joint-witness estimate and does not establish it.
See `SCOPED_REVIEWS.md` for the exact review boundary.
