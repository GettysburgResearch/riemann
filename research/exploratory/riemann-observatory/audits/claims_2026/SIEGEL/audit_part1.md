# CLAIM SIEGEL: Level-2 audit, part 1 of 2 (load-bearing steps 1–4, Guo in full, Kerr's key step, constants, consequences, barriers)

```text
Status:  Level-2 audit, part 1 of 2. This is the exploration layer, not an integrated or reviewed packet.
         Verified errors: none. Suspected gaps in load-bearing steps 1-4: none.
         Guo's paper was re-derived in full. Kerr's key step (Lemmas 2-7 + Masser Thm 1) was re-derived.
         The Lean development was not replayed. RH is untouched by this claim.
Scope:   Steps 1-4 of the map in ARCHITECTURE.md §5. These are:
           1. prime bias from the zero;
           2. Frobenius congruence;
           3. unitriangular weight-lowering change of basis;
           4. p-adic extraction.
         They are audited in the principal source (OAI paper.tex) and cross-checked in Banks, Kerr and Guo.
         Also in scope: Guo in full; Kerr's key step; consistency of the constants; numerical consequences
         (L(1,chi), class numbers); known barriers.
         Steps 5-9 belong to part 2. These are nonvanishing, degree concentration, Archimedean size, the
         exponent gap, and parameters/small q. Part 1 touches them only inside the Guo full audit and
         Kerr's key step.
Exact sources or dependencies (all re-hashed in this session):
  [OAI]    openai/math preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/
           paper.pdf  sha256 fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef
           build/paper.tex sha256 b011ba9c1f55ee2164292492c55e0c6d75c458eb30d4808808f9953823b8ded4 (773 lines)
  [Banks]  arXiv:2610.15483v1, PDF sha256 54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f
  [Kerr]   arXiv:2610.21099v1, PDF sha256 30dc40c959735eaaddd3609919695f87258ec2807fb615a9a4386702f3536116;
           LaTeX e-print sha256 d98b7b51b818b7c15a29a5fe17ff9a9f4673172453458b50cfedfad922ee2c48 (read only)
  [Guo]    arXiv:2610.30476v1, PDF sha256 f3058ae2a77e5c8e277cf90ed0faf8f745b8b638442b3439dfbf230e93e47a7e;
           LaTeX e-print sha256 a517c3bf95d5a341c77a00b52faa682564134c5a02b9db0342461247a5fe543c (read only)
  [Kimura] arXiv:2610.21511v2, PDF sha256 5987fa4df134c5d94faf92a0278af96fcf18ac6adfb25adaddb7d6ff63e5e733.
           Read only for Thm 1, Lemma 8, Remark 7 and Table 1.
  [Masser] Invent. Math. 63 (1981) 81-95. Thm 1 and the definition of mu were re-read on the GDZ scan, p. 82.
What was actually run: four scripts, our own code (python3 -I), in
  experiments/code/claims_2026/siegel_l2_part1/ (paths under research/exploratory/riemann-observatory/).
  Results: 94 PASS, 0 FAIL, plus INFO tables.
  These scripts are re-implementations. They do not re-run SIEGEL/architecture_checks/.
  Nothing from any audited repository was executed.
Smallest remaining gap: none was found in steps 1-4.
  The statements whose failure would invalidate this half are:
    OAI Lemma 7 (Delta in p^{E_p} R for admissible p);
    Guo (3.10) with Lemma 3.2;
    Kerr Lemma 4.
  Each was re-derived and replayed exactly on toy sizes.
  The open items are outside this half or are bookkeeping: independent expert review, the Lean replay,
  and the LZZ computation (which only Banks's all-q constant needs).
```

---

## 0. Verdict in one paragraph

Load-bearing steps 1–4 hold as stated in all four sources. We checked quantifiers, constants, uniformity and every imported statement we could locate. Each step has an explicit derivation, and each finite identity was replayed exactly.

- The main analytic and certificate checks are:
  - the zero-free form of the log-derivative inequality;
  - Rosser–Schoenfeld to 10^7;
  - Guo's paired-tail identity, tested in unconditional form against 390 exact (χ, β, t) triples;
  - all rational certificates in Guo, recomputed exactly.
- The finite algebra of steps 2–4 holds in every test:
  - Frobenius congruences: about 55,000 exact tests;
  - unitriangular bases: exact transition matrices;
  - OAI Lemma 7 *inside R itself*, with Δ reconstructed exactly by CRT. All 9 admissible tests passed, 6 of them with equality.
- The toy replay also produces explicit witnesses that the hypotheses **p > H** and **Frob_p ∈ {σ, στ}** are both necessary. When either is dropped, the divisibility conclusion fails.
- Guo's elementary proof is correct as far as we can check, in every line.
- Kerr's key step matches Masser's Theorem 1 as printed.
- The constants are mutually consistent. Guo's 1/100 is essentially optimal *for his own chain at q = 3* (0.01018). Banks's 3.07e-3 is within 1.3% of the optimum of *his* recipe (3.108e-3). Both are lower bounds for the same quantity.
- The implied effective bounds L(1,χ) ≥ 0.00767/log q and h(D) ≥ 0.00244√|D|/log|D| have no violations against 18,238 imaginary and 909 real fundamental discriminants. This is expected, since they only become informative at |D| ≳ 5·10^7.

None of this is evidence beyond the finite instances examined. The global statement rests on the proofs.

---

## 1. Step 1: prime bias from the zero (analytic layer)

**Principal-source statement (OAI Lemma 2, paper.tex l.181–244).** Let χ be a primitive, nonprincipal, real character of conductor q ≥ 3, with a real zero β ∈ (0,1). Put ℓ = log q and δ = (1−β)ℓ.
- For X ≥ 3: Σ_{p≤X, χ(p)=1} log p/p ≪ ℓ + δ(log X)²/ℓ.
- For every integer H ≥ 2: Σ_{H<p≤X, p∤2q, χ(p)=−1} log p/p ≥ log X − Cℓ − Cδ(log X)²/ℓ − C_H.
- C is absolute, and C_H depends only on H.

**Verification, line by line.**

