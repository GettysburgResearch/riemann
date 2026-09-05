# R-105024 — Fixed-cut depth-truncated gates are analytically empty: the truncation installs its own s = 1/2 singularity, and positivity of the truncated witness carries no zero-free information

Claim ID: `R-105024`
Status: **PROVED CLASS-LEVEL NO-GO (Mellin side) — RECORDS THE DEATH OF A CANDIDATE IDEA; RH NOT ADDRESSED**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Depends on: `L-99270`/`L-99272` @
`review/gpt56-pro/99700-owner-degeneracy-cross-core` (kernel transform and
Landau engine); `L-105025` (depth-split calculus, this packet);
complements `T-105000` (budget) and `O-105010` (moving cut).
RH status: **unproved, not addressed**

## 1. The killed idea (recorded per protocol: failures are deliverables)

Candidate idea: truncate the rough Euler product at a FIXED cut (67) and
bounded depth `K` — e.g. the depth-`\le 2` witness
`\Psi^{(\le2)}(x) = \sum_{n \le x,\ \Omega_{\text{rough}}(n) \le 2}
\mu(n)n^{-1/2}T(x/n)` and its Harnack form `h^{(\le2)}` — hoping the
truncated gate is easier while keeping the Landau detector.

## 2. The death, in three exact steps (full derivations in `L-105025`;
replay `X-105020/lane_primezeta/`)

1. **Transform.** For `\Re s > 1/2`, `z = s + 1/2`:
   `F^{(\le2)}(s) = (1 - 67^{-z})\,\frac{s+3/2}{s(s-1/2)}\,S(z)\,
   [1 - P_{67}(z) + (P_{67}(z)^2 - P_{67}(2z))/2]`, with
   `S(z) = \prod_{p\le61}(1-p^{-z})` and `P_{67}` the tail prime zeta.
   (Numerically verified against sieve-exact `h^{(\le2)}` to `2.8\cdot
   10^{-12}` at `s=2`.)
2. **Unconditional pin.** As `z \to 1^+` the truncated bracket blows up:
   `B_2(z) = \tfrac12\log^2(z-1) + (1-a_{67})\log(z-1) + O(1) \to +\infty`
   (measured: `1.81, 19.60, 58.67` at `z-1 = 10^{-2},10^{-4},10^{-6}`).
   The kernel's `1/(s-1/2)` pole is therefore NOT cancelled — in the full
   gate it is cancelled precisely by the zero of `1/\zeta(z)` at `z = 1`,
   i.e. by the all-depth alternating cancellation that truncation
   discards. Hence `F^{(\le2)}(s) \to +\infty` as `s \to 1/2^+`, and the
   abscissa of convergence is **exactly `1/2`, unconditionally** (upper
   bound from `|\Psi^{(\le2)}| = O(\sqrt x \log x)`).
3. **Landau saturated by an artifact.** The Landau step (`L-99272 §3`)
   says: nonneg density ⟹ the real point of the abscissa is singular. Here
   that singularity exists for structural reasons having nothing to do
   with zeta zeros. The off-line branch points (at `s = \rho - 1/2`, all
   with `\Re < 1/2`, genuinely present by `L-105025`'s no-cancellation
   lemma) are never reached. **Positivity of `h^{(\le2)}` — verified
   empirically on all of `[1,10^6]` (min `1.28` on `[2,10^6]`;
   `h(1^+) = 1`), and expected at
   main-term level from the Mertens-type divergence `A^{(\le2)}(x) =
   (S(1)/2)(\log\log x)^2(1+o(1))` (Selberg–Delange-type; asserted here at
   heuristic-plus-numerics strength, and NOT needed for this refutation) —
   yields no zero-free statement whatsoever.**

## 3. The parity see-saw (why no fixed depth works)

As `z \to 1^+`, `e_k \sim \log^k(1/(z-1))/k!`, so a depth-`K` truncation
has bracket `\sim \ell^K/K!` with `\ell \to -\infty`: for **even `K`** the
gate is (asymptotically) true but the transform diverges to `+\infty` at
`s = 1/2` — consumer empty; for **odd `K`** the transform diverges to
`-\infty` — the gate itself is false. Subtracting finitely many
compensator terms cannot repair it: the `s = 1/2` germ is an infinite
singular series `\alpha(z)\ell^2 + \beta(z)\ell` with analytic
`\alpha,\beta`, and matching it in `x`-space is a Selberg–Delange
error-term problem whose unconditional control is the classical zero-free
region — the truncation converts RH-hard cancellation into a PNT-strength
error problem, gaining nothing. (This compensator paragraph is an argued
reduction, not a proof; the proved per-`K` see-saw fully supports the
headline no-go on its own.) **Depth truncation at a fixed cut and
RH-sensitivity are mutually exclusive.**

## 4. What survives, and the Mellin-side echo of the budget theorem

* The blow-up `\tfrac12\log^2(1/(z-1))` at `z = 1` is exactly the Mellin
  shadow of the budget divergence `\sum_{67\le p\le Y}1/p \to \infty`
  (`T-105000`): an independent, purely analytic confirmation that the
  FIXED cut is what is fatal.
* Under the MOVING cut (`O-105010`) depth `\le 2` is exact, not a
  truncation: there is no discarded depth-`\ge 3` mass, no see-saw, and
  the analogue of the divergent `u` is the bounded `\log(1/\theta)` — the
  `z = 1` catastrophe is priced **down** (`L-105032`, corrected: the pole
  cancels exactly but a `\pm4\log` germ survives between the pieces; not
  priced out). The open object becomes a two-variable
  Dickman/Hildebrand–Tenenbaum transform; this refutation contributes its
  negative boundary: any frozen-cut approximation of it reinstates the
  `\log^2` wall.
* The reusable positive machinery (depth-split Dirichlet identity,
  prime-zeta branch calculus, the `m^2\ell^2/2` no-cancellation lemma at
  off-line zeros) is deposited as `L-105025`.

## 5. Falsifiers

A bounded limit of `F^{(\le2)}(s)` as `s \to 1/2^+` (contradicts the
measured and derived blow-up); a cancellation of the `\log^2` germ by
`S(z)` or the kernel (both are finite and nonzero at `z = 1`); an error in
the sieve/transform agreement (replay the lane scripts).
