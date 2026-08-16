# X-91880 — live arithmetic coupling stress test

This lightweight replay performs:

- the exact PR #503 negative infinitesimal witness;
- a rational-interval positive finite-Q witness with a rational moat at the same parameters;
- an actual Möbius bulk Hall fibre at `(X,s,x)=(3600,225,16)`;
- the actual P61 Target-Lorenz leaf `(p,y)=(67,15)`, with cutoff 133;
- all rows `2..66` as a high-precision diagnostic on that leaf;
- fail-closed mutations for the source/placement/quantizer/detail/Y4 interfaces.

The replay does not replace the directed all-parameter AVLT or the analytic
all-column and endpoint-consumer proofs.
