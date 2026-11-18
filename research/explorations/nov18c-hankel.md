# The Schatten norms of the zeta translation and its arithmetic Hankel kernel

**Proposed analytic theorem.** In the notation of the [compressed translation](nov18c-shift.md), write $T_t=P_KM_{e^{-tz}/(2+z)}|_K$ and $d_*=3/2-\Theta$. For every $2\le p\le\infty$,
\[
     \lim_{t\to\infty}-\frac1t\log\|T_t\|_{S_p}
                   =\min\{d_*,1-1/p\}.                               \tag{1}
\]
Here $S_\infty$ is the operator norm. In particular the Hilbert–Schmidt norm always decays as $e^{-t/2+o(t)}$. The contribution forcing this rate comes from the actual arithmetic kernel. An absolute bound for that kernel cannot give even the known smaller operator norm. We identify below a rank-one term that cancels across all divisors, an operator estimate at exponent one for every fixed collection of the remaining divisors, and the precise large-divisor part left open.

More generally let $T_{\alpha,t}=P_K M_{e^{-tz}(2+z)^{-\alpha}}|_K$. For every $0<p<\infty$ and $t\ge0$ it belongs to $S_p$ exactly when $\alpha>1/p$. In that case the exponent in (1) is $\min(d_*,\alpha-1/p)$, using the Schatten quasi-norm when $p<1$. In particular smoothing of order $3/2$ suffices for the Hilbert–Schmidt norm to detect the full zero abscissa. The last section uses a different compact smoothing for which the requisite arithmetic estimate reduces to a mean square of explicit Möbius sums in short multiplicative ranges.

## The kernel in physical coordinates

Use the Laplace transform on $L^2(0,\infty)$ and boundary measure $dy/(2\pi)$. Its range is the right half-plane Hardy space. For the meromorphic inner function $I(z)=\xi(z-1/2)/\xi(z+3/2)$ let $P_-$ be projection onto negative times. For every analytic bounded multiplier $f$ and $v$ in the Hardy space,
\[
 I P_-(\overline I f v)=P_K(fv).
\]
Indeed $I P_+(\overline I fv)$ is the orthogonal projection of $fv$ onto $I H^2$. The right-hand side annihilates $I H^2$ as a function of $v$. Consequently the nonzero singular values of $T_t$ are precisely those of the Hankel operator with symbol $\overline I e^{-tz}/(2+z)$.

Let $i(u)$ be the real causal inverse Laplace kernel in equation (6) of the linked translation proof. For $u\ge0$ put
\[
 a(u)=\int_0^\infty e^{-2v}i(u+v)\,dv .
\]
The inverse transform of $e^{-tz}/(2+z)$ is $e^{-2(u-t)}\mathbf1_{u\ge t}$. Convolution with the time reversal of $i$, followed by reflection of the negative output axis, gives the Hankel kernel $a(t+x+y)$, $x,y\ge0$. This identity also follows distributionally. The formula for $i$ gives $i(u)=O(e^{u/2})$, so $a$ is defined classically and $a'=2a-i$ almost everywhere. The bound $a(u)=O((1+u)e^{-u/2})$ proved below makes the zero extension of $2a-a'$ on the positive half-line tempered, using the derivative of the zero extension and the endpoint mass $a(0)\delta_0$. Its Laplace transform agrees with $I$ on the original half-plane, hence on the right half-plane by analytic continuation. On negative output times the convolution above takes its classical value. As an alternative expression, integrating the two partial fractions termwise gives, for $X=e^u$,
\[
 \frac{a(\log X)}{2\pi}
  =\frac67 X^{-3/2}\sum_{n\le X}J_2(n)
     -\frac45 X^{-1/2}\sum_{n\le X}\frac{J_2(n)}{n}
     +\frac{2}{35}X^2\sum_{n>X}\frac{J_2(n)}{n^{7/2}}.              \tag{2}
\]
Here $J_2(n)=\sum_{d\mid n}\mu(d)(n/d)^2$, so all three sums in (2) converge at each fixed $X$. Termwise integration is allowed even in the two future tails before combining them, since $J_2(n)\le n^2$.

## A rational Fourier coefficient surviving at all scales

