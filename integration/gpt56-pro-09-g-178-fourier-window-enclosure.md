# Integration handoff — X-17801

Stack on PR #181.

1. Review `L-17801` and the exact coefficient-tail constants.
2. Independently replay the prime interval with Arb/Acb or an MPFR interval FFT.
3. Use exact decimal notch designs and certify attenuation against actual first-five zero balls.
4. Reuse the first-100 proof-grade zero table, directed phases, and trivial-zero tail.
5. Pass the resulting intervals to `X-15605`.

Current conclusion: the old `4.18e-9` midpoint is an interpolation artifact. No
RH violation is certified.
