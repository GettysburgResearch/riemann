# Current research read-back and choice of attack

Snapshot checked on 17 October 2026. Later PR creation is not mathematical
integration or automatically a stronger result. All numerical regions
below are the authors' proposed conclusions, not newly certified global
theorems in this pass.

| PR | Frozen head | Relevant conclusion and read scope |
|---|---|---|
| #962 | b2032c663736ecd1e3872559d160ce069664ea06 | Prior packet: exact critical scattering, free-z projection, prime memory and Fourier logarithmic transfer. Local complete packet available and the relevant full proofs reread. Its principal critical estimate remains open. |
| #963 | c91fd9ddfb37668338d9aec22c0e29cfe741cf07 | Full main geometric proof read. Hybrid radial/angular ideal resolution and a smaller logarithmic power; no fixed-member extraction. The new ray theorem exploits actual signs and removes the radial average in a scalar second-moment theorem. |
| #964 | 09ab9bc067bc66278fad8fcd883e8c8569b0cbc9 | Full proof read. Complete Eisenstein norm tensors, local polynomial uniformity with arbitrary fixed log savings in its stated interval range. The current linear-phase power theorem has a different range and does not supersede all polynomial/short-interval conclusions. |
| #965 | d58e3282a9379b6ae165681bc2e21e4f9fd18c26 | Full proof and source file read. Proposed 91/100 all-field region via reconstructed subcritical reflection, retaining T+T^2/Z. Its full upstream theta construction is not re-certified here. |
| #966 | 8d94494698ee447711a53dec922986586418e398 | Full selected-moment proof and source file read. Proposed 109/120 all-field region, with improved exceptional-character density. Its complete contour theorem is not independently certified in this pass. |
| #967 | b7215948884cedb1b5062dd541bc79ec765e8e4c | PR description read: historical archive recovery, not a new analytic input. No claim that its archived files were replayed in this pass. |
| #968 | 14f544fb4293ffb59942ff8d345ab9d6da67025c | Full numerator-moment proof, complete zero-free composition and source file read. Proposed 10/11 all-field region from the fourth numerator mean. |
| #969 | 2eaa5b5221c1f2b8998fa32ebf9023471e5b7a18 | Full new off-central numerator proof and changed-file inventory read during final review. Fourth moments at 7/12 and 5/12; the one-file checkpoint explicitly claims no new zero-free region. See the final addendum below. |

Among #965, #966 and #968, 109/120 is the smallest proposed boundary.
Indeed 10/11-109/120=1/1320. The later #968 therefore does not supersede
#966 numerically. Both remain proposed all-field compositions, and neither
is numerically stronger than the reported special-setting 7/8 theorem.

## Primary-source checks that changed the assessment

The suspected fourth-moment family mismatch is absent. Fresh de Faveri
primary HTML explicitly defines the larger sieve with sixth-power-free
rows AND columns, and Theorem 1.1 supplies the exact four-monomial bound
used in these packets. Its conductor and zero-extension conventions also
support their complete n=c d^6 adapter. Fresh BGL Section 5 supplies the
pre-Cauchy mean used by #966's exceptional-row Holder argument. See
MOMENT_INTERFACE_AUDIT.md for exact scope and the limits of this review.

This pass also tried higher numerator/mollifier moments and direct LM
powering. No improvement of the active middle-class bottleneck was found
in the stated exploration. The finite optimization is not a proof of
optimality. A small high-sigma density opportunity was recorded but was
not promoted as a critical-line advance or composed into another global
region.

OpenAI/math main was freshly checked at
1581d4cbdd69a0faf34b2089614fe2a814316a6a, unchanged from the previous
pass. The September 30 paper's actual theorem and definitions were fetched
again: the 7/8 assertion is COMMON to every Dirichlet character and all
conductors and heights, with principal poles allowed. This exact scope,
not merely a fixed-field Dedekind statement, is what the new Fourier
adapter requires. We do not claim a new transitive audit of that proof
or its Lean formalization.

