# 06. Every-prefix witnesses, exact growth exponent, and multiplicity

**Status: proposed component proofs.** These are lower bounds and equivalence statements, not the missing arithmetic upper estimate. The classical analytic input in the upper-exponent argument is stated separately. Chapter 09 gives an alternative, simpler fixed-Gaussian sparse criterion.

## 1. Why a sparse sequence requires a separate theorem

An all-cutoff energy bound implies an RH-strength Mertens estimate by Chapter 05. A bound at sparse cutoffs does not automatically interpolate, because Q_j need not be monotone. The needed mechanism is instead: every off-critical zero forces every sufficiently large cutoff to be expensive.

Write
\[
\Theta=\sup_{\zeta(\rho)=0,\ 0<\Re\rho<1}\Re\rho.
\]
Classical symmetry gives 1/2<=Theta<=1. Theta=1 is not excluded in an unconditional argument, and the supremum need not be attained.

## 2. An exact causal arithmetic kernel

Let
\[
d(t)=e^{-t/2}\{\lfloor e^t\rfloor(1-t)+\log(\lfloor e^t\rfloor!)\}1_{t\ge0}.
\]
The expression in braces is sum_(k<=e^t)(1-t+log k). Integral comparison gives
\[
0\le d(t)\le(1+t)e^{-t/2},\qquad\|d\|_1\le6.
\]
With s=z+1/2, termwise integration for Re s>1 and continuation of the convergent kernel integral give
\[
\mathcal Ld(z)=\frac{(s-1)\zeta(s)}{s^2},\quad\Re s>0.
\]
The apparent pole of zeta at 1 is removed. This is the factorial kernel used in the repository's causal programme; its normalization matters.

Let
\[
\nu_N=\sum_{n\le N}\frac{\mu(n)}{\sqrt n}\delta_{\log n},\quad
q_N=d*\nu_N,\quad
v(t)=e^{-t/2}(1-t)1_{t\ge0},\quad T=\log(N+1).
\]
For t<T, divisor inversion gives q_N(t)=v(t). After removing e^(-t/2), group the double sum by r=nk; the coefficient sum_(n|r)mu(n) vanishes except at r=1. For t>=T,
\[
|q_N(t)-v(t)|\le(N+1)(1+t)e^{-t/2}.
\]
This is a literal prefix statement with its entire late-time remainder.

## 3. Transfer to the noncausal Q_0 kernel

The Q_0 source in log coordinates is
\[
g_N(u)=e^{3u/2}F_N(e^u)=\phi_0*\nu_N,
\quad\phi_0(u)=e^{3u/2}e^{-e^u},\quad\|g_N\|_2^2=Q_0(N).
\]
Since phi_0 is not causal, the prefix equality cannot be convolved and then treated as exact on an initial interval.

For an integer k>=1 set b=k+3/2, a=k+2,
\[
\phi_k(u)=e^{bu}e^{-e^u},\quad
h_k(u)=u^{k-1}e^{-au}1_{u\ge0}/\Gamma(k),\quad
\psi_k=h_k*\phi_k.
\]
Its bilateral transform is
\[
\Psi_k(z)=\frac{\Gamma(b-z)}{(a+z)^k}.
\]
On the Fourier axis,
\[
\left|\frac{\Psi_k(i\tau)}{\Gamma(3/2-i\tau)}\right|
=\prod_{r=0}^{k-1}\frac{\sqrt{(r+3/2)^2+\tau^2}}{\sqrt{a^2+\tau^2}}\le1.
\]
Therefore \(||\psi_k*\nu_N||_2\le\sqrt{Q_0(N)}\). Also
\(|\psi_k(u)|\le(a+b)^{-k}e^{bu}\).

Put y_N=psi_k*q_N=d*(psi_k*nu_N), y_*=psi_k*v. Then
\[
\|y_N\|_2\le6\sqrt{Q_0(N)},\qquad
|y_N(x)-y_*(x)|\le C_k(1+T)e^{b(x-T)+T/2}.
\]
The second inequality integrates the complete remainder starting at T; no finite truncation is substituted for it.

## 4. An off-critical zero forces polynomial growth at EVERY large cutoff

Suppose rho=beta+i gamma is a zero with beta>1/2; put alpha=beta-1/2 and z_rho=alpha+i gamma. The transforms converge absolutely at this point. The kernel identity gives
\[
\mathcal Ly_N(z_\rho)=0,\qquad
\mathcal Ly_*(z_\rho)=\Psi_k(z_\rho)(\rho-1)/\rho^2\ne0.
\]
Gamma has no zeros, and rho is neither 0 nor 1.

