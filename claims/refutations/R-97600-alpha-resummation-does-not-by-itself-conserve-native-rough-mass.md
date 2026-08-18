# R-97600 — The alpha-child parity resummation does not by itself conserve one native rough coefficient

Claim ID: `R-97600`  
Status: **PROVED EXACT INTERFACE OBSTRUCTION**  
Created: 2026-08-17  
Frozen predecessor: PR #566 at `2407b4ffe5024a2e3898922cf0b722d5cf69e496`  
RH status: **unproved**

Let a single rough prime `p>=67` be active and put `r=p^{-1/2}`.  A native
paired occurrence has even parent coefficient one and odd child coefficient
`r`; its signed observation is

\[
 P-rC.
\tag{R-97600.1}
\]

The causal weights used in the predecessor are

\[
 s=1-r,\qquad \lambda=r,\qquad \alpha=r\lambda=r^2.
\]

Represent the causal difference as the positive pair `(P,rC)`.  The current
part of the predecessor's unsigned identity is

\[
 s(P,0)+\lambda(P,rC)=(P,\alpha C).
\]

If the recursive `alpha` child is placed in the swapped channel, it contributes
another odd coefficient `alpha`.  The resulting odd coefficient is therefore

\[
2\alpha=2r^2,
\]

whereas the native coefficient is `r`.  The missing positive odd-history demand
is

\[
\boxed{\delta_p=r-2r^2=r(1-2r)>0.}
\tag{R-97600.2}
\]

For `p=67`, more than three quarters of the native rough coefficient lies in
this omitted compensation term.

Thus the abstract identity

\[
P=sP+\lambda(P-rC)+\alpha C
\]

is a correct unsigned packet identity, but it is not an atomwise conservation
identity for the parity-observed native source after the `alpha` child is
recursed.  Any valid completion must exhibit, own and transport the complete
`delta_p` compensation source, together with its target, row, score and
barycenter coordinates.  Calling it a reserve does not prove its existence or
its global Hall feasibility.

This refutes only the unstated conservation inference.  It does not refute the
possibility of a different completed-parity coupling.
