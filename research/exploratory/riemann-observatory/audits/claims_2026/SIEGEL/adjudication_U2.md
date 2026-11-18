# SIEGEL adjudication of audit item U2 (Banks (2.7): Rosser–Schoenfeld 1962, Theorem 6)

```text
Status: EXPLORATORY ADJUDICATION. No new mathematical claim. Nothing here says RH is proved or closer to proved,
        or adds anything to the Landau-Siegel question beyond one cited inequality.
        It decides one audit item (U2 of audit_part1.md §11) about a citation in Banks arXiv:2610.15483v1.
Scope: Banks Lemma 2.1, proof of (2.4), the display before (2.7) and (2.7) itself (PDF p. 7), together with
        every later use of Lemma 2.1 in Banks (Cor 6.3, §7, Remark 7.1).
        Out of scope: the rest of Lemma 2.1 (already checked in audit_part1.md §1), and every other step of
        the SIEGEL map.
Exact sources or dependencies:
  [Banks] arXiv:2610.15483v1 PDF sha256 54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f
          (identical to the part-1 copy).
  [RS62]  J. B. Rosser, L. Schoenfeld, Illinois J. Math. 6 (1962) 64-94, Theorem 6.
          NOT OBTAINED. The publisher site (Project Euclid) returned a 1154-byte bot-challenge HTML page,
          not the PDF, and no workaround was attempted. The zbMATH review (Zbl 0122.05001, fetched through
          the zbMATH Open API) does not state Theorem 6.
  Secondary quotations of RS62 (read as data):
  [BFKNW] Broadbent-Fiori-Kadiri-Ng-Wilk, "Bounds for Mertens sums", arXiv:2608.01498v1,
          PDF sha256 c74069a47ac8a98de243bdd0a82dc61beace5f7312c9504ceaf8c1ed31e33fa7;
          e-print sha256 26ae32b50cd89f5bf167ae5fd29f320df6a8b683ddf824fed0d7cf4a5d99d1a6,
          MertensNathanversionsubmissionArxiv.tex (sha256 80f6863d...0518e0) lines 2315-2322.
  [Joh]   D. R. Johnston, arXiv:2201.06184v2, PDF sha256 75bc30df5b939e57e1cefef216e5e252f7fb29cdc9dfb5b5403f8c5f26ebcd74;
          e-print sha256 9df8051fb4a8c79d457486044186d3cf4ef7bd9a43400d146df6b3024360f3e6, final.tex lines 395-398.
  [Kha]   T. Khale, arXiv:2210.06457v1, PDF sha256 e232e295f93e4b3be4e33d4a0043145645832316fd765fde89eadfc7b735c136,
          text p. 1601ff.
  Imported analytic input for the RS62-independent route (§4):
  [BKLNW] Broadbent-Kadiri-Lumley-Ng-Wilk, Math. Comp. 2021, arXiv:2002.11068v2,
          PDF sha256 4260869785b9c77294519851a520429a2870aaa513813585e67b985a59b76bb8:
          Table 15 (row log X0 = log 10^7) and (3.39).
What was actually run: one new script, our own code, run with python3 -I. Nothing from any audited repository
        and no downloaded code was run; the e-prints were only searched as text.
          experiments/code/claims_2026/siegel_adjudication/adj_U2_rosser_schoenfeld.py
            sha256 c8575ef191d97a90d96cf93b54f127cec9ec78ed1c4adc19b7674b5d0ea9513e
          experiments/code/claims_2026/siegel_adjudication/adj_U2_rosser_schoenfeld.out
            sha256 c83aadd095a555f30731363c47c3dceebca2440d34de25c969ce77c257f1b3ea
        Result: 13 PASS / 0 FAIL, 8.5 s. Lines (2a), (2d), (3a) and (3b) use arb ball arithmetic (python-flint,
        96 bits) and are rigorous. (6f)-(7) use float64 and are evidence only. The rest are mpmath at 30-40 digits.
Smallest remaining gap: a page-level re-read of RS62 p. 70 is still not done. This is bibliographic only.
        The inequalities Banks uses are re-established below without RS62 (§4), assuming BKLNW Table 15.
```

## 0. Verdict

