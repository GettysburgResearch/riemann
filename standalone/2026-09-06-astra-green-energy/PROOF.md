# Full balanced-source energy as a finite Green form

Status: proposed component proofs; independent mathematical review required.
**RH, the full-dictionary uniform gain, and balanced-source subpower growth
remain unproved.** This is an author continuation of PR #805, not a review
verdict. It preserves the original source, including the coarse component.

Frozen parent: `7919f443c0c2c2a87f95d3237d4fe77fb87f9a74`.
The balanced-lift packet and the intervening growth-transfer packet are both
preserved. The new arguments reconstruct the scalar convolution rather than
assuming its conclusion or importing a zero-free region.

## 0. Source and precise outcome

For real step functions, zero below 1, put
\[
 \|f\|_H^2=\sum_{n\ge1}\frac{f(n)^2}{n(n+1)},\qquad h_k(n)=\{n/k\},\quad h_1=0.
\]
Fix finitely supported real coefficients on odd positive integers, subject to
\[
 \sum_{k\text{ odd}}\lambda_k/k=0.
 \tag{0.1}
\]
Usually these are the exact rational balanced optimum of the parent, also
satisfying \(\lambda_1=1\). Define the ORIGINAL full-source vector
\[
 F[\lambda]=\sum_k\lambda_k(h_{2k}-h_k),\qquad E[\lambda]=\|F[\lambda]\|_H^2.
 \tag{0.2}
\]
Nothing below replaces this norm by the parent's detail norm.

The main identity is a finite, positive Green-energy formula for (0.2).
The rational coefficients give \(E[\lambda]/\pi\) algebraic. Its dimension
is quadratic in the largest source index, not the exponentially large
common period. A tridiagonal inverse and a positive interval-square formula
are explicit. All original cross terms survive inside the interval sums.

For the prescribed balanced optimum, elementary scalar convolution improves
its coefficient and detail bounds to \(O(k/M)\) and \(O(1/M)\). The complete
Green energy outside a single shrinking endpoint has a proved polylogarithmic
bound. The endpoint has not been bounded sufficiently to prove RH. A specific
nonnegative first-interval term already contains a signed Mobius statistic.
This locates, rather than solves, the remaining cancellation problem.

## 1. GE26.1: exact odd primitive, finite spectrum, and parity signs

Write \(M\) for an upper bound on the odd support. Balance cancels the linear
part of the fractional parts:
\[
 F(n)=\sum_k\lambda_k\left(\lfloor n/k\rfloor-\lfloor n/(2k)\rfloor\right).
 \tag{1.1}
\]
With \(d(m)=\sum_{k\mid m}\lambda_k\) on odd \(m\), finite differencing gives
\[
 F(n)=\sum_{\substack{m\le n\\m\text{ odd}}}d(m),\qquad
 F(2j-1)=F(2j).
 \tag{1.2}
\]
Consequently, if \(f(j)=F(2j)\), then
\[
 E=\sum_{j\ge1}\frac{2f(j)^2}{4j^2-1}.
 \tag{1.3}
\]
Indeed the two cell weights telescope to
\(1/(2j-1)-1/(2j+1)=2/(4j^2-1)\). The functions in (0.2) are bounded and
periodic, so all norm sums converge absolutely. Equation (1.1), extended to
integer arguments, also gives \(f(-j)=-f(j)\). For each odd k, divisibility
of \(2j\) by k is equivalent to divisibility by \(2k\), which cancels the
endpoint corrections in the negative-floor identity.