| # | Step in the proof | Check | Result |
|---|---|---|---|
| 1a | −L′/L(s,χ) = ½log(q/π) + ½ψ((s+ε)/2) − Σ_ρ Re 1/(s−ρ) for real s > 1 | Imported (E1: Davenport Ch. 12 (17)–(18); Re B(χ) = −Σ Re 1/ρ). Re 1/(s−ρ) = (s − Re ρ)/\|s−ρ\|² > 0 since Re ρ ≤ 1 < s. Dropping all zeros except β gives an upper bound, and multiplicity is irrelevant. | OK. The book was not re-read. The zero-free consequence −L′/L(s,χ) ≤ ½log q − κ was confirmed for **all 75 fundamental \|D\| ≤ 120** at s ∈ {1.01, 1.05, 1.2, 1.5, 2} with mpmath Hurwitz-zeta derivatives. Minimum slack 0.168 (D = −3, s = 2). [s1 (d)] |
| 1b | Gamma term bounded on (1,2] for both parities | (s+ε)/2 ∈ (½, 3/2], so ψ ∈ (−1.96351, 0.03649]. | OK [s1 (b)] |
| 1c | −ζ′/ζ(s) = 1/(s−1) + O(1) on (1,2]; Banks needs ≤ 1/(s−1) | max_{(1,2]}[−ζ′/ζ − 1/(s−1)] = −0.43004 (at s = 2), tending to −γ as s → 1⁺. | OK [s1 (a)] |
| 1d | s = 1 + 1/log X ∈ (1,2) | Holds because log X ≥ log 3 > 1. | OK |
| 1e | Σ Λ(n)(1+χ(n))n^{−s} ≥ (2/e)·Σ_{p≤X,χ(p)=1} log p/p | Every term is ≥ 0, Λ(p)(1+χ(p)) = 2 log p, and p^{−s} = p^{−1}e^{−log p/log X} ≥ e^{−1}p^{−1}. | OK |
| 1f | 1/(s−1) − 1/(s−β) ≤ (1−β)(log X)² | Equals (1−β)/((s−1)(s−β)), and s−β ≥ s−1 = 1/log X. | OK |
| 1g | (eq:mass) | Uses Mertens; Σ_{p\|q} log p/p ≤ Σ_{p\|q} log p ≤ log q; removing p ≤ H costs log H + O(1). p = 2 is excluded automatically because H ≥ 2. The condition p∤q is implied by χ(p) = −1, so it is redundant and harmless. | OK |

Uniformity: every constant is absolute or depends on H only. No limit is interchanged.

**Cross-source checks.**
- **Banks Lemma 2.1** (explicit: λ ∈ (0,2], C1 ≥ e^λ/(2λ²), C2 ≥ e^λ/4, X ≥ 8, H ≥ 319) was re-derived line by line:
  - (2.5) uses ψ increasing and −ζ′/ζ ≤ 1/(σ−1).
  - (2.6) follows on multiplying by e^λ/2.
  - (2.7) uses Rosser–Schoenfeld (3.21) at x = X and (3.22) at x = H.
  - (2.8) holds.
  - Σ_{p>H, p\|q} log p/p ≤ L/H, because H^k < q forces k < L/log H.
  - The final positivity is e^λκ/2 − 1/log 319 = 1.068 > 0. Banks uses the weaker κ/2 > 0.277 > 0.174.
  - Recomputed constants: κ = 0.554120, C1 = 2e^{3/2}/9 = 0.995931, C2 = e^{3/2}/4 = 1.120422. [s1 (b)–(c)]
  - Rosser–Schoenfeld (3.21)–(3.22) as quoted hold at every prime < 10^7, which are the extremal points of the step function. Minimum margins are 0.031 and 0.0013 [s1 (e)]. This is evidence only; the 1962 paper was not re-read in this part.
- **Kerr Lemma 1.** This is the same inequality in ≪ form. Its citation, "[Davenport, (2), p. 89]", was not checked against the book (U1, carried over). The content equals OAI Lemma 2, line 1.
- **Guo: no L′/L at all.** Prop 4.1 (paired tails) and Lemma 5.1 replace the explicit formula; see §8 for the full derivation.
  - The algebra of Prop 4.1 was tested in its *unconditional* form, re-derived by us:
    H_β(t) = L(1,χ)t^ε/ε + ζ(β)L(β,χ) + θ L(β,χ)u^{−β} + E(t), with \|θ\| ≤ 1 and \|E\| ≤ (q+1+½log t)t^{1/2−β}.
  - When L(β,χ) = 0 this is exactly Guo (4.4).
  - Over 13 characters, β ∈ [½, 0.995] and t ≤ 10^6 (390 triples), max \|H − main\|/bound = 0.066. The main term is reproduced to 10^{−4}–10^{−6} absolute. For example, at D = −163, β = 0.95, t = 10^6: H = 5.555487, main = 5.555495, bound = 0.34. [s1 (g)]
  - The finite injection inequality H_1(y)J ≤ N(xy) − N(y) of Lemma 5.1 holds in every tested case. [s1 (h)]

**Verdict, step 1: no_issue_found_in_inspected_portion.**

## 2. Step 2: Frobenius congruence

**Principal-source statement (OAI (frobenius), l.579–596).** For odd p ∤ q with χ(p) = −1, in R/pR (R = Z[a,b], a² = d, b² = 2) we have a^p ≡ −a and b^p ≡ (2/p)b. Hence θ^p ≡ g_p(θ) (mod pR) for every θ ∈ R, where g_p = σ if (2/p) = 1 and g_p = στ if (2/p) = −1.

**Verification.**
- The p-power map is a ring endomorphism of R/pR, which has characteristic p, and it fixes the image of Z (Fermat).
- Euler's criterion gives a^p = a·d^{(p−1)/2} ≡ (d/p)a. Here (d/p) = χ(p) for odd p ∤ q (E5), and p ∤ d because every prime dividing d divides q.
- b^p ≡ (2/p)b.
- Therefore θ^p ≡ z1 − z2a + (2/p)z3b − (2/p)z4ab, which is σθ or στθ.
- The congruence holds in R itself, so maximality of R is not needed.

The full classification is (χ(p),(2/p)) = (1,1) → 1, (1,−1) → τ, (−1,1) → σ, (−1,−1) → στ.

**Cross-sources.**
- Banks Lemma 6.1 is identical.
- Kerr (3)–(4) uses O = Z[√q, √2] with q the fundamental discriminant. This needs [K:Q] = 4, which fails only for q = 8 (M1, carried over).
- Guo (3.9): ρ((u+vt)^p) ≡ u − vt (mod p) in Z[t]/(t²−d). Guo needs only the conjugation of Q(√d), because his second variable w is the conjugate point.
- Guo (3.6), at the auxiliary prime: ξ^{p0} ≡ u + (dv²)^{(p0−1)/2}(ξ−u) ≡ 2u − ξ mod (p0, f_{u,v}).

**Exact replays** [s2 (2a)–(2c)]:
- 11,410 tests in Z[√d,√2] over 15 values of d, including d = ±(10^9+…), and all odd p < 400;
- 9,880 tests in Kerr's Z[√D,√2];
- 32,340 cases of Guo (3.9), and the factor p in every z-derivative of z^p − w;
- 1,788 cases of Guo (3.6), together with irreducibility of f_{u,v} mod p0;
- all four Frobenius classes occur; 0 failures.

