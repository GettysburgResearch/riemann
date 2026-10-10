# A2 literature check: cubic Weyl group MDS, GL(3) theta, mean values

```text
Status: SURVEY + PROPOSED assessment. No theorem is proved here and nothing here bears on RH directly.
  Tags: [LIT] stated or proved in the cited source; [CONJ] conjectured there; [INF] our inference;
  [EMP] finite numerics.
Scope: the fourth-moment dual C_h(X) of FOURTH_MOMENT_A2.md (PR 910 eq. (3.5)) and its proposed
  identification with the cubic type-A2 Weyl group multiple Dirichlet series (WMDS)
Exact sources or dependencies: listed at the end. Read in full or in the relevant sections: BBCFH06,
  CG10, CG07 (intro), FG15, DIPP26 (intro). Read at abstract level only: DR24, dFDH26, Dunn25,
  DdFDS24, BBFH07, BBFH12, Gao17, Chen24, CFH12. Known only through citations: BH86, Proskurin,
  KP84, HB00, HBP79, FHL03, BFH05, LP02. Louvel's papers were not located.
What was actually run:
  a2/bbf_dictionary.py: 314 coprime prime pairs and 1431 (pair, row) tests, max deviation 7.6e-16;
    stable p-parts over 36 primes, max deviation 6.9e-11
  a2/dual_diagonal_check.py: squarefree columns, L = 108, up to 4692 rows
Smallest remaining gap: an unconditional asymptotic (dispersion) estimate
  Σ_{N h ≤ 𝓗} |C_h|² = S_diag + (explicit secondary terms) + O(L^{2+ε}) with 𝓗 = L²/H > L.
  No reflection-type theorem supplies this, whether for GL(3) or GL(2).
```

## 0. Verdict in brief

* **The shape identification is correct and exact** [LIT + EMP]. On coprime squarefree pairs, our
  coefficient is the cubic A2 WMDS coefficient `H(d, e; h, h)` (twisting parameter `m = (h, h)`),
  normalized by `N(de)^{-1/2}` and multiplied by an extra *quadratic* character `(h/de)₂`. That
  quadratic factor lies outside every cubic WMDS.
* **The proposed "GL(3) cubic theta reflection" does not exist in the needed form** [LIT + INF]. The
  cubic theta function on GL(3) has Whittaker coefficients `τ(m,1) = 0` unless `m` is a cube, so its
  coefficients vanish on our support. Patterson's GL(2) coincidence (Gauss sums as both moduli
  coefficients and theta coefficients) fails one rank up.
