# X-105210 light replay

This standard-library replay verifies only:

- the final rational rearrangement;
- the sixfold gap-overlap conversion;
- the block reverse–Rolle algebra;
- numerical fixtures for the 90% conditional gate;
- fail-closed status flags.

It does **not** rerun the external Arb subdivision certificate. The finite
certificate is pinned by source commit and must be replayed separately in its
native repository.
