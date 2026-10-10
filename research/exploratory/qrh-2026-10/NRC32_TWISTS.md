# NRC32 twists: which characters the coarse kernel generates (C2), and the twisted checker (C1)

```text
Status: EXPLORATORY. Statements are PROPOSED, with short proofs, and unreviewed. Finite instances
  are EXACT-checked by machine. One table is EMPIRICAL (double precision). There is no RH claim and
  nothing here is reviewed. The labels NT-1..NT-9 are local to this note; they are not claim IDs.
Scope: (C2) the Dirichlet characters that the NRC32 coarse kernel generates under each way of
  separating its variables, with costs. (C1) an exact checker for the twisted Newton adapter and the
  centred cubic-mesh compression, over all 27 primitive characters mod q <= 12 and Y <= 31.
  Consequence for the family-relative step BM-3 of issue 902.
Exact sources or dependencies:
  PR 905 head 0f82df3bf1d0bc669a1bbca09f8404b77c6fecde (local ref pr905), file
    standalone/2026-09-21-native-covariance-compression/PROOF.md: (1.1), (2.1), (3.1)-(3.3),
    (4.1)-(4.5), (5.1)-(5.2), (6.1); same directory verify.py. All of this is NRC32, PROPOSED there
    and unreviewed.
  This folder: BRIDGE_MELLIN.md §3 (twisted adapter, BM-2, BM-3; PROPOSED, unreviewed) and AGENDA.md D1.
    BRIDGE names "K_I(r,s)" but does not define it; §1 below fixes the definition.
  Classical inputs, cited and not re-proved: Perron's formula with kernel 1/(w(w+1)); the convexity
    bound for zeta and L(s,chi); Ramanujan sums (von Sterneck and Hoelder formulas); Gauss sums of
    induced characters; the additive and multiplicative large sieve; Euler-Maclaurin for H_x.
  PR 909 OAI-NB26-L1 (mu = beta * chi_{-3}) appears only in a remark. It is unreviewed and not used.
What was actually run (Python 3.13.16, sympy 1.14.0, mpmath 1.3.0; one niced process at a time):
  scripts/nrc32_twists_check.py (stdlib only, exact arithmetic). The full panel PASSes in 29 s.
    Report sha256: e54d29cd1efb37486b9ff50f00167360c127caf7e0c1eab3de24c0c25414e358. The report was
    written to scratch and is not committed; regenerate it with --write. --quick also PASSes. All
    5 mutation controls are REFUSED (§5).
  scripts/nrc32_residue_sympy.py: R1-R3 PASS, and a mutated residue target is rejected.
  scripts/nrc32_twists_empirical.py: the double-precision display behind Table 2.
  PR 905 verify.py --quick, extracted unchanged to scratch: its chi_0 panels at Y = 2, 3, 7, 15
    (annular F, S, D) agree with this checker's chi_0 panels to all 12 displayed places.
  Script sha256: nrc32_twists_check.py df77cfe74f9b3aa1931c97512e987c71533080f676cc5c34792d5021dd17cab2,
    nrc32_residue_sympy.py a03fffafe5ae917acca8701ad9ea86ac7c1ddb864d02c29068a9e2f8cb8dfa15,
    nrc32_twists_empirical.py e65da2ab93ac16be14b6c2a04fca6607681138fb3b69851e2cdb9b99faa13a4b.
Smallest remaining gap: the single-member relative step FR (§6): "if Theta > 1/2, then
  S_Y << Y^eps (1+F_Y)^(2-delta)". FR is RH-equivalent. The family supremum adds nothing, because
  the kernel generates no nonprincipal twist. What is missing is a zero-blind ("low")
  representation of S_Y. Any such representation found would bring its own twist family.
```

RH remains unproved. Nothing below is evidence for RH. Finite panels cannot supply BM-3's hypothesis.

## 0. Verdict

