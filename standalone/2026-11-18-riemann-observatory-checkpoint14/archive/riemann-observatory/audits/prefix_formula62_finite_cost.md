# Exact finite prefix cost from the moment problem

The definitions here are the matrix and vector in equation (80) of [rStation48 v2](../sources/ratio62_q1_priority/rstation_48_v2.md). The calculation applies to those finite objects independently of any arithmetic model. Let $m\ge1$ be an integer, $0\le b<1$, $h=1-b$, $w=1/h$, and $R_n(y)=P_n(2y-1)$, using $P_n(1)=1$.

## Legendre representation

Let $L(q)=-q(0)+m\int_0^b q(x)\,dx$ act on real polynomials of degree below $m$. The moment matrix is the Gram matrix in the monomial basis for $\langle p,q\rangle_b=\int_b^1pq$. It is positive definite because a polynomial of zero square integral vanishes identically. The coefficient vector of its representer $f_b$ is $M^{-1}v$, and $c_m(b)=m^2b+\|f_b\|_b^2$.

The basis $q_n(x)=R_n((1-x)/h)$ has squared norms $h/(2n+1)$. With $\ell_n=L(q_n)$ this gives
$$
c_m(b)=m^2b+w\sum_{n=0}^{m-1}(2n+1)\ell_n^2.
$$
Here $\ell_0=m-1-m/w$. For $n\ge1$, $\int_0^1R_n=0$, so
$$
\ell_n=-R_n(w)+\frac{m}{w}\int_0^w R_n(y)\,dy
=\sum_{j=0}^n(-1)^{n-j}\binom nj\binom{n+j}j\left(\frac m{j+1}-1\right)w^j.
$$
In particular $c_m(0)=\sum_{n=0}^{m-1}(2n+1)=m^2$. Direct evaluation gives $c_1(b)=1$.

## Positive coefficients

Write $u_b=M^{-1}v$ and $d=(1,b,\ldots,b^{m-1})^{\mathsf T}$. Differentiating gives $M'=-dd^{\mathsf T}$, $v'=md$, and
$$
c'_m(b)=m^2+2u_b^{\mathsf T}v'-u_b^{\mathsf T}M'u_b=(m+f_b(b))^2.
$$
Let $K(y)=\sum_{n=0}^{m-1}(2n+1)R_n(y)$. Since $q_n(b)=1$, the basis formula for $f_b$ gives
$$
m+f_b(b)=-wK(w)+m\int_0^wK(y)\,dy.
$$
The integration from 0 includes the constant term correction $\ell_0=m-1-m/w$.

Put $s=w-1$ and $H(s)=(1+s)K(1+s)-m\int_0^{1+s}K(y)\,dy$. The endpoint Christoffel–Darboux identity gives $K(1+s)=m(R_m(1+s)-R_{m-1}(1+s))/(2s)$, interpreted by continuity at $s=0$. In the expansion $R_n(1+s)=\sum_j\binom nj\binom{n+j}j s^j$, the coefficient of degree $j+1$ in that difference is $2m\binom{m-1}{j}\binom{m+j}{j}/(j+1)$. Thus the coefficient $S_j$ of $s^j$ in $K(1+s)$ is $m^2\binom{m-1}{j}\binom{m+j}{j}/(j+1)$.

As $\int_0^1K=1$, the constant coefficient of $H$ is $m^2-m$. For $1\le j\le m-1$, its coefficient is
$$
S_j+(1-m/j)S_{j-1}=S_j\frac{m-1}{m+j},
$$
by $S_j/S_{j-1}=(m-j)(m+j)/(j(j+1))$. The coefficient at $j=m$ vanishes. Define
$$
G_m(s)=m(m-1)\sum_{j=0}^{m-2}\frac{\binom{m-2}j\binom{m+j}j}{j+1}s^j
\qquad (m\ge2).
$$
Writing $g_j=[s^j]G_m$, the ratios to $S_j(m-1)/(m+j)$ of $g_j$ and $g_{j-1}$ are respectively $(m-1-j)(m+j)/(m(m-1))$ and $j(j+1)/(m(m-1))$. Their sum is one, with out-of-range coefficients taken as zero. This proves $H=(1+s)G_m$. Consequently $c'_m(b)=(1+s)^2G_m(s)^2$ and $db=ds/(1+s)^2$ give
$$
\boxed{c_m(b)=m^2+\int_0^{b/(1-b)}G_m(s)^2\,ds.}
$$
The Legendre expansion above also gives $G_m(s)=2P'_{m-1}(1+2s)$. In particular $c_m(b)=m^2+2\int_1^{(1+b)/(1-b)}P_{m-1}'(x)^2\,dx$ for all $m\ge1$.

