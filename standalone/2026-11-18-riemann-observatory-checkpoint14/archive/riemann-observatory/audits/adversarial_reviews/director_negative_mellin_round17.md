# The signed critical weight cannot be weakened logarithmically

18 November 2026. The director proposed the escaped-prime packet construction, independently reconstructed its norm and trace estimates, read the full advocate and skeptic, and checked the separate Fourier-packet and diagonal reviews. There is **one real smooth test in every strictly negative logarithmic strip space whose ordinary symmetric zero sums fail to converge**. The arithmetic side is finite and every prime-power sample vanishes. Together with the critical signed theorem this determines the exact boundary in this logarithmic scale for the stated source-admissible class. Publication novelty has not been established.

Evidence: [full construction](weighted160_negative_log_counterexample_campaign.md), [independent skeptic and bounded subsequence](geometry160_negative_log_skeptic.md), [independent Fourier packet lemma](analytic160_negative_log_packet_lemma.md), [diagonal review](analytic165_diagonal_log_weakening_review.md), and [bounded provenance and isolated-atom comparison](weighted164_negative_log_provenance.md). The [critical positive theorem](director_signed_mellin_round16.md) uses the same Mellin and Fourier conventions. No RH, simplicity, zero-spacing model, or numerical zero computation is used.

## Exact statement

Fix a strip [-epsilon,1+epsilon] with 0<epsilon<1/4. There exists a real f in C-infinity(0,infinity), zero near zero and one, with f(x)=O(x^(-3/2)) at infinity, such that for its Mellin transform h and **every fixed q>0**,

```text
N_(-q)²=integral_(-epsilon)^(1+epsilon) integral_R
   sqrt(1+t²)/log^q(e+abs(t)) · abs(h(beta+it))² dt d beta < infinity.
```

All prime-power values f(n) with Lambda(n) nonzero are zero; f(1/n)=0 for n>=1. Nevertheless the real sums S(T)=sum_(abs(Im rho)≤T)h(rho), with multiplicity, have a subsequence tending to negative infinity and another bounded subsequence. They therefore have neither a finite limit nor a limit at infinity. The pole and archimedean terms are absolutely finite.

The same witness belongs to every polynomial strip space with weight (1+t²)^s, s<1/2, since each such weight is bounded by a constant times the q=1 weight. Its critical norm N_0 is infinite by the positive theorem. Monotone convergence gives N_(-q)→infinity as q decreases to zero. The assertion has the quantifiers “one f, each fixed q,” not a uniform norm bound in q.

## One packet: a large sharp inverse with small weakened norm

Choose a prime p, put u_*=log p, and fix its physical amplitude b=exp(-u_*). Take smooth cutoffs eta and chi with eta zero at and below 1 and one at and above 2, and chi one near zero and supported in (-1,1). For fixed q>0 and 0<A<q let

```text
W=(log T)^A/T,
F_T(u_*+v)=b chi(v/W) eta(Tv) sin(Tv).
```

Its support is on the positive side 1/T<v<W. As T grows it can be placed before the next prime-power logarithm and separated from every other packet. Its value at its own prime is zero. The associated physical test is f_T(x)=x^(-1/2)F_T(log x).

For beta in the fixed strip, tilt F_T by exp((beta-1/2)u). At this fixed prime its L^2 norm is O_p(b sqrt(W)), and its H^1 norm is O_p(b T sqrt(W)): the lower cutoff derivative contributes O(T) to the squared unamplified derivative norm, while the main carrier contributes O(T²W), which dominates because TW grows. Interpolation gives squared H^{1/2} norm O_p(b² TW).

Below abs(t)=sqrt(T), Plancherel bounds the weaker weighted squared norm by O_p(b² W sqrt(T)). Above it, the logarithmic denominator is at least a constant times log^q T, giving O_p(b² TW/log^q T). Thus N_(-q)(h_T) tends to zero as T tends to infinity with p,A,q fixed. A separate review derives the same estimate by splitting the modulated transform into its main band and controlled cutoff leakage. Constants may depend on the stage; uniformity in q is unnecessary.

At the physical prime center, the sharp Fourier inverse on the exterior line a=1+epsilon/2 is

```text
I_(T,a)(u_*)
 =b exp((a−1/2)u_*)/(2pi) · log(TW)+O_p(b).
```

Indeed its Dirichlet kernel pairs sin(Tv) with itself, giving the integral of sin²(Tv)/v between scales 1/T and W. Since TW=(log T)^A, this grows like A loglog T. The exponential tilt changes it only by a bounded error. Changing the cutoff from T to any U in [T,T+1] costs O_p(bW), because the transform is bounded by the tilted physical L^1 norm. These statements include the Fourier factor 1/(2pi).

## The exact prime atom becomes a zero-sum witness

