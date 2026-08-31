# Actual source polarization, the prime-core domain, and four-node residuals

Status: PREREGISTERED ANALYTIC/FINITE DESIGN; not yet a frozen science packet.
Authoring base: `8f01064df805624c045877655893c324a220975d`.
RH remains unproved. No external novelty or priority claim is made.

## Frozen pre-computation design

This design is committed before evaluating any new actual-Xi matrix. The
algebraic four-node identity was discovered analytically and checked on the
single exact rational cell x=(1,2,3,4), p=(1,3,2,7). That discovery cell is
not held out. The arithmetic controls below will retain it as a known control.

The intended analytic results are: the exact full-line polarization of the
actual Fourier density; the equivalence between RH and closability of the
full prime multiplier on the finite exponential core; an exact four-node
factorization, its singular-anchor-safe residual, and its literal source
reconstruction. A pointwise positive one-spectator Volterra factorization
of the coefficient u+v is impossible. This last obstruction does not rule
out global factorization or an arithmetic source-specific construction.

Normalization: X(z)=xi_R(1/2+iz), Y(x)=xi_R(1/2+x)=X(ix),
F=Y'/Y, p(t)=F(sqrt(t))/sqrt(t), safe nodes x>1/2. The full-line
Fourier density is Phi=2 phi0 in XL1--XL4, not the historical half-density.

The numerical panel is fixed to these six ordered rational quadruples:

1. (3/4,1,3/2,2);
2. (1,2,4,8);
3. (1,65/64,33/32,67/64);
4. (2,3,5,7);
5. (8,16,32,64);
6. (16,32,64,128).

For every quadruple, compute the full native safe matrix, all its principal
minors, both four-node factors and divided-difference residuals, and the
fraction-free three-anchor residual. Use literal completed Xi through the
native FLINT zeta/Gamma series, with a fresh signed first jet at each node;
512-bit precision, no escalation, domain 1/2<x<=128. Retain every nonfinite,
zero-containing, or wrong-sign enclosure as unresolved or failed as
appropriate; do not move nodes. All six panels are finite controls only.

Exact controls use Fraction arithmetic and two independent determinant
routes (permutation expansion and elimination), including Gaussian rank-one
data, one-atom and two-atom Stieltjes data, the known discovery cell, and a
fixed rational grid of non-Stieltjes data. Test dimensions are capped at four.
The existing positive smooth exact-Xi-tail counterfeit is used as an
analytic countercontrol, not numerically integrated: its previously proved
off-real zero and wrong-sign Laguerre point imply that its polarized source
is not PSD. No new location, finite-order witness, or Xi zero is inferred.

Arithmetic class: MIXED {DIRECTED_BALL_ENCLOSURES, EXACT_RATIONAL,
CERTIFIED_INTEGER_COVERAGE}. Native ball endpoints are rounded outward to
dyadic rational intervals. Ordinary decimal output is display only.
Artifact and source seals, strict types/caps, fresh reconstruction, semantic
mutations, normal/optimized tests and exact emits are required before freeze.

The earlier integrated size-three theorem is used only in its repaired PSD
form, for safe real nodes, with grouped C2 convergence, multiplicities,
the corrected external lock, and the single shared critical reserve. It
does not provide strict three-anchor invertibility. No all-order source
positivity, prime factorization, closability, or RH premise is assumed.
