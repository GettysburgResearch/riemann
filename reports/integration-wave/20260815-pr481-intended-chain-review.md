# Independent intended-chain reconstruction and review of PR #481

**Repository:** `gfreund123/riemann`  
**Review cutoff:** `2026-08-15T00:55:54Z`  
**Main at review start:** `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
**Proposal PR:** `#481`  
**Proposal branch:** `research/gpt56-pro/91726-pr476-native-slack-repair`  
**Reviewed head:** `005ae49723898d8661d407a0433a6d69cb6d6efc`  
**Reviewed base:** PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`  
**Earlier review PR #482:** `b8428601ad0f046442558b677e5b3ed3139e7527`, frozen against the older proposal head `f41bbd7608cc70bc2a8002d43ef99b5e35977968`

## Executive verdict

This review first reconstructs the intended mathematical chain without treating PR #480, PR #482, or any review-response file as a theorem antecedent. Those review files are lifecycle records and useful falsifiers, not proof inputs.

The live PR #481 packet materially repairs several real defects in the earlier factor-67 composition:

- the aggregate and variable-list child target-mass normalization is now explicit;
- the physical columns `2 <= q < K` are covered by an actual retained-cell cumulative seed;
- the activation-knot relative-refinement issue is addressed by removing atomless collars and refining only on retained cells;
- the false `4 sqrt(X)-H(d_X)=O(1)` normalization is no longer the declared native conclusion;
- the retained physical root target mass is bounded by an actual target-mass calculation, not by the historical certificate count `54`;
- the native slack cocycle is stated with actual-mass children and the positive descendant envelope is charged separately from the one-time root realization.

Those are genuine advances.

The conclusion-producing chain nevertheless remains incomplete at the reviewed head. The earliest unresolved producer arrow is still

\[
\boxed{
\text{positive root fibers + Hall + quantization + all corrections}
\not\Longrightarrow
\text{one explicit exact current/full-child/root-slack identity}
}
\]

because `L-91730` and `L-91736` assume that identity rather than deriving it from one concrete corrected packet. The same omission leaves the complete common-port demand and the exact `Y_4` pairing of the terminal/base/port corrections uninstantiated.

There is also an independent RH-bearing circularity in the score interface. `L-91735`, `T-91724`, and `T-91725` import

\[
J_\Lambda(X)-4\sqrt X<4\log X
\]

as a frozen “elementary benchmark bridge.” No path/blob theorem establishing this bound is supplied in the live locks. More importantly, an eventual one-sided bound

\[
J_\Lambda(X)-4\sqrt X\le C\log X
\]

already implies RH by the Mellin transform and Landau’s one-sign theorem. It therefore cannot be used as an unconditional pre-RH input without a separate proof that would itself settle the problem.

The exact verdict is

```text
L-91732 actual child target-mass contraction       VERIFIED WITH FIXES
L-91733 retained-cell all-column arithmetic        VERIFIED WITH FIXES
L-91734 collar score and retained-cell refinement  VERIFIED WITH FIXES
L-91735 local error sums / thinning scope          VERIFIED WITH FIXES
L-91730 concrete corrected root packet             UNPROVEN / GAP
L-91725 complete common-port demand                 UNPROVEN / GAP
terminal/base/port exact Y4 cost                    UNPROVEN / GAP
J_Lambda - 4sqrt(X) < 4log(X) bridge               RH-BEARING / UNPROVEN
L-91727/L-91736 native slack cocycle                VERIFIED CONDITIONAL
L-91737 physical target-mass bound                  VERIFIED WITH FIXES
positive causal descendant envelope                VERIFIED CONDITIONAL
T-91724/T-91725 complete composition                UNPROVEN / GAP
endpoint-to-RH chain                                CONDITIONAL / NOT TRANSITIVELY LOCKED
Riemann Hypothesis                                  UNPROVEN
```

PR #481 is therefore a serious conditional architecture and a useful repair packet. It is not yet a complete proof of RH and, under the project’s strict terminology, it is not yet a self-contained complete proposal because it explicitly leaves conclusion-producing identities as reconstruction obligations.

---

# I. The intended proof packet, reconstructed independently

The clean intended proof does **not** depend mathematically on PR #480 or PR #482. The canonical packet is the following selected graph.

## Stage A — native endpoint datum

At endpoint `X`, define the native datum

\[
\mathcal N_X=(J_\Lambda(X),w_X,\Omega_X,\text{row and boundary coordinates}),
\]

where

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
\qquad
\Omega_X(q)=w_X(q)-2w_X(4q).
\]

The full Möbius equality row `c_X` has exactly these ordinary and radix-four responses, and its literal entropy is `J_Lambda(X)`. The positive radix-four dual satisfies

\[
J_\Lambda(X)-\mathcal H(d)
=\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)].
\]

Primary files:

```text
L-91377  full Möbius row has native responses and benchmark
L-91378  positive radix-four dual
T-91313  one-sided endpoint-deficit consumer
```

## Stage B — positive factor-67 root fibers

Use the continuum endpoint density

\[
d\nu(x)=\frac{2L(x)}x\,dx,
\qquad 1\le x<67,
\]

where

\[
L(x)=2\sqrt x\sum_{n\le x}\frac{\mu(n)}n
-\sum_{n\le x}\frac{\mu(n)}{\sqrt n}>0.
\]

On each fiber, apply the factor-67 target Hall theorem to the finite `P_61` source. The same target transport gives:

```text
exact residual target;
score superordination;
nonnegative component-row bonus;
exact total-row transparency.
```

Keep the endpoint, Hall, first-owner rough-prime, and generation labels.

Primary files:

```text
L-91107  endpoint inverse and positive equality density
L-91682  target-normalized component-row monotonicity
L-91688  exact rough first-owner partition
L-91690  factor-67 target Hall root thinning
L-91674  positive endpoint integration and common-parent sum
```

## Stage C — one physical root realization

Before labels are forgotten:

1. omit the bottom strip;
2. omit the fixed top strip;
3. remove activation-knot collars;
4. positively refine only inside retained cells;
5. form the common positive endpoint measure;
6. apply one square-root thinning;
7. apply one global martingale/B-spline quantizer;
8. retain the finite/continuum mismatch through the actual retained-cell cumulative seed;
9. add one finite base correction;
10. use one uncolored common root port.

The intended output is one concrete positive parent packet `P_X`, one current row `d_X^cur`, actual child packets `P_b`, and one root slack `r_X` satisfying

\[
\boxed{
\Omega_X
=\Xi(d_X^{\rm cur})+r_X+
\sum_b\beta_bU_b\Omega(P_b),
\qquad r_X\ge0.
}
\tag{A}
\]

Primary files:

```text
L-91733  retained-cell all-column mismatch seed
L-91734  activation collars and same-cell refinement
L-91725  narrow common uncolored port, on PR #479
L-91730  abstract capacity identity once the packet exists
L-91735  proposed native root-cost accounting
```

Equation (A), not a scalar score inequality, is the load-bearing root theorem.

## Stage D — actual-mass children

Use either of two equivalent forms.

### Aggregate global-list form

Let `p_i` be the global rough-prime list, with zero child on inactive fibers. Define aggregate child operators `B_i`. Then

\[
P=P^{\rm cur}+\sum_i\alpha_iB_iP,
\]

and target monotonicity gives

\[
\sum_i\alpha_i m(B_iP)
\le m(P)\sum_i\alpha_i
<\frac18m(P).
\]

### Variable-list actual-mass form

Derive fiberwise

\[
\sum_i a_i(s)m(U_{s,i}Q_{s,i})
<\frac18m(P_s),
\]

integrate by Tonelli, group by complete placement/provenance class, and normalize each nonzero aggregate child by its actual target mass.

Primary files:

```text
L-91650  exact causal coefficient identity
L-91658  same-index child functor
L-91375  child target nonexpansivity and causal debt
L-91732  aggregate and variable-list actual-mass compilation
```

For clarity and provenance, the variable-list form is the safer canonical presentation. The global-list form should explicitly say that `B_i` is restricted to its first-owner slice; otherwise “active prime” can be misread as duplicating a rough monomial divisible by several primes.

## Stage E — native slack cocycle

Insert any feasible child rows `d_b`. Equation (A) gives

\[
s_X=r_X+\sum_b\beta_bU_bs_b
\]

and therefore

\[
\boxed{
\Delta_X
=\delta_{\rm root}(X)+
\sum_b\beta_b\Delta_b,
\qquad
\delta_{\rm root}(X)=\langle Y_4,r_X\rangle.
}
\tag{B}
\]

Primary files:

```text
L-91727  packet-native slack cocycle
L-91736  actual-mass root-to-causal composition
```

## Stage F — one-time root cost and positive descendant envelope

The distinguished root realization must prove

\[
\delta_{\rm root}(X)=O(\log X).
\]

The factor-67 retained positive root packet has physical target mass `<3020`. The children are already positive typed packets, so they do not receive another endpoint frame, collar, mismatch, taper, or common port. The positive causal reset gives

\[
\Delta(P)\le C_+m(P)
\]

for every positive descendant packet. Since child target mass is `<1/8` of the root target mass, all descendants contribute `O(1)` to (B).

Primary files:

```text
L-91735  proposed one-time native root-cost accounting
L-91737  retained root target mass <3020
L-91731 / T-91312  positive descendant envelope
```

The intended conclusion is

\[
\Delta_X=O(\log X)=o(\log^2X).
\]

## Stage G — endpoint criterion

Ordinary/detail feasibility gives

\[
F_\Lambda(X)\le\Delta_X.
\]

The complete-prime-power endpoint theorem separates the positive prime-square moat:

\[
A(X)=F_\Lambda(X)-rac{-1-\zeta(1/2)}4\log^2X+o(\log^2X).
\]

Thus `F_Lambda=o(log^2 X)` forces eventual negativity of the prime endpoint. The Mellin/Landau theorem then excludes off-line zeros and the functional equation gives RH.

Primary files:

```text
T-91313  finite one-sided native endpoint consumer
L-90020 / T-90011 on PR #353  prime-square separation
L-90004 / T-90008 on PR #352  Mellin pole and Landau consumer
```

This is the intended complete chain. Review PRs are not arrows in it.

---

# II. Review of the repaired local components

## 1. Child target-mass normalization

### Verdict: VERIFIED WITH FIXES

`L-91732` now supplies the missing weighted target inequality in both forms.

For the aggregate-list form, target monotonicity gives

\[
m(B_iP)\le m(P),
\]

and therefore

\[
\sum_i\alpha_i m(B_iP)
<\frac18m(P).
\]

For variable fiberwise lists, the pointwise weighted premise is derived before Tonelli, rather than assumed. The actual-mass normalization then gives child coefficients summing to `<1/8`.

This resolves the mathematical substance of the PR #478 mass-normalization concern. The earlier frozen PR #473 exposition was incomplete, but the current live supplement repairs it.

Required fix: in the global-list presentation, define `B_i` on the exact first-owner source slice. A source monomial divisible by two rough primes must not be exported to two same-generation children merely because both primes divide it. The variable-list/provenance-class formulation already avoids this ambiguity and should control the final theorem.

## 2. Retained-cell all-column mismatch

### Verdict: VERIFIED WITH FIXES

`L-91733` correctly replaces a naive cumulative cutoff by

\[
E_X^I(n)=\sum_{m\in I_X,\ m\ge n}\varepsilon_X(m),
\]

so that

\[
E_X^I(n)-E_X^I(n+1)
=\mathbf1_{I_X}(n)\varepsilon_X(n).
\]

The carry identity

\[
v_q(E_X^I)=\sum_{jq\in I_X}\varepsilon_X(jq)
\]

and the constants

```text
ordinary:          57/(2q sqrt K)
detail:            171/(4q sqrt K)
collar+mismatch:   971/(4q sqrt K)
relative:          129/sqrt K
```

are correct on the frozen adjacent-error and collar inputs. The thinning

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

then leaves strict reserve in every nonterminal column, including `q<K`.

Remaining interface: `I_X` is described as a set of complete integer endpoint cells, whereas `L-91734` removes small neighborhoods of activation knots in the quotient variable `x=X/s`. Their preimages generally cut endpoint cells partially. The finite value minus integral over a partially retained cell is not the full-cell error `epsilon_X(n)`. The packet needs one explicit partial-cell quadrature identity, or a proof that the collars and refinement partition are chosen so that `I_X` really consists of complete cells. This is part of the missing concrete root packet.

## 3. Activation-knot collars

### Verdict: VERIFIED WITH FIXES

The measure

\[
d\nu(x)=2L(x)dx/x
\]

is finite and atomless on `[1,67)`. For each fixed `X`, absolute continuity of the integral does permit collars around finitely many activation knots with arbitrarily small target, score, and port coordinates. On the retained compact cells, active capacities have positive minima and the deterministic finite Hall map is locally Lipschitz. Positive same-cell interpolation can therefore be made arbitrarily accurate in the relative typed norm.

This repairs the invalid raw “piecewise Lipschitz implies relative convergence” step.

The theorem remains conditional on the source interpretation of the endpoint frame and on the partial-cell ownership issue described above. It also chooses the collar and mesh separately for each `X`; that is acceptable for an existence theorem but must be reflected in the final measurable packet construction.

## 4. Root target mass

### Verdict: VERIFIED WITH FIXES

On the frozen endpoint measure,

\[
\nu([1,67))<183/10.
\]

One Hall fiber has target mass below

\[
4\sqrt{67}H_{66}<165.
\]

Hence the retained integrated target mass is

\[
m(P_X)<165\cdot183/10=6039/2<3020.
\]

This is an actual physical target-mass bound and correctly replaces the historical certificate-count bound `54`.

Its only unresolved premise is that the endpoint measure and Hall target coordinate are the actual root packet being realized.

## 5. Native slack cocycle

### Verdict: VERIFIED CONDITIONAL

`L-91727` and `L-91736` contain correct linear algebra. If the exact full-child root identity (A) exists, inserting feasible child rows gives the vector cocycle and pairing with `Y_4` gives the scalar cocycle (B).

Same-index placement preserving the numerical detail coordinate is the correct normalization. The current and child capacities are not compared with separate copies of the native root target.

This algebra does not construct (A); it consumes it.

## 6. Positive descendant envelope

### Verdict: VERIFIED CONDITIONAL

Once a child is a complete positive typed packet, the causal generator is nonnegative in row, ordinary, detail, target, and literal entropy coordinates. Its deficit is at most twice its target mass. The recursive target mass is below one eighth. Positive homogeneity and subadditivity therefore give a uniform deficit-per-target bound for the entire positive descendant tree.

It is correct not to rerun the native root endpoint frame on every child. The root realization is one-time; the positive causal envelope is hereditary.

---

# III. First unresolved producer interface

## Exact corrected packet equality

### Verdict: UNPROVEN / GAP

`L-91730` starts with:

```text
Suppose the all-column realization gives Xi(P_X) <= Omega_X.
Suppose the aggregate causal split is exact.
```

It then defines the external reserve and derives the desired identity. `L-91736` likewise starts by supposing the exact current/full-child/root-slack identity and explicitly says that it must be reconstructed.

The current PR does not display one concrete object containing, in one typed vector space:

```text
post-Hall residual source and Hall bonus;
endpoint integration;
bottom and top omissions;
activation collars and retained-cell refinement;
one global quantizer;
retained finite/continuum mismatch seed;
square-root thinning;
finite base packet;
complete current correction demand;
one uncolored common port;
full child capacities;
unused native detail slack.
```

Nor does it prove one equality showing that these pieces have disjoint source ownership and add to the exact native datum.

The needed theorem is

\[
\boxed{
\mathcal N_X
=\mathcal C_X^{\rm fully\ corrected}
+\mathcal R_X^{\rm root\ slack}
+\sum_b\beta_bU_b\mathcal P_b,
}
\]

as an equality simultaneously in source, component row, ordinary responses at `q` and `4q`, radix-four detail, literal score, and every boundary/port coordinate, with all three summands positive in their declared cones.

Until this equality is produced, the later slack cocycle is conditional and the SONTR/NRCT producer is not established.

---

# IV. Common-port interface

## Abstract aggregation

### Verdict: VERIFIED

If each fiber has a positive-semidefinite available port `P_s` and a complete demand `D_s` satisfying `0 <= D_s <= P_s`, then positive integration gives one aggregate demand below one aggregate port. Children may have zero root-global port coordinate.

The older colored-to-physical projection is not needed for this narrow argument.

## Actual complete demand

### Verdict: UNPROVEN / GAP

The theorem assumes that `D_s` is the **complete** correction demand. The PR never constructs the `2 x 2` demand contributed by the retained mismatch, B-spline collar, activation refinement, terminal taper, finite base packet, and any Hall/current correction, nor proves their sum is the matrix dominated by the branch Schur reserve.

A scalar bound on ordinary/detail overfill is not automatically a matrix-port demand inequality. The exact port coordinate of every correction must be written and charged once.

---

# V. Native root-cost review

## 1. Sparse-dual sums and localized errors

### Verdict: VERIFIED WITH FIXES

The support formulas for `Y_4`, the convergence

\[
\sum_qY_4(q)q^{-3/2}<11,
\]

and the partial estimate

\[
\sum_{q\le X}Y_4(q)/q=O(\log^2X)
\]

are sufficient to show that the retained all-column mismatch/collar errors have `o(1)` native cost. The terminal `q^{-3/2}` mismatch has bounded native cost.

## 2. Square-root thinning

### Verdict: VERIFIED AT ITS STATED SCOPES

The continuum shortfall satisfies

\[
4\sqrt X-\tau_KH_0(X)<4290
\]

provided `H_0>=4sqrt(X)`. Independently, the incremental native capacity removed by the scalar thinning is bounded by

\[
(1-\tau_K)J_\Lambda(X)<4290\log X.
\]

These are valid but different statements.

## 3. Terminal/base/port native cost

### Verdict: UNPROVEN / GAP

`L-91728` and `L-91735` import the combined fixed terminal/base/common-port native cost as `O(1)`. The supplement lock itself lists the exact `Y_4` pairing of these packets as an open reconstruction obligation.

A bounded endpoint width or bounded port mass does not, by itself, bound the `Y_4`-weighted detail slack. The exact detail vectors of the terminal packet, finite base packet, and common-port correction must be paired with `Y_4`, or dominated by a proved summable envelope.

---

# VI. The benchmark bridge is RH-bearing

## Submitted use

The proposal repeatedly imports

\[
\boxed{J_\Lambda(X)-4\sqrt X<4\log X}
\tag{C}
\]

as a frozen elementary bridge. Neither live lock identifies a path/blob theorem proving (C).

## Exact Mellin audit

For

\[
J_\Lambda(X)=
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log(X/n),
\]

direct integration gives, initially for `Re z>1/2`,

\[
\widehat J_\Lambda(z)
=\frac{-\zeta'/\zeta(z+1/2)}{z^2}.
\]

The Mellin transform of `4sqrt(X)` is

\[
\frac4{z-1/2}.
\]

Thus

\[
\widehat D(z)
:=\widehat{J_\Lambda-4\sqrt{\cdot}}(z)
=
\frac{-\zeta'/\zeta(z+1/2)}{z^2}
-rac4{z-1/2}.
\]

The pole at `z=1/2` cancels. Every zero

\[
\rho=1/2+\delta+i\gamma,
\qquad\delta>0,
\]

produces a genuine nonreal pole at `z=delta+i gamma`. There is no positive-real pole: zeta has no real zero for `s>1/2`, and the pole at `s=1` has been removed.

Assume an eventual one-sided upper bound

\[
D(X)\le C\log X.
\]

After modifying a compact interval, put

\[
g(X)=C\log X-D(X)\ge0.
\]

Its Mellin transform has every off-line nonreal pole of `D`, but no positive-real singularity. If its abscissa of convergence lies left of `delta`, the defining transform is holomorphic at `delta+i gamma`, contradiction. If the abscissa is at least `delta>0`, Landau’s theorem for a nonnegative function forces a singularity at the real abscissa, again contradicting the real-pole audit.

Therefore

\[
\boxed{
J_\Lambda(X)-4\sqrt X\le C\log X
\text{ eventually}
\Longrightarrow RH.
}
\]

The bridge (C) is consequently an RH-bearing criterion, not an innocuous elementary estimate. It may be true, but it cannot be imported as an unconditional input to a proof of RH without circularity.

## Effect on the submitted composition

The fallback estimate

\[
(1-\tau_K)J_\Lambda(X)<4290\log X
\]

controls only the incremental cost of thinning. It does not bound the baseline difference between the native benchmark and the unthinned positive root score. The current packet therefore still needs either:

1. a direct exact `Y_4` pairing of the entire root slack, avoiding (C); or
2. an independent proof of (C), which would already prove RH by the preceding argument.

This is a separate load-bearing gap from the missing root packet equality.

---

# VII. Endpoint-to-RH consumer

## Finite dual orientation

### Verdict: VERIFIED

For a detail-feasible row,

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X)=\Delta_X.
\]

The sign and normalization are correct.

## Prime-square and Landau chain

### Verdict: VERIFIED WITH FIXES / NOT TRANSITIVELY LOCKED

The intended external chain is:

```text
L-90020  higher-prime-power source has positive prime-square limit;
T-90011  sub-log-squared complete gap forces eventual prime endpoint negativity;
L-90004  prime endpoint Mellin transform retains every off-line zero;
T-90008  eventual one-sign plus Landau excludes every off-line zero;
functional equation -> RH.
```

The core logic is coherent. The live PR #481 locks do not freeze these exact branch-qualified paths and transitive analytic dependencies. A final proof packet must lock and reconstruct the prime-number-theorem Riemann-sum step, meromorphic continuation, pole audit, contour estimates, Landau hypothesis, and real/integer endpoint comparison.

This external chain is not reached until the native root producer and root-cost problems above are solved.

---

# VIII. Claim-level disposition

## New live repair claims

```text
L-91726  child target monotonicity                  VERIFIED
L-91727  abstract native slack cocycle              VERIFIED CONDITIONAL
L-91728  sparse-dual local costs                    VERIFIED WITH FIXES
L-91729  abstract reserve-versus-error algebra       VERIFIED CONDITIONAL
L-91730  packet-native root identity                UNPROVEN / ASSUMED
L-91731  positive descendant envelope              VERIFIED CONDITIONAL
L-91732  actual-mass direct-integral contraction    VERIFIED WITH FIXES
L-91733  retained-cell all-column arithmetic        VERIFIED WITH FIXES
L-91734  knot-collar score/refinement               VERIFIED WITH FIXES
L-91735  score-scope separation                     VERIFIED WITH FIXES
L-91736  actual-mass slack cocycle                   VERIFIED CONDITIONAL
L-91737  physical root target mass <3020            VERIFIED WITH FIXES
T-91724  corrected factor-67 composition            UNPROVEN / GAP
T-91725  audit supplement composition               UNPROVEN / GAP
```

## Lifecycle review files

```text
R-91726/R-91727 and PR #480/#482 reports
    REVIEW/REFUTATION CONTEXT;
    NOT MATHEMATICAL ANTECEDENTS OF THE INTENDED PROOF.
