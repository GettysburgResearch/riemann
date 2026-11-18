# Uniform Voronoi kernel summation and a larger inverse-prime region

18 November 2026. For the remaining smooth signed twist with coefficient \(d_2*(\Lambda\log^2)\), the contribution from coprime prime factors can be removed on an explicit two-dimensional region larger than the narrow band from prime107. Summing a common Bessel envelope absorbs the entire dual length. Grouping by the gcd of the dual index and the modulus handles nonunit dual indices. [Fixed sequence](prime98_fixed_arithmetic_sequence.md) · [Earlier inverse-prime estimate](prime107_inverse_prime_voronoi.md)

## Statement

Let \(K\asymp T^\theta\) be a dyadic modulus scale with \(1/2<\theta<2/3\), and \(P\asymp T^\xi\) a dyadic prime scale. Let \(a_k\) be the coefficients of the fourth power of the band polynomial, so that \(|a_k|\le24\), and let \(H=T^\kappa\) with \(\kappa<1\) chosen sufficiently close to 1. The compact smooth time cutoff is supported at heights comparable to \(T\), with \(\|w_T^{(j)}\|_\infty\ll_j H^{-j}\). On either of the following **strict** regions the dyadic contribution of the prime factors \(p\in(P,2P]\), \((p,k)=1\), is \(O(T^{1-c})\) for some \(c>0\):
\[
\begin{array}{ll}
\text{Baker region:}&
 \theta/2<\xi<\theta,\quad
 \tfrac{11}{10}\theta+\tfrac45\xi<1,\quad
 \theta+\tfrac{11}{12}\xi<1;\\[2pt]
\text{Fouvry--Shparlinski region:}&
 0<\xi<\tfrac32\theta,\quad
 \tfrac{13}{10}\theta+\tfrac35\xi<1,\quad
 \tfrac{13}{12}\theta+\tfrac56\xi<1.
\end{array}
\]
Constants are uniform on compact subsets of the indicated region if the transition exponent is chosen for that subset. Common sliced intervals within a prime block are allowed. There is no condition on the size of the smallest prime factor of \(k\) in this argument. For instance, the Baker region reaches \(\xi<0.425\) at \(\theta=0.60\), above the earlier \(T/K\) threshold \(\xi=0.40\). At \(\theta=0.51\), the Fouvry–Shparlinski region reaches \(\xi<0.537\) and includes \(P>K\). The remaining much longer prime scales and the square-prime phase are outside this conclusion.

## A common dual envelope

