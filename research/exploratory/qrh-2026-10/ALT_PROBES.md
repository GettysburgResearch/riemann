# Alternative metaplectic probes: what boundary could each reach?

```text
Status: PROPOSED / HEURISTIC. Each table row carries its own label. No theorem here, and no RH claim.
Scope: exponent bookkeeping for QRH-type probes (theta coefficients x residue-symbol average ->
  Poisson -> principal row containing 1/L), with the [OAI] Sections 6-7 architecture held fixed:
  low side >= Z^{lx/2}, dual length h <= 1. Field F must contain mu_N; abelian F transfers to
  Dirichlet L-functions as in [OAI] Section 11.2.
Exact sources or dependencies:
  [OAI]  OpenAI, "The Quasi-Riemann Hypothesis ... Re s > 7/8", 30 Sep 2026 (sha256 in
         scripts/SOURCES.txt): Prop. 2.1, eq. (6.1), (7.1), (7.3)-(7.5), Lemma 7.1 and table (7.16).
  [W5]   origin/claude/openai-math-riemann-analysis-w5copg:
         standalone/2026-10-07-openai-quasi-rh/README.md, sections 2, 3, 6 item 7, 6a, 7.
  [CFH]  Chinta-Friedberg-Hoffstein, "Double Dirichlet series and theta functions" (2011),
         chinta.ccny.cuny.edu/publ/patterson.pdf: Hecke relations (2.5), Patterson's n=4
         conjecture, Conj. 2.1 (n=6), Davenport-Hasse forms (3.7)-(3.8).
  [DDHL] David-Dunn-Hamieh-Lin, arXiv:2306.11875, sections 1.2 and 4.5: Suzuki's quartic results,
         status of the Eckhardt-Patterson conjecture, count of undetermined coefficients.
  [DR]   Dunn-Radziwill, Ann. of Math. 200 (2024), arXiv:2109.07463: cubic large sieve sharp under GRH.
  [DdDS] David-de Faveri-Dunn-Stucky, arXiv:2410.03048.
  [BBFH] Brubaker-Bump-Friedberg-Hoffstein, Springer Proc. Math. 9 (2012) 83-95.
  [KP]   Kazhdan-Patterson, Publ. IHES 59 (1984); uniqueness for r = n, n-1 cited second-hand.
What was actually run: read [OAI] Sections 2, 6, 7; [W5]; [CFH] Sections 1-3; summary-level reads
  of [DDHL], [DR], [DdDS], [BBFH]. Exact-rational enumeration in Appendix A. No Gauss sums computed
  here; the sign facts are taken from [W5] section 7, which replays them numerically.
Smallest remaining gap: no known automorphic object has explicit prime coefficients whose
  Gauss-sum angle allows an averaging symbol of order N <= 4 AND has a reflection that reduces
  the low side to the quadratic large sieve. The concrete sub-gap nearest to this is the sign of
  the quartic theta coefficient tau_4(p) (Eckhardt-Patterson). Separately, the floor itself
  requires h > 1 to beat ([W5] section 6a).
```

RH remains unproved. The 7/8 and 11/12 statements below are claims from an unreviewed external manuscript.

## 1. Where the 6 and the 5/6 come from in [OAI]

**The probe.** Eq. (6.1) averages a twisted cubic-theta row
`T_{m,s,η}(t) = Σ γ2(c) α(cn³) η(cn³) χ_{cn³}(m) … q_c^{-1/2-t} q_n^{-1-3t}` over an element `m` (scale `X q_s`). The weight is a *sextic* Gauss sum `g_{χ_s}(s,−m)`, with `s` at scale `Y`. Here `χ` is the sextic residue symbol and `χ_p(x)² = (x/p)_3`. So `γ2(c)` is the normalized cubic Gauss sum, i.e. Patterson's coefficient. `γ1` is the sextic Gauss sum and `γ3` the quadratic one.

**Why the frequencies are `u a⁶`.** Poisson in `m` modulo `s b* A` gives `F(s,A,H)` (7.1). `F` sees `H` only through valuations, the sextic unit symbols `χ_p(h_p)` (7.9), and the twist `A ↦ χ_A(H)`, all invariant under `H ↦ H a⁶`. So `H = u a⁶` with `u` sixth-power-free, and the `a`-sum produces `V = Q^{-6z}`, i.e. `ζ_F^S(6z)` (Lemma 7.1, eq. (7.13)). **The 6 is the order of the averaging symbol `χ_A(m)`**, which is the character that pairs with the theta coefficient in the Poisson dual.

