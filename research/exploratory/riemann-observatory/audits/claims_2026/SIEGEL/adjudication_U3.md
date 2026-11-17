# SIEGEL adjudication of audit item U3 (Banks Thm 1.1: the all-q constant c = 3.0·10⁻³)

```text
Status: EXPLORATORY ADJUDICATION. No new mathematical claim. Nothing here says RH is proved or closer to proved,
        or settles the Landau-Siegel question. It decides one audit item (U3 of audit_part1.md §11,
        carried in audit_part2.md and ARCHITECTURE.md §13) about one sentence of Banks arXiv:2610.15483v1.
Scope: Banks Theorem 1.1, last sentence ("By the computation of [5], one can take c = 3.0 x 10^-3"), the proof of
        the second and third assertions (PDF pp. 2-3), and Remark 7.1 (p. 18). The imported result is Lu-Zaman-Zhao
        (LZZ) Theorem 1.1. LZZ is read in full: its Theorem 2.1 and Sections 3-7 are audited at the level of
        statements, formulas and constants. Its imported lemmas (Thorner-Zaman Prop 2.10, Platt Thm 7.1) are checked
        against their sources. Rademacher 1959, Bennett-Sharpley and Heath-Brown 1992 are not re-read.
        Out of scope: steps 1-9 of the SIEGEL map, Banks's q >= 10^10 proof, Guo's and Kimura's proofs.
Exact sources or dependencies:
  [Banks] arXiv:2610.15483v1, PDF sha256 54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f
          (identical to the part-1 copy).
  [LZZ]   R. F. Lu, A. Zaman, H. Zhao, "Numerical computations concerning Landau-Siegel zeros", arXiv:2602.03626.
          v1 (3 Feb 2026, the only version that existed on Banks's date, 11 Oct 2026):
            PDF sha256 77388d40267e90684e02ec8e666a9d55b0ceb159fa6b5b9eea1faf3dd09b1a40,
            e-print sha256 0f369e2b6b3ba8c0329afc14693ece72781c043c942837ef79e907e71e74c8ab
            (landau-siegel-computations-arxiv-v1.tex sha256 0f5239418a9795ea5c75d972a5f9cff2379cb2a47e798376b2d4c8126ce23639).
          v2 (20 Oct 2026, thanks "anonymous referees"; latest):
            PDF sha256 24b4f92ee29ba504467ad562d290664bedba779434701e8503d61f47def442d8,
            e-print sha256 4cd34646af67ad68434fab919094d9f5ef0779cd57d751e869374a92828cfea1
            (landau-siegel-computation-arxiv-v2.tex sha256 1c5db14af9dbe049f494b9536c58e22a81d1c13b6180572dc80bd677bed6c6bd).
  [LZZ code] github.com/asif-z/landau-siegel-zero-tester, commit a783ffdfbfdf431bb0fa03c81d5b7b0e7515d26e
          (12 Feb 2026, the HEAD on 2026-11-17). READ ONLY, NOT BUILT OR RUN. File hashes in §4.2.
  [Platt] D. J. Platt, "Numerical computations concerning the GRH", arXiv:1305.3087v1 (published Math. Comp. 85 (2016)),
          PDF sha256 8fd109aa21345bc3feac4fde2faa7dfb51b4ef1fc9a430f643323612a39ef417, Thm 7.1 and Thm 3.2.
  [TZ24]  J. Thorner, A. Zaman, arXiv:2208.11123v4 (Forum Math. 36 (2024)),
          PDF sha256 64c02753b55698f64625d3c84721303fa61fea7120bca993ffcd907456a104c6, Prop 2.10.
  [Guo]   arXiv:2610.30476v1, PDF sha256 f3058ae2a77e5c8e277cf90ed0faf8f745b8b638442b3439dfbf230e93e47a7e, Thm 1.1, §1.1, §5.
  [Kim]   arXiv:2610.21511v2, PDF sha256 5987fa4df134c5d94faf92a0278af96fcf18ac6adfb25adaddb7d6ff63e5e733, §1 only.
What was actually run: our own code only, run with python3 -I. Nothing from LZZ's repository or any e-print was run.
          experiments/code/claims_2026/siegel_adjudication/adj_U3_lzz_constants.py (+ .out)
            arb ball arithmetic (python-flint 0.9.0, 200 bits) for C4, C8, C16, the 1.912 constant, phi, rho, K, E.
            Rigorous given the transcribed formulas. The sup over t in TZ24 Prop 2.10 and in LZZ's P is a grid check (mpmath).
          experiments/code/claims_2026/siegel_adjudication/adj_U3_lzz_predicate.py           (library)
          experiments/code/claims_2026/siegel_adjudication/adj_U3_predicate_random.py       (+ .out)
          experiments/code/claims_2026/siegel_adjudication/adj_U3_adversarial_search.py     (+ .out, .json)
          experiments/code/claims_2026/siegel_adjudication/adj_U3_predicate_adversarial.py  (+ .out)
            Our own re-implementation of LZZ's test (2.5). float64 with a 1e-6 safety margin; NOT certified.
            Conditional on LZZ Theorem 2.1 (whose constants are re-derived above).
          The run copies of the last three drivers imported the library from the session scratchpad. The repository
          copies differ only in that one sys.path line.
          sha256: adj_U3_lzz_constants.py 60e6764f8e33a6ced2de6f0e96ccd2e53954259aa7fdff6ba487432467433ccc
                  adj_U3_lzz_constants.out ca8e4ab6df8200299cfd1e0b18827c19bf42ab21af80cc455cde327a7e8ed61a
                  adj_U3_lzz_predicate.py 511750c65ca79cde792aa9e314a19ec74bd92661b73d2a08cea39c9434df1721
                  adj_U3_predicate_random.py 849c77dc8f4a34950bbdd4a9aabed4784d4c43282d2fb34afc76db114ca0dd03
                  adj_U3_predicate_random.out db96480ed3db8205c0ef35618686823ec5e4261645719f2a2c2cc11de66cbbda
                  adj_U3_adversarial_search.py 53b2df968ba03c13fe371a8ab4f5638040d6a1c8800492758b0a236f6d17d7cc
                  adj_U3_adversarial_search.out b40af8be1bdebe13df09f8618bec734b8c8fb42d956e9b5044a544b882dad973
                  adj_U3_predicate_adversarial.py 06917c3a910b202ef80deb3aa836ec3abb0f4310e07fb0b360f24351cb6f6fd4
                  adj_U3_predicate_adversarial.out 504fdb768109603150ec8f8d30367f46240d5b0447de3e1cce05c5f9e6f074cd
          Results: all constants reproduced (stated values are valid upward roundings); 300/300 random and 12/12
          adversarial discriminants pass LZZ's test within LZZ's own caps. Run time: about 2 min (random) and 8 min (adversarial).
Smallest remaining gap: the LZZ production run (about 150,000 core hours, 4·10^5 < q <= 10^10) is not replayed, and its
        configuration and per-discriminant output are not published. This is an external-dependency boundary that
        Banks discloses. It is not a defect of Banks and not an ambiguity.
```

