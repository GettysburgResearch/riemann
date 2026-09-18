# Spectral obstructions and an explicit logarithmic mollifier

Date: 2026-09-17.
Status: deductions and sufficient conditions; no RH proof, no new unconditional
zero-free region, and no priority claim. The finite identity checks are not
numerical evidence for the unproved asymptotic estimate.

## 1. Space, zero kernels, and the proposed synthesis statement

Let H be the complex sequence Hilbert space with inner product linear in the
first argument,

\[
\langle f,g\rangle=\sum_{k\ge1}\frac{f(k)\overline{g(k)}}{k(k+1)}.
\]

Put b_n(k)={k/n}, n>=2, B=closed span of the b_n. Define

\[
\mathcal T f(s)=\sum_{k\ge1}f(k)(k^{-s}-(k+1)^{-s}),\qquad \Re s>1/2.
\]

This is analytic in the indicated half-plane, by Cauchy--Schwarz or the step
function Mellin transform. Its evaluation kernels are

\[
h_z(k)=k(k+1)(k^{-\bar z}-(k+1)^{-\bar z}).
\]

They satisfy <1,h_z>=1 and

\[
\langle b_n,h_z\rangle=\zeta(z)(1/n-n^{-z}).
\]

For a zero rho of multiplicity m_rho, the vectors
h_{rho,j}=partial_{bar z}^j h_z evaluated at rho, 0<=j<m_rho, all lie in B^perp.
Their scalar products with f are (T f)^(j)(rho). Hence, if Z is their closed span,

\[
Z\subseteq B^\perp,\qquad
Z^\perp=\{f\in H:(\mathcal T f)/\zeta\text{ is holomorphic on }\Re s>1/2\}.
\]

The proposed full characterization is B^perp=Z, equivalently B=Z^perp.
The discrete divisibility-to-approximability converse is the substance of
Question 2 in Balazard [1], after restricting to his D_0 sequence space.
The sources checked here do not establish this converse. It must not be
inferred from holomorphic division alone. Multiplicity derivatives and closure
are essential in the statement. NB--Baez-Duarte theory already gives
RH iff 1 belongs to B, so the equivalence between a positive limiting distance
and an off-line zero does not require this stronger synthesis theorem.

## 2. Explicit coefficients and exact divisor-sum formula

For integer N>=2 define

\[
c_{N,n}=-\mu(n)\left(1-\frac{\log n}{\log N}\right),\quad 2\le n\le N,
\qquad U_N=\sum_{n=2}^N c_{N,n}b_n,
\qquad u_N=1-U_N,\quad Q_N=\|u_N\|^2.
\]

These are prescribed coefficients, NOT the optimal projection coefficients.
The associated Dirichlet polynomial is

\[
V_N(s)=\sum_{n\le N}\mu(n)\left(1-\frac{\log n}{\log N}\right)n^{-s},
\qquad P_N(s)=V_N(s)-V_N(1).
\]

P_N(1)=0 and T U_N(s)=zeta(s)P_N(s). Logarithmic mollifiers V_N are classical;
[3] proves a sharp asymptotic assuming RH and an additional reciprocal-derivative
hypothesis. That conditional estimate is NOT used below.

Define

\[
\Lambda_N(m)=\sum_{d\mid m,\ d\le N}\mu(d)\log(N/d),\qquad
T_N=\sum_{d\le N}\frac{\mu(d)}d\log(N/d),\qquad
\Psi_N(k)=\sum_{m\le k}\Lambda_N(m).
\]

Expanding the floor function proves, for every integer k>=1,

\[
U_N(k)=\frac{\Psi_N(k)-kT_N}{\log N},\qquad
u_N(k)=\frac{\log N+kT_N-\Psi_N(k)}{\log N}.
\]

For 1<=k<=N, Mobius inversion gives

\[
\Psi_N(k)=\log N+\psi(k),\qquad
u_N(k)=\frac{kT_N-\psi(k)}{\log N},
\]

where psi(k)=sum_{m<=k} Lambda(m) is Chebyshev's prime-power sum. The truncated
Lambda_N is the divisor sum used in Goldston--Yildirim [4].

### Elementary bound on T_N

Let m(N)=sum_{d<=N}mu(d)/d. The identity
sum_{d<=N}mu(d)floor(N/d)=1 gives |m(N)|<=1+1/N<=2.
Furthermore,

\[
1=\sum_{d\le N}\frac{\mu(d)}d H_{\lfloor N/d\rfloor}.
\]

For y>=1, |H_floor(y)-log y-gamma|<=2/y. Therefore
1=T_N+gamma m(N)+R_N with |R_N|<=2, whence |T_N|<5.
Chebyshev's elementary estimate psi(k)<=4(log 2)k<3k follows by bounding
psi(2m)-psi(m) by log binomial(2m,m), summing at powers of two, and monotonicity.
Thus

\[
|u_N(k)|\le \frac{8k}{\log N},\qquad 1\le k\le N.
\]