Write $b(x)=1/2-\{x\}$, and set $A(X)=X^{1/2}a(\log X)/(2\pi)$ and $S(X)=i(\log X)/(2\pi\sqrt X)$. Differentiation and the floor formula give, for $X\ge2$,
\[
 A'(X)=\frac{5}{2X}A(X)-S(X),\qquad
 S(X)=\sum_{d\ge1}\frac{\mu(d)}{d^2}b(X/d)
                        +O\!\left(\frac{\log(2X)}X\right).           \tag{3}
\]
The differential identity holds almost everywhere. For the uniform error, replace $\lfloor X/d\rfloor(\lfloor X/d\rfloor+1)$ by $(X/d)^2+O(X/d+1)$ in the exact finite sum divided by $X^2$ and pay $O(1/X)$ for the added infinite tail.

The decay condition at infinity inherited from $i(u)=O(e^{u/2})$ gives $A(X)=X^{5/2}\int_X^\infty S(V)V^{-5/2}\,dV$. The displayed error in (3) costs $O(\log X)$ in this formula. For $d\le X$ the periodic function $b(V/d)$ has mean zero and an absolute primitive bound $O(d)$. Integrating by parts bounds its contribution by $O(1/d)$ after the coefficient and the factor $X^{5/2}$. For $d>X$ use the uniform bound $O(1/X)$ on the tail of the series. This proves $A(X)=O(\log(2X))$ and the asserted bound for $a$.

For each nonzero integer $m$ and smooth $\phi$ supported on $[1,2]$,
\[
 \lim_{Y\to\infty}\int\phi(v)A(Yv)e^{-2\pi i mYv}\,dv
      =\frac{1}{4\pi^2m^2\zeta(3)}\int\phi(v)\,dv .                 \tag{4}
\]
The limit is uniform over bounded $C^1$ families with this support. For $S$ in place of $A$ the coefficient is $1/(2\pi i m\zeta(3))$. Indeed, $b(V/d)e^{-2\pi i mV}$ is periodic of period $d$ and has mean $1/(2\pi i m d)$. Subtracting its mean leaves a bounded primitive for fixed $d$, so integration against $\phi(V/Y)$ gives the indicated limit for any fixed finite set of divisors, uniformly in the family. The remaining divisor mass is bounded by $\sum_{d>D}d^{-2}$ and the error of (3) tends to zero. Integration by parts against $e^{-2\pi i mYv}$ and (3) now give (4), since the two terms containing $A(Yv)/Y$ cost $O(\log Y/Y)$.

In particular $\int_Y^{2Y}|A(V)|^2\,dV\gg Y$ for every sufficiently large $Y$, by Cauchy–Schwarz with any fixed $\phi$ of nonzero integral. The Hilbert–Schmidt identity is
\[
 \|T_t\|_{S_2}^2=\int_0^\infty v\,|a(t+v)|^2\,dv.
\]
The bound for $A$ gives $O((1+t)^2e^{-t})$. For the reverse bound restrict $v$ to $[\log 2,\log4]$ and apply the dyadic lower bound. Thus even before using the location of any zeta zero, its squared Hilbert–Schmidt norm is at least $ce^{-t}$ for all large $t$.

## Many independent tests of the kernel

Set $X=e^t$. Changing variables from $x=\log p$, $y=\log q$ to $p,q\ge1$ with the unitary weight $p^{-1/2}$ sends the Hankel kernel to
\[
                 2\pi X^{-1/2}(pq)^{-1}A(Xpq)
\]
on $L^2([1,\infty),dp)$. Choose a nonnegative smooth $\chi$ of positive integral supported in $(1,2)$. For each integer $\ell\in[X,2X]$ use input $f_\ell(q)=q\chi(q)e^{-2\pi i\ell q}$. These inputs have a uniform Bessel bound, by orthogonality of the integer exponentials on $[1,2]$ and boundedness of $q\chi(q)$. For $p\in[\ell/X,(\ell+\delta)/X]$ the integral in the output, after the factor $2\pi X^{-1/2}/p$, is the left side of (4) with $m=1$, $Y=Xp$ and $\phi(q)=\chi(q)e^{2\pi i(Xp-\ell)q}$. Its real part is bounded below uniformly by a fixed positive constant for small fixed $\delta>0$ and large $X$. This uses the uniformity in (4).

Take the normalized interval indicators on those disjoint output intervals as $g_\ell$. Each diagonal pairing has real part $\gg X^{-1}$. The synthesis maps associated with $f_\ell,g_\ell$ have bounded norm. Compressing between them and taking the diagonal of the resulting finite matrix are bounded operations on $S_p$, the latter contractive by averaging diagonal unitary conjugations. Hence for $1\le p\le\infty$ whenever the norm is finite,
\[
                    \|T_t\|_{S_p}\gg_p X^{-1+1/p}.                  \tag{5}
\]
In particular the arithmetic gives a uniform $ce^{-t}$ lower bound for the actual operator norm.

