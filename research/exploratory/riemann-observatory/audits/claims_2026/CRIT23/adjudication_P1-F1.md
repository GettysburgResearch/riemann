# CRIT23 adjudication of finding P1-F1 (AF Prop 4.2, proof of the trace estimate)

```text
Status: EXPLORATORY ADJUDICATION. No new mathematical claim. Nothing here says RH is proved or closer to proved.
        It decides one audit finding about one proof step in Alpoge-Furman arXiv:2608.13637v2 (AF).
Scope: AF Proposition 4.2 ("Trace", tr G~ = N(I') + O_chi(T^{1/2} L^2)), its proof (LaTeX lines 319-335,
        PDF p. 6), and the grid definition it relies on (line 217). Downstream use checked at line 560 (Section 6).
        AF Prop 4.3, Section 5 and the Lean formalisation were not re-audited, except that Prop 5.2 (line 418)
        is quoted for its handling of k = d, d+1.
Exact sources or dependencies: AF v2 e-print tarball sha256 d6a2e5ca0b1d2cece6597ccdfc6cbb0f458739113f28ca4ce84ac307de6b682d
        (fresh download on 2026-11-17, byte-identical to the part-1 copy), file paper-v5-draft18.tex
        sha256 ae369aaffb66335ff0dd5ebeafa59da7ca1fc26affa748960e7cdc3d82df26b3; AF v2 PDF
        sha256 6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444 (pdftotext of p. 6 agrees with
        the LaTeX). The arXiv API lists v2 (2026-08-19) as the latest version. Zero ordinates: Observatory EXP-0001
        (experiments/results/zeros/zeta_zeros_1_100000_arb.tsv.gz, sha256 4d364a6ba8043e878409fe7d2ce89d2e9c6a29ba48dc1446b54c468579715603).
What was actually run: line-by-line reading of AF Sections 2.2-2.3 and 4 and the uses of Prop 4.2; hand derivation
        of the step, the counterexample and the repair; two new scripts (independent of the part-1 audit's code,
        which was read for its choice of chi but not imported or run), non-rigorous double precision except the
        lines marked "analytic":
          experiments/code/claims_2026/crit23_adjudication/adj_P1F1_trace.py   (+ .out)
          experiments/code/claims_2026/crit23_adjudication/adj_P1F1_witness.py (+ .out)
        No author code, Lean or downloaded code was run.
Smallest remaining gap: none for the statement of Prop 4.2 or anything downstream. The repaired proof in Section 5
        below was checked by hand and numerically. It has not been through an independent second review.
```

## 0. Verdict

| Item | Decision |
|---|---|
| P1-F1 overall | **verified_error at the level of one proof step; severity minor, disposition repaired_minor.** The statement of Prop 4.2, the §6 chain, Theorem A and Theorem B are unaffected. |
| Sub-claim (a): the inequality \|Re γ_ρ − α_k\| ≥ D_ρ and the resulting tail bound are applied to zeros with Re γ_ρ ∈ I′∖I | **Confirmed, explicit witness.** It is false for every such zero with D_ρ > h/2. The intermediate claim that "the rest" (D_ρ ≥ 1) contribute ≪ X^{1/2} is also false. Their true total is ≍ √T·L. |
| Sub-claim (b): α_d ∈ [T, 2T) when LT/2π ∉ ℤ | **Confirmed, explicit witness.** This is a precision slip only. The inequality fails for every Re γ_ρ ∈ (3T/2, α_d), but by less than h. For D_ρ ≥ 2h that changes the tail bound only by a constant factor, and the ≪ log T zeros with D_ρ < 2h are covered by the trivial bound. AF's own Prop 5.2 (line 418) handles k = d, d+1 correctly. |
| Auditor's numerical witnesses | **Reproduced independently** with two different C^∞ cut-offs χ (identical values for χ_A, the auditor's χ). |
| Auditor's repair | **Confirmed**, analytically (Section 5) and numerically (table (R)). It gives tr G̃ = N(I) + O(X^{1/2}L) = N(I′) + O(√T log T). |
| Public characterization as an error | **Allowed, scoped:** "a local error in the proof of AF Prop 4.2, with a short repair; the Proposition and all results are unaffected." **Not allowed:** any wording that says Prop 4.2, Theorem A or Theorem B is false, or that the 2/3 or 5/6 results are in doubt. |

## 1. The text under adjudication

AF line 217 places α_k := T + 2πk/L (k ∈ ℤ) with step h = 2π/L and sets d := ⌊LT/2π⌋. It then says "so α_0, …, α_{d−1} ∈ [T, 2T)". This is true.

