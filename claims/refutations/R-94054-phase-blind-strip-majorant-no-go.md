# R-94054 — The phase-locked filter cannot beat its terminal depth by a strip majorant

Claim ID: `R-94054`  
Status: **PROPOSED COMPLETE MAXIMUM-MODULUS NO-GO — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94050`  
Scope: analytic filter/absolute-majorant strategies; does not refute arithmetic signed cancellation

## 1. The filtered Gaussian

For \(q>0\) and integer \(m\ge0\), put

\[
G_{q,m}(z)=e^{-qz^2}P(z)^{2m}.
\tag{R-94054.1}
\]

Fix \(0<y<1/2\). The matched terminal amplitude is

\[
T_{q,m}(y)=|G_{q,m}(iy)|
 =e^{qy^2}P(iy)^{2m}.
\tag{R-94054.2}
\]

On the real boundary,

\[
\sup_{t\in\mathbb R}|G_{q,m}(t)|
 \le9^{2m}.
\tag{R-94054.3}
\]

On the critical shifted boundary,

\[
|G_{q,m}(t+i/2)|
 =e^{q/4-qt^2}|P(t+i/2)|^{2m}.
\tag{R-94054.4}
\]

## 2. Maximum-modulus inequality

Apply the maximum-modulus principle to the rectangle

\[
-R\le\Re z\le R,
\qquad 0\le\Im z\le1/2,
\]

and let \(R\to\infty\). The Gaussian kills the vertical sides. Therefore

\[
\boxed{
T_{q,m}(y)
 \le
\max\left\{
 9^{2m},
 \sup_{t\in\mathbb R}
 e^{q/4-qt^2}|P(t+i/2)|^{2m}
\right\}.
}
\tag{R-94054.5}
\]

Whenever

\[
qy^2+2m\log P(iy)>2m\log9,
\tag{R-94054.6}
\]

one must have

\[
\boxed{
\sup_t e^{q/4-qt^2}|P(t+i/2)|^{2m}
 \ge e^{qy^2}P(iy)^{2m}.
}
\tag{R-94054.7}
\]

For fixed \(m\), or more generally \(m=o(q)\), condition (R-94054.6) holds
for every fixed depth \(y>0\) and all large \(q\).

## 3. Meaning for the proof programme

The shifted line \(\Im z=1/2\) is the critical Laplace saddle behind the
phase-blind prime envelope. Equation (R-94054.7) says that this phase-locked analytic multiplier, and the same maximum-modulus template for any scalar multiplier with comparable boundary control, cannot make its entire critical shifted-line envelope exponentially smaller than its retained terminal amplitude.

Thus the following proposed shortcut is false:

```text
choose a carrier-local entire multiplier;
kill the critical prime saddle by analytic zeros;
retain the off-line terminal signal;
close RH using only absolute prime bounds.
```

Finite or sublinear filter order can improve polynomial and sublinear terms, as
`T-94051` proves, but it cannot create the fixed exponential gap needed for a
fixed shallow depth.

This no-go does **not** apply to:

```text
genuine signed prime cancellation;
carrier-specific arithmetic information;
bilinear dispersion using more than an absolute strip majorant;
a source identity which changes the arithmetic measure itself.
```

It is therefore a method firewall, not a refutation of the First-Hermite or Q4
criteria.
