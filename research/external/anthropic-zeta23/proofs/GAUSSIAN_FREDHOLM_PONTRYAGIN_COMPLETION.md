# Gaussian Fredholm–Pontryagin completion of the finite Weil-compression program

**Status:** proposed complete operator-theoretic reduction; independent analytic review required.  
**RH status:** unproved.  
**Input:** the centered Weil zero-side formula and the Xi-cardinal source theorem of PR #365.

## 1. Purpose

The finite Gabor/rank–trace method reads finitely many linear spectral statistics. A single off-line pair can be arbitrarily shallow, and every fixed finite channel bank remains a pullback of one hyperbolic plane. The natural nonlinear completion is the full exterior algebra of one trace-class compression of Weil's Hermitian form.

This note constructs a **Gaussian-confined global compression** and proves

\[
\mathrm{RH}
\iff A_\sigma\succeq0
\iff \det(I+tA_\sigma)>0\quad(t>0)
\iff H_d(A_\sigma)\succeq0\quad(d=0,1,2,\dots)
\iff \operatorname{tr}(\wedge^kA_\sigma)\ge0\quad(k=1,2,\dots).
\]

It also proves that false RH has a witness at a **finite exterior degree**, **finite prime cutoff**, and **finite Galerkin dimension**. The unsolved theorem is the all-order arithmetic positivity of these absolutely convergent prime-cluster quantities.

The Gaussian confinement is stronger than an exponential strip weight: the prime tail is super-polynomial in the cutoff, while the exact Xi-cardinal sources remain in the range because they decay faster than every Gaussian.

## 2. Centered Weil form

Write

\[
\Xi(z)=\xi\!\left(\tfrac12+iz\right)
\]

and let \(\mathcal Z\) be its distinct zero set, with multiplicities \(m_z\). Grouping conjugate points, the centered Weil form is

\[
\begin{aligned}
Q_W(f,g)
={}&\sum_{x\in\mathcal Z\cap\mathbb R}m_x\,
 \widehat f(x)\overline{\widehat g(x)}\\
&+\sum_{\{z,\bar z\}\subset\mathcal Z,\;\Im z>0}m_z
 \left(
 \widehat f(z)\overline{\widehat g(\bar z)}
 +\widehat f(\bar z)\overline{\widehat g(z)}
 \right).
\end{aligned}
\tag{FP.1}
\]

Each real zero gives a positive rank-one block. Each nonreal reflected pair gives

\[
m_z\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{FP.2}
\]

## 3. Gaussian trace-class confinement

Fix \(\sigma>0\), and put

\[
w_\sigma(u)=e^{-\sigma u^2},\qquad
R=(1-\partial_u^2)^{-1},\qquad
J_\sigma=M_{w_\sigma}R:L^2(\mathbb R)\to L^2(\mathbb R).
\tag{FP.3}
\]

Here \(R\) is convolution by \(r(u)=\tfrac12e^{-|u|}\). The map \(J_\sigma\) is Hilbert–Schmidt because its kernel is \(w_\sigma(u)r(u-v)\).

For \(z=t+iy\), \(|y|<\tfrac12\), let \(k_z\in L^2\) represent evaluation:

\[
\langle h,k_z\rangle=\widehat{J_\sigma h}(z).
\]

### Lemma 3.1 — evaluation decay

There is \(C_\sigma<\infty\) such that

\[
\boxed{\|k_{t+iy}\|_2\le C_\sigma(1+t^2)^{-1}\qquad(|y|\le\tfrac12).}
\tag{FP.4}
\]

Indeed,

\[
k_z=R\bigl(w_\sigma(u)e^{-i\bar zu}\bigr).
\]

Writing \(w_{\sigma,y}(u)=w_\sigma(u)e^{-yu}\),

\[
\|k_z\|_2^2
={1\over2\pi}\int {\left|\widehat{w_{\sigma,y}}(\xi-t)\right|^2\over(1+\xi^2)^2}\,d\xi.
\]

