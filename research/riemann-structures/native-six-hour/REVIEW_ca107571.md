# Independent review of the single-activation packet

Reviewed freeze: `ca107571d2693e00947df8fee1860b0575fc1f97`.
Reviewer: the native structures agent, independently of the root author.
Verdict: no remaining blocker for the finite-arity and cofinal claims
stated in the packet.

I read the complete `SINGLE_NATIVE_ACTIVATION.md`, the complete
`single_native_activation.py`, and all15 tests in
`test_native_six_hour_single_activation.py`. A read-only Git comparison
showed no difference between those reviewed files and this freeze.
Their respective Git blobs are:

- `094a0a3809f5aea6013eb9b085e0290f1675ffd8`;
- `ac3175b3b00bcb0f959e57148b509867cd833893`;
- `cac221429c570db3fee8658d4fdc35a0c38a226f`.

I checked the source normalization and the complete-subset reconstruction.
For each arity the final producer enumerates all2^r subsets, records
cardinality coverage, and rebuilds every distance-matrix entry using
`W(A_i+A_j)-2A_i A_j` across cumulative cuts. This is independent of the
discovery's incidence-polynomial/distance-prefix route. The producer then
checks the displayed KKT slack in every original coordinate, rather than
accepting symmetry-reduced stationarity alone. Strict concavity from the
singleton band supplies uniqueness.

The stability proof was checked separately. Sup-norm shape error eta
changes a matrix entry by at most2r C_r eta and a gradient coordinate by
at most4r C_r eta. Doubling the error for an inactive-minus-active
comparison gives the displayed perturbation bound. The rational
epsilon threshold makes that perturbation at most mu against an
original gradient gap of at least2mu, and also keeps every frequency in
the native small-shift domain. With only one active coordinate, exact
vertex KKT requires no unproved active-face continuation argument.

The source realization is an actual monotone path: hold the central
coordinate at zero while activating the others, then activate it. Its
measure remains2ds and all factor allocations remain accounted for.
The cofinal prime construction uses fixed relative intervals one horizon
at a time; it does not invoke a uniform shrinking-interval PNT.

Executable discovery bytes are authenticated before import. The final
checks compare typed canonical JSON and reject numeric aliases and
nonfinite values. The tests cover changed matrices, missing mass,
coverage, exact thresholds at several M values, and incorrect source
pins, alongside the substantive full-arity and KKT checks.

The root reported successful producer write/check/optimized-check and
15 ordinary plus15 optimized tests. I did not execute these jobs or an
independent large-arity numerical run. My review was proof and source
inspection, including the independent reconstruction algorithm.

The result is finite-arity (2 through16) with cofinal original-kernel
consequences at11,13,15. The rejected central-three hypothesis is
retained as a discovery outcome. Neither the code nor this review
establishes an all-arity classification, an actual high-arity prime
fixture, a full retained-gamma identification, or a growing moment bound.
