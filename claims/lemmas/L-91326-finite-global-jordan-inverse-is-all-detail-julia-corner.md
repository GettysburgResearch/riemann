# L-91326 — Finite global Jordan inversion is the all-detail corner of the prime Julia tensor product

Claim ID: `L-91326`  
Status: **EXACT FINITE-PRIME TENSOR/CHAOS IDENTITY; RENORMALIZED LIMIT OPEN**  
Created: 2026-08-12  
Depends on: `L-91325`  
RH status: **unproved**

## 1. Finite-prime inverse

For a finite prime set \(P\), define

\[
D_{\omega,P}(s)
=
\prod_{p\in P}D_{p,\omega}(s).
\tag{L-91326.1}
\]

By `L-91325`,

\[
\boxed{
D_{\omega,P}(s)
=
\left(\prod_{p\in P}\delta_{p,\omega}^{-1}\right)
\prod_{p\in P}
d_{p,\omega}^{\rm J}(z_p(s)).
}
\tag{L-91326.2}
\]

The product on the right is the transfer of the tensor output that selects the
detail port at every prime. Thus the finite signed inverse is literally the
all-detail corner of a positive tensor product of Julia nodes.

## 2. Coefficient recovery

Expanding each normalized detail,

\[
D_{p,\omega}(s)
=
1-\left(p^{2\omega}-1\right)
\sum_{k\ge1}p^{-k(s+\omega)},
\tag{L-91326.3}
\]

and multiplying over \(p\in P\) yields

\[
D_{\omega,P}(s)
=
\sum_{\substack{n\ge1\\p\mid n\Rightarrow p\in P}}
\frac{d_\omega(n)}{n^s},
\tag{L-91326.4}
\]

with

\[
d_\omega(n)
=
\prod_{p^k\parallel n}
-\left(p^{2\omega}-1\right)p^{-k\omega}.
\tag{L-91326.5}
\]

This is exactly the global Dirichlet inverse coefficient system of
`L-91311`.

## 3. Growing chaos order

The unnormalized all-detail corner has Hilbert norm at most one, but recovering
the scalar inverse removes the factor

\[
\prod_{p\in P}\delta_{p,\omega}.
\tag{L-91326.6}
\]

Since

\[
\delta_{p,\omega}\sim p^{-\omega},
\tag{L-91326.7}
\]

the inverse normalization grows like

\[
\exp\!\left(\omega\sum_{p\in P}\log p+o(\pi(P))\right).
\tag{L-91326.8}
\]

Thus global inversion leaves every fixed finite Poisson/Fock chaos sector. It
is an increasing-order, Wick-normalized detail corner.

## 4. Exact viable interpretation

The correct infinite object is not an ordinary vector in the naive prime Fock
space. It must be treated as a generalized Wick exponential/distribution whose
Green/theta image may nevertheless be a Hilbert vector.

This identifies the exact algebraic object that `GEJWO_omega` must
renormalize:

\[
\boxed{
:\!\prod_p
\delta_{p,\omega}^{-1}d_{p,\omega}^{\rm J}\!:
\quad\longmapsto\quad
f_\omega\oplus q_\omega.
}
\tag{L-91326.9}
\]

The colons denote the source-ordered renormalized limit, not an already
constructed object.

## 5. Scope

Closed:

```text
finite-prime inverse = all-detail Julia corner;
exact multiplicative coefficients;
unbounded chaos order and normalization.
```

Open:

```text
definition and closability of the infinite Wick inverse on the Green core;
theta/gamma counterterm;
Hilbert output norm identity;
RH.
```