**Why √2 is adjoined.** With Q(√d) alone there are two Galois coordinates for a rank-2 lattice, so no exponent gain is available. Adjoining √2 gives a rank-4 lattice. The Frobenius at *every* inert p is then σ or στ, and both are among the three chosen coordinates (θ, σθ, στθ). This is the source of log N = ¾ log U. Primes with Frobenius τ (split in Q(√d), inert in Q(√2)) are unusable, but in a Siegel world they are rare. Banks makes the same point in Remark 7.2 (ii) and (iv).

**Verdict, step 2: no_issue_found_in_inspected_portion.**

## 3. Step 3: unitriangular, weight-lowering change of basis

**Principal-source statement (OAI Lemma 7, (replacement), l.606–629).** Take a retained α with α1 = pk + r, and let j ∈ {2,3} be the coordinate of g_p. Then
R̃_α := (θ^r(θ^p − g_pθ)^k σθ^{α2} στθ^{α3})_n = R_α + Σ_{m=1}^k (−1)^m C(k,m) R_{α−pme1+me_j}.
Each row on the right has weight w(α) − m(p−H), which is < w(α) when p > H. Each such row therefore lies in the K-span of earlier retained rows, so R̃ = L·R with L lower unitriangular over K, and det R̃ = Δ.

**Verification.**
- The binomial expansion is exact.
- The indices lie in N³ because α1 − pm ≥ r ≥ 0. They range over all of N³, not only the T-box of Cor 4, so the rows exist.
- A strict weight decrease means "strictly earlier" in any weight-compatible order. Banks fixes such an order (w(β) < w(α) ⇒ β ≺ α). It has order type ω because each weight is attained only finitely often.
- Banks Lemma 4.1(a) is the needed induction: span{rows ⪯ α} = span{retained rows ⪯ α}.
- Integrality of L is not needed, because divisibility is read from R̃ itself.

**Cross-sources.**
- **Kerr Lemma 2.** G_{ijk} = x1^v(x1^p − x_ℓ)^e x2^j x3^k. Its expansion terms have weight i + 8(j+k) − m(p−8), so the step needs p > 8. Kerr's set S has p > 8. The transition is unitriangular over O, so the G_{ijk} form an O-basis of L_D.
- **Guo (3.8).** g^{(p)}_{r,s} = z^{r−ph}w^s(z^p−w)^h with h = min(⌊r/p⌋, s0−1−s). Its monomials z^{r−pk}w^{s+k}, 0 ≤ k ≤ h, stay in the rectangle because s + h ≤ s0 − 1. The transition is triangular in r, so the g^{(p)}_{r,s} form an integer basis.
  - No condition p > H appears. Guo's argument is a counting argument, not a greedy determinant, so only an integer basis is needed.

**Exact replays** [s2 (3a)–(3b)]:
- Kerr: transition matrices for D ∈ {40, 64, 97}, p ∈ {11, 13, 17, 23}, ℓ ∈ {2, 3}, with up to 3,094 monomials. All are unitriangular in the weight order, and every expansion monomial lies in L_D.
- Guo: 16 configurations with (p0, s0) ∈ {(31,3), (37,4), (41,5), (61,6)} and p ∈ {3, 5, 7, 11}. All monomials stay in the rectangle and det = ±1 (python-flint).

**Verdict, step 3: no_issue_found_in_inspected_portion.**

## 4. Step 4: p-adic extraction

**Principal-source statement (OAI Lemma 7, then (lower-primes) and (lower), l.630–657).**
- For admissible p (p > H, p ∤ 2q, χ(p) = −1): Δ ∈ p^{E_p}R, where E_p = Σ_{α∈𝒫} ⌊α1/p⌋.
- Hence p^{4E_p} | N(Δ), and ¼log\|N(Δ)\| ≥ Σ_{adm p≤U} E_p log p ≥ S1·Σ_{adm p≤U} log p/p − M·Σ_{p≤U} log p.
- With Lemma 2 at X = U and Chebyshev, this is ≥ S1(log U − Cℓ − Cδ(log U)²/ℓ − C_H) − CMU.

**Verification.**
- Every entry of R̃_α lies in p^kR by (frobenius). Factoring p^k out of each row gives Δ ∈ p^{E_p}R.
- σ and τ preserve R and p^E R. So N(Δ) ∈ p^{4E_p}R ∩ Z = p^{4E_p}Z, using R = Z ⊕ Za ⊕ Zb ⊕ Zab.
- Distinct primes are coprime, so their powers combine. This needs N(Δ) ≠ 0, which is supplied by step 5 (Δ ≠ 0) and deferred to part 2.
- ⌊x⌋ ≥ x − 1 gives E_p ≥ S1/p − M. Dropping admissible p > U is a valid lower bound.
- The admissible set {H < p, p ∤ 2q, χ(p) = −1} is exactly the set in (eq:mass), so Lemma 2 applies verbatim.

**Cross-sources.**
- **Banks Lemma 6.2 and Cor 6.3.** Identical, with the explicit Chebyshev bound Σ_{p≤M} log p ≤ 2M. H ≥ 319 makes "admissible" equal to {H < p ≤ M, χ(p) = −1}.
- **Kerr Lemma 4.**
  - G_{ijk}(θ_n, σθ_n, στθ_n) ∈ p^{⌊i/p⌋}O.
  - The class of c_{ijk} mod p^{k_p−⌊i/p⌋} determines f mod p^{k_p}. Since k_p ≥ ⌊D/p⌋, every exponent is ≥ 0.
  - The count is Π p^{4(k_p−⌊i/p⌋)} = p^{4k_p r − 4E_p}, using that O is free of rank 4. CRT combines the primes.
- **Guo (3.10) and Lemma 3.2.**
  - By Leibniz, every term of ∂_z^j g^{(p)}_{r,s} contains h factors ∂_z^{j_i}(z^p−w). Each has remainder ≡ 0 (mod p) at every grid point:
    - j_i = 0: by (3.9);
    - 1 ≤ j_i ≤ p: the coefficient p!/(p−j_i)! is divisible by p;
    - j_i > p: the derivative is 0.
  - So ι(g^{(p)}_{r,s}) ∈ p^{h_{r,s}(p)}Z^{2m(m−1)s0}.
  - Lemma 3.2 converts this into H ≤ n log n + Σ log w_i. We re-derived it: image mod p^ν ≤ p^{νn − Σh_i}; CRT; the box 0 ≤ c_i < d0/(n w_i) injects mod d0 because ‖ι(c−c′)‖_∞ < d0.
  - The auxiliary prime p0 lies in 𝒫 but contributes h = 0, since r < p0.

