# Determinants aimed at a single exceptional zero

**Proposed component proofs and a source import. No RH proof or new fixed
complex zero-free half-plane is claimed. Independent review is required.**

## What is new in this packet

[RECTANGULAR_JETS.md](RECTANGULAR_JETS.md) separates the derivative depth
from the grid-incidence parameter in the supplied Green argument. A
balanced rectangular quadratic grid then gives the proposed uniform bound

    sum_(p<=R,chi(p)=-1) log(p)/p
       <= (1/2)log R+(1/4)log q+O(1+log log(3R)), R>=max(q,R0),

for every primitive nonprincipal real Dirichlet character of conductor q.
The classical logarithmic derivative yields the proposed real-zero corollary

    (1-beta)log q >= 1-O(log log q/log q), q -> infinity.

The first is a PRIME-BIAS estimate; the second excludes exceptionally near-one
REAL zeros. Neither is a statement that all complex zeros lie left of 1/2
or an improvement over a separately established fixed strip. No zero-free
strip or earlier no-Siegel-zero theorem is used as an input to these proofs.

## The single full-RH direction pursued

[ZERO_PRESERVING_ROUTE.md](ZERO_PRESERVING_ROUTE.md) follows determinant
profiles down to one fixed zeta denominator. It identifies two traps:
inert-prime profiles can cancel common zeros, and a perfectly integral
all-prime Hermite determinant has Mellin transform -zeta', not -zeta'/zeta.
An exact Mobius desieving restores every zero, with its multiplicity, and
still yields the positive integer

    A_N=product_(p^j<=N)p^(N-p^j)=product_(r<N)lcm(1,...,r).

The centered log-volume's Mellin transform is exactly

    [-zeta'/zeta(s)-1/(s-1)]/[s(s+1)].

Its full Gaussian transfer agrees with the fixed prime source in #991.
The missing signed height bound is explicitly OPEN-PD. It is a classical
RH-strength lcm/Riesz-mean target, not a claimed weaker substitute or an
already proved determinant inequality. The identities, their classical
antecedents, and the failed shortcuts are all stated in the proof.

## Source and execution boundaries

Read [IMPORT.md](IMPORT.md) and the supplied note's complete
[mathematical transcription](sources/GREEN_NOTE.md). Its identifier is
hexagon, not arXiv; the printed attribution is not independently authenticated.
The unchanged PDF is included in the conversation download, not the Git
text import. The original OpenAI source is already pinned in #908 and is
not duplicated. The new mathematics does not depend on either author's
reputation or on the imported no-Siegel-zero conclusion.

Run `python -B replay.py` from this directory. It verifies every manifested
payload, reproduces the exact finite tests in ordinary and optimized Python,
and executes seven corrupted processes which must fail at the specified gates.
The tests include complete quadratic grids, actual Gram determinants and
p-adic row reductions, Hermite/Sylvester determinants, and full declared
integer desieving ranges. They are not a verification of the infinite proof.

[REVIEW.md](REVIEW.md) records the same-author audit and remaining review
obligations. [VALIDATION.md](VALIDATION.md) records actual execution scope.
No independent referee, separate research agent, Lean build, remote CI,
actual L-values, or numerical zero census is claimed. Main and inherited
mathematical statements are unchanged.