## 0. Verdict

| Item | Decision |
|---|---|
| U3 as filed ("unresolved_ambiguity") | **Reclassified: not_an_issue** as a defect of Banks. Banks's text is unambiguous. The all-q value c = 3.0·10⁻³ is stated as conditional on LZZ [5] in Theorem 1.1, in its proof and in Remark 7.1 ("a computation that we have not verified"). The deduction from LZZ Thm 1.1 is correct. What remains is a declared external dependency that was not replayed. It belongs in the "not replayed" list, not in the issue list. |
| The auditor's factual content | **Confirmed.** The value 3.0·10⁻³ for 3 ≤ q < 10¹⁰ does rest on LZZ Thm 1.1. It is not needed for steps 1–4, for Banks's q ≥ 10¹⁰ statement, for Banks's qualitative all-q statement (some c > 0), or for Guo's 1/100. |
| Imported statement vs. use | **Exact match.** LZZ Thm 1.1 reads the same in v1 and v2, and it gives (1−β) log q > 1/5 for every primitive real χ with q ≤ 10¹⁰. |
| LZZ's analytic constants (Thm 2.1, Table 1) | **Reproduced independently** in ball arithmetic. Every stated value is a valid upward rounding (§4.1). |
| LZZ's computational predicate | **Spot-checked, not replayed.** 300/300 random fundamental discriminants and 12/12 adversarial ones pass with LZZ's own rows and caps (§4.3). The hardest one we could find, d = 9 447 241 877 (χ_d(p) = −1 for every p ≤ 127), needs 104 754 006 primes in row 4. LZZ's cap is 130 000 000. |
| Explicit witness against Banks or LZZ | **None found.** |
| Severity if the dependency failed | **Repairable** (agree with the filing). The qualitative all-q statement survives by finiteness. The value 3.0·10⁻³ would survive through Guo Thm 1.1 (1/100), if Guo is accepted. |
| Public characterization as an error | **Not allowed.** There is no witness, and nothing was found wrong. Allowed wording is given in §5. |

