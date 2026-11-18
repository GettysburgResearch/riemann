# Individual height intervals and the inverse zeta problem

Let \(1/2<\sigma<1\), \(a=2\sigma\). Write \(M(s)=\sum_{d\in D}\lambda_d d^{-s}\), with \(|D|\le B\), and \(e(n)=\mathbf1_{n=1}-\sum_{d\mid n}\lambda_d\). A band-limited weight lets us extract the actual low coefficients of \(1-\zeta M\) on an arbitrarily translated interval. Removing the zeta pole from the testing weight is essential.

**Finite interval bound.** Fix \(A\ge0\). For each \(B\ge1\), \(t_0\in\mathbb R\), and every choice of the positive integer frequencies with \(|\lambda_d|\le(2+B+|t_0|)^A\), put \(H=C_{A,\sigma}B\log(2+B+|t_0|)\). With a sufficiently large constant,
\[
 \frac1{2H}\int_{t_0-H}^{t_0+H}|1-\zeta(\sigma+it)M(\sigma+it)|^2dt
 \gg_{A,\sigma} B^{1-2\sigma}.                                      \tag{1}
\]
There is no upper bound on the largest integer frequency. The power of \(B\) matches the [optimal long mean](nov18b-mollifier.md). Thus concentrating on one height interval still incurs this arithmetic error when the interval is sufficiently long compared with the cardinality. For a single term, one cannot replace the height-dependent interval by *any fixed interval* uniformly in its translation. Voronin universality applied to the target function 1 gives arbitrarily close approximations by zeta on each such vertical segment, and \(M=1\) then has arbitrarily small error. [Lamzouri, Lester and Radziwiłł, introduction](https://arxiv.org/abs/1611.10325)

## Coefficient extraction on the actual line

Let \(X\) be a positive integer. Take a nonnegative weight \(w\) of integral one on the real axis, entire of exponential type at most \(1/(4X)\), with Fourier support in \([-1/(4X),1/(4X)]\) using the phase \(e^{-itv}\). Require \(w(-i(1-\sigma))=0\) and sufficiently rapid polynomial decay on bounded horizontal strips. All weights below satisfy this explicitly. For \(m\le X\),
\[
 \int_{\mathbb R}(1-\zeta(\sigma+it)M(\sigma+it))m^{it}w(t)dt
       =e(m)m^{-\sigma}.                                             \tag{2}
\]
Indeed shift the line of integration of
\((1-\zeta(s)M(s))m^{s-\sigma} w((s-\sigma)/i)\) to \(\Re s=2\). The indicated zero cancels the sole pole. The Dirichlet series there converges absolutely, and for each monomial one shifts back by analyticity. The resulting Fourier coefficient vanishes for every integer \(n\ne m\), since \(|\log(n/m)|\ge\log(1+1/X)>1/(4X)\). Only the term \(n=m\) survives. The functions \(m^{-it}\) for \(m\le X\) are orthonormal under \(w(t)dt\) by the same spacing. Bessel's inequality gives
\[
 \int_{\mathbb R}|1-\zeta M|^2w\,dt\ \ge\sum_{m\le X}|e(m)|^2 m^{-a}.       \tag{3}
\]
The omitted-squarefree proof of (5) in the [long-mean calculation](nov18b-mollifier.md) uses only \(e(n)\) with \(n\le X=\lceil4B/(2-\zeta(2))\rceil\). Keeping this cutoff throughout its nonnegative sum proves that (3) is \(\gg_\sigma B^{1-a}\), for every translation of such a weight.

## Removing the tails in physical height

Here are weights with effective concentration at the required scale. Choose an integer \(k\ge4\), increase it if necessary for the fixed growth exponent below, and put \(R=64kX\). Normalize \(\phi(v)=(\sin(v/(8kX))/(v/(8kX)))^{2k}\) to integral one. Convolve it with the uniform probability density on \([-R,R]\), giving the even density \(p\) with \(0\le p\le1/(2R)\). Set
\[
 w(t)=\frac{(t^2+(1-\sigma)^2)p(t-t_0)}
 {t_0^2+(1-\sigma)^2+\int v^2p(v)dv}.
\]
Its Fourier support is unchanged by convolution, translation and polynomial multiplication, and its mass is one. The denominator is at least \(t_0^2+(1-\sigma)^2+R^2/3\). Thus \(w\ll 1/R\) for \(|t-t_0|\le2R\). Entire continuation, strip decay and the pole zero are immediate from the construction.

The normalizing integral of the unnormalized sinc power is \(\gg X\), by restriction to \(|v|\le X\). If \(|v|>2R\), the convolution has
\[
 p(v)\ll X^{-1}(16kX/|v|)^{2k}.
\]
On the specified vertical line, \(|\zeta(\sigma+it)|\ll_\sigma(2+|t|)^{C}\) and \(|M|\le B(2+B+|t_0|)^A\), independently of its frequency locations. Substitute \(|v|=2Ru\), \(u\ge1\), in the tail integral of (3). Every factor besides the sinc power and the fixed normalization is bounded by \((2+B+|t_0|+k)^{O_{A,\sigma}(1)}u^{O_{A,\sigma}(1)}\). The sinc power is at most \(8^{-2k}u^{-2k}\). With \(k\) the ceiling of a sufficiently large constant times \(\log(2+B+|t_0|)\), the whole tail costs less than half the lower bound in (3). This proves (1) first with half-length \(2R\). Enlarging to the displayed constant multiple changes the normalized inequality by a bounded factor.

**Implication for the zero detector.** The residual equals one at every zero, regardless of the filter. The low-frequency contribution in (3) exists at every height and already consumes a definite portion of the bulk error. A proof from one small global second moment would have to overcome this contribution. The weighted inequality is valid even for unbounded coefficients. The passage to (1) uses the stated size restriction.
