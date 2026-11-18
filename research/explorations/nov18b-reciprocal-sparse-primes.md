# Sparse changes of the Möbius prime signs and a real-axis rigidity theorem

Fix any \(1/2<\beta<1\), \(\gamma>0\), \(Y>0\) and \(\varepsilon>0\). There exists a real multiplicative function \(f\) on ordinary integers with \(|f(n)|=\mu(n)^2\), equal to \(\mu(p)\) for every prime \(p\le Y\), differing from \(\mu(n)\) on a set of upper density less than \(\varepsilon\). Its Dirichlet series has poles at \(\beta+i\gamma\), \(\beta-i\gamma\), and \(\beta\). The changes preserve the unconditional Möbius summatory bound up to an arbitrarily small loss in the exponential constant, Davenport's uniform additive exponential-sum bounds to every logarithmic power, Möbius orthogonality to fixed nilsequences, mean-square short-interval cancellation relative to the trivial scale, and logarithmically averaged fixed-shift two-point Chowla cancellation.

Nevertheless for every \(2(1-\beta)<\alpha<1\) and \(h=\lfloor X^\alpha\rfloor\) its actual short-interval square sum satisfies
\[
 \limsup_{X\to\infty}\frac1{\log X}
   \log\left(\frac1{hX}\sum_{X/2<n<3X}
              \left|\sum_{0\le j<h} f(n+j)\right|^2\right)
        \ge 2\beta-2+\alpha>0.                                  \tag{1}
\]
Thus even a power-sized excess over the square-root mean-square scale is consistent with all the named inputs. The example uses a real pole. The final theorem shows exactly why that feature is necessary for a sparse prime-sign perturbation which adds interior poles. These statements do not assert such a pole for the actual Möbius function.

## Deterministic prime selection

Past a cutoff \(P_0\ge Y\), take \(w_p=p^{\beta-1}(1+\cos(\gamma\log p))\), increasing \(P_0\) until \(0\le w_p\le1\). Let \(W(p)\) be their partial sum over primes up to \(p\). Put \(p\) in \(S\) when \(\lfloor W(p)\rfloor\) increases. Then
\[
 \left|\sum_{P_0<p\le x}(1_S(p)-w_p)\right|<1 .
\]
The series \(\sum_{p>P_0}(1_S(p)-w_p)p^{-s}\) is holomorphic for \(\Re s>0\) by partial summation, locally uniformly. Also \(\sum_{p\in S}1/p\ll_\beta P_0^{\beta-1}\) by partial summation and the convergent integer tail. Set \(f(p)=1\) for \(p\in S\) and \(-1\) otherwise, with \(f(p^j)=0\) for \(j\ge2\). Any changed integer is divisible by a prime of \(S\), giving upper density at most \(\sum_{p\in S}1/p\). This can be made less than \(\varepsilon\).

On \(\Re s>1\) its Dirichlet series \(F\) satisfies
\[
 F(s)\zeta(s)=\prod_{p\in S}\frac{1+p^{-s}}{1-p^{-s}}
             =\sum_{d\ge1}\frac{b(d)}{d^s},\qquad b(d)\ge0.     \tag{2}
\]
Here \(b(d)=2^{\omega(d)}\) for integers supported on \(S\), and is zero otherwise. This last series converges absolutely for every \(\Re s>\beta\), since \(\sum_{p\in S}p^{-\sigma}<\infty\) there. Its logarithm on the original half-plane is \(2\sum_{p\in S}p^{-s}\) plus a function holomorphic on \(\Re s>1/2\). Replace \(1_S\) by \(w_p\) using the discrepancy estimate. If \(w=s+1-\beta\), the remaining prime terms are those of
\(2\log\zeta(w)+\log\zeta(w+i\gamma)+\log\zeta(w-i\gamma)\).
The respective higher-prime-power sums converge absolutely because \(\Re w>1/2\) throughout \(\Re s>1/2\). Finite omitted factors contribute holomorphic logarithmic remainders there. Exponentiating these remainders gives a single-valued nonvanishing holomorphic \(H\) on that half-plane and the meromorphic continuation
\[
 F(s)= H(s)\,
 \frac{\zeta(s+1-\beta)^2\zeta(s+1-\beta+i\gamma)
                         \zeta(s+1-\beta-i\gamma)}{\zeta(s)}.     \tag{3}
\]
At each indicated point the other shifted zeta factors on the line one are nonzero. At \(\beta\) the pole has order two. At \(\beta\pm i\gamma\) it has order at least one, including the possibility that the denominator also vanishes.

## What passes through the perturbation

