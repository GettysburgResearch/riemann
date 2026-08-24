# Unimodular realization of the Hermitian Wick bank

## 1. Exact completion

Put

\[
W_0=I-X/2-X^2/4,
\qquad W_1=X/2,
\qquad B=I+X/2.
\]

Then `W0+B W1=I`, and

\[
U(X)=\begin{pmatrix}W_0&-B\\W_1&I\end{pmatrix},
\qquad
U(X)^{-1}=\begin{pmatrix}I&B\\-W_1&W_0\end{pmatrix}.
\]

This is an exact identity for every operator X.  Hence the bank map
`f -> (W0 f,W1 f)` has the left inverse `(g0,g1) -> g0+B g1`.  It is a
holomorphic embedding with no common zero, no dimension loss, and no bank
partial index.

## 2. Folded source

On two safe-line factors the bank multiplier is

\[
[W_0(X_+)W_0(X_-)+W_1(X_+)W_1(X_-)]
\frac{(I-X_+)^{-1}+(I-X_-)^{-1}}2.
\]

The exact independent-variable calculation has no terms of total degree one
or two.  Its error begins in degree three.  Since the Xi normalized safe-line
source is O(1/log T), the horizontal anchor is I+O(log(T)^-3).

## 3. Xi transfer

The functional equation folds the left line exactly.  The omitted reciprocal
tail is power-saving, and the differentiated coefficient re-expansion makes
the entry-dependent freezing error o(d_T) in the one-copy and two-copy norms.
Fixed-degree bank multiplication preserves those estimates.  The exact left
inverse preserves the observation dimension and proves that the bank itself
has zero partial index.  Therefore BANKREAL105530 holds.

## 4. Remaining theorem

The complete contour still contains the genuine Xi companion, vertical, and
partial-index field.  If its Gram-normalized negative trace is less than
`(1/20-o(1))d_T`, negative-trace absorption leaves more than 19/20 positive
directions, and the full confluent Cauchy-index identity gives more than 90%
of zeta zeros on the critical line.

That signed flux estimate is MATRIXLERC105541.  It remains open; 90% and RH
are unproved.
