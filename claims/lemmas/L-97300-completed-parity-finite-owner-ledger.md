# L-97300 — Completed rough-history expansion is finite and parity-covariant

Claim ID: `L-97300`  
Status: **PROVED EXACT INTERFACE THEOREM**  
Created: 2026-08-17  
Frozen inputs: PR #561, PR #567, PR #568  
RH status: **unproved**

Let

\[
P_{61}=\prod_{p\le61}p.
\]

Every squarefree source index has a unique factorization

\[
k=d p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t.
\tag{L-97300.1}
\]

Write `h(k)=(p_1,...,p_t)`, let `S(E,O)=(O,E)` be the parity swap, and let
`P_l` be the canonically oriented terminal packet whose small-prime colour
contains `mu(d)`.  For the finite first-owner stopping tree, the native atomwise
ledger is

\[
\boxed{
\mathscr N_X
=\bigoplus_{\ell\in\mathcal L_X}
\omega_\ell S^{|h_\ell|}\mathscr P_\ell,
\qquad \omega_\ell\ge0.
}
\tag{L-97300.2}
\]

Every original occurrence retains

\[
\boxed{
\text{magnitude }k^{-1/2},\qquad
\text{activation }X/k,\qquad
\text{sign }\mu(d)(-1)^{|h|}=\mu(k).
}
\tag{L-97300.3}
\]

For a fixed endpoint `X` the ledger is finite: a source atom contains at most

\[
\left\lfloor\frac{\log X}{\log67}\right\rfloor
\]

rough factors, and the root source itself is finite.  Hence completed parity at
one endpoint requires no infinite projective limit.

Now let `G` be any finite-colour grouping map acting diagonally on parity space,

\[
\widetilde G(E,O)=(GE,GO),
\]

and let

\[
\mathcal O_\ell(E,O)=\ell(E)-\ell(O)
\]

be any signed row or scalar observation.  Then

\[
\boxed{
\mathcal O_\ell\widetilde G S^m
=(-1)^m\mathcal O_\ell\widetilde G.
}
\tag{L-97300.4}
\]

In particular, complete `P_61` colour grouping and the scalar

\[
\mathcal R=5\mathcal O_2+3\mathcal O_3
\]

both preserve the accumulated character `(-1)^m`.

## Proof

Moving a rough prime `p|k` into the history sends `(X,k)` to `(X/p,k/p)` and
contributes `p^{-1/2}`.  Therefore

\[
\frac{X/p}{k/p}=\frac Xk,
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\]

The same move exchanges the parity channels once.  Unique factorization and
first ownership give (L-97300.2)–(L-97300.3).  Diagonal grouping commutes with
`S`, while signed observation anti-commutes with one swap, proving
(L-97300.4).

This theorem repairs the owner ledger.  It does **not** make the swapped
terminal packet positive.
