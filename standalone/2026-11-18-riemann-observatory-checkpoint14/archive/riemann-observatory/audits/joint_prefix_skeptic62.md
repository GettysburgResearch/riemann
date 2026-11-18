# Independent audit of the joint finite-prefix limits

Let $m$ be a positive integer, $0\le b<1$, $s=b/(1-b)$, and $a=1+2s$. The starting identity is $c_m(b)=m^2+2\int_1^a[P'_{m-1}(x)]^2\,dx$. Both proposed limits hold. The bounded transition has a uniform absolute error $O_R(m^{-1})$ for $r=m^2s\in[0,R]$. The relative Legendre asymptotic holds along every joint limit $m\to\infty$ with $m\sqrt b\to\infty$. The crossover computation below also bounds the extent of the Bessel approximation. [Finite identity](prefix_skeptic62.md)

## Bounded transition

Write $G_m(t)=2P'_{m-1}(1+2t)$. The exact integral is
$$
\frac{c_m(b)}{m^2}=1+\int_0^r \left(\frac{G_m(v/m^2)}{m^2}\right)^2\,dv.
$$
Rodrigues' expansion at 1 gives
$$
\frac{G_m(v/m^2)}{m^2}
=\sum_{j=0}^{m-2}\frac{v^j}{j!(j+1)!}
\prod_{\ell=0}^j\left(1-\frac1m-\frac{\ell(\ell+1)}{m^2}\right).
$$
The product lies in $[0,1]$. Its defect from 1 is at most
$(j+1)/m+j(j+1)(j+2)/(3m^2)$, by summing the factor defects. For the omitted terms $j\ge m-1$, the coefficient defect is 1 and $(j+1)/m\ge1$. Thus the power series is within $O_R(1/m)$ of $H(v)=\sum_{j\ge0}v^j/[j!(j+1)!]$ uniformly on $[0,R]$. The finite series and $H$ are bounded by $H(R)$. After squaring and integrating,
$$
\frac{c_m(b)}{m^2}=\Phi(r)+O_R(m^{-1}),\qquad
\Phi(r)=I_0(2\sqrt r)^2-I_1(2\sqrt r)^2.
$$
Indeed $H(v)=I_1(2\sqrt v)/\sqrt v$, extended to $H(0)=1$, and the Bessel differentiation formulas give $\Phi'(v)=H(v)^2$ for $v>0$ and $\Phi(0)=1$.

The same coefficient argument sharpens the result in the natural coordinate $r_*=m(m-1)s$. After rescaling $G_m$ by $m(m-1)$, the product becomes $\prod_{\ell=0}^j(1-\ell(\ell+1)/[m(m-1)])$. The bound $j(j+1)(j+2)/[3m(m-1)]$ on its defect is at least 1 for the omitted terms when $m\ge2$. Therefore $(c_m-m^2)/[m(m-1)]=\Phi(r_*)-1+O_R(m^{-2})$ on $r_*\in[0,R]$.

## Uniform relative asymptotic

Put $n=m-1$ and $u=\operatorname{arcosh}a=2\operatorname{arctanh}\sqrt b$. The condition $m\sqrt b\to\infty$ is equivalent to $n\min(u,1)\to\infty$, since $\min(2\operatorname{arctanh}x,1)$ is comparable to $x$ on $0<x<1$. For $v>0$ define $q(v)=e^{-v}\sinh v=(1-e^{-2v})/2$. Differentiating the Legendre Laplace integral in $v$, before dividing by $\sinh v$, gives
$$
\frac{d}{dv}P_n(\cosh v)
=\frac{ne^{nv}}{\pi}\int_0^\pi
 [1-q(v)(1-\cos\theta)]^{n-1}
 [1-(q(v)+q'(v))(1-\cos\theta)]\,d\theta .
$$
The second bracket has absolute value at most 1 for all $v>0$ and $\theta\in[0,\pi]$, since $q+q'=(1+e^{-2v})/2\in[1/2,1]$. This form controls the derivative even when $v\to\infty$. Write $N=(n-1)q(v)$ and set $y=\sqrt N\,\theta$. For each bounded $y$, the first factor tends uniformly to $e^{-y^2/2}$ as $N\to\infty$ and the second tends uniformly to 1. Indeed $1-\cos\theta=\theta^2/2+O(\theta^4)$ and $q\le 1/2$. The rescaled integrand, extended by zero beyond $\pi\sqrt N$, is dominated by $e^{-2y^2/\pi^2}$, using $1-\cos\theta\ge2\theta^2/\pi^2$ and $1-t\le e^{-t}$. Therefore the integral is $\sqrt{\pi/(2N)}(1+o(1))$ uniformly as $N\to\infty$. After dividing by $\sinh v$, this yields
$$
2[P_n'(\cosh v)]^2\,\sinh v
=\frac n\pi \frac{e^{(2n+1)v}}{\sinh^2 v}(1+o(1)).
$$
On $u/2\le v\le u$ the error is uniform, as $q(v)$ is bounded below by a positive constant times $\min(u,1)$.

To integrate the main term put $\lambda=2n+1$ and $f(v)=\sinh^{-2}v$. For $0\le h\le u/2$, $1\le f(u-h)/f(u)\le e^{2\coth(u/2)h}$. Here $\coth(u/2)=O(1/\min(u,1))=o(\lambda)$ and $\lambda u\to\infty$. Integrating $e^{-\lambda h}$ times these bounds gives
$$
\int_{u/2}^u e^{\lambda v} f(v)\,dv
\sim \frac{e^{\lambda u}}{\lambda\sinh^2u}.
$$

For the initial interval its contribution to $c_m$ is at most $2(\cosh(u/2)-1)[P_n'(\cosh(u/2))]^2$. This follows from the nonnegative Taylor coefficients of $P_n'$ at 1. The above derivative estimate applies at $u/2$. Dividing the bound by $e^{\lambda u}/(2\pi\sinh^2u)$ gives
$$
O\!\left(n(\cosh(u/2)-1)\frac{\sinh^2u}{\sinh^3(u/2)}e^{-\lambda u/2}\right)
=O\!\left(n\min(u,1)e^{-(n-1/2)u}\right)=o(1).
$$
For the equality of the two bounds use $(\cosh t-1)\sinh^2(2t)/\sinh^3t=4\tanh(t/2)\cosh^2t$ at $t=u/2$. The additive $m^2$ has relative size $O((nu)^2e^{-(2n-1)u})=o(1)$ by $\sinh u\le u e^u$. Combining intervals and $n/\lambda\to1/2$ proves
$$
c_m(b)\sim\frac{e^{(2n+1)u}}{2\pi\sinh^2u}
=\frac{(1-b)^2}{8\pi b}
\left(\frac{1+\sqrt b}{1-\sqrt b}\right)^{2m-1}.
$$
The conditions in this proof control both the derivative asymptotic and the lower interval along sequences with $b\to0$ or $b\to1$.

## Extent of the Bessel approximation

For $r\to\infty$, $\Phi(r)\sim e^{4\sqrt r}/(8\pi r)$. One derivation uses $I_0(z)\pm I_1(z)=\pi^{-1}\int_0^\pi e^{z\cos\theta}(1\pm\cos\theta)\,d\theta$ at $z=2\sqrt r$. Laplace's method gives $I_0+I_1\sim 2e^z/\sqrt{2\pi z}$ and $I_0-I_1\sim e^z/(2z\sqrt{2\pi z})$. Thus the product has leading term $e^{2z}/(2\pi z^2)$.

In the joint limit $r\to\infty$ and $m\to\infty$, one has $m\sqrt b\to\infty$. The uniform relative Legendre result, with $u=2\operatorname{arsinh}(\sqrt r/m)$, consequently gives
$$
\frac{c_m(b)/m^2}{\Phi(r)}
\sim \frac{\exp[(4m-2)\operatorname{arsinh}(\sqrt r/m)-4\sqrt r]}{1+r/m^2}.
$$
In particular the ratio tends to 1 when $r\to\infty$ with $r=o(m^{4/3})$. If instead $r\sim Lm^{4/3}$ for fixed $L>0$, the cubic term in $\operatorname{arsinh}x=x-x^3/6+O(x^5)$ gives the limit $e^{-(2/3)L^{3/2}}$. This supplies a counterexample to a relative $1+o(1)$ Bessel approximation on that wider scale. If $r/m^{4/3}\to\infty$, the ratio tends to zero. To see this, put $x=\sqrt r/m$ and use $x-\operatorname{arsinh}x=\int_0^x[1-(1+t^2)^{-1/2}]\,dt\ge c\min(x^3,x)$ for an absolute $c>0$. Then $m\min(x^3,x)\to\infty$.

The numerical diagnostics evaluate the original finite Taylor square with 55-digit arithmetic. For $m=512$, the Legendre ratios are approximately $1.0056836758$, $1.0005196189$, and $1.0004898358$ along $b=1/m$, $b=1/2$, and $b=1-2^{-m}$, respectively. Evaluating the last path via $s=2^m-1$ avoids subtraction near 1. These are finite-cost results. An arithmetic moving-prefix estimate would require control of the arithmetic remainder along the corresponding joint limit. [Reproduction script](../scripts/joint_prefix_skeptic62.py)
