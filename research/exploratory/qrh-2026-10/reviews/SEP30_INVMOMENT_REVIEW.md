# Sep 30 marked inverse-moment engine (Section 17): statement diff against Oct 5, and the mechanized ledgers

```text
Status: REVIEW (bounded; external, unreviewed manuscript). Target 2 of SEP30_VERIFICATION_MAP.md.
  Verdict: the ledgers PASS. The statement diff is CONFIRMED at the level of statements only. This
  is not a verdict on Lemma 17.1, 17.2 or 17.6, and not a verdict on Theorem 1.1.
Scope: paper.tex Section 17. Statements: Lemma 17.1 (9250-9269 in the map; text 9296-9340) and
  Lemma 17.2 (9296-9340). Helpers: Lemma 17.3, Cor 17.4 and Lemma 17.5 (9348-9781). Proof of
  Lemma 17.2 (9789-11599): the terminal ledger 9870-9925, both Poisson transforms 10145-10913
  read at the identity level, and the ledgers 10913-11118, 11402-11474 and 11474-11599 checked
  line by line. Proof of Lemma 17.1 (11606-12341): the overlap reduction and initialization
  ledger. Lemma 17.6 (12343-12469).
Exact sources or dependencies:
  [OAI] pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
        standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (the scratch copy was re-hashed: identical).
  [O5]  paper2.tex at the same ref, SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
  Reviewed analogs: OCT5_R1_REDUCTION_POISSON.md, OCT5_R2_ITERATION_TRANSFER.md, OCT5_REVIEW_SUMMARY.md.
  Imported and NOT checked here: Lemma 14.3 (reflected energy, 7747-), eq:signal and
  eq:G-quadratic-refinement (950-970), Lemmas 4.4, 4.5 and 4.7, and Prop 5.1.
What was actually run: reviews/sep30_invmoment_ledger.py
  (SHA-256 076f904ab7016b5a27c73fb50246418884cfa24e410bc1534ee4c2a213dfb48f), written for this
  review, run as `python3 -I` and `python3 -I -O`. Both runs printed identical output
  (SHA-256 6532d4c2...9b27), with 120/120 checks passing in about 3 s.
  The 120 checks:
    * 7 statement-dictionary identities;
    * 10 exhaustive local-table checks (valuations up to 12);
    * 28 exact sympy identities;
    * 15 error-budget maxima;
    * 41 inequality checks, of which 24 carry exact Farkas certificates. The multipliers were
      found by LP, rationalized and re-verified as polynomial identities;
    * 21 failing controls, each of which perturbs a constant and exhibits an exact rational
      counter-witness or cycle;
    * 1 labelled MODEL check.
  The remaining text was read by hand. No Gauss sum or character value was computed.
Smallest remaining gap: inside Section 17, the first-Poisson character identification
  (10214-10245 -> eq. (C), 10279). It claims that CRT and sextic reciprocity leave on the u_1
  side the factors gamma_1(u_1) conj(chi_{u_1}(h)) chi_{u_1}(d_k R_1) prod chi_{u_1}(p^{t_p}),
  together with the fixed-ray quotient G(u_1 u_2^{-1}) R(u_1 u_2^{-1}, P_T). This identity is
  new relative to Oct 5. The exponent table that follows from it was verified exhaustively, but
  the identity itself was neither re-derived from eq:signal nor replayed numerically.
  Outside the section, the terminal branch bounds of Lemma 14.3 enter (old-eq:4.6), via
  (inverse-terminal-width) at 9884. All three terminal estimates rest on them, and they are
  target 1 of the map.
```

RH remains unsolved. This note checks bookkeeping in one block of an external manuscript that claims a fixed zero-free half-plane Re s > 7/8. Nothing here bears on the critical line. Passing ledgers do not show that the analytic estimates which supply those exponents are true.

## 1. Verdict