Equation (2) gives \(f=\mu*b\). If \(|\sum_{m\le u}\mu(m)|\ll u\exp[-c(\log u)^{3/5}(\log\log u)^{-1/5}]\), the same holds for \(f\) with every \(c'<c\). Indeed split the convolution at \(d=x^\eta\) for fixed small \(\eta>0\). Up to the split use \(\sum b(d)/d<\infty\) and apply the input bound at \(u=x/d\). Beyond the split the trivial bound costs \(O(x^{1-\eta(1-\sigma)}\sum b(d)d^{-\sigma})\), where \(\beta<\sigma<1\). Choose \(\eta\) sufficiently small in terms of \(c'/c\). The same argument with Davenport's bound at the additive frequency \(d\theta\) gives
\[
 \sup_{\theta\in\mathbb R}\left|\sum_{n\le x} f(n)e^{2\pi i n\theta}\right|
       \ll_{A,f}x(\log x)^{-A}\qquad (A>0).
\]
For a fixed nilsequence \(g(n)\), Green–Tao orthogonality applies to each fixed dilation \(g(dm)\), and dominated convergence against \(b(d)/d\) gives \(\sum_{n\le x}f(n)g(n)=o(x)\). [Green and Tao, *The Möbius function is strongly orthogonal to nilsequences*](https://arxiv.org/abs/0807.1736)

The short-interval theorem of Matomäki and Radziwiłł for real 1-bounded multiplicative functions, together with the long-interval estimate just proved, gives
\[
 \sum_{X\le n\le2X}\left|\sum_{j<h}f(n+j)\right|^2=o(Xh^2)
\]
as \(X,h\to\infty\) with \(h=o(X)\). The sum here and in (1) over \(j<h\) runs from \(j=0\). Qualitative convergence in measure suffices since the normalized short sums have modulus at most one. Tao's logarithmically averaged two-point Elliott theorem applies as well. The pretentious distance from \(f\) to any Dirichlet character times \(n^{it}\) differs in its square from the corresponding distance for \(\mu\) by at most \(2\sum_{p\in S}1/p\), uniformly in the cutoff, character, and \(t\). Thus \(f\) satisfies the same strong nonpretentiousness condition as \(\mu\). For every fixed pair of distinct nonnegative integer shifts \(a,b\), \(\sum_{n\le X} f(n+a)f(n+b)/n=o(\log X)\). [Matomäki–Radziwiłł](https://arxiv.org/abs/1501.04585) · [Tao](https://arxiv.org/abs/1509.05422)

To prove (1), choose a nonnegative nonzero smooth \(W\) supported in \((1,2)\). The integral over \(X>0\) of \(\sum_n f(n)W(n/X)X^{-s}\,dX/X\) equals \(F(s)\int W(v)v^s\,dv/v\) initially for \(\Re s>1\). Its real pole at \(\beta\) shows that the smooth sum cannot be \(O(X^a)\) for any \(a<\beta\). The averaging and finite Taylor inverse in the [native short-shift argument](nov18b-reciprocal-theta.md) express this smooth sum as \(h^{-1}\sum_n P(n/X)\sum_{j<h}f(n+j)+O_k(X(h/X)^k)\), with a uniformly bounded smooth weight supported on \([1,2]\). Consequently if the limsup in (1) were below \(2\beta-2+\alpha\), Cauchy–Schwarz would give such a bound with \(a<\beta\) by taking \(k\) sufficiently large. The same argument with \(n^{-i\gamma}f(n)\) uses the pole at \(\beta+i\gamma\) of (3) and gives the twisted form of (1).

## Real-axis rigidity for prime-sign replacements

More generally, take *any* set \(S\) of ordinary primes and make the same squarefree sign replacements. Suppose \(F\) has a meromorphic continuation to \(\Re s>\alpha\) with \(0\le\alpha<1\), is holomorphic at every real \(s\in(\alpha,\infty)\), and \(F(1)=0\). Then
\[
 \sum_{p\in S}p^{-\sigma}<\infty\quad(\sigma>\alpha),\qquad
 F(s)=H_0(s)/\zeta(s)\quad(\Re s>\alpha)
\]
with \(H_0\) holomorphic and nowhere zero throughout the latter half-plane. In particular \(F\) has precisely the poles of the actual reciprocal zeta there, with matching orders.

Indeed \(F(s)\zeta(s)\) continues holomorphically across every real point above \(\alpha\), including one. Its original Dirichlet series in (2) has nonnegative coefficients. Landau's theorem for Dirichlet series says a finite abscissa of convergence is a singular point on the real axis, so the abscissa is at most \(\alpha\). The prime terms in the absolutely convergent series prove the displayed summability. Each local factor in (2) is nonzero for \(\Re s>0\), and the product converges absolutely and locally uniformly for \(\Re s>\alpha\). Use this product for \(H_0\). This also shows that \(F\) then has a simple zero at one.

For example, a random squarefree multiplicative sign model with square-root summatory cancellation and a genuine zero at one would immediately have the same poles as \(1/\zeta\) in the open right half of the critical strip. A randomization on a prime set with divergent \(\sum_{p\in S}p^{-\sigma}\) anywhere there cannot simultaneously give those two properties. Real-axis regularity of \(1/\zeta\) is known. Turning it into a bound on its actual nonreal singularities still requires control of the full ordinary prime signs.

The example also preserves the stronger stretched-exponential upper estimate for actual short-interval squares. For every fixed \(\eta>0\) and \(X^{1/6+\eta}\le h\le X^{1-\eta}\),
\[
  X^{-1}\sum_{X\le n\le2X}\left|\sum_{0\le j<h}f(n+j)\right|^2
      \ll_{f,\eta} h^2\exp[-c(\log X)^{1/6}].
\]
For terms \(d\le D=X^{\eta/4}\) in \(f=\mu*b\), use Minkowski and the ordinary Möbius short-interval estimate of Ramachandra–Sankaranarayanan–Srinivas at \(X/d,h/d\), as in the [sawtooth estimate](nov18b-reciprocal-sawtooth.md). Here \(\sum b(d)/d\) is fixed. For the rest write \(r(n)=\sum_{d\mid n,d>D}b(d)\mu(n/d)\). By the divisor bound and Cauchy–Schwarz, for any \(\beta<\sigma<1\) and \(\epsilon>0\),
\[
 \sum_{n\le3X}|r(n)|^2\ll_\epsilon X^{1+\epsilon}
       D^{-(1-\sigma)}\sum_{d\ge1} b(d)^2/d^\sigma.
\]
The last series converges by its Euler factors over \(S\). Choose \(\epsilon<\eta(1-\sigma)/8\). On the short sums, Cauchy–Schwarz followed by counting each index at most \(h\) times gives at most \(h^2\sum_{n\le3X}|r(n)|^2\). This is a fixed power smaller than \(h^2 X\). This comparison retains an upper estimate stronger than qualitative short-interval cancellation while (1) still holds.
