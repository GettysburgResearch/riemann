# L-23810 — Möbius divergence and balanced fragmentation equivalence

Claim ID: `L-23810`  
Title: Exact carry saturation is equivalent to routing one Möbius-derived node divergence through the balanced Pascal fragmentation cone  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE PROOF**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`, `L-23809`  
Scope: finite algebra and convex duality; no asymptotic sign theorem

## 1. Target and multiple-Möbius transform

Fix an integer `X>=2`. Let

\[
 w=(w(2),\ldots,w(X))
\]

be any real column target, and set `w(q)=0` for `q>X`. Define

\[
 \boxed{
 U_w(m)=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad 1\le m\le X,}
 \tag{L-23810.1}
\]

with `U_w(X+1)=0`, and its first difference

\[
 \boxed{
 R_w(m)=U_w(m)-U_w(m+1).}
 \tag{L-23810.2}
\]

Möbius inversion over multiples gives

\[
 \boxed{
 w(q)=\sum_{k\le X/q}U_w(qk).}
 \tag{L-23810.3}
\]

Summation by parts therefore yields

\[
 \boxed{
 w(q)=\sum_{m=1}^{X}R_w(m)
 \left\lfloor\frac mq\right\rfloor,
 \qquad 2\le q\le X.}
 \tag{L-23810.4}
\]

The node `m=1` is invisible in (L-23810.4).

For the critical carry target

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \tag{L-23810.5}
\]

(L-23810.1) is exactly the smoothed Möbius coordinate already isolated in
`L-23803`.

## 2. Split flows and divergence

For `2<=n<=X` and `1<=j<n`, let `d_(n,j)` be a finitely supported real split
flow. Its node divergence is

\[
 \boxed{
 (\partial d)_m
 =\sum_{j=1}^{m-1}d_{m,j}
 -\sum_{n>m}\bigl(d_{n,m}+d_{n,n-m}\bigr),}
 \tag{L-23810.6}
\]

where a central child is counted twice, exactly as it occurs in the split.
The carry load is

\[
 L_q(d)=\sum_{n=2}^{X}\sum_{j=1}^{n-1}
 d_{n,j}\chi_{n,j}(q).
 \tag{L-23810.7}
\]

The floor definition of `chi` gives the exact divergence identity

\[
 \boxed{
 L_q(d)=\sum_{m=1}^{X}(\partial d)_m
 \left\lfloor\frac mq\right\rfloor.}
 \tag{L-23810.8}
\]

This is the atomized version of the carry adjoint. It retains the complete split
coordinate and uses no averaging in `j/n`.

## 3. Exact saturation theorem

If

\[
 (\partial d)_m=R_w(m)
 \qquad(2\le m\le X),
 \tag{L-23810.9}
\]

then (L-23810.4) and (L-23810.8) imply

\[
 \boxed{L_q(d)=w(q)\qquad(2\le q\le X).}
 \tag{L-23810.10}
\]

Conversely, if (L-23810.10) holds, the strict triangularity of the floor matrix
on nodes `m>=2` gives (L-23810.9). Equivalently, apply the multiple-Möbius
transform to the load columns and then take first differences.

Thus exact carry saturation is not an opaque `X`-column system. It is exactly
one fragmentation problem:

\[
 \boxed{
 \partial d=R_w
 \quad\text{on nodes }2,\ldots,X.}
 \tag{L-23810.11}
\]

The divergence at node one is forced by conservation of total integer size and
is invisible to every carry column `q>=2`.

## 4. Balanced fragmentation cone

Fix `0<eta<=1/2` and retain only splits

\[
 \eta n\le j\le(1-\eta)n.
 \tag{L-23810.12}
\]

Let `G_(X,eta)` be the matrix whose column for `(n,j)` is

\[
 e_n-e_j-e_{n-j}.
 \tag{L-23810.13}
\]

Then a zero-slack balanced carry packing exists if and only if

\[
 \boxed{R_w\in G_{X,\eta}\,\mathbb R_{\ge0}^{\mathcal B_\eta(X)}.}
 \tag{L-23810.14}
\]

Farkas duality gives the exact alternative. Equation (L-23810.14) holds if and
only if

\[
 \boxed{
 \sum_{m=2}^{X}R_w(m)\varphi_m\ge0}
 \tag{L-23810.15}
\]

for every real sequence `varphi_1,...,varphi_X`, normalized by `varphi_1=0`,
that is balanced-superadditive:

\[
 \boxed{
 \varphi_n\ge\varphi_j+\varphi_{n-j}
 \quad((n,j)\in\mathcal B_\eta(X)).}
 \tag{L-23810.16}
\]

Under the floor transform

\[
 F_\varphi(n)=\sum_{q\le n}h_q\left\lfloor\frac nq\right\rfloor,
 \tag{L-23810.17}
\]

this is precisely the signed dual form of `L-23809.23`--`L-23809.24`.

## 5. Descending randomized producer

For each `n`, let `pi_n` be a probability distribution on the allowed balanced
children `j`. Define coefficients descending from `n=X` to `2` by

\[
 \boxed{
 d_n=R_w(n)+
 \sum_{m=n+1}^{X}d_m
 \bigl[\pi_m(n)+\pi_m(m-n)\bigr].}
 \tag{L-23810.18}
\]

Put

\[
 d_{n,j}=d_n\pi_n(j).
 \tag{L-23810.19}
\]

Then (L-23810.18) is exactly the node equation

\[
 \partial d=R_w.
 \]

Consequently:

\[
 \boxed{
 d_n\ge0\text{ for every }n
 \quad\Longrightarrow\quad
 L_q(d)=w(q)\text{ for every }q.}
 \tag{L-23810.20}
\]

This supplies a proof-producing route: choose one explicit balanced branching
law and prove positivity of its descending renewal coefficients.

## 6. Relation to the scalar Gamma obstruction

The scalar Gamma-carry proposal averaged the split coordinate before inversion.
That forced one log-translation-covariant convolution factor and the compactness
argument `FGCM => GCF`.

Equations (L-23810.18)--(L-23810.20) retain the parent size, both child sizes,
and a scale-dependent branching law. No scalar convolution limit is forced.
This is the exact mathematical distinction between the atomized transport route
and scalar GCF.

## 7. Proof boundary

Closed exactly:

- the multiple-Möbius target divergence;
- carry load equals floor pairing with divergence;
- exact saturation is equivalent to one balanced fragmentation flow;
- the Farkas dual;
- the descending randomized producer.

Open:

- positivity of any cofinal explicit producer for the critical target;
- BCT;
- RH.
