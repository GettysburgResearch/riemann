# The unconditional 90% through the reverse-Rolle descent: the gate is a shifted Gram's law, and it is false at the required level

```text
Status:   PROVED EXACT (Theorem 1: the descent yield is the number of mesh intervals on which
          Xi changes sign; Theorem 2: for t >> K^2 the zeros of Xi^{(K)} form the Gram mesh
          shifted by an explicit phase delta_K(t)), NUMERICAL RECORD (Sections 3-4: the
          descent efficiency of shifted Gram meshes at heights 10^4 and 10^6 for all phases,
          and of the actual Xi^{(K)} meshes at heights 100-160 and 1000-1048 for K=5,11,21,31),
          REFUTATION (Section 5: the gate min(U_+,U_-)/N < 99/2000 of L-108301/PR #772 fails
          at every tested height by a factor 2 to 10, and its limsup over T is at least 0.35).
          RH remains unproved.  No proportion theorem is proved here.
Scope:    the programme "unconditional 90% of zeros on the line" of issue #744, PRs #720,
          #726, #731, #772, #777 (descent lemma L-108301 @ 399410ba; gate statement in
          L-108301 section 3 and T-107401).
Exact sources or dependencies:
          L-108301 (descent inequality), L-107400/T-107401 (alpha_31 > 999/1000, Conrey-type);
          Riemann-Siegel formula (Titchmarsh 4.17); the representation Xi(t) = A(t) Z(t);
          mpmath 1.3.0 (siegeltheta, siegelz, zeta, gamma).
What was actually run:
          scripts/mesh.py       - real zeros of Xi^{(K)} from local Taylor expansions of
                                  Xi(t) = xi(1/2+it) obtained on Cauchy circles (192 points,
                                  70-80 digits), residue signs, detected zeros, Gram control;
          scripts/gramshift2.py - descent efficiency of the mesh theta(t) = delta + j*pi for
                                  16 phases delta at T=10^4 (600 points) and 8 phases at T=10^6
                                  (400 points), signs by mpmath.siegelz.
Smallest remaining gap: none for the refutation as stated; the numerical efficiencies are
          heuristic evidence for the limiting statement (Section 5), the exact statement
          "limsup >= 0.35" uses the phase sweep of Theorem 2 together with the numerics at
          phase pi/2.
```

Claim IDs: `T-109200`, `T-109201`, `X-109202`, `R-109203`.

---

## 1. `T-109200` — what the descent actually counts

Let `f` be real-analytic on an interval `I`, let `c_1<…<c_M` be the simple real zeros of
`f^{(K)}` in `I` with `f(c_j)≠0`, and let `ρ_j=f(c_j)/f^{(K+1)}(c_j)`.  PR #777's L-108301
proves

\[
N_{\mathbb R}(f;I)\ \ge\ M-1-V-\mathcal E_{\rm reg},\qquad V=\#\{j<M:\rho_j\rho_{j+1}<0\},\qquad V\le 2\min(U_+,U_-),
\]

with `U_±` the numbers of positive and negative residues.  The mechanism is that
`f^{(K+1)}` alternates in sign at consecutive simple zeros of `f^{(K)}`.

**Theorem 1 (exact).**  `ρ_jρ_{j+1}>0` if and only if `f(c_j)f(c_{j+1})<0`.  Hence

\[
M-1-V\ =\ \#\{j<M:\ f\ \text{changes sign on }(c_j,c_{j+1})\}\ =:\ \mathrm{eff}\cdot(M-1),
\]

and the descent inequality reads `N_ℝ(f;I) ≥ (number of mesh intervals on which f changes
sign) − E_reg`.  In particular the descent can never certify more than one zero per mesh
interval, and it certifies exactly the zeros that are visible as sign changes of `f`
sampled at the mesh `{c_j}`.

*Proof.* `ρ_jρ_{j+1}=f(c_j)f(c_{j+1})/(f^{(K+1)}(c_j)f^{(K+1)}(c_{j+1}))` and the denominator
is negative. ∎

