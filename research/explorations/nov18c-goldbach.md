# What the exact divisor identity contributes to the centered Goldbach problem

**Status.** Proposed deformation theorem. Under the strip hypothesis $\Theta<9/10$, one positive integral Euler product on the ordinary primes can remove every hypothetical off-line zero in a half-plane extending strictly left of $1/2$. It retains the ordinary critical-line zeros with their multiplicities and matches any prescribed finite number of Laurent coefficients at $1$. The construction changes prime multiplicities. The ordinary von Mangoldt function continues to satisfy its divisor identity at every integer.

Write $a(n)=\Lambda(n)-1$ and $B_f(x)=\sum_{j+k\le x}f(j)f(k)$. The [one-sided Goldbach criterion](nov18b-goldbach-local.md) would follow from a sufficiently strong upper bound for the negative mass of $B_a$. A candidate source of this cancellation is the exact identity $\sum_{d\mid n}\Lambda(d)=\log n$. We determine how accurately its averaged versions can be preserved while changing the multiplicity of a hypothetical off-line zero.

## An explicit comparison on all the ordinary primes

Fix $\rho=\beta+i\gamma$ with $1/2<\beta<1$ and $\gamma\ne0$. For all sufficiently large primes take the local factors of
\[
 Z(s)=\frac{\zeta(s)}{\zeta(s+1-\rho)\zeta(s+1-\bar\rho)}.
\]
Retain the ordinary zeta factors at the remaining finitely many primes. At a large prime the coefficient of $p^{-s}$ is $1-2\Re(p^{\rho-1})>0$, and every higher coefficient is $|1-p^{\rho-1}|^2>0$. The prime-power weights of $-Z'/Z$ are $\Lambda(n)(1-2\Re(n^{\rho-1}))$ there. The factor creates one extra zero at $\rho$, counted with multiplicity, since $\zeta(1+2i\gamma)$ is finite and nonzero and the finite restoration factors are regular and nonzero there.

On $[X,2X]$ all prime-power weights have relative change $O(X^{\beta-1})$, including the unchanged small-prime powers. Every fixed product of these weights on that interval, and every nonnegative weighted sum of those products, has the same relative accuracy wherever the original sum is positive. For a residue class modulo $q$ the cumulative absolute change below $X$ is $O_\beta(\log(2X)(1+X^\beta/q))$ by summing the decreasing majorant $n^{\beta-1}$. Thus every level-of-distribution upper bound with error $X/(\log X)^A$, up to $q\le X^\vartheta$ for fixed $\vartheta<1$, transfers from the primes. This is an implication between distribution statements. The extra zero does not follow from any distribution conjecture.

## A conditional deformation which also passes smooth divisor tests

Suppose now that $\rho=\beta+i\gamma$ is an actual nontrivial zero of ordinary zeta of multiplicity $m$, with $1/2<\beta<9/10$ and $\gamma>0$. This interval covers the hypothetical right-hand zeros under the [strip used in the preceding work](nov18b-quasi-rh-source.md). Set
\[
 \nu=\max\{\beta-2/5,\ \beta/2\}<1/2 .
\]
For any fixed integer $J\ge1$, $0<\eta<1-\beta$ and $\varepsilon>0$ there are marks $e_p\in\{-1,0,1\}$ on the ordinary primes with the following properties. Set $h(p^j)=e_p\log p$ for $j\ge1$ and $h(n)=0$ elsewhere. Define
\[
 T(n)=\sum_{d\mid n}h(d)=\sum_p e_p v_p(n)\log p,\qquad
 Z_\pm(s)=\prod_p(1-p^{-s})^{-(1\pm e_p)} .
\]