1. **Ledgers: PASS.** Every displayed exponent identity, error budget and inequality in "The new canonical data and their admissibility", "The energy exponent" and "Order of choices and termination" holds exactly. So do those in the terminal (short-completion) ledger and in the Lemma 17.1 initialization ledger.
   * The margin losses 5η and 7η, the row decrease 2(ℓ+V)−8η, the step loss 40η and the initialization losses 9η and 22η are all **tight**: each certificate has zero constant term, and lowering any of these constants by one unit of η fails, with an exact witness.
   * Termination is genuine. The row length M drops by at least 3d/2 > d at each nonterminal passage, so the recursion stops before depth D = ⌈(M_max+2)/d⌉+1. The margin decays to c_* − 7Dη ≥ c_*/2, and the ε budget is D(40η+τ+π) ≤ 3ε/4.
2. **Diff against Oct 5: confirmed for statements, refuted for proofs.**
   * *Lemma 17.2 at z_0 = 0.* Its statement is a special case of [O5] `prop:canonical` (κ = c_*), combined with `lem:remove-exclusions` and positivity.
   * *Lemma 17.1 at z = 0.* Its statement is the normalized form of [O5] `thm:ms`, with θ = (m−r)/r.
   * *The proof of Lemma 17.2 is a different recursion.* It is not a normalized form of the R2-reviewed descent, so the R2 PASS cannot be transferred to it, not even at z_0 = 0. The marked case z_0 > 0, which is what Prop 19.2 uses, rests entirely on the new proof.
3. **Two Poisson transforms.** Lemma 17.5 is [O5] `lem:poisson` verbatim. About half of the arithmetic identities are reviewed Oct 5 identities in new clothing; §4 lists the 11 new ones.

## 2. Task 1: statement comparison and parameter dictionary

### 2.1 Lemma 17.1 against [O5] `thm:ms` (paper2 679-689)

| [O5] | Sep 30 | check |
|---|---|---|
| `A_u(D) = Σ μ ν χ_n(u) W(N n/D)` | `M_u(Z^r;W) = Z^{-r/2} Σ μ ν χ_n(u)^{ε_χ} W(q_n/Z^r)` | D = Z^r |
| rows `0 < N(u) ≤ D^{1+ϑ}` | rows `0 < q_u ≪ Z^m` | m = (1+ϑ) r |
| bound `D^{2+ϑ+ε}` | bound `Z^{m+ε}` | −r + r(2+ϑ) = m exactly (A1) |
| `0 < ϑ ≤ 1/10` | `r ≤ m − c_1`, `2r ≤ 3m − c_2` | ϑ r ≥ c_1 (A2). The second condition is redundant once m ≥ c_2 − 2c_1 (A7) |
| `‖W‖_{C^k}`, k = k(ϑ,ε) | "finitely many seminorms"; norm twists at a fixed polynomial cost | see 2.3 |

At z = 0 and ε_χ = +1, Lemma 17.1 with (m−r)/r ∈ (0, 1/10] is exactly `thm:ms`. The sign ε_χ = −1 is the complex conjugate of the case (ν̄, W̄), and the text itself reduces it this way at 11712. **Delta: the full r range.**
* Lemma 17.1 also claims (m−r)/r > 1/10 and r → 0.
* For m ≥ 2r + ε the bound is the trivial completion bound.
* For 1/10 < ϑ < 1, the Oct 5 proof of `thm:ms` uses ϑ only through κ = ϑ/2 > 0 in sec:completion (1612-1630). A grep of paper2 finds the restriction ϑ ≤ 1/10 only in statements (271, 296, 680, 695, 1001, 1614). R1's reduction was not re-reviewed for ϑ > 1/10.

### 2.2 Lemma 17.2 against [O5] `prop:canonical` (paper2 1261-1277; family eq:energy 944)

