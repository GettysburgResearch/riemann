# Fixed positive-shift full-support minor: preregistration

This is a new bounded experiment, declared before its first execution. The
previous fixed minor and its UNKNOWN tail results remain unchanged. The
one-sided radical theorem proves existence of some four positive shifts per
prime; it does not prove that the specific shifts selected here will pass.

Fix primes (2,3,5), shifts (1,2,3,4) at every prime, local cutoff 64 and
coefficient cap 80. There is no calibration-driven shift replacement.
Use columns (AA,AC,CA,CC), with A(z)=sqrt(1-z^2), C(z)=sqrt(1-z), their
branches equal to 1 at zero. The source proofs at frozen 822646ff and the
literal alias helper at frozen 3ba47924 are authenticated before calculation;
no predecessor executable is imported or run.

For q=1/p, the exact partial local matrix has entries

    K64[beta,(i,j)]=sum_(k=0)^64 q^k f_(i,k) f_(j,k+beta).

Only coefficients through 68 are used. The recurrence
c_0=1, c_n=c_(n-1)(2n-3)/(2n), and A's even coefficients c_(n/2)
independently reconstruct the literal square roots. Their absolute values
are at most 1. Thus every infinite local entry has error at most

    t_p=q^65/(1-q).

Retain every partial matrix, both exact inverse identities when nonsingular,
and each row sum of |K64^(-1)| times the constant-entry tail matrix.
Let eta_p be the maximum row sum. A singular partial matrix records
UNKNOWN_SINGULAR_PARTIAL. An eta_p>=1 records
UNKNOWN_TAIL_NOT_CONTRACTIVE. Neither outcome disproves the existential
theorem. No alternate shifts, larger cutoff, or fitted minor are attempted.

When eta_p<1, Neumann's lemma gives

    ||K_infinity^(-1)||_infinity
        <= B_p=||K64^(-1)||_infinity/(1-eta_p).

Retain this exact rational B_p and also its exact integer ceiling. If all
three local comparisons pass, their Kronecker matrix has 64 rows indexed by
beta in {1,2,3,4}^3 and inverse norm at most B=product_p ceil(B_p).
The outward integer rounding avoids needless denominator growth in the
global threshold; it is not a numerical approximation.
The physical frequency is 1/b, b=2^beta_1 3^beta_2 5^beta_3; every row has
full prime support. The row matrix here is unscaled: the actual physical
frequency coefficient has the additional nonzero factor 1/sqrt(b).

The tensor coordinates are also declared explicitly. If v_orig is the
original monomial-schedule coefficient vector and v_AC is the (A,C)
coefficient vector, then v_orig=T v_AC, with
T=[[1,0],[-1,1]] tensor power 3. Thus the original current matrix
M_ab=2 integral d(u^a) u^b becomes M_AC=T^t M T in the row matrix tested
here. Equivalently its entries are 2 integral d(psi_a) psi_b, where the
local schedule basis is psi=(1-u,u) and the global basis is its tensor
product. This is an invertible fixed coordinate change, not a change in
the literal current or its physical observation.

For completeness, this yields an explicit all-future finite-horizon bound,
without assuming the old fixed minor is usable. In the (A,C) tensor basis,
the total unweighted coefficient-vector l1 sum is S=4^3=64, because each
of A and C has absolute coefficient sum 2. Each omitted alias d^2 b>H
in a matrix entry has weight 1/d<sqrt(b/H). Absolute summation bounds an
entry's error by S^2 sqrt(b/H). As b<=30^4=810000, the 64-row infinity
norm error is at most

    L/sqrt(H),  L=64*900*64^2=235929600.

Choose the exact integer H0=floor((2BL)^2)+1. For every integer H>=H0,
||K_infinity^(-1)(K_H-K_infinity)||_infinity<1/2. This proves the full
64-dimensional unscaled tensor minor is invertible there. Nonzero physical
row rescaling preserves rank; restricting to the literal 20-dimensional
three-prime current-variation space gives an injective observation. This
does not identify 20 particular rows, improve the old minor, or claim an
energy minimum or full retained-gamma decoder.

Resource contract: root-serialized 128 MiB worker and 2 GiB free-memory
reserve, fixed dimensions 4 locally and 64 only for row labels, no materialized
64 by 64 rational inverse. Stored rational inputs, normalized elimination
rows, inverse products and result fractions have a 4096-bit guard; this is
not an instrumented bound on every transient arithmetic operation. Maximum
artifact size is 2 MiB. Cap refusals raise an explicit execution error and
are distinct from mathematical UNKNOWN. The output binds all four owned
source files and frozen predecessor blobs; checks compare strict canonical
JSON, so bool/float aliases cannot pass as integer data. The raw JSON parser
also rejects duplicate keys at every nesting depth, float/exponent tokens,
and nonfinite constants before they can be overwritten or coerced.

This declaration contains no acquisition result.
