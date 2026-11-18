> Work identity update, 18 November 2026: PAPER-E001 is the stable alias for the expanded May preprint of [canonical work PAPER-E014](PAPER-E014.md). The following historical notes retain May-specific theorem numbering and reading scope. They do not count as a separate selected work. See the [identity adjudication](../audits/adversarial_reviews/director_baez_whole_round13.md).

# PAPER-E001 — A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis, 2

**Id:** PAPER-E001

**Title:** A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis, 2

**Authors:** ["Luis Báez-Duarte"]

**Date:** 2002-05-01

**Year:** 2002

**Doi:** None

**Arxiv:** math/0205003

**Source url:** https://arxiv.org/abs/math/0205003v1

**Version:** v1

**Family:** ["C", "A"]

**Audit level:** 1

**Read scope:** Complete nine-page preprint text read; ordered-limit argument reconstructed; external dependencies not fully independently checked.

**Access status:** full_text_accessed

**Venue:** arXiv preprint; distinct from original math/0202141 and subsequent published text

**Publication status:** preprint_version_inspected

**Source file:** baez_duarte

**Main result:** In H=L²((0,infinity),dx), let rho_a(x)={1/(a x)}, chi=1_(0,1], and B_nat=span{rho_a:a in positive integers}. RH iff chi belongs to the H closure of B_nat (Theorem1.1, pp.1–2). Under RH, for some c>0, ||chi+sum_{a<=n}mu(a)exp(-c log(a)/loglog(n))rho_a||_H << (loglog(n))^(-1/3) (Proposition3.1, pp.6–8).

**Proof architecture:** ["RH plus Balazard–Saias truncated Möbius estimate", "Mellin transform of fractional part is -zeta(s)/s in 0<Re(s)<1", "Functional-equation ratio bound Lemma2.2", "H convergence n→infinity for fixed sufficiently small epsilon", "H convergence epsilon↓0 to -chi, then closure"]

**Limitations:** ["No RH-independent construction attaining convergence is supplied.", "The two limits are ordered; pointwise convergence of raw Möbius truncations does not imply H convergence.", "Proposition3.1 is a sketch with external input.", "Displayed integrability range in p.5 needs epsilon<1/4 for the particular majorant; sufficiently small epsilon suffices."]

**Historical importance:** Reduces continuous dilation parameters to integer dilations; turns an abstract closure criterion into arithmetic approximation.

**Reusable lemma:** Lemma2.2 bounds |zeta(1/2-epsilon+it)/zeta(1/2+epsilon+it)| by C(1+|t|)^epsilon, for 0<=epsilon<=epsilon0<1/2, interpreted at removable common zeros; the functional equation supplies the modulus bound.

**Research questions:** ["Can a quantitative uniform error bound replace the sequential limiting argument?", "Which smoothing schemes preserve norm convergence with a useful explicit rate?"]

**Accessed at:** 2026-11-17

**Original notation:** See downloaded source; normalized notation in this record uses rho for a zero except rho_a in E001.

**Source sha256:** 13a2dcc763d3fdd5b52afc87845c6d77c83764a56aab06f574a91ee43c8a152b

**Correction search status:** arXiv history inspected; exhaustive later-correction search incomplete
