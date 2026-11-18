# Independent check of the weighted Mellin counterexample to Theorem 5.5

The published implication from zero-freeness to approximation fails at the permitted pair $(\alpha,a)=(-3,7/4)$. The implication from approximation to zero-freeness holds throughout the printed parameter range by the same functional. [Version of Record](https://doi.org/10.1007/s11785-025-01661-2)

## Printed statement and analytic branches

Publisher PDF p. 3 defines $\|f\|_{D_\gamma}^2=\sum_{n\ge0}(n+1)^\gamma|[z^n]f|^2$. Equation (2) on p. 4 defines $h_k=(1-z)^{-1}\log((1+z+\cdots+z^{k-1})/k)$. The display on p. 21 defines $T_af=((1-z)^af)'/(1-z)^a=f'-af/(1-z)$. Theorem 5.5 on p. 26 states that $(1-z)^{1-a}$ lies in the $D_{\alpha+2}$-closure of the span of $(1-z)^{1-a}h_k$, $k\ge2$, **if and only if** $\zeta$ has no zeros in $\Re s>(-1-\alpha)/2$, for $\alpha\in[-3,-2]$ and $1\le a<(1-\alpha)/2$. ArXiv v6 PDF p. 21 gives the same statement. [Publisher PDF](../../sources/logarithmic_riesz_round3/gallardo_seco2025.pdf) [arXiv v6 PDF](../../sources/logarithmic_riesz_round3/gallardo_seco2206v6.pdf)

Put $t=-(\alpha+1)/2$, $c=a-1$, $\beta=\alpha+2=1-2t$, $u=(1-z)^{-c}$ and $b=t-c>0$. Powers use the analytic logarithm of $1-z$ with value zero at $z=0$. The normalized analytic logarithm in $h_k$ is
$$
B_k(z)=(1-z)h_k(z)=\operatorname{Log}(1-z^k)-\operatorname{Log}(1-z)-\log k.
$$
Its value at zero is $-\log k$, and its values along $0\le r<1$ are real. Its exponential is the normalized polynomial in (2), whose zeros are on the unit circle away from $1$. Its value at $1$ is $1$, so the logarithm $B_k$ extends analytically across $1$. Noor explicitly uses this same logarithm in the coefficient expansion after Lemma 7. [Noor, PDF p. 6](../../sources/noor_advocate_round4/noor2019_advocate.pdf)

Expansion of the logarithms gives $[z^n]h_k=H_n-H_{\lfloor n/k\rfloor}-\log k=O_k((n+1)^{-1})$, using the harmonic number asymptotic with $O(1/n)$ remainder and $H_0=0$. For $c>0$, the binomial coefficients of $u$ are $O_c((n+1)^{c-1})$ by the gamma ratio. In the convolution for $uh_k$, sum the $h_k$ indices $j\le n/2$ using the bound $(n+1)^{c-1}\sum_{j\le n/2}1/(j+1)$, and sum $j>n/2$ using $(n+1)^{-1}\sum_{m\le n/2}(m+1)^{c-1}$. This bounds the coefficients of $uh_k$ by $O_{c,k}((n+1)^{c-1}\log(n+2))$. Both $u$ and $uh_k$ belong to $D_\beta$ since $\beta+2c-2=-1-2b<-1$. At $c=0$, membership follows from $u=1$ and the coefficient bound on $h_k$.

## Boundedness and exact values

For $\sigma=\Re s>b$, define
$$
\Lambda_s(f)=\frac1{s\Gamma(s)}\int_0^1(-\log r)^{s-1}(1-r)^{c+1}
 \left(f'(r)-\frac{a f(r)}{1-r}\right)\,dr.
$$
The complex power uses the real logarithm of $-\log r$. For $1/2\le r<1$, let $\delta=1-r$. Coefficient Cauchy–Schwarz bounds the evaluation of $f$ by its norm times the square root of $\sum(n+1)^{-\beta}r^{2n}$, and that of $f'$ by its norm times the square root of $\sum_{n\ge1}n^2(n+1)^{-\beta}r^{2n-2}$. For $p\ge0$, $\sum_{n\ge0}(n+1)^pe^{-2n\delta}=O_p(\delta^{-p-1})$ by grouping indices into blocks of length $\lceil\delta^{-1}\rceil$. Using $r^{2n}\le e^{-2n\delta}$ and $r^{-2}\le4$ therefore gives $|f(r)|\lesssim_\beta\|f\|_{D_\beta}\delta^{-t}$ and $|f'(r)|\lesssim_\beta\|f\|_{D_\beta}\delta^{-t-1}$. Since $-\log r\asymp\delta$, the absolute integrand is bounded by $C_{s,\alpha,a}\|f\|_{D_\beta}\delta^{\sigma+c-t-1}$. This is integrable by $\sigma>t-c$. On $[0,1/2]$ both evaluations are uniformly bounded by geometric coefficient sums, and integrability of $(-\log r)^{\sigma-1}$ follows from $x=-\log r$. This establishes continuity without Proposition 5.1.

Because $a=c+1$,
$$
(1-r)^{c+1}T_a(uv)(r)=((1-r)v(r))'.
$$
At $v=1$ this is $-1$, giving $\Lambda_s(u)=-1/s$. At $v=h_k$ the integrand's analytic factor is
$$
B_k'(r)=\frac1{1-r}-\frac{k r^{k-1}}{1-r^k}.
$$
The coefficient of $z^{n-1}$ here is $1-k\mathbf 1_{k\mid n}$. Its partial sum is $n-k\lfloor n/k\rfloor$, which also independently verifies the remainder generating function upon division by $1-r$.

For $\sigma>1$ the two geometric series may be integrated separately because their absolute integral sums are $\Gamma(\sigma)\sum_{n\ge1}n^{-\sigma}$ and $k\Gamma(\sigma)\sum_{n\ge1}(kn)^{-\sigma}$. The identity $\int_0^1(-\log r)^{s-1}r^{n-1}\,dr=\Gamma(s)n^{-s}$ then gives $(1-k^{1-s})\zeta(s)/s$. Since $B'_k$ is bounded on $[0,1]$, the original integral is holomorphic on $\sigma>0$ by local domination at both endpoints. The product $(1-k^{1-s})\zeta(s)$ has a removable singularity at $1$. Thus the formula for $\Lambda_s(uh_k)$ holds by continuation throughout $\sigma>b$.

## Counterexample and scope

If $\zeta(\rho)=0$ and $\Re\rho>b$, then $\Lambda_\rho$ vanishes on the entire closed span and equals $-1/\rho$ on $u$. This gives the strictly positive distance bound $1/(|\rho|\,\|\Lambda_\rho\|)$ and shows that approximability implies zero-freeness in $\Re s>b$, which contains the printed region $\Re s>t$.

At $(-3,7/4)$ the triple $(t,c,b)$ is $(1,3/4,1/4)$. The Euler product gives zero-freeness of the printed region $\Re s>1$. The Riemann–von Mangoldt formula gives $N(T)\to\infty$ and thus a nontrivial zero, and symmetry $\rho\mapsto1-\bar\rho$ gives one with real part at least $1/2$. This puts a zero strictly inside the functional's region, so the target lies outside the closed span. The same argument works for $\alpha=-3$ and $3/2<a<2$. [Titchmarsh, 2nd ed., §§2.12 and 9.3–9.4](../../sources/equivalence_round2/titchmarsh1986.pdf)

For an explicit norm estimate at the exhibited pair, $D_{-1}$ coefficient Cauchy–Schwarz gives $|f(r)|\le\|f\|/(1-r^2)$. The identity $\sum_{n\ge1}n^2(n+1)x^{n-1}=2(1+2x)/(1-x)^4$ gives $|f'(r)|\le\sqrt{2(1+2r^2)}\,\|f\|/(1-r^2)^2$. Therefore $|T_af(r)|\le(\sqrt6+7/4)(1-r)^{-2}\|f\|$. Write $\sigma_\rho=\Re\rho\in[1/2,1]$. Since $-\log r\ge1-r$ and $\sigma_\rho-1\le0$, the log power in the absolute integrand is at most $(1-r)^{\sigma_\rho-1}$. Multiplying by the remaining factor $(1-r)^{c+1-2}$ and integrating gives $1/(\sigma_\rho-1/4)$. The distance is consequently at least
$$
\frac{|\Gamma(\rho)|(\sigma_\rho-1/4)}{\sqrt6+7/4}>0.
$$

The multiplier $(1-z)^c$ tends to zero on the radius when $c>0$, so the bounded-below hypothesis in Proposition 5.1 cannot justify inverse transfer with that multiplier. The integral supplies a direct obstruction in the actual approximation norm, at $a>t$. The sufficiency of zero-freeness on $\Re s>b$ is separate from this witness. Its scope is the printed reverse implication of Theorem 5.5. The staged Crossmark record dated 2026-11-17 displays “Document is current” without a listed update. The staged arXiv abstract identifies v6 of 5 June 2024 as the latest version. [Crossmark snapshot](../../sources/logarithmic_riesz_round3/gallardo_seco_crossmark_content_20261117.txt) [arXiv snapshot](../../sources/logarithmic_riesz_round3/gallardo_seco_arxiv_abs_20261117.html)