```

---

# IX. First broken and open arrows

## First open arrow in construction order

\[
\boxed{
\text{retained positive endpoint fibers}
\longrightarrow
\text{one concrete fully corrected native root identity (A)}
}
\]

Status: **UNPROVEN / GAP**.

## First circular arrow in the scalar conclusion

\[
\boxed{
\text{native benchmark}
\longrightarrow
J_\Lambda(X)-4\sqrt X<4\log X
}
\]

Status: **RH-BEARING / UNPROVEN AS AN INPUT**.

## Additional open interfaces

```text
partial activation collars -> retained-cell correction seed   UNPROVEN
complete correction stack -> one matrix port demand           UNPROVEN
terminal/base/port packets -> exact bounded Y4 cost            UNPROVEN
external endpoint chain -> transitive immutable lock           OPEN
```

---

# X. Recommended integration and repair actions

1. **Do not treat PR #482 as an antecedent.** Retain it as a frozen review of `f41bbd...`; the live theorem chain should name only mathematical source files.
2. **Make the variable-list actual-mass theorem controlling.** It is clearer and source-faithful. State the first-owner restriction explicitly if the aggregate-list shortcut is retained.
3. **Construct one packet, not another composition theorem.** Give the complete corrected endpoint measure, quantized row, retained mismatch seed, port demand, current row, full child capacities, and root slack as explicit formulas, then prove (A) coordinate by coordinate.
4. **Resolve partial-cell ownership.** Derive the quadrature error for a cell intersected by an activation collar, or align the collar/refinement partition with the exact finite-cell discretization.
5. **Instantiate the port.** Export the exact `2 x 2` demand of every correction and prove its aggregate sum is below the one root port.
6. **Pair every correction with `Y_4`.** Replace the imported `O(1)` label by an explicit terminal/base/port calculation.
7. **Delete the benchmark bridge from the proof DAG.** It is RH-bearing. Bound the root native slack directly from the actual detail vector.
8. **Freeze the external consumer transitively.** Lock the exact PR #352/#353 paths, blobs, theorem scopes, and analytic dependencies.
9. **Only then rerun the full hostile suite**, including all historical normalization, Hall-domain, source-duplication, small-column, activation-knot, and seed-discrepancy falsifiers.

---

# XI. Computation boundary

No heavy experiment was rerun. I inspected the live theorem files, replay sources, retained results, locks, and frozen antecedents. I independently reconstructed the factor-67 local constants and the exact Mellin/Landau implication for the benchmark bridge. The retained replays certify finite algebra and control examples; they do not certify the missing root packet, port demand, correction `Y_4` pairing, or RH.

# Final verdict

\[
\boxed{
\text{PR #481 contains substantial correct repairs and a coherent intended architecture.}
}
\]

\[
\boxed{
\text{Its actual-mass and all-column repairs survive review at their stated scopes.}
}
\]

\[
\boxed{
\text{The fully corrected root packet is still assumed, not constructed.}
}
\]

\[
\boxed{
\text{The imported }J_\Lambda-4\sqrt X\text{ bridge is itself RH-bearing.}
}
\]

\[
\boxed{
T\text{-}91724/T\text{-}91725\text{ do not establish RH at }005ae497\ldots
}
\]

\[
\boxed{\mathrm{RH}\text{ remains unproved.}}
\]