AF lines 319–335 (Prop 4.2 and its proof), verbatim in substance:

> tr G̃ = N(I′) + O_χ(T^{1/2}L²). *Proof.* By Lemma 2.1, for each zero with Re γ_ρ ∈ I′, tr(v_ρ v_ρᵀ) = aL² − Σ_{k∉[0,d)} φ̂(γ_ρ − α_k)². For k ∉ [0,d) one has α_k ∉ [T, 2T), hence |Re γ_ρ − α_k| ≥ D_ρ := dist(Re γ_ρ, {T, 2T}). By (2.8), |φ̂(γ_ρ − α_k)|² ≤ e^{L/2} C_χ² |Re γ_ρ − α_k|^{−4}, and Σ_{k∉[0,d)} |Re γ_ρ − α_k|^{−4} ≤ 2(D_ρ^{−4} + h^{−1}∫_{D_ρ}^∞ s^{−4} ds) ≪ L min(L³, D_ρ^{−3}). Dividing by aL² and summing over zeros in I′ (… O(L) zeros have D_ρ < 1, contributing ≪ X^{1/2}L²; the rest satisfy Σ_ρ D_ρ^{−3} ≪ L, contributing ≪ X^{1/2}), |tr G̃ − N(I′)| ≪ X^{1/2}L².

Here I = [T, 2T), I′ = [T − √T, 2T + √T), and G̃ sums over all zeros with Re γ_ρ ∈ I′ (line 225, eq. (2.10)). Write head_ρ := Σ_{0≤k<d} φ̂(γ_ρ − α_k)² and tail_ρ := Σ_{k∉[0,d)} φ̂(γ_ρ − α_k)². Lemma 2.1 gives head_ρ + tail_ρ = aL² exactly. My implementation reproduces this to 1e−13 for real and complex arguments (output (0)).

## 2. Strongest defense

1. **The statement is true.** For an on-line zero, 0 ≤ head_ρ ≤ aL², so its error |1 − head_ρ/aL²| is at most 1. There are N(I′∖I) = (√T/π)log(T/2π) + O(log T) ≍ √T·L zeros in I′∖I (Riemann–von Mangoldt). So even if the step fails there, its cost is ≍ √T·L, which is inside the stated O(T^{1/2}L²) with a factor L to spare. The final displayed bound |tr G̃ − N(I′)| ≪ X^{1/2}L² is correct.
2. **The correct argument is already in the paper.** For Re γ_ρ ∉ I, every α_k with 0 ≤ k < d lies on one side of Re γ_ρ at distance ≥ D_ρ = dist(Re γ_ρ, I). So AF's own display, applied to *head* instead of *tail*, is valid there. That one-sided decay estimate is the one AF use for Ẽ in Prop 4.3 ("as above ‖v_ρ‖² ≪ X^{1/2}L D^{−3}") and for σ(τ) in Prop 5.2. The fix uses the paper's own tools: the I′∖I zeros contribute ≈ 0 instead of ≈ 1, and the difference is N(I′∖I).
3. **Slip (b) is harmless and AF know about it.** The proof of Prop 5.2 says "T + (d+1)h > 2T" and charges k = d, d+1 separately, so AF do not rely on α_d ∉ I elsewhere. In Prop 4.2 the slip only shifts the distance by at most h. It is covered by the trivial bound |φ̂(z)|² ≪ X^{1/2}L² for the ≪ log T zeros with D_ρ < 2h.
4. **Nothing downstream depends on the per-zero bound.** Line 560 uses only tr G̃ = N(I′) + o(N). Part 2 of the audit (audit_part2.md, lines 145 and 365) confirms that S6–S10 use neither the per-zero tail bound nor the value of d.

**What the defense cannot do.** There is no reading of the text under which the inequality |Re γ_ρ − α_k| ≥ D_ρ holds for ρ ∈ I′∖I. D_ρ is defined explicitly as dist(Re γ_ρ, {T, 2T}), and the sum is explicitly over all zeros in I′. Point 1 alone does not finish the proof either. For a hypothetical off-line zero in I′∖I, head_ρ is complex, and the bound |head_ρ| ≤ aL² does not follow from Lemma 2.1. The crude bound Σ_k |φ̂(γ_ρ − α_k)|² = L∫φ²e^{2yu} ≤ L²X^{|y|} would give ≪ X^{1/2}·√T·L in total, which is far too much. So the decay argument of point 2 is required. That makes this a genuine, if short, repair, not a reading.

## 3. Strongest attack (explicit witnesses)

