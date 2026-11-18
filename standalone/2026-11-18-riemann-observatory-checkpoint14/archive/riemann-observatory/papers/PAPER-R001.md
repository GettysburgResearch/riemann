# PAPER-R001 — An Elementary Problem Equivalent to the Riemann Hypothesis

Jeffrey C. Lagarias. Publication: American Mathematical Monthly 109 (2002), 534–543. DOI [10.1080/00029890.2002.11919883](https://doi.org/10.1080/00029890.2002.11919883). Inspected source: [arXiv:math/0008177v2](https://arxiv.org/abs/math/0008177v2), 6 May 2001, nine PDF pages, internal manuscript date 5 May 2001. The journal version was not compared. Author-hosted retrieval returned HTTP403; arXiv PDF succeeded 2026-11-17.

## Scope and evidence

Level 1 substantive reading of the entire inspected version; scoped Level 2 reconstruction of §3 transfer argument and finite computation. Original Robin dependencies were not re-proved. This is not a complete technical audit of Robin's theorem or of the publication version.

## Exact content

Let H_n=sum_{j=1}^n 1/j and σ(n)=sum_{d|n}d. Theorem1.1 (PDF p1), with Problem E (1.1), states RH is equivalent to σ(n)≤H_n+exp(H_n)log H_n for all integers n≥1, with equality only n=1. Natural logarithms throughout.

Lemma3.1 (§3, pp6–7): for n≥3, exp(H_n)log H_n≥e^γ n log log n. Its proof writes H_n=log n+γ+∫_n^∞{t}/t² dt. Positivity of log log n is needed when multiplying lower bounds; n≥3 supplies it.

Lemma3.2 (§3,p7): for n≥20, H_n+exp(H_n)log H_n≤e^γ n log log n+7n/log n. These elementary bounds are combined with two statements attributed to Robin: RH implies σ(n)≤e^γ n log log n for n≥5041 (Proposition3.1); if RH fails, there are C>0 and β∈(0,1/2) such that σ(n)≥e^γ n log log n+C n log log n/(log n)^β infinitely often (Proposition3.2). Here β can lie between 1−Reρ and1/2 for a zero Reρ>1/2. These are *source-reported dependencies*, not independently audited Robin results.

## Architecture and quantifiers

RH → Robin bound beyond5040 → Lemma3.1 → strict Problem E beyond5040; finitely many smaller integers are checked. Conversely, assuming Problem E for every n and ¬RH gives infinitely many Robin excesses; their ratio to7n/log n is (C/7)(log n)^{1−β}log log n→∞, contradiction. No explicit first-counterexample bound follows because the oscillation subsequence and C are not effective data here.

Sections1–2 give historical motivation through Gronwall maximal order, colossally abundant numbers and Ramanujan's suppressed sections. They do not make elementary reformulation into an elementary RH proof.

## Independent finite check

experiments/code/lagarias_finite.py checks all n≤5040 with integer lower bounds. At scale S=2^80, h=sum floor(S/j)≤SH_n. exp(h/S) is bounded below by100 positive Taylor terms with every multiplication rounded down. log(h/S) is bounded below by100 terms of2atanh((h−S)/(h+S)), also rounded down. Both factors are nonnegative. Therefore computed B/S≤H_n+exp(H_n)log H_n. The program verifies B−Sσ(n)>0 for n=2..5040 and exact equality at1. Minimum certified absolute gap is at n=2, >0.31716. The certificate is exact integer arithmetic, not a floating-point heuristic, and independently rechecks the finite dependency stated by the paper. No claim of new mathematics.

## Research follow-up

The comparison slack has sharper asymptotic Δ(n)~e^γ γ n/log n; see independent_campaigns/lagarias_slack.md. An explicit bound on Δ can improve numerical screening thresholds but cannot remove the need for an oscillation theorem or infinite tail proof. A sparse test strategy needs a proved reduction from *all* integers to its chosen extremal set and exact tie conventions in colossally abundant numbers.
