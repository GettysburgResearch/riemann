# High-carrier Fredholm firewall: every fixed nonlinear degree becomes positive

**Status:** proposed complete trace-class theorem; independent analytic review required.  
**RH status:** unproved.  
**Depends on:** the Gaussian Fredholm–Pontryagin operator of PR #373 and the Xi-cardinal capture theorem of PR #365.

## 1. Purpose

PR #373 replaces the finite two-trace compression by one global trace-class Weil operator whose complete exterior algebra detects every hypothetical off-line pair at a finite degree. A natural next attempt is to add a large carrier height and evaluate fixed exterior or Hankel degrees asymptotically, in analogy with the successful finite Gabor argument.

That attempt is structurally incapable of proving RH.

For every fixed exterior degree and every fixed shifted-Hankel degree, the high-carrier Gaussian-confined operator is eventually strictly positive at that degree **whether or not RH is true**. If RH is false, the degree needed to detect its negative spectrum must tend to infinity with the carrier.

This does not weaken the fixed global criterion of PR #373. It says that the all-order quantifier there is essential and cannot be replaced by any fixed nonlinear order followed by a high-height limit.

## 2. Modulated Gaussian confinement

Fix \(\sigma>0\), and retain

\[
w_\sigma(u)=e^{-\sigma u^2},
\qquad
R=(1-\partial_u^2)^{-1},
\qquad
J_\sigma=M_{w_\sigma}R.
\tag{HC.1}
\]

For a carrier \(T>0\), let

\[
(M_Tf)(u)=e^{iTu}f(u),
\qquad
J_{\sigma,T}=M_TJ_\sigma,
\tag{HC.2}
\]

and define the self-adjoint trace-class pullback

\[
\boxed{
\langle A_{\sigma,T}h,g\rangle
=Q_W(J_{\sigma,T}h,J_{\sigma,T}g).
}
\tag{HC.3}
\]

Exactly as in PR #373, every Xi-cardinal source lies in the range of \(J_{\sigma,T}\). Indeed, if \(q_z\) is one of the super-Gaussian cardinal sources, then

\[
h_{z,T}
=(1-\partial_u^2)
\left(\frac{e^{-iTu}q_z(u)}{w_\sigma(u)}\right)
\in L^2,
\qquad
J_{\sigma,T}h_{z,T}=q_z.
\tag{HC.4}
\]

Therefore

\[
\boxed{
n_-(A_{\sigma,T})
=\#\{\text{distinct nonreal reflected Xi-zero pairs}\}
}
\tag{HC.5}
\]

for every \(T\). The modulation changes magnitudes, not the exact index.

## 3. Carrier decomposition on the prime side

Put

\[
B_\sigma=J_\sigma^*J_\sigma\succeq0.
\tag{HC.6}
\]

The operator \(J_\sigma\) is injective and has infinite rank, so \(B_\sigma\) is positive trace class with infinitely many strictly positive eigenvalues.

Let

