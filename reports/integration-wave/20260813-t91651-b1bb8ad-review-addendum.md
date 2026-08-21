# Review addendum for `T-91651` at `b1bb8ad`

Review cutoff: `2026-08-13T19:06:48Z`  
Main: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Frozen PR #439 target: `b1bb8ad23747bd1b04f31a7e7dc796ed1e5bc911`

PR #439 moved during review to `e78e6bae43f41790f41de6132cf71b5b7f9041aa`, eight commits ahead. Those commits add a separate CFFP packet and do not modify the frozen `T-91651` files.

## Verdict

```text
9165x packet now physically present                   VERIFIED
historical firewalls                                  VERIFIED
causal realized identity                              VERIFIED
recursive coefficient mass <1/8                      VERIFIED
free certificate / physical realization distinction VERIFIED IN PRINCIPLE
causal target, row and response positivity           VERIFIED
D'(u)>0 above 67 and D(67)>1                         VERIFIED
compact causal literal-debt proof                     SIGN REPAIR NEEDED
packet deficit convexity and envelope consumer        VERIFIED CONDITIONAL
primary machine lock                                  INVALID: 1/14 MISMATCH
import machine lock                                   INVALID: 7/11 MISMATCH
cross-endpoint child placement U_p                    OMITTED DEPENDENCY
root finite-correction ledger                         PROPOSED, NOT PROVED
endpoint-to-RH dependency graph                       NOT FROZEN
T-91651 complete composition                          UNPROVEN / GAP
Riemann Hypothesis                                    UNPROVEN
```

The new packet closes the earlier missing-deposit objection and materially improves historical `T-91304`. No counterexample was found to the central causal architecture.

## Exact surviving core

For

\[
r_i=p_i^{-1/2},\quad s_i=\prod_{h\le i}(1-r_h),\quad
\lambda_i=r_is_{i-1},\quad \alpha_i=r_i\lambda_i,
\]

one has

\[
s_k+\sum_i\lambda_i=1
\]

and, after physical realization,

\[
P_X=s_kP_X+\sum_i\lambda_i(P_X-r_iU_{p_i}P_{X/p_i})
      +\sum_i\alpha_iU_{p_i}P_{X/p_i}.
\]

The child terms cancel exactly and

\[
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

`L-91652` correctly separates the free provenance cone from the physical realization, so coefficient mass is measured before quotienting while deficit is measured after realization. `L-91654` correctly proves nonnegative causal target, component rows, ordinary response and radix-four response. `L-91406/T-91650` then give a valid abstract recurrence

\[
\Lambda(X)\le C+\rho\Lambda(X/67),\qquad \rho<1/8,
\]

provided the concrete current-debt, child-placement and root hypotheses hold.

## Literal-score repair

With

\[
D(u)=E(u)-(5\sqrt u-3),
\]

`L-91656` correctly proves `D'(u)>0` for `u>67` and correctly records

\[
D(67)=1.2764007195549669\ldots>1.
\]

For a causal datum the declared-minus-literal shortfall is

\[
-D(u)+rD(v),\qquad v=u/p.
\]

The file bounds this using `max[-D(v)]_+`, but the adverse child term is `rD(v)_+`. Replace the displayed compact constant by

\[
C_{abs}=\max_{1\le v\le67}|D(v)|.
\]

Then

\[
[-D(u)+rD(v)]_+\le r|D(v)|\le C_{abs}.
\]

This is a proof repair, not a counterexample to uniform boundedness.

## Replay scope

`X-91650` checks one finite rational coefficient example and the directed gate `D(67)>1`. Its root mass fields are inserted constants: the script does not reconstruct Hall support or residual coefficients. The result file itself correctly excludes imported finite campaigns and the complete RH composition from its scope.

## Missing child-placement theorem

The realized identity uses `U_pP_(X/p)`, but the envelope recurses on a deficit at endpoint `X/p`. A theorem must transport arbitrary feasible child rows, benchmark, ordinary/detail responses, literal score and boundary data between these endpoint types.

Resident `L-91361` supplies the intended same-index multiplicative placement and exact score/response scaling. It is not cited by `L-91652/T-91651`, is not in either lock, and `U_p` is not identified with its functor. Importing and locking `L-91361` is a direct repair.

## Root theorem remains open

`L-91655` asserts

\[
\Delta_X(P_X^{nat})\le C_{root}+\Delta_X(P_{rec})
\]

without stating an equality of complete endpoint data from which subadditivity would yield it. A complete root theorem still must define the global `P_X^{nat}` with benchmark `J_Lambda(X)` and prove, in one physical coordinate system:

```text
native root datum
 = one bounded current datum
 + realization of a recursive certificate of mass <=54.
```

It must also type Hall-edge benchmarks and capacities, prove that mismatch, collar, terminal omission and common ports are charged once, and verify every physical integer column. Saying that Hall edges have nonnegative score is not enough without their benchmark and feasible-packet data.

The imported source files do not close this automatically. Several remain proposed and independently unreviewed; `L-91110` leaves collar feasibility open, `L-91111` is omitted from the lock, and imported `L-91112` is explicitly refuted except for retained component formulas.

## Endpoint bridge

The intended sign is correct: feasibility gives `Score(d)<=P_Lambda(X)`, hence

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\le J_\Lambda(X)-\operatorname{Score}(d).
\]

But `L-91655` attributes this to `L-90029`, which delegates it to branch-qualified PR #353 `L-90023` at blob
`04c178e4abd54a32f10d4a96cee6d4cd1f7c319b`. The implication from `F_Lambda=o(log^2 X)` to RH then uses PR #353 `T-90011` at blob
`9c93dc10bb12d85785d16f4643dd81d3070c0043` and further dependencies. None is frozen in the `T-91651` import lock.

## Final boundary

```text
causal packet machinery                  strong and review-surviving
abstract O(1) envelope                   correct conditional theorem
complete root producer and one-use datum open / load-bearing
endpoint consumer dependency closure     open / load-bearing
T-91651                                  serious conditional architecture
RH                                       unproved
```

The first honest closing target is a branch-pinned complete root identity, with valid transitive locks, that produces one uniformly bounded current physical datum plus one recursive provenance certificate of mass at most `54`.
