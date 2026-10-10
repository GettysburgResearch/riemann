# L-105032 — The moving boundary cancels the pole but not the log: the θ = 1/2 germ ledger is ±4·log(s−1/2), and the pieces are NOT individually regular

Claim ID: `L-105032`
Status: **PROVED EXACT POLE CANCELLATION + DERIVED-AND-MEASURED LOG GERM (±4); CORRECTED DEPOSIT — the first push of this claim wrongly asserted bounded pieces; the error, its cause, and its catch are recorded in §5**
Created: 2026-08-21 (corrected same day)
Agent: claude (external reviewer lane)
Companions: `R-105024` (fixed-cut death: ½log² wall), `L-105025`
(depth-split calculus), `O-105010` (architecture). Replay:
`experiments/X-105030-maximal-license-and-circ13/lane_boundary/`.
RH status: **unproved, not addressed**

## 0. The reframe (proved trivially, load-bearing)

For `θ ≥ 1/3` no `n ≤ x` has three prime factors `> x^θ`; for `θ ≥ 1/2`
at most one. The "moving-cut witness" **equals the full SHARP witness**
for every `θ ∈ [1/3, 1/2]`: the architecture never changes the gate — it
decomposes it. At `θ = 1/2`: `Ψ = Ψ_sm + Ψ₁`,
`Ψ₁(x) = Σ_{n=mp≤x,\ p>√x} μ(n)n^{-1/2}T(x/n)` (`m < p` automatic; the
class window of the pair `(m,p)` is `x ∈ [mp, p²)`).

## 1. Exact transform and the two germ layers

For `Re s > 1/2`, `z = s+1/2`, `K(s) = (s+3/2)/(s(s−1/2))`,
`R_s(v) = 4v^{1/2−s}/(s−1/2) − 3v^{−s}/s`:

```
F₁(s) = K(s)·D₁(z) + 4/(s−1/2)·S₂(s) − (3/s)·S₃(s),
  D₁(z) = −Σ_p p^{−z} M_z(p⁻),   M_z(t) = Σ_{m≤t} μ(m)m^{−z},
  S₂(s) = Σ_p p^{−2s} A_{p⁻},    S₃(s) = Σ_p p^{−2s−1/2} B½_{p⁻}.
```

**(a) Pole layer — cancels exactly (proved, unchanged).** The two
`1/(s−1/2)` coefficients are `4·D₁(1) = −4Σ_p A_{p⁻}/p` and
`+4Σ_p A_{p⁻}/p`: equal and opposite **by definition** (indeed
identically at every finite truncation of the prime sum). `κ₁ =
Σ_p A_{p⁻}/p = 0.737223…` (PNT-convergent). `S₃` is analytic near `1/2`.
**F₁ has no pole at `s = 1/2`.**

**(b) Log layer — survives (derived; measured two independent ways).**
`M_z(p⁻) = 1/ζ(z) − Σ_{m≥p}μ(m)m^{−z}` gives
`D₁(z) = −P(z)/ζ(z) + (PNT-regular)`, and near `z = 1`:
`−P(z)/ζ(z) = (z−1)\log(z−1)(1+o(1))` (the `1/ζ` zero times the prime-zeta
log). The kernel pole multiplies this vanishing-but-not-linear term:

```
F₁(s)  =  4·log(s−1/2) + C₁ + o(1),
F_sm(s) = −4·log(s−1/2) + C₂ + o(1),      C₁ + C₂ = F(1/2) = 4.
```

The moving boundary `p² = x` enters only the analytic tail terms
(`S₂, S₃`); the surviving log lives in `K·D₁` — the pair-set/hyperbola
structure — **so smoothing the boundary weight `w(p²/x)` cannot remove
it**; only a pair-set reorganization or an explicit `P(z)/ζ(z)`
compensator could.

## 2. Measurements (two independent routes, agreeing)

*Mellin side* (sieve `10⁶`, true `M_z`): `F₁(s)` at
`s = 0.6, 0.55, 0.52, 0.51, 0.505`:
`−4.34, −5.77, −6.99, −7.47, −7.74` — divergent downward drift consistent
with the log germ (finite prime truncation moderates the slope).
*x-space* (truncation-free, decisive):
`Ψ₁(10⁴) = −47.589`, `Ψ₁(10⁶) = −328.953`, with
`Ψ₁(x)·\log x/√x = −4.38, −4.55` — i.e.

```
Ψ₁(x) ≈ −(4+o(1))·√x/log x,     Ψ_sm(x) ≈ +(4+o(1))·√x/log x,
```

while `Ψ = Ψ_sm + Ψ₁` stays `≈ 2`. The cancellation demand between the
pieces grows like `√x/(\log x·|Ψ|)`: ≈ 26 at `10⁴`, ≈ 147 at `10⁶`.

## 3. The corrected verdict

* The fixed cut's wall was `½\log²(z−1)` (`R-105024`); the moving
  boundary **demotes it to a single log — priced down, not out.**
  (`R-105024 §4`'s phrase "priced out" is corrected accordingly.)
* Separate-piece positivity/estimation at `θ = 1/2` is **impossible**:
  each piece is log-singular at `s = 1/2` and of one-signed size
  `∓4√x/\log x` in `x`-space. The `102000` Type-II program must estimate
  its piece **with** the smooth-block cancellation, or reorganize the
  pair set first (hyperbola-symmetrization direction; open).
* What remains genuinely better than the fixed cut: the pole is gone
  exactly; the singular ledger is one explicit log with coefficient `±4`
  and PNT-convergent constants; and the demotion mechanism (incomplete-
  kernel tails at the moving boundary) is now explicit for the
  `θ ∈ [1/3,1/2)` three-piece follow-up.

## 4. Scope

The pole cancellation and the transform identity are proved; the log germ
is derived at zero-free-region strength (`−P/ζ` structure) and measured
two ways; no unconditional claim is made about finer continuation
structure. Nothing here proves positivity of any piece or bears on RH.

## 5. Correction record (per the failure-ledger protocol)

The first push of this claim asserted "pieces individually regular,
ledger 4 = 3.37 + 0.63," supported by a numeric that evaluated `D₁` with
the **z-independent** prefix `A_{p⁻} = M_1(p⁻)` in place of the required
`M_z(p⁻)` — a substitution valid only exactly at `s = 1/2`, which
manufactured spurious boundedness. The originating memo had explicitly
flagged the hole ("if `D₁ ~ (z−1)\log(z−1)` then contributes log") and
the conclusion overrode the flag. The error was caught within the hour by
this session's own recovery/adversarial pipeline (independent re-check
contradicted the numbers; the orchestrator re-verified with the correct
`M_z` and confirmed the contradiction on every digit). The corrected
driver `lane_boundary/f1_regularity.py` now asserts the divergent drift,
the x-space `−4√x/\log x` law, and the exact pole-coefficient
cancellation — the parts that were always true.
