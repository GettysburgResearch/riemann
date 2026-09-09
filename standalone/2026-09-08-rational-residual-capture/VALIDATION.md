# Validation and trust boundaries

The accepting program uses Python's standard library, integer arithmetic and
Fraction only. It does not call numerical log/trigonometric, zeta, gamma,
digamma, linear-algebra or optimization libraries. Numerical decimal output
is directed integer division of exact rational endpoints. Large internal
rational solutions are fingerprinted in hexadecimal, avoiding Python's
large-decimal-string conversion limit; their stationarity is checked exactly.

The final commands and results are recorded in the accompanying delivery
execution receipt. The packet commands are:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py --part 1
    python -I -S -B test_rejections.py --part 2
    python -I -S -B -O test_rejections.py --part 1
    python -I -S -B -O test_rejections.py --part 2

There are 841 bounded panels in eleven named groups. These include 256
independent Mobius sieve/trial-factor comparisons, 144 CRT pairs, 128 Jordan
identities, twelve complete small-period means, 144 finite block checks,
36 independent exact-period tail-bracket controls, 23 actual centered prefix
constructions, eighteen jet-preserving correction panels, fourteen bare-cutoff
false-zero controls, 63 Farey-spacing/rank-horizon panels, and THREE global
finite-support minimum brackets. Counts are bounded checks, not analytic
proofs or independent-theorem counts.

The three finite minima use Y=2,3,4, N=4Y and H=4096. The code constructs
both bounding quadratic forms from all H-1 integer cells and the complete
Jordan-totient covariance. It solves both finite rational problems (and the
middle problem), checks exact stationarity/feasibility, and rounds the
resulting lower/upper rational bounds outward. It does NOT evaluate a
truncated norm and silently call it complete. Analytic justification of the
infinite remainder and of global minimality is in PROOF.md.

These new numerical classes impose p(1)=0 ONLY. They do not impose the
parent's p'(1)=1, or the optional p(0)=-2. They therefore are not direct
improvements of the earlier four minimum certificates. The universal form
theorem covers the earlier classes as well, but those constrained producers
have not been rerun here.

Nine deliberate mutations are checked through the actual CLI in each mode:
false RH, false subpower, Boolean/numeric alias, changed minimum, duplicate
JSON, changed proof bytes, missing checksum, a resealed extra file, and wrong
locked parent. Semantic result mutations are resealed so that reconstruction,
not merely checksum failure, rejects them. Each partition has a pristine copied
packet control (two per mode). Integrity refusals do not demonstrate the falsity of an
arbitrary modified mathematical proof.

The exact nine-file inventory and eight SHA256 entries authenticate the
packet. Source metadata bind the two locally available parent manuscripts
to their verified Git blobs and SHA256 values. New code does not load or
execute parent code. There is no parent-suite replay, remote CI claim, full
repository checkout/build, Lean/kernel proof, zero table, continuum quadrature,
large-cutoff campaign, or independent referee acceptance.

Development history: exploratory prototype code initially attempted a decimal
string conversion of an exact rational numerator exceeding Python's 4300-digit
limit. That diagnostic invocation failed before producing its intended panel.
The final verifier uses hex fingerprints and does not disable the runtime
limit. The exploratory floats were display-only and were not used as proof
inputs or accepted intervals. Initial prototype runs are not counted as the
final sealed executions.
