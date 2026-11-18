# A fixed Weil test sampled on any geometric progression

**Proposed analytic result.** Fix any spacing $h>0$ and any width $w>0$. There is an explicit nonnegative real function $g\in C_c^\infty([0,w])$, independent of $h$ and of the zeta zeros, with the following properties. Write $\tau_y g(u)=g(u-y)$ and
\[
 c_k=W(\tau_{kh}g,g),\qquad d_*=\Theta-\tfrac12,
 \qquad \Theta=\sup_\rho\Re\rho.
\]
Here $W$ is the ordinary sesquilinear Weil form, linear in its first argument. The numbers $c_k$ are real. RH is equivalent to nonnegativity of the two numbers $W(g+\tau_{kh}g)$ and $W(g-\tau_{kh}g)$ at every integer $k\ge1$. This conclusion holds for **each prescribed spacing**, with no assumption on rational relations among zero ordinates. The two supports are disjoint as soon as $kh>w$.

There is an exact growth law if an off-line zero exists. Put $q(\sigma)=3(1-\sigma)/(2-\sigma)$. For each $q(\Theta)<a<1$,
\[
 \lim_{N\to\infty}\frac1N
 \log\!\left(1+\max_{N\le k\le N+N^a}|c_k|\right)=h d_* .
 \tag{1}
\]
Here and below the indices $k,N$ are integers. Under RH the limit is zero for every $0<a<1$. For example $N^a$ can be replaced by $N/\log N$ in (1) for all possible values of $\Theta$, including $1/2$. A bound $\max_{N\le k\le N+N/\log N}|c_k|=e^{o(N)}$ along even one unbounded sequence of $N$ is therefore equivalent to RH. On RH, $|c_k|\le c_0$.

The explicit formula below identifies $c_k$ with the error of one fixed smooth prime sum, using only prime powers with $e^{kh-w}\le n\le e^{kh+w}$. The relative logarithmic coverage $2w/h$ can be chosen arbitrarily small and the progression can be fixed before choosing the bump. The proof supplies the exponent and its converse. It supplies no upper bound $e^{o(N)}$ for the arithmetic errors.

## A compact test whose zero weights cannot cancel at an aliased frequency

Set $\widehat g(z)=\int g(u)e^{izu}\,du$ and $A(z)=\widehat g(z)\overline{\widehat g(\bar z)}$. We construct $g$ with $\int g=1$ such that, throughout $z=t+iv$, $|v|\le1/2$,
\[
 A(z)\ne0,\qquad |\arg A(z)|<\pi/4,\qquad
 |A(z)|\le C\exp\!\left(-c\frac{|t|}{\log^4(3+|t|)}\right).
 \tag{2}
\]
The argument here is a branch centered at zero. All implied constants may depend on $w$.

For $j\ge1$ take $b_j=Bj\log^4(j+2)$, $H_j=D\log(j+2)/b_j$. Convolve the probability densities proportional to $e^{-b_j u}\mathbf1_{[0,H_j]}(u)$. Fix $D$ sufficiently large, then $B$ sufficiently large so that $b_j\ge2$, $\sum 1/b_j$ is as small as desired and $\sum H_j<w$. The distribution of the sum of independent variables exists, is a nonnegative probability measure on $[0,w]$, and its entire transform is the locally uniform product of their transforms. Indeed each summand is bounded by $H_j$ and $\sum H_j<\infty$.

The $j$th factor of $A(z)$ is
\[
 \frac{b_j^2}{b_j^2+z^2}
 \frac{(1-e^{(-b_j+iz)H_j})(1-e^{(-b_j-iz)H_j})}
 {(1-e^{-b_jH_j})^2}.
 \tag{3}
\]
The denominator $b_j^2+z^2$ has positive real part and the absolute value of its argument is $O(1/b_j)$, since $2|tv|/(b_j^2+t^2-v^2)\ll 1/b_j$. The arguments of the numerator corrections sum absolutely to $O(\sum_j(j+2)^{-D/2})$, uniformly on the strip. Neither correction vanishes there. These two argument bounds give the first two assertions of (2), using local convergence and nonvanishing of the product at fixed $z$ (the absolutely summable small changes in the individual probability transforms suffice). For the modulus, the product of the corrections in (3) is bounded uniformly. The factors $b_j^2/|b_j^2+z^2|$ are collectively at most $\prod_j(1-1/(4b_j^2))^{-1}<\infty$; each is at most $1/2$ when $b_j\le |t|/2$ and $|t|$ is sufficiently large. There are $\gg_B |t|/\log^4(3+|t|)$ such indices. This proves the last bound. On the real line $A(t)=|\widehat g(t)|^2$, so Fourier inversion gives a $C^\infty$ density $g$ for the limiting probability.

