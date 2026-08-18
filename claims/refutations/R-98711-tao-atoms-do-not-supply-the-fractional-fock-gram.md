# R-98711 — The Tao atoms do not supply the fractional Fock cross-state Gram

Claim ID: `R-98711`  
Status: **REFUTATION OF A STATEMENT-TO-USE INTERFACE**  
Created: 2026-08-18  
Refutes: the cross-state and trace assertions used in `L-98703`, not `T-98300` itself  
RH status: **not assumed**

## 1. Fractional prime-square mismatch

For one odd prime `p`,

\[
(1-p^{-s})^\theta
=1-\theta p^{-s}-\frac{\theta(1-\theta)}2p^{-2s}-\cdots.
\]

Thus the fractional heat packet has the nonzero signed coefficient

\[
b_\theta(p^2)=-\frac{\theta(1-\theta)}2.
\tag{R-98711.1}
\]

The trace-free Tao atom at an integer `n` is proportional to `mu(n)`. At
`n=p^2` it is exactly zero. Consequently the atoms in `L-98701` cannot, without
an additional fractional decoration theorem, realize the signed `p^2` history
appearing in the Fock packet.

`L-98710` gives the correct repair: the `p^2` coefficient is one positive
Sibuya mark on the squarefree support `{p}`. This repair is not contained in
`L-98703`.

## 2. The local Tao labels are not a directed isometric system

At `x=2`, for the empty prime set,

\[
K_\varnothing(2)=
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

After adjoining `2`,

\[
K_{\{2\}}(2)=
\begin{pmatrix}3/4&1/2\\1/2&3/4\end{pmatrix}.
\]

The integer label `2` changes from a complementary-semigroup rank-one plus atom
to a semigroup diagonal atom. Moreover

\[
K_\varnothing(2)-K_{\{2\}}(2)
=\begin{pmatrix}1/4&1/2\\1/2&1/4\end{pmatrix}
\]

has eigenvalues `3/4` and `-1/4`. Therefore the atom decomposition by itself
does not define an isometric prime-adjoining embedding or even a PSD monotone
compression. The four scalar recurrences of `T-98300` determine local
marginals; they do not determine cross-state inner products.

## 3. The heat kernel used in L-98703 is not the energy kernel

The exact windowed energy uses the difference kernel in `L-98711.1`.
`L-98703` instead invokes a reflected total-log kernel with `(u+v)`. The latter
would belong to a different bilinear observable. Hence its stated Schur block
is not the left side it claims to estimate.

## 4. Trace consequence

A phase-independent positive completion which dominated the heat packet for
every center would also dominate its Bohr twists. `R-98710` proves that those
twists have energy rate `e^(T/2+o(T))`. Therefore no phase-independent common
diagonal can have logarithmic trace rate `96 theta T+o(T)` for every small
`theta`.

The Tao unit ports and positive Stieltjes source remain valid at their original
integer reciprocal-semigroup scope. What fails is their promotion to the
fractional, cross-state, heat-history Gram asserted in `L-98703`.
