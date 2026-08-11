# L-91004 — The unit-disc generator is the Peano integral of one radial log-curvature

Claim ID: `L-91004`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90905`, `T-91001`, the functional equation of `xi`  
RH status: **unproved**

## 1. Radial entire function

Fix a real centre `x` and put

\[
 s_x=\frac12+ix.
\]

For `t>0`, write `r=sqrt(t)` and define

\[
 P_x(t)=\xi(s_x+r)\xi(s_x-r).
\tag{L-91004.1}
\]

The functional equation and conjugation symmetry give, on the positive real axis,

\[
 P_x(t)=|\xi(s_x+r)|^2.
\tag{L-91004.2}
\]

The product is an entire function of `t`: changing `r` to `-r` exchanges the two factors. Away from its zeros put

\[
 U_x(t)=\frac12\log P_x(t)=\log|\xi(s_x+r)|,
 \qquad
 J_x(t)=tU_x'(t).
\tag{L-91004.3}
\]

Let

\[
 \mathscr X(s)=-\frac{\xi'(s)}{\xi(s)}.
\]

Then

\[
 \boxed{
 J_x(t)=-\frac r2\Re\mathscr X(s_x+r).
 }
\tag{L-91004.4}
\]

Define the radial curvature

\[
 \boxed{
 \mathcal C_x(t)=-J_x''(t).
 }
\tag{L-91004.5}
\]

A direct differentiation gives the single-sample formula

\[
 \boxed{
 \mathcal C_x(t)
 =\frac1{8r^3}\Re\left[
 -\mathscr X(s_x+r)
 +r\mathscr X'(s_x+r)
 +r^2\mathscr X''(s_x+r)
 \right].
 }
\tag{L-91004.6}
\]

Thus the complete curvature at radius `r` uses only one horizontal sample of the completed logarithmic derivative.

## 2. Absolutely convergent zero kernel

For a critical-line zero `rho=1/2+i gamma`, put `u=gamma-x`. Its contribution is

\[
 \boxed{
 \mathcal C_{\rho,x}(t)
 =m_\rho\frac{u^2}{(t+u^2)^3}.
 }
\tag{L-91004.7}
\]

For one right-side reflected pair, write

\[
 \rho=\frac12+d+i\gamma,
 \qquad z=d+i(\gamma-x),
 \qquad 0<d<\frac12.
\]

Its complete pair contribution is

\[
 \boxed{
 \mathcal C_{\rho,x}^{\rm pair}(t)
 =-2m_\rho\Re\frac{z^2}{(t-z^2)^3}.
 }
\tag{L-91004.8}
\]

The kernels are `O(|gamma-x|^-4)`, so the standard local zero count gives absolute and locally uniform convergence away from the displayed poles. Hence

\[
\boxed{
\begin{aligned}
 \mathcal C_x(t)
={}&\sum_{\rho=1/2+i\gamma}
 m_\rho\frac{(\gamma-x)^2}{[t+(\gamma-x)^2]^3}\\
 &-2\sum_{\Re\rho>1/2}m_\rho
 \Re\frac{[\rho-s_x]^2}{[t-(\rho-s_x)^2]^3}.
\end{aligned}}
\tag{L-91004.9}
\]

## 3. The safe-line hierarchy is the curvature jet

The normalized safe-line coefficients of `T-91001` are

\[
 a_k(x)=\frac{\mathfrak S_k(x)}{(k+2)!}.
\]

Differentiating (L-91004.9) termwise at `t=1` gives

\[
 \boxed{
 a_k(x)
 =\frac{4(-1)^k}{(k+2)!}
 \mathcal C_x^{(k)}(1).
 }
\tag{L-91004.10}
\]

Thus the one-safe-line hierarchy is precisely the normalized alternating Taylor jet of one radial curvature.

## 4. Peano identity for the unit-disc function

Let

\[
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k
\]

be the unit-disc generator of `T-91001`. Taylor's formula and (L-91004.10) give

\[
 \boxed{
 \mathcal A_x(w)
 =\frac4{w^2}\int_0^w
 (w-u)\mathcal C_x(1-u)\,du.
 }
\tag{L-91004.11}
\]

This holds on every simply connected pole-free region reached from the origin. Equivalently,

\[
 \boxed{
 \frac{d^2}{dw^2}
 \left[\frac{w^2}{4}\mathcal A_x(w)\right]
 =\mathcal C_x(1-w).
 }
\tag{L-91004.12}
\]

For real `0<t<1`, with `w=1-t`, this becomes

\[
 \boxed{
 \mathcal A_x(1-t)
 =\frac4{(1-t)^2}
 \int_t^1(v-t)\mathcal C_x(v)\,dv.
 }
\tag{L-91004.13}
\]

The same identity is the tangent-defect formula

\[
 \boxed{
 \mathcal A_x(1-t)
 =\frac4{(1-t)^2}
 \left[
 J_x(1)+J_x'(1)(t-1)-J_x(t)
 \right].
 }
\tag{L-91004.14}
\]

Hence the real radial generator measures exactly how far `J_x` lies below its tangent at the safe point `t=1`.

## 5. Heat/resolvent relation

Let `M(q,x)` denote the first-Hermite zero-heat scalar of PR #379. At the zero-kernel level,

\[
 \frac12\int_0^\infty q^2e^{-tq}
 z^2e^{qz^2}\,dq
 =\frac{z^2}{(t-z^2)^3}
\]

whenever `Re(t-z^2)>0`. Therefore

\[
 \boxed{
 \mathcal C_x(t)
 =\frac12\int_0^\infty q^2e^{-tq}M(q,x)\,dq.
 }
\tag{L-91004.15}
\]

The identity holds on the common convergence region, and elsewhere by meromorphic continuation. The radial curvature is the Laplace transform of first-Hermite heat with the exact `q^2/2` weight.

## 6. Boundary

Established here:

```text
one radial entire product P_x(t);
exact curvature C_x(t) from one Xcal sample;
absolute zero-kernel expansion;
safe-line coefficients as the curvature Taylor jet;
unit-disc generator as a twofold Peano integral;
real tangent-defect identity;
first-Hermite heat -> radial-curvature Laplace transform.
```

Not established here:

```text
unconditional nonnegativity of C_x(t) in 0<t<1/4;
prime-side continuation through the unit-disc annulus;
Riemann Hypothesis.
```