1. **The kernel is Archimedean and divisor-type.** `K_I(r,s)` depends on the Möbius variables only through the real size of the product `rs` (NT-1). It is a multiplicative Hankel (Helson) kernel. Its only residue structure is divisibility `rs | n`, the zero class (NT-2). It is not periodic in `r` or `s` for any modulus `q ≤ Y−1` (NT-1(b)).
2. **Separations that close give a finite family, `T(χ0) = {χ0}`.** Three separations close. Mellin/Perron (O1, NT-3) generates only Archimedean twists `n^{−it}`. The Ramanujan/divisor separation (O2, NT-4) generates only principal characters `χ_{0,e}`, which are imprimitive and induced from `χ0`; they cost `e^{o(1)}` (NT-5). The additive-Fourier separation of the floor function (O3, NT-6) reduces to O2. **The family is finite and fixed constants suffice.** For a twisted member, `T(χ) ⊆ {χ, χ0}`.
3. **Routes that put a nonprincipal character on a Möbius variable produce a growing family and do not close.** Expanding the kernel itself in characters of one Möbius variable needs modulus `q ≥ Y` (NT-1(b)). The natural indirect routes are CRT reciprocity plus Gauss sums (O4), whose moduli `r ≤ Y` are the other Möbius variable, and the multiplicative large sieve (O5). They generate every primitive character of squarefree conductor `≤ Y` (O4; the full set lies within conductor `≤ Y²`) or of conductor `≤ Q` (O5). Neither closes into family members' energies `F_Y(ψ)`. O4 leaves Kloosterman-type phases. O5 is stuck at the diagonal (NT-7).
4. **For issue 902 the QRH family mechanism is inert.** With `𝒳 = {χ0}` we have `Θ* = Θ`, and BM-3 is the single-member step FR, which is RH-equivalent (NT-9). Twisting by a completely multiplicative character commutes with the Newton identity. That **decouples** the members; it gives no leverage. A growing family, with uniform `δ` as in [OAI], would arise only together with a new reflection-type second representation, and that representation is the missing ingredient itself.
5. **(C1) is done.** The checker covers all 27 primitive characters mod `q ≤ 12` and `Y ≤ 31`, with 513 panels, 1,291,976 exact `require`s (652,406 of them besides the realness assertions) and 5 mutation refusals (§5). Correction to the bridge's wording: Gaussian rationals cover only the complex characters mod 5. The characters mod 7, 9 and 11 need `Q(ζ3)` and `Q(ζ5)`, and these are used exactly.

## 1. Objects (NRC32 at 0f82df3b)

For integer `Y ≥ 1` put `b = Y+1`, `Λ = b²`, `ℓ = m(Y)`, `m(k) = Σ_{n≤k} μ(n)/n` and `F_K = Σ_{k≤K} m(k)²`. Also `g = μ·1_{≤Y}`, `z = g*g` (so `z(d) = Σ_{rs=d, r,s≤Y} μ(r)μ(s)`) and `H_r = Σ_{j≤r} 1/j`. NRC32 (1.1) states, for `Y < k < Λ`:

`m(k) = 2ℓ − Σ_{d≤Y²} z(d)/d · H_{⌊k/d⌋}`.

The cubic mesh (4.4) partitions `[b, Λ)` into blocks `I = [a, a+h)` with `h = min(Λ−a, ⌊(a²/b)^{1/3}⌋)`, so `h ≤ b`, and there are fewer than `10b` blocks. Put `m̄_I = h^{−1}Σ_{k∈I} m(k)`, `S_Y = Σ_I h m̄_I²` and `D_Y = Σ_I Σ_{k∈I}(m(k)−m̄_I)²`. Then (4.1) is `F_{Λ−1} − F_Y = S_Y + D_Y`, and (4.5) is `0 ≤ D_Y ≤ Z_Y < 5/6`. NRC32 (5.1) defines `A_d(t) = t H_r − d r` with `r = ⌊(t−1)/d⌋`, so that `A_d(t) = Σ_{k<t} H_{⌊k/d⌋}`. The open contraction is (6.1): `S_Y ≤ C (log 2Y)^A (1+F_Y)^{2−δ}`.

**Definition (this note).** For a block `I = [a, a+h)` and `d ≥ 1`,

`Φ_I(d) := [A_d(a+h) − A_d(a)]/(h d) = (1/(h d)) Σ_{k∈I} H_{⌊k/d⌋}`,  `K_I(r,s) := Φ_I(rs)`.

## 2. The coarse covariance as an explicit form

**NT-1 (PROPOSED; (a) is algebra, (b) is EXACT-checked for Y ≤ 15).**

(a) NRC32 (5.2), with `z` expanded, reads `m̄_I = 2ℓ − Σ_{r,s≤Y} μ(r)μ(s) K_I(r,s)`. So `S_Y` is the explicit quartic form in `μ|_{[1,Y]}`

`S_Y = 4(b²−b)ℓ² − 4ℓ Σ_{r,s} μ(r)μ(s) Φ_•(rs) + Σ_{r,s,r',s'} μ(r)μ(s)μ(r')μ(s') 𝒦(rs, r's')`,

with `Φ_•(d) = Σ_I hΦ_I(d) = [A_d(b²) − A_d(b)]/d` and `𝒦(d,d') = Σ_I h Φ_I(d)Φ_I(d')`. Equivalently, `S_Y` is a quadratic form in the vector `(ℓ, z) ∈ R^{1+Y²}` whose `z`-block is the Gram matrix `𝒦`, which is positive semidefinite. The bilinear part `B_I(μ,μ) = Σ μ(r)μ(s)Φ_I(rs)` is a multiplicative Hankel (Helson) form: the kernel depends on `rs` alone. Without the Newton representation, `S_Y = Σ_I h^{−1}(Σ_{k∈I} m(k))²` is a block-averaging projection of the native vector `(m(k))_{b≤k<Λ}`, which contains no arithmetic at all. **Characters can therefore enter only through how the annulus is represented by the prefix, never through `S_Y` itself.**

