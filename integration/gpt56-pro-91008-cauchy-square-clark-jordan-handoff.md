# Handoff — Cauchy-square soft count, Clark common-depth flow, and Jordan source

## Frozen stack

```text
repository: gfreund123/riemann
base PR:    #394
base SHA:   82ee32348b05512514462966bfeb4e2de4ae5ecf
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
RH status:  UNPROVED
```

## Review order

1. `claims/lemmas/L-91008-radial-curvature-is-derivative-of-cauchy-square-soft-count.md`
2. `claims/theorems/T-91003-rh-is-monotonicity-of-cauchy-square-soft-count.md`
3. `claims/lemmas/L-91009-cauchy-square-fourier-and-depth-moment-projectors.md`
4. `claims/lemmas/L-91010-completed-shift-ratio-is-common-depth-clark-family.md`
5. `claims/lemmas/L-91011-generalized-jordan-positive-euler-cocycle.md`
6. `claims/refutations/R-91003-positive-jordan-source-and-centre-mass-do-not-close-rh.md`
7. `experiments/X-91008-cauchy-square-clark/`
8. session report

## Load-bearing checks

- sign and factor in
  \[
  \mathcal N_x'(a)=4a^3\mathcal C_x(a^2);
  \]
- reflected-pair primitive
  \[
  2\Re[a^4/(a^2-z^2)^2];
  \]
- contour orientation in the mass/Fourier projector;
- exact centred second-moment defect \(\pi a d^2\);
- boundary phase orientation
  \(\partial_x\arg\Theta_a=-2p_x(a)\);
- generalized-Jordan coefficient and shifted cocycle formula;
- strict noncancellation of the matched derivative singularity.

## Exact frontier

```text
soft-count primitive and zero expansion          PROPOSED COMPLETE
RH -> soft-count monotonicity                     PROPOSED COMPLETE
off-line pair -> strict monotonicity failure      EXACT
Fourier hyperbolic depth multiplier               PROPOSED COMPLETE
mass and squared-depth projectors                 PROPOSED COMPLETE
common-depth Clark interpretation                 PROPOSED COMPLETE
positive generalized-Jordan source/cocycle        EXACT
prime-side monotonicity                           OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