The \(H^2\)-norms of \(w_{\sigma,y}\) are uniform for \(|y|\le\tfrac12\), and

\[
(1+\xi^2)^{-2}\le C(1+t^2)^{-2}(1+|\xi-t|^2)^2.
\]

The local zero count gives

\[
\sum_{z\in\mathcal Z}m_z\|k_z\|_2^2<\infty.
\tag{FP.5}
\]

Define

\[
\boxed{
A_\sigma
=\sum_{x\in\mathcal Z\cap\mathbb R}m_x|k_x\rangle\langle k_x|
 +\sum_{\Im z>0}m_z
 \bigl(|k_z\rangle\langle k_{\bar z}|+|k_{\bar z}\rangle\langle k_z|\bigr).
}
\tag{FP.6}
\]

Since \(\||u\rangle\langle v|\|_1=\|u\|\|v\|\), (FP.5) proves absolute convergence in trace norm. Thus \(A_\sigma\) is self-adjoint trace class and

\[
\boxed{\langle A_\sigma h,g\rangle=Q_W(J_\sigma h,J_\sigma g).}
\tag{FP.7}
\]

## 4. Super-convergent prime side

Let \(T_yf(u)=f(u-y)\). The prime-power term in Weil's explicit formula pulls back to \(J_\sigma^*T_yJ_\sigma\), with \(y=\pm\log n\).

### Lemma 4.1 — exact Gaussian overlap law

\[
\boxed{
\begin{aligned}
\|J_\sigma^*T_yJ_\sigma\|_1
&\le\|r\|_2^2\int_{\mathbb R}w_\sigma(u)w_\sigma(u-y)\,du\\
&=\|r\|_2^2\sqrt{\pi\over2\sigma}\,e^{-\sigma y^2/2}.
\end{aligned}}
\tag{FP.8}
\]

The inequality follows by writing the kernel as a continuous sum of rank-one kernels. The equality is completion of the square:

\[
u^2+(u-y)^2=2(u-y/2)^2+y^2/2.
\]

Therefore

\[
\boxed{
\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
\bigl\|J_\sigma^*(T_{\log n}+T_{-\log n})J_\sigma\bigr\|_1<\infty.
}
\tag{FP.9}
\]

The pole part is finite rank. For the Gamma multiplier \(\mu(\tau)=O(\log(2+|\tau|))\), put \(U=\mathcal FJ_\sigma\). In Fourier variables,

\[
U(\tau,\xi)=c_\mathcal F\,\widehat w_\sigma(\tau-\xi)(1+\xi^2)^{-1}.
\]

Hence

\[
\begin{aligned}
\bigl\||\mu|^{1/2}U\bigr\|_{HS}^2
&\ll\iint {\log(2+|\tau|)\,|\widehat w_\sigma(\tau-\xi)|^2\over(1+\xi^2)^2}\,d\tau d\xi\\
&\ll_\sigma\int {\log(2+|\xi|)\over(1+\xi^2)^2}\,d\xi<\infty.
\end{aligned}
\]

Therefore \(U^*M_\mu U\) is trace class. Weil's explicit formula, first on smooth rapidly decreasing tests and then by trace-norm/form continuity, gives

\[
A_\sigma=A_{0,\sigma}-\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
J_\sigma^*(T_{\log n}+T_{-\log n})J_\sigma.
\tag{FP.10}
\]

For the cutoff \(P\), the crude bound \(\Lambda(n)\le\log n\), followed by \(v=\log x\), yields

\[
\boxed{
\|A_\sigma-A_{\sigma,P}\|_1
\ll_\sigma
\exp\!\left[-{\sigma\over2}(\log P)^2+{1\over2}\log P\right](1+\log P).
}
\tag{FP.11}
\]

In particular the prime cutoff error is smaller than every fixed power of \(P^{-1}\).

## 5. Exact Pontryagin index

For a nonreal pair \(\{z,\bar z\}\), let \(q_z\) be the exact Xi-cardinal difference from PR #365:

\[
\widehat q_z(z)=1,\quad
\widehat q_z(\bar z)=-1,\quad
\widehat q_z(\zeta)=0\quad(\zeta\in\mathcal Z\setminus\{z,\bar z\}),
\tag{FP.12}
\]

with \(q_z\) decaying faster than every Gaussian. Hence

\[
h_z=(1-\partial_u^2)(q_z/w_\sigma)\in L^2,\qquad J_\sigma h_z=q_z.
\tag{FP.13}
\]

Consequently

\[
\langle A_\sigma h_z,h_z\rangle=-2m_z,
\tag{FP.14}
\]

and cardinal vectors belonging to distinct pairs are mutually \(A_\sigma\)-orthogonal. The hyperbolic direct-sum representation gives the reverse index bound.

### Theorem 5.1 — exact global index

\[
\boxed{n_-(A_\sigma)=\#\{\text{distinct nonreal reflected Xi-zero pairs}\}.}
\tag{FP.15}
\]

Thus

\[
\boxed{\mathrm{RH}\iff A_\sigma\succeq0.}
\tag{FP.16}
\]

## 6. Fredholm and exterior criteria

Define

\[
D_\sigma(t)=\det(I+tA_\sigma)=\prod_j(1+t\lambda_j)=\sum_{k=0}^{\infty}e_k(A_\sigma)t^k,
\tag{FP.17}
\]

where

\[
e_k(A_\sigma)=\operatorname{tr}(\wedge^kA_\sigma),\qquad
|e_k(A_\sigma)|\le{\|A_\sigma\|_1^k\over k!}.
\tag{FP.18}
\]

A positive real zero occurs exactly at the reciprocal of a negative eigenvalue. Therefore

\[
\boxed{\mathrm{RH}\iff D_\sigma(t)>0\quad(t>0).}
\tag{FP.19}
\]

Also

\[
\boxed{\mathrm{RH}\iff e_k(A_\sigma)\ge0\quad(k\ge1).}
\tag{FP.20}
\]

The converse follows because an entire power series with constant term one and all remaining coefficients nonnegative cannot vanish on the positive axis.

## 7. Shifted-Hankel criterion

Put

\[
m_j=\operatorname{tr}(A_\sigma^j),\qquad
H_d=(m_{i+j+1})_{0\le i,j\le d}.
\tag{FP.21}
\]

For \(p(x)=\sum_{i=0}^dc_ix^i\),

\[
\boxed{c^*H_dc=\sum_n\lambda_n|p(\lambda_n)|^2.}
\tag{FP.22}
\]

Thus \(A_\sigma\succeq0\) implies every \(H_d\succeq0\). Conversely, a nonzero negative eigenvalue of a compact self-adjoint operator is isolated. Approximate a continuous spectral selector for that negative point by a polynomial in (FP.22).

### Theorem 7.1 — Stieltjes form

\[
\boxed{\mathrm{RH}\iff H_d\succeq0\quad(d=0,1,2,\ldots).}
\tag{FP.23}
\]

## 8. False RH has a finite exterior-degree witness

Assume \(-\eta<0\) is an eigenvalue and put

\[
R_\sigma={\|A_\sigma\|_1\over\eta}.
\tag{FP.24}
\]

At \(t_0=1/\eta\), \(D_\sigma(t_0)=0\). If \(e_k\ge0\) for \(1\le k\le K\), then the absolute tail beyond \(K\) at \(t_0\) must be at least one. Yet

\[
\sum_{k>K}|e_k|t_0^k\le\sum_{k>K}{R_\sigma^k\over k!}.
\tag{FP.25}
\]

For \(n=K+1\ge2R_\sigma\),

\[
\sum_{k\ge n}{R_\sigma^k\over k!}
\le2{R_\sigma^n\over n!}
\le2\left({eR_\sigma\over n}\right)^n<1
\tag{FP.26}
\]

once \(n\ge\max(2,\lceil2eR_\sigma\rceil)\).

### Theorem 8.1 — finite nonlinear detection

False RH forces

\[
\boxed{e_k(A_\sigma)<0}
\]

for some

\[
\boxed{1\le k\le\max\!\left(1,\left\lceil2e{\|A_\sigma\|_1\over\eta}\right\rceil-1\right).}
\tag{FP.27}
\]

The Xi-cardinal vector gives

\[
\eta\ge{2m_z\over\|h_z\|_2^2}.
\tag{FP.28}
\]

Thus the full exterior algebra converts one hidden pair into a finite nonlinear certificate.

## 9. False RH has a finite prime-and-matrix witness

For trace-class \(A,B\), tensor telescoping gives

\[
|e_k(A)-e_k(B)|
\le k\max(\|A\|_1,\|B\|_1)^{k-1}\|A-B\|_1.
\tag{FP.29}
\]

Combine (FP.11), (FP.27), and (FP.29). Once \(e_k(A_\sigma)<0\), a sufficiently large finite cutoff \(P\) satisfies

\[
\boxed{e_k(A_{\sigma,P})<0.}
\tag{FP.30}
\]

Since every trace-class operator is approximated in trace norm by finite-rank compressions, choose increasing finite-rank projections \(P_M\to I\). Then

\[
\|P_MA_{\sigma,P}P_M-A_{\sigma,P}\|_1\to0.
\tag{FP.31}
\]

A second application of (FP.29) preserves the strict negative coefficient for all sufficiently large \(M\). Hence false RH has a genuinely finite arithmetic certificate:

```text
finite exterior degree k
+ finite prime cutoff P
+ finite Galerkin dimension M
+ strict outward-directed negative separation.
```

The matrix entries consist only of fixed Gamma/pole integrals and a finite prime-power sum.

## 10. All-order prime-cluster expansion

Write

\[
A_\sigma=A_{0,\sigma}+\sum_{n\ge2}B_{n,\sigma},\qquad
\sum_{n\ge2}\|B_{n,\sigma}\|_1<\infty,
\tag{FP.32}
\]

where

\[
B_{n,\sigma}=-{\Lambda(n)\over\sqrt n}
J_\sigma^*(T_{\log n}+T_{-\log n})J_\sigma.
\]

For each fixed \(j\),

\[
\boxed{
m_j
=\sum_{\nu_1,\ldots,\nu_j}
\operatorname{tr}(B_{\nu_1,\sigma}\cdots B_{\nu_j,\sigma})}
\tag{FP.33}
\]

absolutely, with \(B_{0,\sigma}=A_{0,\sigma}\). Newton's identities

\[
ke_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}m_j,\qquad e_0=1,
\tag{FP.34}
\]

