# Two-mollifier reciprocal laws, without a zero-density premise

Status: PROPOSED source-qualified mathematical deductions; independent review required.
Scope: actual capped reciprocal Hecke moments in the fixed full power-free ideal family.
No RH proof, uncapped all-member inverse moment, or new zero-free half-plane.

The new step assigns different jobs to two actual Mobius polynomials. A longer
one controls bad rows and the size of the inverse on the remaining rows. A
shorter one computes the leading Euler constant. An elementary finite-array
transfer combines their bounds without a zero-density theorem, zero-free
rectangle or analytic logarithm of L. The cap loss on GOOD rows is paid too.

At the fixed sextic line s=3/4+it, uniformly on each fixed compact t interval:

    sum_a W(Na/U) min(|L_a(s)|^(-2), U^(1/6))
          = c_W C_1(s) U + O(U^(9/10+epsilon));

    sum_a W(Na/U) min(|L_a(s)|^(-2), U^(1/4))
          = c_W C_1(s) U + O(U^(59/60+epsilon)).

Here C_1(s)=product_p(1+w_p (Np)^(-3/2)), with
w_p=(1-1/Np)/(1-(Np)^(-6)). All rows in the weighted family remain; zeros
are assigned the cap. The moving annulus eventually omits every fixed row,
but adjoining any finite prescribed set, including the principal member,
preserves the law at these error rates. That still does not exclude zeros.

For EVERY FIXED negative order 2k, PROOF Theorem A gives cap U^theta and
error U^(1-min(1/(8k+2),theta,delta_k-theta)+epsilon), 0<theta<delta_k.
The explicitly listed delta_k uses the full residual second/fourth/sixth
moments from #986/#987 at lengths adapted to k. Taking theta=delta_k-1/(8k+2)
gives error saving 1/(8k+2). At k>=16, that cap exponent is
(11k+3)/(2k(4k+1)), larger than the recovered upper-bound cap1/k.
It is not larger than #984's fixed cap1/80 for arbitrarily large k.

Theorem B gives a density-free law at every FIXED sigma>1/2 for every fixed
character order n>=3 and fixed k. It does not assert uniformity as sigma
tends to1/2, as k grows, or across fields.

Read PROOF.md, especially Sections3--7, then SOURCES.md and VALIDATION.md.
VERTICAL_CAP_AUDIT.md records the attempted vertical singularity escape:
a zero of multiplicity m contributes order C^(1-1/(2km)) after integrating
the cap C. That contribution still fits the current family bounds.

The new contribution is the two-mollifier transfer and its improved capped
Euler laws, NOT another claim of the previously published11/15 residual
estimate. All deep family/sieve/functional-equation and character-mean
interfaces are imported explicitly. No worldwide priority claim is made.

Replay the complete finite checks and byte manifest with:

    python replay.py

Intended path: standalone/2026-10-18-two-mollifier-law/.
This is a separately labelled continuation on PR #989's recovery commit
30151b285f3334484758c8305b58da380ff73488. The recovered ten-file packet and
all inherited mathematics are unchanged. The final remote receipt belongs
to the PR description and the outer delivery record, not a self-hashing file.
