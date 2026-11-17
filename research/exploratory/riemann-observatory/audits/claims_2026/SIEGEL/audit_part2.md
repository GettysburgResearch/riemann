# CLAIM SIEGEL: Level-2 audit, part 2 of 2 (load-bearing steps 5–9, cross-checks, Guo and Kerr second half, constants, consequences, barriers)

```text
Status:  Level-2 audit, part 2 of 2. This is the exploration layer, not an integrated or reviewed packet.
         Verified errors: none. Suspected gaps in load-bearing steps 5-9: none.
         The Lean development was not replayed. RH is untouched by this claim.
Scope:   Steps 5-9 of the map in ARCHITECTURE.md §5:
           5. nonvanishing (interpolation lemma / zero estimate / Stepanov injectivity);
           6. concentration of the degree in the Frobenius-divisible coordinate;
           7. the Archimedean size bound;
           8. the exponent gap (divisibility versus size), including order of limits;
           9. parameter choices and small conductors.
         Each is audited in the principal source (OAI paper.tex) and cross-checked in Banks, Kerr and Guo.
         Also in scope: the second half of Guo (Lemma 3.2, Lemma 3.3, (3.11)-(3.17), §5, App. A) and Kerr's
         key step (Lemmas 5-7 with Masser Thm 1); constants; consequences; barriers.
         Steps 1-4 are in audit_part1.md and are not repeated here.
Exact sources or dependencies (all re-hashed in this session):
  [OAI]    openai/math repo HEAD 4eaee87548250b2682affda7d05d947c05554bae,
           preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/
           paper.pdf  sha256 fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef
           build/paper.tex sha256 b011ba9c1f55ee2164292492c55e0c6d75c458eb30d4808808f9953823b8ded4 (773 lines;
           line numbers below refer to it)
  [Banks]  arXiv:2610.15483v1, PDF sha256 54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f
  [Kerr]   arXiv:2610.21099v1, PDF sha256 30dc40c959735eaaddd3609919695f87258ec2807fb615a9a4386702f3536116;
           LaTeX e-print sha256 d98b7b51b818b7c15a29a5fe17ff9a9f4673172453458b50cfedfad922ee2c48 (read only)
  [Guo]    arXiv:2610.30476v1, PDF sha256 f3058ae2a77e5c8e277cf90ed0faf8f745b8b638442b3439dfbf230e93e47a7e
  [Masser] Invent. Math. 63 (1981) 81-95, Theorem 1 and the definition of mu, re-read on the GDZ scan, p. 82.
What was actually run: four scripts, our own code, python3 -I, in
  research/exploratory/riemann-observatory/experiments/code/claims_2026/siegel_l2_part2/
  s5_nonvanishing.py (14 PASS), s6_s7_concentration_size.py (6 PASS), s8_s9_gap_parameters.py (11 PASS),
  s10_consequences.py (5 PASS): 36 PASS, 0 FAIL, plus INFO tables. Outputs are saved as *.out.
  The scripts are re-implementations. They do not re-run architecture_checks/ or siegel_l2_part1/.
  Nothing from any audited repository was executed.
Smallest remaining gap: none was found in steps 5-9.
  The statements whose failure would invalidate this half are:
    OAI Lemma 3 (interpolation on a projected box) with Cor 4 and the greedy selection;
    Kerr Lemma 7 (mu >= 4/3) together with Masser's Theorem 1;
    Guo Lemma 3.3 (injectivity) with Lemma 3.2.
  The three are structurally independent nonvanishing arguments, so the claim does not rest on any one of them.
  Open items are bookkeeping or outside the mathematics checked here: independent expert review, the Lean
  replay (U4), and the LZZ computation (U3), which only Banks's all-q constant needs.
```

---

## 0. Verdict in one paragraph