(b) `Φ_I` is strictly decreasing on `[1, a+h−1]` and vanishes on `[a+h, ∞)`. Hence, for every `s ≤ Y` and `1 ≤ q ≤ Y−1`, `K_I(1,s) > K_I(1+q,s)`. So `r ↦ K_I(r,s)` on `{1,…,Y}` is not `q`-periodic, not even on the residues coprime to `q`, and it has no expansion `Σ_{χ mod q} c_χ(s)χ(r)` with `q ≤ Y−1`. For prime `q > Y` such an expansion always exists, because `[1,Y]` is a set of units. It must contain a nonprincipal character mod `q`, since the function is not constant.

*Proof of (b).* `κ_I(d) = h^{−1}Σ_{k∈I}H_{⌊k/d⌋}` is nonincreasing, and it is positive exactly when `d ≤ a+h−1`. Then `Φ_I(d+1) ≤ κ_I(d)/(d+1) < κ_I(d)/d` whenever `κ_I(d) > 0`. Since `s ≤ Y < a`, `Φ_I(s) > 0`, and `Φ_I((1+q)s)` is either `0` or strictly smaller. ∎

**NT-2 (zero-class form; PROPOSED; EXACT-checked for Y ∈ {2,3,5,7}, every block, every d ≤ Y²).**

`h d Φ_I(d) = Σ_{k∈I} H_{⌊k/d⌋} = Σ_{n < a+h, d | n} (d/n) (a + h − max(n, a))`.

*Proof.* `H_{⌊k/d⌋} = Σ_{n≤k, d|n} d/n`, and `#{k ∈ I : k ≥ n} = a + h − max(n,a)` for `n < a+h`. ∎

So the Möbius variables enter in two ways only: as the real size of `n = rsj ≤ k`, and through the divisibility `rs | n`, the **zero** class mod `rs`. No class `n ≡ c (mod q)` with `(c,q) = 1` occurs. That is the only kind a nonprincipal character could detect.

## 3. Separations of the kernel and the twist sets they generate

**Convention.** A *separation* is an exact identity that writes each `m̄_I` as a finite or absolutely convergent combination, with Möbius-free coefficients, of products of linear forms `Λ(μ) = Σ_{n≤Y} μ(n)ψ(n)ω(n)`. Here `ψ` is a Dirichlet character and `ω(n)` is `n^{−s}` or `1_{n≤x}/n`. It *closes* if nothing else that depends on `μ` remains. Its twist set `T` is the set of primitive characters that induce the `ψ`'s.

### O1. Mellin/Perron: `T(χ0) = {χ0}`

**NT-3 (PROPOSED; classical Perron; residue algebra and kernel residues checked by sympy, R1–R3).** Put `W_I(w) = ((a+h)^{1+w} − a^{1+w})/(w(1+w))` and `D_Y(s) = Σ_{n≤Y} μ(n)n^{−s}`. For `c > 0`:

`h m̄_I = 2hℓ − (2πi)^{−1} ∫_{(c)} ζ(1+w) D_Y(1+w)² W_I(w) dw`.

Shifting to `Re w = −1/2`:

`m̄_I = M_I − (2πh)^{−1} ∫_R ζ(½+it) D_Y(½+it)² W_I(−½+it) dt`,

with Newton main term `M_I = 2ℓ(1 − D_1) − ℓ²(L_I + γ)`. Here `D_1 = −Σ_{n≤Y}μ(n)log n/n` and `L_I = [(a+h)log(a+h) − a log a]/h − 1`.

*Proof.* For integers `n`, `Σ_{k∈I}1_{n≤k} = (a+h−n)_+ − (a−n)_+`, and `(x−n)_+ = (2πi)^{−1}∫_{(c)} x^{1+w}n^{−w}dw/(w(1+w))`, which converges absolutely. Multiply by `(1*z)(n)/n` and sum; `Σ_n(1*z)(n)n^{−1−w} = ζ(1+w)D_Y(1+w)²`, and the interchange is absolutely convergent. The only pole in `−1/2 ≤ Re w ≤ c` is the double pole at `w = 0`; its residue is `R_I = ℓ²[(a+h)log(a+h) − a log a − h + γh] + 2hℓD_1` (R1). On the horizontal segments the integrand is `≪ T^{1/4+ε}·Y·(a+h)^{1+c}T^{−2} → 0`. ∎

For a primitive `χ ≠ χ0`, the same argument with `L(1+w,χ)` and `D_Y(·,χ)` gives residue `hL(1,χ)m_χ(Y)²`, so the centred main term is the exact Newton square `M_I^c(χ) = −L(1,χ)(m^c_χ(Y))²` (R2). The only multiplicative characters present are `n ↦ n^{−1−w}`. **T(χ0) = {χ0}**, `T(χ) = {χ}`, and all constants are fixed. *Cost:* the remainder is a critical-line moment of `ζD_Y²`; see §6.

