# R-30501 — Terminal atomic lifting of the cutoff tail has linear critical cost

Claim ID: `R-30501`  
Title: The finite cutoff tail cannot be converted into a next-half divisor source of polylogarithmic square-root atomic norm  
Status: **EXACT LOAD-BEARING REFUTATION OF PR #304 `L-30403/T-30401`**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #286 `L-28402`; elementary alternating-series and divisor-triangularity arguments  
Scope: the claimed terminal divisor-source lift of one stopped critical power

## 1. The stopped critical power and its cutoff tail

Put

\[
f(x)=x^{-1/2}.
\]

For integer `q>=2`, define the paired infinite shifted operator

\[
(\mathscr C f)(q)
=\sum_{k\ge1}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right].
\tag{R-30501.1}
\]

The paired series converges absolutely after one mean-value estimate. For an endpoint `N`, define

\[
(\mathscr C_N f^{[N]})(q)
=\sum_{k\ge1}
\left[f^{[N]}(2kq-1)-f^{[N]}((2k+1)q)\right]
\tag{R-30501.2}
\]

and the exact cutoff tail

\[
\boxed{
B_N(q)=(\mathscr C f)(q)-(\mathscr C_Nf^{[N]})(q).
}
\tag{R-30501.3}
\]

Let

\[
M=\left\lfloor\frac{N+1}{2}\right\rfloor.
\]

PR #304 requires `B_N`, or each stopped-power component of it, to be represented at the next-half endpoint by a divisor source `sigma_N` satisfying

\[
\boxed{
B_N(q)=\sum_{j\le M/q}\sigma_N(jq)
\qquad(2\le q\le M),
}
\tag{R-30501.4}
\]

with square-root atomic norm

\[
\|\sigma_N\|_{\rm at}
=\sum_{m=2}^{M}\sqrt m\,|\sigma_N(m)|
\tag{R-30501.5}
\]

claimed polylogarithmic.

## 2. A fixed macroscopic quotient cell

Consider integers

\[
\frac N3<q\le\frac N2.
\tag{R-30501.6}
\]

Exactly one shifted-even term remains inside the finite endpoint, and no odd term remains:

\[
\boxed{
(\mathscr C_Nf^{[N]})(q)=(2q-1)^{-1/2}.
}
\tag{R-30501.7}
\]

Indeed `2q-1<=N`, while `3q>N` and `4q-1>N`.

Write

\[
\rho
=\sum_{k\ge1}
\left[(2k)^{-1/2}-(2k+1)^{-1/2}\right]
=1-\eta(1/2).
\tag{R-30501.8}
\]

For `epsilon=1/q`, multiplication of (R-30501.1) by `sqrt(q)` gives

\[
\sqrt q\,(\mathscr C f)(q)
=\rho+S_q,
\tag{R-30501.9}
\]

where

\[
S_q=\sum_{k\ge1}
\left[(2k-\epsilon)^{-1/2}-(2k)^{-1/2}\right].
\]

The mean-value theorem gives

\[
\begin{aligned}
0<S_q
&\le \frac{\epsilon}{2}
\sum_{k\ge1}(2k-\epsilon)^{-3/2}\\
&\le \frac{\epsilon}{2}
\left(\frac23\right)^{3/2}\zeta(3/2)
<\epsilon.
\end{aligned}
\tag{R-30501.10}
\]

The last inequality uses the elementary bound `zeta(3/2)<3`.

## 3. An elementary strict sign moat

Pairing the alternating eta series gives

\[
\eta(1/2)
=\sum_{k\ge1}
\left[(2k-1)^{-1/2}-(2k)^{-1/2}\right].
\]

For `k>=2`,

\[
(2k-1)^{-1/2}-(2k)^{-1/2}
\ge\frac1{2(2k)^{3/2}}.
\]

Hence

\[
\begin{aligned}
\eta(1/2)
&>1-\frac1{\sqrt2}
+2^{-5/2}\int_2^\infty x^{-3/2}\,dx\\
&=\frac54-\frac1{\sqrt2}
>\frac12.
\end{aligned}
\tag{R-30501.11}
\]

Therefore

\[
\rho<\frac12.
\tag{R-30501.12}
\]

Using (R-30501.7), (R-30501.9), and (R-30501.10), for every `q>=10` in (R-30501.6),

\[
\begin{aligned}
\sqrt q\,B_N(q)
&=\rho+S_q-(2-1/q)^{-1/2}\\
&\le \frac12+\frac1q-\frac1{\sqrt2}\\
&<-\frac1{10}.
\end{aligned}
\tag{R-30501.13}
\]

Here `1/sqrt(2)>7/10` was used in the last line. Thus

\[
\boxed{
|B_N(q)|>\frac1{10\sqrt q}
\qquad
\left(\frac N3<q\le\frac N2,\ q\ge10\right).
}
\tag{R-30501.14}
\]

This is a cofinal analytic estimate, not finite reconnaissance.

## 4. Triangular uniqueness forces linear atomic norm

For every `q>M/2`, equation (R-30501.4) has only one term:

\[
\boxed{
\sigma_N(q)=B_N(q).
}
\tag{R-30501.15}
\]

The whole interval in (R-30501.6) lies above `M/2` once `N>3`. Therefore, for every `N>=60`,

\[
\begin{aligned}
\|\sigma_N\|_{\rm at}
&\ge
\sum_{N/3<q\le N/2}
\sqrt q\,|\sigma_N(q)|\\
&>\frac1{10}
\left(\left\lfloor\frac N2\right\rfloor
-\left\lfloor\frac N3\right\rfloor\right)\\
&\ge\boxed{\frac N{100}}.
\end{aligned}
\tag{R-30501.16}
\]

Thus no next-half divisor source reproducing the cutoff tail can have polylogarithmic square-root atomic norm.

## 5. Consequence for the stopped-power layer cake

PR #301 resolves the critical logarithmic target as

\[
w_X(q)=\sum_{Y=q}^{X-1}
\log\frac{Y+1}{Y}\,q^{-1/2}.
\]

For one endpoint layer `Y`, (R-30501.16) and

\[
\log\left(1+\frac1Y\right)\ge\frac1{Y+1}
\]

show that terminally lifting that layer already costs at least one absolute constant in atomic norm. Summing layer norms before cancellation therefore costs order `X`, not `polylog(X)`.

A valid continuation must recombine the endpoint layers and the analytic tail **before** applying an atomic norm. The large cutoff source is canceled by the large analytic continuation on the same quotient cells. PR #304 separated those two terms and paid the cancellation twice.

## 6. Exact disposition

```text
adjacent commutator realizes a genuine divisor source       VERIFIED
bounded map sigma -> Phi(sigma)                             VERIFIED
cutoff tail is a next-half divisor source of polylog norm   FALSE
PR #286 cap norm = PR #304 atomic divisor norm              FALSE AS CLAIMED
terminal boundary lifting in T-30401                        REJECTED
Cycle Debt and RH                                           UNPROVEN
```

This refutation does not reject the central cascade. It rejects only the terminal atomic treatment of the cutoff tail. The correct route must preserve the complete finite analytic/cutoff cancellation.