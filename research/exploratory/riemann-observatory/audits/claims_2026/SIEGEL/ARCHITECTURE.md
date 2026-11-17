# CLAIM SIEGEL: no Landau–Siegel zeros, (1−β) log q ≥ c for every primitive real χ

```text
Status: architecture map plus audit (exploration layer). This is not an integrated or reviewed packet.
        We found no verified error. We did not replay any Lean formalization.
Scope:  the claim "there is an absolute c>0 with (1-beta) log q >= c for every real zero beta in (0,1) of
        every primitive real Dirichlet L-function of conductor q>=3" (a logarithmic real-zero gap; it is
        not GRH and not a zero-free half-plane).
Exact sources or dependencies:
  [OAI]   OpenAI, "Uniform exclusion of Landau–Siegel zeros", Oct 1 2026, openai/math repo
          preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/ at repo HEAD 4eaee875;
          paper.pdf sha256 fab9f6e8...14ef, build/paper.tex sha256 b011ba9c...ded4 (line numbers below
          refer to paper.tex; result numbers follow the PDF: Thm 1, Lem 2, Lem 3, Cor 4, Rem 5, Lem 6, Lem 7).
  [Banks] W. D. Banks, arXiv:2610.15483v1 (Oct 11 2026), PDF sha256 54891704...6d7f.
  [Kerr]  B. Kerr, arXiv:2610.21099v1 (Oct 15 2026), PDF sha256 30dc40c9...6116.
  [Guo]   V. Z. Guo, arXiv:2610.30476v1 (Oct 21 2026), PDF sha256 f3058ae2...e47a7e.
  Secondary sources, read only for the cited statements: Masser, Invent. Math. 63 (1981) 81-95,
  Thm 1 (read from the GDZ scan, pp. 81-82); Lu-Zaman-Zhao arXiv:2602.03626, Thm 1.1;
  Kimura arXiv:2610.21511v2 (abstract, Lemma 8, Prop 9, Table 1).
What was actually run: line-by-line reading of all four proofs; exact toy replays of the OAI
  divisibility lemma and of Guo's injectivity and divisibility; recomputation of every stated constant
  and rational certificate; numerical sanity checks of the unconditional inert-prime bound and of
  class-number consequences. The scripts are in architecture_checks/ and are our own code. They are run
  with `python3 -I`. Nothing from other repositories was executed.
Smallest remaining gap: independent expert review of OAI Lemma 3 + Lemma 7 (or Guo Prop. 3.1). We
  re-derived every step and found no gap. The Lean development (69,818 lines,
  lean/OAI/NumberTheory/SiegelZeros) and the Lu-Zaman-Zhao computation (used only for Banks's
  all-q constant) were not replayed.
```

---

## 1. Exact main theorems (statements and locations)

| Source | Statement | Location |
|---|---|---|
| OAI | **Theorem 1.** There is an absolute constant c>0 such that every real zero β∈(0,1) of every primitive nonprincipal real Dirichlet L-function of conductor q≥3 satisfies (1−β) log q ≥ c. No value of c is given. The proof is by contradiction along a sequence, and bounded conductors are handled by finiteness and analyticity. | paper.tex l.66–73; proof §6 l.663–719 |
| Banks | **Theorem 1.1.** There are absolute q0≥9 and δ0>0 with (1−β) log q ≥ δ0 for all q≥q0. **One can take q0=10^10 and δ0=3.0×10^−3**, and exactly δ0 = 81/(5888 e^{3/2}) = 3.0696×10^−3 (Remark 7.1). For all q≥3, c=3.0×10^−3 follows *by the computation of* Lu–Zaman–Zhao [LZZ Thm 1.1: no real zero σ ≥ 1−1/(5 log q) for q ≤ 10^10]. Banks states that he did not verify that computation. | §1.2 p.2; proof §7 pp.17–18 |
| Kerr | **Theorem 1.** There is an absolute c>0 such that, for every primitive real χ(n)=(q/n), q a fundamental discriminant, every real zero β∈(0,1) satisfies (1−β) log\|q\| ≥ c. The constant is not explicit. | p.1; proof pp.5–6 |
| Guo | **Theorem 1.1.** For every primitive quadratic χ of conductor q≥3, every real zero β∈(0,1) satisfies **(1−β) log q > 1/100**. Remark 1.2 and App. A give **c=1/64**, using q≥7 with x=q^46, y=q^4 and positivity for q=3,4,5. **Proposition 3.1** is unconditional: S_−(x,χ) := Σ_{p≤x, χ(p)=−1} log p/p ≤ (11/20) log x + (29/60) log q + 6 for every x≥2. | Thm 1.1 p.2 (1.1); Prop 3.1 p.5 (3.1); proof §5 p.15; App. A p.16 |
| Lean (OAI repo) | `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap`: ∃ c>0, ∀ q≥3, χ primitive, χ≠1, real-valued, ∀ β∈(0,1), L(β,χ)=0 ⇒ c ≤ (1−β) log q. We read this statement. It matches OAI Thm 1. **The proof was not replayed.** | lean/ComparatorChallenges/SiegelZeros.lean; lean/docs/003.md |