| [O5] | Sep 30 | check |
|---|---|---|
| X, F, ℋ | Z^N, Z^V, Z^M | — |
| `(1/(XF)) Σ_f Σ_k |Σ_n a_ξ χ_n(k) χ_n(f)^4 W|²` | `Z^{-V} Σ_f w(f) Σ_k |Z^{-N/2} Σ_n ᾱγ_2 ν ρ χ_n(k) χ_n(f)^4 𝔡 W|²` | Z^{−V−N} = 1/(XF) (A3) |
| bound `D^ε Σ`, Σ = XF | bound `Z^{F_0+ε}`, F_0 = N+V | — |
| `ℋ ≤ Σ D^{−κ}` | `q_𝔯 ≤ Z^{F_0−M−z_0−c_*}`, `3M + 6z_0 + c_* ≤ 4F_0` | at z_0 = 0, Q ≥ 0 gives M ≤ F_0 − c_* (A4), and the second invariant is redundant (A5). For z_0 > 0 the two invariants are independent (A6) |
| f dyadic, unweighted | q_f ≍ Z^V, weight w(f) ≤ C d(f)^C | positivity, with w ≪ Z^ε on the bounded range |
| exclusions removed by `lem:remove-exclusions` | puncture ρ carried, with a norm cap | `lem:remove-exclusions` keeps Σ and ℋ, at a τ(r_0) ≪ Z^ε loss |

The conventions match where they were spot-checked: Sep 30 966-967 has γ_2³ = μα and γ_1γ_2 = μαG, the same as [O5] eq:gj (841-842).

**The deltas, precisely:**
1. **Marks.** These are the product-form slot coefficients 𝔡(n), with cap z_0. They force the second invariant 4F − 3M − 6z_0 ≥ c, which is binding only when z_0 > 0, and an extra −z_0 in the first invariant.
2. **Punctures.** These are carried as fixed punctures whose radical norm Q is part of the invariant, F − M − Q − z_0 ≥ c. Oct 5 removed exclusions instead.
3. **Divisor-bounded label weights.** The recursion produces child weights d(f)^{9+4K_slot} (eq:inverse-new-fibre, 11299). Oct 5 instead had the exact sign sum Σμ(e)μ(w) = τ(r)1_{f'|k'}.
4. **Moving twists.** See 2.3.

### 2.3 Moving twists and order dependence

Lemma 17.3, Cor 17.4 and the common log-Fourier density (eq:inverse-log-fourier, 10083) make the height dependence explicit. The degrees are finite for each fixed ε, but they are **not uniform in ε**:
* the tail order is A > 1 + (B_crude+T)/τ with τ ≤ ε/(4D) (F8);
* the Fourier and seminorm orders are chosen above A.

This is the same qualitative status as R2 finding F3 (k ≥ 5·4^{⌈4/ϑ⌉} in Oct 5). Lemma 17.3 asserts only that the orders are fixed *before* the external cutoff T_1 = Z^τ. That order of quantifiers is consistent (F10, F12).

Lemma 17.3 itself is a correct abstract backward induction on a finite DAG. No explicit order recursion is displayed, unlike Oct 5's J_{j+1} = 4J_j + 12. A MODEL run of its update rule, with assumed edge data (F14), shows that the orders are finite but grow very fast with depth: about 10^10 at depth 10. These numbers are illustrative only.

### 2.4 The proofs are not a diff

| | [O5] descent (R2) | Sep 30 Lemma 17.2 |
|---|---|---|
| induction variable | ℋ ≤ D^{jκ} | depth h, with row cap M ≤ M_max − hd |
| use of the completed/reflected estimate | Prop R on the short cube part at **every** level | Lemma 14.3 only at **terminal** nodes, where V < d and the cube dyad ℓ_1 < d |
| cube variable | Cauchy over b, then sup_b E(ℋ, L_b, F) | both copies b_1, b_2 kept inside the square |
| new label | f' = Cew | f_new = J C d_2 v', where **J = s J_2 is extracted from b_1 b_2** |
| collapse | exact sign sum (R2 script D) | weighted Cauchy (D) plus divisor fibre bounds |
| contraction | ℋ' < ℋ(ℋ/Σ)², a factor ≥ D^{2κ} | M − M_ch ≥ 2(ℓ+V) − 8η ≥ 3d/2 |
| frequency cutoff | supp Φ̂ compact, exact ranges | Schwartz kernels; tails discarded at Z^τ; outer masks 𝓑_1, 𝓑_2 |

