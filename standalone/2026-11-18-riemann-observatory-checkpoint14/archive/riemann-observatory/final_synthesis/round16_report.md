# Round 16 — signed convergence at critical regularity and a whole audit of Riemann

Cutoff: 18 November 2026 UTC. The live archive contains **1,010 selected works, 965 accessed full texts, 13 additional excerpt-only sources, 130 complete readings, nine whole-work Level 3 audits and 120 scoped adjudicated groups**. There are 482 theorem, conjecture and exercise records, 95 connections, and 2,680 graph nodes with 2,631 edges. The catalogue includes one further deferred supporting work. The findings ledger remains at 59 findings, including 17 independently witnessed version-specific error groups; this round adds no author-error finding.

The main mathematical outcome resolves the signed convergence question left open in the dated Round 15 synthesis. The ordinary symmetric explicit formula holds at the critical Mellin strip H^{1/2} norm, even though absolute sampling can fail under a substantially stronger logarithmic weight. A separate continuous cusp shows why the local condition at one matters. The whole-source audit of Riemann's ten-page first print is complete, with its original claims, later proofs and known historical corrections kept distinct. An adjacent Bergman embedding paper was selected and completely read. No RH resolution, improved zero-free or zero-density exponent, or established publication novelty is claimed.

## Signed and absolute sums have different regularity requirements

Let f be continuous on (0,infinity), with f(x)=O(x^delta) at zero and O(x^(-1-delta)) at infinity. Set F(u)=exp(u/2)f(exp u), and let h be its Mellin transform. Assume F belongs to H^1 near u=0 and, for 0<epsilon<delta,

```text
N_0²=integral_(-epsilon)^(1+epsilon) integral_R
          sqrt(1+t²) abs(h(beta+it))² dt d beta < infinity.
```

Then the ordinary inclusive symmetric sum over the nontrivial zeta zeros, counted with multiplicity, converges unconditionally to the compensated Guinand–Weil formula:

```text
lim_(T→infinity) sum_(abs(Im rho)≤T) h(rho)
 =h(0)+h(1)−sum_n Lambda(n)[f(n)+f(1/n)/n]
  −(log pi+EulerGamma)f(1)
  −integral_1^infinity
    [f(x)+f(1/x)/x−2f(1)/x²] x/(x²−1) dx.
```

The prime and archimedean terms are ordinary absolutely convergent expressions. The zero sum need not converge absolutely. The same theorem applies with any stronger weight sqrt(1+t²)log^p(e+abs(t)), p>=0.

The manuscript's literal local condition (A) already gives the needed local regularity when this critical norm is finite. Both f and f′ have finite one-sided limits at its finitely many exceptional points, and f has midpoint values. The central Fourier trace lies in H^{1/2}, whose Gagliardo seminorm rules out genuine jumps. Continuity together with the locally bounded one-sided derivatives then gives local H^1. This implication retains the derivative part of the printed hypothesis; merely saying piecewise differentiable would be insufficient.

Consequently the earlier real smooth p=3 example has a **convergent signed symmetric sum and a divergent absolute zero sum**. The distinction is a proved compatibility result on the actual zeros, not an analogy with a random spectrum.

## The endpoint step is uniform sharp Fourier inversion

Holomorphic mean value controls the weighted vertical traces uniformly on an inner strip, including their high-frequency tails. For each such line the physical function F_beta(u)=exp(beta u)f(exp u) is continuous and exponentially decaying. Compare sharp Fourier inversion with a Gaussian approximate identity. The difference multiplier has uniformly bounded squared norm against dt/sqrt(1+t²). Splitting into a fixed low-frequency range and a small weighted high-frequency tail makes the difference tend uniformly to zero. Thus the sharp inverse itself converges uniformly in the physical point and the line.

A shorter Fejér comparison gives the same endpoint fact: the difference from the sharp multiplier is abs(t)/T on abs(t)<=T and zero elsewhere, with squared inverse-weight norm at most one. Neither argument assumes absolute Fourier integrability at the endpoint.

