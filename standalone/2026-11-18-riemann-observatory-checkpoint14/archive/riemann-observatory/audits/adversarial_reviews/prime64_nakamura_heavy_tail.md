# Tail, atoms, and scaling of the Nakamura–Suzuki law

Let \(g_\zeta\) be the function of Nakamura–Suzuki. Under RH their Theorem 1.2 gives the characteristic function \(\exp g_\zeta\) of a symmetric compound Poisson law \(\mu\) on \(\mathbb R\), with no Gaussian part or compound-Poisson drift. Their equation (1.6) is
\[
 \nu=\sum_\gamma \frac{m_\gamma}{\gamma^2}\delta_{-\gamma},
 \qquad g_\zeta(t)=\int_{\mathbb R}(e^{itx}-1)\,\nu(dx).
\]
Here \(\gamma\) runs through the distinct signed zeros of \(\xi(1/2-iz)\), and \(m_\gamma\) is the multiplicity. Both signs are included. The series in their equation (1.7) also makes sense unconditionally with complex zeros and is used below for the unconditional cusp. The probability claims in this note assume RH. [Nakamura–Suzuki, Theorems 1.1–1.2, Lemma 2.1, and equations (1.6)–(1.7)](https://arxiv.org/pdf/2306.08317v1)

## Strict Lévy and probability tails

Write \(N(v)\) for the multiplicity-counted positive nontrivial zeros with ordinates at most \(v\). Hasanalizade–Shen–Wong define the inclusive positive count on p. 1, use the argument principle for its two-sign multiple in §2, and prove in Corollary 1.2, equation (1.5), that
\[
 N(v)=\frac{v}{2\pi}\log\frac{v}{2\pi e}+R(v),\qquad
 |R(v)|\le 0.1038\log v+0.2573\log\log v+9.3675\quad(v\ge e).
\]
In particular \(|R(v)|\le a\log v+b\) with \(a=0.3611\), \(b=9.3675\). The formula involves positive ordinates of all nontrivial zeros unconditionally. Under RH it counts all the positive atoms of the Lévy measure with multiplicity. [Primary Riemann–von Mangoldt estimate](https://arxiv.org/pdf/2107.06506v1)

Strict-tail partial summation gives
\[
 \nu(|x|>Y)=2\int_{(Y,\infty)} v^{-2}\,dN(v)
   =\frac{\log(Y/(2\pi))+1}{\pi Y}+\mathcal E(Y),\qquad
 |\mathcal E(Y)|\le\frac{4a\log Y+4b+a}{Y^2}\quad(Y\ge e).
\]
The main term integrates the density \((2\pi)^{-1}\log(v/(2\pi))\). The error is \(-2R(Y)/Y^2+4\int_Y^\infty R(v)v^{-3}\,dv\). In particular the lower endpoint subtracts the inclusive count, even when \(Y\) is an ordinate.

Let \(S=\nu(\mathbb R)\in(0,\infty)\) and draw \(J_i\) independently with law \(\nu/S\). Then \(X=\sum_{i=1}^{K}J_i\), with \(K\) an independent Poisson random variable of rate \(S\), has law \(\mu\). In fact
\[
 \boxed{\mathbb P(|X|>Y)
  =\nu(|x|>Y)+O\!\left(\frac{\log^3Y}{Y^2}\right)
  =\frac{\log(Y/(2\pi))+1}{\pi Y}
       +O\!\left(\frac{\log^3Y}{Y^2}\right).}                         \tag{1}
\]
This transfer is proved directly, including possible cancellations and the unbounded Poisson number of jumps.

Put \(F(x)=\mathbb P(|J_1|>x)\). The Lévy tail shows \(F(x)\ll \log x/x\) for \(x\ge e\). It also gives
\[
 \sup_{u\in\{x-v,x+v\}} |F(u)-F(x)|
 \ll (v+1)\frac{\log x}{x^2}
 \qquad (0\le v\le x/2,\ x\ge2e).
\]
For this inequality use the mean-value theorem on the smooth main term and bound the two remainder values separately, which permits atoms at all endpoints. Two other consequences are \(F(x/m)\ll m\log x/x\) uniformly over \(m\ge1\) and
\(\mathbb E[|J_1|\mathbf 1_{\{|J_1|\le x\}}]\ll\log^2x\). For \(x/m\ge e\) the first bound uses \(\log(x/m)\le\log x\). For \(x/m<e\) use \(F\le1\) and \(m>x/e\). The second bound follows by integrating \(F\) on \([0,x]\).

Condition on \(K=n\ge2\), set \(u=x/[2(n-1)]\), and put
\[
 G_i=\{|J_j|\le u\ \text{for every }j\ne i\},\qquad
 R_i=\sum_{j\ne i}J_j.
\]
Let \(D\) be the event that at least two jumps exceed \(u\) in absolute value. By independence and the uniform bound,
\(\mathbb P(D)\le {n\choose2} F(u)^2\ll n^4\log^2 x/x^2\).
Outside \(D\), a sum of absolute value greater than \(x\) has exactly one jump exceeding \(u\), since \(nu\le x\). Its index satisfies \(G_i\) and \(|J_i|>x-|R_i|\). Conversely the events \(G_i\) and \(|J_i|>x+|R_i|\) are disjoint across \(i\) and imply absolute sum greater than \(x\). Independence of \(J_i\) from the other jumps therefore sandwiches the conditional probability between
\[
 \sum_i \mathbb E[\mathbf1_{G_i}F(x+|R_i|)]
 \quad\hbox{and}\quad
 \mathbb P(D)+\sum_i\mathbb E[\mathbf1_{G_i}F(x-|R_i|)].
\]
On \(G_i\), \(|R_i|\le x/2\) and
\(\mathbb E[\mathbf1_{G_i}|R_i|]\ll n\log^2x\) by the truncated first moment. Also \(\mathbb P(G_i^c)\le(n-1)F(u)\ll n^2\log x/x\). Comparing both displayed sums to \(nF(x)\) gives a total error \(O((1+n)^4\log^3x/x^2)\). All implied constants can be independent of \(n\). The \(n=0,1\) cases have exact main term. Average against the Poisson probabilities, which have finite fourth moment, and use \(\mathbb E K=S\). This proves (1).

Each one-sided strict probability tail is half of (1) by symmetry. The leading term \(\log Y/(\pi Y)\) implies, for every \(p>0\),
\[
 \mathbb E|X|^p=p\int_0^\infty y^{p-1}\mathbb P(|X|>y)\,dy<\infty
 \quad\Longleftrightarrow\quad 0<p<1.
\]
Each signed first-moment part diverges and the usual mean is undefined. The zero drift in the characteristic exponent is compatible with this. The conditional law of \(|X|/Y\) given \(|X|>Y\) tends to the Pareto law with survival \(1/z\) for \(z\ge1\).

## Rate, atoms, and support

The Hadamard logarithmic derivative of \(\xi\), differentiated at \(s=1/2\), gives
\[
 S=\frac{\xi''(1/2)}{\xi(1/2)} .
\]
Indeed \(\xi'(1/2)=0\) by the functional equation, and the differentiated zero sum is \(-\sum_\rho(1/2-\rho)^{-2}=\sum_\gamma m_\gamma/\gamma^2\) under RH. This sum is absolutely convergent. Equivalently the same expression follows by differentiating the paired canonical product in the zero-ordinate variable. The analytic ratio can be evaluated unconditionally; the identification with the Poisson rate uses RH. This rate uses multiplicity divided by squared ordinate and is distinct from the derivative sum defining the tapered-array constant.

Write \(w_\gamma=m_\gamma/\gamma^2\) for the positive ordinates. Conditioning on \(K=0,1,2\) gives
\[
 e^{-S}\left(1+\sum_{\gamma>0}w_\gamma^2\right)
 \le \mu(\{0\})\le
 e^{-S}\left(1+\sum_{\gamma>0}w_\gamma^2\right)+\mathbb P(K\ge3).
\]
The \(K=1\) term vanishes. For \(K=2\), the only zero sums are ordered pairs of opposite ordinates, giving the displayed square sum exactly. Consequently \(\mu(\{0\})>e^{-S}\), and also \(\mu(\{0\})\le 1-Se^{-S}\). The contributions from all larger jump counts are nonnegative and can depend on additive relations. No assumption about independence of the ordinates over \(\mathbb Q\) is needed.

A 128-bit Arb check of the completed-\(\xi\) Taylor series gave \(S=0.046209986230837941577867620860678028\) with radius less than \(8.3\cdot10^{-37}\). For the cancellation lower bound it uses the 29 positive simple zeros below 100. For the upper bound, the jump of \(N\) at \(\gamma\) and its left limit in the count bound give \(w_\gamma\le2(a\log\gamma+b)/\gamma^2\). This is decreasing for \(\gamma\ge100\). The missing square sum is therefore at most \(2(a\log100+b)/100^2\) times the remaining positive mass \(S/2-\sum_{0<\gamma\le 100}w_\gamma\). Adding \(\mathbb P(K\ge3)=1-e^{-S}(1+S+S^2/2)\) gives the outward verified interval
\[
 0.95487677454644730 < \mu(\{0\}) < 0.95490529007639706 .
\]
Only the existing small finite height is revisited. [Arb checks](../../scripts/prime64_nakamura_heavy_tail_checks.py)

The set of atoms is exactly the additive subgroup
\[
 \Gamma=\left\{\sum_{\gamma>0} n_\gamma\gamma:
            n_\gamma\in\mathbb Z,\; n_\gamma=0
                 \text{ for all but finitely many }\gamma\right\}.
\]
Each finite representation has positive probability by taking one prescribed finite count and prescribed jump order. Conversely the finite jump sum always lies in this countable set. The topological support is \(\overline\Gamma=\mathbb R\). Indeed Bui–Conrey–Young prove an unconditional lower proportion \(\kappa^*\ge .4058\) for simple critical-line zeros, hence the distinct positive ordinates below \(T\) number \(\gg T\log T\). A nondense additive subgroup of \(\mathbb R\) is discrete cyclic and contains only \(O(T)\) elements in that range. Thus the law is pure point with dense atoms. [Bui–Conrey–Young, Theorem 1.1](https://arxiv.org/pdf/1002.4127v2)

## Cusp and Cauchy scaling

In fact the local cusp of the function \(g_\zeta\) is unconditional. The result is
\[
 g_\zeta(t)= -\frac{|t|}{2}
  \left[\log\frac1{|t|}+1-\gamma_E-\log(2\pi)\right]
       +O\!\left(t^2\log\frac1{|t|}\right),\qquad t\to0,              \tag{2}
\]
where \(\gamma_E\) denotes Euler's constant.

To see this, pair the zeros of \(\xi(1/2-iz)\) under \(\gamma\mapsto-\gamma\) in equation (1.7) of Nakamura–Suzuki. Put \(u=|t|\) and \(k(z)=(1-\cos z)/z^2\), with the removable value at zero. The paired expression is \(-2u^2\sum_{\Re\gamma>0}m_\gamma k(u\gamma)\). There are no zeros with \(\Re\gamma=0\), by the eta-series sign on the real critical strip, and \(|\Im\gamma|\le1/2\). For \(\lambda=\Re\gamma>0\), compare \(k(u\gamma)\) to \(k(u\lambda)\) along the vertical segment. For \(u\lambda\le1\), the analytic derivative is \(O(u(\lambda+1))\), since \(k'(0)=0\). For \(u\lambda\ge1\), direct differentiation gives \(O((u\lambda)^{-2})\) on the segment because its imaginary height is at most \(u/2\). The summed error, with the outside \(u^2\) and segment length at most \(u/2\), is
\[
 O\!\left(u^4\sum_{\lambda\le1/u}m_\gamma(\lambda+1)
        +u\sum_{\lambda>1/u}m_\gamma/\lambda^2\right)
 = O\!\left(u^2\log(1/u)\right)
\]
by the unconditional count. The real parts have the same positive-ordinate multiplicity count \(N\) by symmetry.

Now partial-sum the real-ordinate expression \(-2\int(1-\cos(uv))v^{-2}\,dN(v)\) above any fixed height at least \(e\). The counting remainder contributes \(O(u^2\log(1/u))\), because the derivative of the kernel is \(u^3 k'(uv)\) and \(\int_0^\infty |k'(w)|(1+|\log w|)\,dw<\infty\). The fixed low part, including the smooth extension of the main density down to zero, is \(O(u^2)\). After substitution the main part is
\[
 -\frac{u}{\pi}\int_0^\infty k(w)
                 \left[\log\frac1{2\pi u}+\log w\right]\,dw .
\]
For \(0<\alpha<2\) the Mellin integral is
\[
 \int_0^\infty (1-\cos w) w^{-1-\alpha}\,dw
   =\frac{\pi}{2\Gamma(1+\alpha)\sin(\pi\alpha/2)}.
\]
Use the Laplace representation of \(w^{-1-\alpha}\), Tonelli for \(1-\cos w\ge0\), and \(\int_0^\infty (1-\cos w)e^{-tw}\,dw=1/[t(1+t^2)]\). Evaluating and differentiating at \(\alpha=1\) gives \(\int k=\pi/2\) and \(\int k(w)\log w\,dw=(\pi/2)(1-\gamma_E)\). This proves (2).

The defining prime-side formula (1.5) gives an independent check and one more term. For \(0<t<\log2\) its prime sum is empty. Set \(x=e^{-t/2}\). The derivative of the Lerch term is
\[
 -2\sum_{n\ge0}\frac{x^{4n+1}}{4n+1}
 =-\operatorname{arctanh}x-\arctan x,
\]
by integrating the geometric expansion of \(1/(1-x^4)\). Here
\(\operatorname{arctanh}(e^{-t/2})=\tfrac12\log(4/t)+O(t^2)\)
and \(\arctan(e^{-t/2})=\pi/4-t/4+O(t^2)\). With
\(\psi(1/4)=-\gamma_E-\pi/2-3\log 2\), equation (1.5) therefore gives
\[
 g_\zeta'(t)=\tfrac12[\log(2\pi t)+\gamma_E]-\tfrac74t+O(t^2).
\]
In particular the remainder on the right of (2) is actually \(-7t^2/8+O(|t|^3)\). This computation uses the unconditional defining formula and its even extension.

Under RH take iid draws \(X_1,X_2,\ldots\) from the law and let \(a_n=\tfrac12 n\log n\) for \(n\ge2\). The cusp gives \(n g_\zeta(t/a_n)\to-|t|\) for each fixed real \(t\). Lévy's continuity theorem yields \((X_1+\cdots+X_n)/a_n\) converging in law to the standard Cauchy with characteristic function \(e^{-|t|}\). Symmetry supplies the zero centering. Formula (2) also formally gives this pointwise scaling limit unconditionally, without first identifying globally positive-definite functions.

For a synthetic control choose a nonreal \(\omega=a+ib\) with \(a,b>0\) and add the off-real quartet \(\pm\omega,\pm\bar\omega\) to a real-zero model with bounded exponent \(g\) and the cusp in (2). Its added exponent is \(4\Re[(\cos(\omega t)-1)/\omega^2]\). This is \(O(t^2)\) at zero, so the pointwise Cauchy scaling is identical. It has positive exponentially large values along a sequence \(t\to\infty\) by choosing the phase of \(e^{-iat}/\omega^2\) positive real. Thus every positive exponential power of the perturbed exponent is unbounded on the real line and fails the modulus bound for characteristic functions. The finite synthetic quartet exemplifies the gap between a local scaling limit and global positive definiteness.

## Comparison with the prime torus

The derivative-weighted prime-torus result samples one large ordinate with weight \(|\zeta'(\rho)|^2/|\rho|^2\) and gives a limit on \(\widehat{\mathbb Q_{>0,\mathrm{disc}}}\). The Nakamura–Suzuki law is the entire finite random sum of signed zero ordinates with weights \(m_\gamma/\gamma^2\), and lives on the ordinary additive real line. Push it to the torus by \(x\mapsto(e^{ix\log p})_p\). Its coefficients at \(m/n\) are \(\exp(g_\zeta(\log(m/n)))\), lying in \([e^{-2S},1]\) from the finite symmetric Lévy measure. The derivative-weighted limit has coefficient \(\gcd(m,n)/\sqrt{mn}\), which tends to zero along \(m=p^j,n=1\). Also the pushed-forward compound Poisson law has an atom at the identity, whereas each Poisson-circle marginal of the derivative-weighted limit has a density. These facts distinguish the two laws even on the same compact group. Publication priority of the deductions in this note has not been assessed. [Derivative-weighted prime-torus limit](director_hlz_prime_torus_round9.md)
