# L-91406 — The Wick–Green endpoint counterterms are finite jets of the safe zeta logarithmic derivative

Claim ID: `L-91406`  
Status: **PROVED EXACT FINITE-JET COMPRESSION OF THE PRIME ENDPOINTS**  
Created: 2026-08-12  
Depends on: `L-91405`  
RH status: **unproved**

## 1. Safe logarithmic derivative

Put

\[
 \boxed{
 Z(s)=-\frac{\zeta'}{\zeta}(s)
 =\sum_{n\ge2}\Lambda(n)n^{-s},
 \qquad \Re s>1.
 }
\tag{L-91406.1}
\]

Then

\[
 \sum_n\Lambda(n)(\log n)^k n^{-s}
 =(-1)^k Z^{(k)}(s).
\tag{L-91406.2}
\]

Every evaluation below has real part `1/2+ra>1` and is therefore absolutely
convergent.

Retain the causal state

\[
 \psi_a(v)
 =\sum_{r\in\{1,2,4\}}
  (A_r+B_rv)e^{-rav}
 \qquad(v\ge0),
\tag{L-91406.3}
\]

suppressing the scale label `a` on the residue coefficients.

## 2. The common state correlation

For a carrier difference

\[
 q=x-y,
\]

put

\[
 \boxed{
 R_a(q)
 =\int_0^\infty e^{iqv}|\psi_a(v)|^2dv.
 }
\tag{L-91406.4}
\]

For `r,s in {1,2,4}`, let

\[
 \Lambda_{rs}(q)=(r+s)a-iq.
\]

Direct integration gives the explicit rational function

\[
\boxed{
\begin{aligned}
 R_a(q)=\sum_{r,s}\Bigg[
 &\frac{A_r\overline{A_s}}{\Lambda_{rs}(q)}\\
 &+\frac{A_r\overline{B_s}+B_r\overline{A_s}}
        {\Lambda_{rs}(q)^2}\\
 &+\frac{2B_r\overline{B_s}}
        {\Lambda_{rs}(q)^3}
 \Bigg].
\end{aligned}}
\tag{L-91406.5}
\]

## 3. The `V` endpoint

Let

\[
 \sigma_r=\frac12+ra.
\]

The `V` map of `L-91405` is independent of the jump coordinate except for the
safe measure. Therefore

\[
\begin{aligned}
 \langle V_{r,a,x},V_{r,a,y}\rangle
 &=\Pi_{r,a}((0,\infty))R_a(q)\\
 &=Z(\sigma_r)R_a(q).
\end{aligned}
\]

Thus

\[
 \boxed{
 \langle V_{a,x},V_{a,y}\rangle
 =R_a(q)\sum_{r\in\{1,2,4\}}Z(\sigma_r).
 }
\tag{L-91406.6}
\]

No prime sum remains.

## 4. The `U` endpoint

Fix `r` and put

\[
 \lambda_r(q)=2ra-iq,
 \qquad
 c_r=2\Re(A_r\overline{B_r}),
 \qquad
 b_r=|B_r|^2.
\]

The state integral in the `U` endpoint is a quadratic polynomial in the jump
length `tau`:

\[
 \int_0^\infty
 e^{iqv}|A_r+B_r(v+\tau)|^2e^{-2rav}dv
 =C_{r,0}(q)+C_{r,1}(q)\tau+C_{r,2}(q)\tau^2,
\tag{L-91406.7}
\]

where

\[
 \boxed{
 C_{r,0}(q)
 =\frac{|A_r|^2}{\lambda_r(q)}
  +\frac{c_r}{\lambda_r(q)^2}
  +\frac{2b_r}{\lambda_r(q)^3},
 }
\tag{L-91406.8}
\]

\[
 \boxed{
 C_{r,1}(q)
 =\frac{c_r}{\lambda_r(q)}
  +\frac{2b_r}{\lambda_r(q)^2},
 }
\tag{L-91406.9}
\]

\[
 \boxed{
 C_{r,2}(q)=\frac{b_r}{\lambda_r(q)}.
 }
\tag{L-91406.10}
\]

The jump modulation contributes `e^(iq tau)`, so (L-91406.2) gives

\[
 \boxed{
\begin{aligned}
 \langle U_{r,a,x},U_{r,a,y}\rangle
 ={}&C_{r,0}(q)Z(\sigma_r-iq)\\
 &-C_{r,1}(q)Z'(\sigma_r-iq)\\
 &+C_{r,2}(q)Z''(\sigma_r-iq).
\end{aligned}}
\tag{L-91406.11}
\]

Hence the complete `U` endpoint is the sum of only nine safe logarithmic-
derivative jet evaluations.

## 5. The mixed `U`–`V` endpoint

For fixed `r`, define

\[
\boxed{
\begin{aligned}
 K_{r,0}(q)=\sum_s\Bigg[
 &\frac{A_r\overline{A_s}}{\Lambda_{rs}(q)}\\
 &+\frac{A_r\overline{B_s}+B_r\overline{A_s}}
        {\Lambda_{rs}(q)^2}\\
 &+\frac{2B_r\overline{B_s}}
        {\Lambda_{rs}(q)^3}
 \Bigg]
\end{aligned}}
\tag{L-91406.12}
\]

and

\[
 \boxed{
 K_{r,1}(q)
 =\sum_s\left[
  \frac{B_r\overline{A_s}}{\Lambda_{rs}(q)}
  +\frac{B_r\overline{B_s}}{\Lambda_{rs}(q)^2}
 \right].
 }
\tag{L-91406.13}
\]

The jump modulation in
`<U_(r,a,x),V_(r,a,y)>` is `e^(ix tau)`, not merely the carrier
difference. Therefore

\[
 \boxed{
\begin{aligned}
 \langle U_{r,a,x},V_{r,a,y}\rangle
 ={}&K_{r,0}(x-y)Z(\sigma_r-ix)\\
 &-K_{r,1}(x-y)Z'(\sigma_r-ix).
\end{aligned}}
\tag{L-91406.14}
\]

The opposite mixed endpoint is obtained by Hermitian symmetry:

\[
 \langle V_{r,a,x},U_{r,a,y}\rangle
 =\overline{
   \langle U_{r,a,y},V_{r,a,x}\rangle
  }.
\tag{L-91406.15}
\]

Equations (L-91406.12)--(L-91406.15) replay the full independent-carrier prime
block without a prime sum.

## 6. Exact finite-jet Green counterterm

Let

\[
 \mathfrak E_a^{\rm prime}(x,y)
 =\langle U_{a,x},U_{a,y}\rangle
  +\langle V_{a,x},V_{a,y}\rangle.
\tag{L-91406.16}
\]

By (L-91406.6) and (L-91406.11),

\[
 \boxed{
 \mathfrak E_a^{\rm prime}(x,y)
 }
\]

is an explicit rational linear combination of

```text
Z(sigma_r),
Z(sigma_r-i(x-y)),
Z'(sigma_r-i(x-y)),
Z''(sigma_r-i(x-y)),
r=1,2,4.
```

Thus the Green boundary kernel of `L-91405` is not an uncontrolled infinite
prime object. It is

\[
 \boxed{
 \mathfrak B_a(x,y)
 =\mathfrak A_a(x,y)-\mathfrak E_a^{\rm prime}(x,y),
 }
\tag{L-91406.17}
\]

where the first term is the explicit gamma/pole integral and the second is the
finite safe zeta jet above.

## 7. Completion opportunity

Write

\[
 \xi(s)=\gamma(s)\zeta(s),
 \qquad
 \gamma(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

The corresponding completed logarithmic derivative is

\[
 -\frac{\xi'}{\xi}
 =-\frac{\gamma'}{\gamma}+Z.
\tag{L-91406.18}
\]

Equations (L-91406.6)--(L-91406.17) show exactly where a completed finite-jet
cancellation theorem must act: the gamma/pole kernel must be combined with the
same rational coefficient functionals applied to the archimedean logarithmic
derivative.

No such cancellation or positivity is asserted here. The theorem removes the
prime summation from the remaining boundary obligation and turns it into a
finite collection of safe analytic functions.

## 8. Exact boundary

```text
state correlation R_a(q)                            EXPLICIT RATIONAL
V endpoint                                           EXACT Z-values
U endpoint                                           EXACT Z,Z',Z'' jet
mixed endpoint                                       EXACT Z,Z' jet
full prime Green counterterm                         FINITE SAFE JET
completed gamma/pole finite-jet cancellation         OPEN
Green boundary / Schur-complement positivity         OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
