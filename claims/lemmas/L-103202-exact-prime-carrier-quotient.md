# L-103202 — Exact prime-carrier quotient before regional norms

Claim ID: `L-103202`  
Status: **PROVED EXACT SOURCE RE-CENTERING**  
Created: 2026-08-20  
Depends on: `L-103200`  
RH status: **not assumed**

Let a source-faithful partition of the same wavelet be

\[
G_1=G_{\rm left}+G_{\rm right}.
\]

Define the literal prime packet

\[
P_1(X)=-\sum_p\frac1{\sqrt p}K_1(X/p).
\]

Set

\[
\widetilde G_{\rm left}=G_{\rm left}-P_1,
\qquad
\widetilde G_{\rm right}=G_{\rm right}+P_1.
\]

Then

\[
\boxed{
G_1=\widetilde G_{\rm left}+\widetilde G_{\rm right}
}
\]

exactly.  No asymptotic subtraction is used and no detector multiplier is
changed.

This is the mandatory first quotient for any short/long or diagonal/off-
diagonal norm.  It removes the explicit singleton-prime covariance from the
regional ledgers while retaining it in the total scalar.

The theorem does not assert that the two centered regional norms are subpower.
Composite prime-chaos carriers may remain, and any finite chaos subtraction
has to be performed by another exact source partition.  It only prevents the
known first-chaos carrier from being charged twice or destroyed by absolute
values.
