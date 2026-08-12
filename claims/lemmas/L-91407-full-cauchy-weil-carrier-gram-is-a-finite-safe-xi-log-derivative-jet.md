# L-91407 — The full Cauchy–Weil carrier Gram is a finite safe xi logarithmic-derivative jet

Claim ID: `L-91407`  
Status: **PROVED EXACT FULL-CARRIER COMPLETED RESOLVENT FORMULA; POSITIVITY OPEN**  
Created: 2026-08-12  
Depends on: `L-91026`, `L-91405`, the functional equation of `xi`  
RH status: **unproved**

## 1. Zero-coordinate entire function

Put

\[
 \mathfrak X(z)=\xi\!\left(\frac12+iz\right).
\tag{L-91407.1}
\]

Its zeros, with multiplicity, are exactly

\[
 \gamma_\rho=\frac{\rho-1/2}{i}
\]

for the nontrivial zeros `rho` of `zeta`. Define

\[
 \boxed{
 \mathcal L(z)=\frac{\mathfrak X'(z)}{\mathfrak X(z)}
 =i\frac{\xi'}{\xi}\!\left(\frac12+iz\right).
 }
\tag{L-91407.2}
\]

Let

\[
 \Psi_a(z)
 =\sum_{r\in\{1,2,4\}}
  \left[
   \frac{C_{r,a}}{z+ira}
   +\frac{D_{r,a}}{(z+ira)^2}
  \right]
\tag{L-91407.3}
\]

be the exact partial-fraction expansion of the causal spectral factor of
`L-91026`. Put

\[
 \Psi_a^\#(z)=\overline{\Psi_a(\overline z)}
 =\sum_r\left[
  \frac{\overline{C_{r,a}}}{z-ira}
  +\frac{\overline{D_{r,a}}}{(z-ira)^2}
 \right].
\tag{L-91407.4}
\]

## 2. Full independent-carrier Gram

For real carriers `x,y`, define

\[
 \boxed{
 \mathfrak W_a(x,y)
 =\sum_\rho m_\rho
  \Psi_a(\gamma_\rho-x)
  \Psi_a^\#(\gamma_\rho-y).
 }
\tag{L-91407.5}
\]

The sum is absolutely convergent because `Psi_a(z)=O_a(z^(-3))` and

\[
 \sum_\rho m_\rho(1+|\gamma_\rho|)^{-2}<\infty.
\]

No assumption on the real parts of the zeros is made.  When RH holds,
(L-91407.5) is the usual positive Gram; unconditionally it is the Hermitian
Cauchy–Weil form.

Put

\[
 F_{x,y}(z)=\Psi_a(z-x)\Psi_a^\#(z-y).
\tag{L-91407.6}
\]

Then `F_(x,y)(z)=O_a(z^(-6))`.

## 3. Contour reduction

Integrate

\[
 F_{x,y}(z)\mathcal L(z)
\]

around expanding rectangles avoiding the zeros of `mathfrak X`.  Standard
order-one bounds give

\[
 \mathcal L(z)=O(\log(2+|z|))
\]

on a sequence of such boundaries, while `F=O(|z|^(-6))`; hence the boundary
integrals tend to zero.

The poles inside are:

```text
the zeros gamma_rho of mathfrak X;
the lower double poles p_r=x-ira of Psi_a(z-x);
the upper double poles q_r=y+ira of Psi_a#(z-y).
```

Therefore the residue theorem gives

\[
 \boxed{
 \mathfrak W_a(x,y)
 =-\sum_r\operatorname{Res}_{z=p_r}
   [F_{x,y}(z)\mathcal L(z)]
  -\sum_r\operatorname{Res}_{z=q_r}
   [F_{x,y}(z)\mathcal L(z)].
 }
\tag{L-91407.7}
\]

This identity already removes the infinite zero sum.

## 4. Lower-pole jet

For

\[
 p_r=x-ira,
 \qquad
 H_r(z)=\Psi_a^\#(z-y),
\]

one has near `p_r`

\[
 F_{x,y}(z)
 =\frac{D_{r,a}H_r(p_r)}{(z-p_r)^2}
 +\frac{
   C_{r,a}H_r(p_r)+D_{r,a}H_r'(p_r)
  }{z-p_r}
 +O(1).
\]

Hence

\[
\boxed{
\begin{aligned}
 \operatorname{Res}_{p_r}[F\mathcal L]
 ={}&D_{r,a}H_r(p_r)\mathcal L'(p_r)\\
 &+\left[
   C_{r,a}H_r(p_r)+D_{r,a}H_r'(p_r)
  \right]\mathcal L(p_r).
\end{aligned}}
\tag{L-91407.8}
\]

The corresponding xi arguments are

\[
 \frac12+ip_r
 =\frac12+ra+ix,
\]

which lie in the absolute safe half-plane.

## 5. Upper-pole jet

For

\[
 q_r=y+ira,
 \qquad
 G_r(z)=\Psi_a(z-x),
\]

one has

\[
\boxed{
\begin{aligned}
 \operatorname{Res}_{q_r}[F\mathcal L]
 ={}&\overline{D_{r,a}}G_r(q_r)\mathcal L'(q_r)\\
 &+\left[
   \overline{C_{r,a}}G_r(q_r)
   +\overline{D_{r,a}}G_r'(q_r)
  \right]\mathcal L(q_r).
\end{aligned}}
\tag{L-91407.9}
\]

Here

\[
 \frac12+iq_r
 =\frac12-ra+iy.
\]

The functional equation `xi(s)=xi(1-s)` gives

\[
 \frac{\xi'}{\xi}\!\left(\frac12-ra+iy\right)
 =-\frac{\xi'}{\xi}\!\left(\frac12+ra-iy\right),
\tag{L-91407.10}
\]

and, after differentiating,

\[
 \left(\frac{\xi'}{\xi}\right)'\!\left(\frac12-ra+iy\right)
 =\left(\frac{\xi'}{\xi}\right)'\!\left(\frac12+ra-iy\right).
\tag{L-91407.11}
\]

Thus the upper-pole terms also use only safe right-half-plane evaluations.

## 6. Explicit completed finite-jet formula

Combining (L-91407.7)--(L-91407.11), the full Gram is

\[
\boxed{
\begin{aligned}
 \mathfrak W_a(x,y)=-\sum_{r\in\{1,2,4\}}
 \Bigg\{&
 D_{r,a}\Psi_a^\#(x-y-ira)\mathcal L'(x-ira)\\
 &+\Big[
 C_{r,a}\Psi_a^\#(x-y-ira)
 +D_{r,a}(\Psi_a^\#)'(x-y-ira)
 \Big]\mathcal L(x-ira)\\
 &+\overline{D_{r,a}}\Psi_a(y-x+ira)\mathcal L'(y+ira)\\
 &+\Big[
 \overline{C_{r,a}}\Psi_a(y-x+ira)
 +\overline{D_{r,a}}\Psi_a'(y-x+ira)
 \Big]\mathcal L(y+ira)
 \Bigg\}.
\end{aligned}}
\tag{L-91407.12}
\]

Every term is explicit and uses only

```text
xi'/xi and its first derivative;
arguments 1/2+ra+ix and 1/2+ra-iy;
r=1,2,4;
rational residue coefficients of Psi_a.
```

Equation (L-91407.12) is Hermitian in `(x,y)` by construction.

## 7. Relation to the prime finite jets

Write

\[
 \xi(s)=\gamma(s)\zeta(s).
\]

Then

\[
 \frac{\xi'}{\xi}
 =\frac{\gamma'}{\gamma}+rac{\zeta'}{\zeta}.
\tag{L-91407.13}
\]

`L-91406` expresses the full prime Wick–Green maps through finite jets of

\[
 Z(s)=-\frac{\zeta'}{\zeta}(s).
\]

Equation (L-91407.12) gives the completed finite jet in the same safe
coordinates. Consequently the exact Green boundary kernel

\[
 \mathfrak B_a
 =\mathfrak W_a-D_a^*D_a
\]

can be evaluated from a finite collection of:

```text
zeta logarithmic-derivative jets;
gamma/pole logarithmic-derivative jets;
rational residue coefficients.
```

No zero sum, critical Euler product, or numerical continuation is required.
The positivity of this finite-jet kernel or its conservative Schur complement
remains open.

## 8. Numerical control

At `a=4`, summing only the first 100 positive zeta ordinates and their
reflections differs from the exact finite-jet formula by approximately

\[
 5.04\times10^{-7}
\]

on carriers in `{0.31,0.83,1.37}`. The discrepancy decreases as more zeros are
included and is consistent with the `O(|gamma|^(-6))` tail. This is a diagnostic,
not part of the proof.

## 9. Exact boundary

```text
full independent-carrier completed zero Gram         EXACT
contour reduction to six rational poles              EXACT
safe xi'/xi finite-jet formula                       EXACT
functional-equation reflection of upper poles        EXACT
prime and completed kernels in common safe coordinates EXACT
finite-jet Green boundary kernel                     EXPLICIT
finite-jet / Schur-complement positivity              OPEN / RH-BEARING
delayed bridge completion                            OPEN
Riemann Hypothesis                                    UNPROVED
```