## 1. The text under adjudication

Banks, Theorem 1.1 (p. 2): "One can take q0 = 10¹⁰ and δ0 = 3.0 × 10⁻³. Consequently, there is an absolute constant c > 0 such that (1 − β) log q ⩾ c … for every primitive real Dirichlet character χ of conductor q ⩾ 3. By the computation of [5], one can take c = 3.0 × 10⁻³."

Proof (p. 3): finiteness gives c := min{δ0, c0}. "For the last assertion … By [5, Theorem 1.1], which rests on a computation of Lu, Zaman, and Zhao, the function L(s, χ) has no real zero β ⩾ 1 − 1/(5 log q) when q ⩽ 10¹⁰. Hence c0 > 1/5 > δ0, and therefore c = δ0."

Remark 7.1 (p. 18): "a computation that we have not verified bounds these zeros away from one, and with it one can take c = 3.0 × 10⁻³."

Reference [5]: "Preprint, arXiv:2602.03626, 2026". No version is given. On 11 Oct 2026 only v1 existed.

LZZ Theorem 1.1, verbatim in v1 and v2: "If q ⩽ 10¹⁰ and χ is a quadratic Dirichlet character modulo q, then L(σ, χ) ≠ 0 for σ ⩾ 1 − 1/(5 log q)." Its proof (§3) has two parts.
- **q ≤ 4·10⁵:** Platt [Pla16].
- **4·10⁵ < q ≤ 10¹⁰:** for every d with 4·10⁵ < |d| ≤ 10¹⁰ and d ≡ 1 (mod 4) or d ≡ 8, 12 (mod 16), a FLINT/arb program finds N such that inequality (2.5) fails. It runs in four passes with rows λ = 1.6, 1.3, 1.2, 1.1 of Table 1, with caps of 6·10⁴, 5·10⁶, 5·10⁷ and 1.3·10⁸ primes. Inequality (2.5) is LZZ Thm 2.1 combined with β1 ≥ 1 − c/log q and c = 1/5.

Later papers describe the dependence the same way. Kimura §1: "for all q ≥ 3 when combined with the computation of [LZZ26]". Guo §1.1: "for all q ≥ 3 when combined with the small-conductor zero computations cited there".

## 2. Strongest defense

1. **The deduction is correct and complete.** Take a primitive real χ of conductor q. It is χ_d for a fundamental discriminant d with |d| = q, so it is a quadratic character modulo q.
   - If q ≤ 10¹⁰, LZZ gives β < 1 − 1/(5 log q) for every real zero β ∈ (0,1). So (1−β) log q > 1/5 = 0.2.
   - If q ≥ 10¹⁰, Banks's first assertion gives (1−β) log q ≥ 81/(5888 e^{3/2}) = 3.069556·10⁻³ ≥ 3.0·10⁻³ (recomputed, adj_U3_lzz_constants.out).

   The two ranges overlap at q = 10¹⁰, and 10¹⁰ is not a conductor anyway. Strictness is respected: LZZ gives a strict bound, and Banks needs only ≥.