Known misreadings to avoid:
- The theorem is a gap of size c/log q at s=1. It does **not** exclude real zeros below 1−c/log q, and it is far from GRH. The Lean doc says the same.
- OAI's c is not numerical. The explicit constants come from Banks (3.0e−3 for q≥10^10), Guo (1/100 for all q, 1/64 in App. A) and Kimura (5.8e−4 for all q, rising to 0.01015 for log q ≥ 10^4).
- Guo's Prop. 3.1 is unconditional. It is the "arithmetic half" of every proof, and no zero enters it.

## 2. Proof architecture and dependency structure

All four proofs have the same three-layer skeleton.

**(A) Analytic layer: a zero forces inert primes.** If δ=(1−β) log q is small, primes with χ(p)=−1 carry almost all of Σ log p/p up to X=q^A, for any fixed A with Aδ small.

**(B) Arithmetic layer, unconditional and the new content.** For every real primitive χ, inert primes carry at most a fraction κ<1 of the logarithmic mass, up to an O(log q) term:
S_−(X) ≤ κ log X + O(log q). The value of κ depends on the proof:

| Proof | κ |
|---|---|
| OAI/Banks | 3/4·(1+S_2/S_1) ≤ 13/16 |
| Kerr | (13/10)·(3/4) = 39/40, via 5/4 < 13/10 < 4/3 |
| Guo | 11/20 |
| Barreto/van Dijk (cited by Guo) | 1/2 + o(1) |

**(C) Comparison.** Take X a large power of q. The quantity log X·(1−κ) eventually exceeds the O(log q) losses plus δ(log X)²/log q, which gives the contradiction, or an explicit δ0.

Dependency graphs:

- **OAI:** Thm 1 ⇐ (master) [§6] ⇐ {Lem 2 (prime bias), Lem 6 (S_2/S_1 ≤ (C0/c0)/H), (upper) [Hadamard], (lower) ⇐ Lem 7 (divisibility) ⇐ {(frobenius), greedy rule}}. Lem 6 and greedy ⇐ Cor 4 ⇐ Lem 3 (interpolation on a projected box) ⇐ {dimension count, nearest-point lemma, Carathéodory, Lagrange on a rational face}.
- **Banks:** same graph, explicit; see the diagram in Banks §1.6. Thm 1.1 ⇐ {Lem 2.1, Lem 4.2, Lem 5.1, Cor 6.3}. Cor 6.3 ⇐ {Lem 6.2 ⇐ Lem 6.1, Lem 4.1 ⇐ Cor 3.5 ⇐ Prop 3.4 ⇐ Lem 3.1–3.3}. The all-q constant additionally needs [LZZ Thm 1.1].
- **Kerr:** Thm 1 ⇐ {Lem 1 (prime bias), Lem 5 (Siegel-lemma pigeonhole ⇒ F∈L_D vanishing on all N^4 points), Lem 6 (= Masser 1981 Thm 1), Lem 7 (μ(π(Z^4)) ≥ 4/3)}. Lem 5 ⇐ {Lem 2 (triangular basis), Lem 3 (box count), Lem 4 (residue count mod ∏p^{k_p} via Frobenius (3)–(4))}.
- **Guo:** Thm 1.1 ⇐ {Prop 3.1, Lem 5.1 ((5.1)–(5.3)), Lem 2.1 (2.6)}. Prop 3.1 ⇐ {Lem 3.2 (CRT box counting), Lem 3.3 (injectivity by auxiliary inert prime p0 + polynomial division), (3.8)–(3.10) (triangular basis + derivative-stable Frobenius divisibility), (3.12)–(3.15), Lem 2.1}. Lem 5.1 ⇐ Prop 4.1 (paired-tail hyperbola) ⇐ (4.1).

There is no circularity in any of the four. Guo's proof uses no complex analysis: no Hadamard product, functional equation or contour integration.

## 3. The core mechanism

The reported labels all describe the same principle, implemented three ways.

**The common principle.** Take an algebraic integer, or an integer lattice index, built from values of high-degree monomials at small points of Z[√d]. Its size is about (point size)^{degree}. If χ(p)=−1, Frobenius at p acts on Z[√d] as conjugation: θ^p ≡ σ(θ) (mod p). So every p-th power in the degree can be traded for a conjugate. When that trade lowers a weight, the object is divisible by p^{degree/p}. Summing over inert p≤U gives roughly degree·(inert mass up to U). Divisibility cannot exceed size unless the object is 0, and a zero estimate ensures it is not 0 at degree U ≫ (point size)^{1/κ}. Hence inert mass ≤ κ log U + O(log q).

The three implementations:

1. **Interpolation determinants (OAI, Banks).** The interpolation-determinant method follows Laurent 1991 §6.
   - Points: (θ_n, σθ_n, στθ_n) ∈ C^3 for n∈{0..N−1}^4 in K=Q(√d,√2).
   - The rank-4 lattice sits in 3 coordinates, so full rank needs degree U=N^{4/3} (Lem 3/Prop 3.4). Point size is N√q, so log N = (3/4) log U.
   - Adjoining √2 makes the Frobenius at every inert p equal to σ or στ, and both are among the three chosen conjugates.
   - Weighted greedy rows and a unitriangular row replacement give p^{Σ⌊α1/p⌋}.
   - Hadamard's inequality gives the size bound.
2. **Siegel lemma plus zero estimate (Kerr).**
   - Pigeonhole on coefficient boxes, using residues modulo ∏p^{k_p}, produces F∈L_D vanishing at all N^4 points (the p-adic Siegel lemma, Lemmas 3–5).
   - Masser's zero estimate with μ(π(Z^4)) = 4/3 says no nonzero F of degree < ((N−1)/3)^{4/3} vanishes there.
   - The rank-4/3-variables exponent 4/3 appears here as Masser's μ.
