# P. The direct side as a multiple Dirichlet series: identification of Z_η, its functional equations, and what a convexity/Lindelöf bound would buy

Sources: main paper `dl/qrh_main.txt` (Prop. 5.1 lines 1389–1530; probe (6.1)–(6.2) lines 2684–2830), Kintali `dl/kintali_qrh.txt` §3 (lines 429–615), notes C §3(i)/§4.3, I §0, J; literature fetched today (URLs in §6). Labels: **[P]** proven in the literature or in the OpenAI paper, **[H]** heuristic (formal bookkeeping, not checked at the level of correction factors/phases), **[O]** open.

---

## 0. Correction of the set-up: where the quadratic twist actually lives

The direct side, after the separation (6.2) of the main paper, is a *trilinear* form in three ideal variables, not a bilinear form in (s, c):

    I = Q^{-1/2} Σ_σ ∫ Ŵ_0(iv) Σ_{m≠0} Ω(q_m/Q) ξ(m) (q_m/Q)^{-iv} A_{m,σ,v}(Y) B_{m,σ}(Z) dv,     Q = q_{b*}XY,

    A_m = Y^{-1} Σ_{s∈σ, q_s≍Y} w(s) q_s^{-1/2} g_{χ_s}(s,−m)  =  Y^{-1} Σ_{s≍Y} w(s) γ_1(s) χ̄_s(m) 1_{(m,s)=1},
    B_m = ∫ Z^t Φ(t) T(t+½, ν_σθ χ_•(m)) dt  ≈  Σ_{A≍Z} γ_2(c) α(A) η(A) (phases) χ_A(m) q_A^{-1/2}.

Three facts that the "Z_η over s ≍ Y" picture of note C §3(i) got wrong:

1. The Cauchy–Schwarz of the direct bound is over the **≍ Q ≍ Z rows m**, not over the ≍ Y variable s (Kintali §3.3; main paper §6.2 and Prop. 15.2). ‖A‖² ≪ (Q+Y²)/Y is the planar additive large sieve on the Y² fractions d/s, ‖B‖² ≪ Z^{1+ε} is the reflected row energy, and |I| ≪ Q^{-1/2}(Q/Y)^{1/2}Z^{1/2} = Z^{1/4} at X = Y = Z^{1/2}.
2. The moving **quadratic** character after reflection is (µ/R)_2 = χ_R(λ⁴µ)³ with **R = squarefree part of the row m** (Prop. 5.1, item 2: j_p = v_p(m) mod 6 = 1 ↦ B_p = χ_p^{−j_p−2} = χ_p^{−3}), so the quadratic-twist modulus has size ≍ Q ≍ Z, not Y.
3. The s ≍ Y variable does **not** carry a fixed ray phase: g_{χ_s}(s,−m)q_s^{-1/2} = χ̄_s(−m)·γ_1(s) with γ_1(s) the normalised **sextic** Gauss sum (|γ_1| = 1, genuinely oscillating; it is the Patterson-bias-carrying sequence of note J §3). So Σ_s w(s)γ_1(s)χ̄_s(m)q_s^{-s_1} is the m-th Whittaker coefficient of Kubota's Eisenstein series on the **6-fold** cover of GL(2,F), i.e. the sextic Kubota series D_6(s_1; m) = Σ_s g̃_6(s,m)q_s^{-s_1}.

Also, since (m/A)_6 = (m/A)_2·(m/A)_3^{-1} and γ_2(A)(m/A)_3^{-1} = g̃_3(A,m) is the m-th cubic Kubota coefficient, the row B_m is the *cubic Kubota series at frequency m, twisted by the quadratic Kummer character (m/·)_2 and by η* — so "quadratic twists of the cubic theta" do occur on the direct side already before reflection, with the twist variable m.

Hence the honest Dirichlet-series object behind the direct side is the **triple** series

    𝒵(s_1, s_2, s_3) = Σ_{s,m,A} c_σ(s) γ_1(s) χ̄_s(m) · ξ(m) · θ_η(A) χ_A(m) · q_s^{-s_1} q_A^{-s_2} q_m^{-s_3}
                     = Σ_m ξ(m) q_m^{-s_3} · D_6(s_1; m) · D_3^{(2)}(s_2; m),     D_3^{(2)}(s_2; m) := Σ_A g̃_3(A,m)(m/A)_2 η(A)… q_A^{-s_2},

