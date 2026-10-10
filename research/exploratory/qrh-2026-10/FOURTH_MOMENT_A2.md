# The fourth-moment input has the shape of a cubic GL(3) metaplectic object

```text
Status: PROPOSED (structural identification) + EMPIRICAL exact-symbol checks of two identities
Scope: the fourth-moment target of PR 910 (eq. 3.5) for the sextic Moebius family of the OpenAI
  Oct 5 (11/12) architecture; no zero-free region and no RH claim
Exact sources or dependencies: OpenAI Oct 5 2026 manuscript (PR 908 import, paper2.tex Sections 2-3:
  Poisson step, mu(n)gamma_{-1}(n) = chi_n(-1) G(n)^{-1} conj(alpha(n)) gamma_2(n), cubic theta reflection);
  PR 910 FOURTH_MOMENT_REDUCTION.md (3.1)-(3.5) and UPSTREAM_HEIGHT_AND_MOMENTS.md Sec. 7;
  Brubaker-Bump-Friedberg, Weyl group multiple Dirichlet series (type A, incl. A2, n-th order Gauss
  sums; Whittaker coefficients of metaplectic Eisenstein series on covers of GL(r+1));
  Kazhdan-Patterson (theta on the n-fold cover of GL(3) has a unique Whittaker model for n = 3, 4)
What was actually run: a2/check_twisted_mult.py (362 coprime prime pairs, max dev 1.0e-14) and
  a2/check_nesting.py (1296 triples, max dev 5.3e-15); exact sextic symbols, floating Gauss sums
Smallest remaining gap: no reflection / functional-equation estimate for the twisted A2 partial sums
  is proved or even precisely formulated here; the identification is of coefficient shape only
```

## 1. Why the fourth moment matters

In the Oct 5 architecture, the 11/12 zero-free half-plane follows from the mean square

    Σ_{N u ≤ H} |A_u(D)|² ≪ D^{1+ε} H,   H = D^{1+θ},
    A_u(D) = Σ_n μ(n) ν(n) χ_n(u) W(N n / D),