### O2. Ramanujan/divisor: `T(χ0) = {χ0}` (principal moduli only)

**NT-4 (PROPOSED; every identity EXACT-checked).** Write `c_q` for the Ramanujan sum and `R_q(k) = Σ_{n≤k} c_q(n)/n`.

1. `1_{d|n} = d^{−1}Σ_{q|d} c_q(n)`, hence `H_{⌊k/d⌋} = Σ_{q|d} R_q(k)` (checked for d ≤ 40, k ≤ 120).
2. **Separated form.** For `Y < k < Λ`: `m(k) = 2ℓ − Σ_{q≤Y²} R_q(k) Z_q`, where `Z_q = Σ_{q|d} z(d)/d = Σ_{r≤Y} (μ(r)/r)(μ(e_r)/e_r) m_{χ_{0,e_r}}(⌊Y/e_r⌋)`, `e_r = q/(q,r)` and `m_{χ_{0,e}}(x) = Σ_{t≤x,(t,e)=1} μ(t)/t` (checked for Y ≤ 7). The derivation uses `μ(et) = μ(e)μ(t)1_{(t,e)=1}`.
3. **Principal-only.** By Hölder, `c_q(n) = μ(q/g)φ(q)/φ(q/g)` with `g = (n,q)` (checked for q ≤ 60, n ≤ 120). So `c_q(un) = c_q(n)` for every unit `u`, and `Σ_u χ(u)c_q(un) = 0` for every nonprincipal `χ mod q` (checked for q ≤ 12).
4. **Twisted.** If `(d,q_χ) = 1`, then `H_χ(⌊k/d⌋) = χ̄(d) Σ_{e|d} R^χ_e(k)` with `R^χ_e(k) = Σ_{n≤k} c_e(n)χ(n)/n`. Hence `m_χ(k) = 2m_χ(Y) − Σ_e R^χ_e(k) Z^{(q_χ)}_e`, where `Z^{(q)}_e = Σ_{e|d,(d,q)=1} z(d)/d` is **untwisted** (checked for all 27 characters, Y ≤ 5). The twist moves entirely onto the Möbius-free output side.

The generated characters are `χ_{0,e}` with `e ≤ Y`. They are imprimitive, induced by `χ0`, and `L(s,χ_{0,e}) = ζ(s)∏_{p|e}(1−p^{−s})` has the same zeros in `Re s > 0`. **T(χ0) = {χ0}** and `T(χ) ⊆ {χ, χ0}`.

**NT-5 (Euler-factor transfer; PROPOSED; the identity is EXACT-checked for e ≤ 30, k ≤ 300).** `m_{χ_{0,e}}(k) = Σ_{u | e^∞} m(⌊k/u⌋)/u`. By Minkowski and `Σ_{k≤Y} m(⌊k/u⌋)² ≤ u F_Y`,

`F_Y(χ_{0,e}) ≤ ∏_{p|e}(1 − p^{−1/2})^{−2} F_Y`,

and the product is `exp(O(√(log e)/log log e)) = e^{o(1)}`. With `e ≤ Y`, the loss is `Y^{o(1)}` and is absorbed by BM-3's `Y^ε`. A float sanity check of the inequality over the same range gives a maximum ratio of 1.0, at `e = 1`.

*Cost of O2.* The output-side moduli `q` run up to `Y²` (`Z_q ≠ 0` up to there). Blocks have `h ≤ b`, and the annulus has length `≈ Y²`. Ramanujan sums are orthogonal only over ranges much longer than `q`. The additive large sieve over the moduli `q ≤ Q = Y²` and length `N ≈ Y²` carries the factor `N + Q² ≈ Y⁴`, which is **worse than trivial by `≈ Y²`**. This is the square-step geometry: the Newton moduli reach the full output length. (The large-sieve factor is sharp in general. Sharpness for these particular coefficients is not claimed.)

### O3. Additive Fourier of the floor function: reduces to O2

**NT-6 (PROPOSED).** For `x ≥ 1`, Euler–Maclaurin gives `H_{⌊x⌋} = log x + γ − ψ(x)/x + ∫_x^∞ ψ(u)u^{−2}du`, with `ψ(u) = u − ⌊u⌋ − ½`. For integer `k`, `ψ(k/d)` is `d`-periodic in the **output** variable `k`. Its discrete Fourier transform lives on the frequencies `ν/d`: additive characters of `k` modulo `d | rs`. The Möbius variables only label the modulus. Grouping by reduced denominator gives Ramanujan sums `c_q`, which is O2, and those contain only principal characters (NT-4 (3)). No Dirichlet twist of `μ` appears.

### O4 and O5. Nonprincipal twists on a Möbius variable: growing families that do not close

**NT-7 (PROPOSED; identities EXACT-checked).**