2. **There is nothing ambiguous.** The theorem, its proof and Remark 7.1 each say that the numerical all-q value is imported and was not verified by the author. The audit's own wording ("depends on … which neither Banks nor we verified") restates Banks's disclosure. It does not identify a second reading of the text.
3. **The imported statement is stable across versions.** The v1→v2 diff (pdftotext and LaTeX) leaves Theorem 1.1, Theorem 2.1, Table 1 and the §3 run description unchanged in substance. The changes are expository; §3(d) lists them.
4. **LZZ is rigorous by design and partly checkable.** It uses ball arithmetic, public code and a published GRH verification for small q. The v2 acknowledgements thank anonymous referees. Our independent checks (§4) found every analytic constant correct, the code consistent with the paper, and the predicate satisfied on every discriminant we tried, including the most adversarial ones we could construct.
5. **Platt's input matches its use.** Platt Thm 7.1 says GRH holds for every primitive χ of modulus q ≤ 400 000 up to a height t0 ≥ 200. Platt Thm 3.2 counts all zeros with |Im s| ≤ t0 and Re s ∈ (0,1), and it handles the real axis explicitly ("allow for the possibility that S_χ(0) isn't small"). So there is no real zero in (1/2, 1). This covers LZZ's q ≤ 4·10⁵, since 1 − 1/(5 log 3) = 0.818 > 1/2.
6. **Independent routes to the same value exist.**
   - Guo Thm 1.1 gives (1−β) log q > 1/100 > 3.0·10⁻³ for every q ≥ 3 "without separate small-conductor zero computations" (Guo p. 2 and end of §5).
   - Banks's qualitative all-q statement (some c > 0) uses only finiteness and does not use LZZ.

**What the defense cannot do.**
- It cannot make LZZ Thm 1.1 verified. The production run (≈150 000 core hours) was not replayed by Banks, by the earlier audit or here.
- The public repository does not pin the production configuration. At HEAD a783ffd, main.c has qMax = 500000, preset smallX1 (λ = 1.4) and N0 = 10 000, and main_by_file.c has N0 = 5·10⁶. The repository has no per-discriminant pass/fail output and no hashes.
- So "every d was covered" rests on the authors' report.
- The Guo route replaces a refereed computation with a new, unreviewed proof of the main claim itself. It is a parallel route, not a stronger one.

## 3. Strongest attack

We looked for an explicit witness in five places. None was found.

**(a) A counterexample to LZZ Thm 1.1.** Such a counterexample would be a real zero β ≥ 1 − 1/(5 log q) with q ≤ 10¹⁰. By LZZ Thm 2.1, it would force (2.5) to hold for every N. Every discriminant we tested violates (2.5) at some N (§4.3). This includes those with χ_d(p) = −1 for all p ≤ 103…127. Those make L(1, χ_d) unusually small, so they are the natural hard cases. No witness.

**(b) An error in LZZ's analytic constants.** We re-derived these from the v2 LaTeX:
- the P-polynomial of Lemma 5.3, from the moments 1/4, 5/16 and 61/64 of sech(πy);
- the convex-interpolation coefficients of Lemmas 6.1 and 6.2;
- the log q coefficients summing to φ;
- K1 and ρ from the J1 interpolation.

We then recomputed every constant in arb (§4.1). Every stated value is ≥ the recomputed value, which is the safe direction. No witness.

**(c) A coverage hole in the run.** We read the code at a783ffd (§4.2).
- The residue filter is right for both signs under C's truncating remainder.
- The loop over d ∈ [−qMax, qMax) misses only d = +qMax, and 10¹⁰ is not a discriminant.
- |d| ≤ 400 000 is skipped, which Platt covers.
- The Kronecker symbol at 2 and at p | d is right.
- The comparison is arb_gt, which certifies a strict inequality.
- The presets match Table 1 exactly.

