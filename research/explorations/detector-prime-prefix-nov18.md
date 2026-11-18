# A signed unsmoothing estimate from verified prime data

The height-20000 replay in [the diffusion note](detector-diffusion-nov18.md) gives strict native positivity through \(2\cdot10^{17}\). With the same zero enclosures one obtains
\[
 w(\log X)>0\qquad(2<X\le9.9\cdot10^{18}).
\]
Thus the cumulative negative mass is exactly zero throughout this range.

## A finite Mertens estimate

Put \(Q=10^{16}, P=10^{19}\). Use the three explicit bounds \(|M(x)|\le\sqrt x\) for \(x\le Q\), \(|\psi(x)-x|\le0.94\sqrt x\) for \(11<x\le P\), and \(\psi(x)\le1.04x\). These are (5), (11), and Lemma 2.3 of [Ramaré and Zuniga-Alterman](https://arxiv.org/abs/2408.05969). We prove \(|M(x)|<0.61x^{3/4}\) for \(Q\le x\le P\).

Write \(E(y)=\psi(y)-\lfloor y\rfloor\), \(S(x)=\sum_{n\le x}\mu(n)\log n\), \(K=\lfloor\sqrt x\rfloor\). The identities \(\mu\log=-\mu*\Lambda\) and \(\mu*1=\delta_1\) give
\[
 S(x)=-1-\sum_{l\le x/K}\mu(l)E(x/l)-\sum_{k\le K}(\Lambda(k)-1)M(x/k)+E(K)M(x/K).
\]
This is the hyperbola split for the convolution, counting the intersection rectangle once. On \([K,P]\), \(|E(y)|\le.941\sqrt y\). Thus the first sum costs at most \(1.882 x/\sqrt K<1.883 x^{3/4}\), and the rectangle term costs at most \(.941\sqrt x\). For the second sum with \(x/k\le Q\), partial summation of \(\psi(y)\le1.04y\) gives \(\sum_{k\le K}(\Lambda(k)+1)/\sqrt k\le4.08\sqrt K\), hence a cost of at most \(4.08x^{3/4}\). For the other terms set \(b=\sup_{Q\le x\le P}|M(x)|/x^{3/4}\). Their cost is at most \(bx^{3/4}L\), where \(L=\sum_{k\le1000}|\Lambda(k)-1|k^{-3/4}<25.513\).

Finally \(M(x)\log x=S(x)+\int_1^x M(t)dt/t\). The integral costs \(2\sqrt Q+4bx^{3/4}/3\). Divide by \(x^{3/4}\), take the supremum and obtain \(b(\log Q-L-4/3)<5.97\), proving the estimate.

## Recovering the native sign

Let \(2\cdot10^{17}\le X\le.99P\), \(u=\log X\), \(t=2u/(3\cdot20000^2)<7.4\cdot10^{-8}\). The diffusion note proves \(g(u)>6.5u\) and gives the exact hinge correction \(g(u)-w(u)=\sum_n q(n)n^{-1/2}R_t(u-\log n)\). Use \(q=6\delta_1-6\mu+9\mu(\cdot/2)-3\mu(\cdot/4)\), with nonintegral arguments interpreted as zero. For each dilation \(d=1,2,4\), set \(z=X/d\) and \(f(m)=m^{-1/2}R_t(\log(z/m))\). Partial summation bounds the corresponding unscaled Möbius sum by \(\int_1^\infty |M(m) f'(m)|dm\).

On \(|\log(z/m)|\le.01\) we have \(Q<m<P\), giving \(|M(m)|\le.61e^{.0025}z^{-1/4}m\). With \(y=\log(z/m)\), \(R_t(y)\le\sqrt{t/\pi}e^{-y^2/(4t)}\) and \(|R_t'(y)|\le e^{-y^2/(4t)}/2\), direct Gaussian integration gives
\[
 \int_0^\infty m |f'(m)|dm\le \sqrt z\,(\sqrt{\pi t}+t)e^{t/4}.
\]
On the complement use \(|M(m)|\le m\). Completing the square in the same integral multiplies its bound by at most \(2\exp[-(.01-t)^2/(4t)]<10^{-145}\). Summing the three dilation coefficients including their \(d^{-1/2}\) factors, using \(\sum_d |a_d|d^{-3/4}<13\), gives
\[
 |g(u)-w(u)|\le 6R_t(u)+.61 e^{.0025}13X^{1/4}(\sqrt{\pi t}+t)e^{t/4}+10^{-130}<219.
\]
Here the last estimate uses \(X\le.99P\) and \(t<7.4\cdot10^{-8}\). Throughout the interval \(6.5u>258\). This proves strict positivity. The finite inputs concern prime-counting and Mertens data together with the previously enclosed low zeros.

## Dyadic continuation through \(327680000000000000000\)

The same arithmetic input, with the global \(|\psi(y)-y|\le1.93378\cdot10^{-8}y\) for \(\log y\ge40\) from (14) of the same source, extends strict positivity through \(2^{15}Q\). Define \(X_j=2^jQ\), \(B_0=0\), and let \(B_j\) bound \(|M(x)|/x\) on \(X_{j-1}<x\le X_j\) for \(j\ge1\). The symbol \(B_0=0\) discards terms already bounded using the Hurst input. Compute the exact finite weights \(W_r=\sum_{2^r\le k<2^{r+1}}|\Lambda(k)-1|/k\). For \(j\le16\) choose the inductive bounds by
\[
 B_j(\log X_{j-1}-1.5)=F_j+
 \sum_{l=1}^{j-1}2^{l-j}B_l+
 \sum_{r=1}^{j-1}W_r\max(B_{j-r-1},B_{j-r}),
\]
where, writing \(L=X_{j-1}\),
\[
 F_j=6.1L^{-1/4}+3L^{-1/2}+2\sqrt Q/L+
 2.1\cdot10^{-8}(1+\max(0,\log(X_j/P))).
\]
To check this bound use the hyperbola identity again. For \(x/l>P\), use \(|E(x/l)|\le2.1\cdot10^{-8}x/l\) and sum the harmonic series. All other first-sum terms, the intersection, and the terms with \(x/k\le Q\) obey the former explicit bounds. In this range \(x/K<Q\) and \(K<P\). After division by \(x\), the earlier bins of the integral cost the displayed length ratios. The current bin costs at most one half times its supremum. The \(k=1\) contribution costs one further copy of that supremum. For \(k\ge2\) with \(x/k>Q\), the quotient lies in one of the two indicated earlier bins, and the normalized coefficient is \(|\Lambda(k)-1|/k\). Moving the two current-bin terms to the left proves the induction.

Use these bounds locally in the deconvolution formula above. Its variation bound improves to
\[
 \int_0^\infty m|f'(m)|dm\le \sqrt z\big(2\sqrt{t/\pi}+t/2\big)e^{t/4}.
\]
Indeed \(\tfrac12\int e^{-y/2}R_t(y)dy=2(e^{t/4}-1)\) and \(\int e^{-y/2}|R'_t(y)|dy=2e^{t/4}\operatorname{erf}(\sqrt t/2)\) by integration of the complementary error function. The previous Gaussian complement estimate gives a total cost below 1 including \(6R_t(u)\) for \(2^8Q\le X\le2^{15}Q\), since \(t<8\cdot10^{-8}\). For \(d=2^i\), \(|\log(z/m)|\le.01\) and \(X\) in bin \(j\), the admissible \(m\) range lies in bins \(j-i-1,j-i,j-i+1\). The three coefficients weighting these local bounds are \(6,4.5,.75\). The [96-bit replay](check_detector_prime_prefix_nov18.py) checks bins \(9\le j\le15\) using their larger endpoint for \(X,t\) and their smaller endpoint for the positive drift. The largest correction-to-\(\log X\) upper bound is below 6.452. The beginning of bin 9 overlaps the preceding prefix. Therefore the cumulative native negative mass is zero through \(2^{15}Q\).
