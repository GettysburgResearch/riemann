# Fixed-detector positivity is never easier than RH: the Landau–Ingham dichotomy

**Scientific status:** RH remains unproved. This packet proves that every one-sided
positivity target attached to a *fixed* zero-safe Möbius detector of the August 22
release is either exactly equivalent to RH, strictly harder than RH, or false. It
refutes one registered target unconditionally (the minimal ratio-eight wavelet), shows
that the pointwise SHARP-scalar target is false under linear independence of the zero
ordinates, and supplies exact numbers for every canonical detector.

Claim IDs allocated here: `L-109000`, `T-109001`, `R-109002`, `X-109003`, `X-109004`.
No historical ID is reused.

---

## 0. The class of detectors

Throughout, a *band kernel* is a function `K : (0,∞) → ℝ` with `K = 0` on `(0,1)` and

\[
K(y) = a_i\sqrt y + b_i + c_i \log y \qquad (m_i \le y < m_{i+1}),
\]

on finitely many intervals with `1 = m_0 < m_1 < … < m_r`, the last interval being
`[m_r, ∞)`. Every detector kernel of the August 22 release is of this form:

| detector | source | kernel | Mellin multiplier `K̂(s)` |
|---|---|---|---|
| `h_μ`, `h_67` (SHARP scalar, L-99270) | `μ`, `β` | `T(y) = 4√y − 3` on `[1,∞)` | `(s+3/2)/(s(s−1/2))` |
| rows `2`, `3` (L-96000) | `μ` | piecewise `log(Y/m)` | `H_j(s+1/2)/s²` |
| fixed `5:3` scalar `W` (L-99261) | `μ` | `5Q(2)+3Q(3)` | `(6ζ(z)+5P_2(z)+3P_3(z))/s²`, `z=s+1/2` |
| ratio-eight wavelet `G_μ` (PR #674) | `μ` | three bands on `[1,8]` | `(s+3/2)(1−√2·2^{−s})(1−2^{−s})²/(s²(s−1/2))` |
| box smoothing `S_A h_67` (L-99270.3) | `β` | `T` smoothed | `((1−A^{−s})/s)·(1−67^{−z})(s+3/2)/(s(s−1/2))` |

Here `β(n) = μ(n) − 𝟙_{67|n}μ(n/67)`, with Dirichlet series `(1−67^{−z})/ζ(z)`.

For a band kernel and a source `a ∈ {μ, β}` with Dirichlet series `A(z)`, put

\[
D_K(x) = \sum_{n\le x} \frac{a(n)}{\sqrt n}\,K(x/n),
\qquad
F_K(s) = \int_1^\infty D_K(x)\,x^{-s-1}\,dx = \widehat K(s)\,A(s+\tfrac12)
\quad(\Re s > \tfrac12).
\tag{0.1}
\]

Since `∫_m^∞ √y·y^{−s−1}dy = m^{1/2−s}/(s−1/2)`, `∫_m^∞ y^{−s−1}dy = m^{−s}/s`, and
`∫_m^∞ log y·y^{−s−1}dy = m^{−s}(log m/s + 1/s²)`, the multiplier `K̂` is entire
except for a pole of order at most one at `s = 1/2` and order at most two at `s = 0`.
Hence `F_K` is meromorphic on `ℂ`, and in `Re s > −1/2` its poles lie in

\[
\{0,\ \tfrac12\}\ \cup\ \{\rho - \tfrac12 : \zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

The kernel is **zero-safe** if `K̂(ρ−1/2) ≠ 0` at every nontrivial zero `ρ` with
`Re ρ ≠ 1/2` (this is the hypothesis the release verifies for each of its kernels; for
the table above the multipliers vanish only on `Re s ∈ {0, 1/2}`, so off-line zeros are
never cancelled).

**Main term.** Let `P_K(u)` be the sum of the residues of `F_K(s)e^{su}` at the real
poles `s ∈ {0, 1/2}`. For every kernel in the table the point `s = 1/2` is removable,
because `A(1) = 0` cancels the simple pole of `K̂`. Thus `P_K(u) = c_1 u + c_0`
(double pole at `0`), `P_K = c_0` (simple pole) or `P_K = 0` (no pole). Explicitly:

| detector | `P_K(log X)` |
|---|---|
| `h_μ` | `c_0 = −3/ζ(1/2) = 2.054296` |
| `h_67` | `c_0 = −3(1−67^{−1/2})/ζ(1/2) = 1.803324` |
| `S_67 h_67` | `c_0 = 1.803324·log 67 = 7.5824` |
| row 2 | `1.111710·log X − 0.063153` |
| row 3 | `0.406456·log X − 0.059039` |
| `W` | `6.777920·log X − 0.492884` |
| `G_μ` | `0` (the factor `(1−2^{−s})²` cancels `s²`) |

**Zero residues.** At a simple zero `ρ = 1/2 + iγ` on the line, `F_K` has the simple
pole `s = iγ` with residue

\[
r_\gamma = \frac{\widehat K(i\gamma)\,A_0(\rho)}{\zeta'(\rho)},
\qquad A_0 = 1 \text{ for } \mu,\quad A_0(\rho) = 1-67^{-\rho} \text{ for } \beta.
\tag{0.2}
\]

Note the decay classes: `|K̂(iγ)| ≍ 1/|γ|` for the SHARP kernel (a discontinuous
kernel with a `√y` mode), while `|K̂(iγ)| ≍ 1/|γ|²` for the rows, `W`, `G_μ` and the
box smoothing.

---

## 1. `L-109000` — Ingham's oscillation inequality in Mellin form

**Lemma.** Let `D : [1,∞) → ℝ` be locally integrable with `D(x) = O_ε(x^ε)` for every
`ε > 0`, and suppose `F(s) = ∫_1^∞ D(x)x^{−s−1}dx` (absolutely convergent for
`Re s > 0`) continues meromorphically to `Re s > −δ_0` for some `δ_0 > 0`, with all
poles on the closed half-plane `Re s ≥ −δ_0` lying on the imaginary axis, and with the
pole at `s = 0` (if any) having Laurent principal part `Σ_{k≥1} c_k s^{−k}`. For real
`T > 0` not the ordinate of a pole, let

\[
\mathcal P_T(u) = \sum_{0<|\gamma|<T}\Big(1-\frac{|\gamma|}{T}\Big)\operatorname{Res}_{s=i\gamma}\big(F(s)e^{su}\big),
\qquad
R_0(u) = \operatorname{Res}_{s=0}\big(F(s)e^{su}\big).
\]

If `D(x) ≥ 0` for all sufficiently large `x`, then for every such `T`

\[
\liminf_{u\to\infty}\big(R_0(u) + \mathcal P_T(u)\big) \ \ge\ 0.
\tag{1.1}
\]

*Proof.* Write `A(u) = D(e^u)`, so `F(s) = ∫_0^∞ A(u)e^{−su}du`. Fix `T`, and let
`k_T(v) = (T/2π)(\sin(Tv/2)/(Tv/2))^2 ≥ 0`, the Fejér kernel, with `∫k_T = 1`,
`k_T(v) ≤ 2/(πTv²)`, and `∫k_T(v)e^{−itv}dv = (1−|t|/T)_+`.

Fix `σ > 0`. Since `A(u)e^{−σu} ∈ L¹(0,∞)` and `k_T` is bounded with compactly
supported Fourier transform, Fubini gives, for every real `y`,

\[
\int_0^\infty A(u)e^{-\sigma u}k_T(u-y)\,du
= \frac1{2\pi}\int_{-T}^{T}\Big(1-\frac{|t|}{T}\Big)F(\sigma+it)e^{ity}\,dt.
\tag{1.2}
\]

Suppose `A(u) ≥ 0` for `u ≥ u_0`. Then for `y > u_0` the left side of (1.2) is at least
`−∫_0^{u_0}|A(u)|k_T(u−y)du ≥ −C_A/(T(y−u_0)²)`, uniformly in `σ`.

The right side equals `e^{−σy}·(2πi)^{−1}∫_{σ−iT}^{σ+iT} w(s)F(s)e^{sy}ds` with
`w(s) = 1 − |Im s|/T`. Move the contour to `Re s = −δ` for a fixed `0 < δ < δ_0`
chosen so that no pole lies on the new line; `w` vanishes on the horizontal segments
`Im s = ±T`, so they contribute nothing, and the finitely many poles enclosed are
`s = 0` and `s = iγ` with `|γ| < T`. Hence

\[
\text{RHS of (1.2)} = e^{-\sigma y}\Big[R_0(y) + \mathcal P_T(y) + \frac1{2\pi i}\int_{-\delta-iT}^{-\delta+iT} w(s)F(s)e^{sy}\,ds\Big],
\]

and the last integral is `O_T(e^{−δy})` because `F` is bounded on the compact segment.
Let `σ ↓ 0` at fixed `y`: the bracket does not depend on `σ` and `e^{−σy} → 1`, while
the lower bound on the left side is uniform in `σ`. Therefore, for all `y > u_0`,

\[
R_0(y) + \mathcal P_T(y) \ \ge\ -\frac{C_A}{T(y-u_0)^2} - O_T(e^{-\delta y}),
\]

which is (1.1). ∎

**Remarks.** (i) No linear-independence hypothesis, no convergence of the full zero
sum, and no simplicity of zeros beyond the finitely many poles with `|γ| < T` is used;
for a multiple pole the residue is still a finite exponential polynomial in `u`.
(ii) When `R_0 ≡ c_0` is constant and all poles with `|γ| < T` are simple,
`𝒫_T(u) = Σ_{0<γ<T}(1−γ/T)·2Re(r_γe^{iγu})` is a real trigonometric polynomial with
mean zero. By almost periodicity its infimum is a limit inferior, so (1.1) reads
`inf_u 𝒫_T(u) ≥ −c_0`. (iii) This is Ingham's theorem of 1942 in the normalisation used
for `lim sup M(x)/√x` computations (Kotnik–te Riele, Hurst); it is reproved here so that
the packet is self-contained.

---

## 2. `T-109001` — the dichotomy

**Theorem.** Let `K` be a zero-safe band kernel and `a ∈ {μ, β}`, with `D_K`, `F_K`,
`P_K`, `r_γ` as in §0. Then:

**(A) Negative mass.** For every `ε > 0` the following are equivalent:
`∫_1^X (D_K)_-(t)\,dt/t = X^{o(1)}`; `D_K(x) = O_ε(x^ε)`; RH. In particular the
"subpower logarithmic negative mass" premise of the Mellin–Landau consumer
(`API.MELLIN.SUBPOWER_NEGATIVE_MASS`, `OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS`,
`OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS`, `OPEN.DIRECTMAIN.TAYLOR_CRITICAL`, `MWOC99910`)
is, for every fixed kernel, a restatement of RH and not a weaker or intermediate
statement.

**(B) Eventual nonnegativity.** Suppose `D_K(x) ≥ 0` for all large `x`. Then RH holds,
and for every `T` as in §1,

\[
\inf_u \mathcal P_T(u) \ \ge\ -\,\liminf_{u\to\infty} P_K(u)\qquad\text{(with the convention that a divergent main term dominates)}.
\tag{2.1}
\]

Consequently:

1. *No main term* (`P_K ≡ 0`): eventual nonnegativity is **false**, unconditionally,
   as soon as `K̂(iγ_1) ≠ 0` at the first zero `ρ_1 = 1/2 + 14.1347…i`.
2. *Bounded main term* (`P_K ≡ c_0 > 0`): eventual nonnegativity implies RH and
   `2Σ_{0<γ<T}(1−γ/T)|r_γ| ≤ c_0` **on every set of zero ordinates that is linearly
   independent over ℚ**; in particular it is false under the Linear Independence
   hypothesis whenever `Σ_γ|r_γ| = ∞` or `2Σ_γ|r_γ| > c_0`. Unconditionally it is false
   as soon as one exhibits `T` and `u` with `𝒫_T(u) < −c_0`.
3. *Growing main term* (`P_K(u) = c_1u + c_0`, `c_1 > 0`): eventual nonnegativity
   implies RH; conversely it follows from RH **together with** the boundedness of
   `D_K − P_K(log ·)`, which holds if all zeros are simple and `Σ_γ|r_γ| < ∞`
   (sufficient when `K̂(s) ≪ |s|^{−2}` on vertical lines and
   `Σ_γ |ζ'(ρ)|^{−1}γ^{−2} < ∞`). It is therefore **at least as hard as RH and not known
   to follow from RH**.
4. *Negative growing main term* (`c_1 < 0`): eventual nonnegativity is **false**.

In no case is a fixed-detector positivity statement weaker than RH.

*Proof of (A).* `RH ⇒ D_K ≪ x^ε`: under RH, `M(t) = Σ_{n≤t}μ(n) ≪ t^{1/2+ε}`
(Littlewood), hence by partial summation `Σ_{n≤t}μ(n)/n ≪ t^{−1/2+ε}`,
`Σ_{n≤t}μ(n)n^{−1/2} ≪ t^ε` and `Σ_{n≤t}μ(n)n^{−1/2}log n ≪ t^ε`; the same bounds hold
for `β` because `Σ_{n≤t}β(n)f(n) = Σ_{n≤t}μ(n)f(n) − Σ_{m≤t/67}μ(m)f(67m)`. On each
band `[m_i, m_{i+1})` the sum `Σ_{x/m_{i+1}<n≤x/m_i} a(n)n^{−1/2}K(x/n)` is a linear
combination of `√x·Σ a(n)/n`, `Σ a(n)/√n` and `log x·Σ a(n)/√n − Σ a(n)log n/√n` over
the same range, each `≪ x^ε`. Summing the `r+1` bands gives `D_K ≪ x^ε`, hence
`∫_1^X(D_K)_- dt/t ≪ X^ε`.

`Negative mass X^{o(1)} ⇒ RH`: this is the release's Mellin–Landau consumer
(L-99270 §2 with L-99272 §3–5, PROOF.md §4 of the wavelet packet), whose hypotheses
(finite abscissa, analyticity of `F_K` at every positive real `s`, zero-safety) hold
for every kernel in §0; we do not repeat it. ∎

*Proof of (B).* RH follows from (A) since eventual nonnegativity forces bounded negative
mass. Under RH, `D_K ≪ x^ε` by (A), so `L-109000` applies to `D = D_K` with `F = F_K`
(meromorphic on `ℂ`; poles in `Re s ≥ −δ_0` only at `0` and `ρ − 1/2 = iγ` for
`0 < δ_0 < 5/2`, the trivial zeros being at `Re s ≤ −5/2`), which gives (2.1).

Case 1. With `P_K ≡ 0` and `γ_1 < T < γ_2 = 21.02…`, `𝒫_T(u) = 2(1−γ_1/T)|r_{γ_1}|\cos(γ_1u + \arg r_{γ_1})`
(the zero `ρ_1` is simple, `ζ'(ρ_1) = 0.78330 + 0.12470i`), whose infimum is
`−2(1−γ_1/T)|r_{γ_1}| < 0`, contradicting (2.1). If RH fails, eventual nonnegativity is
already excluded by (A).

Case 2. (2.1) with `P_K ≡ c_0` is `inf_u 𝒫_T(u) ≥ −c_0`. If the ordinates in `(0,T)`
are linearly independent over ℚ, Kronecker's theorem gives
`inf_u 𝒫_T(u) = −2Σ_{0<γ<T}(1−γ/T)|r_γ|`.

Case 3. `⇒ RH` as above. For the converse, assume RH, all zeros simple, `K̂(s) ≪ |s|^{−2}`
on vertical lines and `Σ_γ|r_γ| < ∞`. Under RH one has `1/ζ(σ+it) ≪ |t|^ε` for
`σ ≥ 1/2 + ε` (Titchmarsh, *Theory of the Riemann zeta-function*, Thm 14.2), and by the
functional equation `1/ζ(σ+it) ≪ |t|^{σ−1/2+ε}` for `σ < 1/2`. Mellin inversion of (0.1)
on `Re s = 1` (valid at points of continuity of `D_K`, i.e. for `x ∉ ℕ·{m_i}`), followed
by moving the contour to `Re s = −δ` along a sequence of heights `T_k → ∞` at distance
`≫ 1/\log T_k` from every ordinate (where `1/ζ(σ+iT_k) ≪ T_k^ε` uniformly in
`σ ≥ 1/2−δ`, Titchmarsh Thm 14.16), gives

\[
D_K(x) = P_K(\log x) + \lim_k \sum_{|\gamma|<T_k} r_\gamma x^{i\gamma} + O_K(x^{-\delta}),
\]

the vertical integral on `Re s = −δ` being absolutely convergent because
`|K̂(s)/ζ(s+1/2)| ≪ |t|^{−2−δ+ε}` there. With `Σ|r_γ| < ∞` the limit is the absolutely
convergent series `Σ_γ 2Re(r_γx^{iγ})`, bounded by `2Σ_γ|r_γ|`, so
`D_K(x) ≥ c_1\log x + c_0 − 2Σ_γ|r_γ| − o(1) > 0` for large `x`.

Case 4 is immediate from Case 3's expansion when `Σ|r_γ|<∞`, and in general from (2.1),
since `P_K(u) → −∞` while `𝒫_T` is bounded. ∎

**Scope note.** The theorem is about the *conclusion-facing* statements. It says nothing
against the exact identities, kernel factorisations, or finite computations of the
release, which are correct at their scopes. It says that attaching a positivity or
negative-mass target to a fixed detector cannot lower the difficulty below RH, whatever
the kernel.

---

## 3. `R-109002` — refutation: the ratio-eight wavelet is negative for arbitrarily large `X`

**Statement.** Let `G_μ(X) = Σ_{n≤X}μ(n)n^{−1/2}K_0(X/n)` be the minimal ratio-eight
ordinary-Möbius wavelet of PR #674 (`ARITH.WAVELET.MINIMAL_RATIO8`). Then there is no
`X_0` with `G_μ(X) ≥ 0` for all `X ≥ X_0`. More generally the same holds for every
zero-safe band kernel whose multiplier has no pole in `Re s ≥ 0` and satisfies
`K̂(iγ_1) ≠ 0`.

*Proof.* This is Case 1 of `T-109001`. For `G_μ`,
`K̂(s) = (s+3/2)(1−√2·2^{−s})(1−2^{−s})²/(s²(s−1/2))`, holomorphic at `s = 0` (double
zero of `(1−2^{−s})²`) and at `s = 1/2` after multiplication by `1/ζ(s+1/2)`
(PROOF.md §4 of the wavelet packet). At `s = iγ_1`,
`2^{−iγ_1} = e^{−iγ_1\log 2}` with `γ_1\log 2/2π = 1.5593…∉ℤ`, so `(1−2^{−iγ_1}) ≠ 0`,
and `|√2·2^{−iγ_1}| = √2 ≠ 1`, so `K̂(iγ_1) ≠ 0`. Numerically
`r_{γ_1} = −0.036586 + 0.045196i`, `|r_{γ_1}| = 0.058148`, so already
`inf_u 𝒫_T(u) ≤ −0.1163·(1−γ_1/T)` for `T ∈ (γ_1, γ_2)`. ∎

**Corroboration.** Direct evaluation up to `X = 10^7` finds `G_μ < 0` on roughly one half
of a logarithmic grid, with minimum `−1.526` and last observed sign change beyond
`1.8·10^6` (see `X-109003`). The refutation supersedes the packet's remark "pointwise
positivity is false at `X = 4`" by the infinite statement.

**What this changes in the graph.** `MWOC99910` and the negative-mass form
`∫_1^X (G_μ)_- dt/t = X^{o(1)}` remain exactly RH (Theorem (A)); the pointwise form is
false. Any proposal that routes through eventual pointwise positivity of a detector with
no main term (every "critical-zero-safe" kernel with an `s²` in its numerator) is dead
on arrival.

---

## 4. `X-109003` — exact numbers for the canonical detectors

Zeros: Odlyzko's table of the first 100,000 ordinates (9 decimals). `ζ'(ρ)`: mpmath
1.3.0 at 20 digits. Residues from (0.2). Detectors evaluated directly from a Möbius sieve
to `10^7`. Scripts and raw outputs are in `scripts/` and `outputs/`.

**Validation of the residue formulas** (`outputs/detectors_1e7.txt`): at
`X = 10^3 … 10^7`, `main term + Σ_{γ≤γ_N} 2Re(r_γX^{iγ})` reproduces the direct values of
rows 2, 3, `W` and `G_μ` to `10^{−5}` or better, and the SHARP scalars to `10^{−2}`
(their zero sum converges only conditionally). The identity `5·row₂ + 3·row₃ = W` holds
to `10^{−8}`, and `G_μ(4) = −1.46194`, inside the packet's certified interval.

**Zero mass** `2Σ_{γ≤γ_N}|r_γ|` versus the main term:

| `N` zeros | `h_μ` (`c_0 = 2.054`) | `h_67` (`c_0 = 1.803`) | row 2 | row 3 | `W` | `G_μ` (`c_0 = 0`) | `S_{67}h_{67}` (`c_0 = 7.58`) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 0.556 | 0.566 | 0.048 | 0.031 | 0.294 | 0.187 | 0.040 |
| 100 | 1.170 | 1.199 | 0.059 | 0.038 | 0.351 | 0.219 | 0.050 |
| 1000 | 1.988 | 2.030 | 0.062 | 0.039 | 0.366 | 0.228 | 0.052 |
| 4840 | 2.643 | 2.694 | 0.063 | 0.040 | 0.368 | 0.229 | 0.052 |
| 10000 | 2.966 | 3.021 | 0.063 | 0.040 | 0.369 | 0.229 | 0.052 |
| 17496 | 3.224 | 3.283 | 0.063 | 0.040 | 0.369 | 0.230 | 0.053 |

(`ζ'(ρ)` was computed for the first 17,496 zeros, up to height `T = 16056`; the raw
values are in `outputs/zetaprime_first17496.txt`.)

**Reading.**

- `h_μ`, `h_67` (bounded main term, `|r_γ| ≍ 1/(γ|ζ'(ρ)|)`): the zero mass passes the
  main term between `N = 1000` and `N = 4840`, reaches `3.22` at `N = 17496`, and keeps
  growing by roughly `0.9` per decade of `N` (under the Hughes–Keating–O'Connell conjecture
  `Σ_{γ≤T}|ζ'(ρ)|^{−1} ≍ T(\log T)^{1/4}` it diverges). Under LI the pointwise SHARP
  target of PR #647 (T-99250) is therefore **false**; unconditionally its refutation is a
  finite Kronecker alignment computation of the Kotnik–te Riele/Hurst type on the first
  few thousand zeros. Direct evaluation shows `h_67 ≥ 1.285` on `[2, 10^7]`, so the
  first negative value lies far beyond direct reach, exactly as for `M(x)/√x`.
- rows 2, 3, `W` (growing main term, zero mass `0.06`, `0.04`, `0.37`): the targets
  `OPEN.ARITH.ROWS23_NATIVE`, `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` (sign form) are
  Case 3: `RH + (simple zeros and Σ|r_γ|<∞) ⇒ target ⇒ RH`. They are RH plus a
  summability hypothesis, never less.
- `S_{67}h_{67}` (L-99270.8; main term `7.58`, zero mass `0.05`): same as the rows.
- `G_μ`: Case 1, false.

---

## 5. `X-109004` — control experiment where RH is a theorem

Over `F_q[T]` the Riemann hypothesis for `L(u,χ)` is Weil's theorem. For an irreducible
`Q` of degree `d` and the quadratic character `χ(f) = f^{(q^d−1)/2} \bmod Q`, the exact
analogue of the cumulative fixed detector is

\[
D_\chi(n) = \sum_{\deg f \le n} \mu(f)\chi(f)\,q^{-\deg f/2},
\qquad
\sum_n D_\chi(n)u^n = \frac{1}{(1-u)\,L(u/\sqrt q,\chi)},
\]

so `D_χ(n) = A_χ + Σ_j B_j u_j^{−n}` with `A_χ = 1/L(q^{−1/2},χ)` (the main term from the
pole at `u = 1`) and `|u_j| = 1` (Weil). The question "is `D_χ(n) ≥ 0` for all large
`n`" is decided by the balance `A_χ` versus `Σ_j|B_j|`, i.e. by the central value against
the residues, and not by RH, which holds for every `χ`. Census (`scripts/ffield.py`,
`n ≤ 20000`; every reciprocal root checked to have modulus `√q`):

| field | degrees | characters | negative infinitely often | eventually nonnegative |
|---|---|---:|---:|---:|
| `F_3` | `2–6` | 193 | 128 | 65 |
| `F_3` | `2–7` | 505 | 440 | 65 |
| `F_5` | `2–4` | 200 | 65 | 135 |
| `F_7` | `2–3` | 133 | 112 | 21 |

The number-field detectors sit in the same picture, with two differences: the zero mass
of the SHARP kernel diverges (infinitely many zeros with `|r_γ| ≍ 1/(γ|ζ'(ρ)|)`), and
the main term of the rows grows like `log X` (double pole). Neither difference makes
positivity a *mechanism*: in the function-field laboratory, positivity is downstream of
the zero locations and never upstream.

---

## 6. Consequences for the open-cut inventory

| node | form | verdict from this packet |
|---|---|---|
| `OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS`, `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` (mass form), `OPEN.DIRECTMAIN.TAYLOR_CRITICAL`, `MWOC99910` | subpower negative mass of a fixed detector | **= RH** exactly (Theorem A) |
| `OPEN.ARITH.ROWS23_NATIVE` (sign form), `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` (sign form), L-99270.8 box positivity | eventual nonnegativity, growing/large main term | **RH + zero-summability**: at least as hard as RH, not implied by RH |
| pointwise SHARP tail (T-99250, PR #647) | eventual nonnegativity, bounded main term | **false under LI**; finite computation away from unconditional |
| pointwise `G_μ ≥ 0` and every kernel with no real pole | eventual nonnegativity, no main term | **false unconditionally** (`R-109002`) |
| `OPEN.ARITH.FCHD67` | one-sided native producer for rows 2, 3 | implies the sign form of `ROWS23_NATIVE`, hence at least "RH + summability" |
| `OPEN.ARITH.CV` | weighted downward variation of `𝔥_1` | already RH-equivalent (L-99944); Theorem A gives the same for every band kernel |

The "positive reserve" strategy (adding a positive main term, choosing a kernel with a
larger `c_0`, or smoothing) only moves a target between the rows of this table; it cannot
move it below RH. This is the precise sense in which the fixed-detector programme is a
closed loop.

---

## 7. Falsifiers

- A zero-safe band kernel with `P_K ≡ 0`, `K̂(iγ_1) ≠ 0`, and `D_K ≥ 0` eventually would
  contradict `L-109000`; exhibiting one would refute this packet.
- A proof that `Σ_γ 1/(γ|ζ'(ρ)|)` converges would remove the LI-conditional falsity
  claim for the SHARP tail (it would not create a route to RH).
- An error in the residue formula (0.2) would show up as a mismatch in
  `outputs/detectors_1e7.txt`; none is present at the `10^{−5}` level for the four
  absolutely convergent detectors.