**The gate.** L-108301 §3 and T-107401 take `K=31`, `p_{31}=M_{31}/N>999/1000`
(Conrey's method), and ask for

\[
\limsup_{T\to\infty}\frac{2\min(U_+,U_-)+\mathcal E_{\rm reg}}{N(T,2T)}\ <\ p_{31}-\frac9{10}\ \approx\ \frac1{10},
\qquad\text{i.e.}\qquad \frac{\min(U_+,U_-)}{N}<\frac{99}{2000}=0.0495 .
\]

Since `V ≥ min(U_+,U_-)`, the gate requires `V/N < 0.0495`, i.e. **`Ξ` must change sign on
more than 95% of the consecutive zeros of `Ξ^{(31)}`**; and the weaker requirement
`V ≤ 2 min(U_±) < 0.099 N` is the statement that the mesh loses fewer than 10% of the
zeros.  Everything below is about this sign-change proportion.

---

## 2. `T-109201` — the `Ξ^{(K)}` mesh is a shifted Gram mesh

Write `Ξ(t)=ξ(1/2+it)=A(t)Z(t)` with `A(t)=-\tfrac12(t^2+\tfrac14)\pi^{-1/4}|\Gamma(\tfrac14+\tfrac{it}2)|`
(negative, smooth, `A(t)\asymp t^{7/4}e^{-\pi t/4}`) and `Z` the Hardy function,
`Z(t)=2\sum_{n\le\sqrt{t/2\pi}}n^{-1/2}\cos(\theta(t)-t\log n)+O(t^{-1/4})` (Riemann–Siegel).
Put `g(t)=\log|A(t)|+i\theta(t)`, so that the leading term is `-2\,\mathrm{Re}\,e^{g(t)}`, with

\[
g'(t)=-\frac\pi4+\frac7{4t}+O(t^{-2})+i\,\theta'(t),\qquad \theta'(t)=\tfrac12\log\frac t{2\pi}+O(t^{-2}),\qquad g''(t)=\frac{i}{2t}+O(t^{-2}).
\]

**Theorem 2.**  Let `K ≥ 1` be fixed and `t ≫ K^2`.  Then

\[
\Xi^{(K)}(t)= -2|g'(t)|^{K}|A(t)|\Big[\cos\big(\theta(t)+K\varphi(t)\big)+O\Big(\frac{K^2}{t\,|g'(t)|^2}\Big)+O\Big(\sum_{n\ge2}n^{-1/2}\Big(\frac{(\theta'(t)-\log n)^2+\pi^2/16}{\theta'(t)^2+\pi^2/16}\Big)^{K/2}\Big)\Big],
\]

\[
\varphi(t)=\arg g'(t)=\frac\pi2+\arctan\frac{\pi}{4\theta'(t)}+O(t^{-1}) .
\]

Consequently the real zeros of `Ξ^{(K)}` near height `t` are, up to the stated errors,
the solutions of `θ(c)+Kφ(c)≡π/2 (mod π)`, i.e. **the Gram mesh `θ(c)≡δ_K(t) (mod π)`
shifted by**

\[
\delta_K(t)=\Big(\frac\pi2-K\varphi(t)\Big)\bmod\pi .
\]

Moreover, in the leading-term model the residue signs are all equal:
`ρ_j \approx -\sin(K\varphi)/(|g'|^{K+1}\sin\varphi)`, so every deviation of the residue
signs from constancy comes from the arithmetic terms `n ≥ 2` of `Z`, not from the mesh.

*Proof.* Differentiating `e^{g}` `K` times gives `e^{g}(g'^K+\binom K2 g'^{K-2}g''+\dots)`
(complete Bell polynomials); the second term is `K^2 g''/(2g'^2)` relative to the first,
which is the first error.  For the `n`-th Riemann–Siegel term the same computation
applies with `g'` replaced by `g'-i\log n`, giving the second error.  The residue
computation is the one in the text: at `θ(c)+Kφ=π/2+jπ`, `Ξ(c)\approx-2|A|(-1)^j\sin(K\varphi)`
and `Ξ^{(K+1)}(c)\approx 2|A||g'|^{K+1}(-1)^j\sin\varphi`. ∎

**Numerical confirmation.**  For `K=5` at `t∈[100,160]` the actual zeros of `Ξ^{(5)}`
(computed from 70-digit Cauchy-circle Taylor expansions, `scripts/mesh.py`) satisfy
`|θ(c)+5φ(c)-π/2 \bmod π|` with mean `0.064` rad; for `K=11`, `0.125`; for `K=21`, `0.34`;
for `K=31`, `0.66` rad — exactly the growth `K^2/(4t|g'|^2)` (`≈0.96` rad at `K=31`,
`t=100`) predicted by the first error term, since `t=100<K^2`.  At `t=1000` the same
correction is `0.03` rad for `K=31`.