## Discrete separation in the presence of aliases

Let $z=\gamma+i(1/2-\beta)$ run over the zeros of $\Xi(z)=\xi(1/2+iz)$, with multiplicities. Set $\lambda_z=e^{ihz}$. The zero side gives the absolutely convergent identity
\[
       c_k=\sum_z A(z)\lambda_z^k .                         \tag{4}
\]
The symmetry $z\mapsto-\bar z$ makes the sum real since $g$ is real. Its absolute value is at most $e^{hd_*k}\sum|A(z)|$ for $k\ge0$, by (2) and Riemann–von Mangoldt. If all zeros lie on the line, (4) is a sum of unit phases with nonnegative weights $A(\gamma)$, proving the RH assertions.

Fix a zero with $\beta_0>1/2$, and fix $1/2<\sigma<\beta_0$ and $q(\sigma)<a<1$. Write $\lambda_0=e^{ihz_0}=r_0 e^{i\theta_0}$, where $r_0=e^{h(\beta_0-1/2)}>1$. For large $N$ take $T=N\log^6(3+N)$. Form the monic polynomial $Q$ with the **distinct** roots $\lambda_z$ from $\beta\ge\sigma, |\gamma|\le T$. Ingham's density estimate $N(\sigma,T)\ll_\sigma T^{q(\sigma)}\log^5(2T)$ bounds its degree $m\le N^{q(\sigma)+o(1)}$. In particular $m\log N=o(N)$, $m\le N^a$. Multiplicities at an identical root need no repetition because (4) has no derivative factors. [Density theorem and multiplicity convention](nov18b-compact-zero-filter.md)

Choose a small fixed $\epsilon>0$ in terms of $r_0$. For some $R\in[\epsilon/N,2\epsilon/N]$ the circle $D=\{|u-\lambda_0|=R\}$ satisfies
\[
                  \min_{u\in D}|Q(u)|\ge e^{-C m\log N}.
 \tag{5}
\]
For each root $v$, the distance from it to the circle is $||v-\lambda_0|-R|$. The mean of the positive part of the logarithm of its reciprocal over the indicated interval of radii is at most $\log N+C_\epsilon$, by scaling the integrable logarithmic singularity. Sum and choose a radius whose sum is no greater than its mean. Orient $D$ positively and define the polynomial
\[
 P(x)=\frac{1}{2\pi i}\int_D
          \frac{Q(u)-Q(x)}{(u-x)Q(u)}\,du
      =\sum_{j=0}^{m-1}p_j x^j .                               \tag{6}
\]
At any root $v$ of $Q$, $P(v)$ is 1 inside $D$ and 0 outside. This interpolates whole clusters and needs no separation among their members. All roots and contour points are in a fixed disk depending on $h$. The coefficient norm of $Q$ is at most $(1+e^{h/2})^m$. Expanding the divided differences of its monomials and using (5) gives $\sum|p_j|\le e^{C_hm\log N}$ and $\max_{|v|\le e^{h/2}}|P(v)|\le e^{C_hm\log N}$.

In $\sum_{j}p_j c_{N+j}$, first consider the projected roots inside $D$. For each, $|\arg(\lambda_z^N e^{-iN\theta_0})|<\pi/8$ modulo $2\pi$, by choosing $\epsilon$ small, since $|\lambda_z-\lambda_0|\le2\epsilon/N$. The weights $A(z)$ have arguments in $(-\pi/4,\pi/4)$. Thus the real part after the common rotation is at least $\cos(3\pi/8)|A(z_0)|r_0^N$ from $z_0$ alone, and every other included term has positive real part. This is the step that tolerates even exact aliasing. The roots of $Q$ outside $D$ contribute zero.

