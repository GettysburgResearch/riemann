# Round three: arithmetic support survives the strongest deletion tests

This report adds evidence-supported model mathematics and source corrections. It claims no new theorem about actual zeta zeros, no proof or disproof of RH, and no priority-verified novel result. Source ingredients often prove older and stronger than a modern abstract suggests; Pólya1926 is a central example.

## What the strongest countermodel now preserves

For everyN>=1 there is a real symmetric entireF, normalizedF(0)=F(1)=1, with a positive even smooth double-exponential kernel whose second logarithmic derivative is strictly negative everywhere. Its zeros have the Riemann–von Mangoldt smooth count withO(1) error, and exactly four lie off the critical line. The quartet can be placed above any prescribed finite height. Every firstN Li coefficient is strictly positive; every positive-degree Taylor coefficient ofF(1/(1−z)) is positive. A separate generic-parameter refinement makes every zero simple.

The model is explicit up to a one-variable tuning equation with a proved root. Letw=s−1/2, a=1/4, Q_T(w)=((w−a)^2+T²)((w+a)^2+T²), and letM_delta be the normalized MGF of the compact density proportional to(delta²−u²)^(3/4). Setc=2pi exp(2delta), F=A K_(w/2)(c)Q_T(w)M_delta(w). ForT=10N(8N²+50), a suitable0<delta<.01 exists and lambda_n>1/[12(8N²+50)²] for1<=n<=N. Fixed-T tuning can retain double line zeros; avoiding a countable collision set gives the all-simple existence statement with an adjustableT. Those quantifiers must not be merged.

DefineZ=pi^(s/2)F/[s(s−1)Gamma(s/2)] with NO factor1/2. This gives the standard completion and functional equation, residue1 at1, value−1/2 at0 and exactly simple negative-even trivial zeros. It is bounded on each fixed right vertical strip and has the correct leading maximal-modulus scale. Its real right limit is1.

Nevertheless Z(sigma)=1−b/sigma+O(sigma^−2), b=c²/2+21/(32delta)−3/16>0. An ordinary Dirichlet series convergent in some half-plane instead has an exponentially small tail after its first coefficient. This exact algebraic discrepancy rules out an ordinary integer Dirichlet expansion. Bounded critical-line values also imply mean squareO(X), so matching ordinary upper growth bounds does not reproduce the actual zeta moment asymptotics.

The point is precise: symmetry, smooth counting, strong kernel shape, standard gamma completion, finite positivity and finitely many exceptional zeros do not replace arithmetic. No argument retaining a genuine Dirichlet expansion or prime-side explicit formula is refuted. The classical Bessel zero/count theorem is Pólya1926; the assembly's priority is unassessed. Full proofs and independent rational sign certificates are in the Bessel/beta audits and director_round3_adjudication.md.

## When finite Li tests finally detect the quartet

For any tuned branch and quartet heightT→infinity, the first negative coefficient exists and satisfies

n_-(T)=8T²logT+8T²loglogT+8(log2)T²+o(T²).

The proof compares the uniform Bessel contribution .5nlogn+O(n), negligible beta contribution and exact quartet term4[1−cosh(n eta_T)cos(n theta_T)], eta_T~1/(4T²), theta_T~1/T. It excludes every earlier index and constructs a phase-aligned later index. The resulting sharp model-only inverse scale isT~(1/2)sqrt(N/logN). This is an asymptotic result with no effective starting height or claimed computed first-negative index. The masking mechanism was already described by Bombieri–Lagarias and Lagarias; the archive does not claim its discovery.

## A constructive window removes a finite-model obstruction

The unchanged linear reciprocal taper fails near merging roots. A fixed higher-power scalar taper succeeds uniformly for every configuration of a fixed numberm of unit-circle roots:

A_M(z)=Sum_(n=0..M−1)b_n(1−n/M)^m z^n, where1/Q=Sum b_nz^n.

The squared H2 error is at mostK_m/M, with explicit degree-only constants and no separation denominator. Its leading error at complete coalescence ism²/M, matching the exact optimum. The proof's twisted finite-difference identity pairs a k-th taper difference with onlyk reciprocal factors; crude bounds on the entire reciprocal sequence miss this cancellation. Constants grow rapidly withm. This does not prove a growing-cluster or arithmetic estimate. Exact quadratic worst-case and fractional-power threshold refinements have separately recorded review statuses in the campaign files.

The one-cluster exact optimum also gives the complete growing-multiplicity transition: E~m²/N holds exactly whenm=o(sqrtN); ifm²/N→lambda, E→1−exp(−lambda), while larger multiplicity makesE→1. This is a finite degreeN, not automatically a logarithmic Dirichlet cutoff.

## A converse theorem makes the missing arithmetic condition concrete

