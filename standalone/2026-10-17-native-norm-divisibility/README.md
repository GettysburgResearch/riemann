# Native fixed-center norm-divisibility covariance

**Proposed complete unconditional component proofs; independent review pending.**
No full critical energy upper bound, moment exponent improvement, or RH proof.
No new remote branch, commit or PR was created in this session.

The source is the actual principal ideal Mobius function over Q(omega), with
exactly the prime ideals over 2 and 3 excluded, and the full Gaussian W_c.
There is no deformation of the coefficients and no average over Mellin twists.

## Main result

Decompose the complete native critical energy as

    E_t(D) = Delta(D) + P_t(D) + R_t(D).

Delta contains every equal-rational-norm ideal pair. P contains every
unequal-norm pair whose rational norms divide one another, in either
orientation. R contains the remaining pairs. These are not ideal-gcd sectors:
P also contains incomparable ideals of different norms.

The complete absolute P sector is O_c(log^2 D). More sharply, for every
0<epsilon<1/2,

    Delta(D) = c_* log^2 D + d_1 log D + d_0
                                      + O(D^(-1/2+epsilon)),
    P_t(D) = -Lambda(t)c_* log^2 D + B(t)log D + C(t)
                                      + O(D^(-1/2+epsilon)).

Here c_*>0, all three coefficient functions are explicitly defined by
absolutely convergent series, and the error is uniform in real t.
The integer-interval certificate and its proved infinite tail imply

    2.153 < Lambda(0) < 2.155,
    Lambda(t) > 2.1 for every |t| <= 0.05.

Thus at center zero the entire rational-divisibility covariance is
asymptotically negative at MORE THAN TWICE the full norm-diagonal leading
size. Both signs inside that covariance were summed. This is not a claim
that its finite-D sign is negative for every D.

Nonnegativity of E forces the still-uncontrolled R to satisfy

    R_t(D) >= 1.1 Delta(D) - C_c(1+log D),  |t|<=0.05.

This is a genuine fixed-center signed-sector evaluation and a necessary
positive compensation in its complement. The displayed lower bound for R
is NOT the missing upper bound. The power-decaying error belongs to this
selected-sector asymptotic; it is not an RH saving.

## Mechanism and reading order

THEOREMS.md gives the exact ratio/shared-prime formula, an elementary
square-norm Euler factorization, the all-moving-exclusion contour argument,
the full quadratic polynomial and explicit infinite coefficient tail. It
also gives the exact rationally incomparable core sum where the attempt
at a full upper bound stops. No reciprocal-zeta contour or quasi-RH theorem
is imported into the proof.

SOURCES.md distinguishes prior ideal-divisibility work (#953), norm-fiber
work (#954), and the native-sign/worst-center work (#955). Their general
methods and earlier results are credited; no world-first claim is made.
VALIDATION.md states the finite and infinite-certificate boundaries.

## Replay

    python verify.py --output /tmp/native-checks.json
    cmp CHECKS.json /tmp/native-checks.json
    python -O verify.py --output /tmp/native-checks-opt.json
    cmp CHECKS.json /tmp/native-checks-opt.json
    python run_mutations.py
    python verify_manifest.py

Python 3.10+ standard library only. The certificate uses all 65,536 rational
indices, including all 6,293 supported nonzero coefficients; it does NOT
enumerate 65,536 independent analytic cases. Separate coefficient checks
compare local Euler arithmetic with mu*(chi_-3*mu) through norm 4096 and
complete good squarefree ideal enumeration through norm 1024. Every norm
pair in the stated small finite covariance box is included.

PUBLICATION.md records the verified remote base and why this packet is
not pushed. The add-only patch is for the branch at that exact base; no
inherited file is changed. The archived fourteen-file earlier norm-fiber
packet is separately preserved in the download companion, not imported as
a premise or claimed newly published.
