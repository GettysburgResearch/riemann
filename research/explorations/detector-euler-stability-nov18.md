# Exact multiplicativity, sparse prime edits, and the real-axis condition

Let \(b\) be real multiplicative with \(|b(n)|=\mu(n)^2\) and \(b(1)=1\). In the native fixed detector replace \(\mu\) by \(b\), write \(D_b(z)=\sum b(n)n^{-z}\), \(s=z-1/2\), and use
\[
 F_b(s)=\{6+P(z)D_b(z)\}/s^2,\qquad P(z)=-3(2^{-z}-1)(2^{-z}-2).
\]
The original row and the heat averages are specified in [the diffusion note](detector-diffusion-nov18.md).

## Stability under real-axis regularity

Write \(E=\{p:b(p)=1\}\). In \(\Re z>1\),
\[
 G(z)=\zeta(z)D_b(z)=\prod_{p\in E}\frac{1+p^{-z}}{1-p^{-z}}.
\]
This is a Dirichlet series with nonnegative coefficients, including coefficient 2 at every changed prime. Suppose \(D_b\) continues holomorphically along the entire real interval \((1/2,\infty)\) and \(D_b(1)=0\). The second condition follows already from the first if \(\sum_{p\in E}1/p<\infty\), by taking real limits of the convergent Euler correction from the right. Then \(G\) also continues holomorphically along that interval. Landau's theorem applied to its positive coefficients gives convergence everywhere in \(\Re z>1/2\). In particular \(\sum_{p\in E}p^{-\sigma}<\infty\) for each \(\sigma>1/2\); conversely this condition makes \(G\) holomorphic, nonvanishing and bounded with bounded reciprocal on each such closed right half-plane by its Euler product.

Thus the two real-axis conditions force **every pole of \(D_b\) in \(\Re z>1/2\) to coincide, including its order, with a pole of \(1/\zeta\)**. Both signed parts of the unsmoothed modified row have exactly the same limiting growth exponent \(\Theta-1/2\) on every arbitrarily slowly widening window as the true row, by [positive isolation](detector-positive-isolation-nov18.md). The proof there carries through with the bounded, nonvanishing multiplier \(G\) on each shifted strip. In particular subpower negative mass at arbitrarily sparse unbounded horizons for the modified row is equivalent to RH itself. An exact scalar check at any fixed real \(z>1\) is even more rigid: \(D_b(z)=1/\zeta(z)\) would force \(G(z)=1\), hence \(E=\varnothing\).

## A multiplicative example with eventual positive heat and large negative native mass

Without the real-axis condition the following holds independently of RH. Fix an arbitrary finite list of prescribed primes, a finite native prefix, and \(\eta>0\). Fix any \(1/2<\beta<3/4\) different from \(\Theta=\sup_\rho\Re\rho\), and put \(a=\beta-1/2\). There is an exactly multiplicative squarefree sign system as above, matching all prescribed entries and with \(\sum_{p\in E}1/p<\eta\), such that

1. its heat average is positive at every sufficiently large center, **uniformly** for \(\epsilon\ge10^{-6}\);
2. on every sufficiently late log window \([T-C,T]\) of some fixed length its native negative mass is \(\gg e^{aT}\).

Thus the changed integers have upper natural density at most \(\eta\), by summing \(\lfloor x/p\rfloor\) over changed primes. One of the two choices \(\beta=2/3,7/10\) always suffices. The construction introduces a real pole at \(z=\beta\); its heat claim concerns eventual positivity. The [sparse nonmultiplicative construction](detector-backward-heat-nov18.md) instead preserves every prime coefficient, positivity at all centers and regularity on the positive shifted real axis.

