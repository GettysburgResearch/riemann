# Corrected Suzuki norms and the limits of finite certificates

The source is Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*, Cambridge FirstView 2025, with his [author erratum](https://drive.google.com/file/d/1Gi7cUoqA_izzdsH5lzEL48bl20Lf9c8_/view?usp=sharing). Write $\gamma$ for a zero of $A(z)=\xi(1/2-iz)$, $m_\gamma$ for its multiplicity, $g=-\Psi$ for the even function in (4.3), and $G_g(t,u)=g(t-u)-g(t)-g(u)+g(0)$. The analysis concerns the corrected identities and finite checks of them. [Cambridge source](https://doi.org/10.4153/S0008414X25101739) · [Suzuki’s source for $\Psi$](https://arxiv.org/pdf/2206.03682v4)

## 1. The two sides and the precise RH dependency

Set $E(z)=A(z)+iA'(z)=\xi(1/2-iz)+\xi'(1/2-iz)$, use $F^\sharp(z)=\overline{F(\bar z)}$, and put $\Theta=E^\sharp/E$. With the erratum’s sign, the Cambridge formula (1.5) is
$$
 S_t(z)=-\frac{i}{2}(1+\Theta^\sharp(z))\,\mathfrak P_t(z).
$$
For $t\ge0$ the explicit expression (1.6) for $\mathfrak P_t$ is arithmetic and uses no zero list. It agrees with the meromorphic series $P_t(z)=\sum_\gamma m_\gamma(e^{-i\gamma t}-1)/[\gamma(z-\gamma)]$. For negative $t$, use $\mathfrak P_t(z)=\overline{\mathfrak P_{-t}(\bar z)}$ and keep this same signed series formula for $P_t$. This is erratum items (1)–(3). Conjugation symmetry of the zeros gives the signed rule. The equality $P_{-t}(z)=P_t(-z)$ also follows by the symmetry $\gamma\mapsto-\gamma$. Item (4) corrects the printed coefficient bound on p. 14 to $4\pi$, in agreement with $|e^{-i\gamma t}-1|\le2$ for real $\gamma$.

The **unconditional side** has $S_t\in L^2(\mathbb R,dx)$ for every real $t$ and, on compact parameter intervals, an effectively bounded norm, as shown below. Thus the family $B(t,u)=\langle S_t,S_u\rangle/\pi$ is positive semidefinite on finite sets unconditionally. Separately, $\Psi$ is unconditionally real, even and continuous, with $\Psi(0)=0$. The product expression
$$
 \Psi(t)=\sum_\gamma m_\gamma\frac{1-\cos(\gamma t)}{\gamma^2}
$$
converges normally on compact real parameter intervals even if some $\gamma$ are not real. The arithmetic formula for $\Psi(t)$ involves only primes up to $e^{|t|}$ and explicitly computable archimedean terms.

The **conditional step** is the identification of these kernels. Under RH, $E$ supplies the arithmetic Hermite–Biehler input, $\Theta$ defines the intended model space, and the real-frequency normalized kernels in Proposition 4.1 give Parseval. This proves $B(t,u)=G_g(t,u)$, and in particular
$$
 \frac{\|S_t\|_2^2}{2\pi}=\Psi(t).
 \tag{A}
$$
The unconditional positivity of $B$ cannot be transferred to $G_g$ by invoking the conditional basis argument. For the test-function variant, $D\psi=i\psi'$ and the corrected source gives $\|\widehat{P D\psi}\|_2^2=\pi\langle\psi,\psi\rangle_W$ when the global equality is established. To see the converse, this equality for all test functions makes the Weil form nonnegative and one can invoke the classical Weil criterion directly. This avoids reliance on the printed interpolation choices on p. 15, whose two displayed functions appear to target the same ordinate and are unnecessary for this inference.

## 2. What bounded computation can enclose

For every fixed $T$, on the real $x$ axis the bound
$$
 |S_t(x)|\le B_T\frac{1+\log(2+|x|)}{1+|x|},\qquad |t|\le T
 \tag{B}
$$
has an effectively obtainable finite constant under ordinary certified evaluation of the classical special functions. No lower bound on $\zeta$ on the critical line is required.

Indeed, $A(x)$ is real and $\xi'(1/2-ix)=iA'(x)$ is imaginary. Thus $|A/E^\sharp|\le1$ and $|\xi'/E^\sharp|\le1$ on the real axis, first off isolated real zero points and then by removable continuation of the quotient. A real zero of $A$ of order $m\ge1$ gives order $m-1$ in $E^\sharp$, so these ratios remain bounded even at multiple roots. Write $1+\Theta^\sharp=2A/E^\sharp$. In the logarithmic-derivative term of (1.6), use
$$
 \frac{\zeta'}{\zeta}(s)=\frac{\xi'}{\xi}(s)-\frac1s-\frac1{s-1}
              +\frac{\log\pi}{2}-\frac12\frac{\Gamma'}{\Gamma}(s/2).
$$
The singular $\xi'/\xi$ then becomes $\xi'/E^\sharp$ after multiplication by $A/E^\sharp$. The quotient $(e^{-ixt}-1)/x$ is bounded by $\min(|t|,2/|x|)$. The two polar terms have denominators $1\pm 2ix$ and are bounded by elementary functions of $T$. The finite prime sum is bounded explicitly with $\sum_{n\le e^T}\Lambda(n)/\sqrt n$, using the same elementary quotient.

The two remaining differences are digamma and Lerch differences. The digamma series bounds their difference at arguments $1/4$ and $1/4-ix/2$. The Lerch difference is bounded in modulus by
$$
 \frac{|x|}{2}\sum_{n\ge0}
 \frac{1}{(n+1/4)\sqrt{(n+1/4)^2+x^2/4}},
$$
uniformly in $q=e^{-2t}\in[0,1]$ for $t\ge0$. Splitting at $n\asymp1+|x|$ gives $O(1+\log(2+|x|))$ for $|x|\ge1$ and $O(|x|)$ for $|x|\le1$, with explicit elementary constants. The same difference bound follows for the digamma series. This proves (B) including the apparent quotient at zero. Negative $t$ follows by the reflected-conjugate rule and the even absolute values of the real-axis phase factor. At $t=0$ the formula has its stated zero value.

Thus finite inner products at prescribed computable times are computable to arbitrary absolute tolerance by truncating the $x$ integral with certified squared tail $O(B_T^2(1+\log R)^2/R)$, $R\ge2$. On a compact interval use interval quadrature of the regular expression. The elementary bound (B) permits omitting tiny neighborhoods of real zeros of the denominators: finite many such points occur on any fixed compact interval, and interval exclusion on a refining subdivision has arbitrarily small total exceptional length because every point away from them has a neighborhood where the denominator is certified nonzero. This procedure does not need an exact multiplicity certificate. The finite sum in $\Psi$ can use the continuous real hinge $(|t|-\log n)_+$, which also avoids deciding equality at a breakpoint.

The alternate zero-side truncation of $\Psi$ at $|\Re\gamma|\le R$ has absolute error $O(e^{T/2}\log R/R)$ for $|t|\le T$, by the unconditional unit-window zero count and $|\Im\gamma|<1/2$. Likewise on $|t|,|u|\le A$, the truncation in $G_g$ has error $O(e^A\log R/R)$, using the product $(e^{i\gamma t}-1)(e^{-i\gamma u}-1)/\gamma^2$. This truncation requires all the relevant zeros, not just a list of known on-line ones. The real-axis norm truncation and the finite-height spectral truncation control different variables.

For a fixed finite matrix, a certified strictly positive least eigenvalue exceeding an entrywise perturbation bound times the matrix size proves positivity of that compression. A certified negative direction disproves the global positivity criterion. Equality such as (A) is stronger than membership of zero in finite-error intervals. There is also a compact-operator obstacle on an entire support interval: even if a compact self-adjoint operator is positive on an infinite-dimensional space, it has no positive uniform least Rayleigh quotient. Given an error tolerance, choose a unit direction in the orthogonal complement of the finite compression with Rayleigh quotient less than half that tolerance. Subtract a rank-one operator of that size in this direction. This preserves the compressed matrix entries and violates positivity. An operator-norm tail bound combined with a finite positive compression therefore does not by itself certify the remaining infinite-dimensional positivity.

## 3. A precise strip implication and its quantitative requirement

Put
$$
 D(t)=\frac{\|S_t\|_2^2}{2\pi}-\Psi(t).
$$
For every $\omega\ge0$ the following condition is equivalent to $\xi(s)\ne0$ on $\Re s>1/2+\omega$:
$$
 \Psi(t)\ge -C e^{\omega t}\quad\text{for all sufficiently large }t,
 \tag{C}
$$
where $C<\infty$ can depend on $\omega$. In particular a one-sided norm-defect estimate $D(t)\le C e^{\omega t}$ eventually suffices. The latter is only used as a sufficient condition, by nonnegativity of the squared norm. With $\omega=0$ even a bounded eventual upper defect would imply RH by the functional equation. This is a stronger tolerance formulation than requiring exact norm equality.

The easy direction of (C) follows from the zero expansion and $\sum_\gamma m_\gamma/|\gamma|^2<\infty$. A zero-free half-plane and reflection put every $|\Im\gamma|\le\omega$, and hence $|\Psi(t)|\le 2e^{\omega t}\sum_\gamma m_\gamma/|\gamma|^2$. For the other direction, enlarge $C$ to absorb the finite initial interval and set $f(t)=\Psi(t)+Ce^{\omega t}\ge0$ on $[0,\infty)$. The one-sided Laplace transform, initially for real part large, is
$$
 \int_0^\infty e^{-ut}f(t)\,dt
   =\frac{1}{u^2}\frac{\xi'}{\xi}(1/2+u)+\frac{C}{u-\omega}.
 \tag{D}
$$
This is Suzuki’s formula (1.2) with $z=iu$. Its right-hand side is meromorphic and has no pole for real $u>\omega$. Indeed $\xi$ has no real zero, by the usual real-axis continuation and signs of $\zeta$ on $(0,1)$ and its Euler product on $(1,\infty)$, together with its functional equation.

A nonnegative function’s finite Laplace abscissa cannot be a point of analytic continuation on the real axis. In this setting one sees it directly. If the abscissa $u_c>\omega$, choose $v>u_c$ close enough that the continued transform is analytic on a disk about $v$ of radius larger than $v-u_c$. The coefficients of its Taylor series in $v-u$ are $\int_0^\infty f(t)t^ne^{-vt}dt/n!\ge0$. Summing them at a positive $a>v-u_c$ inside that disk and using monotone convergence gives a finite integral at $v-a<u_c$, a contradiction. Thus the transform is holomorphic on $\Re u>\omega$. Its equality to the meromorphic expression (D) continues there; any zero of $\xi$ in the asserted half-plane would cause a nonremovable logarithmic-derivative pole. This proves (C). Suzuki’s shifted variant $\Psi_\omega$ in §11 of *Aspects* is related but tests eventual nonnegativity of a transformed function. Here the error tolerance is directly on the unshifted $\Psi$ or on the norm defect.

For clarity, bounded-time numerical data can be extended to a bounded time interval with a modulus. On $0<\eta\le t\le T$, the regular expression in §2 has a termwise $t$-derivative bound $C_{\eta,T}(1+\log(2+|x|))$ off finitely many prime breakpoints. The prime series on this bounded interval is a finite sum of continuous hinged exponential differences; at a breakpoint the new term vanishes. The Lerch coefficients and their $t$ derivatives have a summable majorant since $e^{-2t}\le e^{-2\eta}<1$. Together with (B) and splitting at $|x|=1/h$, this gives
$$
 \|S_{t+h}-S_t\|_2\ll_{\eta,T}\sqrt{|h|}\log(2/|h|),\quad
 0<|h|\le1/2,
$$
when both times lie in the compact interval. The derivative bound controls the low-$x$ integral and (B) controls its complement. $\Psi$ is locally Lipschitz on that interval by the finite hinge sum and smooth archimedean terms. Consequently the same modulus, up to a new constant, controls $D$ there. This enables a finite certified upper bound on one compact interval. To infer (C) from a grid one needs an unbounded cover with a certified bound. For instance, if $T_j\to\infty$ and $E_j\ge\sup_{t\in[T_j,T_{j+1}]}(D(t)-D(T_j))$, an upper enclosure satisfying $D(T_j)+E_j\le Ce^{\omega T_j}$ for all $j$ suffices. A finite subset of these checks leaves an uncontrolled tail unless coupled with an analytic estimate that covers it.

## 4. Both sides can be approximated by a model with off-axis zeros

Here is a finite-window obstruction for a symmetric entire-function model with the same zero-series and phase algebra. It does not replace the Euler product of $\zeta$. Choose a real even polynomial $A_0$ with distinct nonzero real roots, and define its phase and $P_t,S_t,\Psi$ by the corrected formulas above with this finite zero set. Fix $a>0$ and add a unit-multiplicity quartet by forming
$$
 A_B(z)=A_0(z)Q_B(z),\qquad
 Q_B(z)=((z-B)^2+a^2)((z+B)^2+a^2).
$$
For $B$ large the four new zeros are distinct, at $\pm B\pm ia$. Thus their putative critical-line translates include points of real part $1/2+a$. The two functions $\Psi$ and the two time kernels differ uniformly on every bounded time window by $O_{T,a}(B^{-2})$, by the finite old-plus-new expansion. The phase-side norms and Gram data converge as well.

To see the latter, put $r_0=A_0'/A_0$ on the real line. The phase multiplier apart from a fixed unit factor is $A_0/E^\sharp_0=(1-ir_0)^{-1}$. For $A_B$ replace $r_0$ by $r_0+q_B$, where
$$
 q_B(x)=\frac{2(x-B)}{(x-B)^2+a^2}
       +\frac{2(x+B)}{(x+B)^2+a^2}.
$$
It satisfies $|q_B|\le2/a$ and tends to zero at each fixed real $x$. The variation of the multiplier is bounded by $|q_B|\,|(1-ir_0)^{-1}|$, using that the new denominator has modulus at least one. The old $S_t$ family admits a common $L^2$ majorant on each $|t|\le T$, since the old rational sum is finite, its real poles are canceled, and its remaining tail is $O_T(1/|x|)$. Dominated convergence therefore controls the contribution of this multiplier change uniformly on that time interval. The added $\gamma$ term has coefficient $O_{T,a}(1/B)$ and real-axis resolvent $(x-\gamma)^{-1}$ of $L^2$ norm $\sqrt{\pi/a}$, so the four new terms together give $O_{T,a}(1/B)$ in norm. Consequently all bounded-window phase Gram and norm-defect data converge to those of the real-rooted model.

For that reference model the exact norm identities hold on the finite expansion. Indeed $r_0(z)=\sum_{\gamma}1/(z-\gamma)$ has negative imaginary part for $\Im z>0$. Hence $\Theta_0=(1-ir_0)/(1+ir_0)$ is inner there. Its boundary reproducing kernels at the distinct points where $\Theta_0=-1$ are mutually orthogonal. The local identity $(1+\Theta_0(z))/2\sim-i(z-\gamma)$ gives squared norm $\pi$ for the factor $i(1+\Theta_0(x))/(2(x-\gamma))$. Conjugation on the real line gives the same result for the corrected factor using $\Theta_0^\sharp$. Parseval on this finite orthogonal family gives both sides of (A), and likewise the mixed Gram identity, without a completeness assumption at a possible atom at infinity.

Thus for any strict finite measurement tolerance and $0\le\omega<a$ this model can agree with exact real-spectrum data to within that tolerance on the whole compact time window and still contain zeros beyond the proposed strip. It also defeats finitely many strict positive kernel tests: a positive least eigenvalue has an open perturbation margin. The result concerns finite approximate data in the indicated model class. It does not rule out a finite exact certificate exploiting additional arithmetic identities or an independent global tail theorem for the actual zeta function.

For an exact obstruction in the larger Laplace-data class alone, add to a given even $\Psi$ an even delayed term $1_{\{|t|\ge T_0\}}[\cos(B(|t|-T_0))\cosh(a(|t|-T_0))-1]$. This changes none of the data up to $T_0$, yet its one-sided Laplace transform has poles at $u=\pm a\pm iB$ provided $a,B>0$. This follows by translating the elementary transform of the cosine–hyperbolic-cosine product. It illustrates why continuation from finite sampled values requires control beyond a generic meromorphic transform formula. This delayed perturbation is only a Laplace-data control and is not asserted to come from an arithmetic entire function.