**Exact toy replay of OAI Lemma 7 inside R** [s2 (4)]. This is new relative to ARCHITECTURE.md, which tested only v_p(N(Δ)).
- **Row selection.** Greedy weighted rows were selected modulo two primes P ≈ 2^62 that split completely in K. Both primes gave the same selection. The selection was then certified exactly:
  - retained rows are F_P-independent, hence K-independent (P is unramified);
  - every skipped row lies in the K-span of the earlier retained rows. This was certified by the exact integer rank of the regular representation, where K-span corresponds to the Q-span of {row, a·row, b·row, ab·row}.
- **Reconstructing Δ.** Δ was reconstructed exactly in Z⊕Za⊕Zb⊕Zab by CRT, from determinants under the four embeddings modulo up to 63 split primes P > 2^61. The modulus exceeds twice the Hadamard bound, and the result was re-verified at a fresh prime. v_p(Δ) is the minimum over the four integer coordinates.
- **Cases (d, N, H):** (−163,2,1), (−163,2,3), (−7,2,2), (5,2,4), (13,2,6), (−1,2,3), (−3,2,5), (229,2,2), (−163,3,2), (5,3,4). M = 16 or 81.
- **Result:** 9 admissible tests, **0 failures**, equality v_p(Δ) = E_p in 6 of them. Examples: d = 5, N = 3, H = 4 gives p = 7: 24 = 24 and p = 13: 3 = 3. d = −163, N = 3, H = 2 gives p = 7: 5 = 5.
- **Necessity witnesses: the hypotheses are load-bearing, not cosmetic.**
  - *p ≤ H.* d = 5, N = 2, H = 4, p = 3 (Frob στ): v_3(Δ) = 5 < Σ⌊α1/3⌋ = 9. The weight-lowering fails and so does the conclusion.
  - *Frobenius τ.*
    - d = −1, N = 2, H = 3, p = 5: v_5(Δ) = 0 < 1.
    - d = 13, N = 2, H = 6, p = 3: v_3(Δ) = 1 < 10.
    - d = 5, N = 3, H = 4, p = 11: v_11(Δ) = 1 < 7.
    - τθ is not one of the three coordinates.
  - OAI, Banks and Kerr all state exactly the restrictions that these witnesses show to be necessary. Nothing is overstated.
- **Control (our strengthening).** The same unitriangular trick gives Δ ∈ p^{E^full_p}R, where E^full_p sums ⌊α_i/p⌋ over the coordinates that Frob_p maps into the variable set:
  - Frob 1: all three coordinates;
  - σ: coordinates 1 and 2;
  - στ: coordinates 1 and 3;
  - τ: coordinates 2 and 3.
  - Result: 14 tests, 0 failures. Only 3 are nontrivial: d = −163, N = 3, p = 3 gives 73 ≥ 54; p = 5 gives 19 ≥ 16; d = −3, p = 7 (Frob 1) gives 1 ≥ 1.

**Verdict, step 4: no_issue_found_in_inspected_portion.** The toy sizes (N ≤ 3, α1 ≤ 15) test the exact algebra only, not the asymptotic inequalities.

## 5. The core mechanism

The three reported labels are accurate, but they name implementation layers of **one** mechanism.

1. **An auxiliary arithmetic object built from the field's own small integers.** It is a determinant of monomial rows (OAI/Banks), a vanishing polynomial in L_D (Kerr), or an injective integer evaluation map (Guo). Its points are θ ∈ Z[√d] (and Z[√d,√2]) in a box of side N, with height ≈ N√q per unit of degree.
2. **Frobenius equals conjugation at inert p (step 2).** It turns every block of p powers of θ into one power of a conjugate. Through a unitriangular change of basis (step 3), this gives p-adic divisibility of order degree/p (step 4). Summed over inert p ≤ degree, the divisibility is ≈ (degree)·(inert log-mass up to the degree).
3. **A rank/dimension or multiplicity count (step 5, part 2)** makes the object nonzero, or the map injective, at a degree where "size per unit degree" is a fraction κ < 1 of log(degree):
   - OAI/Banks: rank 4 in 3 coordinates gives log N = ¾ log U (interpolation lemma);
   - Kerr: Masser's μ = 4/3;
   - Guo: points of height √p0 against degree p0, using Stepanov multiplicities in z only, gives ½ + (3/2)λ ≤ 11/20.
4. **Size versus divisibility** then gives the unconditional bound S_−(X) ≤ κ log X + O(log q).
5. **Step 1** turns a zero with δ → 0 into S_−(X) ≥ log X − o(log X) for X = q^{O(1)}, which contradicts the bound in 4.

So "interpolation determinants" (OAI/Banks) and "Siegel-lemma pigeonhole" (Kerr) are the two classical dual forms of the transcendence method, as in Laurent's duality. Guo's "integer coefficient counting" is Kerr's pigeonhole recast as injectivity plus counting. Guo's "polynomial congruences" appear twice: as divisibility (z^p − w) and as nonvanishing (a Stepanov auxiliary prime p0). The new idea relative to earlier work is that both the arithmetic input (Frobenius) and the nonvanishing input live inside Z[√d]. That is how the inert-prime bias forced by a Siegel zero becomes an archimedean-versus-p-adic contradiction.

## 6. Guo's elementary proof: full audit (2610.30476v1)

Every displayed inequality was re-derived by hand from the LaTeX source. Every rational certificate was recomputed exactly with fractions [s3 (G)]. Highlights, including points not recorded in ARCHITECTURE.md §7:

- **(2.2) series certificates.** Using the stated truncations (x, m) = (2,1), (3,2), (5,3), (7,9), the truncated sum and its remainder bound give: log 2 < 0.69444; for log 3, *exactly* 13/12 < log 3 < 11/10 (both endpoints are attained by the bounds, with strictness from 0 < R_m < bound); log 5 < 1.61364; 35/18 ≤ 1.944996 < log 7 < 1.946013 ≤ 39/20. OK.
- **Lemma 2.1.**
  - Chebyshev by binomial coefficients: ψ(2m)−ψ(m) ≤ log C(2m,m), and ψ(2m+1)−ψ(m+1) ≤ log C(2m+1,m) ≤ 2m log 2. The induction starts at ψ(1) = 0.
  - nM(n) ≤ log n! + ϑ(n).
  - Convexity: f″ = (6 log t − 5)/t⁴ > 0 for t ≥ 3. Primes > 7 lie in 11+6j or 13+6j. The certificate is 30607/88200, and the exact-log value is 0.34536 (true sum 0.319804).
  - (2.7) bounds on A(n).
  - V ≤ 589/720, true value 0.755362.
  - Loss 2 − 7/675, or 1.97199 with exact logs.
  - Numerically, ψ(x)/x ≤ 1.0388, M(x) ≤ log x + log 4 with margin ≥ 1.73, and inf[M(x)−M(y) − log(x/y)] = −0.194 > −2 for 100 ≤ y ≤ x < 10^7. [s1 (f)]
