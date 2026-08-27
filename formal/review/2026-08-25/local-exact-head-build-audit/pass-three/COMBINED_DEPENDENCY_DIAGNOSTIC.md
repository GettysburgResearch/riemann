# Combined dependency diagnostic

The first disposable combined attempt had a runner preflight working-directory
error. A later attempt saw transient pinned-dependency sidecar/resource
failures, including `std::bad_alloc`; it made no manifest or source change.

The final runner first verified dependency sidecars byte-for-byte against the
green C cache, restored the committed cache without downloads, and explicitly
built:

- `Zeta23.Hypotheses`;
- `Zeta23.GammaFacts`;
- `Zeta23.Defs.Counting`;
- `Zeta23.FromPNTPlus.StrongPNTPrefix`.

All four passed. The subsequent 8,806-job aggregate build and every downstream
validation also passed. The committed manifest remained unchanged throughout.

Final classification: `PASS`; earlier attempts are retained as diagnostic
evidence, not silently discarded.
