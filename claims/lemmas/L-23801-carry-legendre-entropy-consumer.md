# L-23801 — Carry--Legendre entropy consumer

Claim ID: `L-23801`  
Title: Every nonnegative carry packing is a certified lower bound for the prime ramp, and near-saturation implies RH  
Status: **PROPOSED COMPLETE FINITE/ANALYTIC TRANSFER**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`; the safe-filter Hardy/Landau transfer of `L-15151` and the square-screw criterion of PR #202  
Scope: exact consumer; the packing theorem remains separate

## 1. Carries in one binomial row

Fix `2<=q<=n` and write

\[
 n=aq+r,
 \qquad
 0\le r<q.
\]

For `0<=j<=n`, put

\[
 C_q(n,j)
 =\left\lfloor\frac nq\right\rfloor
  -\left\lfloor\frac jq\right\rfloor
  -\left\lfloor\frac{n-j}{q}\right\rfloor.
 \tag{L-23801.1}
\]

The value is `0` or `1`; it is the carry across the `q`-place in the addition
`j+(n-j)=n`. Since

\[
 \sum_{j=0}^n\left\lfloor\frac jq\right\rfloor
 =q\frac{a(a-1)}2+a(r+1),
 \tag{L-23801.2}
\]

we obtain

\[
 \boxed{
 \frac1{n+1}\sum_{j=0}^nC_q(n,j)
 =\frac{a(q-1-r)}{n+1}
 =\beta_{nq}.}
 \tag{L-23801.3}
\]

## 2. Exact Legendre identity

For a prime `p`, Legendre's formula gives

\[
 v_p\binom nj
 =\sum_{k\ge1}C_{p^k}(n,j).
 \tag{L-23801.4}
\]

Therefore, with

\[
 G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj,
\]

finite rearrangement yields

\[
 \boxed{
 G_n
 =\sum_{p^k\le n}\log p\,\beta_{n,p^k}
 =\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.}
 \tag{L-23801.5}
\]

No asymptotic estimate is used.

## 3. Entropy lower bound

The elementary type bound

\[
 \binom nj
 \ge\frac1{n+1}
 \exp\left[nH\!\left(\frac jn\right)\right],
 \qquad
 H(x)=-x\log x-(1-x)\log(1-x),
 \tag{L-23801.6}
\]

and a one-interval comparison with

\[
 \int_0^1H(x)dx=\frac12
 \tag{L-23801.7}
\]

give the safe uniform estimate

\[
 \boxed{
 G_n
 \ge\frac n2-\log(n+1)-3.}
 \tag{L-23801.8}
\]

The constant `3` is deliberately nonoptimal. A proof may instead use the exact
factorial identity

\[
 (n+1)G_n
 =(n+1)\log(n!)-2\sum_{j=1}^n\log(j!)
 \tag{L-23801.9}
\]

and elementary integral bounds for `log Gamma`.

## 4. Packing lower bound for the prime ramp

Define the complete prime-power ramp

\[
 \mathcal P(X)
 =\sum_{q=p^k\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 =\sum_{q=p^k\le X}\Lambda(q)w_X(q).
 \tag{L-23801.10}
\]

Let `d` be any carry packing. Since `Lambda(q)>=0`, feasibility and
(L-23801.5) give

\[
 \begin{aligned}
 \mathcal P(X)
 &\ge
 \sum_{q=p^k\le X}\Lambda(q)(B_X^Td)(q)\\
 &=\sum_{n=2}^Xd(n)G_n.
 \end{aligned}
 \tag{L-23801.11}
\]

Put

\[
 \mathcal M_X(d)=\sum_{n=2}^Xn d(n),
 \tag{L-23801.12}
\]

\[
 \mathcal L_X(d)
 =\sum_{n=2}^Xd(n)(\log(n+1)+3).
 \tag{L-23801.13}
\]

Then

\[
 \boxed{
 \mathcal P(X)
 \ge\frac12\mathcal M_X(d)-\mathcal L_X(d).}
 \tag{L-23801.14}
\]

In profile coordinates of `D-23801`,

\[
 \mathcal M_X(d)
 =6P_d(2)+2\sum_{j=4}^XP_d(j).
 \tag{L-23801.15}
\]

Thus a sharp prime-ramp lower bound is reduced to the area of one nonnegative
admissible convex profile.

## 5. Carry-envelope criterion

Assume that for every `epsilon>0` and all sufficiently large `X` there is a
carry packing `d_(X,epsilon)` such that

\[
 \boxed{
 \mathcal M_X(d_{X,\varepsilon})
 \ge8\sqrt X-C_\varepsilon X^\varepsilon,}
 \tag{L-23801.16}
\]

and

\[
 \boxed{
 \mathcal L_X(d_{X,\varepsilon})
 \le C_\varepsilon X^\varepsilon.}
 \tag{L-23801.17}
\]

Then

\[
 \boxed{
 \mathcal P(X)
 \ge4\sqrt X-C'_\varepsilon X^\varepsilon.}
 \tag{L-23801.18}
\]

This criterion is strictly weaker than exact Carry Saturation. It neither
requires `B_X^Td=w_X` nor requires the exact inverse coefficients to be
nonnegative.

## 6. Transfer to RH

The square-screw identity has the form

\[
 \Psi(\log X)
 =4\left(\sqrt X+X^{-1/2}-2\right)
 -\mathcal P(X)
 +O(\log X),
 \tag{L-23801.19}
\]

with the exact gamma/Lerch correction recorded in PR #202. Equation
(L-23801.18) implies, for every `epsilon>0`,

\[
 \Psi(\log X)
 \le C_\varepsilon X^\varepsilon.
 \tag{L-23801.20}
\]

At square samples `X=N^2`, the negative-part/rightmost-zero theorem gives

\[
 \Theta_\zeta
 =\limsup_{N\to\infty}
 \frac{\log(1+(-\Psi(2\log N))_+)}{2\log N}=0.
 \tag{L-23801.21}
\]

Functional-equation symmetry then gives

\[
 \boxed{\mathrm{RH}.}
 \tag{L-23801.22}
\]

The same conclusion follows through the safe-filter Hardy abscissa theorem
`L-15151`.

## 7. Proof boundary

Closed:

- exact carry average;
- exact Legendre identity;
- elementary entropy lower bound;
- packing-to-prime-ramp inequality;
- carry-envelope criterion implies RH.

Open:

- the near-saturating packing estimates (L-23801.16)--(L-23801.17).