**(a1) The inequality itself.** Take T = 10⁴: L = 7.372463, h = 0.852250, d = 11733. The zeta zero γ = 9949.990912 lies in I′∖I with D_ρ = 50.0091. The grid point k = −59 ∉ [0, d) has α_{−59} = 9949.717222, so |γ − α_{−59}| = 0.2737 < D_ρ. In general, every zero in I′∖I with D_ρ > h/2 has a grid point with k ∉ [0, d) within h/2 of Re γ_ρ. (adj_P1F1_witness.out (i).)

**(a2) The displayed per-zero inequality, with AF's explicit constants.** For the same zero and χ = χ_A (C_χ = ‖(φ²)″‖₁ = 11.068; ‖φ″‖₁ = 8.000), AF's chain gives tail_ρ ≤ e^{L/2}C_χ²·2(D^{−4} + h^{−1}D^{−3}/3) = 0.0321. The actual value is tail_ρ = 45.590383 = aL²·(1 − 1.6e−10). The inequality fails by a factor of 1419 (2716 with ‖φ″‖₁). (witness.out (ii).)

**(a3) No implied constant can rescue the displayed bound shape.** Take the point γ = T − √T/2, with D_ρ = √T/2.

| χ / window | T | tail/aL² | analytic lower bound (χ-free) | X^{1/2}L D^{−3}/(aL²) | ratio | TL |
|---|---|---|---|---|---|---|
| χ_A / flat | 2·10³ | 0.999999732 | ≥ 0.99207 | 3.49e−4 | 2.87e3 | 1.15e4 |
| χ_A / flat | 10⁴ | 0.9999999998 | ≥ 0.99759 | 5.16e−5 | 1.94e4 | 7.37e4 |
| χ_A / flat | 10⁶ | 1.000000000 | ≥ 0.99987 | 2.96e−7 | 3.38e6 | 1.20e7 |
| χ_B / flat | 10⁴ | 0.999999999996 | ≥ 0.99759 | 5.14e−5 | 1.95e4 | 7.37e4 |
| χ_A / MT | 10⁴ | 0.9999999999 | ≥ 0.99683 | 5.48e−5 | 1.83e4 | 7.37e4 |

The "analytic" column does not depend on χ. Since χ is monotone and 0 ≤ φ ≤ 1 is unimodal, ‖φ′‖₁ = 2, so |φ̂(r)| ≤ 2/|r| for real r. Every α_k with 0 ≤ k < d lies at distance ≥ D. Hence head ≤ Σ_{j≥0} 4/(D + jh)² ≤ 4/D² + 4/(hD), and aL² ≥ (L − 2)L (flat) or cos(1/√2)(L − 2)L (MT). Asymptotically tail/aL² → 1, while the displayed shape equals 8(2π)^{−1/2}/(aLT) → 0. The ratio is therefore ≍ TL; the computed ratio/TL is 0.25–0.28 and tends to (2π)^{1/2}a/8.

**(a4) The summed intermediate claim is false.** AF say the zeros with D_ρ ≥ 1 contribute ≪ X^{1/2} in total. In fact Σ_{ρ∈I′, D_ρ≥1} tail_ρ/aL² ≥ N(I′∖I) − O(log T) ∼ √T·L/π. Its ratio to X^{1/2} = (T/2π)^{1/2} grows like L·√(2/π) → ∞. On real zeros (output (D)):

| T | Σ_{D≥1} tail/aL² (χ_A) | X^{1/2} | ratio | L√(2/π) |
|---|---|---|---|---|
| 2000 | 85.26 | 17.84 | 4.78 | 4.60 |
| 6000 | 177.30 | 30.90 | 5.74 | 5.47 |
| 20000 | 376.31 | 56.42 | 6.67 | 6.44 |
| 30000 | 483.02 | 69.10 | 6.99 | 6.76 |

A finite table cannot by itself refute a "≪"; the refutation is the asymptotic (Riemann–von Mangoldt) statement. The table only shows it numerically.

**(b) The grid point α_d.** d·h = h⌊T/h⌋ ∈ (T − h, T], so α_d ∈ (2T − h, 2T], and α_d < 2T exactly when LT/2π ∉ ℤ.

| T | α_d | 2T − α_d | h |
|---|---|---|---|
| 10³ | 1998.8894 | 1.1106 | 1.2393 |
| 2·10³ | 3999.5334 | 0.4666 | 1.0903 |
| 10⁴ | 19999.4547 | 0.5453 | 0.8523 |
| 3·10⁴ | 59999.6984 | 0.3016 | 0.7417 |

