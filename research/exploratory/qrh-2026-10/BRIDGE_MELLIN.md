# Bridge: fixed Mellin detectors and the QRH "continuation from a common signal"

```text
Status: PROPOSED (framework comparison; any lemma explicitly labeled)
Scope: structural comparison of two conditional zero-exclusion principles; exponent bookkeeping;
  local PROPOSED items BM-1..BM-4 (labels local to this note, not claim IDs). No RH claim. Nothing
  here is reviewed. QRH-IMPORT is used only where marked.
Exact sources or dependencies:
  repo: research/integrated/CURRENT_RESULTS.md#mellin; research/integrated/mellin_landau/README.md;
    canonical/consumers/mellin-landau/{CONTRACT,FIXED_ROWS_2_3,FIVE_THREE_SCALAR,MULTIPLIER_FIREWALLS}.md;
    reviews/C/pass4-math-completion/proofs/MELLIN_ANALYTIC_GAPS.md (M2-M7);
    claims/lemmas/L-96000, L-96001; canonical/2026-08-22/claims.tsv rows OPEN.DIRECTMAIN.MELLIN.ALL_ROWS,
    DIRECTMAIN.MELLIN.T96000; this folder: INTAKE.md, CONDITIONAL_CONSEQUENCES.md (Lemma G),
    THRESHOLD_CALCULUS.md, scripts/barrier_lp.py.
  prior QRH bridge work (draft, unreviewed): PR 908 standalone/2026-10-07-openai-quasi-riemann-import/
    CONDITIONAL_BRIDGES.md §§2-5 and RESEARCH_PLAN.md §7; PR 909 standalone/2026-10-09-openai-riemann-
    companion/NATIVE_MOBIUS_BRIDGE.md (OAI-NB26-L1); PR 910 standalone/2026-10-10-quasi-riemann-height-
    descent/TAIL_AND_EULER.md §§3, 7; branch claude/openai-math-riemann-analysis-w5copg
    standalone/2026-10-07-openai-quasi-rh/README.md §§3-5; NRC32 PROOF.md at 0f82df3b (PR 905);
    issue 902 (balanced Newton energy as primary attack).
  manuscript [OAI] (untrusted, unreviewed): Sec. 1 overview; Sec. 2 Prop. 2.1; Sec. 6.1 (6.1);
    Sec. 7.1 (7.3)-(7.5); Sec. 7.2 Lemma 7.1, (7.13); Def. 10.1 C(s).
What was actually run: reading; scratch scripts (not committed) for: exact sympy check of
  5P_2+3P_3 = -3(a-1)(a-2) and of the C(1/2)/floor arithmetic below; float check of identity BM-1 at
  X = 7.3, 50, 333.7, 2000 (|diff| <= 3e-13); exact Fraction check of the twisted Newton identity and
  centered mesh compression (BM-3 adapter) for chi_0, chi_-3, chi_-4, Y in {4,7,12,20}: all pass;
  rerun of scripts/barrier_lp.py (13/15 and 167/192 reproduced).
Smallest remaining gap: a second, independent ("reflection-small") representation of some fixed
  detector or of the NRC32 coarse covariance S_Y. By BM-2, any unconditional S_Y << Y^{2-eta} is
  already QRH-strength, and the relative step in BM-3 is RH-strength.
```

RH remains unproved. [OAI] is an external, unreviewed manuscript (INTAKE.md). Exponent bookkeeping and the low-side barrier are already in w5copg §3, PR 910 and THRESHOLD_CALCULUS.md. Conditional energy exponents are in PR 908. This note does not redo them. It adds three things: the exact two-representation versus one-sided-positivity comparison (§1); a verdict on whether the fixed rows admit a reflection-small dual (§2); and the family-supremum bootstrap mapped onto the NRC32 energy of issue 902 (§3).

## 0. Summary