3. **Integer coefficient counting plus polynomial congruences (Guo, following Kerr, Green and van Dijk).** This uses a single quadratic field and no √2.
   - Polynomials f(z,w) = Σ c_{rs} z^r w^s with r<p0 and s<s0≈p0/30 are evaluated at (u+v√d, u−v√d) with derivatives ∂_z^j, j<s0. The points satisfy |u|,|v|<√p0, so log(point size) ≈ (1/2) log p0 + (1/2) log q.
   - **Injectivity** (Lemma 3.3) is a Stepanov-type argument. The auxiliary inert prime p0 gives g(ξ)=f(ξ,ξ^{p0}) mod p0, which is divisible by ∏f_{u,v}^{s0}, whose degree 2m(m−1)s0 exceeds p0 s0.
   - **Divisibility** (3.10) uses z^p−w. All its z-derivatives are divisible by p because w is not differentiated.
   - **Size** comes from CRT box counting (Lemma 3.2).
   - Result: κ = 1/2 + λ(2−1/2) with λ = (s0−1)/(p0−1) ≤ 1/30, which is 11/20.

A remark on why derivatives in z only matter: for a split p, z^p−z is congruent to 0 at the points, but ∂_z(z^p−z) ≡ −1 is not. So split primes do not contribute in Guo's construction. This is necessary, since otherwise Guo would bound the total mass M(x) by 0.55 log x, which is false. The mechanism is honestly specific to inert primes.

## 4. The new idea relative to prior work

Each ingredient was classical:
- prime bias from a real zero (Landau, Page, Linnik; Friedlander–Iwaniec 2018 §5);
- interpolation determinants (Laurent 1991);
- zero estimates (Masser 1981, Philippon 1986, Fischler 2005);
- Stepanov's method;
- Frobenius p-curvature arguments (Bost 2001).

The new idea is to turn the Siegel-zero prime bias into an **arithmetic contradiction inside the ring of integers of the quadratic field itself**. Frobenius at the (overwhelmingly inert) primes is the Galois conjugation. That makes an auxiliary algebraic object built from the field's own small integers divisible far beyond what its Archimedean size, which carries only a factor √q per degree, allows.

The technical enablers differ by proof:
- OAI: a rank-4 lattice viewed through 3 Galois coordinates (the √2 trick), which gives 3/4<1; plus a heavy weight H on the two conjugate coordinates, so the divisible coordinate carries almost all the degree.
- Guo: Stepanov multiplicities, which give 1/2+1/20.

Before October 2026, an unconditional bound S_−(x) ≤ κ log x + O(log q) with any κ<1 was not known. It is equivalent in strength to the theorem; see the barrier discussion in §12.

## 5. Load-bearing steps (numbered), with their locations in each independent proof

| # | Step | OAI (paper.tex) | Banks | Kerr | Guo |
|---|---|---|---|---|---|
| 1 | **Prime bias from the zero.** S_+(X) ≪ log q + δ(log X)²/log q, so the inert mass is ≥ log X − O(log q) − O(δ(log X)²/log q). | Lem 2, l.181–244 | Lem 2.1 (2.3)–(2.4), with explicit C1=2e^{3/2}/9 and C2=e^{3/2}/4 via Rosser–Schoenfeld Thm 6 | Lem 1 | Prop 4.1 (paired tails) + Lem 5.1 (5.1)–(5.3): elementary, positivity of 1∗χ, no L′/L |
| 2 | **Frobenius congruence.** For χ(p)=−1, θ^p ≡ σθ or στθ (mod p) according to (2/p). | (frobenius) l.579–596 | Lem 6.1 | (3)–(4) | (3.6) at p0, (3.9) at p∈P |
| 3 | **Unitriangular weight-lowering change of basis** (needs p>H, or p>8). | Lem 7 (replacement), l.606–629 | Lem 6.2 Steps 2–3, Lem 4.1(a) | Lem 2 | (3.8), Green Lem 5.1, cap h≤s0−1−s |
| 4 | **p-adic extraction.** The value is divisible by p^{Σ⌊α1/p⌋}. Distinct primes combine through the nonzero integer norm. | Lem 7 + (lower-primes)/(lower), l.630–657 | Lem 6.2 Step 1, Cor 6.3 | Lem 4 (residue count) | (3.10), derivative-stable |
| 5 | **Nonvanishing at degree U≍N^{4/3} (zero estimate).** Needs the kernel vector to have Q-independent coordinates (K biquadratic, d≠2). | Lem 3 + Cor 4, l.252–432; (A) l.470–485 | Prop 3.4, Cor 3.5, Lem 4.1(b) | Lem 6 (Masser Thm 1) + Lem 7 (μ≥4/3) | Lem 3.3 (2m(m−1)s0 > p0 s0) |
| 6 | **Degree concentration in the reducible coordinate.** | Lem 6 (c0=1/(4·97²), C0=192), l.517–550 | Lem 4.2; H=9216·97² gives S23 ≤ S1/12 | weight 8: W/Σi → 5/4 | λ ≤ 1/30, from s0=⌊p0/30⌋ |
| 7 | **Archimedean size bound.** | (upper) l.562–577, Hadamard | Lem 5.1 | Lem 3 + norm step in Lem 5 | Lem 3.2 + w_{r,s}, (3.11) |
| 8 | **The exponent gap (the heart):** leading divisibility vs leading size. | (master) l.678–718: 1 ≤ 13/16 + 1/16 | (7.3): 3/16 ≤ (4/3)(ω+1)C1δ + 3/32 | 5/4 < 13/10 < 4/3 | 11/20 per log x vs (93/2)/70 = 0.664 at x=q^70: (5.13)–(5.15) |
| 9 | **Parameters and small conductors.** | H with (C0/c0)/H ≤ 1/12, N=⌈q^γ⌉, δ→0; bounded q by finiteness, l.665–676 | ω=22, q0=10^10; q<10^10 by [LZZ] | γ large, ε small; small \|q\| left implicit | y=q^6, x=q^70, rational certificate; covers all q≥3 with no computation |

