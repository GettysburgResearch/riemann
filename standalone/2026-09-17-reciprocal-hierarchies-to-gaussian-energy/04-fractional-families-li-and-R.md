# 04. Fractional multiplicative families, Li, R, and power-free densities

**Status:** classical generalized-divisor/Riesz ingredients with explicit derived connections. Local singularity calculations below are not unrestricted zero-sum formulas. Independent review is requested for the proposed compositions. References: [SOURCES](SOURCES.md).

## 1. Multiplicative convolution depth

Define d_alpha multiplicatively by d_alpha(1)=1 and
\[
d_\alpha(p^k)=\frac{\alpha(\alpha+1)\cdots(\alpha+k-1)}{k!}.
\]
For Re s>1,
\[
\sum_n d_\alpha(n)n^{-s}=\zeta(s)^\alpha,\qquad
d_\alpha*d_\beta=d_{\alpha+\beta}.
\]
The Euler logarithm fixes the branch. For positive integer alpha, these count ordered factorizations; positive fractional alpha gives nonnegative weights. For example d_(1/2)(p)=1/2, d_(1/2)(p^2)=3/8 and d_(1/2)(pq)=1/4 for distinct primes.

The Selberg–Delange theorem [SD] gives, for fixed alpha>0,
\[
\sum_{n\le x}d_\alpha(n)\sim
\frac{x(\log x)^{\alpha-1}}{\Gamma(\alpha)},\quad
\sum_{n\le x}d_\alpha(n)/n\sim
\frac{(\log x)^\alpha}{\Gamma(1+\alpha)}.
\]
This is an exact continuous algebraic family of fractional harmonic scales, not an assertion that every natural fractional-density set has transform zeta^alpha.

At alpha=0, d_0 is the identity mass at 1. Differentiating coefficientwise at a fixed finite cutoff gives
\[
\left.\partial_\alpha d_\alpha(n)\right|_0
=\begin{cases}1/k&n=p^k,\\0&\text{otherwise.}\end{cases}
\]
Thus the prime-power counting function
\[
J(x)=\sum_{p^k\le x}1/k
=\left.\partial_\alpha\sum_{n\le x}d_\alpha(n)\right|_0
\]
is the infinitesimal generator of multiplicative counting. Also d_1(n)=1 and d_(-1)(n)=mu(n). The integers, prime-power generator and multiplicative inverse lie in one family.

Primitive extraction is exact:
\[
J(x)=\sum_{m\ge1}\pi(x^{1/m})/m,\quad
\pi(x)=\sum_{m\ge1}\mu(m)J(x^{1/m})/m.
\]
Both are finite for fixed x, because J and pi vanish below 2.

## 2. Why the Li correction coefficients are factorials

Put L=log x, q(w)=w zeta(1+w), and
\[
a_j(\alpha)=[w^j]\frac{q(w)^\alpha}{1+w}.
\]
The local Selberg–Delange expansion is
\[
\sum_{n\le x}d_\alpha(n)
\sim x\sum_{j\ge0}\frac{a_j(\alpha)L^{\alpha-j-1}}{\Gamma(\alpha-j)}.
\]
This means a finite asymptotic expansion to each fixed order, with a suitable locally uniform error before differentiating in alpha. It is not a convergent infinite series or a zero-free continuation assumption.

At alpha=0,
\[
a_j(0)=(-1)^j,\qquad
\Gamma(\alpha-j)^{-1}=(-1)^jj!\alpha+O(\alpha^2).
\]
Terms from differentiating a_j and L^alpha are multiplied by 1/Gamma(-j)=0. Therefore
\[
\left.\partial_\alpha
\frac{a_j(\alpha)L^{\alpha-j-1}}{\Gamma(\alpha-j)}\right|_0
=\frac{j!}{L^{j+1}}.
\]
The tangent gives
\[
J(x)\sim\frac{x}{\log x}+\frac{x}{\log^2x}
+\frac{2!x}{\log^3x}+\cdots,
\]
the Li expansion. The factorial coefficients arise from zeros of reciprocal Gamma; the finer coefficients of q disappear at first order. This gives the user's proposed family interpretation of the smooth corrections.

## 3. The same tangent exposes zero contributions