Fix 0<c<1 and choose k large enough that b>alpha and b(1-c)>1/2. Split the transform of y_N-y_* at cT. The part before cT is bounded by
\[
C_{k,\rho}(1+T)e^{[1/2-b(1-c)-\alpha c]T}\to0.
\]
The part after cT is at most
\[
\frac{e^{-\alpha cT}}{\sqrt{2\alpha}}
(6\sqrt{Q_0(N)}+\|y_*\|_2)
\]
by Cauchy–Schwarz. It must account for a fixed nonzero transform value, so
\[
\boxed{Q_0(N)\ge c_{\rho,c}N^{c(2\beta-1)}}
\]
for every sufficiently large N. Constants may depend on the fixed zero and c. This is not a lower bound only along a subsequence, and no simplicity assumption enters.

Let c tend to 1 and take a supremum over fixed zeros to obtain lower exponent 2Theta-1.

## 5. Matching upper exponent: the classical analytic dependency

Use the generalized Littlewood implication: if zeta is zero-free in Re s>theta with 1/2<=theta<1, then M(x)=O_epsilon(x^(theta+epsilon)). The repository manuscript at the frozen #869 follow-up reconstructs the disk/three-circles/Perron argument. It is an interior estimate, not a bound on Re s=theta. This packet does not infer it from zero counting alone.

For Theta<1 it gives
\[
|P_N(1/2+i\tau)|\ll_\eta(1+|\tau|)N^{\Theta-1/2+\eta}.
\]
The exact Gamma moments are
\[
\frac1{2\pi}\int W_j=1/4,\qquad
\frac1{2\pi}\int \tau^2W_j=(j+3/2)/8.
\]
Thus
\[
Q_j(N)\ll_\eta(1+j)N^{2\Theta-1+2\eta}.
\]
For Theta=1, the bound Q_j<=N follows from the absolute kernel sum. Combine these upper bounds with Q_j>=Q_0/A_j. If \(\log(1+j_N)=o(\log N)\), then
\[
\boxed{\lim_{N\to\infty}\frac{\log(1+Q_{j_N}(N))}{\log N}=2\Theta-1.}
\]
This identifies an unknown exponent. It does not prove it is zero.

## 6. Sparse and relative-growth criteria

For j_N=ceil(log^4N), the exponent theorem gives
\[
\mathrm{RH}\iff\exists N_r\to\infty:\ Q_{j_{N_r}}(N_r)\le N_r^{o(1)}.
\]
Since D(N)=O(log N), the same holds with a one-sided upper bound on B_j=Q_j-D. This is the conversation's target (27).

For any fixed q>1 and 0<delta<q, a further sufficient target is, along an unbounded sequence,
\[
1+Q_0(\lfloor N_r^q\rfloor)
\le N_r^{o(1)}(1+Q_0(N_r))^{q-\delta}.
\]
Writing kappa=2Theta-1, its exponents would give q kappa<=(q-delta)kappa, hence kappa=0. No such relative contraction is established here.

## 7. Critical-line multiplicity forces logarithmic growth

If rho=1/2+i gamma is a zero of multiplicity m>=1, then the same filtered source yields the proposed lower bound
\[
\boxed{Q_0(N)\ge c_\rho(\log N)^{2m-1}}
\]
for every sufficiently large N.

Here is the argument. Choose a smooth compactly supported chi in (-1,1), equal to 1 near zero. Put L=cT and f_L(x)=e^(i gamma x)chi(x/L). The transform of y_* at i gamma is nonzero, and the leakage estimate makes <y_N-y_*,f_L> tend to zero. Thus |<y_N,f_L>| stays bounded below.

Write y_N=d*u_N with ||u_N||_2<=sqrt(Q_0(N)). The zero and conjugate-zero multiplicities give
\[
\int_0^\infty v^r d(v)e^{i\gamma v}dv=0,\quad0\le r<m.
\]
Taylor-expand the translated cutoff in the adjoint convolution d^*f_L. All terms below order m vanish. Minkowski's inequality for the integral remainder gives
\[
\|d^*f_L\|_2\le
\frac{\|\chi^{(m)}\|_2}{m!}L^{1/2-m}
\int_0^\infty v^m|d(v)|dv.
\]
The last integral is finite. Cauchy–Schwarz proves the lower bound.

Consequently O(log N) energy would exclude multiple critical-line zeros as well as off-line zeros; it is stronger than the subpolynomial target needed for RH. The packet does not assume simple zeros, and does not promote a random-sign logarithmic heuristic to the necessary target.
