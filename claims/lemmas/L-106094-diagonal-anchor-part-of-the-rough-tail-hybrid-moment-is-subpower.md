# L-106094 — The diagonal anchor part of the rough-tail hybrid moment is subpower

Claim ID: `L-106094`  
Programme aliases: `LFAM1.ANCHOR_DIAGONAL_PAYMENT`, `LFAM2.ROUGH_TAIL_HYBRID_DIAGONAL`, `STRESS.LEAST_PRIME_SOURCE_ENERGY`  
Status: **PROVED UNCONDITIONAL SUBPOWER DIAGONAL THEOREM**  
Created: 2026-08-25  
Depends on: `L-106092--L-106093`; parent `L-102952`, `L-102955`, `L-102962`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Expand the squares in the moment \(\mathfrak M_{\rm LDRT}\) of
`L-106093.9` with respect to the left-anchor index \(\alpha\).  This lemma
controls the terms with the same anchor on both sides.

After equal-product and Boolean-representation aggregation, one anchor has
physical coefficient

\[
a_\alpha
=
\frac{\gamma_\alpha}{g\,c\sqrt P},
\qquad
|\gamma_\alpha|\le X^{o(1)},
\tag{L-106094.1}
\]

where

\[
\ell=P^-(c),\qquad \ell\le c.
\tag{L-106094.2}
\]

The canonical equal-pair share has modulus at most one and its total labelled
square energy is no larger than the concentrated-owner energy.

For fixed \(g,\ell,Q,\sigma,\alpha\), `L-106092` gives

\[
\sum_{h=1}^{\ell-1}
\|B_{\alpha;g,Q,\sigma,h}\|^2
\ll
\frac{X^{o(1)}}{g^2Q}.
\tag{L-106094.3}
\]

Multiplying the diagonal term by the natural moment weight \(g^2\ell Q\)
therefore gives

\[
g^2\ell Q\,|a_\alpha|^2
\sum_{h=1}^{\ell-1}
\|B_{\alpha;g,Q,\sigma,h}\|^2
\ll
X^{o(1)}
\frac{\ell}{g^2c^2P}.
\tag{L-106094.4}
\]

Using \(\ell\le c\),

\[
\frac{\ell}{g^2c^2P}
\le
\frac1{g^2cP}.
\tag{L-106094.5}
\]

On one finite horizon,

\[
\sum_g{1\over g^2}<\infty,
\qquad
\sum_{c\le X}{1\over c}\ll\log X,
\qquad
\sum_{P=pq\le X}{1\over P}
\le
\left(\sum_{p\le X}{1\over p}\right)^2
\ll(\log\log X)^2.
\tag{L-106094.6}
\]

All squarefree, coprimality, shell and activity restrictions only decrease
these majorants.  The universal Boolean coefficient and all finite
representation multiplicities contribute \(X^{o(1)}\).

Consequently the complete same-anchor part of the hybrid moment satisfies

\[
\boxed{
\mathfrak M_{\rm LDRT}^{\rm anchor\ diagonal}(Y)
=
Y^{o(1)}.
}
\tag{L-106094.7}
\]

## Exact remaining part

Only pairs of distinct anchors remain:

\[
\boxed{
\alpha\ne\alpha'.
}
\tag{L-106094.8}
\]

Thus the open hybrid theorem is no longer a diagonal, local family-size or
conductor-payment problem.  It is the coherent cross-anchor correlation of
the principal and nonprincipal rough-tail L-channels.

## Scope

The theorem does not take absolute values before the fixed-fibre phase
energy, and it does not identify distinct anchors orthogonally.  It closes
only the literal diagonal in the exact amplified moment.  The cross-anchor
moment is isolated in `T-106090`.