A fresh primary read also found Baiying Liu, arXiv:2610.12234v1, refining
the special-setting boundary to

    (1507-2sqrt(921))/1653 = 0.874957069799... .

The introduction, stated original/common Dirichlet scope, parameter
derivation and relevant dependency account were inspected. Its full
proof and Lean files were not independently rebuilt. Its numerical
refinement is not an input here: the simpler reported 7/8 boundary already
produces the explicit 15/16 Fourier theorem. This outside work further
supports the decision to pursue a different arithmetic estimate instead
of presenting another nearby parameter optimum as the main result.

## What the new packet actually adds

The two new written arguments change the estimated arithmetic object.
The first keeps a complete reciprocal product inside a finite inverse
identity and obtains a conductor-priced major/minor-arc power saving.
The second keeps native signs along rational rays before angular
resolution, obtaining a sharp scalar ray diagonal and a finite
angular-only energy bound. Neither uses the unproved prime-memory
stability or principal free-z projection bound from #962.

## Concurrent PR #969: off-central numerator checkpoint

During the final source check, PR #969 was a draft at exact head
`2eaa5b5221c1f2b8998fa32ebf9023471e5b7a18`, stacked on #968 at
`14f544fb4293ffb59942ff8d345ab9d6da67025c`. Its changed-file inventory
contained only the 91-line
[OFFCENTER_MOMENT.md](https://github.com/GettysburgResearch/riemann/blob/2eaa5b5221c1f2b8998fa32ebf9023471e5b7a18/standalone/2026-10-18-offcentral-numerator/OFFCENTER_MOMENT.md),
blob `03cd95684d539733880e49538846c6e8e3ebd3cf`, which was read in full.
There was no new separate source account or completed composition file
in that checkpoint. Despite the title, the document explicitly announces
no new zero-free boundary.

The proposed new component is the pair of numerator fourth-moment bounds

    sum_(Na<=U)^flat |L_F^S(7/12+it,psi chi_a)|^4
                      << U^(1+eta)(2+|t|)^C,
    sum_(Na<=U)^flat |L_F^S(5/12+it,psi chi_a)|^4
                      << U^(4/3+eta)(2+|t|)^C.

The main new interface was checked against the S6 sieve and complete AFE
already reviewed in this pass. It separates rows by ACTUAL conductor Q,
where Q<=C U, before retaining the dual AFE factor Q^(-1/3) in its fourth
power. The product-ideal dyadic bound at the right-hand line is
V^(-1/6)K(U,V). Its four terms are each O(U) for 1<=V<=U.
On a conductor dyad the dual gives Q^(-1/6)K(U,Q), again O(U), up to the
stated small losses and fixed height factors. This avoids replacing a
negative conductor power by a negative U power. Sixth-power removal
retains shared primes and the original row mask. The functional equation
then uses the positive Q^(1/3)<=C U^(1/3) to obtain the left-hand bound.
No flaw was identified in this limited component check. The full upstream
AFE and sieve are still imported inputs, not independently reconstructed
from first principles.

For a zero-selected subset of size U^nu the left-hand fourth moment gives
the first-mean exponent 3nu/4+1/3. Moving the actual CT numerator from
w=1/2 to w=5/12 changes its physical exponent by a saving
(3a-1)/24; at a=4/9 this is 1/72. The correction condition
3x+w>5/2 requires x>25/36 on that contour, so the good class near x=2/3
must retain its central second-moment treatment. A complete new contour
and exceptional-class certificate is expressly left for later work.

This checkpoint is compatible with the present Fourier and angular
results. It does not change the imported common 7/8 Dirichlet strip
used in the direct Fourier proof, and that proof does not depend on
#969. The new moment is finite-order and concerns numerator L-values;
it supplies neither an infinite-order angular theorem nor a native
inverse-Mobius moment, critical covariance estimate, or RH conclusion.
