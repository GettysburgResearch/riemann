# Reflection, GCD positivity, and the prime-power source

Date: 2026-09-18.

**Status.** Unconditional deductions and a proved separation between two norms.
No proof of RH, no new zero-free region, and no priority claim. The accompanying
program checks finite identities using exact rational arithmetic. It is not
an RH computation. The two metrics below must not be interchanged.

## 1. Setting

Let H be the sequence Hilbert space

\[
 \langle f,g\rangle_H=\sum_{k\ge1}\frac{f(k)\overline{g(k)}}{k(k+1)},
 \qquad b_n(k)=\{k/n\},\quad b_1=0.
\]

The inner product is linear in its first argument. Write
B_N=span(b_2,...,b_N), B=closure of their union, and
E_N=dist_H(1,B_N)^2. The discrete Nyman--Beurling--Baez-Duarte criterion
identifies E_N -> 0 with RH [1].

The evaluation transform and kernels are

\[
 Tf(s)=\sum_{k\ge1}f(k)(k^{-s}-(k+1)^{-s}),
 \qquad
 h_z(k)=k(k+1)(k^{-\bar z}-(k+1)^{-\bar z}).
\]

For Re z>1/2, h_z belongs to H, <f,h_z>=Tf(z), and

\[
 \langle1,h_z\rangle=1,
 \qquad \langle b_n,h_z\rangle=\zeta(z)(n^{-1}-n^{-z}).
\]

These follow by telescoping and the floor-function Mellin identity. At a
right-side zero rho, h_rho belongs to B-perp.

## 2. Reflection is not a bounded duality in this space

### 2.1 Exact dilation operators

Extend every sequence by f(0)=0 and define

\[
 (D_mf)(k)=f(\lfloor k/m\rfloor),\qquad m\ge2.
\]

Grouping k=mq,...,m(q+1)-1 gives exactly

\[
 \|D_mf\|_H^2=\frac1m\|f\|_H^2.
\]

Also

\[
 D_mb_n=b_{mn}-\frac1n b_m.
\]

Thus B is D_m-invariant, and B-perp is D_m^*-invariant. The operators
C_m=sqrt(m) D_m^* restricted to B-perp are contractions.

The transform identity T(D_mf)(s)=m^{-s}Tf(s) yields

\[
 C_mh_\rho=m^{1/2-\bar\rho}h_\rho.
\]

For rho=1/2+delta+i gamma, delta>0, the eigenvalue has modulus m^{-delta}<1.
If the reflected zero rho*=1-bar(rho) supplied a kernel in the same space,
its eigenvalue would have modulus m^{delta}>1, contradicting contractivity.
But it does not supply such a vector.

### 2.2 The reflected functional is unbounded

For fixed z != 0,

\[
 h_z(k)=\bar z\,k^{1-\bar z}(1+O_z(k^{-1})).
\]

Consequently, for rho*=1/2-delta+i gamma,

\[
 \sum_{k\le K}\frac{|h_{\rho^*}(k)|^2}{k(k+1)}
 \sim\frac{|\rho^*|^2}{2\delta}K^{2\delta}.
\]

The putative reflected evaluation is therefore unbounded on H. Its value on
each b_n still exists (the associated series is absolutely convergent for
Re z>0), and functional-equation reflection correctly gives another zero.
What is invalid is extending that operation to a bounded symmetry on the
completed defect space.

Completed test functions of the form xi(s)A(s) reflect to xi(s)A(1-s).
The common xi factor is preserved, not contradicted. The functional equation
[2] alone does not supply the additional defect-space duality.

A rigidity proof could still try to construct a bounded defect-space duality
forcing reciprocal-conjugate dilation eigenvalues. Such a construction is NOT
established here. Treating it as an automatic consequence of xi(s)=xi(1-s)
would skip the load-bearing step.

## 3. An exact arithmetic basis: cumulative Ramanujan sums

For d>=2 put

\[
 s_d(k)=\sum_{n\mid d}\mu(d/n)\,n b_n(k).
\]

Mobius inversion gives

\[
 nb_n=\sum_{d\mid n,d\ge2}s_d.
\]

Thus the first N atoms span exactly B_N; no approximation is involved.

If c_d(j) denotes the Ramanujan sum

\[
 c_d(j)=\sum_{\substack{a\bmod d\\(a,d)=1}}e^{2\pi iaj/d}
       =\sum_{n\mid(d,j)}n\mu(d/n),
\]

then s_d(0)=0 and

\[
 s_d(k)-s_d(k-1)=-c_d(k),
 \qquad s_d(k)=-\sum_{j=1}^k c_d(j).
\]

