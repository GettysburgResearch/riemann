# Chow-module source replay: preregistration

Status: declared before this packet's first computation, 2026-08-31.
This is a source-binding and exact algebra packet, not a new claim of the
classical Chow-module construction or a finite determinant parent.

## Inputs and comparison boundary

Write `d=dim(V)` and `m=number of factors`. The source is
`R_r=(Sym^r V)^{tensor m}` and the polynomial base is
`S'=Sym(W)`, `W=Sym^m V`, acting by orbit sums in `V^{tensor m}=R_1`.
The replay constructs that multiplication; it does not reconstruct a companion
matrix from a rational series.

PR781 is pinned at `ac1cc5eaf229087b6d805e908897c7c8c99a58b7`.
Its generic recurrence denominator is `det(1-T Sym^m A)`.
The concurrent ambient bridge at
`64c8664a2fee08ae2e249743d6f784a7bec61b83`, path
`research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md`,
uses the different polynomial base `Sym(V^{tensor m})`.
Its rank-three cube, order-three collision, and reciprocal slice have already
been inspected. They are not untouched heldouts here.

Raicu--Sam--Weyman, arXiv:2108.10910, already constructs this finite module,
its Cohen--Macaulay structure and binary freeness. In particular their
Example 4.5 exhibits a degree-two `det(V)^2` generator in the invariant
normalization summand for `(d,m)=(3,3)`. Therefore the tempting resolution
inferred solely from `[1,17,-9,-65,65,9,-17,-1]`, with no degree-two generators,
is a predeclared false control.

## Panels and predictions

1. Binary `m=2,...,8`, eigenvalues `(2,3)`: `QF` equals the permutation
   descent/major-index polynomial after homogeneous substitution, has degree
   `m-1`, is effective, and has total dimension `m!` at identity.
   All permutations are enumerated only for this bounded comparison.
2. Rank-three square and cube: exact character comparison and degree-two/three
   Koszul homology from the actual orbit-sum multiplication. The cube has
   `(s,D,c,deg N)=(10,7,3,7)`, and at identity the above signed numerator.
   Its degree-two quotient has at least the invariant determinant generator;
   no other Betti number is inferred from that numerator in advance.
3. New source-replay heldout `(d,m)=(3,4)`, eigenvalues `(2,3,5)`:
   `(s,D,c,deg N)=(15,9,6,12)`, top coefficient `det(A)^16`, first coefficient
   `tr(A)^4-tr(Sym^4 A)`. This is a heldout relative to this packet's previously
   inspected repository computations, not a literature priority claim.
   Its degree-two source Koszul complex is constructed independently. No
   quotient or Tor rank is preassigned before the exact calculation.
4. Collision controls: identity rank-three cube reduces the scalar recurrence
   denominator to `(1-T)^7` while universal `Q=(1-T)^10`; this does not change
   the source module. A nontrivial unipotent matrix has the same character
   series as identity but is not the identity matrix.
5. Independent-factor deformation: on binary square, `diag(2,3) tensor
   diag(5,7)` does not preserve `W`, because the two mixed coefficients are
   `14` and `15`. Proportional factors do preserve it.
6. Ramification: for `V=1+sgn` of `C2`, binary-square `R^I` has degree-two
   dimension `5`, versus `3` after replacing both base and quotient by their
   fixed parts. The full invariant complex is the correct operation.

## Computation contract

Only the parent runs jobs, one at a time under the shared RAM gate. The replay
uses exact integers and rational sparse elimination, never modular rank as a
proof of characteristic-zero rank. Every tested Koszul differential is built
from orbit sums, every consecutive differential is checked to compose to zero,
and image traces are computed on the actual rational image subspace.
All complex bases, matrix blocks and arithmetic loops have explicit caps.
The degree-three cube has 4,495 total chain basis elements; the degree-two
four-factor ternary heldout has 2,616. No full higher-degree resolution is
claimed from these truncations.

No computation or validation result is asserted in this preregistration.
