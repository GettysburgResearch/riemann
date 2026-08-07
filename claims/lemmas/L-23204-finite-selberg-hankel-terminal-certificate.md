# L-23204 — Scalar Selberg–Hankel certificate adapter and packet-source firewall

Claim ID: `L-23204`  
Title: Positive exponential adjoints give a valid scalar terminal adapter only after an exact packet source map or coupled Selberg equation is supplied  
Status: **ABSTRACT SCALAR ADAPTER VERIFIED WITH FIXES; FROZEN PACKET APPLICATION GAP/BLOCKED**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Corrected: 2026-08-07 after review of frozen PR #233  
Issue: #232  
Dependencies: PR #229 `L-23001`; PR #216 `L-21503`  
Scope: optional analytic mechanism; not load bearing in corrected `T-23202`

## 1. Scalar centered Selberg identity

Let

\[
dP_0(y)=e^{y/2}\mathbf1_{y\ge0}\,dy,
\qquad
\mathscr L\nu=y\,d\nu+2dP_0*d\nu,
\]

and assume the exact scalar centered equation

\[
\boxed{
\mathscr L\nu+\nu*\nu=R.
}
\tag{L-23204.1}
\]

For `lambda>1/2`, define

\[
w_\lambda(s)
=
\mathbf1_{s\ge\lambda}
\left(\frac{\lambda-1/2}{s-1/2}\right)^2,
\qquad
f_\lambda(y)=\int_\lambda^\infty e^{-sy}w_\lambda(s)ds.
\]

The reviewed scalar identity gives

\[
\mathscr L^*f_\lambda=e^{-\lambda y},
\tag{L-23204.2}
\]

and

\[
f_\lambda(u+v)
=
\int_\lambda^\infty w_\lambda(s)e^{-su}e^{-sv}ds
\]

is a positive Hankel Gram.

For a finite positive mixture `F=sum a_ell f_(lambda_ell)`, pairing
(L-23204.1) gives

\[
\boxed{
\langle\nu*\nu,F\rangle
=
\langle R,F\rangle
-
\sum_\ell a_\ell
\int e^{-\lambda_\ell y}d\nu(y).
}
\tag{L-23204.3}
\]

This scalar statement is valid.

## 2. Conditional kernel adapter

Suppose one has a scalar energy

\[
E(J)=\iint K_J(u,v)d\nu(u)d\nu(v)
\]

formed from the **same** source `nu` appearing in (L-23204.1), together with

\[
K_J\preceq F(u+v)+K_J^{\rm low}.
\tag{L-23204.4}
\]

If directed bounds give

\[
\langle R,F\rangle-
\sum_\ell a_\ell H(\lambda_\ell)
\le A_J
\]

and

\[
\langle\nu\otimes\nu,K_J^{\rm low}\rangle\le L_J,
\]

then

\[
\boxed{E(J)\le A_J+L_J.}
\tag{L-23204.5}
\]

This is the verified abstract adapter.

## 3. Packet-source gap

The auxiliary energies of PR #158 use packet-specific signed sources

\[
\nu_{K,\tau,J},
\]

not automatically the single global centered prime measure `nu` satisfying
(L-23204.1).  The frozen proposal supplied neither

1. an exact map `nu_(K,tau,J)=A_(K,tau,J)nu` with all induced cross terms, nor
2. a well-typed coupled vector/matrix Selberg equation for the complete packet
   vector.

Consequently (L-23204.3) could not be applied to the terminal packet
self-energies as written.

The finite control

\[
h_1=v,
\qquad h_2=-v
\]

has aggregate source zero but sum of self-energies `2||v||^2`, demonstrating
why aggregate positivity alone is insufficient.

## 4. Corrected role

The terminal Type-I family is now closed directly by Euler cancellation in
`L-23205/L-23206`, so this source-map gap is removed from the load-bearing proof
spine.

The scalar adjoint may still contribute to a future proof of the balanced
Type-II theorem `BTP(K)`, but only after an explicit packet source map or coupled
Selberg equation is emitted and reviewed.

## 5. Type discipline for a future vector extension

A valid vector/matrix extension must specify separately:

```text
packet source Hilbert space
linear Selberg operator on the vector source
quadratic tensor/convolution channel
matrix-valued forcing
all packet cross terms
scalar test or matrix test pairing
Loewner order target
```

A vector-valued linear term may not be added directly to a matrix-valued
quadratic term without this typing.

## 6. Proof boundary

Retained:

- the scalar positive exponential adjoint;
- the scalar Selberg pairing;
- the conditional same-source kernel adapter.

Blocked at the frozen head:

- identification of terminal packet sources with the global Selberg source;
- a coupled packet equation;
- production `STC(K)` certificates.

Not claimed:

- a balanced Type-II estimate;
- RH.