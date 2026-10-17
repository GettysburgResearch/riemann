# Five density strata: a proposed all-field 25/27 refinement

**Status: PROPOSED source-composition theorem; independent review pending.**
The exact analytic input and source-access limits are in CONTRACTS.md.
No RH, GRH, unknown native moment or signed covariance hypothesis is used.
However, the CT v2 analytic contracts are adopted from the pinned #957
adapter rather than independently reverified against a newly retrieved
primary manuscript. A rational checker cannot validate that import.

## The new consequence

With the stated imported CT/DF/BGL inputs, PROOF.md derives

    zeta_K(s) != 0 for Re(s)>25/27, s!=1,

for every number field K, and the finite-order Hecke corollary. This improves
#957's proposed all-field boundary 23/24 under the same analytic foundation.
The excluded width increases from 1/24 to 2/27. It does NOT improve the
stronger previously reported 7/8 special-setting bound for ordinary zeta,
prove RH, or settle the critical native covariance recovered in this PR.

## The finite-stratum gain

Instead of treating all exceptional denominator characters at one contour,
partition their zeros at real parts 2/3, 3/4, 17/20, 19/20. The four exact
family-count exponents are 5/6, 8/11, 191/359, 11/47. A class is counted using
its LOWER threshold but shifted only to the right of its UPPER threshold.
The ordinary good class is retained as the fifth class.

Use alpha=5/9, beta=4/9+e with each fixed 0<e<=1/10000. All five central
bounds, the theta estimate, both principal remainders, the small/large
frequency ranges and the joint height tails have saving at least
2/27-3e after the displayed loss budget. The actual signed detector has
Mellin shift 35/54 and growth at most 5/18+3e. Therefore the zero-free
boundary is 25/27+3e. Selecting a fixed sufficiently small e separately
for each point proves the OPEN 25/27 half-plane. The argument never sets
M=1 or uses constants uniform as e tends to zero.

The new written proof includes the fixed-twist family adapter, full detector
columns, all contour domains, reciprocal disks, height quantifiers and the
Mellin/descent step. It imports rather than reproves the theta construction,
large-sieve theorem, and classical analytic zero detector. Stratification
itself is classical; no exhaustive historical priority claim is made.

A separate exact dual bound shows that 2/27 is the ceiling of the stated
positive theta/good-row exponent model with M>1 and beta<=alpha. This is
NOT an arithmetic lower bound or a universal obstruction to further RH work.
Further bins alone do not improve the model's limiting good class.

## Verification

    python verify.py --output /tmp/density-checks.json
    cmp CHECKS.json /tmp/density-checks.json
    python -O verify.py --output /tmp/density-checks-O.json
    cmp CHECKS.json /tmp/density-checks-O.json
    python run_mutations.py
    python verify_manifest.py

Python 3.10+ standard library. The 1,821 explicit finite predicates include
512 synthetic zero-set partitions, not observations of real L-function zeros.
Every all-e polynomial inequality uses an exact rational Bernstein test;
there is no fitted exponent or sampled-parameter proof. Four separately
executed corrupted optimized processes are rejected. These arithmetic tests
are not independent analytic review, a Lean build or a proof of CT inputs.

## Publication and relation to the recovered packets

Base for this continuation: cec073b584a9e305fd09f6d31361d0f3f77cadb0 on
research/native-recovery-density-strata-20261017, draft PR #958.
That base already recovers the two previously unpublished user packets,
unchanged, in two preceding commits. The new mathematics adds only this
standalone directory. No old proof, main or integrated-status file is edited.
The newly used #957 proof is cited at ec54cb6b0029aedd8a99e6016a42a1426a0223a2;
its branch is not silently merged or promoted to reviewed status.

Read CONTRACTS.md first, then PROOF.md Sections 2--5. The decisive independent
review targets are the source family, all-M CT rescaling and joint tails,
not merely the fraction 25/27. SOURCES.md and VALIDATION.md state precisely
what was read and run.
