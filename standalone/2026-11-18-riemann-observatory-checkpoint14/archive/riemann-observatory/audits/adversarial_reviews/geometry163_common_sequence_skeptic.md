# Independent check of the common-sequence phase obstruction

2026-11-18. The real nonnegative sequence in prime161 satisfies the two stated whole-interval progression bounds and has the stated large **absolute** moving-phase projection. The construction does supply genuine compatibility of the full progression rows from a single sequence. It does not supply a unit-supported prime-model sequence or a substitute for the prime estimate. An elementary rounding step below also gives integer-valued weights if desired. This last strengthening is separate from the original proof. [Construction](prime161_common_sequence_phase_campaign.md)

## Window, Ramanujan centering and the norm lower bound

Take \(\theta\in(1/2,2/3)\) fixed, \(K\asymp T^\theta\), \(P\asymp KT\) an integer. For a fixed small \(\eta>0\), choose primes in \([K^{1/4},(1+\eta)K^{1/4}]\), where \((1+\eta)^4<2\). The \(\binom{\#p}{4}\) distinct squarefree products belong to \([K,2K)\) by unique factorization, with each prime factor comparable to \(K^{1/4}\). The prime number theorem for a proportional interval yields \(S=|\mathcal S|\asymp K/\log^4 K\). A band ceiling requires a correspondingly positioned shell with an available proportional prime subinterval. The lower bound concerns the selected shell family, including the coefficient 24 on the squarefree four-prime products; it does not claim survival after unrestricted additional terms are appended.

Define \(h_k(n)=\mathbf1_{(n,k)=1}(\cos(2\pi n/k)-\mu(k)/\varphi(k))\), and let \(H=\sum_{\mathcal S}(Kc_k/k)h_k\), with bounded strictly positive \(c_k\). The average of \(h_k\) over a full residue system is zero exactly. The coefficient of \(e(n/k)\) is
\[
k^{-1}\left(\tfrac12(\varphi(k)+c_k^{\rm Ram}(2))
    -\mu(k)c_k^{\rm Ram}(1)/\varphi(k)\right).
\]
For odd squarefree \(k\) here, both Ramanujan sums equal \(\mu(k)=1\). Since all four prime factors tend uniformly to infinity, \(\varphi(k)/k=1+O(K^{-1/4})\). The coefficient is uniformly positive for large \(K\). No different \(k'\in[K,2K)\) can contribute to this reduced frequency: it would require \(k\mid k'\). The exact induced unit mean can be subtracted inside every tested row because \(h_k\) has zero sum on the units. The real part of the centered complex moving mode is this same test.

For \(L=\lfloor K/100\rfloor\), convolution by the symmetric probability kernel on \([-L,L]\) preserves the coefficients at \(1/k\) up to uniformly positive factors, because all averaging angles there have modulus at most \(2\pi/100\). At a nonzero reduced frequency \(a/q\), it has multiplier at most \(C\min(1,q/K)\) from the geometric sum and \(|\sin(\pi a/q)|\ge 2/q\). Frequency differences are circularly separated by \(1/(4K^2)\). Grouping distances in shells of that width bounds each off-diagonal Gram row by \(O(K^2\log(2K))\), using the finite interval geometric sum and both directions around the circle. The same row bound controls the Hermitian quadratic error, hence both the lower synthesis bound and the upper adjoint bound. With \(I=[P+L,2P-L)\cap\mathbb Z\), \(F=(\psi*H)\mathbf1_I\) and \(M=\|F\|_2\), this gives \(M^2\gg PS\) because \(|I|\asymp P\gg K^2\log(2K)\). The comparison uses \(T/K\to\infty\); the stricter lower condition on \(\theta\) comes from the final projection threshold.

## Positivity, norms and compatibility

Center each part \(F^\pm\) on \(I\), scale by \(K/M\), and call the resulting input \(a^\pm\). Orthogonal projection gives \(\|a^\pm\|_2\le K\), and the nonnegative originals make \(a^\pm\ge-K/\sqrt{|I|}\). The convolution \(g^\pm=\psi*a^\pm\) has zero sum, is supported in \(J=[P,2P)\cap\mathbb Z\), and has the same lower bound because the kernel is nonnegative and sums to one. In particular the uniform baseline \(b^\pm=\mathbf1_J+g^\pm\) is nonnegative for large \(T\) since \(K/\sqrt P\to0\). Both sequences have exactly mass \(P\). With integer \(P,L\), the rightmost point of \(I+[-L,L]\) is \(2P-1\), so no mass leaks at the upper endpoint.

Finite Fourier orthogonality expresses the full residue variance of \(g^\pm\) as \(k^{-1}\sum_{r=1}^{k-1}|\widehat g^\pm(r/k)|^2\); the zero-frequency term vanishes for every \(k\). At any reduced \(a/q\), the total weight from all moduli \(k\le2K\) is
\[
\sum_{m\le2K/q}\frac{1}{mq}\le q^{-1}(1+\log(2K/q)).
\]
After the squared multiplier it is \(O(1/K)\), uniformly: for \(q\le K\) use boundedness of \((q/K)\log(e2K/q)\), and for \(K<q\le2K\) both factors are already bounded by their stated constants. Apply the adjoint Gram bound on \(I\) to obtain \(O((P/K)\|a^\pm\|_2^2)=O(PK)\), with every rational multiplicity included. The uniform interval contributes \(O(K^2)\) because each full-residue discrepancy from \(P/k\) is at most one. The sum of row maxima is at most \(O(\sqrt K)\) times the square root of the cumulative quadratic error, giving \(O(K\sqrt P)=O_B(P/\log^B T)\) for every fixed \(B\). All constants can be chosen independently of \(T\) for fixed \(\theta\), window and coefficient bounds. The unit-mean re-centering decreases the squared error and at most doubles each row maximum.

For a common divisor \(d\mid k,k'\), the marginal of either full row in a class \(r\bmod d\) is exactly \(\sum_{n\equiv r(d)}b(n)\). This verifies the asserted CRT compatibility of the full rows. Restricting a row to units uses a \(k\)-dependent condition on \(n\), so equality of the restricted marginals is not a further consequence. Likewise the unit-row mean is not the prime-style baseline \(P/\varphi(k)\). For example the all-residue norm puts the mass in the single unit class modulo 2 at \(P/2+O(\sqrt{PK})=P/2+o(P)\), so that class differs by order \(P\) from the prime-model reference \(P\). The two scopes cannot be conflated.

## Large projection and optional integer weights

Self-adjointness of \(\psi\) gives
\[
 \sum_n H(n)(b^+(n)-b^-(n))
   =(K/M)\left(M^2-\frac{|\sum_{n\in I}F(n)|^2}{|I|}\right).
\]
Indeed \(a^+-a^-=(K/M)(F-\langle F\rangle_I\mathbf1_I)\). The mean term is negligible: each bounded periodic \(\psi*h_k\) has zero period average, so the interval contributes at most \(O(k)\) per \(k\), and \(|\sum_I F|\ll KS\). The ratio of the subtracted square to \(M^2\) is \(O(K^2 S/P^2)=o(1)\). The difference is positive of order \(KM\). This proves a large **absolute** projection for at least one of the individual sequences. Dividing by \(K\) yields \(\gg\sqrt{PS}\asymp K\sqrt T/\log^2 T\), which dominates \(T\log^4T\) since \(T^{\theta-1/2}/\log^6 T\to\infty\). No sign for the individually selected projection is needed.

The source proof has real weights on integer indices. To obtain nonnegative integer weights with exactly the same mass \(P\), let \(X_n\) be independent rounding of the selected \(b(n)\) to one of its two adjacent integers, with expectation \(b(n)\). Then the rounding error \(e_n=X_n-b(n)\) is centered, bounded by 1, and has variance at most \(1/4\). The expected summed full-residue squared discrepancy of the errors is at most \(O(PK)\) by independence, since every \(n\) enters exactly one class per modulus. The mass error variance is \(O(P)\). Since \(\|H\|_\infty\ll S\), the projection error variance is \(O(PS^2)\). Markov and Chebyshev with fixed sufficiently large constants jointly give an outcome with error budgets \(O(PK)\), \(O(\sqrt P)\), and \(O(\sqrt P\,S)\), respectively. This projection error is \(o(K\sqrt{PS})\) since \(\sqrt S/K\to0\).

Correct the total integer mass by adding at any one site, or by removing at most \(O(\sqrt P)\) units from occupied sites in \(J\) without creating negative values. The correction has total absolute mass \(O(\sqrt P)\). Thus for each modulus its squared row norm is at most \(O(P)\), and its \(H\)-projection is \(O(\sqrt P\,S)\). The final integer-valued sequence keeps the quadratic and maximum norm bounds, the nonnegative exact mass, and the absolute lower bound. This extension does not supply a zero–one-valued indicator or prime support.

No quantifier failure found for fixed \(\theta\) and the selected whole interval with the specified centering. The counterexample rules out the inference from these norm bounds and common full rows alone. A prime-only local density condition, uniform estimates across additional intervals, or smoothing of the entire target phase sum remains outside the conclusion. No canonical changes.
