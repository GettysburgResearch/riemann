# Primitive-twist Type-I cancellation: beyond the pure cubic block

20 October 2026. **PROPOSED source-dependent analytic proof and exact
finite checks. No new zeta or L-function zero-free boundary is proved.**

This packet pursues the correlated-moment route to a numerical boundary
improvement. It extends the pure cubic/angular block in PR #1009 to
primitive finite twists, including a genuine quadratic component, and
keeps the conductor cost that prevents an immediate full-moment claim.

## Main contribution

For a primitive character psi modulo a squarefree Eisenstein modulus c,
put c=c0*c1, where psi_p cancels the cubic character at primes of c0 and
does not at primes of c1. Let Cj=N(cj). Given the stated common zero-free
input at beta for the completion character psi^3 alpha^(3ell), the
[proposed proof](PROOF.md) obtains

    sum_u g_tilde(u) psi(u) alpha(u)^ell W(Nu/X)
       = explicit possible main term
         + O((X Nc)^epsilon X^p C0^q C1^(2q)),
    p=(2 beta+1)/6, q=(5-2 beta)/12.

The main term is absent whenever c1!=1, including angular degree ell=0.
At ell=0, Liu's finite-order theorem supplies the beta=B_flat input;
the proposed infinite-order extension in #1009 is not needed here.
For sixth-order psi the completion is quadratic or principal.

The important new calculation is the exact local transform: nonmatching
primes kill the zero-frequency term but have Gauss mass Q, not sqrt(Q).
Their cost therefore doubles in the effective level K=C0*C1^2. The proof
includes every local cube power and zero-only coprimality mask.

A coherent bounded short-divisor mark, including a Mobius mark, satisfies

    |T| << (AB Nc Nm)^epsilon A^p B^(1+q) C0^q C1^(2q).

For example, Y=AB, B=Y^(1/4), C0 fixed and C1<=Y^(3/10) give
Y^(791/960+epsilon) using beta=7/8. This is below Y^(5/6) by the power
3/320; the same Euler-only baseline has exponent 67/80>5/6.
**791/960 is a sum exponent, not a new zero-free boundary.**
[MIXED_SCOPE.md](MIXED_SCOPE.md) gives the precise gain and remaining gap.

## Status and review

The transfer proof uses Dunn--Radziwill's general periodic-twist functional
equation, not their GRH-dependent prime theorems. Its generalized cubic
completion is derived rather than asserted from their cubic-only lemma.
Liu's zero-free theorem is an imported preprint input, not independently
reconstructed in this packet. There has been no independent human or
separate-agent review, formal analytic verification, or integration approval.

The complete U^(6/5) mixed norm, its long-inverse edge and its large
nonmatching-conductor remainder remain open. The present result does not
establish the repo's conditional 0.874 target, improve B_flat for already
covered L-functions, or prove RH. No literature-wide priority is claimed.

## Reproduction

    python -I -S -B verify.py
    python -I -S -B -O verify.py

Both give [REPLAY.json](REPLAY.json). The exact checker verifies 1,983
local transform identities for 87 characters over six finite fields,
198 additional unit-phase identities, 87 Gauss norms, cube inversion,
conductor exponents and a rational quartic-root isolation. Three deliberate
errors are rejected in both ordinary and optimized Python. These checks
validate finite algebra, not the global analytic proof.
See [VALIDATION.md](VALIDATION.md) and [SOURCES.json](SOURCES.json).

Publication is confined to this new standalone directory on its own
research branch. Existing research branches and main are unchanged.