together with prime extraction from the sixth-power rows `u = p⁶`. PR 910 (Prop. 7.2, which the
same PR's review found no error in) shows that diagonal-size `2k`-th moments would give
`1/2 + 5(1+θ)/(12k)`. That is **17/24** at `k = 2`, and the exponent tends to 1/2 as `k → ∞`.

This is the opposite of the Sep 30 architecture, whose barriers stall at 13/15
([THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md)). Here every new moment rung moves the boundary
toward the critical line.

PR 910 reduces the fourth moment to a squarefree balanced-divisor mean square (its (3.5)):

    Σ_{N u ≤ H} |B_u(X)|² ≪ D^ε H X²,
    B_u(X) = Σ_{r squarefree} μ(r) ν(r) χ_r(u) Σ_{d e = r} W(N d/X) W(N e/X).

## 2. Two identities (EMPIRICAL checks, exact symbols)

For coprime primary primes `d, e` and normalized Gauss sums `γ_j`:

* **Twisted multiplicativity.** `γ_j(de) = χ_d(e)^j χ_e(d)^j γ_j(d) γ_j(e)`. Since
  `χ_d(e)/χ_e(d) = ±1` (sextic reciprocity up to the finite sign bicharacter; observed exponents
  `{0, 3}` only), the cubic case collapses to

      γ₂(de) = γ₂(d) γ₂(e) · conj((e/d)₃).

* **Nesting.** Cubic reciprocity gives `conj((e/d)₃) = χ_e(d⁴)`, hence for every row `h`

      γ₂(de) χ_{de}(h) = [γ₂(d) χ_d(h)] · [γ₂(e) χ_e(h·d⁴)].

  The zero extension of `χ_e(d⁴)` enforces `(d, e) = 1` automatically.

Both were checked numerically (`a2/check_twisted_mult.py`, `a2/check_nesting.py`). Each is also an
immediate consequence of CRT and cubic reciprocity; the numerics confirm the manuscripts'
conventions (primary generators, `e(z) = exp(4πi Im z/√3)`, symbol orientation).

## 3. The dual of the fourth-moment target

Expanding (3.5) and applying Poisson summation in `u`, exactly as in the Oct 5 Step 3, produces
Gauss sums `γ_{-1}(r)`. The Oct 5 identity absorbs the Möbius factor:

    μ(r) γ_{-1}(r) ∝ conj(α(r)) γ₂(r)   (up to fixed ray-class phases).

For squarefree `r = de` with the balanced divisor weight, Section 2 turns the dual column sum into

    C_h(X) = Σ_{d,e} a(d) a(e) conj((e/d)₃) χ_d(h) χ_e(h) W(N d/X) W(N e/X)
           = Σ_d a(d) χ_d(h) W(N d/X) · B^{(2)}_{h·d⁴}(X),

with `a(n) = conj(α(n)) γ₂(n) × (fixed ray phases)`. Here `B^{(2)}_{h'}(X)` is precisely the Oct 5
**second-moment** dual column sum at the shifted row `h' = h·d⁴`. The ray phases (the sign
bicharacter `R(d, e)` of the quadratic refinement `G`) descend to a fixed ray class group and only
split the sum into finitely many classes. (Heuristic derivation; the exact masks and coprimality
bookkeeping of the source have not been redone here.)

**Equivalent GL(2) view.** For squarefree `r = de` with `(d, e) = 1`, the identity
`γ₂(de) = γ₂(d)γ₂(e)·conj((e/d)₃)` is exact. The dual column sum therefore equals

    C_h(X) = Σ_{r squarefree} conj(α(r)) γ₂(r) · W_X(r) · χ_r(h),
    W_X(r) = #{(d, e) : de = r, N d, N e ∈ (X, 2X]}   (smoothed),

up to ray phases. This is a *GL(2) cubic-theta coefficient sum* (Patterson's `γ₂`), weighted by a
balanced divisor function instead of a smooth function of `N r`. Mellin inversion in the two
factor sizes turns `W_X` into the double series `Σ_{d,e} γ₂(de) χ_{de}(h) N(d)^{-s₁} N(e)^{-s₂}`.
The "A2" and "theta × divisor function" descriptions are the same object, so two toolboxes are in
play:

* `GL(3)` metaplectic reflection (A2 functional equations);
* Rankin–Selberg / shifted-convolution methods for the cubic theta against Eisenstein series on
  the cubic cover of `GL(2)`.

This also explains PR 910's reduction (3.5): its balanced-divisor column weight is exactly `W_X`.

**Shape identification.** On coprime squarefree pairs, the coefficient `γ₂(d)γ₂(e)·(e/d)₃^{-1}` has
the twisted-multiplicative form of the coefficients `H(c₁, c₂)` of the **type-A2 Weyl group multiple
Dirichlet series with cubic Gauss sums** (Brubaker–Bump–Friedberg; Chinta–Gunnells for A2). Those
series are Whittaker coefficients of Eisenstein series on the cubic cover of `GL(3)`. The Oct 5
second moment is the `GL(2)` instance of the same pattern: `γ₂(n)` are Patterson's coefficients of
the cubic theta function on the cubic cover of `GL(2)`. The exact BBF normalization and orientation
of the interaction symbol still have to be matched.

| Moment | Dual coefficient | Automorphic object supplying a "reflection" |
|---|---|---|
| 2nd (proved in Oct 5, imported) | `γ₂(n)`, squarefree `n` | cubic theta on the 3-fold cover of GL(2) (Kubota–Patterson; Dunn–Radziwiłł expansions) |
| 4th (open; PR 910 (3.5)) | `γ₂(d)γ₂(e)(e/d)₃^{-1}`, balanced coprime squarefree `(d,e)` | A2 cubic Weyl group MDS = Whittaker coefficients of cubic GL(3) Eisenstein series; the residue/theta on the cubic cover of GL(3) has a unique Whittaker model (Kazhdan–Patterson, `n = 3`) |

## 4. Why a large sieve cannot close (3.5), and what the A2 structure would have to supply

Let `L = X²` be the column length of `B_u`. Poisson duality gives, schematically,

    Σ_u |B_u|² ≲ H L + (H/L) Σ_{h ≤ 𝓗} |C_h|²,   𝓗 ≍ L²/H.

The target `H L` requires `Σ_h |C_h|² ≲ L²`, i.e. `|C_h|² ≲ H` on average. For the second moment
the analogous requirement is met: there `𝓗 = D²/H < D`, and after theta reflection the quadratic
large sieve gives `(𝓗 + D)·D = D²`.

For the fourth moment `𝓗 = X⁴/H ≥ X²`. The required size `√H` is below the generic size `X` of a
sum of `X²` unimodular terms when `X > H^{1/2}`, which happens for `X` near `D`. An optimal large
sieve on the dual gives only `(𝓗 + X²)X² = X⁶/H`, missing by `X²/H = D^{1−θ}`.

So (3.5) needs **structural cancellation in the dual double sums**. Section 3 says exactly which
structure is available: the `GL(3)`-metaplectic one. The natural programme, mirroring the Oct 5
proof one rank higher:

1. *Completion.* Add the prime-power parts `H(p^{k₁}, p^{k₂})`, which are known for cubic A2
   through Gelfand–Tsetlin/crystal formulas. This is the analogue of the `n b³` cube completion
   (Dunn–Radziwiłł) used in the second moment.
2. *Reflection.* Use the `S₃` functional equations of the twisted A2 series (or the automorphy of
   the cubic `GL(3)` theta function) to shorten the balanced double sum. Check that after
   reflection the twist by `χ_{de}(h)` becomes a character family with an optimal (quadratic-type)
   large sieve, as `χ_h(m)³` was for `GL(2)`.
3. *Removal.* Undo the completion by Möbius inversion in the prime-power parts.

**Why `GL(2)` steps alone cannot do it (bookkeeping).** In the useful regime `H = D^h` with
`h < 2`, the dual rows satisfy `N h ≲ 𝓗 = X⁴/H > X²` (at `X ≍ D`). By the nesting identity, a
cubic-theta reflection in `d` with `e` fixed acts on a twist of conductor about `N(h)N(e)`. It maps
length `X` to about `(N(h)N(e))²/X ≫ X`, so it *lengthens*. The same holds for `e`.

`GL(2)` reflections shorten only when `𝓗 < X`, i.e. `H > X³`. There the leverage
`1/2 + 5h/24` exceeds 1 and is useless. Any proof of the useful rung therefore needs a genuinely
joint transformation, such as the long Weyl element of the A2 series acting on both variables at
once, or a non-reflection argument. Iterating the `GL(2)` theory will not do.

**Second-step analysis: the problem reproduces itself (heuristic derivation; local identities
verified).** Apply the Oct 5 reflection (Prop. `lem:reflection`, local transform
`eq:ray-local-transform`) to the `d`-sum in the nesting form, with row `g = h·e⁴`.

* Primes `p | h` have twist exponent `j = 1`. They give the quadratic factor
  `B_{p,1} = χ_p³`, as in the second moment.
* Primes `p | e` have `j = 4`. They give the Ramanujan-type factor
  `B_{p,4}(x) = N(p)^{-1/2}(−1 + N(p)·1_{p|x})` with local unit `ω_{p,4} = γ₄(p)`.

For dual indices `ℓ` coprime to `e`, the product over `p | e` is `μ(e) N(e)^{-1/2} ∏_{p|e} γ₄(p)`.
In our conventions (`a2/check_second_step.py`, 104 primes):

* `γ₂(p)³ = −α(p)`, deviation `7·10⁻¹⁵`;
* `γ₄(p) = conj(γ₂(p))`, deviation `2·10⁻¹⁵`.

The column coefficient's Gauss sum `γ₂(p)` is therefore cancelled exactly by `ω_{p,4}`. The
remaining `e`-sum is a **Möbius sum** twisted by `conj(α(e)) χ_e(h)`, with the residual cubic pair
phases of `γ₂(e)` (the twisted-multiplicativity cocycle) and weight `N(e)^{-1/2}`. That is an
inverse-`L` type sum of the same kind as the original `A_u`, now with an angular twist.

So one `GL(2)` reflection returns the fourth-moment dual to the original difficulty, a
Möbius sum against characters. The Möbius absorption `μγ_{-1} ∝ conj(α)γ₂` that powers the
second moment does not recur at the second step. This is a structural reason why iterated `GL(2)`
reflection cannot close the fourth moment, beyond the length bookkeeping above.

*Caveat.* The fixed-ray phases (`χ_p(σ_p)^{-2}`, the additive characters `ψ`) and the treatment of
the pair phases under CRT in the reflection were not tracked. The claim concerns the generic local
structure only.

**First concrete obstacle.** In the `GL(2)` case the row twist became quadratic after reflection
(`χ_p^{-1}χ_p^{-2} = χ_p^{3}`), which is why Goldmakher–Louvel's quadratic large sieve applied.
Whether the `GL(3)` reflection produces a quadratic or a cubic/sextic twist is the decisive local
computation. With a cubic twist, only the weaker Blomer–Goldmakher–Louvel large sieve (extra
`(ML)^{2/3}` term) is available.

## 5. Next steps (bounded)

* Match BBF's A2 cubic coefficient formula (normalization, orientation, the `H(p,p)` term) to
  `C_h(X)` and record the exact dictionary. This is a literature and algebra task, checkable
  numerically with `a2/eis.py`.
* Compute the local twist produced by the A2 functional equation at a prime `p | h`. This is the
  analogue of `χ_p^{-1}χ_p^{-2} = χ_p^3`.
* Numerically compare `Σ_h |C_h(X)|²` with `X⁴` at small `X`. See [moments/](moments/) for the
  direct fourth-moment numerics. A finite trend is not a theorem.

## 6. Dual off-diagonal reconnaissance (EMPIRICAL, tiny scale)

**Correction to Section 4.** Exact duality subtracts the *dual diagonal*. The off-diagonal of the
original moment is

    (H/L) · (S_true − S_diag),   S_true = Σ_{N h ≤ 𝓗} |C_h|²,   S_diag = Σ_h Σ_r |c(r)|² 1_{(r,h)=1}.

So generic dual behaviour (`S_true ≈ S_diag`) is exactly what a diagonal-sized fourth moment
needs. The target is `ρ := (S_true − S_diag)/L² = O(1)`. The schematic Section 4 upper bound keeps
`S_diag`, which is why a large sieve alone cannot reach it. What a proof needs is an *asymptotic*
for the dual mean square with error `O(L²)`, i.e. control of the dual off-diagonal.

Setup of `a2/dual_offdiag.py` (results in `a2/results/dual_offdiag.jsonl`):
* columns `r = de` balanced in `(X, 2X]²`;
* exact sextic symbols;
* ray phases and the paper's unit/lattice conventions are ignored;
* rows are all elements with `N h ≤ 𝓗`.

| X | rows `N h ≤ 𝓗` | L | `S_true/S_diag` | ρ |
|---|---|---|---|---|
| 30 | 200 / 1000 / 3000 | 21 | 0.959 / 0.983 / 0.997 | −5.0 / −10.3 / −4.7 |
| 60 | 500 / 3000 / 12000 | 151 | 0.976 / 1.017 / 1.004 | −1.0 / +4.4 / +4.5 |

At these tiny scales the A2-structured dual mean square equals its diagonal within 4%. At `X = 60`,
ρ stays at about 4.5 as the row range grows fourfold. This is *consistent with*, and not evidence
for, a diagonal-sized fourth moment. Proving it would require exactly the dual off-diagonal control
that the A2 reflection is proposed to supply.