Define the rational-frequency source coefficients
\[
 L_q=\sum_{\substack{k\le M\\k\text{ odd},\ q\mid k}}\frac{\lambda_k}{k}
 \quad(q\text{ odd}),\qquad L_1=0.
 \tag{1.4}
\]
All odd q occur, not just primes or squarefree integers. Finite character
orthogonality and grouping equal reduced frequencies give
\[
 d(2j-1)=\sum_{\substack{3\le q\le M\\q\text{ odd}}}L_q
 \sum_{\substack{1\le a<q\\(a,q)=1}} e^{2\pi i a(2j-1)/q}.
\]
Its primitive with f(0)=0 is
\[
 f(j)=\sum_q L_q\sum_{(a,q)=1}
       \frac{e^{4\pi i aj/q}}{2i\sin(2\pi a/q)}.
 \tag{1.5}
\]
To check both the primitive and its constant, subtract the values at j and
j-1. The difference is exactly the displayed d(2j-1). At j=0, terms for a
and q-a cancel, so the constant is zero. Oddness of q ensures all denominators
are nonzero. No infinite Fourier expansion is used in (1.5).

Let
\[
 \mathcal X_M=\{x=r/q:3\le q\le M\text{ odd},\ 1\le r<q/2,\ (r,q)=1\}.
\]
The reduced fraction determines q and r uniquely. Put
\[
 \sigma_x=(-1)^{r+1}L_q\cot(\pi x),\qquad t_x=\tan(\pi x)>0.
 \tag{1.6}
\]
Then the real sine form of (1.5) is
\[
 \boxed{f(j)=-\sum_{x\in\mathcal X_M}
                  \frac{\sigma_x}{\cos(\pi x)}\sin(2\pi jx).}
 \tag{1.7}
\]
For verification of its sign, choose the inverse of 2 modulo q as
\(a=(r+q\mathbf1_{r\text{ odd}})/2\). Then
\(\sin(2\pi a/q)=(-1)^r\sin(\pi r/q)\). Pair the frequencies r/q and
1-r/q in (1.5). This proves (1.7), including both orientations.

## 2. GE26.2: the complete infinite norm is a finite positive Green form

Order \(\mathcal X_M\) as \(0<x_1<\cdots<x_J<1/2\), set
\(t_i=\tan(\pi x_i)\), \(t_0=0\), and set
\[
 C_\lambda(t)=\sum_{t_i\ge t}\sigma_{x_i}.
 \tag{2.1}
\]
Zero coefficients may be retained as zero charges. There are exactly
\(J=\frac12\sum_{3\le q\le M,\ q\text{ odd}}\varphi(q)\) mesh points.

The exact identity is
\[
 \boxed{E[\lambda]=\frac\pi2\int_0^\infty C_\lambda(t)^2\,dt
 =\frac\pi2\sum_{i=1}^J(t_i-t_{i-1})
                 \left(\sum_{j=i}^J\sigma_{x_j}\right)^2.}
 \tag{2.2}
\]
There is no omitted Gram tail, unpriced complement, or free coarse source.
This integral is a finite step-function integral and stops at t_J.

**Proof.** The elementary absolutely convergent Fourier identity
\[
 \sum_{j\ge1}\frac{2\cos(2\pi ju)}{4j^2-1}
 =1-\frac\pi2|\sin(\pi u)|
 \tag{2.3}
\]
holds periodically in u. For example, integrate \(\sin(\pi u)\) against the
cosines on [0,1]: its mean is 2/pi and its j-th cosine coefficient is
\(-4/[\pi(4j^2-1)]\). The resulting absolutely convergent Fourier series
identifies the continuous function, proving (2.3).
For 0<x,y<1/2, product-to-sum gives
\[
 \sum_{j\ge1}\frac{2\sin(2\pi jx)\sin(2\pi jy)}{4j^2-1}
 =\frac\pi2\sin(\pi\min(x,y))\cos(\pi\max(x,y)).
 \tag{2.4}
\]
The right side divided by \(\cos(\pi x)\cos(\pi y)\) is
\((\pi/2)\min(\tan(\pi x),\tan(\pi y))\).
Substitute the FINITE sine sum (1.7) in (1.3), apply (2.4), and use
\(\min(t_i,t_j)=\int_0^\infty\mathbf1_{t\le t_i}\mathbf1_{t\le t_j}\,dt\).
This proves (2.2). Absolute convergence of (2.4) and finiteness of the source
justify every interchange. End of proof.

