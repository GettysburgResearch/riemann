# L-19880 — The native endpoint ramp is the exact Laplace basis of the prime radial Clark source

Claim ID: `L-19880`  
Status: **PROPOSED EXACT NATIVE-TO-RADIAL SOURCE LOCK — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-14  
Frozen inputs: PR #468 at `a41f81466f85d52597c97b41505756a8860698d0`; PR #470 at `89af3206ea1894884613e1188b5ab9a6a4cd74f0`; PR #404 at `ab71aa1fe0b1fd192011bbf40f032d2f42889ea0`; PR #427 at `e4cba612839efb7296c1664f173e924f9e252bbf`; PR #430 at `cedf2f5b43c99d6e6f9a760236432b123dd91770`  
Scope: exact prime-channel source dictionary and intervalwise positive slack; no model domination and no RH claim

## 1. Native and radial coordinates

For an integer `q>=2`, the native ordinary endpoint capacity of PR #468 is

\[
 w_X(q)=q^{-1/2}\log(X/q)\,\mathbf 1_{q\le X}.
 \tag{L-19880.1}
\]

Put

\[
 x=\log X,\qquad u_q=\log q,
 \tag{L-19880.2}
\]

so that

\[
 w_{e^x}(q)=q^{-1/2}(x-u_q)_+.
 \tag{L-19880.3}
\]

Let `sigma` and `r` be real parameters with

\[
 \lambda_{\sigma,r}
 =\sigma+2r-\frac12>0.
 \tag{L-19880.4}
\]

Then the following identity is exact:

\[
 \boxed{
 \lambda_{\sigma,r}^{2}
 \int_0^\infty e^{-\lambda_{\sigma,r}x}
 w_{e^x}(q)\,dx
 =q^{-(\sigma+2r)}.}
 \tag{L-19880.5}
\]

### Proof

The integrand vanishes for `x<u_q`. Hence

\[
\begin{aligned}
 \int_0^\infty e^{-\lambda x}w_{e^x}(q)\,dx
 &=q^{-1/2}\int_{u_q}^\infty
   e^{-\lambda x}(x-u_q)\,dx\\
 &=q^{-1/2}e^{-\lambda u_q}
   \int_0^\infty e^{-\lambda y}}\,dy\\
 &=\frac{q^{-1/2-\lambda}}{\lambda^2}.
\end{aligned}
\]

Since `lambda+1/2=sigma+2r`, multiplication by `lambda^2` proves
(L-19880.5). QED.

For a prime power `q=p^k`, multiplication by `2 Lambda(q)` gives

\[
 \boxed{
 2\Lambda(q)\lambda_{\sigma,r}^{2}
 \int_0^\infty e^{-\lambda_{\sigma,r}x}
 w_{e^x}(q)\,dx
 =2\Lambda(q)q^{-(\sigma+2r)}.}
 \tag{L-19880.6}
\]

The right side is exactly the coefficient of the prime radial innovation in
`L-91800`.

## 2. Source-owned thinning survives the transform coefficientwise

Let `A` be a finite or countable immutable source-label set. Suppose measurable
functions

\[
 U_\alpha(x,q)\ge0
 \qquad(\alpha\in A)
 \tag{L-19880.7}
\]

satisfy, for almost every `x>=0` and every integer `q>=2`,

\[
 \sum_{\alpha\in A}U_\alpha(x,q)
 \le w_{e^x}(q).
 \tag{L-19880.8}
\]

Define the radial coefficient owned by label `alpha` by

\[
 c_\alpha(\sigma,r;q)
 =2\Lambda(q)\lambda_{\sigma,r}^{2}
  \int_0^\infty e^{-\lambda_{\sigma,r}x}
  U_\alpha(x,q)\,dx.
 \tag{L-19880.9}
\]

For non-prime-powers, `Lambda(q)=0`, so these columns disappear automatically.
For every prime power,

\[
 c_\alpha(\sigma,r;q)\ge0,
 \tag{L-19880.10}
\]

and Tonelli's theorem plus (L-19880.6)--(L-19880.8) gives

\[
 \boxed{
 \sum_\alpha c_\alpha(\sigma,r;q)
 \le2\Lambda(q)q^{-(\sigma+2r)}.}
 \tag{L-19880.11}
\]

The exact coefficient slack is

\[
 \boxed{
 s(\sigma,r;q)
 =2\Lambda(q)\lambda_{\sigma,r}^{2}
  \int_0^\infty e^{-\lambda_{\sigma,r}x}
  \left[w_{e^x}(q)-\sum_\alpha U_\alpha(x,q)\right]dx
 \ge0.}
 \tag{L-19880.12}
\]

Thus the positive Laplace transform preserves source ownership and converts
native one-use capacity into coefficientwise radial one-use capacity. No
selection, cancellation, or post hoc matrix factorization is used.

## 3. One common polarized feature dictionary

Fix a finite carrier packet

\[
 F=(t_1,\ldots,t_m)\subset\mathbb R.
 \tag{L-19880.13}
\]

For every prime power `q`, define the common carrier column

\[
 v_q^F
 =\bigl(1-e^{-it_j\log q}\bigr)_{j=1}^{m}
 \in\mathbb C^m.
 \tag{L-19880.14}
\]

For a half-open radial interval `I`, define the full prime radial source matrix

\[
 \mathsf A_{\rm pr}(I;F)
 =\int_I\sum_{q=p^k}
   2\Lambda(q)q^{-(\sigma+2r)}
   v_q^F(v_q^F)^*\,dr,
 \tag{L-19880.15}
\]

