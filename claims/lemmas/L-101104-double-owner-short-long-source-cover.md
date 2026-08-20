# L-101104 — Double ownership gives an exact short/long source cover

Claim ID: `L-101104`  
Status: **PROVED EXACT SOURCE PARTITION + SHORT-SECTOR CLOSURE**  
Created: 2026-08-20  
Depends on: PR #691 `L-100605`; `L-101102`  
RH status: **not assumed**

For a finite ordered Euler source
\[
 \mathcal F=\prod_{h=1}^k(I-r_hU_h),
\]
the exact double-owner identity of `L-100605` is
\[
 \mathcal F
 =
 I+\sum_i(-r_iU_i)
 +\sum_{i<j}
 r_ir_jU_iU_j
 \prod_{i<h<j}(I-r_hU_h).                           \tag{L-101104.1}
\]

Split the off-diagonal owner pairs into
\[
 \mathcal S=\{(i,j):p_j/p_i\le8\},\qquad
 \mathcal L=\{(i,j):p_j/p_i>8\}.                    \tag{L-101104.2}
\]
Then for every linear physical observation \(\mathcal O_X\),
\[
 \boxed{
 \mathcal O_X\mathcal F
 =
 \mathcal D_X+\mathcal S_X+\mathcal L_X,
 }                                                   \tag{L-101104.3}
\]
where \(\mathcal D_X\) is the identity-plus-diagonal channel and
\(\mathcal S_X,\mathcal L_X\) are the exact short and long off-diagonal
channels.  Every source monomial occurs exactly once.

For the positive final critical Bernstein kernel, every interior label of a
short block satisfies the ratio in `L-101102`.  Hence
\[
 \boxed{\mathcal S_X\ge0}                            \tag{L-101104.4}
\]
at that scope.

For a sign-changing compact wavelet observation, (L-101104.4) is not asserted.
Instead the same partition identifies the short sector on which the
phase/near-collision machinery is naturally localized, while long intervals
are the sector on which finite interior squaring and positive divisor renewal
apply.

This is an exact source cover, not a similarity of formulas.  It permits
different proof technologies on \(\mathcal S\) and \(\mathcal L\), followed by
one recombination through (L-101104.3).
