# Review contract and the attempted end-to-end finish

## Four claims submitted

**SC1: full spectral compression.** Reconstruct the critical-line mean-square
bound from DLMF25.9.3, retaining the moving Dirichlet cutoff. Check the complete
dyadic zeta-weight tail, the real Taylor remainder and columnwise Hilbert--Schmidt
sum. Then verify the trace approximation principle and the index conversion to
lambda_(r+1)<=C_A Y log(r+2)/(r+1)^2. The auxiliary Taylor range need not be causal;
only its rank and error are used. The final map is actual T times a coefficient
projection. All constants are existence constants, not numerical certificates.

**SC2: finite arithmetic selection.** The earlier RC form contains V/H and a
complete tail bound before any coefficient selection. Check its b=0 homogeneous
version and both relative inequalities. The leading eigenspace of that finite
form gives (16). Exact derivative constraints include logarithms; the underlying
matrix alone is rational. No large-rank projector or bit-complexity theorem is
claimed. Eigenvalue ties allow any orthonormal choice of the needed dimension.

**SC3: the graph adapter.** For a tail [Y,AY], all downward prime-power edges to
parents below Y contribute to (18). Check the original log-prime weights and
zero lower vertices. The resulting generalized eigenvalue bound counts high-gain
modes. It does not put every high-ratio vector literally in a chosen subspace,
or prove the full Weil sign, or discard the retained channel.

**SC4: constrained optimization.** Center at the coefficient-norm minimizer,
not an unproved physical solution. The tangent projection preserves prefix and
all affine constraints and cannot increase S. Verify square-root error (24)
using the full norm difference. Nonemptiness of S<=130(1+logY), N=4Y, follows
from the explicit BMC family. The coefficient budget is load-bearing.

## First unproved theorem

For N=4Y, the prescribed near-square-root retained affine space, and coefficient
budget S<=130(1+logY), prove subpower physical minimum along one unbounded integer
sequence Y. Section7 states this as OPEN, then gives the complete conditional
RH implication via the delayed Hardy value. A reviewer is not being asked to
supply that arithmetic inequality under the label of routine verification.

The dimension is now O(sqrt(Y)log^2Y), but assembling its source matrix may still
require the original O(Y)-dimensional matrix and a polynomially larger physical
cutoff. There is no claim that computing the remaining task is cheap. Nor does
this result show that the unrestricted physical minimum has a bounded-coefficient
optimizer. Its scope is the explicitly nonempty coefficient-budgeted class.

## Relation to the prior corpus

The parent's worst-case graph-to-physical factor Y/logY survives fixed safe jets.
The new theorem quantifies how many independent high-gain directions it can
occupy, retaining them instead of assuming they vanish. It does not refute the
parent's source-preserving variations. The original source and Hilbert norms
are unchanged. No outerness or sign assumption is imported.

The classical zeta second moment is unconditional; it is not the RH-conditional
Cramer bound for prime-discrepancy energy on #818. The earlier spectral-exponent,
intrinsic-entropy and square-grid criteria remain context, not a missing upper
bound supplied by this composition. The integration candidate #830 and published
review #827 do not independently accept this new author manuscript.

## Finite evidence

The checker tests exact geometric integer nodes, where critical and safe jets
reduce to rational identities after factoring common powers of log4. It tests
finite spectral ordering on declared rational models, not actual large zeta
matrices. Complete small integer period means and prime-power graph expansions
are independently reconstructed. No numerical zeta norm or new minimum is run.
The full infinite arguments need mathematical review beyond these tests.