Load-bearing steps 5–9 hold as stated in all four sources. We re-derived each step and checked quantifiers, constants, the order in which parameters are chosen, and every imported statement we could locate (Masser's Theorem 1 against the scan). Finite instances were replayed exactly or with certified modular ranks:

- **Step 5.** The minimal spanning box for OAI Lemma 3 is the same for 9 fields with |d| up to 10^9, and equals the dimension floor at N ≤ 5.
- **Step 5, Masser's bound.** It holds in every toy. The true minimal vanishing degree grows like 1.4–1.65·N^{4/3}.
- **Step 5, Guo.** Lemma 3.3 is sharp: injectivity holds at exactly the threshold allowed by dimension, in 40 random configurations and 21 actual grids.
- **Step 6.** Toy data agree with the a-priori bounds.
- **Step 7.** The size and divisibility inequalities are correctly oriented around exact values of N(Δ), and Guo's Lemma 3.2 chain holds exactly.
- **Step 8.** The exponent gaps are re-derived. All leading coefficients κ lie in [½, 1), so none contradicts the prime ideal theorem.
- **Step 9.** Guo's single parameter choice works on 65 conductors from 3 to 10^15, with the worst case at q = 3.

We also give explicit witnesses that the hypothesis "kernel coordinates linearly independent over Q" is load-bearing, and correctly stated:
- at d = 2, i.e. q = 8, OAI Lemma 3's conclusion fails once N ≥ 53;
- at q = 8, Masser's μ drops to ≤ 1.

This confirms the harmless missing-hypothesis item M1 (Kerr, q = 8) with a concrete witness.

None of this is evidence beyond the finite instances examined. The global statement rests on the proofs.

---

## 1. Step 5: nonvanishing

### 1.1 Principal source (OAI)

**Lemma 3** (paper.tex l.252–408). Let A: C^4 → C^3 be surjective with ker A = C·c, where the four coordinates of c are linearly independent over Q. Let N ≥ 1, and let t_j be integers with t_j ≥ 3(N−1) and Π_j (t_j − 3(N−1) + 1) > (4N−3)^4. Then evaluation B ↦ (B(An))_{n∈E_N}, from polynomials with deg_{z_j} B ≤ t_j onto C^{E_N}, is surjective.

**Cor 4** (l.410–432). For 1 ≤ H ≤ N, put U = N^{4/3}, T1 = 32H^{2/3}U and T2 = T3 = 32H^{−1/3}U. Then the rows (An)^α with α_j ≤ T_j span C^{E_N}.

**Application** (l.451–513).
- A = [[1,a,b,ab],[1,−a,b,−ab],[1,−a,−b,ab]] with a² = d and b² = 2. ker A = C(ab, b, −a, −1).
- Its coordinates are Q-independent because [K:Q] = 4 (d ≠ 1, 2).
- The greedy rule ordered by w(α) = α1 + H(α2+α3) retains M = N^4 rows, all of weight ≤ 96H^{2/3}U.
- Δ ∈ Z[a,b] \ {0}.

**Line-by-line verification.**

| # | Step | Check | Result |
|---|---|---|---|
| 5.1 | Non-surjective implies a nonzero functional v; S = supp v, P = conv S ⊂ [0,N−1]^4 | Linear algebra | OK |
| 5.2 | A nonzero R exists with deg_{z_j} R ≤ b_j = t_j − 3(N−1) and R(Am) = 0 on 4P ∩ Z^4 | #(4P ∩ Z^4) ≤ (4(N−1)+1)^4 < Π(b_j+1) | OK |
| 5.3 | R∘A ≢ 0; some m ∈ Z^4 has R(Am) ≠ 0 at least distance from 4P; h = m − y ≠ 0 | A surjective, so R∘A is a nonzero polynomial. A nonzero polynomial cannot vanish on Z^4 (one variable at a time). Bounded neighbourhoods contain finitely many lattice points. m ∉ 4P by 5.2. | OK |
| 5.4 | y/4 lies in the face G = argmax_P h·v; dim G ≤ 3; Carathéodory gives ≤ 4 vertices; some u has weight ≥ ¼; y − u ∈ 3P | Nearest-point inequality h·(x−y) ≤ 0. G is proper if dim P = 4. Vertices of G are vertices of P, hence lie in S. The coefficients 4λ_i and 4λ_u − 1 are ≥ 0 and sum to 3. | OK |
| 5.5 | For n ∈ S \ G: R(A(m+n−u)) = 0 | y′ = y+n−u ∈ 3P + P = 4P (P convex). h·(u−n) > 0, so ‖h − η(u−n)‖² < ‖h‖² for small η > 0. m′ ∈ Z^4 is strictly closer to 4P than m. If m′ ∈ 4P, 5.2 applies directly; Banks treats this case explicitly. | OK |
| 5.6 | On G: a rational hyperplane r·v = k contains G; r·c ≠ 0; A restricted to the hyperplane is an affine bijection; the Lagrange Q has total degree ≤ 3(N−1) with Q(Au) = 1 and Q(An) = 0 on (S∩G)\{u} | G's vertices are integral, so the hyperplane is rational. Q-independence gives r·c ≠ 0. Two distinct points of the hyperplane differ in some coordinate i ≠ i0. The denominators u_i − a are nonzero integers. | OK |
| 5.7 | B = Q·R(· + A(m−u)) satisfies deg_{z_j} ≤ 3(N−1) + b_j = t_j, and Σ v_n B(An) = v_u R(Am) ≠ 0 | Translation preserves separate degrees | OK |
| 5.8 | Cor 4 arithmetic | T_j ≥ 32N (uses H ≤ N); T1T2T3 = 32³N^4; T_j − 3(N−1) ≥ T_j/2; ⌊T⌋ + 1 > T; 4096N^4 > (4N−3)^4 | OK (also part 1 s3) |
| 5.9 | Kernel, rank, Q-independence | Minor 4ab ≠ 0; A·(ab, b, −a, −1) = 0, re-multiplied by hand. 1, a, b, ab form a Q-basis iff d ∉ {1, 2}. Rank over K equals rank over C. | OK |
| 5.10 | Greedy | Every Cor-4 row has w ≤ T1 + 2HT2 = 96H^{2/3}U. Rows of weight ≤ that bound form an initial segment of the order and span, so exactly M rows are retained, all within the bound. | OK |

Uniformity: Lemma 3 uses nothing about A except surjectivity and the Q-independence of the kernel. No height of A, no field constant and no aspect-ratio constant enters. This matters because a q-dependent constant here would change the √q bookkeeping in step 7.

### 1.2 Cross-sources

- **Banks Prop 3.4, Cor 3.5, Lemma 4.1.** The same proof, written out. Step 5 obtains "dim ≤ 3" from orthogonality to h, which is cleaner than OAI's case split. Lemma 3.3 ("nonzero F does not vanish on Z^4") has the proof "Exercise" (T3, carried over). The standard induction on variables suffices.
- **Kerr Lemma 6 = Masser 1981, Theorem 1.** Re-read on the GDZ scan, p. 82, and confirmed:
  - "Let γ1, …, γl be basis elements of Γ, and for real N ≥ 0 denote by Γ(N) the set of points of the form n1γ1 + … + nlγl for non-negative integers n1, …, nl not exceeding N."
  - Theorem 1: "For real N ≥ 0, D ≥ 1 let P be a non-zero polynomial of total degree at most D such that P(γ) = 0 for all γ in Γ(N). Then we have D ≥ (N/n)^μ."
  - μ = min_{1≤r≤n}(l − l_r)/r, where l_r is the maximal rank of a subgroup lying in a subspace of dimension n − r. This is Kerr's min over L ⊊ C^n of rank(Γ/Γ∩L)/(n − dim L).
  - Kerr's box {0..N−1}^4, i.e. M = N−1, is one-sided as in Masser. The basis hypothesis is not stated by Kerr (M2) but holds, since π is injective on Z^4.
- **Kerr Lemma 7.** Re-derived.
  - W = span_C(π^{−1}(L) ∩ Z^4) is a proper rational subspace.
  - ker π is a line not contained in W, so it meets W only in 0.
  - Hence rank(Γ∩L) = dim W = dim π(W) ≤ dim L, and μ ≥ min_{h<3}(4−h)/(3−h) = 4/3.
  - Application: γ1 = (1,1,1), γ2 = √q(1,−1,−1), γ3 = √2(1,1,−1), γ4 = √(2q)(1,−1,1).
  - det(γ1,γ2,γ3) = 4√(2q), recomputed by cofactor expansion. The kernel v = (√(2q), √2, −√q, −1) was verified coordinate by coordinate.
  - With M = N−1 and n = 3: deg F ≥ ((N−1)/3)^{4/3} > D = ⌊½((N−1)/3)^{4/3}⌋, while F ∈ L_D has total degree ≤ i + j + k ≤ D. OK.
- **Guo Lemma 3.3.** Re-derived (the details are also in part 1 §6):
  - f_{u,v} = (ξ−u)² − dv² is irreducible mod p0 and pairwise coprime;
  - f_{u,v} | h_{u,v,j} in Z[ξ];
  - ξ^{p0} ≡ 2u − ξ mod (p0, f_{u,v}), by Frobenius in F_{p0}[ξ]/(f_{u,v}) ≅ F_{p0²};
  - g^{(j)} ≡ (∂_z^j f)(ξ, ξ^{p0});
  - the Hasse-type induction f^k | g ⇒ f^{k+1} | g uses (f^k)^{(k)} ≡ k!(f′)^k mod f, that k! is a unit, and that gcd(f, f′) = 1;
  - degree count 2m(m−1)s0 > p0s0 > deg g.

  Observation (ours): the proof never uses that the points form Guo's grid. Any set G of pairs (u, v), 0 ≤ u < p0, 1 ≤ v ≤ (p0−1)/2, with 2|G| > p0 gives injectivity, and for any s0 < p0. Below that size, injectivity is impossible by dimension. So the Stepanov count equals the linear-algebra count exactly.

### 1.3 Numerical and exact checks (s5_nonvanishing.py)

All ranks are taken modulo primes P that split completely in K. A full rank mod P certifies full rank over K. Deficiencies are confirmed modulo a second prime, or forced by a dimension count or an explicit polynomial.

- **(5a) Minimal spanning cube and uniformity in the field.**

  | N | t_min (all 9 fields) | dimension floor | Lemma 3 sufficient cube | Cor 4 T = 32N^{4/3} |
  |---|---|---|---|---|
  | 2 | 2 | 2 | 11 | 81 |
  | 3 | 4 | 4 | 24 | 138 |
  | 4 | 6 | 6 | 39 | 203 |
  | 5 | 8 | 8 | 55 | 274 |

  - The 9 fields were d ∈ {−1, −3, −7, −163, 5, 13, 229, −1000003, 999999937}. The minimal cube t with [0,t]³ spanning is identical in all of them and equals the dimension floor.
  - Lemma 3 and Cor 4 are therefore lossy by large constant factors but correct.
  - Aspect ratio (N = 4, boxes (ρt2, t2, t2), ρ ≤ 32): the rows needed are 1.16–2.29 × M. The cost of an extreme aspect ratio stays O(M), as OAI's product-form budget asserts.
- **(5b) Necessity witness: d = 2, i.e. q = 8. All four papers exclude this case or leave it to finiteness.**
  - With a = b = √2, the kernel (2, √2, −√2, −1) has Q-dependent coordinates. A is still surjective and injective on Z^4.
  - z1 = (n1+2n4) + √2(n2+n3) and z3 = (n1+2n4) − √2(n2+n3), so (z1, z3) is constant on fibres of size up to ⌈N/2⌉·N. z2 separates each fibre; this was checked exactly on 40 fibres at N = 6.
  - Spanning by [0,t]³ therefore forces t + 1 ≥ (max fibre).
  - At **N = 53** Lemma 3's budget is met with t = 1396, but spanning needs t ≥ 1430. The lemma's conclusion fails without the hypothesis, so the hypothesis is load-bearing and correctly stated.
  - At small N the degenerate minimal cubes are 2, 5, 7 against the generic 2, 4, 6, i.e. already above.
  - For Kerr at q = 8: γ1, γ4 and γ2 − 2γ3 are Z-independent and lie in the plane x1 = x3 (sympy, exact). So l_1 ≥ 3 and **μ ≤ 1 < 4/3**.
  - F = Π_{s=0}^{3N−3}(x1 − x3 − 2√2 s), of degree 3N−2, vanishes on all of Kerr's points. This beats ((N−1)/3)^{4/3} from N = 2189 on.
  - This sharpens M1: Kerr's Lemma 7 hypothesis genuinely fails at q = 8, and Theorem 1 for q = 8 rests only on the implicit finiteness argument. It is harmless because it concerns a single conductor.
- **(5c) Masser-type minimal vanishing degree.**

  | N | D_min | dimension-count degree | Masser ((N−1)/3)^{4/3} | Kerr's D |
  |---|---|---|---|---|
  | 2 | 3 | 3 | 0.23 | 0 |
  | 3 | 6 | 6 | 0.58 | 0 |
  | 4 | 9 | 10 | 1.00 | 0 |
  | 5 | 13 | 14 | 1.47 | 0 |
  | 6 | 18 | 18 | 1.98 | 0 |
  | 7 | 22 | 23 | 2.52 | 1 |

  - The minimal total degree of a nonzero polynomial vanishing on all N^4 points is identical for d ∈ {−163, 5, −1000003}. The lower bound is certified; existence is confirmed mod two primes.
  - D_min/N^{4/3} = 1.39–1.65, rising towards 6^{1/3} = 1.82.
  - Masser's bound holds everywhere. Its constant 3^{−4/3} = 0.23 is lossy by about 7×, but its exponent 4/3 (rank 4 in 3 coordinates) is visibly the true one.
  - Our observation, not a claim of any paper: D_min can lie one below the dimension count (N = 4, 5, 7), so the projected box is not in general position for total degree.
  - Degenerate map d = 2: D_min = 5, 7, 9, 11 = 2N − 1 for N = 3–6. This is linear in N, as the explicit polynomial Π_s(z1 − z3 − 2√2 s) predicts.
- **(5d) Guo Lemma 3.3.**
  - Exact threshold: random G with |G| = (p0+1)/2 (so 2|G| = p0+1). There were 40 cases with d ∈ {−163, −7, 5, 13, −1, 229, −3}, inert p0 ∈ [11, 61] and s0 from 1 up to (p0−1)/2. All 40 are injective, certified because the rank mod 2^61−1 equals p0·s0.
  - Guo's actual grid m = ⌈√p0⌉ with s0 ∈ {⌊p0/30⌋, 3, 5}: injective in all 21 cases.

**Verdict, step 5: no_issue_found_in_inspected_portion** (OAI Lemma 3, Cor 4, (A), greedy; Banks §3, §4; Kerr Lemmas 6–7 with Masser; Guo Lemma 3.3).

## 2. Step 6: concentration of the degree in the Frobenius-divisible coordinate

### 2.1 Principal source (OAI)

**Lemma 6** (l.517–550). There are absolute c0 = (4·97²)^{−1} and C0 = 192 such that, for fixed H ≥ 1 and N large in terms of H, S1 ≥ c0MH^{2/3}U and S2 ≤ C0MH^{−1/3}U. Hence S2/S1 ≤ (C0/c0)/H.

**Verification.**
- **Weight bounds.** w(α) ≤ 96H^{2/3}U gives α2, α3 ≤ B := 96H^{−1/3}U, so S2 ≤ 2MB = 192MH^{−1/3}U.
- **Q0.** H^{−1/3}U ≥ N ≥ 1 (from H ≤ N), so ⌊B⌋ + 1 ≤ (97/96)B and Q0 = (⌊B⌋+1)² ≤ 97²H^{−2/3}U².
- **Sorted first coordinates.** At most Q0 retained indices share a value of α1, so b_i ≥ ⌊(i−1)/Q0⌋.
- **Sum.** Writing M = kQ0 + r, Σ = Q0k(k−1)/2 + kr = M²/(2Q0) − M/2 + r(Q0−r)/(2Q0).
- **Large N.** If M ≥ 2Q0, which holds when H^{2/3}N^{4/3} ≥ 2·97², then S1 ≥ M²/(4Q0) ≥ MH^{2/3}U/(4·97²), using N^4 = U³.
- OK. Banks Lemma 4.2 is identical, with his B = ⌊96H^{−1/3}M⌋ + 1 being OAI's ⌊B⌋ + 1.

**Cross-sources.**
- **Banks.** H = 9216·97² = 12·C0/c0, so S23 ≤ S1/12. The condition H ≥ 8·97³ gives H^{2/3} ≥ 4·97², and then S1 ≥ N^4M (re-checked in s8 (9a); part 1 s3).
- **Kerr (weight 8).** We derived that, for monomials i + w(j+k) ≤ D, Σ(j+k)/Σ i → (D⁴/(12w³))/(D⁴/(24w²)) = 2/w. So W/Σi → 1 + 2/w, and Kerr's leading comparison needs (¾)(1 + 2/w) < 1, i.e. **w > 6**. Kerr's w = 8 gives 5/4, with 13/10 placed between 5/4 and 4/3. The exact counts converge at the O(1/D) rate (s6 (6b)).
- **Guo.** λ = (s0−1)/(p0−1) < 1/30 holds because s0 = ⌊p0/30⌋ ≤ p0/30. The coefficient of λ in (3.11) is 2 log p0 − log b0 > 0, since b0 ≤ p0, so substituting the upper bound for λ is legitimate.

### 2.2 Toy replay (s6 (6a))

- **Setup.** Greedy selection modulo split primes P < 2^26. Selections agree modulo two primes, and are identical for the fields tested at each N.
- **A-priori bounds.** w_max ≤ 96H^{2/3}U and S2 ≤ 192MH^{−1/3}U hold for every toy with H ≤ N.
- **S2/S1 values.** Monotone decreasing in H:
  - N = 4, d = −163: 1.467 (H=1), 0.788 (2), 0.386 (4), 0.171 (8), 0.078 (16), 0.033 (32).
  - N = 5: 1.670, 0.862, 0.410, 0.191, 0.088, 0.038 at H = 1, 2, 4, 8, 16, 32.
  - The values sit somewhat below the simplex-centroid heuristic 2/H.
- **Leading coefficient.** The first term (¾)(1+S2/S1) of (master) drops below 1 at H = 6 (N = 4) and H = 8 (N = 5).
- **Lossiness of Lemma 6.** Lemma 6's guaranteed ratio 7,226,112/H needs H > 2.2×10^7 for the same purpose. The bound is very lossy (T6, carried over) but correct, and only its existence matters.

**Verdict, step 6: no_issue_found_in_inspected_portion.**

## 3. Step 7: Archimedean size bound

### 3.1 Principal source (OAI (upper), l.562–577)

For every embedding ν and every n ∈ E_N, |ν(θ_n)| ≤ (N−1)(1+√|d|)(1+√2) ≤ 8N√q. Hadamard's inequality over the 4 embeddings then gives
¼log|N(Δ)| ≤ (M/2)log M + (S1+S2)(log N + ½ℓ + log 8).

**Verification.**
- (1+√|d|)(1+√2) ≤ 2√|d|·2.415 < 8√q, using |d| ≤ q.
- Each entry of ν(R_α) is a product of conjugates of θ_n, so it is ≤ (8N√q)^{|α|}, and each row norm is ≤ √M·(8N√q)^{|α|}.
- |N(Δ)| = Π_ν |ν(Δ)|.
- OK. Banks Lemma 5.1 is identical, since √(N^4) = N² gives 2N^4 log N = (M/2) log M.

### 3.2 Cross-sources

- **Kerr (Lemma 3 and the norm step of Lemma 5).**
  - Coefficient-box size: (1+√2)(1+√|q|) ≤ 8√|q|.
  - ‖θ‖, ‖σθ‖, ‖στθ‖ ≤ (N−1)(1+√|q|)(1+√2) ≤ B = 8N√|q|.
  - In each embedding, |F(point)| ≤ Σ‖c_{ijk}‖B^{i+j+k} ≤ 2rH = P/2.
  - F(point) ∈ PO and O ⊂ O_K, so a nonzero value has |N| ≥ P^4 > (P/2)^4. Hence F(point) = 0. OK.
  - The degree-4 norm requires [K:Q] = 4, which fails only at q = 8 (M1).
- **Guo (coordinate bound, Lemma 3.2, (3.11)).**
  - ‖u ± vt‖ ≤ (m−1)(1+√|d|) < √p0(1+√q) ≤ b0.
  - r!/(r−j)! ≤ p0^j.
  - b0 ≤ p0 follows from p0 ≥ 4q, which gives w_{r,s} = (p0/b0)^{s0−1}b0^{r+s}.
  - Lemma 3.2 was re-derived (CRT image count, half-open box injective mod d0).
  - Σ(r+s) = p0s0(p0+s0−2)/2.
  - The identity 2(s0−1)log(p0/b0) + (p0+s0−2)log b0 = 2(s0−1)log p0 + (p0−s0)log b0, divided by p0−1, gives log b0 + λ(2 log p0 − log b0) exactly.
  - Coefficients 11/20, 29/60 and 29/30 (exact fractions, s8 (8a)). OK.

### 3.3 Exact checks

- **(7a) OAI/Banks sandwich (s6).**
  - N(Δ) was computed exactly as the determinant of the 4M×4M integer regular representation (python-flint), for 8 toys with M = 16 and M = 81.
  - In every toy: N(Δ) ≠ 0; v_p(N(Δ)) ≥ 4E_p for admissible p; and Σ_{adm} 4E_p log p ≤ log|N(Δ)| ≤ (actual per-embedding Hadamard) ≤ 4 × OAI (upper).
  - Example, d = −163, N = 3, H = 2: 439.2 ≤ 3882.2 ≤ 6398.9 ≤ 9871.8.
  - At toy sizes the gap between the two sides is large, as expected. Few admissible primes are ≤ max α1 and U is tiny, so the toys certify only that both inequalities are correctly oriented and that Δ ≠ 0.
  - Our tie-breaking rule differs from part 1's, which shows that the conclusions do not depend on it.
- **(7b) Guo Lemma 3.2 chain (s6).**
  - Exact integer ι in 7 toys with p0 ≥ 4q, so that Guo's w_{r,s} apply.
  - G = gcd of maximal minors, computed as the product of the row-HNF diagonal (A = U[T;0]).
  - In every toy: v_p(G) ≥ H_p for every inert p ≤ p0 (equality for most p); H ≤ Σ_P v_p(G)log p ≤ log G ≤ log covol ≤ Σ log‖col‖₂; H ≤ n log n + Σ log w_i; and ‖ι(e_{r,s})‖_∞ ≤ w_{r,s}.
  - Example, d = −7, p0 = 41, s0 = 2: 338.6 ≤ 461.7 ≤ 1585.5 ≤ 3949.8 ≤ 4810.7, and H ≤ 6299.0.
  - The loss in Lemma 3.2 at toy size is the n log n term together with sup-norm weights that use b0 for every derivative order. Both are lower order asymptotically: n log n = o(p0²s0 log p0).

**Verdict, step 7: no_issue_found_in_inspected_portion.**

## 4. Step 8: the exponent gap (the heart)

### 4.1 OAI (master), l.663–719, re-derived

Combining (upper) with (lower) and dividing by S1 log U gives
1 ≤ ¾(1+ρ) + (C + ½(1+ρ))ℓ/log U + Cδ log U/ℓ + (C_H + (1+ρ)log 8)/log U + (CMU + ½M log M)/(S1 log U), where ρ = S2/S1. We re-derived it term by term, using log N = ¾ log U and log M = 3 log U.

**Order of choices (checked for circularity).**
1. Choose H, absolute, so that (C0/c0)/H ≤ 1/12. The first term is then ≤ 13/16 once N ≥ N0(H).
2. Choose γ, absolute, using only the H-independent bound ρ ≤ 1/12. Since log U/ℓ → 4γ/3, the second term tends to ≤ (C + 13/24)·3/(4γ) < 1/16.
3. Let q → ∞ along the hypothetical sequence with δ → 0. Term 3 = Cδ·(4γ/3 + o(1)) → 0, term 4 → 0, and term 5 ≪ H^{−2/3}/log U + H^{−2/3}/U → 0.

The upper limit is ≤ 13/16 + (something < 1/16) < 7/8 < 1, a contradiction. No limit is interchanged: every constant is absolute or depends only on the already-fixed H, and the side conditions N ≥ H, U ≥ 3 and H^{2/3}N^{4/3} ≥ 2·97² hold eventually.

**The source of ¾.** It is log N / log U for a rank-4 lattice seen through 3 coordinates. It is exactly the exponent that the zero estimate makes sharp (step 5: D_min ≍ N^{4/3}), so the arithmetic gain has to come from Frobenius (steps 2–4).

### 4.2 Cross-sources

- **Banks (7.3) and Step 4, re-derived.**
  - (3/16)log M ≤ C1δ(log M)²/L + (C2+8/5)L. The constants needed are 2N^4M ≤ 2S1, (3/2)N^4 log M ≤ S1 (since 3 log M/(2M) ≤ 1 for M ≥ 8), S1 + S23 ≤ (13/12)S1, log H + 3 + (13/12)log 8 = 23.53 < (24/23)L, and 1/(2H) + 13/24 + 24/23 = 1.5851 < 8/5.
  - Dividing by log M and using (4/3)ωL ≤ log M ≤ (4/3)(ω+1)L gives 3/16 ≤ (4/3)(ω+1)C1δ + 3(C2+8/5)/(4ω) ≤ (4/3)(ω+1)C1δ + 3/32.
  - δ0 = 9/(128(ω+1)C1) solves the equality to 25 digits (s8 (9a)), and ω = 22 ≥ 8(C2+8/5) = 21.763. OK.
- **Kerr, (9) ⇒ (11) and the theorem.**
  - Σ_S E_p log p = (D⁴/1536)Σ_S log p/p + O(D³Q).
  - W log B + r log(32r√|q|) = (D⁴/1536)(5/4)log B + O(D³ log(D|q|)).
  - With Q = D/(log N)², the error D³Q = D⁴/(log N)² is o(D⁴ log B). So 13/10 > 5/4 suffices for all large N, uniformly in q, because |q| = N^{1/γ}.
  - In the theorem: Σ_S log p/p ≥ (4/3)log N − O(log N/γ) − O(εγ log N) − o(log N), against (13/10)(1 + 1/(2γ))log N + O(1).
  - The gap 4/3 − 13/10 = 1/30 absorbs the errors for γ large, then ε small, then |q| large. OK.
  - The PDF text layer shows "log Q = 34 log N". The LaTeX source has \frac43, so this is a pdftotext artifact, not a typo (P2-8).
- **Guo (5.11)–(5.15).** All certificates were recomputed in part 1. Here the whole chain was re-evaluated with exact logarithms and the paper's own error terms at δ = 1/100 (s8 (9b)):
  - **Positive margin everywhere.** The margin is > 0 on 65 conductors in [3, 10^15].
  - **Worst case q = 3.** The minimum is **0.3256**. The paper's rational version gives (451/60)log 3 − 8 = 0.2579, slightly smaller because of rounded certificates.
  - **Large q.** The margin grows linearly in log q, reaching 360.4 at 10^15.

### 4.3 The unified comparison (s8 (8a)–(8b))

Every proof yields an unconditional bound S_−(X) ≤ κ log X + e log q + O(1) at X a power of q.

| Proof | κ as used | κ intrinsic limit | Source of the exponent |
|---|---|---|---|
| OAI/Banks | ¾(1 + 1/12) = 13/16 | ¾ (H → ∞) | rank 4 in 3 coordinates |
| Kerr | ¾·13/10 = 39/40 | ¾·5/4 = 15/16 at w = 8; → ¾ as w → ∞ | Masser μ = 4/3; weight w > 6 needed |
| Guo | ½ + (3/2)/30 = 11/20 | ½ (λ → 0) | point height √p0 per unit degree p0 (Stepanov) |
| Barreto/van Dijk | ½ | ½ | (cited by Guo) |

- All κ lie in [½, 1).
- κ ≥ ½ is forced by the prime ideal theorem, since S_−(x) ~ ½ log x for a fixed field. So no version proves something false about ordinary fields.
- Guo's limiting κ = ½ is asymptotically sharp in the x-aspect.

**The generic chain.** It reads (1−κ)A − K ≤ bδA² at X = q^A, with optimum **δ\* = (1−κ)²/(4bK)** at A\* = 2K/(1−κ).
- **Banks.** With 1−κ = 3/16, b = C1 and K = C2 + 8/5, the continuous optimum is **3.244×10^−3** at log M/L = 29.0 (ω\* = 21.76). With ω = 22 and log M = (4/3)ωL exactly, since N = q^ω is an integer power, the value is 3.209×10^−3. Banks states 81/(5888e^{3/2}) = **3.070×10^−3**, using the conservative slack (ω+1) (P2-7, harmless). Part 1 found that the integer-ω optimum over λ is 3.108×10^−3.
- **Guo, as q → ∞.** The supremum of min(2((9/20)A − B − 29/60)/(AB + A²/2), 1/(A+B)) is **0.0609** (part 1: 0.06095).
- **Why the constants differ.** The factor (9/20)²/(3/16)² = 5.76 comes from κ alone; the analytic constants account for the rest. Asymptotically Guo's chain gives about 19 times Banks's continuous optimum (0.061 versus 0.0032). For the stated values the ratio is about 3.3 (1/100 versus 3.07×10^−3), because Guo fixes one parameter pair for all q ≥ 3 and his worst case is q = 3. There is no disagreement between the two.

**Verdict, step 8: no_issue_found_in_inspected_portion.**

## 5. Step 9: parameters and small conductors

**OAI** (l.665–676). The proof argues by contradiction along a sequence.
- Bounded conductors carry finitely many characters.
- L(1,χ) ≠ 0 and analyticity give a zero-free neighbourhood of 1, so min(1−β) > 0.
- Hence q → ∞ can be assumed, and Q(√d) ≠ Q(√2) eventually, so d = 2 (q = 8) is excluded.
- The parameter conditions hold as soon as q^γ ≥ H = 8.7×10^7 for Banks's explicit H (s8 (9a)). OK.

**Banks.** Banks takes q0 = 10^{10}, which is forced by his bookkeeping (L > 23), not by the method.
- Step 1 conditions were re-checked: 319 ≤ H ≤ q ≤ N, M ≥ 8, and d ≠ 2 for q ≥ 9.
- For q < 10^{10} the all-q constant cites LZZ Thm 1.1, which is unverified (U3, carried over).
- *Cross-check consequence:* if Guo's Theorem 1.1 is accepted, its 1/100 > 3.0×10^−3 for every q ≥ 3 makes the LZZ input unnecessary for the statement "c = 3.0×10^−3 for all q".

**Kerr.** Small |q| is implicit (T1). q = 8 lies genuinely outside the argument (step 5 witness), and finiteness covers it (M1).

**Guo.** A single choice, y = q^6 and x = q^70, is made for every q ≥ 3. The Lemma 5.1 hypotheses hold for all q: 76δ ≤ 0.76 < 1, q^6 ≥ max(q, 100), and β > ½. The q-dependent error terms f_k(q) decrease, so q = 3 is the worst case, which is confirmed numerically in §4.2. App. A gives 1/64: the chain with (46, 4) covers q ≥ 7, and positive period blocks cover q = 3, 4, 5. There is no primitive conductor 6 (part 1).

**Small conductors, the computed truth** (s8 (9c), **uncertified**, grid only).
- The check covered all 1820 fundamental discriminants with 3 ≤ |D| ≤ 3000, including D = 8.
- L(σ,χ_D) > 0 at 23 grid points in [½, 1], including σ = 1 − 1/(5 log q) and 1 − 1/(100 log q). The minimum value is 0.0225, at D = −2787, σ = ½.
- The Euler–Maclaurin routine agrees with mpmath to 2×10^−11 at σ ∈ {0.5, 0.8}, and with the exact digamma formula at σ = 1.
- This is consistent with every stated constant, and far weaker than the certified LZZ computation (q ≤ 10^{10}).

**Verdict, step 9: no_issue_found_in_inspected_portion.** The carried items are T1, M1 (sharpened) and U3.

## 6. The core mechanism, as seen from steps 5–8

The three reported labels describe one mechanism. Steps 5–8 are where they differ.

- **Divisibility (steps 2–4).** The same in all proofs. Frobenius at inert p is conjugation, which buys p-adic divisibility of order (degree)/p in the Frobenius-divisible coordinate.
- **Nonvanishing (step 5).** Implemented three ways, each sharp in its own sense:
  - OAI's interpolation lemma, whose spanning threshold equals the dimension floor in toys;
  - Masser's zero estimate, where 4/3 is the true exponent;
  - Guo's Stepanov count, which equals the dimension count.

  None of them sees χ: they depend only on the field (OAI/Kerr) or the point set (Guo).
- **Degree concentration (step 6).** Makes sure the non-divisible coordinates carry little degree: S2/S1 small, w > 6, or λ ≤ 1/30.
- **The exponent gap (step 8).** Compares the "size per unit degree" log N = ¾ log U (or ½ log p0 + ½ log q in Guo) with the "divisibility per unit degree" Σ_{inert p ≤ U} log p/p.
- **Where the zero enters.** A Siegel zero would make the divisibility side ≈ log U, against κ log U with κ < 1. Only through step 1 does the zero enter.

So "interpolation determinants" (OAI/Banks), "Siegel-lemma pigeonhole plus zero estimate" (Kerr) and "integer coefficient counting plus polynomial congruences" (Guo) are dual implementations of the transcendence method: Laurent's interpolation determinants versus Siegel's lemma. They are applied inside Z[√d] (and Z[√d, √2]), with Frobenius-equals-conjugation as the arithmetic input.

## 7. Guo (second half) and Kerr (key step): audit summary

- **Guo, full paper.** The whole paper was inspected in part 1. Here we independently re-derived:
  - Lemma 3.2;
  - Lemma 3.3, together with its general subset form;
  - (3.8)–(3.10), the parts used by Lemma 3.2;
  - the coordinate bound and (3.11);
  - (3.12)–(3.15): the min-sum identity with defect (k−s0)(k−s0+1); the floor-sum identity pa(a−1)/2 + ab = p0(p0−p)/(2p) + b(p−b)/(2p); and Σ⌊r/p⌋² ≤ p0(p0−1)(2p0−1)/(6p²);
  - the assembly of (3.16)–(3.17), with R(p0) < 141/100 + 1/50 + 53/15 + 77/75 = 599/100;
  - the small cases (59/10 and 623/300);
  - §5, as a whole chain with exact logs;
  - App. A.

  No issue was found. Two exact replays support this: Lemma 3.3 injectivity at its sharp threshold (s5 (5d)) and the Lemma 3.2 chain (s6 (7b)). **Verdict: no_issue_found_in_inspected_portion.**
- **Kerr, key step.**
  - Lemma 5 (pigeonhole, norm step, asymptotics (9) ⇒ (11)) was re-derived.
  - Lemma 6 matches Masser's Theorem 1 as printed (scan p. 82). The basis hypothesis is satisfied (M2).
  - Lemma 7 was re-derived.
  - The final degree comparison is OK.
  - The single substantive caveat is q = 8: the explicit witness μ ≤ 1 and the degree-(3N−2) vanishing polynomial (P2-5). Only implicit finiteness covers this case.

  **Verdict: no_issue_found_in_inspected_portion,** with M1 sharpened, M2 and T1.

## 8. Are the claimed constants consistent?

Yes. All of them are lower bounds for the same quantity, inf (1−β)log q, and a smaller constant is a weaker theorem, not a disagreement.

| Source | Constant | Range | What explains it |
|---|---|---|---|
| Guo | 1/100 | all q ≥ 3 | fixed (A,B) = (70,6); worst case q = 3 (margin 0.33 exact, 0.26 rational); his chain gives 0.0102 at q = 3 (part 1) and 0.061 as q → ∞ |
| Guo App. A | 1/64 | all q ≥ 3 | (46,4) for q ≥ 7, positivity for q = 3, 4, 5 |
| Banks | 81/(5888e^{3/2}) = 3.070×10^−3 | q ≥ 10^{10} | κ = 13/16 effective; continuous optimum 3.244×10^−3, ω = 22 exact 3.209×10^−3 |
| Banks | 3.0×10^−3 | all q | needs LZZ (U3), or Guo's theorem |
| Kimura v2 | 5.811×10^−4; 0.005965 (log q ≥ 35.01); 0.01015 (log q ≥ 10^4) | as stated | Read in part 1 only for the statements |

All of these lie far below the computed truth for small q (s8 (9c); LZZ: ≥ 1/5 for q ≤ 10^{10}) and below ½log 3, the value under GRH.

## 9. Consequences: L(1,χ) and class numbers (s10)

These checks are independent of part 1. They use the analytic class-number formula instead of reduced forms, and a re-derived bound.

- **Analytic class numbers.** h(D) = w√|D|L(1,χ)/(2π) for all 911 imaginary fundamental |D| ≤ 3000.
  - L(1,χ) was computed by Euler–Maclaurin and checked against −(1/q)Σχ(a)ψ(a/q) to 2×10^−12.
  - Every value is integral to 10^−6. The h = 1 list is {3, 4, 7, 8, 11, 19, 43, 67, 163}.
  - (count, max|D|) for h = 1..5 is (9,163), (18,427), (16,907), (54,1555), (25,2683). This equals Watkins (2004) Table 4 and agrees with part 1's reduced-form computation.
- **Implied bound, re-derived** (auditor's derivation, the same mechanism as Kimura's Lemma 8).
  - With b0 = 1 − c/log q, there is no zero in [b0, 1), so L(b0,χ) > 0, and ζ(b0)L(b0,χ) < 0 can be dropped.
  - With H_{b0}(t) ≥ 1, |L(b0,χ)| ≤ e^c(3/2 + log q), and the unconditional paired-tail identity, this gives L(1,χ)log q ≥ c e^{−kc}[1 − e^c(3/2+log q)e^{kc/2}q^{−k/2} − (q+1+(k/2)log q)e^{kc}q^{−k/2}].
  - At q = 10, k = 4, c = 1/100 the value is 0.007671, which reproduces part 1.
  - For all four constants (1/100, 1/64, 3.0×10^−3, 5.811×10^−4) there are **0 violations** over 1820 fundamental D (imaginary and real, q ≥ 10). The smallest data/bound ratio for c = 1/100 is 131 (D = −163; part 1 found 163× against the uniform constant 0.00767).
- **When the bound becomes informative.** h > 1 and h > 100 are forced, respectively, only for:

  | Constant | h > 1 for \|D\| ≥ | h > 100 for \|D\| ≥ |
  |---|---|---|
  | 1/100 | 3.1×10^7 | 7.8×10^{11} |
  | 1/64 | 1.2×10^7 | 3.1×10^{11} |
  | 3.0×10^−3 | 4.4×10^8 | 1.0×10^{13} |
  | 5.811×10^−4 | 1.6×10^{10} | 3.3×10^{14} |

  - These thresholds use the q-optimized bound. Part 1's 5.3×10^7 used the uniform constant 0.00767.
  - The ordering is monotone in c.
  - Every threshold lies far beyond the Heegner range, so class-number tables cannot contradict any of the constants. They can only confirm that nothing implied is violated, and nothing is.

## 10. Barriers: why steps 5–8 do not prove too much

- **The prime ideal theorem / Chebotarev.** Every κ lies in [½, 1) (§4.3), and Guo's limiting κ = ½ is exactly the truth for a fixed field. A κ < ½ would have signalled an error. None occurs.
- **The q-aspect** (s8 (8c)).
  - From Guo's (3.1) and Rosser–Schoenfeld: if every odd prime ≤ x is inert, then log x ≤ (29/27)log q + 18.2.
  - Exponent 29/27 > 1 is *weaker* than the trivial bound (a ramified prime p | q is non-inert). Barreto's shape gives about q^{1/2}, which is weaker than Linnik–Vinogradov/Burgess q^{1/4+ε}.
  - Data: over 115,502 fundamental discriminants with 10^4 ≤ |D| ≤ 2×10^5, max log p1/log q = 0.362 (D = −10987, p1 = 29).
  - So the arithmetic layer is not "too strong" in q. Its whole strength is the x-slope κ < 1, which matters only at X = q^{large}, exactly where a Siegel zero would force inert dominance.
- **The zero estimate is χ-blind and field-uniform** (s5).
  - The nonvanishing steps do not see the values χ(p) at all, so they cannot "know" about a Siegel zero.
  - Their exponent 4/3 is the true one, and they fail exactly when the field degenerates (d = 2).
  - The only χ-dependent input to steps 5–8 is *which* primes are inert, and that enters through Frobenius, an algebraic property of Z[√d]. The Liouville or "pretentious" model λ(p) ≡ −1 has no such ring.
  - Part 1 (C5) shows that the sign pattern alone violates (3.1) once x > q^{1.66–4.27}.
- **Parity.** None of the steps is a sieve. The decisive information is integrality of an algebraic object (Δ, F(point), ι), which the sieve axioms do not see.
- **Deuring–Heilbronn.** Steps 5–8 make no use of zeros at all. The only use of the hypothetical zero is step 1's prime bias, which is the input that Deuring–Heilbronn and Linnik also use. In a Siegel world the inert dominance would extend to q^{c/δ}, which contains X = q^{70} (Guo) or q^{4γ/3} (OAI). The contradiction therefore arises inside the regime the Siegel world itself predicts. Conditional "illusory world" theorems become vacuous; none is contradicted.
- **Siegel's ineffectivity.** The proofs are effective: Guo and Banks give explicit constants. The resulting h ≫ √|D|/log|D| supersedes Goldfeld–Gross–Zagier's log|D|. No theorem forbids this.

## 11. Classification of findings (part 2)

| ID | Location | Classification | Finding |
|---|---|---|---|
| P2-1 | OAI Lem 3, Cor 4, (A), greedy, Lem 6, (upper), §6 (master) | no_issue_found_in_inspected_portion | Steps 5–9 re-derived line by line; order of parameter choices checked; toy replays consistent |
| P2-2 | Banks §3 (Prop 3.4, Cor 3.5), §4 (Lem 4.1, 4.2), §5 (Lem 5.1), §7 | no_issue_found_in_inspected_portion | Every inequality and constant of §7 recomputed; δ0 identity to 25 digits |
| P2-3 | Kerr Lemmas 5–7, Masser Thm 1, proof of Thm 1 | no_issue_found_in_inspected_portion | Masser re-read on the scan; Lemma 7 re-derived; weight threshold w > 6 derived (w = 8 used) |
| P2-4 | Guo Lemma 3.2, 3.3, (3.11)–(3.17), §5, App. A | no_issue_found_in_inspected_portion | Re-derived; Lemma 3.3 shown sharp (Stepanov count = dimension count); exact-log margin 0.3256 at the worst conductor q = 3 |
| P2-5 | Kerr, q = 8 (sharpens M1) | missing_hypothesis (harmless) | Witness: γ1, γ4, γ2−2γ3 are Z-independent in the plane x1 = x3, so μ ≤ 1. F = Π(x1−x3−2√2 s) of degree 3N−2 vanishes on all points. Kerr's Theorem 1 covers q = 8 only through the implicit finiteness argument (T1). One conductor. |
| P2-6 | OAI Lem 3 / Banks Prop 3.4 hypothesis "Q-independent kernel coordinates" | no_issue (necessity witness) | d = 2: the budget holds at N = 53 (t = 1396) but spanning needs t ≥ 1430. The hypothesis is load-bearing and correctly stated; d = 2 is excluded by every source. |
| P2-7 | Banks §7, (7.1) | typo_or_presentation (conservative slack) | N = q^ω exactly, so log M = (4/3)ωL. The (ω+1) slack costs 4.4%: 3.209×10^−3 would follow from the same chain. Harmless. |
| P2-8 | Kerr PDF text, proof of Thm 1 | no_issue (extraction artifact) | pdftotext renders \frac43 as "34". The LaTeX source reads log Q = (4/3)log N. Recorded so that later readers do not mistake it for a typo. |
| P2-9 | OAI Lem 6 / Banks Lem 4.2 constants | typo_or_presentation (lossy, carried T6) | The guaranteed S2/S1 ≤ 7.2×10^6/H versus toy S2/S1 below 1/3 already at H = 6–8. Correct but very lossy; only existence matters. |
| U3 | Banks all-q constant | unresolved_ambiguity | LZZ computation unverified. Would be unnecessary if Guo's theorem is accepted. |
| U4 | OAI Lean development | unresolved_ambiguity | Not replayed |
| T1, T3 | Kerr small \|q\|; Banks Lem 3.3 "Exercise" | typo_or_presentation | Carried over |
| — | all four sources, steps 5–9 | verified_error | **none** |
| — | steps 5–9 | suspected_gap | **none** |

## 12. Checks run (our own code)

Directory: `research/exploratory/riemann-observatory/experiments/code/claims_2026/siegel_l2_part2/`.
- Run with `python3 -I` on Python 3.13.18, python-flint 0.9.0, numpy 2.5.3, mpmath 1.3.0 and sympy 1.14.0.
- Outputs are saved as `*.out` next to each script.

| Script (sha256 prefix) | What it checks | Result |
|---|---|---|
| `s5_nonvanishing.py` (a72e7177) | Minimal spanning cube for OAI Lem 3 in 9 fields, N ≤ 5; aspect-ratio uniformity; d = 2 necessity witnesses (fibre bound, N = 53); Kerr q = 8 plane/μ ≤ 1 (sympy exact) and explicit vanishing polynomial; minimal vanishing degree vs Masser for N ≤ 7 in 3 fields; Guo Lemma 3.3 at the exact threshold (40 random G) and on Guo's grid (21) | 14 PASS / 0 FAIL |
| `s6_s7_concentration_size.py` (5a995b7a) | Greedy weighted selection (N ≤ 5, H ≤ 32) against Lemma 6 bounds; Kerr weight threshold 1 + 2/w; exact N(Δ) sandwich in 8 toys (flint regular representation); Guo Lemma 3.2 chain via exact HNF, Gram determinant and column norms in 7 toys | 6 PASS / 0 FAIL |
| `s8_s9_gap_parameters.py` (12e72354) | κ table (exact fractions); Guo (3.11) coefficients; closed-form δ\* for Banks and Guo; q-aspect bound and least non-inert prime data (115,502 D); Banks/OAI parameter conditions and the δ0 identity; Guo's chain margin with exact logs on 65 conductors; small-q L(σ,χ) > 0 grid (1820 D, uncertified) | 11 PASS / 0 FAIL |
| `s10_consequences.py` (a4372677) | Analytic class numbers (911 D, Watkins h ≤ 5); re-derived L(1,χ) bound for four constants (0 violations over 1820 D); thresholds for h > 1 and h > 100 | 5 PASS / 0 FAIL |

**Debugging notes, recorded so that nobody mistakes them for findings.**
- A first version of (5c) asserted *our own* guess that D_min equals the dimension-count degree. It failed at N = 4, 5, 7 (D_min is one lower). This is not a claim of any paper, and the check was rewritten to compute D_min exactly.
- A first version of (6b) used a tolerance (3×10^−3) tighter than the O(1/D) finite-size deviation at D = 6000. It was replaced by a convergence check.
- `mpmath.dirichlet` at s = 1 exhausted memory. Validation at s = 1 uses the exact digamma formula instead.

**Limits.**
- The toy sizes (N ≤ 7, M ≤ 2401; p0 ≤ 67; exact N(Δ) for M ≤ 81) test exact algebraic identities and the orientation of inequalities. They do not test the asymptotic regime U = q^{4γ/3} or X = q^{70}, which is covered by the derivations and by the exact-log evaluation of Guo's chain.
- Modular ranks certify full rank. Rank deficiencies are confirmed mod two primes, or forced by dimension or an explicit polynomial.
- The small-q L(σ,χ) check is a grid evaluation, not a certificate.

## 13. Not done in part 2

- The Lean replay (U4).
- The LZZ computation (U3).
- A page-level check of Davenport (U1) and Rosser–Schoenfeld (U2), carried over from part 1.
- Guo's cited hexagon and web sources (not load-bearing).
- Kimura's chain beyond its stated constants.
- Independent expert review. Nothing above substitutes for it.
