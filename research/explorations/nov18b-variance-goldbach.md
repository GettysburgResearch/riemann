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

## An inequality at a specified scale and the abundance of both signs

Write \(P_\pm(Y)=\int_0^\infty B_\pm(x)e^{-x/Y}\,dx\). For \(X=e^v\), \(v\ge20R\), and \(R\ge1\), there is an absolute constant \(C\) such that
\[
 P_+(X)\ge XF(v)^2,\qquad
 XF(v)^2\le 2P_-(Xe^{2R})+C X^{1+2\Theta}e^{-10R}.              \tag{10}
\]
Thus a large prime exponential sum forces actual mass of each sign. The enlargement of the second scale and the exponential remainder are explicit.

The first inequality is (5). For the second, suppose \(P_-(Xe^{2R})<XF(v)^2/2\). Positivity makes \(P_+\) and \(P_-\) individually nondecreasing. At \(Y=Xe^t\), \(0\le t\le2R\), equation (5) gives
\[
 YF(v+t)^2=P_+(Y)-P_-(Y)\ge XF(v)^2/2.
\]
Consequently \(f\) retains its sign there and \(|f(v+t)|\ge2^{-1/2}|f(v)|e^{-(\Theta+1/2)t}\). Use mean \(v+R\) and variance \(R/14\) in the Gaussian comparison. The central probability is fixed, the exterior error is \(O(e^{-7R})\), and (4) gives spectral expectation \(O(e^{-195R/28}+e^{-v/3})\). More precisely its second summand is \(O(e^{-\Theta(v+R)+\Theta^2R/28})=O(e^{-10R})\) since \(v\ge20R\). Thus
\[
 |f(v)|\ll \exp\big((\Theta+1/2)(R+\sqrt{R/14})-195R/28\big)
            \ll e^{-5R}
\]
using \(R\ge1\) and \(\Theta\le1\). Squaring proves (10).

In fact both signs have the full integrated exponent
\[
 \limsup_{X\to\infty}\frac{\log(1+\sum_{n\le X}B_\pm(n))}{\log X}=1+2\Theta.       \tag{11}
\]
The published pointwise upper bounds above give the upper inequality. If for either sign \(\sum_{n\le X}B_\pm(n)\ll X^{1+2b}\) with \(0<b<\Theta\), partial summation gives \(P_\pm(Y)\ll Y^{1+2b}\) for \(Y\ge1\). For the positive sign use the first inequality of (10). For the negative sign set \(R=\eta\log X\), with \(0<\eta<1/20\) small enough that \((1+2b)(1+2\eta)<1+2\Theta\). Both terms on the right of (10) then have an exponent strictly below \(1+2\Theta\), contradicting (2).

For each \(\epsilon>0\) and each sign, infinitely many dyadic blocks \([X,2X)\) contain at least \(X^{1-\epsilon}\) integers with \(B_\pm(n)\ge n^{2\Theta-\epsilon}\). Indeed (11) supplies infinitely many dyadic blocks with sum at least \(X^{1+2\Theta-\delta}\) for every fixed \(\delta>0\), or geometric summation would contradict (11). Values below the proposed threshold contribute \(O_\epsilon(X^{1+2\Theta-\epsilon})\). The upper envelope \(B_\pm(n)\ll_\delta X^{2\Theta+\delta}\) on the block gives the count on taking \(0<2\delta<\epsilon\).

The large positive and negative sets can also be taken in a common window. For each \(0<\epsilon<1\) there are arbitrarily large \(X\) for which at least \(X^{1-\epsilon}\) integers of each sign exceed the respective threshold \(B_\pm(n)\ge n^{2\Theta-\epsilon}\) within \([X^{1-\epsilon},X^{1+\epsilon}]\). Choose \(0<\delta<\epsilon/20\) and a scale in (2). Use \(R=(\delta/4)\log X\) in (10). Both \(P_+(X)\) and \(P_-(X^{1+\delta/2})\) are \(\gg X^{1+2\Theta-2\delta}\). With the same upper envelope, the part below \(X^{1-3\delta}\) is \(O(X^{(1-3\delta)(1+2\Theta+\delta)})\), and the part above \(X^{1+2\delta}\) is negligible by exponential decay. Values below \(n^{2\Theta-\epsilon}\) in this window contribute \(O(X^{(1+2\delta)(1+2\Theta-\epsilon)})\). Each remaining value is \(O(X^{(1+2\delta)(2\Theta+\delta)})\). The choice of \(\delta\) proves the simultaneous count, with integer endpoints absorbed by enlarging the final window.

## Recurrence when a zero attains the supremum