**Why that order must be 6 (the Möbius absorption).** In row u = 1, the coefficient of `q_c^{-x}` at `c = p` is the theta coefficient `γ2(p)` times the Poisson Gauss sum `G1 = Q^{1/2}γ1(p)`. [OAI] rewrites `γ2 = μ α G/γ1`; the paper's eq. (4.7) is the identity

`γ1(p) γ2(p) = −α(p) χ_p(4) γ3(p)`.

This identity is Davenport–Hasse duplication, `g(χ)g(χ⁴) = χ̄(4)g(χ²)g(χ³)`, combined with the cubic Stickelberger evaluation `γ2(p)³ = −α(p)` ([W5] section 2 step 3 and section 7, numerically replayed there). The ray-class factor `G` absorbs `χ(4)γ3`, which is explicit by Gauss's sign theorem plus quadratic reciprocity. The residual **minus sign is μ(p)**. It turns the `A`-series into `1/L^S(x, ηχ_•(u))` (table (7.16), row `(1,2r), k=0`: `−η(p)ρ^{-1}Q^{-x}`). Equivalently, as in [W5]: "Möbius times a sextic Gauss sum is a cubic Gauss sum." [CFH] (3.6)–(3.7) records the same Davenport–Hasse structure, with order 2n symbols for n odd. So 6 = lcm(3,2) is correct. More precisely, 1/6 is the denominator-6 angle 1/2 − 1/3 (section 2).

**Derivation of the offset.** Section 7.1 sets `x = t + 1 − z`, so the common Mellin weight is
`W = X^{1/2−z} Z^{x+z−1} Y^{w−1} Φ(x+z−1) M(z) Ŵ1(w)`.
Row u = 1 has numerator `ζ_F^S(6z) ζ_F^S(w)`. Its double residue at `z = 1/6`, `w = 1` gives

`X^{1/3} · Z^{x−5/6} · M(1/6) Ŵ1(1) Φ(x−5/6) · H_η(x)/L^S(x,η)`, with `M(1/6) > 0` by (7.2).

With `X = Z^{lx}` this is `C(s) = s − 5/6 + lx/3`. Part I has `lx = 1/2`, giving `C_I = s − 2/3`. The low estimate is `Z^{1/4}` (Prop. 6.3), and `C(σ0) = 1/4` gives `σ0 = 11/12`. In the team convention `C(s) = s − 1 + lx/2 + h/6` with `h = 1 − lx + ℓ`, the residue factor `X^{1/2−1/6}Z^{1/6}` reads `X^{1/2}·(Z^h)^{1/6}`. That is the noise scale times **the number of principal-copy rows `a⁶` up to the dual length `Z^h`**. Against `|J| ≳ Z^{lx/2}` this gives

`σ0 ≥ 1 − h/6`.

For Part II, `lx = 17/48`, `ℓ = 1/6` and `h = 13/16` give 83/96. The extra low-side loss `b/12 = 1/96` raises this to 7/8; Appendix A checks it, and it matches [W5] section 6a.

**Relation to [W5]'s leverage law (requested check).** [W5] section 3 says that square-root mean square plus principal-copy density `H^{−c}` gives `Re s > (1+c)/2`, and that sixth powers (`c = 5/6`) give 11/12. I agree. Write `1 − c = 1/N` for the density exponent of N-th powers. The leverage law is then the `h = 1/2` case of

**σ0 = 1 − h(1 − c) = 1 − h/N**, and the structural floor at `h = 1` is `σ0 ≥ c = 1 − 1/N`.

Part I is exactly `h = 1/2`. The 7/8 paper buys `h = 13/16` through the closed-family bootstrap. Reaching `σ0 = 1/2` needs `h(1−c) = 1/2`, so for `h ≤ 1` it needs `N ≤ 2`. Section 3 shows that `N ≤ 2` cannot carry the Möbius sign.

**Remark.** Patterson's cubic Gauss-sum series also has its pole at 5/6 = `1/2 + 1/n` ([CFH] (2.4)). This is a coincidence: `1 − 1/(2n) = 1/2 + 1/n` holds only for n = 3.

## 2. A Gauss-sum budget law (HEURISTIC)

Abstract the mechanism. The theta coefficient at a prime is a product of Gauss sums with total Galois angle `a` (mod 1); a Gauss sum of a character `(·/p)_N^e` has angle `e/N`. A probe uses `k_P` Poisson averages, each producing one Gauss sum of angle `b_i` and order `N_i`. The averaged character must pair with the theta coefficient into something explicit. That requires the total angle `a + Σ b_i` to lie in `{0, 1/2}` mod 1, because only then is the product Galois-invariant up to a quadratic Gauss sum.

