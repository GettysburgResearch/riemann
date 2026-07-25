# Cross-height Arb production request

This child revision exists solely to trigger `.github/workflows/arb-cross-height-pick.yml` from a base branch that already contains and reviews that workflow.

Requested finite computation:

- 428 exact dyadic primitive `xi'/xi` points;
- 208 exact Gaussian-rational cross-height Pick packet channels;
- Python-FLINT/Arb primitive rectangles at 160 and 224 bits;
- exact standard-library contraction of real and imaginary rectangles;
- strict sign classification for every channel;
- exact interval nesting across the precision ladder;
- uploaded certificates, verification files, compact summaries, timings, and SHA-256 ledger.

No counterexample is asserted by this trigger. A negative directed upper endpoint would be a rigorous nomination pending independent directed reproduction and review of D-3201/L-3202/L-3905.
