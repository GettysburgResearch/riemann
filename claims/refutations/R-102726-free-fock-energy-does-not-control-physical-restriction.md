# R-102726 — Free Fock energy does not control the physical logarithmic restriction

Claim ID: `R-102726`  
Status: **PROVED SOURCE-BLIND COUNTERMODEL**  
Created: 2026-08-23  
Depends on: `L-102743`  
RH status: **not assumed**

Let `phi` be a nonzero continuous compactly supported logarithmic kernel. For
integers

\[
 n_j=M+j,
 \qquad 1\le j\le N,
\]

put

\[
 F_{M,N}(u)=\sum_{j=1}^N\phi(u-\log n_j).
\]

Give the `N` labels independent phase coordinates. The free labelled energy is
exactly

\[
 \|F_{M,N}\|_{\rm free}^2
 =N\|\phi\|_2^2.
\]

Choose `N=o(M)` and let `M` tend to infinity. Then

\[
 \max_{i,j}|\log n_i-\log n_j|
 \le\log(1+N/M)\longrightarrow0.
\]

By continuity of translation in `L2`, every pairwise inner product tends to
`||phi||_2^2`. Hence

\[
 \boxed{
 \|F_{M,N}\|_{L^2(du)}^2
 =(1+o(1))N^2\|\phi\|_2^2.
 }
\]

The physical restriction can therefore amplify free energy by an arbitrarily
large factor `N`.

This countermodel does not match the completion-defect coefficients. Its role
is a firewall:

```text
polylog free labelled energy
+ subpower same-product multiplicity
```

cannot, by themselves, establish physical distinct-product occupancy. A proof
of `WNC102743` must use the literal prime-source coefficients, greatest-owner
geometry, carrier recombination, or an equivalent arithmetic restriction
theorem.