# Independent reconstruction of the small-shift ratio slope

2026-11-17. Investigator `/root/li_skeptic`. The statement and mechanism proposed by the root were challenged and reconstructed independently before reading any root proof. **The argument below supports the stated RH-conditional limit.** It includes an explicit negative control showing why contractivity alone would not justify exhaustion by zeros. Historical priority is unassessed; no publication novelty, zero simplicity, or RH assertion is made.

This refines the prior `J_epsilon<<epsilon` estimate of **PAPER-C103**, Proposition2, without changing its attribution. The actual source's remark onp8 asks for a more precise asymptotic, but an open question in a2008/2018 manuscript is not evidence that it remained open at the present cutoff. Prior-literature comparison is a separate task.

## Statement

Assume RH. For each distinct real ordinate `gamma` of a nontrivial zeta zero, let `m_gamma` be its multiplicity; both positive and negative ordinates appear separately. Put

\[
 b_m=4^{-m}\binom{2m}{m},\qquad D_\gamma=1/4+\gamma^2.
\]

Then the independently reconstructed limit is

\[
 \lim_{\epsilon\downarrow0}\frac1\epsilon\frac1{2\pi}
 \int_{\mathbb R}\left|
 \frac{\zeta(1/2+it)}{\zeta(1/2+\epsilon+it)}-1
 \right|^2\frac{dt}{1/4+t^2}
 =\sum_{\gamma\ {m distinct}}
 \frac{m_\gamma(1-b_{m_\gamma})}{D_\gamma}.
 \tag{S1}
\]

The positive series converges. Under RH its value is at least `xi'(1)/xi(1)`, with equality precisely when every nontrivial zero is simple. Neither side has been evaluated from a finite zero list as a proof about actual simplicity.

## 1. Exact total mass available for localization

Let `F(w)=xi(1/2+w)` and `H_epsilon(w)=F(w)/F(w+epsilon)`. The standard RH paired product, with multiplicities, is

\[
 F(w)=F(0)\prod_{\gamma>0}(1+w^2/\gamma^2)^{m_\gamma}.
\]

Its reciprocal-square sum converges and it has no nonconstant zero-free exponential factor: evenness removes the linear exponential allowed for an order-one entire function. The independently reviewed Poisson proof shows that `H_epsilon` is holomorphic and contractive on the right half-plane, continuous at each finite boundary point, and

\[
 \int \operatorname{Re}H_\epsilon(it)d\nu(t)=H_\epsilon(1/2),
 \qquad d\nu(t)=\frac{dt}{2\pi(1/4+t^2)}.
\]

Define positive finite measures

\[
 d\mu_\epsilon(t)=\frac{1-\operatorname{Re}H_\epsilon(it)}\epsilon d\nu(t),
 \qquad d\lambda_\epsilon(t)=\frac{|1-H_\epsilon(it)|^2}\epsilon d\nu(t).
\]

Contractivity gives `lambda_epsilon<=2mu_epsilon` as measures. Their relevant total-mass identity is

\[
 \mu_\epsilon(\mathbb R)
 =\frac{1-F(1/2)/F(1/2+\epsilon)}\epsilon
 \longrightarrow r:=F'(1/2)/F(1/2).
 \tag{S2}
\]

Logarithmic differentiation of the normally convergent paired product is absolutely justified at the positive real point, and gives the exact positive sum

