# L-26205 — Atomized carry packing is an exact balanced fragmentation problem

Claim ID: `L-26205`  
Title: Möbius inversion determines one signed node divergence, Pascal split flows are exactly its nonnegative fragmentation realizations, and Farkas duality gives the complete finite review criterion  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: atomized carry identity `L-23808`; elementary Möbius inversion and Farkas' lemma  
Scope: arbitrary finite target; no RH assumption

## 1. Atomized split matrix

For `0<eta<1/2`, let

\[
\mathcal B_\eta(X)
=\{(n,j):2\le n\le X,\ \eta n\le j\le(1-\eta)n\}.
\]

For every integer base `q>=2`, put

\[
\chi_{n,j}(q)
=\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}{q}\right\rfloor
\in\{0,1\}.
\tag{L-26205.1}
\]

Let `d_(n,j)>=0` be a finite split flow and define its column load

\[
L_q(d)=\sum_{(n,j)\in\mathcal B_\eta(X)}d_{n,j}\chi_{n,j}(q).
\tag{L-26205.2}
\]

## 2. Node divergence

Define

\[
\boxed{
r_m(d)
=\sum_{j}d_{m,j}
 -\sum_{n>m}\bigl(d_{n,m}+d_{n,n-m}\bigr),}
\tag{L-26205.3}
\]

where a central child is counted twice. Expanding the three floors gives

\[
\boxed{
L_q(d)=\sum_{m=1}^{X}r_m(d)\left\lfloor\frac mq\right\rfloor.}
\tag{L-26205.4}
\]

Every split conserves integer size, so

\[
\boxed{
\sum_{m=1}^{X}m r_m(d)=0.}
\tag{L-26205.5}
\]

Pascal four-cycles lie in the kernel of the divergence and therefore preserve
all carry columns and the complete binomial objective.

## 3. Unique divergence forced by a target

Let `w(2),...,w(X)` be any target and define its multiples-Möbius transform

\[
\boxed{
u_m=\sum_{k\le X/m}\mu(k)w(mk),
\qquad2\le m\le X,}
\tag{L-26205.6}
\]

with `u_(X+1)=0`. Set

\[
\boxed{
r_m^w=u_m-u_{m+1}\quad(2\le m\le X),}
\tag{L-26205.7}
\]

and choose

\[
\boxed{
r_1^w=-\sum_{m=2}^{X}m r_m^w.}
\tag{L-26205.8}
\]

Then a split flow satisfies

\[
L_q(d)=w(q)\qquad(2\le q\le X)
\tag{L-26205.9}
\]

if and only if

\[
r(d)=r^w.
\tag{L-26205.10}
\]

### Proof

Let `R_m=sum_(ell>=m) r_ell`. From (L-26205.4),

\[
L_q(d)=\sum_{k\le X/q}R_{kq}.
\]

Möbius inversion over multiples gives

\[
R_m=\sum_{k\le X/m}\mu(k)L_{mk}(d).
\]

Thus exact target loads force `R_m=u_m`, hence (L-26205.7). The converse is the
same calculation in reverse. The coordinate `r_1` does not enter any `q>=2`
column and (L-26205.8) is exactly the size-conservation completion.

## 4. Complete finite dual criterion

Let `B_eta` be the node-divergence matrix whose `(n,j)` column is

\[
e_n-e_j-e_{n-j}.
\]

By finite-dimensional Farkas duality, a nonnegative balanced split flow with
exact target loads exists if and only if

\[
\boxed{
\sum_{m=1}^{X}r_m^w F(m)\ge0}
\tag{L-26205.11}
\]

for every real potential `F(1),...,F(X)` satisfying

\[
\boxed{
F(n)\ge F(j)+F(n-j)
\qquad((n,j)\in\mathcal B_\eta(X)).}
\tag{L-26205.12}
\]

Thus the closing theorem is a source-specific balanced-fragmentation statement,
not a Hankel kernel assertion or a face-count estimate.

## 5. RH target and outer source sign

For

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

write `Y=X/m`. Then

\[
u_m=X^{-1/2}\,U(Y),
\qquad
U(Y)=\sqrt Y\sum_{k\le Y}\frac{\mu(k)}{\sqrt k}\log(Y/k).
\tag{L-26205.13}
\]

On `1<=Y<5`, only `mu(1),...,mu(4)` occur. Direct differentiation on the four
quotient intervals gives

\[
U'(Y)>0.
\tag{L-26205.14}
\]

For the only decreasing derivative branch, `3<=Y<5`, the minimum occurs at
`Y=5` and the bracket is greater than `0.048`. Consequently

\[
\boxed{
r_m^{w_X}\ge0\qquad(5m>X).}
\tag{L-26205.15}
\]

This recovers the rigorous outer carry region in divergence form. No sign is
asserted for the inner divergence.

## 6. Fragmentation theorem (`MFT`)

The proposed arithmetic closing statement is:

> For one fixed `eta>0` and every sufficiently large `X`, the divergence
> `r^(w_X)` satisfies the dual inequalities (L-26205.11), equivalently it has a
> nonnegative `eta`-balanced split-flow realization.

Call this **Möbius Fragmentation Transport (`MFT`)**.

`MFT` is strictly source specific. It retains every Möbius sign through `u_m`,
and the exact `2/3` or dyadic Mertens shell remains a scalar projection of the
same divergence.

## 7. Proof boundary

Closed exactly:

- carry load equals floor pairing with node divergence;
- target loads determine one unique divergence;
- Pascal cycles preserve it;
- Farkas gives a necessary-and-sufficient finite theorem;
- the complete outer source lies on the positive side.

Open:

- the inner dual inequalities / `MFT`;
- a symbolic or cofinal proof-producing realization;
- RH.
