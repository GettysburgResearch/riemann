# Independent audit of the complete-pair Laguerre identity

Verdict: **ACCEPT at the complete-product/localization scope.** Reviewed
[PAIRWISE_COMPLEX_LAGUERRE.md](../xi/outer-ray/PAIRWISE_COMPLEX_LAGUERRE.md)
at SHA256
`d71611e93f975c7f722685c1f55ed0a5bb002b04ef9a659ba2a30761862abb97`,
2026-10-10 14:38 UTC. This is a separate alternate proof of the already
accepted finite companion column. No mathematical correction was found.

For a real linear root factor the normalized complex Laguerre numerator
is exactly 1/[(x-alpha)^2+y^2]. For the complete conjugate pair
g=(z-gamma)^2+eta^2, direct differentiation g'=2(z-gamma), g''=2 gives
the numerator 2[(x-gamma)^2+3y^2-eta^2]/|g|^2. Its imaginary logarithmic
derivative is exactly 2y[(x-gamma)^2+y^2-eta^2]/|g|^2. Both are strictly
positive at every y>0 when |x-gamma|>|eta|.

The complete block product identity PL5 has the correct factors 2 on
the multiplicity-diagonal correction and 4 on distinct-block cross
terms. Positive integer multiplicities make every correction
nonnegative. The absolute convergence of complete imaginary
logarithmic sums and of the differentiated inverse-square sum follows
from the bounded root strip and complete genus-zero inverse-square
summability. Passing finite complete blocks to the limit retains a fixed
strict lower bound from any first block. No exponential contribution is
missing under the parity source's constant-exponential product.

Derivative localization gives the required horizontal gap greater than A
on |Re z|<C_(r+1). The middle coefficient is therefore positive at all
lower depths there. The smaller C_(r+2) column retains the two strict
imaginary logarithmic derivatives needed for the constant and quadratic
coefficients. This proves the companion sector directly for all y>0,
with the existing simple-census real boundary handling y=0. The finite
real-part width, derivative-order range and imported census qualifications
remain unchanged; no RH conclusion follows.
