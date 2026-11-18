# Both signs of the centered Goldbach residual detect the zero abscissa

**Research statement for independent review.** Write \(a_n=\Lambda(n)-1\), let \(\Theta=\sup_{\zeta(\rho)=0,\ 0<\Re\rho<1}\Re\rho\), and set
\[
 B(x)=\sum_{m+n\le x}a_ma_n,\qquad B_+(x)=\max(B(x),0),\qquad B_-(x)=\max(-B(x),0).
\]
For both signs one has
\[
    \limsup_{N\to\infty}\frac{\log(1+B_\pm(N))}{\log N}=2\Theta.       \tag{1}
\]
The limsup is over integers. The argument includes the case where no zero attains \(\Theta\). In particular, each of the two assumptions \(B(N)\ge-O_\epsilon(N^{1+\epsilon})\) for every \(\epsilon>0\), and \(B(N)\le O_\epsilon(N^{1+\epsilon})\) for every \(\epsilon>0\), implies RH. Conversely RH implies \(|B(N)|\ll N\log^3N\).

The convolution is exactly \(E(N)\) in the circle integral of Goldston and Suriajaya, by coefficient extraction in their Theorem 1, equation (12). Their equation (11) gives its relation to the usual Fujii error after the linear zero terms are removed. The difference is \(O(N)\) at integers. Bhowmik, Ramaré and Schlage-Puchta studied two-sided oscillations on RH by examining the doubled first ordinate in the Goldbach Dirichlet series. The proof below uses the whole zero spectrum in the presence of off-line zeros. [Goldston–Suriajaya](https://arxiv.org/abs/2110.14250) · [Bhowmik–Ramaré–Schlage-Puchta](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/oscillation.pdf)

## The prime exponential sum

For real \(v\) let
\[
 F(v)=\sum_{n\ge1}a_n e^{-n e^{-v}},\qquad f(v)=e^{-\Theta v}F(v).
\]
Its Mellin transform in \(t=e^{-v}\) is \(\Gamma(s)(-\zeta'(s)/\zeta(s)-\zeta(s))\) for \(\Re s>1\). A bound \(F(v)=O(e^{cv})\) at positive infinity for \(c<\Theta\) would continue this transform holomorphically to \(\Re s>c\), contradicting a zero in that half-plane since the logarithmic derivative has nonzero residue there. For every \(\delta>0\) we can therefore choose arbitrarily large \(v\) with
\[
                   |F(v)|\ge e^{(\Theta-\delta)v}.                \tag{2}
\]

Mellin inversion and displacement to \(\Re s=-1/2\) give, for \(v\ge0\),
\[
              F(v)=-\sum_\rho\Gamma(\rho)e^{\rho v}+c_0+O(e^{-v/2}),\tag{3}
\]
with multiplicities. The two poles at 1 cancel. The gamma pole at zero contributes the constant \(c_0\). One can take the horizontal lines at zero-avoiding heights with logarithmic-derivative bound \(O(\log^2 T)\) in the contour strip. Stirling decay then makes the connecting integrals vanish. On the final line the functional equation and absolute convergence at \(3/2\) give polynomial growth for the zeta terms. Stirling's formula and the zero count imply \(\sum_\rho|\Gamma(\rho)|<\infty\).

It follows that \(f\) is bounded on the whole real line, using double-exponential decay of \(F(v)\) as \(v\to-\infty\). Moreover, for every real \(w\),
\[
 f(w)=-\sum_\rho\Gamma(\rho)e^{(\rho-\Theta)w}+O(e^{-\Theta w}).  \tag{4}
\]
For \(w<0\) this last bound follows directly from \(\Re\rho>0\) and absolute summability.

## The restriction imposed by a one-sided convolution bound

For every real \(t>0\), absolute convergence and integration on \([m+n,\infty)\) give
\[
       \int_0^\infty B(x)e^{-tx}\,dx=t^{-1}F(-\log t)^2.        \tag{5}
\]
Suppose first that \(B(x)\le Cx^{2b}\) for \(0<b<\Theta\). Equation (5) immediately gives \(F(v)^2\le C\Gamma(2b+1)e^{2bv}\), contrary to (2).

For the other direction, assume \(B(x)\ge-Cx^{2b}\) for some \(0<b<\Theta\). An eventual bound at integers implies the bound on \([0,\infty)\) after increasing \(C\), since \(B(x)=B(\lfloor x\rfloor)\) vanishes on \([0,2)\). Put \(C_b=C\Gamma(2b+1)\). Positivity of \(B(x)+Cx^{2b}\) makes its Laplace integral nondecreasing as \(t=e^{-v}\) decreases. By (5) this says that
\[
                 e^v\big(F(v)^2+C_b e^{2bv}\big)
                      \quad\text{is nondecreasing in }v.          \tag{6}
\]
Choose \(0<\eta<\min(1/100,(\Theta-b)/(3(1+2b)))\) and \(0<\delta<\min(\eta/8,(\Theta-b)/3)\). At each sufficiently large \(v\) in (2), for \(0\le t\le 2\eta v\), (6) gives
\[
 F(v+t)^2\ge e^{-t} F(v)^2-C_b e^{2b(v+t)}\ge\tfrac12 e^{-t}e^{2(\Theta-\delta)v}.
\]
Indeed the ratio of the subtracted term to the first lower bound is at most \(C_b\exp((-2(\Theta-b-\delta)+2\eta(1+2b))v)\), which tends to zero. Continuity forces one sign throughout this interval, and
\[
 |f(v+t)|\ge 2^{-1/2}\exp(-\delta v-(\Theta+1/2)t).              \tag{7}
\]

## A Gaussian average rules out the one-sign interval

Let \(W\) be real Gaussian with mean \(v_0=v+\eta v\) and variance \(K=\eta v/14\). The probability of falling outside \([v,v+2\eta v]\) is at most \(2e^{-7\eta v}\). On \(|W-v_0|\le\sqrt K\), estimate (7) gives \(|f(W)|\ge e^{-2\eta v}\) for all sufficiently large \(v\), since \(\Theta+1/2\le 3/2\) and \(\delta<\eta/8\). This central event has fixed positive probability. All remaining contributions inside the interval have the same sign and \(f\) is globally bounded. Hence
\[
                         |\mathbb E f(W)|\gg e^{-2\eta v}.         \tag{8}
\]

Every nontrivial zero of zeta has \(|\Im\rho|>14\). Applying the Gaussian exponential moment to (4) gives instead
\[
 |\mathbb E f(W)|\le \sum_\rho |\Gamma(\rho)|
   e^{(\Re\rho-\Theta)v_0+((\Re\rho-\Theta)^2-(\Im\rho)^2)K/2}
      +O(e^{-\Theta v_0+\Theta^2K/2})
     \ll e^{-195\eta v/28}+e^{-v/3} .                            \tag{9}
\]
Termwise integration is justified by \(\sum|\Gamma(\rho)|<\infty\) and the absolute majorant \(\max(1,e^{-\Theta W})\) for the exponentials before Gaussian integration. This contradicts (8). Only a fixed low-lying zero exclusion was needed. [First zeta zeros and verified zero count](https://arxiv.org/abs/2004.09765)

Consequently neither positive nor negative part is \(O(x^{2b})\) for any \(0<b<\Theta\). This proves the lower bounds in (1). For \(1/2<\Theta<1\), Goldston and Suriajaya's Theorem 6, equation (33), gives \(|B(N)|\ll N^{2\Theta}\log^5N\). For \(\Theta=1/2\) use their Theorem 4, and for \(\Theta=1\) ordinary Chebyshev bounds give \(\sum_{n\le N}|a_n|\ll N\). These estimates give the upper bounds in (1). The one-sided hypotheses are estimates still to be proved for the actual primes at exponent one. [Goldston–Suriajaya, Theorems 4 and 6](https://arxiv.org/abs/2110.14250)
