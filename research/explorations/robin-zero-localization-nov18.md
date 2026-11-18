# A uniform zero-tail estimate for the tangent form of Robin's inequality

**Proposed asymptotic theorem.** Let $y=\log n$, $L=\log y$ and $\Phi(y)=(L/\log L)^{1/3}$. There are effectively determinable absolute constants $a,c>0$ such that, for all sufficiently large $y$, with $H=y^{1/4}e^{-a\Phi(y)}$,

$$
 \sum_{|\Im\rho|>H}\frac{y^{(\Re\rho-1/2)_+}}{(\Im\rho)^2}
 \ll e^{-c\Phi(y)} .                                           \tag{1}
$$

Here zeros have their actual multiplicities and both ordinate signs are counted. The assertion is unconditional. No numerical threshold for its asymptotic range is claimed. Define $d(y)=L\max_{0<|\Im\rho|\le H}|\Re\rho-1/2|$. Then uniformly over integers in this range,

$$
 \sqrt y L\log\frac{\sigma(n)}{e^\gamma n\log y}
 \le 2-2\sqrt2 +0.047(1+1/L)\cosh d(y)+O(1/L).                \tag{2}
$$

In particular, a sufficiently large Robin violation requires a zero at height at most $H$ with $|\Re\rho-1/2|>3.55/L$. The point is the absolute bound on the full signed-height tail in (1) and the explicit dependence on the width of the remaining zero strip in (2). The constants and the starting threshold depend only on the classical distribution estimates used below.

## Density and the zero-free region

We use the classical Ingham density bound, uniformly on $1/2\le s\le1$,

$$
 N(s,T)\ll T^{d(s)}(\log T)^5,\qquad d(s)=3(1-s)/(2-s),
$$

where $N(s,T)$ counts the positive ordinates up to $T$ with real part strictly greater than $s$. The explicit Table 1 form of Chourasiya–Simonič also suffices. The Vinogradov–Korobov zero-free region supplies an absolute $b>0$ with $\Re\rho\le 1-b/[(\log|\Im\rho|)^{2/3}(\log\log|\Im\rho|)^{1/3}]$ for sufficiently high zeros. Both inputs admit effective constants. [Explicit density theorem](https://arxiv.org/abs/2507.15184) · [Explicit zero-free regions, Mossinghoff–Trudgian–Yang](https://doi.org/10.1007/s40993-023-00498-y)

By the ordinary zero count the terms with $|\Im\rho|>y$ cost $O((\log y)/\sqrt y)$ using $y^{(\Re\rho-1/2)_+}\le\sqrt y$. On the remaining dyadic intervals $T<|\Im\rho|\le2T$, $H\le T\le y$, every zero has real part at most $1-\delta$ where $\delta\ge b'\Phi(y)/L$ for some effective $b'>0$. Applying the layer identity $y^{(\beta-1/2)_+}=1+\int_{1/2}^1 L y^{s-1/2}1_{\beta>s}\,ds$ and dividing by $T^2$, the constant part across all intervals costs $O((\log H)/H)$. The remaining integrands up to factors $O(L^6)$ are bounded by

$$
 y^{s-1/2}T^{d(s)-2}
 \le e^{2a\Phi(y)}y^{s-1+d(s)/4}
 \le e^{2a\Phi(y)}y^{-(1-s)/4}.
$$

Indeed $d(s)\le1$, $T\ge H$, and $d(s)\le3(1-s)$. For the active $s\le1-\delta$ the bound is at most $\exp[(2a-b'/4)\Phi(y)]$. Choose $a<b'/16$. The number of dyadic intervals is $O(L)$, and all fixed powers of $L$ are absorbed into the exponential by reducing $c$. This proves (1).

## From a zero tube to an arithmetic bound

The [free tangent inequality](robin-tangent-nov18.md) at the unshifted point $v=y$ gives the left side of (2) bounded above by $\sqrt y L[-K(y)-A(y)]$. Its [integrated explicit formula](robin-finite-horizon-nov18.md) gives for the zero part the upper bound

$$
 (1+1/L)\sum_{\rho}\frac{y^{\Re\rho-1/2}}{|\rho||1-\rho|}.
$$

The terms with $|\Im\rho|>H$ cost (1). The remaining terms can be reflected by $\rho\mapsto1-\bar\rho$ inside the cutoff, without changing the denominator. Thus their total is at most $\cosh(d(y))\sum_{\rho}1/(|\rho||1-\rho|)$. The latter sum is below $0.047$. In fact the exact signed sum of $1/(\rho(1-\rho))$ is $2+\gamma-\log(4\pi)<0.0462$ and every real part is positive. For a zero on the line, its modulus equals its real part. All zeros off the line have height greater than $3\cdot10^{12}$ by the imported finite verification. Their ratio of modulus to real part is at most $\sqrt{1+(\Im\rho)^{-2}}$, because the real part of $\rho(1-\rho)$ is at least $(\Im\rho)^2$ and its imaginary part has modulus at most $|\Im\rho|$. These bounds justify the stated constant without assuming RH.

For the remaining terms, the archimedean contribution is $O(y^{-1/2})$ after scaling. The prime powers satisfy $\psi(t)-\vartheta(t)=\sqrt t[1+O((\log t)^{-2})]$ uniformly for $t\ge y$: use the quantitative PNT for $\vartheta(\sqrt t)$ and $O(t^{1/3}\log t)$ for the higher powers. The elementary integral $F_{1/2}(y)$ in the explicit formula therefore gives a scaled prime-power contribution $2+O(1/L)$. Finally let $q>1$ solve $q^2\log q=yL$ as in the [smoothed proof](robin-smoothed-nov18.md). Then $q/\sqrt y=\sqrt2+O(1/L)$. The prime count at $q$ and partial summation on $(q,y/2]$, with quantitative PNT relative error $O(1/L^2)$, give $\sqrt y L A(y)\ge 2\sqrt2-O(1/L)$. Indeed the initial part is $(1+O(L^{-2}))q/\sqrt y$ and the integral part is at least $(1-O(L^{-1}))\sqrt y L/(q\log q)-O(y^{-1/2})$, with $\sqrt y L/(q\log q)=q/\sqrt y$. This proves (2). Since $0.047\cosh(3.55)<0.819<2\sqrt2-2$, the stated necessary zero follows.

## Transport to a Weil window

Under the proven implications above and the proposed [cluster capture theorem](weil-contour-nov18.md), a sufficiently large violating $n$ would admit a compact smooth test with negative Weil form, capturing an actual cluster of the localized zeros and its conjugate. Its support radius is at most

$$
 \tfrac18\log y-\tfrac a2\Phi(y)-\tfrac12\log(2\pi)+o(1).
$$

Indeed for the specified defect its height $T$ satisfies $100<T\le H$ by the finite zero census, while its horizontal distance is at least $3.55/L$. The error parameter in the capture theorem is at most $\log H\,(1+\log L)$. Substitution into its monotone upper bound for $e^{2\,\mathrm{radius}}$ gives $H/(2\pi)+o(H)$. This argument neither supplies a violating integer nor establishes unbounded Weil positivity.
