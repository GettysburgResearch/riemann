# The first negative eigenmode of the centered Goldbach sum

Let $a_n=\Lambda(n)-1$ and $B(N)=\sum_{m+n\le N}a_ma_n$. If even one zero of zeta has real part $\beta>1/2$, the first negative eigenmode in the exact quadratic form for $B(N)$ contributes at least $N^{2\beta-\epsilon}$ in magnitude for arbitrarily large $N$, for each $\epsilon>0$. In fact both signs of its underlying linear statistic have limsup exponent $\Theta=\sup_\rho\Re\rho$. An attempt to prove the required one-sided bound for $B$ by bounding the entire negative spectral part individually would already have to settle RH. This complements the [signed convolution theorem](nov18b-variance-goldbach.md).

## Diagonalization at the actual integer endpoint

Take $N\ge3$, $1\le m,n\le N-1$, and $H_{mn}=\mathbf 1_{m+n\le N}$. For $0\le j\le N-2$ set
\[
 \omega_j=(2j+1)\pi/2,\quad \theta_j=\omega_j/(N-1/2),\quad
 v_j(n)=\cos((n-1/2)\theta_j).
\]
Summing cosines gives $(Hv_j)(m)=\sin((N-m)\theta_j)/(2\sin(\theta_j/2))$. Since $(N-1/2)\theta_j=\omega_j$, the eigenvalue is $\lambda_j=(-1)^j/(2\sin(\theta_j/2))$. Their magnitudes strictly decrease. The vectors therefore form an orthogonal basis. Direct summation gives $\|v_j\|^2=(2N-1)/4$. Thus, with $C_j(N)=\sum_{n<N}a_n v_j(n)$, the identity
\[
                B(N)=\sum_{j=0}^{N-2}\frac{4\lambda_j}{2N-1} C_j(N)^2
 \tag{1}
\]
has no off-diagonal remainder. For fixed $j$, the coefficient tends to $2(-1)^j/\omega_j$.

## A Mellin kernel that sees all zeta zeros

For $\omega=3\pi/2$, write
\[
 S(x)=\sum_{n\le x}a_n\cos(\omega n/x),\qquad
 K(s)=\int_0^1 u^{s-1}\cos(\omega u)\,du .
\]
Chebyshev's bound gives $\sum_{n\le x}|a_n|\ll x$. For $x\in[N,N+1)$ this implies $S(x)=C_1(N)+O(1)$ uniformly. On the old terms the change of phase is $O(1/N)$, and the endpoint term for $n=N$ is $O(\log(2N)/N)$ because $\cos\omega=0$.

For $\Re s>1$ the Mellin transform of $S$ is
\[
 \int_1^\infty S(x)x^{-s-1}\,dx
       =K(s)\left(-\frac{\zeta'(s)}{\zeta(s)}-\zeta(s)\right).
 \tag{2}
\]
The singularity at $1$ cancels. Three integrations by parts, using $\sin\omega=-1$ and $\cos\omega=0$, give
\[
 K(s)=-\frac{\omega}{s(s+1)}
       \left(1+\frac{\omega^2}{s+2}\int_0^1 u^{s+2}\sin(\omega u)\,du\right).
\]
The last term in parentheses after $1$ has modulus at most $\omega^2/(|s+2|(\Re s+3))$. At every nontrivial zeta zero this is less than $1$, since $|\Im\rho|>14$. Thus a zero of multiplicity $m_\rho$ produces a genuine pole with residue $-m_\rho K(\rho)$ in (2). [Verified low zeta zeros](https://arxiv.org/abs/2004.09765)

Fix $0<b<\Theta$. If either $S(x)\le Cx^b$ or $S(x)\ge-Cx^b$ eventually, add $Cx^b$ with the appropriate sign to make a nonnegative function for $x\ge1$, increasing $C$ if needed. Its Mellin transform in the convergent half-plane is $C/(s-b)$ plus or minus (2). It has analytic continuation through each real point $s>b$, because zeta has no real zero in $(0,1)$ and its pole has canceled. Landau's theorem for the Mellin transform of a nonnegative function forces its abscissa of convergence to be at most $b$. Its defining integral is then holomorphic on $\Re s>b$, contradicting the surviving pole there. This proves unbounded positive and negative excursions relative to $x^b$. The standard explicit-formula estimate $\psi(x)-x\ll_\epsilon x^{\Theta+\epsilon}$ and partial summation give the reverse upper exponent. One may also use the trivial bound if $\Theta=1$.

Taking the two signs separately proves
\[
 \limsup_{N\to\infty}\frac{\log(1+\max(\pm C_1(N),0))}{\log N}=\Theta .
\]
The first negative summand in (1) therefore has absolute limsup exponent $2\Theta$. The full negative part of this *spectral decomposition* dominates that one term in absolute magnitude. Controlling the actual negative values of $B$ can still use the positive eigenmodes in (1). Its one-sided bound at exponent one remains the arithmetic question.

## A test on sparse grids of integers

Fix $c>0$, $0\le\delta<1$, and either sign. Let $I_X=[X\exp(-c\sqrt{\log X}),X\exp(c\sqrt{\log X})]$. Suppose $X_j\to\infty$ and for each $j$ one has a grid $G_j$ of integers such that every integer of $I_{X_j}$ lies within $X_j^{\delta+o(1)}$ of a grid point. The error in this covering radius is uniform over the window. Then
\[
 \max_{g\in G_j}B_\pm(g)\le X_j^{1+\delta+o(1)}
       \quad\Longrightarrow\quad \Theta\le\frac{1+\delta}{2}.
\]
For the converse take the grid points in $I_{X_j}$ or within the indicated radius of it. If $\Theta\le(1+\delta)/2$, the published upper bounds for $B$ give the displayed grid bound at every sufficiently large scale. At $\delta=0$, this gives an RH equivalence on any such grid of subpower spacing, for either sign separately. The points may be chosen after seeing the arithmetic data.

Indeed
\[
 |B(n+1)-B(n)|\le \sum_{m+\ell=n+1}\Lambda(m)\Lambda(\ell)
                         +2\psi(n)+n\ll n\log(2n)
\]
by Chebyshev and $\Lambda(\ell)\le\log(n+1)$. The same increment bound applies to both positive and negative parts. Telescoping from a nearest grid point propagates the upper bound to $B_\pm(n)\le X_j^{1+\delta+o(1)}$ everywhere in the window. Integer endpoint discrepancies are covered by one more increment. Its integral is then at most $X_j^{2+\delta+o(1)}$. The [local signed mass lower bound, equation (6)](nov18b-goldbach-local.md) contradicts this for any zero with $2\Re\rho>1+\delta$. This interpolation uses the original additive increments and has no hypothesis on the multiplicity or location of the grid representatives.