\[
 r=\frac12\sum_{\gamma\ {m distinct}}
               \frac{m_\gamma}{D_\gamma}
 =\frac{\xi'(1)}{\xi(1)}.
 \tag{S3}
\]

This equality, rather than only the boundedness of total mass, will rule out escaped mass.

## 2. The local profile at a zero

Fix an ordinate `gamma` with multiplicity `m`. Locally factor

`F(w)=(w-i gamma)^m G(w)`, where `G` is holomorphic and nonzero near `i gamma`.

For every fixed compact real `u` interval, direct substitution gives uniformly

\[
 H_\epsilon(i\gamma+i\epsilon u)
 =\left(\frac{iu}{1+iu}\right)^m
   \frac{G(i\gamma+i\epsilon u)}
        {G(i\gamma+\epsilon+i\epsilon u)}
 \longrightarrow h_m(u):=\left(\frac{iu}{1+iu}\right)^m.
 \tag{S4}
\]

There is no assumption of simple zeros here. The denominator local factor stays nonzero for sufficiently small epsilon on each fixed `u` interval. At `u=0` the identity and limit hold with numerator zero.

Write `w_gamma=1/(2pi D_gamma)`. Rescaling `t=gamma+epsilon u`, compact dominated convergence now yields, for every fixed `R>0`,

\[
 \mu_\epsilon([\gamma-\epsilon R,\gamma+\epsilon R])
 \longrightarrow w_\gamma\int_{-R}^R(1-\operatorname{Re}h_m(u))du,
 \tag{S5}
\]

and the analogous identity for `lambda_epsilon` with integrand `|1-h_m|²`. The Poisson density is continuous at the fixed ordinate, and both profile integrands are bounded on a compact interval.

## 3. Exact profile integrals

For every positive integer `m`,

\[
 \int_{\mathbb R}(1-\operatorname{Re}h_m(u))du=m\pi.
 \tag{S6}
\]

To prove this, expand `h_m=(1-(1+iu)^(-1))^m`. The `k=1` real-part integral is pi and has coefficient `m`. For `k>=2`, the integral of `(1+iu)^(-k)` is zero by its decaying antiderivative. All the real-part terms are absolutely integrable, including the `k=1` real part, so this is not an interchange of divergent imaginary integrals.

Also `|h_m|²=(u²/(1+u²))^m`. Integration by parts on the positive half-line, whose boundary term vanishes at zero and infinity, gives

\[
 \begin{aligned}
 \int_{\mathbb R}(1-|h_m|^2)du
 &=4m\int_0^\infty\frac{u^{2m}}{(1+u^2)^{m+1}}du\\
 &=2m B(m+1/2,1/2)
 =2m\pi b_m.
 \end{aligned}
\]

Since `|1-h|²=2(1-Re h)-(1-|h|²)`, it follows that

\[
 \int_{\mathbb R}|1-h_m(u)|^2du
 =2m\pi(1-b_m).
 \tag{S7}
\]

The corresponding local masses are thus

`r_gamma=m_gamma/(2D_gamma)` for `mu`, and
`s_gamma=m_gamma(1-b_(m_gamma))/D_gamma` for `lambda`.

They are nonnegative, with `s_gamma<=2r_gamma`. Equation(S3) says that the sum of **all** `r_gamma` is the entire limiting mass `r`.

## 4. Exhaustion proof: no missing far-height or intermediate-scale mass

This step is indispensable. Pointwise convergence away from zeros and local profile calculations alone would not determine the full integral.

Choose any finite set `Z` of distinct ordinates and any fixed `R`. For sufficiently small epsilon the rescaled windows about these finitely many ordinates are disjoint. Let `M(Z,R)` and `S(Z,R)` be the finite sums of the right sides in(S5) and its squared-defect version. By compact local convergence and(S2),

\[
 \liminf\lambda_\epsilon(\mathbb R)\ge S(Z,R),
\]

\[
 \limsup\lambda_\epsilon(\mathbb R)
 \le S(Z,R)+2\bigl(r-M(Z,R)\bigr).
 \tag{S8}
\]

The second inequality uses domination by `2mu_epsilon` on the entire complement of those windows. It includes both high ordinates and all intermediate distances from the selected zeros; there is no discarded vertical tail.

Let `R` tend to infinity for each finite set, then let the finite sets increase to all ordinates. The nonnegative profile integrals increase to(S6)–(S7). Equations(S3) and(S6) give `M(Z,R)->r`, while the sum of(S7) converges by `s_gamma<=2r_gamma`. The upper and lower bounds(S8) therefore coincide and prove

\[
 \lambda_\epsilon(\mathbb R)\longrightarrow
 \sum_\gamma s_\gamma.
 \tag{S9}
\]

Every limit here has a stated order. No uniform bound on multiplicities, zero gaps, derivative values, or the behavior of all local factors simultaneously was needed: the finite-set/finite-window exhaustion avoids those unsupported uniformities.

## 5. Completion factors do not change the slope

As in the independently checked Poisson upper-bound proof, write

`zeta(s)/zeta(s+epsilon)=H_epsilon(it)g_epsilon(s)`,

where `g_epsilon=A(s+epsilon)/A(s)` and `||g_epsilon-1||_(L²(dnu))=O(epsilon)`. Contractivity gives

`||H_epsilon(g_epsilon-1)||=O(epsilon)`,

while(S2) and domination give `||H_epsilon-1||=O(sqrt(epsilon))`. Expanding the two squared norms shows that replacing `H_epsilon` by the zeta ratio changes the integral by at most

`O(epsilon^(3/2))+O(epsilon²)=o(epsilon)`.

This proves(S1) from(S9), with exactly the source's normalization. No first derivative of the completion factor has been silently dropped inside an unbounded pointwise integral.

## 6. Multiplicity consequence and a necessary negative control

The central-binomial numbers satisfy `b_1=1/2` and `b_(m+1)/b_m=(2m+1)/(2m+2)<1`. Therefore each `1-b_m>=1/2`, with equality exactly for `m=1`. The positive sum in(S1) is consequently at least the value(S3), with equality precisely when all zeros are simple. A single multiple zero would give a strictly positive excess; zeros at very high ordinates can give an arbitrarily small excess. This is an RH-conditional criterion, not a practical finite certificate of simplicity.

**Negative control:** take the even zero-free entire function `F(w)=exp(w²)`, of order two. Its quotient `H_epsilon(w)=exp(-2epsilon w-epsilon²)` is still holomorphic and contractive on the right half-plane. At a general Poisson center `x>0`,

\[
 \int|H_\epsilon(it)-1|^2P_x(t)dt
 =1+e^{-2\epsilon^2}-2e^{-\epsilon^2-2x\epsilon},
\]

using the elementary Fourier transform of the Poisson kernel. Its slope is `4x`, hence2 for `x=1/2`, despite having no zeros. The positive real-defect mass escapes to infinity. This refutes any version of the proposed proof based on **contractivity and evenness alone**. The actual xi setting avoids it because its order-one paired product yields(S3), exactly exhausting the real-defect mass by its zeros. That structural input must be preserved in every statement of the result.

The mathematical proof within the stated xi/RH scope passes this challenge. Prior-source search, including work subsequent to PAPER-C103, is still required before any novelty or publishability claim.
