# Beta smoothing: a normalized right limit does not supply a Dirichlet expansion

2026-11-17. Independent reconstruction by `/root/li_skeptic`, developed in discussion with root and independently reviewed by corpus. Novelty has not been investigated sufficiently to claim it. This is a countermodel in a broader analytic class, not an RH result. Classical Bessel ingredients and their original Pólya1926 source are recorded in the preceding Bessel audit. The base positive/log-concave kernel certificate has a separate third review, `audits/adversarial_reviews/bessel_third_round3.md`.

## The theorem, including its quantifiers

For every integer `N>=1`, set

\[
 B_N=8N^2+50,\qquad T_N=10NB_N,\qquad a=1/4.
\]

There exists a real `delta_N` in `(0,1/100)` with the following properties. Put `T=T_N`, `delta=delta_N`, `c=2pi exp(2delta)`, `w=s-1/2`,

\[
 Q_T(w)=((w-a)^2+T^2)((w+a)^2+T^2),
\]
\[
 M_\delta(w)=\Gamma(9/4)\sum_{k=0}^\infty
       \frac{(\delta^2w^2/4)^k}{k!\Gamma(k+9/4)},
\]
\[
 A=\big[K_{1/4}(c)Q_T(1/2)M_\delta(1/2)\big]^{-1},\qquad
 F(s)=A K_{w/2}(c)Q_T(w)M_\delta(w).
\]

Then `F` is real entire, symmetric under `s -> 1-s`, normalized by `F(0)=F(1)=1`, of order one and infinite exponential type. Its centered bilateral Laplace kernel is even, smooth, everywhere strictly positive, and has strictly negative second logarithmic derivative. There are exactly four off-line zeros, `s=1/2 +/-1/4 +/-iT`; every other zero is on the line, with multiplicity retained. No assertion that distinct factors have no common line zeros is needed. Its positive-ordinate count is

\[
 N_F(X)=\frac X{2\pi}\log\frac X{2\pi}-\frac X{2\pi}+O(1).
\]

The first `N` Li coefficients satisfy `lambda_n(F)>1/(12B_N^2)`, `1<=n<=N`. The function is permitted to depend on `N`; no all-coefficient positivity is claimed.

Define **without a factor of one half**

\[
 Z(s)=\frac{\pi^{s/2}F(s)}{s(s-1)\Gamma(s/2)}.
\]

This convention makes `F` analogous to `2xi`, and gives residue one, not two, at `s=1`. The function has the standard completed functional equation, `Z(0)=-1/2`, exactly simple trivial zeros at the negative even integers, and only a simple pole at one. Uniformly on every fixed finite real strip,

\[
 Z(\sigma+it)\ll |t|^{\max(0,1/2-\sigma)}.
\]

In particular it is bounded on every fixed right strip `sigma>=1/2`, and satisfies the usual convexity-shaped upper bounds on `0<=sigma<=1`. Nevertheless it cannot be an ordinary Dirichlet series on any nonempty half-plane. The decisive exact obstruction is

\[
 Z(\sigma)=1-\frac{b}{\sigma}+O(\sigma^{-2}),\qquad
 b=\frac{c^2}{2}+\frac{21}{32\delta}-\frac3{16}>0.
\]

An absolutely convergent ordinary Dirichlet series with right limit one instead has `Z(sigma)-1=O(2^{-sigma})`.

## 1. The beta smoothing factor and its zeros

Let `p=3/4` and normalize the even probability density

\[
 b_\delta(v)=\frac{\Gamma(9/4)}{\sqrt\pi\Gamma(7/4)\delta}
       \big(1-v^2/\delta^2\big)^{3/4}\mathbf1_{|v|<\delta}.
\]

The beta integral proves that it has mass one. Expanding its exponential transform term by term, or using the actually inspected DLMF10.32.2 integral, gives exactly the entire series defining `M_delta` above. In conventional Bessel notation,

\[
 M_\delta(w)=\Gamma(9/4)(2/(\delta w))^{5/4}I_{5/4}(\delta w).
\]

The entire series, not a branch-ambiguous fractional power, is the definition. `M_delta(0)=1`, and it is positive on the real axis. Its zeros are `w=+/-i j_{5/4,k}/delta`; all are simple within this factor. DLMF10.21.15 gives the exact normalized `J` product for fixed nonnegative order; DLMF10.21.19 gives `j_{5/4,k}=pi(k+3/8)+O(1/k)`. Hence its positive-ordinate count is `delta X/pi+O(1)`.

