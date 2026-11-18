# The large-prime part of a native Newton step

**Status.** Proposed unconditional obstruction for the literal Möbius source. The scale-to-scale upper bound and RH remain open. This application uses classical prime number theorem estimates. No priority is claimed for smooth-number asymptotics.

**Scope and dependencies.** BNR26, §§0–4 of [the original proof](https://github.com/GettysburgResearch/riemann/blob/a1b4625f9775df1fdbd431b5198309a2fce9b038/standalone/2026-09-10-astra-balanced-newton/PROOF.md), supplies the identification of its output with the ordinary Möbius coefficients through the strict square endpoint. At [the later #848 head](https://github.com/GettysburgResearch/riemann/tree/7de75c02417d5d8db7eafb1ceba364380e72d16a/standalone/2026-09-19-newton-rough-core), RCB26 groups the *products inside the harmonic kernel*. Here the split acts on the *reconstructed output coefficients*. An obstruction for this split leaves the RCB26 estimates intact.

## Statement

Let integers $b\to\infty$, $Y=b-1$, $B=b^2-1$. Split $\mu=r+s$ on $1\le n\le B$, where $r(n)=\mu(n)$ if $n$ has a prime factor greater than $b$, and $r(n)=0$ otherwise. For a real sequence $a$ put

$$
 M_a(x)=\sum_{n\le x}a(n),\quad m_a(x)=\sum_{n\le x}a(n)/n,\quad
 u_a(N)=m_a(N)-M_a(N)/(N+1).
$$

The BNR26 norm squared and its associated inner product at an integer endpoint $N$ are

$$
 A_N(a)=\sum_{k=1}^N\frac{M_a(k)^2}{k(k+1)}+2(N+1)u_a(N)^2,\qquad
 \langle r,s\rangle_N=\tfrac12(A_N(r+s)-A_N(r)-A_N(s)).
$$

For every fixed $0<\delta<1$, uniformly over $b^{1+\delta}\le x\le B$, with $L=\log x$,

$$
 M_r(x)=\frac{x}{L^2}+O_\delta(x/L^3),\qquad
 m_r(x)=-\frac{1}{L}+O_\delta(L^{-2}).                         \tag{1}
$$

Both corresponding smooth-source values have the opposite main term. In particular

$$
 A_B(r)\sim A_B(s)\sim-\langle r,s\rangle_B\sim\frac{2B}{(\log B)^2}. \tag{2}
$$

The negative covariance already appears in the cumulative energy. On the terminal window $B/2\le k\le B$ the two separate squared norms before the balancing fee are each asymptotic to $B/(2\log^4 B)$, and the signed cross inner product on that window is asymptotic to its negative.

For every fixed $p\le2$ and $C>0$, both $A_B(r)$ and $A_B(s)$ eventually exceed $C(1+A_Y(\mu))^p$. Thus termwise bounds on these two actual output sectors cannot even give the quadratic recurrence. The exact signed interaction is indispensable at orders much larger than the entire desired output. This holds on every sufficiently large Newton stage.

## Proof

Use the classical zero-free-region consequences $M_\mu(t)\ll_K t/(\log(2t))^K$ and
$\pi(t)=\operatorname{li}(t)+O_K(t/(\log(2t))^K)$ for every fixed $K>0$ and $t\ge2$. For each fixed $j\ge0$,

$$
 D_j=\sum_{n\ge1}\frac{\mu(n)(\log n)^j}{n}
 =(-1)^j(1/\zeta)^{(j)}(1).
$$

The truncation error at $H\ge2$ is $O_{j,K}((\log H)^{-K})$ by partial summation with the bound on $M_\mu$. These convergent series have the asserted values by taking a real limit from $\sigma>1$ in the differentiated Dirichlet series. In particular $D_0=0$, $D_1=-1$, and $m_\mu(t)\ll_K(\log(2t))^{-K}$.

There is at most one prime factor $p>b$ of any $n\le B$, and $m=n/p<b<p$. Thus $\mu(pm)=-\mu(m)$, including squareful cofactors. With $T=x/b$,

$$
 M_r(x)=-\sum_{m\le T}\mu(m)[\pi(x/m)-\pi(b)],\qquad
 m_r(x)=-\sum_{m\le T}\frac{\mu(m)}m
                  \sum_{b<p\le x/m}\frac1p.                            \tag{3}
$$

The factor $\pi(b)M_\mu(T)$ is $O_{K,\delta}(xL^{-K})$ since $T\ge b^\delta$. Partial summation of the prime number theorem gives
$\sum_{b<p\le v}p^{-1}=\log(\log v/\log b)+O_K((\log b)^{-K})$ uniformly for $b\le v\le b^2$. Summing its error absolutely in (3) costs at most $1+\log T$. The same absolute loss handles the remainder in
$\pi(x/m)=(x/m)\sum_{i=1}^{J}(i-1)!/(\log(x/m))^i+O_J((x/m)L^{-J-1})$.
Here $\log(x/m)\ge\log b\ge L/2$.

All expansion and truncation operations below admit arbitrary fixed inverse-log precision. Set $H=\exp(\sqrt L)$, which is below $T$ eventually. For $H<m\le T$, each smooth multiplier just displayed, after dividing the first expression by $x$, has magnitude $O_J(1/m)$ and derivative $O_J(1/m^2)$ as a function of $m$. The reciprocal-prime logarithm is bounded because $\log(x/m)/\log b\in[1,2]$. Partial summation with the arbitrarily strong logarithmic bound on $M_\mu$ makes these tails $O_{K,J}(L^{-K})$ for each fixed $K$. On $m\le H$, expand in $v=\log m/L\le L^{-1/2}$. Taylor expansion through degree $h$ costs $O_{h,J}((1+\log H)L^{-(h+1)/2})$ after summation with weight $1/m$. Taking $h$ and $J$ sufficiently large relative to the requested order justifies replacing all resulting log moments by $D_j$.

Specifically, the terms through order $L^{-2}$ of $M_r(x)/x$ are
$-D_0/L-(D_1+D_0)/L^2$.
For $m_r(x)$, the multiplier inside the negative sum is
$\log(L/\log b)+\log(1-v)$, so its constant term disappears and its first surviving term gives $D_1/L$. This proves (1), and subtraction from the bounds on $M_\mu,m_\mu$ gives the smooth component.

For the total cumulative energy of $r$, indices $k<b^{3/2}$ contribute $O(b^{3/2})$ by $|M_r(k)|\le k$, and the rest contribute $O(B/\log^4 B)$ by (1). The same bounds hold for $s$. At $B$, (1) gives $u_r(B)=-1/\log B+O(1/\log^2 B)$ and $u_s(B)=+1/\log B+O(1/\log^2 B)$. Consequently the balancing fee supplies the leading term in (2). Polarization gives the covariance since the native source satisfies $A_N(\mu)\ll_K N/(\log(2N))^K$ for every fixed $K$ (split its energy sum at $\sqrt N$). The terminal-window statements follow directly by summing (1), using $\log k=\log B+O(1)$. The recurrence obstruction now follows from (2) and the same bound for the native input at $Y$, already at $p=2$.

## How far deterministic inverse-log subtraction goes

For each fixed integer $h\ge1$, the same expansion proves

$$
 m_r(x)=\sum_{j=1}^{h}\frac{D_j}{j L^j}+O_{h,\delta}(L^{-h-1}).       \tag{4}
$$

Infinitely many $D_j$ are nonzero. Otherwise the Taylor series of $1/\zeta(s)$ at $1$ would terminate and agree with a polynomial throughout $\Re s>1$ by the identity theorem. Its limit along the positive real axis is one, forcing that polynomial to be constant, contrary to $D_1=-1$. After subtracting any fixed truncation of (4), let $j$ be the first omitted nonzero order. Summing the squared reciprocal residual on $[B/2,B]$ still costs asymptotically $B D_j^2/(2j^2\log^{2j} B)$. All of these fixed truncations therefore leave an above-subpower cost on this source sector. This conclusion concerns the isolated reciprocal component and allows an exact paired compensation or an order increasing with the cutoff.

**Verification.** The displayed errors and endpoint conventions are derived analytically above. The remaining RH-facing problem is to estimate the joint compensated source to subquadratic precision. These asymptotics quantify one mandatory cancellation without establishing that estimate.

## An adaptive deterministic subtraction

Put $f(s)=1/\zeta(s)$ with its removable value at $s=1$, $a=14/25$, and let

$$
 {\cal C}(L)=\int_0^a e^{-Lt}\frac{f(1-t)}{t}\,dt,\qquad
 S_h(L)=\sum_{j=1}^h\frac{D_j}{jL^j}.
$$

The integral at the origin uses the limiting integrand $-1$. There is a uniform, purely deterministic estimate

$$
 |{\cal C}(L)-S_{\lfloor 13L/25\rfloor}(L)|\ll e^{-11L/20}\qquad(L\to\infty). \tag{5}
$$

Consequently the sum of the squared errors in (5) over $B/2\le k\le B$, with $L=\log k$, is $O(B^{-1/10})$. A growing subtraction can remove the entire deterministic series at a cost below the critical squared-energy scale.

Here is a self-contained disk estimate sufficient for (5). For $\sigma=\Re s>0$ the continuation formula gives

$$
 \frac{s-1}{s}\zeta(s)=1-(s-1)\int_1^\infty\{v\}v^{-s-1}\,dv.
$$

On every unit interval the increasing function $\{v\}$ has mean $1/2$ and is oppositely ordered to $v^{-\sigma-1}$. Their integrated product is at most half the integral of $v^{-\sigma-1}$, by integration of the pairwise difference inequality on that interval. Thus the integral has absolute value at most $1/(2\sigma)$. When $|s-1|<2/3$ we have $|s-1|<2\sigma$, proving nonvanishing of the normalized zeta throughout that disk. At $s=1$ its value is one. With $R=3/5$ Cauchy's estimate gives $f(1-t)=\sum_{j\ge1}c_jt^j$ and $|c_j|\le C R^{-j}$, $c_j=D_j/j!$.

For any integer $1\le h\le(13/25)L$, replacing the integrand by its degree $h$ Taylor truncation of the numerator costs at most

$$
 C R^{-h-1}\int_0^a e^{-Lt}t^h\,dt
 \le C\frac{h!}{(RL)^{h+1}}.
$$

Extending each resulting term through $t=\infty$ changes the sum by $O(e^{-aL}/L)$ uniformly in that range of $h$. Indeed for $t\ge a$ one has $t^{j-1}\le a^{j-1}\exp((j-1)(t-a)/a)$, and the geometric sum of $R^{-j}a^{j-1}$ is bounded since $a<R$. The full Laplace moments give $c_j(j-1)!/L^j=D_j/(jL^j)$. At $h=\lfloor\kappa L\rfloor$, $\kappa=13/25$, Stirling's estimate gives exponential rate $\kappa(1+\log(R/\kappa))>11/20$. Also $a>11/20$, proving (5).

### Accuracy for the actual large-prime sector

Using the classical de la Vallée Poussin error terms for $M_\mu(t)/t$ and $(\pi(t)-\operatorname{li}(t))/t$, both $O(\exp(-c\sqrt{\log t}))$ for $t\ge2$, one gets, uniformly over the range of (1),

$$
 m_r(x)-{\cal C}(\log x)=O_\delta\!\left(e^{-c_\delta\sqrt{\log x}}\right),
 \qquad c_\delta>0.                                                   \tag{6}
$$

For details, first replace the prime reciprocal sum in (3) by $\log(\log(x/m)/\log b)$. Partial summation of the prime error gives $O(e^{-c_1\sqrt L})$ uniformly at its endpoints. Summing $1/m$ costs $O(L)$, absorbed into the exponent. Put $\eta=\delta/(2+2\delta)$ and $H=x^\eta<T$. The sum for $H<m\le T$ of the resulting log multiplier against $\mu(m)/m$ is $O_\delta(e^{-c_2\sqrt L})$ by partial summation. The multiplier is bounded and its derivative has absolute value at most $1/(m\log b)$.

On $m\le H$, expand $\log(1-\log m/L)$ through $h=\lfloor\lambda\sqrt L\rfloor$ for a sufficiently small fixed $\lambda>0$. The absolute sum of remainders is $O_\delta(L\eta^{h+1})$. To extend every moment to infinity uniformly in $j\le h$, put $v=\log t$. For $v\ge\eta L$,

$$
 (v/L)^j\le \exp((2/e)\lambda\sqrt v),
$$

using $\log^+u\le(2/e)\sqrt u$. Choose $\lambda$ with $(2/e)\lambda<c/2$. In partial summation of the tail with weight $(\log t/L)^j/t$, the derivative has at most the extra factor $1+j/v\le2$ for all large $L$. The boundary term and the integral of $2e^{-c\sqrt v/2}$ over $v\ge\eta L$ are both $O_\delta(e^{-c_3\sqrt L})$. The constant moment is treated the same way and vanishes. Summing over $j\le h$ still gives stretched exponential decay. This proves the bound in (6) with $S_h(L)$ in place of $\mathcal C(L)$. The preceding Taylor and endpoint bounds at this smaller $h$ give $|\mathcal C(L)-S_h(L)|\ll e^{-c_4\sqrt L}$, which proves (6).

Together (5) and (6) identify the two errors in adaptive subtraction. The error from evaluating the deterministic correction can be made small enough for a bounded terminal-window energy. The remaining signed arithmetic error in (6), after squaring and summing, only has the proved bound $O_\delta(B e^{-c'_\delta\sqrt{\log B}})$. No estimate at subpower scale follows.

## How much prime-location information the joint energy needs

The following finite adapter uses the *actual* prime counts in a coarse grid. It applies to the signed sum with the smooth sector still in place. For $b\ge3$ construct integer grid points starting at $b$, setting

$$
 v'=\min(B,\,v+\lceil v/b\rceil)
$$

at each step until $B$ is reached. For every cell $(v,v']$ replace its primes by $\pi(v')-\pi(v)$ copies of its right endpoint, producing a nonnegative integer sequence $\widetilde P$. Let $P$ be the true prime indicator on $(b,B]$, extended by zero elsewhere, and set

$$
 \widetilde r=-(\mu\,1_{[1,b-1]})*\widetilde P,\qquad
 \widetilde a=s+\widetilde r.
$$

The convolution is Dirichlet convolution. On $n\le B$ the same rule with $P$ is exactly $r$, because at most one prime greater than $b$ divides $n$. Both output sequences agree with $\mu$ through $b-1$.

There are $O(b\log b)$ cells, since each step except the final one increases $v$ by a factor at least $1+1/b$. At the full output endpoint,

$$
 A_B(\widetilde a-\mu)\ll (\log(2b))^2,\qquad
 \left|\sqrt{A_B(\widetilde a)}-\sqrt{A_B(\mu)}\right|\ll \log(2b).  \tag{7}
$$

In particular subpower growth of the native output is equivalent to subpower growth of this surrogate. The estimate is additive in the norm. An unqualified constant-factor comparison of small energies would be stronger.

To prove (7), write $D(y)=\sum_{n\le y}(\widetilde P-P)(n)$. Only the cell containing $y$ contributes, and for $b\le y\le B$ its length is $\le 2y/b$. For the reciprocal discrepancy $d(y)=\sum_{n\le y}(\widetilde P-P)(n)/n$, the absolute error on this partial cell is $O(1/b)$. On all complete cells, rounding a prime $p$ up changes its reciprocal by at most $2/(bp)$. Mertens' prime harmonic sum gives $\sum_{b<p\le b^2}1/p=O(1)$, and hence $|d(y)|=O(1/b)$ uniformly. The discrepancies vanish below $b$. In the native convolution, for $b\le x\le B$,

$$
 |M_{\widetilde a-\mu}(x)|
 \le\sum_{m\le x/b}|D(x/m)|
 \ll \frac{x}{b}(1+\log(x/b)),\qquad
 |m_{\widetilde a-\mu}(x)|
 \le\sum_{m\le x/b}\frac{|d(x/m)|}{m}
 \ll \frac{1+\log(x/b)}b .
$$

Inserting these bounds into both terms of $A_B$ gives (7), using $B<b^2$. The norm difference is the reverse triangle inequality. No signs of the discarded prime-position errors, or signs of the surviving smooth/rough covariance, have been assumed.

The cell masses can be specified entirely from primes $\le b$. If $P_b=\prod_{p\le b}p$, every integer in $(b,B]$ coprime to $P_b$ is prime. Thus the mass on $(v,v']$ equals the finite sum $\sum_{d\mid P_b}\mu(d)(\lfloor v'/d\rfloor-\lfloor v/d\rfloor)$. This representation demonstrates information dependence, without a claim of improved running time. What remains is to estimate the signed pairing of these cell counts with the actual smooth sector at unbounded cutoffs.

## Conditional leading coefficient and the endpoint balancing fee

Write $E_N=\sum_{k\le N}M(k)^2/(k(k+1))$. Under the weak Mertens
hypothesis the balanced Möbius energy obeys
$$
 A_N(\mu)= E_N+2G(\log(N+1))^2+O((N+1)^{-1/2}),\qquad
 G(t)=\sum_\rho \frac{e^{i\gamma t}}{\rho(\rho-1)\zeta'(\rho)}.
$$
The sum includes both signs and converges absolutely and uniformly. Indeed
partial summation gives exactly $u_\mu(N)=\int_1^{N+1}M(x)x^{-2}\,dx$.
Apply [Inoue, Corollary 3](https://arxiv.org/abs/1705.00853) with $\kappa=2$:
the constant term vanishes by the prime number theorem and the
identity above as $N\to\infty$. The other error in that corollary is
$O((N+1)^{-1})$ before multiplication by $\sqrt{N+1}$. Absolute
convergence follows by Cauchy–Schwarz from the classical weak Mertens
necessary condition $B=\sum_\rho |\rho\zeta'(\rho)|^{-2}<\infty$
and $\sum_\rho|\rho-1|^{-2}<\infty$.

Since $E_N=\int_1^{N+1}M(x)^2x^{-2}\,dx$, the
[proposed mean-square converse, equation (6)](trace-weak-mertens-nov18.md)
gives $A_N(\mu)\sim B\log N$ and $A_{b^2-1}(\mu)/A_{b-1}(\mu)\to2$.
Even without that proposed converse, the first displayed formula and
the classical weak Mertens upper bound imply $A_N(\mu)\ll\log(2N)$.
Conversely this last estimate on all integers implies weak Mertens
directly by positivity. The bounded fee in the first formula contrasts
with the explicit size $2B_0/\log^2 B_0$ of each separated sector at
a Newton endpoint $B_0=b^2-1$.