### 3.1 Periodic covariance diagonalizes

Let M denote uniform average over a common period. Direct residue averaging
gives

\[
 M(b_n)=\frac{n-1}{2n},\qquad
 \operatorname{Cov}_M(b_m,b_n)=\frac{\gcd(m,n)^2-1}{12mn}.
\]

This is the discrete version of the familiar fractional-part/GCD covariance
mechanism [3]. Define

\[
 \phi(d)=d\prod_{p\mid d}(1-p^{-1}),\qquad
 J_2(d)=d^2\prod_{p\mid d}(1-p^{-2}).
\]

Then

\[
 M(s_d)=\frac{\phi(d)}2,
 \qquad
 \operatorname{Cov}_M(s_d,s_e)
 =\begin{cases}J_2(d)/12,&d=e,\\0,&d\ne e.\end{cases}
\]

One proof expands gcd(m,n)^2-1 as
sum_{a|m,a|n,a>=2} J_2(a) and applies Mobius inversion in both variables.
Equivalently, the centered s_d has Fourier frequencies of reduced denominator
exactly d, so distinct denominators have disjoint frequency supports.

If A=sum_{d=2}^N y_d s_d, the exact periodic error is

\[
 M(|1-A|^2)=
 \left|1-\frac12\sum_d\phi(d)y_d\right|^2
 +\frac1{12}\sum_d J_2(d)|y_d|^2.
\]

### 3.2 The H-source is prime powers, not totients

The exact weighted expectation is

\[
 \langle1,s_d\rangle_H
 =\sum_{n\mid d}\mu(d/n)\log n
 =\Lambda(d).
\]

This uses <1,b_n>_H=log(n)/n. In particular, the source is zero unless d is
a prime power. For d=p^a it is log p.

The same fact appears in the transform:

\[
 T s_d(s)=-\zeta(s)J_{1-s}(d),\qquad
 J_w(d)=\sum_{n\mid d}\mu(d/n)n^w.
\]

At s=1 the apparent singularity is removable and the value is Lambda(d).

Thus, with K_N(d,e)=<s_d,s_e>_H and lambda_N=(Lambda(2),...,Lambda(N)),

\[
 E_N=1-\lambda_N^T K_N^{-1}\lambda_N.
\]

K_N is positive definite. The expression is the SAME optimization as before,
not a new RH criterion or a new estimate.

## 4. A finite counterexample to mixing the metrics

For the two atoms s_2,s_3, their periodic Gram matrix is

\[
 R=\begin{pmatrix}1/2&1/2\\1/2&5/3\end{pmatrix}.
\]

Their periodic source is (1/2,1). Their H-source is
lambda=(log 2,log 3).

Combining R with the H-source would give the invalid squared distance

\[
 1-\lambda^TR^{-1}\lambda
 =1-\frac{20\log^2 2-12\log2\log3+6\log^2 3}{7}.
\]

The exact rational certificate proves

\[
 1.1018<\lambda^TR^{-1}\lambda<1.1019,
\]

so this putative squared distance is strictly negative. This is a
counterexample to a specific substitution of one metric for another, NOT a
counterexample to an unspecified GCD approach.

## 5. Stronger separation: the periodic optimizer fails in H

Set

\[
 S_N=\sum_{d=2}^N\frac{\phi(d)^2}{J_2(d)},\qquad D_N=1+3S_N.
\]

The unique optimal periodic coefficients in the s-basis are

\[
 y^{\rm per}_{N,d}=\frac{6\phi(d)}{J_2(d)D_N},
\]

with exact error

\[
 \min_{A\in B_N}M(|1-A|^2)=D_N^{-1}.
\]

This follows by completing the square in section 3.1, or by solving the
rank-one normal equations.

### 5.1 Size of the denominator

The multiplicative function f(d)=phi(d)^2/J_2(d) satisfies

\[
 f(d)=\prod_{p\mid d}\frac{p-1}{p+1}
     =\sum_{q\mid d}a(q),
\]

where a(q)=0 for nonsquarefree q and, for squarefree q,

\[
 a(q)=\mu(q)\prod_{p\mid q}\frac2{p+1}.
\]

Since |a(q)|<=tau(q)/q,

\[
 S_N=\kappa N+O((1+\log N)^2),\qquad
 \kappa=\prod_p\left(1-\frac2{p(p+1)}\right)>0.
\]

Indeed, floor-function errors are bounded by
sum_{q<=N} tau(q)/q <= H_N^2. The absolutely convergent mean has tail
N sum_{q>N} tau(q)/q^2=O(1+log N), using
sum_{q<=x}tau(q)<=x(1+log x). Thus the displayed asymptotic is elementary and
does not require a zero-location theorem.

