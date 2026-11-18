# Coercivity of the full Weil form on the window of half-width 3/2

**Status.** Proposed finite-window theorem for review. This argument uses the published Platt–Trudgian verification through height $T_0=3\,000\,175\,332\,800$, the classical explicit formula, and elementary bounds. It derives a lower bound for every compact smooth complex test on the given interval. It does not certify positivity at growing radii. The imported zero verification is computational. There is no numerical minimization over the continuum of tests here. [Platt–Trudgian](https://arxiv.org/pdf/2004.09765) · [Observatory's bounded-window question](https://github.com/GettysburgResearch/riemann/blob/2dbadaef2014cbebd1881b5ce261575e14f4edb7/research/exploratory/riemann-observatory/frontiers/unsolved_questions.md)

## Statement and normalization

Let $L=3/2$, let $m=2^{29}$, and use $\widehat g(z)=\int g(u)e^{izu}\,du$ and $\rho=1/2+iz$ for the zeta zeros, counted with multiplicity. For every $g\in C_c^\infty(-L,L)$,
$$
 W(g)=\sum_z\widehat g(z)\overline{\widehat g(\bar z)}
 \ \ge\ \tfrac12\,2100^{-2m}\,\|g\|_2^2.
$$
At this radius the autocorrelation includes the primes through 19. The lower constant is deliberately small. The construction splits the form into a passband governed by the verified real ordinates and a complement with a positive arithmetic multiplier at high frequency. A finite-difference estimate gives the complement a lower floor on all supported tests.

## 1. Arithmetic side at the slightly enlarged radius

Write $R=128m$ and $\tau=6m/R=3/64$. For all tests supported in $[-L-\tau,L+\tau]$ use the same symbol
$$
 w(t)=\Re\psi(1/4+it/2)-\log\pi
 -2\Re\sum_{2\le n<23}\Lambda(n)n^{-1/2-it}.
$$
Since $e^{2(L+\tau)}<23$ and in fact exceeds 22, the usual explicit formula is
$$
 W(g)=2\Re\!\left(\widehat g(i/2)\overline{\widehat g(-i/2)}\right)
   +{1\over2\pi}\int_{\mathbb R}w(t)|\widehat g(t)|^2dt .
 \tag{1}
$$
Including all $n<23$ in this common symbol remains exact on any smaller support. Terms beyond a test's autocorrelation support have zero integral.

We use $w(t)\ge1$ for $|t|\ge10^7$ and $w(t)\ge-20$ everywhere. For the prime sum, upper bounds for $2\sum_{p^k<23}\log p/\sqrt{p^k}$ grouped by $p=2,3,5,7,11,13,17,19$ are respectively $2.52,2.01,1.45,1.48,1.45,1.43,1.38,1.36$, summing to less than $13.1$. The series for $\psi$ gives $\Re\psi(1/4+iy)\ge\psi(1/4)=-\gamma_E-\pi/2-3\log2$. Euler summation for the digamma series gives, for $s=1/4+iy$, $y\ne0$,
$$
 |\psi(s)-\log s|\le (2|s|)^{-1}+\tfrac12\int_0^\infty |v+s|^{-2}dv
 \le (1/2+\pi/4)/|y|.
$$
These inequalities imply both symbol bounds (in particular $\log(10^7/(2\pi))>14.27$).

## 2. A flat passband with a finite support cost

Put $\operatorname{sinc}u=\sin(u)/u$ with its removable value, $y(z)=\operatorname{sinc}^2(z/R)$ and
$$
 P(z)=\sum_{j=0}^{m-1}{3m-1\choose j}(1-y(z))^j y(z)^{3m-1-j}.
$$
This even real-entire multiplier has exponential type less than $\tau$. On the real axis $0\le y,P\le1$. There $P$ is the probability that a binomial random variable with $3m-1$ trials of success probability $1-y$ has fewer than $m$ successes. In particular
$$
 (1-y)^m\le1-P^2\le 2^{3m+1}(1-y)^m.
 \tag{2}
$$
The lower bound uses the event that the first $m$ trials succeed. For the upper bound sum the terms for $j\ge m$ and use $1+P\le2$. By the compact interval transform of sinc, multiplication by $P$ convolves with a finite signed measure supported in $[-\tau,\tau]$. Thus $g_P$ defined by $\widehat{g_P}=P\widehat g$ is smooth and supported in $[-L-\tau,L+\tau]$, and (1) applies to it.

For real $u$,
$$
 \tfrac14|1-e^{iu}|^2\le1-\operatorname{sinc}^2 u\le u^2/3.
 \tag{3}
$$
For the left inequality use $\operatorname{sinc}u=\operatorname{sinc}(u/2)\cos(u/2)$. For the right one use $1-\cos v\le v^2/2$ with $v=u(U-V)$ for independent uniforms $U,V$ on $[-1,1]$.

## 3. A lower bound for the full complement

Put $F=\widehat g$ and $I=(2\pi)^{-1}\int(1-P^2)|F|^2$. Let $\Delta f(x)=f(x)-f(x-1/R)$. By (2), (3), and Plancherel,
$$ I\ge 4^{-m}\|\Delta^m g\|_2^2.$$
On $[-L,L]$ invert this difference by the finite sum
$$
 g(x)=\sum_{j=0}^{3R}{m+j-1\choose j}\,(\Delta^m g)(x-j/R).
$$
Indeed the infinite inverse series is locally finite on left-bounded support, and terms with $j>3R$ vanish on this interval. Taking norms and using the hockey-stick identity yields
$$
 \|g\|_2\le{3R+m\choose m}\|\Delta^m g\|_2
 \le [e(3R+m)/m]^m\|\Delta^m g\|_2.
$$
Since $2e(3R+m)/m=770e<2100$, this proves $I\ge2100^{-2m}\|g\|_2^2$. On $|t|\le10^7$, (2)–(3) give $1-P^2\le2\cdot4000^{-2m}$ because $\sqrt{8/3}\,10^7/R<1/4000$. Consequently the integral in (1) for the difference of forms satisfies
$$
 (2\pi)^{-1}\int w(t)(1-P(t)^2)|F(t)|^2dt
 \ge \big[2100^{-2m}-42\cdot4000^{-2m}\big]\|g\|_2^2.
 \tag{4}
$$

## 4. The two poles and all unverified ordinates

At $z=\pm i/2$, the power series for $\sinh v/v$ gives $|1-y(z)|\le R^{-2}$ and $|y(z)|\le1+R^{-2}$. The complementary binomial sum (a polynomial identity valid for complex arguments) gives $|1-P(z)|\le2^{3m}(1+R^{-2})^{3m}R^{-2m}\le2^{3m+1}R^{-2m}$. In particular $|1-P(i/2)\overline{P(-i/2)}|\le3\cdot2^{3m+1}R^{-2m}$. Cauchy–Schwarz gives $|F(z)|^2\le2L e^L\|g\|_2^2<14\|g\|_2^2$ on the entire zero strip and at the two poles. The possible pole loss in $W(g)-W(g_P)$ is thus at most $168\cdot 8^m R^{-2m}\|g\|_2^2$.

For $|\Re z|=t>T_0$ and $|\Im z|\le1/2$, put $q=(2R/t)^2<1/400$. Then $|y(z)|\le q$, by $|\sin(z/R)|\le e^{1/(2R)}<2$. The powers of $y$ in $P$ have degree at least $2m$. Hence
$$
 |P(z)|\le 2^{3m}(1+q)^m q^{2m}\le 2^{4m}(2R/t)^{4m}.
$$
The standard explicit Riemann–von Mangoldt estimate gives $N(u)\le u\log u$ for $u\ge100$. Applying it on $[2^jT_0,2^{j+1}T_0]$, and including negative ordinates, gives
$$
 \sum_{|\Re z|>T_0} |P(z)|^2
 \le 20 T_0\log(2T_0)\,2^{8m}(2R/T_0)^{8m}
 \le 20 T_0\log(2T_0)\,10^{-8m},
$$
because $T_0>40R$. All ordinates through $T_0$ are real by the imported verification and give nonnegative contributions to $W(g_P)$. The outside set is closed under conjugation. Cauchy–Schwarz, or pairing each term with its conjugate, bounds the absolute outside contribution by $\sum_{\rm outside}|P(z)F(z)|^2$. It is at most $10^{17}10^{-8m}\|g\|_2^2$.

Adding (4), the pole error, and this full exterior bound proves the result: for $m=2^{29}$ the sum $42\cdot4000^{-2m}+168\cdot8^mR^{-2m}+10^{17}10^{-8m}$ is less than $\tfrac12\,2100^{-2m}$. Each comparison is a scalar elementary inequality; no matrix eigenvalues or sampled test functions are used.

**Boundary.** The finite verified height is essential in this argument. Extending the window increases the prime contribution and the frequency at which the archimedean term dominates. This proof supplies no uniform all-window lower bound.
