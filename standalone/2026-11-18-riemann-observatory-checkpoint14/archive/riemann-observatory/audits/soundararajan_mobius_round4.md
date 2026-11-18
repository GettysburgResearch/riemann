# Original Soundararajan Möbius source: dependency reconstruction

Date:17November2026. Source PAPER-E013, actual arXiv0705.0723v2. All11pages read. This is a substantive-reading and scoped-reconstruction audit, not a whole-work Level2 promotion or a claim of novelty.

## Source theorem and later refinement must remain distinct

OriginalTheorem1 p1 proves underRH M(x)≪sqrt(x)exp(sqrt(logx)(loglogx)^14). PAPER-C103 explicitly quotes this exponent14, then explains that modifications of the same method yield5/2+delta. Its stronger inverse-Dirichlet-polynomial approximation also handles an imaginary shift in the coefficients. The exact later delta-dependent definition of typical height differs from the original conditions3V and unscaled interval lengths, so the two sources cannot be substituted without tracking that change.

## Proof dependency tree

Theorem1 -> Propositions4,5 + truncated Perron + low-height inverse-zeta estimate(Titchmarsh14.14.2).

Proposition4 -> Theorem2 + prime-polynomial large sieve(Lemma8) + Goldston–Gonek local zero-count estimate.

Theorem2 -> Selberg interval majorants(Lemma6) + explicit formula(Lemma7) + prime large sieve(Lemma8).

Proposition5 -> Lemma9(local cluster integration) + Lemma10(smoothed prime/zero identity) + Lemma11(typical prime polynomial and localF bound).

Lemma6's construction is displayed, but its full Beurling/Vaaler source ancestry is accepted rather than independently proved. Lemma7 is an explicitly cited classical formula; in its RH application the zeros are1/2+i gamma. Lemma8 is cited from Maier–Montgomery and not reproved from their original paper. These are recorded external inputs, not silently audited theorems.

## Theorem2: where the moment restriction enters

Use exponential typeDelta=(1+eta)logT/(2piV),eta=1/logV. The interval-majorant error is logT/(2piDelta)=V(1−eta+O(eta²)). If the zero count exceeds its expected value byV, a prime or prime-square polynomial must have modulus at leastetaV after negligible higher powers. Fourier support limits its length toT^((1+eta)/V); hence the large sieve permits onlyk<=V/(1+eta).

The coefficient variance isO(loglogT): logp times the Fourier coefficient is bounded uniformly, and the prime harmonic sum gives the logarithm. The resulting Markov bound is

R≪T(logT)^2 [C k loglogT/(eta²V²)]^k.

Taking the largest admissiblek gives the displayed−Vlog(V/loglogT)+3VloglogV exponent. The precise length^k<=T restriction is an obstruction to inserting an unrestricted Gaussian high-moment estimate. The prime-square term has smaller coefficient variance and no worse length restriction. The rangeh<=sqrtT is used in the gamma-factor smoothing error, not merely in the count interpretation.

## Typical height -> reciprocal-zeta bound

For sigma>1/2 defineF(s)=sum_gamma (sigma−1/2)/[(sigma−1/2)^2+(t−gamma)^2]. Absolute local convergence follows from the zero count; Hadamard and Stirling give Re(zeta'/zeta)=F−(1/2)logT+O(1).

Lemma10 p8 is obtained from the exact inverse-Mellin kernel x^w/w² applied to−zeta'/zeta(z+w), followed by a contour shift and horizontal integration fromsigma to2. For2<=x<=T, the pole/trivial-zero terms are uniformly absorbed inO(1) after that integration. The nontrivial-zero remainder is bounded by x^(1/2−sigma)F/[(sigma−1/2)(logx)^2]. Its positivity and the exact distance factor are essential.

Atx=T^(1/V),sigma>=sigma0, one has(sigma−1/2)logx>=1, so the bracketed remainder coefficient is bounded by2. Typicality(i) bounds the prime polynomial below by−2V. Typicality(ii) boundsF≪logT by dividing ordinates into one-sided intervals of length2piV/logT; the two sides contribute only an absolute factor. The tail beyond distance1/2 isO(logT). This provesLemma11's stronger lower bound−CV and hence the stated−VloglogV for sufficiently largeV.

For1/2<sigma<sigma0, integrateF horizontally. The exact expression to bound is

(1/2)sum_gamma log{[(sigma0−1/2)^2+(t−gamma)^2]/[(sigma−1/2)^2+(t−gamma)^2]}.

The finest typicality condition controls the coefficient of the divergent log[(sigma0−1/2)/(sigma−1/2)] near an actual zero. It cannot be replaced by a generic totalzero-count bound with an unspecified multiple ofV.

### A precise central-width choice for the reconstruction

To apply condition(iii) literally to one central interval, take|t−gamma|<=piV/((logV)logT), whose **full width** is the stated2piV/((logV)logT). It then contains at mostV ordinates, giving exactlyV times the logarithmic distance ratio. Divide the remaining near ordinates into one-sided intervals of length2piV/logT, starting at the above radius. Each pair contains at most6V zeros; the resulting sum is bounded by

3V sum_(n>=0) log[1+1/(4pi²(n+1/(2logV))²)]
 <=6VloglogV+O(V).

The far tail isO(V²/logT)=o(V). Thus the claimedLemma9 bound with7VloglogV follows for sufficiently largeT,V. This explicitly specifies the half-width/full-width distinction; it is a rigorous reconstruction of the lemma, not an asserted counterexample to it or a new error finding.

## Perron contour and rarity cost

For x with fractional part1/2, the truncated Perron formula atc=1+1/logx and heightfloorx has errorO(logx). The central vertical segment extends to exp(sqrt(logx)); its crude inverse-zeta loss gives exp(sqrt(logx)loglogx), below the final claimed bound. At each integer height interval beyond it, choose a minimal typicality parameterV_n and move to real part1/2+V_n/logx. Horizontal connectors are bounded using the two neighboring parameters. The intervals can be organized with a fixed dyadic sizeT so the typicality definition and the exceptional-count theorem have the same scale; no change of prime-polynomial cutoff is silently assumed.

Summing over a dyadic block produces the rarity-weight balance

exp[V log(logx/logT)−V log(V/loglogT)+13VloglogV].

The small-V block contributes at mostexp((loglogx)^4). Maximizing the displayed exponent over the allowedV and summing dyadic heights gives the source's exponent14. The later method refinement changes these losses and thresholds; this reconstruction does not assert that14 is optimal or the best present bound.

## Concrete remaining questions

1. Audit the original large-sieve and Beurling-majorant dependencies if a whole-paper Level2 audit is desired.
2. Reconstruct the later5/2+delta refinement from its own source definitions rather than attributing it toTheorem1 here.
3. For the growing-Riesz array, prove a weighted average reciprocal-zeta estimate with the exact vertical translations before importing a typical-height distribution. The current worst-height proof does not automatically benefit from a count of rare heights.
4. If using a proposed Gaussian exceptional bound, state it for all three typicality failures over the full allowedV range. A zero-count theorem alone omits condition(i).

No numerical experiment is substituted for these analytic transitions. The inspected source and reconstructed portions reveal reusable mechanisms and exact matching requirements; no new arithmetic theorem or RH proof is claimed.
