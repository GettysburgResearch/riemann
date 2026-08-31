# Independent review of restricted native Mellin observability

Reviewed scientific commit: `6dbab098bb057d76748d12e37900efeff571f8a9`.

Review object: the five new restricted-Mellin files at this commit. Later
README or handoff edits are not part of this scientific freeze. The
predecessor multiplicity/rank packet at `9547f4cdc2c8e27a36704029fd74470de844d401`
has its own independent review.

Verdict: no remaining mathematical or implementation blocker found for the
specified coefficient projection, exact autonomous linear realization, and
absolute estimates for the isolated restricted grid. None of these claims
establishes survival in the complete weighted source assembly.

## Evidence boundary

I independently read the proof, complete producer, manifest, and twelve
tests, and inspected the final coefficient, tensor-generator, channel, and
test corrections at this exact commit. I checked the relevant frozen
L-106025/026, L-106080, L-102746, L-106120/191, and T-106140 source formulas.
I did not execute a producer, test, linter, logarithm calculation, or search.

The implementation agent reports Ruff, producer `--write`, ordinary and
optimized `--check`, and twelve tests in both ordinary and optimized Python
passing, with proof-object digest
`f4dd93b81eba3adfa36e96276540030504482ea741eb6d162b15cef17b1055c7`.
These are reported runs, not independent executions by this reviewer.

## Native coefficients and scope of the projection

The projection order is explicit. It selects the balanced squarefree
coefficient coordinate and finite core shells, retains the actual equal-pair
shares and reciprocal weights, and aggregates the two positive Boolean
histories per side. Principal character values at these cores are one by
the checked owner/core coprimality. Carrier and other formal source labels
remain separate; their final weighted recombination is not replaced by one.

The source formulas give one-sided amplitudes `2/(15 sqrt(N_i))` and
`2/(15 sqrt(M_j))`. Consequently the conjugate-left/right convention yields

`F(t)=sum c_ij (N_i/M_j)^(it)`,

where `c_ij=4/(225 sqrt(N_i M_j))`
`=4/(225*35*g^2*sqrt(P_i Q_j))>0`.

Source-dual scaling is exactly `Ftilde=35g F`, so
`ctilde_ij=4/(225g sqrt(P_i Q_j))`. These are actual positive irrational
weights, not substituted rational weights. The replay records rational
squares together with their positive branch. Reversing the whole Fourier
orientation changes frequency signs but not distinctness or minimum rank.

This is an authenticated coefficient-level finite-shell projection. It is
not a proof that all original carrier, selector, renewal, marked-prime, or
coupled-mask data combine into this naked scalar member, nor that the full
source can be recovered from this projection alone.

## Observability and its exact limits

Global owner-prime disjointness proves that every ratio
`(25/49)P_i/Q_j` is distinct: equality would force equal left and right
owners by prime valuations. The ratios remain positive and near one, and
each coefficient is nonzero. There are mn modes after the four literal
histories per pair have been combined, not 4mn modes.

The standard exponential-independence argument proves the differential
annihilator has exactly these mn distinct roots. Cayley-Hamilton then gives
the lower bound for a constant generator with a constant linear readout on
any nonempty open real interval. The derivative Hankel determinant is the
displayed product of nonzero coefficients, exponential factors, and squared
frequency Vandermonde differences.

The upper realization is source-defined: the Kronecker difference of the
two diagonal physical dilation generators on C^m tensor C^n, with the
actual one-sided coefficient vectors and tensor sum readout, gives the
same member in dimension mn. No desired zeros or observed spectrum are used
to construct that generator.

The conclusion is specific to exact autonomous **linear** realization.
It does not assume arbitrary source-vector freedom or faithful action of
every source idempotent. Conversely it does not exclude time-dependent or
nonlinear readouts. For example, keeping the two one-sided flows in a
direct sum and combining their two outputs multiplicatively uses a
different, nonlinear readout class. The theorem does not supply a lower
bound for that class. It also supplies no stable numerical rank,
conditioning, fixed-tolerance approximation, or sampled-time theorem.

