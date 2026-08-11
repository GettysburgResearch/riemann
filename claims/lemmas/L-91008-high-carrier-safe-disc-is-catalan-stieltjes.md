# L-91008 — The high-carrier safe-disc limit is a Catalan Stieltjes law

Claim ID: `L-91008`  
Status: **PROPOSED COMPLETE ASYMPTOTIC / STIELTJES LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91003`, `L-91004`, the absolutely convergent Euler expansion in `Re(s)>1`, and Stirling's formula  
RH status: **unproved**

## 1. Setup

Fix a real carrier `x` and put

\[
 s_x=\frac12+ix,
 \qquad
 \ell_x=\log(2+|x|).
\]

Let

\[
 \mathscr X(s)=-\frac{\xi'}{\xi}(s)
\]

and let `A_x(w)` be the one-safe-line generating function of `T-91001` and `L-91003`. With

\[
 r_w=\sqrt{1-w},
 \qquad r_0=1,
\]

that formula is

\[
 \mathcal A_x(w)
 =-\frac12\bigl(\mathcal G_{s_x}(w)+\mathcal G_{\overline{s_x}}(w)\bigr),
\]

where

\[
 \mathcal G_s(w)
 =\frac{
 (2-w)\mathscr X(s+1)
 -w\mathscr X'(s+1)
 -2r_w\mathscr X(s+r_w)
 }{w^2}.
\tag{L-91008.1}
\]

The apparent singularity at `w=0` is removable.

Define the universal function

\[
 \boxed{
 \Phi(w)=\frac1{2(1+\sqrt{1-w})^2}.
 }
\tag{L-91008.2}
\]

The lemma proves that `ell_x Phi` is the complete high-carrier background of `A_x` throughout the direct absolute-Euler disc.

## 2. Uniform high-carrier asymptotic on safe circles

For

\[
 \frac12\le R<\frac34,
\]

put

\[
 \delta_R=\sqrt{1-R}-\frac12>0.
\tag{L-91008.3}
\]

### Theorem 2.1

There is an absolute constant `C` such that, for all sufficiently large `|x|`,

\[
 \boxed{
 \max_{|w|=R}
 \left|
 \mathcal A_x(w)-\ell_x\Phi(w)
 \right|
 \le C\left(1+\delta_R^{-1}\right).
 }
\tag{L-91008.4}
\]

Consequently, for every fixed `R<3/4`,

\[
 \boxed{
 \frac{\mathcal A_x(w)}{\ell_x}
 \longrightarrow \Phi(w)
 }
\tag{L-91008.5}
\]

locally uniformly on `|w|<R` as `|x|->infinity`.

### Proof

On `|w|=R`, the principal square root satisfies

\[
 \Re r_w
 =\sqrt{\frac{|1-w|+\Re(1-w)}2}
 \ge\sqrt{1-R}
 =\frac12+\delta_R.
\tag{L-91008.6}
\]

Hence

\[
 \Re(s_x+r_w)\ge1+\delta_R.
\]

In `Re(s)>1`,

\[
\begin{aligned}
 \mathscr X(s)
 ={}&\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
 -\frac1s-\frac1{s-1}
 +\frac12\log\pi
 -\frac12\frac{\Gamma'}{\Gamma}(s/2).
\end{aligned}
\tag{L-91008.7}
\]

Stirling's formula and absolute convergence therefore give, uniformly on the circle,

\[
\begin{aligned}
 \mathscr X(s_x+1)&=-\frac12\ell_x+O(1),\\
 \mathscr X'(s_x+1)&=O(1),\\
 \mathscr X(s_x+r_w)&=-\frac12\ell_x
   +O\left(1+\delta_R^{-1}\right).
\end{aligned}
\tag{L-91008.8}
\]

For the last line use

\[
 \sum_{n\ge2}\Lambda(n)n^{-1-\delta_R}
 =-\frac{\zeta'}{\zeta}(1+\delta_R)
 \ll1+\delta_R^{-1}.
\]

Insert (L-91008.8) in (L-91008.1). The leading numerator is

\[
 -\frac{\ell_x}{2}
 \bigl[(2-w)-2r_w\bigr].
\]

Since

\[
 2-w=1+r_w^2,
 \qquad
 (2-w)-2r_w=(1-r_w)^2,
 \qquad
 w^2=(1-r_w)^2(1+r_w)^2,
\]

its quotient is

\[
 -\frac{\ell_x}{2(1+r_w)^2}.
\]

Averaging the `s_x` and `conj(s_x)` expressions gives `ell_x Phi(w)`. On the circle `|w|=R>=1/2`, all remaining rational prefactors are uniformly bounded, proving (L-91008.4). The difference is analytic inside the circle, so the maximum principle gives (L-91008.5). `square`

## 3. Exact Catalan coefficients

The function `Phi` has the expansion

\[
 \boxed{
 \Phi(w)=\sum_{k\ge0}c_k w^k,
 \qquad
 c_k=\frac{C_{k+1}}{8\,4^k},
 }
\tag{L-91008.9}
\]

where

\[
 C_n=\frac1{n+1}\binom{2n}{n}
\]

is the `n`th Catalan number.

Indeed,

\[
 \frac1{1+\sqrt{1-w}}
 =\frac{1-\sqrt{1-w}}w
 =\frac12\,C(w/4),
\]

where `C(z)=sum_(n>=0) C_n z^n` is the Catalan generating function. Thus

\[
 \Phi(w)=\frac18 C(w/4)^2,
\]

and `C(z)^2=sum_(k>=0) C_(k+1)z^k`.

Stirling gives

\[
 \boxed{
 c_k\sim\frac1{2\sqrt\pi}\,k^{-3/2}.
 }
\tag{L-91008.10}
\]

## 4. Exact Stieltjes measure

The same function is the Stieltjes transform

\[
 \boxed{
 \Phi(w)
 =\int_0^1\frac{d\nu(\lambda)}{1-w\lambda},
 \qquad
 d\nu(\lambda)
 =\frac1\pi\sqrt{\lambda(1-\lambda)}\,d\lambda.
 }
\tag{L-91008.11}
\]

Indeed,

\[
 \int_0^1\lambda^k\,d\nu(\lambda)
 =\frac1\pi B\left(k+\frac32,\frac32\right)
 =\frac{C_{k+1}}{8\,4^k}=c_k.
\tag{L-91008.12}
\]

Thus the high-carrier background is not merely positive coefficientwise: it is a strict Hausdorff moment sequence and a Stieltjes/Pick function.

For its Pick kernel,

\[
 \boxed{
 \frac{\Phi(z)-\overline{\Phi(\zeta)}}
 {z-\overline\zeta}
 =\int_0^1
 \frac{\lambda\,d\nu(\lambda)}
 {(1-z\lambda)(1-\overline\zeta\lambda)}.
 }
\tag{L-91008.13}
\]

Every finite Pick matrix is positive semidefinite, and it is positive definite at distinct nodes because `nu` has a density on an interval.

## 5. Quantitative coefficient remainder

Write

\[
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k.
\]

Cauchy's estimate and (L-91008.4) give, for every `1/2<=R<3/4`,

\[
 \boxed{
 |a_k(x)-\ell_xc_k|
 \le C\left(1+\delta_R^{-1}\right)R^{-k}.
 }
\tag{L-91008.14}
\]

Choose

\[
 R_k=\frac34-\frac1{k+4}.
\tag{L-91008.15}
\]

Then

\[
 \delta_{R_k}^{-1}\ll k+4,
 \qquad
 R_k^{-k}\ll\left(\frac43\right)^k.
\]

Therefore

\[
 \boxed{
 |a_k(x)-\ell_xc_k|
 \ll(k+4)\left(\frac43\right)^k.
 }
\tag{L-91008.16}
\]

The estimate is uniform in the real carrier once `|x|` is sufficiently large.

## 6. Fixed safe-disc Pick tests are asymptotically universal

Let `z_1,...,z_m` be distinct fixed points in `|z|<R<3/4`. Local uniform convergence in (L-91008.5) implies that the Pick matrix of `A_x/ell_x` converges entrywise to the strictly positive Pick matrix of `Phi`.

Likewise, every fixed shifted Hausdorff or Hankel matrix built from the coefficients `a_k(x)/ell_x` converges to the corresponding Gram matrix of the beta density in (L-91008.11).

Hence every fixed finite test wholly inside the direct safe disc is eventually strictly positive at high carrier, independently of RH.

## 7. A sign-transfer interface at the annular boundary

For real `w`, put `r=sqrt(1-w)`. Formula (L-91008.1) shows that annular real-ray positivity follows from one sublogarithmic estimate:

\[
 \mathscr X(s_x+r)+\frac12\ell_x=o(\ell_x)
\tag{L-91008.17}
\]

uniformly in the desired range of `r<1/2`; the two fixed samples at `s_x+1` already have `O(1)` remainders.

Under (L-91008.17),

\[
 \mathcal A_x(w)=\ell_x\Phi(w)+o(\ell_x)>0.
\tag{L-91008.18}
\]

The classical zero-free region in `L-91007` supplies holomorphy beyond `w=3/4`, but this file does not silently upgrade that holomorphy to the sublogarithmic logarithmic-derivative estimate (L-91008.17). The latter is the exact additional sign input.

## 8. Boundary

Established here:

```text
high-carrier safe-disc asymptotic              PROPOSED COMPLETE
universal limiting function Phi                EXACT
Catalan coefficient law                        EXACT
beta(3/2,3/2) Stieltjes measure                EXACT
strict limiting Pick/Hausdorff/Hankel geometry EXACT
quantitative coefficient remainder             PROPOSED COMPLETE
fixed safe-disc tests eventually positive      PROPOSED COMPLETE
annular sign reduced to one sublog Xcal bound  EXACT INTERFACE
```

Not established here:

```text
sublogarithmic Xcal control inside Re(s)<1;
Pick/Stieltjes positivity through 3/4<|w|<1;
radial curvature positivity on 0<t<1/4;
Riemann Hypothesis.
```