At a zero rho of multiplicity m,
\[
\zeta(s)=c_\rho(s-\rho)^m(1+O(s-\rho)),\quad c_\rho\ne0.
\]
For generic nonintegral alpha, zeta^alpha has a branch point there. A local Hankel calculation, when included in a justified contour deformation, has leading contribution
\[
\frac{c_\rho^\alpha}{\rho\Gamma(-m\alpha)}
\frac{x^\rho}{(\log x)^{m\alpha+1}}.
\]
Since 1/Gamma(-m alpha)=-m alpha+O(alpha^2), its derivative at zero is
\(-m x^\rho/(\rho\log x)\), the leading term of -m Li(x^rho). The pole at 1 contributes +Li(x). The classical explicit formula [R1859] supplies the global conventions and remaining terms; this local calculation is not a license to sum residues without bounds.

For rho=beta+i gamma, x^rho has envelope x^beta and frequency gamma in log x. For each fixed beta<1, x^beta/log x is smaller than x/log^K x for every fixed K. Thus every coefficient of the smooth inverse-log expansion can be known without locating the zeros. No finite collection of log_2 x, log_3 x, etc. corrections cancels the known two-sided prime-counting oscillations. The handoff cited the classical scale \(\Omega_\pm(\sqrt x\log_3x/\log x)\) for pi-Li; this is background, not a new proof or a quantitative input below.

## 4. A continuous integer-counting comparison

The discrete measure nu=sum delta_n has count floor x and Mellin transform zeta(s). Compare it with
\[
\nu_0=\delta_1+1_{x>1}dx,
\quad \nu_0([1,x])=x,
\quad Z_0(s)=s/(s-1).
\]
Its multiplicative generator satisfies
\[
\log Z_0(s)=\int_1^\infty
x^{-s}\frac{1-x^{-1}}{\log x}\,dx.
\]
Consequently define
\[
L_0(x)=\int_1^x\frac{1-t^{-1}}{\log t}\,dt
=\operatorname{Li}(x)-\log\log x-\gamma,\quad x>1,
\]
using Li(x)=Ei(log x). The combination is regular at 1. In logarithmic coordinates,
\[
\mathcal L(u):=L_0(e^u)=\sum_{k\ge1}\frac{u^k}{k\,k!}
\]
is entire.

Applying the same primitive-extraction operation gives the absolutely convergent identity
\[
R(x)=1+\sum_{m\ge1}\frac{\mu(m)}m L_0(x^{1/m})
=1+\sum_{k\ge1}\frac{(\log x)^k}{k\,k!\zeta(k+1)}.
\]
Absolute convergence follows from L_0(x^(1/m))=O_x(1/m). This avoids the delicate limiting interpretation of a bare Mobius–Li sum.

With E(x)=J(x)-L_0(x),
\[
\pi(x)-R(x)+1=\sum_{m\ge1}\mu(m)E(x^{1/m})/m.
\]
The tail is absolutely convergent because J vanishes below 2. Thus R is what prime extraction produces from continuous integer counting, while pi-R is the same extraction applied to the discrete-versus-continuous generator discrepancy.

## 5. Power-free densities literally supply R's coefficients

Let \(\delta_k=1/\zeta(k)\) for k>=2, the density of integers divisible by no p^k. Put delta_1=0. Then
\[
R(e^u)=1+\sum_{k\ge1}\delta_{k+1}\frac{u^k}{k\,k!}.
\]
If N is Poisson with mean log x, differentiating gives
\[
R'(x)=\frac{\mathbb E\delta_{N+1}}{\log x},\quad x>1.
\]
This is an exact interpretation of a smooth approximation, not a probability that a particular integer is prime.

The k-free counting Dirichlet series is zeta(s)/zeta(ks). Its candidate zero-induced poles are rho/k, with numerator cancellations checked. This explains rescaled spectral contributions but is not an optimal unsmoothed error theorem.

## 6. Differentiate R on the negative logarithmic axis

Set Phi(t)=R(e^(-t)) and
\[
F(t)=-\frac{d}{dt}\left(t\frac{d}{dt}\Phi(t)\right).
\]
The entire series gives
\[
\boxed{F(t)=\sum_{k\ge0}\frac{(-t)^k}{k!\zeta(k+2)}
=\sum_{n\ge1}\frac{\mu(n)}{n^2}e^{-t/n}.}
\]
The second interchange is absolute on compact t sets. These are analytic values of R below 1, not a claim about prime counting there.

