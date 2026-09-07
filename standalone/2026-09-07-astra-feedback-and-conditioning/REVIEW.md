# Independent-review handoff

This is an AUTHOR submission, not a referee verdict. All mathematical results
below are proposed component theorems. The full RH theorem is not supplied.

## Proof obligations and status

| Record | Exact statement | Scope / dependencies | Disposition |
| --- | --- | --- | --- |
| FC26.1 | A relative Schur residual plus an exact horizon produces bounded, source-admissible, expanding-horizon outputs | Conditional; Hardy multiplier invariance and weak compactness; PROOF section 1 | Proof supplied; Schur premise not established |
| FC26.2 | Second Newton iterate of FR26 ideal degree-four correction has a nonzero atom | Literal authenticated rational polynomial; local causal distributions; section 2 | Proof supplied; not a retraction of FR26 finite norm |
| FC26.3 | Critical-boundary relative multiplier mean square tends to infinity | Actual zeta/factorial source; one FIXED compact input in stated regularity class; all finite jump times including irrational ones; section 3 | Proof supplied |
| FC26.4 | Reusing that fixed residual has superexponential Newton-iteration cost | Section 3 and boundary Plancherel; output may leave L2; section 4 | Proof supplied; does not concern reoptimized horizons |
| FC26.5 | Source-specific quasipolynomial finite Gram conditioning | Euler-safe bounds, local Jensen/Harnack, polynomial concentration; section 5 | Proof supplied; no zero-free critical region assumed |
| FC26.6 | Full finite source cutoff with time O(log squared rank) | Section 5 and the exact FR26 source/filter tail inequality; section 6 | Proof supplied; conservative constants |
| FC26.OPEN | A varying source-admissible sequence with exact horizons T_j and error exp(o(T_j)) | Section 8 | UNPROVED; remains RH-bearing |

## Load-bearing checks for a reviewer

Check the cancellation of the pole at s=1 BEFORE the contour used to transfer
frequency means. The boundary mean argument must keep the prime p fixed while
sending the interval length to infinity, and only afterward enlarge the finite
prime set. It uses divergence of the prime harmonic series, not an unproved
critical-line mean-value estimate or independence of prime logarithms.

Check the finite exceptional-prime classification for jump ratios exp(tau):
if p=n exp(tau) and tau>0, the reduced numerator of exp(tau) must be p.
This is why no algebraicity or irrationality oracle is used for actual jump times.
The theorem is not extended to infinitely many accumulating jumps.

Check the source impulse at time 2log2 in section 2. The ideal polynomial
correction has feedthrough p(1)!=0. The compact-input realization has a different
regularity and must NOT be assigned the same Dirac mass by analogy.

Check the exact normalized Cayley boundary measure in section 5. The removed
set is small enough that a degree-K polynomial cannot put all its L2 mass
there. Jensen counts ALL relevant zeros with multiplicity; off-line zeros are
not omitted. The rational floor is intentionally very small. Its improvement
is asymptotic, not a new measured condition number or a practical high-rank run.

## Current proof boundary

Finite conditioning, finite realization, and convergence toward an intrinsic
model-space floor do not identify that floor as zero. Section 7 gives an exact
synthetic example with exponential convergence to a positive floor.

The fixed-controller completion was actually tested mathematically and is
refuted for the stated class. A future proof must use varying controllers,
a different relative norm, or a different mechanism, and must establish the
actual output bound in FC26.OPEN. Reviewers are not being asked to fill that
central estimate. No older source, claim, numerical certificate or review is
silently overwritten by this packet.
