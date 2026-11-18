# Robin's inequality on least common multiples in short power ranges

**Proposed dichotomy.** Write $m_x=\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)$ and
$$
 B(x)=\log\frac{\sigma(m_x)}{e^{\gamma_E} m_x\log\log m_x}.
$$
Under RH one has
$$
 \limsup_{x\to\infty}\sqrt x\log x\,B(x)=1+\gamma_E-\log(4\pi)<0 .
$$
If RH fails, put $\Theta=\sup_\rho\Re\rho$. For every $1/2<c<\Theta$, every $0<\eta<1$, and **every sufficiently large** $Y$, there is an $x\in[Y^{1-\eta},Y]$ with $B(x)>x^{c-1}$. In particular RH follows if some fixed $\eta>0$ has arbitrarily large such intervals on which all these least common multiples satisfy Robin's inequality. The scale $x$ here is the largest index in the least common multiple and $\log m_x=\psi(x)\sim x$.

## An explicit arithmetic comparison

Use $K,J,R,M$ from the [tangent identity](robin-tangent-nov18.md) and the [integrated explicit formula](robin-finite-horizon-nov18.md). Thus $K$ uses $\vartheta(t)-t$, $J$ uses $\psi(t)-t$, $R$ is the nonnegative omitted prime-power correction in the logarithm of the Mertens product $M(x)$, and $s_x=1/(x\log x)$. For $p\le x$ the exponents in $m_x$ are $a_p=\lfloor\log x/\log p\rfloor$. With $D(x)=-\sum_{p\le x}\log(1-p^{-(a_p+1)})$ the identity gives
$$
 B(x)=-K(x)-R(x)-D(x)-s_x(\psi(x)-\vartheta(x))+Q(x)
$$
where
$$
 Q(x)=\log\log x+s_x(\psi(x)-x)-\log\log\psi(x)\ge0
$$
by concavity. Unconditionally $R(x)=O(1/x)$, $\psi(x)-\vartheta(x)=O(\sqrt x)$ and $-K(x)\ge-J(x)$. Also $D(x)=O(1/(\sqrt x\log x))$: primes up to $\sqrt x$ each cost $O(1/x)$, and larger primes contribute $O(\sum_{p>\sqrt x}p^{-2})$. This proves $B(x)\ge-J(x)-O(1/(\sqrt x\log x))$.

In fact $D(x)\sim 2/(\sqrt x\log x)$. For $p\le x^{1/3}$ the preceding simple bound costs $O(x^{-2/3})$. For $x^{1/3}<p\le\sqrt x$ one has $a_p=2$, and summing $O(p^{-3})$ costs $O(x^{-2/3})$. The leading term is $\sum_{\sqrt x<p\le x}p^{-2}$ by expansion of the logarithm, and partial summation of the prime number theorem gives its stated asymptotic.

Under RH, $Q(x)=O(x^{-1}\log^3 x)$ by Taylor's theorem and the von Koch bound. The square primes give $\psi(x)-\vartheta(x)\sim\sqrt x$ unconditionally, hence $\sqrt x\log x\,(J(x)-K(x))\to2$ by direct integration of the defining kernel. In the integrated zero formula, each $\sqrt x\log x\,F_\rho(x)/\rho$ equals $e^{i\gamma\log x}/[\rho(1-\rho)]+o(1)$ under RH, with the sum of the errors $o(1)$ by dominated convergence using the summable reciprocal-square ordinates. The archimedean remainder tends to zero on this scale. Consequently
$$
 \sqrt x\log x\, B(x)=-1+\sum_\rho e^{i\gamma\log x}/|\rho|^2 +o(1).
$$
The coefficients are positive and summable with total $2+\gamma_E-\log(4\pi)$. Simultaneous recurrence of finitely many phases, then passage through the absolutely convergent tail, attains this total as a limsup. This use of recurrence follows the argument of Nicolas for the primorial totient ratio; no priority claim is made for the least-common-multiple specialization. [Nicolas, Theorem 1.1 and its proof](https://arxiv.org/abs/1202.0729)

## Every power range if there is an off-line zero

Fix $c,\eta$ as in the claim and a zero $\rho_0$ with $\Re\rho_0>c$. Choose $0<d<\eta/8$ sufficiently small that $c(1+d)<\Re\rho_0$. For small $\epsilon>0$, to be fixed, average $Z(u)=-e^u J(e^u)$ against the Gaussian of mean $t$ and variance $2\epsilon t$, restricted to $|u-t|\le dt$ without renormalizing. The integrated explicit formula gives, on this support as $t\to\infty$,
$$
 Z(u)=\sum_\rho\frac1\rho\int_0^\infty\frac{1+w}{1-\rho+w}e^{(\rho-w)u}\,dw+O(1/u).
$$
The sum includes both signs and all multiplicities. The $O(1/u)$ is the constant and trivial-zero integral. For $w\ge1$, use $\Re\rho\le1$, $u\ge(1-d)t$ and $|1-\rho+w|\ge|1-\rho|$. The entire contribution from this range is $O(1/t)$ since $\sum1/(|\rho||1-\rho|)<\infty$.

For $0\le w\le1$, $|\Re(\rho-w)|\le1$. Completing the real Gaussian square shows the cost of extending the integral in $u$ to the full line is at most $2\exp(t[1+\epsilon-(d-2\epsilon)^2/(4\epsilon)])$ per term before its integrable absolute coefficient, provided $2\epsilon<d$. Take $\epsilon$ small enough that this exponent is negative and $\Re(\rho_0+\epsilon\rho_0^2)>c(1+d)$. Full Gaussian integration then gives the exponential
$$
 \exp\{t[\rho+\epsilon\rho^2-(1+2\epsilon\rho)w+\epsilon w^2]\}.
$$
The maximal real part $A=\max_\rho\Re(\rho+\epsilon\rho^2)$ exists and has a gap to the next smaller value, because $-\epsilon\gamma^2\to-\infty$. The $w$-dependent real factor is at most $e^{-(1-\epsilon)tw}$. The nonmaximal terms are therefore $O(e^{(A-\kappa)t}/t)$ for some $\kappa>0$. For each of the finitely many maximizing terms endpoint Laplace integration at $w=0$ (or dominated convergence after $w=v/t$) gives the average of $Z$ as
$$
 \frac{e^{At}}t\left[
 \sum_{\Re(\rho+\epsilon\rho^2)=A}
 \frac{e^{it\Im(\rho+\epsilon\rho^2)}}{\rho(1-\rho)(1+2\epsilon\rho)}
 +o(1)\right].
$$
The finite sum is real, has zero mean and is nonzero. Indeed $z\mapsto z+\epsilon z^2$ is injective in the right half-plane, and no image has zero imaginary part; equal zeros contribute multiplicity with the same coefficient. A positive value bounded away from zero recurs with bounded gaps by compact torus rotation. Thus within bounded distance of $(1-\eta/2)\log Y$ there is a center $t$ with the displayed average $\gg e^{At}/t$ for every sufficiently large $Y$.

Since the weight is positive and has mass at most one, some $u$ in its support satisfies $Z(u)\gg e^{At}/t$. The support lies within $[(1-\eta)\log Y,\log Y]$ for large $Y$. By $A>c(1+d)$ and $u\le(1+d)t$, the lower bound for $e^{-u}Z(u)=-J(e^u)$ exceeds $2e^{(c-1)u}$ eventually. The unconditional arithmetic comparison above gives $B(e^u)>e^{(c-1)u}$ there, as claimed. This proof does not require a rightmost zeta zero.