| Item | Decision |
|---|---|
| U2 overall | **not_an_issue.** The inequalities Banks quotes are true on exactly the stated ranges. They are proved here independently of RS62: rigorous ball arithmetic for 1 < x ≤ 10⁷, and an imported modern θ-bound for x > 10⁷. The quoted form also matches three independent published quotations of RS62 Theorem 6. Its thresholds are the least integers produced by our own computation. |
| Part-1 classification "unresolved_ambiguity (harmless)" | **Superseded.** The mathematics is resolved. Only the page-level bibliographic check of the 1962 paper remains open. |
| Auditor's numerical statements (min margins 0.031 and 0.0013 below 10⁷, at the extremal points) | **Reproduced independently and made rigorous** (0.031198 and 0.001267; the second is at x = 467). |
| Is the citation load-bearing for Banks's theorem? | **Weakly.** E cancels in (2.7). The last step of Lemma 2.1 tolerates RS error constants with c_l + c_u < 1.597 for every λ ∈ (0, 2], and c_l + c_u < 7.159 at the λ = 3/2 actually used. RS62 gives c_l + c_u = 1. |
| Public characterization as an error | **Not allowed.** There is no witness of any kind. The only allowed wording is: "Banks's citation of RS62 Theorem 6 was checked against secondary quotations and re-proved independently; the original page was not re-read." |

## 1. The text under adjudication

Banks, proof of (2.4), PDF p. 7, in substance: if X ≤ H the sum is empty, so assume X > H ≥ 319. "By the explicit form of Mertens' theorem [8, Theorem 6], with a certain absolute constant E,

  Σ_{p≤x} log p/p > log x + E − 1/(2 log x)  (x > 1),  Σ_{p≤x} log p/p < log x + E + 1/(2 log x)  (x ≥ 319).

Using the first bound at x = X and the second at x = H, we get

  Σ_{H<p≤X} log p/p > log X − log H − 1/(2 log X) − 1/(2 log H) > log X − log H − 1/log H.  (2.7)"

Here [8] is RS62. Banks cites only "Theorem 6". The labels (3.21) and (3.22) come from the audit's ARCHITECTURE.md (E3). Remark 7.1 repeats that Lemma 2.1 "relies on the explicit form of Mertens' theorem given by Rosser and Schoenfeld [8, Theorem 6]". This is the only place RS62 is used.

Downstream uses (all re-read): Lemma 2.1 requires X ≥ 8 and an integer H ≥ 319. Corollary 6.3 (p. 16–17) restates H ≥ 319 and applies (2.4) with X := M. §7 takes λ = 3/2 and H = 9216·97² = 86,713,344, and checks 319 ≤ H explicitly. So in the actual proof, the upper bound is used at x = H ≈ 8.7·10⁷ and the lower bound at x = M ≥ q^{4ω/3}, which is astronomically large.

Audit item (audit_part1.md, §1 and the §11 table): "The 1962 original was not re-read in this part. The quoted form is standard and holds at every prime < 10⁷." Classified unresolved_ambiguity (harmless).

## 2. Strongest defense

1. **The algebra of (2.7) is correct as written.** Write Δ(x) = Σ_{p≤x} log p/p − log x − E. Then Σ_{H<p≤X} = log X − log H + Δ(X) − Δ(H). Banks bounds Δ(X) > −1/(2 log X) using x = X > H ≥ 319 > 1, and −Δ(H) > −1/(2 log H) using the integer H ≥ 319. Since X > H > 1 we have 1/(2 log X) < 1/(2 log H), which gives the final strict inequality. Both bounds use the same E, so E cancels. Banks's phrase "a certain absolute constant E" is therefore all that is needed. The value of E plays no role.

2. **Three independent published quotations agree with Banks's form, including the thresholds.**
   - [BFKNW], lines 2315–2322: "the classic bounds of Rosser-Schoenfeld [Theorem 6, Corollary, p.70]: |Υ(x) − log x + M′| ≤ 1/(2 log x) for x ≥ 319, ≤ 1/log x for x ≥ 32". Here Υ(x) = Σ_{p≤x} log p/p and M′ = 1.33258227573322… = −E (their (2) and (6)).
   - [Kha]: "By [RS62, (2.8), (3.22)] … Σ_{p≤x} log p/p < log x + E + 0.06456". We have 0.06456 = 1/(2 log 2310) to four figures. This is the 1/(2 log x) error term of (3.22), and it supports the audit's label (3.22) for the upper bound.
   - [Joh]: "[RS62, Equation (3.23)]: Σ_{p≤x} log p/p < log x + E + 1/log x", used for x > 200. This is the weaker companion bound, consistent with (3.21)–(3.22) being the 1/(2 log x) pair.