**Parity rule.** A product of `k` standard Gauss sums with total angle θ equals `(−1)^k·Hecke` if θ = 0, and `(−1)^{k+1}·Hecke·g(ρ)` if θ = 1/2. This is the Weil/Gross–Koblitz statement that Galois-balanced products of `g* = −g` are Hecke characters. The rule agrees with four known evaluations:

- `g(χ)g(χ̄) = χ(−1)q`;
- `g(ρ)² = ρ(−1)q`;
- `γ2³ = −α`;
- `γ1γ2 = −αχ(4)γ3`.

The last two are replayed in [W5] section 7.

A minus sign at every prime, which is μ and therefore 1/L, appears **iff (θ = 1/2 and k_P odd) or (θ = 0 and k_P even)**.

**Budget.** Each Poisson average contributes `X_i^{1/2−z_i}` and costs a Z-shift. The general offset is `C(s) = s − [1/2 + Σ_i(1/2 − 1/N_i)] + …`, and the floor is

**σ0 ≥ 1/2 + Σ_i (1/2 − h_i/N_i), with h_i ≤ 1.**

For `k_P = 1` this reduces to `1 − h/N`.

**Consequences.** All of these come from the exact enumeration in Appendix A.

1. **Quadratic data never produce μ.** k quadratic Gauss sums have θ = k/2, so the sign is always `+`. Möbius absorption therefore needs at least one Gauss sum of order ≥ 3 in the Poisson dual. That costs at least `1/2 − 1/3 = 1/6`, so in this model **σ0 ≥ 2/3 for every theta function**, and RH strength is out of reach.
2. **For the actual cubic theta (`a = 2/3`), the minimum offset over all `k_P ≤ 3` is exactly 5/6.** It is attained by one sextic average (the [OAI] choice), by sextic plus quadratic, by two cubic averages (θ = 0 via `γ2³ = −α`), and by those plus quadratic averages. A quadratic average is a no-op: it shifts both angle and parity. **The 5/6 cannot be lowered by re-choosing the averaging pattern.** It is intrinsic to `a = 1/3`.
3. **Hypothetical theta whose prime coefficient is one order-n Gauss sum.** The single-average order is `N = 2n` (n odd), `n/2` (n ≡ 2 mod 4), or `n` (n ≡ 0 mod 4). This refines [W5]'s "order 2m, m odd". Floors `1 − 1/N`: n=3 → 5/6, n=4 → 3/4, n=5 → 9/10, n=6 → **2/3**, n=8 → 7/8. Among odd n, n = 3 is optimal; only n = 4 and n = 6 would beat 5/6.

## 3. Which theta functions actually supply the input

The Hecke relations for the k-fold theta on GL(2) are ([CFH] (2.5), from [KP]/Hoffstein)

`τ(m p^i) = G_{i+1}^{(k)}(m,p) τ(m p^{k−2−i})` for `0 ≤ i ≤ k−2`, together with `τ(m p^k) = Np^{1/2} τ(m)`.

These relations determine `τ(p)`, the valuation-1 coefficient that must carry μ at the leading `q^{−x}` level, **only for k ≤ 3**:

- **k = 2:** `τ(p) = 0`. The classical theta is supported on squares.
- **k = 3:** `τ(p) = G_2^{(3)}(1,p)`, Patterson's cubic Gauss sum.
- **k ≥ 4:** `τ(p)` is tied only to `τ(p^{k−3})` and is undetermined. [DDHL] counts the undetermined classes as n/2 − 1 for n even and (n−1)/2 − 1 for n odd.
  - **n = 4:** Patterson / Eckhardt–Patterson conjecture `τ(p)² = 2G_3^{(4)}(1,p)`, still open ([DDHL] section 1.2). Bump–Hoffstein prove it on average. Suzuki determines `τ(a²) = conj(g̃4(a))/N(a)^{1/4}` and the vanishing at cubes, but says nothing about `τ(π)`.
  - **n = 6:** [CFH] Conj. 2.1 predicts only `τ(p²) = 2G_1^{(3)}(1,p)`.
  - **n = 5 and n ≥ 7:** no conjecture at all.

**Verdict on [W5] section 6 item 7, that m = 3 is "essentially forced".** Confirmed for GL(2) covers, with these refinements:

