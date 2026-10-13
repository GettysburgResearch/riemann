# A. Exponent model of the 7/8 (and Liu 0.874957) argument — reconstruction, sensitivity, barrier

Script: `scratchpad/scripts/exponent_model.py` (`python3 exponent_model.py check|sens|best`). Logs: `scripts/log_check.txt`, `log_sens2.txt`, `log_best2.txt`.
Sources: main paper Secs 15, 19, 20 (eqs (19.2)-(19.7), (20.4), (20.6)-(20.11)); Liu Secs 15-26 (eqs (15.2)-(15.3), (18.2)-(18.5), (22.2)-(22.5), (23.1), (24.1), (25.1)-(25.3), Lemma 19.2).

## 1. The constraint system (all exponents base Z)

Free parameters: b = ly − lx > 0, ℓ = total selected prime length. Balanced scales (Liu 15.2): lx = (1−b−ℓ)/2, ly = (1+b−ℓ)/2, h = 1−lx+ℓ = (1+b+3ℓ)/2.
Fixed inputs ("dials"): α = 5/6 (Lemma 17.6 slope), plain capacity zP(m) = c_κ(1−2m) with c_κ = 1/(6κ) = 2/9 (Lemma 18.1, κ = 3/4), inverse capacity zM(r) = c_M(1−r), c_M = 1/2 (Lemma 17.1: r+2z ≤ 1, 2r+8z ≤ 3), Gram loss θ = 1/12 (low bound lx/2 + θ b, from the P_a^{1/6} term of Prop 15.2 with P_a = Z^b), z0 = 17/50, floor a0 = 51/100 (δ0 = 1/50), supply 7/37, dmin = 1/100.

* Signal exponent C(s) = s − 5/6 + lx/3 + ℓ/6 (Liu 22.1) = s − (4+b)/6 on balanced scales.
* Direct bound (Liu Prop 22.2): Llow = lx/2 + max{0, θb, b − ly/2} + k(M,ℓ)/2, k = max{0, (1+3ℓ−2M)/4, M+ℓ−1, (3ℓ−1)/2}, M = 1−ℓ. Matching C(B) = Llow gives
  **B_low = 11/12 − ℓ/4 + b(θ − 1/12) + (8b+3ℓ−3)₊/12 + (5ℓ−1)₊/8.**
* Nonprincipal row class (U = Z^d, δ = 2a−1, x = ḡ/δ ∈ [0,1/2], count exponent R), Liu (18.4)/main (20.4):
  **E0(d) = a + h(z0−1/6) − a·ly − ℓ/2 + xδℓ + d(R + δ/2 − z0)**, constraint B ≥ E0(d). z0 cancels at d = h. Slope R+δ/2−z0 > 0, so d = h is extremal on [1/2, h].
