# Prime161 — A common nonnegative sequence with a large moving-phase projection

This is a counterexample to an implication from progression norm bounds and common-sequence compatibility alone. It concerns a constructed sequence on all integers in one interval. It gives no estimate for the primes.

## Statement

Fix \(1/2<\theta<2/3\), \(K\asymp T^\theta\) and an integer \(P\asymp KT\). There is a set \(\mathcal S\subset[K,2K)\) of odd squarefree four-prime products with \(|\mathcal S|\asymp K/\log^4 K\) and every prime factor \(\gg K^{1/4}\). It suffices to take four distinct primes from \([X,(1+\eta)X]\) with \(K=X^4\), \(X=T^{\theta/4}\), and a fixed small \(\eta>0\) satisfying \((1+\eta)^4<2\). The prime number theorem counts these products. If an upper band cutoff meets the shell at its top, take primes in \([(1-\eta)X,X]\) and start the dyadic modulus shell at \((1-\eta)^4X^4\) instead. The statement works for the corresponding weights \(c_k=24\) of the fourth prime-polynomial power on this selected squarefree subfamily. It also works for any weights \(0<c_-\le c_k\le c_+\) there.

There exists \(b(n)\ge0\), supported on \(J=[P,2P)\cap\mathbb Z\), with \(\sum_n b(n)=P\). For \(1\le k\le2K\) write \(B_{k,u}=\sum_{n\equiv u\bmod k}b(n)\). Then
\[
 \sum_{k\le2K}\sum_{u\bmod k}|B_{k,u}-P/k|^2\ll PK,\qquad
 \sum_{k\le2K}\max_{u\bmod k}|B_{k,u}-P/k|\ll K\sqrt P .
\]
In particular the latter is \(O_B(P/\log^B T)\) for each fixed \(B\), since \(K/\sqrt P\asymp T^{(\theta-1)/2}\). Let \(\overline B_k^\times=\varphi(k)^{-1}\sum_{(u,k)=1}B_{k,u}\) denote the unit-row mean. Both bounds also hold on units with this mean: subtracting the unit mean decreases the quadratic error, and at most doubles the maximum error relative to the all-residue mean.

Yet, using the exact unit-centered moving phase,
\[
 \left|\sum_{k\in\mathcal S}\frac{c_k}{k}
 \sum_{\substack{n\in J\\(n,k)=1}} b(n)
 \left(\cos(2\pi n/k)-\frac{\mu(k)}{\varphi(k)}\right)\right|
 \gg \sqrt{P|\mathcal S|}
 \asymp \frac{K\sqrt T}{\log^2 T}.
\]
This exceeds \(T\log^4 T\) by a factor tending to infinity. The progression rows of \(b\) automatically have identical common-divisor marginals, because all rows are induced by one sequence. The unit-centered complex phase gives the same real-part test.

## Proof

Define the real periodic test
\[
 h_k(n)=\mathbf 1_{(n,k)=1}
 \left(\cos(2\pi n/k)-\frac{\mu(k)}{\varphi(k)}\right),
 \qquad H(n)=\sum_{k\in\mathcal S}\frac{Kc_k}{k}h_k(n).
\]
Every \(h_k\) has mean zero over its period by the Ramanujan sum identity. Let \(L=\lfloor K/100\rfloor\) and let \(\psi\) be the symmetric uniform averaging kernel on the integers \([-L,L]\). Its Fourier multiplier, with \(e(x)=e^{2\pi ix}\), satisfies for reduced \(a/q\ne0\)
\[
 |\widehat\psi(a/q)|
 \le \min\!\left(1,\frac{1}{(2L+1)|\sin(\pi a/q)|}\right)
 \ll \min(1,q/K).
\]
At \(a/q=1/k,\ k\in\mathcal S\), each cosine contributing to this symmetric multiplier is uniformly positive and the multiplier is \(\gg1\).