- **(i)** The operative constraint is the parity rule together with the explicitness of `τ(p)`. Kazhdan–Patterson uniqueness (`r = n` or `n−1`) is the representation-theoretic reason that `τ(p)` is explicit for (GL2, n = 3).
- **(ii) m = 1 fails, for two separate reasons.**
  - With classical theta, `τ(p) = 0`. The only Möbius available is the Ramanujan sum of the principal character, which comes from coprimality at the zero frequency, and that is circular.
  - In [W5]'s Step-2 family with quadratic symbols, the square rows `u = v²` are principal copies. The full mean square including them is equivalent to `|A_1|² ≪ D(H+D)/H^{1/2}`, which is the target itself. Heath-Brown's quadratic large sieve covers only squarefree rows. Poisson in `u` leaves `μ(n)ε_n`, so μ is not absorbed. The hypothetical floor would be `1/2` at `h = 1`, and that is exactly where the parity rule blocks it.
- **(iii) m = 5 over Q(ζ5) is blocked twice.** `τ_5(p)` is undetermined, with no conjecture. Even if it were one quintic Gauss sum, the symbol order would be N = 10, giving floor 9/10 and Part-I analogue 19/20, which is worse than 5/6.
- **(iv)** The only hypothetical improvements come from even n (n = 4 → 3/4, n = 6 → 2/3), and these are the cases with *unknown* `τ(p)`. Under Eckhardt–Patterson, `τ_4(p)` is a square root of a quartic Gauss sum: its angle is 3/8 mod 1/2. **The unknown sign of `τ_4(p)` is precisely the unknown Möbius parity.** Even if that sign followed a Hecke law, the pairing symbol would be octic (N = 8, needs Q(ζ8)), giving floor 7/8, which is worse.
- **(v)** Explicit coefficients off the prime level do not help. Suzuki's `τ_4(a²)`, the CFH `τ_6(p²)` and the general `τ(p^{k−2}) = G_{k−1}` all put μ on `p^j` with j ≥ 2. The principal row then contains `1/L(jx + …, η^j)`, and its Euler factor still contains the unknown `τ(p)` term.

So the bottleneck is **explicit prime coefficients plus Möbius parity**, not sieve quality.

## 4. Other directions (task item 3)

**(a) Cubic theta with cubic instead of sextic symbols.** A single cubic average has angle `2/3 + 1/3 = 0` with `k_P = 1`, so the sign is `+`. The principal row becomes `ζ(3z)ζ(w)·L(x,η)/L(2x,η²)·H`, with L in the numerator. Its singularities in `Re x > 1/2` are only the principal pole, so it detects nothing. The conjugate pairing has angle 1/3 and is not explicit. The `A`-series is then a twisted cubic Gauss-sum series, which is controlled by metaplectic Eisenstein series and not by `L(x,η)`. The lattice `u a³` (pole at `z = 1/3`, which would give 2/3) is therefore unavailable. Two cubic averages do absorb μ (via `γ2³ = −α`), but their offset is again 5/6, and their finite-length boundary is `5/6 + L/3` with `L = log_Z(X1X2)`, against `5/6 + lx/6`. So this is no gain.

**(b) Higher rank and Weil-representation thetas.**

- **Weil-representation thetas** (quadratic forms, half-integral weight, Shimura–Waldspurger) are n = 2 objects. Their coefficients are 0 at squarefree indices (unary theta), positive densities or class numbers (genus theta), or `±√L(1/2, f⊗χ_D)` with unknown signs (cusp forms). By consequence 1 of section 2 they cannot carry μ.
- **GL(r) thetas on n-fold covers with r = n** (or r = n−1 for certain covers) have locally determined Whittaker coefficients in terms of order-n Gauss sums ([KP]; [BBFH] links prime-power coefficients to Weyl group multiple Dirichlet series p-parts). [W5] says the coefficients are "not known"; that should be refined to "locally determined, but multi-index". The budget allows quartic or cubic pairing symbols here (n = 4 → 3/4, n = 6 → 2/3, if the Möbius slot is a single Gauss sum). The obstruction moves to the **low side**:
  - A GL(r) row twisted by a symbol of conductor `q_m` has conductor about `q_m^r`, so reflection does not shorten it at `q_m ≈ Z`.
  - No reduction of the order-N symbol to a quadratic one is known.
  - The optimal order-N large sieve fails in general: the cubic large sieve is sharp under GRH [DR], and Gauss-sum sequences realize the extra `(QZ)^{2/3}` term.

  So the assumption `|J| ≈ Z^{lx/2}` behind every floor here is unproved for these probes. Status: **UNASSESSED** beyond this.

## 5. Summary table

The floor assumes `h ≤ 1`. The Part-I analogue is `h = 1/2`, i.e. [W5]'s leverage law `(1+c)/2`.

