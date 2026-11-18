# A logarithmically longer horizon for positivity of Li coefficients

**Status.** Proposed analytic result for review. Write $\mathrm{RH}(T)$ when every nontrivial zeta zero of positive ordinate at most $T$ lies on the critical line. Count zeros with multiplicity and take natural logarithms throughout.

**Source.** Campaign C1 asks for an explicit positive constant $c$ such that $\mathrm{RH}(T)$ implies Li positivity up to $cT^2\log T$. It attributes the original $T^2$ result to Oesterlé. The arguments below use its counting bounds. Priority beyond this campaign has not been established. [Frozen C1 final report, §§3.1 and 8](https://github.com/GettysburgResearch/riemann/blob/2dbadaef2014cbebd1881b5ce261575e14f4edb7/research/exploratory/riemann-observatory/proposals/independent_campaigns/C1-detection-horizons/FINAL.md)

## Explicit theorem

If $T\ge100$ and $\mathrm{RH}(T)$ holds, then $\lambda_n>0$ for every integer
$$1\le n\le 2T^2\log T.$$

Use the symmetric Li sum $\lambda_n=\sum_\rho[1-(1-1/\rho)^n]$. Write $\rho=\beta+i\gamma$ with $\gamma>0$, $\delta=|\beta-1/2|$ and $a=|\log|1-1/\rho||$. The involution $\rho\mapsto1-\bar\rho$ negates the logarithmic radius while preserving the argument $\phi=\arg(1-1/\rho)$. After averaging over this involution, the contribution per positive ordinate, including its conjugate, is $2[1-\cosh(na)\cos(n\phi)]$. This convention counts line zeros correctly. Symmetric grouping converges absolutely for fixed $n$. The squared moduli and $\log(1+x)\le x$ give $a\le\delta/\gamma^2$.

We import three estimates from C1 §3.1, steps 4 and 8. For $\gamma\ge n\ge100$ the averaged contribution is at least $0.894n^2/\gamma^2$. With $\ell_x=\log(x/(2\pi))$ and $x\ge100$, its counting estimates give
$$
 S_4(x)=\sum_{\gamma>x}\gamma^{-4}\le {2(\ell_x+1/3)\over3\pi x^3},
 \qquad \sum_{\gamma\ge x}\gamma^{-2}\ge {\ell_x\over10\pi x}.
$$
Thus the contribution at and above $n$ is at least $0.894n\ell_n/(10\pi)$.

The source already treats $n\le T^2$. For $T^2<n\le M=2T^2\log T$, let $U=n/(2T^2)$. The entire loss from $T<\gamma<n$ is at most
$$
 D(n)=2\sum_{\gamma>T}\bigl(\cosh(n/(2\gamma^2))-1\bigr)
 \le 2T^4 S_4(T)(\cosh U-1).
$$
Indeed $\cosh(ux)-1\le x^2(\cosh u-1)$ for $u\ge0$, $0\le x\le1$, term by term in the power series. The last upper bound divided by $n$ increases with $n$, so evaluate it at $M$. Here $\cosh(\log T)-1<T/2$ and $\ell_T+1/3<\log T$. These give $D(n)/n < 1/(3\pi)$. On the other hand $0.894\ell_n/10>1/3$ for $n>T^2\ge10^4$. Every term through height $T$ is nonnegative by hypothesis. This proves strict positivity.

At the Platt–Trudgian verified height $T=3{,}000{,}175{,}332{,}800$, this gives $\lambda_n>0$ for $n\le5.17\cdot10^{26}$. This deduction uses the imported zero census. No individual coefficient at those indices was evaluated.

## Density refinement

For each fixed $A\ge0$, there exists $T_A$ such that $\mathrm{RH}(T)$ for $T\ge T_A$ gives positivity for every integer
$$
 1\le n\le M_A=T^2(4\log T+A\log\log T).
$$

Consider $T^2<n\le M_A$. Bound the middle loss by $2\sum_{\gamma>T}(\cosh(na)-1)$. It suffices to show this is $o(T^2)$ uniformly there, since the high tail is $\gg n\log n$. The portion above $2T$ is at most
$$
 2(2T)^4 S_4(2T)(\cosh(M_A/(8T^2))-1)
 \ll_A T^{3/2}(\log T)^{1+A/8}.
$$
For $T<\gamma\le2T$, reflect so that $\beta\ge1/2$, allowing an overall factor of two. For $\beta\le0.6$ the count is $O(T\log T)$ and each loss is $O_A(T^{0.4}(\log T)^{A/10})$.

For $\beta>0.6$ use Ramaré's uniform explicit density bound in the corrected form quoted in Kadiri–Lumley–Ng, *Explicit zero density for the Riemann zeta function*, introduction, equation (1.5). It implies, for $0.52\le\sigma<1$ and $H\ge2000$,
$$
 \#\{\rho:0<\gamma<H,\ \beta>\sigma\}\ll H^{(8/3)(1-\sigma)}(\log H)^5.
$$
The displayed absolute constants in that reference ensure uniformity as $\sigma\to1$. Partition $(0.6,1)$ into intervals $(s,s+1/\log T]$, truncating the last interval. In each nonempty interval the number of relevant zeros satisfies this bound at $(s,3T)$, while their individual exponential weight is
$$
 e^{na}\le e^4 T^{4(s-1/2)}(\log T)^{A/2}.
$$
The product of the two powers of $T$ is $T^{2-(4/3)(1-s)}$. The classical Vinogradov–Korobov zero-free region gives an absolute $b>0$ with $1-s\ge b(\log T)^{-2/3}(\log\log T)^{-1/3}$ for every nonempty interval and sufficiently large $T$, since $s<\beta$ and $\gamma\in(T,2T]$. Summing at most $O(\log T)$ intervals gives
$$
 O_A\!\left(T^2(\log T)^{6+A/2}
  \exp\{-\tfrac43 b(\log T/\log\log T)^{1/3}\}\right)=o(T^2).
$$
This establishes the stated implication. Its constants have not been evaluated at the verified height.

**Remaining gap.** A finite interval of positive coefficients permits a later sign failure. To obtain all-order positivity by this argument one would need control beyond every established height.

## Uniform two-term formula in the longer range

Under the density refinement's hypotheses, uniformly for $T^2<n\le M_A$ as $T\to\infty$,
$$
 \lambda_n=\tfrac12 n\log n+\tfrac12(\gamma_E-1-\log(2\pi))n+o(n).
$$
Here $\gamma_E$ denotes Euler's constant. Put $\phi_0(t)=2\arctan(1/(2t))$ and
$$L_n^0=2\sum_{\gamma>0}(1-\cos(n\phi_0(\gamma))).$$
This sum uses every actual ordinate, with each projected to real part $1/2$. Under $\mathrm{RH}(T)$ the difference from $\lambda_n$ is supported above $T$. There $\phi=\arctan(\beta/\gamma)+\arctan((1-\beta)/\gamma)$, and $0\le u-\arctan u\le u^3/3$ shows $|\phi-\phi_0|\ll\gamma^{-3}$ uniformly. The counting bound gives $\sum_{\gamma>T}\gamma^{-3}\ll T^{-2}\log T$ by summing over dyadic blocks. Thus
$$
 |\lambda_n-L_n^0|\le 2\sum_{\gamma>T}(\cosh(na)-1)+O(nT^{-2}\log T)=o(n)
$$
by the preceding full-tail estimates and $n>T^2$.

For completeness, write $N(t)=(t/(2\pi))\log(t/(2\pi e))+O(\log t)$ for $t\ge 2$. In computing $L_n^0$, discard the ordinates at most $\sqrt n$ at cost $O(\sqrt n\log n)$. On the rest replace $\phi_0(t)$ by $1/t$ at cost $O(n\sum_{\gamma>\sqrt n}\gamma^{-3})=O(\log n)$. Stieltjes integration by parts against the counting error on $(\sqrt n,\infty)$ costs $O(\log n+n\int_{\sqrt n}^\infty t^{-2}\log t\,dt)=O(\sqrt n\log n)$. Extending the resulting integral to $0$ costs $O(\sqrt n\log n)$, since $\int_0^{\sqrt n}|\log(t/(2\pi))|\,dt$ has that order. Consequently
$$
 L_n^0={1\over\pi}\int_0^\infty (1-\cos(n/t))\log(t/(2\pi))\,dt+O(\sqrt n\log n).
$$
Substitute $u=n/t$. The required Mellin integrals follow from
$$
 J(\alpha)=\int_0^\infty (1-\cos u)u^{-1-\alpha}\,du
 ={\pi\over2\Gamma(1+\alpha)\sin(\pi\alpha/2)}\qquad(0<\alpha<2).
$$
For instance, insert the Laplace integral for $u^{-1-\alpha}$, integrate in $u$, and evaluate the remaining beta integral. Differentiation at $\alpha=1$ gives $J(1)=\pi/2$ and $-J'(1)=(\pi/2)(1-\gamma_E)$. This evaluates the integral and proves the formula.

The same positivity and two-term conclusions hold if $A\log\log T$ in $M_A/T^2$ is replaced by $B(\log T/\log\log T)^{1/3}$ for some fixed absolute $B>0$. The extra factor in the near-height estimate is then at most $\exp\{(B/2)(\log T/\log\log T)^{1/3}\}$, which is absorbed when $B/2<4b/3$. In the two preceding height and real-part estimates this factor is $T^{o(1)}$.

**Verification record.** The arguments are analytic. The verified-height numerical horizon is rounded down from $2T^2\log T$. The density input was checked directly against equation (1.5) and its correction footnote in the primary PDF, SHA-256 fb11226af17a06d9246120d827abe98bec817ecec23554573d6b84110b4c3303. Its right side is $965(3H)^{8(1-\sigma)/3}(\log H)^{5-2\sigma}+51.5(\log H)^2$. [Kadiri, Lumley and Ng](https://arxiv.org/pdf/2101.12263)
