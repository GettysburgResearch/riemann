# Consequences of an imported zero-free half-plane for this repository's programmes

```text
Status: PROPOSED (native graded lemma, Sec. 2) + CONDITIONAL on QRH-IMPORT (Secs. 1, 3) + survey
Scope: conditional / quantitative; nothing here proves or approaches RH (target exponent stays 0)
Exact sources or dependencies: QRH-IMPORT (INTAKE.md); Titchmarsh, Theory of the Riemann
  Zeta-Function, 2nd ed., Sec. 14.2 argument; Bourgain, JAMS 30 (2017) mu(1/2) <= 13/84;
  de Bruijn (1950) strip theorem; repository Mellin route (research/integrated/CURRENT_RESULTS.md#mellin,
  reviews/C/pass4-math-completion/proofs/MELLIN_ANALYTIC_GAPS.md); R15 adapter (reviews/D-final/REPAIRS.md).
What was actually run: no computation; proofs below are short adaptations, not reviewed.
Smallest remaining gap: each RH-equivalent premise in the repo needs exponent 0; QRH-IMPORT gives 3/8.
```

> **Status update (10 Oct 2026, end of wave).** The ζ-part of QRH-IMPORT, `ζ(s) ≠ 0` for
> `Re s > 7/8`, is now also a Lean theorem about Mathlib's `riemannZeta`. Lean's kernel accepted it
> through comparator, using only the three standard axioms ([LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md),
> Addenda A–B, where the trust assumptions are listed). The Dirichlet version is axiom-clean too.
> * Statements below that use only `H(7/8)` for ζ are conditional on accepting the comparator
>   check, not on the unreviewed manuscript text.
> * Statements that use `H(7/8)` for Dirichlet `L`-functions rest on the `#print axioms` check
>   (comparator status: LEAN_BUILD_ATTEMPT Addendum C).
> * The classical derivations they rest on are still imported or PROPOSED as labelled.
> * Statements that need the Hecke family or the Oct 5 claim are unchanged.