The kernel in (2.4) is the Dirichlet Green kernel of a shifted second-order
operator on (0,1/2), up to its displayed normalization. Equivalently the
min(t_i,t_j) matrix is the standard one-dimensional Green covariance after
the tangent change of variables. These are classical facts, not a new
positivity principle for zeta.

For rational lambda, every t_i and sigma_i is algebraic, since sines and
cosines at rational multiples of pi are algebraic and their denominators
here are nonzero. Therefore E/pi is algebraic. This is a statement about
these exactly balanced parity vectors. It does NOT say that the general
Nyman--Beurling Gram or its target pairing is algebraic. Target pairings can
still contain logarithms.

## 3. GE26.3: a local inverse and source reconstruction

Let \(K_{ij}=\min(t_i,t_j)\) and \(d_i=t_i-t_{i-1}>0\). If B is unit
lower triangular with all entries on/below its diagonal equal to 1, then
\[
 K=B\operatorname{diag}(d_i)B^T.
\]
Thus its inverse is tridiagonal:
\[
 (K^{-1})_{ii}=d_i^{-1}+d_{i+1}^{-1}\ (i<J),\quad
 (K^{-1})_{JJ}=d_J^{-1},\quad
 (K^{-1})_{i,i+1}=-(d_{i+1})^{-1}.
 \tag{3.1}
\]
The remaining entries vanish. This follows by writing B^{-1} as the first
backward-difference matrix. It is a finite positive-definite matrix identity,
not an inverse of a compact infinite-dimensional operator.

Also all original coefficients can be recovered from the frequency source:
\[
 \frac{\lambda_k}{k}=\sum_{\substack{m\le M/k\\m\text{ odd}}}\mu(m)L_{km},
 \qquad k\text{ odd},
 \tag{3.2}
\]
with L_1=0. This is finite Mobius inversion on the multiples poset. In
particular the nonsquarefree coefficient lambda_9 is not lost in the
cotangent representation. Reading each L_q from sigma_{1/q} is possible,
as cot(pi/q) is nonzero. Thus the transformation is injective on the balanced
source space. Locality of (3.1) is in frequency order, not in the integer
source indices. The latter remain coupled through the map (1.4).

At M=4 the balanced coefficients are lambda_1=1, lambda_3=-3. There is one
frequency, x=1/3, with L_3=-1 and sigma=-1/sqrt(3). Equation (2.2) gives
\[
 \boxed{E_4=\frac{\pi}{2\sqrt3}.}
 \tag{3.3}
\]
This illustrates the exact algebraic norm. It is not an all-scale estimate.

## 4. GE26.4: sharper genuine-source coefficient and detail bounds

Use the exact rational balanced coefficients from the parent:
\[
 S=\sum_{d\le M,\ d\text{ odd}}\frac{\mu(d)^2}{J_2(d)},\quad
 A=\sum_{d\le M,\ d\text{ odd}}\frac{\mu(d)\varphi(d)}{J_2(d)},\quad
 D=\sum_{d\le M,\ d\text{ odd}}\frac{\varphi(d)^2}{J_2(d)},\quad K=SD-A^2,
\]
\[
 v_k=k^2\sum_{km\le M,\ m\text{ odd}}\frac{\mu(m)\mu(km)}{J_2(km)},\quad
 w_k=k^2\sum_{km\le M,\ m\text{ odd}}\frac{\mu(m)\varphi(km)}{J_2(km)},\quad
 \lambda_{k,M}=(Dv_k-Aw_k)/K.
 \tag{4.1}
\]
For M>=3, K>0, lambda_1=1 and sum lambda_k/k=0, by the parent divisor-matrix
proof; these finite identities are reconstructed by the accompanying checker.
Let eta_M denote their constrained DETAIL error, not their full energy.
Then the improved all-scale estimates are
\[
 \boxed{|\lambda_{k,M}-\mu(k)|<72k/M,\qquad
          0<\eta_M<18/M\quad(M\ge128).}
 \tag{4.2}
\]
These remove the logarithmic factors in the earlier elementary bounds.
No PNT or RH is used.