and the source-owned used matrix

\[
 \mathsf U_{\rm pr}(I;F)
 =\int_I\sum_{\alpha,q=p^k}
   c_\alpha(\sigma,r;q)
   v_q^F(v_q^F)^*\,dr.
 \tag{L-19880.16}
\]

Whenever the displayed positive forms are finite, or on their monotone
quadratic-form domains, (L-19880.11)--(L-19880.12) give the exact common-column
identity

\[
 \boxed{
 \mathsf A_{\rm pr}(I;F)-\mathsf U_{\rm pr}(I;F)
 =\int_I\sum_{q=p^k}
   s(\sigma,r;q)v_q^F(v_q^F)^*\,dr
 \succeq0.}
 \tag{L-19880.17}
\]

This identity is automatically compatible with:

```text
disjoint union and monotone refinement of radial intervals;
enlargement or restriction of finite carrier packets;
source-label refinement;
carrier modulation and polarization.
```

The dictionary is canonical: it is indexed by the same prime-power occurrence
`q`, source owner `alpha`, radial depth `r`, and physical carrier column
`v_q^F` on both sides.

## 4. Radix-four detail slack produces the required ordinary slack

Let `d_X` be a nonnegative native current row. Write its radix-four detail
slack as

\[
 s_X^{(4)}=\Omega_X-\Xi(d_X)\ge0.
 \tag{L-19880.18}
\]

The positive inverse from `L-91687` gives

\[
 w_X-\Gamma(d_X)
 =\mathcal R_4s_X^{(4)}\ge0.
 \tag{L-19880.19}
\]

Hence the theorem applies with

\[
 U(x,q)=\Gamma(d_{e^x};q)
 =w_{e^x}(q)-[\mathcal R_4s_{e^x}^{(4)}](q).
 \tag{L-19880.20}
\]

If `d_X` is partitioned atomwise among source owners before summation, the
linearity of `Gamma` gives the labelled functions `U_alpha` required by
(L-19880.7)--(L-19880.8). Therefore a source-owned `SONTR` certificate has a
canonical radial prime-source image; no additional allocation theorem is
needed for this prime channel.

## 5. The native score debt becomes an exact radial slack budget

Let

\[
 \Delta(X)
 =J_\Lambda(X)-\mathcal H(d_X)
 =\sum_q\Lambda(q)\,[w_X(q)-\Gamma(d_X;q)]
 \ge0.
 \tag{L-19880.21}
\]

The second equality is the native ordinary-response Fubini identity of PR #468.
Nonnegative Tonelli interchange and (L-19880.12) give

\[
 \boxed{
 \sum_{q=p^k}s(\sigma,r;q)
 =2\lambda_{\sigma,r}^{2}
  \int_0^\infty e^{-\lambda_{\sigma,r}x}
  \Delta(e^x)\,dx.}
 \tag{L-19880.22}
\]

Since `||v_q^F||^2<=4m`, the intervalwise prime slack obeys the quantitative
trace bound

\[
 \boxed{
 \operatorname{tr}\bigl[
 \mathsf A_{\rm pr}(I;F)-\mathsf U_{\rm pr}(I;F)
 \bigr]
 \le8m\int_I\lambda_{\sigma,r}^{2}
 \int_0^\infty e^{-\lambda_{\sigma,r}x}
 \Delta(e^x)\,dx\,dr.}
 \tag{L-19880.23}
\]

Thus the native `Y_4`/entropy ledger is not merely analogous to radial source
loss: after positive radix-four inversion it is its exact Laplace budget.

## 6. Radix-four null gauge

`L-19881` sharpens the preceding budget. If a detail-slack column `Q` has
`Y_4(Q)=0`, then every ordinary ancestor `Q/4^k` has `Lambda(Q/4^k)=0`.
Therefore its positive ordinary slack `R_4 e_Q` has identically zero image
under the prime radial transform. The large zero-weight triangular repair cone
of PR #470 is a genuine radial null gauge.

Only the positive-`Y_4` quotient contributes to (L-19880.22). This permits
coefficientwise current repair before any RH-bearing radial source is spent.

## 7. Completed arithmetic direct sum

The prime dictionary (L-19880.14) may be adjoined orthogonally to the exact
eta, compact-bridge, gamma/pole, reflected-orientation, and compressed-delay
source columns of PRs #404, #427 and #430. Those channels already carry
coefficient-one positive interval refinements. Therefore they add zero
source-allocation slack, while the prime channel carries the explicit slack
(L-19880.12).

This gives one source-owned **completed arithmetic** radial feature dictionary.
It does not yet identify the complete critical/stable/hyperbolic model measure
as a contraction of that dictionary.

## 8. Exact proof boundary

Proved here, pending review:

```text
native ordinary ramp -> prime radial coefficient       EXACT LAPLACE IDENTITY
source-owned native thinning -> radial thinning        COEFFICIENTWISE POSITIVE
common carrier dictionary                              EXPLICIT
interval refinement and packet compatibility           EXACT
radix-four detail slack -> ordinary/radial slack        EXACT ON L-91687
native entropy debt -> radial slack Laplace budget      EXACT
Y4-zero repair -> prime radial null gauge                EXACT / L-19881
eta/bridge/gamma source completion                      DIRECT-SUM IMPORT
```

Not proved here:

```text
SONTR finite native producer                            OPEN ON PR #470
complete model allocation in the same columns           OPEN
intervalwise arithmetic >= complete model kernel        OPEN
Riemann Hypothesis                                      UNPROVED
```
