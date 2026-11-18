# The integer comb as an extremizer of the completed theta transform

**Status.** Proposed analytic results. Riemann's hypothesis remains open. The sharp auxiliary function used below is Cohn and Kumar's Proposition 9.6. The comparison of completed transforms, its equality case, and the constructions below are deductions. No zero census or numerical calculation enters the arguments.

## A sharp comparison for positive self-dual measures

Use the Fourier convention with kernel $e^{-2\pi ixy}$, and let $\omega=\sum_{n\in\mathbb Z}\delta_n$. Suppose $\mu$ is an even positive tempered measure on the line, $\widehat\mu=\mu$ as tempered distributions, $\mu(\{0\})=1$, and
\[
 E(\mu)=\int_{x\ne0} x^{-2}\,d\mu(x)<\infty .
\]
Write $\theta_\mu(t)=\int e^{-\pi t x^2}\,d\mu(x)$ for $t>0$ and $D(t)=\theta_\mu(t)-\theta_\omega(t)$. Then
\[
 D(t)\ge0,\qquad E(\mu)\ge E(\omega)=\frac{\pi^2}{3}.
 \tag{1}
\]
Both theta functions obey $\theta(t)=t^{-1/2}\theta(1/t)$ by Fourier transformation of the Gaussian.

Here is the sharp input for the first inequality. For each $t>0$, Cohn and Kumar construct an even function $h$ with $h(x)\le e^{-\pi t x^2}$ for $x\ne0$. Its Fourier transform is continuous, nonnegative, and supported on $[-1,1]$, and
\[
 \widehat h(0)-h(0)=\sum_{n\in\mathbb Z\setminus\{0\}}e^{-\pi t n^2}.
\]
Apply their Proposition 9.6 to $f(r)=e^{-\pi tr}$. [Cohn and Kumar, *Universally optimal distribution of points on spheres*, §9](https://doi.org/10.1090/S0894-0347-06-00546-7)

For $\epsilon>0$, $h_\epsilon(x)=h(x)e^{-\pi\epsilon x^2}$ is Schwartz, since all derivatives of $h$ are bounded by its compact Fourier support. Also $h_\epsilon(x)\le e^{-\pi t x^2}$ off zero, including at points where $h(x)<0$. Its Fourier transform is nonnegative. Pairing with the self-dual measure gives
\[
 \theta_\mu(t)-1+h(0)
 \ \ge\ \langle\mu,h_\epsilon\rangle
 =\langle\mu,\widehat h_\epsilon\rangle
 \ \ge\ \widehat h_\epsilon(0).
\]
As $\epsilon\downarrow0$ the last expression converges to $\widehat h(0)$ by the Gaussian approximate identity. This proves $D(t)\ge0$. Tonelli's theorem for the two nonnegative integrands away from the origin gives
\[
 \int_0^\infty D(t)\,dt=\frac{E(\mu)-E(\omega)}{\pi}.
 \tag{2}
\]

Define the regularized completed transform on $-1<\Re s<2$ by
\[
 X_\mu(s)=\xi(s)+\frac{s(s-1)}4 M_\mu(s),\quad
 M_\mu(s)=\int_0^\infty D(t)t^{s/2}\,\frac{dt}{t}.
 \tag{3}
\]
In particular $X_\omega=\xi$. This normalization equals the usual completed Mellin transform of $\mu$ in $1<\Re s<2$:
\[
 X_\mu(s)=\frac{s(s-1)}4\pi^{-s/2}\Gamma(s/2)
                \int_{x\ne0}|x|^{-s}\,d\mu(x).
 \tag{4}
\]
Indeed $\theta_\mu(t)\to1$ as $t\to\infty$ by dominated convergence against a Gaussian, hence $\theta_\mu(t)=O(t^{-1/2})$ near zero by reciprocity. Bounding the mass of $[-R,R]$ by $e^\pi\theta_\mu(R^{-2})$ gives $O(R)$ at infinity. The integral in (4) therefore converges at infinity for $\Re s>1$ and at zero for $\Re s\le2$ by the energy assumption. Termwise Gaussian Mellin integration for both measures gives (4).

To continue (3) to the critical strip, split the Mellin integral at one and use reciprocity:
\[
 M_\mu(s)=\int_1^\infty D(t)\big(t^{s/2}+t^{(1-s)/2}\big)\,\frac{dt}{t}.
\]
For $-1\le\sigma\le2$, the sum of these two powers at real $s=\sigma$ is at most the corresponding sum at $s=2$. This follows by centering the exponents at $1/4$ and using monotonicity of $\cosh$ on the positive axis. Thus $|M_\mu(s)|\le M_\mu(2)$ throughout the closed strip, and (2) gives absolute convergence on its boundaries and holomorphy in its interior. We obtain
\[
 \boxed{\quad |X_\mu(s)-\xi(s)|\le
   \frac{|s(s-1)|}{4\pi}\left(E(\mu)-\frac{\pi^2}{3}\right),
  \qquad -1\le\Re s\le2.\quad}
 \tag{5}
\]
The endpoint $s=2$ gives equality and $X_\mu(2)=E(\mu)/(2\pi)$.

For every fixed real $0<\sigma<1$, the comb uniquely maximizes $X_\mu(\sigma)$ in this class. Indeed the multiplier $\sigma(\sigma-1)$ is negative, while $D\ge0$. Equality forces $D(t)=0$ for every $t>0$ by continuity. The same conclusion holds if $E(\mu)=E(\omega)$. To see that it forces $\mu=\omega$, differentiate the Gaussian pairing at $t=1$. The even tempered distribution $\mu-\omega$ then annihilates every even polynomial times $e^{-\pi x^2}$. It also annihilates the odd such functions by parity. Their span is dense in Schwartz space by the Hermite expansion after a fixed dilation.

## A sufficient approximation theorem and one independent comparator

Suppose $\mu_j$ belong to the class above and $E(\mu_j)\to\pi^2/3$. Equation (5) implies $X_{\mu_j}\to\xi$ uniformly on compact subsets of $-1<\Re s<2$. If each $X_{\mu_j}$ has no zero on $1/2<\Re s<1$, then Hurwitz's theorem and the symmetry of $\xi$ prove RH. The limit is nonzero as a function, since $\xi$ is positive on the real interval in question. Equivalently a hypothetical zero off the line would require a zero close to it in every sufficiently near-optimal comparator. The construction of zero-confined comparators approaching this sharp energy remains open.

One comparator with an independent proof of zero confinement is
\[
 \mu_G=\delta_0+(1-e^{-\pi x^2})\,dx .
\]
The Gaussian is Fourier-invariant, and Lebesgue measure and the unit atom exchange under Fourier transformation. Its energy is $2\pi$, by integration by parts on the positive half-line. Substituting $v=\pi x^2$ into (4), integrating by parts in $1<\Re s<2$, and continuing gives
\[
 X_{\mu_G}(s)=\pi^{-1/2}\Gamma(1+s/2)\Gamma((3-s)/2).
\]
This has no zeros in the comparison strip. Its energy is strictly above the comb's value.

## Analytic self-reciprocal theta models with displaced zeros

Let $0<\delta<1/2$, $h>0$, $c=2\cosh(\delta h)$ and $A=c+2\cosh(h/2)$. Put
\[
 \theta_h(t)=\frac{c\theta_\omega(t)+e^{h/2}\theta_\omega(e^{2h}t)
                               +e^{-h/2}\theta_\omega(e^{-2h}t)}{A}.
\]
This is the Gaussian theta series of a positive linear combination of the combs on $\mathbb Z,e^h\mathbb Z,e^{-h}\mathbb Z$. Poisson summation exchanges the last two weighted terms. Their sum with the first, normalized by $A$, is therefore a Fourier-selfdual measure $\mu_h$ in the comparison class. It has a unit atom at zero. All of the complete monotonicity inequalities $(-1)^k\theta_h^{(k)}(t)\ge0$ hold for every $t>0$ and every $k\ge0$ by the positive discrete Gaussian representation. Formula (4) now gives exactly
\[
 X_{\mu_h}(s)=\xi(s)\frac{c+2\cosh(h(s-1/2))}{A}.
 \tag{6}
\]
It follows that $X_{\mu_h}(0)=X_{\mu_h}(1)=1/2$. The extra zeros, counted as zeros of the multiplier, are exactly
\[
 s=\frac12\pm\delta+\frac{(2k+1)\pi i}{h},\qquad k\in\mathbb Z.
 \tag{7}
\]
For any prescribed finite height, $h$ can be chosen so that the entire zero multiset below that height agrees with the original. Meanwhile $X_{\mu_h}\to\xi$ locally uniformly, and $E(\mu_h)\to\pi^2/3$ by (6) at $s=2$.

The ordinary positive Fourier kernel is preserved as well. Write $G(u)=e^{u/2}\theta_\omega(e^{2u})$ and $K=(d^2/du^2-1/4)G$. Modularity makes $G$ and $K$ even. For $u\ge0$ each nonconstant term in $K$ is $e^{u/2}e^{-v}(4v^2-6v)$ with $v=\pi n^2e^{2u}\ge\pi$, so $K$ is strictly positive. It decays faster than exponentially in both directions. Twice integrating by parts on $G-e^{u/2}$ for $\Re s>1$ gives $\int K(u)e^{(s-1/2)u}\,du=2\xi(s)$, and continuation applies. For $\theta_h$ the Fourier kernel is exactly
\[
 K_h(u)=\big(cK(u)+K(u+h)+K(u-h)\big)/A>0.
\]
Thus the theta modular law, positivity of both kernels, the complete monotonicity of every theta derivative, and any finite initial zero census admit all the displaced zeros (7). The comb's extremality in (1) identifies the actual source. An argument deriving its zero confinement from that extremality is still required.

## Spectral measures from Hermite functions

Let $H_n$ be the physicists' Hermite polynomial and set
\[
 k_m(x)=e^{-\pi x^2}H_{4m}(\sqrt{2\pi}\,x)/H_{4m}(0).
\]
These functions are Fourier-invariant and $k_m(0)=1$. For a real finite combination $k=\sum a_m k_m$ with $\sum a_m=1$, put $\mu_k=\delta_0+(1-k(x))\,dx$. The Fourier symmetry and unit atom are automatic and the energy integral converges, with sign if necessary. Membership in the positive comparison class requires $k(x)\le1$ everywhere.

Its completed transform is $X_{\mu_k}(s)=X_{\mu_G}(s)P(s)$ with $P$ a real polynomial even about $1/2$ and $P(0)=P(1)=1$. For an individual $k_m$ the polynomial is
\[
 P_m(s)={}_2F_1(-2m,(1-s)/2;1/2;2).
 \tag{8}
\]
Indeed $H_{4m}(\sqrt{2v})/H_{4m}(0)={}_1F_1(-2m;1/2;2v)$, where $v=\pi x^2$. The transformed integral of $1-k_m$ for $1<\Re s<2$ is the negative analytically continued integral of $k_m$ there. This follows by splitting at $x=1$ and continuing the constant term explicitly. Termwise gamma integration of the finite series proves (8), and linearity gives $P=\sum a_mP_m$. Equivalently symmetry follows from the functional equation and normalization from the gamma formula at $s=0,1$.

Each $P_m$ has all its zeros on the critical line. To verify this property put
\[
 q_n(y)=i^n(1/2)_n\,{}_2F_1(-n,1/4+iy;1/2;2)/n!.
\]
Its generating function, obtained by expanding the finite hypergeometric coefficients, is $(1-iz)^{-1/4+iy}(1+iz)^{-1/4-iy}$. Differentiation gives
\[
 (n+1)q_{n+1}=2yq_n-(n-1/2)q_{n-1},\quad q_0=1,\quad q_1=2y .
\]
The coefficient $n-1/2$ is positive for $n\ge1$ and every leading coefficient is positive, so induction on the recurrence gives simple real interlacing zeros. Substituting $(1-s)/2=1/4+iy$ yields the asserted confinement. These are the classical Meixner–Pollaczek polynomials.

For **every** such signed mixture for which all polynomial zeros are on the critical line, the real factorization gives
\[
 \frac{E(\mu_k)}{2\pi}=P(2)=\frac{P(2)}{P(0)}
          =\prod_j\frac{9/4+\gamma_j^2}{1/4+\gamma_j^2}\ge1.
 \tag{9}
\]
The factors are the pairs $1/2\pm i\gamma_j$, including a possible even multiplicity at the center. Thus proving real-rootedness of every entire polynomial multiplier in this Gaussian basis leaves a strict energy gap. In fact any such normalized symmetric polynomial with $|P(2)|<1$ must have a root $s_j$ satisfying $\Re((s_j-1/2)^2)>5/4$: in the variable $w=(s-1/2)^2$ the distances $|9/4-w_j|$ are at least $|1/4-w_j|$ whenever $\Re w_j\le5/4$.

Zero confinement only in the critical strip can evade (9). Take
\[
 k(x)=\tfrac98 k_0(x)-\tfrac18 k_1(x)
      =e^{-v}(1+v-2v^2/3),\qquad v=\pi x^2 .
\]
Here $1+v\le e^v$ proves $k\le1$. Equation (8) yields $P(s)=1-s(s-1)/6$. Its roots at $-2,3$ cancel the first pair of exterior poles of $X_{\mu_G}$. The resulting positive spectral measure has a zero-free completed transform throughout the critical strip and has $E=4\pi/3$. This example verifies both feasibility conditions exactly while retaining a positive gap above the sharp energy.

## Removing a hypothetical quartet fails at the first spectral gap

Suppose a quartet of zeros of $\xi$ is $1/2\pm a\pm i\gamma$ with $0<a<1/2$ and $\gamma>2\pi/\log2$. Let
\[
 L(s)=\big((s-1/2-a)^2+\gamma^2\big)
       \big((s-1/2+a)^2+\gamma^2\big),\qquad P(s)=L(s)/L(0).
\]
Then $P(0)=P(1)=1$ and $P(2)>1$ because the squared distances of $2$ to both conjugate pairs exceed the corresponding product at $0$ (equivalently translate $0$ to $1$ by symmetry and increase the real argument from $1$ to $2$). If $X=\xi/P$ came from a positive measure in the comparison class, its value at $2$ would therefore contradict (1). The failure of positivity can be located directly without invoking (1).

For $\Re s>1$, the underlying Dirichlet transform on the positive half-axis would have to be $\zeta(s)/P(s)$ by (4), with the even measure furnishing the factor of two. In the variable $y=\log x$, the causal inverse Laplace transform of $1/P$ is $L(0)q(y)$, where
\[
 q(y)=\frac{e^{(1/2-a)y}}{\gamma^2}
       \int_0^y e^{2au}\sin(\gamma u)\sin(\gamma(y-u))\,du
       \quad(y\ge0),
\]
and $q(y)=0$ for $y<0$. This is the convolution of the elementary inverse transforms of the two quadratic factors. The inverse of $\zeta/P$ thus has density $L(0)\sum_{n\ge1}q(y-\log n)$. For any fixed $1<\sigma<2$ the exponentially weighted density is integrable in absolute value since each factor has an absolutely convergent Laplace integral and $\zeta(\sigma)<\infty$. The pushforward of any candidate positive measure on $x>0$, weighted by $e^{-\sigma y}$, is finite by (4). Uniqueness of Fourier transforms of finite measures on that vertical line identifies it with the stated weighted density.

At $y=2\pi/\gamma\in(0,\log2)$ the sum contains only $n=1$, and $\sin(\gamma(y-u))=-\sin(\gamma u)$. Its value is strictly negative and remains negative on an interval. The signed spectrum therefore already fails in $1<x<2$. In particular, the positivity required for the most direct deletion argument cannot be recovered from cancellations among higher integers.

## What an approximating sequence must reproduce

Let $\mu_j$ be positive comparison measures with $E(\mu_j)\to\pi^2/3$. For every fixed $t>0$, their theta values converge to $\theta_\omega(t)$. In fact (2) gives $D_j\to0$ in $L^1(dt)$ and $\theta_{\mu_j}$ is decreasing. For $0<b<t$ its value at $t$ is bounded above by the average over $[t-b,t]$. Pass to the limit in that average and let $b\downarrow0$. Inequality (1) supplies the lower bound.

The measures converge to $\omega$ in the sense of tempered distributions. They have uniformly bounded mass on each compact interval by a fixed Gaussian test, so every subsequence admits a vaguely convergent further subsequence. For a fixed Gaussian the tails beyond $R$ are bounded by $e^{-\pi tR^2/2}\theta_{\mu_j}(t/2)$, uniformly small. Thus every vague limit agrees with $\omega$ on all the Gaussians. It is tempered, since the uniform energy bound gives $O(R^2)$ mass on $[-R,R]$ for $R\ge1$. The Hermite argument above identifies the limit with $\omega$. For an arbitrary Schwartz test $f$ the tails are bounded by $\sup_{|x|>R}|x^2 f(x)|\sup_jE(\mu_j)$, yielding the claimed distributional convergence. In particular any approximants with continuous densities away from zero must concentrate unit mass at each fixed nonzero integer in the limit. A uniform local $L^p$ bound for any $p>1$ near an integer precludes this by Hölder's inequality on shrinking intervals.

There is also a uniform energy gap for a family whose transforms miss any disk containing a genuine zero. Let $B$ be a disk with closure in the open critical strip, with at least one zero of $\xi$ inside and none on its boundary. Define
\[
 b(B)=4\pi\min_{s\in\partial B}\left|\frac{\xi(s)}{s(s-1)}\right|>0 .
\]
Whenever $E(\mu)-\pi^2/3<b(B)$, (5) and Rouché's theorem force $X_\mu$ to have exactly as many zeros in $B$ as $\xi$, counting multiplicities. In particular a sequence of transforms zero-free on the *whole* critical strip cannot approach the infimum, because the existence of critical-line zeros is classical. A successful sequence with zeros on the critical line must reproduce these local multiplicities as well as the atomic mass concentration.

Finally suppose a comparison measure has no mass on $0<|x|<1$. Taking $S(x)=(\sin(\pi x)/(\pi x))^2$, $S(0)=1$, gives $\widehat S(y)=(1-|y|)_+$. Both pairings with $\mu$ are defined: $S=O(x^{-2})$ and the energy is finite. To justify Fourier exchange, pair the Schwartz function $S(x)e^{-\pi\epsilon x^2}$ and let $\epsilon\downarrow0$. On the Fourier side the triangles convolved with the Gaussian approximate identity converge boundedly on compact sets. For $|y|>2$ and $0<\epsilon\le1$ they are uniformly bounded by $C e^{-c y^2}$, which is integrable against $\mu$. It follows that $\int S\,d\mu=\int (1-|y|)_+\,d\mu(y)=1$. Positivity and $\mu(\{0\})=1$ force the remaining support onto the nonzero integers, the zeros of $S$. An integer-supported measure is fixed by multiplication by $e^{2\pi i x}$. Its Fourier transform is therefore invariant under translation by one. Self-duality and the unit atom now give $\mu=\omega$. Thus any genuinely different positive comparison measure has some mass strictly inside the first gap of the comb.

## A positive average of dilations cannot afford to repair quartet deletion

Here the amount of smoothing can vary with the height and the shifts can have unbounded support. For each $\gamma\to\infty$ take any $0<a<1/2$ and the polynomial $P=P_{a,\gamma}$ above. Let $\nu=\nu_\gamma$ be a symmetric probability measure on the real line with $m(3/2)<\infty$, where $m(r)=\int\cosh(ru)\,d\nu(u)$. Use the symmetric multiplier
\[
 M(s)=\frac{\int e^{-(s-1/2)u}\,d\nu(u)}{m(1/2)}.
\]
It preserves the boundary values at $0,1$. Suppose $\zeta(s)M(s)/P(s)$ on $1<\Re s<2$ is the bilateral Laplace transform of a positive measure on the log-coordinate line, absolutely convergent on that strip. This is necessary for $\xi M/P$ to arise from a positive comparison measure. Then
\[
 \liminf_{\gamma\to\infty}\gamma^2\big(M(2)-1\big)\ \ge\ \pi^2/2 .
 \tag{10}
\]
In comparison, the exact quartet obeys $P(2)=1+4/\gamma^2+O(\gamma^{-4})$ uniformly for $0<a<1/2$, by expansion of its two quadratics. Since $\pi^2/2>4$, a positive repaired quotient at sufficiently high ordinates has $M(2)>P(2)$; its energy exceeds the original energy. The theorem does not require the existence of any displaced zeta zero.

To prove (10) restrict to a subsequence on which $\gamma^2(M(2)-1)$ tends to a finite limit, writing $U\sim\nu$. Put $B(u)=\cosh(3u/2)-\cosh(u/2)=2\sinh(u)\sinh(u/2)$. This satisfies $B(u)\ge u^2$ and $\cosh(u/2)-1\le B(u)/8$ by the triple-angle identity. Therefore $m(1/2)=1+O(\gamma^{-2})$, $\mathbb E B(U)=O(\gamma^{-2})$, and $W=\gamma U$ has uniformly bounded second moment. After passage to a further subsequence $W$ converges in distribution to a symmetric random variable $V$ with $\mathbb E V^2\le\liminf\mathbb E W^2$.

Write the signed inverse density in the $y=\log x$ coordinate. By the convolution formula in the preceding section, after suppressing its positive constant $L(0)/m(1/2)$ and multiplying by $\gamma^3e^{-y/2}$, the density equals
\[
 \sum_{n\ge1} n^{-1/2}\,
 \mathbb E\, I_{a,\gamma}\big(\gamma(y-\log n-U)\big),
 \quad
 I_{a,\gamma}(w)=\mathbf1_{w\ge0}\int_0^w
       e^{(a/\gamma)(2r-w)}\sin r\sin(w-r)\,dr.
 \tag{11}
\]
Indeed the multiplier translates log mass by $U$ with weight $e^{U/2}$, which cancels the corresponding factor in the centered quartic kernel. For each fixed $1<\sigma<2$ all three ingredients have finite absolute Laplace transform, so Fourier uniqueness identifies this signed density with the assumed positive inverse measure. The density is continuous: the bounds in the next paragraph dominate the series of absolute values uniformly on a compact $y$ interval, using the exponential moment for large $|U|$. It is therefore nonnegative pointwise.

Fix a real $x$ and set $y=x/\gamma$. For $n\ge2$ the integral is zero unless $T=y-U\ge\log2$, hence $|U|\ge c=(\log2)/2$ for large $\gamma$. As $|I(w)|\le w e^{aw/\gamma}$ for $w\ge0$, the entire $n\ge2$ sum at a fixed $U$ has absolute value at most
\[
 \gamma e^{aT}\sum_{2\le n\le e^T} n^{-1/2-a}(T-\log n)
 \le C\gamma(1+T)^2e^{T/2}.
\]
For the last bound use $n^{1/2-a}\le e^{(1/2-a)T}$ and the harmonic sum. On $|u|\ge c$, $(1+|u|)^2 e^{|u|/2}\le C_c B(u)$. The expected contribution is consequently $O(\gamma^{-1})$.

For $n=1$, $I_{a,\gamma}(w)$ converges uniformly on compact $w$-sets to
\[
 q_0(w)=\tfrac12\mathbf1_{w\ge0}(\sin w-w\cos w).
\]
The part $|U|\ge c$ again has expectation $O(\gamma^{-1})$. In $|U|<c$, the bound is $C_x(1+|W|)$, whose expectation over $|W|>K$ is $O_x(1/K)$ by the second moment. Weak convergence applied first on compact sets and then with $K\to\infty$ therefore gives
\[
 \mathbb E q_0(x-V)\ge0\quad\text{for every real }x.
\]
For $x\to+\infty$, omitting the cutoff $V\le x$ in this expectation costs $o(1)$ because $\mathbb E|V|<\infty$. By symmetry, if $A=\mathbb E\cos V$ and $C=\mathbb E[V\sin V]$, this yields
\[
 2\mathbb E q_0(x-V)=-Ax\cos x+(A+C)\sin x+o(1).
\]
The two sequences with $\cos x=1,-1$ force $A=0$ and then those with $\sin x=1,-1$ force $C=0$.

Finally, for every real $v$,
\[
 v^2-\tfrac{\pi^2}{2}(1-\cos v)+2v\sin v\ge0 .
\]
Indeed divide by $4\sin^2(v/2)$ and set $z=v/2$. The variable part is $z^2\csc^2z+2z\cot z$, whose derivative is $2\cot z(1-z^2\csc^2z)$. On each interval between successive nonnegative multiples of $\pi$ its minimum occurs at the midpoint, where the value is at least $\pi^2/4$. The omitted multiples follow directly. Taking expectations thus gives $\mathbb E V^2\ge\pi^2/2$. Since $\mathbb E W^2\le\gamma^2\mathbb EB(U)=\gamma^2(M(2)-1)m(1/2)$, this proves (10).

The constant in (10) is attained to leading order. Set $h=\pi/\gamma$ and take the symmetric law on $0,\pm h$ whose moment generating function is
\[
 m(z)=\frac{\cosh(ha)+\cosh(hz)}{\cosh(ha)+1}.
\]
The weights are nonnegative and sum to one. With $z=s-1/2$, factor the numerator as
$2\cosh(h(z-a)/2)\cosh(h(z+a)/2)$. Since $\gamma h/2=\pi/2$,
\[
 \int_{-h/2}^{h/2}e^{bu}\cos(\gamma u)\,du
       =\frac{2\gamma\cosh(hb/2)}{b^2+\gamma^2},
\]
with removable values understood. The integrand's cosine is nonnegative on its support. Taking $b=z-a$ and $b=z+a$ shows that $M/P$ is the moment generating function in $z$ of a positive constant times the convolution of two oppositely tilted compact cosine densities. This measure is symmetric because the two densities reflect into one another. The normalization at $s=0,1$ is one. Consequently multiplying $\xi$ by $M/P$ amounts to a positive symmetric average of dilations of the comb, with the same normalization as (6). Its underlying spectral measure is positive and Fourier-selfdual. Finally,
\[
 M(2)=\frac{\cosh(ha)+\cosh(3h/2)}{\cosh(ha)+\cosh(h/2)}
      =1+\frac{\pi^2}{2\gamma^2}+O(\gamma^{-4}).
\]
The error is uniform for $0<a<1/2$. Thus the smoothing cost and the uncorrected deletion gain differ at their leading order.

## A support gap forces the energy towards the lattice minimum

For a measure in (1), suppose its support apart from zero avoids $(-r,r)$, where $0<r\le1$. Then
\[
 0\le E(\mu)-\pi^2/3
 \le \frac{1-r}{r^3}-\frac{\pi^2}{3}(1-r)^2.                      \tag{11}
\]
Thus a sequence of positive self-dual measures with support gaps tending to one would automatically meet the energy part of the approximation theorem. The required zero confinement of their completed transforms remains an additional condition.

Put $C(t)=\int_{x\ne0}(1-\cos(2\pi tx))x^{-2}\,d\mu(x)$. The energy bound gives continuity. Its second derivative as a tempered distribution is $4\pi^2(\mu-dt)$ by self-duality and the subtracted atom. One can differentiate after testing against a Schwartz function, whose Fourier transform handles the tail. On $(-r,r)$, evenness and $C(0)=0$ therefore give $C(t)=2\pi^2(|t|-t^2)$, also at the endpoints by continuity. In particular with $S(x)=\sin(\pi r x)/(\pi r x)$,
\[
 \int_{x\ne0}S(x)^2\,d\mu(x)=C(r)/(2\pi^2r^2)=1/r-1 .
\]
Averaging $C(t)$ against the triangular probability density $(1-|t|/r)_+/r$ gives
\[
 \int_{x\ne0}\frac{1-S(x)^2}{x^2}\,d\mu(x)
   =2\pi^2(r/3-r^2/6).
\]
The omitted integral of $S(x)^2/x^2$ is at most $r^{-2}(1/r-1)$ by the support gap. This proves the upper bound in (11), and the lower bound is (1). At $r=1$, the sinc-square identity forces the nonzero support onto the integers. In particular no other measure with that gap and normalization can give a different extremal transform.
