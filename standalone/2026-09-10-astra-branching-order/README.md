# A genuine order invariant for the Brownian–Xi orbit

**Proposed component proofs; independent review required. RH and the
Gamma(5/2) orbit's unbounded-depth zero property remain OPEN.**

This continues PR #850, rather than substituting a new source. For

    X_0 ~ Gamma(5/2, rate5/2),
    X_(n+1) = (X_n+X_n')/U^2, U uniform[1,2],

with independent children and the SAME U for both, the paper proves

    nu_0 <=_3 nu_1 <=_3 ... <=_3 nu_*,
    zeta_3(nu_n,nu_*) = (4/175)(31/80)^n.

The order compares functions with nonnegative third derivative; it is NOT
ordinary stochastic dominance. A beta-density three-crossing argument and
beta–gamma factorization start the induction. The exact metric formula follows
from the actual third moment, not a fitted convergence curve. Uniform inverse
moments then give a complete, closed-critical-strip Mellin estimate

    |M_n(s)-2xi(s)| <= (12/175)|s(s-2)(s-4)|(31/80)^n,

and an explicit bound for the normalized reflected H_n. The exact error is a
third-derivative polynomial times the Mellin transform of a positive finite
measure. It does not establish that adding that error preserves complex zeros.

The direct test of a broader proposed induction is negative: Gamma(1,1) has
the parent's zero property, but one application of the LITERAL same map has a
simple zero near 0.8720593240 +41.2391452185 i in 1/2<Re s<1. A radius10^-20
Rouché disk is certified by complete integral/series arithmetic. This is NOT
an actual xi zero, and the Gamma(5/2) orbit is NOT refuted: its variance and
special ordering differ. No arbitrary gamma-family preservation should be
used in an RH proof.

Read **PROOF.md** Sections2–5 for the positive invariant and Section6 for the
counterexample, then **VALIDATION.md** and **SOURCES.json**. Classical BPY,
beta–gamma, Peano/Zolotarev, gamma and Hurwitz ingredients are credited. There
is no external priority claim or independent acceptance claim.

## Reproduction

Run from this directory in an isolated Python process:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py --part fast
python -I -S -B test_check.py --part full
python -I -S -B -O test_check.py --part fast
python -I -S -B -O test_check.py --part full
```

The full reconstruction evaluates the actual one-step mixing law through600
EXACT rational moments, with an analytic bound for every later term, plus
directed gamma normalization and a whole-disk derivative bound. There is no
quadrature, external gamma/zeta oracle, zero table or float in acceptance.
Bounded algebra tests do not machine-prove the all-depth stochastic theorem.

`check.py --emit output.json` is a producer operation, not authentication.
Checksums provide a reproducibility record, not an independently trusted code
signature. The test runner reports skipped host capabilities explicitly and
does not print success after a failed/erroring test. The earlier #850 Windows
symlink/reporting issue remains historical and is not silently rewritten.

No main, prior research, reviewer, canonical/formal, workflow or permissions
change is part of this packet. Publication is for component review, not an RH
proposal with the remaining zero invariant delegated to reviewers.
