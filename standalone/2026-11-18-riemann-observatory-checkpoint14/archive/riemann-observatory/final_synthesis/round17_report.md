# Round 17 — sharp test-space boundaries and bounded arithmetic countermodels

Research cutoff: 18 November 2026 UTC. This checkpoint contains **1,010 selected works, 965 accessed full texts, 13 additional excerpt-only sources, 131 complete substantive readings, nine whole-work Level 3 audits and 123 scoped adjudicated groups**. Its structured archive has 489 theorem, conjecture and exercise records, 97 connections, and 2,691 graph nodes with 2,658 edges. One further catalogued work is deferred. The 5,203 provider matches are an overlapping discovery pool, not additional reviewed works.

The principal results are precise boundaries for a Mellin explicit-formula test space and countermodels for an arithmetic inference from progression norms. Their proofs have separate advocate, skeptic and director records, with fresh independent checkpoint reviews. Publication novelty has not been established. No proof or disproof of RH, improved zero-free region or improved zero-density exponent is claimed. The thousand-work reading program remains unfinished: 879 selected works still have Level 0 coverage.

## The universal signed and absolute thresholds are different

For a test f on (0,infinity), write h(s)=integral f(x)x^(s-1)dx and F(u)=exp(u/2)f(exp u). Fix 0<epsilon<1/4 and consider tests with some value-decay margin delta>epsilon, so f(x)=O(x^delta) at zero and O(x^(-1-delta)) at infinity. The logarithmic strip norm is

```text
N_p²=integral_(-epsilon)^(1+epsilon) integral_R
       sqrt(1+t²) log^p(e+abs(t)) abs(h(beta+it))² dt d beta.
```

For the literal local class in the pinned Bombieri–Lagarias manuscript, the following are universal guarantees, rather than necessary conditions for each individual test. That local class permits finitely many exceptional points with finite one-sided limits of both f and f′ and midpoint values for f. For the positive statements one may instead assume continuity and local H^1 regularity of F near u=0.

| Norm exponent | Ordinary symmetric height formula | Absolute zero sampling |
|---|---|---|
| p>3 | Guaranteed | Guaranteed, with a quantitative tail estimate |
| 0<=p<=3 | Guaranteed | A universal guarantee fails |
| p<0 | A universal guarantee fails, even for a smooth test | A universal guarantee fails |

The symmetric cutoff is sum over abs(Im rho)<=T, with multiplicities and every endpoint height. It is not a height subsequence or an averaged summation convention. The critical p=0 positive proof uses uniform sharp Fourier inversion and a folded completed-function contour. A separate Selberg proof gives convergence on each half-height axis for p>1; the smaller exponents above are statements about symmetric summation.

The absolute threshold uses holomorphic area mean value, local zero counting and a weighted cell estimate. At p=3 a real smooth source-admissible test has finite norm and divergent absolute zero trace. Its signed symmetric sum nevertheless converges by the critical theorem. This compatibility result prevents one summation mode from being silently substituted for the other.

[Critical positive theorem and source hypotheses](../audits/adversarial_reviews/director_signed_mellin_round16.md) · [Absolute threshold and smooth endpoint witness](../audits/adversarial_reviews/director_critical_endpoint_round15.md).

## One smooth test defeats every strict logarithmic weakening

The new counterexample is stronger than failure of a proof estimate. On one fixed strip there is **one real smooth test**, vanishing near zero and one and satisfying f(x)=O(x^(-3/2)), such that N_(-q) is finite for every fixed q>0. All its prime-power samples f(n) vanish, as do f(1/n) for n>=1. Its pole and compensated archimedean terms are absolutely finite. Yet its signed symmetric zero sums have a subsequence tending to negative infinity and another bounded subsequence.

The construction places shrinking one-sided oscillatory packets immediately after escaped prime logarithms. For a fixed prime center, a packet with width W=log^A(T)/T and carrier T, with 0<A<q, has weakened squared norm bounded by a constant times

```text
W sqrt(T) + T W/log^q(T),
```

which tends to zero. Its sharp inverse at the prime center grows as log(TW)/(2pi), up to its fixed amplitude and tilt. That one arithmetic atom gives the large negative contribution to the finite zero contour. Other prime-power centers remain separated from the shrinking support, and the gamma functional is uniformly controlled in the weakened norm because the packets vanish near the logarithmic origin.

At stage j choose q_j=1/j and A_j=q_j/2 before choosing its enormous carrier. Make the new norm summable, dominate all earlier packet traces at the new witness height, and make its contribution tiny at the finitely many protected earlier heights. For each fixed q>0 the stage norms are eventually dominated by the q_j norms. This gives one witness for all strict logarithmic weakenings without any uniform bound as q decreases to zero. Protecting a later height at which each finite prefix has settled gives the bounded subsequence.

The same test belongs to every polynomial strip space with weight (1+t²)^s for s<1/2. Its critical norm is infinite, consistently with the positive theorem. The weaker norms diverge as q decreases to zero.

At each fixed prime-power argument, Fourier inversion of this final smooth function converges correctly. The failed step is passing that limit through the **infinite** weighted prime sum. This isolates a concrete exchange-of-limits obstruction despite strong value decay, interior smoothness, strip analyticity and an absolutely defined arithmetic target. A vanishing upper-bound argument at p=0 and a counterexample at every strict weakening now fit together.

[Complete proof and independent reviews](../audits/adversarial_reviews/director_negative_mellin_round17.md) · [Fresh checkpoint audit](../audits/adversarial_reviews/checkpoint14_negative_math_final_review.md) · `OBS-MELLIN-ALL-NEGATIVE-LOG-SIGNED-DIVERGENCE` · `THM-MELLIN-EXACT-SIGNED-LOG-BOUNDARY`.