a Rankin–Selberg convolution over the frequency m of a 6-fold-cover Whittaker coefficient with a quadratically twisted 3-fold-cover Whittaker coefficient. With the weights of (6.1) (Mellin variables w_1 for W_1(q_s/Y), w_0 for W_0(q_m/(q_{b*}q_sX)), t for Z^t):

    I = Y^{-1} (2πi)^{-3} ∫∫∫ Ŵ_1(w_1) Ŵ_0(w_0) Φ(t) · Y^{w_1} (q_{b*}X)^{w_0−1/2} Z^{t} · 𝒵(½ + w_1 − w_0, ½ + t, w_0) dw_1 dw_0 dt,

so **the direct side is a vertical-line evaluation of 𝒵 at (Re s_1, Re s_2, Re s_3) = (½, ½, 0)** with prefactor Y^{-1}X^{-1/2}; it needs three Mellin variables, not one. The user's Z_η is obtained from 𝒵 by deleting the s-variable (replacing γ_1(s)χ̄_s(m) by a fixed phase) and renaming m → s: Z_η is the correct model of the *row side* (B) and of the reflected row energy, but not of the pairing with A_m, and it is in the pairing (the Cauchy–Schwarz over m) that the Z^{5/12} is lost. This is the same conclusion as note J §3 (the Gram loss is intrinsic; only the bilinear form can be improved).

I nevertheless analyse Z_η in full below (it is the two-variable building block that any treatment of 𝒵 must contain), and return to 𝒵 in §3–§4.

---

## 1. Identification of Z_η

Definition (squarefree part; the non-squarefree terms are the "correction factors" discussed in §2.4):

    Z_η(s,w) = Σ_{c sf} Σ_s γ_2(c) ᾱ(c) η(c) (c/s)_2 q_c^{-s} q_s^{-w}
             = Σ_c θ_η(c) L(w, ψ_c^{(2)}) q_c^{-s},         ψ_c^{(2)} = (c/·)_2 = (·/c)_2·(fixed phase)   [quadratic Kummer character]
             = Σ_s q_s^{-w} D(s, η χ_s^{(2)}),                D = Kubota/Patterson cubic series, Prop. 5.1 with j_p = 3 for all p | s.