3. **The thresholds are reproduced by our own computation as least integers. This is a fingerprint.** On each interval [p, p′) the sum is constant and log x + E + c/log x has an explicit minimum. Computing the exact failure sets at 30 digits [(4a)–(4e)] gives:
   - The upper bound with +1/(2 log x) fails on parts of 54 prime gaps. The last failure set is **[317, 318.5586)**. So **319 is exactly the least integer** from which (3.22) holds. The margin at x = 319 is only 0.00136.
   - The lower bound with −1/(2 log x) never fails on (1, 2000), consistent with "x > 1". It never fails below 10⁷ either; see (3a).
   - The upper bound with +1/log x fails last on **[31, 31.6907)**. So **32 is exactly the least integer**, matching [BFKNW]'s "x ≥ 32". The lower bound with −1/log x never fails.

   A misquotation, whether of the constant 1/2, of E, or of the sum being over primes rather than prime powers, would not reproduce both published thresholds as the exact least-integer cut-offs.

4. **E is the Mertens constant to 30 digits.** E = −γ − Σ_p log p/(p(p−1)). The arb enclosure (primes ≤ 10⁷ plus an explicit tail bound log N/(N−1) + log(N/(N−1))) gives [−1.332583 ± 8.9·10⁻⁷]. The mpmath prime-zeta series gives −1.33258227573322088176582877607. Both agree with the part-1 constant and OEIS A083343 [(2a)–(2d)].

5. **The inequalities are true on the whole stated ranges, independently of RS62.** See §4. Below 10⁷ this is a rigorous ball-arithmetic check. Above 10⁷ it follows from BKLNW Table 15 via an exact partial-summation identity.

6. **The downstream argument has slack.** If the lower and upper RS constants were c_l and c_u instead of ½ and ½, (2.7) would lose (c_l + c_u)/log H. The last line of Lemma 2.1 needs e^λκ/2 − (c_l + c_u)/log H > 0 for H ≥ 319. With κ = 0.5541199559, this holds for every λ ∈ (0, 2] whenever c_l + c_u < κ log 319/2 = 1.5973. At λ = 3/2 it holds whenever c_l + c_u < 7.1586 [(1c)]. Banks's own numbers check out: κ/2 = 0.27706 > 0.277 and 1/log 319 = 0.173455 < 0.174 [(1a)–(1b)]. The final positivity at λ = 3/2 is e^{3/2}κ/2 − 1/log 319 = 1.068.

**What the defense cannot do.** It cannot certify the bibliographic detail: the page number, the exact equation labels, or whether p. 70 states x ≥ 319 or x > 318.6. The original was not seen. Nothing in Banks depends on these details.

## 3. Strongest attack

Each route below would give a real witness if it succeeded. None did.

1. **A counterexample to the quoted inequalities.**
   - (3.21) for 1 < x ≤ 10⁷ and (3.22) for 319 ≤ x ≤ 10⁷ were checked *rigorously* (arb balls, rigorous enclosure of E) at the extremal points. For (3.21) these are the left limits x → p′⁻ at each next prime, plus (1, 2), where the right side is −1.36 < 0. For (3.22) they are x = p for p ≥ 331, plus x = 319 for the interval [319, 331). Minimum margins are 0.031198 and 0.001267 (the latter at x = 467) [(3a)–(3b)].
   - A float64 extension to 10⁸ gives margins 0.02721 and 0.00127 [(6f)].
   - Above 10⁷ the bounds hold analytically (§4). **No witness.**

2. **The threshold.** (3.22) is genuinely false on [317, 318.5586). The attack would succeed if Banks used it at some x < 319. He does not. Lemma 2.1, Cor 6.3 and §7 all require H ≥ 319, and in §7 H = 86,713,344. **No witness.**

3. **E or the summation range.** If RS62's sum ran over prime powers, Σ_{n≤x} Λ(n)/n, with constant −γ, then the quoted primes-only inequalities with an unspecified E could fail. At x = 10⁶, for example, Σ_{p≤x} log p/p − log x ≈ −1.3326, while −γ − 1/(2 log x) = −0.6134. But Banks needs only *some* common E. With E = Mertens's constant, the primes-only inequalities are exactly what §2.3–2.4 and §4 verify. The secondary sources state primes-only sums (Υ in [BFKNW]). **No witness.**