Fold the completed-function logarithmic-derivative contour onto Re s=a>1. The folded test is h(a+it)+h(1-a-it), with a plus sign. The right-edge zeta logarithmic derivative has an absolutely convergent Dirichlet series. Uniform sharp inversion now permits its limit to pass through the prime series. Good-height horizontal bounds and the local zero count restore **every** height, including zero ordinates. The spectral sum is not Cesàro averaged and is not restricted to an admissible subsequence.

The gamma part needs separate treatment. Its Stirling expansion has both a logarithmic term and different constant values on the two height half-axes. Split the physical function near zero, where local H^1 gives an absolute logarithmic transform integral. Away from zero divide by iu; its transform is a primitive with weighted L^2 bounds and a vanishing logarithmic boundary. This proves the required conditional gamma convergence. Compact cutoff and mollification identify the exact compensated formula while preserving a uniform value envelope. Only the gamma functional is claimed continuous in norm plus local H^1; the prime approximation also uses that envelope.

An independent Selberg route remains valuable. The uniform near-line density estimate and the second moment of S(T) give absolute convergence of the off-line projection and counting-remainder corrections for p>1. This route establishes separate convergence on each half-height axis. The critical p=0 contour result above asserts symmetric convergence. Those modes are not silently identified.

[Complete statement, source passages and three proof reviews](../audits/adversarial_reviews/director_signed_mellin_round16.md) · `THM-MELLIN-CRITICAL-STRIP-SYMMETRIC-EXPLICIT-FORMULA` · `LEM-MELLIN-SELBERG-PROJECTION-AND-COUNT-REMAINDER`.

## Removing local regularity can make both sides diverge

A distinct continuous real compactly supported test has finite p=3 norm but raw symmetric sums tending to positive infinity. In frequency, take a positive even profile comparable to 1/[abs(t)log²(abs(t))loglog(abs(t))]. It is L^1 and weighted L^2, but its logarithmic integral diverges. A positive-definite smooth compact physical multiplier preserves the weighted norm and produces a nonnegative central transform with the same lower tail.

The Selberg projection and count-remainder pieces converge, while the smooth logarithmic zero density diverges positively. A separate folded-contour calculation confirms the sign. Fourier inversion and Tonelli also show the matching divergence of the local compensated archimedean term. The physical test is smooth away from x=1 but lacks the finite derivative behavior required by (A) there. This is a boundary example for the general continuous class, not a further error attributed to the manuscript.

The broader lesson is specific: a global strip norm and endpoint values control different operations from the local subtraction at one. A finite norm does not automatically license every singular integral or every ordering of zero terms.

## The first-print Riemann audit is complete

PAPER-S001 is the ninth whole-work Level 3 audit. Two agents read and reconstructed all ten actual German first-print pages, and the director read those pages alongside the complete Wilkins translation. The original print controls differences among manifestations. The audit covers both continuation arguments, the theta kernels, zero count forecast, paired product, prime-power transform, midpoint inversion, branches, ordered zero series, Möbius inversion and the final empirical claims.

The product has a concise modern reconstruction: G(w)=Xi(sqrt(w)), defined by the even Taylor series, has order exactly 1/2. Genus-zero Hadamard factorization gives the paired product without RH or a zero-count asymptotic. This supplies a missing proof ingredient in the original growth paragraph; it is not credited as an 1859 proof of Hadamard's later theorem.

Product normalization must be carried into inversion. Evaluating at the modern completed-function value xi_*(0)=1/2 gives the arithmetic constant **-log 2**, replacing the first print's +log Xi(0). Genocchi already derived that correction in 1860, pp.57–58, equation (11); the director inspected the original. The 1892 collected note records it too. The related centered-contour shift is the same correction, not another discovery.

The ordered logarithmic-integral series requires a later von Mangoldt midpoint formula and a summable O(abs(Im rho)^(-2)) remainder. Distributional inversion alone does not supply pointwise raw convergence. The known branch convention is continuation with log(x^rho)=rho log x. A new principal logarithm of the exponentiated number would change the terms. Local zero counts identify height order with the memoir's magnitude order.