**The smallest statement whose failure invalidates the result:**
- OAI/Banks: Lem 7 together with Lem 3. Weighted-greedy rows of weight ≤ 96H^{2/3}U must give a nonzero Δ∈Z[a,b] that is divisible by p^{Σ⌊α1/p⌋} for every inert p>H.
- Guo: Prop. 3.1.
- Kerr: Lemma 5, with Masser's theorem used as a black box.

## 6. Imported results, with exact citations, as checked

| ID | Result | Used by | Status |
|---|---|---|---|
| E1 | Hadamard/log-derivative identity −L′/L(σ,χ) = ½log(q/π) + ½ψ((σ+ε)/2) − Σ_ρ Re 1/(σ−ρ). Each term is ≥0 for σ>1, and Re B(χ) = −Σ Re 1/ρ. [Davenport, Multiplicative NT, 2nd ed., Ch. 12 eqs. (17)–(18); Ch. 14] | OAI Lem 2, Banks (2.1)–(2.2), Kerr Lem 1 | Standard; re-derived. Kerr cites "[2, Equation (2), p. 89]", and that page/equation was **not** checked against the book (U1, harmless). |
| E2 | −ζ′/ζ(σ) ≤ 1/(σ−1) on (1,2], or 1/(σ−1)+O(1) | OAI, Banks | Checked numerically on a grid (max of the difference = −0.43) |
| E3 | Mertens Σ_{p≤x} log p/p = log x + O(1). Explicitly, Rosser–Schoenfeld 1962 Thm 6 (3.21)–(3.22): > log x + E − 1/(2 log x) for x>1, and < log x + E + 1/(2 log x) for x≥319, with E=−1.33258… | OAI, Banks (2.7), Kerr | RS bounds checked at every prime < 10^6 (0 violations) |
| E4 | Chebyshev ϑ(x) ≪ x (Banks uses ϑ(x) ≤ 2x; Guo proves ψ(x) ≤ (log 4)x) | all | Checked |
| E5 | Kronecker symbol: χ=(D/·) with D a fundamental discriminant, \|D\|=q, χ(p)=(d/p) for odd p | all | Standard (Davenport Ch. 5; Goldmakher notes for Guo) |
| E6 | Euler's criterion / Frobenius in Z[√d,√2]/p [Milne ANT §8 Ex. 8.19 for Kerr] | all | Re-derived |
| E7 | Hadamard's inequality; Carathéodory's theorem; existence of a nearest point in a compact convex set | OAI, Banks | Standard |
| E8 | **Masser, Invent. Math. 63 (1981), Theorem 1.** Let γ_1..γ_l be *basis elements* of Γ⊂C^n, rank l, and Γ(N) = {Σn_iγ_i : 0≤n_i≤N}. If P≢0 has total degree ≤D (D≥1) and vanishes on Γ(N), then D ≥ (N/n)^μ, where μ(Γ) = min_{1≤r≤n} (l−l_r)/r and l_r = the max rank of Γ′⊂Γ lying in a subspace of dimension n−r. | Kerr Lem 6 | **Verified against the scan (pp. 81–82).** Kerr's μ (min over L⊊C^n of rank(Γ/Γ∩L)/(n−dim L)) is the same quantity. Kerr omits "basis" (M2); in the application γ1..γ4 are Z-independent, so harmless. |
| E9 | Lu–Zaman–Zhao arXiv:2602.03626 **Thm 1.1**: if q ≤ 10^10 and χ is quadratic mod q, then L(σ,χ)≠0 for σ ≥ 1−1/(5 log q) | Banks (all-q c only) | The statement matches its use verbatim. This is a computation, not verified by Banks or by us (U3). |
| E10 | Apostol, Intro. to ANT: Euler summation Thm 3.1, partial summation Thm 4.2, hyperbola Thm 3.17, Thm 3.12(17), Thm 3.14, Thm 6.17; CRT; quadratic reciprocity | Guo | Standard; every use re-derived |
| E11 | Guo's sources [4] Green (hexagon:2610.00311v2, Lem 5.1, triangular basis), [14] van Dijk (hexagon:2610.00409v2, nonvanishing), [9] Pescador web (Stepanov lemma), [5] Kerr Lemmas 2–5 | Guo | Not fetched (U5). Guo re-proves every ingredient he uses, so these are not load-bearing. |
| E12 | Context only, not load-bearing: Siegel 1935, Page 1935, Linnik 1944, Heath-Brown 1992, Benli–Goel–Twiss–Zaman 2026, Friedlander–Iwaniec 2018, Philippon 1986, Fischler 2005, Laurent 1991, Bost 2001, Goldfeld 1976, Gross–Zagier 1986, Tao blog Oct 19 2026, OpenAI quasi-RH 7/8 [Guo ref 8] | — | — |