It follows that the optimal periodic error is asymptotic to 1/(3 kappa N).

### 5.2 The corresponding H-function tends to zero

In the b-basis, the same periodic optimizer has coefficients

\[
 c^{\rm per}_{N,n}
 =n\sum_{j\le N/n}\mu(j)y^{\rm per}_{N,nj}.
\]

Because phi(d)/J_2(d)<=1/d,

\[
 |c^{\rm per}_{N,n}|\le\frac{6H_{\lfloor N/n\rfloor}}{D_N}.
\]

Hence

\[
 \sum_{n=2}^N|c^{\rm per}_{N,n}|
 \le\frac{6N\zeta(2)}{D_N}=O(1).
\]

For fixed k, b_n(k)<=min(k/n,1). Splitting at n=k shows
A_N^{per}(k)->0. The preceding uniform coefficient bound permits dominated
convergence in H, because sum_k 1/[k(k+1)]=1. Consequently,

\[
 \boxed{
 M(|1-A_N^{per}|^2)\longrightarrow0,
 \quad \|A_N^{per}\|_H\longrightarrow0,
 \quad \|1-A_N^{per}\|_H^2\longrightarrow1.
 }
\]

There is also the quantitative bound ||A_N^{per}||_H^2=O(1/N).
For k<=N, the coefficient estimate gives

\[
 |A_N^{per}(k)|
 \ll \frac{k}{N}(1+\log(N/k))^2;
\]

for k>N it is O(1). Summing the H-weights proves the claimed norm bound.

Finally,

\[
 \langle1,A_N^{per}\rangle_H
 =\frac6{D_N}\sum_{d\le N}\frac{\phi(d)\Lambda(d)}{J_2(d)}
 =\frac{6\log N}{D_N}+O(N^{-1}).
\]

For the last equality, on prime powers phi(d)/J_2(d) differs from 1/d by an
absolutely summable Lambda-weighted correction, and
sum_{d<=N}Lambda(d)/d=log N+O(1) follows from the elementary Chebyshev bound
and log(N!)=sum_{d<=N}Lambda(d)floor(N/d). Thus

\[
 \|1-A_N^{per}\|_H^2
 =1-\frac{4}{\kappa}\frac{\log N}{N}+O(N^{-1}).
\]

This optional refinement is not used in the main separation result.

## 6. Exact elimination to a prime-power matrix

Let P_N={d<=N:d is a prime power}, and let C_N be the other integers
between 2 and N. Partition the actual H-Gram matrix as

\[
 K_N=\begin{pmatrix}K_{PP}&K_{PC}\\K_{CP}&K_{CC}\end{pmatrix},
 \qquad \lambda_N=\binom{\lambda_P}{0}.
\]

When C_N is empty, omit those blocks. Otherwise define

\[
 K_N^{\rm eff}=K_{PP}-K_{PC}K_{CC}^{-1}K_{CP}.
\]

Then K_eff is positive definite and

\[
 \boxed{E_N=1-\lambda_P^T(K_N^{\rm eff})^{-1}\lambda_P.}
\]

This eliminates the composite coordinates exactly; it does NOT simply drop
them. They can reduce the energy through the Schur correction even though
their direct target expectation is zero.

More explicitly, put

\[
 H_N^{\rm eff}=K_N^{\rm eff}-\lambda_P\lambda_P^T.
\]

This is positive definite: it is the covariance Gram after removing the
composite directions. The centered original family s_d-Lambda(d) is
linearly independent, because a constant finite combination of s_d must
vanish at a common period and hence be zero. Therefore

\[
 E_N=\frac1{1+\lambda_P^T(H_N^{\rm eff})^{-1}\lambda_P}.
\]

Proving divergence of the denominator's second term is still the RH-bearing
problem. Positivity alone only proves it is nonnegative.

For the nested full K-basis, the exact dyadic Schur gain is

\[
 E_N-E_{2N}
 =r_N^T S_N^{-1}r_N,
\]

where r_N=lambda_new-K_new,old K_old,old^{-1}lambda_old. Here S_N denotes the
block Schur matrix, NOT the scalar S_N from section 5. Spectral upper bounds
on the Schur matrix would give lower bounds on gain ONLY after a lower bound
on this source vector (in a compatible metric) has been established.

## 7. The correlations discarded by period averaging

Write e(theta)=exp(2 pi i theta). The centered s_d has the exact Fourier
expansion