> **Prior work.** Most of Sections 1.3 and 3 already appear in branch
> `claude/openai-math-riemann-analysis-w5copg`
> (`standalone/2026-10-07-openai-quasi-rh/README.md` §§4–5) and in
> [PR 908](https://github.com/GettysburgResearch/riemann/pull/908) `CONDITIONAL_BRIDGES.md`.
> That includes the fixed-detector bound `N_F(Y) ≪ Y^{3/8+ε}`, the converse direction of Lemma G
> below. Cite those for the overlapping items.
>
> New here:
> * the *forward* graded implication (Lemma G: premise exponent θ ⇒ no zero right of `1/2 + θ`);
> * the corrected de Bruijn–Newman normalization (`9/32`, a non-improvement);
> * the Linnik non-improvement;
> * the explicit μ(σ) convexity numbers.

Throughout, `Θ = sup{Re ρ : ζ(ρ) = 0}`. **QRH-IMPORT** (INTAKE.md) is the unreviewed claim that
every Dirichlet `L` is zero-free in `Re s > 7/8`. Sections 1.1–1.3, 2 and 3 use only its ζ-part
`Θ ≤ 7/8`; the least-prime bullet of §1.4 and the Siegel bullets of §1.5 use the full statement.
Write `θ_* = Θ − 1/2 ≤ 3/8` for the "excess".

## 1. Classical analytic consequences (conditional, imported)

**1.1 Lindelöf in the zero-free half-plane.** If ζ has no zero in `Re s > Θ`, then for every fixed
`σ > Θ`, `ζ(σ+it) = t^{o(1)}` and `1/ζ(σ+it) = t^{o(1)}`. *Route:* Borel–Carathéodory for
`log ζ` on the disk about `2+it` of radius `2−Θ−δ`, then Hadamard three circles with an inner disk
in `Re s > 1` (Titchmarsh Sec. 14.2; the same argument is Lemma 5 of [K]). Hence `μ(σ) = 0` for
`σ ≥ Θ` (continuity of μ). Under QRH-IMPORT: `μ(σ) = 0` on `[7/8, 1]`.

**1.2 Convexity interpolation.** With `μ(1/2) ≤ 13/84` (Bourgain) and convexity of μ,
QRH-IMPORT gives `μ(σ) ≤ (26/63)(7/8 − σ)` on `[1/2, 7/8]`; e.g. `μ(3/4) ≤ 13/252 ≈ 0.0516`
versus `13/168 ≈ 0.0774` from convexity with `μ(1)=0`. *Superseded by a sharper envelope:*
[ZERO_DENSITY_CONDITIONAL.md](ZERO_DENSITY_CONDITIONAL.md) computes the exact convex hull of all
μ data in ANTEDB together with `(7/8, 0)`. The result is `μ_QRH(σ) ≈ 0.4088(7/8 − σ)` on
`[0.5734, 7/8]`. It also shows that QRH-IMPORT does **not** improve the best zero-density exponents
`A(σ)` on `[1/2, 7/8)`, nor the density-hypothesis range `σ ≥ 25/32`.

**1.3 Prime and Möbius sums.** `ψ(x) = x + O(x^{7/8} log² x)` and `M(x) ≪ x^{7/8+ε}` (Perron with
1.1). Note the repository's SHARP/critical-Taylor obstruction (`OPEN.ARITH.CV`) is a *sign*
statement; a size bound `x^{7/8+ε}` only grades it (R17-style splitting gives `X^{3/8+ε}` where RH
would give `X^{ε}`).

**1.4 Non-improvements (recorded to prevent misreadings).**
* de Bruijn–Newman: with `H_0(z) = ξ((1+iz)/2)/8`, `Θ ≤ 7/8` puts zeros in `|Im z| ≤ 3/4`, and
  de Bruijn's strip theorem gives only `Λ ≤ 9/32`, weaker than the known `Λ ≤ 0.2`.
  (A survey note giving `9/128` used the wrong normalisation.)
* Zero density: `N(σ,T) = 0` for `σ > 7/8` is new, but the density hypothesis is already known
  on `σ ≥ 25/32`; nothing follows directly on `[1/2, 25/32]`.
* Least prime in a progression: a uniform zero-free half-plane `Re s > θ` gives `p ≪ q^{1/(1−θ)+ε}
  = q^{8+ε}`, weaker than Linnik with `L = 5`.
* Robin: the repository's Robin packet has no Θ-graded statement, and its canonical reduction
  and bounded tail are finite arithmetic, so they are unaffected.
  [ROBIN_GRADED.md](ROBIN_GRADED.md) supplies a graded statement (PROPOSED upper bound, IMPORTED
  lower bound):
  * with no zeros in `Re s > θ`, `σ(n)/(e^γ n log log n) ≤ 1 + C(log n)^{θ−1}/log log n` for
    large `n`;
  * so QRH-IMPORT bounds the relative size of any Robin violation by `(log n)^{−1/8+ε}`;
  * with Robin's Ω-result this exponent is sharp: `Θ ≤ 7/8` ⟺ that inequality for every `ε`.
  Violations are bounded in size, not excluded.

**1.5 Siegel zeros and class numbers (CONDITIONAL on QRH-IMPORT for all real primitive
characters).** Standard argument, recorded in [SIEGEL_DETERMINANT.md](SIEGEL_DETERMINANT.md) §5.
* If the imported half-plane holds for every real primitive Dirichlet character, every real zero
  has `β ≤ 7/8`. Then `(1−β) log q ≥ (log 3)/8` for all `q ≥ 3`, which is an *effective*
  Landau–Siegel exclusion. (From the Oct 5 claim: `β ≤ 11/12`, hence `(1−β) log q ≥ (log 3)/12`.)
* The Siegel–Goldfeld positivity argument then gives `L(1,χ) ≫ 1/log q` with effective constants.
* Hence, **if QRH-IMPORT (or the Oct 5 claim) holds for every real primitive Dirichlet character**,
  `h(D) ≫ √|D|/log|D|` for imaginary quadratic fields, with an effectively computable constant.
  A half-plane should give more (`L(1,χ) ≫ 1/log log q` by the usual short Euler product argument;
  standard, not re-derived here). The logarithmic form is recorded only for comparison with the
  Oct 1 paper.
* This would be a significant consequence of the external claims if they hold, but it says nothing
  about RH. The separate Oct 1 determinant paper gives only the weaker logarithmic statement; read
  with the manuscript's constants (effective in principle, PROPOSED reading), `c ≈ 3·10⁻⁴`
  (2.8·10⁻⁴ at the paper's `H`).

## 2. A graded form of the repository's Mellin criterion (native, PROPOSED)

**Lemma G (graded Mellin premise).** Let `F` be a fixed, noncancelling Mellin detector satisfying the
hypotheses of `research/integrated/CURRENT_RESULTS.md#mellin` (local integrability, initial absolute
convergence, continuation `MF` holomorphic near each real `s > θ`, multiplier not cancelling any
reciprocal-zeta pole in the relevant half-strip). Let `θ ≥ 0`. If

    N_F(Y) = ∫_1^Y F_-(x) dx/x = O_ε(Y^{θ+ε})   for every ε > 0,

then ζ has no zero with `Re ρ > 1/2 + θ` (at the poles `s = ρ − 1/2` of the fixed rows' consumer).

*Proof (adaptation of the repository route).* For `Re s ≥ θ + η`, dyadic summation of the premise
gives absolute convergence of `M(F_-)(s) = ∫ F_- x^{-s-1} dx` and of its derivatives, so `M(F_-)` is
holomorphic on `Re s > θ`. The positive part has a Laplace-type transform with abscissa `c`.
If `c > θ`, then `M(F_+) = MF + M(F_-)` extends holomorphically through a neighbourhood of the real
point `c` (both summands do), contradicting the tail Landau theorem used in the repository route.
Hence `c ≤ θ`, so `MF` is holomorphic on `Re s > θ`; noncancellation then excludes a reciprocal-zeta
pole there, i.e. a zero with `Re ρ − 1/2 > θ`. The case `c = −∞` is as in the original route. ∎

*Converse under QRH-IMPORT (sketch, needs the row-specific growth of the multiplier).* If
`MF(s) = H(s)/(s² ζ(s+1/2))` with `H` holomorphic and `H(s) ≪ (1+|t|)^{1−η}` on `Re s ≥ θ_* + ε`,
then Perron inversion and 1.1 give `|F(x)| ≪ x^{θ_*+ε}`, hence `N_F(Y) ≪ Y^{3/8+ε}`.
So for such rows the premise exponent is *exactly* the zero excess: **QRH-IMPORT moves the Mellin
premise from the trivial exponent 1/2 to 3/8; RH requires 0.** The graded lemma is consistent with
(and adds nothing beyond) QRH-IMPORT; it is recorded because it makes the gap quantitative.

## 3. Repository hooks located by the survey (all quantitative, none closes a criterion)

| Hook | File | Effect of `Θ ≤ 7/8` |
|---|---|---|
| R15 reciprocal-growth / wavelet energy abscissa `Θ + 1/2` | `reviews/D-final/REPAIRS.md` (R15) | energy finite for `σ0 > 11/8`; `1/ζ ≪ t^ε` on `Re w > 7/8` |
| A-115 / A-117 (tent energy `2Θ−1`, Mertens shift) | `reviews/A/CLAIMS.tsv` | tent-energy exponent `≤ 3/4` |
| T-9502 / T-9503 totient errors (PROPOSED) | `claims/theorems/` | error `O(x^{-9/8+ε})`; RH would give `x^{-3/2+ε}` |
| Dyadic cocycle `Θ_a` positivity (PROPOSED) | `claims/lemmas/L-91027…` | holds for every `a > 3/8` |
| Safe-line VK disc (`CONDITIONAL_EXACT`) | `research/integrated/safe_line/README.md` | half-plane input is far stronger than VK; region could enlarge (unverified) |
| Xi order-3 conditional theorem | `research/integrated/xi` | offsets `a_i ≤ 3/8` shrink the reserve budget; order ≥ 4 untouched |

Every RH-equivalent premise in the repository is a *subpower* (exponent-0) statement; QRH-IMPORT
supplies exponent `3/8` uniformly. This is the precise sense in which the quasi-RH claim is
"structurally adjacent but quantitatively distant" from every open node here.