For 3T/2 < Re γ_ρ < α_d one gets |Re γ_ρ − α_d| = D_ρ − (2T − α_d) < D_ρ. So the literal inequality fails here too, but only by less than h. For D_ρ ≥ 2h the distance is ≥ D_ρ/2, which only changes the constant by 16.

**What the attack cannot do.** It cannot reach the statement. On real zeros tr G̃ − N(I′) ≈ −N(I′∖I) (= −87.6, −179.2, −379.2, −485.3), which is inside O(T^{1/2}L²). Section 5 proves the corrected bound unconditionally.

## 4. Independent reproduction on real zeros (output (D))

The zeros are from EXP-0001, all simple and on the line. Two C^∞ cut-offs were used: χ_A(t) = f(t)/(f(t) + f(1−t)) with f(t) = e^{−1/t}, and χ_B, the normalised integral of the bump e^{−1/(s(1−s))}. Both use the flat window ψ₀.

| T | χ | N(I) | N(I′) | N(I′∖I) | tr G̃ | tr G̃ − N(I) | tr G̃ − N(I′) | Σ_I tail/aL² | Σ_{I′∖I} head/aL² |
|---|---|---|---|---|---|---|---|---|---|
| 2000 | A | 1957 | 2044 | 87 | 1956.3628 | −0.6372 | −87.6372 | 1.340 | 0.703 |
| 2000 | B | 1957 | 2044 | 87 | 1956.3655 | −0.6345 | −87.6345 | 1.355 | 0.721 |
| 6000 | A | 6921 | 7100 | 179 | 6920.7579 | −0.2421 | −179.2421 | 0.414 | 0.172 |
| 6000 | B | 6921 | 7100 | 179 | 6920.7560 | −0.2440 | −179.2440 | 0.436 | 0.192 |
| 20000 | A | 26904 | 27282 | 378 | 26902.8213 | −1.1787 | −379.1787 | 1.333 | 0.154 |
| 20000 | B | 26904 | 27282 | 378 | 26902.8209 | −1.1791 | −379.1791 | 1.351 | 0.172 |
| 30000 | A | 42290 | 42776 | 486 | 42290.7387 | +0.7387 | −485.2613 | 0.196 | 0.935 |
| 30000 | B | 42290 | 42776 | 486 | 42290.7363 | +0.7363 | −485.2637 | 0.218 | 0.954 |

The χ_A rows at T = 2000, 6000 and 20000 match the auditor's values (−0.6372, −0.2421, −1.1787; −87.6372, −179.2421, −379.1787) to every printed digit. They were obtained with a different quadrature, using per-zero windows |γ − α_k| ≤ 150 where max φ̂² beyond 150 is ≤ 1.3e−16. tr G̃ tracks N(I), not N(I′), as the finding says.

## 5. The repair (checked)

Use (2.8) in its full form |φ̂(z)| ≪ e^{L|Im z|/2} min(L, |z|^{−1}, |z|^{−2}) with |Im γ_ρ| < 1/2, and write r_k := |Re γ_ρ − α_k| ≤ |γ_ρ − α_k|. Then |φ̂(γ_ρ − α_k)|² ≪ X^{1/2} min(L², r_k^{−2}, r_k^{−4}).

**One-sided sum.** Suppose the points r_k are ≥ D, ≥ D + h, ≥ D + 2h, …. Then

  S(D) := Σ_j min(L², (D + jh)^{−2}, (D + jh)^{−4}) ≪ min(L², L D^{−3}).

For D ≥ 1, the sum is ≤ D^{−4} + h^{−1}∫_D^∞ s^{−4} ds ≪ L D^{−3}. For D < 1, split it into three ranges:

* the ≤ 2 terms with D + jh ≤ 1/L, each ≤ L²;
* the terms with D + jh ∈ (1/L, 1), which sum to ≤ L² + h^{−1}∫_{max(D,1/L)}^1 s^{−2} ds ≪ min(L², L/D);
* the terms with D + jh ≥ 1, which sum to ≪ L.

**Zeros with Re γ_ρ ∈ I′∖I.** All α_k with 0 ≤ k < d lie on one side of Re γ_ρ, at distance ≥ D_ρ = dist(Re γ_ρ, I). So |head_ρ| ≪ X^{1/2} min(L², L D_ρ^{−3}), and these zeros contribute Σ m_ρ head_ρ/aL² ≪ X^{1/2}·[L·1 + L^{−1}·Σ_{D≥1} m_ρ D_ρ^{−3}] ≪ X^{1/2}L. This uses N(t, t+1) ≪ log t, so Σ_{D≥1} m_ρ D_ρ^{−3} ≪ L.

