# The prime-square correction in the abundance moment

Let $W_\sigma(s)$ and $W_\phi(s)$ denote the logarithms of the limiting positive moments of $\sigma(n)/n$ and $n/\phi(n)$ respectively. Their local variables under the usual geometric prime-valuation law $\Pr(k=j)=(1-1/p)p^{-j}$ are
$$
 A_p(k)=\log(1+\cdots+p^{-k}),\qquad B_p(k)=b_p\mathbf1_{k\ge1},\qquad b_p=-\log(1-p^{-1}).
$$
Each log moment is the sum of $\log\mathbb E\exp(sA_p)$ or its $B_p$ analogue. These products describe the moments of the established limiting arithmetic distributions. For bounded real $s$ the sums and the first two derivatives converge locally uniformly: at large $p$ each tilted nonzero probability is $O(1/p)$ and scores are $O(1/p)$. [Weingartner on the limiting distributions and moment products](https://arxiv.org/abs/1011.4262)

Write $D=W_\sigma-W_\phi$. Unconditionally as $s\to\infty$,
$$
 D''(s)\sim\frac{1}{\sqrt{2\log s}\ s^{3/2}},\qquad
 D'(s)\sim-\frac{\sqrt2}{\sqrt{s\log s}},\qquad
 D(s)\sim-2\sqrt2\sqrt{s/\log s}.
 \tag{1}
$$
In particular the curvature difference costs $O_\epsilon(s^{-3/2+\epsilon})$, and the two functions have the same limiting linear correction relative to the continuous prime model.

## What survives subtracting the first prime mode

Put $K(u)=e^u/(1+e^u)^2$. For every $\epsilon>0$,
$$
 D''(s)=\sum_p p^{-4}K(s/p^2-\log p)+O_\epsilon(s^{-5/3+\epsilon}).
 \tag{2}
$$
All curvature terms here are physical tilted variances: $\partial_s^2\log\mathbb E e^{sA}=\operatorname{Var}_s(A)$. Fix small $\eta>0$ and split at $P_0=s^{1/3+\eta}$ and $P_1=s/(\log s)^2$, taking $\eta<1/12$.

For $p\le P_0$, put $k=\lfloor\log s/\log p\rfloor$. Its geometric mass is at least $1/(2s)$, and $s(b_p-A_p(k))=-s\log(1-p^{-k-1})\le2$. The normalizing mass after removing $e^{s b_p}$ is therefore at least $e^{-2}/(2s)$. Under the tilt, $\Pr(b_p-A_p>5\log s/s)=O(s^{-4})$, hence the variance costs $O((\log s/s)^2)$. For $B_p$ the occupied mass $1/p$ supplies the same bound. This range costs $O(s^{-5/3+\eta}\log^2s)$, and the right-hand shell in (2) is exponentially small here since $s/P_0^2$ grows as a power.

For $p>P_1$ the two scores on the same valuation differ by $O(p^{-2})$: on $k=0$ they agree, and on $k\ge1$ their difference is $-\log(1-p^{-k-1})$. Their magnitudes are $O(p^{-1})$. Under a common law the variance difference is $O(p^{-3})$. The two tilted laws have likelihood ratio in $[\exp(-Cs/p^2),\exp(Cs/p^2)]$, hence changing the law adds $O(s/p^4)$ to the variance bound (use either the centered second moment or the two raw moments). Summation over all integers costs $O(P_1^{-2}+sP_1^{-3})$. The logistic shell here is bounded by $O(\sum_{p>P_1}p^{-4})$.

In $P_0<p\le P_1$, the tilted absent probability for either score is $O(p\exp(-s\log(1+1/p)))$, negligible even after summing over $p$. The occupied $B_p$ is constant. For $A_p$, split the occupied law into $k=1$ and $k\ge2$. Relative to the $k=2$ term, the weights above two have total $O(1/p)$ because $s(b_p-A_p(2))=O(s/p^3)=o(1)$. The log odds of $k\ge2$ versus $k=1$ are thus
$$
 u_p+O(s/p^3+1/p),\qquad
 u_p=s/p^2-\log p,
$$
since $A_p(2)-A_p(1)=\log(1+1/(p+p^2))=p^{-2}+O(p^{-3})$. The conditional mean of the $k\ge2$ scores differs from $A_p(1)$ by $p^{-2}+O(p^{-3})$, and their conditional variance costs $O(p^{-6})$. The total-variance identity and $|(\log K)'|\le1$ give for this range
$$
 \operatorname{Var}_s(A_p)=p^{-4}K(u_p)(1+O(s/p^3+1/p))+O(p^{-6})
$$
up to the negligible absence estimate. Summing $p^{-6}$ costs $O(P_0^{-5})$.

Let $Q^2\log Q=s$ and $\ell=\log Q$. For $P_0<p<Q/2$ the shell is at most $p^{-3}\exp(-4\ell)$, and its sum costs $O(P_0^{-2}Q^{-4})$. For $p>2Q$ it is at most $p^{-5}e^{\ell/4}$, costing $O(Q^{-15/4})$. Both are $O(s^{-5/3})$. On $[Q/2,2Q]$ the relative error above is $O(s/Q^3+1/Q)=O(\ell/Q)$, costing $O(\ell Q^{-4})$ on summing even over all integers. These bounds prove (2), choosing $\eta$ sufficiently small relative to $\epsilon$.

It remains to evaluate the central shell. On $[Q/2,2Q]$ the function $p^{-4}K(s/p^2-\log p)$ has total variation $O(Q^{-4})$ by the product variation bound and unimodality of $K$. Classical PNT with any fixed inverse-log-power remainder replaces its prime sum by the integral against $dp/\log p$, with error $O_A(Q^{-3}/\ell^A)$ for every fixed $A$. Substitute $u=s/p^2-\log p$, for which $|dp/du|=p/(2s/p^2+1)$. The new integrand divided by $Q^{-3}/(2\ell^2)$ tends to $K(u)$ at each fixed $u$, and is bounded by $C K(u)$ over the central range. Since $\int_{\mathbb R}K(u)du=1$, the shell is asymptotic to $Q^{-3}/(2\ell^2)\sim s^{-3/2}/\sqrt{2\log s}$. This gives the first formula in (1).

## Anchoring the derivative and centering the moments

Pointwise $0\le B_p-A_p\le C p^{-2}$, where the absent scores are zero. Thus the normalized local log-moment difference $s^{-1}(\log\mathbb E e^{sB_p}-\log\mathbb E e^{sA_p})$ is bounded by $C p^{-2}$. It tends to zero for fixed $p$, because both geometric-law scores have essential supremum $b_p$. Dominated convergence gives $D(s)=o(s)$. By integrability of $D''$ the derivative has a finite limit, necessarily zero. Hence $D'(s)=-\int_s^\infty D''(v)dv$ and ordinary integration gives the remaining two formulas in (1).

For the smooth continuous prime comparison put
$$
 M(s)=\int_2^\infty\log\!\left(1+\frac{e^{s b(x)}-1}{x}\right)\frac{dx}{\log x},
 \qquad b(x)=-\log(1-1/x).
$$
The common limiting derivative offset is
$$
 d=\lim_{s\to\infty}(W_\phi'(s)-M'(s))
   =\lim_{s\to\infty}(W_\sigma'(s)-M'(s))
   =\gamma_E+\log\log2-\int_2^\infty\frac{b(x)-1/x}{\log x}dx .
$$
Indeed the differentiated weight is $b(x)/(1+(x-1)e^{-s b(x)})$. It differs in total sum, and in total integral against $dx/\log x$, by $o(1)$ from $b(x)\mathbf1_{x\le Z}$ where $Z\log Z=s$. Below $Z/2$ the excluded fraction is $O(1/Z)$; above $2Z$ the tail is bounded by $O(Z^{0.51}/x^2)$ for large $Z$. On $[Z/2,2Z]$ the transition has absolute error $O(Z^{-1}e^{-c|x-Z|\log Z/Z})$, using the derivative of $s b(x)-\log(x-1)$ and its value $O((\log Z)/Z)$ at $Z$. Summing over all integers, or integrating, costs $O(1/\log Z)$. Mertens' product theorem for the truncated sums now gives $d$.

Thus the centered values $U_\sigma=W_\sigma-M-ds$ and $U_\phi=W_\phi-M-ds$ differ by precisely $D(s)$, with the leading negative correction in (1). Their derivative limits are zero. An $O_\epsilon(s^{1/2+\epsilon})$ value criterion, $O_\epsilon(s^{-1/2+\epsilon})$ first-derivative criterion or $O_\epsilon(s^{-3/2+\epsilon})$ curvature criterion for one is equivalent to the respective criterion for the other. A curvature bound implies the derivative and value estimates by integration with the derivative anchor. For the converse analytic continuation from a value bound, integration by parts on the initial common Mellin strip gives, modulo lower-endpoint entire terms,
$$
 \int_1^\infty s^{z-1}U''(s)ds
 =(z-1)(z-2)\int_1^\infty s^{z-3}U(s)ds.
$$
The initial identity holds for real part of $z$ sufficiently negative and then by continuation; all relevant derivatives there have polynomial bounds. A centered value bound $O_\epsilon(s^{1/2+\epsilon})$ makes the right side holomorphic for $\Re z<3/2$. The [prime discrepancy argument](abundance-curvature-nov18.md) treats the resulting zeta-zero obstruction. In this Mellin convention (1) also gives the genuine real boundary asymptotic
$$
 \int_1^\infty s^{z-1}D''(s)ds\sim
 \sqrt{\pi/2}\,(3/2-z)^{-1/2}\qquad(z\uparrow3/2),
$$
by the substitution $v=\log s$ and scaling, since the tail is eventually positive. Equation (2) identifies a discrete correction whose subtraction extends this comparison to $\Re z<5/3$.

## Centering each arithmetic distribution by its own smooth prime model

Alternatively let $M_\sigma(s)$ be the integral against $dx/\log x$ of the exact local log moment of the geometric law at the real parameter $x\ge2$, and put $M_\phi=M$ as above. Then
$$
 (W_\sigma-M_\sigma)-(W_\phi-M_\phi)
 =O_\epsilon(s^{\Theta/2+\epsilon}),\qquad \Theta=\sup_\rho\Re\rho .
 \tag{3}
$$
In particular this difference is $O_\epsilon(s^{1/4+\epsilon})$ under RH. The common prime-square correction of size $\sqrt{s/\log s}$ in (1) is absorbed by the second centering. Both derivative offsets are still $d$: the derivative difference $M_\sigma'-M_\phi'$ tends to zero by applying the same three-range variance argument and dominated-convergence slope anchor with $dx/\log x$ in place of the prime sum.

To prove (3) write $d_s(x)$ for the difference of local log moments at $x$. The left side is exactly its Stieltjes integral against $d(\pi(x)-\int_2^x du/\log u)$. We claim
$$
 |d_s'(x)|\ll
 \begin{cases}
 (\log s)^2/x,&2\le x\le\sqrt s,\\
 s(\log s)^2/x^3,&x\ge\sqrt s .
 \end{cases}
 \tag{4}
$$
The prime parameter is differentiated here, at fixed $s\ge s_0$. Factor out the common $(1-1/x)e^{s b(x)}$; the remaining normalizing sums are
$$
 Z_A=\sum_{k\ge0}x^{-k}(1-x^{-k-1})^s,\qquad
 Z_B=(1-1/x)^s+1/(x-1).
$$
In the first range, $Z_A\gg1/s$ by the candidate $k=\lfloor\log s/\log x\rfloor$. Its logarithmic derivative in $\log x$ is the tilted expectation of $-k+s(k+1)x^{-k-1}/(1-x^{-k-1})$. On $k\le 20\log s$, $s x^{-k-1}\le10\log s$ this is $O((\log s)^2)$. The tail $k>20\log s$ is negligible by the summable majorant $O(s(1+k)2^{-k})$ before division by $Z_A$; the remaining exceptional weights have $(1-x^{-k-1})^s\le s^{-10}$ and the derivative factor is $O(s\log s)$. The log derivative of $Z_B$ is bounded since its first term relative to the second is at most $x e^{-s/x}$ in this range. This proves the first bound.

In the second range write
$$
 d_s(x)=\log(1-r(1-w)),\quad
 r=(1+(x-1)e^{-s b(x)})^{-1},\quad
 w=\sum_{k\ge1}(1-1/x)x^{1-k}(1-x^{-k-1})^s .
$$
Here $r$ is the tilted occupancy probability for the totient score and $w$ averages the depletion conditional on occupancy. We have $w\gg1$, $0\le1-w\ll s/x^2$, and $|w'|\ll s/x^3$. For the last bound differentiate the series for $1-w$: the logarithmic derivative of each conditional probability is $O((1+k)/x)$, the conditional geometric mean of $1+k$ is bounded, and the derivative of $(1-x^{-k-1})^s$ is $O(s(k+1)x^{-k-2})$. Also $x|r'|\ll r(1-r)(1+s/x)\ll(\log s)^2$. Below $s/(\log s)^2$ use $1-r\le x e^{-s/x}$ and above it use $s/x\le(\log s)^2$. The derivative of the displayed logarithm proves (4).

The PNT discrepancy $\pi(x)-\int_2^xdu/\log u$ is $O_\alpha(x^\alpha)$ for each $\Theta<\alpha<2$, by the usual explicit formula and partial summation (the trivial bound suffices for $\alpha\ge1$). Integration by parts with (4) gives $O(s^{\alpha/2}(\log s)^2)$. There is no endpoint at infinity since $d_s(x)=O(s/x^2)$ there. This proves (3).

The bound differentiates at every fixed order. If $G=(W_\sigma-M_\sigma)-(W_\phi-M_\phi)$, then
$$
 G^{(j)}(s)=O_{j,\epsilon}(s^{\Theta/2-j+\epsilon})\qquad(j\ge0).
 \tag{5}
$$
For clarity this follows from a complex-disc bound for $G$, not from formal differentiation of (3). Fix a sufficiently small absolute $c>0$ and allow $z$ in $|z-s|\le c s/\log s$. In the formulas for $d_s$ replace $s$ by $z$, using the logarithm continued from the positive real axis. For $x\le\sqrt s$, $Z_A(z)/Z_A(\Re z)$ is the real tilted average of $\exp(i\Im z\log(1-x^{-k-1}))$. The probability that $-\log(1-x^{-k-1})>10\log s/s$ is $O(s^{-7})$, using $Z_A(\Re z)\gg1/s$ and $\Re z\ge0.9s$. On the complementary event the phase has modulus at most $10c$. Thus $Z_A(z)$ is bounded below in modulus by a fixed positive multiple of $Z_A(\Re z)$. The differentiated numerator is bounded in absolute value by the real-weight derivative majorant used above. The other sum $Z_B(z)$ is dominated by $1/(x-1)$ as before. The first part of (4) holds uniformly on the disc.

For $x\ge\sqrt s$, retain the formulas for complex $r,w$. Each phase in $w$ is $O(c/\log s)$ and its modulus is bounded below by an absolute positive constant since $k\ge1$; hence $\Re w\gg1$. Also $|1-w|\ll s/x^2$ and $|w'|\ll s/x^3$, from the same series bounds. On $\sqrt s\le x\le s/(4\log s)$ we have $|(x-1)e^{-zb(x)}|\le x e^{-0.9s/x}=o(1)$. Thus $r=1+o(1)$, $1-r(1-w)=w+o(1)$ is bounded away from zero, and $x|r'|\ll(1+s/x)x e^{-0.9s/x}=O(1)$. On $x\ge s/(4\log s)$ we have $|\Im z|b(x)\le5c$ for large $s$. The denominator $1+(x-1)e^{-zb(x)}$ stays bounded away from zero in a fixed sector, both $r$ and $1-r$ are bounded, and $|1-w|=O((\log s)^2/s)=o(1)$. Here $x|r'|\ll1+s/x\ll\log s$. This proves the remaining part of (4) uniformly and verifies the needed local logarithms are holomorphic. Their difference decays as $O(s/x^2)$ at infinity, which also permits integration and summation on compact subdiscs. The Stieltjes bound proving (3) now holds on the whole disc. Cauchy's derivative estimate, absorbing each fixed extra power of $\log s$ into $s^\epsilon$, proves (5).

## Explicit all-scale arithmetic margins for finite zero-height tests

Set $s=xL$, $L=\log x\ge1000$, and
$$
 H_s(v)=\frac{s b(v)-\log(1+(e^{s b(v)}-1)/v)}{\log v}
 =1-\frac{\log(1+(v-1)e^{-s b(v)})}{\log v}.
$$
Then
$$
 1.97\sqrt x < P_s:=\sum_{k\ge2,p}H_s(p^k)\log p <2.001\sqrt x,
 \qquad W_\phi(s)-W_\sigma(s)>2.80\sqrt x .
 \tag{6}
$$
We use $|\vartheta(v)-v|\le\eta v$ for $v\ge e^{30}$ with $\eta=10^{-6}$, and $\vartheta(v)\le2v$ globally. The first follows from $0.0244v/\log^3v$ above $e^{30}$; the global bound follows, for instance, from $\psi(v)<1.03883v$. [Broadbent et al., Theorem 1](https://arxiv.org/abs/2002.11068) · [Ramaré and Zuniga-Alterman, Lemma 2.3](https://arxiv.org/abs/2408.05969)

We have $0\le H_s(v)\le\min(1,s b(v)/\log v)$. On $p\le q=\sqrt x$ the square terms cost at most $(1+\eta)q$. Above $q$, $b(p^2)\le p^{-2}/(1-1/x)$ and
$$
 \int_{(q,\infty)}u^{-2}d\vartheta(u)\le (1+3\eta)/q
$$
by partial summation. Their total is at most $s(1+3\eta)/(2q(1-1/x)\log q)$. For the higher powers set $A(v)=\sum_{k\ge3,p^k\le v}\log p\le2v^{1/3}\log v/\log2$. Since $H_s(v)\le2x/v$ for $v>x$, their contribution is at most $A(x)+2x\int_{(x,\infty)}v^{-1}dA(v)\le(2/\log2)(4L+5)x^{1/3}<0.0001\sqrt x$. The last ratio decreases for $L\ge1000$. This proves the upper bound.

For reference partial summation gives, for $q\ge e^{30}$ and $R>1$, also including $R=\infty$ by a limit,
$$
 \sum_{q<p\le Rq}p^{-2}
 \ge \frac{(1-\eta)(1-1/\log q-1/R)-2\eta}{q\log q}.
 \tag{7}
$$
Indeed integrate $(u^2\log u)^{-1}$ against $d\vartheta$, using $\vartheta\ge(1-\eta)u$ in the positive terms and $\vartheta(q)\le(1+\eta)q$ at the negative boundary. In the resulting ordinary integral use $\int_q^\infty du/(u^2\log u)\ge (1-1/\log q)/(q\log q)$ and the upper bound $1/(Rq\log q)$ for the removed tail.

For $p^2\le0.98x$, $H_s(p^2)\ge1-e^{-0.02L}/\log4$ since $s b(p^2)\ge L/0.98$. This square range contributes at least $(1-e^{-0.02L}/\log4)(1-\eta)\sqrt{0.98x}$. For $p^2\ge1.02x$ we have $s b(p^2)\le s/(p^2-1)<0.981L$. Hence the subtracted first-prime log factor is at most $s b(p^2)e^{s b(p^2)}/p^2\le e^{-0.019L}s b(p^2)$. By (7) this range contributes at least
$$
 (1-e^{-0.019L})\frac{s}{2}\,
 \frac{(1-\eta)(1-1/\log q)-2\eta}{q\log q},\qquad q=\sqrt{1.02x}.
$$
The first lower contribution exceeds $0.989\sqrt x$ and the second exceeds $0.987\sqrt x$ throughout $L\ge1000$. This proves the lower bound on $P_s$.

Finally put $q=\sqrt{2x}$, $R=1000$. Under the totient tilt the absent probability is at most $p e^{-s/p}\le1/p$ for all $p\le Rq$, since $2p\log p\le s$ on that range. Conditional on occupancy the geometric probabilities of exponent one and higher total $1-1/p$ and $1/p$, respectively. The normalized divisor-sum moment therefore has ratio to the totient factor at most $e^{-s/p^2}+2/p$. The log deficit at $p$ is consequently at least $\min(s/p^2,\log p)-\log3$. Charge this error only at $p\le2q$; its total is
$$
 (\log3)\pi(2q)\le(\log3)(\sqrt{2q}+2\vartheta(2q)/\log(2q))<0.013\sqrt x.
$$
For $2q<p\le Rq$ the sharper elementary bound is $s/p^2-2e^{L/8}/p$, since $s/p^2\le L/8$. The total error is at most $2e^{L/8}(1+\log R)<0.001\sqrt x$. For $p\le q$ we have $\min(s/p^2,\log p)\ge[L/(L+\log2)]\log p$, giving at least $1.412\sqrt x$. For $q<p\le Rq$ the minimum is $s/p^2$ and (7) gives at least $1.408\sqrt x$ since $s/(q\log q)=\sqrt{2x}L/(L+\log2)$. Dropping the other nonnegative deficits proves (6).
