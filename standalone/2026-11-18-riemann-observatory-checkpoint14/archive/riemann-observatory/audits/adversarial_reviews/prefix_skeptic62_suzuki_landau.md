# Suzuki’s unshifted function and eventual exponential lower bounds

I checked Suzuki’s *Aspects of the screw function corresponding to the Riemann zeta-function*, version of May 31, 2023, Theorem 1.1, §7.2 and §11. The cached primary PDF is [suzuki_aspects.pdf](../../sources/effective_cluster62_operator2/suzuki_aspects.pdf), SHA-256 eabccec3c2bfee2eb12077181b564e508270f80698f4a8c64ccf105b30119f41. The norm identity comes from Theorem and Corollary 1.1 and §3.3 of [suzuki_screw_line.pdf](../../sources/effective_cluster62_operator2/suzuki_screw_line.pdf), SHA-256 022d42869c10420f81c0f09ccf49c5e0a037a2fd50c35392d4205db61683db42.

For each real $\omega\ge0$, the following are equivalent.

1. There are finite $C,T\ge0$ such that Suzuki’s unshifted $\Psi(t)=-g(t)$ satisfies $\Psi(t)\ge-Ce^{\omega t}$ for every $t\ge T$.
2. The completed zeta function $\xi$ has no zero in $\Re s>1/2+\omega$.

The exponent in the first condition is exact. The strict inequality specifying the zero-free half-plane allows zeros on its boundary.

## From zeros to growth

Put $Z=\{\gamma:\xi(1/2-i\gamma)=0\}$, with multiplicities. Suzuki’s formula (1.3) gives
\[
\Psi(t)=\sum_{\gamma\in Z}\frac{1-e^{i\gamma t}}{\gamma^2}.
\]
The $\xi$ zero count $O(Y\log(Y+2))$ for $|\Im s|\le Y$ and the absence of a central zero give $S=\sum_{\gamma\in Z}|\gamma|^{-2}<\infty$. The functional equation gives $|\Im\gamma|\le\omega$ from condition 2, so $|\Psi(t)|\le S(1+e^{\omega t})$ for every $t\ge0$. Under ordinary RH the real-ordinate cosine formula also gives $\Psi(t)\ge0$. For $\omega\ge1/2$, the standard zero strip already gives condition 2.

## From eventual domination to a zero-free half-plane

In (1.2), set $z=iu$. The initial identity on $\Re u>1/2$ is
\[
\int_0^\infty\Psi(t)e^{-ut}\,dt=\frac{\xi'(1/2+u)}{u^2\xi(1/2+u)}.
\]
Take $f(t)=\mathbf1_{[T,\infty)}(t)(\Psi(t)+Ce^{\omega t})$. Its nonnegative Laplace integral has an abscissa of convergence $a\le\max(1/2,\omega)$ by the absolute series and the standard zero strip. It may be $-\infty$. On the initial common half-plane its transform is the following meromorphic expression.
\[
M(u)=\frac{\xi'(1/2+u)}{u^2\xi(1/2+u)}
+\frac{C}{u-\omega}-\int_0^T(\Psi(t)+Ce^{\omega t})e^{-ut}\,dt.
\]
The last term is entire by continuity on the finite interval. Analyticity of the integral on $\Re u>a$ and the meromorphic identity theorem identify its transform with $M$ throughout that half-plane. This also makes every possible pole there removable.

If $a$ were finite and greater than $\omega$, the expression would be regular near the real point $a$. Indeed $\xi(s)\ne0$ for real $s>1/2$. For $1/2<s<1$, the alternating eta series is strictly positive by grouping consecutive pairs, while $1-2^{1-s}<0$, hence $\zeta(s)<0$. At $s=1$ the $\xi$ factor cancels the simple zeta pole and leaves a nonzero value. For $s>1$ the convergent Euler product is nonzero. Both explicit denominators outside $\xi$ are nonzero at $a$.

Such continuation contradicts the Laplace form of Landau’s theorem. For completeness, if the analytic continuation exists on a disk centered at finite $a$, choose a real center $b>a$ close enough to $a$ that its Taylor disk inside that continuation disk reaches a real $x<a$. Moments give the Taylor coefficients of $F(b-v)$ as $\int t^n f(t)e^{-bt}\,dt/n!$. Differentiation is justified by convergence at a real point between $a$ and $b$. At $v=b-x$ the Taylor series converges and all terms are nonnegative. Tonelli then gives $\int f(t)e^{-xt}\,dt<\infty$, contradicting the abscissa.

Consequently $a\le\omega$. The meromorphic identity implies regularity of $M$ across $\Re u>\omega$. A zero $\rho$ there would give the nonzero residue $m_\rho/(\rho-1/2)^2$ at $u=\rho-1/2$, since both the finite-interval correction and rational compensator are regular there. This proves condition 2. The possible singularity at $u=0$ when $\omega=0$ is outside the open half-plane in this argument.

## Scope

A polynomial factor in the permitted negative bound gives the same zero-free conclusion. For every $\epsilon>0$ that bound implies a constant multiple of $e^{(\omega+\epsilon)t}$, so the open half-planes exhaust $\Re s>1/2+\omega$. Conversely the exact bound follows from the first direction. A zero strictly past the line forces $\liminf_{t\to\infty} e^{-\omega t}\Psi(t)=-\infty$, by negating the quantified eventual bound.

Suzuki §7.2 already uses Landau’s argument for positivity. §11 shifts the argument of $\xi'/\xi$ and studies the resulting modified function $\Psi_\omega$. The present formulation keeps $\Psi$ fixed and shifts the size of the permitted deficit. At $\omega=0$ it identifies an eventual constant lower bound as equivalent to RH. Suzuki’s screw-line §3.3 already uses eventual nonnegativity in proving the corollary to the norm identity.

A finite calculation of $\|S_t\|^2$ gives a nonnegative norm. Using it to establish criterion 1 would still require a comparison with $2\Psi(t)$ with a certified deficit bound over the entire tail. The positivity of a norm or evaluations at finitely many $t$ alone supply no such comparison. This argument establishes an equivalence and supplies no unconditional bound of the form in criterion 1 for $\omega<1/2$.
