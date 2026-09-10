# Execution and independent-review boundary

Date: 2026-09-07. Arithmetic: Python standard-library integer/Fraction
calculations, including outward rational atanh-series log intervals.

The new checker performs eight named groups, totaling 1,119 bounded cases
per mode. Most are the 1,024 integer-pair phase identities; these are not
1,119 independent analytic theorems. Normal and optimized outputs match.
Six finite Gram matrices have exact positive rational LDL pivots. The prime
2/3 covariance and indefinite difference are exact rational calculations.
The 35 convex-jump tests and 20 full-log-jump tests use complete log interval
remainders, not binary floating point. The prime harmonic comparison is
sampled at eight fixed endpoints; its all-X proof is in PROOF.md, not in
these samples. Likewise the all-packet domination obstruction is proved
analytically; bounded checks do not supply its unbounded quantifier.

Commands:

    python checks.py > checks.normal.json
    python -O checks.py > checks.optimized.json
    python checks.py --check checks.normal.json
    python -O checks.py --check checks.optimized.json
    python validate.py
    python -O validate.py
    python rejections.py

The actual checker CLI rejects six altered results per mode, including a
false RH flag, false work-bound flag, bool/integer alias, altered covariance,
floating numeric alias, and duplicate JSON key. The actual package validator
rejects a changed proof, missing claim ledger, and extra file per mode.
An initial combined rejection command hit its execution timeout and is not
counted as completed. The final normal/optimized partitions completed.
Pristine result checks pass in both modes. The sealed result is in
rejections.json. Hash validation is an inventory/byte contract, not proof of
analytic truth or authentication of an external repository by itself.

The downloaded parent manuscript bytes match the declared Git blob and SHA256
pins. Parent mathematical suites were NOT rerun. No new zero census, Lean,
Comparator, external PNT computation, or independent referee acceptance is
claimed. The conditional RH ending uses the source identities proved in the
parent and reconstructs its zero argument; it does not prove the work premise.

Exploratory computation, not proof: an early SciPy quadrature over a wide
single interval returned zero for E(2), missing its small central positive
region. Pointwise checking exposed this; that output was discarded and is
not retained as evidence. PROOF.md instead proves E(2)>1/20 analytically.
Other exploratory floating values were not used in any inequality or cutoff
claim. No numerical entropy or work integral is certified in this packet.

Publication validation will compare the newly created Git subtree with the
local tree and all its blob identities. Publication does not promote the
component claims to independent acceptance. The complete remaining work
bound and RH are explicitly OPEN in README, PROOF, ATTEMPT, CLOSURE and
CLAIMS; no finite check is labelled as their proof.
