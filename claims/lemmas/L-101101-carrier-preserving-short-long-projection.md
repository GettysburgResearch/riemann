# L-101101 — The only valid short/long XD projection is the carrier-preserving sum channel

Claim ID: `L-101101`  
Status: **PROVED EXACT LINEAR-ALGEBRAIC AND ASYMPTOTIC THEOREM**  
Created: 2026-08-21  
Frozen input: PR #694 at `e6d923c1069f5a481abdf0769ca6d870a8b5ae4b`  
RH status: **not assumed**

PR #694 proves the exact source partition

\[
G_\mu=G_{\rm sh}+G_{\rm lo}
\]

and the asymptotics

\[
G_{\rm sh}(X)
=-P(X)+O\!\left({\sqrt X\over\log^2X}\right),
\]

\[
G_{\rm lo}(X)
=+P(X)+O\!\left({\sqrt X\over\log^2X}\right),
\]

where

\[
P(X)=\kappa_0{\sqrt X\over\log X},
\qquad
\kappa_0=8\log2(1-2^{-1/2})^2>0.
\]

Put

\[
v_X=\binom{G_{\rm sh}(X)}{G_{\rm lo}(X)},
\quad
e_+={1\over\sqrt2}\binom11,
\quad
e_-={1\over\sqrt2}\binom{-1}{1}.
\]

Then

\[
\boxed{
\langle v_X,e_+\rangle={G_\mu(X)\over\sqrt2},
}
\tag{L-101101.1}
\]

while

\[
\boxed{
\langle v_X,e_-\rangle
=\sqrt2P(X)+O\!\left({\sqrt X\over\log^2X}\right).
}
\tag{L-101101.2}
\]

The rank-one orthogonal projection

\[
\Pi_+=e_+e_+^*
={1\over2}\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]

annihilates the complete first-chaos carrier `(-P,+P)` and retains exactly the
physical minimal wavelet:

\[
\boxed{
\Pi_+v_X={G_\mu(X)\over2}\binom11.
}
\tag{L-101101.3}
\]

By contrast, any regional norm that dominates `|G_sh|` before applying
`Pi_+` pays

\[
\int_{2^L}^{2^{L+1}}|G_{\rm sh}(X)|^2{dX\over X}
\asymp {2^L\over L^2}.
\]

This is the exact failure of `SCME100704`.

## Meaning

The long sector is eventually positive, but its positive carrier is the
cancellation partner of the negative singleton-prime carrier. It cannot be
discarded before the two coordinates are projected onto `e_+`.

The corrected XD hybrid must therefore be a centered cross-covariance estimate
on the pair `(G_sh,G_lo)`. After exact projection, its scalar output is `G_mu`
itself. No separate short-sector absolute estimate remains.
