# Two uniform regimes for the finite Legendre prefix cost

Start from the finite Gram formula independently reconstructed in [the director’s prefix review](director_prefix_cost_round6.md). For integer $m\ge1$ and $0\le b<1$, write $a=(1+b)/(1-b)$, $n=m-1$ and
$$
 c_m(b)=m^2+2\int_1^a P_n'(x)^2\,dx .
$$
Here $P_n(1)=1$. The results below concern the finite Gram cost. The arithmetic approximation problem has additional uniformity requirements.

## Bounded transition

Put $r=m^2b/(1-b)$ and define
$$
 \Phi(r)=I_0(2\sqrt r)^2-I_1(2\sqrt r)^2.
$$
For every $R\ge0$, uniformly for $0\le r\le R$ and $m\ge2$,
$$
 \left|\frac{c_m(b)}{m^2}-\Phi(r)\right|
 \le \frac{2R}{m}H(R)J(R),\qquad
 H(R)=\sum_{j\ge0}\frac{R^j}{j!(j+1)!},\quad
 J(R)=\sum_{j\ge0}\frac{[(j+1)+j(j+1)(j+2)/6]R^j}{j!(j+1)!}.
 \tag{1}
$$
In particular if $m\sqrt b\to\lambda<\infty$ as $m\to\infty$, then $c_m(b)/m^2\to\Phi(\lambda^2)$. At $b=0$ the normalized cost and $\Phi(0)$ equal 1 exactly.

To prove (1), set $G_m(s)=2P_{m-1}'(1+2s)$. The change of variables $t=m^2(x-1)/2$ in the exact integral gives
$$
 \frac{c_m(b)}{m^2}=1+\int_0^r H_m(t)^2\,dt,\qquad
 H_m(t)=m^{-2}G_m(t/m^2).
$$
The exact Legendre coefficient formula gives
$$
 H_m(t)=\sum_{j=0}^{m-2}
 \frac{t^j}{j!(j+1)!}\left(1-\frac1m\right)
 \prod_{i=0}^{j-1}\left(1-\frac1m-\frac{(i+1)(i+2)}{m^2}\right).
$$
All factors belong to $[0,1]$ on the indicated index range. The product bound $1-\prod_k(1-\varepsilon_k)\le\sum_k\varepsilon_k$ gives for $j\le m-2$ a coefficient defect at most
$$
 \frac{j+1}{m}+\frac{j(j+1)(j+2)}{3m^2}.
$$
For $j\ge m-1$ the coefficient defect equals 1. Thus for all $j$ it is bounded by $[(j+1)+j(j+1)(j+2)/6]/m$ when $m\ge2$, using $m^{-2}\le (2m)^{-1}$, and $(j+1)/m\ge1$ past the truncation. Since $0\le H_m(t)\le H(t)\le H(R)$, the bound on the difference of squares is $2H(R)J(R)/m$. Integrating proves (1). The natural Taylor parameter $m(m-1)s$ gives a sharper error.

Let $\widetilde H_m(t)=G_m(t/[m(m-1)])/ [m(m-1)]$. Its $j$-th factor relative to the coefficient of $H$ is $\prod_{i<j}(1-(i+1)(i+2)/[m(m-1)])$. The defect for $j\le m-2$ is bounded by $j(j+1)(j+2)/[3m(m-1)]$. The same bound is at least 1 for every $j\ge m-1$ when $m\ge2$. Hence for $m\ge2$,
$$
 0\le H(t)-\widetilde H_m(t)\le
 \frac{J_3(R)}{3m(m-1)},\qquad
 J_3(R)=\sum_{j\ge0}\frac{j(j+1)(j+2)R^j}{j!(j+1)!}.
$$
This gives a second, sharper transition statement if one keeps the natural parameter and normalization. With $r_*=m(m-1)b/(1-b)$, uniformly for $0\le r_*\le R$,
$$
 \left|\frac{c_m(b)-m^2}{m(m-1)}
       -(\Phi(r_*)-1)\right|
 \le \frac{2R H(R)J_3(R)}{3m(m-1)},\qquad m\ge2 .
 \tag{2}
$$


Finally $H(t)=I_1(2\sqrt t)/\sqrt t$ for $t>0$, continued by $H(0)=1$. From the power series $I_0'=I_1$ and $I_1'=I_0-I_1/x$, so $\frac{d}{dx}(I_0(x)^2-I_1(x)^2)=2I_1(x)^2/x$. Substituting $x=2\sqrt t$ proves $1+\int_0^r H(t)^2dt=\Phi(r)$, including $r=0$ by continuity.

