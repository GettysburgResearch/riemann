# Testing one abundance inequality on a cubic logarithmic grid

Let \(k_n=\lfloor\exp(n^{1/3})\rfloor\). Use the arithmetic log moments \(W_\phi,W_\sigma\) and their common continuous model \(W_*\) from the [curvature theorem](abundance-curvature-nov18.md). The following are proposed equivalent statements.

* RH.
* \(W_\phi(k_n)\ge W_*(k_n)\) for every sufficiently large positive integer \(n\).
* \(W_\sigma(k_n)\le W_*(k_n)\) for every sufficiently large positive integer \(n\).

There are asymptotically \((\log S)^3\) sample indices up to moment order \(S\). More precisely, if RH fails and \(1/2<c<\Theta\), each sign of each moment discrepancy exceeds \(k_n^c\) in absolute size infinitely often on this same grid. The equivalence and the larger excursions also hold for either sequence of arithmetic moments obtained by replacing \(k_n\) by the unrounded order.

### Analytic continuation of the real log moment

Write \(D(s)=W_\phi(s)-W_*(s)\). For \(w=v+it\), \(v\) large and \(|t|\le 1/(2v)\), there is a holomorphic continuation, with a neighborhood of the displayed region, satisfying
\[
 |D(e^w)|\ll e^v(1+\log v).
 \tag{1}
\]
In fact, put \(S=e^v\), \(b(p)=-\log(1-1/p)\). The elementary factors are \((p-1+e^{s b(p)})/p\). If \(p\le S/(2v)\), then \(\Re(s)b(p)\ge 2v\cos t >\log(2p)\), and their local logarithms can be written as
\[
 s b(p)-\log p+\log(1+(p-1)e^{-s b(p)}).
\]
If \(S/(2v)<p\le S\), then \(|\Im(s)b(p)|\le (1+o(1))\) uniformly, so the arguments of both terms of \(p-1+e^{sb(p)}\) have magnitude below \(1.1\). Its normalized logarithm has absolute value \(O(1+S b(p))\), using the positive real projections. For \(p>S\) the log factors are \(O(S/p^2)\). The local logarithms in overlapping descriptions agree by continuation from the real axis. Summing by the elementary estimates for \(\sum_{p\le S}p^{-1}\), \(\vartheta(S)\) and the prime tail proves the bound for \(W_\phi\). The same argument with \(p\) replaced by a real variable and \(dv'/\log v'\) in place of counting measure proves it for \(W_0\). Normal convergence on compact sets gives holomorphy. The real linear model correction is harmless.

### A contour quadrature for the Gaussian mean

Fix a sufficiently small \(\epsilon>0\). Let \(g_u(v)=(4\pi\epsilon u)^{-1/2}\exp[-(v-u)^2/(4\epsilon u)]\) for large real \(u\). Set \(a,b\) to the nearest half-integers to \((u/2)^3,(2u)^3\), respectively. Then
\[
 \int_0^\infty g_u(v)D(e^v)\,dv
 =\sum_{a<n<b}\frac{g_u(n^{1/3})}{3n^{2/3}}D(e^{n^{1/3}})+O_\epsilon(e^{-u/5}).
 \tag{2}
\]
On the rectangular contour \(a\le\Re z\le b, |\Im z|\le u/4\), define
\[
 H(z)=\frac{g_u(z^{1/3})D(e^{z^{1/3}})}{3 z^{2/3}}
\]
using the principal powers. For \(q=(\Re z)^{1/3}\), direct Taylor expansion gives \(\Re z^{1/3}=q+O(u^{-3})\), \(\Im z^{1/3}=\Im z/(3q^2)+O(u^{-3})\), uniformly on the rectangle. Thus \(|\Re(z^{1/3})\Im(z^{1/3})|\le 1/6+o(1)\), strictly inside (1). Completing the square on the horizontal edges gives \(|H(z)|\ll_\epsilon (1+u)^C e^{(1+\epsilon)u}\). At either vertical edge \(q=u/2+O(u^{-2})\) or \(2u+O(u^{-2})\), so \(|H(z)|\ll_\epsilon e^{-2u}\) for \(\epsilon<1/100\), by (1). The same Gaussian tail calculation bounds the cost of cutting the original real integral at these endpoints by \(O_\epsilon(e^{-u})\).