\[
\mu(\tau)
=\frac1{2\pi}\operatorname{Re}
\frac{\Gamma'}{\Gamma}
\left(\frac14+\frac{i\tau}{2}\right)
-\frac{\log\pi}{2\pi}
\tag{HC.7}
\]

be the archimedean density. Set

\[
c_T=\mu(T)
=\frac1{2\pi}\log\frac{T}{2\pi}+O(T^{-2}).
\tag{HC.8}
\]

### Lemma 3.1 — uniform archimedean remainder

As \(T\to\infty\),

\[
\boxed{
\left\|
J_{\sigma,T}^*M_\mu J_{\sigma,T}
-c_TB_\sigma
\right\|_1
\ll_\sigma1.
}
\tag{HC.9}
\]

### Proof

In Fourier variables, if \(U=\mathcal FJ_\sigma\), modulation translates the multiplier, so the left side of (HC.9) is

\[
U^*M_{g_T}U,
\qquad
g_T(\tau)=\mu(T+\tau)-\mu(T).
\]

Stirling's formula together with boundedness of \(\mu\) on compact intervals gives, uniformly for \(T\ge3\),

\[
|g_T(\tau)|
\ll1+\log(2+|\tau|).
\tag{HC.10}
\]

The Fourier kernel of \(U\) is a Gaussian convolution followed by the multiplier \((1+\xi^2)^{-1}\). Hence

\[
\bigl\||g_T|^{1/2}U\bigr\|_{HS}^2
\ll_\sigma
\iint
\frac{(1+\log(2+|\tau|))
 |\widehat w_\sigma(\tau-\xi)|^2}
 {(1+\xi^2)^2}
\,d\tau d\xi
<\infty
\tag{HC.11}
\]

with a bound independent of \(T\). Since

\[
\|U^*M_{g_T}U\|_1
\le\bigl\||g_T|^{1/2}U\bigr\|_{HS}^2,
\]

(HC.9) follows. ∎

The prime translations acquire only phases:

\[
M_T^*T_yM_T=e^{-iTy}T_y.
\tag{HC.12}
\]

Therefore the trace-norm bound of PR #373 is unchanged, and

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left\|
J_\sigma^*
\bigl(e^{-iT\log n}T_{\log n}
     +e^{iT\log n}T_{-\log n}\bigr)
J_\sigma
\right\|_1
\ll_\sigma1
\tag{HC.13}
\]

uniformly in \(T\). The two pole evaluation vectors are shifted to real frequency \(T\) and have norm \(O_\sigma((1+T^2)^{-1})\), so their finite-rank contribution is uniformly bounded as well.

Combining these facts with the explicit formula gives:

### Theorem 3.2 — positive leading operator

There are self-adjoint trace-class operators \(E_{\sigma,T}\) such that

\[
\boxed{
A_{\sigma,T}=c_TB_\sigma+E_{\sigma,T},
\qquad
\sup_{T\ge3}\|E_{\sigma,T}\|_1<\infty.
}
\tag{HC.14}
\]

Consequently

\[
\boxed{
\frac{A_{\sigma,T}}{c_T}
\longrightarrow B_\sigma
\quad\text{in trace norm.}
}
\tag{HC.15}
\]

In particular

\[
\|(A_{\sigma,T})_-\|_1
\le\|E_{\sigma,T}\|_1
\ll_\sigma1,
\tag{HC.16}
\]

while

\[
\|A_{\sigma,T}\|_1
=c_T\operatorname{tr}B_\sigma+O_\sigma(1)
\asymp_\sigma\log T.
\tag{HC.17}
\]

Thus a false-RH negative sector can persist only as a bounded trace-mass defect inside a positive trace mass growing like \(\log T\).

## 4. Every fixed exterior degree is eventually positive

For trace-class operators, the elementary symmetric functional

\[
e_k(A)=\operatorname{tr}(\wedge^kA)
\]

is continuous in trace norm and homogeneous of degree \(k\). Equation (HC.15) therefore gives, for every fixed \(k\ge1\),

\[
\boxed{
\frac{e_k(A_{\sigma,T})}{c_T^k}
\longrightarrow e_k(B_\sigma).
}
\tag{HC.18}
\]

Because \(B_\sigma\) has infinite rank and all its nonzero eigenvalues are positive,

\[
e_k(B_\sigma)>0
\qquad(k\ge1).
\tag{HC.19}
\]

Hence:

### Theorem 4.1 — fixed exterior-degree blindness

For every fixed \(k\), there is \(T_k(\sigma)\) such that

\[
\boxed{
e_k(A_{\sigma,T})>0\qquad(T\ge T_k(\sigma))}
\tag{HC.20}
\]

without assuming RH.

If RH is false, PR #373 guarantees that for each \(T\) **some** exterior coefficient is negative. Theorem 4.1 forces the first such degree to satisfy