**Zeros with Re γ_ρ ∈ I and D_ρ ≥ 2h.** Every k ∉ [0, d), including k = d, has r_k ≥ D_ρ − h ≥ D_ρ/2, and each side is one-sided. So tail_ρ ≪ X^{1/2}L D_ρ^{−3}. This is AF's bound with the constant changed by 16.

**Zeros with Re γ_ρ ∈ I and D_ρ < 2h.** There are ≪ log T of them. Each has tail_ρ ≪ X^{1/2}(L² + S(0)) ≪ X^{1/2}L².

Summing:

  tr G̃ = Σ_{I} m_ρ(1 − tail_ρ/aL²) + Σ_{I′∖I} m_ρ head_ρ/aL² = N(I) + O(X^{1/2}L).

Since N(I′) − N(I) ≪ √T log T (AF Cor 4.5 uses this),

  tr G̃ = N(I′) + O(√T log T),

which is stronger than the stated O(T^{1/2}L²). The table (R) checks |head|/[X^{1/2}min(L², LD^{−3})] at complex points T − D + iy for y ∈ {0, 0.25, 0.49}, D ∈ {0, …, 30} and T ∈ {2000, 20000}. The ratio is at most 0.24, consistent with the bound.

The D_ρ < 1 accounting here gives X^{1/2}L, not AF's X^{1/2}L². This agrees with the earlier finding F7 (ARCHITECTURE.md), which is separate from P1-F1 and was not re-adjudicated here.

## 6. Downstream effect

* Prop 4.2 is used at AF line 560 only in the form tr G̃ = N(I′) + o(N). The repaired bound gives exactly that.
* Cor 4.5 and Prop 4.3 do not use the per-zero tail bound of Prop 4.2. Prop 4.3 has its own one-sided estimate with D ≥ √T.
* Section 5 (Prop 5.2) handles k = d, d+1 correctly.
* The constants 2 − R(ψ) and (3 − R(ψ))/2 are unchanged. So are Theorem A (2/3, 5/6, MT 0.6725…, 0.8362…) and Theorem B.

## 7. Decision

* **Classification:** verified_error, confined to one proof step (proof of AF Prop 4.2, line 327: the inequality and the tail bound are applied to zeros with Re γ_ρ ∈ I′∖I; plus the α_d off-by-one). Severity minor. **Disposition: repaired_minor.** The statement is true with a better error term, and every downstream use is unaffected.
* **Sub-item (b) on its own** would be typo_or_presentation (verified).
* **Public characterization:** permitted as a local, repaired proof error, citing the explicit witnesses in Section 3 (a1)–(a4) and (b). It must be stated together with "the Proposition and Theorems A and B are unaffected". Calling AF's results, or Prop 4.2's statement, wrong is not permitted, because no witness against them exists and the repair proves them.
* **Agreement with the auditor:** every factual statement in P1-F1 is confirmed. One refinement: the inequality fails for zeros in I′∖I with D_ρ > h/2, not literally for every such zero. The finding's "≈ aL²" is accurate for D_ρ ≫ 1.

## 8. Reproduction

From `research/exploratory/riemann-observatory/experiments/code/claims_2026/crit23_adjudication/`:

```text
python3 -I adj_P1F1_trace.py     # (0) Poisson-Gabor sanity, (B) alpha_d, (C) point witness, (D) real zeros, (R) repair bound
python3 -I adj_P1F1_witness.py   # explicit-constant witness on the zero 9949.990912 at T = 1e4
```

Environment: Python 3, numpy 2.5.3 (no other packages). The trace script takes about 6 minutes on 4 vCPU. Script and output hashes (sha256):

| File | sha256 |
|---|---|
| adj_P1F1_trace.py | fd421ed9352ff2dbcd1d9df0401b0557b30a7795c3e266363173149c1217f53e |
| adj_P1F1_trace.out | 720f702bc8ab66f36a07ac5fdd2c5b161522b0f6f76993cff89e3484ee971efd |
| adj_P1F1_witness.py | 96a467e96adf8d1819b0fa0e3823ae73c025931579333aa879471baf55986c38 |
| adj_P1F1_witness.out | c3a6c43dfb6b756fa21132ee63d2ff5bfcc0313672c377a9e70e3394f0d27158 |

Everything is double-precision floating point, and none of it is directed or certified arithmetic. The decisive witnesses (a1), (a3, analytic column) and (b) are exact or analytic. The numerical ones only illustrate them.
