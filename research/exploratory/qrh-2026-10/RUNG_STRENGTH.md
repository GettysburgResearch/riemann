# The moment ladder is one statement: sub-diagonal cancellation in the sextic family

```text
Status: PROPOSED (Prop. R and Observations 1-2 are elementary and proved here, not reviewed)
  + HEURISTIC (Section 3: barrier for the Oct 5 pipeline) + EMPIRICAL (Section 5, finite numerics)
Scope: the 2k-th moment hypotheses of PR 910 Prop. 7.2 for the sextic Moebius family of the OpenAI
  Oct 5 (11/12) manuscript. No zero-free region is proved; nothing here bears on RH directly.
Exact sources or dependencies: Oct 5 manuscript (PR 908 import, paper2.tex Sections 1-3: the family
  A_u(D), sextic reciprocity, prime extraction); PR 910 UPSTREAM_HEIGHT_AND_MOMENTS.md Prop. 7.2
  (Hoelder exponent (k + h - h/6)/(2k)); A2_LITERATURE.md Sections 0 and 5; FOURTH_MOMENT_A2.md
  Sections 4 and 6; ALT_PROBES.md (why the family is sextic); moments/README.md
What was actually run: moments/moments.py with theta in {-0.1, ..., -0.6} (k = 1, rows H = D^0.4 to
  D^0.9), D in {1000, ..., 64000}; output moments/results/subdiag_k1.{json,log}; about 10 s
Smallest remaining gap: no unconditional mechanism is known that proves any mean square of this
  family with fewer rows than columns (rho < 1). Section 4 lists what such an input must contain.
```

RH remains unproved. The OpenAI manuscripts are external and unreviewed; "imported" below means
taken from them or from PR 910 without independent proof.

## 1. Setting

The Oct 5 family over `K = Q(ω)` is

    A_u(D) = Σ_n μ(n) ν(n) χ_n(u) W(N n / D),

with `n` over primary elements prime to 6, `χ_n(u)` the sextic residue symbol, and `W` a smooth bump
on `[1, 2]`. Write

    M_{2k}(D; h) = Σ_{0 < N u ≤ D^h} |A_u(D)|^{2k}.

**Mom(k, h)** is the hypothesis `M_{2k}(D; h) ≪_ε D^{k+h+ε}` for all large `D`. This is diagonal size:
`A_u(D)^k` is a Dirichlet polynomial of length about `D^k`, and there are about `D^h` rows.