- **Lemma 3.2** (counting) and **Lemma 3.3** (injectivity).
  - f_{u,v} = (ξ−u)² − dv² is irreducible mod p0, because dv² is a non-residue.
  - The f_{u,v} are pairwise coprime: u, u′ < m < p0 and 2 ≤ v+v′ ≤ 2(m−1) < p0.
  - f_{u,v} | h_{u,v,j} in Z[ξ], via the homomorphism ξ ↦ u+vt into Z[t]/(t²−d), since the remainder satisfies (au+b) + avt = 0 and v > 0.
  - g ≢ 0 because the exponents r + p0 s are distinct.
  - g^{(j)} ≡ (∂_z^j f)(ξ, ξ^{p0}), since every derivative of ξ^{p0} vanishes mod p0.
  - The induction f^k | g ⇒ f^{k+1} | g uses three facts: (f^k)^{(k)} ≡ k!(f′)^k mod f; k! is invertible since k < s0 < p0; gcd(f, f′) = 1 since f(u) = −dv² ≢ 0.
  - Degree count: 2m(m−1) ≥ m² > p0 because m ≥ 2 and p0 is not a square.
  - OK. The toy check of injectivity is in architecture_checks. Our s2 replays the congruences it rests on.
- **(3.8)–(3.11).** Basis and divisibility as in §§3–4.
  - Coordinate bound: ‖u ± vt‖ ≤ (m−1)(1+√\|d\|) < √p0(1+√q) ≤ b0, and r!/(r−j)! ≤ p0^j. b0 ≤ p0 follows from p0 ≥ 4q, giving w_{r,s} = (p0/b0)^{s0−1}b0^{r+s}.
  - Σ(r+s) = p0s0(p0+s0−2)/2.
  - The middle expression in (3.11) equals log b0 + λ(2 log p0 − log b0), *with equality*, since (p0+s0−2) − 2(s0−1) = p0 − s0.
  - Substituting λ ≤ 1/30 gives (11/20)log p0 + (29/60)log q + (29/30)log 2, checked symbolically.
- **(3.12)–(3.15).**
  - The min-sum identity, including the defect (k−s0)(k−s0+1), was brute-forced for s0 < 25 and k < 60.
  - The floor-sum identity and both inequalities were checked for every p0 < 400 and every odd prime p ≤ p0.
  - The summation to (3.15) uses Σ_{p∈𝒫} log p ≤ ϑ(p0) and the odd-square bound.
- **Proof of Prop 3.1.**
  - The four remainder terms are 14040/9999 (1.39012 with exact logs at p0 = 10^4), 0.017157, 2107/600 and 77/75. Their sum is 599/100 < 6. Note 22/15 = 29/30 + 1/2 collects both log 2 terms.
  - The monotonicity claims hold.
  - Small cases: 59/10, and 623/300 via log q > log p0 − log 4.
  - The case with no inert odd prime is trivial.
  - OK. An independent numerical sanity check was run on 20 inert-heavy discriminants (all h ≤ 7 maxima, Heegner, small real) at every prime x ≤ 10^7. The maximum excess over the bound is −6.57, with no violation. The Barreto/van Dijk shape has maximum excess −0.86. [s4 (C4)]
- **Prop 4.1** (paired tails), re-derived.
  - \|A_u(v)\| ≤ min(r, q−r).
  - (4.1).
  - The hyperbola split at u = √t: for d > u, the conditions dm ≤ t and m < u are equivalent.
  - The first line is bounded by (q/2)t^{−β}⌊u⌋.
  - The Euler-summation remainder lies in [−u^{−β}, u^{−β}].
  - E0 ≤ u^{ε−β}(1 + log u).
  - The kernel identity g(v) = v^{−1}∫_u^v w^{−β}dw holds, and g′ changes sign once.
  - The bound max g ≤ u^{−β}/2 comes from ∫_1^x y^{−β} ≤ 2(√x−1) for β ≥ ½ and (√x−2)² ≥ 0.
  - The boundary terms vanish: A_u(u) = 0, A is bounded, and g → 0.
  - OK. The unconditional generalization was tested numerically (§1).
- **Lemma 5.1.**
  - The injection (n, p) ↦ np holds, with (n, p) = 1 since p > y ≥ n.
  - The Abel identity's main term is (L/ε)[log(xy) − log y − log x + (ε/2)(log²(xy) − log²y)] = Lκ, recomputed.
  - The remainder is R = D(xy)log(xy) − D(y)log y + ∫(ε log t − 1)D(t)/t dt, with \|D\| ≤ B.
  - ∫_y^∞ B(t)/t dt = 2B(y) + 2y^{−1/2}, recomputed.
  - L(1)/ε ≤ H_1(y) + B(y), using H_β(y) ≤ y^ε H_1(y).
  - (5.3) needs y ≥ q, so that a(p) ∈ {0, 2} for p > y.
- **Proof of Thm 1.1.**
  - β > ½, and ε log(xy) = 76δ ≤ 0.76.
  - H_1(y) ≥ Σ_{m≤27} 1/m² ≥ 282431/176400 > 8/5.
  - f_k(q) is decreasing: the derivative bracket (1 − k/2)q − (k²/4) log q is < 0 for k ≥ 2.
  - B(y) < 73/270 (exactly 0.27022), and B(xy) = 3.39·10^{−17}.
  - The certificate is 332/585 < 4/7.
  - κ = 2870 log²q, with (5.10) = 1176629/118125.
  - J/log q < 699/20, giving 93/2 versus 2339/60, a gap of 451/60.
  - (451/60)·log 3 = 8.2579 > 8. OK.
- **App. A (1/64).** Every certificate checks: 17/70 (attained as (8+3.9)/49, strict via log 7 < 39/20), 621/32, 6 − 21863/548800, 741/32, and 4453/960. With exact log 7 the margin is 9.026 > 8. For q = 3, 4, 5, the positive-block argument (strict convexity for q = 5) is correct, and there is no primitive conductor 6. OK.

**Verdict on Guo: no_issue_found_in_inspected_portion.** The whole paper was inspected.

