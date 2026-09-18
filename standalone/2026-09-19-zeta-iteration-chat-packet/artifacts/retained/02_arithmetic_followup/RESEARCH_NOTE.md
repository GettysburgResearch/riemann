# RH arithmetic follow-up: exact obstructions, tail localization, and certificates

Date: 2026-09-17. Status: unconditional lemmas and finite numerical certificates;
no proof of RH, no new zero-free region, and no priority claim for the lemmas.

## 1. Setup and the one-sided bound

Let H be the complex Hilbert space with inner product, linear in its first argument,

\[
\langle f,g\rangle=\sum_{k\ge1}f(k)\overline{g(k)}/[k(k+1)].
\]

Put b_n(k)={k/n}, B_N=span(b_2,...,b_N), A_N=P_N 1, e_N=1-A_N,
and E_N=||e_N||^2. For G_mn=<b_m,b_n> and v_n=log(n)/n,

\[
A_N=\sum_{n=2}^N c_{N,n}b_n,\quad c_N=G_N^{-1}v,\quad
E_N=1-v^TG_N^{-1}v.
\]

The Balazard–Saias–Yor quantity is

\[
\mathcal D=\frac1{2\pi}\int_{\mathbb R}
\frac{\log|\zeta(1/2+it)|}{1/4+t^2}\,dt
=\sum_{\Re\rho>1/2}\log|\rho/(1-\rho)|\ge0.
\]

Zeros are counted with multiplicity. Thus RH is equivalent to D=0 [1].
For every real c with c^Tv nonzero, the argument from the preceding pass gives

\[
\mathcal D\le\frac12\log\frac{c^TG_Nc}{(c^Tv)^2},\qquad
\mathcal D\le-\tfrac12\log(1-E_N).
\]

For completeness, put P_c(s)=sum c_n(1/n-n^{-s}). It vanishes at 1 and
P_c'(1)=c^Tv. Extend A_c to the step function
sum c_n({x/n}-{x}/n), zero below 1. Its Mellin transform is zeta(s)P_c(s)/s.
Mellin Plancherel gives int |zeta P_c|^2 dmu=c^TGc, where
 dmu=dt/[2pi(1/4+t^2)]. The bounded analytic function P_c(s)/(s-1) on Re s>1/2
satisfies the Poisson–Jensen inequality at s=1. Since
int log|(-1/2)+it| dmu=0, this gives int log|P_c| dmu >= log|c^Tv|.
Concavity of log then proves the asserted bound. This argument does not assume
the multiplier is zero-free.

The Hilbert-space setting and its connection to RH are established
Nyman–Beurling–Báez-Duarte theory [2].

## 2. Minimum scale criterion and its exact obstruction

The errors decrease to a limit L. Let B be the closed union of the B_N and P
its projection. Then

\[
e_N=e_\infty+(P-P_N)1,\quad e_\infty=(I-P)1,\quad
\|e_\infty\|^2=L,\quad\|(P-P_N)1\|^2=E_N-L.
\]

Every b_n is orthogonal to e_infinity. Consequently the exact Schur gain

\[
\Delta_N=E_N-E_{2N}=r_N^TS_N^{-1}r_N
\]

only sees the transient component, and 0<=Delta_N<=E_N-L.

Here, when the larger Gram matrix is partitioned as [[G,B],[B^T,C]],
S=C-B^TG^{-1}B and r=w-B^TG^{-1}v. This identity follows by block inversion
or by orthogonalizing the new vectors against the old span.

If L>0, it suffices to show Delta_{2^j} >= c(L)/(j log j) on a set J with
sum_{j in J}1/(j log j)=infinity. An infinite set of scales alone is not enough.
The contradiction follows by telescoping the finite total drop in E. No such
lower bound is proved here.

### Exact zero kernels

For Re z>1/2 define

\[
h_z(k)=k(k+1)(k^{-\bar z}-(k+1)^{-\bar z}).
\]

Then

\[
h_z(k)\sim\bar z\,k^{1-\bar z},\quad
\langle1,h_z\rangle=1,\quad
\langle b_n,h_z\rangle=\zeta(z)(1/n-n^{-z}).
\]

The first inner product telescopes. The second follows by multiplying the
Mellin identity for b_n's step extension by z. All these scalar products
converge in the stated half-plane. Cauchy–Schwarz on each interval [k,k+1]
shows