At ℓ = 0 the Sep 30 contraction M_c = M − 2V − 2(A_i+t+g−θ) matches Oct 5's ℋ' ≤ ℋL/(ΣF) at L = X (C8). With cubes it does not: Oct 5 gives ℋ' ≤ ℋ/(N(b)³F²), whereas Sep 30 gives M − 4ℓ + j − 2V with j ∈ [0, 2ℓ+3η].

## 3. Task 2: the ledgers (script sections C-F)

| Ledger (lines) | Claims | Result |
|---|---|---|
| Terminal: (inverse-terminal-width) to (old-eq:4.9)-(4.11), 9884-9925 | (4.9) from the first invariant, V < d and ĥ < d+η. (4.10) needs O ≥ 0 and Q ≥ 0; its control without O ≥ 0 fails. (4.11) cancels O exactly. All three, plus π_ref, are strictly below F under c_node ≥ c_*/2, d ≤ c_*/200 and η, τ_ref, π_ref ≤ c_*/1000 | PASS (E15-E21). These constants have **large slack**: d ≤ c_*/20 or c_node ≥ c_*/8 would still pass |
| First Poisson scales, 10184-10453 | κ split and its 9η/2 budget; root and kernel; ŷ bound; H_c and its 12η budget | PASS (C1-C7, D1-D2) |
| Second Poisson scales, 10690-10770 | L_2 and its 10η budget; k_new ≤ M_c + η; M_c identity; λ budget 18η+τ; principal exponent F−B−j and its 26η+τ budget | PASS (C8-C9, D3-D7) |
| **Admissibility, 10913-11118** | Child lengths (6η, 4η); D_c transition identities; center inequalities g−θ ≥ −2η and j ≤ 2ℓ+3η from actual divisibility; Q_new ≤ Q + D_c + 4η; child margins ≥ c − 5η and c − 7η (including the δ_N forms); row decrease ≥ 2(ℓ+V) − 8η ≥ 3d/2; F_c ≤ F − ℓ − V + 5η; F_ch ≤ F + 11η | PASS (C10-C15, C18, D8-D10, E1-E10), all tight. Controls at 4η, 6η, 7η and η ≤ d/12 fail |
| **Energy exponent, 11402-11474** | κ_i + λ_c + C_c + 2F_c = F exactly, with every extracted length cancelling; per-side exponent F + 28η + 2δ_N + τ + π + ε_child ≤ F + 40η + τ + π + ε_child; both principal terms fit | PASS (C16, D11-D12, E11-E14). Control at 39η fails |
| **Order of choices and termination, 11474-11599** | Cap negative at depth D (already at depth D−1); c_h ≥ c_*/2; D·L_step ≤ 3ε/4; the backward-induction step; c_{h+1} = c_h − 7η matches the child hypothesis; tail orders; H_use ≤ 7F_max + 18η + τ; the quantifier order is a DAG | PASS (F1-F13). Controls: η ≤ ε/(40D) and η ≤ c_*/(7D) fail, and a cycle is detected |
| Init (17.1), 11606-12271 | D' = r+z−2G normalization; F_c = D'−P_1; root and kernel; κ_c + P_1 + 2F_c = m; margins m−r−2z+2G and 3m−2r−8z+10G+2P_1; actual margins ≥ c_1 − 9η − τ and c_2 − 22η − 3τ; both ≥ 3c̄/4; energy loss 11η + π ≤ ε/4; a priori ranges | PASS (C19-C25, D13-D15, E22-E26). Controls at 8η, 21η, η ≤ c̄/50 and η ≤ ε/80 fail |
| 17.6, 12343-12469 | H/P = U^{1/6}H^{5/6}; e(r) = max(1, (1+5r)/6) as c → 0; the raw-moment instance m = 1, r = 1/(1+c) satisfies both premises | PASS (C26-C28). The sixth-power column identity and the injectivity of (u,a) ↦ ua⁶ were checked by hand (valuations mod 6) |

