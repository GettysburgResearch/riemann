# L-23801 — Exact carry, Legendre, entropy, and packing-mass consumer

Claim ID: `L-23801`  
Title: Every feasible carry packing gives a prime-ramp lower bound, has logarithmic coefficient mass, and converts mass eight into entropy four  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-23`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`  
Scope: finite algebra and elementary estimates; no asymptotic packing theorem

## 1. Floor-sum form of the carry matrix

For `n=aq+r`, `0<=r<q`,

\[
\sum_{j=0}^{n}\left\lfloor\frac jq\right\rfloor
=q\frac{a(a-1)}2+a(r+1).
\tag{L-23801.1}
\]

Substitution gives the equivalent identity

\[
\boxed{
\beta_{nq}
=\left\lfloor\frac nq\right\rfloor
-\frac2{n+1}\sum_{j=0}^{n}
 \left\lfloor\frac jq\right\rfloor.}
\tag{L-23801.2}
\]

The right side is the average carry across the `q`-place in
`j+(n-j)=n`.

## 2. Exact Legendre factorization

For a prime `p`, Legendre's formula yields

\[
v_p\binom nj
=\sum_{k\ge1}
\left(
 \left\lfloor\frac n{p^k}\right\rfloor
 -\left\lfloor\frac j{p^k}\right\rfloor
 -\left\lfloor\frac{n-j}{p^k}\right\rfloor
\right).
\]

Average over `j` and use (L-23801.2). Then

\[
\frac1{n+1}\sum_{j=0}^{n}v_p\binom nj
=\sum_{k\ge1}\beta_{n,p^k}.
\]

Consequently

\[
\boxed{
G_n
=\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.}
\tag{L-23801.3}
\]

This is an exact finite identity.

## 3. Packing lower bound for the prime ramp

Let `d` be a carry packing. Since `Lambda(q)>=0`,

\[
\begin{aligned}
\mathcal P(X)
&=\sum_{q=p^k\le X}\Lambda(q)w_X(q)\\
&\ge\sum_{q=p^k\le X}\Lambda(q)(B_X^Td)(q)\\
&=\sum_{n=2}^Xd(n)G_n.
\end{aligned}
\]

Thus

\[
\boxed{
\mathcal P(X)\ge\sum_{n=2}^Xd(n)G_n.}
\tag{L-23801.4}
\]

Only a lower packing is used.

## 4. Elementary entropy estimate

For `0<=x<=1`, let

\[
H(x)=-x\log x-(1-x)\log(1-x).
\]

The type bound

\[
\log\binom nj
\ge nH(j/n)-\log(n+1)-2
\]

and elementary integral comparison with

\[
\int_0^1H(x)dx=\frac12
\]

give

\[
\boxed{
G_n\ge\frac n2-\log(n+1)-3.}
\tag{L-23801.5}
\]

The constant is deliberately nonoptimal.

## 5. Every all-column packing has logarithmic coefficient mass

Put

\[
S_n=\sum_{q=2}^n\frac{\beta_{nq}}q.
\]

For `n>=8`, restrict to

\[
\left\lceil\frac{3(n+1)}4\right\rceil\le q\le n.
\]

There are at least `n/8` such integers. On this range `q>n/2`, so

\[
\beta_{nq}=\frac{2q-n-1}{n+1}\ge\frac12,
\qquad q^{-1}\ge n^{-1}.
\]

Hence `S_n>=1/16`. Direct checking gives the same bound for `2<=n<8`.
Therefore

\[
\boxed{
S_n\ge\frac1{16}\qquad(n\ge2).}
\tag{L-23801.6}
\]

Multiply every packing constraint by `1/q` and sum:

\[
\frac1{16}\sum_{n=2}^Xd(n)
\le
\sum_{q=2}^X\frac{w_X(q)}q
=
\sum_{q=2}^Xq^{-3/2}\log(X/q)
\ll\log X.
\]

Thus

\[
\boxed{
\mathcal C_X(d)=\sum_{n=2}^Xd(n)\ll\log X}
\tag{L-23801.7}
\]

for every feasible all-column packing.

## 6. Mass eight gives entropy four

Combining (L-23801.5) and (L-23801.7),

\[
\begin{aligned}
\sum_{n=2}^Xd(n)G_n
&\ge\frac12\mathcal M_X(d)
 -\sum_{n=2}^Xd(n)(\log(n+1)+3)\\
&\ge\frac12\mathcal M_X(d)-O(\log^2X).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal M_X(d)
\ge8\sqrt X-X^{o(1)}
\Longrightarrow
\mathcal P(X)
\ge4\sqrt X-X^{o(1)}.}
\tag{L-23801.8}
\]

Here `X^(o(1))` means `O_epsilon(X^epsilon)` for every fixed positive
`epsilon`.

## 7. Proof boundary

Closed exactly:

- the carry/floor identity;
- the averaged Legendre factorization;
- the packing-to-prime-ramp inequality;
- the entropy lower bound;
- logarithmic coefficient mass for every all-column packing;
- mass-eight to entropy-four conversion.

Open:

- a packing with the required mass;
- the Greedy Residual theorem;
- RH.
