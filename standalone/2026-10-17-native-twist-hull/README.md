# Native twist hull: stop treating the averaging price as removable

**PROPOSED unconditional component mathematics, not independently reviewed.**
This continuation does not improve the fixed-principal-twist moment, the
zero-free boundary, or RH. It proves that a proposed way of upgrading #955
fails for the ORIGINAL native coefficients, not merely for changed phases.

## Main result

For a Galois number field, a nonnegative compact or Gaussian test, principal
Mobius coefficients and nonnegative masks, the supremum over Mellin-twist
CENTERS of the complete Gaussian-averaged 2k-th moment equals the unsigned
moment at center zero. It also holds for full cumulative Gaussian energies.
No ideals, cross terms, tails, or shared-prime zeros are deleted.

Thus native coefficient specificity alone cannot improve an estimate whose
constant is uniform over the whole real twist line. The unsigned vector lies
in the closure of the actual native twist orbit. This uses classical torus
approximation; a complete elementary quantitative proof is supplied rather
than a claim of novelty for Kronecker's theorem.

On actual Eisenstein sixth-power rows, for H=X^h there are native centers with

    M_k(X,H,T,t0) >= c H^(1/6) X^(2k)/(1+T).

The replica count has no prime-generator logarithmic loss: an elementary
squarefree/coprime ideal-pair density and Jensen give all H^(1/6) replicas in
aggregate. Centers can be chosen below exp(C X^2 log^2(3X)), an extremely loose
but explicit finite bound. These centers MOVE WITH X. They are coefficient
twists, not physical row heights or zero ordinates.

Uniform-center diagonal-power hypotheses consequently need a width exponent
at least k-e-5h/6 (when positive). At fourth order with no excess this is 7/6
for h=1, and 9/8 for h=21/20. A single principal scalar row needs exponent k.
The exact native cumulative Gaussian energy has supremal order D^k.

## An actual native peak, not an arbitrary prime-phase model

The complete ideal window 32<NI<=64 has native sum

    A_t=49^(it)-2*37^(it)-2*43^(it)-2*61^(it).

At t=0 it equals -5. At the INTEGER t=842800609, an exact rational Taylor
certificate encloses Re(49^(-it) A_t) in

    [6.999890106922709531522815, 6.999890106922709531522816].

The unsigned maximum is 7. This is a finite illustration, not evidence about
asymptotic growth at center zero or a certificate for the whole prime-phase box.

## Reading and replay

1. THEOREMS.md: exact hull identity, residue-degree compatibility, effective
   approximation, literal physical rows, and the remaining boundary.
2. ATTACK_AND_SOURCES.md: why the attempted upgrade fails, the newly read
   October 13 sextic-sieve obstruction, source credits and reading limits.
3. VALIDATION.md, CHECKS.json, MUTATIONS.json: exact coverage and limitations.

    python verify.py
    python -O verify.py
    python verify_manifest.py

All 4,162 finite predicates agree in both Python modes; four separately run
corrupted optimized processes fail. Counts include setup and repeated guards,
not independent asymptotic cases. The written analytic proof and checker have
the same author. No independent referee, Lean build or full-repository CI is
claimed. The prior #955 proof files and their manifest remain unchanged.

## Relation to the user's requested stronger result

A new fixed-center upper estimate was NOT obtained. This result blocks a
specific invalid route and makes the admissible next target more precise.
The unresolved task remains genuine prime/composite cancellation at a fixed
or explicitly height-controlled twist. Do not describe this obstruction as a
new RH-bearing moment bound or a general impossibility theorem for RH research.