Presentation notes, carried over:
- Guo's comparison with Kimura uses 1/100 rather than his own 1/64 (T4).
- Guo cites the unrefereed 7/8 half-plane claim as "already implying" the result, but does not use it (T5).
- The Kimura figures Guo quotes, 0.0005811, 0.005965 for log q ≥ 35.0131, and 0.01015, **match Kimura v2's Theorem 1, proof and Table 1**: 5811·10^{−7}, 1193/200000, ≥ 0.01015. These were re-read this session.

## 7. Kerr's key step (2610.21099v1: Lemmas 2–7 and the application of Masser)

- **Lemma 3 (coefficient box).** The choice u_t ≤ ⌊H/(8√\|q\|B^{i+j+k})⌋ gives ‖c‖B^{i+j+k} ≤ H, because (1+√2)(1+√\|q\|) ≤ 4.83√\|q\| ≤ 8√\|q\|. There are (⌊X⌋+1)⁴ > X⁴ choices. OK.
- **Lemma 4 (residues).** See §4. OK.
- **Lemma 5 (pigeonhole).**
  - The count is (P/(32r√\|q\|))^{4r}B^{−4W}, which beats P^{4r}Πp^{−4E_p} under (6).
  - F = f1 − f2 satisfies \|F^{(t)}(point)\| ≤ Σ‖c‖B^{i+j+k} ≤ 2rH = P/2.
  - F(point) ∈ PO, so a nonzero value would have \|Nm\| ≤ (P/2)⁴ < P⁴ while P⁴ \| Nm. Hence the value is 0. OK.
  - Asymptotics, recounted exactly at D = 2000 and 8000:
    - r/(D³/384) = 1.0034;
    - W/(5D⁴/6144) = 1.0039;
    - E_11/(D⁴/(1536·11)) = 1.0018;
    - E_101 ratio 0.979, with the O(p/D) deviation expected.
  - The threshold ratio is W/(D⁴/1536) → 5/4 < 13/10 < 4/3. The O(D³Q) error is o(D⁴) because Q = D/(log N)². [s3 (K)]
- **Lemma 6 = Masser 1981, Theorem 1.** Re-read on the scan, p. 82:
  - "Let γ1,…,γl be *basis elements* of Γ … Γ(N) the points n1γ1+…+nlγl for *non-negative* integers n_i *not exceeding N*."
  - Theorem 1: for real N ≥ 0 and D ≥ 1, a nonzero P of total degree ≤ D vanishing on Γ(N) satisfies D ≥ (N/n)^μ, where μ = min_{1≤r≤n}(l − l_r)/r.
  - Kerr's box 0 ≤ m_j ≤ M with M = N − 1 matches. It is a one-sided box, not a symmetric one, so no factor-2 loss arises.
  - Kerr's μ (min over L ⊊ C^n of rank(Γ/Γ∩L)/(n − dim L)) is the same quantity.
  - The basis hypothesis is satisfied but not stated by Kerr (M2, harmless): π is injective on Z⁴ because ker π ∩ Q⁴ = 0.
  - D ≥ 1 is harmless, since a nonzero constant cannot vanish.
- **Lemma 7 (μ ≥ 4/3).**
  - W = span_C(π^{−1}(L) ∩ Z⁴) is proper. If it were all of C⁴, then L ⊇ π(C⁴) = C³.
  - W is rational, so ker π ⊄ W. Since ker π is a line, ker π ∩ W = 0.
  - Hence rank(Γ∩L) = dim W = dim π(W) ≤ dim L, and the ratios are (4−h)/(3−h) ∈ {4/3, 3/2, 2}.
  - Hypothesis check: v = (√(2q), √2, −√q, −1) has Q-independent coordinates, which is equivalent to [K:Q] = 4. This fails only for q = 8 (M1).
  - det(γ1,γ2,γ3) = 4√(2q) and π(v) = 0, both by sympy.
- **Application.** deg F ≤ D_Kerr = ⌊½((N−1)/3)^{4/3}⌋ < ((N−1)/3)^{4/3} ≤ deg F gives the contradiction.
- **Theorem proof.** The condition (PS) reduces to γ/30 > (C + 13/20) + C(16/9)εγ² + o(1). Choose γ large, then ε small, then \|q\| large. The finiteness for small \|q\|, and for q = 8, is left implicit (T1).

**Verdict on Kerr's key step: no_issue_found_in_inspected_portion.** The minor items M1, M2 and T1 are carried over.

## 8. Are the claimed constants consistent?

All the constants are lower bounds for the same quantity, inf (1−β)log q. A smaller constant is a weaker theorem, not a disagreement.

| Source | Constant | Range | Status in this audit |
|---|---|---|---|
| OAI | c > 0, not explicit | all q | proof by contradiction along a sequence |
| Banks | δ0 = 81/(5888e^{3/2}) = 3.069556·10^{−3} | q ≥ 10^{10} | recomputed: ω = ⌈8(C2+8/5)⌉ = ⌈21.763⌉ = 22; H = 9216·97² = 12·C0/c0 of OAI Lem 6; log H + 3 + (13/12)log 8 = 23.531 < 24; 1/(2H) + 13/24 + 24/23 = 1.58514 < 8/5 |
| Banks | 3.0·10^{−3} | all q | needs LZZ Thm 1.1 (q ≤ 10^{10}: (1−β)log q ≥ 1/5), not verified by Banks or by us (U3) |
| Guo | 1/100 | all q ≥ 3, no computation | fully re-derived (§6) |
| Guo App. A | 1/64 | all q ≥ 3 (q ≥ 7 by the chain; q = 3, 4, 5 by positivity) | fully re-derived |
| Kimura v2 | 5.811·10^{−4}; 0.005965 for log q ≥ 35.0131; ≥ 0.01015 for log q ≥ 10^4 | stated ranges | statements re-read; Lean-certified per Kimura; not re-checked by us |

**Recomputed optimizations** [s3 (B), (X)]:
- **Banks's recipe.** δ0(λ, ω) = (3/16 − 3(C2+8/5)/(4ω))/((4/3)(ω+1)C1). Optimized over λ ∈ [¼, 2] and integer ω, the maximum is **3.108·10^{−3}** (λ ≈ 1.45, ω = 22). Banks's stated 3.0696·10^{−3} is within 1.3% of what his chain can give, so the small constant is intrinsic to that chain.
  - The coefficient C1·(4/3)(ω+1) ≈ 30.5 on δ comes from log M ≈ (4/3)(ω+1)L.
  - The fixed costs come from the √q factor of the point size (13/24) and from C2.
