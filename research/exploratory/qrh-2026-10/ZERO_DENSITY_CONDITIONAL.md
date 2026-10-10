# Zero-density estimates under an imported zero-free half-plane Re s > 7/8

```text
Status: CONDITIONAL on QRH-IMPORT (external, unreviewed) / reconnaissance
Scope: zero counts N(sigma,T) as T -> infinity, 1/2 < sigma < 7/8
Exact sources or dependencies: QRH-IMPORT (INTAKE.md; [OAI] Thm 1.1, unreviewed); ANTEDB =
  Analytic Number Theory Exponent Database, github.com/teorth/expdb at commit
  c8eda5e4f1f51024b6cbf70c7bef6c33da74c691 (blueprint ch. "Zero density", "Zeta large values",
  Cor. 11.7 = Lemma zero-from-large + power lemma); literature exactly as encoded there:
  Ingham 1940, Huxley 1972, Jutila 1977, Heath-Brown 1979, Ivic 1979/80/84, Bourgain 2000/2002,
  Pintz 2023, Chen-Debruyne-Vindas 2024, Guth-Maynard 2024, Tao-Trudgian-Yang 2024/25
  (arXiv 2501.16779); Titchmarsh Sec. 14.2; Bourgain mu(1/2) <= 13/84.
What was actually run: scripts/zd_antedb_qrh.py (ANTEDB Python, sandboxed, exact rationals:
  mu envelope with/without the QRH point; Cor. 11.7 runs with/without QRH zeta data; aggregate
  best-known table; 4 of 6 interval pairs completed, all 0 changes) and
  scripts/zd_short_intervals.py (float grid search). Not reviewed.
Smallest remaining gap: no argument here shows that QRH can NOT improve A(sigma) on [1/2,7/8);
  the one unexamined route is energy/double-zeta-sum large-value estimates at heights
  T > N^{tau*}, tau* = 92791/37936 ~ 2.446 (Sec. 7).
```

RH remains unproved; nothing here bears on `Re ρ = 1/2`. **(QRH-IMPORT)** is the unreviewed external
claim that ζ and every Dirichlet `L(s,χ)` have no zero in `Re s > 7/8`. Every statement below marked
*conditional* depends on it.

## 0. Answer

1. **Rigorous-conditional:** `N(σ,T) = 0` for `σ > 7/8`, i.e. `A(σ) = 0` on `(7/8, 1]`. Unconditionally
   the best is `3/(10σ−7)`, `24/(30σ−11)`, Bourgain–TTY, then Pintz near 1.
2. **On `[1/2, 7/8)` no entry beats the best unconditional `A(σ)`.** The mechanism is explained by
   four short lemmas (Sec. 3). Every ANTEDB run that completed gave identical `A(σ)` with and without
   QRH data at every sampled point (Sec. 4; two literature-set intervals did not finish).
3. **The density-hypothesis range stays `σ ≥ 25/32`.** QRH does not extend it.
4. **Primes in short intervals:** the Hoheisel–Guth–Maynard exponent `17/30` and the almost-all
   exponent `2/15` are unchanged. What is new (conditional) is a **power-saving** error term for every
   `θ > 17/30` (Sec. 6).

*Prior work.* This extends the one-line remark in [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md)
§1.4 ("nothing follows directly on `[1/2, 25/32]`") to all of `[1/2, 7/8)` and adds evidence for it. The `M(x)`
and `m(x)` exponent tables in PR 908 (`standalone/2026-10-07-openai-quasi-riemann-import/CONDITIONAL_BRIDGES.md`,
ref `pr908` = 31c706bb) and the consequences in branch `claude/openai-math-riemann-analysis-w5copg`
(`standalone/2026-10-07-openai-quasi-rh/README.md` §5, bd670c92) are not repeated here. Neither treats
`N(σ,T)`.

## 1. What QRH-IMPORT actually supplies

**(Q1)** There are no zeros in `Re s > 7/8`. The boundary line is allowed, so `N(7/8,T)` keeps its
unconditional bound.

