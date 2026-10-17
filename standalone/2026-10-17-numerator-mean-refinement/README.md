# Numerator-family averaging: a proposed 11/12 all-field refinement

Status: PROPOSED source-composition theorem; independent review required.
No RH/GRH, unknown native moment, or critical covariance estimate is assumed.
Main and the inherited mathematical/status files are unchanged.

Read PROOF.md, then SOURCES.md and VALIDATION.md.

## New step, not another critical criterion

The proposed theorem excludes zeros of every Dedekind zeta function in
Re(s)>11/12, away from the principal pole, and gives the corresponding
finite-order Hecke result. It improves #958's proposed all-field 25/27 boundary
using its unconditional analytic foundation. It does not improve the earlier
reported 7/8 special-setting Riemann-zeta bound, prove RH, or settle the original
fixed-twist critical moment.

The full CT Poisson summand contains a numerator L(w,chi_u). Individual
convexity at Re(w)=1/2 charges U^(1/4) for each row. BGL's actual sixth-free
family second mean instead bounds the sum of numerator absolute values by
U^(1+epsilon) across the entire U-row family. Taking uniform bounds on the
reciprocal and correction BEFORE Cauchy costs no independence assumption.
This removes U^(1/4) on the good class. The other classes retain convexity.

Three density thresholds, 3/4, 21/25 and 19/20, cover all nonprincipal rows
in four disjoint classes. For EACH FIXED 0<e<=1/100000 take

    alpha=1/2+e, beta=1/2, M=1+e>1.

The actual principal detector has Mellin shift 2/3-e/3 and growth at most
Z^(1/4+3e), giving the strict half-plane 11/12+8e/3. Choosing e separately
for each point proves the proposed strict 11/12 boundary. There is no use of
M=1 and no assumption of constants uniform as e tends to zero.

## Source and recovery improvements

The actual CT v2 TeX/PDF analytic interfaces were accessible and freshly read
this time. The packet does not claim a complete re-proof of CT or a Lean build.
The fixed-S-unit twist adapter, complete AFE columns, original nonunit zeros,
full sixth-free norm, changed detector normalization and joint height tails
are explicit in PROOF.md.

Both formerly unpublished user packets were ALREADY pushed on #958. Their
27 original files were hash-checked against the retrieved remote tree objects;
both full checkers freshly reproduce their archived outputs in normal and
optimized Python. No duplicate recovery, historical-status rewrite, or recovery
of unseen work from other conversations is claimed.

## Reproduce

    python verify.py
    python -O verify.py
    python run_mutations.py
    python verify_manifest.py

The new checker authenticates exact density/contour/scale bookkeeping across
the whole parameter interval, and explicit synthetic finite checks. It does
NOT verify actual L-values, an L-zero census, the imported analytic theorems,
or the source-composition proof. See VALIDATION.md for precisely what ran.

The unchanged positive theta estimate reaches its own 1/12 saving ceiling.
Further bins alone cannot improve that particular bound. Progress beyond this
proposal requires a stronger binding estimate, such as cancellation retained
before the theta/additive Cauchy step. This is not a mathematical no-go for RH.