then give an absolutely convergent noncommutative prime-cluster expansion for every exterior coefficient.

This escapes the support-one higher-moment ceiling of finite asymptotic Gabor compressions: every moment exists unconditionally because the Gaussian confinement supplies \(e^{-\sigma(\log n)^2/2}\). The difficulty is the **all-order sign**.

## 11. Exact remaining theorem

Two equivalent formulations remain.

### Fredholm/Lee–Yang target

\[
\boxed{D_\sigma(t)=\det(I+tA_\sigma)>0\qquad(t>0).}
\tag{FP.35}
\]

### Stieltjes target

\[
\boxed{H_d=(\operatorname{tr}A_\sigma^{i+j+1})_{0\le i,j\le d}\succeq0\qquad(d\ge0).}
\tag{FP.36}
\]

Either proves RH. False RH is guaranteed to fail at a finite degree, finite prime cutoff, and finite matrix dimension.

## 12. Honest boundary

Proposed complete here:

```text
Gaussian trace-class global Weil compression
super-convergent all-prime operator formula
exact negative index = distinct off-line pairs
Fredholm positive-axis criterion
exterior-coefficient criterion
shifted-Hankel/Stieltjes criterion
finite exterior-degree witness under false RH
finite prime-cutoff and Galerkin witness under false RH
all-order prime-cluster expansion
```

Still open:

```text
Fredholm determinant positivity from the prime side
or equivalently all shifted-Hankel matrices PSD
Riemann Hypothesis
```