Use \(I=[P+L,2P-L)\cap\mathbb Z\) and \(M=\|(\psi*H)\mathbf1_I\|_{\ell^2}\). We need only a lower bound for \(M\). All frequencies of \(\psi*H\) are rational with reduced denominator at most \(2K\). Its coefficient at \(1/k\) is attributable only to \(h_k\), since a modulus \(k'\in[K,2K)\) divisible by \(k\) must equal \(k\). Before multiplication by \(Kc_k/k\) and \(\widehat\psi(1/k)\) this coefficient is
\[
 \frac{\varphi(k)+c_k^{\rm Ram}(2)}{2k}-
 \frac{\mu(k)c_k^{\rm Ram}(1)}{k\varphi(k)}
 \gg 1,
\]
where \(c_k^{\rm Ram}\) is the Ramanujan sum, distinct from the polynomial weight. Indeed \(c_k^{\rm Ram}(1)=c_k^{\rm Ram}(2)=\mu(k)\) for these odd \(k\), and \(\varphi(k)/k\to1\) uniformly. The squared Fourier coefficient sum is thus \(\gg|\mathcal S|\).

For completeness a direct interval Gram-matrix estimate supplies the lower bound and the additive upper estimate used below. Distinct rational frequencies with denominators at most \(2K\) are circularly separated by at least \(1/(4K^2)\). In any row of the Gram matrix obtained by summing the exponentials over an interval of \(N\) integers, the off-diagonal entries are bounded by \(1/(2\|\alpha-\beta\|)\). Ordering the distances around the circle gives absolute off-diagonal row sum \(O(K^2\log(2K))\). The associated quadratic form differs from \(N\) times the squared coefficient norm by at most that row bound times the squared norm. This proves both lower and upper bounds, and the adjoint upper bound for finite vectors supported on the interval. Here \(P\gg K^2\log(2K)\), so \(M\gg\sqrt{P|\mathcal S|}\).

Put \(F=(\psi*H)\mathbf1_I\), \(F^+=\max(F,0)\), \(F^-=\max(-F,0)\), and \(\lambda=K/M\). Define
\[
 a^\pm=\lambda(F^\pm-\langle F^\pm\rangle_I\mathbf1_I),
 \qquad b^\pm=\mathbf1_J+\psi*a^\pm ,
 \qquad
 \langle f\rangle_I=|I|^{-1}\sum_{n\in I} f(n).
\]
Both \(a^\pm\) are mean zero and supported on \(I\). Removing the mean is an orthogonal projection, so \(\|a^\pm\|_2\le K\). Each \(a^\pm(n)\ge-K/\sqrt{|I|}\) by Cauchy–Schwarz. Thus \(b^\pm\ge0\) since \(K/\sqrt{|I|}=o(1)\), convolution is positive, and \(I+[-L,L]\subset J\). The mass of each \(b^\pm\) is exactly \(P\).

Here is the variance calculation with all divisibilities accounted for. For a mean-zero \(g=\psi*a^\pm\), finite Fourier orthogonality on \(\mathbb Z/k\mathbb Z\) gives
\[
 \sum_{u\bmod k}\left|\sum_{n\equiv u\bmod k}g(n)\right|^2
 =\frac1k\sum_{r=1}^{k-1}|\widehat g(r/k)|^2.
\]
In the sum over \(k\le2K\) the weight at a reduced \(a/q\) is \(\sum_{k\le2K:q\mid k}1/k\ll q^{-1}\log(e\,2K/q)\). After inserting \(|\widehat\psi(a/q)|^2\), the weight is \(O(1/K)\) uniformly for every \(2\le q\le2K\): for \(q\le K\) use boundedness of \((q/K)\log(e\,2K/q)\), and for larger \(q\) the conclusion is immediate. The adjoint Gram bound on \(a^\pm\) then gives cumulative variance \(\ll(P/K)\|a^\pm\|_2^2\ll PK\). For \(\mathbf1_J\), each residue error relative to \(P/k\) is \(<1\), giving variance \(O(K^2)\). Combine the two parts via the square triangle bound. Cauchy–Schwarz over \(O(K)\) moduli proves the maximum estimate. For the unit-mean variant apply the least-squares minimizing property of that mean and its maximum-error bound row by row.

Finally, by symmetry of \(\psi\) and \(F^+-F^-=F\),
\[
 \sum_n H(n)(b^+(n)-b^-(n))
 = \lambda \left(M^2-|I|\,\langle F\rangle_I^2\right).
\]
The sum of \(\psi*H\) over \(I\) is \(O(K|\mathcal S|)\). Each \(\psi*h_k\) is bounded uniformly and mean-zero periodic with period \(k\), so only the last incomplete period can contribute. Consequently
\[
 \frac{|I|\,\langle F\rangle_I^2}{M^2}
 \ll \frac{K^2|\mathcal S|}{P^2}=o(1).
\]
Thus at least one \(b^\pm\) has absolute projection against \(H\) at least a fixed multiple of \(KM\). Divide by \(K\) to obtain the claimed moving-phase lower bound.

## Scope

The all-residue variance in this example is deliberately stronger than the corresponding variance on units centered by the induced unit mean. The sequence need not put mass only on units, prime powers, primes, or numbers with a prescribed sieve profile. Its reference mass on a unit residue is the row's unit mean, approximately the natural uniform-integer value, rather than the prime-model baseline \(P/\varphi(k)\) for a measure supported entirely on units. Accordingly, this establishes a common-sequence obstruction for precisely the centered norm budgets displayed above. Additional arithmetic support or local density conditions on the true prime sequence remain available to an actual prime estimate. The projection here uses one interval and a selected four-prime subfamily with bounded positive weights. It makes no claim for an unsigned norm with arbitrary interval dependence, or for the full smooth \(C_*\) sum. The key distinction from a direct additive large-sieve argument is the short positive convolution, which suppresses the low-denominator imprimitive multiplicities while preserving the moving frequencies.

## Extension to the full fourth-power coefficient support

Let \(\mathcal P=[X,(1+\eta)X]\cap\{\text{primes}\}\) with \(0<\eta<2^{1/4}-1\), \(X\asymp T^{\theta/4}\), and \(K=X^4\). Define \(D_{\mathcal P}(s)=\sum_{p\in\mathcal P}p^{-s}\) and write \(D_{\mathcal P}(s)^4=\sum_k a_k k^{-s}\). Then the construction and both progression bounds above hold with the projection summed over **all** \(k\) for which \(a_k>0\), using \(c_k=a_k\).

Indeed, if \(k=\prod_{p\in\mathcal P}p^{m_p}\) with \(\sum_p m_p=4\), then \(a_k=4!/\prod_p m_p!\) and \(1\le a_k\le24\). The entire support lies in \([K,2K)\). For \(N=|\mathcal P|\), its cardinality is \(\binom{N+3}{4}\), by unique factorization and multisets of four primes. The prime number theorem gives \(N\asymp X/\log X\), hence the full support has size \(\asymp K/\log^4 K\). For large \(X\) all \(k\) are odd, and \(\varphi(k)/k=\prod_{p\mid k}(1-1/p)\ge(1-1/X)^4\). Since \(1\) and \(2\) are each coprime to \(k\), both Ramanujan sums at those arguments equal \(\mu(k)\), including the value zero for nonsquarefree \(k\). The Fourier coefficient of \(h_k\) at \(1/k\) is therefore
\[
 \frac{\varphi(k)+\mu(k)}{2k}-\frac{\mu(k)^2}{k\varphi(k)}
 =\frac12+O(X^{-1}),
\]
uniformly on the full support. The dyadic-shell argument still separates \(1/k\) from frequencies of all other supported moduli. Periodicity, unit centering, and the uniform bounds on weights and kernels are the only remaining support properties used in the proof. Applying the construction with this full support proves the same lower bound \(\gg K\sqrt T/\log^2 T\).

The progression bounds here continue to use \(P/k\) for all residues and the induced mean for unit rows. The construction imposes neither prime or rough support, a baseline \(P/\varphi(k)\), nor a pointwise von Mangoldt bound. It concerns the full fourth-power coefficients of the specified short prime band, whose support fits into one dyadic modulus shell.
