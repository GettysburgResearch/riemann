# L-23813 — Balanced-fragmentation Farkas theorem and randomized producer

Claim ID: `L-23813`  
Title: The exact carry-flow divergence has a balanced-superadditive dual and one descending randomized producer  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE PROOF**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810-carry-flow-divergence-and-mobius-inversion.md`  
Scope: finite convex algebra; no asymptotic sign theorem

## 1. Balanced fragmentation cone

Fix `0<eta<=1/2`. For every allowed split

\[
(n,j),\qquad \eta n\le j\le(1-\eta)n,
\]

put

\[
g_{n,j}=e_n-e_j-e_{n-j}.
\]

Let `R_X` be the exact critical node divergence from `L-23810`. A zero-slack
balanced carry packing exists exactly when

\[
\boxed{
R_X\in\operatorname{cone}\{g_{n,j}:(n,j)\in\mathcal B_\eta(X)\}.}
\tag{L-23813.1}
\]

This is the divergence form of exact BCT; no floor or carry coordinate remains
hidden in the statement.

## 2. Exact Farkas dual

Normalize `varphi_1=0`. Finite-dimensional Farkas duality gives the equivalence

\[
\boxed{
R_X\in\operatorname{cone}(g_{n,j})}
\tag{L-23813.2}
\]

if and only if

\[
\boxed{
\sum_{m=2}^{X}R_X(m)\varphi_m\ge0}
\tag{L-23813.3}
\]

for every balanced-superadditive sequence

\[
\boxed{
\varphi_n\ge\varphi_j+\varphi_{n-j}
\quad((n,j)\in\mathcal B_\eta(X)).}
\tag{L-23813.4}
\]

Indeed, the dual pairing with one generator is precisely

\[
\langle\varphi,g_{n,j}\rangle
=\varphi_n-\varphi_j-\varphi_{n-j}.
\]

Thus the primal BCT problem and the signed transport inequality of `L-23809`
are the same finite theorem in two coordinate systems.

## 3. Descending randomized producer

For every `n`, choose a probability distribution `pi_n` on the allowed children
`j`. Starting at `n=X` and descending, define

\[
\boxed{
d_X(n)=R_X(n)+
\sum_{m=n+1}^{X}d_X(m)
[\pi_m(n)+\pi_m(m-n)].}
\tag{L-23813.5}
\]

Put

\[
d_X(n,j)=d_X(n)\pi_n(j).
\tag{L-23813.6}
\]

The recurrence is exactly the node equation

\[
\partial d_X=R_X.
\tag{L-23813.7}
\]

Consequently `L-23810` gives, without approximation,

\[
\boxed{
\sum_{n,j}d_X(n,j)\chi_{n,j}(q)=w_X(q)
\quad(2\le q\le X).}
\tag{L-23813.8}
\]

Therefore

\[
\boxed{
d_X(n)\ge0\text{ for all }n
\Longrightarrow\text{zero-slack BCT at level }X.}
\tag{L-23813.9}
\]

This is a proof-producing interface: a fixed branching law converts the whole
balanced transport problem into one descending scalar sign ledger.

## 4. Relation to scalar Gamma carry

The scalar Gamma proposal averages the split coordinate before inversion and
therefore forces one log-translation-covariant convolution factor. Equations
(L-23813.5)--(L-23813.9) retain parent scale and both child scales. The compactness
argument `FGCM => GCF` does not identify a scalar limit for this producer.

This is a scope distinction only. Positivity of a chosen renewal remains an
RH-bearing theorem.

## 5. Proof boundary

Closed exactly:

- cone formulation of exact balanced saturation;
- balanced-superadditive Farkas dual;
- descending randomized producer;
- exact saturation conditional only on coefficient sign.

Open:

- a cofinal positive producer;
- BCT;
- RH.