## Matching upper bounds

For $2\le p<\infty$ fix $0<b<d<\min(d_*,1-1/p)$. The holomorphic approximation in the [shift proof](nov18c-shift.md) gives a bounded analytic $H$ for $f=e^{-tz}/(2+z)$, whose boundary residual $r=f-IH$ equals $Iu$ on the imaginary axis. There $u$ is the Cauchy transform of a function supported on $b\le\Re z\le d$ of modulus $\ll e^{-bt}(1+|\Im z|)^{-\nu}$ with a fixed $1/p<\nu<1-d$. Its distance in real part from the boundary is at least $b$. Splitting the convolution of $(1+|v|)^{-\nu}$ and $(1+|v|)^{-1}$ at $|v-y|=|y|/2$ and $|v|=2|y|$ gives
\[
 |r(iy)|\ll e^{-bt}(1+|y|)^{-\nu}\log(2+|y|).
\]

For any finite orthonormal set $e_j$ in $K$, almost everywhere
$\sum_j|e_j(iy)|^2\le |I'(iy)|$. Indeed Bessel's inequality at $x+iy$ bounds the sum by $(1-|I(x+iy)|^2)/(2x)$, the squared model-space reproducing-kernel norm with our normalization. Approach the boundary, where $I$ is regular and unimodular. Furthermore $|I'(iy)|\ll\log(2+|y|)$ because $I(iy)=\overline{\xi(3/2+iy)}/\xi(3/2+iy)$; its phase derivative is bounded by Stirling and the absolutely convergent logarithmic Euler derivative.

On any finite-dimensional input section take eigenvectors $e_j$ of the compression of $M_{|r|^2}$. Scalar Jensen for the convex power $p/2$ gives
\[
 \sum_j \left(\int |r|^2|e_j|^2\,\frac{dy}{2\pi}\right)^{p/2}
 \le \int |r(iy)|^p |I'(iy)|\,\frac{dy}{2\pi}\ll e^{-pbt}.
\]
Since this holds on all finite sections, $M_r|_K$ has $S_p$ norm $\ll e^{-bt}$. Its compression equals $T_t$. Letting $b$ increase proves the required upper bound. Conversely the operator norm lower bound from any individual zero gives the decay exponent at most $d_*$ for every $p$. Combine it with (5) to obtain (1), using the shift proof for the $p=\infty$ upper bound. In particular the ratio $\|T_t\|_{S_2}^2/\|T_t\|^2$ has logarithm $2(1-\Theta)t+o(t)$.

## The threshold for arbitrary smoothing order

For $p\ge2$, $\alpha>1/p$, the upper-bound argument just given applies with $d<\min(d_*,\alpha-1/p)$ and any $1/p<\nu<\min(1,\alpha-d)$. At $t=0$, integrability follows also by applying the trace bound directly to $(2+iy)^{-\alpha}$. For $0<p<2$ take an integer $k$ with $kp\ge2$. Factor the compression into $k$ factors, assigning smoothing order $1/(kp)+\epsilon$ and time zero to $k-1$ factors, and the remaining order and all time $t$ to the last. Compressions of analytic multipliers multiply because $IH^2$ is invariant. The Schatten Hölder product inequality (valid for positive exponents) applied with all factors in $S_{kp}$ gives the upper decay bound for every $b<\min(d_*,\alpha-1/p-(k-1)\epsilon)$. Let $\epsilon\downarrow0$.