In particular u_N(k)->0 for each fixed k, without using RH or even the PNT.
For J_N=floor(log N),

\[
\|u_N\,1_{k\le J_N}\|^2\le \frac{64}{\log N}.
\]

## 3. A zero forces logarithmic growth of this explicit error

Suppose rho=beta+i gamma is a zero with delta=beta-1/2>0.
By Cauchy--Schwarz on each interval [k,k+1],

\[
\|h_\rho\,1_{k>J}\|^2
\le \frac{|\rho|^2}{2\delta}(J+1)^{-2\delta}.
\]

Since <U_N,h_rho>=0, <u_N,h_rho>=1. The preceding head estimate gives

\[
|\langle u_N1_{k\le J_N},h_\rho\rangle|
\le \frac{8\|h_\rho\|}{\sqrt{\log N}}\longrightarrow0.
\]

It follows that

\[
Q_N\ge \frac{2\delta}{|\rho|^2}(1-o(1))(J_N+1)^{2\delta}.
\]

In particular, for all sufficiently large N (depending on rho),

\[
\boxed{Q_N\ge \frac{\delta}{2|\rho|^2}(\log N)^{2\delta}.}
\]

The explicit sufficient threshold obtained from the crude head bound is
log N >=128 |rho|^2/delta, apart from immaterial small-N restrictions. The
asymptotic mechanism is therefore not a practical high-zero detection method.

Consequently, a bound

\[
\forall\eta>0\quad Q_N\ll_\eta (\log N)^\eta
\]

would prove RH. A fixed power of log log N is already sufficient. This is
an implication, not an unconditional assertion of that upper bound.
It uses the individual zero kernels and does NOT require full spectral synthesis.

## 4. A stronger growth criterion from averaging over the length

The following implication is proved here as a deduction, without a priority
claim. It is a shifted-Mobius/Hardy-space argument in the established
Nyman--Beurling setting (compare [7]).

**Growth lemma.** Let alpha>=0. If the prescribed errors satisfy
Q_N=O(N^(2 alpha)) for all integer N>=2, then zeta has no zero with
real part greater than 1/2+alpha.

Extend the coefficients to real x>1 using the same formula, with U_x=0 for
1<x<2. If N<=x<N+1, then

\[
(\log x)U_x=(\log N)U_N+
\log(x/N)\left(-\sum_{n=2}^N\mu(n)b_n\right).
\]

Since ||b_n||<=sqrt(2/n), the second term has norm O(N^(-1/2)).
Thus the assumed integer bound gives ||U_x||=O(x^alpha) for real x>=2.
For every real a>alpha the Hilbert-space integral

\[
F_a=\int_1^\infty (\log x)U_x\,x^{-a-1}\,dx
\]

converges in norm. In particular T F_a is holomorphic on Re s>1/2.
For Re s>1, scalar absolute convergence permits interchanging the sums
and integrals. Using

\[
\int_n^\infty\log(x/n)x^{-a-1}dx=\frac{n^{-a}}{a^2}
\]

and the Euler product in its absolute-convergence half-plane gives

\[
\boxed{
\mathcal T F_a(s)=\frac{\zeta(s)}{a^2}
\left(\frac1{\zeta(s+a)}-\frac1{\zeta(1+a)}\right).
}
\]

Both sides continue meromorphically to Re s>1/2, while the left side is
holomorphic there. The apparent singularity at s=1 on the right is removable,
because the bracket vanishes at s=1.

Suppose rho is a zero with beta=Re rho>1/2+alpha. Choose
alpha<a<beta-1/2 such that zeta(rho-a) is nonzero. Such choices exist because
zeros are isolated; the excluded shifts are discrete in this interval.
At s=rho-a the right side then has a genuine pole, whereas the left side is
holomorphic. This contradiction proves the growth lemma. Multiplicity does
not alter the argument.

Consequently,

\[
\boxed{
[\ \forall\varepsilon>0:\ Q_N\ll_\varepsilon N^\varepsilon\ ]
\quad\Longrightarrow\quad\mathrm{RH}.
}
\]

The upper bound is NOT proved. It is much less restrictive than a bounded
error, error tending to zero, or a subpower of log N. For example,
Q_N=O(exp(C sqrt(log N))) for one fixed C would suffice.
The length-averaging argument needs control over all sufficiently large N;
it does not justify using only a sparse unbounded sequence of good lengths.

Equivalently, a zero rho=1/2+delta+i gamma implies

\[
\limsup_{N\to\infty}\frac{\log(1+Q_N)}{\log N}\ge2\delta.
\]

This is a subsequence polynomial-growth obstruction, not a polynomial lower
bound for every sufficiently large N. Section 3 gives the weaker logarithmic
lower bound for every sufficiently large N.

## 5. The explicit coefficients give a direct cutoff at N squared

For this prescribed family we do not need the earlier optimal-residual tail
theorem, or a large-sieve absorption argument. Directly,