## 7. Full audit of Guo (the shortest independent human version)

Every step was re-derived by hand. Every rational certificate was recomputed with exact fractions (check_constants.py).

- **§2 Lemma 2.1.**
  - (2.3): the binomial induction is correct.
  - (2.4): n·M(n) ≤ log n! + ϑ(n). Correct.
  - (2.5): the convexity of log t/t² for t≥3 holds, and every prime >7 lies in 11+6j or 13+6j. The certificate is 30607/88200 = 0.34702 < 7/20. The true sum is 0.31980.
  - (2.6): (2.7) from log n! = ΣΛ(r)⌊n/r⌋. V ≤ 589/720 < 33/40, with true value 0.75537. The loss is 2 − 7/675 < 2; with exact logs it is 1.97199. **OK.**
- **Lemma 3.2 (CRT box counting).** The image mod p^ν is bounded through the adapted basis. The box B of side d0/(n w_i) injects modulo d0 because ‖ι(c−c′)‖∞ < d0. This gives H ≤ n log n + Σ log w_i. **OK.**
- **Lemma 3.3 (injectivity).**
  - Each f_{u,v} = (ξ−u)² − dv² is irreducible mod p0, since d is a non-residue and v≢0.
  - They are pairwise coprime, since u, u′ < m ≤ p0 and v+v′ ≤ 2(m−1) < p0.
  - f_{u,v} | h_{u,v,j} in Z[ξ], by the homomorphism ξ ↦ u+vt into Z[t]/(t²−d).
  - g ≢ 0, because the exponents r+p0 s are distinct.
  - (3.6): ξ^{p0} ≡ 2u−ξ.
  - g^{(j)} ≡ (∂_z^j f)(ξ, ξ^{p0}), by the chain rule mod p0.
  - The induction to f^{s0} | g uses that k! is invertible because k < s0 < p0, and that f′ is coprime to f.
  - The degree count is 2m(m−1)s0 > p0 s0 > deg g. **OK.**
  - Toy check: 5 instances (d=−163, 5, −7, 13; p0 = 17..37; s0 = 3..4) all have full column rank.
- **(3.8)–(3.10).**
  - The triangular basis stays inside the rectangle.
  - (3.9): ρ((u+vt)^p) ≡ u−vt.
  - ∂_z^j(z^p−w) ∈ pZ[z] for j≥1. Under Leibniz, every term keeps all h factors of p. **OK.**
  - Toy check: v_p(gcd of maximal minors of ι) ≥ H_p for every inert p, and *equality holds for almost every p* (e.g. d=−163, p0=37: p=5,7,…,31 all equal). This shows the extraction is sharp.
- **Coordinate bound and (3.11).** b0 ≤ p0 follows from p0 ≥ 4q. Σ(r+s) = p0 s0(p0+s0−2)/2. The algebra gives the coefficients 1/2+λ·3/2 = 11/20, (1−λ)/2 = 29/60 and (1−λ) log 2 = (29/30) log 2. **OK.**
- **(3.12)–(3.15).**
  - 2Σ_s min(k, s0−1−s) ≥ (2s0−1)k − k², with the difference (k−s0)(k−s0+1) ≥ 0.
  - The floor-sum identities hold.
  - Summation then gives (3.15). **OK.**
- **(3.16)–(3.17).**
  - The four terms are < 141/100, 1/50, 53/15 and 77/75, summing to 599/100 < 6. The first term with exact logs is 1.39012.
  - The small cases are p0 < 10^4, which gives 59/10 < 6, and p0 < 4q, which gives 623/300 < 6.
  - The case with no inert odd prime is trivial. **OK.**
- **Prop. 4.1 (paired tails).**
  - The hyperbola split is at u=√t, and u need not be an integer.
  - |A_u(v)| ≤ q/2.
  - The Euler-summation remainder satisfies |R_β(u,v)| ≤ u^{−β}.
  - The kernel g(v) = (1/v)∫_u^v w^{−β}dw is unimodal, with max ≤ u^{−β}/2 when β≥1/2, because (√x−2)² ≥ 0.
  - The three errors add up to (q+1+½log t)t^{1/2−β}. **OK.**
- **Lemma 5.1.**
  - The injection (n,p) ↦ np holds, with a(np)=a(n)a(p) for p>y≥n.
  - The partial summation gives exactly L(1,χ)κ with κ = log x log y + ½(log x)².
  - |D(t)| ≤ B(t), and ∫_y^∞ B(t)/t dt = 2B(y) + 2y^{−1/2}.
  - L(1,χ)/ε ≤ H_1(y) + B(y) follows from positivity.
  - (5.3) holds because a(p) = 1+χ(p) ∈ {0,2} for p > y ≥ q. **OK.**
- **Proof of Thm 1.1.**
  - The parameter conditions hold: β > 1/2, 76δ ≤ 0.76, y ≥ 729.
  - The certificates are H_1 ≥ 282431/176400 > 8/5 (barely: 1.60108), B(y) < 73/270, B(xy) < 10^−4, (5.10) 332/585 < 4/7, (5.11) 1176629/118125 < 10, and J < 699/20 < 35.
  - These give S_−(q^70) > (93/2)log q − 2 against the upper bound (2339/60)log q + 6, and (451/60)log 3 = 8.258 > 8. **OK.**
  - The f_k are monotone in q, checked for k=4, 6, 76.