There is also an independent all-complex-zero check. For `nu=5/4`, the normalized entire `J` solution `r^{nu+1/2} E_nu(zr)` solves the finite-interval equation

\[
 -u''+\frac{\nu^2-1/4}{r^2}u=z^2u,\qquad0<r<1,
\]

with the regular/Friedrichs behavior `u~r^{nu+1/2}` at zero and a Dirichlet zero at one whenever `E_nu(z)=0`. Integration against the conjugate solution has vanishing zero-endpoint boundary term and forces `z^2>0`; therefore every nonzero zero is real. Ordinary ODE uniqueness at a nonzero argument excludes simultaneous zeros of `J` and `J'`, proving simplicity. The positive inverse-square operator has compact resolvent and infinitely many eigenvalues. This avoids inferring absence of complex zeros merely from the existence of many real zeros.

## 2. Parameter range and exact zero-count retuning

For `0<delta<=1/100`, `6<c<7`: use `3<pi<22/7` and `exp(1/50)<50/49` to get `c<(44/7)(50/49)<7`. Thus the already proved base-kernel sign and concavity certificate applies with the same `T>=32`; it is not being extrapolated to arbitrary `c`.

The baseline Bessel positive-ordinate count is

\[
 N_{K,c}(X)=\frac X{2\pi}\log(X/c)-\frac X{2\pi}+O(1)
\]

by the classical Pólya result, independently reconstructed in the previous audit. Adding `M_delta` contributes `delta X/pi+O(1)`; adding the quartet contributes two once `X>=T`. Since `log(c/(2pi))=2delta`, the added linear term exactly cancels the retuning shift. Multiplicities are additive at any coincident line zeros. This proves the displayed RVM smooth count with `O(1)` error. It does not match the true zeta oscillatory term or individual zero ordinates.

## 3. Strict log-concavity after beta convolution, with all endpoint terms checked

The base kernel `k=Q_T(D) exp[-c cosh(2u)]` is smooth, even, positive and has `(log k)''<0` on the certified domain. Its beta convolution is smooth because derivatives fall on `k`, and is everywhere positive because `k` is positive and `b_delta` has positive mass. The beta density itself is not smooth at its support endpoints; no such claim is needed. A bounded convolution preserves the double-exponential tail bounds needed for all bilateral exponential moments.

Here is a self-contained one-dimensional Brascamp–Lieb argument proving the stronger pointwise second-derivative statement, not merely strict Jensen concavity. Write `V=-log k`, `W=-log b_delta` on the support interior. At fixed `x`, define the probability density

\[
 p(v)\propto e^{-U(v)},\quad U(v)=V(x-v)+W(v),
 \quad -\delta<v<\delta.
\]

`V''>0`, and

\[
 W''(v)=\frac32\frac{\delta^2+v^2}{(\delta^2-v^2)^2}>0.
\]

For `h=k*b_delta`, differentiation under the compact integral gives