**(a) Rankin–Selberg identification [H, standard shape].** L(w, ψ_c^{(2)}) is, up to the explicit quadratic Gauss-sum phase ε(d) (a fixed ray-class function over Q(ω)), the c-th Fourier coefficient of Kubota's Eisenstein series E^{(2)}(z,w) on the 2-fold cover of GL(2,F): Σ_d g_2(d,c)q_d^{-w'} = Σ_d ε(d)(c/d)_2 q_d^{1/2−w'}. γ_2(c)ᾱ(c)η(c) is the c-th coefficient of the η-twisted Patterson theta function θ_3 ⊗ η (3-fold cover; DR Appendix A, Patterson 1977). Therefore Z_η is the Rankin–Selberg Dirichlet series "L(s, (θ_3⊗η) × E^{(2)}(w))". Automorphically, since Kubota cocycles multiply (κ_3 · κ_2^{-1} has order 6), the integral representation is

    Z_η(s,w) · G(s,w) = ∫^{reg}_{Γ\H³} (θ_3⊗η)(z) · \overline{E^{(2)}(z,w)} · E^{(6)}(z,s) dµ(z),

a *triple-product-type* integral with the integrating kernel a Borel Eisenstein series on the **6-fold** cover (needed to make the integrand Γ-invariant); unfolding E^{(6)} gives the Mellin transform of the constant term of θ_3·\overline{E^{(2)}}, i.e. Σ_c a_θ(c)\overline{b_w(c)} q_c^{-s} times a ratio of Gamma functions G(s,w) (product of two K-Bessel Mellin transforms). Both θ_3 (residual) and E^{(2)} (Eisenstein) are non-cuspidal, so the integral needs Zagier regularisation — exactly the device de Faveri–Dunn–Hoffstein use for θ_3 ⊗ θ̄_3 (arXiv:2607.07911, "adapt a Rankin–Selberg regularization method due to Zagier"). Unfolding the *other* Eisenstein series instead gives Σ_c γ_2(c) · [Σ_d g̃_6(d) η(d)(c/d)̄_6 q_d^{-s}] q_c^{-w'}: the same function has a second representation with sextic Gauss sums and a sextic cross-character — this is the "sextic-twist family" of §2.2 and the two unfoldings *are* the s-functional equation. So: **Z_η is a Rankin–Selberg (triple-product) object on covers of degree 3, 2, 6 of GL(2,Q(ω)), not a Whittaker coefficient of a single higher-rank metaplectic Eisenstein series.** CFH's survey (§2.3.2) lists the obstructions of this route: truncation/regularisation and bad finite primes.

**(b) Is it a Weyl-group MDS?** In the BBFH/Chinta–Gunnells dictionary (degree n, root system Φ, short roots ‖α‖² = 1): diagonal coefficient g(χ^{‖α_i‖²}), cross term (c_i/c_j)_n^{2⟨α_i,α_j⟩}. Z_η needs n = 6, ‖α_c‖² = 2 (cubic Gauss sum g(χ_c²)), ‖α_s‖² ≡ 0 (trivial coefficient), 2⟨α_c,α_s⟩ = 3. The Cartan integer 2⟨α_c,α_s⟩/‖α_c‖² = 3/2 is not an integer: **Z_η is not a classical Weyl-group MDS of any root system/cover.** The closest classical object is the degree-6 **G_2** WMDS (short root ‖α‖²=1 → sextic Gauss sums, long root ‖β‖²=3 → explicit quadratic Gauss sums, 2⟨α,β⟩ = −3 → quadratic cross character): after summing the long-root variable it is Σ_c g̃_6(c) L(w, ψ_c^{(2)}) q_c^{-s} — *sextic* Gauss sums times quadratic L-functions. By the Hasse–Davenport/Jacobi relations of note C §1.1 (γ_1γ_2 = µ·α·(ray phase)·γ_3), Z_η and the G_2-type series are related by a Möbius factor, not by a functional equation (§2.2). [H]

In Sawin–Whitehead's axiomatic framework (arXiv:2507.08662, Axiom 1: cross term Π_{i≤j}(f_i/g_j)_χ^{M_ij}(g_i/f_j)_χ^{M_ij}, M integer mod n, odd entries allowed), Z_η has the formal data **n = 6, M = [[2,3],[3,0]]**: one Kubota-type variable (order-3 Gauss sums) and one Dirichlet-type variable. Whether this (n,M) is in their finite-groupoid list (Heckenberger's rank-2 classification; their §5) I could not check in this session; it is the first thing to verify (§4). Their "Further questions" item 4 states explicitly that twisting by fixed characters (our η) is outside the axioms: "At present, the axioms do not allow for twisting".

**(c) What exists in the literature (none is Z_η).**
- Friedberg–Hoffstein–Lieman, Math. Ann. 327 (2003): Σ_d L(s, ξχ_d^{(n)}) a(s,ξ,d)|d|^{-w} (n-th order twists of a *fixed* Hecke character ξ — so a fixed twist is included) and its partner with n-th order Gauss sums (= Fourier coefficients of E^{(n)} on the n-fold cover of GL(2)); continuation to C² "from Bochner's theorem" (CFH survey §4.1); group of order 32 per the secondary descriptions found today. Same-order twists only. [P]
- Diaconu–Ion–Paşol–Popa arXiv:2607.27131: WMDS family built from twisted Kubota series D^T(s,a,ψ) = Σ_b ψ(b)G(a,b)|b|^{-s} with **ψ^r = 1** (twists of order dividing r only), continuation to C³, finite group of FEs, convexity bounds via BB06; their 4.1.8: the residue of D̂ at s = ½ + 1/r is "an outstanding open problem for r ≥ 4". Their auxiliary series Z_aux = Σ_a D(s_1,a,ψ_1ρ)D(s_2,a,ψ_2ρ)ρ(a)|a|^{-s_3} has exactly the Rankin–Selberg shape of our 𝒵, but with both Kubota series of the same order r; 𝒵 has orders 6 and 3. [P]
- Chinta–Friedberg–Hoffstein, "Double Dirichlet series and theta functions" (Patterson volume): Gauss sums G_j^{(k)}(m,d) "formed with the j-th power of the k-th power residue symbol", on both the n- and 2n-fold covers; FE (2.2), poles at ½ ± 1/k, residue = theta coefficient. This is the only place where the mixed-power structure (k = 6, j ∈ {2,3}) is treated systematically, but only one Dirichlet variable at a time. [P]
- Blomer–Goldmakher–Louvel arXiv:1112.1650: uniform subconvexity for a double Dirichlet series built from central values of n-th order Hecke L-functions (the input is their large sieve) — the one precedent for *subconvexity in w* of an n-th order double series. [P]
- Searches for "quadratic twists of cubic theta", "Eisenstein series double cover cubic theta", "sextic multiple Dirichlet series" returned nothing on a mixed (3,2)-order double series; the sextic literature is on moments of sextic Hecke L-functions and on quartic/sextic twists of elliptic curves.

---

## 2. Heuristic analytic properties of Z_η

### 2.1 The two generating functional equations [H, exponents exact; phases/correction factors not tracked]

Write u = s − ½, v = w − ½.

- **σ_s (Dirichlet type, from L(w, ψ_c^{(2)}), conductor q_c):** L(w,ψ_c) = γ_3(c) q_c^{½−w}(Γ) L(1−w, ψ_c). Since γ_3 (normalised quadratic Gauss sum) is a fixed ray phase, the family is preserved (η ↦ η·γ_3-phase): Z_η(s,w) = Γ_s · Z_{η'}(s+w−½, 1−w). Matrix S = [[1,1],[0,−1]] on (u,v).
- **σ_c (Kubota type, Prop. 5.1 with j_p = 3, conductor q_s² of the quadratic twist of a GL(2)-object):** D(s, ηχ_s³) ≈ q_s^{1−2s} D^∨(1−s), dual coefficient d(µ)α(µ) (conjugate cusp coefficient, class θ̄) twisted by B_p = χ_p^{−j_p−2} = χ_p^{−5} = χ_p: the dual twist is the **sextic** Kummer character (µ/s)_6, so the family changes: Z_η(s,w) = Γ_c · Z^{(sext)}(1−s, w+2s−1) with Z^{(sext)}(s',w') = Σ_s q_s^{-w'} Σ_µ d(µ)α(µ)ϑ(µ)(µ/s)_6 q_µ^{-s'}. Matrix C = [[−1,0],[2,1]].

SC = [[1,1],[−2,−1]] has trace 0, det 1, so (SC)⁴ = 1 and ⟨S,C⟩ ≅ **D_4 = W(B_2), order 8**, with (SC)² = −1: (s,w) ↦ (1−s, 1−w). (For comparison the FHL/Goldfeld–Hoffstein quadratic series has C' = [[−1,0],[1,1]], SC' of order 3, W(A_2).) The B_2 shape is forced by the conductor exponent 2 of the twisted GL(2) object versus 1 for the L-function. Mirrors: u = 0, v = 0, v = −u, v = −2u; the positive quadrant {Re s > 1, Re w > 1} is a chamber.

### 2.2 The orbit of coefficient classes and the appearance of Möbius [H]

Use note I §0's algebra: classes θ^k (θ = ᾱγ_2, θ³ = µ mod ray phases and α-powers), with γ_a ~ θ^{3−a} (γ_1 ~ µθ̄, γ_2 ~ θ, γ_3 ~ 1, γ_4 ~ θ̄, γ_5 ~ µθ, Ramanujan ~ µ). Label a family by (k, b): coefficient θ^k in c, L(w, χ_c^b) in the other variable. Then σ_s: (k,b) ↦ (k+3−b, −b); σ_c: (1,b) ↦ (5, −b−2), (5,b) ↦ (1, −b+2) (Prop. 5.1 and its conjugate). Starting from Z_η = (1,3):

    (1,3) —σ_s→ (1,3)  [self-dual]
    (1,3) —σ_c→ (5,1) —σ_s→ (1,5) —σ_c→ (5,5) —σ_s→ (3,1) = Σ_c µ(c)L(w,χ_c)q_c^{-s} = Σ_s q_s^{-w} / L(s, ψ_s^{(6)}·phase).

So three theta-type families (quadratic-twisted θ; sextic-twisted θ (= the paper's *row* class (1,1)/(5,5), which is where Prop. 5.1's mechanism (C) "sextic → quadratic" lives); and their conjugates) and, four reflections away, the **Möbius/inverse-L family**, which is the Poisson-side object of the paper (F_{η,u} ∝ 1/L(x, ηψ_u)). The identity "direct = Poisson" of the paper is the σ_m-image (Dirichlet FE in the row variable m, root number γ_1, γ_1γ_2 ∝ µ) of the triple series 𝒵; the direct bound is a bound at (½,½,0) and the Poisson side is the same function read at the σ_m-image point.

**A bookkeeping inconsistency that is informative.** The two words SCSC and CSCS both equal −1 on (u,v), but the naive squarefree class-tracking gives (3,1) for one and (5,5) for the other at the same point −x. Since Σ_c µ(c)L(w,χ_c)q_c^{-s} and Σ_c θ̄(c)L(w,χ̄_c)q_c^{-s} are different functions, the squarefree-supported bookkeeping cannot be the whole story: the **non-squarefree correction factors and the scattering-matrix mixing of ray classes must reconcile the two chains**, and whether consistent corrections exist is exactly the question "is (6, [[2,3],[3,0]]) an axiomatic MDS with finite groupoid?" (SW's classification). I flag this as unresolved; it is part of the open lemma in §4.

### 2.3 Continuation to C² via Bochner [H → conditional P]

Regions of absolute convergence/holomorphy with polynomial growth: R_0 = {Re s > 1, Re w > 1}; by one-variable convexity, R_1 = R_0 ∪ {|v| ≤ ½, u > ¾ − v/2} ∪ SR_0 (Dirichlet direction: |L(w,ψ_c)| ≪ q_c^{(1−Re w)/2+ε}) and R_2 = R_0 ∪ {|u| ≤ ½, v > ½ − u} ∪ CR_0 (Kubota direction: |T(s,Ψ_s)| ≪ (q_s²)^{(1−Re s)/2+ε}, which is the convexity bound for the entire function T of Prop. 5.1 — its "polynomial growth" clause). The images g(R_1 ∪ R_2) for the **seven** non-Möbius chamber elements of D_4 form a connected tube whose base covers all directions except the open sector 180°–270°; its convex hull is already all of R². Hence **Bochner's tube theorem gives meromorphic continuation of Z_η to C² without ever using the Möbius family**, provided the three theta-type families have the needed uniform (in the twist modulus) continuation and growth — i.e. provided (i) Prop. 5.1 holds with growth constants uniform in the moving primes P (the identity (5.1) is exact; the paper's growth clause allows constants depending on P, which must be made explicit — the Rankin–Selberg representation of §1(a) would give this automatically), and (ii) the correction factors of §2.2 exist. The Möbius representation Z_η(x) = (Γ)·𝓕_{(3,1)}(−x) then becomes a *consequence* on −R_0 (an absolutely convergent series there), with no contradiction from the dense poles of 1/L: those live outside −R_0, where Z_η is given by the other representations.

### 2.4 Polar divisor [H]

The only pole of the squarefree series is the c = 1 term η(1)ζ_F(w) (c squarefree ⇒ ψ_c nonprincipal for c ≠ 1); with ᾱ built in, T(s,Ψ) is entire (Prop. 5.1), so no Patterson pole at s = 5/6 in the c-variable. The D_4-orbit of {w = 1} consists of four lines:

    w = 1,   w = 0,   w + 2s = 2,   w + 2s = 1.

(The line v + 2u = ½ is S-stable.) On the direct line Re s = ½ these pass through w = 1 and w = 0 (double poles there). Residues are "principal-row" type: at w = 1 the c = 1 term, which in the smoothed probe carries V(1/Z) ≈ 0; at w = 0 its σ_s-dual. Nothing of size Z^{C(β*)} appears in Z_η's residues — consistent with §0: the 1/L main term of the paper comes from the σ_m-FE of 𝒵 in the row variable, which Z_η has deleted.

### 2.5 Convexity bound and the meaning of "evaluating on a line" [H]

Z_η contains no Y or Z. In the model J_mod = Σ_{s≍Y} φ(s) W_1(q_s/Y) Σ_{c≍Z} θ_η(c)(c/s)_2 q_c^{-½} V(q_c/Z) = (2πi)^{-2}∫∫ Ŵ_1(w) V̂(s') Y^w Z^{s'} Z_η(½+s', w), the contour sits at (Re s, Re w) = (½, 0) — the left edge of the w-strip and the centre of the s-strip — and the size of J_mod is governed by the contour positions one may shift to and by the residues crossed, not by a "value" of Z_η. Shifting w left of 0 crosses the double pole at w = 0 (residue of size Y⁰·Z^{s'}-weight) and the remaining integral is ≪ Y^{−A}·sup|Z_η|; so **if Z_η continues to C² with polynomial growth, the model sum is O(Z^ε) uniformly in Y** — which is correct: at Y = Z^{1/2} the smoothed s-sum Σ_s (c/s)_2 W_1(q_s/Y) is a *complete* character sum (smoothed Pólya–Vinogradov, length ≥ conductor^{1/2}), of size O(1) per c, and the model's "Cauchy–Schwarz diagonal Y^{1/2}" was never the right trivial bound for it. This confirms §0: the Y^{1/2}·Z^{…} loss of the actual direct bound is not visible in Z_η; it is a statement about 𝒵 at (½,½,0).

For 𝒵 itself the direct-line position is (Re s_1, Re s_2, Re s_3) = (½, ½, 0) with prefactor Y^{-1}X^{-1/2}. Shifting the s-variable (w_1 ↦ w_1 − δ, gain Y^{−δ}) moves s_1 to ½ − δ, where the sextic Kubota series at frequency m has conductor q_m ≍ Q = XY and costs Q^{δ} (CFH (2.2): D̃(s,m) ≈ Nm^{½−s}D̃(1−s,m)): net X^{δ} ≥ 1, a loss. Shifting the row variable s_3 ↦ −δ gains (XY)^{−δ} and costs the conductor of L(s_3, ξχ̄_sχ_A), which is q_sq_A ≍ YZ: net (Z/X)^{δ}, a loss for X < Z. So **no single-variable contour shift of 𝒵 beats the direct bound; any gain must come from a genuinely two-variable (subconvex) estimate in the (m, s) or (m, A) directions**, i.e. from off-diagonal cancellation in the bilinear form Σ_m ξ(m)A_mB_m that Cauchy–Schwarz discards.

---

## 3. Quantification: what a saving over the diagonal would give

Exponent bookkeeping (note C §1.3, Kintali §3.3): Part I has C(s) = s − 2/3, direct bound Z^{1/4}, truth under RH Z^{−1/6}; the contradiction needs Z^{β*−2/3} ≤ direct bound. With Y = Z^{l_y}, l_y = ½:

- A saving Y^{−κ'} over the Cauchy–Schwarz step gives |J| ≪ Z^{1/4 − κ' l_y} and **σ_0 = 2/3 + 1/4 − κ'/2 = 11/12 − κ'/2**. Range: κ' ∈ [0, 5/6]; κ' = 5/6 (direct bound = RH truth) gives σ_0 = ½.
- Part II (Liu's B(ℓ) = 11/12 − ℓ/4 at the Gram loss θ = 1/12): the same saving enters the low bound |J| ≪ Z^{l_x/2 + b/12 − κ' l_y} and re-optimisation moves B by roughly −κ'·l_y·(dB/d(low exponent)) ≈ −κ'/2 as well (note J §5 shows B is linear in the low exponent with slope ≈ 1 over the active range), so **B_II ≈ 0.875 − κ'/2** until the floor/class constraints of note J §5 bind (≈ 0.864 at θ = 0, i.e. the Gram-side part of the loss is at most 0.011; the rest of a hypothetical κ' acts on the bilinear part).
- "Convexity bound with w-conductor exponent A": for the row energy (Z_η-side) convexity already gives Lindelöf-on-average (Σ_m|B_m|² ≪ Z^{1+ε}) because rows ≍ columns; so a *convexity* bound in w for Z_η reproduces κ' = 0 — it is exactly what the quadratic large sieve already delivers. **κ' > 0 requires subconvexity for 𝒵 in the row aspect**, not convexity for Z_η.
- A Lindelöf-type bound for 𝒵 on the direct line (|𝒵| ≪ (conductors)^{ε}, i.e. square-root cancellation in all three variables simultaneously) would give the RH-strength bound |J| ≪ Z^{−1/6+ε}, κ' = 5/6, σ_0 = ½ — this is just RH for the probe in disguise and cannot be the target. The realistic target is half the gap: κ' ≈ 5/12 (σ_0 ≈ 0.71) is already "Weyl-strength" subconvexity for a triple series; κ' = l_y/4 = 1/8 (σ_0 = 11/12 − 1/16 ≈ 0.854, matching C §3(i)'s guess ≈ 0.79 only if l_y is re-optimised upwards) is the Burgess-type benchmark.
- Mean value / second moment in w over a short range: a bound Σ_{|t|≤T} |Z_η(½, it)|² or, better, ∫ |𝒵(½+it_1, ½, it_3)|² over |t_i| ≤ T with the *large-sieve diagonal only* (no off-diagonal) is what Cauchy–Schwarz + large sieve already encodes; a second-moment bound beats Cauchy–Schwarz only if it is applied to the bilinear form with a *weight that separates A from B* — but note J §3 shows the Gram operator of A has the probe's own coefficient as a top eigenvector, so no weighted second moment helps there. **Verdict: a mean-value bound in w of Z_η does not beat Cauchy–Schwarz; only an estimate of the trilinear form with genuine off-diagonal cancellation does.**

