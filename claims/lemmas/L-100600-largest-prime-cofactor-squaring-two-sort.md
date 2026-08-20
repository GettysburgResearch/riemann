# L-100600 — Largest-prime ownership and finite cofactor squaring form one exact two-sort source

Claim ID: `L-100600`
Status: **PROVED EXACT SOURCE IDENTITY; CLOSURE ESTIMATE OPEN**
RH status: **not assumed**

Let `K_0` be the ratio-eight ordinary-Möbius wavelet kernel of PR #674, and write every squarefree nonunit source integer uniquely as

\[
n=pm,\qquad p=P^+(n),\qquad P^+(m)<p.
\]

Then

\[
G_\mu(X)
=-\sum_p p^{-1/2}
  \sum_{\substack{X/(8p)\le m\le X/p\\P^+(m)<p}}
  \mu(m)m^{-1/2}K_0(X/(pm))
\]
for `X>8`.

Fix cutoffs `Y<Z`. Split the outer owner primes into `p<=Y` and `p>Y`, and on the rough part `p>Y` apply only to the cofactor coordinates the finite operator

\[
\mathscr C_Z^{(m)}=
\prod_{\substack{q\le Z\\q<p}}(I+q^{-1/2}S_q^{(m)}),
\]
where `S_q^(m)` acts by `m -> qm` and is zero when `qm` violates squarefreeness or `P^+(qm)<p`.

For each fixed owner `p`, the cofactor Möbius source is

\[
\prod_{q<p}(I-q^{-1/2}S_q^{(m)})\delta_1.
\]
Hence, by commutation of the squarefree cofactor shifts,

\[
\boxed{
\mathscr C_Z^{(m)}
\prod_{q<p}(I-q^{-1/2}S_q^{(m)})
=
\prod_{\substack{q\le Z\\q<p}}(I-q^{-1}S_{q^2}^{(m)})
\prod_{Z<q<p}(I-q^{-1/2}S_q^{(m)}).
}
\]

Thus finite cofactor squaring is source-faithful before physical summation:

- the terminal largest-prime owner `p` is untouched and remains unique;
- every cofactor prime `q<=Z` is replaced by one `q^2` label of activity `1/q`;
- every cofactor prime `Z<q<p` remains an ordinary label of activity `q^-1/2`;
- no source occurrence is duplicated;
- no inverse operator is used in this identity.

This is exactly the interface absent when finite Euler squaring is applied after scalar collapse.

## Consequence

For any positive kernel on the cofactor source satisfying the same one-label scaling inequality as in PR #677, the completed cofactor level mass obeys an adjacent-level estimate with owner budget

\[
\Sigma_{p,Z}
\le \sum_{q\le Z}q^{-2}+\sum_{Z<q<p}q^{-1}.
\]

Therefore whenever this budget is `<1`, each fixed-owner completed cofactor packet has positive parity sum by the same adjacent-level pairing.

## Boundary

The identity does **not** by itself return the unsquared physical wavelet. The remaining theorem `HCFB100600` must exploit the common largest-prime owner before collapse to transfer positivity/negative-mass control from these completed cofactors to the original rough bilinear sum without a signed inverse.
