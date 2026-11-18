# An order-one countermodel with Riemann–von Mangoldt counting

18 November 2026. For every $H>0$, every $0<a<1/2$, and every prescribed height, there is an even real entire function $E$ of order one with $E(0)=1$, $E(iy)>0$ for all real $y$, and exactly one simple off-real quartet beyond that height in the strip $|\operatorname{Im}z|\le a$. Its positive-ordinate zero count, including the two members of the quartet with positive real part, satisfies
$$
N_E(x)=M(x)+O(1),\qquad
M(x)=\frac{x}{2\pi}\log\frac{x}{2\pi}-\frac{x}{2\pi}+\frac78 .
$$
The Nakamura–Suzuki zero-sum exponent for $E$ gives positive semidefinite characteristic matrices for every positive exponential power and every finite grid of diameter at most $H$. It nevertheless takes arbitrarily large positive values. Here $M$ is the smooth Riemann–von Mangoldt main term for positive heights in the $s$-plane. Under $s=1/2-iz$, positive real parts in the $z$-plane correspond to negative heights, and evenness makes the two counts equal. The model matches the smooth main term and the first two small-time terms of the actual zeta exponent. The actual zeta count has an additional fluctuation, and the zeta Euler product and arithmetic formula on the whole line remain outside this construction. Publication priority is unassessed. [Earlier bounded-diameter proof](geometry64_infdiv_skeptic.md) · [Nakamura–Suzuki, (1.5), (1.7) and Lemma 2.2](https://arxiv.org/pdf/2306.08317v1)

## Fill the deficit with simple real zeros

Choose $b>0$ so small that $b\sqrt2 H<2\pi$ and $C_b=\pi(b^{-1}+(b\sqrt2)^{-1})>(1+2\cosh(aH))H$. Keep the two full sinc lattices at $\pm nb$ and $\pm nb\sqrt2$, $n\ge1$. They are simple and disjoint. Their positive zero count is
$$
L(x)=\lfloor x/b\rfloor+\lfloor x/(b\sqrt2)\rfloor,\qquad
\lambda_0=b^{-1}+(b\sqrt2)^{-1}.
$$
Put $D(x)=M(x)-L(x)$. Choose $x_0>2\pi+1$ off the lattice, sufficiently large that $M'(x)\ge\lambda_0$ for $x\ge x_0$ and $D(x_0)>2$. This is possible because $M'(x)=(2\pi)^{-1}\log(x/(2\pi))$ tends to infinity and $L(x)=\lambda_0x+O(1)$. For $x\ge u\ge x_0$,
$$
L(x)-L(u)\le \lambda_0(x-u)+2,\qquad D(x)\ge D(u)-2.
$$
Thus the running supremum $B(x)=\sup_{x_0\le u\le x}D(u)$ satisfies $0\le B(x)-D(x)\le2$. It increases to infinity and is continuous. Between successive lattice points $D$ is smooth and increasing, so $B$ is the maximum of the previous record and the current $D$. At lattice points $D$ jumps down, so the running supremum includes the left-limit value and remains continuous.

Choose $\theta\in(0,1)$ so that no $B(\ell)$ with $\ell\ge x_0$ a lattice point, and no $B(x_0)$, belongs to $\theta+\mathbb Z$. This omits only a countable set. Put $K=\lfloor B(x_0)-\theta\rfloor$ and add $K$ distinct positive points in $(x_0-1,x_0)$ away from both lattices, with their negatives. For each integer $k>K$, add the first $x\ge x_0$ at which $B(x)=k+\theta$, and its negative. Continuity and unboundedness give all these first hitting times. They are strictly increasing, exceed $x_0$, and cannot occur at a lattice point by the choice of $\theta$. They are locally finite because $B$ is bounded on compact intervals. For $x\ge x_0$, the added positive count is exactly $\lfloor B(x)-\theta\rfloor$, including at a hitting time. The sum of this count and $L(x)$ differs from $M(x)$ by $B(x)-D(x)-\theta-\{B(x)-\theta\}$, with absolute value at most two. This construction requires no zeros to be removed even if the sinc lattices exceed $M$ over a large initial range.

## Entire product, strip and transform

Let $\mathcal L$ denote the union of all positive real zeros just constructed. The counting bound implies $\sum_{\lambda\in\mathcal L}\lambda^{-2}<\infty$ by partial summation. Thus
$$
E_{\mathrm{real}}(z)=\prod_{\lambda\in\mathcal L}\left(1-\frac{z^2}{\lambda^2}\right)
$$
converges normally on compact sets. This is the paired genus-one product, because the canonical factors $(1-z/\lambda)e^{z/\lambda}$ and $(1+z/\lambda)e^{-z/\lambda}$ multiply to the displayed factor. On a compact set avoiding the prescribed zeros the infinite product tail converges to a nonzero value because the deviations from $1$ are absolutely summable. This proves that the list exhausts the zeros and each is simple. Its factors are positive at $iy$. For any $R>a$ beyond the prescribed height, multiply by $\bigl(1-z^2/(R+ia)^2\bigr)\bigl(1-z^2/(R-ia)^2\bigr)$ to get $E$. These factors are a positive absolute square at $iy$ and give the simple quartet $\pm(R\pm ia)$. For $x\ge x_0$, the positive count becomes $N_{\mathrm{real}}(x)+2\mathbf1_{x\ge R}$. The error from $M(x)$ is bounded by four uniformly in the quartet location.

For growth, on $|z|\le r$, $\log|E_{\mathrm{real}}(z)|$ is bounded above by $\sum_{\lambda\in\mathcal L}\log(1+r^2/\lambda^2)$. In Stieltjes form this last sum is the integral of $2r^2 N_{\mathrm{real}}(u)/(u(u^2+r^2))$ over $u>0$. Below the smallest zero the integrand is zero. Up to $u=r$ use $N_{\mathrm{real}}(u)\ll u\log(2+u)$, and above $r$ use the same bound with the kernel dominated by $2r^2/u^3$. Both portions are $O(r\log(2+r))$. At $z=ir$ every term from $\lambda\le r$ contributes at least $\log 2$, giving growth of order at least $r\log r$ for the logarithm of the maximum modulus. The quartet affects these growth bounds by $O(\log r)$ as $r\to\infty$. The order is therefore exactly one, with infinite exponential type. The function $\Xi(s)=E(i(s-1/2))$ is real entire, symmetric under $s\mapsto1-s$, strictly positive on the real axis, and all its zeros satisfy $|\operatorname{Re}s-1/2|\le a$.

The exponent $g_E(t)=\sum_{\gamma} (e^{-i\gamma t}-1)/\gamma^2$ is even, real, continuous, and zero at $t=0$. Uniform convergence on compact real intervals follows from the strip bound and inverse-square summability. For $\operatorname{Im}z>a$ the bound $(e^{a t}+1)e^{-(\operatorname{Im}z)t}\sum_\gamma|\gamma|^{-2}$ is integrable for $t\ge0$, so direct termwise integration gives
$$
\int_0^\infty g_E(t)e^{izt}\,dt
=\frac{i}{z^2}\sum_\gamma\left(\frac1{z-\gamma}+\frac1{\gamma}\right)
=\frac{i}{z^2}\frac{E'(z)}{E(z)}.
$$
The second equality follows from normal convergence of the logarithmic derivatives away from the zeros. Every signed zero in the paired product has unit multiplicity. No linear exponential factor occurs, and the coordinate change gives the Nakamura–Suzuki form $z^{-2}(\Xi'/\Xi)(1/2-iz)$. [Primary transform identity](https://arxiv.org/pdf/2306.08317v1)

## Uniform grid positivity and late failure

A new positive real zero $\lambda$, with its negative, adds $2(\cos(\lambda t)-1)/\lambda^2$ to the exponent. This is nonpositive on $\mathbb R$. On any finite grid with coefficients $u_i$ of sum zero, its conditional quadratic form is
$$
\lambda^{-2}\left(
\left|\sum_i u_i e^{i\lambda t_i}\right|^2+
\left|\sum_i u_i e^{-i\lambda t_i}\right|^2\right)\ge0.
$$
The sum over all added zeros preserves these inequalities by absolute convergence. This argument needs no lower bound on the spacing of the added zeros.

For completeness, on $[-H,H]$ the two original sine lattices give $-C_b|t|+t^2$ by the Fourier series of the periodic quadratic. A zero-sum grid defines the compactly supported step function $F(x)=\sum_i u_i\mathbf1_{[t_i,\infty)}(x)$. Integrating twice in the quadratic form gives $2\|F\|_2^2$ for $-|t|$ and $-2|\int F|^2$ for $t^2$. The quartet adds $q_R(t)=4\operatorname{Re}[(\cos((R+ia)t)-1)/(R+ia)^2]$ and $\|q_R''\|_{\infty,[-H,H]}\le4\cosh(aH)$. Its form in absolute value is at most $4H\cosh(aH)\|F\|_2^2$. Since $2C_b-2H-4H\cosh(aH)>0$, we obtain conditional positivity on every finite grid of diameter at most $H$. Anchoring the kernel at one grid point makes its centered matrix positive semidefinite, and taking its entrywise exponential uses the positive Schur powers. Diagonal conjugation returns the matrix $[\exp(cg_E(t_i-t_j))]$ for every $c>0$. Two-point grids in particular give $g_E(t)\le0$ on $[-H,H]$.

The entire real-zero part of the exponent is uniformly bounded on $\mathbb R$ by $4\sum_{\lambda\in\mathcal L}\lambda^{-2}$. At $t_n=2\pi n/R$, however, $q_R(t_n)=4\operatorname{Re}((R+ia)^{-2})(\cosh(a t_n)-1)$ tends to positive infinity because $R>a$. The real part of the inverse square is positive. Thus even this Riemann–von Mangoldt model fails the real-line characteristic-function modulus bound. [Compact-grid estimate for the original lattices](geometry64_infdiv_skeptic.md)

## The small-time cusp is preserved to its linear term

The bounded counting discrepancy also fixes the leading small-time expansion. Write $\varepsilon=|t|$ and $\phi_t(u)=2(\cos(tu)-1)/u^2$. Extend the discrepancy $N_{\mathrm{real}}(u)-M(u)$ to $u>0$ using the same formula for $M(u)$. It stays bounded since $u\log u\to0$ at zero, the real count is zero near zero, and the discrepancy is bounded above $x_0$. The real-zero exponent is $\int_{(0,\infty)}\phi_t\,dN_{\mathrm{real}}$. Replacing $dN_{\mathrm{real}}$ by $M'(u)\,du$ costs $O(t^2)$. Indeed $\phi_t(0)=-t^2$, the function vanishes at infinity, and $\int_0^\infty|\phi_t'(u)|\,du=O(t^2)$ by scaling and integrability of the derivative of $2(\cos v-1)/v^2$. Stieltjes integration by parts then controls both the boundary and the remaining discrepancy integral. The quartet gives an additional $O(t^2)$ for each fixed $R$.

The remaining integral equals
$$
-\frac{\varepsilon}{\pi}\int_0^\infty
\frac{1-\cos v}{v^2}\left(\log(1/\varepsilon)+\log v-\log(2\pi)\right)\,dv .
$$
For $|w|<1$, a Laplace integral for $v^{w-2}$ and the transform $\int_0^\infty e^{-yv}(1-\cos v)\,dv=1/(y(1+y^2))$ give
$$
J(w)=\int_0^\infty \frac{1-\cos v}{v^{2-w}}\,dv
=\frac{\pi}{2\Gamma(2-w)\cos(\pi w/2)}.
$$
Use $J(0)=\pi/2$ and $J'(0)=(\pi/2)(1-\gamma_{\mathrm E})$. This yields
$$
g_E(t)=-\tfrac12 |t|\log(1/|t|)
 +\tfrac12\bigl(\log(2\pi)+\gamma_{\mathrm E}-1\bigr)|t|+O(t^2).
$$
The first two terms agree with the expansion from the arithmetic definition of $g_\zeta$. Matching them therefore cannot distinguish the globally positive-definite property from bounded-diameter tests in this analytic model. [Independent arithmetic cusp calculation](geometry64_infdiv_skeptic.md)
