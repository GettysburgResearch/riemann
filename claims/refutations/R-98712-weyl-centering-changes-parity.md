# R-98712 — Weyl translation does not preserve the parity matrix coefficient

Claim ID: `R-98712`  
Status: **EXACT OPERATOR-IDENTITY FIREWALL**  
Created: 2026-08-18  
Refutes: the main-mode-renormalization sentence in `L-98703`  
RH status: **not assumed**

Let `W(f)` be the Weyl displacement on bosonic Fock space and let

\[
\mathsf P=(-1)^{\mathsf N}=\Gamma(-I)
\]

be parity. The canonical commutation relations give

\[
\mathsf P W(f)\mathsf P=W(-f).
\]

Therefore

\[
\boxed{
W(f)^*\mathsf P W(f)=W(-2f)\mathsf P,
}
\tag{R-98712.1}
\]

up to the standard harmless Weyl phase, which is one when the same vector `f`
is used on both sides. This equals `mathsf P` only for `f=0`.

Consequently a Weyl translation may remove a linear carrier from the state,
but it changes the trace-free parity observable into a displaced-parity
observable. The correction factor and every resulting cross term must be
retained. Unitarity of the translation alone does not preserve the matrix
coefficient used to define the fractional heat packet.

This is independent of the Bohr refutation. Even at one finite cutoff, the
main-mode removal in `L-98703` is not the asserted invariant operation.
