# L-23802 — Carry packing/covering duality and the canonical greedy producer

Claim ID: `L-23802`  
Title: The prime ramp admits finite nonnegative packing and covering programs, and a fail-closed descending greedy packing exists at every endpoint  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`  
Scope: finite convex algebra; no sharp asymptotic estimate

## 1. Finite carry programs

Let `B_X` be the lower-triangular matrix

\[
(B_X)_{nq}=\beta_{nq},
\qquad 2\le q,n\le X,
\]

with rows indexed by `n` and columns by `q`. Let

\[
g_X=(G_2,\ldots,G_X)^T,
\qquad
w_X=(w_X(2),\ldots,w_X(X))^T.
\]

Define the nonnegative packing value

\[
\boxed{
\mathfrak L(X)
=\max\{g_X^Td:d\ge0,\ B_X^Td\le w_X\}}
\tag{L-23802.1}
\]

and the nonnegative covering value

\[
\boxed{
\mathfrak U(X)
=\min\{g_X^Te:e\ge0,\ B_X^Te\ge w_X\}.}
\tag{L-23802.2}
\]

Because `B_X` has a strictly positive diagonal, both feasible sets are nonempty
and the optima are attained.

By `L-23801`,

\[
\boxed{
\mathfrak L(X)\le\mathcal P(X)\le\mathfrak U(X).}
\tag{L-23802.3}
\]

The exact triangular inverse is not required to be nonnegative for this
sandwich.

## 2. Linear-programming duals

Finite LP duality gives

\[
\boxed{
\mathfrak L(X)
=\min\{w_X^Ty:y\ge0,\ B_Xy\ge g_X\}}
\tag{L-23802.4}
\]

and

\[
\boxed{
\mathfrak U(X)
=\max\{w_X^Tz:z\ge0,\ B_Xz\le g_X\}.}
\tag{L-23802.5}
\]

The von Mangoldt vector

\[
y_q=\begin{cases}
\Lambda(q),&q=p^a,\\
0,&\text{otherwise}
\end{cases}
\]

satisfies `B_X y=g_X` by `L-23801`. Hence it is simultaneously feasible for
both dual programs, and

\[
\mathfrak L(X)\le\mathcal P(X)\le\mathfrak U(X)
\]

is sharp at the source vector.

The proof problem is not LP existence. It is to construct source-independent
nonnegative primal certificates whose entropy values nearly meet the common
archimedean barrier.

## 3. Canonical descending greedy packing

Initialize residuals

\[
\rho_X^{(X)}(q)=w_X(q),
\qquad2\le q\le X.
\]

For `n=X,X-1,...,2`, define

\[
\boxed{
 d_X^{\rm gr}(n)
 =\min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 {\rho_X^{(n)}(q)\over\beta_{nq}},}
\tag{L-23802.6}
\]

and update

\[
\rho_X^{(n-1)}(q)
=\rho_X^{(n)}(q)
 -d_X^{\rm gr}(n)\beta_{nq}
\qquad(q\le n),
\tag{L-23802.7}
\]

leaving the already terminal columns unchanged.

Inductively, every residual is nonnegative. Therefore

\[
\boxed{
 d_X^{\rm gr}\ge0,
 \qquad
 B_X^Td_X^{\rm gr}\le w_X.}
\tag{L-23802.8}
\]

This produces a canonical nonnegative carry packing for every finite `X`, with
no unproved sign assertion.

At least one active column is saturated at every nonzero step. If the minimum
in (L-23802.6) is always attained at `q=n`, the greedy vector is exactly the
ordinary triangular inverse and Carry Saturation holds. The full proposal does
not assume this stronger statement.

## 4. Canonical covering

Let `c_X` be the unique real triangular inverse

\[
B_X^Tc_X=w_X.
\tag{L-23802.9}
\]

Write `c_X=c_X^+-c_X^-` coordinatewise. Since `B_X>=0`,

\[
\boxed{
B_X^Tc_X^+
=w_X+B_X^Tc_X^-
\ge w_X.}
\tag{L-23802.10}
\]

Thus

\[
\boxed{e_X^{\rm can}=c_X^+}
\tag{L-23802.11}
\]

is an unconditional nonnegative cover. The only question is its weighted mass.

This exposes a strictly weaker target than pointwise Carry Saturation:

\[
\boxed{
\sum_{n\le X}n(c_X(n))_-=X^{o(1)}.}
\tag{L-23802.12}
\]

A subpolynomial weighted negative part makes the canonical cover asymptotically
as sharp as the signed inverse, even if isolated coefficients are negative.

## 5. Two proposed sharp forms

The **carry sandwich theorem** may be established in either of two ways.

### Packing/covering form

Construct `d_X,e_X>=0` such that

\[
B_X^Td_X\le w_X\le B_X^Te_X,
\tag{L-23802.13}
\]

and

\[
\sum_n d_X(n)G_n
\ge4\sqrt X-X^{o(1)},
\qquad
\sum_n e_X(n)G_n
\le4\sqrt X+X^{o(1)}.
\tag{L-23802.14}
\]

### Negative-mass form

Prove the sharp signed-mass ledger for the exact inverse and
(L-23802.12). The entropy upper bound `G_n<=n/2` then controls the cover; the
entropy lower ledger controls a packing or the exact inverse from the other
side.

The packing/covering form is logically weaker than requiring `c_X(n)>=0` for
every `n`.

## 6. Proof boundary

Closed exactly:

- finite primal and dual programs;
- the prime-ramp sandwich;
- an unconditional greedy packing;
- an unconditional canonical cover;
- reduction of exact saturation to weighted negative mass.

Open:

- the sharp carry sandwich theorem;
- a subpolynomial negative-mass bound;
- RH.