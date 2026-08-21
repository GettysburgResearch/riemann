# T-102110 — The fractional-Hankel near-collision estimate is an incoming edge to the joint Perron matrix

Claim ID: `T-102110`  
Status: **PROVED CONDITIONAL COMPOSITION; HCNC103100 OPEN**  
Created: 2026-08-21  
Depends on: `L-102106`; PR #702 `T-103100`; PR #697 Perron absorption  
RH status: **unproved**

PR #702 proves that `HCNC103100` is equivalent to subpower dyadic mass of the
half-completed Haar field energy `mathcal H_U`.  `L-102106` proves that the two
carrier-free balanced coordinates satisfy

\[
|B_A^\dagger(X)|+|B_Q^\dagger(X)|
\le C\mathcal H_U(X)
\]

with one absolute constant `C`.

Therefore

\[
\boxed{\mathrm{HCNC103100}
\Longrightarrow
N_A(Y)+N_Q(Y)=Y^{o(1)}.}
\tag{T-102110.1}
\]

In particular the Perron condition `CFBB102100` holds with zero matrix and a
subpower error term.  Hence

\[
\boxed{\mathrm{HCNC103100}
\Longrightarrow
\mathrm{CFBB102100}
\Longrightarrow RH.}
\tag{T-102110.2}
\]

This theorem does not prove `HCNC103100`.  It identifies the exact overlap
between the joint quadratic--wavelet implication matrix and the independently
obtained fractional-Hankel route: the latter supplies both arithmetic rows at
once after the common carrier-free filter.

The converse is not asserted.  A strict Perron matrix may close the two-channel
system even when the full unsigned Haar energy is not subpower, so
`CFBB102100` remains the potentially weaker target.
