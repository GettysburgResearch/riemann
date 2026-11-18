# Deterministic comparison with Weingartner's saddle integral

Let $b(v)=-\log(1-1/v)$ for $v\ge2$ and define
$$
 W_0(s)=\int_2^\infty\log\left(1+\frac{e^{s b(v)}-1}{v}\right)\frac{dv}{\log v},
 \qquad
 c=\gamma+\log\log 2-\int_2^\infty\left(b(v)-\frac1v\right)\frac{dv}{\log v}.
$$
Here $W_0$ is a deterministic integral of local log moments, distinct from Weingartner's moment product $W$. For $y=\exp(te^{-\gamma})\to\infty$, put $J_y=[y\log y-y,y\log y+y]$. Weingartner's equation (3) uses exactly
$$
 I(y,s)=\int_e^y\log(1+v e^{-s/v})\frac{dv}{\log v}
 +\int_y^{y\log y}\log(1+v^{-1}e^{s/v})\frac{dv}{\log v}.
$$
Then
$$
 \inf_{s\in\mathbb R}\{W_0(s)+cs-s\log t\}
 =-y+\min_{s\in J_y} I(y,s)+O(1).
 \tag{1}
$$
The same infimum results if one restricts to $s\ge0$ or $s\ge e$ for large $t$. [Weingartner, Theorem 2 and equation (3)](https://arxiv.org/abs/1011.4262)

## Uniform comparison in the saddle bracket

Since $\log t=\gamma+\log\log y$, the part below $y$ satisfies
$$
 \int_2^y\frac{sb(v)-\log v}{\log v}\,dv+cs-s\log t
 =-y+2-s\int_y^\infty (b(v)-1/v)\frac{dv}{\log v}=-y+O(1)
$$
uniformly for $s\in J_y$, using $0\le b(v)-1/v\ll v^{-2}$. The remaining integrand below $y$ is exactly $\log(1+(v-1)e^{-sb(v)})$. On $2\le v\le y/2$ this and $\log(1+v e^{-s/v})$ are $O(1/y)$, since $s\ge y(\log y-1)$. This also absorbs the change from lower endpoint $2$ to $e$. On $y/2\le v\le y$ the difference is
$$
 O\big(|\log(v-1)-\log v|+s|b(v)-1/v|\big)
 \ll v^{-1}+s v^{-2},
$$
by the unit Lipschitz bound for $z\mapsto\log(1+e^z)$ on the real line. Its integral against $dv/\log v$ is $O(1)$.

Above $y$, through $y\log y$, first restore the omitted $1/v$ inside the logarithm at a cost $O(1/v)$, since the original log argument is at least one. Replacing $e^{s b(v)}$ by $e^{s/v}$ then has the same $O(sv^{-2})$ Lipschitz cost. Integrating gives $O(1)$: the $1/v$ term is $O((\log\log y)/\log y)$ on this interval. Above $y\log y$, one has $0\le s b(v)\ll1$, so the original integrand is $O(s/v^2)$ and its integral is $O(1/\log y)$. This proves
$$
 W_0(s)+cs-s\log t=-y+I(y,s)+O(1)
$$
throughout $J_y$.

## The unique minimizer lies in the bracket

Differentiation under the integral gives, for real $s$,
$$
 W_0'(s)=\int_2^\infty \frac{b(v)}{1+(v-1)e^{-s b(v)}}\frac{dv}{\log v},\qquad
 W_0''(s)>0 .
$$
These differentiations are justified locally uniformly since the tails have integrable majorants. For $s=x\log x$, let $H(v)=\log(v-1)-s b(v)$, $f(w)=(1+e^w)^{-1}$. We show
$$
 W_0'(x\log x)+c=\gamma+\log\log x+o((\log x)^{-2}).
 \tag{2}
$$
Subtract the truncated integral over $2\le v\le x$ of $b(v)/\log v$. The remainder is the integral with factor $f(H(v))-\mathbf1_{v\le x}$. For $v\le x/2$ the absolute factor is $O(1/x)$ and its weighted integral is $O(\log\log x/x)$. For $v\ge2x$ it is $O(x^{1/2+o(1)}/v)$, contributing $O(x^{-1/2+o(1)})$.

On $[x/2,2x]$ change to $u=(v-x)\log x/x$. Here $H(x)=O((\log x)/x)$ and
$$
 H'(v)=1/(v-1)+s/(v(v-1))\asymp (\log x)/x .
$$
Thus the absolute residual is $\ll e^{-c_1|u|}$ uniformly. For fixed $u$, $H(v)\to u$ and $(\log x)^2 b(v)\,dv/\log v=(1+o(1))\,du$. The normalized weight is bounded on the entire comparison interval. Dominated convergence yields the normalized residual
$$
 \int_{\mathbb R}\big(f(u)-\mathbf 1_{u<0}\big)\,du+o(1)=o(1),
$$
by antisymmetry away from zero. Finally the truncated base integral plus $c$ is $\gamma+\log\log x-\int_x^\infty(b(v)-1/v)dv/\log v$, whose last term is $O(1/(x\log x))$. This proves (2).

Let $x_\pm\log x_\pm=y\log y\pm y$. The mean value theorem gives $x_\pm/y=1\pm1/\log y+O((\log y)^{-2})$, whence $\log\log x_\pm-\log\log y=\pm(\log y)^{-2}+O((\log y)^{-3})$. In (2) the derivatives of $W_0(s)+(c-\log t)s$ at the endpoints of $J_y$ consequently have opposite strict signs. Strict convexity places the unique global minimizer in $J_y$. The uniform $O(1)$ comparison on this bracket proves (1).

## The bounded normalization error

One can sharpen the $O(1)$ in (1), and in its uniform integrand comparison, to the explicit additive correction
$$
 \frac32-\frac{\log\log y}{\log y}+O((\log y)^{-1}).
$$
Indeed $b(v)-1/v=1/(2v^2)+O(v^{-3})$ and an integration by parts shows that the residual main term below $y$ is $-y+3/2+O(1/\log y)$. In the lower replacement of $\log(1+(v-1)e^{-sb(v)})$ the part up to $\sqrt y$ is exponentially small and the part from $\sqrt y$ to $y/2$ is $O(1/\log y)$ by the earlier pointwise bound. On $[y/2,y]$ the exponent difference $O((\log y)/y)$ is multiplied by a logistic derivative $\ll\exp(-c(y-v)\log y/y)$, giving another $O(1/\log y)$ after integration. The analogous upper exponent replacement on $[y,2y]$ has the bound with $v-y$ in the exponent; on $[2y,y\log y]$ the logistic derivative is $O(y^{-1/2+o(1)})$, so its total cost is smaller still. These exponential bounds follow from the derivative of $\log v-s/v$, bounded below by $c\log y/y$ on $[y/2,2y]$, with endpoint value $O(1)$ at $y$.

Restoring the subtraction of $1/v$ in the upper logarithm changes it by $-1/(v+e^{sb(v)})+O(v^{-2})$. Replacing this by $-1/v$ costs $O(1/\log y)$ after integration: on $[y,2y]$ this follows even from $\int_y^{2y}dv/(v\log v)$, and on $[2y,y\log y]$ one gains an additional $O(y^{-1/2+o(1)})$. Its contribution is therefore $-\log(1+\log\log y/\log y)+O(1/\log y)$. The tail beyond $y\log y$ was already $O(1/\log y)$. All bounds are uniform in $s\in J_y$, so taking minima preserves the displayed correction.

## Explicit constants above $\log y=1100$

For all $L=\log x\ge1000$ the derivative estimate in (2) satisfies
$$
 |W_0'(xL)+c-\gamma-\log L|\le25/L^3.
 \tag{3}
$$
Here are explicit error bounds. Use $u=L\log(v/x)$ and denote $H=\log(v-1)-xLb(v)$ as before. On $|u|\le L/4$, $\log v=L+u/L$, $xL/v=L e^{-u/L}$, and
$$
 |H-u|\le (|u|+0.65u^2)/L+4Le^{-L}.
$$
This follows by Taylor's bound $|1-e^{-z}-z|\le e^{1/4}z^2/2$ and $0\le b(v)-1/v\le 1/v^2$ for $v\ge2$. The derivative $dH/du=(v+xL)/(L(v-1))\ge e^{-1/4}>0.77$, and $|H(0)|\le3Le^{-L}$. Thus for every point $w$ between $H$ and $u$, $|f'(w)|\le 1.01 e^{-0.75|u|}$. Also $|f(H)-\mathbf1_{u<0}|\le1.01e^{-0.75|u|}$, apart from the irrelevant point at zero. The normalized weight in this coordinate is $L^2 b(v)dv/\log v=R(u)du$, with
$$
 |R(u)-1|=\left|\frac{v b(v)}{1+u/L^2}-1\right|
 \le 2|u|/L^2+3e^{-L}.
$$
The integral over $[-L/4,L/4]$ of $f(u)-\mathbf1_{u<0}$ is exactly zero. The integrals there of $|f(H)-f(u)|$ and $|R-1|\,|f(H)-\mathbf1_{u<0}|$ together are bounded by $12/L$: extend the exponential majorants to the whole line and use $\int_\mathbb R (|u|+0.65u^2)e^{-0.75|u|}du<9.8$ and $\int_\mathbb R|u|e^{-0.75|u|}du<3.6$.

Below $v=xe^{-1/4}$, the error factor is at most $e^{-0.28L}$ and $\int_2^x b(v)dv/\log v\le2(\log L+1)$. Above $v=xe^{1/4}$ we have $xL b(v)\le0.78L$, so the integrated logistic tail is bounded by $4e^{-0.22L}$ using $f(H)\le2e^{0.78L}/v$ and $b(v)\le2/v$. Both tails together, multiplied by $L^2$, are below $1/L$ for $L\ge1000$; the right-hand exponential bounds decrease after multiplication by $L^3(1+\log L)$ in this range. The base correction $\int_x^\infty(b(v)-1/v)dv/\log v\le1/(xL)$ is also less than $1/L^3$. These inequalities prove (3).

Now let $\ell=\log y\ge1100$, and define $v_\pm=\log(x_\pm/y)$ at the endpoints of $J_y$. Then
$$
 e^{v_\pm}(1+v_\pm/\ell)=1\pm1/\ell,\qquad
 0.99/\ell\le |v_\pm|\le2/\ell .
$$
The second statement follows by evaluating the strictly increasing left side at $\pm0.99/\ell$ and $\pm2/\ell$; use $1+w\le e^w\le1+w+w^2$ for $|w|\le0.01$. The signed difference $\log\log x_\pm-\log\ell$ has magnitude at least $0.99/(\ell(\ell+2/\ell))>0.98/\ell^2$. By (3), the derivative signs at both endpoints are as asserted in the asymptotic proof. Thus the unique model saddle lies in $J_y$ for every $\ell\ge1100$.

Finally, the uniform error in the first integral comparison above is strictly less than 10 throughout $J_y$ in this range. The base term differs from $-y$ by at most 2 since $0\le s\int_y^\infty(b-1/v)dv/\log v\le1+1/\ell$. The lower comparison up to $y/2$ costs less than 3: both logarithms are nonnegative and individually at most $e^2/(2y)<4/y$, including the section from 2 to $e$ present in just one integral. From $y/2$ to $y$, the exponent comparison costs at most $[2\log 2+s/y]/(\ell-\log 2)<1.01$. From $y$ to $y\ell$, the two upper replacements cost at most $\log(1+\log\ell/\ell)+s/(y\ell)<1.02$. Finally $v\ge y\ell$ gives $sb(v)<1.01$ and $(e^{s b(v)}-1)/v\le 4s/v^2$, so the remaining tail costs at most $4s/(y\ell\log(y\ell))<0.01$. Taking the minima gives the explicit deterministic bound
$$
 \left|\inf_s\{W_*(s)-s\log t\}+y-\min_{s\in J_y}I(y,s)\right|<10
 \qquad(\log y\ge1100).
$$
