# A bandlimited tangent average for Robin's inequality

**Proposed finite theorem.** Every integer $5040<n\le \exp(1.5\cdot 10^{48})$ satisfies $\sigma(n)<e^{\gamma_E}n\log\log n$. This combines the earlier [finite Robin argument](robin-smoothed-nov18.md) with the following new upper-range estimate. It requires the published verified zero height $H=3\cdot10^{12}$ and explicit estimates for $\vartheta$. It does not require a high-zero density estimate. No claim of historical priority is made.

Put $y=\log n$, $L=\log y$. It suffices to cover $10^{38}\le y\le1.5\cdot10^{48}$ since the earlier argument extends from the published low-range result beyond the lower endpoint. As in the [arbitrary-integer tangent inequality](robin-tangent-nov18.md), average over $v=y e^U$ with a positive probability law. We use the notation and exact inequalities (1)–(8) in [the Gaussian calculation](robin-smoothed-nov18.md). The choice of probability law and the all-range prime estimate below are different.

## An average that suppresses all unverified ordinates

With unitary Fourier normalization let $f$ have Fourier transform $\sqrt{2/H}\cos(\pi\xi/H)$ on $[-H/2,H/2]$ and zero elsewhere. Then $k=|f|^2$ is a probability density. Set $b=\pi/H$. Direct inversion and Plancherel give
$$
 k(u)=\frac{4 b^2}{\pi H}\frac{\cos^2(Hu/2)}{(b^2-u^2)^2},
 \qquad \int u^2 k(u)du=b^2.
$$
Removable values are understood. The full characteristic function vanishes for $|\gamma|>H$ since it is the autocorrelation of the prescribed Fourier transform. Its first derivative vanishes there too. Fix $a=10^{-4}$ and condition $k$ to $|u|\le a$, obtaining the law of $U$. Since $a>2b$, we have $k(u)\le23/(H^3u^4)$ for $|u|>a$. The discarded mass is at most $\tau=16/(Ha)^3$ and its first absolute moment is at most $23/(H^3a^2)$. Hence $\mathbb E U^2\le V=b^2/(1-\tau)$.

For $-2\le h\le0$, $|\gamma|>H$, Taylor's formula bounds $|e^{hu}-1-hu|\le2e^{2a}u^2$ on the retained interval. The constant and linear terms against $e^{i\gamma u}$ have zero integral for the unconditioned kernel. Restoring just their two discarded tails gives the uniform bound
$$
 |\mathbb E e^{(h+i\gamma)U}|\le \varepsilon
 =\frac{\tau+46/(H^3a^2)+2 e^{2a} b^2}{1-\tau}<3\cdot10^{-24}.
$$
This argument controls the nonreal frequencies of hypothetical off-line zeros without evaluating an untruncated Laplace transform at those points.

## Paying the tangent cost

In the cited tangent calculation, the curvature term in (2) uses $V$ in place of the Gaussian variance. Its proof only uses support, the second moment, and the explicit derivative of the tangent penalty. Equations (4) and (6) apply with the present $a$ and $\varepsilon$: the latter enters only for $w\in[0,1]$ in the Laplace integral (3), where $-2\le\beta-1-w\le0$. Above $w=1$ the support bound suffices. The sum of $1/(|\rho||1-\rho|)$ over signed high ordinates is below $3.1\cdot10^{-12}$ by the earlier Lehman-tail calculation. This covers every unverified zero.

For the square primes we use $|\vartheta(t)-t|\le0.0244t/\log^3t$ on $t\ge e^{30}$, the $k=3$, $X_0=X_1=e^{30}$ case of Broadbent–Kadiri–Lumley–Ng–Wilk Theorem 1. Thus a relative error $\eta=10^{-6}$ suffices throughout $t\ge\sqrt{v_0}$ with $v_0=10^{38}e^{-a}$. Combining it with the elementary $\vartheta(t)\le2t$ bound on the higher powers gives
$$
 \psi(t)-\vartheta(t)\le P\sqrt t\quad(t\ge v_0),\qquad
 P=1+\eta+2v_0^{-1/6}+2(\log v_0)v_0^{-1/4}/\log2 .
$$
Both higher-power ratios decrease in this range. Consequently the prime-power term in (7) is bounded by $2P e^{a/2}L(1+1/(L-a))/(L-a)$ with no upper endpoint. In the cost lower bound (8) take the prime interval $(q,10000q]$, $q=\sqrt{2v}$, inside $(q,v/2]$. The same all-range estimate supplies the required $\eta$ at both endpoints and throughout the partial summation integral. [Broadbent et al., Theorem 1 and the paragraph before Table 5](https://arxiv.org/pdf/2002.11068)

Using $L\ge\log(10^{38})$ in each decreasing factor and $\sqrt y\le\sqrt{1.5\cdot10^{48}}$ for the increasing terms, the scaled total of curvature, both zero bands, archimedean contribution and prime powers is less than $2.750$. The scaled exponent cost exceeds $2.774$. These are strict outward comparisons for the full continuous interval. The script evaluates the endpoint formulas in 144-bit Arb arithmetic, obtaining respectively $2.7497898819253$ and $2.7740896460101$ to the shown precision. The weights are positive, so the averaged upper bound applies to each individual integer. This proves the proposed range. [Endpoint and tail checker](check_robin_bandlimited_nov18.py)