---

## 4. Deliverables

**Definition and identification.** Z_η(s,w) = Σ_c θ_η(c) L(w, ψ_c^{(2)}) q_c^{-s} = Rankin–Selberg series of (θ_3⊗η) × E^{(2)}(w), representable as a Zagier-regularised triple integral against a 6-fold-cover Borel Eisenstein series; not a classical WMDS (Cartan entry 3/2); formally an axiomatic MDS with (n,M) = (6,[[2,3],[3,0]]) whose finiteness/correction factors are unverified; η-twist outside Sawin–Whitehead's axioms. The actual direct side is the triple series 𝒵 of §0 (6-fold × quadratically-twisted 3-fold Whittaker coefficients convolved over the row m), evaluated at (½,½,0).

**Conjectural analytic properties.** [H] D_4 = W(B_2) group of 8 FEs in (s,w), generated by the quadratic-L FE and Prop. 5.1; three theta-type families plus the Möbius/inverse-L family in the orbit; polar divisor = four lines w ∈ {0,1}, w + 2s ∈ {1,2}; continuation to C² by Bochner using only the seven non-Möbius chambers. [P inputs] Prop. 5.1 (identity exact; growth constants depend on P), BB06/Kubota continuation of twisted Kubota series (DIPP 4.1.4, for twists of order dividing r — our quadratic twist of the cubic series is covered instead by Prop. 5.1/DR Appendix A), FHL03 continuation of same-order double series via Bochner, DFDH's regularised Rankin–Selberg for metaplectic theta functions. [O] uniformity in the modulus, correction factors reconciling the two length-4 chains, polynomial growth on the Bochner hull.

