# Round 13 — an explicit fourth-moment obstacle and checked limits of extrapolation

Literature cutoff: 18 November 2026 UTC. This remains an active research checkpoint. The archive contains 1,001 selected works, 956 accessed full texts, 13 additional excerpt-only sources, 126 complete substantive readings, seven version-pinned whole-work Level 3 audits, and 103 scoped adjudicated claim groups. The catalogue has 1,002 canonical identities including one deferred supporting work. The theorem ledger has 449 claims and exercises, and the connection ledger has 85 records. These counts measure different kinds of work; most selected works still require complete reading. There is no proof or disproof of RH, improved zero-free or zero-density exponent, or established claim of publication novelty.

The most useful new arithmetic output is a reduction of one fourth-moment extension to one explicit signed sum. The reduction survives three independent reconstructions. The sum has not been bounded as required. The strongest negative output is that the same all-order formal extrapolation fails positivity at every fixed integer root-tilt rank. Exact finite and source-based checks explain why that failure does not contradict the valid low-moment formulas or the full intrinsic random-matrix law.

## A concrete arithmetic problem replaces a broad analogy

Assume RH. Fix 0<a<b with 1/8<b<1/6 and let D(s) be the sum of p^(-s) over Y^a<p≤Y^b. Expectations here use the established symmetric strict derivative-square weighted zero tail. Put W=Re D, H0=log(b/a), d=b−a and m_j=(b^j−a^j)/j. The 3+1 and 2+2 terms of W^4 are already within the source shifted-moment range because their longest side is at most Y^(3b)<sqrt(Y). A sixth absolute moment is also controlled. Only the pure term Re E D^4 is missing.

The exact difference from the formal fourth cosine coefficient is one eighth of the pure-arm difference, up to o(1). Its pure-arm target is

```text
4! [z^4] exp(H0 z) [(1−d z)^4+2m3 z(1−d z)+3m2² z²].
```

A one-sided continuous shifted moment against a bounded-coefficient polynomial of length y≤T^theta, theta<1, has error bounded by T^epsilon times [(yT)^(1/2)+y^(1/4)T^(3/4)]. Thus that continuous estimate does not impose the half-power obstruction. An independently checked smooth contour construction also removes the reflected saddle error: a compact comparable-height cutoff w_T with two transitions of width H=T^kappa works for (1+theta)/2<kappa<1. This is a smooth saddle theorem; it does not improve the source's hard arithmetic cutoff. Sharp zero-sum endpoints are recovered separately after differentiation.

Write c_k for the coefficients of D^4, theta=4b and C_*=d_2*(Lambda log²). The remaining sufficient estimate is

```text
Re sum_(k≤Y^(4b)) (c_k/k) sum_(m≥1) C_*(m) w_T(2πm/k)
 [exp(−2πim/k)−mu(k/gcd(m,k))/phi(k/gcd(m,k))]
   = o(T log^4 T),  T comparable to Y.
```

The bracket is the additive phase minus its average over all unit numerators modulo k. It includes noncoprime m and the modulus-one case exactly. Fully differentiating the source's three shifted factors first produces the coefficient of −zeta'^3/zeta and an elementary divisor-logarithm term. Both Poisson summation with a smooth hyperbola split and an independent Hurwitz–Mellin argument remove all two-factor divisor derivatives with arbitrary power saving. The identity

```text
−zeta'^3/zeta = (1/2)[−zeta² (zeta'/zeta)''
                           +zeta zeta'''−3zeta' zeta'']
```

then leaves one half of the displayed C_* sum. The arbitrary saving applies to these discarded divisor terms; the contour and saddle errors retain their own proved bounds. No cancellation estimate for C_* follows from its nonnegative coefficients. Absolute values over character expansions discard precisely the Gauss phases that may be needed. This is a publishable-problem candidate with an exact sufficient condition, rather than an asserted new fourth-moment theorem. Publication priority remains to be checked.

[Director proof and full hypotheses](../audits/adversarial_reviews/director_pure_fourth_round13.md) · [Independent fixed-sequence adjudication](../audits/adversarial_reviews/uniform99_fixed_sequence_adjudication.md) · `OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION`.