The local tables of the first transform were checked exhaustively (B1-B9) over valuations v_1, v_2 ≤ 12 and a_ip ∈ {0,1}:
* t_p = a_1 − a_2 + 3π mod 6;
* the exponent 4a_i + 1_{t≠0}(1 ± t) + π(a_1+a_2) is the same on both sides, and is 0 or 4;
* ξ(n) = χ_n(J)⁴ 1_{(n, rad q_0)=1};
* R̂ − Â_1 − Â_2 + Ê = ŝ − 2ĵ_2 and R̂ = ŝ + r̂_diff;
* t_p = 0 implies p ∈ J_2 ∪ supp q_0 (eq:poisson-divisor-reconstruction);
* q_0 is integral, J is squarefree, and 4ℓ_pair − 2s + j_2 = 4c + 5j_2.

Replacing 3π by 2π breaks the table (B10).

## 4. Task 3: the two Poisson transforms (10145-10913), same versus new

**The same as reviewed Oct 5 identities, up to notation:**
* Lemma 17.5 is [O5] `lem:poisson` (875-932; R1 C4). The formula, the zero frequency and the |γ| = 1 Parseval argument are the same. The principal bound A Σ_{h≠0} |𝓕Φ(Aq_h)| ≪ 1 was checked by hand.
* gcd extraction, mutual-gcd Möbius (t'), and the first paired Gauss/reciprocity structure, γ_2(ab) = γ_2(a)γ_2(b)χ_b(a)⁴ (cubic reciprocity χ_a(b)² = χ_b(a)²). These correspond to [O5] eq:paired-first-gauss and eq:crt-a.
* Second transform:
  * the gcd g' and the primitive character χ̄_{z_1}χ_{z_2};
  * μ(z)γ_{−1}(z) = ᾱγ_2 χ_z(−1) Ḡ(z), and 𝔊(a,b) = G(ba^{−1}). These match [O5] (322) and the second paired identity;
  * the extraction a_0(v'n) = a_0(v')a_0(n)χ_n(v')⁴;
  * χ̄_n(d_2) = χ_n(d_2)χ_n(d_2)⁴ (= [O5] χ̄_z(e) = χ_z(e)⁵).
* The regrouping k_new = d_k d_2 k'' corresponds to [O5] k' = deh (d ↔ d_k, e ↔ d_2, h ↔ k''). The Möbius v' corresponds to w, and the puncture r_g = g'/d_2 corresponds to r = tg/e.
* The enlarged frequency range is again Heath-Brown's positivity device.

**New relative to Oct 5 (none is in a reviewed analog):**
1. The cube pair (b_1, b_2) inside the square, with the 8-row parity/a_ip table (10252-10272) and the primitive conductor m_1 = u_1u_2R_1 including R_1 (eq:first-masked-data, 10166).
2. **The u_1-side CRT/reciprocity identification (10214-10245), eq. (C) (10279), and the fixed-ray quotient G(u_1u_2^{−1})R(u_1u_2^{−1}, P_T).** Only the downstream exponent table is verified here.
3. The cube label: J = sJ_2 and q_0 (eq:retained-cube-label, 10316), the identity (inverse-cube-actual) and the count (fixed-cube-count). J enters the new label f_new = JCd_2v'.
4. ỹ = h f² E, with E taken from the odd-parity primes, and the actual-norm identity R̂ − Â_1 − Â_2 + Ê = ŝ − 2ĵ_2 (10331).
5. Side-dependent polynomials P_1 ≠ P_2 (different ν_i, A_i, s_i and marks). The weighted Cauchy (D) then takes a geometric mean of two positive majorants, where Oct 5 had one symmetric square.
6. The slot-priority partition (eq:inverse-slot-priority, 9950) and the survival of marks as original subcollections.
7. Fixed punctures γ = (q_0, t', r_g), counted by #Γ_σ ≤ Z^{C_c+11η/2}, and the normalized label measure (11336-11365).
8. The old-label fibre bound (10573) and the new fibre D_K(f)C_K(γ) (11299) in place of the sign-sum collapse.
9. Outer row masks 𝓑_1, 𝓑_2 with Schwartz-tail discards (eq:inverse-raw-tail, 10127; the bound was checked by hand) in place of compactly supported Φ̂.
10. The second principal exponent F − B − j, which carries J and q_0 (10755).
11. The common log-Fourier densities in 9 and 6 coordinates (10444, 11135). The "common density" requirement replaces Oct 5's `lem:smooth-mean-square` and was read, not mechanized.

## 5. Findings (none load-bearing)

* **N1.** F_ch ≤ F + 11η (11107) is loose: the same hypotheses give F_ch ≤ F − 5η (E6'). The window F' ≤ F + 11η and F_max = N_max + V_max + 11Dη are therefore conservative.
* **N2.** The terminal parameter conditions (9921-9925) have large slack. d ≤ c_*/20 and c_node ≥ c_*/8 also pass, and the controls fail only at d ≤ c_*/4 and c_node ≥ c_*/100. By contrast, every recursive and initialization margin is exactly tight.
* **N3.** The step "(4.10)" silently uses O ≥ 0 and Q ≥ 0. Here O is a Lemma 14.3 length, and the check fails without O ≥ 0. Q ≥ 0 holds because Q is the log of an ideal norm. O ≥ 0 must come from Lemma 14.3.
* **N4.** The η bookkeeping concerns fixed compact ratio windows (10049-10051), so every "η" is really an O(1)/log Z constant. The bookkeeping is consistent, and the threshold log Z ≥ L_win/η is imposed last (11576-11584).

## 6. What remains unverified, smallest first

1. **Eq. (C) and the u_1-side factor list (10214-10245, 10279).** This is CRT plus sextic reciprocity at the primes of 𝔅 = rad(b_1b_2), with ray quotient G(u_1u_2^{−1})R(u_1u_2^{−1}, P_T). It can be replayed empirically with the sextic-symbol code of `oct5_r2_iteration_check.py` (section E) at small norms.
2. The Lemma 14.3 branch outputs used at 9884-9921: the row branch E_ref ≤ M + z_a + 5η/3, the column-branch forms, and u ≠ z_a ⇒ u ≥ v/2. These are target 1 (Lemma 14.3 at 7747-7993).
3. eq:signal and eq:G-quadratic-refinement (950-970), the Sep 30 counterparts of [O5] eq:quotient. They are needed to identify P_T and 𝔊.
4. The common-density requirement of Lemma 4.5 (`lem:smooth-calculus`) as used in both separations, and the Lemma 17.3 hypotheses (the edge profile and coefficient-measure bounds) for the actual edges. These were read only.

## 7. Misreadings to avoid

* "Ledger PASS" means that the displayed exponent arithmetic is exactly right. It does not mean that Lemma 17.2 is proved: the exponents are inputs from items 1-4 of §6.
* The statement diff lets the Oct 5 *statements* cover z = 0 and z_0 = 0. It does **not** let R2's review of the Oct 5 *proof* cover Sep 30's proof, which is a different recursion. The case Prop 19.2 needs (z > 0, marked) has no reviewed analog.
* The MODEL order growth (F14) uses assumed edge data and is not a property of the manuscript.
* RH remains unsolved. Even if accepted, 7/8 is a fixed half-plane statement.
