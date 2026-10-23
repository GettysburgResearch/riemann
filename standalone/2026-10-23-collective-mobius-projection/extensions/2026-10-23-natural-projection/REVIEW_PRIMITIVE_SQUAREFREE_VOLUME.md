# Review of the squarefree primitive volume extension

23 October 2026. Reviewer: type_i_gain. This receipt binds
`../two-hour-boundary-20261023/COHERENT_PRIMITIVE_VOLUME_SQUAREFREE.md`,
SHA256 `5c94ecba69197b8f129d47b5891d7a2d0adcd1835dd39778b3f03ed68e03f5ed`.
It also uses the frozen coherent primitive theorem at
`bb321aae05c906187371ea7cd7a01062b19f0c0a2d889b3106c4d6e48eaaeca4`
and retained-support lemma at
`499e1333611699c91a6c3b2cf5376f5b702bca74254b222bab47fdc93043f1dc`.

I read the complete final note and the two stated inputs. No additional
gap was found in this extension, conditional on their stated analytic
inputs and exact coefficient family. I co-derived some of the local
tables and the high-range repair; this is an independent check of their
final assembly, not an independent discovery of every ingredient.

The low-divisor calculation retains the physical support in the sieve.
Summing the positive d0 amplitude through its actual cutoff produces
the stated D^(-1/12) K^(5/12) U^(5/12) mixed amplitude. Its square is
at most U in the claimed parameter range. The selected inside-modulus
weights are only logarithmically summable in their limiting branch;
the allowed subpower, not absolute convergence at that endpoint,
accounts for this.

The original-only range requires a different exact grouping. With
w=e*d0 and r=w^2*c0, the identity d^2*c=f^6*r makes the physical test
independent of the partition of w. The free length depends on its
dyad; the partitions and the empty-head condition remain column
coefficients and restrictions. This licenses the common-row estimate
without replacing the physical Möbius coefficient. Its mixed cost
K^2*sqrt(U) is at most U because U>=sqrt(DK) and K^7<=D imply U>=K^4.

I also checked the nonvolume part of that same grouping. Summation
over w-dyads followed by the ideal k split at sqrt(B_*) gives
sum k^(-3/2) min(1,(B_*/k^2)^(-5/12)) << B_*^(-1/4).
Applying this with B_*/f changes f^(-29/12) to f^(-13/6).
The resulting D, K, P, G, S powers are precisely the middle CP bound.
For B_*<1 the convergent full k-sum is smaller than the displayed
upper bound. The plateau k^(-1) sum is finite by original support;
there is no claim that its infinite series converges. The exact
subunit pole tails remain those of the frozen CP argument.

The small-U assertion follows from the already proved primitive
finite-minus-whole-pole estimate. The all-scale label denominator
closure is compatible with U replacing KU, since its scale shift
only decreases this term and preserves the scale-uniform remainder.

Thus the reviewed conclusion is

    sum_(R squarefree, NR<=K) |P_R(U)|^2
      << (UDKNQ)^epsilon [U + D^(11/12)K^(1/12) + D^(5/6)K^(7/6)]

for K<=D^(1/7), U>=1, with the fixed profiles and zeros of the input.
The sixth-power-free extension of this new volume treatment is not
claimed. The projection consumer additionally needs its stated Gram
range and whole-pole term. At U=D^(6/7), K=D^(1/10), its largest
exponent is 20/21. This does not bound the complementary inverse
vector, improve B_flat, or establish RH.