All zeros with $\beta<\sigma$ contribute $O(e^{h(\sigma-1/2)N+C_hm\log N}\sum_z|A(z)|)$. All remaining zeros above $T$ in absolute ordinate contribute $O(e^{hN/2+C_hm\log N-c'T/\log^4(3+T)})$, by (2) and the unit-interval zero count. Both are $o(r_0^N)$. Consequently
\[
          \max_{N\le k\le N+N^a}|c_k|
               \ge e^{h(\beta_0-1/2)N-o(N)} .
\]
For $a>q(\Theta)$, take zeros $\beta_0$ arbitrarily close to $\Theta$ and choose $\sigma<\beta_0$ with $q(\sigma)<a$. Together with the upper bound from (4), this proves (1). Finally $W(g\pm\tau_{kh}g)=2(c_0\pm c_k)$, so (1) forces a strictly negative test if RH fails.

## The exact prime shell

Let $K=g*\widetilde g$ with $\widetilde g(u)=g(-u)$. This is a nonnegative real even smooth function supported in $[-w,w]$, with transform $A$. Let $y=kh>w$. The full arithmetic explicit formula gives
\[
 c_k = e^{y/2} A(i/2)
       -\sum_{|\log n-y|\le w}\frac{\Lambda(n)}{\sqrt n}K(y-\log n)
       -\int_{-w}^w K(u)
               \frac{e^{-5(y-u)/2}}{1-e^{-2(y-u)}}\,du .          \tag{7}
\]
Indeed the two poles give $2\cosh(y/2)A(i/2)$. Away from zero the inverse Fourier transform of $\Re\psi(1/4+it/2)-\log\pi$ is $-e^{-|v|/2}/(1-e^{-2|v|})$, by the integral representation of the digamma function with the substitution $v=x/2$. The subtraction at zero has support disjoint from $K(y-\cdot)$. The first term of the geometric expansion of this inverse transform contributes $-e^{-y/2}A(i/2)$ by evenness of $K$. The other branch of the prime-power term has $K(y+\log n)=0$. This proves (7) and identifies the remaining arithmetic question as the uniform square-root-scale accuracy of these specified smoothed prime sums on one sequence of index windows. [Explicit formula in the same normalization](weil-prime-local-nov18.md)

## Sampling several spacings and the exact prime coefficients

The [positive Euler deformation](nov18c-goldbach.md) shows why comparing a finite number of progressions using only positivity, the ordinary PNT and the prime-power support does not establish the sharp error bound. Here is its effect on exactly (7). Fix $1/2<\beta<1$ and $\gamma>0$. Keep all factors for primes $p\le P$ and apply the indicated reciprocal product of the two shifted incomplete zeta functions for $p>P$. For $n=p^j$ with $p>P$, the modified logarithmic derivative coefficient is
\[
   \Lambda'(n)=\Lambda(n)[1-2n^{\beta-1}\cos(\gamma\log n)].
\]
It agrees with $\Lambda(n)$ otherwise, and is positive on every prime power once $2P^{\beta-1}<1$. Denote the arithmetic expression on the right of (7), with this replacement only, by $c'(y)$, and its original value by $c(y)$. The ordinary prime number theorem gives
\[
 c'(y)-c(y)
 =2 e^{(\beta-1/2)y}
       \Re\!\left[e^{i\gamma y}
           A\bigl(\gamma-i(\beta-1/2)\bigr)\right]
      +o(e^{(\beta-1/2)y}) .                                      \tag{8}
\]
Indeed the difference is twice the real part of the prime sum with weight $n^{\beta-3/2+i\gamma}K(y-\log n)$. After division by $e^{(\beta-1/2+i\gamma)y}$, substitute $n=e^yv$ and use weak convergence of $e^{-y}d\psi(e^yv)$ to $dv$ on $[e^{-w},e^w]$. Substituting $v=e^u$ gives the coefficient in (8), by evenness of $K$. Powers of the finitely many omitted primes contribute $o(1)$ after normalization.

For any finite prescribed collection $h_1,\ldots,h_j>0$, the conditions $|e^{i\gamma N h_\ell}-1|<\delta$ hold simultaneously on a relatively dense set of positive integers $N$, for each fixed $\delta>0$. Translation by the vector of phases is a rotation on its compact orbit closure. Finitely many translates of a neighborhood of the identity cover that closure and give the bounded return gaps. The strict sector in (2) and (8) now give fixed positive multiples of $e^{(\beta-1/2)Nh_\ell}$ as simultaneous lower bounds for $c'(Nh_\ell)-c(Nh_\ell)$, by choosing $\delta$ small. The sign and size can therefore survive simultaneous sampling even when the prime coefficients agree to arbitrarily small relative error and the first arbitrarily many Euler factors agree exactly. The deformation changes the global analytic object. A proof for ordinary zeta must use some additional property, such as its exact prime coefficients or its unmodified functional equation.