We found no hole in the code we inspected. We cannot inspect the production configuration (see §2).

**(d) Version drift.** Banks cited LZZ v1. Three v1 passages were corrected in v2:
- an intermediate limit in the proof of Lemma 4.4 ("0 + lim log(1 + 1/(b cos θ))", which diverges as written; the final value α = log b⁻¹ is the same in both versions);
- the J1 step, which in v1 cites only Prop 5.2 but already displays the factor (1 + r⁻¹) that comes from the trivial bound on Re s = 1 + r;
- the truncation remark in the proof of Prop 5.2. v2 adds "at an odd number of terms". The sum over j = 0…1000 has 1001 terms, so v1's numbers are unaffected.

The LaTeX of Lemmas 5.3, 6.1 and 6.2, of Theorem 6.3 and of Corollary 6.4 is otherwise identical. Apparent differences in pdftotext output are extraction artefacts.

The formulas that produce the constants are the same in both versions, Table 1 is unchanged, and we reproduce the table from the corrected v2 formulas. So these are presentation slips in the cited version, not a witness against the theorem Banks uses.

**(e) Margin as a substitute for the computation.** The value 1/5 exceeds 3.0·10⁻³ by a factor of 66. The margin is irrelevant to soundness, though. A single missed discriminant with an exceptional zero would make c arbitrarily small there. This is the real content of U3, and it is a provenance point, not a witness.

How much of q < 10¹⁰ rests on LZZ alone?
- Platt covers q ≤ 4·10⁵ (checked).
- Watkins 2004 covers odd χ with q ≤ 3·10⁸, and Bordignon gives (1−β) log q ≥ 3.0·10⁻³ only for q ≤ 3.17·10⁶ (adj_U3_lzz_constants.out). Both are known to us only through LZZ's summary and were not checked against their originals.
- So, at least, even χ with 3.2·10⁶ < q < 10¹⁰ and odd χ with 3·10⁸ < q < 10¹⁰ rest on LZZ alone.

Banks's own method does not close this range at the value 3.0·10⁻³. In our side computation, with Banks's H, λ, C1 and C2 unchanged, Steps 3–4 close with ω = 22 only for log q ≥ 21.63 (q ≥ 2.47·10⁹). For 8.67·10⁷ = H ≤ q < 2.47·10⁹ they give ω = 23 or 24, and δ0 = 2.94·10⁻³ or 2.82·10⁻³. This side computation is not reviewed and not needed for the verdict. So the dependence that U3 records is genuine. It is disclosed, though, and it is not an error.

**Attack outcome:** no verified_error, no suspected_gap and no missing_hypothesis. The only residual is the unreplayed external computation.

## 4. Independent checks

### 4.1 LZZ analytic constants (adj_U3_lzz_constants.out; arb, 200 bits)

| Quantity | Recomputed | Stated | OK |
|---|---|---|---|
| TZ24: 2Σ(−1)^j log ζ(j+3/2) | 1.498793383 | ≤ 1.4988 | yes |
| TZ24: sup_t exp(…) (max at t = 0) | 2.976544 | C2 = 2.97655 | yes |
| C4 (Lemma 5.3, k = 1; sup P at t = 0) | 5.137806345 | 5.13781 | yes |
| C8 (k = 2) | 9.495616563 | 9.49562 | yes |
| C16 (k = 3) | 18.23873011 | 18.23874 | yes |
| Lemma 4.4 at b = 7/8 (closed form = quadrature) | 1.911944931 | ≤ 1.912 | yes |
| φ, E at λ = 1.6 | 0.2267481057, 1.161302048 | 0.22675, 1.1614 | yes |
| φ, E at λ = 1.3 | 0.2308290915, 1.180416287 | 0.23083, 1.1805 | yes |
| φ, E at λ = 1.2 | 0.2322164917, 1.186929464 | 0.23222, 1.1870 | yes |
| φ, E at λ = 1.1 | 0.2336177301, 1.193517854 | 0.23362, 1.1936 | yes |
| φ, E at λ = 1.4 and 1.0 (code presets) | 0.2294553466, 1.173975515; 0.2350329927, 1.200184881 | 0.22946, 1.1740; 0.23504, 1.2002 | yes |

