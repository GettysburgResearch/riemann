# Repository assessment — 2026-09-01

```text
Status:   ASSESSMENT with one new proof packet (standalone/2026-09-01-fixed-detector-dichotomy/)
Scope:    the 2026-08-22 reviewed release (PRs #375–#707, 139 claims), the formal-v0.1 Lean
          spine, the 11 programme issues #736–#746, #763, #764, and the ~55 research PRs
          #708–#785 deposited after the freeze.
Basis:    direct reading of the front-door documents and of the load-bearing source lemmas
          (L-99602, L-99261, L-99613, L-99940/42/44, L-99270/72, L-96000/01, L-100131,
          L-103102, L-91904, the minimal-wavelet PROOF.md, the First-Hermite proofs);
          five parallel PR-level surveys with per-PR spot checks of the most load-bearing
          theorem; the issue threads; and the computations in the new packet.
RH:       UNPROVED. Nothing below claims otherwise.
```

## 1. Verdict in ten lines

The project has built an unusually honest and well-provenanced record of *reformulations*
of the Riemann Hypothesis, together with a genuinely valuable formal-verification spine
and a small number of clean unconditional lemmas. It has not moved the mathematical
frontier: no reviewed statement is an estimate that was unknown before and sits strictly
between the literature and RH. Every conclusion-facing "open cut" in the release is
either RH itself in different coordinates, a statement strictly harder than RH, or (in at
least three cases now) false. The post-freeze wave of ~55 PRs repeats this pattern at
larger volume and with more vocabulary, and its two most important contributions are
*negative*: refutations of the project's own gates. The distance to a proof is, as far as
this repository is concerned, unchanged from the published state of the art. The honest
way forward is to stop generating equivalences, and to redirect the same machinery at
targets where it can win: quantitative proxies, formalization of classical criteria, and
structural work anchored in existing frameworks, tested first where RH is a theorem.

## 2. What has actually been established, in standard language

The release's arithmetic route rests on one classical mechanism. For a fixed kernel `K`
and `D_K(x) = Σ_{n≤x} μ(n) n^{−1/2} K(x/n)`, the Mellin transform is `K̂(s)/ζ(s+1/2)`;
Landau's theorem says that if `D_K` is eventually nonnegative, or has subpower negative
mass, then `1/ζ` has no pole in `Re s > 0`, i.e. RH. The release verifies this consumer
for several kernels (the SHARP scalar `4√y − 3`, rows 2 and 3, the `5:3` scalar, the
ratio-eight wavelet, the logarithmic box) and correctly labels the producer premises as
open. The other routes are classical criteria in disguise: the "actual-Xi Pick" kernel
is the Nevanlinna–Pick form of Lagarias's positivity criterion (`Re ξ'/ξ > 0` on
`Re s > 1/2 ⟺ RH`); the "First-Hermite" criterion is Weil positivity for the Gaussian
family `(z−x)²e^{−q(z−x)²}` with a neat terminal-zero argument; `CV`, `XD`, `MWOC`,
`UOSACF`, the "beta" criteria and the Nyquist/harmonic variants are all the Mertens
criterion `M(x) = O(x^{1/2+ε})` after two lines of Abel summation.

A glossary for the next reader:

| repository term | standard object |
|---|---|
| native source, `β(n)` | `μ(n)`, or `μ(n) − 𝟙_{67|n}μ(n/67)` (Dirichlet series `(1−67^{−s})/ζ(s)`) |
| fixed zero-safe detector, row, scalar | `Σ_{n≤x} μ(n)n^{−1/2}K(x/n)` for an explicit band kernel `K` |
| Mellin–Landau consumer | Landau's theorem on Dirichlet integrals with nonnegative density |
| subpower negative mass, `CV`, `XD`, `MWOC`, `UOSACF` | `M(x) ≪ x^{1/2+ε}` (RH) |
| SHARP power `m ≥ 2` | positivity of `Σ β(n)n^{−1/2}(4√(x/n)−3)^m`, dominated by the absolutely convergent `n^{−3/2}` term |
| carrier, first chaos | the deterministic main term (pole of `ζ` at 1, or the single-prime term) |
| half-divisor, `η`, `λ` | coefficients of `ζ^{±1/2}` |
| physical shell / occupancy | passing from the free monoid on prime labels to the integers |
| actual-Xi safe Pick matrix | `((L(q_i)+L(q_j))/(1+q_i+q_j))`, `L(q) = ξ'/ξ(1+q)`; PSD for all tuples ⟺ Lagarias/Hinkkanen criterion |
| First-Hermite, zero heat | Gaussian Weil positivity, `Σ_ρ (γ_ρ−x)²e^{−q(γ_ρ−x)²} ≥ 0` |
| reverse Rolle, wrong extremum, residue | Levinson/Conrey descent from `ξ^{(k)}` to `ξ`; a positive local minimum of `ξ^{(k)}` |
| beta harmonic, Nyquist compression, coarea | Dirichlet polynomial of `β` at frequency `2πh/log X`; Parseval; Fejér averaging |
| shared fibre, Kummer sheaf, relative Frobenius | pairs of Dirichlet characters modulo two primes; character orthogonality; a permutation of a finite index set |
| F1 Frobenius–Hodge, activation polymatroid | `ℝ[x_1..x_m]/(x_i²)` with vector coefficients; the submodular function `min(T, Σ log p_e)` |
| Architecture E, E–Widder cone | Lagarias + Hermite–Biehler + Widder's Stieltjes criterion; finite-order tests are blind to zeros above height `≈ 2k/π` |