Suppose at least one zeta zero has real part \(\Theta\). Then for constants \(C>1,c>0\) and every sufficiently large \(X\),
\[
   \int_X^{CX}B_+(y)\,dy\ge c X^{1+2\Theta},\qquad
   \int_X^{CX}B_-(y)\,dy\ge c X^{1+2\Theta}.                    \tag{12}
\]
This includes RH and a hypothetical attained edge to its right. The lower zeros may approach the edge. The constants in (12) are qualitative. In particular each sign exceeds \(c'X^{2\Theta}\) at \(\gg X/(\log X)^5\) distinct integers in every such interval, by the pointwise upper envelope with the fifth logarithmic power, after reducing \(c'\). On RH the third power suffices.

We first justify a uniform estimate permitting compact localization of the Laplace tests. For \(w\in C_c^\infty([1/2,2])\) and \(X\ge1\), some fixed integer \(J\) gives
\[
    |D_X[w]|\ll\|w\|_{C^J},\qquad
         D_X[w]=X^{-2\Theta}\int_0^\infty B(Xu)w(u)\,du.        \tag{13}
\]
For \(z=1+it\), apply the contour proof of (3) with the additional factor \(z^{-s}\). It gives
\[
    \left|\sum_{n\ge1}a_ne^{-zn/X}\right|\ll X^\Theta(1+|t|)^A
\]
for some absolute \(A\). In both the zero sum and the final contour integral the exponential decay rate in the spectral ordinate is at least \(\pi/2-|\arg z|\gg(1+|t|)^{-1}\), so the zero count and polynomial growth on the final line give the asserted fixed power. Write \(W(y)=\int_y^\infty w(u)\,du\) for \(y\ge0\). The function \(e^yW(y)\) on the positive half-line extends smoothly to a compactly supported function of \(y\in\mathbb R\) with \(C^J\) norm \(\ll_J\|w\|_{C^J}\), since \(W\) is constant near zero. Fourier inversion of this extension expresses \(\int w(u)B(Xu)\,du=\sum_{m,n}a_ma_nW((m+n)/X)\) as the integral of its Fourier transform times the square of the complex exponential sum. Choose \(J>2A+2\). This proves (13). For \(X<1\), the same integral vanishes by support.

For the kernels \(K_c(u)=e^{-u/c}\) with fixed \(c>0\), a smooth nonnegative dyadic partition reduces (13) on \(u\asymp d\) to the same estimate at scale \(Xd\) with multiplier \(d^{1+2\Theta}\). On dyadic \(d\le1\) the resulting test has bounded seminorm. On \(d\ge1\) its seminorm is \(O_{c,J}((1+d)^Je^{-d/(2c)})\). Both tails are summable uniformly in \(X\). Consequently \(K_c\) and nonnegative differences \(K_{c'}-K_c\) for \(c'>c\) may be approximated in \(D_X\), uniformly in \(X\), by nonnegative tests supported on compact subsets of \((0,\infty)\). Positivity is preserved by multiplying the kernel by a partial sum of the nonnegative partition.

If (12) fails for the negative sign, choose \(Y_j\to\infty\) such that \(\int_{Y_j}^{e^{2j}Y_j} B_-(y)\,dy\le Y_j^{1+2\Theta}/j\), and center at \(X_j=e^jY_j\). For every nonnegative compact test \(w\) on \((0,\infty)\) this gives \(\liminf_j D_{X_j}[w]\ge0\). Pass to a subsequence along which all phases \(e^{i\gamma\log X_j}\) of zeros on the edge converge. By (3) and absolute summability, the translates \(f(\log X_j+t)\) converge on every fixed compact to a real uniformly almost-periodic function
\[
     P(t)=-\sum_{\rho=\Theta+i\gamma}m_\rho\Gamma(\rho)z_\gamma e^{i\gamma t},\qquad |z_\gamma|=1,
\]
where this sum lists distinct zeros and \(m_\rho\) is their multiplicity. The terms strictly below the edge vanish by dominated convergence. Uniqueness of a Fourier coefficient shows that \(P\) is nonzero, and it has mean zero since no zero has ordinate zero. It has both signs, since a real uniformly almost-periodic function that is positive somewhere and nonnegative everywhere has positive mean by recurrence. It therefore has a zero after a point where it is nonzero, by continuity and recurrence.

By (5), \(D_{X_j}[K_c]=c^{1+2\Theta}f(\log X_j+\log c)^2\). The compact approximation and \(\liminf D_{X_j}[K_{c'}-K_c]\ge0\) therefore imply that \(c^{1+2\Theta}P(\log c)^2\) is nondecreasing for \(c>0\), impossible at that later zero. For a failure of the positive sign the argument instead gives \(\limsup D_{X_j}[K_c]\le0\) for each \(c>0\), which would force \(P=0\). Taking the larger interval factor and the smaller positive constant gives (12) jointly.
