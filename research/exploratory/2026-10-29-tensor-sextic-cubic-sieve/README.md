# Two-variable Gram reduction for square-part theta rows

**Status.** Exact algebraic reduction and an obstruction to deriving an improved bound solely from the two individual operator norms. It does not rule out an arithmetic mixed-sieve theorem. Source reciprocity/sector identification and the physical completed-theta interface are the inputs of [the fixed-w cubic moment](../2026-10-29-squarepart-cubic-theta-moments.md).

Let W,V,X denote dyadic ideal norm bounds. On enlarged independent sets of squarefree good w and cube-free good v, consider the common-column matrix
\[
 A_{(w,v),n}=\chi_n(w)\chi_n(v)^2,
\qquad n\text{ good squarefree},\quad Nn\ll X.\tag{1}
\]
Coefficients \(c_n\) are independent of w and v. The original rows \(b=wv^2\) and their annular/norm restrictions form a subset of this product, so their positive second moment is bounded by the product-row moment. The equality also holds when w and v share primes: multiplicativity with zero extension is exact. Fixed k,f, finite-ray phases and the differentiated smooth profile enter the common column coefficients after fixing their sectors. The theta cube-index factor is removed as a bounded row contraction *before* enlarging; it is never treated as a row-independent column vector.

Define the two column Gram matrices
\[
 G_6(n,m)=\sum_w\overline{\chi_n(w)}\chi_m(w),\quad
 G_3(n,m)=\sum_v\overline{\chi_n(v)^2}\chi_m(v)^2.\tag{2}
\]
On independent product rows the exact column Gram matrix is
\[
 A^*A=G_6\circ G_3,\tag{3}
\]
where \(\circ\) is entrywise product. Both matrices are Hermitian positive semidefinite, including at noncoprime indices. Schur's positive-product inequality gives
\[
 \|G_6\circ G_3\|\le\min\{(\max_nG_3(n,n))\|G_6\|,
 (\max_nG_6(n,n))\|G_3\|\}.
 \tag{4}
\]
The diagonal bounds are \(O(V)\) and \(O(W)\), up to subpowers. Applying the sixth- and cubic-order source sieves to the separate matrices recovers precisely the two existing bounds
\[
 \|A\|^2\ll (WVX)^\epsilon\min\{V\Theta_6(W,X),\ W\Theta_3(V,X)\}.\tag{5}
\]
The unstratified \(\Theta_6(WV^2,X)\) estimate is a separate physical-row input, so all three can be minimized.

## Why separate norms alone do not close the gap

The inequality (4) can be sharp even with unit-modulus matrix entries and diagonal sizes W,V. For any positive odd integer M and X divisible by M, let W=V=M, take an M-by-M discrete Fourier matrix F with entries of modulus one, and repeat each of its M columns X/M times to form an M-by-X matrix A₆. Let A₃ be its entrywise square. Oddness makes the squared Fourier columns mutually orthogonal as well. When \(M\le X^{1/2}\), the source expressions \(\Theta_6(M,X)\) and \(\Theta_3(M,X)\) are both \(\asymp X\). Each separate Gram matrix has operator norm X; their common block structure gives \(\|G_6\circ G_3\|=MX\). Thus the Schur upper bound \(\min(V\|G_6\|,W\|G_3\|)=MX\) is attained. This is an abstract bounded-phase model, not an example of number-field residue symbols or a lower bound for the physical theta moment. It establishes only that a power gain cannot follow from separate operator norms and bounded entries alone.

A useful genuinely mixed estimate would have to control correlations in (3), for example the off-diagonal quadratic form
\[
 \sum_{n\ne m} \overline{c_n}c_m\,G_6(n,m)G_3(n,m),\tag{6}
\]
with the actual sextic Gauss/theta coefficients, original zero masks and common fixed profiles. Bounding the magnitudes of the two Grams separately or applying only (4) loses the sought joint cancellation. In the latest certified whole-cube scalar bottleneck one may take \(V=1\), so (3) reduces to the ordinary sixth-order Gram matrix; no improvement there can come from averaging a nontrivial v-family. Any route through this corner must exploit the actual theta/Gauss coefficients or their correlation with the Möbius/angular prefix. This observation does not preclude a genuine two-variable saving elsewhere in the core.

**Independent review.** High_match checked the Gram orientation, zero masks, Schur inequality, Fourier block construction and V=1 scope under the stated source matching.