The first print's missing sum and simple-pole sign are visibly repaired in the 1892 edition. The Wilkins intermediate theta-limit discrepancy belongs to those transcriptions; the original limits and all final theta formulas are correct. No new author-error flags are added. The root-reality assertion remains conjectural. Finite spectral differentiation and historical tables do not establish a square-root prime-counting error or a permanent sign for li(x)-pi(x).

[Whole-memoir adjudication, exact source hashes and page ledger](../audits/adversarial_reviews/director_riemann1859_whole_round16.md) · `THM-RIEMANN1859-MODERN-GENUS-ZERO-PAIRED-PRODUCT` · `THM-RIEMANN1859-MODERN-ORDERED-J0-FORMULA`.

## A general predecessor and two finite arithmetic constants

Daniel H. Luecking's 1986 seven-page paper, *Multipliers of Bergman spaces into Lebesgue spaces*, was admitted as a source-backed H-family dependency and completely read by two independent agents. It remains Level 1. Its exact embedding criterion, transferred to the strip, explains the ambient absolute-sampling thresholds: the cell condition is sum_j N_j²/w(j)<infinity. It supplies neither the physically constrained smooth witness nor the signed criterion by itself. The theorem, original proof and strip transfer are recorded with their actual hypotheses. [Primary publication](https://doi.org/10.1017/S001309150001748X) · [Source and comparison](../audits/adversarial_reviews/prime146_mellin_trace_prior_art.md).

Weil's 1952 text already contains the folded contour and ordinary cutoff framework. Its later final-formula test class adds derivative decay. The critical criterion here assembles a different sufficient interface from classical ingredients; no novelty of the method or priority of the combined statement has been established. The [bounded signed-criterion comparison](../audits/adversarial_reviews/analytic156_signed_critical_provenance.md) states which original texts and formulations were checked and which remained unavailable.

The explicit Gonek input ledger also advances. For positive integer derivative orders mu,nu, M=mu+nu and L=log z, the log-power divisor convolution has the beta-integral main term, with error at most

```text
[min(mu,nu)+1/e+mu^mu nu^nu/M^M] z L^M.
```

Centered floor summation and unimodality prove this for every real z>1, including integer cutoffs. A convenient rational (1,1) bound 9zL²/4 combines with the earlier explicit Abel estimate to give the finite Lemma 8 remainder x[(19/4)log³x+(229/4)log²x+90log x] for x>1 and real abs(delta)<=1/2. Zero derivative orders have separate endpoint bounds. These finite constants do not provide a full contour or weighted-tail onset.

[Proofs, conventions and exact finite application](../audits/adversarial_reviews/director_gonek_constants_round16.md) · `LEM-GONEK-EXPLICIT-POSITIVE-DERIVATIVE-CONVOLUTION`.

## Next work and remaining coverage

The long-prime moving-phase target from Round 15 is still an arithmetic priority. Padded factorability is available; a fixed-residue theorem still does not supply the required simultaneous Fourier mode. Testing how much common-sequence compatibility strengthens the phase-blind norm budgets is a concrete next campaign. The logarithmically weaker signed strip classes are a separate next-round investigation; no sharpness claim below the critical weight is part of this checkpoint.

For analysis, instantiate usable local zero-count constants and certified trace tails for an actual positivity test, and compare the signed criterion with the precise existing variation classes. For the historical program, audit the later von Mangoldt ordered-limit proof completely. For numerical derivative tails, continue the explicit ledger through the gamma and contour steps. The [twenty-five ranked tasks](top_25_research_opportunities.md) retain the broader approximation, geometry, spectral and random-matrix programs.

The thousand-work mission is unfinished: 880 selected works still have only Level 0 coverage. Whole-source audit, scoped theorem verification, bibliographic discovery and physical access remain separate counts. The archive has accumulated precise reusable mathematical interfaces and negative examples; it has not replaced the remaining source work with invented summaries.
