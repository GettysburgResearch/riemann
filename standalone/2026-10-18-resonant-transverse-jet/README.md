# Resonant divisor and transverse prime detector

**Proposed unconditional component arguments; no new zero-free bound or RH proof.**

This pass does not advertise a smaller decimal in the previous Dedekind
composition. It investigates the functional-equation diagonal of the actual
three-variable unramified correction. The residue is zero-insensitive; its
first transverse coefficient is not.

Read PROOF.md. Its three new deductions, relative to the inspected #971
local formulas, are:

1. Extract exactly H(s,w,z)=zeta_F^S(s+w)K(s,w,z). K converges normally on
   Re s,Re w>0, Re z>1, 2 Re s+Re w>1, crossing the old Re(s+w)>1 barrier.
2. Prove K(s,1-s,z) never vanishes in the ENTIRE open critical strip,
   uniformly over the allowed theta phases. Its local numerator error is
   less than 1/32 of a nonzero base; the infinite product is controlled.
3. The transverse Laurent finite part V has a simple pole at every target
   zero rho with residue -multiplicity(rho)*R(rho), where R is holomorphic
   and nonzero. After explicitly bounded analytic compensation, the detector
   is exactly -d/ds log zeta_F^S(s), independent of the auxiliary phases.

The logarithmic derivative and its prime-power series are classical. The
claim is the source-specific factorization, nonvanishing normalizer and
exact transverse adapter, not the discovery of a new RH equivalence.

**Still missing:** a complete physical transverse projection with all test
and contour derivatives retained, and a new signed estimate for it. An
upper bound for the residue alone does not supply this. No S6 sieve, native
critical moment, short-support theta bound or quasi-RH conclusion is a
premise of the component Euler/functional-equation theorems.

Sources are pinned in PROOF.md: #971 at 3f1d2a07631eb6cca1f2716be01f64e874667639;
parent #969 at 6542781188469e8a23dadf9d419b3d5cf4d11de7. #962's independent
prime detector and multiplicity warnings are credited at PR-description scope.
No original source file or accepted scientific status is modified.

Replay:

    python verify.py
    python -O verify.py

Both reproduce CHECKS.json: 2,035 finite algebra predicates. Six actual
mutated optimized executions are recorded in MUTATIONS.json. They are not
analytic proofs, native ideal censuses or independent referee reports.
See VALIDATION.md and MANIFEST.json for the precise boundaries.