Use the finite completed-xi contour at a good height U in [T,T+1]. Classical local zero counting and partial fractions give O(log² T) for xi′/xi on its horizontal segments. Holomorphic submean for this moderate weaker weight bounds h there by C N_(-q) log^(q/2)T/sqrt(T); the horizontal integral tends to zero. Folding by the functional equation gives the same exterior-line pair as in the positive theorem.

Expand zeta′/zeta on a>1. The target prime supplies

```text
−b log(p)/(2pi sqrt(p)) · log(TW).
```

Every other prime-power argument, and every reflected negative argument, stays a positive distance from this shrinking packet at the fixed stage. The Dirichlet-kernel bound away from its center is O_p(bW/distance). The weighted sum of these errors is finite because sum Lambda(n)n^(-a)<infinity. Thus they are negligible as W tends to zero.

The gamma/rational piece stays uniformly bounded by C_q N_(-q). There is no local-origin term since all packets vanish near zero in u. Divide the exterior physical function by iu, with a fixed smooth cutoff at the origin. The transform and its derivative remain in weighted L^2 by a polynomially weighted L^1 convolution bound. Unit-interval Sobolev gives a primitive bounded by C_q N_(-q)/sqrt(w_(-q)(t)). Both its logarithmic boundary and the integral against 1/t are controlled: log t/sqrt(w_(-q)(t)) tends to zero and integral_3^infinity dt/[t sqrt(w_(-q)(t))] is finite. Treat the two constant half-axis Stirling terms separately. This proves a uniform finite-height bound, not merely convergence after fixing a packet.

The one packet therefore has a raw spectral value tending to negative infinity along its own associated good heights as its carrier parameter grows, even while its weakened norm tends to zero. Each fixed packet still has an absolutely convergent full zero sum: it is smooth with compact log support. There is no contradiction between these two quantifiers.

## A single globally smooth test

Choose prime centers tending to infinity with disjoint small support intervals. At stage j fix q_j=1/j and A_j=q_j/2 **before** choosing T_j. Choose T_j sufficiently large that:

- The packet norm N_(-q_j) is at most 2^(-j).
- Its raw value at its new good height is below -j minus the sum of uniform absolute zero-trace bounds for all earlier fixed packets.
- Its absolute contribution at every earlier protected finite witness height is at most 2^(-j).
- Its shrinking support avoids the prime-power centers and all other packets.

All are compatible: the norm and finite-height Mellin values tend to zero, while the target logarithmic sharp inverse tends to infinity. The bounds for the finitely many past packets are finite by rapid Mellin decay and the local zero count. The future constraints concern only finitely many actual zeros, and follow from the physical L^1 bound. No uniform convergence rate for all past packets is assumed.

The locally finite sum is smooth at every interior point, including every prime center. The amplitude b_j=exp(-u_j) and W_j<1 give f(x)=O(x^(-3/2)); it vanishes near zero and one. Its prime-power samples vanish. The value envelope justifies Mellin integration on the closed strip. Triangle inequality gives finite N_(-q) for each fixed q: eventually q>=q_j and w_(-q)<=w_(-q_j), while the finite prefix has rapid transform decay. Finite height sums may be evaluated packetwise, and the future budgets make the negative witness subsequence survive in the final test.

To protect a bounded subsequence as well, after fixing packet j choose a later height V_j at which the finite prefix is close to its convergent full trace. Add V_j to the finite protected list for all future stages. The prefix arithmetic formulas are uniformly bounded by the common value envelope, zero prime samples and vanishing near one. Thus S(V_j) remains bounded after the future corrections. This strengthening is independently recorded in the skeptic and diagonal reviews.

## What this obstruction says

At every **fixed** prime-power argument the sharp Fourier inverse of this final smooth function converges correctly. Its local C^1 behavior and integrable exterior tail ensure ordinary pointwise inversion. What fails is the passage of that limit through the **infinite** weighted prime sum. The critical norm supplied uniform inversion; every strict logarithmic weakening permits this escaped-center failure. This is an explicit convergence obstruction with an absolutely defined arithmetic target, not numerical disagreement or a conclusion drawn from failure of Cauchy–Schwarz alone.

The underlying mechanism is an atomic trace obstruction. A bounded primary-source comparison relates finite-atom versions to classical Fourier summability and uniform boundedness, while distinguishing the noncompact smooth escaped-center construction from compact continuous fixed-point examples. The statement is not evidence of a problem in a source imposing derivative decay or a different valid test space. Nor does it alter the valid compact jump tests of the original arithmetic criterion.

The next useful task is to determine whether other trace formulas with infinitely many atomic arithmetic inputs admit the same sharp interface, with their exact contour bounds checked separately. For numerical positivity work, use the critical or stronger norm and its own approximation estimates; a weaker finite sampled norm cannot certify the exchange of limits established here to fail. No claim about a solution of RH, a new zero-free theorem, or publication priority follows.