Apply the ordinary divisor Voronoi transform at modulus \(k\) after freezing the coprime prime \(p\), as in prime107. Put \(U=KP/T\), \(\delta=H/T\), and \(M=kT/p\). After \(x=Mu\), the weight on each dual index \(l\) for either Bessel kernel is
\[
 B_{k,l}(p)=\frac{M}{k^2}\int w_T(2\pi Tu)
                 J^\pm(\sqrt{lMu}/k)\,du ,
 \qquad J^-(z)=-2\pi Y_0(4\pi z),\quad J^+(z)=4K_0(4\pi z).
\]
This includes both the outer \(1/k\) and the \(1/k\) from Voronoi. The \(u\)-support is fixed and separated from zero. The prime derivative acts on \(M\) and the Bessel argument, since \(p\,dM/dp=-M\) and \(w_T(2\pi T u)\) is independent of \(p\). In particular the derivative has the same fixed-support integral structure with \(J^\pm\) replaced by a fixed linear combination of \(J^\pm(z)\) and \(z(J^\pm)'(z)\).

For each fixed \(A>3\) and \(r=(l/U)^{1/2}\), the following common envelope holds throughout the dyadic block:
\[
 |B_{k,l}(p)|+P|\partial_p B_{k,l}(p)|
 \ll_A U^{-1}(1+|\log r|+r^{1/2})(1+\delta r)^{-A}.
\]
For \(r\le1\) this follows from the small-argument Bessel series. For \(r\ge1\), the \(K_0\) term and its derivative decay exponentially. For the \(Y_0\) term and its derivative, write the large-argument form as two phases \(e^{\pm 4\pi i\sqrt{lM}\sqrt u/k}\) with symbol amplitudes bounded with all fixed \(u\)-derivatives by \(O(r^{1/2})\). This uses the derivative asymptotics on the positive axis. At fixed support each integration by parts in \(u\) gains \(r^{-1}\) and costs at most \(\delta^{-1}\), with no boundary terms. Combine the resulting estimates with the zeroth integration bound. [Arbitrary-modulus divisor Voronoi, Blomer–Harcos–Michel (2.25)–(2.27)](../../sources/prime107_references/blomer_harcos_michel2007_annales.pdf) · [Bessel derivative asymptotics](https://dlmf.nist.gov/10.17) · [Modified Bessel asymptotics](https://dlmf.nist.gov/10.40)

The sum of the displayed envelopes over \(l\ge1\) is \(O_A(\delta^{-5/2})\), independently of \(U\). To check this also for \(U<1\), compare the summand at \(v=l/U\) with its integral on \([l/U,(l+1)/U]\). The positive function \((1+|\log \sqrt v|+v^{1/4})(1+\delta\sqrt v)^{-A}\) is comparable up to constants depending only on \(A\) at arguments with ratio in \([1,2]\). The sum is therefore bounded by its integral on \((0,\infty)\). Substitute \(v=r^2\). The logarithmic singularity at zero is integrable, and the large-\(r\) integral is \(O(\delta^{-5/2})\). The comparison holds even if the first dual index lies beyond the natural cutoff. In particular the normalization \(U^{-1}\) cancels the density of dual indices.

The arithmetic factor \(d_2(l)\tau(l)\) can be included at cost \(T^\varepsilon\). On a polynomial range \(l\le T^C\) this follows from the divisor bound. Beyond it choose \(C\) larger than a fixed upper exponent for \(U\) plus, say, 4. The \(l^{-A/2}\) gain in the envelope then controls the tail with arbitrary power savings even after absolute summation over \(k,p,l\), by increasing \(A\). Taking \(\kappa\) sufficiently close to 1 makes \(\delta^{-5/2}\) a prescribed small power of \(T\).

## The dual gcd and the two available prime bounds

For every \(k,l\), let \(d=(k,l)\), \(q=k/d\). The phases after transforming the divisor sum are \(e(\pm(l/d)\bar p/q)\). The transformed unit average is exactly the average at modulus \(q\), by surjectivity from the units modulo \(k\). Since \(l/d\) is a unit modulo \(q\), the average is \(\mu(q)/\varphi(q)\) for each sign, and \(q=1\) cancels exactly. For each fixed divisor \(d\mid l\), the moduli \(k=dq\) project one-to-one to a subset of the block \(Q'<q\le2Q'\) with \(Q'=K/d\). The residue \(l/d\) remains fixed for that divisor, and a maximum over units is available from the source estimates. The extra restriction \((p,k)=1\), compared with \((p,q)=1\), excludes at most \(O(\log T)\) primes per \(k\), or at most four on the actual support. After summing over \(q\) this costs \(O(T^\varepsilon Q')\) per \(d\), within the bounds below. The Ramanujan term has sum \(O(T^\varepsilon P)\) per \(d\) over \(q\), using \(1/\varphi(q)\ll T^\varepsilon/q\).

Baker, Theorem 2, bounds the sum over \(q\sim Q'\) of the maximal unit-numerator inverse-prime dyadic sum by
\[
 \ll_\varepsilon (Q'^{11/10}x^{4/5}+Q'x^{11/12})Q'^\varepsilon,
 \qquad Q'^{1/2}\le x\le2Q'.
\]
Fouvry and Shparlinski, Theorem 3.3, bounds the same sum by
\[
 \ll_\varepsilon (Q'^{13/10}x^{3/5}+Q'^{13/12}x^{5/6})Q'^\varepsilon,
 \qquad 1\le x\le Q'^{3/2}.
\]
Both articles define the prime sum over \(x<p\le2x\). Bounds for each common partial summation endpoint \(t\in[P,2P]\) follow by dyadically decomposing the prefix. For Baker, stop at \(x<Q'^{1/2}\) and use the trivial \(O(Q'^{3/2})\) bottom bound, which is absorbed when \(P\ge Q'^{1/2}\). For Fouvry–Shparlinski, all smaller dyadic scales satisfy its upper condition provided \(P\le Q'^{3/2}\). In either case the power sums form geometric series. Use Abel summation with the common envelope for \(B_{k,l}\) and its prime derivative, also including the fixed \((\log p)^3\) coefficient. At each common endpoint the corresponding average bound applies even though the individual weights depend on the modulus. This avoids exchanging the sum over moduli with distinct suprema over prime endpoints. [Baker, journal pp. 351–352](../../sources/prime107_references/baker2012_acta.pdf) · [Fouvry–Shparlinski, journal p. 296 definition of \(S_q\) and Theorem 3.3 p. 301](../../sources/prime113_references/fouvry_shparlinski2011.pdf) · [Journal DOI](https://doi.org/10.4064/aa150-3-5)

## Budgets and conclusion

In the Baker region, when \(Q'\ge P\), Baker gives the stated budget with \(Q'\) replaced by \(K\), since \(P>K^{1/2}\). When \(P^{2/3}\le Q'<P\), use Fouvry–Shparlinski. Its two terms are bounded by \(P^{19/10}\) and \(P^{23/12}\). When \(Q'<P^{2/3}\), the triangle bound costs \(O(Q'P)\ll P^{5/3}\). Since \(\xi<\theta\) and \(\theta+11\xi/12<1\), one has \(23\xi/12<1\), so the fallback \(P^{23/12}\) saves a power as well. For all \(d\) the total budget, after the common envelope and summing divisors \(d\mid l\), is thus
\[
 T^\varepsilon \bigl(K^{11/10}P^{4/5}+ KP^{11/12}+P^{23/12}+K+P\bigr)
\]
with an arbitrarily small fixed \(\varepsilon\) obtained by choosing \(\kappa\) sufficiently close to 1 as above. Every displayed term, after taking \(\varepsilon\) small, is \(O(T^{1-c})\).

In the Fouvry–Shparlinski region, apply that theorem whenever \(Q'\ge P^{2/3}\), using \(K\) in its outer powers. The smaller-\(Q'\) triangle budget is again \(P^{5/3}\). The hypothesis \(13\theta/10+3\xi/5<1\) with \(\theta>1/2\) implies \(\xi<7/12\), so \(5\xi/3<1\). The budget
\[
 T^\varepsilon \bigl(K^{13/10}P^{3/5}+K^{13/12}P^{5/6}+P^{5/3}+K+P\bigr)
\]
has the same power saving. Neither proof discards a Gauss phase or drops a gcd stratum. The remaining estimate at larger \(P\) still requires further arithmetic cancellation.
