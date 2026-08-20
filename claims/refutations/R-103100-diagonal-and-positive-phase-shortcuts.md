# R-103100 — Diagonal and unsigned phase shortcuts do not close the half-completed field

**Status:** PROVED METHOD FIREWALL.

1. The coefficient diagonal is already `N^o(1)` by `L-103101`; proving it again cannot address `HHFE102010`.

2. The exact kernel `R` changes sign. Replacing

\[
h_U(m)h_U(n)R(\log(m/n))
\]

by its absolute value destroys both the Möbius correlation and the negative outer portion of the Haar autocorrelation.

3. The Fourier identity

\[
R(v)=\frac1{2\pi}\int|\widehat\psi(\gamma)|^2e^{i\gamma v}\,d\gamma
\]

makes the *complete* energy positive, but it does not make every off-diagonal coefficient positive. A free-labelled or coefficient-diagonal phase square therefore does not prove `HCNC103100`.

4. Narrow-scale factorization is only a reduction. Taking `M` comparable to the physical integer scale would make the reconstruction mass power-sized. Valid use requires `M=X^{o(1)}` and still leaves a genuine signed `1+o(1)` near-collision estimate.
