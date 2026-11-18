# A wrong abundance sign requires a displaced zero in a quantitative height window

Use \(L=\log x\ge1000\), \(s=xL\), \(H=3\cdot10^{12}\), and the two moment signs in [the finite sign theorem](abundance-finite-horizon-nov18.md). If either inequality there fails, some zero \(\rho=1/2+a+i\gamma\) has \(a>0\), \(|\gamma|>H\), and, with \(m=|\gamma|/(L+3)\),
\[
 aL>\pi m-\log(1+m)
       +\max\{20.5,\ \log|\gamma|-3\log\log|\gamma|-2\}.       \tag{1}
\]
In particular \(a>20.5/L\), and \(|\gamma|<(L+3)(L/2+\log L-20.5)/\pi\). These are necessary conditions for a sign failure, without a converse at a given zero. For a tail sign failure at \(\ell=t e^{-\gamma_E}\ge1100\) the same obstruction applies with some \(|L-\ell|<6\). No conditional zero-location assumption enters.

## The almost maximal shift without a power of the center

Let \(\kappa=-h''-h'\) be the [exact smooth kernel](abundance-low-zero-kernel-nov18.md). For every \(0<\beta<1\),
\[
 \left|\int_{\mathbb R}\kappa(u)e^{(\beta+i\gamma)u}du\right|
 \le 4+150(1+m)e^{\beta L-\pi m}.                             \tag{2}
\]
The 4 is an endpoint allowance from \(0<u<1\); the exponential factor estimates the analytic ray, not an exponentially decaying bound for the entire nonanalytic extension at zero.

For \(0<\delta\le1\) use the horizontal shift \(v=\pm(\pi-\delta)/(L+3)\), using the strip up to this height. Write \(w=u+iv\), \(z=w+(s+1)\log(1-e^{-w})\), \(Z=\Re z\), \(p=(s+1)/(e^w-1)\), \(d=(e^w-1)^{-1}\). On \(u\ge1\) the argument of \(e^w-1\) has absolute value below \(0.006\), so \(Z'=\Re(1+p)\ge0.999|1+p|\), and \(Z\) increases. For \(|u-L|\le1/L\),
\[
 |\Im z|\le |v|(1+(s+1)/(e^u-1))\le \pi-\delta
\]
because \(1+(s+1)/(e^{L-1/L}-1)<L+3\). At the left endpoint \(Z<-0.98\), and at the right endpoint \(Z>0.98\). For the first bound use \(\log|1-e^{-w}|\le-e^{-u}(\cos v-e^{-u}/2)\), \(\cos v\ge1-5/L^2\), and \(e^{1/L}\ge1+1/L\). For the second use \(|\log(1-e^{-w})|\le(e^u-1)^{-1}\) and \(e^{-1/L}\le1-1/L+1/(2L^2)\). These inequalities also give \(|Z(L)|<0.01\). Thus the principal middle patch and the small-\(e^{\pm z}\) outer patches glue just as in the wider-strip proof; outside the middle patch \(|Z|>0.9\).

On \(L-1\le u\le L+1\) the leading curvature is \(K(z)(1+p)^2/w\), \(K(z)=e^z/(1+e^z)^2\). Its weighted integral divided by \(e^{\beta L}\) is at most \(2.75\int |K(z)|dZ\), by \(Z'\ge0.999|1+p|\) and
\[
 \frac{e^{\beta(u-L)}(1+|p|)}{u}
 \le \frac{e+(L+e^{-L})e/(1-e^{1-L})}{L-1}<2.74 .
\]
On \(|Z|<0.9\), integrate the pointwise phase bound using the full real \(Z\)-axis:
\[
 \int_{-\infty}^\infty\frac{e^Z\,dZ}{1-2\cos(\delta)e^Z+e^{2Z}}
    =\frac{\pi-\delta}{\sin\delta}<3.75/\delta .
\]
On \(|Z|\ge0.9\) the reverse triangle bound costs at most \(2e^{-0.9}/(1-e^{-0.9})^2<2.4\). Thus the leading central mass is below \(17/\delta\).

For the other central terms use the lower-side \(F(z)=\log(1+e^z)\), upper-side \(F(-z)\), and their logistic derivatives. On the respective sides \(\pm Z\le0.01\). From the same phase bound on \(|Z|<0.9\), and the convergent small-exponential patch otherwise, \(|F(\pm z)|\le7/\delta\), \(|f(\pm z)|\le4/\delta\). The absolute remainder is bounded by
\[
 (4/\delta)(|1-pd|/u+2|1+p|/u^2)
 +(7/\delta)(u+2.01)/u^3 ,
\]
using \(|w|\ge u\) (equivalently bound the last term directly by \(1/u^2+2/u^3\)). Since \(|p|+1<2.73L\) and \(|pd|<0.001\) here, its normalized weighted integral is below \(0.2/\delta\).

On the right use \(h_0=(s+1)[-\log(1-e^{-w})]/w\) and the small transition \(F(-z)/w\). The integral of the bulk curvature on \(L\le u\le U=L+4\log L\), normalized by \(e^{\beta L}\), is below 4: use \(|d|,|\log(1-e^{-w})|\le1.001e^{-u}\), the identity \((h_0''+h_0')/(s+1)=d^2/w+(2d-b)/w^2+2b/w^3\), and \(e^{\beta(u-L)}\le e^{u-L}\). On \(L+1\le u\le U\), \(Z\ge u-0.37L\), so the transition terms are bounded by \(4L e^{-u+0.37L}\); the normalized integral is below 0.001. On \(u\ge U\) the full curvature integral is below 3 after normalization. Indeed the tail bound in the wide-strip note gives
\[
 s(U^{-1}+U^{-2})e^{-(1-\beta)U-\beta L}
 +2000(s+1)^2e^{-(2-\beta)U-\beta L}<3 .
\]
For \(1\le u\le L-1\) write \(Y=(s+1)e^{-u}\ge eL\). Then \(Z\le u-0.75Y\), \(|p|\le1.59Y\), and the lower transition curvature is at most \(40(1+Y)^2e^{u-0.75Y}\) by its differentiated formula. Its normalized integral is below 0.001 even discarding \(e^{\beta(u-L)}\le1\), by substituting \(du=-dY/Y\). In total the shifted-ray norm is less than \(50e^{\beta L}/\delta\). At the connector \(u=1\) the same last bound is below 1 since \(Y=(s+1)/e\); the real segment below 1 costs less than 3 by the low-kernel note. Shifting and taking \(\delta=\min(1,1/m)\), or 1 if \(m=0\), gives (2) since \(50e<150\).

## From the filter to one zero

Every zero with \(\Re\rho\le1/2\) costs at most \(1.70\sqrt x/(|\rho||1-\rho|)\), by the real kernel estimate and support of \(\kappa\) in positive \(u\). The total of these costs is below \(0.081\sqrt x\), using the critical census and the signed high-ordinate weight \(<3.1\cdot10^{-12}\). The [prime-square bounds](abundance-curvature-sigma-nov18.md) hold throughout \(L\ge1000\): \(1.97\sqrt x<P_s<2.001\sqrt x\) and \(W_\phi-W_\sigma>2.80\sqrt x\). The archimedean terms in the true explicit formula cost less than 5. Thus either wrong moment sign requires right-half-strip zeros to contribute in absolute sum more than \(0.70\sqrt x\), still so after the additive 4 in (2) is charged to their reciprocal-square sum.

The same implication holds for wrong tail signs. At \(\ell\ge1100\), the global real derivative estimates in the finite sign note put the true totient saddle at \(|L-\ell|<6\), and the deterministic saddle is in the narrower Weingartner bracket. For a wrong upper divisor tail, Markov at the model saddle forces \(W_\sigma-W_*\ge-10\). For a wrong lower totient tail, the explicit tilted lower bound at its true saddle forces \(W_\phi-W_*\le0.34\sqrt x+\log(50L)+10\). Both leave the claimed \(0.70\sqrt x\) margin. These steps use the estimates that hold globally for \(L\ge1000\), not positivity beyond the finite census horizon.

For signed ordinates above \(H\), Lehman's zero-sum estimate applied to \(1/(t\log^3t)\) gives
\[
 \sum_{|\gamma|>H}\frac1{|\gamma|\log^3|\gamma|}
 \le\frac{1}{\pi\log H}
 +0.56\left(\frac{2}{H\log^2 H}+\frac{1}{H\log^3 H}\right)<0.012 .
\]
This is the same [Lehman lemma used for the reciprocal-square tail](robin-finite-horizon-nov18.md). If every right zero failed (1), (2) and \(|\rho||1-\rho|\ge\gamma^2\) would bound the remaining normalized contribution by
\[
 150\big(e^{20.5}(3.1\cdot10^{-12})+e^{-2}(0.012)\big)<0.62,
\]
contradicting the necessary 0.70. Finally \(\pi m-\log(1+m)\ge(\pi-1)m\) implies \(m<L\); substituting \(\log(1+m)\le\log L\) is valid since actually \(m<L/[2(\pi-1)]\). This yields the stated explicit height restriction.

## Why the leading constant is π for this specific observable

Fix \(0<\beta<1\). For each real \(v\), the native kernel has the scaling limit
\[
 \lim_{L\to\infty} e^{-(\beta+i vL)L}
     \int_{\mathbb R} e^{(\beta+i vL)u}\kappa(u)du
   =\int_{\mathbb R}e^{ivq}K(q)dq
   =\frac{\pi v}{\sinh(\pi v)} ,
\]
with the continuous value one at zero. Indeed at \(u=L+q/L\) the real \(z\) tends to \(q\) and \((1+p)/L\to1\). On \(|u-L|\le1\), \(z'\) is comparable to \(L\) and \(|z(L)|=o(1)\), giving an integrable \(O(e^{-c|q|})\) bound after scaling the leading \(K(z)(1+p)^2/u\) term. The lower-order central terms contribute \(O(1/L)\). The left and right transition tails are exponentially small as above. For fixed \(\beta<1\), the right bulk is \(O_\beta(1/L)\) after normalization: keep the decaying factor \(e^{-(1-\beta)(u-L)}\) when integrating the \((s+1)e^{-u}/u^2\) term. The full far tail at \(L+4\log L\) tends to zero on this normalization by the same fixed-\(\beta\) estimates. The Fourier transform follows by substituting \(e^q\) and using the beta integral.

Thus an ordinate-uniform filter bound of the form (2) with \(\pi\) replaced by any larger fixed constant and any fixed polynomial factor in \(m\) would fail for this kernel: first take \(L\to\infty\) with \(\gamma=vL\), and then \(v\to\infty\). This is sharpness for unrestricted Fourier frequencies. It does not assert that zeta ordinates and off-line real parts realize the obstruction.

The same barrier can be located in the transition itself. With \(n=L+1\) and bounded complex \(p_0\), the solution near \(L\) of \(z(w)=p_0\) has expansion
\[
 w=L+\frac{p_0}{n}+\frac{L p_0^2}{2n^3}
         +\frac{L(2L-1)p_0^3}{6n^5}+O_{p_0}(L^{-4}).
\]
To justify inversion, put \(w=L+q/n\) on a fixed \(q\)-disk around \(p_0\). There \(z=q+O_{p_0}(1/L)\) with derivative in \(q\) tending to one, from \(z=L+q/n-Le^{-q/n}+O_{p_0}(Le^{-L})\). Rouché gives the local root, and substitution of the displayed expansion leaves error \(O_{p_0}(L^{-3})\) in \(z\), hence \(O_{p_0}(L^{-4})\) in \(w\). Taking \(p_0=i\pi\) produces a simple zero of \(1+e^{z(w)}\); the logarithm in \(h\) has a genuine branch point there. Its distance above the real axis is \(\pi/(L+1)-\pi^3 L(2L-1)/(6(L+1)^5)+O(L^{-4})\). Consequently a contour argument restricted to a pole-free horizontal strip cannot achieve a fixed leading constant greater than \(\pi\).

## An explicit finite consequence with the classical zero-free region

The published height \(H_1=3{,}000{,}175{,}332{,}800\) and \(R=5.558691\) give \(a\le1/2-1/(R\log|\gamma|)\) for every right-half-strip zero above that height. This is the same [zero-free input as in the Jensen sector estimate](jensen-finite-sector-nov18.md). Consequently **both desired moment signs hold throughout \(1000\le L\le4{,}369{,}185\)**, and the tail signs hold throughout \(1100\le\ell\le4{,}369{,}179\). The sole purpose of the last six units is to accommodate displacement of the true tail saddle.

For \(L\le4.4\cdot10^6\) the function
\[
 \pi m-\log(1+m)+20.5
    -L\left(\frac12-\frac1{R\log |\gamma|}\right)
\]
increases with \(|\gamma|\ge H_1\): multiply its derivative by \(L+3\), and the positive term is at least \(\pi-1\), whereas \(L(L+3)/(R H_1\log^2 H_1)<0.002\). It decreases with \(L\) at fixed \(|\gamma|\). At the worst endpoint the following 128-bit ball comparison proves it strictly positive, contradicting (1):

~~~python
from flint import arb, ctx
ctx.prec = 128
H, R, L = arb(3000175332800), arb("5.558691"), 4369185
m = H / (L+3)
margin = arb.pi()*m - (1+m).log() + arb("20.5") - L*(arb(1)/2 - 1/(R*H.log()))
assert margin > arb("0.0016")
~~~

With just the rounded verified height \(3\cdot10^{12}\) and the critical strip, the same comparison gives \(L\le4{,}341{,}613\) from (1). The bound using the zero-free region improves the endpoint and keeps the leading \(\pi\) spectral filter unchanged.

## The profile at an attained or unattained off-line edge

If \(\Theta=\sup\Re\rho>1/2\), define the uniformly absolutely convergent real series
\[
 F_\Theta(v)=\sum_{\Re\rho=\Theta}
                 \frac{e^{i\gamma v}}{\rho(1-\rho)}
\]
including multiplicities, with value zero for an empty edge. Then, for either actual distribution,
\[
 \frac{W_Z(x\log x)-W_*(x\log x)}{x^\Theta}
       =F_\Theta(\log x)+o(1),\qquad
 \frac{\mathcal E_Z(t)}{y^\Theta}=F_\Theta(\log y)+o(1).
\]
Consequently if the supremum is attained, both wrong signs occur on subintervals of uniformly positive length in every sufficiently long fixed window of \(\log y\), at size \(\gg y^\Theta\). If the edge is unattained, both normalized residuals tend to zero even though their separate signed power exponents still equal \(\Theta\).

For the moment formula, each fixed zero has \(e^{-\rho L}\int e^{\rho u}\kappa(u)du\to1\), by the preceding transition scaling argument with the scaled frequency \(\gamma/L\to0\). Estimate (2) bounds the normalized transform uniformly over all zeros by 154 after division by \(e^{\Theta L}\). The reciprocal-square series converges absolutely. Dominated convergence therefore removes all strictly lower real parts and replaces the kernel by 1 at the exact edge. The prime-square, archimedean and difference-of-moments terms are \(O(\sqrt x)\).

For the tails use the two Legendre minima as in the [stochastic comparison](abundance-stochastic-comparison-nov18.md): their difference lies between \((W_Z-W_*)(s_*)\) and \((W_Z-W_*)(s_Z)\). Both saddle coordinates \(s_j=x_j\log x_j\) satisfy \(x_j/y\to1\) *unconditionally* by the [real derivative calibration and exact tilted saddle](abundance-exact-saddle-nov18.md) and the deterministic model calibration. Uniform continuity of \(F_\Theta\) thus gives the same normalized expression at both endpoints. The saddle logarithmic correction and Weingartner-model bounded offset vanish on this scale. This sandwich works equally for the two critical-line profiles when RH holds.

If the edge is nonempty, the uniformly almost periodic \(F_\Theta\) has zero first mean and strictly positive squared mean: after combining repeated frequencies each coefficient is nonzero. Approximation by finite truncations shows convergence of the first and second means uniformly in the initial point of long intervals. Hence it has peaks of both signs of uniform magnitude on every sufficiently long interval, and uniform continuity gives subintervals of fixed positive length. Their measure proportion is positive, with constants depending on the edge spectrum.

## Improved unconditional remainder in Weingartner's Theorem 2

Put \(c_0=1/55.241\). As \(y\to\infty\), with \(L=\log y\), both actual Weingartner remainders satisfy
\[
 |\mathcal E_Z(t)|\ll y\exp\!\left[
   -\frac{c_0 L}{(2\log L)^{2/3}(\log(2\log L))^{1/3}}\right].
                                                               \tag{3}
\]
The analogous unconditional estimate holds for both centered log moments, replacing \(y\) by \(x\) and \(L\) by \(\log x\). In particular the leading coefficient relative to \(L/(\log L)^{2/3}(\log\log L)^{1/3}\) is at least \(2^{-2/3}/55.241-o(1)\). The scale in (3) is smaller than the unconditional remainder \(y\exp[-cL^{3/5}/(\log L)^{1/5}]\) stated in [Weingartner's Theorem 2](https://arxiv.org/abs/1011.4262). This comparison concerns the published bound in that theorem and makes no claim about other literature.

Indeed the [Mossinghoff–Trudgian–Yang zero-free region](https://arxiv.org/abs/2212.06867) gives \(1-\beta\ge c_0/[(\log|\gamma|)^{2/3}(\log\log|\gamma|)^{1/3}]\) at high ordinates. For \(|\gamma|\le L^2\) it gives precisely the exponent in (3), after extracting the common \(e^L\) in (2); the finitely many lower ordinates satisfy the same bound eventually because \(\beta<1\). The factor \((1+m)e^{-\pi m}\le1\). For \(|\gamma|>L^2\) one has \(m>L-3\), so the entire high-frequency exponential costs \(O(e^{-2L})\) relative to \(e^L\), even without a zero-free region. Summing (2) costs a constant in both ranges by the absolutely convergent reciprocal-square weights. The endpoint allowance, the archimedean terms and the deterministic prime-square contributions are all \(O(\sqrt x)\). This proves the moment bound. For the tails, the same Legendre sandwich evaluated at the actual and model saddles applies. At both, \(x_j/y\to1\) and \(\log x_j-L=o(1)\); the function in the exponential in (3) has bounded derivative for large \(L\). The logarithmic prefactor and bounded comparison of the deterministic Legendre minimum with Weingartner's integral are absorbed in (3). No density estimate or RH is required.
