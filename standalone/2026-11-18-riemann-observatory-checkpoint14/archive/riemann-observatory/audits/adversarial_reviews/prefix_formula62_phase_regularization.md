# Exact Mellin regularization of a phase-transformed indicator

Let $\mathcal M f(s)=\int_0^\infty f(x)x^{s-1}\,dx$ on $s=1/2+it$, with Plancherel measure $dt/(2\pi)$. Let $U$ be a Mellin multiplier with measurable symbol $u(s)$ of modulus one almost everywhere and put $g=U\mathbf1_{(0,1)}$. Thus $\widehat g(s)=u(s)/s$ and $\|g\|_2=1$. In this note $L^2$ is complex unless a real constraint is explicitly imposed.

## Closed derivative and unique minimizer

Use the maximal distributional operator $Df=x f'(x)$ on $L^2(0,\infty;dx)$. For $y=\log x$ the unitary $Jf(y)=e^{y/2}f(e^y)$ identifies $D$ with $\partial_y-1/2$ on $H^1(\mathbb R)$. This proves closedness and shows that the closure of the derivative on compactly supported smooth functions is the same operator. With Fourier sign $e^{ity}$, its Mellin multiplier is $-s$:
$$
\operatorname{Dom}(D)=\{f:\ |s|\widehat f(s)\in L^2(dt/(2\pi))\},\qquad
\|Df\|_2^2=\int_\mathbb R (t^2+1/4)|\widehat f(1/2+it)|^2\,\frac{dt}{2\pi}.
$$
In particular $g$ itself is outside the derivative domain since the last integrand becomes one.

For $\tau>0$ put $a=t^2+1/4$. Minimizing over the closed domain the functional $\|f-g\|_2^2+\tau\|Df\|_2^2$ gives
$$
\widehat f_\tau(s)=\frac{u(s)}{s(1+\tau a)} .
$$
Indeed the pointwise identity
$$
|F-G|^2+\tau a|F|^2
=(1+\tau a)\left|F-\frac{G}{1+\tau a}\right|^2
+\frac{\tau a}{1+\tau a}|G|^2
$$
has a nonnegative first term, vanishing only at the stated function. The function is in the closed domain by its square-integrable weighted transform.

Let $\varepsilon_\tau=\|f_\tau-g\|_2$. Then $\varepsilon_\tau$ increases continuously and strictly from zero to one as $\tau$ increases from zero to infinity. This follows directly by integrating $(\tau a/(1+\tau a))^2|\widehat g|^2$ and using dominated convergence. For $0<\varepsilon<1$ take the unique $\tau$ with $\varepsilon_\tau=\varepsilon$. Every $f$ satisfying $\|f-g\|_2\le\varepsilon$ has
$$
\tau\|Df\|_2^2
\ge \tau\|Df_\tau\|_2^2+\varepsilon_\tau^2-\|f-g\|_2^2
\ge\tau\|Df_\tau\|_2^2 .
$$
Equality requires $f=f_\tau$, by the pointwise square identity. At $\varepsilon=0$ there is no feasible element in the domain. At $\varepsilon\ge1$ the unique minimizer is zero, since the derivative has trivial kernel on $L^2(dx)$.

## Exact curve and small-error constant

Put $\alpha=1+\tau/4$. The elementary integrals with $v=t\sqrt{\tau/\alpha}$ give
$$
I_1=\int_\mathbb R\frac{dt/(2\pi)}{1+\tau a}
=\frac1{2\sqrt{\tau\alpha}},\qquad
I_2=\int_\mathbb R\frac{dt/(2\pi)}{(1+\tau a)^2}
=\frac1{4\sqrt{\tau}\alpha^{3/2}} .
$$
The cost is $I_2$. The error is $\tau(I_1-I_2)$ because $|\widehat g|^2=1/a$. Hence
$$
\|Df_\tau\|_2^2=\frac1{4\sqrt\tau(1+\tau/4)^{3/2}},\qquad
\varepsilon_\tau^2=\frac{\sqrt\tau(1+\tau/2)}{4(1+\tau/4)^{3/2}} .
$$
In terms of $z=\sqrt{\tau/(4+\tau)}$ the exact eliminated parameter is particularly simple:
$$
\varepsilon^2=\frac{z+z^3}{2},\qquad
\inf_{\|f-g\|_2\le\varepsilon}\|Df\|_2^2=\frac{(1-z^2)^2}{8z},\qquad 0<z<1.
$$
The product of the squared error and squared cost is $(1+z^2)(1-z^2)^2/16$. In particular the norm cost is asymptotic to $1/(4\varepsilon)$ as $\varepsilon\downarrow0$. All constants here use $dt/(2\pi)$, including the unit value of $\|g\|_2^2$.

## Centered derivative and real constraints

The distinct centered derivative $D+1/2$ has multiplier $-it$. Its unique regularized solution replaces $a$ in the filter by $t^2$, while $|\widehat g|^2$ remains $(t^2+1/4)^{-1}$. Put $r=\sqrt\tau/2$. Partial fractions give
$$
I(\tau)=\int_\mathbb R\frac{dt/(2\pi)}{(t^2+1/4)(1+\tau t^2)}=\frac1{1+r}.
$$
The squared centered cost is $-I'(\tau)$, and the squared error is $1-I(\tau)+\tau I'(\tau)$, by differentiation under the integral on compact positive $\tau$-ranges. Thus
$$
\|(D+1/2)f_\tau\|_2^2=\frac1{4\sqrt\tau(1+r)^2},\qquad
\varepsilon_\tau^2=\frac{r(r+1/2)}{(1+r)^2}.
$$
Equivalently, with $z=r/(1+r)$ the centered curve has $\varepsilon^2=z(1+z)/2$ and squared cost $(1-z)^3/(8z)$. Its small-error norm asymptotic is again $1/(4\varepsilon)$, although the finite curve differs. In the original derivative domain, $\|Df\|_2^2=\|(D+1/2)f\|_2^2+\|f\|_2^2/4$.

If $g$ is real, the filter preserves the usual Mellin conjugate symmetry and the complex extremizer is real, so the real and complex problems agree. Reality of $g$ holds if the phase multiplier preserves real functions, as happens for the usual zeta phase. A general unimodular Mellin symbol need not preserve reality. For real competitors and complex $g$, one has the exact constraint $\|f-g\|_2^2=\|f-\Re g\|_2^2+\|\Im g\|_2^2$. The attainable error floor is therefore $\|\Im g\|_2$, and the regularizer applies to the real part with the reduced error budget. At the floor feasibility requires $\Re g$ to lie in the derivative domain. The universal unit-norm curve above describes the complex problem and the real problem with a real target.
