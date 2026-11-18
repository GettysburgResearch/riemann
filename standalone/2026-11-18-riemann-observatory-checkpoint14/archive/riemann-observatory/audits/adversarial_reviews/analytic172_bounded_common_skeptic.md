# Independent bounded common-sequence phase check

The proposed construction works with deterministic weights between \(1/2\) and \(3/2\) on the integer interval, or with integer weights in \(\{0,1,2\}\) and the same exact mass. It controls the progression budgets centered at \(P/k\) and, on units, at the induced unit mean. The argument only tests the stipulated common-sequence norm implication. [Earlier common-sequence construction](prime161_common_sequence_phase_campaign.md) · [Independent earlier check](analytic163_common_sequence_review.md)

## Setup and full kernel energy

Let \(P\) be an integer with \(P\asymp KT\), \(K\asymp T^\theta\), \(1/2<\theta<2/3\). The modulus shell is \([K,2K)\), and its four-prime support \(\mathcal S\) lies in a sufficiently narrow band \([X,(1+\eta)X]\) with \(X^4\asymp K\). We assume \(S=|\mathcal S|\asymp K/\log^4K\), as holds for the full narrow band by the prime number theorem and unique factorization, including the distinct-prime subfamily. For the full family with repeats the multinomial coefficients \(c_k\) count ordered tuples and satisfy \(1\le c_k\le24\). Define \(e(v)=e^{2\pi iv}\) and
\[
h_k(n)={\bf1}_{(n,k)=1}\left(\cos(2\pi n/k)-\mu(k)/\varphi(k)\right),
\qquad H(n)=\sum_{k\in\mathcal S}(Kc_k/k)h_k(n).
\]
Each \(h_k\) has zero period mean. For a divisor \(q\mid k\), the Fourier component on denominators dividing \(q\) is the conditional average on classes mod \(q\). On a unit class \(n=a\bmod q\), write \(n=a+qj,\ j\bmod r=k/q\). In the exponential term the factor \(e(j/r)\) multiplies a unit condition periodic in \(j\) with period \(d=\prod_{p\mid r,\ p\nmid q}p\), where \(d\mid r\). A geometric sum cancels exactly when \(d<r\). This includes all cases \((q,r)>1\), as well as square factors in the part of \(r\) coprime to \(q\). If \(d=r\), the CRT gives one forbidden class per prime and a complete additive sum with magnitude \(|\mu(r)|=1\), before dividing by \(r\). A nonunit class modulo \(q\) gives a zero average. The correction term is bounded by \(1/\varphi(k)\ll 1/r\) and vanishes for repeated-prime \(k\). Thus the conditional average has modulus \(O(1/r)\), and the squared coefficient norm at exact denominator \(q\) is \(O(r^{-2})\) by orthogonal projection and normalized finite Parseval. This supplies the repeated-prime case of the conditional-average argument in [weighted170](weighted170_unit_baseline_campaign.md).

Count prime factors with multiplicity. For fixed \(q\) having \(4-m\) factors, at most \(O(X^m)\) supported \(k\)'s are multiples of \(q\), and each \(k/q\gg X^m\). Cauchy–Schwarz over these \(k\)'s, then summation over exact denominators, bounds the squared coefficient energy of \(H\) by
\[
C\sum_{k\in\mathcal S}\sum_{q\mid k}X^m(k/q)^{-2}\ll S.
\]
There are boundedly many divisors per \(k\). This proof retains all proper denominators, rather than ignoring them when estimating the Gram error.

## The bounded perturbation

Let \(J=[P,2P)\cap\mathbb Z\), \(L=\lfloor K/100\rfloor\), \(I=[P+L,2P-L)\cap\mathbb Z\), and \(\psi\) be uniform on \([-L,L]\cap\mathbb Z\). Its multiplier \(\widehat\psi(\pm1/k)\) is bounded below by a positive absolute constant for \(k\) in the modulus shell, because every cosine in its symmetric average is positive and bounded below. For a nonzero reduced frequency \(a/q\), \(|\widehat\psi(a/q)|\ll\min(1,q/K)\) by the geometric series. Convolution therefore preserves the coefficient upper bound for \(H\) and the endpoint lower bound for its selected shell frequencies.

Put \(F(n)=\sum_{K\le l<2K,\ l\in\mathbb Z}\cos(2\pi n/l)\). For \(n\in I\), the real phase \(f(l)=n/l\) has second derivative \(2n/l^3\asymp T/K^2\) throughout that interval, with absolute constant ratio in the upper and lower bounds. The second-derivative estimate yields
\[
 |F(n)|\ll K(T/K^2)^{1/2}+(T/K^2)^{-1/2}
 =\sqrt T+K/\sqrt T\ll\sqrt T.
\]
This is uniform over the whole support of the centered vector. No estimate for \(F\) at a displaced \(n\notin I\) is used. The interval Gram estimate for reduced denominators \(\le2K\) gives \(\|F{\bf1}_I\|_2^2\ll PK\), because its distinct \(\pm1/l\) coefficients are \(1/2\) and the Gram off-diagonal norm is \(O(K^2\log K)=o(P)\). The latter follows by \(1/(4K^2)\) circular separation and the harmonic upper bound for the absolute row sum.