**(Q2)** `μ(σ) = 0` on `[7/8,1]`. This follows from the Titchmarsh §14.2 argument for `σ > 7/8` and
from continuity of the convex function `μ` at `7/8`.

**(Q3) Exact μ envelope.** `part mu` takes every μ point that ANTEDB encodes: literature μ bounds,
`μ(l−k) ≤ k` for each of its 61 exponent pairs, the functional equation, and the trivial points. It builds
the exact lower convex hull. Adding the point `(7/8, 0)` changes the hull on `[1/2,1]` to the vertices

`(1/2, 13/84)`, `(α*, μ*) = (88225/153852, 4742/38463)`, `(7/8, 0)`, `(1, 0)`,

so `μ_QRH(σ) = μ*(7/8−σ)/(7/8−α*) ≈ 0.4088(7/8−σ)` on `[α*, 7/8]`. This is slightly better than the
chord `(26/63)(7/8−σ)` through Bourgain's point alone.

| σ | μ unconditional (ANTEDB hull) | μ under QRH | (26/63)(7/8−σ) |
|---|---|---|---|
| 0.60 | 0.112532 | 0.112429 | 0.113492 |
| 0.70 | 0.072546 | 0.071546 | 0.072222 |
| 0.75 | 0.056512 | 0.051104 | 0.051587 |
| 0.80 | 0.041509 | 0.030662 | 0.030952 |
| 0.85 | 0.027736 | 0.010221 | 0.010317 |
| 0.875 | 0.021450 | 0 | 0 |

`μ(1/2)` is **not** improved. Phragmén–Lindelöf between `(1/8, 3/8)` and `(7/8, 0)` gives only `3/16 > 13/84`.

**(Q4) Zeta sums.** Write `σ_max(τ)` for the infimum of the exponents `s` with `Σ_{n∈I⊂[N,2N]} n^{−it} ≪ N^{s+o(1)}`
for `|t| ≍ N^τ`. ANTEDB's Cor. `lvz-mu` gives `σ_max(τ) ≤ min_α (α + τμ(α))`. Under QRH:

`σ_max^QRH(τ) = min(σ_max^unc(τ), 7/8)`, and this differs from the unconditional value only for
`τ > τ* = (7/8−α*)/μ* = 92791/37936 ≈ 2.446`, i.e. for sums of length `N < T^{0.409}`.

`part mu` checks this identity exactly at nine values of τ. It is Lemma 1 below.

**(Q5) Moments.** Gabriel/Hölder interpolation between the unconditional moments on `Re s = α₁` and
the Lindelöf bound at `7/8+` gives `∫_T^{2T}|ζ(α+it)|^{m(α₁)(7/8−α₁)/(7/8−α)} ≪ T^{1+ε}`.

## 2. How the machinery uses ζ

ANTEDB Cor. 11.7 (Lemma zero-from-large: Heath-Brown-type zero detection with smoothing,
approximate functional equation, power lemma) states that for every `τ₀ ≥ 2`

`A(σ)(1−σ) ≤ max( sup_{2≤τ<τ₀} LV_ζ(σ,τ)/τ , sup_{τ₀≤τ≤2τ₀} LV(σ,τ)/τ )`.

Here `LV` is the large-value exponent for **arbitrary** 1-bounded Dirichlet polynomials, which come from
the mollified sums, and `LV_ζ` is the exponent for **zeta sums** `Σ_{n∈I} n^{−it}`. The large-value level
is the **same σ** in both. Every named estimate in the table is a choice of `τ₀` plus inputs of three
kinds:

