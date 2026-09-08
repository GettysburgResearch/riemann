# L-91405 — The beta-binomial shadow has an exact Hahn spectrum and a uniform two-moment resolvent

Claim ID: `L-91405`  
Status: **EXACT FINITE SPECTRAL THEOREM**  
Created: 2026-08-12  
Depends on: the beta-binomial shadow law of `L-91403`  
RH status: **unproved**

## 1. Reversible shadow chain

For an integer `N>=1`, put

\[
 \pi_N(k)=\frac{6(k+1)(N-k+1)}{(N+1)(N+2)(N+3)},
 \qquad 0\le k\le N,
\]

\[
 \lambda_k=(k+2)(N-k),
 \qquad
 \mu_k=k(N-k+2),
\]

and

\[
 (\mathcal L_Nf)(k)=\frac14\bigl[
 \lambda_k(f(k+1)-f(k))+
 \mu_k(f(k-1)-f(k))
 \bigr],
\]

with missing boundary terms omitted. Detailed balance gives

\[
 \pi_N(k)\lambda_k=\pi_N(k+1)\mu_{k+1}.
\]

Hence `L_N` is self-adjoint and nonpositive in `L^2(pi_N)`, with

\[
 \mathcal E_N(f,f)
 :=-\langle f,\mathcal L_Nf\rangle_{\pi_N}
 =\frac14\sum_{k=0}^{N-1}
 \pi_N(k)\lambda_k|f(k+1)-f(k)|^2.
\tag{L-91405.1}
\]

## 2. Exact spectrum

The polynomial flag of degree at most `j` is invariant under `L_N`. For a monic polynomial of degree `j`, direct expansion gives

\[
 \mathcal L_N k^j
 =-\frac{j(j+3)}4 k^j+
 \text{a polynomial of degree at most }j-1.
\tag{L-91405.2}
\]

Indeed, the degree-`j+1` terms cancel between the forward and backward differences; the surviving degree-`j` coefficient is

\[
 \frac14[-4j-j(j-1)]=-rac{j(j+3)}4.
\]

Self-adjointness now implies that the monic orthogonal polynomial of degree `j` is an eigenfunction. Therefore

\[
 \boxed{
 \operatorname{Spec}(-\mathcal L_N)
 =\left\{\frac{j(j+3)}4:0\le j\le N\right\}.
 }
\tag{L-91405.3}
\]

These are the Hahn/Jacobi shadow eigenvalues, independent of `N`.

## 3. First two nonconstant modes

Put

\[
 X_N(k)=k-\frac N2,
 \qquad
 v_N=\operatorname{Var}_{\pi_N}(K)
 =\frac{N(N+4)}{20},
\]

and, for `N>=2`,

\[
 H_{2,N}(k)=X_N(k)^2-v_N.
\]

Symmetry of `pi_N` makes `1`, `X_N`, and `H_(2,N)` mutually orthogonal. Equation (L-91405.3) gives

\[
 \boxed{
 -\mathcal L_NX_N=X_N,
 \qquad
 -\mathcal L_NH_{2,N}=\frac52H_{2,N}.
 }
\tag{L-91405.4}
\]

## 4. Uniform Poincare and two-moment gaps

For every `f` with mean zero,

\[
 \boxed{
 \|f\|_{L^2(\pi_N)}^2\le\mathcal E_N(f,f).
 }
\tag{L-91405.5}
\]

If in addition

\[
 \langle f,X_N\rangle_{\pi_N}=0,
\]

then

\[
 \boxed{
 \frac52\|f\|_{L^2(\pi_N)}^2
 \le\mathcal E_N(f,f).
 }
\tag{L-91405.6}
\]

The constants `1` and `5/2` are sharp.

Equivalently, if a source `g` is orthogonal to the constant and linear modes and `h` is the zero-mean solution of

\[
 -\mathcal L_Nh=g,
\]

then

\[
 \boxed{
 \|h\|_2\le\frac25\|g\|_2,
 \qquad
 \mathcal E_N(h,h)
 =\langle g,(-\mathcal L_N)^{-1}g\rangle
 \le\frac25\|g\|_2^2.
 }
\tag{L-91405.7}
\]

Thus every two-moment-neutral finite shadow has a uniformly bounded adjacent-butterfly Poisson solution. No dimension-dependent coercivity loss occurs.

## 5. Relevance to the three fronts

- The factor-54 endpoint butterflies cancel the constant and linear endpoint moments, so their natural Hilbert shadow starts at the sharp `5/2` sector.
- The final Cauchy/Jordan numerator removes the same low-order Green data; any faithful finite shadow should therefore be tested in this two-moment complement.
- The Brownian Beta(2,2) reservoir is the continuum limit of this chain, with the same eigenvalues.

This theorem supplies coercivity, not coefficientwise positivity. A positive endpoint allocation or a source-specific boundary identity remains necessary.
