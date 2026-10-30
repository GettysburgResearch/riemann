# Theta source, a Pólya obstruction, and a convergent Bessel-order approximation

Status: proposed mathematical results with complete proofs below; the rational derivative certificate is independently replayable. No RH proof or smaller zero-free region is claimed.

Scope: the literal classical Riemann theta kernel, a global obstruction to fixed Pólya envelopes, and a new explicit family whose Fourier transforms converge locally uniformly to the actual Xi function. Worldwide novelty has not been established.

Exact sources/dependencies: the theta and Fourier normalization in Romik, arXiv:1902.06330v3, equations (1.6)–(1.11); the elementary modified-Bessel series and integral in DLMF 10.25.2 and 10.32.9; Gaussian Poisson summation; elementary probability, normal families, and Hurwitz's theorem. The proofs here do not assume a zero-free region or RH.

What was run: standard-library exact rational interval calculation of the complete eighth derivative, with a proved bound for its infinite arithmetic tail; ordinary and optimized executions agree. Separate SciPy floating-point diagnostics sample a positive approximation and locate some low zeros. The latter are not interval results or complete zero counts.

Smallest remaining gap: establish real-rootedness (or a vanishing nonreal-zero strip) for the *complete Bessel-order sums* along a cofinal parameter sequence. Positivity of their coefficients does not supply this statement.

## 1. The exact source and normalization

Put

\[
\theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},\quad
\omega(x)=\tfrac12(2x^2\theta''(x)+3x\theta'(x)),
\]

and

\[
\Phi(t)=2e^{t/2}\omega(e^{2t})
 =\sum_{n\ge1}\bigl(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2}\bigr)
 e^{-\pi n^2e^{2t}}.                                      \tag{1}
\]

The Jacobi relation gives \(\Phi(-t)=\Phi(t)\), and the Fourier normalization is

\[
\Xi(z)=\xi(\tfrac12+iz)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt. \tag{2}
\]

For \(t\ge0\), every summand in (1) is positive. Thus \(\Phi>0\) on the real line. The sum defines a holomorphic function in \(|\operatorname{Im}t|<\pi/4\), with locally uniform convergence of every derivative there. This follows directly from \(\operatorname{Re}e^{2t}>0\) on that strip.

We use \(K_\nu\) for the modified Bessel function and \(\mathcal K_{a,M}\) for our approximation kernel, so their zeros are not confused.

## 2. A source-specific fixed-envelope obstruction

### Theorem 1: a strict eighth-order obstruction

For

\[
G(t)=e^{2\pi\cosh(2t)}\Phi(t),
\]

one has the strict rational interval

\[
-8,951,861<G^{(8)}(0)<-8,951,860.                         \tag{3}
\]

Consequently, there is no positive measure \(\nu\) for which

\[
\Phi(t)=e^{-2\pi\cosh(2t)}\int_0^\infty\cosh(bt)\,d\nu(b) \tag{4}
\]

on any real neighborhood of zero where the integral is finite. More generally, no sequence of entire even functions with nonnegative Taylor coefficients, multiplied by this fixed envelope, converges pointwise to \(\Phi\) on a real neighborhood of zero.

#### Proof of the derivative interval

After multiplying the nth term of (1) by the envelope, its two pieces are constant multiples of

\[
h_{n,r}(t)=\exp\{rt-\pi(n^2-1)e^{2t}+\pi e^{-2t}\},
\quad r=9/2,5/2.
\]

Write \(A=\pi(n^2-1), B=\pi\), and set

\[
\ell_j=r\mathbf1_{j=1}-2^jA+(-2)^jB,\qquad
v_0=e^{-A+B},\qquad
v_m=\sum_{j=1}^m\binom{m-1}{j-1}\ell_jv_{m-j}.          \tag{5}
\]

Then \(v_m=h_{n,r}^{(m)}(0)\). The checker evaluates (5) for \(n=1,2,3,4\), using rational outward intervals for \(\pi\) and exponentials. Its pi interval comes from Machin's formula and alternating rational arctangent series; it does not assume a floating-point pi value.

For \(n\ge5\), \(|\ell_j|\le2^j(4n^2)\) for \(1\le j\le8\), since \(\pi<22/7\). The eighth complete Bell polynomial therefore gives