* Count exponent with selected primes (Prop 19.2 / Liu 18.1, 23.1): detector t ∈ [1,3/2], witnesses r ∈ [t−1/2, 1], m = t−r ≤ 1/2;
  FI(r) = r + 2x·min(c_M(1−r), ℓ/d), FS(r) = 2m + 2x·min(c_κ(1−2m), ℓ/d); Rshort(t) = 1 − δ·min_r max(FI,FS); long witnesses (r ≥ 1): L(t) = 1−α+(α−δ)·max(1,t)[r=t worst if α ≥ δ]; R*(δ,x) = min_t max(Rshort, L). Uncapped closed form (Liu 18.2): R* = 1−δ+(α−δ)δP_x/(2J), D_x = 3−17x/9, P_x = (2−8x/9)(1−x), J = (α−δ)D_x+δP_x; r*(t) = ((2−8x/9)t−5x/9)/D_x, t* = 1+δP_x/(2J). Model reproduces the closed form to 3e-16 (cap ℓ/h never binds at the paper's parameters).
* Floor class (a0, no witness, R = 1, ḡ ≤ δ0/2): B ≥ E0(h) = 2/3 + b/6 + ℓ + δ0(1/2+3ℓ/2) (= −1/4+b/6+5ℓ/4+... in Liu's normalisation).
* Intermediate rows dmin ≤ d ≤ 1/2, no primes, R = 76/75 − 2δ/3, x = 1/2: B ≥ E0(1/2) (affine in δ; endpoints δ0, 5/6).
* Small rows: ly/2 − h(z0−1/6) − 2dmin > 0 (relative to C(β*), independent of B). Supply ℓ/h > 7/37; lx > ℓ, ly > ℓ, 1−3ℓ > 0, b > 0.
* Principal Euler domain (Liu Lemma 17.1) verified for B ≥ 437/500; the actual convergence exponents need only 4−6B−6(33/200) < −1, i.e. B > 0.668, so not structural.

Achievable boundary: B(b,ℓ) = max{B_low, max_{δ,x} E0(h; R*), E0_floor, E0_int}, minimised over (b,ℓ).

## 2. Verification
* (i) b = 1/8, ℓ = 1/6: lx = 17/48, ly = 23/48, h = 13/16, B_low = 7/8, floor E = −7/1200, E(1/2) ≤ −49/14400, small-row margin 63/800, supply 8/39: all reproduced exactly. Endpoint: min over [0,5/6]×[0,1/2] of −E* = **2.282e−4** at (δ,x) = (79/204, 1/2). The paper's certificate value 49/440640 = 1.112e−4 is the *weakened* bound (uses J ≤ 5/2 in 49/(176256 J)); at the true J ≈ 1.218 the paper's identity (20.9) gives 2.28e−4, matching the model. So the certificate is reproduced, and its stated constant has a factor-2 slack by design.
* (ii) Optimising (b,ℓ): **B = 0.874957069** at b = 0.1232, ℓ = 0.166838; Liu's B_new = 0.874957069799 reproduced to 7e−10 (b is flat at optimum: ∂_b E = 0 at the critical class, Liu's b_new = 0.1234 is fixed by a stationarity condition). Active constraints: B_low = Hmod, tight class **(δ,x) = (δ_c, 1/2) = (0.38858, 1/2)**, where R*(δ_c,1/2) = 2/3 exactly (Liu 24.1). Floor and intermediate constraints are slack (0.8691, 0.8723). Structure: B_new = (7+18δ_c)/(9+18δ_c).

## 3. Sensitivity (each dial moved alone, (b,ℓ) re-optimised; derivative at current point)

| dial | current | hypothetical | B | dB/d(dial) | new active |
|---|---|---|---|---|---|
| α (Lemma 17.6 slope e(r)=1−α+αr) | 5/6 | 1 (trivial large sieve) | 0.876526 (worse) | +0.0047 | low, floor, int |
| | | 2/3 | 0.873916 | | low, class (0.381, ½) |
| | | 1/2 | 0.872227 | | low, class (0.31, ½), b→0 |
| | | 0 (Lindelöf on average) | 0.869792 | | low, floor (b=0, ℓ=3/16) |
| c_κ = 1/(6κ) (Lemma 18.1, 2m+6κz ≤ 1) | 2/9 | 1/4.2 (κ=0.7) | 0.874925 | −0.0020 | low, class |
| | | 1/3 (κ=1/2) | 0.874708 | | |
| | | 1 (2m+z ≤ 1, Lindelöf) | 0.874052 | | low, class (0.245, 0), int |
| c_M (Lemma 17.1, r+2z ≤ 1) | 1/2 | 3/4 or 1 | 0.874052 | −0.0096 | cap ℓ/h binds; int active |
| θ (Gram loss b/12) | 1/12 | 1/24 | 0.869608 | **+0.100** | low, floor |
| | | 0 | **0.863950** | | low, floor (b=0.169, ℓ=0.154) |
| z0 | 17/50 | 0.30, 0.25 | 0.874957 | 0 | (cancels at d=h) |
| a0 (floor) | 51/100 | 0.505, 0.5 | 0.874957 | 0 | floor slack |
| supply | 7/37 | 0.15, 0.10 | 0.874957 | 0 | slack |
| sextic large sieve (Lemma 9.1) | — | — | no effect | 0 | only enters Stage 1 (11/12) and the no-prime count 1−2δ/3 is already moment-based |

Note on α: "α = 1" is the *trivial* large-sieve mean square (Σ|M_u(U^r)|² ≪ U^r), which is worse than the sixth-power amplification 1/6+5r/6 for r>1; the ideal direction is α → 0 (Lindelöf-on-average for long inverse polynomials). α = 1−1/k for a k-th-power amplifier; k = 6 is forced by the sextic symbol; alternatively extending Lemma 17.1 to polynomials of length D ≤ H^γ gives α = 5/(6γ).

**Most valuable single lemma: the additive/Gram mean square (Prop 15.2), i.e. the P_a^{1/6} term.** dB/dθ ≈ 0.10 is 10–50× any count dial; θ = 0 gives 0.86395, more than all count dials combined (0.8698). Among the count lemmas, c_M (inverse capacity) has the largest slope but is quickly capped by the prime supply ℓ/h; α is next.

## 4. Where "3/4" comes from, and the real floor of the architecture
* Formal origin: B(ℓ) = 11/12 − ℓ/4 (Liu 0.1) equals 3/4 at ℓ = 2/3 (lx = ly = 1/6 at b=0). Equivalently B = 5/6 + (lx−ℓ)/6 + θb: the constant 5/6 is the Mellin shift (pole of ζ_F(6z) at z = 1/6, Gaussian e^{(s−5/6)²}); 3/4 needs ℓ − lx = 1/2.
* What forbids ℓ → 2/3 (model, b→0): (a) **floor rows**: on balanced scales with δ→0, R=1 the raw floor-row exponent is exactly ℓ while the signal is lx/2+b/12 = C_b(B); so ℓ ≤ lx/2 + b/12 ⇔ ℓ ≤ 1/5 − 2b/15 ⇒ B ≥ 13/15 + b/30 even with perfect counts. At ℓ = 2/3 the floor excess is +0.61. (b) reflected majorant (Liu 22.5): (5ℓ−1)₊/8 makes B_low increase for ℓ > 1/5 (B_low(2/3) = 1.04). (c) lx > ℓ fails for ℓ > 1/3 (direct bound hypotheses). (d) h = (1+b+3ℓ)/2 enters E0 with coefficient (1−R) ≥ 0, so ∂_ℓE0 = 5/4 + δ(1+x) − 3(1−R)/2 ≥ 5/4 − δ/2 > 0 always. The supply 7/37 and the moment capacities are *not* what stops ℓ (ℓ/h increases with ℓ).
* Other places a literal 3/4 appears: κ ≥ 3/4 in Lemma 18.1 (κ = 2β*−1 ≥ 3/4 ⇔ β* ≥ 7/8, so 7/8 is exactly the κ=3/4 threshold; Liu fixes κ=3/4 using the proved 7/8); the principal residue error exponent 3−5s ≤ −B ⇔ B ≥ 3/4 (cosmetic, only o(1) is needed); under Lindelöf the Halász–Turán density is T^ε for σ > 3/4. None of these is the binding mechanism.
* Infimum under the best conceivable inputs (model, cumulative): counts ideal (α=0, c_M=c_κ=1): 0.869792 (b=0, ℓ=3/16, floor active); + floor a0→1/2: **13/15 = 0.8667** (ℓ = 1/5); θ=0 alone: 0.86395; θ=0 + ideal counts: 0.86395; + a0→1/2: 0.859848; + no supply: **6/7 = 0.857143** at (b,ℓ) = (2/7, 1/7), pinned by B_low = 11/12−ℓ/4−b/12, floor B ≥ 2/3+b/6+ℓ, and the second Gram term b ≤ ly/2 (P_a²/Y' ≤ 1); dropping also the Gram second term and reflected penalty gives the degenerate 5/6 (b→1, ℓ→0, X=1).
* **Pinning feature**: the floor-row cost Z^ℓ (U=Z^h rows × square-root-size prime sums Z^{ℓ/2}, squared) versus the signal Z^{lx/2+b/12} coming from the cubic Gauss sum size q_c^{1/2} in the theta mean square (Lemma 15.1 gives Z^{M'} with M' = lx+ly), together with the 5/6 shift. Nothing in the count machinery can go below the trivial floor count, so with this architecture B ≥ 5/6 strictly (lx > ℓ, θ ≥ 0), realistically ≥ 6/7. 3/4 is not attainable by any improvement of the moment lemmas; it would require changing the signal normalisation (the 5/6 shift / the sextic family) or beating the trivial floor count.

Uncertainties: (1) the intermediate-row range uses the paper's loosened R = 76/75 − 2δ/3 and no primes (mesh restriction d ≥ 1/2); I did not model relaxing it, and it becomes active once c_M or c_κ improve (0.874052 rows). (2) The claim that long witnesses with α < δ are worst at r = 1 is my inference (not in the paper, which only needs α = 5/6 ≥ δ). (3) The Gram exponent 1/6 of P_a (origin in the complete cubic correlations of Prop 15.2) — I did not trace which sub-estimate produces exactly 1/6, so "θ = 0" is a conjectural target, not a known obstruction level. (4) Lemma 17.1 principal domain for B < 437/500 would need re-verification (expected harmless).

## 5. Stones unturned (lemma → predicted B)
1. **Gram bound without the P_a^{1/6} term** (Prop 15.2 with Σ_m|A_m|² ≪ (Q/Y')(1 + P_a²/Y')Z^ε): B → 0.86395 now; 6/7 with everything else ideal. Even halving the exponent (P_a^{1/12}): 0.869608.
2. **Inverse moment with r + z ≤ 1** (Lemma 17.1, c_M = 1): B → 0.874052; the cap ℓ/h then binds, so pair it with
3. **Selected-prime counts on d < 1/2** (remove the mesh restriction in Lemma 18.1 so Prop 19.2 applies for dmin ≤ d ≤ 1/2): removes the Hint constraint active at 0.874052 (unquantified here, ≤ 0.0004 further).
4. **Plain fourth moment with 2m + 2z ≤ 1** (Lemma 18.1, c_κ = 1): 0.874052 (with κ merely lowered to 1/2: 0.874708).
5. **Longer inverse polynomials in Lemma 17.1** (D ≤ H^γ instead of H^{1−c}), equivalently α = 5/(6γ): γ = 5/4 → 0.873916; γ = 5/3 → 0.872227; Lindelöf-on-average (α=0) → 0.869792.
6. **Detector down to a = 1/2+ε** (a0 → 1/2): no gain alone; with ideal counts 0.8698 → 13/15, with θ=0 0.86395 → 0.85985.
