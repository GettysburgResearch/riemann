# DSE27 — complete native-energy certificates, not another isolated diagonal

**Proposed research; independent mathematical review required. RH and the
native unbounded energy gain remain open.** Continuation of #902, stacked on
#848 at `617cfaca6130addd2d16bbce6af117a55aef761b`.

Read [PROOF.md](PROOF.md) first. This pass adds three concrete components.

1. **Prime-mode cancellation.** An exact rational Fourier decomposition of the
   physical Newton output has B_p=-(sum_(p|n)c(n)/n)^2 at every prime denominator.
   The entire combined prime-denominator contribution has annular energy at
   most K^4 H_L^6/(4b) for a balanced source capped by K. At native reciprocal
   crossings this improves to 81 H_b^2/(4b), using the actual inverse equations.
   These are ALL prime denominators, not just a small prime bank. Composite
   modes, the constant, the collar and their mixed terms remain.
2. **Critical-mesh error bound.** From exact Mertens values on a square-root-
   spaced mesh, a nearest-sample step function with energy S gives a full
   interval enclosure (sqrt(S)-sqrt(Z))_+^2 <= I <= (sqrt(S)+sqrt(Z))^2.
   The entire between-sample error Z is explicitly rational and logarithmic.
   A coarser mesh can hide power-sized energy for bounded fake sources.
3. **A complete finite native certificate.** Starting with mu through Y=4095,
   exact divisor recurrence generates 16,129 samples and certifies
   E_(16777215)<2.96907798291454<3, covering all 16,773,120 new cells.
   A separately run full-length sieve checks every sample and gives the
   sharper independent full energy 1.7465305178196... to 1.7465305178206....

The finite E-energy square-ladder gain is certified at Y=4095 (also Y=1023).
This is not verification of every smaller stage, an asymptotic gain, a new
zero-verification record, or a bound on the original finite A/F quantities.
The short-prefix sample recurrence uses no future Mobius values; the second
full-sieve comparison deliberately DOES compute them as an independent check.

## Reproduce

Python 3.10+ and a GNU/Clang-compatible C++17 compiler are sufficient; no Python
packages or numerical zeta library are used. C++ uses the compiler-supported
unsigned __int128 extension. Linux/GCC was tested; MSVC/native Windows was not.

From this directory:

```sh
python -B test_check.py
python -O -B test_check.py
python -B check.py --Y 1023 --check result_1023.json
python -O -B check.py --Y 1023 --check result_1023.json

g++ -std=c++17 -O2 -Wall -Wextra -Wconversion native.cpp -o native
python -B check.py --Y 4095 --engine ./native --full-check --check result_4095.json
python -O -B check.py --Y 4095 --engine ./native --full-check --check result_4095.json
```

Without --engine the same interface uses an exact pure-Python recurrence.
The largest pure-Python run was interrupted by the session's execution limit;
use the compiled engine for the published large replay. Sample count is not a
sublinear runtime claim. The compiled source and the full sieve perform more
arithmetic than the number of retained samples.

`result_1023.json` and `result_4095.json` store outward integer endpoints in
units of 2^-112. No rounded decimal is an accepting input. The independent
full sieve uses separate 64-bit fractional precision with exact 128-bit
integer divisions and outward endpoints. `check.py` requires that its full
energy enclosure be contained in the sparse one.

## Why this is not simply the previous partition

RCB26 grouped integer PRODUCTS by rough parity core in reciprocal-innovation
coordinates. Here the primary norm is

    E_X=sum_(k<=X) M(k)^2/[k(k+1)].

The Fourier labels are reduced rational denominators of periodic physical
kernels, not product cores, and not Nyman-Beurling basis denominators. No
prime-power support theorem is contradicted. B_4=+1 in the supplied balanced
control, while B_2=-1: the prime identity cannot be generalized by relabeling.

The floor(j^2/16) mesh decomposes into sixteen exact quadratic progressions.
This exposes a weighted quadratic-phase covariance with source-defined B_q.
Its diagonal is not the answer: even the mean of e(n^2/4) is nonzero. The
complete constant and composite sectors must be controlled without an
unproved orthogonality or a family-to-member inference.

## What should happen next

The selected arithmetic programme remains #902. The next analytic target is
an upper estimate for the retained COMPOSITE-mode covariance, using its
actual divisor-derived amplitudes. A generic quadratic large-sieve slogan is
not an adapter. The critical-mesh error has been paid; the native values on
the mesh have not been bounded at arbitrary scale.

This pass provides a source-complete finite test and one more rigorously paid
sector. It did not deliver the all-scale native gain sought in the strategy
brief. That limit should survive every summary of this PR.

See [SOURCES.json](SOURCES.json) for exact reading scope and overlap and
[VALIDATION.md](VALIDATION.md) for executed versus unexecuted checks. Prior
manuscripts, main, accepted claims, formal sources and workflows are unchanged.