For the matching lower bound take fixed $0<x<1/2$, $L=M e^t$ and points $s_j=x+ij$ for integers $j\in[L,2L]$. The normalized Hardy kernels $k_{s_j}$ have a Bessel bound depending only on $x$. Their inverse Laplace functions are $\sqrt{2x}e^{-xu}e^{iju}$; decompose the positive half-line into intervals of length $2\pi$ and use Fourier orthogonality with a geometric majorant. For an integer $m\ge\alpha$, put $\psi_L(z)=(z/(z+L))^m$. This is a contraction, satisfies $|\psi_L(s_j)|\gg_m1$, and
\[
          \sup_y|\psi_L(iy)(2+iy)^{-\alpha}|\ll_\alpha L^{-\alpha}
\]
for $L\ge1$, by splitting at $|y|=L$. Apply $T_{\alpha,t}$ to $P_K(\psi_L k_{s_j})$ and pair with $P_K k_{s_j}$. Both families have uniform Bessel bounds. The difference from $e^{-ts_j}(2+s_j)^{-\alpha}\psi_L(s_j)$ has absolute value at most $C L^{-\alpha}|I(s_j)|$, since $\|(1-P_K)k_{s_j}\|=|I(s_j)|$. The [shift proof](nov18c-shift.md) gives $|I(s_j)|\ll_x L^{-x}$. Choosing $M$ large in terms of $x,\alpha$ yields diagonal absolute values $\gg e^{-tx}L^{-\alpha}$ for all large $t$. For $p\ge1$, as in (5) the $S_p$ norm is therefore $\gg e^{-tx}L^{1/p-\alpha}$. For $p<1$ let $E$ be the finite matrix of these pairings including off-diagonal entries. Its operator norm is $O_x(L^{-\alpha})$: use $P_KM_f=P_KM_f P_K$ to put $\psi_L$ directly next to $f$, and apply the Bessel bounds. Its trace norm is at least the sum of absolute diagonal values. Thus $\sum s_j(E)^p\ge\|E\|^{p-1}\sum s_j(E)\gg_x e^{-tx}L^{1-\alpha p}$. The two Bessel compressions are bounded also on Schatten quasi-norms. Let $x\downarrow0$ and combine with the bound at each zero to get the stated exponent.

Finally, in every sufficiently high dyad $Y\le|\Im\lambda|\le2Y$ there are $\gg Y$ distinct zeros $\lambda$ of $I$, by Riemann–von Mangoldt and the $O(\log Y)$ unit-interval multiplicity bound. Their Hardy kernels are linearly independent adjoint eigenvectors (finite Cauchy kernels with distinct poles are independent). On their finite spans the sum of the $p$th powers of the eigenvalue moduli is bounded by the $p$th power of the full $S_p$ norm, by the finite-dimensional Weyl inequality. Each modulus is $\gg_{\alpha,t}Y^{-\alpha}$, since $1/2<\Re\lambda<3/2$. Adding disjoint dyads forces nonmembership when $\alpha p\le1$, including the endpoint.

## Individual singular values and a rank-one allowance