**Predicted boundary.** Convexity in w for Z_η: no change (0.875 / 11/12 Part I), because convexity = quadratic large sieve here. Subconvexity for 𝒵 in the row aspect with saving Y^{−κ'}: σ_0 = 11/12 − κ'/2 (Part I), B_II ≈ 0.875 − κ'/2. Lindelöf for 𝒵 on the direct line: σ_0 = ½ (equivalent to RH-strength control of the probe; not a target).

**Single most concrete open lemma.** *Existence lemma for the mixed-order double series.* Determine the correction factors (non-squarefree coefficients, including the b³-completion L_0(s,Ψ) = L(3s−½, ᾱ³η³ψ_s^{(2)}) forced by Prop. 5.1 and the b²-structure forced by E^{(2)}) such that the completed Z_η satisfies **both** σ_s and σ_c exactly, and check that (6,[[2,3],[3,0]]) is in Sawin–Whitehead's finite list; equivalently, prove via the regularised triple integral that Z_η continues to C² with polynomial growth on vertical strips and the four polar lines of §2.4. Independent of any application, this would be the first continued double Dirichlet series mixing Gauss sums of one order with characters of another.

**Feasibility.** The existence lemma is a bounded, realistic project (tools: Prop. 5.1/DR Appendix A, Kubota's E^{(2)} over Q(ω), Zagier regularisation as in DFDH, SW's classification), comparable to FHL03 in difficulty. What it buys for the 7/8 problem is, however, **nothing by itself** (§2.5, §3): the loss sits in the pairing with the 6-fold-cover coefficient A_m, i.e. in the triple series 𝒵, for which one needs a subconvex bound in a two-variable direction — an object with no precedent (DIPP's Z_aux is the same-order analogue and they obtain only convexity-type bounds, 7.2.2). I rate: existence lemma for Z_η — likely true and provable in months; continuation of 𝒵 — plausible by the same Rankin–Selberg technology with E^{(6)} × E^{(3)}-type kernels but with the 6-fold cover's unknown residues (DIPP 4.1.8) as a complication for its polar divisor; **subconvexity for 𝒵 beating the large-sieve diagonal — open with no known mechanism**, and note J's eigenvector argument shows the needed cancellation is not of Gram/large-sieve type.

**Weaker provable version.** A second moment of Z_η in w over a short range, or a second moment of 𝒵 in any single variable, reproduces the large-sieve bound and does not beat Cauchy–Schwarz. The only weaker statement with content is a *bias-subtracted* mean value: subtract the Patterson-bias component of A_m (the 6-fold-cover residue direction, size Y^{−1/6}τ(m), note J §6.2) and prove square-root cancellation for the remainder against B_m; that is the slot-prime-in-s idea of note J §6.1 in MDS language (it twists the s-variable of 𝒵 by a character η(p) that kills the fixed-modulus phases), ceiling ≈ 0.864–0.867 per note J §5.

---

## 5. Summary (≤350 words)

The OpenAI direct side is a trilinear form over (s ≍ Y, m ≍ XY, A ≍ Z) with Cauchy–Schwarz taken over the rows m; the moving quadratic character after reflection has modulus sf(m) ≍ Z, and the s-variable carries sextic Gauss sums γ_1(s)χ̄_s(m), i.e. it is the m-th Whittaker coefficient of Kubota's Eisenstein series on the 6-fold cover. The right Dirichlet-series object is therefore the triple series 𝒵(s_1,s_2,s_3) = Σ_m ξ(m)q_m^{−s_3}·D_6(s_1;m)·D_3^{(2)}(s_2;m), evaluated at (½,½,0) with prefactor Y^{−1}X^{−1/2}; the proposed Z_η = Σ_c θ_η(c)L(w,ψ_c^{(2)})q_c^{−s} models only the row side.

Z_η is identified as the Rankin–Selberg series of Patterson's cubic theta (3-fold cover) with Kubota's quadratic Eisenstein series (2-fold cover), realisable as a Zagier-regularised triple integral against a 6-fold-cover Eisenstein series (DFDH's technique, arXiv:2607.07911). It is not a classical Weyl-group MDS (Cartan entry 3/2); formally it is a Sawin–Whitehead axiomatic MDS with (n,M) = (6,[[2,3],[3,0]]), twisting by η being outside their axioms (arXiv:2507.08662, open question 4). Nothing in the literature treats a Gauss-sum-of-order-3 × character-of-order-2 double series: FHL03 (same-order twists, Bochner continuation), DIPP arXiv:2607.27131 (twisted Kubota series with ψ^r = 1; residues unknown for r ≥ 4), CFH's Patterson-volume survey (mixed powers G_j^{(k)}, one variable) are the nearest.

Heuristically: two FEs — the quadratic-L FE (s,w)↦(s+w−½,1−w) and Prop. 5.1 (s,w)↦(1−s,w+2s−1) — generate W(B_2) of order 8; polar lines w∈{0,1}, w+2s∈{1,2}; Bochner continuation to C² using only the seven theta-type chambers; the eighth chamber is the Möbius/inverse-L family (the Poisson side). A squarefree class-bookkeeping inconsistency between SCSC and CSCS shows the correction factors are essential and unverified — this is the concrete open lemma.

Quantitatively: convexity (or any w-mean value) for Z_η reproduces the quadratic large sieve, κ' = 0, no change to 7/8 or 11/12. A row-aspect saving Y^{−κ'} for 𝒵 gives σ_0 = 11/12 − κ'/2 (Part I) and B_II ≈ 0.875 − κ'/2; Lindelöf for 𝒵 would give ½ and is RH in disguise. No single-variable contour shift of 𝒵 gains; the needed object is a genuinely two-variable subconvex bound for a mixed-cover triple series, with no known mechanism.

URLs: https://chinta.ccny.cuny.edu/publ/cfh2.pdf ; https://chinta.ccny.cuny.edu/publ/patterson.pdf ; https://arxiv.org/abs/2507.08662 ; https://arxiv.org/abs/2607.27131 ; https://arxiv.org/abs/2607.07911 ; https://link.springer.com/article/10.1007/s00208-003-0455-4 ; https://arxiv.org/abs/1112.1650 ; https://arxiv.org/pdf/0803.0691 ; https://arxiv.org/abs/2109.07463
