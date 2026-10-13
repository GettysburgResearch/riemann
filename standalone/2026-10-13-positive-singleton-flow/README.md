# A positive, compensated singleton flow

**PROPOSED component mathematics. No improved zero-free boundary, full native
fourth moment, cofinal native hierarchy, or RH proof. No independent review.**

This continuation of #940 uses Mammen's classical two-point wild-bootstrap
multiplier to retain third occurrences while removing singletons. A particular
positive Peano kernel turns prime restoration into an exact signed injection
minus a coercive nonnegative remainder, at every fixed even order.

Read [MATHEMATICS.md](MATHEMATICS.md) for all proofs and quantifiers, then
[VALIDATION.md](VALIDATION.md) for the precise finite coverage and limitations.

## The concrete change of mechanism

For the classical law

    Z=(1+sqrt(5))/2 with probability (1-1/sqrt(5))/2,
    Z=(1-sqrt(5))/2 otherwise,

one has E Z=0, E Z^2=E Z^3=1, E Z^4=2. Thus at order four it deletes a
singleton, keeps double and triple occurrences unchanged, and doubles only
fourfold occurrences. The law and its minimum-fourth-moment property are
classical, explicitly credited; the native application is the present proposal.

The exact local identity is

    |U+V|^4 = E|U+ZV|^4 + 4|U|^2 Re(U conjugate(V)) - |V|^4.

For every integer k>=2, the analogous remainder R_k is nonnegative and obeys

    R_k(U,V) >= [(2k)_4/24]*(8/75)^(k-2)*|V|^(2k).

The written proof gives a nonnegative, explicit Peano kernel on
[(1-sqrt(5))/2,(1+sqrt(5))/2]. Its normalized variance is exactly 8/75.
At the sixth moment, the sharp uniform lower coefficient from this argument
is 8/5. This is not positivity of the original singleton covariance.

## Positive reference, original endpoint

Attach independent multipliers only to prime ideals above (log X)^2. Leave
all actual Mobius signs, sextic phases, exclusions and nonunit zeros in place.
The resulting positive reference G has every fixed moment at diagonal size,
G << H X^(k+epsilon). Its 2k-th root also has the explicit X^(1/2+o(1)) bound
uniformly for k<=log X. This is a RANDOMIZED reference theorem.

Its difference from the larger smooth-singleton sector of #940 starts only
at prime occurrence four. Section 5 quantifies that difference and gives an
exact two-way, mask-preserving common-divisor identity at the fourth moment.

Restore the remaining multipliers to 1, in any fixed order. The complete
original moment is exactly

    M_(2k)=G+I_k-D_k,       D_k>=0.

I_k is the full signed first-derivative sum; D_k is the sum of the positive
local remainders. At k=2 it is the actual cofactor fourth-energy sum. Each
cofactor keeps its original scale D/Np, moving exclusion, all composite terms,
and the same physical row. No assumed independence of U and V is used.

The new one-sided target is

    I_2 <= D_2+C_epsilon H D^(2+epsilon).

It is OPEN and equivalent to the missing full moment up to the proved bounded
reference. The old target is not solved or made easier merely by this identity.
The useful new structure is the explicit compensating energy that may be kept
while estimating the signed prime/cofactor sum.

## Finite checks: all columns and all rows in the declared cases

The complete hard-window census (D/2<Nn<=D, 0<Nu<=ceil(D^(21/20))) gives:

| D | frozen prime norm cap | reference G | signed injection I_2 | D_2 | native M4 |
|---:|---:|---:|---:|---:|---:|
|64|17|25,704|2,496|1,728|26,472|
|128|23|381,876|-13,392|8,820|359,664|
|256|30|2,953,074|106,608|38,436|3,021,246|

The native moments match #943's values; they are not claimed as new records.
At D=256 all 37 squarefree good columns and all 1,236 nonzero rows are included.
The safe-cutoff input integers are specified explicitly; no asymptotic claim
is inferred from approximating logarithms in these finite tests.

A fourth case D=128 with no frozen good primes confirms genuine order dependence:
ascending restoration gives (I_2,D_2)=(-23,400,21,288), while descending gives
(-23,352,21,336). The difference I_2-D_2 is identical. Both positive and negative
individual steps occur. Ordering alone cannot improve the endpoint.

The checker also tests the local inequalities at orders 4 through 20 on
625 complex pairs and directly enumerates the irrational two-point atoms in
192 auxiliary three-coordinate models. The complete diagnostic passes 235,666
explicit predicates, including repeated setup and unit-block zero tests.
Ordinary and optimized Python reproduce results.json byte for byte.

## What is and is not published

This packet adds only its own directory on top of #940 at
59d5a8ebcd390ff898d63b2fc5ed7290995ae58b. It leaves all inherited mathematics and
the integrated record unchanged. It does not claim independent review, a Lean
build, remote CI, or a replay of the imported theta framework. The entire
native signed injection remains the arithmetic obstacle. The inherited
17/24 extraction retains all its original test, twist and height hypotheses.