**Lattice of prime packets.** Choose a spacing \(h>0\), to be specified below, and a sufficiently large integer \(J\). For each \(j\ge J\) put \(y_j=e^{jh}\), and select exactly \(\lfloor y_j^\beta/(2j)\rfloor\) primes in \([y_j,y_j+y_j^{4/5}]\). The classical prime number theorem in short intervals guarantees the supply, since the exponent \(4/5>7/12\) and \(\beta<3/4\). For large \(J\) the cells are disjoint and their total harmonic prime mass is \(O(\sum_{j\ge J}e^{-(1-\beta)jh}/j)\). Use precisely these primes as \(E\). [Huxley](https://doi.org/10.1007/BF01418933)

For \(q=e^{-h(z-\beta)}\) the Euler correction satisfies
\[
 G(z)=\frac{E_J(z)}{1-q},\qquad
 \log E_J(z)=-\sum_{1\le j<J}q^j/j+
 \sum_{j\ge J}\left(2\sum_{p\text{ chosen in }j}p^{-z}-q^j/j\right)
 +2\sum_{p\in E}\sum_{l\ge1}\frac{p^{-(2l+1)z}}{2l+1}.
\]
Initially this is an identity for \(\Re z>\beta\). Rounding and shifting \(p\) within its cell cost \(O(y_j^{-\sigma}+(1+|z|)y_j^{\beta-\sigma-1/5}/j)\) per cell, for \(\sigma=\Re z\) in any fixed positive bounded interval. The higher powers converge for \(3\sigma>\beta\). Thus \(E_J\) is holomorphic and nonvanishing for \(\sigma>\max(\beta-1/5,\beta/3,0)\). On every finite set of harmonics \(z_k=\beta+2\pi ik/h\),
\[
 e^{H_{J-1}}E_J(z_k)\longrightarrow1\qquad(J\to\infty),
\]
where \(H_{J-1}=\sum_{j<J}1/j\). In particular the residue of \(F_b\) at \(s=a\) is strictly positive since \(E_J(\beta)>0\), \(P(\beta)<0\) and \(\zeta(\beta)<0\).

**Eventual heat sign.** Fix \(0<\alpha<a\) sufficiently close to \(a\) for this continuation, avoiding poles on the vertical segment to be used. Shift the heat contour in a finite rectangle from \(\Re s=1\) to \(\alpha\), with height \(H\) avoiding the lattice and zeta poles and chosen so \(1+10^{-6}(1-H^2)<-1\). The right tails and the horizontals cost \(O(e^{-U})\) uniformly in \(\epsilon\ge10^{-6}\). The finite left segment costs \(O(e^{(\alpha+\epsilon\alpha^2)U})\). Each crossed nonreal lattice pole has strictly smaller real heat exponent than the real pole by at least \(\epsilon(2\pi/h)^2\). The shifted zeta zeros have negative real heat exponent for \(\epsilon\ge10^{-6}\) by the previously cited verified zero census and \(a'+\epsilon((a')^2-\gamma^2)\) with \(|a'|<1/2\). Coincident zeta and lattice poles merely increase polynomial factors. Relative to the real exponent, all these finitely many nonreal contributions have a gap bounded below by \(c(1+\epsilon)\) for some \(c>0\): each gap is affine increasing in \(\epsilon\) with strictly positive slope and is positive at \(10^{-6}\). Their polynomial factors in \(U(1+\epsilon)\) are absorbed by exponential decay. The real pole therefore supplies a strictly positive leading term uniformly over the asserted diffusion range.

**Native sign when \(\Theta>\beta\).** Select an actual zero farther to the right than \(\beta\) and put the safe contour of the positive isolation proof strictly between these two real parts. On this strip \(G\) is an absolutely convergent nonzero Euler factor; there is no real pole there. The original proof applies, yielding a larger exponential negative mass than asserted.

**Native sign when \(\Theta<\beta\).** Write \(f(v)=w(v)-6v_+\) with the actual row extended by zero to the left. In this case \(f(v)=O(e^{(a-\nu)v})\) for some \(\nu>0\) as \(v\to\infty\), by shifted inversion in the positive isolation note. On \(0<v<\log2\) it is exactly \(-6v\). Therefore for sufficiently large fixed \(h\), the continuous \(h\)-periodic function
\[
 Q_h(v)=\sum_{j\in\mathbb Z} e^{-a(v+jh)}f(v+jh)
\]
is strictly negative on a nonempty compact subinterval of \((0,\log2)\). Its Fourier coefficients at \(\omega_k=2\pi k/h\) are
\[
 c_k=\frac{P(z_k)}{h(a+i\omega_k)^2\zeta(z_k)}.
\]
A translated Fejér kernel gives a nonnegative trigonometric polynomial \(p(v)=\sum p_k e^{i\omega_k v}\) satisfying \(\sum_k c_k p_{-k}<0\). Use the positive convolution measure \(e^{ax}p(-x)\mathbf1_{[0,h]}(x)dx/h\). Its transform at every \(a+i\omega_k\) equals \(p_{-k}\); hence it eliminates every lattice pole beyond the finite degree of \(p\). All poles there are simple because \(\beta>\Theta\). Convolve with a narrow positive Gevrey density from the isolation proof so that its transform \(V\) is arbitrarily close to 1 on these finitely many points. Then, for sufficiently large \(J\),
\[
 \sum_k c_k p_{-k} V(a+i\omega_k) E_J(z_k)<0
\]
by the harmonic limit above; the expression is real by conjugation.

For contour justification take a line \(\Re z=\beta-d>\max(\Theta,1/2)\) with \(0<d<1/20\). Uniformly between it and the original line, \(|E_J(z)|\le\exp(O_J((2+|t|)^{5d}\log(2+|t|)))\). Indeed for the cell errors split at \(y_j=(2+|t|)^5\), bounding smaller cells trivially by \(O(y_j^d/j+y_j^{-\sigma})\) and larger ones by the derivative estimate. The finite missing sum and higher-prime-power sum are bounded on this strip. The Gevrey multiplier decays as \(e^{-c\sqrt{|t|}}\). Take horizontal contours midway between consecutive lattice heights; the factor \((1-q)^{-1}\) is bounded there and on the left line. The zeta reciprocal is subpolynomial on this zero-free strip by the three-circles argument. The convolved row is consequently a finite lattice trigonometric polynomial times \(e^{au}\), with error \(O(e^{(a-d)u})\). At \(u\in h\mathbb Z\) its leading polynomial is exactly the negative sum displayed above. Positivity, bounded density and fixed support of the kernel transfer this lower bound to the integrated native negative mass in each sufficiently long fixed log window. No independence of ordinates is used.
