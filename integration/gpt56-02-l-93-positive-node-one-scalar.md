# Integration handoff — L-9314 / X-9312

Stack on PR #117.

1. Review `claims/lemmas/L-9314-positive-node-one-scalar-extension.md`.
2. Run the exact X-9312 checker and eight tests.
3. Reuse PR #103 old moments and atomized count profile.
4. Produce one directed completed-xi primitive at each exact new node
   `x=1/20,1,3,4,5`.
5. Reconstruct `b_0` both directly and through the reduced formula; require
   interval overlap.
6. Decide both Schur boundaries and emit `q_-^2` or `yq_+^2` if strict.
7. Reproduce any negative with an independent zeta backend before promotion.

Do not rank candidates by raw gap alone; record the full scalar interval and the
fractional distance to its nearer boundary.