(a) **CRT plus Gauss sums.** For `(r,s) = 1`, `s s̄ + r r̄ ≡ 1 (mod rs)` (checked for r, s ≤ 60), so `e(x/(rs)) = e(x s̄/r) e(x r̄/s)`. For `(y,r) = 1`, `φ(r)e(y/r) = Σ_{χ mod r} τ(χ)χ̄(y)` (checked for r ≤ 12). Therefore `e(x s̄/r) = φ(r)^{−1}Σ_{χ mod r} τ(χ)χ̄(x)χ(s)`, which twists `μ(s)` by every `χ mod r`. For squarefree `r`, `|τ(χ)|² = cond(χ) ≠ 0` (checked for squarefree r ≤ 15). So after applying O3's sawtooth expansion to `ψ(k/(rs))`, **every primitive character of squarefree conductor `≤ Y` appears with a nonzero coefficient**. Non-coprime pairs `(r,s)` give moduli dividing `g²r's'`, so `T_{O4} ⊆ {conductor ≤ Y²}`. *O4 does not close.* The cofactor `e(x r̄/s)` is a phase of modulus `s` in the variable `r`. The result is a Kloosterman-type bilinear form, not a combination of members' prefix forms. Using it needs bilinear or Kloosterman input, and any bound must hold uniformly over conductors up to `Y`.

(b) **Multiplicative large sieve.** Here `Σ_{q≤Q}(q/φ(q))Σ*_χ|Σ_{n≤N} a_nχ(n)|² ≤ (N+Q²)Σ|a_n|²`, and `T` is every primitive character of conductor `≤ Q`. The bound sits at the diagonal. For the principal member alone it is weaker than Cauchy–Schwarz, so it cannot produce a member-relative saving. This is the principal-member extraction firewall of AGENTS.md.

(c) **Inserted residue partitions.** One can always insert `1 = Σ_{a mod q} 1_{r≡a}` and expand by characters mod a fixed `q`. By NT-1(b) the kernel does not respect these classes. Exact Parseval (EXACT-checked for q ∈ {3,4,5,7,8,9,12}, Y ∈ {3,5}) gives `Σ_{χ mod q} S_Y(χ) = φ(q) Σ_{(a,q)=1} S_Y^{AP}(q,a)`, and the same for `D_Y`. So the inserted family recombines into progression energies. It adds the members `χ mod q` but no information about the principal one.

(d) **Remark (HEURISTIC; nothing proved).** The norm-coefficient route of PR 909 (`μ = β * χ_{−3}`, i.e. `1/ζ = L(·,χ_{−3})/ζ_K`) adds the single fixed twist `χ_{−3}`, as long as `β` is treated as a function on `Z`. As soon as harmonic analysis on `Z[ω]` is used, which is where the QRH reflection lives, Hecke characters of `Q(√−3)` of growing conductor enter. That family is the [OAI] one.

**Summary table.**

| route | exact? | closes? | twist set `T(χ0)` | finite? | main cost |
|---|---|---|---|---|---|
| O1 Mellin/Perron | yes (NT-3) | yes | `{χ0}`, plus Archimedean `n^{−it}` | yes | critical-line moments of `ζD_Y²` (§6) |
| O2 Ramanujan/divisor | yes (NT-4) | yes | `{χ0}` (principal `χ_{0,e}`, `e ≤ Y`) | yes | Euler factor `Y^{o(1)}` (NT-5); moduli `≤ Y²` vs length `≈ Y²` |
| O3 additive floor | yes (NT-6) | reduces to O2 | `{χ0}` | yes | as O2 |
| O4 CRT + Gauss | yes (NT-7a) | **no** | squarefree conductors `≤ Y` (within `≤ Y²`) | **grows** | Kloosterman-type cofactor; uniform `δ` |
| O5 multiplicative large sieve | inequality | **no** | conductors `≤ Q` | **grows** | diagonal floor; no principal extraction |
| inserted classes mod fixed q | yes | yes, trivially | characters mod q | yes | Parseval recombination; no information |
| β over `Q(√−3)` | identity of PR 909 | — | `{χ0, χ_{−3}}`, then Hecke | grows once Hecke analysis is used | the [OAI] uniformity |

**Answer to (C2).** Under its exact closing separations, the NRC32 coarse kernel generates **`T(χ0) = {χ0}`**. The family is finite, conductors stay at 1, imprimitive principal moduli cost `Y^{o(1)}`, and fixed constants suffice. Directly on the kernel there is no middle option: a nonprincipal character needs modulus `≥ Y` (NT-1(b)), and the natural routes that introduce one generate all conductors up to `Y` (or `Q`) without closing.

## 4. Twisted objects (mathematics behind C1)

Let `χ` be primitive mod `q`. Put `g_χ = μχ1_{≤Y}`, `z_χ = g_χ*g_χ`, `H_χ(r) = Σ_{j≤r}χ(j)/j`, `C_χ(r) = Σ_{j≤r}χ(j)` and `m_χ(k) = Σ_{n≤k}μχ(n)/n`.

