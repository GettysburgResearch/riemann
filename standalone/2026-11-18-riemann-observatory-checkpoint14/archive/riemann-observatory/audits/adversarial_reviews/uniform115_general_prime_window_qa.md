# Independent QA of the general inverse-prime window

18 November 2026. The gcd grouping does remove the minimum-prime restriction in the earlier unit-only argument. Both stated regions and all fallback exponents hold. This is a power-saving estimate for part of the compact-local prime stratum of the signed smooth sum. It gives no estimate for the remaining prime scales or the full fourth moment. [Prime113 proof](prime113_uniform_voronoi_envelope.md) · [Earlier independent kernel bound](uniform113_bessel_kernel_mass_review.md)

## Primary inverse-prime estimates and common endpoints

I checked the pinned Fouvry–Shparlinski PDF and text hashes and read the primary passages. The paper defines \(q\sim Q\) as \(Q<q\le2Q\). Section 3.1, p. 296, defines the prime sum on \(x<p\le2x\), \((p,q)=1\), with the inverse phase and general integer modulus. Theorem 3.3, p. 301, bounds its outside modulus sum of the maxima over unit numerators by
\[
 Q^\varepsilon(Q^{13/10}x^{3/5}+Q^{13/12}x^{5/6})
 \qquad (1\le x\le Q^{3/2}).
\]
The sum's definition says \(x\ge2\) while the theorem prints 1 as the lower endpoint. The finitely many primes at bounded bottom scales can be estimated trivially, so that wording poses no problem for the conversion. Baker's primary pp. 351–352 give the corresponding annular bound \(Q^\varepsilon(Q^{11/10}x^{4/5}+Qx^{11/12})\) for \(\sqrt Q\le x\le2Q\). Neither source puts a freely varying prime endpoint inside the modulus sum. [Fouvry–Shparlinski primary PDF](https://www.impan.pl/shop/publication/transaction/download/product/82801) · [Baker primary PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82065)

At each fixed \(t\in[P,2P]\), a prime prefix decomposes into annuli with initial base \(t/2\le P\) and decreasing bases. Thus for Fouvry–Shparlinski all relevant bases are within its upper bound if \(P\le Q^{3/2}\). For Baker one requires \(\sqrt Q\le P\le2Q\), with scales below \(\sqrt Q\) estimated at cost \(O(Q^{3/2})\), absorbed by \(Q^{11/10}P^{4/5}\). The dyadic annular terms sum geometrically. Subtraction of a fixed lower prefix thus gives the source bounds at each common endpoint of the partial summation integral. A common slice works by the same calculation.

## Gcd grouping and its weights

For one fixed dual index \(l\), partition the original moduli by \(d=(k,l)\). In each class write \(q=k/d\). The map \(k\mapsto q\) is one-to-one into \(K/d<q\le2K/d\), and \(l/d\) is a unit modulo \(q\). The reduction of \(\bar p\) modulo \(k\) is exactly the inverse modulo \(q\). Reduction of unit groups is onto with equal fibers, so the normalized Ramanujan subtraction is \(\mu(q)/\varphi(q)\), and \(q=1\) cancels exactly. In applying either source we can extend the subset of \(q\)'s to the whole dyadic block because the maximal sums are nonnegative. The original requirement \((p,k)=1\) demands deleting only primes dividing \(d\) that were not already excluded by \((p,q)=1\). Their number is \(O(\log T)\) per modulus even for a general integer \(k\). Their cumulative error is \(O(T^\varepsilon K/d)\) for each divisor group. The separate Ramanujan term is bounded by \(O(T^\varepsilon P)\) per group using \(1/\varphi(q)\ll T^\varepsilon/q\). Groups with \(K/d<1\) contain no \(q\ge2\).

The smooth transformed weight still depends on the original \(k=dq\), but its value and scaled derivative have a common pointwise envelope on the original block. Abel summation is applied on a common interval. At each integration endpoint the sum of modulus-dependent weighted terms is therefore at most the common derivative envelope times the *sum* of fixed-endpoint absolute prime sums. This remains true on any gcd subset. A uniform total variation bound considered one modulus at a time would not by itself imply this outside-average statement. The proof's common derivative majorant is the relevant stronger bound. The factor \(|a_k|\le24\) enters only in this majorization. Thus no size assumption on the smallest prime factor of \(k\) is used.

The sum over at most \(\tau(l)\) gcd groups meets exactly the weight \(d_2(l)\tau(l)\) in the dual envelope. The Prime113 summation with a polynomial cutoff as a proof device and a rapidly decaying far tail is valid. It can alternatively be done without a cutoff by observing \(d_2(l)\tau(l)=\tau(l)^2\le d_4(l)\). At a prime power this is \((e+1)^2\le\binom{e+3}{3}\), and the inequality follows for every \(l\) by multiplicativity. The elementary harmonic divisor count gives \(\sum_{l\le X}d_4(l)\ll X\log^3(2X)\). Shell summation with the weighted envelope then adds only fixed log powers, including when \(U\Delta^{-2}<1\). No fixed all-unit truncation or independent small-prime restriction is necessary. The \(\Delta^{-5/2}\) bound in Prime113 follows from using the derivative kernel at face value. The separate \(\Delta^{-3/2}\) improvement uses the two-transition derivative-support condition explained in Uniform113. Either fixed power can be absorbed by choosing \(\kappa\) close enough to one *after* fixing the exponent gaps.

## Fallback table

Let \(Q'=K/d\). In the Baker region \(P>\sqrt K\) by a fixed power margin, so whenever \(Q'\ge P\), Baker applies without a lower-endpoint issue. The complete partition is
\[
\begin{array}{c|c|c}
\text{reduced block} & \text{input} & \text{budget before }T^\varepsilon\text{ losses}\hline
Q'\ge P & \text{Baker} & K^{11/10}P^{4/5}+KP^{11/12}\\
P^{2/3}\le Q'<P & \text{Fouvry--Shparlinski} & P^{19/10}+P^{23/12}\\
Q'<P^{2/3} & \text{absolute count} & P^{5/3}
\end{array}
\]
The middle row uses \(P\le(Q')^{3/2}\) before replacing the two powers of \(Q'\) by powers of \(P\). The exponent \(23/12\) is \(13/12+5/6\), dominates \(19/10\) and \(5/3\), and satisfies \((23/12)\xi<\theta+(11/12)\xi<1\) since \(\xi<\theta\). Thus the fallbacks do not introduce a new restriction in the stated region.

In the Fouvry–Shparlinski region apply its theorem for \(Q'\ge P^{2/3}\) and bound the remainder by \(Q'P\le P^{5/3}\). The first source cost inequality with \(\theta>1/2\) gives \(\xi<7/12\), hence \((5/3)\xi<35/36<1\). The \(K+P\) errors from exclusions and centering also save a power. This leaves no uncovered reduced-modulus range. The example cutoffs at \(\theta=0.60\) and \(0.51\) are respectively \(0.425\) for Baker and \(0.537\) for Fouvry–Shparlinski, as stated.

**Disposition.** The common-endpoint and gcd arguments are valid, and the two strict regions remain valid with uniform constants on compact subsets when the taper exponent is chosen for the subset. The estimates are for inverse primes. They provide no transfer to inverse squares or to the longer prime ranges left open. No canonical file was changed.
