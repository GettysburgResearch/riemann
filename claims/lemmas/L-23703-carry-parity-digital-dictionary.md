# L-23703 — Exact carry–parity digital dictionary

Claim ID: `L-23703`  
Title: Binary carry occupation and the positive parity-comb inverse are the forward and backward ledgers of the same digit filtration  
Status: **PROPOSED EXACT DICTIONARY PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`; PR #236 `L-23010`--`L-23012`  
Scope: exact finite and distributional identities; no coercivity estimate is asserted

## 1. Binary carry occupation

For `q=2^k`, let

\[
C_{n,k}(j)
=
\mathbf1_{\{j\bmod2^k>n\bmod2^k\}}.
\tag{L-23703.1}
\]

Then

\[
\boxed{
\beta_{n,2^k}
=
\frac1{n+1}\sum_{j=0}^n C_{n,k}(j).}
\tag{L-23703.2}
\]

Kummer's theorem gives

\[
 v_2{n\choose j}
=
\sum_{k\ge1}C_{n,k}(j).
\tag{L-23703.3}
\]

Therefore the binary part of the carry row is

\[
\boxed{
(\log2)
\sum_{2^k\le n}\beta_{n,2^k}
=
\frac{\log2}{n+1}
\sum_{j=0}^n v_2{n\choose j}.}
\tag{L-23703.4}
\]

Using

\[
 v_2(m!)=m-s_2(m),
\]

one also has

\[
\boxed{
 v_2{n\choose j}
=s_2(j)+s_2(n-j)-s_2(n).}
\tag{L-23703.5}
\]

Thus every nonnegative carry coefficient is an average conditional digit loss.

## 2. Euler-aligned dyadic source

Retain the multiplicative coefficient

\[
 b_2(m)=
 \mu(m)-\mathbf1_{2\mid m}\mu(m/2).
\tag{L-23703.6}
\]

Its summatory function is the dyadic Mertens shell:

\[
\boxed{
\sum_{m\le x}b_2(m)=M(x)-M(x/2).}
\tag{L-23703.7}
\]

In normalized logarithmic coordinates,

\[
\beta_2
=
\sum_{m\ge1}{b_2(m)\over\sqrt m}\delta_{\log m}
\tag{L-23703.8}
\]

satisfies

\[
\boxed{
\left(\partial_t+\frac12\right)Q_{1/2}=\beta_2.}
\tag{L-23703.9}
\]

## 3. Backward digit Green kernel

Let

\[
S_2(t)=e^{-t/2}s_2(\lfloor e^t\rfloor)
\]

and

\[
P_2(t)=e^{-t/2}
\mathbf1_{\{\lfloor e^t\rfloor\text{ odd}\}}.
\]

PR #236 proves

\[
\boxed{
S_2
=
\sum_{r\ge0}2^{-r/2}\tau_{r\log2}P_2,}
\tag{L-23703.10}
\]

and

\[
\boxed{
S_2*\beta_2
=w_\infty-\sqrt2\,\tau_{\log2}w_\infty.}
\tag{L-23703.11}
\]

Equivalently,

\[
\boxed{
P_2*\beta_2
=w_\infty-rac3{\sqrt2}\tau_{\log2}w_\infty
+\tau_{2\log2}w_\infty.}
\tag{L-23703.12}
\]

The forward carry ledger sums the binary carry indicators `C_(n,k)`. The
backward kernel `S_2` sums the corresponding binary digit layers. Equations
(L-23703.4)--(L-23703.12) are the exact dictionary between the two descriptions.

## 4. Finite integer form of the parity convolution

For integer `N>=1`, (L-23703.12) is equivalent to

\[
\sum_{m\le N}
 b_2(m)
\mathbf1_{\{\lfloor N/m\rfloor\text{ odd}\}}
=
\begin{cases}
1,&N=1,\\
-2,&2\le N\le3,\\
0,&N\ge4.
\end{cases}
\tag{L-23703.13}
\]

Likewise (L-23703.11) gives

\[
\boxed{
\sum_{m\le N}b_2(m)s_2(\lfloor N/m\rfloor)
=
\begin{cases}
1,&N=1,\\
-1,&N\ge2.
\end{cases}}
\tag{L-23703.14}
\]

These are exact finite divisor identities. They give mandatory mutation tests
for any proposed digital or carry completion.

## 5. Why the combination may be stronger than either route alone

The parity-comb equation by itself is a first-kind convolution whose transform
contains the full eta/zeta zero set. Generic stable inversion is RH-equivalent.

Full Carry Saturation by itself asks for every coefficient of one exact
triangular inverse to be nonnegative. That statement is stronger than needed.

The greedy carry minorant provides a third interface:

```text
positive at every finite endpoint
feasible for every prime-power row
not required to invert the carry matrix exactly
measured only by aggregate entropy mass
```

The proposed closing theorem can therefore use the digital identities only to
amortize the aggregate loss created by off-diagonal blockers. It need not prove
a generic inverse bound for `P_2` and need not prove pointwise positivity of the
exact carry inverse.

## 6. Digital blocker theorem — exact formulation

Let `d_X` be the greedy vector of `L-23701` and define

\[
\mathfrak M_X=\sum_{n\le X}n d_X(n),
\qquad
\mathfrak L_X=\sum_{n\le X}d_X(n)(\log(n+1)+3).
\]

The precise remaining arithmetic statement is

\[
\boxed{
\mathrm{DBT}:
\quad
\mathfrak M_X\ge8\sqrt X-O(\log^A X),
\qquad
\mathfrak L_X=O(\log^A X).}
\tag{L-23703.15}
\]

The proposed proof mechanism is a quotient-layer martingale argument:

1. group blockers with the same quotient `floor(n/q)` before taking absolute
   values;
2. expose the base-`p` carry indicators for every prime-power row;
3. use the positive digit kernels as conditional-variance reservoirs;
4. charge only the unmatched parity component to the reflected Selberg square;
5. telescope the remaining band energies to smaller endpoints.

The exact finite object to be bounded is the blocker/slack ledger emitted by
`L-23701`; there is no unspecified Type-II packet family in the statement.

## 7. Proof boundary

Closed exactly:

- binary carry occupation;
- the digit-sum form of Kummer's theorem;
- the dyadic shell source;
- the positive digit and parity convolution identities;
- the finite integer mutation identities;
- the exact aggregate theorem that would finish the route.

Open:

- DBT;
- the quotient-layer conditional-variance estimate proposed to prove it;
- RH.