- **Equivariance (PROPOSED; EXACT-checked).** `(fχ)*(gχ) = (f*g)χ`, so `z_χ = χz` and `v_χ = 2g_χ − χ*z_χ = χv`. The twisted adapter of BRIDGE §3, `m_χ(k) = 2m_χ(Y) − Σ_d z_χ(d)/d · H_χ(⌊k/d⌋)` for `Y < k < Λ`, is the `χ`-image of NRC32 (1.1).
- **Twisted (5.1)/(5.2) (PROPOSED; EXACT-checked).** `A^χ_d(t) := Σ_{k<t} H_χ(⌊k/d⌋) = t H_χ(r) − d C_χ(r)`, with `r = ⌊(t−1)/d⌋`, since each `χ(j)/j` is counted `t − jd` times. Then `m̄_I(χ) = 2m_χ(Y) − h^{−1}Σ_d z_χ(d)/d [A^χ_d(a+h) − A^χ_d(a)]`. For `χ0` this recovers `−dr`. For `χ ≠ χ0` the linear term is a bounded character sum, `|C_χ| ≤ φ(q)/2`.
- **NT-8 (centred compression for every complex centre; PROPOSED; EXACT-checked).** For any vector `x` on the annulus and any `c ∈ C`,
  `Σ_k |x_k − c|² = Σ_I h|m̄_I − c|² + D`, where `D = Σ_I Σ_{k∈I}|x_k − m̄_I|²` does not depend on `c`.
  *Proof.* Both sides are `Σ|x|²`-type terms minus `2Re(c̄ Σ_k x_k)` plus `|c|²(b²−b)`. This uses `Σ_I h m̄_I = Σ_k x_k`, `Σ_I h = b² − b`, and the `c = 0` identity (4.1). ∎
  The checker certifies the `c = 0` identity and the cover length exactly. It also re-runs the whole split at three nonzero exact centres per character. That certifies the split at the transcendental centre `c = 1/L(1,χ)` of BRIDGE §3 without evaluating it. `D_Y(χ) ≤ Z_Y < 5/6` holds because `|μχ(k)/k| ≤ 1/k`, which is checked exactly as `|v_χ(k)|² ∈ {0,1}`.
- `S_Y(χ̄) = S_Y(χ)` and `F_Y(χ̄) = F_Y(χ)`, since `m_{χ̄}` is the complex conjugate of `m_χ`. Conjugate pairs agree exactly in the panels.

## 5. (C1) The checker

`scripts/nrc32_twists_check.py` uses exact integer arithmetic in `Q(ζ_N)`. Each element is a coordinate vector in the basis `1, ζ, …, ζ^{φ(N)−1}`, reduced modulo the cyclotomic polynomial `Φ_N`. Each character takes values in `Q` (orders 1 and 2), `Q(i)` (order 4), `Q(ζ3)` (orders 3 and 6) or `Q(ζ5)` (orders 5 and 10). Real numbers are compared exactly. In `Q`, `Q(i)` and `Q(ζ3)` real elements are rational. In `Q(ζ5)` a real element is `A + B√5`, with its sign decided by comparing `A²` with `5B²`. The Gauss-sum checks use `Q(ζ_{lcm(r,λ(r))})`, up to `N = 156`.

**Coverage.** The checker enumerates all characters mod `q ≤ 12` by generators and homomorphism checks, then selects the primitive ones by conductor. That gives 27 characters, distributed by conductor as 1:1, 3:1, 4:1, 5:3, 7:5, 8:2, 9:4, 11:9, 12:1. Real characters: `chi_3.1 = χ_{−3}`, `chi_4.1 = χ_{−4}`, `chi_5.2 = χ_5`, `chi_7.1 = χ_{−7}`, `chi_8.1 = χ_{−8}`, `chi_8.3 = χ_8`, `chi_11.5 = χ_{−11}`, `chi_12.3 = χ_{12}`. The panel takes `Y ∈ {1,…,16, 20, 24, 31}`, giving 513 panels. The deep checks (pointwise adapter, twisted block-mean formula, pair identity) run for `Y ≤ 8`, 216 panels.

**Per panel.**
- The producer uses `μ` only through `Y` (trial division). It builds `g_χ, z_χ, v_χ`.
- It checks `z_χ = χz`, and `v_χ(n) = μ(n)χ(n)` for every `n < (Y+1)²` against an independent sieve: 104,085 coefficients.
- It forms `L·m_χ(k)` from `v_χ` with `L = lcm(1..Λ−1)`, so no future `μ` enters.
- Exact per-block orthogonal split; (4.1); `D_I ≤ h(h²−1)/(12a²)` per block (51,336 blocks); `Z < 5/6`; `D ≤ Z`; cover length; centre invariance at three exact centres.
- In deep panels also: the pointwise adapter (6,480 values), `A^χ_d` (85,590 values) and the twisted (5.2).

The C2 identities of §§2–3 are checked separately with the counts given there.

**Mutation controls.** Each is run with `--quick` and each is REFUSED:

| mutation | refused at |
|---|---|
| `flip_prefix_mobius` | `twisted_newton_coefficient` |
| `untwisted_harmonic` | `twisted_newton_coefficient` |
| `drop_character_sum` | `twisted_harmonic_primitive` |
| `drop_principal_euler` | `separated_Z_principal_characters` |
| `flat_kernel` | `kernel_strictly_decreasing` |

**What the checker does NOT do:**
- It does not produce a directed or decimal-enclosure output in the PR 905 receipt format. The values in Table 1 are float displays of exact rationals, or of exact `A + B√5`.
- It does not check NT-3's Perron integral, nor any estimate, nor BM-2 or BM-3.
- It does not certify Table 2.

**Table 1 (exact values shown to six places; uncentred `D_Y` equals centred `D_Y`).** All 27 characters share the mesh, with 33 blocks and `Z = 0.125720` at `Y = 15`, and 71 blocks and `Z = 0.154129` at `Y = 31`. The largest `D/Z` over all 513 panels is `0.6244`.

| χ | D at Y=15 | D at Y=31 |
|---|---|---|
| χ0 | 0.021663 | 0.019363 |
| χ_{−3} | 0.018553 | 0.012745 |
| χ_{−4} | 0.019929 | 0.012407 |
| chi_5.1 (order 4) | 0.020417 | 0.014810 |
| chi_7.2 (order 6) | 0.019415 | 0.015285 |
| chi_9.1 (order 6) | 0.018071 | 0.012224 |
| chi_11.1 (order 10) | 0.021893 | 0.016397 |
| χ_{12} | 0.012666 | 0.007940 |

**Table 2 (EMPIRICAL, double precision, not directed). Centred energies at Y = 255 (b² − 1 = 65535), centre 1/L(1,χ).** Conjugate characters give identical rows, so one row per conjugate pair is shown.

| χ | order | F_Y^c | S_Y^c | D_Y | S^c/(1+F^c)² |
|---|---|---|---|---|---|
| χ0 | 1 | 1.4259 | 0.1557 | 0.0059 | 0.026 |
| χ_{−3} | 2 | 0.6538 | 0.2233 | 0.0048 | 0.082 |
| χ_{−4} | 2 | 0.3583 | 0.2794 | 0.0043 | 0.151 |
| chi_5.1 | 4 | 0.5208 | 0.4896 | 0.0051 | 0.212 |
| χ_5 | 2 | 3.9300 | 0.2402 | 0.0052 | 0.010 |
| χ_{−7} | 2 | 0.5394 | 0.5729 | 0.0055 | 0.242 |
| chi_7.2 | 6 | 1.2929 | 1.2483 | 0.0055 | 0.237 |
| chi_7.3 | 3 | 1.9604 | 0.3454 | 0.0050 | 0.039 |
| χ_{−8} | 2 | 0.4686 | 0.5352 | 0.0041 | 0.248 |
| χ_8 | 2 | 1.3081 | 0.2530 | 0.0041 | 0.047 |
| chi_9.1 | 6 | 0.7522 | 0.7569 | 0.0044 | 0.247 |
| chi_9.2 | 3 | 1.3818 | 0.4026 | 0.0049 | 0.071 |
| chi_11.1 | 10 | 0.7061 | 0.7440 | 0.0057 | 0.256 |
| chi_11.2 | 5 | 1.0139 | 0.4543 | 0.0057 | 0.112 |
| chi_11.3 | 10 | 5.3042 | 4.9735 | 0.0053 | 0.125 |
| chi_11.4 | 5 | 1.4523 | 0.6127 | 0.0059 | 0.102 |
| χ_{−11} | 2 | 0.9289 | 1.0771 | 0.0062 | 0.290 |
| χ_{12} | 2 | 0.6775 | 0.3180 | 0.0029 | 0.113 |

For χ0 the rows at Y = 31, 63, 127, 255 have S^c = 0.0797, 0.1112, 0.1283, 0.1557. As in NRC32, the coarse part carries almost all of the annular energy for every twist. The ratios are `O(1)` and are not trending in any direction that this tiny range could show. **No exponent is fitted, and nothing here bears on δ.**

## 6. What a family-relative step must prove, and whether anything makes it easier

**NT-9 (PROPOSED; specialization of BM-3).** By §3, every closing separation keeps `𝒳 = {χ0}` closed (`T(χ0) = {χ0}`; principal moduli are absorbed by NT-5). So BM-3 applies with fixed constants and `Θ* = Θ`. The step to be proved is

**FR.** If `Θ > ½`, then there is `δ > 0` such that `S_Y ≪_ε Y^ε (1+F_Y)^{2−δ}` for all large `Y`.

FR is **RH-equivalent**. RH makes it vacuous, and FR implies RH by BM-3. There is no slack. The argument of BM-2 also gives `limsup log F_Y / log Y = 2Θ−1`. In any world with `Θ > ½`, FR would force `4Θ − 2 ≤ (2−δ)(2Θ−1)`, which is false. So a proof of FR must use an input that fails in every off-line world.