Using our recomputed C4 and C8 instead of the stated ones lowers E by about 3·10⁻⁷.

Several of LZZ's analytic inputs were not re-proved here:
- the Rademacher Γ-ratio and Phragmén–Lindelöf lemmas;
- the Bennett–Sharpley interpolation lemma;
- Heath-Brown's Jensen formula;
- the explicit formula for ζ′/ζ (which was checked against its standard form).

### 4.2 LZZ code, read only (commit a783ffd)

File hashes:
- src/main.c: b4b7634cf8a3a79899835a129adbcdc67e3f4c4471fdad7c8c75d5b4572efca3
- src/compute.c: dd24cbea134b1c0fe36d9482c7db9fbac2ef8c232fe00bf6e51077a297bbf495
- src/buffered_chi.c: b10243f125ee19b88fdbea379d9a46536182644094e7891d8fb5af3074fa6dd3
- src/presets.c: e61e730845a34872c859d190a53b56b2ac7634cef8e0cc39ef458861eef36fed

What the code does:
- `compute_rhs` is exactly the right side of (2.5), with r = λ/log 10¹⁰ and R = r + 0.875.
- `compute` adds log p·χ(p)/(p^σ − χ(p)) to the precomputed Σ log p/(p^σ − 1) and stops at the first certain `arb_gt`, checked every `checkDistance` primes. Working precision is 50 bits.
- `is_valid_d` implements (3.1) for both signs and excludes |d| ≤ 400 000.
- `chi_val` handles p = 2 through d mod 8 and p | d through 0. Below the 10 000th prime it uses a precomputed Legendre table, whose row and column indexing is consistent with misc/precompute_kronecker.c. Above that it uses FLINT `n_jacobi`.
- `presets.c` rows smallX2, mediumX2, largeX2 and hugeX2 equal Table 1.

What the code does not do:
- The committed run parameters are a small test configuration, not the production run.
- The repository publishes no outputs.

### 4.3 Predicate spot-check (float64, not certified; conditional on LZZ Thm 2.1)

The Kronecker routine agrees with sympy on 200 random d × (82 primes ≤ 27 449 plus the three primes 2 147 483 587, 2 147 483 629 and 2³¹ − 1), with 0 mismatches.

**Random sample.** 300 fundamental discriminants, log-uniform in 4·10⁵ < |d| ≤ 10¹⁰, random sign, seed 20261117, run in 116 s. All 300 pass. 277 pass in row 1 (median 4 645 primes, maximum 59 706 against the cap of 60 000), and 23 pass in row 2 (maximum 2 850 026 primes, for d = −433 572 483). This is qualitatively consistent with LZZ Fig. 1, whose sample is uniform in d and so weighted toward q ≈ 10¹⁰.

**Adversarial sample.** These are d ≡ 5 (mod 8), squarefree, with 4·10⁵ < |d| ≤ 10¹⁰ and χ_d(p) = −1 for every prime p ≤ P. They were found by CRT over p ≤ 23 (modulus 892 371 480, 142 560 classes, 3 194 978 candidates) and then filtered prime by prime. No candidate survives p = 131.