- **App. A (c=1/64).** The certificates are (A.1) = 6 − 21863/548800, J < 741/32, and the margin is 4453/960·log 7 = 9.03 > 8. The q=3,4,5 block positivity holds. **OK.**

**Verdict on Guo:** no_issue_found_in_inspected_portion. The whole paper was inspected.

## 8. The key step of Kerr

- **Lemma 7: μ(π(Z^4)) ≥ 4/3.**
  - W = span_C(π^{-1}(L) ∩ Z^4) is a proper rational subspace.
  - The kernel is not contained in any proper rational subspace, so π|_W is injective. Hence rank(Γ∩L) = dim W ≤ dim L.
  - The ratios are (4−h)/(3−h) ∈ {4/3, 3/2, 2}. **OK.**
- **Masser's hypothesis.** The γ_j must be a Z-basis (M2). They are, because ker π ∩ Q^4 = 0. The determinant det(γ1,γ2,γ3) = 4√(2q) and the kernel v = (√2q, √2, −√q, −1) were both verified with sympy.
- **Lemma 6 application.** M = N−1 and n = 3 give deg F ≥ ((N−1)/3)^{4/3} > D = ⌊½((N−1)/3)^{4/3}⌋. A nonzero constant cannot vanish, so Masser's D≥1 condition is harmless.
- **The Siegel-lemma pigeonhole (Lemmas 3–5).** The coefficient box gives ‖c‖·B^{i+j+k} ≤ H, because (1+√2)(1+√|q|) ≤ 8√|q|. The residue count is p^{4k_p r − 4E_p}, combined by CRT. Then |F(point)| ≤ 2rH = P/2 < P while F(point) ∈ P·O, and the norm argument forces 0. **OK.**
- **Asymptotics.**
  - r ~ D³/384, W ~ 5D⁴/6144 and E_p ~ D⁴/(1536p), each with O(D³) error. Numerically the deviation halves when D doubles.
  - The threshold ratio is W/Σ_p E_p p = 5/4 < 13/10, and log Q ~ (4/3) log N. So γ/30 > 13/20 + O(1) suffices. **OK.**
- **Presentation points.**
  - M1: q=8 makes K degenerate (√8 = 2√2), so the coordinates of v become Q-dependent. Kerr's argument is only for large |q|, and the small-|q| finiteness step is left implicit (T1).

**Verdict on Kerr:** no_issue_found_in_inspected_portion, except the harmless M1, M2 and T1.

## 9. OpenAI and Banks: notes from a line-by-line reading

- **Lem 2 (prime bias).** The (2/e) factor holds since p^{−1/log X} ≥ e^{−1}, and (1−β)/((s−1)(s−β)) ≤ (1−β)(log X)². Banks's explicit version checks: κ = ½log π − ½ψ(3/2) = 0.55412, e^λκ/2 − 1/log 319 > 0, and Σ_{p>H, p|q} log p/p ≤ L/H.
- **Lem 3.**
  - K = 4P ⊂ [0, 4(N−1)]^4, which gives #lattice points ≤ (4N−3)^4.
  - R∘A ≢ 0, and m is a nearest nonvanishing lattice point.
  - y/4 lies on the face G. Carathéodory gives at most 4 vertices, and one has weight ≥ 1/4, so y−u ∈ 3P.
  - For n off G, the strict distance decrease gives R(A(m+n−u)) = 0.
  - On a rational hyperplane H ⊃ G, r·c ≠ 0 by Q-independence, and Lagrange in the 3 free coordinates has degree ≤ 3(N−1).
  - B = Q·R(·+A(m−u)) ∈ P_t. **OK.**
- **Cor 4.** T_j ≥ 32N and ∏(T_j − 3(N−1)) ≥ T1T2T3/8 = 4096N^4 > (4N−3)^4. **OK.**
- **Greedy selection and Lem 6.** All retained rows have weight ≤ 96H^{2/3}U. Then S_2 ≤ 192MH^{−1/3}U and S_1 ≥ M²/(4Q_0) ≥ MH^{2/3}U/(4·97²). **OK.**
  - The bounds are very lossy: toy maximum weights were 4–14 against bounds of 240–860 (T6).
  - Banks's H = 9216·97² equals exactly 12·C0/c0 of OAI Lem 6.
- **Lem 7.**
  - Every index α − pme_1 + me_j lies in N^3 and has weight w(α) − m(p−H) < w(α), so it lies in the span of the earlier retained rows.
  - The unipotent L preserves Δ, and the entries are in p^kR. Integrality of L is not needed. **OK.**
  - **Exact toy replay:** for (d,N,H) ∈ {(−163,2,1), (−163,2,2), (5,2,2), (13,2,1), (−7,2,2), (−163,3,2), (5,3,3)}, we computed N(Δ) exactly as a 4M×4M integer determinant. The result v_p(N(Δ)) ≥ 4E_p held for every admissible p, often with **equality** (e.g. d=5, N=3, H=3: p=7 gives 76=76 and p=13 gives 8=8).
