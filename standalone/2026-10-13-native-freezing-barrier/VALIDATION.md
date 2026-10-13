# Validation and review limits

## Mathematical status

Two proposed proof notes, one author. No independent agent or human review,
proof-assistant certification, upstream quasi-Riemann reconstruction, or
full-repository CI run was performed. These are research results for review,
not a promotion of integrated accepted mathematics.

The classical PNT in the fixed progression 1 modulo 3 is an explicit input.
The proof does not assume a target zero-free half-plane or a native fourth
moment. Classical Euler and Mellin machinery is credited in SOURCES.md.

## Same-author reconstruction checks

The derivation was checked in both directions at the following interfaces:

- The finite smooth Mobius polynomial includes all squarefree ideal columns;
  its compact-test Mellin identity is exact for each fixed cutoff.
- The slowly varying frequency is t_y=pi/log y. Its weighted first-prime
  contribution dominates the quadratic logarithm remainder for every fixed
  0<sigma<1, including sigma<=1/2.
- The lower scale D_0=exp(y^(1/A)) makes y<=(log D)^A literal. The optional
  upper scale uses a separate tau<sigma with 1-tau<1/A+eta. No exact-curve
  or every-scale conclusion is inferred from these existential witnesses.
- The actual principal row u=1 already gives a native-coefficient obstruction.
  The stronger average uses genuine distinct rows b^6 of norm <=D^h, with
  Nb>y, not uncontrolled CRT representatives.
- Original nonunit zeros persist at rough primes dividing b. Their terms
  vanish before expectation; they do not alter the smooth conditional mean.
- The exponent identity h/6+2k alpha=h+k+2k(alpha-beta_(k,h)) is exact.
  The concrete h=21/20, k=2, A=4 example has defect 1/16, not an achieved
  upper-moment saving. Endpoints and single prescribed cutoff curves are
  explicitly outside the conclusion.
- The exact forward dilation norm uses the same-sign rational norm fibers
  specific to this quadratic field. Its low-frequency lower asymptotic does
  not require arbitrary rapidly oscillating input functions.

These are disclosed same-author checks, not independent review receipts.

## Finite replay actually performed

`checks/check_native_barrier.py` passed in ordinary Python and `python -O`.
Both outputs were compared byte-for-byte to `results/exact.json`.
The report contains **3,220 explicit predicates**, including six rejection
checks labeled `negative_control_*`. Repeated zero coefficients and setup
conditions are included in this count; it is not a count of independent
asymptotic instances.

Coverage:

- finite Euler products over actual split/conjugate/inert norm patterns;
- grouped norm multiplicities and absence of sign cancellation in these
  specific squarefree norm fibers;
- exact signed products, forward absolute masses, and inverse coefficient
  identities through ordinary norm 400;
- a rational Mellin identity for the hard test 1_[1,2], used ONLY to test
  finite algebra. The analytic theorem uses a fixed smooth W instead;
- all squarefree good ideal columns in [D,2D] for D=8,16,32,64,128,
  with the literal sextic characters at the stated rows;
- conditional means on u=1 and actual b^6, Jensen checks, a nonunit-mask
  witness, small complete phase enumerations, and both signs of the native
  minus projected remainder;
- exact rational threshold, contour, and replica-exponent comparisons.

For example, at D=128 and u=1 with the hard-window diagnostic, the native
sum is -7, so its fourth power is 2401. At y=19 the conditional fourth
moment is 19819 and the smooth mean is 9, whose fourth power is 6561.
This finite example shows that the projection can exceed the native value.
It is not a witness to the asymptotic exponent theorem.

The copied #936 helper is authenticated by its immutable Git blob before
use. The parent #936 manifest verifier also passed, and its original checker
was replayed and matched its saved report exactly. This does not enlarge the
parent theorem's mathematical review scope.

## Publication and integrity

The new packet is intended as one added standalone directory, stacked on
#936 at `eb8d23decc003d36ded287dc98868308192cc889`. The final publication ref
and remote comparison are recorded in its PR. Prior proofs and integrated
status are not changed.

The manifest binds payload bytes by SHA-256, Git blob identity, and length.
It authenticates file identity, not mathematical correctness. Publication
uses connected GitHub actions and remote tree/blob read-back: a local git
clone attempt failed because the runtime could not resolve github.com, so
no claim of a clean cloned repository worktree is made.

The smallest remaining native arithmetic statement is still the one-sided
rough-charge interference bound at the safe log-square cutoff from #936.
No estimate for that full term has been established in this pass.