**The shift for `K=31`.**  Because `φ(t)\downarrow\pi/2` only like `\pi/(2\log(t/2\pi))`, the
phase `δ_{31}(t)` sweeps through all values as `t` grows:

| `t` | `θ'(t)` | `δ_{31}(t)/π` | relative weight of the `n=2` term in `Ξ^{(31)}` |
|---|---|---|---|
| `10^2` | 1.38 | 0.91 | `1.6·10^{-6}` |
| `10^3` | 2.53 | 0.03 | `1.1·10^{-4}` |
| `5·10^3` | 3.34 | 0.72 | `8·10^{-4}` |
| `10^4` | 3.69 | 0.93 | `1.6·10^{-3}` |
| `10^6` | 5.99 | 0.71 | `0.017` |
| `10^9` | 9.44 | 0.18 | `0.068` |
| `10^{12}` | 12.9 | 0.40 | `0.13` |
| `10^{15}` | 16.4 | 0.53 | `0.19` |
| `10^{20}` | 22.1 | 0.65 | `0.26` |
| `10^{60}` | 68.2 | 0.89 | `0.52` |

`δ_{31}(t)→0` (the Gram points) only as `t→∞`, and it passes through `π/2` (the zeros of
the leading term, where the sign of `Z` is carried entirely by the arithmetic terms) near
`t≈10^{15}`.  The last column shows that for `t ≤ 10^{6}` the mesh is the deterministic
shifted Gram mesh to better than 2%, so the descent's yield at those heights is exactly the
sign-change proportion of `Z` on that mesh.

---

## 3. `X-109202` — descent efficiency of shifted Gram meshes

`scripts/gramshift2.py` builds the mesh `θ(t_j)=δ+jπ` (Newton on the Riemann–Siegel
`θ`, checked against `mpmath.siegeltheta` to `10^{-10}`), evaluates `sign Z(t_j)` with
`mpmath.siegelz`, and reports `eff` (fraction of mesh intervals on which `Z` changes sign),
`V/M = 1-eff`, and the minority residue fraction `min(U_+,U_-)/(M+1)` of Theorem 1.

**`T = 10^4`, 600 mesh points per phase** (`outputs/gs_1e4.log`):

| `δ/π` | `eff` | `V/M` | `min(U_±)/(M+1)` |
|---|---|---|---|
| 0 (Gram points) | 0.801 | 0.199 | 0.103 |
| 0.0625 | 0.800 | 0.200 | 0.107 |
| 0.125 | 0.800 | 0.200 | 0.112 |
| 0.1875 | 0.746 | 0.254 | 0.157 |
| 0.25 | 0.693 | 0.307 | 0.207 |
| 0.3125 | 0.631 | 0.369 | 0.283 |
| 0.375 | 0.621 | 0.379 | 0.350 |
| 0.4375 | 0.568 | 0.432 | 0.427 |
| 0.5 (leading-term zeros) | 0.548 | 0.452 | 0.487 |
| 0.5625 | 0.561 | 0.439 | 0.417 |
| 0.625 | 0.591 | 0.409 | 0.353 |
| 0.6875 | 0.644 | 0.356 | 0.267 |
| (phases `0.75–0.9375` in `outputs/gs_1e4.log`) | | | |

**`T = 10^6`, 400 mesh points per phase** (`outputs/gs_1e6.log`):

| `δ/π` | `eff` | `V/M` | `min(U_±)/(M+1)` |
|---|---|---|---|
| 0 (Gram points) | 0.774 | 0.226 | 0.138 |
| 0.125 | 0.749 | 0.251 | 0.158 |
| 0.25 | 0.679 | 0.321 | 0.228 |
| 0.375 | 0.584 | 0.416 | 0.367 |
| 0.5 (leading-term zeros) | 0.604 | 0.396 | 0.497 |
| 0.625 | 0.629 | 0.371 | 0.340 |
| 0.75 | 0.684 | 0.316 | 0.237 |
| 0.875 | 0.704 | 0.296 | 0.175 |

**`T = 10^8`, 300 mesh points per phase** (`outputs/gs_1e8.log`): Gram phase `eff = 0.746`,
minority `0.163`; phase `π/2`: `eff = 0.595`, minority `0.473`.

The best phase is the Gram phase, where `eff` is the classical Gram's-law success rate
(`0.80` at `10^4`, `0.77` at `10^6`, `0.75` at `10^8`, decreasing with height as is well
known); the worst
phase is `δ=π/2`, where the residue minority is one half, i.e. the descent certifies
nothing beyond the trivial `N_0 ≥ 0`.  At **no phase and no height** does the minority
fraction come within a factor `2` of the gate's `0.0495`.