- **(master).** First term ≤ 13/16; second term → (C + 13/24)·3/(4γ) < 1/16; third term Cδ·4γ/3 → 0; and MU/(S_1 log U) ≪ H^{−2/3}/log U. **OK.**
- **Banks §7 arithmetic.**
  - ω = ⌈8(C2+8/5)⌉ = 22.
  - log H + 3 + (13/12)log 8 = 23.53 < 24 < (24/23)L.
  - 1/(2H) + 13/24 + 24/23 = 1.5851 < 8/5.
  - δ0 = 9/(128·23·C1) = 3.06956×10^−3.
  - All recomputed. **OK.**

## 10. Are the claimed constants consistent?

The constants are all lower bounds for the same quantity inf (1−β) log q, so a larger value is simply stronger. They are mutually consistent:

| Source | c | Range |
|---|---|---|
| Guo | 1/100 | all q≥3 (App. A: 1/64) |
| Banks | 3.0×10^−3 | q≥10^10 (all q via LZZ) |
| Kimura | 5.8×10^−4 | all q |
| Kimura | 0.005965 | log q ≥ 35.01 |
| Kimura | 0.01015 | log q ≥ 10^4 |

- The differences come from method efficiency, not disagreement. Guo's arithmetic coefficient 11/20 is much better than the effective 13/16 of OAI/Banks after their H choice. Guo's real-variable step also avoids Banks's δ(log M)²/L loss coefficient C1·(4/3)(ω+1) ≈ 30.5.
- All constants are far below the computational truth for q ≤ 10^10, where (1−β) log q > 1/5 [LZZ], and below the GRH value ½ log 3.
- Guo's remark that "Kimura's last bound [0.01015] is larger" compares against the headline 1/100. His own App. A value 1/64 is larger still (T4). This is not an inconsistency.

## 11. Consequences, and numerical sanity checks against class-number data

**Auditor's derivation (not in the sources; the same mechanism as Kimura's Lemma 8).**
- Put β0 = 1 − 1/(100 log q). By Guo's Thm 1.1, L(t,χ) > 0 on [β0, 1].
- Rerun Guo's hyperbola (4.5) without assuming L(β,χ)=0. It gives H_β(t) = L(1,χ)t^ε/ε + ζ(β)L(β,χ) + θ L(β,χ)u^{−β} + E(t), with |θ| ≤ 1 and |E| ≤ (q+1+½log t)t^{1/2−β}.
- Since ζ(β)L(β,χ) < 0, H_β ≥ 1, t = q^4 and L(β,χ) ≤ 1.505 + e^{0.01}log q, we get:
  **L(1,χ) ≥ 0.00767/log q for q ≥ 10**, hence **h(D) ≥ 0.00244·√|D|/log|D|** for imaginary D < −4.
- This is an effective Siegel theorem. Previously the best effective bound was Goldfeld–Gross–Zagier, h ≫ log|D|.

**Checks against computed data** (check_consequences.py):
- Class numbers by reduced forms for all 6079 imaginary fundamental |D| ≤ 20000. These reproduce the Heegner list {3,4,7,8,11,19,43,67,163}.
- min L(1,χ)·log q is 0.664 (D=−3). Over |D| ≥ 10 it is 1.2534 (D=−163), about 165 times the implied 0.00767.
- The implied bound has 0 violations. It forces h ≥ 1 only for |D| ≥ 5.4×10^7, and h ≥ 100 only for |D| ≥ 1.3×10^12. So it is consistent with all class-number tables and, as expected for c=1/100, uninformative at small |D|.
- Real fields D ≤ 2000: min L(1,χ) log q = 0.6927 (D=5).
- The order of magnitude agrees with Kimura's independent use: class number ≤ 2000 forces |d| < 1.61×10^15. Our crude version with c=1/100 gives |d| ≲ 10^15.

**The unconditional Prop. 3.1 against data:**
- Tested for all 2433 fundamental |D| ≤ 4000, at every prime x ≤ 2×10^6.
- max[S_− − ((11/20)log x + (29/60)log q + 6)] = −6.67. There are no violations, and the bound is loose at this scale.
- The sharper Barreto/van Dijk shape gives max[S_− − (½log x + ¼log q + loglog 3x)] = −1.03.

## 12. Known barriers: why the claim does not contradict them

- **Parity barrier.** This is a limitation of sieve methods that see only the distribution of a sequence in progressions. None of the four proofs is a sieve argument, so the barrier does not apply.
- **The "pretentious" or Liouville model.** This is the relevant barrier. The completely multiplicative λ(p) ≡ −1 has every *statistical* property a Siegel-zero character has on primes. An argument that uses only the values χ(p) cannot work.
  - These proofs use the *algebraic realization* χ(p) = (d/p): Frobenius at p acts on Z[√d] (and Z[√d,√2]) as the conjugation. That yields p-adic divisibility of explicit algebraic integers whose height is controlled by √q.
  - λ has no such ring. Likewise, Beurling-type "fake" L-functions with Siegel zeros lack the integrality (Frobenius congruences mod rational primes) that the proofs use.
  - The theorem is in effect a quantitative Chebotarev statement for quadratic fields: Frobenius cannot concentrate on the nontrivial class up to X = q^{O(1)}.