\[
\|h_z\|^2\le |z|^2/(2\Re z-1).
\]

Indeed, bound |int x^{-z-1} dx|^2 by (int x^{-2Re z} dx)(int x^{-2} dx).

If rho is an off-line zero on the right, h_rho is orthogonal to every b_n,
not merely to one denominator block. Also <e_N,h_rho>=1, so
E_N>=1/||h_rho||^2. A leading-power approximation can destroy these exact
cancellations. We do not assert that the whole orthogonal complement is
spanned by such kernels. The existence of these individual obstruction
vectors suffices to refute the suggested nonzero-correlation shortcut.
Related orthogonality formulations are discussed in [2,3].

A small D only controls weighted displacement. At rho=1/2+delta+i gamma,
its summand is

\[
\tfrac12\log\left(1+\frac{2\delta}{(1/2-\delta)^2+\gamma^2}\right).
\]

It behaves as delta/gamma^2 at large height. Small D does not imply that
hypothetical off-line zeros are few, nor that all are close to the line.

## 3. Unconditional coefficient bounds and conditioning

For arbitrary A=sum_{n=2}^N c_n b_n, set A(0)=0,
a_1=sum c_n/n, a_n=-c_n (n>=2), and u_d=A(d)-A(d-1).
The floor representation gives

\[
A(k)=\sum_{n\le N}a_n\lfloor k/n\rfloor,\quad
u_d=\sum_{n\mid d}a_n\ (d\le N),\quad a=\mu*u.
\]

The elementary bound

\[
\sum_{d\le N}|u_d|^2/d^2\le6\|A\|^2
\]

follows from |A(d)-A(d-1)|^2 <= 2|A(d)|^2+2|A(d-1)|^2,
1/d^2<=2/[d(d+1)], and 1/(k+1)^2<=1/[k(k+1)]. Thus

\[
\sum_{n=2}^N|c_n|
\le N\sum_{d\le N}|u_d|/d
\le\sqrt6\,N^{3/2}\|A\|.
\]

Writing H_N=sum_{j<=N}1/j and x_d=u_d/d, the formula

\[
a_n/n=\sum_{k\mid n}(\mu(k)/k)x_{n/k}
\]

and the triangle inequality for dilation operators on l2 give

\[
\sum_{n\le N}|a_n|^2/n^2\le6H_N^2\|A\|^2.
\]

Therefore

\[
G_N\succeq\frac{I}{6N^3},\qquad
G_N\succeq\frac{I}{6N^2H_N^2}.
\]

Both estimates hold for every N>=2. For the projection ||A_N||<=1, so its
coefficient l1 norm is at most sqrt(6) N^(3/2).

### Certification without an interval inverse

For an exact rational vector c_tilde define
F=1-2v^Tc_tilde+c_tilde^TGc_tilde and d=v-Gc_tilde.
Completing the square gives F-E_N=d^TG^{-1}d, whence

\[
F-6N^3\|d\|^2\le E_N\le F.
\]

This rigorously encloses the optimal error from interval matrix-vector
arithmetic even though the initial candidate was obtained in ordinary
floating point. The bound for D itself only needs a rational witness and
does not need optimality.

## 4. Large-sieve tail theorem: a cutoff near N squared

Let M(F) denote the average of |F|^2 over the common period
lcm(2,...,N). For every K>=N^2 the optimal residual obeys

\[
0\le E_N-\sum_{k\le K}\frac{|e_N(k)|^2}{k(k+1)}
\le\frac{108N^2H_N^3}{K}.
\]

No bound of size O(1) for individual optimal coefficients is assumed.

### 4.1 Periodic mean

The period mean of b_n is (n-1)/(2n). Since sum a_n/n=0,
the mean of A is -sum_{n<=N} a_n/2.
Let M_mu(x)=sum_{n<=x}mu(n),
Delta_d=M_mu(N/d)-M_mu(N/(d+1)), and
j_d=floor(N/d)-floor(N/(d+1)). Summation by parts gives

\[
\sum_{n\le N}a_n=\sum_{d\le N}A(d)\Delta_d.
\]

We have |Delta_d|<=j_d, sum j_d=N, and
j_d<=N/[d(d+1)]+1. Hence