1. Both principles continue a reciprocal L-function by showing that an arithmetic signal is smaller than its rightmost zero allows. The repo's route is **one-sided** and **absolute**: it bounds `N_F` by `Y^ε` and relies on positivity plus Landau. QRH's route is **two-sided** and **relative**: it shows `|f| ≪ Z^{C(β*)−ε*}` and needs only the trivial half of Mellin theory. The relative form transfers verbatim to the repo (BM-0).
2. The fixed rows 2 and 3 and the 5:3 scalar are, exactly, log-Riesz means of a finitely modified Möbius sequence plus a positive logarithmic drift (BM-1). **No known exact representation of them is visibly small.** The available duals are the explicit formula (circular), Möbius inversion to a positive surrogate (signal-free), Farey/Ramanujan expansions (equivalent reformulations) and the functional equation of `1/ζ` (which crosses the poles). QRH never dualizes `1/L` itself. `1/L` appears as the principal Poisson row of an automorphic average.
3. Floor bookkeeping. In the repo normalization the square-root (diagonal) size of the detector equals the RH size `X^{o(1)}`, so there is no exponent gap, but any Cauchy–Schwarz/large-sieve low estimate must be sharp. In QRH normalization the diagonal sits at least `1/3 + (lx−ℓ)/6` above `C(1/2)`.
4. The family supremum is a worst-case bootstrap, not an average. It licenses error terms measured relative to `β*` for every twist the proof generates. On NRC32 it gives an exact exponent identity `limsup log S_Y / log Y = 4Θ − 2` (BM-2). It also weakens the issue-902 contraction to **one** cross-member relative step (BM-3).

## 1. The two principles side by side