4. **Reliance on 1962-era inputs.** RS62 rests on the zero computations available in 1962. If any of those were faulty, the 1962 proof could have a gap for large x. The independent route in §4 uses only BKLNW 2021 and our own computation, so this attack does not reach Banks. **No witness.**

5. **Reliance on BKLNW in the independent route.** Table 15's k = 2 constant 0.13675 for x > 10⁷ is essentially sharp: our float64 maximum of |θ(x) − x| log²x/x over (10⁷, 10⁸] is 0.13674 [(6f)]. So it is a tight, internally consistent value, not a loose one. A second BKLNW bound, (3.39) with k = 4 and 151.3 for x ≥ 2, would already suffice for x > 80,678 [(6b)]. Its fingerprint, the maximum 151.2236 at the prime 1423, is reproduced exactly [(6c)–(6d)]. The analytic range rests on two independently stated BKLNW constants, and on RS62 itself as a third source. **No witness.**

6. **The direct target.** Banks's (2.7) was evaluated directly over all prime pairs 319 ≤ H < X ≤ 10⁸ in float64. Prime H is the worst case for integer H. The minimum margin is 0.0543, at H = 98,654,869 [(7)]. **No witness.**

## 4. RS62-independent proof of the quoted inequalities

*Identity.* For x ≥ 2, Abel summation gives Σ_{p≤x} log p/p = θ(x)/x + ∫₂ˣ θ(t)/t² dt. This was checked exactly at x = 10², 10⁴, 10⁵ [(5)]. With R(t) = θ(t) − t,

  Δ(x) := Σ_{p≤x} log p/p − log x − E = R(x)/x − ∫ₓ^∞ R(t)/t² dt,

where E = 1 − log 2 + ∫₂^∞ R/t² dt = lim (Σ_{p≤x} log p/p − log x). This is the classical Mertens constant −γ − Σ_p log p/(p(p−1)). The integral converges by any bound R(t) = O(t/log²t).

*Range x > 10⁷.* BKLNW Table 15, row log X₀ = log 10⁷, k = 2, gives |R(t)| < 0.13675·t/log²t for t > 10⁷. Hence, with L = log x,

  |Δ(x)| ≤ 0.13675/L² + 0.13675/L,

and this is < 1/(2L) iff 0.13675/L + 0.13675 < 1/2. At L = log 10⁷ the left side is 0.1452 [(6a)], and it decreases in L. So both (3.21) and (3.22) hold, strictly, for every x > 10⁷.

*Range 1 < x ≤ 10⁷.* This is the rigorous arb check in §3.1 [(3a)–(3b)].

*Conclusion.* The two inequalities quoted by Banks hold with E = −1.3325822757… on exactly the ranges x > 1 and x ≥ 319. The only assumption is the imported BKLNW Table 15 entry, which is consistent with our data. RS62 is not used. Since E cancels in (2.7), Banks's (2.7) and hence Lemma 2.1 follow. This makes the 1962 page reference a provenance matter, not a dependency.

## 5. Decision

- **Classification: not_an_issue.** The item was a recorded reading gap ("original not re-read"), not a defect. The quoted statement is corroborated, with matching thresholds, by three independent quotations. It is also re-proved without RS62. Nothing needed repair, so "repaired_minor" does not apply.
- **Error characterization:** not allowed. No witness exists.
- **Residual (bibliographic only):** check RS62 p. 70 against the quoted form when a copy can be obtained legitimately, by hand or through library access. This does not block anything.
- **Known misreadings to avoid:**
  - The audit labels (3.21)–(3.22) are the auditors'. Banks cites only "Theorem 6".
  - (3.22) is false on [317, 318.56), so "x ≥ 319" must not be weakened to "x > 300".
  - The finite checks are evidence only above 10⁷. Coverage there comes from §4.

## 6. Reproduction

```
cd research/exploratory/riemann-observatory/experiments/code/claims_2026/siegel_adjudication
python3 -I adj_U2_rosser_schoenfeld.py     # ~9 s, 13 PASS / 0 FAIL; output in adj_U2_rosser_schoenfeld.out
```
Dependencies: numpy 2.5.3, mpmath 1.3.0, python-flint 0.9.0, Python 3.13.