\[
\sum_{n=2}^N|c_{N,n}|
\le\frac1{\log N}\sum_{n=2}^N\log(N/n)
\le\frac{N}{\log N}.
\]

Thus |u_N(k)|<=1+N/log N for every integer k. Since the weights telescope,
for every K>=1,

\[
0\le Q_N-\sum_{k\le K}\frac{|u_N(k)|^2}{k(k+1)}
\le\frac{(1+N/\log N)^2}{K+1}.
\]

At K=N^2 this gives the unconditional estimate

\[
\boxed{
0\le Q_N-\sum_{k\le N^2}\frac{|u_N(k)|^2}{k(k+1)}
\le\frac4{(\log N)^2}.
}
\]

This is stronger and simpler for this family than applying the previous
N^2(log N)^5 cutoff, which was designed for unknown optimal coefficients.

## 6. One explicit sufficient arithmetic estimate

Put

\[
R_N=\sum_{k\le N^2}
\frac{|\Psi_N(k)-kT_N-\log N|^2}{k(k+1)}.
\]

The proved tail bound states

\[
\frac{R_N}{(\log N)^2}\le Q_N
\le\frac{R_N+4}{(\log N)^2}.
\]

Therefore the following single estimate, for example, would imply RH:

\[
\boxed{
R_N\ll (\log N)^2\exp(C\sqrt{\log N})
\quad\text{for some fixed }C\text{ and all sufficiently large }N.
}
\]

This is an UNPROVED target. More generally,
R_N <<_epsilon (log N)^2 N^epsilon for every epsilon>0 would suffice.
The earlier, stronger target (log N)^2(log log N)^C also suffices; the length
averaging lemma shows that such tight logarithmic control is unnecessary.

To expose the correlation kernel, set

\[
a_N(m)=\Lambda_N(m)-T_N-(\log N)1_{m=1}.
\]

The numerator above is |sum_{m<=k}a_N(m)|^2. Finite rearrangement gives

\[
\sum_{k\le K}\frac{|\sum_{m\le k}a_N(m)|^2}{k(k+1)}
=
\sum_{a,b\le K}a_N(a)a_N(b)
\left(\frac1{\max(a,b)}-\frac1{K+1}\right).
\]

This is an anchored cumulative-discrepancy estimate. Controlling the ordinary
second moment of Lambda_N alone does not control this kernel at the needed
scale. Treating centered increments as independent introduces an unproved
assumption. The Goldston--Yildirim correlation results provide relevant arithmetic
structure, but no theorem checked here supplies the required uniform target.

An elementary bound actually proved here is only Q_N << N/(log N)^2:
||b_n||^2<=2/n and
sum_{n=2}^N n^(-1/2)log(N/n)<=4 sqrt(N) give
||U_N||<=4 sqrt(2N)/log N. Thus
Q_N<=(1+4sqrt(2N)/log N)^2. This is not asserted to be the best literature
bound. In the growth lemma it reaches only alpha=1/2 and hence the already
known zero-free half-plane Re s>1; it establishes no new zero-free region.

## 7. Interpretation

The optimal errors E_N can approach a positive floor if RH fails; the
prescribed Mobius mollifier behaves differently. It converges locally to 1
regardless of RH. Exact orthogonality to an off-line-zero kernel forces its
remaining energy to move to larger k and grow. Averaging over the length
turns this into a stronger polynomial-growth obstruction.

This combines the two proposed paths without first proving that all of
B^perp is synthesized from zero kernels. Neither full synthesis nor the
required subpolynomial upper bound is proved in this note.

## Sources

[1] M. Balazard, An arithmetical function related to Baez-Duarte's criterion
for the Riemann hypothesis, 2018. Proposition 10, Proposition 11, Question 2.
https://arxiv.org/abs/1812.04309

[2] F. Calderaro, J. Manzur, W. Noor, C. Santos, Orthogonality questions in
the Hardy space related to zeta-zeros, version 4 (2024).
https://arxiv.org/abs/2203.05030

[3] S. Bettin, J. B. Conrey, D. W. Farmer, An optimal choice of Dirichlet
polynomials for the Nyman--Beurling criterion.
https://arxiv.org/abs/1211.5191

[4] D. A. Goldston, C. Y. Yildirim, Higher correlations of divisor sums
related to primes I: triple correlations.
https://arxiv.org/abs/math/0111212

[5] L. Baez-Duarte, A strengthening of the Nyman--Beurling criterion for
the Riemann Hypothesis.
https://arxiv.org/abs/math/0202141

[6] Earlier conversation research note, RH arithmetic follow-up: exact
obstructions, tail localization, and certificates, 2026-09-17, sections 3--4.
It is a research derivation, not an independently published theorem.


[7] J.-F. Burnol, On an analytic estimate in the theory of the Riemann Zeta
function and a Theorem of Baez-Duarte, 2002/2003.
https://arxiv.org/abs/math/0202166
