# Determinant rigidity for native moment coefficients

**PROPOSED component mathematics. The generalized native moment and RH remain
open. No moment exponent or zero-free boundary improves in this packet.**

Continuation of PR #935, exact base
`a7a7fad2c5fa1929c7e04570cde4188e3191b071`.
Read [PROOF.md](PROOF.md); [VALIDATION.md](VALIDATION.md) states what ran.

## What this pass adds

### 1. A bounded-rank classification

The previous finite-ray theorem assumed |a(g)|<=1 and forced a=0 or a=-eta.
With an arbitrary fixed bound |a(g)|<=R, and an explicit fixed small-prime
exclusion, a diagonal physical moment at one order 2k and 0<h<6k/5 for
all finite-ray twists instead forces

    a(g) = -sum_eta m_eta eta(g),
    m_eta nonnegative integers,  sum_eta m_eta <= floor(R).

Thus the permissible prime data in this class are negative characters of
actual finite-dimensional representations. This is a necessary condition,
not a theorem that their physical moments are small. The singularity and
sixth-power copying mechanism is inherited from #933/#935; the bounded-rank
classification uses its Fourier coefficients and evaluation at the identity.

### 2. A reversible determinant completion

Complete those prime values to the full local polynomial

    det(I-z rho(g_p)),

instead of retaining just 1-tr(rho(g_p))z. Both directions of the exact
Dirichlet-convolution comparison have absolute coefficient norm at most

    zeta_K(2 sigma)^(4r^2),  sigma>1/2,

after excluding Np<=4r^2. At sigma=1/2 the finite-scale cost is
O(log(2+D)^(4r^2)). The exponent is deliberately not optimized.
This comparison holds on the actual row measure, preserving nonunit zeros,
all original exclusions, and overlapping convolution factors. It requires
all shorter column scales at the SAME row height.

For abelian rho the completed coefficients are a Dirichlet convolution of
r native Mobius-character functions. Its Euler series is a product of r
inverse Hecke L-functions. This is an algebraic and norm comparison, not
a bound for those inverse L-functions on the critical line.

### 3. A nonabelian extension with stronger hypotheses

For a fixed finite Galois extension and central a, impose the moment
hypothesis after EACH irreducible character-valued prime probe. Then -a
is a genuine group character, of dimension at most R. These probes are
not generally one-dimensional Hecke twists; omitting them invalidates the
conclusion. Only classical Artin behavior at s=1, reconstructed from Brauer
induction and Hecke theory, is used. No Artin holomorphy conjecture is assumed.

### 4. The precise conditional hierarchy transfer

In the abelian rank-r case, a native 2kr-th moment with excess e_(kr),
uniform over the specified shorter scales and Mellin tests, supplies a
2k-th moment for the determinant and its squarefree prime-trace form with
excess e_(kr). A finite dyadic decomposition and Holder prove this statement.
It does not turn a linear excess into a sublinear one. At r=1 it just
returns its input, so it is not a new bootstrap to RH.

## A useful failure check

At rank three and a prime ideal of norm 7,

    (1-z)^3/(1-3z) = 1+3z^2+8z^3+24z^4+72z^5+... .

The square-root-weighted local series diverges because 3/sqrt(7)>1.
The fixed small-prime gate in the two-way operator estimate cannot simply
be deleted. This is a kernel counterexample, not a native moment refutation.

## What remains

The #935 Liouville/divisor-profile second moment at product length X^k,
near-linear physical height, and all required shorter scales is still
unbounded at H X^(k+epsilon). The present completion does not supply that
signed cancellation. The contribution is a larger exact coefficient class,
a reversible physical norm comparison, and a fully priced conditional
transfer, not a newly attained fourth moment or zero-free half-plane.

## Executed checks

Run with Python 3 and no third-party packages:

    python -I -S -B verify.py > replay.json
    python -I -S -B -O verify.py > replay.optimized.json
    cmp replay.json results.json
    cmp replay.optimized.json results.json

The reports agree byte for byte. There are 20,535 explicit finite predicates,
including setup checks: 1,555 local eigenvalue lists through degree 12;
1,040 rational local-bound points; finite classifications on C2, C3 and S3;
and 1,944 forward/inverse physical-sum comparisons on 54 actual Eisenstein
rows. Four deliberately invalid substitutions are rejected.

All nonzero rows of norm at most 13 are included. Columns are ONLY the
24 ideals of norm at most 512 in a named five-prime semigroup (prime norms
7,7,13,19,25), not all native ideals below that cap. The small-prime algebra
fixtures test exact identities, not the analytic cutoff condition. The S3
fixtures are character-table computations, not a new arithmetic moment.

The proof and code have the same author. No independent review, Lean proof,
full-repository validator, external theorem replay, or remote CI was run.
The manifest authenticates the listed bytes, not their mathematical truth.
Classical and earlier repository mechanisms are credited in the proof and
source record. No exhaustive priority claim is made.
