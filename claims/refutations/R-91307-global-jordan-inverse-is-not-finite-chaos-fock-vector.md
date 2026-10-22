# R-91307 — The global Jordan inverse is not a finite-chaos or naive Fock vector

Claim ID: `R-91307`  
Status: **EXACT METHOD FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91325/L-91326`

The signed all-prime Dirichlet inverse is the normalized all-detail corner of
the local Julia tensor product. For a cutoff \(P\), the required normalization
is

\[
\prod_{p\le P}\delta_{p,\omega}^{-1},
\qquad
\delta_{p,\omega}\sim p^{-\omega}.
\]

It diverges superpolynomially with the prime cutoff, while the selected chaos
order grows like \(\pi(P)\).

Therefore a proof may not:

- place the complete inverse in any fixed finite chaos sector;
- treat it as an ordinary vector in the safe prime Fock vacuum;
- bound it by the product of local detail norms;
- pass to the all-prime limit before the Green/theta renormalization;
- call the formal Wick product a constructed Hilbert vector.

The correct target is the renormalized cyclic distribution-to-Hilbert map in
`T-91306`.
