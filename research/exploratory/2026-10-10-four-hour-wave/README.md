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
| `heights/` | Height-versus-order mechanisms and global positivity through 700000 points |
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

The fourth checkpoint raises the global kernel order to **700000** at every
packet of positive nodes, using the same published count and finite verified
height inputs. A new weighted rational dilation argument proves positive
definiteness of the complete tail above T through even orders satisfying
6n²<=T, T>=3*10^12; its order grows like sqrt(T/6). The tail theorem does
not assume those tail zeros lie on the critical line. The corresponding
full-kernel theorem has a finite verified-height input and remains finite
order. Neither is an RH proof.

The arithmetic range is now **m>=13/10** for all real x>=1, with separate
normal and optimized directed replays. The signed quasi-RH source adapter
removes an artificial diagonal cost exactly, while leaving its off-diagonal
estimate open. Conditional prime-deletion bootstraps and an exact
same-count-envelope countermodel record both opportunities and barriers.
Full continuum residual integrations and larger native companion-domain
certificates continue separately.

The fifth checkpoint raises global kernel positivity to **888000** using a
Volterra endpoint bound and a sharper complete count discrepancy from the
same published inputs. The complete tail admits even orders satisfying
10000n^2<=2631T, improving the coefficient in its square-root growth.
An independent fallback gives order 866000 with the earlier count constant.

It also adds a complete-tail analytic companion theorem:
for every lambda>0 and every integer 0<=r<=16381, the actual Xi companion
has a strict positive sector on the entire closed lower column
|T|<8192-(r+2)/2, y>=0. The theorem imports the explicitly qualified complete
native census through 8192. It is finite in real part and does not assert RH.
Independent Gaussian certificates through |T|<=13 and |T|<=100 are retained
as separate methods, with their narrower parameter scopes.

A separate published-height corollary extends the open lower column to
|T|<3*10^12-(r+2)/2. Including its real boundary additionally imports the
published sign-change/complete-count saturation method contract. The large
published computation was not rerun; its source audit is kept distinct from
the session's native 8192-height primitive replay.

The sufficient all-real arithmetic power is now **m>=9/7**. The generalized
2k-moment attack adds an exact CRT translation law, finite positive-cumulant
counterexamples, a finite-support Euler correction at the critical exponent,
and a source-qualified second theta reflection. That reflection makes one
whole standard-cusp all-negative component vanish beyond its specified
compact-support threshold. The full signed moment remainder, other cusps
and other allocations remain open. The continuum work adds a reviewed local
gamma evaluator and exact centered parity reduction; its expensive residual
integration still needs a completed lower-matrix certificate.
