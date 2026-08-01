# Source-bound DIRECTED_INTERVAL_ODE production prefix

## Result

A parameterized emitter produced source-bound CCM/prolate primitives at

- gamma = 4096,
- gamma = 32768,
- gamma = 262144,

with modes 0, 4, 8, 12. Each primitive includes directed angular separation
intervals, regular pole Cauchy boxes, transition and residual ledgers,
horizontal-strip companion bounds, tail-energy charges, a p=4 endpoint ledger,
exact repaired-source definitions, and SHA-256 bindings.

The unchanged X-16204 consumer accepts all three wrappers byte-for-byte on
replay. The retained consumer proof-object digests are listed in
`cofinal-prefix.json`.

## Rigorous components

- separation upper endpoints: Rayleigh--Ritz plus directed Sturm count;
- separation lower endpoints: Schur tail floor plus directed Sturm count;
- pole data: Arb Frobenius evaluation plus rational parameter/truncation majorants;
- repaired sources: determinant formulas imposing both CCM source constraints;
- transition bound: explicit L-16229 potential/interaction ledger;
- digests: producer, source, primitive, wrapper, consumer result.

## Exact remaining blocker

Consumer acceptance is structural, not yet a complete production scalarization
certificate. The retained radial and derivative tails were conservatively
charged by full normalized energies, and the endpoint derivative-L1 ceiling was
intentionally loose. The next emitter revision must replace those fields by
source-derived repaired-packet bounds and bind them directly into the
deterministic-error and profile-Gram ledgers.

Until then, the three blocks are a real source-bound cofinal prefix and an
emitter/consumer integration result, not a proof of RH.