\[
|h_{n,r}^{(8)}(0)|
 \le 2^8 B_8(4n^2)^8e^{-\pi(n^2-2)},\quad B_8=4140.
\]

The absolute sum of the two source coefficients is less than \(60n^4\). With

\[
C=60\cdot256\cdot4140\cdot4^8,
\]

the entire omitted derivative tail is bounded by

\[
\sum_{n\ge5}C n^{20}e^{-3(n^2-2)}
 \le2C5^{20}e^{-69}<10^{-3}.                            \tag{6}
\]

Indeed, successive terms have ratio at most \((6/5)^{20}e^{-33}<1/2\). Both numerical inequalities in (6) are checked with rational intervals. Combining the finite prefix with this full tail proves (3). The more detailed accepted interval is approximately

\[
[-8,951,860.539503865,\ -8,951,860.537785906].
\]

For a positive cosh mixture finite on \((-r,r)\), differentiation at zero is justified using its exponential moment at any smaller positive radius; its eighth derivative is \(\int b^8d\nu(b)\ge0\), contradicting (3).

For a sequence \(H_j\) with nonnegative even Taylor coefficients, \(|H_j(z)|\le H_j(r')\) on \(|z|\le r'\). Pointwise convergence at a positive \(r'\) supplies local boundedness. A normal-family subsequence converges holomorphically to \(G\), forcing \(G^{(8)}(0)\ge0\), again a contradiction. ∎

This is an obstruction involving the exact theta source, not a countermodel that merely matches a finite theta jet.

### Theorem 2: no fixed envelope at any positive parameter

Fix \(a>0\). There is no representation

\[
\Phi(t)=e^{-a\cosh(2t)}H(t)                              \tag{7}
\]

with \(H\) entire. In particular, a positive cosh mixture finite for every real \(t\) cannot work. Nor can entire nonnegative-Taylor multipliers \(H_j\) with a bounded positive sequence \(a_j\) give pointwise convergence

\[
e^{-a_j\cosh(2t)}H_j(t)\longrightarrow\Phi(t)
\quad\hbox{for every real }t.                            \tag{8}
\]

#### Proof

The source fails to extend holomorphically across \(t_0=i\pi/4\). To see this without an appeal to an unspecified natural boundary, let \(x=i+\varepsilon\), \(\varepsilon>0\). Gaussian Poisson summation gives the exact identity

\[
\theta(i+\varepsilon)
 =\sum_{n\in\mathbb Z}(-1)^n e^{-\pi\varepsilon n^2}
 =\varepsilon^{-1/2}\sum_{k\in\mathbb Z}
 e^{-\pi(k+1/2)^2/\varepsilon}.                          \tag{9}
\]

Every fixed derivative with respect to \(\varepsilon\) is bounded by a power of \(\varepsilon^{-1}\) times \(e^{-\pi/(4\varepsilon)}\), hence is flat at zero. The same is true of \(\omega(i+\varepsilon)\), and therefore of

\[
\Phi\bigl(\tfrac12\operatorname{Log}(i+\varepsilon)\bigr).
\]

If \(\Phi\) were holomorphic near \(t_0\), this expression would be an analytic function of \(\varepsilon\) near zero with every Taylor coefficient zero. It would vanish identically there, contradicting the identity theorem and \(\Phi(0)>0\). Multiplication by the nonvanishing entire function \(e^{a\cosh(2t)}\) cannot remove this obstruction.

A positive cosh mixture finite on all of \(\mathbb R\) is entire: its exponential moment at \(R+1\) dominates the integral and derivatives on each disk of radius \(R\). Finally, in (8) choose a subsequence \(a_j\to a_*\) from the bounded sequence. Nonnegative Taylor coefficients imply \(\sup_{|z|\le R}|H_j(z)|\le H_j(R)\), while (8) makes the right side bounded. Normal families and the identity theorem would produce an entire extension of \(e^{a_*\cosh(2t)}\Phi(t)\), the contradiction just established. ∎

### Corollary: the necessary parameter and bandwidth escape

In any successful pointwise-all-real approximation (8), \(a_j\to\infty\). If

\[
H_j(t)=\sum_{k}c_{j,k}\cosh(b_{j,k}t),\quad c_{j,k}\ge0,
\quad B_j=\max_k|b_{j,k}|,
\]

then also

\[
B_j/a_j\longrightarrow\infty.                          \tag{10}
\]

For fixed \(R>0\), positivity gives \(H_j(R)/H_j(0)\le e^{B_jR}\), whereas convergence yields

\[
\log\frac{H_j(R)}{H_j(0)}
 =a_j(\cosh(2R)-1)+\log\frac{\Phi(R)}{\Phi(0)}+o(1).
\]

Thus \(\liminf B_j/a_j\ge(\cosh(2R)-1)/R\). Letting \(R\to\infty\) proves (10). No rate is asserted without a specified approximation error.

## 3. A constructive repair: explicit Skellam sampling of the complete source

The fixed-envelope obstruction does not prevent source-faithful approximation with a moving envelope. Define the even source weight

\[
w(x)=\Phi\bigl(\tfrac12\operatorname{arsinh}x\bigr),
\quad x\in\mathbb R.                                    \tag{11}
\]

It is strictly positive, smooth, and has bounded derivatives of every fixed order. For each \(0<c<2\pi\) it satisfies

\[
0<w(x)\le C_c e^{-c|x|}.                               \tag{12}
\]

For completeness, if \(t\ge0\), \(y=e^{2t}\ge1\), then (1) is bounded by \(C y^{9/4}e^{-\pi y}\): factor the first exponential and bound the remaining sum by \(\sum n^4e^{-\pi(n^2-1)}\). In (11), \(y=|x|+\sqrt{1+x^2}\ge2|x|\). The polynomial factor can be absorbed into \(e^{(2\pi-c)|x|}\). Differentiating (1) gives the same conclusion with additional polynomial factors; the derivatives of arsinh are bounded. This proves the stated regularity and (12).

For \(a>0\), set

\[
\mathcal K_a(t)=e^{-a\cosh(2t)}
 \sum_{n\in\mathbb Z}I_{|n|}(a)w(n/a)e^{2nt},            \tag{13}
\]

and truncate the *actual* coefficients by

\[
\mathcal K_{a,M}(t)=e^{-a\cosh(2t)}
 \sum_{|n|\le M}I_{|n|}(a)w(n/a)e^{2nt}.                \tag{14}
\]

### Theorem 3: source convergence, tails, and the diffusion correction

Let \(a_j\to\infty\) and \(M_j/a_j\to\infty\). Then for every \(R\ge0\),

\[
\int_{\mathbb R}|\mathcal K_{a_j,M_j}(t)-\Phi(t)|
 e^{R|t|}\,dt\longrightarrow0.                         \tag{15}
\]

The untruncated kernels obey, for all real \(t\),

\[
|\mathcal K_a(t)-\Phi(t)|
 \le\frac{\|w''\|_\infty\cosh(2t)}{2a}.                \tag{16}
\]

On each fixed compact real interval they also satisfy

\[
\mathcal K_a(t)=\Phi(t)
 +\frac{1}{8a}\frac{d}{dt}\left(\operatorname{sech}(2t)\Phi'(t)\right)
 +O_T(a^{-2}).                                          \tag{17}
\]

#### Proof: exact probability identity

Let \(X,Y\) be independent Poisson random variables of mean \(a/2\), and \(N=X-Y\). Expanding their two elementary exponential series gives

\[
\Pr(N=n)=e^{-a}I_{|n|}(a),\qquad
\mathbb E e^{2tN}=e^{a(\cosh(2t)-1)}.
\]

Exponential tilting by \(e^{2tN}\) changes the two means to \(ae^{2t}/2\) and \(ae^{-2t}/2\). Consequently (13) is exactly

\[
\mathcal K_a(t)=\mathbb E_t[w(N/a)],\qquad
\mathcal K_{a,M}(t)=\mathbb E_t[w(N/a)\mathbf1_{|N|\le M}], \tag{18}
\]

and

\[
\mathbb E_t[N/a]=s:=\sinh(2t),\qquad
\operatorname{Var}_t(N/a)=c_t/a,
\quad c_t:=\cosh(2t).                                   \tag{19}
\]

Taylor's theorem through first order, followed by expectation, proves (16). Thus \(\mathcal K_a\to\Phi\) uniformly on each real compact. The moving cutoff is harmless there: \(M_j/a_j\to\infty\), the means in (19) stay bounded, and Chebyshev's inequality controls its omitted probability uniformly.

For \(\delta=N/a-s\), the exact centered moments are

\[
\mathbb E_t\delta^2=c_t/a,\quad
\mathbb E_t\delta^3=s/a^2,\quad
\mathbb E_t\delta^4=3c_t^2/a^2+c_t/a^3.
\]

Taylor expansion through degree three, with the fourth-derivative remainder bounded globally, gives

\[
\mathcal K_a(t)=w(s)+\frac{c_t}{2a}w''(s)+O_T(a^{-2}).
\]

The chain rule gives

\[
\frac{c_t}{2}w''(s)
 =\frac{\Phi''(t)}{8\cosh(2t)}
  -\frac{\sinh(2t)\Phi'(t)}{4\cosh^2(2t)}
 =\tfrac18\frac d{dt}\bigl(\operatorname{sech}(2t)\Phi'(t)\bigr),
\]

which proves (17). This is the first asymptotic direction of the approximation, not a claim that the operators form an exact diffusion semigroup.

#### Proof: a common full-tail bound

Fix any \(c\in(0,2\pi)\) in (12) and \(a\ge a_0>0\). For \(t\ge0\), (18) and \(w(x)\le C_c e^{-cx}\) give

\[
\mathcal K_a(t)
\le C_c\exp\left\{
 -\frac a2(1-e^{-c/a})e^{2t}
 +\frac a2(e^{c/a}-1)e^{-2t}\right\}.                    \tag{20}
\]

The coefficient \(a(1-e^{-c/a})\) is at least
\(a_0(1-e^{-c/a_0})>0\), while \(a(e^{c/a}-1)\) is at most
\(a_0(e^{c/a_0}-1)\). Evenness therefore supplies constants \(A,B>0\), independent of \(a\ge a_0\) and \(M\), such that

\[
0\le\mathcal K_{a,M}(t)\le\mathcal K_a(t)
 \le A e^{-B e^{2|t|}}.                                 \tag{21}
\]

This bound is integrable after multiplication by any \(e^{R|t|}\). Dominated convergence now proves (15). ∎

Unlike the earlier finite Ising moment constructions, (13)–(15) reproduce the full source on a specified cofinal family. They do not reproduce its desired zero geometry automatically. The same construction works for many other positive kernels, including kernels whose transforms have nonreal zeros.

## 4. The actual transform and a precise open gate

Using DLMF 10.32.9 and the substitution \(u=2t\), one obtains

\[
\int_{\mathbb R}e^{-a\cosh(2t)}e^{2nt}e^{izt}\,dt
 =K_{n+iz/2}(a).                                        \tag{22}
\]

Let \(c_n(a)=I_n(a)w(n/a)\) for \(n\ge0\). The entire Fourier transform of (14) is exactly

\[
\begin{split}
F_{a,M}(z)
 &=c_0(a)K_{iz/2}(a)\\
 &\quad+\sum_{n=1}^M c_n(a)
 \bigl(K_{n+iz/2}(a)+K_{n-iz/2}(a)\bigr).                \tag{23}
\end{split}
\]

Equation (15) proves \(F_{a_j,M_j}\to\Xi\) uniformly on every complex compact. Therefore the following is a sufficient, now completely specified, source-dependent target:

> Find \(a_j\to\infty\), \(M_j/a_j\to\infty\), and \(\varepsilon_j\to0\) such that every zero of the *complete function (23)* lies in \(|\operatorname{Im}z|\le\varepsilon_j\).

The special case \(\varepsilon_j=0\) is enough. Hurwitz's theorem proves the implication: any hypothetical nonreal zero of \(\Xi\) has a small zero-containing disk separated from the shrinking strips, and local uniform convergence forces a zero of (23) there for all large \(j\). The limit is nonzero because \(\Xi(0)>0\).

This is a conditional consumer, not an established real-rootedness theorem. The zeros of the positive kernel or of its cosh multiplier are not the zeros of (23). A kernel approximation alone is not a zero-free region.

## 5. Why the easiest Lee–Yang shortcut also fails

One might try to make

\[
H_{a,M}(t)=\sum_{n=-M}^M c_{|n|}(a)e^{2nt}
\]

a universal multiplier by proving that

\[
P_{a,M}(q)=\sum_{n=-M}^M c_{|n|}(a)q^{n+M}              \tag{24}
\]

has every root on the unit circle. Such a circle-root condition would make \(H_{a,M}(it)\) real-rooted; with the classical universal-factor theorem it would be a sufficient path to real-rootedness of (23). The base transform \(K_{iz/2}(a)\) has only real zeros: if it vanishes, \(y(u)=K_{iz/2}(ae^u)\) is a nonzero decaying Dirichlet solution of \(-y^{\prime\prime}+a^2e^{2u}y=(z/2)^2y\) on \(u\ge0\). Integration against \(\overline y\) makes \((z/2)^2\) positive real, hence \(z\) real. Boundary terms vanish by the standard positive-argument Bessel decay. But this particular sufficient condition is impossible along the cofinal regime just proved.

### Theorem 4: eventual failure of the multiplier circle-root condition

If \(a_j\to\infty\) and \(M_j/a_j\to\infty\), then (24) fails to have all its roots on the unit circle for all sufficiently large \(j\).

#### Proof

If a degree-\(2M\) polynomial with leading coefficient \(c_M>0\) has all its roots on the unit circle, elementary symmetric functions give the necessary central-coefficient inequality

\[
c_0\le\binom{2M}{M}c_M\le4^Mc_M.                       \tag{25}
\]

The positive Bessel series gives

\[
I_M(a)=\sum_{k\ge0}\frac{(a/2)^{M+2k}}{k!(M+k)!}
 \le\frac{(a/2)^M}{M!}\exp\frac{a^2}{4(M+1)}.           \tag{26}
\]

Here \((M+k)!\ge M!(M+1)^k\). Since \(I_0(a)\ge1\), \(w(0)>0\), and \(w\) is bounded by some \(W\), (25) would imply

\[
w(0)\le W\left(\frac{2ea}{M}\right)^M
          \exp\frac{a^2}{4(M+1)}.                      \tag{27}
\]

The logarithm of the right side divided by \(M\) tends to \(-\infty\) when \(M/a\to\infty\), so its right side tends to zero. This contradicts \(w(0)>0\). ∎

This excludes the elementary universal-factor proof for these particular coefficients. It does **not** prove that (23) has nonreal zeros. Direct Bessel interlacing, a self-adjoint realization of the whole sum, or a source-specific bound on its nonreal-zero strip remains a distinct possibility.

## 6. Diagnostics and interpretation

`skellam_diagnostic.py` uses ordinary floating-point SciPy quadrature and root finding. At \(a=5,10,20,50\), with \(M=10a\), the first roots it located were approximately

| a | M | First located positive root | Largest source-kernel error on the 201-point grid in [0,1] |
|---:|---:|---:|---:|
| 5 | 50 | 9.3566654 | 0.24009 |
| 10 | 100 | 10.9454111 | 0.15128 |
| 20 | 200 | 12.1750845 | 0.08747 |
| 50 | 500 | 13.2094127 | 0.03874 |

A fixed ratio \(M/a=10\) is **not** the cofinal regime of Theorem 3; these finite computations only probe a useful large cutoff on the displayed low interval. The run found low real roots and did not locate a nonreal root in its tested starts. Its root search is incomplete, subject to Fourier cancellation and convergence to repeated basins, and proves no zero exclusion. In particular, numerical residuals cannot authenticate the infinitely many zeros needed in Section 4. The exact certificate in Section 2 is logically independent of these experiments.

The concrete next task is to study (23) as a whole under changing \(a\), retaining the actual sample weights (11). Formula (17) gives a computable infinitesimal direction. The elementary multiplier route has been eliminated, so effort should go into a direct order-shift interlacing or spectral argument with a quantitative tail, rather than another finite moment fit.