\[
\boxed{k_*(T)\longrightarrow\infty.}
\tag{HC.21}
\]

## 5. Every fixed shifted-Hankel degree is eventually positive

Put

\[
m_j(T)=\operatorname{tr}(A_{\sigma,T}^j),
\qquad
H_d(T)=(m_{i+j+1}(T))_{0\le i,j\le d}.
\tag{HC.22}
\]

For the diagonal scaling

\[
D_T=\operatorname{diag}
(c_T^{-1/2},c_T^{-3/2},\ldots,c_T^{-d-1/2}),
\tag{HC.23}
\]

trace-norm convergence and continuity of fixed powers give

\[
\boxed{
D_TH_d(T)D_T
\longrightarrow
H_d(B_\sigma)
=(\operatorname{tr}B_\sigma^{i+j+1})_{0\le i,j\le d}.
}
\tag{HC.24}
\]

For a nonzero polynomial \(p\) of degree at most \(d\),

\[
c^*H_d(B_\sigma)c
=\sum_j\lambda_j(B_\sigma)|p(\lambda_j(B_\sigma))|^2>0,
\tag{HC.25}
\]

because the infinitely many positive eigenvalues of \(B_\sigma\) cannot all be zeros of one nonzero polynomial. Hence \(H_d(B_\sigma)\) is positive definite.

### Theorem 5.1 — fixed Hankel-degree blindness

For every fixed \(d\),

\[
\boxed{H_d(T)\succ0}
\tag{HC.26}
\]

for all sufficiently large \(T\), independently of RH. Under false RH the first indefinite shifted-Hankel degree must therefore tend to infinity.

## 6. Fredholm zeros escape every fixed normalized compact set

Define

\[
\mathcal D_{\sigma,T}(s)
=\det\left(I+s\frac{A_{\sigma,T}}{c_T}\right).
\tag{HC.27}
\]

Trace-norm continuity of the Fredholm determinant gives locally uniformly in \(s\),

\[
\boxed{
\mathcal D_{\sigma,T}(s)
\longrightarrow
\det(I+sB_\sigma)>0
\qquad(s>0).
}
\tag{HC.28}
\]

Thus if RH is false, the positive-axis Fredholm zeros of \(A_{\sigma,T}\), expressed in the normalized coordinate \(s=c_Tt\), escape every compact subset of \((0,\infty)\).

This is the determinant version of (HC.21) and (HC.26).

## 7. Consequence for the full-proof strategy

The high-carrier limit recreates the same density-dilution phenomenon that the finite Gabor method encounters:

```text
positive archimedean bulk        grows like log T;
complete false-RH negative mass  stays O(1);
any fixed exterior/Hankel degree reads only the bulk asymptotically.
```

Therefore the following programme is closed:

```text
choose one fixed nonlinear degree k or d;
let the carrier height T tend to infinity;
prove its asymptotic positivity from primes;
conclude RH.
```

That asymptotic positivity is true even if RH is false.

The viable Fredholm routes are instead:

1. fix one carrier (for example \(T=0\)) and prove the **entire** determinant positive;
2. allow exterior/Hankel degree to grow with carrier height and retain quantitative control uniform in that growing degree;
3. isolate an off-line pair before taking the high-carrier limit, rather than burying it in the archimedean bulk.

The all-order quantifier in PR #373 is not cosmetic. It is the exact resource that escapes the finite-statistic ceiling.

## 8. Proof boundary

Proposed complete here:

```text
modulated Gaussian operator keeps exact negative index
A_(sigma,T)=mu(T) B_sigma+O_1(1) in trace norm
negative trace mass is uniformly bounded
all fixed exterior degrees eventually positive
all fixed shifted-Hankel degrees eventually positive
normalized Fredholm zeros escape compact positive-axis sets
```

Still open:

```text
one fixed-carrier all-order determinant positivity
or growing-degree positivity uniform in carrier
Riemann Hypothesis
```