**Scalar convolution proof.** Put S_infty=pi^2/8 and c=1/S_infty. Let
\(m(N)=\sum_{n\le N}\mu(n)/n\). Since
\(\sum_{n\le N}\mu(n)\lfloor N/n\rfloor=1\),
\[
 Nm(N)=1+\sum_{n=2}^N\mu(n)\{N/n\},\qquad |m(N)|\le1.
\]
Separating powers of 2 gives, exactly,
\[
 m_o(N):=\sum_{n\le N,\ n\text{ odd}}\mu(n)/n
 =\sum_{2^j\le N}2^{-j}m(\lfloor N/2^j\rfloor),\quad |m_o(N)|\le2.
 \tag{4.3}
\]
For fixed odd k set psi(k)=k product_{p|k}(1+1/p). Then
\[
 w_k=\frac{k^2}{\psi(k)}
 \sum_{\substack{m\le M/k\\m\text{ odd}}}
  \frac{\mu(m)}{m\prod_{p\mid m,\ p\nmid k}(1+1/p)}.
\]
The coefficient inside the sum is the Dirichlet convolution of mu(m)/m
on odd integers with a NONNEGATIVE multiplicative sequence u_k. For odd
p not dividing k its local terms are
\[
 u_k(p^a)=\frac{p^{-a}}{p+1}\quad(a\ge1);
\]
for p dividing k those terms vanish. This follows by dividing the local
series \(1-X/(p+1)\) by \(1-X/p\). Moreover
\[
 \sum_n u_k(n)\le\prod_{p\text{ odd}}(1+1/(p^2-1))=S_\infty.
\]
The product is absolutely convergent. Applying (4.3) to the FINITE summatory
convolution yields
\[
 \boxed{|w_k|\le2S_\infty k,\qquad |A|=|w_1|\le2S_\infty<5/2.}
 \tag{4.4}
\]
This is a bounded harmonic Mobius sum, not a square-root Mertens estimate.
The related scalar idea occurs in the sibling growth-transfer packet; it is
reconstructed here for the k-dependent normalization correction.

Here are the remaining constants in (4.2). The elementary product inequality
\(\varphi(n)^2/J_2(n)\ge1-\sum_{p\mid n}2/(p+1)\), followed by counting odd
multiples, gives
\[
 D\ge(1-\log2)M-\tfrac12 H_{\lfloor(M+1)/2\rfloor}\ge M/5\quad(M\ge32).
 \tag{4.5}
\]
For the last step use log 2<7/10 and check the increasing difference at 32.
The unconstrained detail optimizer is a*=cv, with detail error
\(e_M=(c/2)\sum_{d>M,\ d\text{ odd}}\mu(d)^2/J_2(d)\le1/(2M)\).
Its coefficient estimate, by completing its absolutely convergent Euler
product and bounding the omitted 1/m^2 tail, is
\[
 |a_k^*-\mu(k)|\le 2S_\infty k/M<5k/(2M).
\]
At nonsquarefree k both a*_k and mu(k) are zero.
Put bar(a)=c(v-(A/D)w) and bar(e)=e_M+(c/2)A^2/D. Direct quadratic
minimization gives
\[
 \bar a_1=1-2\bar e,\quad \lambda=\bar a/\bar a_1,\quad
 \eta_M=\bar e/(1-2\bar e).
\]
Equations (4.4)--(4.5) give bar(e)<13/M, so bar(a)_1>3/4 when M>=128 and
eta_M<18/M. Also
\[
 |\bar a_k-\mu(k)|<(5/2+25)k/M,\quad 1-\bar a_1<26/M.
\]
Dividing by bar(a)_1 gives
\((4/3)((55/2)k+26)/M\le(214/3)k/M<72k/M\), proving (4.2).

