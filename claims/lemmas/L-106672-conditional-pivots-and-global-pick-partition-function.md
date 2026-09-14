# L-106672 — Conditional Pick pivots factor the global partition function

Claim ID: `L-106672`  
Status: **PROVED EXACT FINITE FACTORIZATION**  
Created: 2026-08-26  
Depends on: `L-106670--L-106671`; Schur complements  
RH status: **not assumed**

Retain a simple denominator kernel Gram `G` and put

\[
H_\tau=G-\tau V^*GV,
\qquad 0<\tau<1.
\]

For an arbitrary ordering of the `m` nodes, let `G_k,H_(tau,k)` denote the
leading `k x k` principal blocks, with determinant `1` at `k=0`.  Define the
conditional pivot ratio

\[
\boxed{
q_k(\tau)
=
{\det H_{\tau,k}\,\det G_{k-1}
 \over
 \det H_{\tau,k-1}\,\det G_k}.
}
\tag{L-106672.1}
\]

## 1. Exact product and pivot bounds

Telescoping gives

\[
\boxed{
\mathfrak Z_\tau
={\det H_\tau\over\det G}
=\prod_{k=1}^m q_k(\tau).
}
\tag{L-106672.2}
\]

The numerator-model Pick Gram `H=G-V^*GV` satisfies

\[
0\preceq H\preceq G,
\]

and

\[
H_\tau=(1-\tau)G+\tau H.
\]

A Schur-complement pivot is the minimum of the corresponding quadratic form
over all previous coordinates.  The Loewner sandwich

\[
(1-\tau)G\preceq H_\tau\preceq G
\]

therefore survives every conditional minimization and yields

\[
\boxed{
1-\tau\le q_k(\tau)\le1.
}
\tag{L-106672.3}
\]

Define the local scalar cost

\[
\ell_k(\tau)=-{1\over\tau}\log q_k(\tau).
\]

Then

\[
\boxed{
0\le\ell_k(\tau)\le{-\log(1-\tau)\over\tau},
\qquad
\mathfrak F_\tau=\sum_{k=1}^m\ell_k(\tau).
}
\tag{L-106672.4}
\]

The individual pivots depend on the node ordering, but their total does not.
This is an adaptive scalar recursion with the complete prior-node conditioning
already paid.

## 2. Global block product

For mesoscopic windows `I_j`, let `Z_(j,tau)` be their partition functions.
The block-diagonal global function is

\[
\boxed{
\mathscr Z_T(\tau)=\prod_j\mathfrak Z_{j,\tau},
\qquad
\mathscr F_T(\tau)
=-{1\over\tau}\log\mathscr Z_T(\tau)
=\sum_{j,k}\ell_{j,k}(\tau).
}
\tag{L-106672.5}
\]

Thus the entire shallow endpoint problem is one positive scalar determinant
ratio, or equivalently one sum of bounded conditional node costs.

## 3. Closed-cycle expansion

Writing

\[
M=G^{-1}V^*GV,
\]

which is similar to a positive contraction, gives

\[
\boxed{
-\log\mathfrak Z_\tau
=
\sum_{n=1}^{\infty}{\tau^n\over n}\operatorname{tr}(M^n).
}
\tag{L-106672.6}
\]

The `n=1` term is precisely the T-106650 value–nonnormality charge.  The
higher terms are finite cyclic source correlations, and their total relative
contribution is at most `c(tau)-1` by `L-106670`.

## 4. Scope

```text
one scalar conditional recursion                           PROVED
all pivot costs bounded uniformly                          PROVED
first cycle = exact T-106650 charge                         PROVED
Xi average of the conditional costs below 11/500 N         OPEN
```