Let $j\ge1$ be fixed and put $d_j=\inf\{d:\#\{\lambda:\Re\lambda\le d\}\ge j\}$, counting multiplicities. For every $\alpha>0$,
\[
     \lim_{t\to\infty}-t^{-1}\log s_j(T_{\alpha,t})=\min(\alpha,d_j).
\]
For the upper norm bound fix $0<b<d<\min(\alpha,d_j)$. Remove a finite Blaschke product $B$ consisting of all model zeros with $\Re\lambda\le d$, of degree at most $j-1$, and write $I=B I_1$. Take $d'$ strictly between $d$ and $d_j$. There are only finitely many model zeros with $\Re\lambda\le d'$, so none at sufficiently large height. The disk argument of the shift proof for the reciprocal bound on $0\le x\le d$ therefore applies at large height using $d'$ as rightward margin. Removing $B$ introduces no new small denominator there. On bounded ordinates $I_1$ is zero-free in this closed strip. The same holomorphic approximation gives operator norm $O(e^{-bt})$ on $K_{I_1}$. The subspace $B K_{I_1}$ is invariant for the compressed analytic multiplier, and there it is unitarily equivalent to this smaller compression, since $K_I=K_B\oplus B K_{I_1}$. Its codimension is at most $j-1$, proving the desired upper bound by min–max.

For the other direction take $j$ zeros counted with multiplicity and real parts at most $d_j+\epsilon$. Their evaluation and successive derivative kernels, through the selected local multiplicities minus one, form an independent invariant $j$-dimensional subspace of the adjoint. This follows by the product rule and the distinct poles and orders of the rational Hardy kernels. Its inverse is represented by multiplication on these finite jets by the reciprocal symbol $e^{tz}(2+z)^\alpha$, followed by adjunction. In a fixed basis its norm is $O((1+t)^{j-1}e^{(d_j+\epsilon)t})$. Min–max gives the corresponding lower singular bound. To see the independent floor at exponent $\alpha$, use the high-frequency matrix $E$ in the preceding argument. It has size comparable to $L$, norm $O_x(L^{-\alpha})$ and trace norm $\gg_x L^{1-\alpha}e^{-tx}$. After dropping the first $j-1$ singular values the latter lower bound still holds for large $t$, since $x<1/2$ and $L=M e^t$. Thus $s_j(E)\gg_x L^{-\alpha}e^{-tx}$, and the Bessel bounds give the same estimate up to constants for $T_{\alpha,t}$. Let $\epsilon,x\downarrow0$.

All nontrivial zeta zeros have nonzero imaginary part, and conjugation preserves the real part, so $d_2=d_1=d_*$. Consequently RH would follow even from a bound $e^{-t+o(t)}$ on the distance of $T_{1,t}$ to the operators of rank at most one, along one unbounded sequence of times. Its largest singular value would require no separate estimate in that argument.

## The cancellation across divisors

Define $j$ by the same future exponential average as $a$, starting from the single-divisor input $Y^{-3/2}\lfloor Y\rfloor(\lfloor Y\rfloor+1)b(Y)$, $Y=e^u$. The input vanishes for $Y<1$. Then
\[
 \frac{a(\log X)}{2\pi}=\sum_{d\ge1}\frac{\mu(d)}{d^{3/2}}j(\log(X/d)).
\]
The interchange is absolutely summable under the averaging integral: the sum of the absolute input terms is $O((Xe^v)^{1/2})$ there. For $Y<1$, equation (2) with single-divisor Jordan weight $m^2$ gives $j(\log Y)=(2/35)\zeta(3/2)Y^2$. For $Y\ge1$,
\[
 j(\log Y)=Y^{-1/2}
       \left[\frac12 B_2(\{Y\})+\frac1{15}\right]+O(Y^{-3/2}),
 \qquad B_2(x)=x^2-x+1/6.                                           \tag{6}
\]
Indeed the defining expression is $Y^2$ times the integral from $Y$ to infinity of
$V^{-5/2}b(V)+2V^{-7/2}b(V)^2+O(V^{-9/2})$. The mean-zero periodic primitive of $b$ is $-B_2(\{V\})/2$. A second integration by parts on its mean-zero remainder gives the first term of (6) with error $O(Y^{-3/2})$. The mean of $2b^2$ is $1/6$, yielding $Y^2 (1/6)(2/5)Y^{-5/2}=Y^{-1/2}/15$; its mean-zero remainder costs $O(Y^{-3/2})$ as well.

The constant produces a rank-one contribution proportional to $X^{-1/2}\sum_{d\le D}\mu(d)/d$ in every finite divisor section. Center the full function by replacing $j(\log Y)$ by $j(\log Y)-Y^{-1/2}/15$ for all $Y>0$. Summing in increasing divisor order preserves the full kernel by the classical PNT identity $\sum_{d\ge1}\mu(d)/d=0$. For a cutoff $1\le D\le X$ the centered contribution of $d\le D$ to the Hankel **operator norm** is
\[
                       O(X^{-1}\sqrt D+D X^{-3/2}).                  \tag{7}
\]
To see the oscillatory saving, the Fourier series of $B_2$ has coefficients $O(|m|^{-2})$ for $m\ne0$ and constant zero. In the variables $p,q\ge1$ the corresponding single harmonic, apart from its factor $O(X^{-1/2}/d)$, acts by the kernel $(pq)^{-1}e^{2\pi i mXp q/d}$. Extend the input multiplied by $q^{-1}$ by zero to the real line and apply Plancherel at the rescaled frequency $mXp/d$. Multiplication by $p^{-1}$ on the output is contractive. The resulting norm is at most $(|m|X/d)^{-1/2}$. Summing $m$ and $d$ gives the first term of (7). The error in (6) is $O(X^{-3/2}(pq)^{-3/2})$ in the original logarithmic kernel for each divisor, with integrable squared Hankel weight, giving the second term.

Thus even all divisors through $D=X^{o(1)}$ meet the operator decay rate required by RH after the necessary common centering. The centered remainder includes the actual Möbius signs on growing divisor ranges, in particular where $Xpq/d$ is of order one and there is no large oscillatory phase. Combining (7) with the operator criterion in the shift proof leaves exactly the bound $X^{-1+o(1)}$ for that remainder. The Hilbert–Schmidt exponent and (5) show quantitatively why an estimate that discards the oscillations cannot supply it.

## Removing the far divisor ranges before taking the mean square

Fix any $H>0$. There is a real smooth signed $w$ supported in $[0,H]$ such that, for
\[
 J(Y)=\int_0^H w(v)(Ye^v)^{-3/2}
            \lfloor Ye^v\rfloor(\lfloor Ye^v\rfloor+1)b(Ye^v)\,dv ,
\]
one has $J(Y)=0$ for $Y<e^{-H}$ and $|J(Y)|\ll\sqrt Y\,e^{-c\sqrt Y}$ for $Y\ge1$. For sufficiently large fixed $C=C_H$, set
\[
 B(Z)=\sum_{Z/[C\log^2(2Z)]\le d\le e^H Z}
               \frac{\mu(d)}{d^{3/2}}J(Z/d).
\]
Then the following identity of exponents holds for the actual Möbius coefficients:
\[
 \lim_{X\to\infty}
   \frac{-\log\!\left(\displaystyle\int_0^\infty v
                       |B(Xe^v)|^2\,dv\right)}{\log X}
       =2d_*=3-2\Theta .                                             \tag{8}
\]
In particular a bound by $X^{-2+o(1)}$ even on one unbounded sequence would suffice for RH. The signed square on the specified divisor range remains to be estimated.

To construct $w$, use a real nonnegative compact smooth probability density $g$ with Laplace transform $G$ zero-free on $\Re z\ge0$ and derivative bounds $\|g^{(k)}\|_\infty\le C_0^{k+1}(k!)^2$. For one explicit construction, convolve the tilted exponential densities of the [fixed Weil test](nov18c-weil.md), now taking $b_j=Bj^2$ and $H_j=D\log(j+2)/b_j$ for large fixed $D$, then $B$ large enough that $\sum H_j<H$. Each normalized factor of $G$ is proportional to $(1-e^{-(b_j+z)H_j})/(b_j+z)$ and has no zero in the closed right half-plane. The product is nonzero there at each fixed point, since $\sum H_j<\infty$ makes the deviations from 1 absolutely summable. As on the real Fourier line in the previous construction the numerator corrections have bounded product. The $\gg\sqrt{|\tau|}$ factors with $b_j\le|\tau|/2$ imply $|G(i\tau)|\ll e^{-c\sqrt{|\tau|}}$. Inversion bounds the $k$th derivative by a constant times $\int_0^\infty u^k e^{-c\sqrt u}du=2(2k+1)!/c^{2k+2}$, which gives the desired derivative estimates after enlarging $C_0$.

Put $w=g'-g/2$, whose transform is $F(z)=(z-1/2)G(z)$. Thus $F$ has no zero at any model-space zero $\lambda$, and $\int w(v)e^{-v/2}dv=0$. On each bounded vertical strip $F$ decays faster than every power of the ordinate, by integration by parts. The compressed multiplier with symbol $e^{-tz}F(z)$ has Hilbert–Schmidt decay exponent $d_*$. Indeed the Cauchy-transform and trace proof above works for every $b<d_*$ using rapid vertical decay. Testing at each $\lambda$ gives the converse. Its time-domain Hankel kernel at $t+x+y=\log Z$ is $2\pi\sum_{d\ge1}\mu(d)d^{-3/2}J(Z/d)$ by the compact smoothing, with only finitely many nonzero terms.

For the upper tail bound on $J$, expand the single-divisor input for $V\ge1$ exactly as
\[
 V^{1/2}b(V)+2V^{-1/2}b(V)^2
                  -V^{-3/2}\{V\}(1-\{V\})b(V).
\]
The first and last periodic coefficients have mean zero, and the mean $1/6$ of the middle coefficient contributes zero to $J$ since $F(1/2)=0$. For each remaining periodic coefficient $b_0$ and power $\theta\in\{1/2,-1/2,-3/2\}$ change variable $s=e^v$ to obtain $Y^\theta\int \phi_\theta(s)b_0(Ys)\,ds$ with $\phi_\theta(s)=w(\log s)s^{\theta-1}$ supported in $[1,e^H]$. This function satisfies bounds $C^{k+1}(k!)^2$ on its derivatives. For clarity, the composition bound follows by extracting the $k$th formal Taylor coefficient from $\sum_{j=0}^k w^{(j)}(\log s)[\log(1+h/s)]^j/j!$. The coefficient of $h^k$ in the latter power is bounded in absolute value by $C_H^k$ uniformly in $j\le k$, by Cauchy's bound on a small fixed circle where $|\log(1+h/s)|\le1$. Use $j!\le k!$ and multiply back by $k!$. The analytic factor $s^{\theta-1}$ obeys the same coefficient bound. Vanishing to every order at the support boundaries permits extension by zero. Integrating by parts $k\asymp\sqrt{|\xi|}$ times gives $|\widehat\phi_\theta(\xi)|\ll e^{-c\sqrt{|\xi|}}$. Fourier expansion of $b_0$ therefore gives $O(e^{-c'\sqrt Y})$ for its integral, since all its Fourier coefficients are bounded and its constant term vanishes. One may first use Fejér means of the bounded piecewise polynomial and then dominated convergence on both sides.

