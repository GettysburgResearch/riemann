# R-99820 — The `p^{-1/2}` operator on the normalized box potential is nonnative

Claim ID: `R-99820`  
Status: **EXACT STATEMENT-TO-USE REFUTATION**  
Created: 2026-08-20  
Reviewed object: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
RH status: **unproved**

PR #664 defines the normalized box potential `phi=W/sqrt(.)` but applies

\[
I-p^{-1/2}U_p.
\]

By `L-99820`, the native normalized source instead applies

\[
\boxed{I-p^{-1}U_p.}
\]

For one prime the discrepancy is exactly

\[
\left(p^{-1/2}-p^{-1}\right)\phi(y/p),
\tag{R-99820.1}
\]

which is nonzero whenever `y/p>1`. This is a source coefficient mismatch, not
a harmless scalar renormalization.

## Deep-mode mutation

On the deep formula

\[
\phi(y)=A-By^{-1/2},
\]

the operator used in PR #664 gives

\[
\phi(y)-p^{-1/2}\phi(y/p)=A(1-p^{-1/2}),
\]

so it annihilates the half-order mode. The native normalized operator gives

\[
\boxed{
\phi(y)-p^{-1}\phi(y/p)
 =A(1-p^{-1})-B(1-p^{-1/2})y^{-1/2},
}
\tag{R-99820.2}
\]

and the half-order mode survives.

For two primes the native deep block is

\[
\boxed{
A(1-p^{-1})(1-q^{-1})
-B(1-p^{-1/2})(1-q^{-1/2})y^{-1/2}.
}
\tag{R-99820.3}
\]

Therefore the half-order annihilation in `L-99813--L-99818` and the unweighted
Mertens-window coefficient in `L-99819` are properties of a nonnative operator
when read as statements about the normalized conclusion-facing box scalar.
They may not be composed into the PR #653/#659 Mellin–Landau chain.

The unnormalized `p^{-1/2}` identity remains correct when it is applied to
`W`, as in (L-99820.3). The error is applying that coefficient after replacing
`W` by `phi=W/sqrt(.)`.