| d | P (χ_d(p) = −1 ∀ p ≤ P) | row that succeeds (λ) | primes needed | largest prime used | cap of that row |
|---|---|---|---|---|---|
| 9 447 241 877 | 127 | 1.1 (row 4) | 104 754 006 | 2 140 112 239 | 130 000 000 |
| 5 534 091 197 | 113 | 1.1 (row 4) | 80 126 701 | 1 614 308 387 | 130 000 000 |
| 1 728 061 733 | 113 | 1.2 (row 3) | 23 748 327 | 447 912 499 | 50 000 000 |
| −1 764 959 683 | 107 | 1.2 (row 3) | 30 126 520 | 575 812 189 | 50 000 000 |
| −585 811 843 | 107 | 1.2 (row 3) | 11 773 960 | 213 306 047 | 50 000 000 |
| −3 341 091 163 | 103 | 1.2 (row 3) | 35 134 668 | 677 248 183 | 50 000 000 |
| −269 497 867 | 103 | 1.2 (row 3) | 10 301 083 | 185 153 999 | 50 000 000 |
| −465 670 363 | 103 | 1.2 (row 3) | 11 076 933 | 199 962 187 | 50 000 000 |
| −411 366 547 | 103 | 1.2 (row 3) | 9 766 561 | 174 995 923 | 50 000 000 |
| 578 729 093 | 103 | 1.2 (row 3) | 6 259 128 | 109 184 213 | 50 000 000 |
| 261 153 653 | 103 | 1.2 (row 3) | 19 948 910 | 372 579 593 | 50 000 000 |
| 1 719 936 077 | 103 | 1.2 (row 3) | 12 721 507 | 231 516 823 | 50 000 000 |

All 12 fail rows 1 and 2, as expected for such d. Ten pass in row 3 and two need row 4. The only d ≡ 5 (mod 8) in the range with P ≥ 127 is 9 447 241 877, and it needs about 81% of LZZ's final cap. The search covered every d ≡ 5 (mod 8) with |d| < 1.07·10¹⁰. Even discriminants were not searched. Run time was 0.5 to 3 minutes per d.

This matches LZZ's report that about 100 moduli survived run 3 and were all resolved in run 4 with 1.3·10⁸ primes. It is not a verification of their run. It is evidence that the pass/fail profile they report is reproducible by independent code on the hardest cases we could construct. In every row we required the left side to exceed the right side by at least 10⁻⁶. That is about 50 times a crude worst-case bound (≈ 2·10⁻⁸) on the float64 accumulation error. The sums are computed in 5·10⁶-term chunks, the left side is about 10, and the first chunk carries most of it.

## 5. Decision and wording

**Classification:** not_an_issue (as a defect). It is recorded as a declared external dependency that was partially re-checked and not replayed.

**Public characterization as an error:** not allowed.

**Allowed wording:** "Banks's all-q constant c = 3.0·10⁻³ is, as Banks states, conditional on the Lu–Zaman–Zhao computation for q ≤ 10¹⁰. The audit did not replay that computation. It reproduced LZZ's analytic constants in ball arithmetic, read their code, and spot-checked their test on 312 discriminants (including the most adversarial ones it could construct) without finding any discrepancy. The qualitative all-q statement, the q ≥ 10¹⁰ constant and Guo's computation-free 1/100 do not depend on it."

**Not allowed:**
- "Banks's constant is unproven, wrong or ambiguous".
- "LZZ's computation is unreliable".
- Any wording that turns our 312-case floating-point spot-check into a verification of the full range.

**Recommended edits to the audit files (not made here):**
- In audit_part1.md §11, audit_part2.md and ARCHITECTURE.md §13, change U3 from "unresolved_ambiguity" to "not_an_issue — declared external dependency (LZZ Thm 1.1), not replayed; constants reproduced, predicate spot-checked (adjudication_U3.md)".
- Keep LZZ in the "not replayed" list.
- Cite LZZ as arXiv:2602.03626 with its version (v1 for Banks's citation, v2 current).

## 6. Known misreadings to avoid

- The spot-check is evidence, not a replay. It covers 312 of about 7.5·10⁹ residue-admissible d. It uses float64, and it assumes LZZ Thm 2.1.
- LZZ Thm 1.1 excludes only real zeros near 1 (σ ≥ 1 − 1/(5 log q)). It says nothing about GRH or about complex zeros.
- "Repairable via Guo" means only that Guo's theorem, if correct, implies the same value. It does not mean Guo has been reviewed.
- The side computation on Banks's own range (q ≥ 2.47·10⁹ at ω = 22) is ours and unreviewed. It is not a claim about Banks's paper.