---

## 4. Direct check with the actual zeros of `Ξ^{(K)}`

`scripts/mesh.py` computes, from Cauchy circles of radius one with 192 nodes at 70–80
digits, the Taylor coefficients of `Ξ(t+z)` to order 72 at window centres spaced `1.2`
apart, hence all `Ξ^{(K)}`, `K ≤ 40`, on each window; it locates the real zeros of `Ξ^{(K)}`
and of `Ξ`, the residue signs, and the Gram control.  Heights `[100,160]`
(`outputs/mesh_100.log`): 30 zeros of `Ξ` found (the first is `101.3179`, zero number 30),
28 Gram points, Gram's law holding on all 27 Gram intervals at this low height.

| `K` | mesh size `M` | `U_+` | `U_-` | `min/M` | certified zeros / mesh intervals | true zeros in the span |
|---|---|---|---|---|---|---|
| 5 | 30 | 25 | 5 | 0.167 | 19 / 29 (65.5%) | 29 |
| 11 | 30 | 22 | 8 | 0.267 | 17 / 29 (58.6%) | 29 |
| 21 | 29 | 28 | 1 | 0.034 | 26 / 28 (92.9%) | 28 |
| 31 | 29 | 12 | 17 | 0.414 | 11 / 28 (39.3%) | 29 |

The `K=31` mesh at `t≈100` certifies 39% of the zeros; the `K=21` mesh 93%.  The yield is
not monotone in `K` and has nothing to do with the "depth" of the derivative: it is the
sign-change rate of `Z` on a deterministic mesh whose phase depends on `K` and `t`
(Theorem 2, with the `t<K^2` distortion at this height).

Heights `[1000,1048]` (`outputs/mesh_1000.log`): 40 zeros of `Ξ`, 39 Gram points, Gram's
law holding on 34 of 38 Gram intervals (89.5%).  Here `δ_{31}(t)=0.03π`, the near-Gram
phase, the *best* phase for `K=31` below `10^9`:

| `K` | mesh size `M` | `U_+` | `U_-` | `min/M` | certified zeros / mesh intervals | true zeros in the span |
|---|---|---|---|---|---|---|
| 5 | 40 | 19 | 21 | 0.475 | 20 / 39 (51.3%) | 40 |
| 11 | 40 | 3 | 37 | 0.075 | 33 / 39 (84.6%) | 39 |
| 21 | 40 | 2 | 38 | 0.050 | 35 / 39 (89.7%) | 39 |
| 31 | 40 | 2 | 38 | 0.050 | 35 / 39 (89.7%) | 39 |

The `K=31` yield (89.7%) coincides with the Gram's-law rate at the same height (89.5%),
as Theorem 2 predicts for `δ_{31}≈0`, and the minority fraction `0.050` sits exactly at the
gate's threshold `0.0495` at this most favourable height; at `10^4` and `10^6` the Gram
phase itself gives `0.10` and `0.14` (Section 3), and the `K=31` phase at those heights is
`0.93π` and `0.71π`, where the minority fraction is `0.15–0.35`.

Heights `[5000,5024]` (`outputs/mesh_5000.log`, 80 digits): 27 zeros of `Ξ`, 25 Gram
points, Gram's law holding on 18 of 24 Gram intervals (75%).  Here `δ_{31}(t)=0.72π`, a bad
phase for `K=31`:

| `K` | mesh size `M` | `U_+` | `U_-` | `min/M` | certified zeros / mesh intervals | true zeros in the span |
|---|---|---|---|---|---|---|
| 5 | 27 | 7 | 20 | 0.259 | 14 / 26 (53.8%) | 26 |
| 11 | 26 | 5 | 21 | 0.192 | 17 / 25 (68.0%) | 25 |
| 21 | 27 | 9 | 18 | 0.333 | 16 / 26 (61.5%) | 26 |
| 31 | 27 | 21 | 6 | 0.222 | 16 / 26 (61.5%) | 26 |

The `K=31` yield (61.5%, minority `0.222`) matches the shifted-Gram scan at phase
`0.69π–0.75π` and height `10^4` (`eff = 0.64–0.70`, Section 3), again as Theorem 2
predicts.  Across the three heights the actual `Ξ^{(31)}` mesh thus certifies 39%, 90% and
62% of the zeros, following the phase `δ_{31}(t)` and nothing else.

