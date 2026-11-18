# Exact tilted saddle for both limiting abundance tails

Let $Z$ be either $n/\varphi(n)$ or $\sigma(n)/n$ in its limiting distribution, let $X=\log Z$, $W(s)=\log\mathbb E e^{sX}$ and $A_Z(t)=\Pr(Z\ge t)$. For every sufficiently large $t$ let $s>0$ solve $W'(s)=\log t$ and put $y=\exp(te^{-\gamma})$. Then, unconditionally,
$$
 A_Z(t)\ \sim\ \frac{\exp(W(s)-s\log t)}{s\sqrt{2\pi W''(s)}}
 \ \sim\ \frac{\exp(W(s)-s\log t)}{\sqrt{2\pi y}} .
 \tag{1}
$$
In particular the error in replacing $\log A_Z(t)$ by the real Legendre minimum is $-\tfrac12\log(2\pi y)+o(1)$ at **every** large threshold. The argument uses no density for $X$ with respect to Lebesgue measure: the local limit is tested against the one-sided exponential after changing measure. [Weingartner, limiting moments and his Lemma 2](https://arxiv.org/abs/1011.4262)

## Variance and Lyapunov ratio

Use the independent geometric prime valuations $\Pr(k=j)=(1-1/p)p^{-j}$ and scores $X_p=b_p\mathbf1_{k\ge1}$ for $\varphi$ and $X_p=\log(1+\cdots+p^{-k})$ for $\sigma$, with $b_p=-\log(1-1/p)$. The limiting arithmetic moment products identify $X$ with the sum of these independent scores. Under the tilted probability $d\Pr_s=e^{sX-W(s)}d\Pr$ the components stay independent. Put $s=x\log x$, $L=\log x$. Then
$$
 V=W''(s)\sim\frac1{xL^2},\qquad
 \sum_p\mathbb E_s|X_p-\mathbb E_s X_p|^3\ll\frac1{x^2 L^2}.
 \tag{2}
$$

For $\varphi$, $V=\sum b_p^2 K(sb_p-\log(p-1))$, $K(z)=e^z/(1+e^z)^2$. Below $x/2$ its contribution is $O(x^{-2}\log x)$ by $K\le p e^{-s/p}$; above $2x$ it is $O(x^{-3/2+o(1)})$ by $K\ll x^{1/2+o(1)}/p$. On $[x/2,2x]$ the total variation of $b(v)^2 K(sb(v)-\log(v-1))$ is $O(x^{-2})$ (the first factor decreases and the logistic derivative is unimodal). Quantitative PNT replaces the sum by the $dv/\log v$ integral with error $O_A(x^{-1}L^{-A})$. In $r=(v-x)L/x$ the exponent tends to $-r$ and $K\ll e^{-c|r|}$ by its monotone argument's derivative. This yields the first formula of (2) since $\int K=1$. For $\sigma$ the [prime-square estimate](abundance-curvature-sigma-nov18.md) gives the same variance up to $O_\epsilon(s^{-3/2+\epsilon})$, negligible here.

For $p>x/2$ the score range is $O(1/x)$, so its third absolute centered moment is $\ll x^{-1}\operatorname{Var}_s X_p$. For $p\le x/2$ the tilted probability that $b_p-X_p>C\log s/s$ is $O(s^{-20})$, with an absolute $C$. In fact, for $\sigma$ the valuation $k=\lfloor\log s/\log p\rfloor$ has probability $\ge1/(2s)$ before tilting and $s(b_p-X_p(k))=O(1)$; for $\varphi$ use the occupied mass $1/p$. Normalizing the tilt after removing $e^{s b_p}$ gives the asserted tail bound. Thus $|\mathbb E_s X_p-b_p|\ll1/x$ and, outside the exceptional event, $|X_p-\mathbb E_s X_p|\ll1/x$. Each third moment is at most $O(x^{-1}\operatorname{Var}_s X_p+s^{-20})$ since $b_p\le\log2$. Summing proves (2).

For later conversion to $y$, the same prime-to-integral estimate in the transition yields
$$
 W'(x\log x)=\gamma+\log\log x+o(L^{-2}).
 \tag{3}
$$
For $\varphi$ subtract $\sum_{p\le x}b_p$. This is $\gamma+\log\log x+O_A(L^{-A})$ by quantitative PNT, partial summation and Mertens' constant for the product. The logistic remainder outside $[x/2,2x]$ is $o(L^{-2})$ as in the [continuous model](abundance-weingartner-model-nov18.md). On the central interval its weight $b(v)(f(H(v))-\mathbf1_{v\le x})$ has total variation $O(1/x)$, so replacing the prime sum by the integral costs $O_A(L^{-A})$; the limiting rescaled integral is zero by oddness. For $\sigma$ the [same prime-square calculation](abundance-curvature-sigma-nov18.md) gives $W_\sigma'-W_\phi'=O((s\log s)^{-1/2})$. Equation (3) gives $y/x\to1$ at the exact saddle. Strictly positive variance and unbounded derivative ensure this saddle exists and is unique.

## Native-scale local limit

Write $Y_s=s(X-W'(s))$ under the tilt and $\chi_s(\xi)=\mathbb E_s e^{i\xi Y_s}$. By (2) its variance is asymptotic to $x$ and the Lyapunov ratio is $O(L/\sqrt x)$. Consequently $\chi_s(v/\sqrt x)\to e^{-v^2/2}$ for fixed $v$; for example, apply Berry–Esseen first to finite prime truncations and pass to the limit using convergence of the moments in (2).

For each fixed $A>0$ one has
$$
 |\chi_s(\xi)|\le
 \begin{cases}
 \exp(-c x\xi^2),&|\xi|\le1/L,\\
 \exp(-c_A x/L^4),&1/L\le|\xi|\le A.
 \end{cases}
 \tag{4}
$$
Indeed restrict to $p\in[x,x+x/L]$. For $\varphi$ the two tilted occupancy probabilities are bounded below by absolute constants in this shell. For $\sigma$, the tilted probabilities of valuations 0 and 1 are likewise bounded below: their weight ratio is $p^{-1}e^{s\log(1+1/p)}\asymp1$, and conditional on $k\ge1$ the total weight at $k\ge2$ relative to $k=1$ is $\ll e^{Cs/p^2}/p$. Its characteristic factor therefore has absolute value at most $\exp(-c\sin^2(\xi s a(p)/2))$, where $a(p)=b_p$ or $a(p)=\log(1+1/p)$ respectively. This follows by taking the squared modulus and retaining the contributions from the two specified states. On this shell $s a(p)=L+O(1)$, proving the first part of (4) by the $\asymp x/L^2$ prime count.

For the second part, replace the prime sum of $\sin^2(\xi s a(v)/2)$ on the same shell by its continuous $dv/\log v$ integral. Its total variation is $O_A(1)$ and quantitative PNT gives error $O_{A,B}(x/L^B)$ for arbitrarily large fixed $B$. In the variable $w=s a(v)$ the positive comparison measure has density $\asymp x/L^2$ on an interval of length tending to 1, because $|s a'(v)|\sim L/x$. On any such interval the unweighted integral of $\sin^2(\xi w/2)$ is $\gg_A \min(1,\xi^2)$, uniformly over its initial point. This follows by minimizing over phase, or from $(r-|\sin(\xi r/2)/(\xi/2)|)/2$ for interval length $r$. For $|\xi|\ge1/L$ the resulting lower bound is $\gg_A x/L^4$. Independence proves (4).

The measures $\sqrt x\,\Pr_s(Y_s\in dv)$ converge vaguely to $dv/\sqrt{2\pi}$ and have uniformly bounded mass on every interval of length one, uniformly in its center. For a Schwartz test with compactly supported Fourier transform, Fourier inversion, (4), and dominated convergence at frequency $v/\sqrt x$ prove the asserted limit directly. A fixed nonnegative band-limited Schwartz function bounded below on $[-1,1]$ exists by squaring a suitably dilated inverse Fourier transform of an even smooth bump. The same Fourier bound applied to each translate of this majorant gives the uniform unit-interval bound. By truncating their Fourier transforms in Schwartz topology, all smooth compactly supported tests now obey the same limit; the uniform interval bound permits the usual extension to continuous compactly supported tests. Since the limit has no atoms, a bounded test with finitely many discontinuities on a compact interval also works. Finally sum the uniform unit-interval bounds against the positive exponential tail to obtain
$$
 \sqrt x\,\mathbb E_s[e^{-Y_s}\mathbf1_{Y_s\ge0}]
 \longrightarrow \frac1{\sqrt{2\pi}}\int_0^\infty e^{-v}dv
 =\frac1{\sqrt{2\pi}} .
$$
Untilt at $W'(s)=\log t$ to prove (1).