**Repo (CURRENT_RESULTS#mellin; MELLIN_ANALYTIC_GAPS M7; Lemma G).** `F` is a fixed real, locally integrable function on `[1,∞)` with `𝓜F(s)=∫_1^∞ F(x)x^{−s−1}dx` initially absolutely convergent. It continues as `𝓜F(s)=H(s)+P(s+½)B(s)/(s²ζ(s+½))`, with `H` holomorphic. The fixed multiplier is zero-free in `Re z>0` (rows 2,3: no common zero; 5:3: `−3(2^{−z}−1)(2^{−z}−2)`). The continuation is analytic near each real `s>θ`. Premise: `N_F(Y)=∫_1^Y F_−dx/x = O(Y^{θ+ε})`. Conclusion: no zero with `Re ρ > ½+θ`, and RH when `θ=0`.

**QRH ([OAI] Prop. 2.1).** `β*` is the supremum of zero real parts over all primitive finite-order Hecke characters of `Q(√−3)`. For each `η`: `f_η(Z)=(2πi)^{−1}∫_{(2)} Z^{C(s)}e^{(s−5/6)²}H_η(s)/L^S(s,η)ds`, with `C(s)=s+c` and `sup_{Re s>σ0}|H_η−1|≤½`. A probe `J_η` must satisfy `|J_η|≪Z^{C(σ0)+ω}` (low) and `|J_η−f_η|≪Z^{C(β*)−σ}` (high). `ω<β*−σ0` and `σ>0` are uniform in `η`; constants may depend on `η`. Conclusion: `β*≤σ0`.

| | Repo Mellin–Landau | QRH Prop. 2.1 |
|---|---|---|
| object | one fixed real detector `F` | complex signal `f_η`, one per family member |
| what is continued | `𝓜F` to `Re s>θ` | `1/L^S(s,η)` to `Re s>β*−ε*` |
| premise | one-sided `N_F≪Y^{θ+ε}` | two-sided `|f_η|≪Z^{C(β*)−ε*}`, from low + high |
| reference size | absolute (`Y^θ`) | relative to the hypothetical rightmost zero |
| source of the bound | an arithmetic sign (open producer) | a second exact representation (cubic-theta reflection) |
| analytic engine | Landau: nonnegative density ⇒ abscissa singular (M3) | absolute convergence + Fourier inversion + identity theorem |
| multiplier condition | fixed zero-free numerator | `|H_η−1|≤½` on `Re s>σ0` |
| uniformity | none (one function) | margins uniform over the family |

**Why QRH needs no positivity.** A two-sided bound `|f(Z)|≪Z^{a}` already makes `∫f Z^{−C(s)}dZ/Z` absolutely convergent for `Re C(s)>a` (the M2 argument). Then Fourier inversion on `Re s=2` identifies the transform with `e^{(s−5/6)²}H/L`, and the identity theorem extends this. Landau's theorem exists in the repo route to do one job: upgrade **one-sided** control to two-sided control at the abscissa, using real-axis analyticity. With two-sided control the job is gone. QRH replaces Landau with the elementary direction of Mellin theory. It pays by needing a size bound, and it gets that bound from an independent representation. Two side effects follow:

- Complex signals are fine. The Landau route needs a real detector. For a complex character, `Re F_χ` mixes the poles at `ρ` and `ρ̄`, and the noncancellation of the two would need its own proof. This is one reason the repo's consumer is ζ-only.
- The Gaussian in (2.3) makes every contour absolutely convergent, whatever the growth of `1/L`. The repo's `1/s²` suffices only because Landau needs no contour shift. A Gaussian attenuates a pole but does not remove it (PR 910 §7.2).

**BM-0 (PROPOSED; corollary of Lemma G).** Let `Θ` be the supremum of the real parts of the zeta zeros, and let `F` be a fixed detector as above. Suppose there is a fixed `σ>0` such that **if `Θ>½` then** `N_F(Y)≪Y^{Θ−½−σ}`. Then `Θ=½`.
*Proof.* Assume `Θ>½`. Lemma G with `θ=Θ−½−σ` excludes zeros with `Re ρ>Θ−σ`, contradicting the definition of `Θ`. ∎
The hypothesis must be stated as an implication: `N_F` is nondecreasing, so an unconditional `N_F≪Y^{−σ}` would be false. The proof of the premise may use "no zero right of `Θ`" for ζ. This is exactly the relative/bootstrap form of [OAI] (2.5), now with a **one-sided** left side. The two-sided version is Prop. 2.1 in the normalization `Z=X`, `C(z)=z−½` (with `z=s+½`).

## 2. Does a fixed row admit a reflection-small dual?

**BM-1 (PROPOSED identity; algebra from L-96000 (8) and the VERIFIED 5:3 factorization).** Write `P_j(z)=Σ_{m≤j+1}p_j(m)m^{−z}`. For `X≥1`,

`c_X(j) = C_j log X + Σ_{n≤X} (p_j*μ)(n) n^{−1/2} log(X/n)`,
`W_X := 5c_X(2)+3c_X(3) = 6 log X − 6 Σ_{n≤X} b(n) n^{−1/2} log(X/n)`.

Here `b` is multiplicative with `b(p)=−1`, `b(p^k)=0` for odd `p` and `k≥2`. Its 2-factor is `(1−a)²(1−a/2)=1−(5/2)a+2a²−(1/2)a³` with `a=2^{−z}`. That is, `b(2)=−5/2`, `b(4)=2`, `b(8)=−1/2`, and `b(2^k)=0` for `k≥4`.
*Proof.* Both sides are continuous with absolutely convergent Mellin transforms on `Re s>½`. They agree there: `∫_1^∞ log(X/n)_+X^{−s−1}dX=n^{−s}/s²`, `5C_2+3C_3=6`, `5P_2+3P_3=−6(1−a)(1−a/2)`. Mellin uniqueness finishes. Checked numerically at four `X` (header). ∎

So the open premise `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` reads `∫_1^Y (R_b(X)−log X)_+ dX/X = Y^{o(1)}`, where `R_b` is the log-Riesz mean of `b(n)/√n`. The double pole at `s=0` gives `W_X` a positive drift `6(1−B(½)/ζ(½))log X ≈ 6.778 log X`, with `B(z)=(1−2^{−z})(1−2^{−z−1})`. Heuristically, under RH and absolute convergence of the zero sum, `W_X` is eventually positive. The one-sided premise therefore asks that zero oscillations not beat a log drift on a set of large log-measure. The boxed positivity (L-96000.3) is **not** available. `T-96000` is `GAP_BLOCKED` and the all-rows producer is `OPEN.DIRECTMAIN.MELLIN.ALL_ROWS`.

**Candidate second representations of `W_X` (or any fixed row).**

| Dual | Exact? | Visibly small? | Verdict |
|---|---|---|---|
| explicit formula (sum over zeros of ζ) | yes, under standard truncation | only if the zeros are on the line | circular |
| Möbius inversion to the surrogate `Q_X(j)≥0` | yes | positive, but `𝓜Q=H_j/s²` has no `1/ζ` | signal-free (firewall 2: positive floor kernel); the transport is the open producer |
| `μ(n)=c_n(1)` (Ramanujan sums) → Farey sums | yes | no; Franel–Landau-type equivalents | reformulation |
| functional equation `1/ζ(z)=1/(χ(z)ζ(1−z))` | yes | only after crossing every pole of `1/ζ` | not independent |
| Voronoi/Poisson for `μ` | does not exist: `1/ζ` is not automorphic | — | — |

**Verdict.** The fixed rows 2 and 3 and the 5:3 scalar have no known exact representation in which they are visibly small, even heuristically. QRH does not dualize `1/L`. Its probe (6.1) averages cubic-theta (Gauss-sum) coefficients, which have an exact automorphic reflection (Prop. 5.1). `1/L(x,η)` appears only on the **other** side: in the `u=1` Poisson row via the Euler identity (7.13), `F_{η,1}=ζ_F^S(6z)L^S(w,χ)/L^S(x,η)·H`. The Möbius sign enters through Patterson's coefficient, `γ2(c)=μ(c)α(c)G(c)/γ1(c)` (Sec. 7.2). A QRH-style route for the repo would therefore not dualize `W_X`. It would build a probe whose principal Poisson row reproduces the detector's signal `B(s+½)/(s²ζ(s+½))`, with error rows in a closed family. *Heuristic firewall:* the Newton/convolution algebra, the Mellin consumer and BM-0/BM-2 are purely multiplicative. A proof of the low side must therefore use additive or automorphic input that fails for Beurling-type systems with off-line zeros. In QRH that input is theta reflection plus Poisson summation on `Z[ω]`. (Existence of such Beurling systems, e.g. Diamond–Montgomery–Vorhauer 2006, is cited from memory and was not re-checked.)

**Exponent bookkeeping.**

*Repo normalization.* The detector signal is `(2πi)^{−1}∫X^{z−1/2}B(z)/((z−½)²ζ(z))dz`, i.e. `C(z)=z−½`. RH needs low exponent `C(½)=0`. Lemma G is the same bookkeeping, with "one-sided" for "two-sided" and "absolute" for "relative": exponent `θ` maps to boundary `½+θ`.

*QRH normalization `C(s)=s+c`.* The boundary is `σ0=θ_low−c`, and RH requires `θ_low=C(½)=½+c`. Part I has `c=−2/3`: RH needs `Z^{−1/6}`, achieved `Z^{1/4}`. Part II has `c=−11/16`: RH needs `Z^{−3/16}`, achieved `Z^{3/16}`. With `h=1−lx+ℓ` (Def. 10.1), `c=lx/3+ℓ/6−5/6` and `C(½)=lx/3+ℓ/6−1/3`.

*Floor.* Cauchy–Schwarz separates the probe as `Σ_m A_mB_m`, and the reflected energy cannot fall below its large-sieve diagonal (`E≥M`). With `ly≥lx` this gives `θ_low≥lx/2`, hence `σ0≥1−h/6=5/6+(lx−ℓ)/6`. Since `ℓ≤lx`, `σ0≥5/6` (THRESHOLD_CALCULUS.md §2, barrier_lp.py). The deficit relative to RH is `lx/2−C(½)=1/3+(lx−ℓ)/6≥1/3`. Exact checks: Part I sits **at** its floor (`θ_low=lx/2=1/4`, `σ0=11/12`). Part II sits `1/96` above it (`θ_low=18/96` against `17/96`; floor `83/96`).

*Why the floor is intrinsic.* A Cauchy–Schwarz/large-sieve bound cannot go below the size the probe would have with random phases. The signal comes only through the residue of `ζ_F(6z)` at `z=1/6`: the principal frequencies `a⁶` form a thin subset of the dual frequencies `ua⁶`. So the signal gains `Z^{h/6}` while the diagonal grows like `Z^{lx/2}`. This is w5copg's leverage law, `σ0=(1+c)/2` with principal-copy density `H^{−c}`, `c=5/6`. RH needs `c=0`.

*Contrast.* In the repo normalization the random-sign size of `R_b(X)` is `(Σ_{n≤X}b(n)²log²(X/n)/n)^{1/2} ≍ (log X)^{3/2} = X^{o(1)}`, which equals the RH size. The repo detector is the `c=0` (total-leverage) case. There is no exponent gap, but there is also no slack: a Cauchy–Schwarz-type low estimate for `W_X` would itself be square-root cancellation for `μ`.

*Second QRH floor, on the multiplier side.* `H_η` contains `L_F^S(6s−3,χ_η)` (PR 910 Lemma 3.1). That factor is zero-free unconditionally only for `Re s>2/3`, and the closed-family trick helps only when `β*>3/5`. So (2.2) cannot be verified below about 2/3 without new input. The repo is strictly better here: its fixed multipliers are zero-free on all of `Re z>0`. Its whole deficit is on the producer side.

## 3. Family supremum, mapped onto the NRC32 energy

**What the supremum does in QRH.** The non-principal Poisson rows carry `1/L^S(x,ηχ_•(u))`. These are Hecke twists in the **same** family, so by definition they are holomorphic for `Re x>β*`. Their contours can be moved to `Re x=a+16e` with `a≤β*`, and the high estimate can be measured relative to `C(β*)`. Only the margins `ω, σ` must be uniform. The contradiction then selects some member with a zero within `ε*` of `β*`. Because the conclusion is family-wide, the repo's principal-member firewall (OPEN_CUTS §5) does not bite on the conclusion. It returns as two costs: uniform margins, and closure of the family under every twist the proof generates. The finite-order family is **not** closed under `η↦Ā⁶η⁶` (PR 910 §3). The repo's consumer contract already admits a countable family "when the arithmetic theorem supplies the entire family simultaneously".

**Repo inventory.** The Mellin–Landau consumers are ζ-only and have no producer, so no twisted error rows exist yet. Issue #740's "off-line propagation" is the QRH architecture (w5copg §3). PR 908 §3 shows that MHB32 gives no bootstrap: `Φ(κ)=(191+82κ)/273>κ`. PR 909 gives `μ = β ∗ χ_{−3}` exactly (Dirichlet convolution, with norm coefficients `β(n)=Σ_{N𝔞=n}μ_K(𝔞)`; this `β` is unrelated to the supremum `β*`). NRC32 (PR 905) is the natural host. Its split `F_{b²−1}−F_Y=S_Y+D_Y` (`b=Y+1`, `0≤D_Y<5/6`) and the open contraction `S_Y≤C(log 2Y)^A(1+F_Y)^{2−δ}` (NRC32 (6.1)) are **exponent-multiplicative**, so they are already relative in form.

**Twisted adapter (PROPOSED, exact).** For a primitive Dirichlet character `χ`, put `g_χ=μχ1_{≤Y}`, `z_χ=g_χ*g_χ`, `H_χ(r)=Σ_{j≤r}χ(j)/j`, and `m_χ(k)=Σ_{n≤k}μ(n)χ(n)/n`. Then for `Y<k<b²`:

`m_χ(k) = 2m_χ(Y) − Σ_{d≤Y²} z_χ(d)/d · H_χ(⌊k/d⌋)`.

*Proof.* `(μχ)*χ=δ`, since `χ` is completely multiplicative. Hence `μχ−v_χ=μχ*(δ−χ*g_χ)^{*2}` with `v_χ=2g_χ−χ*g_χ*g_χ`. Also `(χ*g_χ)(n)=χ(n)Σ_{d|n,d≤Y}μ(d)=[n=1]` for `n≤Y`. So the square is supported on `n≥b²`. ∎
Define the centered sequence `m^c_χ=m_χ−1/L(1,χ)` (with `1/ζ(1):=0`). Let `F_K(χ)=Σ_{k≤K}|m^c_χ(k)|²`, and let `S_Y(χ), D_Y(χ)` be the NRC32 cubic-mesh split. NRC32 (4.1) and (4.5) use only orthogonal projection and `|m(k)−m(k−1)|≤1/k`, so they hold verbatim, including for complex `χ`. (Exact checks in the header.)

**BM-2 (PROPOSED: exact exponent identity).** Let `Θ_χ` be the supremum of the real parts of the zeros of `L(s,χ)` (`Θ_{χ0}=Θ`). Then

`limsup_{Y→∞} log(1+S_Y(χ)) / log Y = 4Θ_χ − 2.`

*Proof.* (≤) Classically, for fixed `χ`, `Σ_{n≤x}μχ(n)≪x^{Θ_χ+ε}` (Perron with `1/L≪t^ε` right of `Θ_χ`; the interface of PR 908 §1). Partial summation of the tail gives `m^c_χ(x)≪x^{Θ_χ−1+ε}`, so `F_X(χ)≪X^{2Θ_χ−1+ε}` and `S_Y≤F_{b²−1}≪Y^{4Θ_χ−2+ε}`.
(≥) Suppose `S_Y(χ)≪Y^{c+ε}` for all `Y`. Then `F_X≤F_Y+S_Y+1` with `Y≍√X` gives, by induction, `F_X(χ)≪X^{c/2+ε}`. Cauchy–Schwarz gives `∫_X^{2X}|m^c_χ|≪X^{(1+c/2)/2+ε}`. So `∫_1^∞m^c_χ(t)t^{−s−1}dt=[1/L(1+s,χ)−1/L(1,χ)]/s`, an identity on `Re s>0`, converges absolutely for `Re s>(c−2)/4`. That forces `L(w,χ)≠0` for `Re w>½+c/4`, i.e. `c≥4Θ_χ−2`. ∎
*Calibration.* Trivial is `c=2`; QRH-IMPORT is `c=3/2` (consistent with PR 908's `F_X≪X^{3/4+ε}`); RH is `c=0`. **Any unconditional `S_Y≪Y^{2−η}` is a quasi-RH theorem** with boundary `1−η/4`.

**BM-3 (PROPOSED: family-relative single step).** Let `𝒳` be a set of primitive Dirichlet characters containing `χ0`, and `Θ*=sup({½}∪{Θ_χ:χ∈𝒳})`. Suppose there are a fixed `δ∈(0,1)` and, for each `χ∈𝒳`, a finite set `T(χ)⊂𝒳` such that **if `Θ*>½`**, then for every `ε>0`

`S_Y(χ) ≪_{χ,ε} Y^ε · max_{ψ∈T(χ)} (1+F_Y(ψ))^{2−δ}.`

Then `Θ*=½`; in particular RH holds.
*Proof.* Assume `Θ*>½` and put `κ*=2Θ*−1`. By (≤) of BM-2, `F_Y(ψ)≪Y^{κ*+ε}` for every `ψ`. So `S_Y(χ)≪Y^{(2−δ)κ*+ε'}`, and (≥) of BM-2 gives `Θ_χ≤Θ*−δκ*/4` for every `χ∈𝒳`. The saving is uniform, which contradicts the supremum. ∎

Remarks.
(i) The step need hold only once (not iterated), only up to `Y^ε` (not polylog), and only when `Θ*>½`. Its proof may use (H1): every `L(s,ψ)`, `ψ∈𝒳`, is zero-free on `Re s>Θ*`, with the usual growth consequences. This is strictly weaker as a target than NRC32 (6.1) from a crude seed (PR 908 §5).
(ii) The family is used only if a proof of the step generates twists. That happens, for example, when the floor/harmonic kernel `A_d(t)=tH_r−dr` of NRC32 (5.1) is separated in `r,s` by characters or residue classes, or when one passes to the norm coefficients `β` over `Q(√−3)` via OAI-NB26-L1 (where `χ_{−3}` and Hecke twists enter). `δ` must not depend on the conductors so generated. This is the exact QRH requirement.
(iii) Under the envelope, `F_{Y²}≈F_Y²` is the zero-driven scaling. So `δ>0` is precisely a QRH-type **relative high saving**, and BM-2 shows it cannot hold in any world with a zero near `Θ*`. Any proof of the step needs a low-side input that is true in all worlds (cf. the Beurling firewall in §2).

## 4. Proven versus heuristic, and the next step

| Item | Status |
|---|---|
| BM-0, BM-2, BM-3, twisted adapter | PROPOSED with complete short proofs; inputs: Lemma G (PROPOSED), NRC32 (4.1)/(4.5) (PROPOSED, PR 905), classical `M_χ(x)≪x^{Θ_χ+ε}` |
| BM-1 | PROPOSED identity; Mellin uniqueness plus reviewed algebra; numerically checked |
| floor `σ0≥5/6+(lx−ℓ)/6`, Part I/II positions | arithmetic exact; conditional on the manuscript's stated lemma outputs |
| "no reflection-small dual" for the rows | heuristic survey; not a theorem |
| leverage explanation of the floor; Beurling firewall | heuristic |
| drift `≈6.778 log X` and eventual positivity of `W_X` under RH | constant exact; positivity heuristic (needs RH and convergence of the zero sum) |

**Smallest gap and concrete next work.** The smallest gap is the hypothesis of BM-3 for `𝒳=` all primitive Dirichlet characters. It is RH-strength, and nothing here makes it easier. Two bounded deliverables would make the bridge reviewable:

- **(C1)** Port the scratch twisted checker into the PR 905 checker format. Cover complex characters mod `q≤12` in exact Gaussian rationals, and certify the twisted adapter and centered compression.
- **(C2)** Separate the NRC32 coarse kernel `K_I(r,s)` by Dirichlet characters (or through the norm coefficients `β` over `Q(√−3)`) and record the exact twist set `T(χ0)` generated. This decides whether a QRH-style bootstrap for issue 902 needs only a finite family (fixed constants suffice) or a growing-conductor family (then `δ` must be uniform, as in [OAI]).

Neither deliverable is evidence for RH. A finite panel of `S_Y/F_Y` cannot supply BM-3's hypothesis.