\[
 (\log h)''=-E V''+\operatorname{Var}(V').
\]

For completeness put `phi(v)=V'(x-v)-E V'`, `F(v)=integral_{-delta}^v phi(t)p(t)dt`, and `u=F/p`. Then `F` vanishes at both endpoints, and `phi=u'-U'u`. Two integrations by parts give

\[
 E\phi^2=E(u')^2+E U''u^2,\qquad
 E\phi^2=-E\phi'u.
\]

At either endpoint, with distance `d` to it, `p` is comparable to `d^{3/4}`, `F=O(d^{7/4})`, `u=O(d)`, and `U'=O(1/d)`. Thus the boundary term `U'u^2p` tends to zero; `phi F` does too. All displayed integrals converge. These facts justify integration first on truncated intervals and then taking endpoint limits.

Cauchy–Schwarz and the first identity yield

\[
 \operatorname{Var}(V')\le E\frac{(V'')^2}{V''+W''}.
\]

Consequently

\[
 (\log h)''\le-E\frac{V''W''}{V''+W''}<0.
\]

The integrand is positive and bounded by `V''` on each fixed compact convolution interval, so the inequality is both strict and finite. Positive normalization leaves it unchanged. Evenness then gives strict decrease for positive arguments.

## 4. Vertical bounds with no Stokes-line shortcut

The previous audit proved, uniformly for `sigma` in any fixed finite interval,

\[
 |K_{(s-1/2)/2}(c)|\ll e^{-\pi|t|/4}
       |t|^{|\sigma-1/2|/2-1/2}.
\]

That proof used both `I_{+nu}` and `I_{-nu}`, gamma Stirling and the sine connection denominator; it remains valid at `sigma=1/2`.

For the beta factor one can prove the needed bound directly, without extending a one-exponential `I` expansion across its sector boundary. In the integral for `M_delta(q+it)`, `q=Re(w)` lies in a fixed bounded interval. Write its amplitude as `a_q(v)=b_delta(v)e^{qv}`. With `p=3/4` and `d(v)` the distance to a support endpoint, uniformly in bounded `q`,

\[
 |a_q'(v)|\ll d^{p-1},\qquad |a_q''(v)|\ll d^{p-2}.
\]

The first integration by parts has no endpoint term because `a_q` vanishes at both endpoints, and extracts one factor `1/t`. In the derivative integral split off endpoint layers of width `1/|t|`. Their total absolute contribution is `O(|t|^{-p})`. On the remaining interval integrate once more; the boundary values and the integral of `|a_q''|`, divided by `|t|`, are also `O(|t|^{-p})`. Therefore

\[
 |M_\delta(q+it)|\ll |t|^{-p-1}=|t|^{-7/4}.
\]

Constants may depend on fixed `delta` and the strip; the construction does not require uniformity as `delta` tends to zero while `t` is fixed. Equivalently this bound follows from the inspected fixed-order `J` expansion DLMF10.17.3 in a horizontal strip near the positive real axis, but the endpoint proof already supplies it.

Combining quartet `+4`, beta `-7/4`, `s(s-1)` `-2`, and reciprocal gamma `-sigma/2+1/2`, all exponential factors cancel and the exponent is

\[
 \frac{|\sigma-1/2|-\sigma}{2}+\frac14
 =\max(0,1/2-\sigma).
\]

For `0<=sigma<=1` this is at most `(1-sigma)/2`, as asserted.

## 5. Real-axis expansion and exact normalization

Let `sigma` tend to positive infinity, with the constructed `T,delta,c` fixed. The exact gamma-expectation representation from the previous audit gives, for `nu=sigma/2-1/4`,

\[
 K_\nu(c)=\tfrac12\Gamma(\nu)(c/2)^{-\nu}
       \big[1-c^2/(2\sigma)+O(\sigma^{-2})\big].
\]

This coefficient is rigorously checked by `0<=e^{-y}-1+y<=y^2/2` and the inverse first and second moments of a Gamma variable. No formal large-imaginary-order substitution is used.

For the beta factor, Laplace expansion at its right support endpoint gives

\[
 M_\delta(w)=\frac{2^{3/4}\Gamma(9/4)}{\sqrt\pi\delta^{7/4}}
 e^{\delta w}w^{-7/4}
 \big[1-21/(32\delta w)+O(w^{-2})\big].
\]

To see the coefficient directly, substitute `v=delta-y`: the endpoint weight is a constant times `y^{3/4}(1-y/(2delta))^{3/4}`. Its Taylor expansion is `y^{3/4}[1-3y/(8delta)+O(y^2)]`. Integrating the first two terms against `e^{-wy}` gives the relative coefficient `-(3/4)(7/4)/(2delta w)=-21/(32delta w)`; the remaining endpoint tail is exponentially small and the Taylor remainder contributes `O(w^{-2})` relative error. The inspected DLMF10.40.1 expansion for fixed order `5/4` agrees.

The other first-order terms are

\[
 \frac{\Gamma(\sigma/2-1/4)}{\Gamma(\sigma/2)}
 =(\sigma/2)^{-1/4}[1+5/(16\sigma)+O(\sigma^{-2})],
\]
\[
 \frac{Q_T(\sigma-1/2)}{\sigma(\sigma-1)}
 =\sigma^2[1-1/\sigma+O(\sigma^{-2})],\quad
 (\sigma-1/2)^{-7/4}=\sigma^{-7/4}[1+7/(8\sigma)+O(\sigma^{-2})].
\]

Retuning `c=2pi e^{2delta}` cancels the real exponential `e^{delta sigma}(2pi/c)^{sigma/2}`. Its constant factor also simplifies exactly. The result is

\[
 Z(\sigma)=C(T,\delta)\big[1-b/\sigma+O(\sigma^{-2})\big],
\]
\[
 C(T,\delta)=\frac{A\Gamma(9/4)}{\pi^{1/4}\delta^{7/4}},\qquad
 b=c^2/2+21/(32\delta)-3/16>0.
\]

The constant contains no extra factor two. An independent reviewer initially used the completion `s(s-1)Gamma/2`, doubling both this constant and the residue; the explicit convention `F(1)=1`, `Z=pi^{s/2}F/[s(s-1)Gamma]` resolves that discrepancy. The first correction adds as `5/16-1+7/8-c^2/2-21/(32delta)=3/16-c^2/2-21/(32delta)`.

## 6. Tuning `C=1`: rigorous existence with an explicit endpoint estimate

For each fixed `T`, `C(T,delta)` is positive and continuous on `(0,1/100]`, and tends to infinity as `delta` tends to zero: `c->2pi`, `M_delta(1/2)->1`, and `Q_T(1/2)>0` is fixed.

At `delta_0=1/100`, an elementary lower bound for the Bessel integral is

\[
 K_{1/4}(c)=\int_{\mathbb R}e^{-c\cosh2u}e^{u/2}du
 >\frac15 e^{-9}>\frac1{5\,3^9}.
\]

Indeed integrate over `[-1/10,1/10]`, use the even average `cosh(u/2)>=1`, and `c cosh(1/5)<7e^{1/5}<7(5/4)<9`. Also `M_delta(1/2)>=1`, `Q_T(1/2)>=T^4`, and log-convexity of gamma gives `Gamma(9/4)<=Gamma(2)^{3/4}Gamma(3)^{1/4}=2^{1/4}<2`. Since `pi^{1/4}>1` and `delta_0^{7/4}>10^{-4}`,

\[
 C(T,1/100)<\frac{100000\,3^9}{T^4}<1\qquad(T\ge256).
\]

The intermediate value theorem therefore supplies at least one tuned `delta` for every `T>=256`; uniqueness is neither proved nor needed. Every `T_N` in the theorem is at least580, so the same explicit quartet height suffices for tuning and finite-Li positivity.

Every choice of tuned root has `delta_T->0` as `T->infinity`, since on each fixed closed subinterval away from zero the denominator is bounded below and `Q_T(1/2)` grows as `T^4`. More precisely the equation `C=1` gives

\[
 \delta_T T^{16/7}\longrightarrow
 \left[\frac{\Gamma(9/4)}{\pi^{1/4}K_{1/4}(2\pi)}\right]^{4/7}.
\]

This supplies an additional continuity route to finite prefixes, but the uniform quantitative proof below is stronger and does not depend on selecting a continuous tuning branch.

## 7. Explicit uniform finite-Li margin

Here the min–max and quartet bounds were independently reconstructed, rather than copied from the advocate's draft. For the Dirichlet half-line operator `H_c=-d^2/dt^2+c^2e^{2t}`, denote eigenvalues by `lambda_j` and corresponding Bessel line ordinates by `gamma_j=2sqrt(lambda_j)`.

Take `j=N^2`. Since `c^2e^{2t}>=t^2`, comparison with the Dirichlet half-line harmonic oscillator, whose eigenvalues are `4j-1`, gives `gamma_j>=2sqrt(4N^2-1)>2N`. Conversely the first `j` sine functions supported on `[0,1]` give by min–max

\[
 \gamma_j\le2\sqrt{\pi^2N^4+c^2e^2}
 <2\sqrt{16N^4+441}<8N^2+42<B_N.
\]

The harmonic oscillator eigenvalues are the standard odd Hermite spectrum; their spectral comparison is the only additional classical operator input here.

For the conjugate pair at this ordinate, put `theta=2arctan(1/(2gamma_j))`. Then `1/(2gamma_j)<=theta<=1/gamma_j`, so `0<n theta<1/2` for every `n<=N`. Since `1-cosu>=u^2/3` on this range, that pair contributes

\[
 2(1-\cos n\theta)\ge n^2/(6\gamma_j^2)>1/(6B_N^2)
\]

to every first-`N` baseline Li coefficient. All other line pairs, including all beta-factor pairs, contribute nonnegative terms. Paired Hadamard products have no hidden linear exponential because the factors are even of order one; reciprocal squared ordinates sum.

For the four quartet roots `rho=1/2 +/-a +/-iT`, define `S_k=sum rho^{-k}`. Conjugate pairing gives `|S_1|<=2/T^2`, while `|S_k|<=4/T^k` for `k>=2`. The finite polynomial Li formula and the binomial inequality
`binom(n,k)<=n(n-1)binom(n-2,k-2)/2` imply, for `T>=N`,

\[
 |\lambda_n(Q_T)|\le\frac{2n}{T^2}
 +\frac{2n(n-1)}{T^2}(1+1/T)^{n-2}
 <\frac{8N^2}{T^2}.
\]

For `n=1`, omit the empty tail. The rootwise formula uses reflection symmetry to pass from the derivative expression to the usual inverse-power sum. At `T=T_N=10NB_N`, the perturbation is less than `2/(25B_N^2)<1/(12B_N^2)`, leaving the stated margin `lambda_n(F)>1/(12B_N^2)`. Tuning normalization is a constant and has no Li contribution.

## 8. Why the remaining arithmetic condition is substantive

With `C=1`, the exact first correction has `b>0`, so `Z(sigma)-1` is genuinely of algebraic size `1/sigma`. If `Z=sum a_n n^{-s}` converges absolutely in a right half-plane, dominated convergence gives `a_1=lim Z(sigma)=1`. At any fixed absolute-convergence abscissa `sigma_0`,

\[
 |Z(\sigma)-1|\le2^{-(\sigma-\sigma_0)}
       \sum_{n\ge2}|a_n|n^{-\sigma_0}=O(2^{-\sigma}),
\]

a contradiction. Convergence anywhere implies absolute convergence sufficiently far right, so no ordinary half-plane of convergence is possible.

Thus the exact gamma factor, functional equation, pole/residue, trivial zeros, right limit one, ordinary polynomial vertical bounds, RVM smooth count with bounded remainder, positive strictly log-concave smooth kernel, finitely many off-line exceptions, and any fixed finite positive Li prefix still do not supply the discrete arithmetic expansion. This is a precise generic-class obstruction. It says nothing against a proof that uses genuine Dirichlet/Euler/prime information.

## Source and review boundaries

Actual formula passages inspected: DLMF10.32.2 (beta/I integral); 10.21.15 (J product), 10.21.19 (fixed-order positive zeros); 10.17.1–3 (fixed-order J asymptotic); 10.40.1 (fixed-order I asymptotic), plus the gamma and Bessel connection formulas cited in the previous audit. No entire DLMF chapter is claimed audited. The endpoint real/vertical beta expansions and the strict-concavity inequality were independently derived above, reducing reliance on uninspected uniform asymptotic assumptions. Pólya1926 and the two modern Bessel primary papers retain the precise source records already saved; they are not new source counts for this extension.

All claims are about a deliberately constructed nonarithmetic model. Priority remains unassessed. Source reading, independent reconstruction, exact polynomial-certificate replay, and original numerical validation are distinct statuses and must remain so in the aggregate archive.

## Optional existence refinement: every zero can be made simple

This separate refinement was proposed by corpus and independently checked by root and skeptic. It does not assert that an arbitrary tuned root at the explicit fixed height `T_N` avoids collisions.

Define for `delta>0` sufficiently small

\[
 H(\delta)=\frac{\Gamma(9/4)}
 {\pi^{1/4}\delta^{7/4}K_{1/4}(2\pi e^{2\delta})M_\delta(1/2)},
\]
\[
 T(\delta)^2=\sqrt{H(\delta)+1/16}-5/16.
\]

The quantity is positive for sufficiently small `delta` and tends to infinity. The exact polynomial identity

\[
 Q_T(1/2)=(T^2+1/16)(T^2+9/16)
             =(T^2+5/16)^2-1/16
\]

shows that this formula enforces `C(T(delta),delta)=1` exactly.

The Bessel line ordinates `gamma_j(c)` are real analytic in the positive parameter `c`: the order zeros are simple, so the implicit-function theorem applies locally; the ordered eigenvalues are simple and cannot cross, so the labels patch. Each fixed label also extends analytically through `c=2pi`. Therefore for each positive pair of indices `j,m`, the function

\[
 r_{j,m}(\delta)=\delta\gamma_j(2\pi e^{2\delta})-j_{5/4,m}
\]

is real analytic in an interval including zero and has nonzero value `-j_{5/4,m}` there. It is not identically zero, so its zeros in a small positive interval are discrete and hence countable. The union over all pairs is countable. Outside that set the simple Bessel and simple beta zero sets do not collide. The quartet zeros are already simple and are off line, so cannot collide with either line set.

One can thus choose arbitrarily small positive `delta` outside the countable bad set, with `T(delta)` above any prescribed finite-Li threshold. The resulting model has **all zeros simple**, while retaining the right limit one, the nonzero `1/sigma` Dirichlet obstruction, all listed analytic properties, and any chosen finite positive Li prefix. This is an existence statement; no specific rational or algebraic `delta` is certified outside the bad set. It remains distinct from the explicit-height `T_N` family, where simplicity across factors was not claimed. Neither family matches individual zeta zeros.