- **Deuring–Heilbronn.** This is not a barrier. It states what a Siegel zero would force on other zeros. The proofs use only the classical first step (zero ⇒ prime bias), which is the input to Deuring–Heilbronn and Linnik. Nothing proved contradicts it, and conditional "illusory world" results (Heath-Brown on twin primes, Friedlander–Iwaniec) simply become vacuous.
- **The "proves too much" test, our own consistency analysis.** For a fixed field, the prime ideal theorem gives S_−(x) ~ ½ log x. So any valid unconditional bound must have κ ≥ 1/2. All versions pass: 13/16, 39/40, 11/20, and 1/2+o(1).
  - Sharper check for OAI: the same unitriangular trick gives divisibility for *every* Frobenius class.
    - Frob 1: all three coordinates.
    - Frob σ: coordinates 1 and 2 (σθ^p → θ changes weight by −Hp+1 < 0).
    - Frob στ: coordinates 1 and 3.
    - Frob τ: coordinates 2 and 3 (σθ^p → στθ).
  - With Chebotarev density 1/4 per class, the generic lower bound is (1/4)log U·[(S1+S2) + (S1+Sα2) + (S1+Sα3) + S2] = (3/4)(S1+S2) log U. This is *exactly* the leading term (S1+S2) log N of the Hadamard upper bound.
  - So the method is generically saturated but never overshoots. The slack is (S1+S2)(½ log q + log 8). Inert-dominated (Siegel) Frobenius tips the balance only when log U ≳ 2 log q.
  - This is heuristic: floor and p≤U truncation errors are lower order. It is strong evidence that the method cannot prove anything false about ordinary fields.
  - The exact toy equalities v_p = 4E_p in §9 are consistent with this sharpness.
- **Siegel's ineffectivity.** The new effective bound h ≫ √d/log d supersedes Goldfeld–Gross–Zagier, which gave log d. No theorem forbids this. It is the expected consequence of excluding Siegel zeros.

## 13. Classification of findings

- **verified_error:** none.
- **suspected_gap:** none. No step lacked a derivation after our re-derivation.
- **unresolved_ambiguity:**
  - U1: Kerr Lemma 1's citation "[Davenport, eq. (2), p. 89]" was not checked against the book. The statement is standard and was re-derived (it is OAI Lem 2 / Banks Lem 2.1).
  - U3: Banks's all-q constant depends on the LZZ computation (Thm 1.1, q ≤ 10^10), which was not verified.
  - U4: the OAI Lean development was not replayed. Only the challenge statement was read; it matches Thm 1.
  - U5: Guo's cited hexagon and web sources were not fetched. They are not load-bearing.
- **missing_hypothesis:**
  - M1 (Kerr): "K has degree four" and the Q-independence of v fail for q=8. This only affects finitely many q, and that finiteness step is implicit.
  - M2 (Kerr Lem 6): Masser's Thm 1 requires γ_j to be a basis of Γ. This is satisfied in the application.
- **typo_or_presentation:**
  - T1 (Kerr): small |q| is not explicitly handled.
  - T2 (OAI): c is not explicit, and the proof is by contradiction along a sequence. This is effective in principle, and Banks makes it explicit.
  - T3 (Banks Lem 3.3): "Proof. Exercise." OAI gives the argument.
  - T4 (Guo §1.1): the comparison with Kimura uses 1/100 rather than his own 1/64.
  - T5 (Guo): cites the unrefereed OpenAI 7/8 half-plane claim as "already implying" the result. This is not used.
  - T6 (OAI Lem 6 / Banks Lem 4.1(b)): the weight bound and c0 are very lossy. This is harmless.
- **no_issue_found_in_inspected_portion:** OAI Lemmas 2, 3, 6, 7, Cor 4 and §6; Banks §§2–7 and Remarks 7.1–7.2; Kerr Lemmas 2–7 and the proof of Thm 1; Guo §§2–5 and App. A, in full.

## 14. Numerical and exact checks

All are our own code, in `architecture_checks/`, run with `python3 -I`.

| Script | What it checks | Result |
|---|---|---|
| `check_divisibility_toy.py` | Exact OAI construction: greedy weighted rows over K, decided by Q-rank of 4 multiples, with two 60-bit primes cross-checked; exact N(Δ) as a 4M×4M integer determinant (python-flint); v_p(N(Δ)) vs 4E_p for admissible p; controls for Frobenius-1 and Frobenius-τ primes | 7 cases, N ≤ 3, M ≤ 81: **0 failures**, many equalities |
| `check_guo_injectivity_toy.py` | Guo Lemma 3.3 (full column rank of ι), (3.10) via Smith normal form (v_p(gcd of maximal minors) ≥ H_p), Lemma 3.2 inequality | 5 instances: **0 failures**, mostly equalities |
| `check_constants.py` | 71 checks: all of Guo's rational certificates and log bounds (2.2)–(5.15) and App. A; Banks's C1, C2, κ, ω, δ0, H, (7.3) arithmetic, −ζ′/ζ < 1/(σ−1), Rosser–Schoenfeld (3.21)–(3.22) to 10^6; OAI Cor 4, Lem 6 constants and kernel/minor (sympy); Kerr's r, W, E_p asymptotics and det(γ1,γ2,γ3) = 4√2q | **71/71 PASS** |
| `check_consequences.py` | Prop. 3.1 on 2433 discriminants × primes ≤ 2×10^6; Barreto shape; class numbers and L(1,χ) log q; the implied effective bound | 0 violations; see §11 |

Limits of these checks:
- The toy sizes (N ≤ 3, p0 ≤ 37) test the *exact algebraic identities*: Frobenius extraction, unitriangularity, injectivity. They do not test the asymptotic inequalities, which were checked by hand.
- No check reaches the regime X = q^70 or U = q^{4γ/3}. Nothing in the checks is evidence beyond the finite instances examined.