## The intrinsic model has a larger window, then explicit corrections

For the globally derivative-square tilted rooted CUE model, the limiting joint cosine–sine moments of total degree r agree with coefficients of

```text
exp(H0 z_c+H0(z_c²+z_s²)/4)
 [(1−d z_c)^4+2m3 z_c(1−d z_c)−3m2² z_s²]
```

when rb≤1. The separate arithmetic source window is rb<1/2 under RH. Neither the model's larger range nor numerical agreement extends the arithmetic theorem.

At the first intrinsic crossing, (r−1)b≤1<rb, the cosine raw-moment correction is strictly negative and equals −2^(1−r) times the integral of 2−4t+2t³ over x_i in [a,b], t=sum x_i>1, with measure product dx_i/x_i. Mixed cosine–sine directions can have a different sign or vanish. The finite N=40 calculation with modes 9,10,11 gives the exact fourth discrepancy −3384187/302541624000. A continuum enclosure for band (0.22,0.28), near −1.116093794622113479066e−5, has an independently checked exact rational width below 2.63e−27. Numerical certificates verify the specified calculation, not an arithmetic transfer or convergence rate.

For every fixed integer rank J≥1, the finite-window cosine coefficients have a Gaussian-exponential factor times a determinant polynomial of degree at most J². Its all-order extrapolation has a positive real zero and cannot be a probability moment sequence. For J≥3, a two-by-two principal minor at z=1/d is −20(m3/d)²; continuity forces an earlier zero. Finite polynomial-square witnesses exist, although this checkpoint does not give a useful uniform degree. The first-crossing cosine correction has alternating rank sign (−1)^(J+1). These statements apply to the formal extension and intrinsic model in their stated ranges.

[Exact windows, boundary cases and adversarial checks](../audits/adversarial_reviews/director_cue_windows_round13.md).

## An exact 2026 determinant identity rules out a tempting shortcut

Petrov's arXiv:2605.24976v1 Theorem 4.4 applies directly to the finite polynomial-tilted Toeplitz numerator. It factors that numerator into a Gram determinant and an oblique-tail Fredholm determinant, with explicit normalization. Both factors are strictly positive on the real Laplace axis. The tail contributes at order two even inside the valid moment window, so the normalized Gram alone cannot be the formal complementary polynomial.

For N=4,J=2 and frequency 2 the normalized Gram and complementary determinant have quadratic coefficients 33/800 and −3/200 respectively, a gap of exactly 9/160. The optional fixed-tail chart in Proposition 4.6 can become singular at a positive parameter while the theorem's factors stay positive. This rejects an incorrect identification; it finds no error in Petrov. A useful next problem is uniform control of the full tail quotient, retaining both factors and higher frequency corrections.

[Version-pinned source comparison and exact replay](../audits/adversarial_reviews/director_petrov_round13.md).

## Tightness has a sharp universal threshold, with classical antecedents

Suppose grid-node pth increment moments satisfy C min(h^a+epsilon_n,A_n h^b), with p,a,b>1, A_n≥1 and epsilon_n→0. With tight initial marginals, the polygons are universally tight if A_n epsilon_n^(b−1)→0. A randomly located shrinking spike shows that this is sharp as a guarantee over all grids and laws. It is not a necessary condition for each individual process or every prescribed grid.

The proof gives a quantitative two-scale modulus, requires no lower mesh-spacing bound, and caps interpolation exponents at p. Passing to step processes still requires vanishing mesh or jumps, or an exact composition with a suitable converging clock. Clock convergence alone does not compare unrelated interpolations. For the arithmetic envelope A=L² and epsilon=L^(−M), the universal threshold is M>2; the direct exponent is 2M/(M+2). A locally compiled Lean theorem checks only the elementary M=6 scalar implication from two assumed inequalities. It does not formalize the probabilistic or arithmetic inputs.

Garsia–Rodemich's 1974 reproduction of GRR and Billingsley's 1968 tightness and random-triangle passages are now source-pinned dependencies. Their classical mechanism takes precedence over any claim of novelty for this reformulation. Independent review also caught an incorrect exponent in an internal GRR gauge derivation; that derivation was corrected before integration. The separate dyadic proof was unaffected.