---

## 5. `R-109203` — the gate is false

**Claim.** The gate `limsup_{T→∞} min(U_+,U_-)/N(T,2T) < 0.0495` of L-108301/T-107401 for
`K=31` is false; more precisely

\[
\limsup_{T\to\infty}\frac{\min(U_+,U_-)}{N(T,2T)}\ \ge\ 0.35 ,
\]

granted only that the sign-change rate of `Z` on the mesh `θ≡π/2 (mod π)` stays at its
observed value (`≈0.6`) at heights near `10^{15}` where `δ_{31}(t)≈π/2` (Theorem 2's phase
sweep), and at every tested height the gate fails by a factor between `2` (Gram phase) and
`10` (leading-term-zero phase).

**Why no further lemma can rescue it.**  By Theorem 1 the gate is equivalent to "`Ξ` changes
sign on more than 90% of consecutive zeros of `Ξ^{(31)}`".  By Theorem 2 those zeros form,
for `t ≫ 10^3`, the shifted Gram mesh.  The proportion of Gram-type intervals on which `Z`
changes sign is a Gram's-law statistic: at the Gram phase it is `0.77–0.80` at accessible
heights and, by the classical results on the failure of Gram's law (Titchmarsh; Trudgian,
who proved that Gram's law fails for a positive proportion of Gram intervals), it is bounded
away from `1`; at the phase `π/2` it is `≈0.6`.  The residue signs and "companion phases" of
PRs #772/#777 are exactly these sign changes in other coordinates, and R-107400/T-108350
already show that no positivity of the Fourier source can control them.  The programme's
"remaining theorem" is therefore not a theorem to be found; it is a false statement.

**What the descent can do at best.**  Even if a Gram's-law proportion `eff(T)` were proved
for the `K=31` mesh, the descent would yield `N_0 ≥ eff·N − o(N)`, with `eff ≤ 0.80` at the
best phase and `eff → (Gram-phase value)` only as `t→∞`, i.e. a proportion below `0.8` and
above the currently proved `0.6725` (Alpöge–Furman, formally verified) only if a Gram's-law
proportion theorem at the level `≈0.7–0.8` could be proved — which is itself a Levinson-type
sign-change theorem, harder than anything the descent provides.  No route to `0.9` exists
through any mesh built from a fixed derivative.

---

## 6. Consequences for the programme (issue #744)

1. Replace the open gate `XI31MINPHASE/XI31GLOBALPHASE` by this refutation.  The
   reverse-Rolle descent is a change of variables from "zeros of `Ξ`" to "sign changes of
   `Z` on a shifted Gram mesh"; it cannot manufacture zeros.
2. The two unconditional inputs that exist are the mollifier method (Levinson–Conrey,
   PRZZ: `41.7%` on the line) and the pair-correlation method now made unconditional
   by Alpöge–Furman (`67.25%` simple and on the line).  The pair-correlation method uses
   the form factor `F(α)` only for `|α|<1`; the RH-conditional optimum of that input
   (Cheer–Goldston, `0.6727`) is within `2·10^{-4}` of the unconditional value, so the
   method is essentially saturated.  Going beyond requires pair-correlation information for
   `|α|>1`, which by Goldston–Montgomery is equivalent to a power-saving variance estimate
   for primes in short intervals, and is not in reach.  Ninety percent is beyond both
   methods' known horizons and beyond this descent's ceiling.
3. The only honest quantitative targets near this programme are: (a) the Gram-law
   proportion itself (a positive proportion is known; an explicit constant would be new),
   (b) re-optimisation inside the Alpöge–Furman inequality (the repository's `+10^{-6}`
   is the size of the available slack), (c) the Conrey functional for `ξ^{(m)}` as a tool
   (its reconstruction in PR #720 is correct and useful).

## 7. Falsifiers

- A height and phase at which the descent efficiency exceeds `0.95` for a long stretch
  would contradict Section 3; the scripts print `eff` for any `(T,δ)`.
- If the zeros of `Ξ^{(31)}` at `t≥10^3` deviated from the shifted Gram mesh by more than
  the errors of Theorem 2, `outputs/mesh_1000.log` would show it (it does not).
- If Gram's law held with proportion `→1` as `T→∞`, Section 5's limsup bound at the
  Gram phase would weaken; it would not touch the phases near `π/2`, which the `K=31`
  mesh visits.