The kernel injectivity argument is correct for the complete filtered
function: a nonzero compact kernel has Fourier transform nonzero on some
real open interval, where division followed by exponential independence is
valid. The zero at t=0 does not collapse distinct finite Mellin members.
This does not assert that the filtered function has the same autonomous
realization dimension or that one integrated scalar observation is injective.

## Absolute size and literal diagonal

The physical window gives the exact inequalities
`8mn/(495Y)<sum c_ij<=4mn/(225Y)`.
Combining the upper bound with the predecessor's owner-disjoint rectangle
bound gives the two stated uniform sup-norm orders. Source-dual scaling
uses `35g<35U^2/3` and produces
`sup|Ftilde|=O(Y^(-1/3)/(log Y)^2)`.

Four equal literal histories per pair give the literal diagonal
`Dtilde=(1/4)sum ctilde_ij^2`. Therefore the restricted additive Wick form
is exactly `(24/35)(|Ftilde|^2-Dtilde)`. This retains the repaired literal
normalization; it does not substitute the newly centered arithmetic-pair
diagonal. The pointwise bound by `(24/35)(sum ctilde)^2` is valid.

T-106140.3 confirms the same bilateral measure
`|kappahat(t)|^2 dt/(2pi)`. Its total mass is `||kappa||_2^2`, so the
absolute integral is `O(Y^(-2/3)/(log Y)^4)`. At the fixed cell the principal
and Kummer forms have the same parenthesis with constants 2/35 and 22/35;
the same absolute order follows for all three restricted channels.

This bounds interactions internal to the selected grid only. It does not
bound its cross terms with complementary atoms, sums over common cores or
conductors, or the complete signed current. In particular the large exact
linear rank is compatible with a small absolute signal; the zero
approximation already has small uniform absolute error.

## Adversarial code findings and controls

One incorrect test assumption was found independently and also hit by the
implementation agent's initial run: the reduced numerator of every native
coefficient square need not be a perfect square. When an owner includes
the prime 2, numerator 16 can reduce to 8. The correct rational-square test
asks whether **both** reduced numerator and denominator are squares. The
frozen test now negates that conjunction. This repaired a test assumption;
the native coefficients, producer arithmetic, and mathematical theorem were
unchanged.

The rest of the source inspection found no defect:

- Coefficient squares are checked independently via physical N,M and via
  g,P,Q, including the source-dual scaling and factor sixteen from adding
  four equal histories before squaring.
- Exact rational ratio separation is recorded without evaluating logarithms
  or square roots. The rational Vandermonde is explicitly a surrogate
  separation certificate, not the native derivative Hankel determinant.
- A direct three-node determinant expansion tests that surrogate. Repeated
  frequencies, cancellation, positive aggregation, zero coefficients,
  one-mode data, and the conjugate orientation test the rank hypotheses.
- Both live panels are revalidated through the authenticated predecessor.
  Owner overlap is rejected before any mode claim. Exact positive amplitude
  bounds and the literal quarter-diagonal are checked algebraically.
- Frozen source bytes are read with size caps and rehashed using the Git
  blob convention, not merely accepted from a manifest label. Current
  predecessor executable bytes must match the frozen version before import.
- Mode count, rational size, file size, and fixture size are bounded. Full
  replay, rather than an internal checksum alone, is required for acceptance.
  Production checks use explicit exceptions and are retained under `-O`.

The exact commit above binds this review. Finite replay does not reprove
PNT, logarithmic independence, all-horizon estimates, or external novelty.

## Remaining gate

The substantive bridge is from a declared native coefficient projection to
an exact Mellin function with a minimal linear source parent. A proposed
Riemann structure is constrained by this result only if it must retain that
projected function in the stated realization class. If it needs only the
integrated scalar or another quotient, this rank theorem is not an
obstruction. Complementary signed source terms and their complete
recombination remain open. No RH, GRH, WCADD, WCKUM, WCCORR, automorphic,
motivic, or external-priority conclusion is established.
