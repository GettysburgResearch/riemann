# 06 — Reflection rigidity, Ramanujan coordinates, and the two-norm trap

Source U6/A6; the complete original proof and exact checker are retained in
stage 04. Status: proposed component proofs, imported background, and explicit
refutations. No source-smallness or bounded reflection theorem is proved.

## The operator version of the user's rigidity proposal

Set f(0)=0 and (D_m f)(k)=f(floor(k/m)). Telescoping blocks proves exactly

$$
\|D_m f\|^2=\|f\|^2/m,\qquad D_m b_n=b_{mn}-b_m/n.
$$

Thus B is invariant under D_m and B-perp under D_m^*. On B-perp,
C_m=sqrt(m)D_m^* is a contraction. Its kernel eigenvectors satisfy

$$
C_m h_\rho=m^{1/2-\bar\rho}h_\rho.
$$

An off-line zero on the right yields modulus m^{-delta}<1. A bounded symmetry
forcing a reciprocal-conjugate eigenvalue on the SAME defect space would
contradict contractivity. But the functional equation supplies only the
reflected zero rho*=1-conj(rho). Its formal kernel is not in H:

$$
\sum_{k\le K}|h_{\rho^*}(k)|^2/[k(k+1)]
\sim |\rho^*|^2K^{2\delta}/(2\delta).
$$

Evaluation on each bounded b_n can still converge; it does not extend to a
bounded functional on all H. No bounded defect-space duality was constructed.
Reflecting xi(s)A(s) merely preserves the common zero factor. Burnol's scattering
work [SC00] is a relevant precedent, not a supplied unconditional compatibility
theorem. The proposed expanding-eigenvalue contradiction is only the endpoint
of an unproved operator construction.

## The exact Ramanujan change of basis

Put b_1=0 and

$$
s_d=\sum_{n\mid d}\mu(d/n)n b_n,\qquad
n b_n=\sum_{d\mid n,d\ge2}s_d.
$$

The finite spans are identical. If c_d(k) is the classical Ramanujan sum, then
s_d(k)-s_d(k-1)=-c_d(k), so s_d(k)=-sum_{j<=k}c_d(j). Periodic residue arithmetic
gives

$$
M_{\rm per}(s_d)=\phi(d)/2,\quad
\operatorname{Cov}_{\rm per}(s_d,s_e)=\delta_{de}J_2(d)/12.
$$

For A=sum y_d s_d,

$$
M_{\rm per}(|1-A|^2)
=|1-\tfrac12\sum\phi(d)y_d|^2+\tfrac1{12}\sum J_2(d)|y_d|^2.
$$

These are exact arithmetic positivity statements, without zeta-zero hypotheses.
But the actual weighted source is

$$
\langle1,s_d\rangle=\sum_{n\mid d}\mu(d/n)\log n=\Lambda(d),
$$

zero unless d is a prime power. It is not phi(d)/2.

## A finite refutation of mixing the two metrics

For s_2,s_3 the periodic Gram is [[1/2,1/2],[1/2,5/3]]. Combining it with the
actual source (log 2,log 3) gives

$$
\lambda^TR^{-1}\lambda=
(20\log^22-12\log2\log3+6\log^23)/7\in(1.1018,1.1019).
$$

The resulting supposed squared distance 1-lambda^T R^{-1}lambda is negative.
The retained checker certifies the interval with a rational atanh expansion of
log, not a floating sign test. This refutes replacing the metric while keeping
the original source; it does not refute every use of GCD matrices.

## An all-cutoff separation theorem

Let Theta_N=sum_{d=2}^N phi(d)^2/J_2(d), D_N^per=1+3Theta_N. The periodic optimum
has coefficients y_d^per=6phi(d)/(J_2(d)D_N^per) and error 1/D_N^per. An elementary
divisor expansion gives Theta_N=kappa N+O((1+log N)^2), where

    kappa=product_p(1-2/[p(p+1)])>0.

Thus its periodic error tends to zero at order 1/N. In the b basis the SAME
approximant has

    c_n^per=n sum_{j<=N/n}mu(j)y_{nj}^per,
    |c_n^per|<=6H_{floor(N/n)}/D_N^per.

Its l1 coefficient sum is O(1), it tends to zero at every fixed coordinate,
and dominated convergence in H gives

$$
\|A_N^{\rm per}\|_H\to0,\qquad\|1-A_N^{\rm per}\|_H^2\to1.
$$

The retained proof even bounds ||A_N^per||^2=O(1/N). Consequently perfect
periodic approximation can coexist with complete failure in the RH-weighted
norm. Periodic averages may help estimate tails, but cannot stand in for the
weighted geometry.

## Correct source-aware Schur elimination

Retain K_N(d,e)=<s_d,s_e> and lambda_d=Lambda(d). Partition into prime powers P
and the remaining composite indices C. Since lambda_C=0, block inversion gives

$$
K^{\rm eff}=K_{PP}-K_{PC}K_{CC}^{-1}K_{CP},\qquad
E_N=1-\lambda_P^T(K^{\rm eff})^{-1}\lambda_P.
$$

This is elimination, NOT deletion: composite effects remain in the Schur term.
With H^eff=K^eff-lambda_P lambda_P^T, which is positive definite in finite
sections,

$$
E_N=\frac1{1+\lambda_P^T(H^{\rm eff})^{-1}\lambda_P}.
$$

Divergence of the inverse-source energy would finish the approximation route;
it is unproved. Nonnegative energy is not divergent energy. The new-block source
is lambda_new-K_new,old K_old,old^{-1}lambda_old, not simply the list of new primes.

## The weighted rational-frequency correlations that GCD averaging erases

Write e(theta)=exp(2*pi*i*theta). Then

$$
s_d(k)=\phi(d)/2+
\sum_{1\le a<d,(a,d)=1}\frac{e(a/d)}{1-e(a/d)}e(ak/d).
$$

The weighted Fourier kernel is

$$
W_H(\theta)=\sum_{k\ge1}\frac{e(k\theta)}{k(k+1)}
=1+(e(-\theta)-1)\log(1-e(\theta)),\quad W_H(0)=1,
$$

with the logarithm's radial limit from inside the unit disk. Period averaging
keeps only equal frequencies; the H-norm retains the full matrix
W_H(theta-eta). This matrix is positive semidefinite, but its entries need not
be positive: W_H(1/2)=1-2log2<0. In fact

$$
\Lambda(d)=\phi(d)/2+
\sum_{1\le a<d,(a,d)=1}\frac{e(a/d)}{1-e(a/d)}W_H(a/d).
$$

For a non-prime-power d the oscillatory term cancels the mean exactly. Those
correlations carry the arithmetic distinction the proposed periodic shortcut
would lose. W_H is not the cotangent sum W(a,b) from Chapter 03.

For the logarithmic mollifier,

    y_{N,d}=-sum_{j<=N/d} mu(dj)/(dj) [1-log(dj)/log N],
    Q_N=1-2sum_d y_{N,d}Lambda(d)+sum_{d,e}y_{N,d}y_{N,e}K_N(d,e).

No subpolynomial upper estimate for this correctly weighted quadratic form was
proved. Chapter 07 adds support rigidity and a full norm decomposition, not a
license to discard these correlations.
