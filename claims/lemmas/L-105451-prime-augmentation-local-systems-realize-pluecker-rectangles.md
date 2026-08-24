# L-105451 — Prime augmentation local systems realize the clean Plücker trace

Claim ID: `L-105451`

Status: **PROVED EXACT CHARACTER/HODGE LOCAL-SYSTEM THEOREM**

Work in the clean four-owner largest-two sector

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

with four distinct owner primes and no owner/core incidence. The source
occurrence is already carrier- and homotopy-recombined.

Choose one owner from each physical side, say `p` from `N` and `r` from `M`.
After extracting every common core power as in `L-102860`, write the reduced
products as

\[
\widetilde N,\qquad \widetilde M.
\]

Then

\[
p\mid\widetilde N,\quad p\nmid\widetilde M,
\qquad
r\mid\widetilde M,\quad r\nmid\widetilde N.
\tag{L-105451.1}
\]

## Augmentation representations

For a prime `ell`, let

\[
\mathcal A_\ell
=
\left\{
(z_h)_{h\in\mathbf F_\ell}:
\sum_hz_h=0
\right\}
\]

be the augmentation representation of the Frobenius residue group. For
\(a\in\mathbf F_\ell\), use the nontrivial-character vector

\[
\chi_{\ell,a}
=
\left(e_\ell(ha)\right)_{1\le h<\ell}.
\]

Its Gram matrix is

\[
\boxed{
\langle\chi_{\ell,a},\chi_{\ell,b}\rangle
=
\begin{cases}
\ell-1,&a=b,\\
-1,&a\ne b.
\end{cases}
}
\tag{L-105451.2}
\]

Since the two discrepancies in (L-105451.1) are nonzero,

\[
\sum_{h=1}^{p-1}
e_p\!\left(h(\widetilde N-\widetilde M)\right)=-1,
\]

\[
\sum_{k=1}^{r-1}
e_r\!\left(k(\widetilde N-\widetilde M)\right)=-1.
\]

Multiplying gives

\[
\boxed{
1=
\sum_{h=1}^{p-1}\sum_{k=1}^{r-1}
e_p\!\left(h(\widetilde N-\widetilde M)\right)
e_r\!\left(k(\widetilde N-\widetilde M)\right).
}
\tag{L-105451.3}
\]

Thus every clean four-owner cross coefficient is the trace of the tensor local
system

\[
\mathcal A_p\boxtimes\mathcal A_r.
\]

Both trivial characters are absent before Cauchy, squaring or coherent
summation.

## Plücker compatibility

In the least/greatest gauge of `T-105440`, the degree-at-least-two source is

\[
q_{ij}
=
x_ix_j\prod_{i<t<j}(1-x_t).
\]

For \(a<b<c<d\), its Plücker rectangle is

\[
q_{ac}-q_{ad}-q_{bc}+q_{bd}.
\]

`T-105440.7` factors this as a left endpoint discrepancy, a middle Euler block
and a right endpoint discrepancy. The two augmentation local systems in
(L-105451.3) attach to those two endpoint discrepancies. Common-factor
extraction commutes with the middle Euler block and contributes only its exact
\(1/d\) weight.

Consequently the clean F1 four-label cycle and the balanced two-phase
semiprime-squareclass packet are the same source coefficient in two
coordinate systems:

```text
F1 coordinate:
  Plücker rectangle of four Frobenius divisors;

arithmetic coordinate:
  two nonzero owner phases on opposite physical sides.
```

This theorem is an identity. It does not estimate the coherent sum over
different owner quadruples.