* (i) LV theorems: mean value, Huxley, Jutila, Heath-Brown, Bourgain, Guth–Maynard.
* (ii) Exponent pairs or β bounds, which are general phases.
* (iii) Zeta information through `σ_max` (Halász off-diagonals, `LV_ζ = −∞` regions) and through moments
  (Heath-Brown's twelfth moment gives `LV_ζ ≤ 2τ+6−12σ`).

QRH says nothing about (i) or (ii). It is information about ζ and `L(s,χ)` only.

## 3. Why nothing moves below 7/8 (rigorous lemmas, framework-relative conclusion)

**Lemma 1 (envelope).** Let `c` be a number and τ fixed. "There is an α with `α + τμ_QRH(α) < c`" holds
iff "there is an α with `α + τμ_unc(α) < c`" holds or `c > 7/8`.

*Proof.* `α + τμ` is a linear functional, and the QRH hull is the convex hull of the unconditional hull and
`{(σ,0): σ ≥ 7/8}`. The minimum of a linear functional over a convex hull is attained on the generating
sets. ∎

**Lemma 2 (zeta large values).** For `σ < 7/8` and every τ, QRH adds no `LV_ζ(σ,τ) = −∞` statement. For
`τ ≤ τ*` it adds none at all, because there `σ_max^unc(τ) ≤ 7/8` already.

*Proof.* `lvz-mu` together with Lemma 1. The reflection identity `lvz-basic(iv)` maps QRH information
at `(σ', τ)` with `σ' > 7/8` to levels `1/2 + (σ'−1/2)/(τ−1)`. For `τ ≤ 2` those levels are at least
`σ' > 7/8`. The image of `τ > 2` has τ-coordinate below 2, which Cor. 11.7 never uses. ∎

**Lemma 3 (moments).** A moment bound `∫|ζ(α+it)|^m ≪ T^{1+ε}` yields
`LV_ζ(σ,τ) ≤ τ − m(σ−α)` (respectively `2τ − m(σ−α)` for the twelfth moment's `T²`). The QRH-interpolated
moment on line `α > α₁` gives `τ − m₁(7/8−α₁)·g(α)` with `g(α) = (σ−α)/(7/8−α)`. For `σ < 7/8`, `g` is
strictly decreasing, so this is weaker than the `α₁` bound itself. ∎

**Lemma 4 (Halász–Montgomery off-diagonal).** Raising to powers and Huxley subdivision leave the
condition scale-free. A Halász bound `LV ≤ 2−2σ` on a height range needs `σ_max(τ) < 2σ−1`. QRH changes
`σ_max` only to `7/8`, which matters only if `2σ−1 > 7/8`, i.e. `σ > 15/16`, where there are no zeros
anyway. This also kills the "Halász–Turán near the edge" mechanism, the analogue of how
Vinogradov–Korobov `μ(σ) ≪ (1−σ)^{3/2}` gives `A(σ)(1−σ) ≪ (1−σ)^{3/2}` near 1. Near `σ = 7/8` the
threshold `2σ−1 ≈ 3/4` lies below the QRH cap `7/8`.

**Conclusion (conditional on QRH, relative to Cor. 11.7).** Take inputs (i)–(iii) from any unconditional
set and add every zeta statement derivable from QRH by `lvz-mu`, interpolated moments, or reflection. The
resulting `A(σ)` on `[1/2, 7/8)` equals the unconditional one. In the human-proof form (blueprint
Cor. 11.8, `A = 3/τ₀`), `A ≥ 12/7` on `[1/2, 7/8]` forces `τ₀ ≤ 7/4`. So ζ data are needed only at
`τ < 4τ₀/3 ≤ 7/3 < τ*`, where QRH adds nothing (Lemma 2). The Guth–Maynard and Ingham ranges even have
a vacuous ζ range (`4τ₀/3 < 2`).

*Ingham's route.* `A ≤ 2 + 4μ(1/2)` uses only `μ(1/2)`, which is unchanged. Its line-α variants are
covered by `lvz-mu` and Lemma 1.

## 4. Computation (ANTEDB, sandboxed)

ANTEDB was cloned to the scratchpad, its Python was read and grepped (no network, subprocess or
eval; it only opens `references.bib`), and it was run with `python -I` from a separate directory. The
environment needed `pycddlib 2.1.8` (built against system GMP) and matplotlib.

A **compatibility shim** in `zd_antedb_qrh.py` makes `sympy.real_roots` return `[]` for expressions
containing `±∞`. These come from ANTEDB's `±∞` default in `RationalFunction.max/min`; under sympy 1.14 they
otherwise raise an error. Infinite candidates never win a max or min, so this only coarsens cell
refinement. The count is printed.

`part zd` runs `lv_zlv_to_zd` (Cor. 11.7, `τ₀ = 3`). The baseline is the unconditional μ hull's
`lvz-mu` regions. The QRH run swaps in the QRH hull, which includes `μ(7/8) = 0`. Two input sets:

* **classical:** mean value plus powers k = 2..5.
* **literature:** additionally Huxley, Heath-Brown, Guth–Maynard, Bourgain-optimized, Jutila k ≤ 3,
  Heath-Brown's twelfth-moment `LV_ζ`, and β bounds from the pairs `(3/40, 31/40)` and `(13/84, 55/84)`.

| input set | σ interval | sampled σ (of 23) where QRH changes the derived A |
|---|---|---|
| classical | [0.51, 0.70], [0.70, 0.80], [0.80, 0.875] | 0, 0, 0 (e.g. σ = 0.8031: 2.5132 both) |
| literature | [0.51, 0.70] | 0 |
| literature | [0.70, 0.80], [0.80, 0.875] | **not completed**: the [0.70, 0.80] run exceeded 15 CPU-min and was cut off |

Shim events: 4–56 per run. Log: scratchpad `zdwork/zd_run.log` (not committed). Lemmas 1–2 predict
the two missing literature cells. They are not computational evidence.

These framework values with a fixed `τ₀ = 3` are **not** the best-known bounds: the published ones use
σ-dependent `τ₀` and other inputs. The runs test **invariance** under QRH and do not reproduce the table
below. `σ > 7/8` was not run. There the QRH zeta region is `{ρ = 0}`, which ANTEDB's clipping treats as
empty and rejects, and QRH gives `N = 0` directly.

## 5. Table

`D(σ) = A(σ)(1−σ)`, so `N(σ,T) ≪ T^{D(σ)+ε}`. The best-known column comes from ANTEDB's aggregate of
literature plus TTY (`part best`, which matches the blueprint table and excludes Kerr's unpublished
preprint).

| σ | best known A(σ) [source] | QRH-conditional A(σ) | D(σ) under QRH | source of change / status |
|---|---|---|---|---|
| 0.55 | 2.0690 [Ingham 3/(2−σ)] | 2.0690 | 0.931 | none (Lemmas 1–4; runs) |
| 0.60 | 2.1429 [Ingham] | 2.1429 | 0.857 | none |
| 0.65 | 2.2222 [Ingham] | 2.2222 | 0.778 | none |
| 0.70 | 2.3077 = 30/13 [Ingham = Guth–Maynard] | 2.3077 | 0.692 | none; LV-only (ζ range vacuous) |
| 0.75 | 2.2222 [GM 15/(3+5σ)] | 2.2222 | 0.556 | none; LV-only |
| 0.76 | 2.2059 [GM] | 2.2059 | 0.529 | none |
| 0.77 | 2.1053 [Ivić 6/(5σ−1)] | 2.1053 | 0.484 | none (ζ input at τ < τ*) |
| 7/9 | 2.0250 [Ivić/Heath-Brown 9/(7σ−1)] | 2.0250 | 0.450 | none |
| 25/32 | 2.0000 [TTY 9/(8(2σ−1)); Bourgain DH] | 2.0000 | 0.4375 | none; DH range unchanged |
| 0.80 | 1.8750 [TTY; 3/(2σ)] | 1.8750 | 0.375 | none |
| 0.825 | 1.8182 [Bourgain 2002 3/(2σ)] | 1.8182 | 0.318 | none |
| 0.85 | 1.7647 [3/(2σ)] | 1.7647 | 0.265 | none |
| 0.87 | 1.7241 [3/(2σ)] | 1.7241 | 0.224 | none |
| 7/8 | 1.7143 = 12/7 [3/(2σ) = 3/(10σ−7)] | 12/7 | 3/14 | none (boundary line allowed) |
| 0.90 | 1.5000 [CDV 24/(30σ−11)] | **0** | 0 | QRH directly (rigorous-conditional) |
| 0.95 | 1.0924 [Bourgain-opt., TTY] | **0** | 0 | QRH directly (rigorous-conditional) |

**Status of entries.** The `σ > 7/8` zeros are rigorous-conditional (Q1). The "none" entries are
rigorous-conditional as statements about the Cor. 11.7 framework with inputs (i)–(iii) (Sec. 3). The
blanket claim that *no* method improves them is **heuristic**: it is a survey statement, not a theorem.

**Edge discontinuity.** `D(7/8⁻) = 3/14` but `D(7/8⁺) = 0`. No known mechanism forces `D(σ) → 0` as
`σ ↑ 7/8` (Lemma 4). A Jensen-formula sketch with `μ_QRH` gives only `O(log T)` zeros per unit height
near `7/8`, which is no gain (heuristic).

## 6. Density hypothesis, short intervals, L-functions

**DH range.** It remains `σ ≥ 25/32` (Bourgain 2000). TTY's `9/(8(2σ−1))` equals 2 exactly at 25/32.
Below 25/32 the binding constraints are LV estimates for general polynomials (Guth–Maynard, Ivić/TTY
mixes), or ζ data at `τ < τ*` and level `σ < 7/8`, where QRH adds nothing (Lemmas 1–3). DH follows from
Lindelöf at 1/2 (Ingham) or from Montgomery's LV conjecture. QRH supplies neither.

**Primes in short intervals** (`zd_short_intervals.py`; conditional; grid search, not certified). The
standard explicit formula gives

`ψ(x+h) − ψ(x) − h ≪ h x^{ε} [x^{−η} + max_{1/2 ≤ σ ≤ Θ} x^{(σ−1)+(1−θ+η)D(σ)}]`

with `h = x^θ` and `T = x^{1−θ+η}`. QRH sets `Θ = 7/8` but leaves `sup_{[1/2,7/8]} A = 30/13` (attained
at `σ = 0.7`). So the asymptotic still needs `θ > 17/30`, and almost-all intervals still need
`θ > 2/15`. **New:** for each `θ > 17/30` the saving is a power `x^{−δ(θ)}`, compared with a VK-type
`exp(−c(log x)^{1/3−})` unconditionally.

| θ | 0.57 | 0.60 | 0.65 | 0.70 | 0.75 | 0.80 | 0.875 | 0.90 | 1 |
|---|---|---|---|---|---|---|---|---|---|
| δ(θ) ≈ | 0.0013 | 0.0136 | 0.0339 | 0.0500 | 0.0588 | 0.0675 | 0.0808 | 0.0852 | 0.1029 |
| RH: θ−1/2 | 0.07 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.375 | 0.40 | 0.50 |

For comparison, QRH alone gives `ψ(x) = x + O(x^{7/8+ε})`, i.e. saving `1/8` at `θ = 1`. The grid
value `0.1029` there is a weaker artifact of using the density bound.

**Dirichlet L-functions.** QRH gives `Σ_{χ mod q} N(σ,T,χ) = 0` for `σ > 7/8`. Below that, the
same Lemmas 1–4 apply to `L`-sums, using `L(σ+it,χ) ≪ (q(|t|+2))^{ε}` for `σ > 7/8` uniformly. So
family density exponents are unchanged on `[1/2, 7/8)`. Linnik-type bounds are not improved
(CONDITIONAL_CONSEQUENCES §1.4).

## 7. Smallest remaining gap

The only place QRH supplies ζ information that is unavailable unconditionally is short zeta sums
`N < T^{1/τ*}`: they have no values above `N^{7/8}` (Q4). Large-value estimates built on **additive
energy and double zeta sums** count pairs `(t, t')` by the size of `|Σ n^{i(t−t')}|`. ANTEDB's
energy-region machinery (Heath-Brown, Bourgain, Guth–Maynard) could in principle use that cap at heights
`T > N^{2.446}`.

Guth–Maynard's estimate is applied at `τ ≤ 6/5`, where the cap is vacuous. Whether *some* energy-based
`LV(σ,τ)` at `τ > τ*` beats the power-lemma transfer at levels `σ ≤ 25/32` was **not** tested. The test
would insert the cap only into the double-zeta-sum lemma, because it is not an exponent pair for general
phases, and then recompute.
