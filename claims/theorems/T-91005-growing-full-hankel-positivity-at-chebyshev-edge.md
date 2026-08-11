# T-91005 — The complete safe-line Hankel matrix is positive through the sharp Chebyshev edge scale

Claim ID: `T-91005`  
Status: **PROPOSED COMPLETE UNCONDITIONAL GROWING-MATRIX THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91003`, `L-91008`, `L-91010`  
RH status: **unproved**

## 1. Statement

Write

\[
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k,
 \qquad
 \ell_x=\log(2+|x|),
\]

and form the complete degree-`n` Hankel matrix

\[
 H_n(x)=\bigl(a_{i+j}(x)\bigr)_{0\le i,j\le n}.
\tag{T-91005.1}
\]

Let

\[
 Q_x[p]
 =\sum_{i,j=0}^n\overline{u_i}u_j a_{i+j}(x),
 \qquad
 p(\lambda)=\sum_{j=0}^nu_j\lambda^j.
\tag{T-91005.2}
\]

Then there is an absolute constant `C` such that, for all sufficiently large `|x|`, every `n>=1`, and every polynomial of degree at most `n`,

\[
 \boxed{
 \left|Q_x[p]-\ell_xQ_\nu[p]\right|
 \le C(n+4)^7 9^n Q_\nu[p],
 }
\tag{T-91005.3}
\]

where

\[
 Q_\nu[p]
 =\int_0^1|p(\lambda)|^2
   \frac1\pi\sqrt{\lambda(1-\lambda)}\,d\lambda.
\]

Consequently

\[
 \boxed{
 Q_x[p]\ge
 \left[\ell_x-C(n+4)^7 9^n\right]Q_\nu[p].
 }
\tag{T-91005.4}
\]

In particular, for every fixed `epsilon>0`,

\[
 \boxed{H_n(x)\succ0}
\tag{T-91005.5}
\]

uniformly for all sufficiently large `|x|` and all integers

\[
 \boxed{
 0\le n\le
 \left(
  \frac1{2\log3}-\varepsilon
 \right)\log\ell_x.
 }
\tag{T-91005.6}
\]

Numerically,

\[
 \frac1{2\log3}=0.4551196133134186\ldots.
\]

Thus an entire growing nonlinear moment cone—not merely individual coefficients or fixed finite differences—is unconditionally positive pointwise through `0.455... log log |x|` degrees.

## 2. The full safe parabolic domain

The direct absolutely convergent Euler domain is larger than the radius-`3/4` disc. Put

\[
 r=\sqrt{1-w},
\]

with the branch `r=1` at `w=0`. The square-root formula of `L-91003` is absolutely Eulerian whenever

\[
 \Re r>\frac12.
\tag{T-91005.7}
\]

For `c>1/2`, let

\[
 \Gamma_c:
 \quad
 r=c+iv,
 \quad
 w=1-r^2,
 \quad -\infty<v<\infty.
\tag{T-91005.8}
\]

This is a parabola bounding a domain containing the origin. The negative real direction of the `w`-plane is not a barrier; using the full parabola rather than the inscribed circle is the step that preserves the sharp constant `3` below.

Let

\[
 E_x(w)=\mathcal A_x(w)-\ell_x\Phi(w),
 \qquad
 \Phi(w)=\frac1{2(1+\sqrt{1-w})^2}.
\tag{T-91005.9}
\]

### Lemma 2.1 (integrated parabolic remainder)

For

\[
 \frac12<c\le\frac34,
 \qquad
 \delta=c-\frac12,
\]

one has, uniformly for sufficiently large `|x|`,

\[
 \boxed{
 \int_{\Gamma_c}|E_x(w)|\frac{|dw|}{|w|}
 \ll \delta^{-4}.
 }
\tag{T-91005.10}
\]

### Proof sketch

Insert the exact square-root formula

\[
 \mathcal G_s(w)
 =\frac{(2-w)\mathscr X(s+1)
       -w\mathscr X'(s+1)
       -2r\mathscr X(s+r)}{w^2}
\]

and average the conjugate carriers. On `Re(s_x+r)=1+delta`, the Euler part of `mathscr X` is `O(delta^-1)`. For `|v|<=|x|/2`, uniform Stirling gives

\[
 \mathscr X(s_x+r)=-\frac12\ell_x+O(1+\delta^{-1}),
\]

and the leading `ell_x` term cancels exactly against `ell_x Phi`. For `|v|>|x|/2`, the numerator is at most logarithmic while `w=1-(c+iv)^2` gives cubic or better decay after division by `w^2`; the region `v approximately -x`, where the moving height is small, is suppressed by `|w| asymp x^2`. Splitting the line into these ranges and using `|dw|=2|r|dv` gives (T-91005.10). The power four is deliberately nonoptimal; any fixed polynomial loss in `delta^-1` gives the same edge constant.

## 3. Parabolic Cauchy representation of every Hankel quadratic

Let

\[
 p^\sharp(z)=\overline{p(\overline z)}.
\]

Cauchy's theorem on the region bounded by `Gamma_c`, together with the decay of `E_x` at infinity, gives

\[
 \boxed{
 Q_x[p]-\ell_xQ_\nu[p]
 =\frac1{2\pi i}
  \int_{\Gamma_c}
  E_x(w)
  p(1/w)p^\sharp(1/w)
  \frac{dw}{w}.
 }
\tag{T-91005.11}
\]

This is the matrix-level analogue of coefficient extraction, but on the full safe parabola rather than on a wasteful circular contour.

## 4. Why the parabolic growth constant is exactly three

Put

\[
 \lambda=\frac1w=\frac1{1-r^2},
 \qquad
 q_r=\frac{1+r}{1-r}.
\]

Then

\[
 2\lambda-1
 =\frac{1+r^2}{1-r^2}
 =\frac12\left(q_r+q_r^{-1}\right),
\]

and the exact Chebyshev identity is

\[
 U_j(2\lambda-1)
 =q_r^j+q_r^{j-2}+\cdots+q_r^{-j}.
\tag{T-91005.12}
\]

On `Re r=c<1`,

\[
 |q_r|^2
 =\frac{(1+c)^2+v^2}{(1-c)^2+v^2}
 \le\left(\frac{1+c}{1-c}\right)^2.
\]

Define

\[
 \rho_c=\frac{1+c}{1-c}.
\tag{T-91005.13}
\]

If `p=sum d_j e_j` in the orthonormal basis of `L-91010`, Cauchy–Schwarz and (T-91005.12) give

\[
 \boxed{
 |p(1/w)|^2
 \ll(n+1)^3\rho_c^{2n}Q_\nu[p]
 \qquad(w\in\Gamma_c).
 }
\tag{T-91005.14}
\]

The same bound holds for `p^sharp`.

Choose

\[
 c_n=\frac12+\frac1{n+4}.
\tag{T-91005.15}
\]

Then

\[
 \rho_{c_n}
 =3+\frac8{n+2},
 \qquad
 \rho_{c_n}^{2n}\ll9^n,
 \qquad
 (c_n-1/2)^{-4}\ll(n+4)^4.
\tag{T-91005.16}
\]

Combining (T-91005.10), (T-91005.11), and (T-91005.14) proves (T-91005.3).

The number `3` is not an artefact of a coefficient estimate. It is the exact modulus

\[
 \left|\frac{1+r}{1-r}\right|=3
\]

at the nearest safe-line boundary point `r=1/2`.

## 5. Matrix formulation

Let `S_n` be the triangular monomial-to-orthonormal-Chebyshev change of basis from `L-91010`. Then

\[
 S_n^*H_n^{(\nu)}S_n=I_{n+1}.
\]

Equation (T-91005.3) is equivalent to

\[
 \boxed{
 \left\|
 S_n^*H_n(x)S_n-\ell_xI_{n+1}
 \right\|_{\rm op}
 \le C(n+4)^7 9^n.
 }
\tag{T-91005.17}
\]

Thus every eigenvalue of the fully preconditioned Hankel matrix lies in

\[
 \left[
  \ell_x-C(n+4)^7 9^n,
  \ell_x+C(n+4)^7 9^n
 \right].
\tag{T-91005.18}
\]

This proves (T-91005.5)--(T-91005.6).

## 6. Meaning and limitation

`T-91003` proves many individual coefficient and fixed-difference signs through

\[
 \frac{\log\ell_x}{\log(4/3)}.
\]

The present theorem proves a much stronger object—the entire degree-`n` polynomial sum-of-squares cone—but the natural matrix edge is earlier:

\[
 \frac{\log\ell_x}{2\log3}.
\]

`L-91011` shows that this is exactly the first degree at which an optimally preconditioned deepest off-line pair could compete with the Catalan background. The theorem is therefore sharp at leading exponential order for this complete polynomial-Hankel architecture.

## 7. Boundary

```text
parabolic safe-domain remainder bound              PROPOSED COMPLETE
full Hankel quadratic approximation                 PROPOSED COMPLETE
Chebyshev-preconditioned operator bound             PROPOSED COMPLETE
complete degree-n Hankel positivity                 PROPOSED COMPLETE through
                                                    (1/(2 log 3)-eps) loglog|x|
all polynomial SOS tests in that range              PROPOSED COMPLETE
critical and supercritical Hankel order              OPEN / RH-BEARING
all-order Hankel positivity                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