## Growing transition parameter

For $0<b<1$, put
$$
 u=\operatorname{arcosh}a=2\operatorname{arctanh}\sqrt b,\qquad
 \eta=\min(u,1),\qquad \lambda=2n+1 .
$$
There are absolute constants $A_0,C$ such that if $n\eta\ge A_0$,
$$
 c_m(b)=\frac{e^{(2n+1)u}}{2\pi\sinh^2u}
 \left[1+O\!\left(\frac1{n\eta}\right)\right],
 \qquad
 \left|O\!\left(\frac1{n\eta}\right)\right|\le\frac C{n\eta}.
 \tag{3}
$$
In terms of $b$ the prefactor is
$$
 \frac{(1-b)^2}{8\pi b}
 \left(\frac{1+\sqrt b}{1-\sqrt b}\right)^{2m-1}.
$$
The threshold $n\eta\to\infty$ is equivalent to $m\sqrt b\to\infty$ for $m\to\infty$, since $\min(2\operatorname{arctanh}\sqrt b,1)$ is bounded above and below by fixed positive multiples of $\sqrt b$. Thus (3) includes $b\to1$, fixed positive $b$, and $b\to0$ above the bounded transition scale. The formula (3) excludes $b=0$ because its prefactor contains $1/b$.

For the proof, use the positive integral representation
$$
 P_n(\cosh v)=\frac{e^{nv}}{\pi}\int_0^\pi
 B(v,\theta)^n\,d\theta,\qquad
 B(v,\theta)=1-q(v)\sin^2(\theta/2),\quad q(v)=1-e^{-2v}.
$$
Uniformly for $0<q\le1$ and $nq$ large,
$$
 \int_0^\pi (1-q\sin^2(\theta/2))^n\,d\theta
 =\frac{\sqrt\pi}{\sqrt{nq}}
   \left[1+O\!\left(\frac1{nq}\right)\right].
 \tag{4}
$$
Indeed, on $0\le\theta\le1$ the exponent differs from $-nq\theta^2/4$ by $O(nq\theta^4)$ uniformly in $q$. Both exponents are bounded above by $-c\,nq\theta^2$ for an absolute $c>0$. The mean-value inequality for the exponential bounds the integrated error there by $C\,nq\int_0^\infty\theta^4e^{-c\,nq\theta^2}\,d\theta=O((nq)^{-3/2})$. On $1\le\theta\le\pi$ the integrand is at most $\exp[-nq\sin^2(1/2)]$, and the omitted Gaussian tail has the same type of exponential bound. This proves (4).

Differentiate with respect to $v$ under the integral. The integrand is multiplied by $n$ times
$$
 T(v,\theta)=
 \frac{\sinh v+\cosh v\cos\theta}{\cosh v+\sinh v\cos\theta}.
$$
The denominator is positive, and subtracting the squared numerator from its square gives $\sin^2\theta$, so $|T|\le1$. Moreover $1-T=2e^{-2v}\sin^2(\theta/2)/B(v,\theta)$, which is $O(\theta^2)$ uniformly on $0\le\theta\le1$. The weighted integral thus has the same leading term and relative error as (4). Using $d(\cosh v)/dv=\sinh v$ and $q(v)=2e^{-v}\sinh v$ yields
$$
 2 P_n'(\cosh v)^2\,\sinh v
 =\frac{n}{\pi}\frac{e^{(2n+1)v}}{\sinh^2v}
 \left[1+O\!\left(\frac1{nq(v)}\right)\right].
 \tag{5}
$$

Apply (5) on $u/2\le v\le u$, where $q(v)\ge c\eta$. Put $f(v)=\sinh^{-2}v$. The logarithmic derivative satisfies $|f'(v)|/f(v)\le2\coth(u/2)\le C_1/\eta$. Hence, writing $h=u-v$, the factor $f(u-h)/f(u)$ lies between $1$ and $e^{C_1h/\eta}$. Integration against $e^{-\lambda h}$ on $0\le h\le u/2$ and comparison with the integrals on $[0,\infty)$ give
$$
 \int_{u/2}^u e^{\lambda v} f(v)\,dv
 =\frac{e^{\lambda u} f(u)}{\lambda}
 \left[1+O\!\left(\frac1{n\eta}+e^{-\lambda u/2}\right)\right].
$$
Together with (5) and $n/\lambda=\tfrac12[1+O(1/n)]$, this gives the main term in (3).