\[
 s_d(k)=\frac{\phi(d)}2+
 \sum_{\substack{1\le a<d\\(a,d)=1}}
 \frac{e(a/d)}{1-e(a/d)}e(ak/d).
\]

Primitive denominators are disjoint, explaining diagonal periodic covariance.
But H does not make distinct rational frequencies orthogonal. Its kernel is

\[
 W(\theta)=\sum_{k\ge1}\frac{e(k\theta)}{k(k+1)}
 =1+(e(-\theta)-1)\log(1-e(\theta)),
\]

where the logarithm is the limit from inside the unit disk and W(0)=1.
For theta not 0 modulo 1, the expression is elementary. In particular,

\[
 W(1/2)=1-2\log2<0.
\]

The finite matrix W(theta_a-theta_b) is positive semidefinite, since it is a
Gram matrix. Its individual off-diagonal entries need not be positive.

For a finite Fourier expansion F(k)=sum_theta alpha_theta e(k theta),

\[
 \|F\|_H^2
 =\sum_{\theta,\eta}\alpha_\theta\overline{\alpha_\eta}
 W(\theta-\eta),
 \qquad
 M(|F|^2)=\sum_\theta|\alpha_\theta|^2.
\]

The weighted correlations are essential even for the target expectation:

\[
 \Lambda(d)=\frac{\phi(d)}2+
 \sum_{\substack{1\le a<d\\(a,d)=1}}
 \frac{e(a/d)}{1-e(a/d)}W(a/d).
\]

For non-prime-powers, the oscillatory sum cancels the positive mean exactly.
There is no justification for treating these correlations as a uniformly
small perturbation of the periodic GCD geometry.

## 8. What remains for the explicit mollifier

For the prescribed coefficients

\[
 c_{N,n}=-\mu(n)(1-\log n/\log N),
\]

the s-basis coefficients are exactly

\[
 y_{N,d}=
 -\sum_{j\le N/d}\frac{\mu(dj)}{dj}
 \left(1-\frac{\log(dj)}{\log N}\right).
\]

Consequently its H-error is

\[
 Q_N=1-2\sum_{d\le N}y_{N,d}\Lambda(d)
       +\sum_{d,e\le N}y_{N,d}y_{N,e}K_N(d,e).
\]

The earlier length-averaging argument makes Q_N=N^{o(1)} sufficient for RH.
The present analysis does NOT prove this estimate. It locates precisely why
GCD covariance estimates alone do not establish it: they estimate a different
quadratic form, with a different target mean, and discard the weighted
cross-frequency terms in section 7.

A productive next estimate would preserve those weighted correlations and
control them for the actual Mobius source, or directly for the prime-power
Schur source. Neither the required signed estimate nor a bounded reflection
duality is proved here.

## 9. Exact checks and limitations

Run `python check_identities.py`. The script uses only standard-library exact
fractions. It checks the change of basis, Ramanujan differences, both periodic
covariance identities, the prime-exponent source identity, and the periodic
normal equations for denominators through 8. It also certifies the N=3
mixed-metric counterexample using rational log enclosures from the atanh
series and a geometric tail bound. These are finite checks of the formulas;
the asymptotic separation is justified by the proofs above, not by sampling.

## References

[1] Michel Balazard, *An arithmetical function related to Baez-Duarte's
criterion for the Riemann hypothesis*, arXiv:1812.04309.
https://arxiv.org/html/1812.04309v1

[2] NIST Digital Library of Mathematical Functions, section 25.4,
Reflection Formulas.
https://dlmf.nist.gov/25.4

[3] Christoph Aistleitner, Istvan Berkes, Kristian Seip, Michel Weber,
*Convergence of series of dilated functions and spectral norms of GCD
matrices*, arXiv:1407.5403; Acta Arithmetica 168 (2015), 221--246.
https://arxiv.org/html/1407.5403v2

[4] Sandro Bettin, J. Brian Conrey, David W. Farmer,
*An optimal choice of Dirichlet polynomials for the Nyman--Beurling
criterion*, arXiv:1211.5191.
https://arxiv.org/abs/1211.5191

[5] Jean-Francois Burnol, *An adelic causality problem related to abelian
L-functions*, arXiv:math/0001013; J. Number Theory 87 (2001), 253--269.
https://arxiv.org/abs/math/0001013

[6] Neha Elizabeth Thomas, K. Vishnu Namboothiri,
*On near orthogonality of certain k-vectors involving generalized Ramanujan
sums*, arXiv:2312.07098. Used only as a primary literature entry point for
Ramanujan-sum orthogonality and Jordan-totient conventions.
https://arxiv.org/html/2312.07098v1
