# L-92301 — The fractional-string limit has an explicit beta-Hankel law

Claim ID: `L-92301`  
Status: **EXACT LIMITING MOMENT ALGEBRA; XI CONVERGENCE DEPENDS ON L-92300**  
Created: 2026-08-14  
Depends on: `L-92300`; Selberg's beta integral  
RH status: **unproved**

For `0<alpha<1` put

\[
 c_k(\alpha)=\frac{(\alpha)_k}{k!}
 \qquad(k\ge0)
\]

and define

\[
 \boxed{
 C_n(\alpha)
 =\bigl(c_{i+j+1}(\alpha)\bigr)_{0\le i,j<n}.
 }
 \tag{L-92301.1}
\]

## 1. Positive beta moment representation

Let

\[
 \boxed{
 d\nu_\alpha(q)
 =\frac{\sin(\pi\alpha)}{\pi}
   q^\alpha(1-q)^{-\alpha}\,dq,
 \qquad 0<q<1.
 }
 \tag{L-92301.2}
\]

Then

\[
 \int_0^1q^k\,d\nu_\alpha(q)
 =\frac{(\alpha)_{k+1}}{(k+1)!}
 =c_{k+1}(\alpha).
\]

Consequently

\[
 \boxed{
 C_n(\alpha)
 =\int_0^1
  (1,q,\ldots,q^{n-1})^T
  (1,q,\ldots,q^{n-1})
  \,d\nu_\alpha(q)
 \succ0.
 }
 \tag{L-92301.3}
\]

This is the beta-`(alpha+1,1-alpha)` moment matrix of the homogeneous
fractional string.

## 2. Exact determinant

Andreief's identity and the Selberg integral give

\[
 \boxed{
 \begin{aligned}
 \det C_n(\alpha)
 ={}&\frac1{n!}
 \left(\frac{\sin\pi\alpha}{\pi}\right)^n
 \\&\times
 \prod_{j=0}^{n-1}
 \frac{
  \Gamma(\alpha+1+j)
  \Gamma(1-\alpha+j)
  \Gamma(j+2)
 }{
  \Gamma(n+j+1)
 }.
 \end{aligned}
 }
 \tag{L-92301.4}
\]

Every factor is strictly positive.

At the limiting exponent `alpha=1/2`,

\[
 c_k\left(\frac12\right)
 =\frac{\binom{2k}{k}}{4^k}
\]

and the determinant collapses to the exact power of two

\[
 \boxed{
 \det C_n\left(\frac12\right)
 =2^{-n(2n-1)}.
 }
 \tag{L-92301.5}
\]

The first values are

\[
 \frac12,\quad
 \frac1{64},\quad
 \frac1{32768},\quad
 \frac1{2^{28}},\ldots.
\]

## 3. Xi Hankel convergence

Let

\[
 H_n(t)=\bigl(A_{i+j+1}(t)\bigr)_{0\le i,j<n},
 \qquad
 D_{x,u}=\operatorname{diag}
 \bigl(x^2u,x^4u^2,\ldots,x^{2n}u^n\bigr).
\]

From `L-92300`, for fixed `n` and locally uniformly for positive `u` in a
compact interval,

\[
 \boxed{
 \frac{2}{x\ell_x}
 D_{x,u}H_n(x^2u)D_{x,u}
 =u^{-\alpha_x}C_n(\alpha_x)
  +O_{n,u}(\ell_x^{-2})+O_{n,u}((x\ell_x)^{-1}).
 }
 \tag{L-92301.6}
\]

(The displayed diagonal includes the powers of `u` precisely so that the
right-hand side is the unweighted beta moment matrix.)

Since `alpha_x -> 1/2` and `C_n(1/2)` is strictly positive,

\[
 \boxed{
 H_n(x^2u)\succ0
 }
\]

for every fixed `n`, every fixed compact positive `u`-range, and all
sufficiently large `x`.

## 4. Local matrix-monotonicity consequence

The reciprocal Loewner-Hankel congruence of `L-92204` identifies `H_n` with
the confluent order-`n` Loewner matrix of the Xi impedance `Z=1/p`.
Therefore every fixed matrix order has the universal fractional-string limit.

Combined with the Dobsch--Donoghue--Heinavaara local criterion, positivity of
`H_n(t)` throughout a tail interval implies matrix monotonicity of order `n`
on that interval.

## 5. Exact boundary

```text
fractional beta moment measure                    EXACT
Selberg determinant                               EXACT
central-binomial determinant 2^(-n(2n-1))         EXACT
fixed-order Xi Hankel convergence                 PROPOSED COMPLETE
fixed-order eventual matrix monotonicity          PROPOSED COMPLETE
uniform order growing with x                      NEXT CLAIM
all-order positivity at one finite x              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