[Exact quantifiers, corrected proof and Lean scope](../audits/adversarial_reviews/director_two_scale_round13.md).

## Source audits changed both counts and a theorem's hypotheses

Báez-Duarte's February and May deposits and 2003 Lincei paper are manifestations of one work. A contemporary author self-citation and the primary texts support the merge. Both deposits, numbering and historical references remain traceable. The seven-page journal proof has a whole-work Level 3 adjudication with explicit local normalization and range repairs; its principal criterion and rate conclusion survive. Merging identities lowers work counts rather than padding the target.

Hughes–Rudnick's 2002 journal note now has the seventh whole-work Level 3 audit. Its printed averaging class permits a fixed positive bandlimited weight

```text
w(u)=sum_(j≥1) 2^(−j) b(u−exp(4^j)),
```

where b is a normalized nonnegative bandlimited Schwartz function. This weight has infinite first logarithmic moment. A positive-integral test gives a zero statistic growing as (integral f/log T) log(1+|tau|)+O(1), so the printed averaged first moment is infinite for every fixed T>1. The exact repair for moments through m is integral f=0 or finite integral w log^m(2+|u|). The oscillatory prime moment result survives on the printed weight class; its variance has no extra missing factor. A provisional factor-two allegation was withdrawn after checking the actual rendered source.

This is a narrowly versioned missing-hypothesis finding, independently witnessed and repaired. The ledger now has 52 findings, ten groups flagged for witnessed version-specific false assertions; these are neither ten erroneous papers nor ten failed main theorems. Complete readings of Gonek (1984) and von Mangoldt (1905) were added, but their whole-work adjudications and several original-source issues remain pending. The original Riemann memoir also remains at complete-reading scope pending director adjudication.

[Báez-Duarte audit](../audits/adversarial_reviews/director_baez_whole_round13.md) · [Hughes–Rudnick audit and repair](../audits/adversarial_reviews/director_hughes_rudnick_whole_round13.md).

## What this changes in the research program

The historical transition from Riemann's transform and explicit formula to positivity, spectral and probabilistic frameworks is documented in earlier numbered reports. This round adds a practical lesson: a finite formula can be mathematically correct yet become incompatible with positivity when extrapolated. Analytic support, integrability and uniform limiting arguments recur across apparently different programs. They should be recorded as explicit missing lemmas rather than absorbed into an analogy.

The nearest concrete progress identified here is an incremental weighted fourth moment, not an all-or-nothing RH proof. Its remaining signed sum now has one fixed coefficient sequence and exact modulus structure. The most useful neglected material remains proof passages, alternative manifestations and classical modulus tools whose hypotheses can be compared precisely; no forgotten route to RH was established. The strongest independently reconstructed deductions are the C_* reduction, all-rank extrapolation obstruction, first-chamber corrections and sharp universal tightness statement. Their priority remains unresolved.

Several plausible ideas failed: discarding the tilted Fredholm tail, treating a finite moment surrogate as a full probability law, inferring tightness from clock convergence alone, and deriving a source variance error from a text-extraction omission. These failures have explicit witnesses or corrected proof steps. No unresolved allegation about an author is elevated to a verified finding.

For a team starting tomorrow, the first tasks are to attack the signed C_* estimate with its Gauss phases intact; quantify higher intrinsic frequency corrections while keeping the exact determinant factors; and audit the number-theoretic interfaces needed for effective bounds. The [25 research problems](top_25_research_opportunities.md) and [continuation instructions](../CONTINUATION.md) give further tasks. New strata estimates and finite Hankel-degree bounds developed during release preparation remain in separately reviewed working notes, outside this checkpoint's canonical claim ledger until director integration.

The 5,203 provider metadata candidates have not all been deduplicated or relevance-reviewed; 56 lexical exclusions and the curated selection decisions are distinct records. Selection scale has been reached, but 875 selected works remain at bibliographic or targeted-reading Level 0. Completion means substantially improving that evidence state and the mathematical results, not adding more entries. The current archive is an executable checkpoint of that unfinished program.
