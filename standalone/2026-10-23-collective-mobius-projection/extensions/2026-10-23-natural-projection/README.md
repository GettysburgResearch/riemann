# Natural-length primitive projection: final additive research packet

Status: proposed, source-dependent mathematics with internal reviews.
This is the latest extension of PR1019. Earlier source files remain frozen.
The preceding coherent-support extension supplies the imported definitions,
source pins, physical-support estimate and full-series proofs. The original
parent packet supplies PR1013/1015 imports and its source-identity erratum.

For the actual normalized Möbius coefficient, fixed smooth/ray profiles,
literal zeros and the punctures specified in the proofs, the squarefree-label
primitive projection satisfies

    ||P_K A_U bar(b)||^2
       << ((2+U)DKNQ)^epsilon
          [U + D^(11/12)K^(1/12) + D^(5/6)K + U^(1/3)D^(2/3)],
    U>=1, 1<=K<=D^(1/7), K<=U^(1/2-delta).

At the natural label length K=D/U, this saves a fixed power against the
inherited D^(5/6)U^(1/6) resource whenever U=D^h and 6/7<h<1.
The example U=D^(7/8), K=D^(1/8) gives D^(23/24+epsilon), compared
with D^(47/48+epsilon), a 1/48 saving. The bound includes both the
continuous contribution and the entire pole of the specified projection.

Read `NATURAL_LABEL_PRIMITIVE_PROJECTION.md` for the final argument.
Its main new inputs are:

- `COHERENT_PRIMITIVE_VOLUME_SQUAREFREE.md`: aggregates the actual
  inverse rows in both the nonempty-head and empty-head ranges, replacing
  KU by U. The empty-head range was essential; omitting it was rejected.
- `FIXED_PROGRESSION_RESIDUE_VECTOR.md`: proves a coherent residue bound
  for fixed progressions. Its primitive consumer is explicitly conditional
  within that note. Section 1 of the final natural-label proof supplies
  the missing fixed-puncture identity, without deleting a moving gcd mask.
- The final proof recomputes the continuous plateau using physical local
  support, replacing K^(7/6) by K, and preserves subunit negative poles
  when restoring the label-supported denominator.

The separate global, type and root reviews bind the exact final proof
hash. Authorship overlaps and co-derived ingredients are disclosed in
each receipt. These are internal checks, not external human peer review,
formal verification or repository integration approval. The functional
equation, inverse estimate, large sieve, density identities and Gram
theorem remain explicitly identified analytic imports.

Two finite checkers pass in isolated ordinary and optimized Python with
identical output: 168 exact rational predicates in total. They include
negative controls on invalid ranges and authenticate finite exponent
algebra only. `COMPONENT_MANIFEST.json` binds ten source components.
`FINITE_REPLAY.json` records the outputs. A subsequent review-only commit
may attach the exact mathematical-commit audit.

The orthogonal complement remains uncontrolled. In particular, an upper
bound for this projection cannot be subtracted from an upper bound for
the total norm to obtain a complementary saving. The next missing
estimate is a matching power saving for `(I-P_K) A_U bar(b)` in the
actual signed first-Poisson return. No smaller B_flat, new global
zero-free half-plane, or RH proof is asserted by this packet.