In particular
\[
 B_M:=\sum_{k\le M,\ k\text{ odd}}|\lambda_{k,M}|/k<38+\log M
 \quad(M\ge128).
 \tag{4.6}
\]
This follows from (4.2), sum_{k<=M}1/k<=1+log M, and at most (M+1)/2
odd indices. Also \(\sum|\lambda_k|/k^2<5\) for M>=128, since this sum
is at most \(S_\infty+72(1+\log M)/M\), the last ratio is decreasing,
and log 128<5.

## 5. GE26.5: complete energy away from the reciprocal endpoint is controlled

For ANY finite balanced odd source and tau>0,
\[
 \boxed{E_{\ge\tau}[\lambda]:=\frac\pi2\int_\tau^\infty C_\lambda(t)^2dt
       \le\frac{\pi}{2\tau}\left(\sum_k|\lambda_k|/k\right)^2.}
 \tag{5.1}
\]

**Proof.** Expand L_q in (2.1) and group its multiples BEFORE estimating.
Because k and every divisor k/q are odd, reducing r/k to a/q preserves the
parity of its numerator. Thus for 0<x<1/2,
\[
 C_\lambda(\tan(\pi x))=
 \sum_{k\text{ odd}}\frac{\lambda_k}{k}
 \sum_{\substack{1\le r<k/2\\r/k\ge x}}(-1)^{r+1}\cot(\pi r/k).
 \tag{5.2}
\]
For a fixed k, the inner sum is a consecutive alternating sum of positive
decreasing terms. Its absolute value is at most its first term, hence at
most cot(pi x). Empty sums contribute zero. Therefore
\(|C_\lambda(t)|\le B_M/t\), which integrates to (5.1). End of proof.

For the actual rational balanced optimum, take
\(\tau_M=1/\log(2M)\). Equations (4.6) and (5.1) prove
\[
 \boxed{0\le E_M-E_{<\tau_M,M}
 \le\tfrac\pi2\log(2M)(38+\log M)^2=O(\log^3 M).}
 \tag{5.3}
\]
This controls the ENTIRE complementary Green spectrum, including all source
cross terms, not just finitely many sampled angles. The variable is reciprocal
rational frequency, not the original physical variable or a zero ordinate.

The remaining E_{<tau_M,M} is itself an exact finite interval-square sum:
replace each interval length t_i-t_{i-1} in (2.2) by
\(\min(t_i,\tau_M)-\min(t_{i-1},\tau_M)\).
In particular subpower growth of E_M is equivalent to subpower growth of
this single endpoint energy. The analogous liminf-exponent statements are
also equivalent because the complementary bound is polylogarithmic.
**Neither subpower statement is proved here.**

For comparison an elementary complete-source bound with no logarithmic
factor is \(E_M<50000M\) for M>=128. In the ambient norm
L^2((0,infinity),dt/t^2), let e(t)={t}, so ||e||<=sqrt(2) and
||D_k||=k^(-1/2). Balance gives F=(D_2-I)sum lambda_k D_ke. Therefore
\[
 \|F\|<3\sum|\lambda_k|/\sqrt k\le222\sqrt M.
\]
Use (4.2), sum k^(-1/2)<=2sqrt(M), and sum sqrt(k)<=M sqrt(M).
This coarse bound is not a new power saving or a zero-free-region result.

## 6. GE26.6: one nonnegative interval already contains signed arithmetic

Define
\[
 a(k)=\sum_{1\le r<k/2}(-1)^{r+1}\cot(\pi r/k),\quad a(1)=0.
\]
For every odd k>=1,
\[
 \boxed{a(k)=\frac{k\log2}{\pi}-\epsilon_k,\quad
 0<\epsilon_k<\frac{\pi}{12k}.}
 \tag{6.1}
\]