\[
\sum_{d\le N}d(d+1)\Delta_d^2
\le N^2+\sum_{n\le N}\lfloor N/n\rfloor(\lfloor N/n\rfloor+1)
\le (1+\zeta(2))N^2+NH_N<4N^2.
\]

Cauchy–Schwarz yields |mean(A)|^2<=N^2||A||^2.
Only the trivial inequality |sum mu|<=number of summands has been used.

### 4.2 Periodic variance

A direct residue calculation gives

\[
\operatorname{Cov}(b_m,b_n)=\frac{\gcd(m,n)^2-1}{12mn}.
\]

One proof conditions on the common residue modulo gcd(m,n); the remaining
residue coordinates are independent. Put x_n=c_n/n. Then

\[
\operatorname{Var}(A)
=\frac1{12}\sum_{m,n}x_m\bar x_n(\gcd(m,n)^2-1).
\]

The symmetric matrix (gcd(m,n)^2) has maximum row sum at most N^2 H_N,
since gcd(m,n)^2=sum_{d|m,d|n}J_2(d), J_2(d)<=d^2, and
sigma_1(m)<=m H_m. Subtracting the all-ones matrix only decreases its
quadratic form. Applying the weighted coefficient estimate from section 3,

\[
\operatorname{Var}(A)\le\tfrac12N^2H_N^3\|A\|^2.
\]

It follows that M(A)<=N^2(1+H_N^3/2)||A||^2. Since ||A_N||<=1,

\[
M(e_N)\le2+2M(A_N)\le4N^2H_N^3.
\]

### 4.3 Large sieve and summing the tail

Every Fourier frequency of e_N is rational with reduced denominator <=N.
After duplicate frequencies are combined, Parseval over the common period
identifies M(e_N) with the sum of squared Fourier coefficients. By duality,
the elementary additive large sieve [4] implies, for every interval of J
consecutive integers,

\[
\sum_{k=M+1}^{M+J}|e_N(k)|^2
\le(N^2+4\pi J)M(e_N).
\]

A shift M only changes coefficient phases. Applying this to dyadic intervals
2^j K<k<=2^(j+1)K gives

\[
\sum_{k>K}\frac{|e_N(k)|^2}{k(k+1)}
\le M(e_N)\left(\frac{8\pi}{K}+\frac{4N^2}{3K^2}\right)
\le\frac{108N^2H_N^3}{K}.
\]

Consequently, for every epsilon>0,

\[
E_N=\sum_{k\le\lceil N^{2+\epsilon}\rceil}
\frac{|e_N(k)|^2}{k(k+1)}
+O\big((1+\log N)^3/N^\epsilon\big).
\]

Alternatively K=ceil(N^2(1+log N)^(3+eta)) gives an O((1+log N)^(-eta)) tail.
These formulas localize the error; they do not prove that the retained finite
sum tends to zero.

## 5. Cotangent Gram formula and actual algorithm

For positive coprime a,b define

\[
W(a,b)=\sum_{r=1}^{b-1}\{ar/b\}\cot(\pi r/b),\qquad W(a,1)=0.
\]

For g=gcd(m,n), a=m/g, b=n/g, put

\[
R(m,n)=\frac{(m-n)\log(n/m)-\pi g[W(a,b)+W(b,a)]}{2mn}.
\]

Vasyunin's formula [5], with a gcd rescaling, implies

\[
G_{mn}=R(m,n)-R(m,1)/n-R(1,n)/m.
\]

Indeed, for K(m,n)=int_0^infty {x/m}{x/n}dx/x^2,
K=C(1/m+1/n)+R, with C=(log(2pi)-gamma)/2.
Expanding the Gram product of {x/m}-{x}/m and {x/n}-{x}/n cancels C exactly.

Pairing r with b-r gives

\[
W(a,b)=\frac1b\sum_{1\le r<b/2}(2(ar\bmod b)-b)\cot(\pi r/b).
\]

The code precomputes paired sums, uses oddness, reuses gcd reductions, and
then constructs the Gram matrix. It performs O(N^3) arithmetic operations
and uses O(N^2) memory, improving the previous lcm-based O(N^4) construction.
It does not implement an O(log N) certified continued-fraction evaluator.
Cotangent reciprocity also involves a smooth period function [5]. A faster
individual-entry evaluator would not, by itself, remove a dense cubic solve.