* **Reflections, of whatever rank, are the wrong tool for (3.5)** [INF + EMP]. Since `L > H`, the
  dual has more rows than columns. The positive mean square `Σ_h |C_h|²` is then its diagonal
  `S_diag ≍ 𝓗L` to within a few percent ([EMP], agreeing with FOURTH_MOMENT_A2 §6). What is needed is
  an *asymptotic* for the dual off-diagonal with error `O(L²)`, at relative precision `H/L`.
  Row-by-row functional equations are roughly isometric and leave `S_diag` unchanged. The only
  analogous asymptotic (Dunn–Radziwiłł's dispersion estimate) assumes GRH over `Q(ω)`, which implies RH.
* **Rating: (b), leaning to (c).** As literally proposed, the route is blocked (c). A viable route
  needs a new unconditional dispersion theorem for A2-structured sextic families (§6), with no
  unconditional precedent even in the linear GL(2) case.

## 1. The cubic A2 WMDS: exact formulas [LIT]

Setting: `F ⊇ μ₆` (for us `F = Q(√−3)`, `n = 3`). The residue symbol `(a/c)` is a character in `a`
modulo `c`. Gauss sums are `g(m, c) = Σ_{a mod c} (a/c) ψ(ma/c)`, where `ψ` is trivial on `O_S` and
on no larger ideal (CG10 (2.1)). Our `e(z) = exp(2πi Tr(z/√−3))` meets this condition.

* Series (BBCFH06 (9)):
  `Z_Ψ(s₁, s₂; m) = Σ_{c₁,c₂} H(c₁, c₂; m) Ψ(c₁, c₂) N(c₁)^{-2s₁} N(c₂)^{-2s₂}`.
  CG10 writes `|c|^{-s}`, so `s_CG = 2s`.
* Twisted multiplicativity for `gcd(c₁c₂, c′₁c′₂) = 1` (CG10 (4.3)–(4.4) with `‖α‖² = 1` and
  `2⟨α₁,α₂⟩ = −1`):

      H(c₁c′₁, c₂c′₂) = H(c)H(c′) · (c₁/c′₁)(c′₁/c₁)(c₂/c′₂)(c′₂/c₂) · (c₁/c′₂)^{-1}(c′₁/c₂)^{-1}.

  Hence `H(c₁, c₂) = g(1,c₁) g(1,c₂) (c₁/c₂)^{-1}` on coprime squarefree pairs (BBCFH06 p. 12).
* Twisting (CG10 (4.5)): if `(c₁c₂, m′) = 1`, then
  `H(c; m₁m′₁, m₂m′₂) = (m′₁/c₁)^{-1}(m′₂/c₂)^{-1} H(c; m)`.
* p-parts. A2 is in the **stable range for every `n ≥ 2`** (BBCFH06 §2: `n ≥ Σdᵢ = 2`; CG07,
  introduction). The untwisted support is the hexagon `ρ − wρ` (BBCFH06 (13)):

  | `(k₁,k₂)` | (0,0) | (1,0), (0,1) | **(1,1)** | (2,1), (1,2) | (2,2) |
  |---|---|---|---|---|---|
  | `H(p^{k₁},p^{k₂})` | 1 | `g(1,p)` | **0** | `g(1,p)g(p,p²)` | `g(1,p)²g(p,p²)` |

  All other `H(p^a, p^b)` vanish. For `n = 3`, `g(p, p²) = N(p)·conj(g(1,p))` [EMP]. Hence
  `H(p²,p) = H(p,p²) = N(p)²` and `H(p²,p²) = N(p)² g(1,p)`. At primes `p | m` the p-parts are
  twisted Gelfand–Tsetlin sums; BBFH07 proves these for A2, all `n` and all `m`.
* Functional equations. In BBCFH06 normalization (eqs. (6)–(8)):
  `σ₁ : (s₁,s₂) ↦ (1−s₁, s₁+s₂−½)` and `σ₂ : (s₁,s₂) ↦ (s₁+s₂−½, 1−s₂)`, which generate `S₃`.
  The normalizing factor is `G₃(s₁)G₃(s₂)G₃(s₁+s₂−½) ζ_F(6s₁−2) ζ_F(6s₂−2) ζ_F(6s₁+6s₂−5)`.
  With a twist (CG10 Thm 6.1): `Z*(s; m, Ψ) = |mᵢ|^{1−sᵢ} Z*(σᵢs; m, σᵢΨ)`. The parameter `m` is
  preserved and `Ψ` moves within the finite-dimensional space `M(Ω^r)`. The polar hyperplanes are
  the `W`-translates of `s_CG,i = 1 ± 1/3`. Composing the three reflections of
  `w₀ : s ↦ (2−s₂, 2−s₁)` gives the factor `|m₁m₂|^{2−s₁−s₂}` [INF].
* The Eisenstein conjecture holds for type A: `Z(s; m)` is the `m`-th Whittaker coefficient of the
  Borel Eisenstein series on the 3-fold cover of GL(3) (BBFH07 for `r = 2`; BBF11). The `cᵢ` are
  Bruhat-cell moduli and `m` is the Whittaker index.

## 2. Dictionary with C_h [EMP + INF]

For coprime primary squarefree `d, e` with `(de, h) = 1`, `a2/bbf_dictionary.py` checks:

    γ₂(d)γ₂(e)·conj((e/d)₃)·χ_d(h)χ_e(h) = N(de)^{-1/2} · H(d, e; h, h) · (h/de)₂,   (h/c)₂ := χ_c(h)³.

* **Orientation.** For primary coprime `d, e`, `(d/e)₃ = (e/d)₃` (check (R), deviation exactly 0).
  So our `conj((e/d)₃)` equals BBF's `(c₁/c₂)^{-1}` under either assignment of `(d, e)` to
  `(c₁, c₂)`. In S-adic language, the difference is a Hilbert symbol that is trivial on primary
  elements.
* **Twist.** `χ_c(h) = (h/c)₃^{-1}·(h/c)₂`. The cubic part is exactly BBFH's "twisted" series with
  `m = (h, h)`. In BBFH, "twisted" means a Whittaker index, not a character `ψ`.
* **The quadratic part does not fit.**
  * It is not an `m`.
  * It is not in `M(Ω)`: `Ψ` must be equivariant under `Ω ⊇ F_S^{×3}`, and cubes are not squares.
  * No degree-6 root datum fits either. A node carrying `γ₂` needs `‖α‖² = 2`, and an odd
    interaction exponent then gives a non-integral Cartan entry [INF].
* **Other mismatches.** `C_h` sees only `(c, h) = 1` and coprime squarefree pairs; `conj(α)` and the
  ray phases must be finite S-data (not rechecked).
* **Completion** is finite and explicit: the hexagon adds only `(p²,p)`, `(p,p²)` and `(p²,p²)`.
  This differs from the GL(2) theta's `n b³` completion.

## 3. Residues and theta

* Kubota-pole residues cancel Gauss sums (`Res D(s,a) ∝ conj g(a)`); residues of the cubic A3
  series give the FHL03 series (BB06b, via CG10 §7.2) [LIT].
* **The cubic theta on GL(3)** has a unique Whittaker model (KP84; FG15 §5) [LIT]. Its coefficients
  were computed by Proskurin and by Bump–Hoffstein (BH86). As quoted in FG15 §5:
  `τ(m,1) = 0` unless `m` is a unit times a cube, and `τ(a m³, 1) = |m| τ(a,1)` [LIT].
  Unique Whittaker models give local factorization. Combined with `τ(p,1) = 0` and (symmetrically)
  `τ(1,p) = 0`, this makes **τ vanish on every coprime squarefree pair `(d,e) ≠ (1,1)`** [INF].
  No theta-Voronoi formula on GL(3) can therefore detect `C_h`.
* **A2-shaped theta coefficients need degree `n ≥ 4`.** For the quartic theta on GL(3),
  `τ(p^{4k+1},1) = |p|^{k−½} ḡ(p)` (FG15) [LIT]. For `n > 4`, coefficients are unknown even on GL(2)
  (FG15; CFH12 conjectures the case `n = 6`) [LIT/CONJ]. BBFH12 matches large-`n` theta coefficients
  on Hecke orbits with stable WMDS p-parts (abstract only).
* [INF, unchecked] The quadratic factor might live on a degree-6 Brylinski–Deligne cover with
  `Q(α^∨) = 2` (cubic root Gauss sums, sextic torus data; Gao17, Chen24); its theta would again be
  in the degenerate `n_α = r` regime.

## 4. Mean values and large sieves [LIT]

* **Heath-Brown's cubic large sieve** (HB00):
  `Σ_{N m ≤ M} |Σ_{N n ≤ N} a_n (n/m)₃|² ≪ (M + N + (MN)^{2/3})(MN)^ε ‖a‖²`.
  See also BY10; BGL14 for n-th order.
* **The extra term is necessary.** dFDH26 proves unconditionally that the cubic and quartic large
  sieves are not perfectly orthogonal, and that the obstruction is the **Gauss-sum bias**. Under GRH,
  DR24 shows the cubic large sieve is sharp. Gauss-sum-weighted sequences, which are ours, are the
  extremizers.
* **DR24**: under GRH, an asymptotic for Σ over primes of γ(p), with main term `X^{5/6}/log X`. The
  tools are an explicit level-aspect Voronoi formula and a GRH-conditional **dispersion estimate**,
  "a cubic large sieve with a main-term correction". **Dunn25** proves unconditionally a bilinear
  large sieve whose kernel is a cubic metaplectic cusp form's coefficients, beating the 2/3
  level-of-distribution barrier in a linear estimate.
* **Moments.** DdFDS24: mollified second moment of cubic Hecke L-functions. DIPP26: first and
  second twisted moments for r-th order characters (`r ≥ 3`) via MDS, naming the cubic large sieve
  as the bottleneck. GZ24: sextic Hecke moments.
* **Not found** (search negatives): mean values over A2/GL(3)-metaplectic twisting parameters;
  fourth moments, mollified or not, of cubic/sextic families or of Möbius-weighted character sums.

## 5. GL(2) theta × divisor view

The two views are the same object: `C_h = Σ_r conj(α(r)) γ₂(r) W_X(r) χ_r(h)`, with a divisor
weight `W_X(r)`.

* Mellin transform in the two factor sizes gives
  `Σ_n γ₂(n) σ_w(n) N(n)^{-s} = Σ H(d,e) N(d)^{-(s+½)+w} N(e)^{-(s+½)}` on the squarefree support.
  So the Rankin–Selberg series of θ against `E_w` is the A2 WMDS restricted to a line [INF].
  * The two **completions differ**: the theta side has `τ(nb³)`, the WMDS side has the hexagon.
  * Unfolding `⟨θ·Ē_w, E^{(3)}(·, s̄)⟩`, with Zagier regularization as adapted in dFDH26, should give
    meromorphic continuation of the theta-side series [INF]. I found no paper that does this.
* **(i)** For `Σ τ(n) d(n) ψ(n)` and `Σ τ(n) σ_w(n) N(n)^{-s}` I found no result, and Louvel was not
  located. The nearest work is Patterson's `Σ |τ(n)|²` (the Rankin–Selberg of θ with itself) and
  the Rankin–Selberg lower bounds of dFDH26.
* **(ii) Dunn–Radziwiłł Type II.** `χ_{de}(h) = χ_d(h) χ_e(h)` splits, so the row twist goes into
  the coefficients, and `γ₂(de) = γ₂(d)γ₂(e) conj((e/d)₃)` turns each `C_h` into a bilinear form
  with cubic kernel. The cubic large sieve then gives `|C_h| ≪ X^{5/3+ε}` uniformly in `h`, against
  a square-root size of `X` [INF]. Under GRH this cannot be improved for general coefficients.
* **Verdict on the bilinear machinery: no.** Type I/II bounds act row by row and cannot drop below
  the square-root size `|C_h|² ≈ L`. The fourth moment instead needs
  `Σ_h (|C_h|² − diag_h) = O(L²)`, i.e. cross-row cancellation at relative precision `H/L`.
  `a2/dual_diagonal_check.py` [EMP] gives `M/Diag = 1.137, 1.086, 0.992, 0.968, 0.969, 0.981` at
  `rows/L = 1.8 … 43`. This is consistent with FOURTH_MOMENT_A2 §6: generic, diagonal-dominated
  behaviour. A finite trend is not a theorem.
  The relevant DR ingredient is the *dispersion asymptotic*, not the Type I/II bounds, and that is
  GRH-conditional. GRH for Hecke L-functions over `Q(ω)` includes `ζ_K = ζ·L(·,χ₋₃)`, so it implies
  RH and cannot be imported here.
* Risk to check [INF]: Patterson-bias terms (from the Kubota poles) on rows where `χ_·(h)`
  degenerates to a cubic character (squares times units). Whether `conj(α)` removes them is unchecked.

## 6. The self-reproduction (FOURTH_MOMENT_A2, "Second-step analysis")

**(a) Does an A2 functional equation avoid it? Yes, formally, but this does not help.**

* WMDS functional equations act only on Gauss-sum-weighted variables. The *completed* twisted
  series (all `c`, with hexagon and twisted p-parts) is closed under `S₃` (CG10 Thms 5.8, 6.1):
  `σ₁` returns `H(·, c₂)` with `g(c₂)` intact, and no Möbius variable ever appears [LIT].
* The `μ(e)` in the coordinator's step comes from reflecting a **coprimality-truncated** d-sum
  [INF]. `χ_d(e⁴)` enforces `(d,e) = 1`, and the `B_{p,4}` (Ramanujan-type) factor is that sieve
  after duality. In the completed series, the `p | (c₁,c₂)` terms `(p²,p)`, `(p,p²)` and `(p²,p²)`
  are present and carry `g(p,p²) = N(p)·conj g(p)`. "Complete first, then remove" moves the Möbius
  into a removal variable of norm `≤ X^{2/3}` in a balanced box.
* The relocation does not make the route work:
  * Conductor bookkeeping. CG10 Thm 5.8 gives a single-node conductor `N(h·c_j)`. Our `w₀` factor
    gives a joint conductor `N(h)²`, with dual lengths `N(h)²/X` per variable [INF]. Both lengthen
    the sum, because the bulk rows have `N h ≍ 𝓗 = X⁴/H > X²`.
  * The isometry point from §0 remains.
* The cubic GL(3) theta does not act at all (§3).

**(b) Möbius sum against `conj(α)·χ_·(h)` with cubic pair phases.**

* If `α` is a Hecke character, `e ↦ conj(α(e)) χ_e(h)` is, by sextic reciprocity, a sextic Hecke
  character `ψ` of conductor about `N(h)`. The sum is then a partial sum of the coefficients of
  `1/L(s, ψ)` [INF]. `1/L` has no functional equation.
* Unconditionally, only de la Vallée Poussin-type savings `exp(−c√log X)` are available, uniformly
  only for small conductors. A power saving needs zero-free regions for the same sextic family, which
  is circular.
* The pair phases `(e/d)₃` give a bilinear Type II form. The cubic large sieve handles it *on
  average over `d`* for any coefficients, Möbius included, but at the non-orthogonal strength already
  shown to be insufficient.
* HBP79 and DR24 handle Möbius (via Vaughan) *against Gauss sums*, with Type I from Kubota/theta
  structure. Here the Gauss sum has cancelled (`γ₄ = conj γ₂`), so Type I has none. No automorphic
  interpretation or power-saving bound is known [search negative + INF].

## 7. Is this already in the literature?

The nesting identity is CG10 Prop. 2.1 / (4.3) + (4.5) plus multiplicativity of `(h/·)₂`; at
`h = 1` it is the classical Heath-Brown–Patterson bilinear decomposition. `C_h = Σ_d a(d)χ_d(h)
B^{(2)}_{hd⁴}` is BBCFH06 p. 9 verbatim (`Z = Σ_{c₂} g(1,c₂) D(s₁,c₂) N(c₂)^{-2s₂}`). Related MDS
moment work: FHL03, BFH05, DIPP26. I found no statement that a fourth moment of sextic Möbius sums
is dual to twisted A2 cubic data.

## 8. Verdict

**(c) as proposed.** There is no cubic GL(3) theta with coefficients on our support, and
reflections do not address the dual diagonal.

**(b) if reframed.** The needed new theorem is an unconditional dispersion asymptotic

    Σ_{N h ≤ 𝓗} |Σ_{d,e} H(d,e;h,h)(h/de)₂ N(de)^{-1/2} W W|² = S_diag + secondary + O(L^{2+ε}),   𝓗 = L²/H > L,

or the equivalent off-diagonal statement on the original side. Poisson in `h` makes these two an
exact involution [INF]. The only precedent, for cubic Gauss sums in GL(2), is GRH-conditional (DR24).

## Sources

BBCFH06: Brubaker, Bump, Chinta, Friedberg, Hoffstein, *WMDS I*, PSPM 75 (2006) 91–114.
BBF06: Brubaker, Bump, Friedberg, *WMDS II: the stable case*, Invent. Math. 165 (2006).
BBFH07: Brubaker, Bump, Friedberg, Hoffstein, *WMDS III: Eisenstein series and twisted unstable
A_r*, Ann. of Math. 166 (2007) 293–316. BBF11: *WMDS, Eisenstein series and crystal bases*, Ann.
of Math. 173 (2011); book *Type A Combinatorial Theory*, AMS 175 (not read). CG07: Chinta, Gunnells,
arXiv math/0703040. CG10: *Constructing WMDS*, JAMS 23 (2010) 189–215, arXiv 0803.0691.
BB06b: Brubaker, Bump, *Residues of WMDS associated to GL(n+1)*, PSPM 75. BBFH12: *Coefficients
of the n-fold theta function and WMDS*, Springer PROMS 9 (2012). KP84: Kazhdan, Patterson, Publ.
IHÉS 59. BH86: Bump, Hoffstein, Invent. Math. 84 (1986) 481–505; Duke 53 (1986). Proskurin, Zap.
LOMI 129 (1983). FG15: Friedberg, Ginzburg, JNT 146 (2015), arXiv 1403.3929. CFH12: Chinta,
Friedberg, Hoffstein, *Double Dirichlet series and theta functions*. Gao17: Pacific J. Math. 290,
arXiv 1602.01880. Chen24: arXiv 2411.13143. HB00: Heath-Brown, Israel J. Math. 120 (2000).
HBP79: Heath-Brown, Patterson, Crelle 310 (1979). BY10: Baier, Young, arXiv 0804.2233. BGL14:
Blomer, Goldmakher, Louvel, arXiv 1112.1650. DR24: Dunn, Radziwiłł, Ann. of Math. 200 (2024),
arXiv 2109.07463. Dunn25: ANT 19 (2025) 1823–1880. DdFDS24: arXiv 2410.03048. dFDH26: arXiv
2607.07911. DIPP26: Diaconu, Ion, Paşol, Popa, arXiv 2607.27131. FHL03: Math. Ann. 327 (2003).
BFH05: Invent. Math. 160 (2005). LP02: Livné, Patterson, Invent. Math. 148 (2002). GZ24: arXiv
2201.01885.
