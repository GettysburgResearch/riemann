# L-97200 — Parity-covariant atomwise owner ledger

Claim ID: `L-97200`  
Status: **PROVED EXACT INTERFACE CORRECTION, CONDITIONAL ONLY ON THE WRITTEN FINITE STOPPING TREE**  
Created: 2026-08-17  
Inputs: `L-97001.1`–`L-97001.6`; PR #561 `L-96501`

Let an original squarefree source atom have the unique factorization

\[
k=d\,p_1\cdots p_t,
\qquad d\mid P_{61},
\qquad 67\le p_1<\cdots<p_t,
\]

and let `h=(p_1,\ldots,p_t)` be its ordered rough history. Write
`S(E,O)=(O,E)` for the parity-channel swap. Let `\mathscr P_\ell` denote the
canonically oriented terminal packet whose small-prime colour already carries
`\mu(d)`.

For every terminal owner produced by the finite first-owner tree, the atomwise
identity compatible with the native source is

\[
\boxed{
\mathscr N_X
=
\bigoplus_{\ell\in\mathcal L_X}
\omega_\ell S^{|h_\ell|}\mathscr P_\ell,
\qquad \omega_\ell\ge0.
}
\tag{L-97200.1}
\]

Equivalently, every original occurrence retains all three native invariants

\[
\boxed{
\text{magnitude }k^{-1/2},\qquad
\text{activation }X/k,\qquad
\text{signed parity }\mu(d)(-1)^{|h|}=\mu(k).
}
\tag{L-97200.2}
\]

## Proof

Moving one rough prime `p\mid k` from the atom into the ordered history replaces
`(X,k)` by `(X/p,k/p)`. Hence

\[
\frac{X/p}{k/p}=\frac Xk,
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\]

Thus every row activation and coefficient magnitude is unchanged. In the paired
source category the same move exchanges the even and odd channels, so a history
of length `t` contributes `S^t` and signed factor `(-1)^t`. The small-prime
colour contributes `\mu(d)`, giving `\mu(d)(-1)^t=\mu(k)`.

Unique factorization fixes the ordered rough history. First-owner disjointness
and the decreasing rank in `L-97001.5` give one terminal owner whenever the
finite stopping tree of `L-97001.3`–`L-97001.6` is used. Therefore the corrected
atomwise statement is (L-97200.1), not the parity-blind equality implicit in
`L-97001.7`.

This lemma is an interface correction. It does not assert that every
`S^{|h|}\mathscr P_\ell` has nonnegative signed observation.