For 0<Re s<1, absolute integration gives
\[
\int_0^\infty F(t)t^{s-1}\,dt=\frac{\Gamma(s)}{\zeta(2-s)}.
\]
Therefore
\[
\boxed{\mathrm{RH}\iff F(t)=O_\epsilon(t^{-3/2+\epsilon})
\text{ for every }\epsilon>0.}
\]
Under RH, M(x)=O_epsilon(x^(1/2+epsilon)); partial summation against x^(-2)e^(-t/x) proves the decay. Conversely, the decay continues the Mellin integral holomorphically to 0<Re s<3/2. A zero rho with Re rho>1/2 would create a pole at 2-rho, not cancelled by Gamma. Reflection then gives RH. Multiplicity only changes pole order.

For a simple zero, a justified Mellin shift yields a term proportional to Gamma(2-rho)t^(rho-2)/zeta'(rho); multiple zeros produce log factors. This is a residue interpretation, not a globally unqualified zero sum.

## 7. Finite differences of the same density sequence

Define
\[
C_N=\sum_{j=0}^N(-1)^j\binom Nj\delta_{j+2}
=\sum_{n\ge1}\frac{\mu(n)}{n^2}(1-1/n)^N.
\]
The latter uses the usual 0^0=1 convention at N=0. Exact Poissonization gives
\[
F(t)=e^{-t}\sum_{N\ge0}C_Nt^N/N!.
\]
These are the a=1,b=2 case of generalized Báez-Duarte coefficients [C06], not a claimed new class. Partial summation under RH and the converse through Poissonization show
\[
\mathrm{RH}\iff C_N=O_\epsilon(N^{-3/2+\epsilon})
\text{ for every }\epsilon>0.
\]
For \(P_N(s)=\prod_{j=1}^N(1-(s-1)/j)\), with P_0=1,
\[
1/\zeta(s)=\sum_{N\ge0}C_NP_N(s),\quad\Re s>1.
\]
It follows by expanding n^(2-s) in powers of 1-1/n and interchanging absolutely. Away from terminating cases, P_N(s)~N^(1-s)/Gamma(2-s); the target decay would continue this Newton series normally to Re s>1/2.

The absolute mass is calculable:
\[
S_N=\sum_n\frac{\mu(n)^2}{n^2}(1-1/n)^N
=\frac{1}{\zeta(2)(N+1)}+O(N^{-3/2}).
\]
Use sum_(n<=x)mu(n)^2=x/zeta(2)+O(sqrt x) and partial summation; the main integral is exactly 1/(N+1). Thus the missing sign cancellation is an additional factor approximately N^(1/2), not a consequence of squarefree density. Counting mu=+1 and mu=-1 separately introduces M(x) through their difference.

## 8. Normalize before attempting fractional inverse estimates

Set
\[
H(s)=\zeta(s)/Z_0(s)=((s-1)/s)\zeta(s).
\]
Initially Re s>1, let K_alpha(x) be the cumulative signed multiplicative-convolution source with Mellin–Stieltjes transform H(s)^alpha. Exact special cases are
\[
K_1(x)=\lfloor x\rfloor-\int_1^x\frac{\lfloor u\rfloor}{u}du,
\quad
\left.\partial_\alpha K_\alpha(x)\right|_0=J(x)-L_0(x),
\quad
K_{-1}(x)=x\sum_{n\le x}\mu(n)/n.
\]
Writing N=floor x gives K_1=N-N log x+log(N!), hence
\(K_1(x)=\tfrac12\log(2\pi x)-\{x\}+O(x^{-1})\).
A simple integer discrepancy does not control its fractional roots or inverse: zeros become branch points or poles.

Naively subtracting zeta(s)^alpha-Z_0(s)^alpha leaves
\[
\alpha(\gamma-1)(s-1)^{1-\alpha}+\cdots,
\]
producing a deterministic term proportional to x(log x)^(alpha-2). For fixed 0<alpha<1 this is much larger than square-root error. It vanishes at first order in the alpha=0 tangent, but not for a fixed fractional member. A properly centered convolution source, not a leading-term subtraction, is needed.

Finally, d_(-alpha), 0<alpha<1, has summatory main term
\[
\sum_{n\le x}d_{-\alpha}(n)\sim
\frac{x}{\Gamma(-\alpha)(\log x)^{\alpha+1}}.
\]
Estimating d_(-1/2) factors separately destroys cancellation even though d_(-1/2)*d_(-1/2)=mu. Their branch contributions at 1 cancel only when the factors are kept together. This is an explicit obstruction to factorwise absolute-norm completion arguments.
