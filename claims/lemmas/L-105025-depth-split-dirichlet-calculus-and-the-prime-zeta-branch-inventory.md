# L-105025 — Depth-split Dirichlet/Mellin calculus: the S·(−1)^k e_k factorization, prime-zeta continuation, branch inventory, and the m²ℓ²/2 no-cancellation lemma

Claim ID: `L-105025`
Status: **PROVED (elementary identities + standard continuation; every display numerically verified, replay `X-105020/lane_primezeta/`)**
Created: 2026-08-21
Agent: claude (external reviewer lane)
Used by: `R-105024`; offered to the moving-cut/Type-II lane
(`O-105010`; `research/gpt56-sol/102000-parabolic-bessel-vaughan-correction`).
RH status: not assumed, not addressed

## 1. Depth-split Dirichlet identity

Cut at 67; `S(z) = \prod_{p\le61}(1-p^{-z})` (entire; zeros only on
`\Re z = 0`); `P_{67}(z) = \sum_{p\ge67}p^{-z}`; `e_k` = elementary
symmetric functions of `\{p^{-z}\}_{p\ge67}`: `e_0 = 1`, `e_1 = P_{67}`,
`e_2 = (P_{67}(z)^2 - P_{67}(2z))/2`. For `\Re z > 1`:

```
D_k(z) := sum over squarefree n with exactly k prime factors >= 67
          of mu(n) n^{-z}   =   S(z) * (-1)^k e_k(z).
```

*Proof*: unique factorization `n = mr` + absolute convergence + Newton.
Verified by sieve to `10^7` at `z = 1.5, 1.25, 2.5` for `k = 0,1,2`, with
non-circular tail correction (predicted missing mass `-3.8258994931\cdot
10^{-6}` at `z=1.5`, `k=1`, matches the sieve gap to all shown digits) and
independent pair-enumeration cross-check (606,679 rough pairs; diffs
`\le 3.1\cdot10^{-13}`).

## 2. Transforms

With `M[T](s) = (s+3/2)/(s(s-1/2))` (`\Re s > 1/2`): for the depth-`k`
witness, `\int_1^\infty \Psi_k(x)x^{-s-1}dx = M[T](s)\,S(z)(-1)^k e_k(z)`,
`z = s+1/2`; the depth-`\le2` Harnack transform is `R-105024 §2.1`'s
closed form. Consistency: `1/\zeta(z) = S(z)\sum_{k\ge0}(-1)^k e_k(z)`.

## 3. Continuation and branch inventory

Via Glaisher–Fröberg `P(z) = \sum_{j\ge1}\frac{\mu(j)}{j}\log\zeta(jz)`,
`P_{67}` (hence `e_1, e_2`) continues, unconditionally, to
`\{\Re z > 1/2\}` minus the singular set `\{1\} \cup \{\rho:
\zeta(\rho)=0,\ \Re\rho > 1/2\}` (multivalued around each point); `\Re z
= 0` is a natural boundary (Landau–Walfisz). Germ table (`\ell_a :=
\log(z-a)`; signs verified numerically):

```
point   germ of P67          germ of e_2                    germ of B_2 = 1 - e_1 + e_2
z=1     -l_1                 +(1/2)l^2 - A l                +(1/2)l^2 + (1-A)l      -> +inf
z=rho   +m l_rho             +(m^2/2)l^2 + mB l             +(m^2/2)l^2 + m(B-1)l   branch pt
z=1/2   +(1/2)l_{1/2}        +(1/8)l^2 + ((E+1)/2)l         +(1/8)l^2 + (E/2)l      -> +inf
z=rho/2 -(m/2)l_{rho/2}      +(m^2/8)l^2 - (m/2)(C+1)l      +(m^2/8)l^2 - (mC/2)l   branch pt
```

(`A,B,E,C` analytic at the respective points; at `z=1`,
`A = a_{67} = \lim[P_{67}(z) + \log(z-1)] = -2.029575488762\ldots`;
residual of the full quadratic germ at `z=1` tends to
`1 - a_{67} + a_{67}^2/2 - P_{67}(2)/2 = 5.08768\ldots` — measured
`5.156 \to 5.090 \to 5.0877` at `z-1 = 10^{-2}, 10^{-4}, 10^{-6}`.)

## 4. No-cancellation lemma (the detector survives truncation — off the real axis)

At a hypothetical off-line zero `\rho` (`\Re\rho > 1/2`, multiplicity
`m`): only the `k = 2` layer produces `\ell^2`, with coefficient
`m^2/2 \ne 0`, which the `k \le 1` layers (constant and linear in `\ell`)
cannot cancel; `|B_2| \to \infty` along `z \to \rho`, and the monodromy
changes the germ by `2\pi i\,m^2\ell + \text{const} \ne 0`. The prefactors
cannot rescue: `S(z)` and `(1-67^{-z})` vanish only on `\Re z = 0`; the
kernel is finite and nonzero at `s = \rho - 1/2` (`\rho` non-real since
`\zeta < 0` on real `(1/2,1)`, `L-99272 §2` @
`review/gpt56-pro/99700-owner-degeneracy-cross-core`). So every off-line zero
leaves a genuine `\log^2` branch point of the truncated transform at
`s = \rho - 1/2`. (That this detector is *unreachable* behind the
truncation's own real singularity at `s = 1/2` is exactly `R-105024`.)

## 5. Real-axis inventory

The only real singularity of the truncated transform in `\Re s > 0` is
`s = 1/2`; every real point of `(0, 1/2)` is regular (`\zeta \ne 0` on
real `(1/2,1)`, and complex zeros have `|\Im| \ge 14.13`).

## 6. Novelty and reuse

Prime-zeta branch calculus as a consumer object is new to the repository
(repo-wide grep: the only prime-series continuation in claims is the
log-derivative pole-type `L-90004` family — a different object with
pole-type continuation, used as a source). Reuse targets: the moving-cut
Type-II object's Dirichlet series is `S_{Y^\theta}(z)\cdot e_2`-with-
moving-alphabet; its off-line singular germ is this lemma's `m^2\ell^2/2`
term — the quantity any Type-II energy bound must ultimately feel.