1. The Euler products have nonnegative integer coefficients bounded by the divisor function. In $\Re s>\nu$ they continue meromorphically. There $Z_+$ removes both $\rho,\bar\rho$ with their full multiplicities, and $Z_-$ doubles those multiplicities. All other zeros and poles of zeta in that half-plane retain their orders. Both products satisfy $Z_\pm(s)-\zeta(s)=O((s-1)^J)$ near $1$, so their pole residue and their first $J$ regular Laurent coefficients agree exactly with those of ordinary zeta.
2. For every fixed $W\in C_c^\infty(0,\infty)$ and every $\sigma>\nu$,
\[
                  \sum_n T(n)W(n/X)=O_{W,\sigma}(X^\sigma).
\]
The divisor identity for $\Lambda\pm h$ therefore agrees with the ordinary one to a power strictly better than $X^{1/2}$ in each such smooth test. Uniformly over all $X\ge1$,
\[
              X^{-1}\sum_{n\le X}\big(e^{\eta|T(n)|}-1\big)<\varepsilon.
\]
3. For every fixed $\vartheta<1$ and $A>0$, the cumulative changes of the prime-power weights, maximized over initial segments and reduced residue classes and summed over $q\le X^\vartheta$, are $o(X/(\log X)^A)$. Any fixed $k$-fold translated von Mangoldt correlation on $n\le X$, with all translates in $[1,2X]$, changes by $O_k(X^\beta(\log(2X))^{k-1})$.
4. The centered quadratic forms have the exact difference
\[
 B_{a+h}(X)+B_{a-h}(X)-2B_a(X)=2B_h(X).
\]
For each $\delta>0$ the right-hand source has the asymptotic
\[
 B_h(X)=m^2\sum_{u,v\in\{\rho,\bar\rho\}}
    \frac{\Gamma(u)\Gamma(v)}{\Gamma(1+u+v)}X^{u+v}
    +O_\delta(X^{\beta+\nu+\delta}).
\]
Its positive and negative parts each have integral $\gg X^{1+2\beta}$ on every sufficiently late interval $[X,e^{\pi/\gamma}X]$. This is a statement about the exact quadratic difference. The cross term with the true primes need not be small in either individual perturbed sum.

### Constructing the marks