The initial interval is bounded by $2(\cosh(u/2)-1)P_n'(\cosh(u/2))^2$, using the positive Taylor coefficients of $P_n'(x)$ about $x=1$. Estimate this value by (5). Relative to $e^{\lambda u}/(2\pi\sinh^2u)$ the bound is
$$
 C n(\cosh(u/2)-1)\frac{\sinh^2u}{\sinh^3(u/2)}e^{-\lambda u/2}
 \le
 \begin{cases}
 C n u\, e^{-nu},&0<u\le1,\\
 C n\,e^{-(n-1/2)u},&u\ge1 .
 \end{cases}
$$
The estimate follows by comparing hyperbolic functions with their arguments on the bounded interval and with exponentials above $u=1$. Relative to the same main term, the baseline $m^2$ has size $O((nu)^2e^{-2nu})$ for $u\le1$ and $O(n^2e^{-(2n-1)u})$ for $u\ge1$. These bounds fit the error in (3). No asymptotic step here estimates the arithmetic errors of a moving prefix.

## Relative matching and its boundary

For $m\to\infty$ and $r=m^2b/(1-b)\to\infty$, set $z=\sqrt r/m$. Equations (1) and (3) describe different regions. Their matching can be measured by the precise comparison
$$
 \frac{c_m(b)/m^2}{\Phi(r)}
 =
 \frac{\exp\{(4m-2)\operatorname{arsinh}z-4\sqrt r\}}{1+z^2}
 \left[1+O\!\left(\frac1{\min(m,\sqrt r)}\right)\right].
 \tag{6}
$$
The error is uniform once $\min(m,\sqrt r)$ exceeds an absolute threshold. In fact, $b=r/(m^2+r)$ implies $u=2\operatorname{arsinh}z$ and $(1-b)^2/(bm^2)=1/[r(1+z^2)]$. The error in (3) has the claimed order because $n\min(u,1)$ is comparable to $\min(m,\sqrt r)$ when $m\ge2$.

For the denominator, writing $x=2\sqrt r$ yields
$$
 \Phi(r)=1+2\int_0^x I_1(v)^2\,\frac{dv}{v}
        =\frac{e^{2x}}{2\pi x^2}\bigl[1+O(1/x)\bigr]
        =\frac{e^{4\sqrt r}}{8\pi r}\bigl[1+O(r^{-1/2})\bigr].
$$
Indeed $I_1(v)=\pi^{-1}\int_0^\pi e^{v\cos\theta}\cos\theta\,d\theta=e^v(2\pi v)^{-1/2}[1+O(v^{-1})]$ for $v\ge1$. The Gaussian error follows by bounding the local phase error by $Cv\theta^4$, the amplitude error by $C\theta^2$, and the integrand away from zero by an exponential smaller than $e^v$. On $[x/2,x]$, elementary endpoint integration of $e^{2v}/(\pi v^2)$ gives $e^{2x}/(2\pi x^2)[1+O(x^{-1})]$. For example, the logarithmic derivative of $v^{-2}$ there is bounded by $4/x$. The other part is exponentially smaller by the same growth bound for $v\ge1$ and by the power series near $v=0$. Combining this estimate with (3) proves (6).

For bounded $z$ tending to zero, Taylor expansion gives
$$
 (4m-2)\operatorname{arsinh}z-4\sqrt r
 =-2z-\frac23\,\frac{r^{3/2}}{m^2}+O(z^3+m z^5).
$$
Consequently, as $m\to\infty$, the Bessel approximation has relative ratio tending to 1 throughout $r=o(m^{4/3})$. For bounded $r$ this follows directly from (1) and $\Phi(r)\ge1$, including $r=0$. For diverging $r$ it follows from (6) and Taylor expansion. If $r/m^{4/3}\to\alpha\in(0,\infty)$, the relative ratio instead tends to $\exp[-2\alpha^{3/2}/3]$. At $\alpha=0$, the relative ratio tends to 1 by the subcritical result, whether or not $r$ diverges.

If $r/m^{4/3}\to\infty$, the relative ratio tends to 0. For every $z>0$ there is an absolute $c>0$ such that $z-\operatorname{arsinh}z\ge c\min(z^3,z)$. Integrate $1-(1+t^2)^{-1/2}$ on $[0,z]$ and bound it below by a constant times $t^2$ when $z\le1$, or on $[z/2,z]$ by a positive constant when $z\ge1$. Thus the exponent in (6) tends to $-\infty$, because $m\min(z^3,z)$ tends to infinity under the stated assumption. This identifies the boundary for relative Bessel matching in the finite cost.