| Probe type | Field | Known coefficient input? | Frequency lattice | Signal offset `1/2+Σ(1/2−1/N_i)` | Heuristic floor σ0 (Part-I analogue) | Main obstruction | Label |
|---|---|---|---|---|---|---|---|
| [OAI]: cubic θ × sextic symbol | Q(√−3) | yes: Patterson + Dunn–Radziwiłł cusp expansions | `u a⁶`, ζ_F(6z) | 5/6 | 5/6 (11/12; 7/8 claimed at h = 13/16) | needs h > 1, i.e. cross-row cancellation ([W5] §6a) | IMPORTED claim + PROPOSED model |
| cubic θ × cubic symbol | Q(√−3) | yes | `u a³` (would be) | — | none: no 1/L | parity `+`: L/L(2x) in the numerator, or a non-explicit Gauss series | HEURISTIC (derived) |
| cubic θ × two cubic averages | Q(√−3) | yes (`γ2³ = −α`) | `H1H2 ∈ u·cubes` | 5/6 | 5/6, but `5/6+L/3` at finite length | no gain; extra Voronoi step | HEURISTIC |
| classical θ (n = 2), quadratic or quartic symbols | Q, Q(i) | `τ(p) = 0` | `u a²` / none | — | degenerate (hypothetical 1/2) | no squarefree coefficients; Möbius only by coprimality, which is circular; parity rule | HEURISTIC (derived) |
| Weil-rep / half-integral weight (Shimura–Waldspurger) | Q | densities or `±√L` | — | — | n/a | quadratic data never carry μ; signs unknown | HEURISTIC |
| quartic θ (n = 4) | Q(i) or Q(ζ8) | no: `τ(p)` open (EP conj., sign unknown); Suzuki `τ(a²)` known | `u a⁴` if `τ(p)` were a single quartic Gauss sum; `u a⁸` under EP | 3/4 or 7/8 | 3/4 (7/8) hypothetical; 7/8 (15/16) under EP | sign of `τ_4(p)` = Möbius parity | HEURISTIC, counterfactual |
| sextic θ (n = 6) | Q(√−3) | no: `τ(p)` undetermined; CFH conj. only `τ(p²)` | `u a³` if single sextic Gauss sum | 2/3 | 2/3 (5/6) hypothetical | `τ_6(p) = G_2^{(6)}τ_6(p³)`, unknown | HEURISTIC, counterfactual |
| quintic θ (n = 5) | Q(ζ5) | no, and no conjecture | `u a¹⁰` | 9/10 | 9/10 (19/20) | unknown, and worse anyway | HEURISTIC, counterfactual |
| odd n generally | Q(ζ_n) | only n = 3 | `u a^{2n}` | `1−1/(2n)` | `1−1/(2n)`, increasing in n | n = 3 optimal | HEURISTIC |
| GL(r) θ, r = n (or n−1) | contains μ_n | locally determined, multi-index | per budget (n = 4: a⁴; n = 6: a³) | ≥ 2/3 | 3/4 or 2/3 only if the low side holds | twisted conductor `q^r`, no quadratic reduction, sharp cubic large sieve [DR] | UNASSESSED |
| any theta (model bound) | — | — | needs one factor of order ≥ 3 | ≥ 2/3 | ≥ 2/3; RH needs N ≤ 2 | parity rule | HEURISTIC |

## Appendix A. Exact enumeration (run 2026-10-10, Python 3, `fractions`)

```python
from fractions import Fraction as Fr; from itertools import combinations_with_replacement as cwr
def admissible(a, bs):          # Moebius parity rule, section 2
    t = (a + sum(bs)) % 1; k = len(bs)
    return (t == Fr(1,2) and k % 2 == 1) or (t == 0 and k % 2 == 0)
offset = lambda bs: Fr(1,2) + sum(Fr(1,2) - Fr(1, b.denominator) for b in bs)
# cubic theta a = 2/3; angles in (1/12)Z \ {0}; k_P <= 3
# -> min offset 5/6 via ['5/6'], ['1/2','5/6'], ['2/3','2/3'], ['1/2','1/2','5/6'], ['1/2','2/3','2/3']
# hypothetical a = -1/n, single-average (N, floor): n=3:(6,5/6) 4:(4,3/4) 5:(10,9/10) 6:(3,2/3)
# 7:(14,13/14) 8:(8,7/8) 10:(5,4/5) 12:(12,11/12); k_P <= 3 never beats one average.
# sigma0 = 1 - h/6 + b/12: Part I h=1/2 -> 11/12 (C=s-2/3); Part II h=13/16, b=1/8 -> 7/8 (C=s-11/16).
```

The full script is in the session scratchpad (`altprobes/budget.py`). The enumeration does **not** check the parity rule itself, the low-side floor, or `h ≤ 1`; those are model assumptions.
