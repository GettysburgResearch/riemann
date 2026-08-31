# What positivity survives upstairs in the completed period matrix?

Status: PREREGISTERED SOURCE-EXACT MATRIX-THEOREM TARGET.
Base: `ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf`.
Scope: the actual completed Eisenstein period of a fixed finite-dimensional
cusp-form space; its native positive feature kernel and real-axis variance.
No new motive, RH/GRH, purity theorem, or canonical Hecke flag is claimed.

The target is to construct the positive kernel I(z+conjugate(w)) directly
from the unfolded period measure, and distinguish it from pointwise complex
positivity, a Herglotz function, and the proposed fixed-J scattering identity.
The full period matrix is retained; scalar Schur quotients are not substituted
for its source. The expected no-go statements concern this EXACT unrenormalized
matrix, not every possible normalization, scattering construction, or variable.

Preregistered bounded controls, before computation:

- Independently reconstruct the actual weight24 Miller-basis first four
  q rows and the stacked coefficient/logarithmic-frequency determinant.
  The predicted determinant is L2[211312800 L3+1159692288(L3-L2)], positive
  when L3>L2>0. No floating logarithm acceptance.
- For the fixed synthetic positive three-atom matrix
  D(q)=[[1+q,q],[q,q+q^2]], its Schur quotient is1+q^2/(1+q).
  Evaluate EVERY signed derivative (q d/dq)^r for1<=r<=16 at EACH
  q in{1/3,1/2,2/3}. Record every result, including failures of complete
  monotonicity, and do not extend the order/point grid after seeing it.
- Check the exact block-moment/variance identities on three declared
  rational-frequency feature systems, with Gaussian-rational changes of
  basis. Positive finite Gram controls authenticate their algebra, not an
  infinite period, gamma phase, or analytic continuation.

The three finite feature systems are fixed as follows (rows, frequencies,
positive weights, and invertible complex basis matrix):

1. Rows (1,0),(1,1),(0,1); frequencies0,1,2; weights1,1/2,1/4;
   basis matrix [[1,i],[0,1]].
2. The four literal (g,b) coefficient rows at n=1,2,3,4; frequencies1,2,3,4
   (declared rational proxies, NOT logarithms); weights n^-25;
   basis matrix [[1,1+i],[i,2]].
3. Rows (1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,-1,2);
   frequencies0,1/2,1,3/2,2; weights1,1/3,1/9,1/27,1/81;
   basis matrix [[1,i,0],[0,1,1],[1,0,1]].

Classical feature-kernel, matrix-variance, Schur-complement, Stirling, and
modular-form inputs will be credited. Analytic quantifiers require the
written proofs and subsequent independent exact-SHA review.
