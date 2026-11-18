# The balanced Newton energy through the $2^{32}-1$ prefix

**Proposed finite certificate.** At $Y=65535$, $B=(Y+1)^2-1=4294967295$, the native BNR26 energy satisfies

$$
 1.9078<A_B<1.9079,\qquad (1+A_B)^2<4(1+A_Y)^3 .
$$

Both sides of the proposed fractional-power inequality are positive. The squared comparison verifies that transition of the proposal. All four earlier transitions from the seed $1$ also satisfy it in the same replay. No subsequent transition is covered. The arithmetic here directly enumerates the actual output coefficients from the prime definition of Möbius; the input-to-output Newton identity is the separately proved ring identity in [BNR26 §2](https://github.com/GettysburgResearch/riemann/blob/a1b4625f9775df1fdbd431b5198309a2fce9b038/standalone/2026-09-10-astra-balanced-newton/PROOF.md).

For each $N$ we use $M(k)=\sum_{n\le k}\mu(n)$, $E_N=\sum_{k\le N}M(k)^2/[k(k+1)]$, $u_N=\sum_{k\le N}M(k)/[k(k+1)]$, and $A_N=E_N+2(N+1)u_N^2$. Every integer through $B$ appears exactly once in each producer pass. In particular $M(B)=1814$ and $\max_{k\le B}|M(k)|=25071$. The source stream encodes $\mu(n)+1$ as one byte in increasing integer order, starting at $n=1$. Both prime implementations give SHA-256

~~~text
49e503982415992cb8a2ec63f64f00be9fb18927c21de74f1cc8da07b26d9cc6
~~~

**Primitive arithmetic.** The [C++ producer](newton_prefix_nov18.cpp) has two modes. One generates the base primes by Eratosthenes, multiplies each segment's distinct small prime factors, and crosses out prime squares explicitly; a product less than the original integer in a squarefree row detects its sole remaining prime factor. The other generates base primes by trial division, divides each multiple once, and tests the remainder for another factor of that prime. In both modes all primes through the square root of the segment's right endpoint have been processed. The two complete runs use different segment boundaries and different partitions for interval summation. They share the energy-bound implementation and the prime-factorization theorem.

On each group $l\le k\le r$ the producer sums $M(k)^2$, $M(k)_+$ and $M(k)_-$ separately in integer arithmetic. For each nonnegative sum $S$, divide $2^{64}S$ by $r(r+1)$ rounded down and by $l(l+1)$ rounded up. Subtract interval endpoints in reverse order for the negative first-moment contribution. Each denominator fits in 64 unsigned bits through the specified endpoint. A guard checks that each grouped numerator fits before shifting it into the unsigned 128-bit dividend. Accumulated bounds fit in signed 128 bits: $|M(k)|\le k$, $r/l\le2$, and the lower denominator overestimates each true weight by at most a fixed factor four. Therefore the scaled square sum is at most $2^{64}\cdot4B$ plus at most one rounding unit per group; the absolute scaled mean is bounded the same way. The [recorded intervals](newton-prefix-results-nov18.json) are integers over the common dyadic denominator $2^{64}$.

**Independent checks and replay.** The [Python checker](check_newton_prefix_nov18.py) recomputes all six endpoint Mertens values via $\sum_{k\le n}M(\lfloor n/k\rfloor)=1$, using a linear sieve only through $2^{20}$. It independently verifies the number of squarefree inputs by $\sum_{d\le\sqrt n}\mu(d)\lfloor n/d^2\rfloor$. It rehashes every small prefix via this separate sieve and accumulates independent 96-bit enclosures through 65535. For the full prefix it requires equal stream hashes and overlapping interval outputs from the two segmented runs. The rational comparisons use Python integers and exact fractions. It recomputes the entire primitive stream in both modes when invoked as follows from this directory:

~~~sh
python check_newton_prefix_nov18.py --replay
~~~

Without the flag it checks the saved passes, the independent endpoint identities and the exact inequalities. The recorded runs used GCC 14.2.0 and OpenSSL 3.5.7. SHA-256 is used for source comparison, while the interval bounds use integer arithmetic. None of these finite checks supplies the required all-stage recurrence.