**Proof.** The cotangent reflection integral gives
\[
 \pi\cot(\pi r/k)=k\int_0^\infty
   \frac{e^{-ru}-e^{-(k-r)u}}{1-e^{-ku}}du.
\]
It follows, for example, by subtracting the standard digamma integrals and
using reflection. The difference is integrable at both ends. Pair r and k-r,
sum the FINITE geometric progression, and obtain
\[
 a(k)=\frac{k}{\pi}\left[\log2-
        \int_0^\infty\frac{\tanh(u/2)}{e^{ku}-1}du\right].
\]
Equivalently \(\epsilon_k=\pi^{-1}\int_0^\infty
\tanh(v/(2k))/(e^v-1)dv\). Positivity and tanh(y)<y give (6.1), since
\(\int_0^\infty v/(e^v-1)dv=\sum_{n\ge1}n^{-2}=\pi^2/6\).
At k=1 the same formula gives a(1)=0; no fictitious frequency is added.
End of proof.

Let \(T_M=\sum_{k\le M,\ k\text{ odd}}\lambda_{k,M}\). The endpoint value is
\[
 C_M(0)=\sum_k\lambda_k a(k)/k,
 \qquad |C_M(0)-(\log2/\pi)T_M|<2\quad(M\ge128),
 \tag{6.2}
\]
by (6.1) and sum |lambda_k|/k^2<5. No rational frequency precedes 1/M;
therefore C_M is exactly constant on 0<t<tan(pi/M). This is an actually
present nonnegative summand, and gives
\[
 \boxed{E_M\ge\frac1{2M}
              [\,\log2\,|T_M|-2\pi\,]_+^2.}
 \tag{6.3}
\]
Use tan(pi/M)>=pi/M and (6.2). The total coefficient has the exact finite
formula
\[
 \boxed{T_M=\frac{D_M\,M_o(M)-A_M\,\Phi_o(M)}{S_MD_M-A_M^2},\quad
 M_o(M)=\sum_{n\le M,n\text{ odd}}\mu(n),\quad
 \Phi_o(M)=\sum_{n\le M,n\text{ odd}}\varphi(n).}
 \tag{6.4}
\]
Indeed summing v_k or w_k in (4.1) and using
sum_{k|d} k^2 mu(d/k)=J_2(d) gives M_o or Phi_o respectively.

An E_M=M^{o(1)} upper bound would in particular give
|T_M|<=M^{1/2+o(1)}. No such bound is proved for (6.4). The bounded harmonic
statistic A_M does not supply square-root cancellation of its combination
with M_o(M). Likewise controlling this first interval alone would not bound
the other interval squares. We do not infer RH-equivalence for the scalar
condition on T_M by silently discarding those intervals.

## 7. GE26.7: hypothetical off-line growth is forced into this endpoint

The fixed source construction is independent of hypothetical zeros. The
parent Mellin argument is reconstructed with the improved constants:
\[
 |F_M(n)-1|\le72n^2/M\quad(1\le n\le M,\ M\ge128).
 \tag{7.1}
\]
Insert (4.2) in the finite primitive (1.2) and use odd Mobius inversion;
\(\sum_{k\le n}(n/k)k\le n^2\). At noninteger t replace n by floor(t),
which can only enlarge the right side when written as 72t^2/M.

For \(P_M(s)=\sum\lambda_{k,M}k^{-s}\), balance gives P_M(1)=0 and
\[
 \int_1^\infty F_M(t)t^{-s-1}dt
 =\frac{(1-2^{-s})\zeta(s)P_M(s)}s\quad(\Re s>0).
 \tag{7.2}
\]
First prove it from the finite primitive when Re(s)>1. Both sides continue
holomorphically to Re(s)>0, with the pole at 1 removed exactly. The left side
converges there because F_M is bounded and periodic.