With \(\delta=c/\sqrt T\) and \(c>0\) sufficiently small, take
\[
 a=\delta(F-\langle F\rangle_I){\bf1}_I,\qquad b={\bf1}_J+\psi*a.
\]
Then \(\|a\|_\infty\le1/2\), \(\sum a=0\), and \(\|a\|_2^2\ll\delta^2PK\ll K^2\). Positive convolution preserves the pointwise bound, and \(I+[-L,L]\subset J\) on integers, including the half-open upper edge. Consequently \(1/2\le b\le3/2\) on \(J\), \(b=0\) elsewhere, and its mass is exactly \(P\). In cumulative progression Parseval the smoothed perturbation weight at every reduced \(a'/q\ne0\) is
\[
|\widehat\psi(a'/q)|^2\sum_{\substack{k\le2K\\q\mid k}}\frac1k
\ll \min(1,q^2/K^2)\frac{\log(e\,2K/q)}q\ll K^{-1}.
\]
The adjoint Gram bound on \(I\) gives discrepancy variance \(O(PK)\), including the baseline's \(O(K^2)\) rounding. Cauchy–Schwarz gives the \(O(K\sqrt P)\) sum of row maxima, which has every fixed logarithmic saving against \(P\). The induced unit means minimize quadratic error and increase maximum error by at most a factor 2.

## Positive diagonal, lower-order terms and the signal

At \(1/k\) the unique eligible summand of \(H\) is \(h_k\): if a shell modulus \(k'\) is divisible by \(k\) it equals \(k\). For any odd \(k\) here, repeated or squarefree, \(c_k^{\mathrm{Ram}}(1)=c_k^{\mathrm{Ram}}(2)=\mu(k)\), because each numerator is a unit. Thus the coefficient at each of \(\pm1/k\) in \(h_k\) is
\[
(\varphi(k)+\mu(k))/(2k)-\mu(k)^2/(k\varphi(k))=\tfrac12+o(1)>0
\]
uniformly. The intersection of Fourier supports of \(F\) and \(\psi*H\) consists only of such shell modes. Indeed a denominator \(l\in[K,2K)\) from \(F\) must divide a supported \(k\), so \(l=k\). Therefore their coefficient inner product is positive and \(\gg S\), without any additional contribution at proper denominators on the diagonal.

The finite-interval Gram off-diagonal error in \(\sum_I F(\psi*H)\) is at most \(C K^2\log K\sqrt{KS}\), by the coefficient energy estimates for both functions. Its ratio to \(PS\) is \(O((K/T)\log^3K)=o(1)\). Each cosine in \(F\) has zero period mean and a partial period costs \(O(K)\). Each \(\psi*h_k\) is bounded, periodic and mean zero. Consequently \(\sum_I F=O(K^2)\), \(\sum_I\psi*H=O(KS)\), and the centering subtraction costs \(O(K^3S/P)=o(PS)\). By symmetry of \(\psi\),
\[
 \sum_n (b(n)-{\bf1}_J(n))\,H(n)/K
   =(\delta/K)\sum_I(F-\langle F\rangle_I)(\psi*H)
   \gg S\sqrt T .
\]
The baseline contributes \(O(S)\) to the projection against \(H/K\) by the same incomplete-period bound. The final projection therefore has positive sign and size \(\gg S\sqrt T\asymp K\sqrt T/\log^4T\), exceeding \(T\log^4T\) by a factor growing without bound. The sign and normalization refer to the real unit-centered cosine projection. Taking the real part of the unit-centered complex projection gives it as well.

## Rounding to a cap of two and preserving the mass

Independently round each \(b(n)\) to the neighboring integers with the original real value as its mean, obtaining \(B_0(n)\in\{0,1,2\}\). The rounded mass has mean \(P\) and variance \(O(P)\). In each modulus, the expected squared discrepancy of \(B_0\)'s row from the deterministic \(b\) row is \(O(P)\), by independence within each residue class and summing variances. Thus the total expected error squared is \(O(PK)\). Chebyshev for total mass and Markov for discrepancy yield, simultaneously with probability bounded below, mass error \(m=O(\sqrt P)\) and variance \(O(PK)\). For \(W=H/K\) the change in projection has variance \(O(P\|W\|_\infty^2)=O(PS^2/K^2)\). Relative to the squared deterministic lower bound \(S^2T\) this is \(O(K^{-1})\), so it retains the main term on an event of probability tending to 1.

To restore mass exactly, alter \(m\) distinct positions by one in the required direction. If removing units of mass, at least \((P-O(\sqrt P))/2\) positions are positive, since the cap is two. If adding, at least \(P-(P+O(\sqrt P))/2\) positions are below two. Thus eligible choices suffice in either case. The sum of squared row corrections is at most \(m^2\) per modulus because the signed changes have one sign and total absolute size \(m\). The total is \(O(PK)\). The correction costs \(O(\sqrt P\,S/K)=o(S\sqrt T)\) in the phase. This gives one integer-valued realization of exact mass and the required cap, discrepancy budgets and projection.

The baseline remains that of an integer sequence. Modulo 2 the all-residue bound forces odd mass \(P/2+o(P)\), whereas prime-model unit centering would put mass \(P\) in the odd row. The result therefore leaves the genuine unit-support baseline, the actual primes and the full smooth convolution outside its scope. No canonical files were modified.
