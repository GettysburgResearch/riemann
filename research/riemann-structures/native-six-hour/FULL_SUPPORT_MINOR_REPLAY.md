# Fixed full-support minor replay

Candidate only: no execution or successful local comparison is claimed in
this file. The root owns all computation and resource gating.

Owned files are `native_full_support_minor.py`,
`FULL_SUPPORT_MINOR_PREREGISTRATION.md`, this note, and
`tests/test_native_six_hour_full_support_minor.py`. The proposed output is
`native_full_support_minor.verification.json`. The preregistration gives the
complete proof of the local tail and any conditional global threshold.

The producer authenticates frozen source bytes, reconstructs the square-root
coefficients independently, computes the three fixed 4 by 4 matrices, checks
both inverse identities, and retains each local PASS or UNKNOWN. All 64
full-support denominator labels are recorded. An all-future threshold is
emitted only when all three strict local comparisons pass. This is a new
minor in a declared (A,C) tensor basis; the original physical 1/sqrt(b)
scaling and literal path-current factor 2 remain explicit.

The twelve controls cover literal source identities, exact coefficient
prefix and parity, nonconstant q/orientation in a direct Laurent product,
geometric tails, both inverse identities, singular and noncontractive
UNKNOWN branches, strict threshold rounding, immutable fixed panel labels,
coefficient/dimension/bit guards, and typed JSON counterfeits, including
raw duplicate keys and float/nonfinite number tokens. They do not
assume the three actual comparisons will succeed.

Root commands, under the preregistered guards:

    python research/riemann-structures/native-six-hour/native_full_support_minor.py --write
    python research/riemann-structures/native-six-hour/native_full_support_minor.py --check
    python -O research/riemann-structures/native-six-hour/native_full_support_minor.py --check
    python -m unittest discover -s tests -p test_native_six_hour_full_support_minor.py
    python -O -m unittest discover -s tests -p test_native_six_hour_full_support_minor.py

The former fixed-minor acquisition and acceptance contracts are untouched.