For $d<Z/[C\log^2(2Z)]$, the absolute sum is now $\ll \sqrt Z \sum_{d\ge1}d^{-2} e^{-c\sqrt C\log(2Z)}=O(Z^{-2})$ by increasing $C$. Above $e^H Z$ all terms are zero. The discarded error has norm $O(X^{-2})$ in $L^2(v\,dv)$ at $Z=Xe^v$. The complete Hilbert–Schmidt norm, up to $2\pi$, equals the same weighted norm of the untrimmed sum and has exponent $d_*\le1$. The two-sided triangle inequality then proves (8).

### How short the divisor range can be by absolute estimates

For every fixed $b>1$, the lower cutoff in (8) can be increased to $Z/L_b(Z)$, where
\[
          L_b(Z)=C_{H,b}\log(2Z)(\log\log(10Z))^b .                 \tag{9}
\]
The endpoint $b=1$ fails for this absolute truncation mechanism for **every** nonzero smooth compact $w$ with the required vanishing moment, and every fixed positive constant in (9). More precisely the discarded sum of absolute values is at least $Z^{-1/2-o(1)}$ on an unbounded sequence at that endpoint.

For the upper assertion choose $g$ to be the law of a sum of independent uniform variables on $[0,h_j]$, $h_j=c/[j\log^b(j+2)]$, taking $c$ small enough that $\sum h_j<H$. Its Laplace transform is a product of the factors $(1-e^{-zh_j})/(zh_j)$, each zero-free on the open right half-plane, and the product is nonzero there by absolute summability of the deviations at fixed $z$. Its $k$th derivative is bounded by $2^k/(h_1\cdots h_k h_{k+1})$: differentiate the first $k$ interval densities distributionally, use their total variation bounds, use the next density in $L^\infty$ and the rest as probabilities. A further undifferentiated density gives continuity. The resulting derivative bound is $C^{k+1}k![\log(k+3)]^{bk}$, after absorbing one polynomial factor into the constant power. This derivative class is retained by $g'-g/2$ and by $w(\log s)s^{\theta-1}$, by the same Taylor-coefficient argument as above. Integration by parts $k$ times with $k$ a small constant times $|\xi|/\log^b(3+|\xi|)$ gives Fourier decay $\exp[-c'|\xi|/\log^b(3+|\xi|)]$. Summing over nonzero periodic harmonics preserves this estimate with a smaller constant, since $m/\log^b(3+mY)\gg_b \sqrt m/\log^b(3+Y)$ for $m,Y\ge1$. Thus the bound on $J(Y)$ has the factor $\exp[-c''Y/\log^b(3+Y)]$. Taking $Y\ge L_b(Z)$ and increasing $C_{H,b}$ gives the same $O(Z^{-2})$ error. All other arguments establishing (8) apply to this $g$.

