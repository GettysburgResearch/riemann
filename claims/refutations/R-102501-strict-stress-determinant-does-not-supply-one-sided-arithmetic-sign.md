# R-102501 — A strict stress determinant does not supply the one-sided arithmetic sign

Claim ID: `R-102501`  
Status: **PROVED PROVES-TOO-MUCH FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102501--L-102502`  
RH status: **unproved**

The Heisenberg and CV/XD Gram determinants hold for every finite labelled
coefficient packet. They therefore cannot, by themselves, encode the Möbius
one-sided estimate.

Indeed, let `phi(u)=Phi_*(e^u)` and choose a translation `a>log 16`. For
`M>0` put

\[
F_M(u)=\phi(u)-M\phi(u-a).
\]

The two translates have disjoint support. Every identity in
`L-102501--L-102502` holds, with strict determinant whenever `F_M` is nonzero.
Nevertheless, on any subinterval where the second translate has the sign of
`phi` and the first is absent, the sign and negative mass of `F_M` can be made
arbitrarily large by increasing `M`.

Thus

\[
\boxed{
\text{strict local determinant}
\not\Longrightarrow
\text{subpower negative mass}.
}
\]

The determinant closes reserve accounting and channel compatibility. The
source-faithful arithmetic rows `AR-SCALE102500` and `AR-OCC102500` remain
indispensable.