**What FR says in O1 language (HEURISTIC translation of exact formulas).**

- Exactly, from NRC32 (3.2)–(3.3) at `N = Y`, `Λ = Y+1`:
  `F_Y + (Y+1)ℓ² = (2π)^{−1}∫|sD_Y(s) − ℓ(Y+1)^{1−s}|²|s(s−1)|^{−2}dt` with `s = ½+it`.
- Exactly, by NT-3, `S_Y = Σ_I h|M_I − E_I|²` with `E_I = (2πh)^{−1}∫ ζD_Y²(½+it) W_I(−½+it) dt`.
- Heuristically (block averaging acts as a frequency cutoff `|t| ≲ a/h ≤ Y`), `Σ_I h|E_I|² ≈ (2π)^{−1}∫_{|t|≲Y} |ζ(½+it)|² |D_Y(½+it)|⁴ dt/|½+it|²`.

FR is then:
1. a reverse-Hölder (no-concentration) inequality between the `|ζ|²`-weighted fourth moment and the second moment of the Möbius polynomial `D_Y` on the critical line; and
2. an endpoint condition on the Newton main term, `Y² ℓ⁴ log² Y ≪ Y^ε F_Y^{2−δ}`.

The elementary bound `|ℓ| ≤ (18F_Y/Y)^{1/3}`, which follows from `|m(k) − m(k−1)| ≤ 1/k` on the last `Y|ℓ|/4` cells, gives only `≪ Y^{2/3}F_Y^{4/3}`, which is far from enough. With a zero at `β0`, both sides of (1) are dominated by windows `|t − γ0| ≲ 1/log Y` and scale like `Y^{4β0−2}` against `(Y^{2β0−1})^2`, so `δ = 0` exactly. This is BRIDGE §3 remark (iii), seen in moments.

**Special structure: none of it gives leverage.**
- *Twist equivariance.* Completely multiplicative twists commute with the Newton identity, the adapter and the mesh (§4). So for each `χ`, `S_Y(χ)` involves only `μχ` data, and the members **decouple**. The family supremum gains nothing over the single-member problem: for each `χ` it is GRH for `L(s,χ)`. QRH's leverage comes from an operation that does *not* commute with twisting. Poisson summation (theta reflection) maps one member's signal into other members' error rows. NRC32 has no such map.
- *Nonprincipal members are slightly cleaner.* There is no pole, so the main term is the exact Newton square `−L(1,χ)(m^c_χ)²`, and the linear kernel term is a bounded character sum. The remainder is still a critical-line moment of `L·D_χ²`, which is the same problem.
- *Parseval over `χ mod q`* gives family averages as progression energies (NT-7(c)). Averages are accessible to large-sieve or Bombieri–Vinogradov methods. BM-3 needs the worst member, and a family identity is not principal-member extraction.
- *Growing families* (O4, O5, β/Hecke) would need `δ` uniform for conductors up to `Y^c`. The uniform version of BM-2 (≤) is standard: under zero-freeness right of `Θ*`, `1/L(s,ψ) ≪ (q(|t|+2))^ε` gives `F_Y(ψ) ≪ (qY)^ε Y^{2Θ*−1}`. The conclusion would then be GRH for the whole family, which is a strictly stronger target. Such a family enters only with a route that adds new (reflection-type) input, and that input is precisely what is missing.

**Candid conclusion.** BM-3's hypothesis is RH-strength. (C2) shows the NRC32 kernel needs only the trivial family, so the QRH bootstrap structure reduces to FR and contributes no extra lever. The remaining step is to find a zero-blind ("low") representation of `S_Y`. By BRIDGE §2's firewall heuristic, that will require additive or automorphic input that fails for Beurling-type systems. If such input is found, it will bring its own growing family, and NT-7 then states the uniformity bill.

## 7. Boundaries, misreadings and next steps

- `T(χ0) = {χ0}` is **not** a reduction in difficulty. It says that the family supremum is inert for NRC32.
- Finiteness is a property of the closing separations O1–O3. A proof that introduces reciprocity, a large sieve, or `Q(√−3)` harmonic analysis changes `T` (NT-7).
- The Helson/Archimedean description is structural. No uniqueness theorem for spectral representations of `Φ_I` is claimed. NT-1(b) is the precise exclusion statement.
- The checker certifies finite identities only. NT-3's integral, NT-5's asymptotic, BM-2, BM-3, NT-9 and every "≈" in §6 are not machine-checked. Table 2 is plain double precision.
- BRIDGE §3 says "Gaussian rationals". That is accurate only for the complex characters mod 5.
- Bounded next steps:
  1. Independent review of NT-1 through NT-8. All are short.
  2. A mechanical port of the checker into the PR 905 receipt format, with directed decimal output.
  3. A reconnaissance of the O1 moment formulation of FR as a reverse-Hölder target for `D_Y`. This is exploration only, and it is still RH-strength.