### 2.1 What is impressive

- **Review and provenance discipline.** The front door is literally correct: 139 claims,
  36 typed edges, every open node labelled open, every finite result kept finite, 19
  refutations preserved with the first broken arrow. I found no case where the release
  itself overstates a result. This is rarer than it sounds.
- **The formal spine.** formal-v0.1 is a real artifact: pinned Lean/Mathlib, an 8,806-job
  sorry-free build, only the three standard axioms, a 139-row map that admits most claims
  are unstated. The conditional theorem `fixedDetector_negativeMass_implies_RH` with
  every premise explicit is the right shape for a formal library.
- **A few clean unconditional lemmas.** The labelled-Euler-cube proof that
  `Σ β(n)n^{−1/2}(4√(x/n)−3)^m > 0` for all `x ≥ 1`, `m ≥ 2` (L-99613); the
  two-parameter First-Hermite criterion with its terminal-pair "threat graph" and the
  unconditional wedge `q ≤ (4−ε)\log\log|x|`; the actual-Xi Pick positivity through order
  three with the Platt–Trudgian reserve budget; the minimal dyadic annihilator
  `(I−√2S_2)(I−S_2)²` and its exact Mellin transform; the exact multiplicity-sensitive
  reverse-Rolle identity (PR #767); the `Ω(√Y)` atomic obstruction (PR #757); the
  Cauchy-determinant identity (PR #780). Each is correct and worth a short note.
- **Self-refutation.** The record contains many exact refutations of the project's own
  proposals, several of them structurally important (see §4.4). A research culture that
  retracts within hours is doing something right.

### 2.2 What is less impressive

- **Every unconditional theorem lives where the RH-sensitive term is trivially dominated,
  or is an exact identity.** SHARP `m ≥ 2` is the absolutely convergent region
  (`n^{−3/2}`); the First-Hermite wedge is where a phase-blind prime bound `qe^{q/4}` loses
  to the archimedean term `q^{−3/2}\log|x|`; Pick order ≤ 3 is real-axis data plus verified
  zeros; the Dickman corridor imports Vinogradov–Korobov; the Haar–Gram diagonal is the
  diagonal. None touches the critical exponent.
- **The conclusion-facing layer is a closed loop.** All 35 open nodes are RH-equivalent,
  harder than RH, or false (see §3). The "positive reserve" moves a target between these
  categories and never below RH.
- **Volume and vocabulary.** Roughly 1,000 claim files in the post-freeze wave, with
  ~12 differently named RH-implying gates in four days on one branch, "MAJOR
  UNCONDITIONAL" labels on the parallelogram law, Heisenberg's inequality, and
  inclusion–exclusion, and claim-ID collisions between concurrent branches (PRs #771/#774
  both define `T-107300`, `L-107300`–`L-107302`).
- **Imported records.** The "67.3% simple-zero record" (PRs #726/#731) is an import: the
  baseline 67.25% is the Alpöge–Furman theorem (arXiv:2608.13637, formally verified in
  the `anthropics/zeta-23-lean` repository); the project's own increment is `+1.1·10^{−6}`,
  it rests on an unformalized Gram-kernel bridge and an Arb certificate that was never
  re-run here, and one of its two "exact replays" (`experiments/X-105560-reviewed-record/verify.py`)
  computes the wrong constant (`1.17` for `H_0 = 0.6725`) and passes vacuously.

## 3. The structural diagnosis

The new packet `standalone/2026-09-01-fixed-detector-dichotomy/` proves the following
for every fixed zero-safe band kernel `K` (all kernels of the release qualify):

1. `∫_1^X (D_K)_- dt/t = X^{o(1)}` **⟺ RH**, verbatim. So the Mellin–Landau premise, in
   any of its forms (`FIXED_DETECTOR_NEGATIVE_MASS`, `FIVE_THREE_NEGATIVE_MASS`,
   `TAYLOR_CRITICAL`, `MWOC99910`, `CV`, `XD`), is RH and not an intermediate statement.
2. "`D_K ≥ 0` eventually" is decided by the real-pole main term `P_K(\log x)` against the
   zero-side oscillation `Σ_γ 2\Re(r_γ x^{iγ})`, `r_γ = K̂(iγ)/ζ'(ρ)`, through Ingham's
   inequality (reproved as L-109000, no linear independence needed):
   - no main term (the ratio-eight wavelet `G_μ`, and every "critical-zero-safe" kernel
     with an `s²` in its numerator): **false unconditionally** (R-109002);
   - bounded main term (the SHARP scalars, `c_0 = 2.054` and `1.803`): **false under LI**;
     the first 17,496 zeros already carry oscillation mass `3.22 > 2.05` (growing by about
     `0.9` per decade of zeros), so the unconditional refutation is a Kronecker-alignment
     computation of Kotnik–te Riele/Hurst type;
   - growing main term (rows 2 and 3 at `1.11\log X` and `0.41\log X`, the `5:3` scalar at
     `6.78\log X`, the 67-box at `7.58`): **RH plus a summability hypothesis on the zeros**,
     at least as hard as RH and not implied by RH.
3. Over `F_q[T]`, where RH is Weil's theorem for every character, the same cumulative
   detector is negative infinitely often for 128 of 193 quadratic characters over `F_3`
   (degrees ≤ 6), 440 of 505 with degree 7 included, 65 of 200 over `F_5`, 112 of 133
   over `F_7`. Positivity is a numerical accident of the central value against the
   residues. It is never a mechanism, even where RH is known.

The same diagnosis applies to the other routes: finite sections of the Pick kernel up to
order `k` are blind to zeros above height `≈ 2k/π` (PR #785's "finite-height cone" is
exactly this fact re-expressed on the prime side); the First-Hermite wedge ends where
primes `n ≍ (\log|x|)^4` start to matter and every step past it is RH; the
reverse-Rolle programme's every gate is, by the programme's own counterexamples
(`x²+1`, `c+\cos nt`, R-105203, R-107400), a new zero-count theorem in disguise.

**Two results in the post-freeze wave that change the graph.** PR #742 shows that the
registered half-divisor near-collision gate `HCNC` (the truncated-energy form of
L-103102) has energy `≥ c·2^{L/3}/L` on infinitely many dyadic blocks, because the
truncation exposes `m(U) = Σ_{n≤U}μ(n)/n = Ω(U^{−1/2−ε})`; the argument is stated modulo
one named lemma, but its mechanism is sound, and it makes `HCNC` and hence `BPOE`
false as registered. PR #719's R-103121 shows the "completed" owner/core source carries
a deterministic `−C_0√X\log\log X/\log X` term, which broke the `QPTI ⟺ BCI ⟺ HMO`
chain and, with it, the target of PR #751. Together with the dichotomy above, the entire
positivity wing of the open-cut inventory is now either RH, harder than RH, or false.

## 4. The post-freeze wave, programme by programme

Sources: five PR-level surveys with spot checks (reports in this session), the issue
threads, and my own reading of the load-bearing files. Confidence is high for the
structural verdicts and moderate for any single unread detail.

### 4.1 L-family programmes I–VI (#736–#741; PRs #751, #752, #756–#762, #771, #774–#779)

- The "beta" object is `μ` with a duplicated 67; every "beta RH criterion" is the Mertens
  criterion. PR #762's "one beta harmonic records the zero abscissa" is Titchmarsh §14.25.
- Programme I (Dirichlet completion) was never executed as stated: no `L(s,χ)` moment of a
  canonical detector appears. What appears is a finite Gram matrix `⊗_p(pI−J)` on residue
  sign-pairs, whose "leverage" `∏(p−1)/(p+1)` is linear algebra without a family.
- Programme II (function-field mirror) produced a large, correct body of Katz–Sarnak-style
  small-field statistics and symmetric-power representation algebra (PR #756's genus-2
  trace ladder is paper-sized if a specialist confirms it), but never ported `CV`, `XD`,
  `HCNC` or `BPOE`. Its own honest conclusion: Weil's theorem is imported, and purity plus
  a functional equation do not force a memberwise sign of any toy detector. The packet's
  §5 census makes this exact.
- Programmes III–V (GL(2) twists, trace formula, off-line-zero propagation) are empty:
  one synthetic deflation toy, one comment, nothing.
- Programme VI (atlas): real infrastructure (hashes, schemas, 600+ tests), never run
  against a zero problem.
- The shared-fibre line (#771/#774/#776/#778) rediscovered the standard obstruction in
  its cleanest form: character orthogonality writes the principal member as the family
  total minus the nonprincipal members; Weil controls the latter; the principal term is
  the original problem (L-108440, R-108450). PR #778's disposition is correct and should
  be applied to the still-open #776, #771, #774.
- The only statement in this wave that is not visibly a restatement is the Carleson-type
  square-function gate `PRIMCAR`/`COREWAVE` (PR #757/#760); its sibling `PRIMLS`,
  advertised as "deliberately stronger than RH", is RH-equivalent (under RH the coprime
  Möbius sums are `≪ x^{1/2+ε}m^{o(1)}` uniformly).

### 4.2 Stress tensor, common mother, F1 (#743, #746; PRs #713, #715, #718, #719, #727, #730, #751)

Chains of exact identities: rational multipliers on one kernel, Heisenberg and Poincaré
inequalities, Vaughan's identity, `λ∗λ = μ`, polarization, inclusion–exclusion on
`(ℤ/ℓ)^×`, Witt exponents, the `(P^1)^m` "Hodge–Riemann" identity `Σ_{i≠j}⟨w_i,w_j⟩ = −Σ‖w_i‖²`
for `Σw_i = 0`. No off-diagonal bilinear form is ever bounded. R-102501 admits the
stress-tensor determinant carries no arithmetic sign. The line from PR #719 to #751
(40k lines, three retracted RH closures) returned exactly to main's `OPEN.ARITH.XD`.

### 4.3 Xi reverse-Rolle and residue geometry (#744; PRs #716, #720, #724–#731, #767, #772, #773, #780)

Correct, elementary, sometimes elegant real-variable lemmas (the multiplicity-sensitive
reverse-Rolle identity, the Bezoutian residue diagonalization, the natural-window saddle
with residue rigidity, the Cauchy-determinant CTI). The reconstruction of Conrey's
functional is faithful (it reproduces 0.3474 and 0.7857 and gives `α_5 > 0.985`,
`α_{31} > 0.9995`). Every conclusion-facing gate is a zero-count theorem renamed. On the
"record": see §2.2; the honest statement is "67.25% is a formally verified external
theorem; the project adds an unverified `10^{−6}` lift".

### 4.4 Riemann structures and generalized L-objects (#763, #764; PRs #765, #766, #769, #770, #781–#785)

Competent commutative algebra (Segre coordinate rings, Gorenstein duality, a ternary-cube
Betti table, a rank-65 differential certified modulo two primes) with no contact with
zeros; a 2×2 Rankin–Selberg Schur complement presented as an "L-object" that fails
multiplicativity; a holonomy toy; "Architecture E" = Lagarias + Hermite–Biehler +
Nevanlinna–Pick + Widder + Pólya, with one useful bridge (`A_Φ = 4K_0`) and two useful
firewalls (`PF_∞` is not closed under sums; the innerness premise is RH). PR #781's
axiom-separation matrix is built from classical witnesses (non-Ramanujan graphs, deleted
Euler factors, Davenport–Heilbronn, wrong gamma factors) and says so.

### 4.5 Formal track (PRs #732–#735, #747–#750, #755, #761)

Sound and conservative. Wave two should target exact statements of all 139 claims, the
two missing Mellin propositions, and, above all, the classical equivalences (Weil
positivity, Li, Nyman–Beurling, Báez-Duarte) that would make the library useful outside
this repository. The Alpöge–Furman chain plus the project's bridge is the one place where
formalization could turn an import into a verified statement.

## 5. Distance to resolution, and confidence

There is no metric for distance to RH; the closest proxies are the ones the literature
actually moves: the proportion of zeros on the line (now 67.25%, Alpöge–Furman 2026),
the de Bruijn–Newman constant (`0 ≤ Λ ≤ 0.2`), the zero-free region, the Mertens
exponent, and the support radius for unconditional Weil positivity. This repository has
not moved any of them. My assessment:

- The reviewed release contains no statement that is both easier than RH and unproved:
  confidence ≈ 95% (I read the load-bearing lemmas myself; the packet proves the
  arithmetic case in general).
- The post-freeze wave contains no such statement either, with `PRIMCAR` the only candidate
  and no evidence beyond a random-sign heuristic: confidence ≈ 85–90% (PR-level surveys
  with spot checks, not line-by-line).
- Probability that continuing the present programmes (reformulate, name a gate, attack the
  gate with identities) produces a proof of RH: well under 1%. This is not a statement
  about effort or intelligence; it is what the dichotomy says. Positivity and negative-mass
  targets on fixed detectors cannot be easier than RH, finite sections of positive-real
  criteria cannot see high zeros, and family averages cannot individualize the principal
  member without an input that is itself GRH-strength.
- Where the project genuinely is: it has an excellent map of one basin of dead ends, an
  honest ledger, and formal infrastructure. That is a durable contribution to the *method*
  of agentic mathematics. It is not progress on RH.

## 6. Routes forward — macro

1. **Install a non-triviality gate for research PRs.** A PR must state, in one sentence,
   which estimate it proves that was not known, and in which regime its RH-sensitive term
   is not trivially dominated; or which registered node it refutes; or which quantitative
   proxy it improves. An exact identity, a renamed gate, or a positivity target on a fixed
   detector no longer counts as progress. This single rule would have removed most of the
   post-freeze volume.
2. **Retire the closed loop.** Downgrade `HCNC`, `BPOE` (PR #742), pointwise `G_μ` and the
   pointwise SHARP tail (this packet) to `FALSE`/`FALSE_UNDER_LI`; relabel every
   negative-mass node as an alias of RH; mark the growing-main-term positivity nodes as
   "RH + summability". Run the same pole-exposure/Ingham audit on the remaining
   energy-type gates (`SACF`, `C4MBI` boundary, `CFBB`, the Perron rows, `FCHD67`); I
   expect several to be false as stated.
3. **Redirect compute to proxies where agents can actually win.**
   - Proportion of zeros on the line / simple: the target is now to beat 67.25% by a
     mollifier or Gram-kernel optimization that is honestly verified end to end. This is
     computer-algebra-heavy work where the project's tooling is a real advantage.
   - The de Bruijn–Newman constant: Polymath 15's `Λ ≤ 0.2` used a verification height near
     `6·10^{10}`; Platt–Trudgian's `3·10^{12}` plus the same barrier method should give a
     smaller bound (my rough scaling estimate is in the `0.17` range; it needs a real
     computation, and the gain per compute is logarithmic).
   - Explicit zero-free regions and explicit `M(x)` bounds: unglamorous, publishable,
     and the kind of certified computation the repository already knows how to review.
   - Unconditional Weil positivity for larger support: the first prime is the frontier;
     the archimedean-only region is where every "unconditional region" in this repository
     lives, and pushing past `\log 2` with the prime-2 term as a rank-one perturbation is a
     finite, well-posed analytic problem with a known literature (Yoshida, Burnol,
     Connes–Consani).
4. **Anchor the structural programme (#763) in existing frameworks, and test it where RH is
   a theorem.** The only spectral realizations with published theorems are the
   Connes–Consani scaling-site/prolate constructions and Deninger's foliated dynamics; any
   candidate "Riemann structure" should first reproduce Weil's proof for a curve over
   `F_q` (Hodge index on `C×C`) inside its own formalism before making number-field
   claims. Objects built from the zeros, and positivity obtained by choosing an inner
   product, should be rejected at intake, as the issue already says.
5. **Aim the Lean track at public goods**: the classical equivalences, the explicit
   formula with a fixed normalization, the Alpöge–Furman bridge. A formal library of
   RH-equivalences would outlive every research branch in this repository.
6. **Shrink the language.** Adopt the glossary above (or a better one) as a mandatory
   translation column in every claim file. Most of the repository's difficulty of review
   is self-inflicted.

## 7. Routes forward — for me

What I did in this session: read the release's load-bearing mathematics, surveyed every
post-freeze PR with spot checks, and proved and deposited the dichotomy packet with its
numbers and the function-field control.

What I would do next, in order of expected value:

1. **Finish the audit.** Apply the pole-exposure/Ingham test to `SACF`, the `C4MBI`
   boundary sign, `CFBB`, the joint Perron rows, and `FCHD67`, and produce a single table
   with each node's exact status (RH / RH+hypothesis / false). Two days of work; it
   would leave the open-cut inventory honest to the last row.
2. **Make the SHARP refutation unconditional.** Align the phases of the first few
   thousand zeros (LLL/Kronecker) to exhibit `u` with `𝒫_T(u) < −2.054`; with the mass
   already at `2.64` this is a bounded computation, of the kind done for
   `\limsup M(x)/√x`.
3. **Verify the only record.** Read the Alpöge–Furman zero-side construction, check the
   two prose bridges the project's `+10^{−6}` lift relies on (the Montgomery–Taylor Gram
   kernel and the `(N−S)/2` positive-index budget), fix `verify.py`, re-run the Arb
   certificate, and, if it survives, formalize the bridge on top of Zeta23. That would
   convert the repository's one potential result into a verified one.
4. **A feasibility note on `Λ`.** Reproduce the Polymath 15 barrier computation at the
   Platt–Trudgian height and report the resulting bound; if it lands near `0.17`, it is
   the first quantitative proxy this project would have moved.
5. **A function-field reproduction of Weil's proof in explicit-formula language**, as the
   intake test for #763: which finite-dimensional positivity is used, where the
   diagonal and the graph of Frobenius enter, and what the number-field object would
   have to be. Not a proof strategy; a way to stop the structural programme from
   restating positivity criteria.

What I will not do: propose another gate. I have no route to RH, and I do not believe
anyone in this repository has one; the repository's own firewalls say why, and the
packet proves it for the arithmetic wing.

## 8. Housekeeping

- Claim-ID collisions: PRs #771 and #774 both define `T-107300`, `L-107300`–`L-107302`.
- `experiments/X-105560-reviewed-record/verify.py` (PR #726) computes `H_0` with the
  wrong sign convention (`1 − Σ` instead of `1/2 − Σ`) and passes vacuously.
- PR #776 should carry PR #778's disposition; PRs #771, #774 likewise.
- The pointwise-positivity firewall in the wavelet packet ("`G_μ(4) < 0`") should be
  replaced by R-109002 ("negative for arbitrarily large `X`, unconditionally").
- `OPEN_CUTS.md` rows for `HCNC`, `BPOE`: pending PR #742's lemma, mark
  `FALSE_AS_REGISTERED (modulo W-pinch lemma)`.
