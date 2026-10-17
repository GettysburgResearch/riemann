# Reflected zero-free ratios: a proposed 19/21 all-field composition

Status: PROPOSED source-qualified mathematics; independent review required. NOT PUSHED in this session. No RH proof, native critical moment or accepted zero-free theorem is claimed.

The new use is simple: on a class known to be zero-free, the logarithm argument bounds BOTH L and 1/L. The functional equation reflects the Poisson numerator onto the SAME character as the denominator. The two ordinates may remain independent. This gives row cost U^(sigma-1/2+epsilon), instead of ordinary convexity's U^(sigma/2+epsilon), on that class.

At sigma=3/4 the saving is U^(1/8) in that selected-row estimate. A full 37-class composition with a=3/7 gives the proposed 19/21 boundary for Dedekind zeta functions, subject to the explicitly adopted CT/reflection/correction/family contracts. The four/eight/all-order numerator moments used in recent branches are not required for the new middle classes. Only the earlier second mean is retained for the full good class and the small-frequency range.

Read RATIO_LEMMA.md, then COMPOSITION.md. SOURCES.md lists exact pins and retrieval limits. CHECKS.json is a compact finite certificate; CERTIFICATE.json contains every class and all density monomials. Finite arithmetic is not a proof of the analytic inputs.

## Replay

    python verify.py
    python -O verify.py
    python verify.py --details
    python replay.py

The first two outputs must match CHECKS.json; the detailed output must match CERTIFICATE.json. replay.py also runs eight deliberately corrupted optimized processes and checks their intended errors, then authenticates the byte manifest. It needs only the Python standard library and does not use the network or L-function values.

## Publication boundary

Intended base: #975, edbc27b61208ccc7ee1fa99fa3f4e861f5a03452.
Intended branch: research/reflected-zero-free-ratio-20261018.
Intended directory: standalone/2026-10-18-reflected-ratio/.

The current GitHub connector exposed read actions only; create/push actions were not available after discovery. GitHub reads succeeded. A direct container DNS/network check failed, and no configured Git credential helper or gh executable was available. No remote branch, commit or PR was created. The accompanying add-only Git patch was checked in a fresh local fixture; it changes no inherited files.

The previous #975 source is already published. No unseen or unavailable work from other crashed conversations is claimed recovered.