These statements concern the stated norm scale and local class. A compact jump test from the original arithmetic criterion belongs to a different valid summation argument. The examples do not invalidate that criterion or Weil positivity. Luecking's general Bergman embedding explains the ambient absolute-sampling threshold; Weil's original contour and later variation formulations are acknowledged in the bounded provenance comparisons. No priority claim follows from the archive's reconstruction.

## Common, positive and bounded data still leave a moving phase uncontrolled

The remaining long-prime fourth-moment reduction needs a prescribed additive Fourier mode. Earlier work showed that unrelated residue rows can satisfy two strong norm budgets while their projection is too large. The current round removes the assumption that those rows may be chosen independently: the countermodels come from one sequence, so their complete residue rows have exact common-divisor compatibility.

Fix 1/2<theta<2/3, K comparable to T^theta and an integer P comparable to KT. Use a narrow relative prime band whose entire fourth-power coefficient support S lies in [K,2K), including repeated factors. It has size comparable to K/log^4 K and coefficients 1<=c_k<=24. There exist sequences of exact mass P on the integer interval [P,2P) with either

- real values in [1/2,3/2], or
- integer values in {0,1,2}.

For their residue counts B_(k,u), both satisfy

```text
sum_(k≤2K) sum_(u mod k) abs(B_(k,u)−P/k)² = O(PK),
sum_(k≤2K) max_(u mod k) abs(B_(k,u)−P/k) = O(K sqrt(P)).
```

The latter has every fixed logarithmic saving relative to P. On unit residues the same orders hold about each row's induced unit mean. Nevertheless their real unit-centered projection

```text
sum_(k in S) (c_k/k) sum_((n,k)=1) b(n)
       [cos(2pi n/k)−mu(k)/phi(k)]
```

is positive and at least a constant times K sqrt(T)/log^4 T. It exceeds T log^4 T by a divergent factor. Thus common-sequence consistency, positivity, bounded weights and these two discrepancy budgets alone do not supply the desired mode.

The bounded construction combines a cosine sum over the full modulus shell with a short positive convolution. The classical second-derivative estimate bounds that cosine sum by O(sqrt(T)); scaling it gives the pointwise cap. The convolution suppresses the low-denominator multiplicities in the pooled residue variance while retaining the moving frequencies. A finite rational-frequency Gram estimate identifies a positive diagonal on every fourth-power modulus, including repeated-prime factors. Its strict error margin uses theta<2/3. Independent adjacent-integer rounding and a small exact-mass repair preserve the cap, the variance order and the positive projection.

The centering distinction is decisive. These estimates use **P/k or the induced unit-row mean**. A prime-supported measure in this long interval is simultaneously supported on units of the band moduli and has reference mean P/phi(k). The construction does not meet that different variance specification. It does not give a lower bound for actual primes or the full smoothed C_* sum. A bounded pointwise cap has now been shown insufficient for the displayed ordinary-integer budgets; the sieve profile and prime-model unit baseline remain available arithmetic information.

[Bounded construction, source estimate and exact scope](../audits/adversarial_reviews/director_bounded_common_checkpoint14.md) · [Fresh independent audit](../audits/adversarial_reviews/checkpoint14_bounded_math_final_review.md) · [Earlier larger-signal common-sequence construction](../audits/adversarial_reviews/director_common_sequence_round17.md).

## What has been checked but remains separate from the admitted claims

A further rough-support campaign shows that excluding all the band primes preserves a useful phase-energy scale and permits a positive rough-supported sequence with a large phase. It has **not** established the P/phi(k)-centered progression variance bound. Masking after convolution destroys the multiplier identity used above. A direct sieve error estimate falls short; failure of that upper estimate is not a lower bound on the true error. These partial calculations and independent review are retained as pending research, rather than combined into an unsupported stronger counterexample.

Von Mangoldt's 1895 German paper, printed pp.255–305, received two complete independent 51-page readings and is now Level 1. They reconstruct the count with its historical O(log² h) error, grouped height tails, midpoint values and equation (64). A global reading of a uniform-convergence sentence on p.293 needs qualification; compact-x uniformity suffices for the subsequent fixed-x proof. This remains a conditional domain interpretation in the reading reports, not a new verified author-error finding. Whole-work Level 3 adjudication of these 51 pages remains pending. Riemann's first-print whole audit and the known Genocchi correction retain their earlier precise scope.

The findings ledger remains at 59, with 17 version-specific verified groups. No new author-error entry is added by this round.

## A clean continuation point

The highest-value next arithmetic task is to formulate and prove, or refute, a variance statement with the **actual prime-model unit baseline** while preserving the moving Fourier mode. The bounded ordinary-integer counterexample identifies exactly why the displayed norm budgets alone are insufficient. The separately proved rough-support phase estimate identifies a partial ingredient, not the missing variance result.

For the analytic test-space results, the next task is an expert comparison with the precise published function-space literature and a small formalization of the packet estimate or finite Fourier identities. The program has documented complete proofs and bounded provenance searches, not established publication novelty. Numerical positivity work should use the appropriate absolute-tail certificate rather than infer it from signed convergence alone.

For the corpus, complete the whole-source adjudication of von Mangoldt and continue the highest-priority unread dependencies before expanding the metadata pool. The [one-day guide](../START_HERE.md), [twenty-five ranked tasks](top_25_research_opportunities.md) and [executable continuation](../CONTINUATION.md) identify the current statements, exact source pins and pending work. The archive is a reusable research checkpoint, not a completed thousand-paper audit or a claimed resolution of RH.