- **Guo's chain.** δ*(q; A, B) is the largest δ his inequalities exclude at x = q^A, y = q^B, using exact logs and the paper's own constants: 6 in Prop 3.1, −2 in (5.3), H_1(y) ≥ Σ_{m≤√y} 1/m², and the cap εlog(xy) ≤ 1.
  - **q = 3:** best 0.01018 at (A,B) ≈ (69.5, 6). Guo's choice (70, 6) gives 0.01018. Guo's 1/100 is therefore essentially optimal for his chain at the worst conductor, consistent with his margin 8.258 versus 8.
  - **q = 7:** 0.0165, which yields App. A's 1/64.
  - **Larger q:** q = 100 gives 0.029; q = 10^{10} gives 0.048; q → ∞ gives 0.061 (B → 2⁺).
  - With (A,B) fixed at (70,6), the value saturates at 1/76 because of the cap.
  - Checked: min_{3≤q<2000} δ*(q; 70, 6) = 0.01018 > 1/100, and min_{7≤q<2000} δ*(q; 46, 4) = 0.01642 > 1/64.
- Kimura's Remark 7 gives an asymptotic limit of ≈ 1.02·10^{−2} for his explicit OAI-type chain. This is consistent with an interpolation-determinant chain being less efficient than Guo's elementary one. The gap between the arithmetic exponents, 13/16 effective versus 11/20, is the main reason.

**Conclusion:** consistent. The ordering Banks (3.07e-3, q ≥ 10^{10}) < Kimura (5.8e-4 rising to 1.0e-2) and Guo (1/100 to 1/64) reflects method efficiency. Every value is far below the computed truth for q ≤ 10^{10} (≥ 1/5 by LZZ, unverified) and below ½log 3, the value under GRH.

## 9. Numerical consequences: L(1,χ) and class numbers

**Auditor's derivation** (not in the sources; it uses the same mechanism as Kimura's Lemma 8). Let c = 1/100 and β0 = 1 − c/log q.
- By Guo's Thm 1.1 there is no zero in [β0, 1). Since L(1,χ) > 0, L(β0,χ) > 0.
- The unconditional hyperbola identity of §1, which we tested numerically, applies with β = β0 ≥ 0.99.
- Use H_{β0}(t) ≥ 1, drop −ζ(β0)L(β0,χ) ≥ 0, and use \|L(β0,χ)\| ≤ e^c(3/2 + log q). With t = q^k this gives
  L(1,χ)log q ≥ c e^{−kc}[1 − e^c(3/2+log q)e^{kc/2}q^{−k/2} − (q+1+(k/2)log q)e^{kc}q^{−k/2}] =: g(q).
- At q = 10 and k = 4, g = **0.007671**, which reproduces ARCHITECTURE.md's 0.00767. With k optimized, g(10) = 0.00925.
- g is nondecreasing for 10 ≤ q ≤ 400, and its limit is c e^{−2c} = 0.00980.
- Hence L(1,χ) ≥ 0.00767/log q for q ≥ 10, and h(D) ≥ 0.00244√\|D\|/log\|D\| for D < −4.
- This consequence inherits the status of Guo's theorem: reviewed by no one, and not Lean-checked.

**Data** [s4 (C2)–(C3)], our own reduced-forms class numbers for all 18,238 imaginary fundamental D with \|D\| ≤ 60,000:
- The h = 1 list is exactly {3, 4, 7, 8, 11, 19, 43, 67, 163}.
- The counts and maxima for h ≤ 7 reproduce Watkins (2004, Table 4), as recalled: 9/163, 18/427, 16/907, 54/1555, 25/2683, 51/3763, 31/5923. The table was quoted from memory; the exact agreement cross-validates both the code and the recollection.
- min L(1,χ)log q = 0.6642 (D = −3). For q ≥ 10 the minimum ratio to the bound is **163×**, at D = −163. **0 violations.**
- Real fields, 909 fundamental D ≤ 3000: min L(1,χ)log D = 0.6927 (D = 5). The formula was cross-checked by 2 log ε/√5 = 0.430409. 0 violations.
- **Informative range.** The implied bound forces h > 1 only for \|D\| ≥ 5.3·10^7, h > 100 for \|D\| ≥ 1.3·10^{12}, and h > 2000 for \|D\| ≥ 7.9·10^{14}.
  - Kimura v2 has h > 2000 for \|d\| ≥ 1.6069·10^{15} with his own Lean-certified gap c_2000 = 0.005965, which is less than 1/100. He found the largest \|d_K\| with h ≤ 2000 to be 1,062,350,083.
  - These are consistent in order of magnitude.
  - Class-number tables therefore **cannot** falsify the claim at accessible sizes. They can only confirm that no implied inequality is contradicted, and none is.

## 10. Barriers: why the claim does not contradict them

- **Parity (Selberg).**
  - The parity barrier says that sieve axioms, meaning densities in progressions or levels of distribution, cannot distinguish λ from a Siegel-zero character.
  - In the Friedlander–Iwaniec "illusory sieve" setting, a hypothetical Siegel-zero world satisfies the standard sieve axioms.
  - None of the four proofs is a sieve argument. The decisive input is algebraic integrality: Frobenius congruences mod p in Z[√d] (step 2), used inside an auxiliary object whose nonvanishing is a zero estimate. That information is not part of the sieve axioms, so the barrier does not apply.
- **Pretentious, Liouville and Beurling models. This is the relevant barrier, and the proofs respect it.**
  - Prop 3.1 cannot follow from the values χ(p) alone. The sign pattern "every prime inert" (λ(p) = −1) violates (11/20)log x + (29/60)log q + 6 as soon as x > q^{4.27} (q = 163), x > q^{2.25} (q = 10^6), or x > q^{1.66} (q = 10^{12}) [s4 (C5)].
  - A genuine quadratic character cannot keep χ(p) = −1 that long. The Linnik–Vinogradov (Burgess-type) bound puts the least prime p with χ(p) = 1 at ≪ q^{1/4+o(1)}. Among the Heegner fields, the longest inert run ends at 41 for D = −163.
  - Beurling-type "fake ζ" with zeros near 1 exist, but they have no ring of integers and no Frobenius congruences. Every proof uses exactly that structure.
- **Deuring–Heilbronn.**
  - Deuring–Heilbronn describes what a Siegel zero *would* force on other zeros; the theorem simply excludes that hypothesis. The proofs use only its classical first step (zero ⇒ prime bias, step 1), which is also Linnik's input.
  - Excluding the zero makes the "illusory world" statements vacuous (Heath-Brown on twin primes, Friedlander–Iwaniec). Nothing proved contradicts them.
