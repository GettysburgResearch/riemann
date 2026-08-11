# T-91003 — Safe-disc positivity reaches the sharp growing Catalan-jet scale

Claim ID: `T-91003`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PARTIAL-SIGN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`, `T-91001`, `T-91002`  
RH status: **unproved**

## 1. Statement on the real safe ray

Let

\[
 \ell_x=\log(2+|x|)
\]

and let `A_x(w)` be the one-safe-line generator. There are effective constants `C_0>0` and `X_0>0` such that

\[
 \boxed{
 \mathcal A_x(w)>0
 }
\tag{T-91003.1}
\]

whenever

\[
 |x|\ge X_0,
 \qquad
 0\le w\le\frac34-\frac{C_0}{\ell_x}.
\tag{T-91003.2}
\]

Equivalently, with `t=1-w`, the radial tangent defect of `L-91004` satisfies

\[
 \boxed{
 J_x(1)+J_x'(1)(t-1)-J_x(t)>0
 }
\tag{T-91003.3}
\]

throughout

\[
 \frac14+\frac{C_0}{\ell_x}
 \le t\le1.
\tag{T-91003.4}
\]

This is an unconditional sign theorem approaching the direct-Euler boundary `w=3/4` at distance `O(1/log|x|)`. It does not cross into the RH-detecting annulus.

## 2. Proof of real-ray positivity

By `L-91008`,

\[
 \mathcal A_x(w)=\ell_x\Phi(w)+E_x(w),
 \qquad
 \Phi(w)=\frac1{2(1+\sqrt{1-w})^2}.
\tag{T-91003.5}
\]

On `0<=w<=3/4`,

\[
 \Phi(w)\ge\Phi(0)=\frac18.
\tag{T-91003.6}
\]

For `1/2<=w<3/4`, put

\[
 \delta_w=\sqrt{1-w}-\frac12.
\]

Then

\[
 \delta_w
 =\frac{3/4-w}{\sqrt{1-w}+1/2}
 \gg \frac34-w.
\tag{T-91003.7}
\]

The circle estimate of `L-91008` and the maximum principle give

\[
 |E_x(w)|\ll1+\delta_w^{-1}
 \ll1+\left(\frac34-w\right)^{-1}.
\tag{T-91003.8}
\]

If `3/4-w>=C_0/ell_x`, then

\[
 |E_x(w)|\le\frac1{16}\ell_x
\]

once `C_0` is chosen sufficiently large. Equations (T-91003.5) and (T-91003.6) give positivity. On `0<=w<=1/2`, use the fixed-disc asymptotic of `L-91008`. This proves (T-91003.1).

The tangent-defect form follows from

\[
 \mathcal A_x(1-t)
 =\frac4{(1-t)^2}
 \left[J_x(1)+J_x'(1)(t-1)-J_x(t)\right].
\]

## 3. Pointwise positivity of growing safe-line orders

Write

\[
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k
\]

and

\[
 c_k=\frac{C_{k+1}}{8\,4^k}.
\]

The quantitative coefficient estimate in `L-91008` is

\[
 |a_k(x)-\ell_xc_k|
 \ll(k+4)\left(\frac43\right)^k.
\tag{T-91003.9}
\]

Since

\[
 c_k\gg(k+1)^{-3/2},
\]

we obtain the explicit sufficient condition

\[
 \boxed{
 \left(\frac43\right)^k(k+1)^{5/2}
 \le c\,\ell_x
 \quad\Longrightarrow\quad
 a_k(x)>0.
 }
\tag{T-91003.10}
\]

In particular, for every fixed `epsilon>0`,

\[
 \boxed{
 a_k(x)>0
 }
\tag{T-91003.11}
\]

uniformly for all sufficiently large `|x|` and all integers

\[
 0\le k\le
 \left(
 \frac1{\log(4/3)}-\varepsilon
 \right)
 \log\ell_x.
\tag{T-91003.12}
\]

The critical numerical constant is

\[
 \boxed{
 \frac1{\log(4/3)}
 =3.4760594967822069\ldots.
 }
\tag{T-91003.13}
\]

Thus the single-safe-line hierarchy is unconditionally positive pointwise through a growing order of size `3.476... log log |x|`, up to an arbitrary fixed proportional loss.

## 4. Growing Hausdorff finite differences

For integers `k,m>=0`, define

\[
 D_{k,m}(x)=(-1)^m\Delta^m a_k(x)
 =\sum_{j=0}^m(-1)^j\binom mj a_{k+j}(x).
\tag{T-91003.14}
\]

The Catalan Stieltjes law gives the positive main term

\[
 d_{k,m}
 =\int_0^1\lambda^k(1-\lambda)^m\,d\nu(\lambda)
 =\frac1\pi
 B\left(k+\frac32,m+\frac32\right).
\tag{T-91003.15}
\]

For each fixed `m`,

\[
 d_{k,m}\asymp_m(k+1)^{-m-3/2}.
\]

Applying (T-91003.9) to the `m+1` terms gives

\[
 \boxed{
 D_{k,m}(x)
 =\ell_xd_{k,m}
 +O_m\left((k+4)\left(\frac43\right)^k\right).
 }
\tag{T-91003.16}
\]

Hence

\[
 \boxed{
 \left(\frac43\right)^k
 (k+1)^{m+5/2}
 \le c_m\ell_x
 \quad\Longrightarrow\quad
 D_{k,m}(x)>0.
 }
\tag{T-91003.17}
\]

For every fixed finite-difference order `m` and every `epsilon>0`, positivity therefore holds uniformly throughout the same leading range

\[
 k\le
 \left(
 \frac1{\log(4/3)}-\varepsilon
 \right)
 \log\ell_x.
\tag{T-91003.18}
\]

This is a growing-order partial Hausdorff theorem, not only coefficientwise positivity.

## 5. Fixed Pick and Hankel packets

Let `z_1,...,z_d` be distinct fixed nodes in `|z|<R<3/4`. The Pick matrix of `A_x/ell_x` converges to

\[
 \left(
 \int_0^1
 \frac{\lambda\,d\nu(\lambda)}
 {(1-z_i\lambda)(1-\overline{z_j}\lambda)}
 \right)_{i,j},
\tag{T-91003.19}
\]

which is positive definite. Therefore every such fixed Pick matrix is positive definite for all sufficiently large `|x|`.

The same holds for every fixed Hausdorff, shifted Hankel, or Bernstein packet built from the normalized coefficients.

## 6. Exact scope

This theorem is genuinely unconditional at its declared scope: it uses only Stirling and absolutely convergent Euler series in `Re(s)>1`.

It does not imply RH. The RH-detecting poles of `A_x` lie in

\[
 \frac34<w<1,
\]

and the growing-order theorem stops at the exact asymptotic scale at which a pole approaching `w=3/4` can first compete with the gamma background.

## 7. Boundary

```text
real safe-ray positivity to 3/4-C/log|x|           PROPOSED COMPLETE
radial tangent-defect positivity outside the wall   PROPOSED COMPLETE
coefficient positivity to (1/log(4/3)-eps)loglog|x| PROPOSED COMPLETE
fixed-order Hausdorff differences in same range     PROPOSED COMPLETE
fixed safe-disc Pick/Hankel packets eventually PSD  PROPOSED COMPLETE
positivity in 3/4<w<1                               OPEN / RH-EQUIVALENT
cofinal Hausdorff/Pick positivity                    OPEN / RH-EQUIVALENT
radial curvature positivity on 0<t<1/4              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```