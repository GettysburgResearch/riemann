# Off-central numerator moments and a proposed 49/54 all-field boundary

**Status: proposed source-qualified composition, requiring independent mathematical review. RH is not proved.** No unknown native moment, critical signed-covariance bound or RH/GRH assumption is used. The adopted analytic inputs and preceding short-support reconstruction have not been independently rebuilt.

## What changes

Instead of bounding every numerator on Re(w)=1/2, first prove

    sum_{Na<=U}^{sixth-free} |L_F^S(7/12+it,psi chi_a)|^4
        << U^(1+eta)(2+|t|)^C.

The functional equation then gives U^(4/3+eta) for the fourth moment at 5/12. For a class of U^nu rows the first mean there costs U^(3nu/4+1/3). Although this moment is larger than the central one, the actual physical factor Y^(w-1) improves by more. The net saving is (3a-1)/24, equal to 1/72 at the limiting scales a=4/9.

The full good class keeps its second moment at 1/2. The complete comparison uses 36 disjoint zero classes and the two-term reflected estimate N+N^2/Z, with X=Y=Z^(4/9+epsilon). The new nonprincipal z line is 1/3, and every principal, small-frequency, large-frequency and horizontal contribution is retained.

The resulting proposed conclusion is

    zeta_K(s) != 0 for every number field K,
    Re(s)>49/54, s!=1,

and the finite-order Hecke corollary. It improves #966's proposed 109/120 by 1/1080 and #968's proposed 10/11 by 1/594. It does not improve the reported stronger 7/8 special-setting result, cover infinite-order angular twists, give discriminant-uniform constants, or prove RH.

## Reading and replay

Read OFFCENTER_MOMENT.md for the new AFE/sieve argument, then COMPOSITION.md for the exact imported contracts, all classes and full Mellin conclusion. OFFCENTER_MOMENT.md preserves the first published checkpoint and its historical qualification; COMPOSITION.md supplies the subsequent full composition.

    python verify.py > /tmp/offcentral.json
    cmp /tmp/offcentral.json CHECKS.json
    python -O verify.py > /tmp/offcentral-optimized.json
    cmp /tmp/offcentral-optimized.json CHECKS.json

CHECKS.json contains every threshold and density parameter. The checker uses only exact rational arithmetic and the standard library. Its 3,516 predicates concern finite algebra, not validity of the imported analytic theorems. REPLAY.json records eight actual separately executed corrupted optimized processes, all rejected.

## Publication and remaining boundary

PR #969, branch research/offcentral-numerator-20261018. Parent #968 is frozen at 14f544fb4293ffb59942ff8d345ab9d6da67025c. The first checkpoint is 2eaa5b5221c1f2b8998fa32ebf9023471e5b7a18; its mathematical file is preserved unchanged. This directory is the only addition. Main and the integrated scientific record are unchanged.

The symmetric short-support/full-good-class calculation reaches its 49/54 limit here. Additional exceptional bins alone do not remove the good-class restriction x>2/3. A further advance must change that term or its correction domain, improve the physical estimate, or preserve signed cancellation. None of those subsequent improvements is proved here.

See VALIDATION.md for the exact source-reading, recovery and review boundaries. No global priority claim is made for the classical AFE, functional equation, Holder, zero-density, or contour methods.
