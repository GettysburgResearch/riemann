# Unconditional norm-collision and Mellin-averaged energy estimates

Status: PROPOSED complete unconditional component proofs; not independently
reviewed. No pointwise native moment, improved zero-free region, or RH proof.
This is an actual arithmetic estimate, not another conditional comparison.

## The new result

Use the native ideal Mobius coefficients, or the actual coupled 0/1/m
coefficients from #948/#951/#952. Keep every mask, shared prime, equal-norm
ideal and the full Gaussian. For the same finite physical row measure w at
all scales, define Energy_tau(D) as the squared Gaussian source integrated
against dX/X^2 up to D, with the Mellin twist (Nn)^(i tau).

Write F tensor_Q F as a product of r fields. Theorem A pays the ABSOLUTE
sum of all ideal pairs of the same rational norm by

    C_(F,c) w(total) log(3D)^r.

It also pays any symmetric norm-pair graph of bounded degree Delta with
one additional factor Delta. Thus complete near-norm bands of subpower
width cost only a subpower. This is larger than #952's identical-IDEAL
O(log D) diagonal; that earlier theorem is not altered or refuted.

Theorem B proves the FULL Mellin-twist average, centered at any tau_0:

    integral g_T(tau-tau_0) Energy_tau(D) dtau
       <= C_(F,c) w(total) [log(3D)^r+(D/T)log(3D)^(r-1)].

More precisely its difference from the actual equal-norm block is at most
C_(F,c) w(total) (D/T)log(3D)^(r-1). Here g_T is the normalized real Gaussian
of standard deviation T>=1. Constants are uniform in m>=2, phases and
masks, but NOT over fields/discriminants.

For the Eisenstein field, r=2. The full average is O(log^2 D) at T>=D/log D.
At T=D its error from the norm block is O(log D). Theorem C proves that,
for the principal scalar source and fixed m/profile, the block has a
positive explicit asymptotic C log^2 D. The same asymptotic therefore holds
for the full averaged energy whenever T log D/D tends to infinity.

## Why this is unconditional, and why it is not RH

The proof is a source-specific positive Euler calculation, tensor-square
ideal counting, Gaussian integration and a direct Schur estimate. The only
imported analytic facts are classical fixed-field ideal counts and the
simple pole of Dedekind zeta at one. The sharp asymptotic uses a fully
reconstructed classical positive Laplace Tauberian lemma. No quasi-RH,
GRH, compensation inequality or unknown native moment is assumed.

The entire averaged source is controlled, but extracting the individual
principal twist tau=0 is NOT proved. A long average does not bound a single
member. The complete complement of the paid norm graph remains unbounded
at critical strength. No identification with the different coprime theta
row of the recovered ramified-dilation packet is made.

## Read and reproduce

THEOREMS.md has all statements, full proofs, exact constants' dependencies,
and the quadratic Euler constant. TAUBERIAN.md proves the needed positive
lemma and credits its classical origin. SOURCES.md freezes reading scopes.
VALIDATION.md explains the finite arithmetic and numerical checks.

    python check.py > replay.json
    cmp replay.json CHECKS.json
    python -O check.py > replay-optimized.json
    cmp replay-optimized.json CHECKS.json
    python numerics.py > numerical-replay.json
    cmp numerical-replay.json NUMERICS.json

check.py uses only the standard library. numerics.py additionally needs
mpmath and is ordinary high precision, not directed/certified arithmetic.

The exact report has 159,956 predicates, mostly per-norm aggregation guards,
not that many independent analytic cases. Six complete supported-ideal
censuses retain split conjugates and inert primes; the largest has 37,001
supported ideals through norm 131,072. These use explicit algebraic phase
profiles, not an infinite theta row or a physical sextic-row census.

No global priority claim is made for these classical methods. The proposed
advance over #952 is the complete norm-fiber bound and asymptotic, the
uniform correction-order prefix estimate, and the full long-twist mean.
