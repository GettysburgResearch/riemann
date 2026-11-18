# PAPER-H406 — von Mangoldt1895: targeted original-source audit

Hans von Mangoldt, *Zu Riemanns Abhandlung „Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse“*, Journal für die reine und angewandte Mathematik114(1895),255–305. DOI https://doi.org/10.1515/crll.1895.114.255 . Original GDZ volume PPN243919689_0114, article LOG_0020: https://gdz.sub.uni-goettingen.de/id/PPN243919689_0114 . The first-page footnote links the earlier extract published19July1894; the last page is dated Aachen,2June1894. No exact1895 publication day has been verified. The full article predates de la Vallée Poussin's1896 criticism.

**Version control.** PAPER-H405 is the1894 extract, read through its1896 French translation. This is the longer1895 publication of the same research. Preserve `work_family_id=WORK-MANGOLDT-1894-1895`: these overlapping publication records are not two independent discoveries. The announcement/full-publication counting policy must be explicit; the French translation is not another work.

**Access.** Complete51-page German article accessed2026-11-17. Private extraction `sources/history_round4/mangoldt1895_pp255-305.pdf`,67,800,137bytes, SHA-256 `4a75707d429a2ba3c310e0150bfd00d0c79a2c0d8b94df6eb2fd0a8cc071c3e6`. The original bound-volume URL/hash/byte count and lossless extraction parameters are in `sources/history_round4/mangoldt1895_article_extract_corpus.json` and `mangoldt1895_retrieval_corpus.json`. The551,144,971-byte bound-volume cache was removed after extraction; the article/METS remain. Article printed255–305 = original PDF/physical262–312. Actual endpoint255/305 and interior280 identities were visually verified. All51pages of GDZ OCR are cached with per-page URLs/hashes; cached OCR is not a reading claim.

**Scope.** Original images255,280,282–292,305 substantively read, particularly the complete grouped-limit argument285–292. Bibliographic Level0 plus targeted mathematical analysis; **not a complete51-page Level1 reading or paper-wide technical audit**. Early entire-function/gamma/local-zero-count proofs and later parameter-integration/Li branch arguments remain unaudited. The derived local remainder lemma is in `audits/mangoldt_grouped_remainder_corpus_round4.md`, separately submitted for adversarial review.

## Exact passage and proof architecture

On283–284, equations43–46 separate a paired resolvent integral and compute its individual limit Wν(x,r). On285 the author explicitly asks whether the infinite sum and h→∞ limit can be interchanged. He states convergence in the prescribed increasing-index order and identifies the sum. Here x>1 is fixed, r real, a>0,a+r>1. The local audit does not cover x≤1.

Original notation is αν=βν+iγν, with βν=Re αν>0 and |γν|≤1/2. The audit instead writes γ_j=Re α_j,η_j=Im α_j. The source defines H=#{ν:βν≤h}. Its bν=a+r−1/2+γν lies in the fixed positive interval[a+r−1,a+r]. In denominator majorants one may safely replace bν by the constant b_*=a+r−1>0; this makes the required uniformity explicit.

**286, equation49:** the difference between the partial residue sum through H and the full finite-height integral is decomposed into a bounded coefficient sum times a Perron error, two finite growing kernel-error sums, and an infinite tail above H. This is an exact identity before any limiting operation.

**287:** the paired coefficient sum Σ_(ν≤H)2(r−1/2)/[(r−1/2)²+αν²] is bounded independently of H, by reciprocal-square convergence. The author expressly says the bound holds however large H becomes. Its product with the Perron error tends to zero.

**287–289, equation50 and subsequent bounds:** the growing finite sums reduce to quantities including

\[
 \sum_{\beta_\nu\le h}\frac1{\beta_\nu(h+\beta_\nu)},\qquad
 \sum_{\beta_\nu\le h}\frac1{\beta_\nu(b+h-\beta_\nu)}.
\]

The source partitions[0,h] into intervals2κ, κ=tan1, and applies the earlier local-zero-count bound to each. Explicit integral estimates of the resulting harmonic sums give a displayed289bound of order log²h/h for fixed b>0. The lower bound b_* gives a uniform sufficient version. This retains control when a zero ordinate lies near h.

**289–291, equations51–54:** split the infinite tail into an absolutely summable paired reciprocal-square tail and shifted-kernel terms. The latter are bounded by a multiple of

\[
 \sum_{\beta_\nu>h}\frac1{\beta_\nu(b+\beta_\nu-h)}.
\]

Fixed-size intervals and the local count control a harmonic near tail and integrable far tail. The displayed291bound tends to zero, at most O(log²h/h). This is control of the whole remainder, rather than a sum of unchecked individual limits.

**292, equation55:** equality of the height-ordered residue-series limit and full integral limit follows, giving the arithmetic explicit formula. At r=1/2 the source obtains convergence of Σsin(αν log x)/αν. No arbitrary permutation or uniform convergence across prime-power jumps is licensed.

## Historical adjudication and remaining tasks

Vallée1896 appendix70 alleges that the1894 extract ignores growth of H. The actual translation72 already invokes local-zero-count and kernel inputs. The1895 full article, published before the criticism, explicitly supplies the extended grouped estimates. **No growing-sum error is confirmed in the inspected argument.** This does not certify every step of the full explicit-formula proof.

It would be historically wrong to call the1895 proof a repair prompted by the1896 criticism. The German1894pages891–892 were subsequently compared and confirm the same identity and explicit local-zero-count citation; whole14-pageGermanreading is not claimed. The present reconstruction and source comparison do not establish novelty or a new RH result.

Next: independently check the audit's O(log²h/h) lemma; finish full German1894manifestation reading beyond the already compared891–892; read1895pages256–279 and293–304 before a whole-paper Level1 upgrade; separately audit local counting and the parameter integration/Li branches. Preserve the distinction between the1894/95 O(log²h) global counting remainder and the sharper1905 theorem.
