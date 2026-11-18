# A divergent admissible test and two sufficient Mellin repairs

18 November 2026. The director inspected the controlling author-manuscript pages 5–6 and 8, reconstructed the packet counterexample independently, and read the three separate counterexample reviews and the independent Sobolev and critical-logarithmic proofs. The broad test class printed in this exact manuscript is insufficient for its stated raw height limit. A smooth witness establishes the failure. The fixed compact tests used in the paper's main arithmetic theorem retain a valid midpoint argument. The multiset criterion is unaffected.

Source scope: Bombieri–Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, the twelve-page author-hosted manuscript with internal title `final11aug.dvi`, date unverified, SHA-256 `cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0`. [Pinned author source](https://websites.umich.edu/~lagarias/doc/bombieri.pdf). A separate official journal PDF was not checked. The findings below are not assigned to an uninspected journal manifestation. Two independent complete manuscript readings are recorded separately; this note is a scoped mathematical adjudication, not a whole-work promotion.

## The exact assertion under test

The manuscript's condition (A) permits functions on (0,infinity) continuous and continuously differentiable except at finitely many points, where **both f and f′** have at most first-kind discontinuities, with midpoint values for f. Thus the one-sided derivative limits at an exceptional interior point are finite. Condition (B) bounds the **function** by O(x^delta) at zero and O(x^(−1−delta)) at infinity for some delta>0. It imposes no matching derivative decay at either end. The counterexample below is smooth at every interior point, so it satisfies the full local condition, including the requirement on f′.

For h(s)=integral_0^infinity f(x)x^(s−1)dx and tilde f(x)=f(1/x)/x, p.6 asserts the explicit formula with the zero side interpreted as

```text
lim_(T→infinity) sum_(|Im rho|≤T) h(rho),
```

over the nontrivial zeros, counted with multiplicity. The Mellin integral is holomorphic on −delta<Re s<1+delta, but that fact alone does not supply the asserted zero-sum convergence.

## A fixed smooth witness for which the stated height limit fails

Fix delta>0 and a nonnegative smooth bump psi supported in (−1/8,1/8), of integral one. Define

```text
a_j=exp(−(1/2+delta)j), b_j=exp(−(1+delta)j),
F(t)=sum_(j≥1) a_j psi(t−j) cos(Gamma_j t),
f(x)=x^(−1/2) F(log x).
```

The supports are locally finite and disjoint. Thus f is real C-infinity on (0,infinity), vanishes near zero and near one, and is O(x^(−1−delta)) at infinity. It meets the literal conditions with no exceptional points. Its derivative may grow rapidly at infinity, which the printed conditions do not forbid.

Choose the frequencies Gamma_j inductively using the actual zeta ordinates. The unconditional Riemann–von Mangoldt count gives order T log T zeros in [T,2T]. Partitioning this interval into cells of radius at most 1/(20j) produces a cell containing a constant times log T/j zeros. T can be chosen arbitrarily large. Pick a cell containing at least j/b_j zeros, avoid ordinate endpoints, and let Gamma_j be its midpoint.

On that cell the matching Fourier part of packet j has real Mellin value greater than b_j/3, uniformly for every possible zero real part beta in [0,1]. Indeed |(gamma−Gamma_j)t|≤9/160 on the bump and exp((beta−1/2)t)≥exp(−j/2−1/16). The other half of the cosine is small at the large carrier frequency.

Each bump has a Fourier transform decreasing faster than any fixed inverse power, uniformly in beta on this strip. At step j, choose the frequency threshold large enough that the entire past contribution on its new cell is below b_j/24, and that its contribution on each earlier cell i is below 2^(−(j−i))b_i/24. The nonresonant half costs another b_j/24. Summing the future geometric constraints gives at most b_j/24 on the fixed cell. All these are finite constraints at each stage; zero counting still provides a sufficiently populated cell above the threshold. This explicitly defines an infinite witness by induction. It is not a numerical list of feasible low-height frequencies.

For the final test, every zero in cell [A_j,B_j] therefore has

```text
Re h(beta+i gamma)>b_j/5.
```

Reality of f and conjugation symmetry give

```text
S(B_j)−S(A_j)>2j/5,
S(T)=sum_(|Im rho|≤T) h(rho).
```

These intervals escape to infinity, contradicting the Cauchy criterion. No RH or information about where beta lies inside [0,1] was used. The Mellin integral itself is absolutely convergent: packet absolute integrals are bounded by a constant times exp(−delta j).

Every term of the claimed arithmetic side is absolutely defined. The prime sum is dominated by sum (log n)n^(−1−delta); tilde f(n)=0 for n≥1. Both smooth integrals converge. The archimedean integral has no local singularity because f and tilde f vanish near one and f(1)=0. At infinity its remaining integrand is integrable. The failure is exactly the stipulated raw height sum. Adding the involution does not cure it: rho→1−rho permutes every fixed height set, so symmetrization preserves the divergent increments.

The published status and any later correction of another manifestation remain separate questions. The result here is a verified missing-regularity counterexample to the pinned manuscript's broad auxiliary statement. It neither refutes RH nor invalidates the paper's main Li criteria.

[First complete construction](geometry130_explicit_formula_countermodel.md) · [Independent lacunary proof](weighted130_explicit_formula_countermodel_review.md) · [Third source and compact-test adjudication](analytic131_explicit_formula_countermodel_adjudication.md).

## A sufficient strip-Sobolev condition

Here is a directly checkable repair. Let f be continuous and have the preceding value-decay bounds. Choose 0<epsilon<delta. Its Mellin transform is holomorphic in a neighborhood of the closed strip [−epsilon,1+epsilon]. For a regularity exponent s>1/2 suppose

```text
N_s(f)²=integral_(-epsilon)^(1+epsilon) integral_R
             (1+t²)^s |h(beta+it)|² dt d beta <infinity.
```

Then the zero sum converges absolutely, without RH, and the explicit formula is valid with its ordinary absolutely defined arithmetic side:

```text
sum_rho h(rho)=h(0)+h(1)
 −sum_(n≥1) Lambda(n)[f(n)+tilde f(n)]
 −(log pi+EulerGamma)f(1)
 −integral_1^infinity [f(x)+tilde f(x)−2f(1)/x²] x/(x²−1) dx.
```

This is a sufficient condition, not a necessary one. The jump tests used later in the manuscript require their separate midpoint treatment.

The bound is quantitative. Let C_N be any valid unconditional constant with at most C_N log(2+|n|) zeros in every height cell [n,n+1), including multiplicities. Set r=min(epsilon/2,1/4). Holomorphic disk mean value gives

```text
sum_rho |h(rho)| ≤ C_N/(sqrt(pi) r)
 [2·5^s sum_(n in Z) log²(2+|n|)/(1+n²)^s]^(1/2) N_s(f).
```

The same bound for |Im rho|>T uses only indices |n|>T−1 in the displayed series. In particular the tail is O_(s,epsilon,C_N)(N_s(f) T^(1/2−s)log(2+T)). No numerical value for C_N is invented here; an explicit source-count constant can be inserted when a certified numerical application is prepared.

Proof of the constant: use expanded rectangles with real coordinates [−r,1+r] and heights [n−r,n+1+r]. Each height belongs to at most two rectangles, and 1+n²≤5(1+t²) there. Cauchy–Schwarz over cells gives exactly the convergent series above. The disk mean-value argument also controls each interior vertical weighted-L2 trace, including beta=1/2. Thus a separate physical trace assumption is unnecessary.

Log-coordinate cutoff and smooth mollification converge in the full strip norm. Multiplication by a log-coordinate cutoff acts by a uniformly bounded approximate convolution in the weighted Fourier space. Log-coordinate mollification gives a bounded Fourier multiplier through the exponentially tilted compact mollifier, uniformly in beta. The central H^s trace gives a positive Hölder exponent at x=1. This controls the local archimedean singularity, while the original value decay gives dominated convergence for the remaining integrals and prime sum. Start with the classical smooth compact explicit formula and pass to the limit. This independently proves the repaired formula rather than citing the overly broad auxiliary statement.

[Complete proof](analytic132_mellin_trace_repair.md) · [Independent approximation review](weighted132_mellin_trace_repair_review.md) · [Third constant and tail check](uniform133_mellin_repair_adjudication.md).

## A weaker critical logarithmic class

The same method gives a larger sufficient class. For p>3 replace (1+t²)^s by

```text
w_p(t)=sqrt(1+t²) [log(e+|t|)]^p,
N_log,p(f)²=integral_(-epsilon)^(1+epsilon) integral_R
                  w_p(t)|h(beta+it)|² dt d beta.
```

Finite N_log,p implies absolute zero sampling and the same explicit formula, with tail

```text
O_(p,epsilon,C_N)(N_log,p(f) [log(2+T)]^((3−p)/2)).
```

One may use the explicit cell constant

```text
C_N/(sqrt(pi) r)
 [2 sqrt(5) 2^p sum_(n in Z) log²(2+|n|)/w_p(n)]^(1/2).
```

Indeed w_p(n)≤sqrt(5)2^p w_p(t) in each rectangle. The tail-series condition is sum 1/[n log^(p−2)n]<infinity. Independently, the central weighted Fourier trace yields the modulus

```text
|F(u)−F(0)| ≪ N_log,p(f) [log(e/|u|)]^((1−p)/2),
F(u)=exp(u/2) f(exp u), |u| small.
```

Its Dini integral is finite for p>3. Thus the same exponent condition handles both the log-density of zeros and the archimedean singularity. Smooth cutoff and mollification work for this moderate logarithmic weight. No claim of necessity, optimality or failure at p=3 is made.

The enlargement is strict even among smooth functions satisfying the original value bounds. Take disjoint log-coordinate bumps at j, carriers Gamma_j=2^(j²), and amplitudes

```text
a_j=Gamma_j^(−1/2) [log(e+Gamma_j)]^(−p/2) j^(−2) exp(−2j).
```

Use F=sum a_j psi(u−j)cos(Gamma_j u) and f=x^(−1/2)F(log x), with epsilon=1/4. It is C-infinity and O(x^(−2)) at infinity, and its critical logarithmic strip norm is finite by summing the translated packet norms. In each fixed carrier window its Fourier modulus is bounded below by a constant times a_j after demodulation; all other carriers have uniformly negligible tails. Every s>1/2 Sobolev strip norm then diverges because Gamma_j^(2s−1) dominates the remaining exponential and polynomial factors in j. This example is not the divergent-zero-sum witness above: its critical norm gives a valid absolutely convergent formula.

[Critical proof](analytic135_critical_log_mellin_repair.md) · [Independent critical and strict-inclusion proof](weighted135_critical_log_repair_review.md) · [Third critical adjudication](uniform136_critical_log_adjudication.md).

## A separate finite-cutoff identity and why the main theorem survives

At n=1, epsilon=2/3, the manuscript's compact truncation has Mellin transform (1−epsilon^s)/s. The finite equality (3.5), p.8, drops the gamma compensation beyond x=1/epsilon. For general fixed n the missing term is

```text
n integral_(1/epsilon)^infinity dx/[x(x²−1)]
  =−(n/2)log(1−epsilon²)>0.
```

At this witness it is (1/2)log(9/5). There is no coincident prime-power endpoint. The two integrals and finite prime sum give, before this correction,

```text
log(3/2)+1/3−(log pi+EulerGamma)/2−log(6/5).
```

The valid compact-test formula adds the positive missing term. Its size is O_n(epsilon²), so it disappears in the limit used by Theorem 2. The fixed compact tests are valid independently: the leading endpoint 1/rho terms have the classical height-star convergence, the remaining terms are absolutely summable, and even log-coordinate smoothing yields their stated midpoint values. The counterexample to the broad noncompact class cannot be transferred to them. [Independent finite computation and qualifications](geometry127_bombieri_lagarias_adjudication_input.md) · [Compact bridge](analytic131_explicit_formula_countermodel_adjudication.md).

## Research significance and next steps

These are source-specific mathematical repairs and local reusable lemmas. Their mechanisms use classical zero counting, holomorphic mean value and Fourier approximation. Publication novelty has not been established. The actual new knowledge in the archive is a complete witness for a previously only suspected hypothesis problem, plus precisely stated spaces on which the formula is justified. The [final independent review](analytic138_director_mellin_final_qa.md) checked the exact constants, negative-height tail indexing, approximation, strict inclusion and finite-cutoff computation.

The next concrete tasks are to insert an explicit local zero-count constant and evaluate the trace norm for test functions used in numerical positivity work; compare the logarithmic space with existing explicit-formula test spaces; and investigate the endpoint p=3 without assuming the present sufficient condition is sharp. Any finite positivity certificate still covers only its stated tests, not all of Weil's criterion.

Subsequent scoped work in this round proves the [p=3 failure of universal absolute sampling](director_critical_endpoint_round15.md). The [bounded prior-art comparison](prime146_mellin_trace_prior_art.md) recovers the ambient analytic-strip threshold from Luecking's general Bergman embedding theorem and documents Weil's original derivative-decay condition in the accessed French transcription. The elementary norm proof, its explicit constants and the physically constrained smooth witness are recorded with these predecessors; they are not advertised as a new general embedding principle. Signed endpoint convergence remains separate in the Round 15 adjudicated ledger.