Original Hamburger1921, original Knopp1994, the author's2000 restatement, Burnol's weaker-growth extension and the source Mellin/distribution dictionary were inspected at explicit scopes. An Euler product is not a hypothesis of the relevant self-dual converse. Ordinary integer Dirichlet support is enough, together with the exact completion, finite-pole/growth hypotheses, to force a zeta multiple.

The mechanism can be seen in a short conditional distribution proof: integer support makes the Fourier transform periodic; a quasi-homogeneous self-dual discrepancy extends to a constant; periodicity then forces equal Dirac-comb masses. The deeper analytic dictionary remains a named external/partially reconstructed dependency.

Knopp's abundance is normalized withGamma(u), reflection1/2−u. In the standard variablet=2u, its ordinary series becomes a generalized series with frequencies sqrt(n). A later preprint's literal standard-variable background attribution needs this qualification. Its explicit main examples use generalized frequencies or relax finite-pole regularity and remain outside the converse theorem. The journal version and exhaustive corrections have not been compared. No main theorem is declared false.

## Moment information needs a genuinely one-sided certificate

An ordinary Christoffel function bounds the largest mass at its evaluation point; it does not by itself give a positive-inertia fraction. Two independent exact finite Hermitian witnesses refute the unrestricted reading of an informal AF higher-moment remark. The correct dual task is to bound the positive-halfline indicator by a globally valid polynomial minorant. Negative roots of the minimizing polynomial can invalidate the naive inference.

For the source's actual conditional sine moments(1,1,4/3,2,13/4), the polynomialp=1−7x/4+2x²/3 DOES satisfy p>=1 onx<=0 and E p²=5/36. Hence1−p² is valid and gives positive inertia31/36 and, using the separate source block/count assumptions,13/18 simple-critical. Thus a narrow qualification repairs the generic remark without refuting that specific conditional consequence or the main theorem. A regular-case canonical-quadrature replacement is recorded with all its hypotheses; singular and limiting cases are not silently included.

## Answers to the original synthesis questions

**Conceptual transitions.** The provisional source-grounded map runs from Riemann's analytic continuation/functional equation and prime-zero inversion to zero-free-line/PNT methods, Hilbert-space and positivity equivalences, quantitative analytic estimates, zero statistics/random-matrix models, geometric purity, and modern finite optimization/formal verification. Many landmark originals remain unread; this is not a completed1000-work history.

**Closest to meaningful incremental progress.** The most reviewable targets here are arithmetic bounds for grouped zero residues, precise uniform prime-side moments, source-exact formal replay, effective finite certificates and corrected moment-dual conditions. No evidence supports ranking an approach as close to an RH proof.

**Historical ideas worth reuse.** Pólya's exact Bessel models, Beurling's weaker-closure character argument, original Riesz/Möbius summation and distributional integer-support rigidity supply sharper tools than vague modern analogies. The investigation does not establish that these ideas were historically neglected.

**Strongest new connections.** No connection has passed a complete publication-priority search. The strongest new-to-this-run interfaces are confluent Gram stability to grouped residues, passive realization to asymmetric count cost, zero-free strips to unbuffered nuclear localization, and positive-kernel countermodels to exact Dirichlet/converse obstructions. Their established and conjectural portions are explicit.

**Recurring obstacles.** Growing/infinite limits, uniform constants, sparse exceptional zeros, actual operator domains, integer arithmetic support, pole control and one-sided positivity recur across approaches. Each has an explicit failed inference or countermodel in this archive.

**Credible technical issues.** Repaired trace geometry, the informal Christoffel qualification and the background Knopp normalization comparison have precise independent evidence. Additional Lagarias contour and historical/transcription issues are retained with their current review/prior-correction status; they are not advertised as newly discovered false theorems.

**New claims independently established.** The finite and generic model propositions, exact computational certificates and scoped replacement lemmas described above have independent checks. No new infinite arithmetic theorem for the actual zeta function or priority-verified novel theorem is claimed.

**Failed tests.** Linear smoothing is not collision-uniform; a global unscaled bounded-cluster Riesz model cannot accommodate zeta density; real-axis unitarity does not imply positive spectral flow; a nondense common restriction cannot invoke finite-defect interlacing; zero-buffer relative-HS control does not imply operator-o(1); and generic analytic resemblance does not provide a Dirichlet series. These are preserved as negative knowledge.

**Twenty-five next problems.** Current exact targets and failure controls are in top_25_research_opportunities.md. Completed finite subproblems are removed from the active queue rather than repeatedly investigated.

**What a strong team should do first.** Verify the full prime-moment/formal boundary while deriving one genuine arithmetic estimate on the zero-removed factor. In parallel, finish primary-source/version checks and select the next source corpus by dependency value. Use the exact countermodels and corrected moment conditions to reject invalid hypotheses early. A growing mass of summaries is not a substitute for that work.