Every coefficient of $G_m$ is positive. Hence $c'_m(b)>0$ and $c_m(b)>m^2$ for $m\ge2$ and $0<b<1$. For $m=2$, $G_2=2$, so $c_2(b)=4/(1-b)$.

## The endpoint $b\to1^-$ at fixed $m$

For $m\ge2$, the leading coefficient of $G_m$ is $m\binom{2m-2}{m-2}=2(2m-3)\binom{2m-4}{m-2}$. The leading monomial in the integrated square gives
$$
c_m(b)\sim 4(2m-3)\binom{2m-4}{m-2}^{\!2}(1-b)^{-(2m-3)}.
$$
A direct guess that the top mode would give the power $2m-1$ fails. Its $\ell_{m-1}$ coefficient at $w^{m-1}$ vanishes because $m/(j+1)-1=0$ at $j=m-1$.

## Large $m$ at fixed $b\in(0,1)$

Set $z=2w-1$, $a=\sqrt{z^2-1}$, and $\rho=z+a=(1+\sqrt b)/(1-\sqrt b)$. For $n\ge1$, integrating the Legendre derivative identity gives
$$
\ell_n=-P_n(z)+\frac{mh}{2}\frac{P_{n+1}(z)-P_{n-1}(z)}{2n+1}.
$$
At this fixed $z>1$, the integral representation $P_n(z)=\pi^{-1}\int_0^\pi(z+a\cos\theta)^n\,d\theta$ gives $P_n(z)\sim \rho^{n+1/2}/\sqrt{2\pi n a}$. Indeed the logarithm of the integrand base has its unique maximum at 0 and expansion $\log\rho-a\theta^2/(2\rho)+O(\theta^4)$ there. Rescaling $\theta$ by $1/\sqrt n$ gives the half-Gaussian constant, with the integrand exponentially smaller outside any fixed neighborhood of 0.

For fixed $r\ge0$, at $n=m-1-r$ the ratio $\ell_n/P_n(z)$ tends to $-1+ha/2=-1+\sqrt b$. To sum these modes, for $n\ge m/2$ the displayed formulas give $(2n+1)\ell_n^2\le C_b\rho^{2n+1}$, using the fixed-$z$ asymptotic and boundedness of $m/(2n+1)$. After dividing by $\rho^{2m-1}$ this is a summable geometric bound in $r$. For $1\le n<m/2$, the integral formula gives $P_k(z)\le\rho^k$, and the displayed formula gives $|\ell_n|\le C_b m\rho^n$. Including the $n=0$ and prefix terms, the contribution below $m/2$ is $O_b(m^4\rho^m)$. The Legendre sum therefore yields
$$
c_m(b)\sim \frac{(1-\sqrt b)^2}{\pi h a}\frac{\rho^{2m-1}}{1-\rho^{-2}}
=\boxed{\frac{(1-\sqrt b)^2(1-b)}{8\pi b}
\left(\frac{1+\sqrt b}{1-\sqrt b}\right)^{2m}}.
$$
This limit holds with $b$ fixed. The multiplicity asymptotic yields no uniform estimate for $b$ approaching 0 or 1 with $m$.

The [exact test](../experiments/code/prefix_formula62_exact.py) checks the independent moment solve, Legendre sum and integrated polynomial at 72 rational inputs, including $b=0$, with [retained results](../experiments/results/prefix_formula62_exact.txt).