If zeta(rho)=0, beta=Re(rho)>1/2, choose 0<a<1/(2-beta), and put x=M^a.
Here a<1 because beta<1. Equation (7.1) bounds the local Mellin error by
\(72x^{2-\beta}/[(2-\beta)M]=o(1)\). Thus the integral over [1,x] tends
to 1/rho, while the full integral is zero. Cauchy--Schwarz for the remaining
tail implies, for sufficiently large M,
\[
 E_M\ge\frac{2\beta-1}{4|\rho|^2}M^{a(2\beta-1)}.
\]
Letting a approach 1/(2-beta) proves
\[
 \boxed{\liminf_{M\to\infty}\frac{\log(1+E_M)}{\log M}
       \ge q_\beta:=\frac{2\beta-1}{2-\beta}>0.}
 \tag{7.3}
\]
No simplicity or numerical zero information is required. Combining (7.3)
with the complete complementary bound (5.3) gives the SAME lower exponent
for the endpoint energy E_{<1/log(2M),M}. More quantitatively, for any fixed
0<eps<q_beta, it also holds for E_{<M^{-eps},M}: choose a with
 eps<a(2beta-1)<q_beta and subtract the bound O(M^eps log^2 M) from (5.1).
Take a to the endpoint afterward. Each choice remains fixed before M grows.

Consequently subpower endpoint energy, or just zero liminf of its logarithmic
growth exponent, would imply RH by symmetry of the nontrivial zeros. The
proved polylogarithmic complement is NOT such an endpoint estimate.

## 8. Attempt at completion and the remaining signed estimate

The original unbounded gain assertion has not been proved. This pass attacks
the explicitly balanced family instead. Three steps are now exact or bounded:

1. The full coarse-plus-detail norm becomes (2.2), with an explicit local
   inverse and no infinite numerical Gram tail.
2. The normalization correction has a bounded positive-convolution majorant,
   yielding all-scale coefficient and detail improvements (4.2).
3. Grouping all unreduced source frequencies preserves the alternating
   arithmetic and proves the full polylogarithmic complement (5.3).

The remaining closure target is, for the literal coefficients (4.1),
\[
 \boxed{\frac\pi2\int_0^{1/\log(2M)}
 \left[\sum_{\substack{q\le M\text{ odd}\\1\le r<q/2,(r,q)=1\\
                 \tan(\pi r/q)\ge t}}
 (-1)^{r+1}\cot(\pi r/q)
 \sum_{\substack{k\le M\text{ odd}\\q\mid k}}\frac{\lambda_{k,M}}k
 \right]^2dt=M^{o(1)}.}
 \tag{GE26.OPEN}
\]
Even a sequence with zero liminf logarithmic exponent would suffice. Every
sum is finite and its breakpoints are predetermined algebraic numbers.

Taking absolute values after the alternating inner sum bounds |C(t)| by
B_M/t. This closes the complementary range but gives power cost near its
first breakpoint, t of order 1/M. Equation (6.4) identifies a literal signed
statistic already present there. Applying generic positive-definite-matrix
bounds, replacing signed tails by sums of squares, or independently bounding
all L_q does not give GE26.OPEN. Positivity of (2.2) is an identity for every
balanced source, including hostile sources in the preceding packet; it is
not a positivity mechanism peculiar to zeta.

Partial cotangent reciprocity and Mobius exponential-sum estimates are
relevant possible inputs. The literature check located them but did not
produce a uniform bound for this complete coupled endpoint current. No
unverified range extension or family-to-individual inference is used.

The bounded reconstructions at M=4,8,16 agree with the earlier independent
infinite-Gram intervals, and the finite formula also evaluates M=32. The
unbounded assertions are proved analytically above; the four fixed values
are not evidence of a uniform norm ceiling. Mathematical and code review
remain required; no Lean build, cofinal gain, or RH proof is claimed.