PR 910 Prop. 7.2 [imported; PR 910's own review found no error] says that Mom(k, h) implies that
`ζ_K`, hence `ζ`, has no zero in `Re s > (k + h − h/6)/(2k)`. The mechanism is extraction from the
`≍ D^{h/6}` sixth-power rows `u = π⁶`, on which `χ_n(u)` is principal. The Oct 5 manuscript's own
second-moment bound at `H = D^{1+θ}` is the case `k = 1`, `h = 1 + θ`, and gives 11/12 as `θ → 0`.

## 2. Two elementary observations and one proposition

Define the **row/column ratio**

    ρ = h/k = log(number of rows) / log(length of A_u^k).

**Observation 1 (only ρ matters).** The boundary is

    σ(k, h) = (k + h − h/6)/(2k) = 1/2 + (5/12) ρ.

So the moment order does nothing by itself.
* A second moment over `D^ρ` rows gives the same boundary as a fourth moment over `D^{2ρ}` rows.
* `ρ = 1` gives 11/12 at every `k`.
* Beating 7/8 needs exactly `ρ < 9/10`, and `ρ → 0` approaches 1/2.

The hypotheses Mom(k, kρ) for different `k` are not formally equivalent. Hölder gives
Mom(k, h) ⇒ Mom(1, h), which is a *larger* `ρ`. They are equal only in what they would conclude.
The simplest member of each class is the **sub-diagonal second moment** Mom(1, ρ) with `ρ < 1`.

**Observation 2 (what a single row can do).**
* If `ρ ≥ 1`, the trivial bound `|A_u(D)| ≪ D` shows that no single row contributes more than
  `D^{2k} ≤ D^{k+h}`. No individual row can violate Mom(k, h); its whole content is collective,
  through the multiplicity of the sixth-power rows.
* If `ρ < 1`, positivity gives `max_{N u ≤ D^h} |A_u(D)| ≪ D^{(1+ρ)/2+ε}`. That is a power saving
  `D^{(1−ρ)/2}` for every member of conductor up to `D^h` at once.

**Proposition R (each member, rigorous, elementary).** Suppose Mom(k, h) holds for every smooth `W`
supported in `[1, 2]` (constants may depend on `W`). Then, for every fixed `u ≠ 0`, the Hecke
L-function `L(s, ψ_u)` of the finite-order character `ψ_u : n ↦ χ_n(u)` has no zero in
`Re s > 1/2 + h/(2k)`. Here `𝔫 ↦ (u/𝔫)₆` depends only on the ideal `𝔫 = (n)`. By Artin
reciprocity it is the Hecke character of the Kummer extension `K(u^{1/6})/K`, and `ψ_u` denotes the
primitive character inducing it.

*Proof.* For `D^h ≥ N u`, positivity gives `|A_u(D)|^{2k} ≤ M_{2k}(D; h) ≪ D^{k+h+ε}`. So
`A_u(D) ≪ D^{a+ε}` with `a = 1/2 + h/(2k)`. Also `A_u(D) = 0` for `D < 1/2`.

Since `∫_0^∞ W(N n/D) D^{−s−1} dD = N(n)^{−s} Ŵ(s)` with `Ŵ(s) = ∫ W(y) y^{s−1} dy` entire,

    ∫_0^∞ A_u(D) D^{−s−1} dD = Ŵ(s) F_u(s),   F_u(s) = Σ_n μ(n)ν(n)ψ_u(n) N(n)^{−s},

and the left side converges absolutely, locally uniformly, on `Re s > a`. Hence `Ŵ F_u` is
holomorphic there.

With `ν` the indicator of `(n, 6) = 1`, `F_u = E_u / L(s, ψ_u)`. Here
`E_u = ∏_{𝔭 | 6u} (1 − ψ_u(𝔭) N𝔭^{−s})^{−1}` (only primes where the imprimitive and primitive
characters differ contribute) is holomorphic and nonvanishing on `Re s > 0`. A zero `ρ₀` of `L(s, ψ_u)` with
`Re ρ₀ > a` would force `Ŵ(ρ₀) = 0` for every admissible `W`. That is false, because
`W ↦ Ŵ(ρ₀)` is a nonzero linear functional. ∎

Prop. R is weaker than extraction for the principal row, where `a` improves to `1/2 + 5h/(12k)`.
It is nontrivial exactly when `ρ < 1`.

*Remark (all members get the extraction exponent; PROPOSED adaptation).* For fixed `u`, the rows
`u π⁶` with `π ∤ 6u` have `χ_n(u π⁶) = ψ_u(n) 1_{π ∤ n}`. So every member occurs with the same
multiplicity `≍ (D^h/N u)^{1/6}` as the principal character. PR 910's prime-removal recursion uses only
the multiplicativity of `n ↦ μ(n)ν(n)ψ_u(n)`. It should therefore give `1/2 + 5h/(12k)` for every
fixed member, with the conductor entering only through a factor `(N u)^{1/(12k)}`. This was not
re-verified line by line. The ladder conclusions are family statements, like the imported 7/8 and
11/12 claims.

**Corollary (the endpoints of the ladder).** Write Mom(1, ρ) for the second-moment hypothesis with
`D^ρ` rows, for every smooth `W` on `[1, 2]`.
* `ρ > 1`: Mom(1, ρ) is the imported Oct 5 input, giving 11/12 as `ρ → 1⁺`.
* `ρ → 0`: Mom(1, ρ) holds for every `ρ > 0` **if and only if** GRH holds for every `L(s, ψ_u)`,
  `ψ_u` the sextic characters of the family.
  * ⇒: Prop. R with `k = 1`, `h = ρ → 0`.
  * ⇐: GRH gives `A_u(D) ≪ D^{1/2+ε} (N u)^ε`, by Perron and the GRH bound
    `1/L(s, ψ) ≪ (q(|t|+2))^ε` on `Re s ≥ 1/2 + ε`. Summing over `D^ρ` rows gives `D^{1+ρ+ε}`.
* In between, Mom(1, ρ) gives `1/2 + 5ρ/12` for the principal member (by extraction) and
  `1/2 + ρ/2` for every member (by Prop. R).

In their conclusions, the sub-diagonal hypotheses therefore interpolate between the imported claim and GRH
for the family. They do not imply one another formally: more rows is not implied by fewer. That
is a precise sense in which "the Oct 5 architecture tends to 1/2": its remaining input is a
quantitative fragment of GRH.

## 3. The ρ = 1 wall (HEURISTIC barrier for the Oct 5 pipeline)

**(a) Row-blind bounds stop at ρ = 1.** Consider any bound
`Σ_{N u ≤ H} |Σ_{N m ≤ L} b_m χ_m(u)|² ≤ Δ(H, L) ‖b‖²` valid for *all* coefficient vectors `b`; large
sieves are of this kind. Take `b_m = conj(χ_m(u₀))` on `m` coprime to `u₀`. Then the single row `u₀`
gives `‖b‖⁴`, so `Δ ≥ ‖b‖² ≍ L`.

When `H < L`, i.e. `ρ < 1`, such bounds therefore give at best `L ‖b‖² ≫ H ‖b‖²`. Passing `ρ = 1`
needs input specific to the Möbius coefficients. (This is trivial, but it locates the wall exactly.)

**(b) The same wall in the dual.** For `H < L`, Poisson summation in `u` produces a dual with
`𝓗 = L²/H > L` rows. After Cauchy–Schwarz, the dual diagonal alone contributes `(H/L)·𝓗·L = L²`. In
the actual sextic family the dual mean square equals its diagonal to within 1–3 %
([A2_LITERATURE.md](A2_LITERATURE.md) §5; [FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md) §6). The Oct 5
pipeline (Poisson, Möbius absorption into `conj(α)γ₂`, cubic theta reflection, quadratic large sieve)
ends in a row-blind large sieve. It is therefore capped at `ρ ≥ 1`, i.e. at

    11/12 = (1 + c)/2,   c = 5/6,

for every moment order. The GL(3) cubic theta, which would have been the next reflection, has
coefficients that vanish on the needed support ([A2_LITERATURE.md](A2_LITERATURE.md) §3).

*The same wall inside the manuscript's own induction.* The Oct 5 proof reduces the mean square to
a canonical dual problem `E(H, X, F) ≤ Σ D^ε` and proves it by induction on the row range `H`
(Prop canonical; reviewed in [reviews/OCT5_R2_ITERATION_TRANSFER.md](reviews/OCT5_R2_ITERATION_TRANSFER.md)).
The induction uses three facts:
* the gap `H/Σ ≤ D^{−κ}`, which is initially `D^{−ϑ}` with `ϑ` the primal `θ` (eq:initial-scales);
* the hypothesis `max(H, LF) ≤ Σ`;
* the contraction `H' < H (H/Σ)²` per level.

In the exact Poisson identity at `ρ < 1`, the dual diagonal is cancelled by the Möbius variable
`μ(f)`. The first loss is the positivity step (eq:weighted), which bounds the signed sum by the full
dual mean square, i.e. replaces `μ(f)` by `|μ(f)|`, at a cost of `D^{1−ρ}`
([DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md)).

A sub-diagonal primal (`θ < 0`, i.e. `ρ < 1`) starts with `H/Σ = D^{|θ|} > 1`. Then the hypothesis
fails and the "contraction" becomes an expansion, so the recursion has no base. The level count
`⌈4/ϑ⌉` also blows up as `ϑ → 0⁺`. So the manuscript's own mechanism is exactly the `ρ ≥ 1` method.

**(c) Why `c = 5/6`.** By the heuristic parity rule of [ALT_PROBES.md](ALT_PROBES.md), the Möbius
absorption needs a quadratic factor next to a theta with explicit Gauss-sum coefficients. Only the
cubic theta has such coefficients, so the family is sextic and `c = 1 − 1/6`.

So 11/12 plays the role for the Oct 5 architecture that 13/15 plays for the Sep 30 one
([THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md)). It is a ceiling for the stated pipeline, not a
theorem about the true size of the moments; Section 5 shows the moments themselves are much smaller.

## 4. What any ρ < 1 input must contain

Write the rows as `u = w v⁶`, with `w` sixth-power-free. Then `M_{2k} ≈ Σ_w (D^h/N w)^{1/6} |A_w|^{2k}`,
with coprimality corrections. A proof of Mom(k, h) with `ρ < 1` must deliver all of the following.

1. **Conductor-uniform member bounds:** `|A_u(D)| ≪ D^{(1+ρ)/2+ε}` for all `N u ≤ D^h`
   (Observation 2).
2. **Conductor-graded small-row bounds.** For `N w = D^ω`, Mom(k, h) needs
   `|A_w(D)| ≪ D^{1/2 + 5ρ/12 + ω/(12k)}`. At `ω = 0` this is the *conclusion* itself, so leverage is
   tight. The hypothesis cannot be proved by first proving its conclusion for the small rows and then
   handling the rest; that only closes at the fixed point.
3. **An on-average GRH for generic rows (large-values count):**
   `#{u : |A_u(D)| > D^{1/2+δ}} ≪ D^{h − 2kδ + ε}`.
   Pointwise information cannot supply this. If every member had `|A_u| ≍ D^{σ₀}` with `σ₀ > 1/2`,
   then `M_{2k} ≍ D^{h + 2kσ₀} ≫ D^{k+h}`.
4. **No bootstrap from pointwise bounds.** Combine Hölder, the imported second moment at
   `H = D^{1+θ}`, and a family bound `|A_u| ≪ D^{σ₀}`:
   `M_{2k} ≤ D^{(2k−2)σ₀ + 1 + h + ε}`. Extraction then gives the exponent
   `σ₀(k−1)/k + 11/(12k)` as `θ → 0`. Its fixed point is exactly `σ₀ = 11/12`. Iterating gains nothing.

The same circularity appears in classical families (standard background, stated to our knowledge):

* **t-aspect.** For `T < N`, the excess of `∫_0^T |Σ_{n≤N} μ(n) n^{−1/2−it}|² dt` over its diagonal is
  governed by averaged correlations `Σ_{h ≲ N/T} Σ_n μ(n)μ(n+h)`. Matomäki–Radziwiłł–Tao-type
  results save `o(1)` there; no power saving is known.
* **Dirichlet characters to one modulus `q < N`.** `Σ_χ |Σ_{n≤N} μ(n)χ(n)|²` is the
  Barban–Davenport–Halberstam variance of `μ` in progressions mod `q`. Its known error terms save only
  powers of `log N`, through Siegel–Walfisz for the small conductors.

In each case the obstruction is the same as item 2: small conductors need a quasi-GRH. The sextic
family differs only in that leverage turns this into an exact fixed point.

## 5. The moments themselves are diagonal-sized (EMPIRICAL, finite)

Here `ν = 1` on primary `n` prime to 6, `W` is the bump of `moments/common.py`, and the rows are all
nonzero `u ∈ Z[ω]`. The table gives `M₂ / (#rows · Σ_n W(N n/D)²)`, a naive diagonal that ignores
the coprimality factor. That factor lowers the true diagonal by a few percent at every `ρ`.

| D | ρ = 0.9 | 0.8 | 0.7 | 0.6 | 0.5 | 0.4 | ρ = 1.05 (moments/) |
|---|---|---|---|---|---|---|---|
| 1000 | 0.904 | 0.963 | 0.940 | 0.827 | 0.855 | 0.914 | 0.911 |
| 4000 | 0.928 | 0.915 | 0.932 | 0.904 | 0.904 | 0.988 | 0.932 |
| 16000 | 0.936 | 0.939 | 0.907 | 0.911 | 0.897 | 0.948 | 0.942 |
| 64000 | 0.937 | 0.941 | 0.949 | 0.938 | 0.884 | 0.921 | 0.939 |

Row counts at `D = 64000` run from 76 716 (`ρ = 0.9`) down to 300 (`ρ = 0.4`), so the small-`ρ`
columns are noisy.
* There is no excess at any `ρ`. Sub-diagonal second moments look exactly like super-diagonal ones.
* For `D ≥ 8000`, `M₄/M₂² ∈ [1.86, 2.30]` and `M₆/M₂³ ∈ [4.7, 8.8]`; the full range is
  `[1.60, 2.30]` and `[3.0, 8.8]`, the extremes coming from cells with 54–300 rows. These are the
  complex-Gaussian values 2 and 6 with small-sample noise.
* The higher moments in [moments/](moments/README.md) (`k = 2, 3` at `ρ = 0.525, 0.35`) agree.

This is what on-average GRH predicts, and it says nothing about provability. The hypotheses look
true. What is missing is a mechanism, not evidence.

## 6. Consequences for the agenda

* Restate [AGENDA.md](AGENDA.md) A1. The basic target is the sub-diagonal **second** moment
  Mom(1, ρ), `ρ < 1`. Each `0.1` of `ρ` below 1 is worth `1/24` of boundary, and `ρ = 9/10` already
  reaches 7/8.
* The fourth moment matters only if its bilinear (A2) structure supplies a mechanism that the second
  moment lacks. [A2_LITERATURE.md](A2_LITERATURE.md) found none in the literature.
* Read the statement that the Oct 5 architecture "tends to 1/2" as follows. Its conclusion improves
  continuously as `ρ` decreases, and `ρ < 1` is the entire difficulty. That difficulty is an
  on-average GRH for a family with a fixed point at its own conclusion.

## 7. Relation to the repository's open cut "principal-member transfer"

[OPEN_CUTS.md §5](../../../OPEN_CUTS.md#family-transfer) asks for family-to-principal transfers
that state the family, measure, ramification, masks and conductor dependence. It warns that
nonprincipal control can miss an arbitrarily large principal component. The Oct 5 extraction is a
transfer of exactly this kind, and this note quantifies it (PROPOSED; inputs imported):

| item | value in the Oct 5 family |
|---|---|
| family | Kummer characters `ψ_u` of `K(u^{1/6})/K`, `K = Q(ω)`, rows `0 < N u ≤ H`, all `u` (units and non-primary included) |
| physical measure | counting measure on rows. The principal member has multiplicity `≍ H^{1/6}` (rows `u = unit·v⁶`), and member `ψ_w` has multiplicity `≍ (H/N w)^{1/6}` |
| ramified factors and masks | `ν = 1_{(n,6)=1}` and coprimality to `v`. These are finite Euler products `E_u`, nonvanishing on `Re s > 0` (Prop. R) |
| transfer law | a diagonal-size `2k`-th moment over `D^h` rows gives `1/2 + (1 − 1/6)ρ/2`, `ρ = h/k`, for the principal member (PR 910 Prop. 7.2) |
| why nonprincipal control is not enough | the bound must hold *including* the principal rows. Row-blind bounds therefore stop at `ρ = 1` (§3), and below it the small-conductor rows sit at a fixed point (§4, item 2) |
| conductor dependence | member `ψ_w` with `N w = D^ω` needs `D^{1/2 + 5ρ/12 + ω/(12k)}` |

The cut's warning is visible here in exact form. A family statement transfers to the principal
member only through the principal member's own multiplicity. The family estimate is useful exactly
when it is proved *without* looking at individual members, i.e. at `ρ ≥ 1`.
