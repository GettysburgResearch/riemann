# Deterministic comparison with Weingartner's saddle integral

Let $b(v)=-\log(1-1/v)$ for $v\ge2$ and define
$$
 W_0(s)=\int_2^\infty\log\left(1+\frac{e^{s b(v)}-1}{v}\right)\frac{dv}{\log v},
 \qquad
 c=\gamma+\log\log 2-\int_2^\infty\left(b(v)-\frac1v\right)\frac{dv}{\log v}.
$$
Here $W_0$ is a logarithmic moment, distinct from Weingartner's moment product $W$. For $y=\exp(te^{-\gamma})\to\infty$, put $J_y=[y\log y-y,y\log y+y]$. Weingartner's equation (3) uses exactly
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