The floating formula was checked against the independent digamma-period
formula in the previous certificate, and the block Schur gains were checked
against differences of independently optimized errors. Small-period covariance
and conditioning checks are included. These checks supplement, not replace,
the analytic proofs.

## 6. Computations and certificate status

Floating-point exploration reached N=2048. Exact rational witness and optimum
certification reached N=1024. Selected values:

| N | E_N (rounded) | E_N log N (rounded) | certified D upper bound |
|---|---:|---:|---:|
| 256 | 0.008242256028257 | 0.0457047722 | 0.00413821 |
| 512 | 0.007393375337423 | 0.0461222754 | 0.00371043 |
| 1024 | 0.006534086495726 | 0.0452908363 | 0.00327777 |
| 2048 | 0.006111155075890 | 0.0465952290 | not certified |

For N=1024 the rational coefficients have denominator 10^15. Interval
arithmetic encloses the bound for D between
0.0032777635431873724036703630169170 and
0.0032777635431873724036703633774545.
The certified optimal E_N lies between
0.0065340864957257050718413635997168 and
0.0065340864957257056134299795561362.
Full intervals, rational numerators, precision, and conditioning correction
are in results/certificate_N1024.json.

Cotangent values are enclosed by mpmath.iv, converted outward to exact integer
bounds at scale 2^100, and all cotangent sums are accumulated using signed
arbitrary-size integer arithmetic. Final logarithms, pi, quadratic forms,
and gradient bounds are evaluated with 50-decimal interval arithmetic.
There is no interval matrix inversion. This is a reproducible computational
certificate relying on the mathematical formulas and the interval library,
not proof-assistant formal verification. It is not a claim of a record bound
or a competitive new zero exclusion.

The number 2+gamma-log(4pi)=0.046191417932242... is an asymptotic benchmark,
not a proved limiting value for this constrained E_N. Burnol's lower bound
involves squared zero multiplicities [6]. The sharp optimality result of
Bettin–Conrey–Farmer assumes RH and a further reciprocal-derivative estimate
[7]. Finite values below the benchmark are not contradictory. In particular,
N=256 and N=1024 are already below it.

The positive known 1/log N lower bound also rules out any eventually uniform
fixed-factor decrease E_{2N}<=(1-eta)E_N. The constrained polynomial class
is a subclass of the standard one, so the lower-bound direction is valid.

## 7. Remaining proof obligation

The following statement is sufficient but unproved:

If L=lim E_N>0, there is a set J of dyadic indices with
sum_{j in J}1/(j log j)=infinity and a constant c(L)>0 such that

\[
E_{2^j}-E_{2^{j+1}}\ge c(L)/(j\log j)\quad(j\in J).
\]

The exact zero kernels show why one cannot establish this by claiming the
persistent spectral component has nonzero correlations with new denominators.
It has zero correlations. A proof must use additional arithmetic information
to exclude that component, or directly control the localized finite residual
sum in section 4. The tail theorem and all finite certificates remain valid
in either hypothetical zero configuration; they do not make that final step.

## References

[1] H. M. Bui, S. J. Lester, M. B. Milinovich, On Balazard, Saias, and Yor's
equivalence to the Riemann Hypothesis, arXiv:1306.0856.
[2] M. Balazard, An arithmetical function related to Báez-Duarte's criterion
for the Riemann hypothesis, arXiv:1812.04309.
[3] F. Calderaro, J. Manzur, W. Noor, C. Santos, Orthogonality questions in
the Hardy space related to zeta-zeros, arXiv:2203.05030.
[4] J.-H. Evertse, MasterMath Analytic Number Theory, Chapter 11,
The large sieve, p.57: additive large sieve with Q^2+4*pi*x constant.
[5] S. Darses, E. Hillion, An exponentially-averaged Vasyunin formula,
arXiv:2004.10086, p.2, ordinary Vasyunin formula and reciprocity discussion.
[6] J.-F. Burnol, A lower bound in an approximation problem involving the
zeros of the Riemann zeta function, arXiv:math/0103058.
[7] S. Bettin, J. B. Conrey, D. W. Farmer, An optimal choice of Dirichlet
polynomials for the Nyman–Beurling criterion, arXiv:1211.5191.