For the converse, let $U(Y)=\operatorname{sgn}(Y)|Y|^{3/2}J(|Y|)$. Its Fourier transform, with frequencies $e^{2\pi i\xi Y}$, vanishes on $(-1,1)$ in the sense of distributions. Indeed the three terms in the expansion of the single-divisor input give $U$ as $Y^2$ times a weighted average of the odd periodic $b(Ye^v)$, plus $Y$ times a weighted average of the even $2b(Ye^v)^2$, plus a weighted average of the odd periodic $-\{Ye^v\}(1-\{Ye^v\})b(Ye^v)$. These parities establish the claimed odd extension almost everywhere. The constant term in the middle average cancels by $\int w(v)e^{-v/2}dv=0$. Each remaining Fourier mode has $|\xi|=|m|e^v\ge1$ for $v\in[0,H]$, $m\ne0$. Multiplication by a polynomial preserves that Fourier support. Using Fejér means justifies the assertion against Schwartz tests, by dominated convergence with a polynomial majorant. The function $U$ is nonzero. On $\Re z>3/2$ the bilateral Laplace transform of $J(e^u)$ is
\[
 F(-z)\frac{z-3/2}{(z+3/2)(z+1/2)}\zeta(z-1/2),
\]
by integration in $v$ and the single-divisor transform, and this is not identically zero.

