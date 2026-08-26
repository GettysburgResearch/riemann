# R-106060 — One nonzero linear phase does not control a collision line

Claim ID: `R-106060`  
Status: **PROVED EXACT DIMENSION-LOSS FIREWALL**  
Created: 2026-08-24  
Depends on: finite additive orthogonality  
Programme issues: #743, #736, #737  
RH status: **unproved**

Let `k=F_Q`, let `H` be a Hilbert space, and let `(w_x)_(x in k^*)` be a
finite packet. Put

\[
S=\sum_{x\in k^*}w_x,
\qquad
D=\sum_{x\in k^*}\|w_x\|^2.
\]

For a nontrivial additive character `psi` and `tau!=0`, define

\[
F_\alpha
=\sum_{x\in k^*}w_x\psi(\tau\alpha x),
\qquad \alpha\in k^*.
\]

Additive orthogonality gives

\[
\boxed{
\sum_{\alpha\ne0}\|F_\alpha\|^2
=QD-\|S\|^2.
}
\tag{R-106060.1}
\]

The coherent nonzero-phase sum is

\[
\sum_{\alpha\ne0}F_\alpha=-S.
\]

If every `w_x` equals the same nonzero vector, then

\[
\frac{\|S\|^2}{\sum_{\alpha\ne0}\|F_\alpha\|^2}
=Q-1.
\tag{R-106060.2}
\]

Thus one linear phase direction can cost the complete field dimension. It
cannot provide a source-independent contraction of the coherent collision-line
sum.

The two-phase theorem `L-106060` changes the operator and gives a sharp factor
of order `1/Q`. A proof may not quote that gain after retaining only one of the
two source-exact phase variables.

This is a mechanism firewall and proves no RH result.
