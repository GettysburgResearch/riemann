# L-23707 — Digital-freeze renormalization and first descent

Claim ID: `L-23707`  
Title: A saturated carry column exposes an exact smaller carry matrix on its surviving residue corridor, and the first logarithmic-target deviation descends below one fifth scale  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23701`, `L-23704`, `L-23706`; PR #246 `L-23703` for outer four-band positivity  
Scope: exact finite carry geometry and one source-specific first-deviation theorem; no Greedy Slack estimate is asserted

## 1. Carry matrix

For integers `2<=q<=n`, retain

\[
\beta_{nq}
=\frac{\lfloor n/q\rfloor\bigl(q-1-(n\bmod q)\bigr)}{n+1}.
\tag{L-23707.1}
\]

Let `d_X` be the backward minimum-ratio greedy vector for the logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q).
\tag{L-23707.2}
\]

The exact digital-freeze law of `L-23706` says that if a positive row `N`
is blocked by `q<N`, then every later positive row `m` with

\[
q\le m<N
\]

must satisfy

\[
m\equiv-1\pmod q.
\tag{L-23707.3}
\]

## 2. Exact frozen-corridor renormalization

Let `L>=2` and integers `k>=e>=2`. Put

\[
n=L(k+1)-1,
\qquad
q=Le.
\]

Write

\[
k=ae+r,
\qquad0\le r<e.
\]

Then

\[
\left\lfloor\frac{L(k+1)-1}{Le}\right\rfloor=a,
\]

and the remainder modulo `Le` is

\[
L(r+1)-1.
\]

Therefore

\[
\begin{aligned}
\beta_{L(k+1)-1,Le}
&=\frac{a\,[Le-1-(L(r+1)-1)]}{L(k+1)}\\
&=\frac{a(e-1-r)}{k+1}\\
&=\beta_{k,e}.
\end{aligned}
\]

Hence

\[
\boxed{
\beta_{L(k+1)-1,Le}=\beta_{k,e}.}
\tag{L-23707.4}
\]

This is an exact identity, including every floor and endpoint convention.

### Corridor embedding

For a finite vector `a(k)` define

\[
(\mathcal R_La)(n)
=\begin{cases}
L^{-1/2}a(k),&n=L(k+1)-1,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-23707.5}
\]

Let

\[
Y=\left\lfloor\frac{X+1}{L}\right\rfloor-1.
\]

Then for every integer `2<=e<=Y`, equation (L-23707.4) gives

\[
\boxed{
\sum_{n=Le}^{X}(\mathcal R_La)(n)\beta_{n,Le}
=L^{-1/2}
\sum_{k=e}^{Y}a(k)\beta_{k,e}.}
\tag{L-23707.6}
\]

The target has the matching exact scale law

\[
\boxed{
w_X(Le)=L^{-1/2}w_{X/L}(e).}
\tag{L-23707.7}
\]

Thus the multiple-`L` columns of one frozen corridor are literally a scaled
copy of the original carry problem at endpoint `X/L`. No asymptotic continuum
pass is involved.

The first moment of the embedded vector is

\[
\boxed{
\sum_n n(\mathcal R_La)(n)
=\sqrt L\sum_k k a(k)
+(\sqrt L-L^{-1/2})\sum_k a(k).}
\tag{L-23707.8}
\]

Consequently a sharp `8 sqrt(X/L)` smaller-endpoint mass is transported to a
sharp `8 sqrt(X)` mass, up to the already lower-order coefficient sum.

## 3. Simultaneous blocker sparsity inside one active corridor

Suppose positive off-diagonal blockers

\[
q_1,\ldots,q_r
\]

are simultaneously active, meaning that the current row index `m` is at least
every `q_i`. Put

\[
L_r=\operatorname{lcm}(q_1,\ldots,q_r).
\]

Repeated application of the digital-freeze law gives

\[
\boxed{m\equiv-1\pmod{L_r}}
\tag{L-23707.9}
\]

for every current positive row.

If a new positive off-diagonal blocker `q_(r+1)` divided `L_r`, then
(L-23707.9) would imply

\[
m\equiv-1\pmod{q_{r+1}},
\]

and hence

\[
\beta_{m,q_{r+1}}=0,
\]

contradicting its use as a blocker. Therefore

\[
q_{r+1}\nmid L_r.
\]

Since

\[
\frac{\operatorname{lcm}(L_r,q_{r+1})}{L_r}
=\frac{q_{r+1}}{(q_{r+1},L_r)}
\]

is an integer larger than one,

\[
\boxed{L_{r+1}\ge2L_r.}
\tag{L-23707.10}
\]

As long as all blockers remain active, `L_r<=m+1<=X+1`; hence

\[
\boxed{r\le\lfloor\log_2(X+1)\rfloor.}
\tag{L-23707.11}
\]

This does not bound the total number of blocker phases after old columns fall
below the active row. It proves logarithmic sparsity within every simultaneous
frozen corridor.

## 4. Source-specific first-descent theorem

Let `c_X(n)` be the exact triangular inverse of the logarithmic target. PR #246
`L-23703` proves the unconditional outer theorem

\[
\boxed{c_X(n)\ge0\qquad(5n>X).}
\tag{L-23707.12}
\]

Consider the first row `N` at which the greedy algorithm chooses a positive
off-diagonal blocker. Before row `N`, greedy and exact backward elimination
coincide. Therefore at stage `N`,

\[
\rho_X^{(N)}(q)
=\sum_{m=q}^{N}c_X(m)\beta_{mq}.
\tag{L-23707.13}
\]

The diagonal ratio is

\[
\frac{\rho_X^{(N)}(N)}{\beta_{NN}}=c_X(N).
\tag{L-23707.14}
\]

Assume `N>X/5` and let `q>X/5` with `q<N` and `beta_(Nq)>0`. Every index
`m>=q` then satisfies `5m>X`, so (L-23707.12) gives `c_X(m)>=0`. Hence

\[
\frac{\rho_X^{(N)}(q)}{\beta_{Nq}}
=c_X(N)
+\frac{\sum_{m=q}^{N-1}c_X(m)\beta_{mq}}{\beta_{Nq}}
\ge c_X(N).
\tag{L-23707.15}
\]

Such a column cannot beat the diagonal. Therefore the first positive
off-diagonal event satisfies the dichotomy

\[
\boxed{
N\le X/5
\quad\text{or}\quad
q\le X/5.}
\tag{L-23707.16}
\]

In particular, the first genuine failure of exact Carry Saturation cannot create
an independent same-scale obstruction: it is sourced from the lower fifth of
the endpoint.

## 5. Consequence for a recurrence proof

Equations (L-23707.4)--(L-23707.16) give the exact geometry required by a true
scale recurrence:

1. the first nontrivial source enters below `X/5`;
2. while its blocking column is active, every positive row lies on a frozen
   residue corridor;
3. the multiple-column core on that corridor is an exact smaller carry matrix;
4. simultaneous additional blockers are logarithmically sparse and force
   further modulus growth;
5. only the nonmultiple cross-residue boundary ledger is not yet assigned to a
   smaller copy.

The last item is the precise role of the signed Green correction and the
source-specific two-frequency reflected square. It is not closed by this lemma.

## 6. Proof boundary

Closed exactly:

- frozen-corridor self-similarity;
- target and first-moment scale laws;
- least-common-multiple growth of simultaneous blockers;
- the first-deviation descent below one fifth scale, conditional only on the
  independently stated outer theorem.

Open:

- a polylogarithmic bound for the cross-residue boundary charge;
- the resulting slack recurrence;
- Greedy Slack/DCRS;
- RH.
