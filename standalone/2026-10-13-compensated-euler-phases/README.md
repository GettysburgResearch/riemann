# Compensated macroscopic phases: a stable alternative to prime freezing

**PROPOSED component mathematics. No full generalized moment, new zero-free
boundary, or RH proof. No independent mathematical review.**

This continuation reads #938, #940--#943 and the #939 completion proof. It
replaces the failed uncompleted prime-count deformation by an explicit Euler
compensation. The complete proof is [PROOF.md](PROOF.md).

For every good prime use

    F_z(x)=(1-z*x)(1-x)^(1-z) exp((z^2-z)*x^2/2), |z|<=1.

It has exactly the native coefficients at primes and prime squares. Its
ratio to 1-x, and the inverse ratio, have coefficient absolute mass less
than e^2 at the square-root normalization. This gives a **scale-independent,
all-order, two-way comparison** of the native and completed physical moment
norm envelopes. Every shorter column uses the SAME physical rows and masks.

Full unit-circle averaging is unbiased. Its 2k-th moment equals the native
moment plus an explicit nonnegative sum of holomorphic coefficient energies.
The raw phase model's shrinking-width barrier is avoided by changing the
nonsquarefree completion, not by disproving that barrier. For phases active
only above D^(1/4), the completed polynomial differs from the native one by
O(sqrt(D)) on every row. That gives a direct fixed-scale moment equivalence.

**What remains:** the native constant phase mode is unknown. Randomness in
prime-cube and higher corrections does not estimate it. The completion's
analytic multiplier is nonzero to the right of 1/3 and therefore preserves
all genuine inverse-L singularities there. This packet repairs a deformation
and states the exact remaining estimate; it does not improve its exponent.

## Exact finite results

All good ideal columns in each hard window and all nonzero Eisenstein rows
in each listed norm ball are included. The circle integral is exact Parseval,
not a sampled approximation. Six scales D=256,...,8192 were recomputed at
H=ceil(D^(21/20)); moment orders 2,4,6,8 are in [results.json](results.json).

At D=8192, H=12855, all 46,608 rows and 1,145 native squarefree columns give

    native fourth moment       114923460372
    compensated circle moment  1037951373508/9
    nonnegative excess         3640230160/9.

There are 1,155 nonzero completed columns. The excess is about 0.352% of the
native value; this is a finite diagnostic, not an asymptotic estimate. All
zero-excess cases and the larger relative excess at D=512 are retained.

Run `python verify_completion.py --output replay.json` and repeat with
`python -O`; compare both with results.json. NumPy is used only for guarded
integer row arrays. [VALIDATION.md](VALIDATION.md) records coverage, arithmetic,
source adaptation, and review limits; [SOURCES.md](SOURCES.md) credits overlap.