Start beyond an arbitrarily large $P_0$. Partition the positive real line there into successive blocks $[y,y+y^{3/5})$. The classical short-interval prime number theorem gives $\sum_{p\in I}\log p\asymp y^{3/5}$ uniformly in these blocks, since $3/5>7/12$. For each prime in the block put
\[
 u_p=\frac{m\int_I(t^{\rho-1}+t^{\bar\rho-1})\,dt}
               {\sum_{p\in I}\log p}.
\]
Thus $|u_p|\ll_{m,\rho}p^{\beta-1}<1$. The signed mass $\sum u_p\log p$ is exact on complete blocks. On an incomplete block the discrepancy is $O(y^{\beta-1+3/5})$, using the total prime weight bound on the whole block. Taking $u_p=0$ below $P_0$ costs only a fixed constant in the cumulative asymptotic. [Huxley's short-interval theorem](https://doi.org/10.1007/BF01418933)

Independently set $e_p=\operatorname{sgn}(u_p)$ with probability $|u_p|$ and $e_p=0$ otherwise. For each dyadic $L$, each $q\le L$, each class $a\bmod q$ and each integer $x\le L$, the expected absolute marked count in that class below $x$ is $O(1+L^\beta/q)$ by the decreasing majorant. Bernstein's inequality and a union bound over at most $L^3$ choices show, almost surely on every sufficiently large dyadic scale, that both the signed and absolute counts differ from their expectations by
\[
          O\big(\log(2L)+\sqrt{(1+L^\beta/q)\log(2L)}\big).
\]
Indeed the implicit constant can make the failure probability $O(L^{-2})$ after the union bound. Partial summation costs at most $O(\log(2L))$ for the weights $\log p$. At $q=1$ this gives signed rounding error $O_\delta(L^{\beta/2+\delta})$ for every $\delta>0$. The total absolute weighted count up to $x$ is $O(x^\beta)$ by partial summation with the ordinary Chebyshev bound for its expectation. The contribution of all higher prime powers is $O(x^{\beta/2}\log(2x))$, by summing this last estimate at $x^{1/j}$ for $j\ge2$.

We can choose such an outcome with
\[
 \sum_{e_p\ne0}\frac{(1+\log p)^J}{p}\ll_J P_0^{\beta-1}(1+\log P_0)^J,\qquad
 \sum_{e_p\ne0}p^{\eta-1}\ll_{\eta}P_0^{\beta+\eta-1}.
\]
Their expectations satisfy these bounds by partial summation with $|u_p|\ll p^{\beta-1}$. Markov's inequality gives simultaneous success with positive probability, while the preceding eventual estimates have probability one. Here $J\ge1$ is any fixed integer chosen in advance.

We next impose exact agreement of the prescribed Laurent coefficients. Put $\ell_p(s)=-\log(1-p^{-s})$ in a neighborhood of $s=1$. We want the first $J+1$ raw derivatives of $\sum e_p\ell_p$, of orders $0,\ldots,J$ at $1$, to vanish. They converge absolutely there. At a scale $Y$ use instead the invertible triangular change of coordinates
\[
 v_j^Y(p)= [(-\partial_s-\log Y)^j\ell_p(s)]_{s=1}
     =\sum_{k\ge1}\frac{(k\log p-\log Y)^j}{k p^k},\qquad 0\le j\le J.
\]
On $Y\le p\le2Y$ this column equals $p^{-1}((\log(p/Y))^j)_{j=0}^J$ with entrywise error $O_J((1+\log Y)^J/Y^2)$. Choose $J+1$ distinct centers in $(1,2)$ and narrow, disjoint fixed relative neighborhoods about them. In each corresponding prime band take $M$ fresh primes. The matrix of the $J+1$ column sums, each divided by the sum of $1/p$ in its band, is uniformly invertible for all large $Y$. Indeed it is an arbitrarily small fixed perturbation of the Vandermonde matrix at the logarithms of the centers. Each normalization is comparable to $M/Y$. Every band contains $\gg_J Y/\log Y$ unmarked primes: the ordinary prime number theorem gives a positive fixed total of $\log p/p$ there, while the total from the original marked primes is $o(1)$ as $P_0\to\infty$. For $J>1$ the latter also follows by dividing the first displayed bound by the relevant logarithmic power, or directly from its decay.

Let $r_Y$ be the target correction in these coordinates. Taking $M=\lceil C_J(1+Y\|r_Y\|_\infty)\rceil$ allows one real coefficient in $[-1,1]$ per whole band to solve the system, by the inverse bound. Fix these signs and allow a separate magnitude in $[0,1]$ per selected prime. A vertex of the resulting nonempty bounded polytope has at most $J+1$ fractional magnitudes, since otherwise the corresponding columns have linear dependence. Round those magnitudes down. The new marks are $\pm1$, and the remaining residual has every centered coordinate $O_J(1/Y)$.

Apply this successively at $Y=P_0,4P_0,4^2P_0,\ldots$; the bands from different stages are disjoint. At the first stage $\|r_{P_0}\|_\infty\ll_J P_0^{\beta-1}(1+\log P_0)^{2J}$ by the selected moment bound. Thus $M=o(P_0/\log P_0)$. At the next stages changing center from $Y$ to $4Y$ applies a fixed triangular matrix involving only $\log 4$, so each later $M$ is $O_J(1)$. In raw derivative coordinates the residual is $O_J((1+\log Y)^J/Y)$ and tends to zero. The correction has total $p^{\eta-1}$ cost $O_{J,\eta}(P_0^{\beta+\eta-1}(1+\log P_0)^{2J}+P_0^{\eta-1})=o(1)$. Beyond the finite first stage it adds at most $O_J((\log(2x))^2)$ to the weighted prime count below $x$. Because all corrected raw derivatives vanish, the convergent Euler perturbation has
\[
              \log(Z_+(s)/\zeta(s))=O((s-1)^{J+1})\quad(s\longrightarrow1).
\]
In particular its residue calibration is exact, and $\sum e_p\log p/(p-1)=0$. The corrected marks satisfy
\[
 \sum_{n\le x}h(n)=m(x^\rho/\rho+x^{\bar\rho}/\bar\rho)
                  +O_\delta((1+x)^{\nu+\delta}),\qquad
 \sum_{n\le x}|h(n)|\ll (1+x)^\beta .                                      \tag{1}
\]

### Checking the smooth tests, the distribution and the quadratic response

Write $H(s)=\sum_n h(n)n^{-s}$. Partial summation of (1) continues it to $\Re s>\nu$, with simple poles of residue $m$ precisely at $\rho,\bar\rho$. On each closed substrip away from these poles it grows at most linearly in $|s|$. The first-derivative calibration gives $H(1)=0$. In $\Re s>1$ we have $-(Z_+/\zeta)'/(Z_+/\zeta)=H$ and $Z_-/\zeta=(Z_+/\zeta)^{-1}$. Subtract the two principal parts of $H$ and integrate its holomorphic remainder in the simply connected half-plane. Up to a nowhere-zero holomorphic factor, $Z_+/\zeta=((s-\rho)(s-\bar\rho))^{-m}$ there. This proves the first assertion.

The Dirichlet series of $T$ is $\zeta(s)H(s)$. The actual zeros at $\rho,\bar\rho$ cancel both poles, while $H(1)=0$ cancels the zeta pole. Smooth Mellin inversion can therefore be moved to any line $\sigma>\nu$. Its rapid test decay absorbs the polynomial growth of the two factors. For the assertion about absolute pointwise errors, write $n_{\mathcal P}=\prod_{e_p\ne0}p^{v_p(n)}$. Since $e^{\eta|T(n)|}\le n_{\mathcal P}^\eta$, the nonnegative divisor expansion of the latter multiplicative function gives
\[
 X^{-1}\sum_{n\le X}(e^{\eta|T(n)|}-1)
 \le \prod_{e_p\ne0}\frac{1-1/p}{1-p^{\eta-1}}-1.
\]
Here each divisor contributes with frequency at most its reciprocal. The right side tends to zero with $P_0\to\infty$ by the estimates for the original and correcting marks. This proves assertion 2.

For primes, summing the expectation bound and the rounded count error for $q\le Q\le X$ with logarithmic weights costs
\[
 O\big((X^\beta+Q+X^{\beta/2}\sqrt Q)(\log(2X))^3\big).
\]
The final correction adds $O_{P_0}(Q(\log(2X))^2)$. For higher powers and reduced classes, handle each fixed $j\ge2$ by the elementary bound $O_{j,\delta}(q^\delta)$ for the number of invertible $j$th roots of a residue class modulo $q$. This follows from the cyclic groups for odd prime powers and the two cyclic factors at powers of two, followed by the divisor bound. Thus their total up to any fixed $j\le K$ is $O_{K,\delta}(X^\delta(Q+\sqrt X)(\log(2X))^2)$. The remaining powers have prime base at most $X^{1/(K+1)}$ and contribute $O(Q X^{1/(K+1)}(\log(2X))^2)$. For fixed $\vartheta<1$ choose $K$ large and $\delta$ small. The translate assertion follows by expanding a product difference one changed factor at a time, bounding all other factors by $2\log(2X)$ and using (1).

Finally insert the signed estimate in (1) into $\sum_{j\le X}h(j)\sum_{k\le X-j}h(k)$. Its inner error costs $O_\delta(X^{\beta+\nu+\delta})$ by the variation estimate. In each remaining term partial summation replaces $h(j)$ by the densities $m(j^{\rho-1}+j^{\bar\rho-1})\,dj$ with the same error, since $(X-t)^u$ has total variation $O_u(X^\beta)$. Integrating the two powers over the triangle gives exactly the displayed gamma quotient. The ratio of the oscillating amplitude to the positive constant term of the normalized main term is
\[
                  \frac{\Gamma(1+2\beta)}{|\Gamma(1+2\rho)|}>1.
\]
The strict inequality follows from the strict triangle inequality in the gamma integral when $\gamma\ne0$. One full period of $e^{2i\gamma\log X}$ contains intervals of positive log length where the profile is bounded away from zero with either sign. Choosing $0<\delta<\beta-\nu$ makes the error in the quadratic asymptotic lower order and gives the stated integral bounds.

The exact condition $T(n)=0$ for **all** integers would force $h=0$ by Möbius inversion. This calculation identifies a quantitative distinction: even arbitrarily small uniform exponential moments of $|T|$, all the smooth identities above and the listed prime distribution estimates admit a change in the zero's multiplicity. No estimate for the negative Goldbach mass of the true coefficients follows here.

## Theta inversion over a growing range

The modified prime system can start beyond any prescribed $P_0$. If $b_\pm(n)$ denotes the coefficient of $Z_\pm$, then $b_\pm(n)=1$ for all $n<P_0$, and $0\le b_\pm(n)\le d(n)$ at every integer. Write
\[
 \theta_\pm(t)=1+2\sum_{n\ge1} b_\pm(n)e^{-\pi n^2 t}.
\]
For each fixed $0<\delta<2$ there is $c_\delta>0$ such that
\[
 \sup_{P_0^{-2+\delta}\le t\le P_0^{2-\delta}}
 \left|\theta_\pm(t)-t^{-1/2}\theta_\pm(1/t)\right|
       \ll_\delta \exp(-c_\delta P_0^\delta).
\]
Indeed the differences from the ordinary theta series have support $n\ge P_0$ in both Gaussian sums. In each sum split off $\exp(-\pi P_0^2\min(t,1/t)/2)$, then bound the remaining Gaussian sum with $d(n)+1\ll 1+n$; the cost, including $t^{-1/2}$, is polynomial in $P_0$. The ordinary theta inversion is exact. Thus even this exponentially accurate symmetry on an expanding range can accompany the removal or doubling of a hypothetical zero. The standard exact global inversion with only a simple pole would recover the usual degree-one uniqueness issue; the estimate above imposes its stated finite range.

## Removing the entire off-line spectrum in a single Euler product

The construction extends to an arbitrary conjugation-invariant subset $\mathcal S$ of the ordinary nontrivial zeros, with their given multiplicities, under the single hypothesis $\Theta<b<9/10$. Take any such fixed $b$, put $\nu_b=\max(b-2/5,b/2)<1/2$, and impose any finite jet order $J$ as above. There is **one** pair of positive integral Euler products with the following properties.

* In $\Re s>\nu_b$, $Z_+$ removes the zero divisor of $\mathcal S$ with full multiplicity, $Z_-$ doubles it, and all other zeros and poles retain their orders. In particular, taking all off-line zeros yields a meromorphic $Z_+$ whose only zeros in the entire half-plane $\Re s>\nu_b$ are the ordinary critical-line zeros, with their original multiplicities. The pole at $1$ and the prescribed Laurent coefficients are the ordinary ones.
* The smoothed divisor bound holds for every $\sigma>\nu_b$. The exponential-moment estimate holds for any prescribed $0<\eta<1-b$ and arbitrarily small $\varepsilon$. The progression estimates, translated pattern estimates and theta estimate hold with $b$ replacing $\beta$ where needed. The explicit single-frequency formula for the quadratic response belongs to the single-pair construction.

Here is the simultaneous argument, including convergence when there are infinitely many off-line zeros arbitrarily close to the critical line. Take a real smooth function $\phi$ equal to zero on $(0,1]$ and to one on $[2,\infty)$, with $0\le\phi\le1$. For each distinct selected zero let $m_\rho$ denote its multiplicity, $P_\rho=P_0(1+|\Im\rho|)^A$, and set
\[
 g(t)=\sum_{\rho\in\mathcal S}m_\rho t^{\rho-1}\phi(t/P_\rho).
\]
This is real and locally a finite sum. Choose $A$ with $1/A<b-\Theta$. The ordinary zero count $N(T)\ll T\log(2+T)$, with multiplicity, gives $|g(t)|\ll_b t^{b-1}$ for $t\ge1$ with constants allowed to depend on $A$. The estimate is uniform over $P_0\ge2$.

In the prime blocks replace the preceding single-pair numerator by $\int_I g(t)dt$. The rounding, absolute-count and jet-calibration arguments use only the envelope, the exact full-block integrals and the bounded measure of an incomplete block. They give
\[
 \sum_{n\le x}h(n)=\int_1^x g(t)dt+O_\delta((1+x)^{\nu_b+\delta}),
 \qquad \sum_{n\le x}|h(n)|\ll (1+x)^b .
\]
Consequently $H(s)-\int_1^\infty g(t)t^{-s}dt$ continues holomorphically to $\Re s>\nu_b$ with at most linear vertical growth on closed substrips. The integral itself, initially absolutely convergent for $\Re s>b$, has continuation
\[
 M(s)=\sum_{\rho\in\mathcal S}m_\rho\,
       \frac{P_\rho^{\rho-s}}{s-\rho}
        \int_1^2 \phi'(u)u^{\rho-s}du .
\]
Termwise integration initially follows from the same zero-count majorant used for the envelope. Integration by parts gives the displayed term; its residue at $\rho$ is $m_\rho$. For $s$ on a compact set the last integral decreases faster than every power of $|\Im\rho-\Im s|$, by integration by parts in $\log u$. The factor $P_\rho^{\Re\rho-\Re s}$ grows at most polynomially in the ordinate on that compact set. The series is therefore normally convergent locally away from its stated poles. This argument does not require a density gap at $1/2$.

The function $\zeta(s)H(s)$ is holomorphic in $\Re s>\nu_b$, including at $1$ by the calibration. On bounded-width closed vertical substrips there it has polynomial growth. To verify uniformity at large height, separate the ordinates within one unit of $\Im s$. There are $O(\log(2+|\Im s|))$ with multiplicity. If $|s-\rho|\le1$, the ratio $\zeta(s)/(s-\rho)$ is bounded polynomially in the height by integrating $\zeta'$ along the segment from $\rho$, using the standard bounded-strip polynomial estimate for $\zeta'$. For $|s-\rho|>1$ the denominator is harmless. The remaining ordinates sum polynomially, combining the rapid decay in the difference of ordinates with the polynomial ordinate weight and the zero count. Smooth Mellin inversion proves the asserted divisor estimate.

Finally the integral of $-H(s)\,ds$ around any closed curve avoiding the poles is an integer multiple of $2\pi i$ by the residue theorem in the half-plane. Exponentiating its primitive therefore gives a single-valued meromorphic continuation of $Z_+/\zeta$. Its pole order at each selected zero in this half-plane is exactly the multiplicity there, and it has no other zeros or poles. This gives the full simultaneous removal, and inversion gives the simultaneous doubling. The resulting products have different prime multiplicities; the construction gives no transfer of their zero sets back to ordinary zeta.