There is no $a>0$ with $|J(Y)|=O(\exp[-aY/\log(3+Y)])$ at positive infinity. Such a bound would give $U$ the same decay, with a smaller $a$, at both ends. The derivatives of its Fourier transform would then be bounded by $C^{k+1}k![\log(k+3)]^k$. For the moment estimate, split the tail into dyads above $V=A(k+1)\log(k+3)$; on its $j$th dyad the damping exponent is at least $cA(k+1)2^{j/2}$ for large fixed $A$ (with the constant adjusted for fixed $A$). It dominates the polynomial factor $2^{(j+1)k}$ and leaves a bound $C^{k+1}V^{k+1}$ for the $k$th moment. Stirling gives the stated derivative estimate. The Denjoy–Carleman quasi-analyticity criterion applies since the sum of the reciprocal $k$th roots of these bounds dominates $\sum_{k\ge2}1/(k\log k)$. Vanishing on $(-1,1)$ would make the entire real Fourier transform identically zero, a contradiction. This use of quasi-analyticity can be replaced by elementary holomorphic continuation if only the weaker impossibility of exponential decay in $Y$ is desired.

It follows that on some $Y\to\infty$, $|J(Y)|\ge\exp[-o(Y/\log Y)]$. Put $Z=\exp(Y/(4C\log Y))$, so $C\log(2Z)\log\log(10Z)<Y/2$ eventually. Differentiation after substituting $s=Ye^v$ in the defining integral shows $|J'(Y)|\ll_H Y^{-1/2}$ for $Y\ge1$: only $w'(\log(s/Y))/Y$ is differentiated, and the single-divisor input is $O(\sqrt s)$. Thus $|J|$ stays at least $|J(Y)|/2$ on a one-sided interval of length $\delta\gg\min(1,|J(Y)|)$ at $Y$. The integers $d$ with $Z/d$ in this interval form an interval of length $\gg Z\delta/Y^2$ near $Z/Y$. A positive proportion are squarefree because the elementary squarefree census has error $O(\sqrt{Z/Y})$, and $\delta=Z^{-o(1)}$ after replacing it by a smaller suitable length. These terms alone contribute $\gg Z^{-1/2}Y^{-1/2}\delta |J(Y)|=Z^{-1/2-o(1)}$ in absolute value. They all lie below the putative divisor cutoff. Any improvement past this endpoint must therefore retain cancellation of actual Möbius signs in the discarded terms.

### A signed multiplicative comparison

Fix $1/2<\beta<1$, $\gamma>0$, and an arbitrarily large $P$. A real multiplicative comparison $a$ vanishes on all squareful integers, agrees with $\mu$ on the primes through $P$, and satisfies $|a(n)|\le|\mu(n)|$ everywhere. Take $a(p)=2p^{\beta-1}\cos(\gamma\log p)$ beyond $P$, enlarging $P$ if necessary. For the compact smoothing above and all large $Z$,
\[
 \sum_n a(n)n^{-3/2}J(Z/n)
      =2\Re(cZ^{\beta-3/2+i\gamma})+O(Z^{\beta-3/2-\delta})
\]
for some $c\ne0$ and fixed small $\delta>0$. Indeed the Dirichlet series of $a$ factors as the finite product $\prod_{p\le P}(1-p^{-s})$, the two incomplete zeta factors at $s+1-\beta\pm i\gamma$, and an absolutely convergent nonzero Euler product on $\Re s\ge\beta-\delta$. For the last product the local factor is $(1+u+v)(1-u)(1-v)$ with $u,v=p^{-s-1+\beta\pm i\gamma}$, hence $1+O(p^{-2+2\delta})$; take $P$ large and $\delta<\min(1/2,\beta)$. The poles at $\beta\pm i\gamma$ are simple with nonzero residues by the zero-free line one. Mellin inversion for the displayed sum uses the Dirichlet series at $s+3/2$ times the transform of $J(e^u)$ given above. At the shifted poles this transform is nonzero: $F(-s)\ne0$ and $\Re(s-1/2)=\beta-2$ is negative with nonzero ordinate, where zeta has no zeros. Moving the line by $\delta$ gives the error by rapid vertical decay of $F$ and polynomial zeta growth; the Mellin transform of $J$ is entire by its two tails.

At $Z=e^{t+x+y}$ the leading two terms give a rank-two Hankel operator. After division by $e^{(\beta-3/2)t}$ its second singular value is bounded below uniformly in $t$: the two exponential functions of $x$ are linearly independent, both coefficients have fixed nonzero modulus, and their phases vary over a compact circle. The error is smaller in Hilbert–Schmidt norm by $O(e^{-\delta t})$ in the same normalization. Thus even one unrestricted rank-one correction cannot turn this comparison into an estimate of size $e^{-t+o(t)}$. This counterexample preserves multiplicativity, the squarefree support as a majorant, and all prescribed initial prime data. The signed estimate for the actual $\mu$ remains open.
