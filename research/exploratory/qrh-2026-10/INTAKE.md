# Intake: the October 2026 quasi-Riemann-hypothesis manuscripts

```text
Status: IMPORTED (external, unreviewed claims) + EXACT_RATIONAL ledger check of their stated arithmetic
Scope: global zero-free half-plane claims for Dirichlet / Q(sqrt(-3)) Hecke L-functions (NOT RH)
Exact sources or dependencies:
  [OAI]  OpenAI, "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", 30 Sep 2026,
         github.com/openai/math, preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf
         (fetched 2026-10-10; 196 pp.; sha256 recorded in scripts/SOURCES.txt)
  [K]    S. Kintali, "A Short Proof of the Quasi-Riemann Hypothesis", 7 Oct 2026,
         shivakintali.github.io/papers/QRH.pdf (fetched 2026-10-10; claims Re s > 47/48)
What was actually run: scripts/ledger_check.py (53 exact checks of the rational arithmetic and
  polynomial identities in [OAI] Sections 10-20 and [K] Section 4.4): 53/53 PASS.
Smallest remaining gap: every lemma of [OAI]/[K] (reflection, large sieves, moment inductions,
  zero detector) is unreviewed here; the ledger only certifies that the stated lemma outputs
  combine to the stated margins.
```

> **Prior import.** [PR 908](https://github.com/GettysburgResearch/riemann/pull/908) imported
> openai/math@adc7f124 family 003 byte-exactly on 2026-10-07. That includes this 7/8 paper (same
> sha256 prefix `8fe93046`), the Oct 5 11/12 companion, the Oct 1 Landau–Siegel paper, and the Lean
> closure. [PR 909](https://github.com/GettysburgResearch/riemann/pull/909) and
> [PR 910](https://github.com/GettysburgResearch/riemann/pull/910) build on it. This intake is an
> independent reading; the Kintali paper has no prior repository coverage.

**Nothing in this file is a repository result about RH.** The manuscripts claim a zero-free
*half-plane* `Re s > 7/8`; RH asks for `Re s = 1/2`. Per the repository rules, any downstream use
below must carry the imported hypothesis explicitly:

> **(QRH-IMPORT)** every Dirichlet L-function, including ζ, has no zero with `Re s > 7/8`
> ([OAI] Theorem 1.1; unreviewed, external, Lean status partial per release notes).

## 1. Exact claimed statements

**[OAI] Theorem 1.1.** Every finite-order Hecke L-function over `F = Q(sqrt(-3))` has no zero in
`Re s > 7/8`; the same holds for every Dirichlet L-function, including ζ. A pole at `s = 1` for a
principal character is allowed; the boundary line is not included.

**[OAI] Theorem 3.1 (Part I).** The same with `11/12` in place of `7/8`.

**[OAI] Corollary 1.2.** `n(p) ≤ C (log p)^A` for the least quadratic nonresidue (via the
weak-GRH theorem of Bhargava–Ivanyos–Mittal–Saxena with ε = 7/16), and deterministic
polynomial-time square roots mod p.

**[K] Theorem 1.** ζ, all Dirichlet L-functions and all finite-order Hecke L-functions over F are
zero-free in `Re s > 47/48`. [K] states it adapts the probe/Mellin framework of [OAI] Sections 4, 6, 7,
with the quadratic Hecke large sieve (Goldmakher–Louvel) and a published Hecke zero-density
estimate replacing [OAI]'s sextic large sieve and moment inductions.

## 2. Architecture (both manuscripts)

1. **Family supremum.** `β* = sup({1/2} ∪ {Re ρ : L_F(ρ,η)=0, η primitive finite-order over F})`.
   The whole family is needed even for ζ, because Poisson summation produces Hecke twists.
2. **Continuation criterion ([OAI] Prop. 2.1).** For an affine `C(s) = s + c`, if each target η has a
   probe `J_η(Z)` with `|J_η| ≪ Z^{C(σ0)+ω}` (low estimate) and `|J_η − f_η| ≪ Z^{C(β*)−σ}` (high
   estimate), where `f_η(Z) = (2πi)^{-1}∫ Z^{C(s)} e^{(s−5/6)^2} H_η(s)/L^S_F(s,η) ds` and
   `|H_η − 1| ≤ 1/2` on `Re s > σ0`, with ω < β*−σ0 and σ > 0 uniform in η, then β* ≤ σ0.
   The Mellin transform of `f_η` continues `1/L` a uniform distance left of β*, contradicting the sup.
3. **Probe.** A smoothed average of cubic-theta Fourier coefficients (cubic Gauss sums over
   `Z[ω]`) against sextic residue symbols, with three scales `X = Z^{lx}`, `Y = Z^{ly}`, `Z`.
4. **Low side.** Cubic-theta *reflection* (Dunn–Radziwiłł explicit cusp expansions) turns the
   completed row into a dual sum; a quadratic (Part I) or quadratic–cubic (Part II) large sieve bounds
   the row energy; an additive (Gram) large sieve bounds the other factor; Cauchy–Schwarz combines.
5. **High side.** Poisson summation in the averaging variable expresses the probe as a sum over
   sixth-power-free rows `u` of `ζ_F(6z) L(w, χ_•(u)) H_{η,u} / L(x, ηχ_•(u))`. The row `u = 1`
   contains `1/L(x,η)`; its double residue (`w = 1`, `z = 1/6`) is the principal signal.
   Non-principal rows are moved to `Re x = a + 16e`, `Re w = 1−a−6e`, `Re z = 17/50`, binned by the
   real part `a` of their rightmost zero below a height `T1 = Z^τ`; a truncated-inverse zero
   detector produces large Dirichlet-polynomial witnesses for each binned row, and large-sieve /
   moment estimates count such rows.
6. **Part II refinements.** Prime "compensation" slots of total log-length `ℓ = 1/6`, asymmetric
   scales `lx = 17/48`, `ly = 23/48`, an inverse moment with prime factors (Lemma 17.1), a
   fourth moment with short prime factors (Lemma 18.1, uses `κ = 2β*−1` and needs `κ ≥ 3/4`),
   sixth-power amplification (slope `α = 5/6`), and a detector parameter `t ∈ [1, 3/2]`.
7. **Transfer.** `L_F(s, χ∘N) = L(s,χ) L(s,χχ_{-3})` up to finitely many Euler factors.

## 3. Where the constants come from (verified bookkeeping)

| Constant | Origin | Verified here |
|---|---|---|
| 11/12 (Part I) | low estimate `Z^{1/4}` and `C_I(s) = s − 2/3`; high margin `1021/25000` is slack | ledger |
| 7/8 (Part II) | `C_II(s) = lx/2 + s − 1 + h/6 = s − 11/16` and low estimate `Z^{lx/2 + b/12} = Z^{3/16}` | ledger |
| Part II high margin | Lemma 20.2: `−E* ≥ 49/440640` (true minimum ≈ `2.28·10⁻⁴` at δ ≈ 0.387, x = 1/2) | identity (20.9) exact; minimum numeric |
| 47/48 ([K]) | `max_a (a + R(a)/2 − 1/3) = 29/30` with `R(a) = min(1, 5(1−a))`, plus a `1/80` margin | ledger |

In both parts **the boundary is set by the low estimate**; the high side only constrains the
admissible geometry (Section 2 of [THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md)).

## 4. Dependencies imported by [OAI] (not checked here)

Patterson / Kubota cubic theta; Dunn–Radziwiłł unconditional cusp expansions (Sec. 5, App. A);
Goldmakher–Louvel quadratic Hecke large sieve; Blomer–Goldmakher–Louvel higher-order norm
recursion; Heath-Brown cubic large sieve; Hecke functional equation; prime counting in a fixed ray
class (Thorner–Zaman); Bhargava–Ivanyos–Mittal–Saxena (only for Corollary 1.2).
[K] additionally imports a general Hecke zero-density estimate ([K] ref. [4], Lemma 3.3).

## 5. Known misreadings to avoid

* QRH is **not** RH and does not place any zero on the critical line.
* "Lean-verified" in press coverage refers to a partial formalization catalog; this intake
  verified only rational arithmetic.
* [K] is weaker (47/48 > 7/8) and is not an independent confirmation of [OAI]'s Part II;
  it reuses [OAI]'s probe framework.
* The Hecke family over `Q(sqrt(-3))` is essential to the argument; it is not a special case of a
  ζ-only argument.