For clarity, integrate \(H(z)\cot(\pi z)/(2i)\) counterclockwise around the rectangle. Its residues give the sum in (2). On the upper edge \(\cot(\pi z)=-i+O(e^{-\pi u/2})\), on the lower it is \(i+O(e^{-\pi u/2})\), and on the vertical half-integer edges its modulus is at most one. The constant parts times the horizontal integrals contribute the ordinary real integral of \(H\), up to the same exponentially small vertical errors by Cauchy's theorem. Since \(\pi/2>1+\epsilon+1/5\), this proves (2) after \(z=v^3\).

### Detection of both signs

The [signed Gaussian obstruction](abundance-tail-localization-nov18.md) gives, for arbitrarily small fixed \(\epsilon>0\) and any \(c<d<\Theta\), values of each sign of the left-hand side of (2) of absolute size \(>e^{du}\) along sequences \(u\to\infty\). More explicitly choose a zero with \(\beta_0>d\), then take \(\epsilon\) small enough that \(\Re(\rho_0+\epsilon\rho_0^2)>d\). The finite rectangle and endpoint asymptotic there produce the signed peaks. Decrease \(\epsilon\) further so that \(c+\epsilon c^2<d\). This flexibility is needed for pointwise signed lower bounds on the grid.

If \(D(e^{n^{1/3}})\le e^{c n^{1/3}}\) eventually, the sum on the right of (2) is at most \(O_\epsilon((1+u)^C e^{(c+\epsilon c^2)u})\), by positivity of the weights and completing the square for each term. This contradicts the positive peaks. The identical argument with \(-D\) gives negative excursions. For the divisor-sum moment the unconditional difference \(W_\phi(s)-W_\sigma(s)=O(\sqrt{s/\log s})\) is absorbed by choosing any intermediate exponent strictly between \(c\) and \(\Theta\). Rounding the moment order costs \(O(1+\log\log s)\), since both arithmetic first derivatives and the model derivative are \(O(1+\log\log s)\) by the [saddle calibration](abundance-exact-saddle-nov18.md). Finally on RH the opposite signed margins of order \(\sqrt{s/\log s}\) hold for every sufficiently large real order by the primary profile. These facts prove all assertions.

The test still requires a proof of one eventual inequality on the specified integer sequence. The grid bound alone supplies no final sign.

### A finite arithmetic inequality for every sampled moment

The criterion permits replacing the limiting distribution by an explicit finite average. Let \(M_k=\operatorname{lcm}(1,2,\ldots,k)\), \(z_\phi(d)=d/\varphi(d)\) and \(z_\sigma(d)=\sigma(d)/d\). Put
\[
 B_Z(k)=\frac1{M_k}\sum_{r=1}^{M_k}z_Z(\gcd(r,M_k))^k .
\]
Each is rational and its efficient evaluation uses the product of its prime-local rational factors. The two separate tests in the theorem remain equivalent to RH with \(W_Z(k_n)\) replaced by \(\log B_Z(k_n)\).

Indeed CRT makes the truncated valuations independent, with the distribution of \(\min(v_p,e_p)\) for \(p\le k\), where \(e_p=\lfloor\log k/\log p\rfloor\) and \(v_p\) has geometric tail \(\Pr(v_p\ge j)=p^{-j}\). For either statistic omitting \(p>k\) costs \(O(1)\) in the log moment, since \(0\le\log\mathbb E z_Z(p^{v_p})^k\le \log(1+[(1-1/p)^{-k}-1]/p)\ll k/p^2\) there. Capping the remaining valuations changes no totient factor. For the divisor-sum factor its score changes by at most \(-\log(1-p^{-e_p-1})\le2p^{-e_p-1}\). The log moment thus changes by at most \(2k\sum_{p\le k}p^{-e_p-1}\). For \(p\le\sqrt k\) each summand is at most \(1/k\) and there are \(O(\sqrt k/\log k)\) such primes. For larger primes the reciprocal-square tail is \(O(1/(\sqrt k\log k))\) by Chebyshev and partial summation. Consequently
\[
 0\le W_\phi(k)-\log B_\phi(k)\ll 1,\qquad
 0\le W_\sigma(k)-\log B_\sigma(k)\ll\sqrt k/\log k.
\]
These errors are smaller than the signed RH margins \(\asymp\sqrt{k/\log k}\), as well as the larger excursions upon failure of RH.
