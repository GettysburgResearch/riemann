# L-32704 — Cofinal parity-paired mixed Selberg–Kummer closure

Claim ID: `L-32704`  
Title: The parity-paired Euler source absorbs the complete generalized Selberg forcing on every sufficiently large carry row; the mixed odd-prime/dyadic channel is one strict four-adic descendant plus a current-row term already paid by the Kummer cross energy  
Status: **PROPOSED COMPLETE COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26202/L-26205`; PR #334 `L-32405`; ordinary Kummer/Legendre identities  
Scope: source-complete parity-paired carry-row inequality; physical independent-frequency recurrence and RH remain separate

## 1. Paired generalized-prime rows

Retain the Euler-filtered inverse of PR #263. Its generalized-prime coefficients are

\[
\Lambda_{\mathcal E}^{\#}(p^a)=\log p\qquad(p\ {m odd}),
\tag{L-32704.1}
\]

and

\[
\Lambda_{\mathcal E}^{\#}(2^k)
=(2^{k/2}+1)^2\log2.
\tag{L-32704.2}
\]

Let

\[
\chi_2(d)=(-1)^{v_2(d)},
\qquad
\Lambda_+=\Lambda_{\mathcal E}^{\#},
\qquad
\Lambda_-=\chi_2\Lambda_+,
\tag{L-32704.3}
\]

and

\[
C_\pm=\Lambda_\pm\log+\Lambda_\pm*\Lambda_\pm.
\tag{L-32704.4}
\]

For a carry row `n=j+k`, put

\[
\chi_{n,d}(j)
=\left\lfloor\frac nd\right\rfloor
-\left\lfloor\frac jd\right\rfloor
-\left\lfloor\frac kd\right\rfloor
\in\{0,1\},
\tag{L-32704.5}
\]

and define

\[
P_\pm(n,j)=\sum_{d\le n}\Lambda_\pm(d)\chi_{n,d}(j),
\qquad
S_\pm(n,j)=\sum_{d\le n}C_\pm(d)\chi_{n,d}(j).
\tag{L-32704.6}
\]

The theorem proved below is

\[
\boxed{
P_+(n,j)^2+P_-(n,j)^2
\ge S_+(n,j)+S_-(n,j)
}
\tag{L-32704.7}
\]

for every sufficiently large `n` and every `0<=j<=n`.

This is exactly the source-matched inequality that the generalized-prime counterexample `R-29002` showed could not be obtained from one unpaired scalar row.

## 2. Orthogonalize the two-adic parity

Write

\[
O(n,j)
=\sum_{q=p^a,\ p\ {m odd}}
 \Lambda(q)\chi_{n,q}(j)
=\log\operatorname{odd}\binom nj,
\tag{L-32704.8}
\]

and, with

\[
D_k=(2^{k/2}+1)^2\log2,
\tag{L-32704.9}
\]

put

\[
E(n,j)=\sum_{r\ge1}D_{2r}\chi_{n,4^r}(j),
\qquad
R(n,j)=\sum_{r\ge1}D_{2r-1}\chi_{n,2^{2r-1}}(j).
\tag{L-32704.10}
\]

Then exactly

\[
P_+=O+E+R,
\qquad
P_-=O+E-R,
\tag{L-32704.11}
\]

so

\[
\boxed{
\frac{P_+^2+P_-^2}{2}
=(O+E)^2+R^2.}
\tag{L-32704.12}
\]

Because `C_-=chi_2 C_+`, the paired forcing keeps exactly the destinations of even two-adic valuation:

\[
\frac{S_++S_-}{2}
=S_{\rm odd}+S_{\rm dyad}+M,
\tag{L-32704.13}
\]

where:

- `S_odd` is the Selberg forcing built only from odd prime powers;
- `S_dyad` is the complete pure-dyadic even-parity forcing;
- `M` is the mixed odd-prime/even-dyadic convolution forcing.

PR #334 `L-32405` proves coefficientwise that the full pure-dyadic forcing, including the odd-odd dyadic convolution channel, is dominated by the corresponding even-dyadic generalized-prime square. Therefore, on every row,

\[
\boxed{S_{\rm dyad}\le E^2.}
\tag{L-32704.14}
\]

Indeed each coefficient at `4^r` is at most `D_(2r)^2`, and
`sum D_(2r)^2 chi_(n,4^r)<=E^2`.

## 3. Exact four-adic product-carry identity

Fix

\[
a=4^r,
\qquad
N=\left\lfloor\frac na\right\rfloor,
\qquad
J=\left\lfloor\frac ja\right\rfloor,
\qquad
c=\chi_{n,a}(j).
\tag{L-32704.15}
\]

For every positive integer `q`,

\[
\boxed{
\chi_{n,aq}(j)
=\chi_{N,q}(J)
+c\,\mathbf1_{q\mid N-J}.}
\tag{L-32704.16}
\]

### Proof

The first two floor terms are exactly

\[
\left\lfloor\frac n{aq}\right\rfloor=\left\lfloor\frac Nq\right\rfloor,
\qquad
\left\lfloor\frac j{aq}\right\rfloor=\left\lfloor\frac Jq\right\rfloor.
\]

Since a carry in the `a`-column is binary,

\[
\left\lfloor\frac{k}{a}\right\rfloor=N-J-c.
\]

If `c=0`, (L-32704.16) is immediate. If `c=1`, then

\[
\left\lfloor\frac{N-J}{q}\right\rfloor
-
\left\lfloor\frac{N-J-1}{q}\right\rfloor
=\mathbf1_{q\mid N-J},
\]

which proves the identity.

The mixed forcing is therefore not an irreducible same-scale object. Since an even dyadic prime atom `4^r` and an odd prime-power atom `q` can occur in either convolution order,

\[
M
=2\sum_{r\ge1}D_{2r}
 \sum_{q=p^a,\ p\ {m odd}}
 \Lambda(q)\chi_{n,4^rq}(j).
\tag{L-32704.17}
\]

Applying (L-32704.16) yields the exact decomposition

\[
\boxed{
M=M_{<}+M_{\partial},}
\tag{L-32704.18}
\]

with

\[
\boxed{
M_{<}
=2\sum_{r\ge1}D_{2r}
 O(N_r,J_r),}
\tag{L-32704.19}
\]

and

\[
\boxed{
M_{\partial}
=2\sum_{r\ge1}D_{2r}c_r
 \log\operatorname{odd}(N_r-J_r).}
\tag{L-32704.20}
\]

Here `N_r=floor(n/4^r)`, `J_r=floor(j/4^r)`, and `c_r=chi_(n,4^r)(j)`.

The first term is a strict `4^{-r}` descendant odd-prime Kummer profile. The second is one explicit current-row divisor boundary.

## 4. The current-row boundary is paid exactly by the cross energy

We prove, whenever `c_r=1`,

\[
\boxed{
\log\operatorname{odd}(N_r-J_r)\le O(n,j).}
\tag{L-32704.21}
\]

By symmetry assume `1<=j<=n/2`.

If `j=1`, the condition `c_r=1` says `4^r|n`. Then `J_r=0`, `N_r=n/4^r`, and

\[
\operatorname{odd}(N_r)=\operatorname{odd}(n)
=\operatorname{odd}\binom n1,
\]

so equality holds.

Now let `j>=2` and put `B=binom(n,j)`. Kummer's binary-carry theorem gives

\[
v_2(B)\le\lfloor\log_2n\rfloor,
\]

because a binary addition producing `n` has at most one carry at each position below its top bit. Hence

\[
\operatorname{odd}(B)
=\frac{B}{2^{v_2(B)}}
\ge\frac{B}{n}.
\tag{L-32704.22}
\]

For `2<=j<=n/2`, binomial monotonicity gives

\[
B\ge\binom n2=\frac{n(n-1)}2,
\]

and therefore

\[
\operatorname{odd}(B)\ge\frac{n-1}{2}\ge\frac n4.
\tag{L-32704.23}
\]

But `4^r>=4`, so

\[
N_r-J_r\le N_r\le\frac n{4^r}\le\frac n4.
\]

Thus

\[
\operatorname{odd}(N_r-J_r)
\le N_r-J_r
\le\operatorname{odd}(B),
\]

which proves (L-32704.21).

Since

\[
E=\sum_rD_{2r}c_r,
\]

we immediately obtain

\[
\boxed{M_{\partial}\le2OE.}
\tag{L-32704.24}
\]

This is the no-double-spend step missing from a rowwise source lift: the exact mixed boundary is consumed by the actual odd/even cross term already present in the paired Kummer square.

Combining (L-32704.12)--(L-32704.14) and (L-32704.24),

\[
\boxed{
\frac{P_+^2+P_-^2-S_+-S_-}{2}
\ge O^2-S_{\rm odd}-M_{<}+R^2.}
\tag{L-32704.25}
\]

It remains only to bound the strict four-adic descendants.

## 5. Elementary bounds for the odd-prime row

Again assume `1<=j<=n/2` and write `t=log n`.

Let

\[
g(m)=\log\operatorname{odd}(m).
\]

The odd-prime Selberg identity gives

\[
S_{\rm odd}
=\sum_{m\le n}g(m)^2
 -\sum_{m\le j}g(m)^2
 -\sum_{m\le n-j}g(m)^2.
\]

Consequently

\[
\boxed{0\le S_{\rm odd}\le j(\log n)^2=jt^2.}
\tag{L-32704.26}
\]

Also

\[
O=\log\operatorname{odd}\binom nj.
\]

Kummer again gives `2^(v_2(B))<=n`, while

\[
\binom nj\ge(n/j)^j.
\]

Therefore

\[
\boxed{
O\ge j\log\frac nj-\log n.}
\tag{L-32704.27}
\]

For the descendant term, put `a=4^r`. If `J_r=0`, then `O(N_r,J_r)=0`. If `J_r>=1`, then `a<=j` and

\[
\frac{N_r}{J_r}<\frac{2n}{j},
\]

because `j/a<J_r+1<=2J_r`. Hence

\[
O(N_r,J_r)
\le\log\binom{N_r}{J_r}
\le\frac ja\log\frac{2en}{j}.
\tag{L-32704.28}
\]

Moreover

\[
D_{2r}=(\sqrt a+1)^2\log2
\le\frac94a\log2
\qquad(a\ge4).
\tag{L-32704.29}
\]

There are at most `log_4 j` nonzero descendant levels. Thus

\[
\boxed{
M_{<}
\le\frac94j
 \log\frac{2en}{j}\,\log j.}
\tag{L-32704.30}
\]

This already shows that the mixed source which looked same-scale in coefficient space has only one logarithmic stack of strict four-adic descendants.

## 6. Uniform cofinal domination for every `j>=8`

Let `c_0=log(2e)`. For all sufficiently large `n`,

\[
\log\frac{2en}{j}\le\frac32t,
\qquad
\log j\le t.
\]

Hence (L-32704.26) and (L-32704.30) give

\[
\boxed{
S_{\rm odd}+M_<
\le\frac{35}{8}jt^2.}
\tag{L-32704.31]
\]

(The closing bracket in the tag is typographical only.)

We prove that the right side is at most `O^2` for every `8<=j<=n/2`, once `n` is sufficiently large.

### Case A: `8<=j<=n^(1/8)`

Equation (L-32704.27) gives

\[
O\ge\left(\frac{7j}{8}-1\right)t.
\]

For every `j>=8`,

\[
\left(\frac{7j}{8}-1\right)^2
-\frac{35}{8}j
=\frac{49j(j-8)+64}{64}>0.
\]

Thus

\[
O^2>S_{\rm odd}+M_<.
\tag{L-32704.32}
\]

### Case B: `n^(1/8)<j<=n/2`

Now `log(n/j)>=log2`, so

\[
O\ge j\log2-t.
\]

Since `e^(t/8)/t^2 -> infinity`, for all sufficiently large `t` every
`j>e^(t/8)` satisfies simultaneously

\[
j\log2\ge2t
\]

and

\[
j\ge\frac{35}{2(\log2)^2}t^2.
\]

Therefore

\[
O\ge\frac12j\log2
\]

and

\[
O^2
\ge\frac14j^2\log^22
\ge\frac{35}{8}jt^2
\ge S_{\rm odd}+M_<.
\tag{L-32704.33}
\]

This proves the desired domination uniformly for every `j>=8`.

## 7. The finitely many small child indices

For `j=1`, the complete generalized Selberg identity has endpoint equality:

\[
P_\pm(n,1)^2=S_\pm(n,1).
\tag{L-32704.34}
\]

For `j=2`, no strict four-adic descendant occurs because `floor(2/4^r)=0`. Put

\[
a=\log\operatorname{odd}(n),
\qquad
b=\log\operatorname{odd}(n-1).
\]

Then

\[
O(n,2)=a+b,
\qquad
S_{\rm odd}(n,2)=a^2+b^2,
\]

so

\[
\boxed{O(n,2)^2-S_{\rm odd}(n,2)=2ab\ge0.}
\tag{L-32704.35}
\]

Thus (L-32704.7) holds for `j=2` at every endpoint.

For `j=3`, again `M_<=0`. Equations (L-32704.26)--(L-32704.27) give

\[
O\ge2t-3\log3,
\qquad
S_{\rm odd}\le3t^2,
\]

so `O^2>S_odd` for all sufficiently large `n`.

For each fixed `j in {4,5,6,7}`, only `r=1` can contribute to `M_<`, and

\[
M_<\le18(\log2)t.
\]

Meanwhile

\[
O\ge(j-1)t-j\log j,
\]

and

\[
(j-1)^2-j>0.
\]

Therefore

\[
O^2-jt^2-18(\log2)t>0
\]

for all sufficiently large `n`. Since this is only a fixed finite set of `j`, one common threshold handles all four cases.

By row symmetry the same conclusions hold for `n-j` in place of `j`.

Combining Sections 6--7 proves:

\[
\boxed{
\exists n_0\ \forall n\ge n_0\ \forall 0\le j\le n:\quad
P_+(n,j)^2+P_-(n,j)^2
\ge S_+(n,j)+S_-(n,j).}
\tag{L-32704.36}
\]

## 8. What this closes in the live proof graph

`R-29002` gave the exact unpaired generalized-prime mutation

\[
(n,j)=(6,2):
\qquad
P_\omega^2-S_\omega
=\log3\log(25/32)<0.
\]

The present theorem explains how the parity pair repairs the failure:

1. pure dyadic forcing, including the odd-odd convolution, is absorbed by `L-32405`;
2. the current-scale part of every mixed odd-prime/dyadic destination is paid by the actual `2OE` cross term;
3. every remaining mixed component is a strict `4^{-r}` odd-prime descendant;
4. the descendant stack is cofinally lower order than the odd Kummer square.

Thus the **source-coupled parity-paired generalized Selberg–Kummer carry inequality is cofinally closed**.

This removes the mixed carry-row sign as an independent obstruction on PR #334. It does not by itself prove the physical independent-frequency recurrence: the finite analysis/synthesis map, reflected cross terms, strict-delay source tail, and principal neutral mode must still be assembled in one production energy ledger.

## 9. Proof boundary

Closed here, subject to independent review:

- exact four-adic product-carry decomposition;
- exact current-row mixed-boundary absorption;
- strict four-adic descendant normal form;
- cofinal source-matched parity-paired Selberg–Kummer inequality for all rows;
- exact all-endpoint closure of the first two child indices.

Still open:

- one source-complete physical two-frequency-to-carry recurrence using this cofinal row theorem;
- the neutral principal-mode delayed energy estimate;
- RH.