- **"Proves too much" tests, our own.**
  1. For a fixed field the prime ideal theorem gives S_−(x) = ½log x + O_q(1), so any valid unconditional κ must be ≥ ½. All versions pass: 13/16 effective (OAI/Banks), 39/40 (Kerr), 11/20 (Guo), and ½ + o(1) (Barreto/van Dijk, with a loglog x term).
  2. The extraction is sharp in toys: v_p(Δ) = E_p in 6 of 9 cases.
  3. The 4-class extraction (§4 control) feeds a heuristic Chebotarev balance. With density ¼ per class, the generic lower bound is ¼log U·[(S1+S2) + (S1+S_{α2}) + (S1+S_{α3}) + S2] = ¾(S1+S2)log U. This equals the leading term (S1+S2)log N of the Hadamard bound. The method is therefore saturated, but not overshooting, on ordinary fields, and it gains only when Frobenius concentrates on {σ, στ}, i.e. in a Siegel world. This is a heuristic consistency check, not a proof.
- **Siegel's ineffectivity.** The effective bound h ≫ √d/log d (§9) supersedes Goldfeld–Gross–Zagier (≫ log d). No theorem forbids it; it is the expected consequence of excluding Siegel zeros (Hecke/Landau).
- **Scope.** The analytic layer links only a *real* zero near 1 to prime bias. The method says nothing about complex zeros or about GRH, so the claim is not "too strong" in that direction either.

## 11. Classification of findings (part 1)

IDs U1, U3, U4, M1, M2, T1, T4 and T5 continue the numbering of ARCHITECTURE.md §13. U2, U6, T7 and P1-x are new in this part.

| ID | Location | Classification | Finding |
|---|---|---|---|
| P1-1 | OAI Lem 2, Lem 7 + (lower-primes)/(lower); Banks Lem 2.1, 6.1, 6.2, Cor 6.3 | no_issue_found_in_inspected_portion | Steps 1–4 re-derived and checked numerically, with exact toy replays of Lemma 7 in R |
| P1-2 | Guo 2610.30476v1, whole paper | no_issue_found_in_inspected_portion | Every inequality re-derived and every certificate recomputed exactly; Prop 4.1 algebra tested numerically |
| P1-3 | Kerr Lemmas 2–7 + Masser Thm 1 | no_issue_found_in_inspected_portion | Masser re-read on the scan: one-sided box, basis hypothesis, μ definition all match |
| P1-4 | OAI Lem 7 hypotheses p > H and Frob ∈ {σ, στ} | no_issue (positive sharpness witness) | Explicit toy witnesses that dropping either hypothesis breaks the divisibility. The hypotheses are necessary and correctly stated. |
| U1 | Kerr Lem 1: "[Davenport, (2), p. 89]" | unresolved_ambiguity (harmless) | Not checked against the book. The content is OAI Lem 2, re-derived. |
| U2 | Banks (2.7): Rosser–Schoenfeld 1962 Thm 6 (3.21)–(3.22) | unresolved_ambiguity (harmless) | The original was not re-read in this part. The quoted form is standard and holds at every prime < 10^7. |
| U3 | Banks all-q constant | unresolved_ambiguity | Depends on the LZZ computation (q ≤ 10^{10}), unverified. Not needed for steps 1–4 or for Guo's all-q 1/100. |
| U4 | OAI Lean development | unresolved_ambiguity | Not replayed. Kimura reports kernel-checked use of it, with a different interpolation argument in Lean. |
| U6 | Guo's Apostol theorem numbers; Davenport Ch. 12 (17)–(18) | unresolved_ambiguity (harmless) | Statement numbers not matched against the books. Every use re-derived. |
| M1 | Kerr: K of degree 4 | missing_hypothesis (harmless) | Fails for q = 8 only. Covered by implicit finiteness. |
| M2 | Kerr Lem 6 | missing_hypothesis (harmless) | Masser requires γ_j to be basis elements. True here. |
| T1 | Kerr | typo_or_presentation | Small \|q\| left implicit |
| T4, T5 | Guo §1.1 | typo_or_presentation | Kimura comparison uses 1/100 rather than 1/64; cites the unrefereed 7/8 claim but does not use it |
| T7 | OAI (eq:mass) | typo_or_presentation | Condition p∤q is redundant given χ(p) = −1. Harmless. |
| — | all four sources | verified_error | **none** |
| — | steps 1–4 | suspected_gap | **none** |

## 12. Checks run (our own code)

Directory: `research/exploratory/riemann-observatory/experiments/code/claims_2026/siegel_l2_part1/`. Each script was run with `python3 -I` on Python 3.13.18, mpmath 1.3.0, sympy 1.14.0, python-flint 0.9.0 and numpy 2.5.3. Outputs are saved as `*.out` next to each script.

| Script | What it checks | Result |
|---|---|---|
| `s1_analytic_layer.py` | Step 1: ζ′/ζ and Γ terms; Banks κ, C1, C2 and the λ trade-off; zero-free −L′/L ≤ ½log q − κ (75 discriminants × 5 s); Rosser–Schoenfeld to 10^7; Guo Lemma 2.1 numerics; Guo Prop 4.1 in unconditional form (390 triples); Lemma 5.1 injection | 15 PASS / 0 FAIL |
| `s2_s4_frobenius_extraction.py` | Steps 2–4: Frobenius congruences (about 55k exact cases, all 4 classes); Guo (3.6)/(3.9); Kerr and Guo transition matrices; exact toy replay of OAI Lemma 7 in R (certified greedy selection, Δ by CRT with fresh-prime verification); necessity witnesses; 4-class control | 18 PASS / 0 FAIL |
| `s3_constants_consistency.py` | Every Guo certificate (exact fractions plus exact logs); Banks §7 constants; OAI Cor 4 and master; Kerr counts and the 5/4 threshold; optimization of Guo's and Banks's chains | 54 PASS / 0 FAIL |
| `s4_consequences_barriers.py` | Implied L(1,χ) bound g(q); 18,238 imaginary class numbers (Heegner, Watkins h ≤ 7); 909 real L(1,χ); Prop 3.1 on inert-heavy D to 10^7; the pretentious-pattern barrier | 7 PASS / 0 FAIL |

**Limits.**
- The toy sizes (N ≤ 3, M ≤ 81, α1 ≤ 15; p0 ≤ 400) test the exact algebraic identities only.
- The asymptotic inequalities and the regime X = q^{70} or U = q^{4γ/3} are covered by hand derivation and by the rational certificates, not by computation.
- Numerical non-violation for finitely many discriminants and x ≤ 10^7 is not evidence for the global statement.

## 13. Not done in part 1

- Steps 5–9 in OAI and Banks: Lemma 3 / Prop 3.4, Lemma 6 / 4.2, Hadamard, master inequality, parameters. These are part 2. Guo's and Kerr's versions are covered above.
- The Lean replay.
- The LZZ computation.
- Davenport and Apostol page-level checks; the Rosser–Schoenfeld original.
- Independent expert review. None of the above substitutes for it.
