# Selected fourth moments and a proposed 109/120 Dedekind refinement

**Status: PROPOSED mathematical deductions and composition, independent review
pending. No RH/GRH or unknown native-moment hypothesis is assumed. No proof of
RH, formal verification, or externally accepted zero-free theorem is claimed.**

Read PROOF.md for the new numerator-family and exceptional-character estimates;
CONTOURS.md for the all-field composition; SOURCES.md and VALIDATION.md for
input fidelity and execution boundaries. The exact finite parameter table is
strata.json. Every assertion here is subject to its written analytic proof,
not certified by the number of software predicates.

## The new arithmetic step

For de Faveri's full sixth-power-free family, with original nonunit zeros and
any fixed permitted S-supported character twist, the proposed proof gives

    sum_(Na<=U)^flat |L_F^S(1/2+it,psi chi_a)|^4
         << U^(7/6+epsilon)(2+|t|)^C.

The complete AFE columns and their products are retained. The sixth-power
column decomposition c*d^6 has NO coprimality condition between c and d.
It has an explicit row mask 1_((a,d)=1), including at neutral sixth charge.
This is a moment of the numerator L-family, not an inverse-L/Mobius moment.

Retain the number R of exceptional characters in the pre-Cauchy zero detector:
Holder gives R^(1/4), not U^(1/4). Solving r<=a*r^(1/4)+b costs the exponent
4/3. At real zero threshold 3/4 this yields, for some fixed rho>0,

    #{Na<=U: a has a zero Re s>=3/4, |Im s|<=4U^rho}
         << U^(43/60+epsilon).

The previous displayed DF norm exponent at this threshold is 8/11; the
improvement is 7/660. This is an exceptional-CHARACTER count, not a claimed
optimized T-aspect or total-zero-count theorem. It is independent of CT's
theta argument. No general literature-priority claim is made.

## The proposed global consequence

Combine this and the selected numerator mean with the recovered short-support
reflection theorem and CT's unchanged actual Poisson identity. Choose
X=Y=Z^(9/20), so the physical support has norm Z^(9/10)<Z. Seventeen disjoint
zero classes suffice. The detector exponent is 9/40+3e and its actual Mellin
shift is 41/60. Their sum tends to

    109/120 = 0.908333333... .

Thus the complete proposed composition excludes zeros of every Dedekind zeta
function on Re s>109/120 (s!=1), with the finite-order Hecke corollary.
It improves the separately recovered proposed 91/100 boundary by 1/600.
It does not improve the stronger reported 7/8 Riemann special-setting result,
or control the original critical fixed-center covariance. Every e is fixed
and positive; no endpoint or uniform-as-e-goes-to-zero assertion is used.

## Recovery and replay

The preceding thirteen-file short-support packet is preserved LOSSLESSLY as
an authenticated four-part archive in ../2026-10-17-short-support-recovery/.
Its six transport files are not misreported as thirteen expanded source files.
Run that directory's recover.py into a new directory, with --replay, to recover
all original sources and reproduce its original normal/optimized checker.
Its exact original source tree is a80cb7e2404e0f6835c47017597b6acbeb9cb264.
The download companion additionally provides those expanded old sources.

New checks, from THIS directory:

    python verify_manifest.py
    python verify.py
    python -O verify.py
    python run_mutations.py

The last three outputs must equal CHECKS.json, CHECKS.json and MUTATIONS.json,
respectively. They check finite algebra, not the deep analytic inputs.
