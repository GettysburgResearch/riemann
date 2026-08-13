# Integration handoff: PR #399 direct-Euler factor-54 proposal

Review cutoff: `2026-08-13T07:40:41Z`  
Base/main reviewed: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Displayed PR #399 head reviewed: `4b8b4306142e92d66bc27f7eda10f64a703ed3d8`  
Review branch: `review/pr399-direct-euler-factor54`

## Integration verdict

```text
T-91304 complete RH proposal      UNPROVEN / GAP
L-91350.2                         FALSE
X-91127 complete certificate      FALSE
Riemann Hypothesis                UNPROVEN
```

Do not integrate `T-91304` as a proof, proved theorem, or verified complete
composition.

## Strong results to retain

```text
R-91308 old convex-cell refutation                         VERIFIED
R-91309 target-Hall residual row-typing refutation        VERIFIED
L-91336 hidden least-prime source partition               VERIFIED
L-91342 complete terminal P79 projection                  VERIFIED WITH FIXES
L-91345 large-prefix Hall reserve                         VERIFIED WITH FIXES
L-91346 inherited arithmetic-row positivity              VERIFIED WITH FIXES
L-91351 exact row/target/score Euler identities           VERIFIED
L-91351 first-moment score-minus-target identity          VERIFIED WITH FIXES
T-91302 substochastic recurrence consumer                 VERIFIED CONDITIONAL
```

The strongest new local result is the exact rowwise identity

\[
D_P(py;j)=p^{-1/2}D_P(y;j)+D_{Pp}(py;j),
\]

with `D_(Pp)>0` certified on the inherited range `2<=j<=y<83`.

## First urgent correction

`L-91350.2` replaces the causal parent prefixes with full prefixes through
`t+8`.  At

\[
t=79,\quad p=83,\quad y=1,
\]

the positive sources `85,86,87` belong to the formal prefix but exceed
`py=83`, so their actual `K_a` terms vanish.  The displayed equality includes
all three with strictly positive formal contributions and is false.

The `X-91127` script uses the same false formula and omits the parent activation
boundaries `y=d/p`.  Its retained JSON also does not match the output schema of
the checked-in script and has no hash manifest.

Integration action:

```text
mark L-91350.2 false;
mark actual low-prefix Hall theorem unproved/gap;
replace X-91127 with a parent+child activation checker;
regenerate and hash the exact result.
```

## Second urgent correction

The hidden hazard partition and direct Euler canonical-child split are not yet
compatible branchwise.  On the pure reserve state and `r=p^-1/2`, a hazard
branch has

\[
(T,S)=(2r,r^2),
\]

whereas an `r`-scaled canonical child has

\[
(T,S)=(2r,r).
\]

The child already exhausts the target but overspends the complete hazard score.
This is the exact `R-91307` obstruction.  A hidden hazard branch therefore
cannot literally be

```text
r canonical child + positive score-superordinate residual.
```

Integration action: require one explicit regrouping/commuting theorem before
accepting any global recurrence.

## First open RH-bearing theorem after finite repair

A valid continuation must prove one of the following.

### Scalar native-packet version

For every colored least-prime branch `b`, construct a scalar `alpha_b>=0`, a
native complete child packet `P_(X_b)`, and a positive residual packet `R_b`
such that

\[
\mu_b=\alpha_bP_{X_b}+R_b,
\qquad
\sum_b\alpha_b\le1,
\]

with the same identity in target, score, every ordinary/radix-four component
row, and all boundary ports.

### Measure-valued version

Replace the endpoint-indexed scalar consumer by a consumer for arbitrary
normalized positive packet measures, and prove that its potential dominates the
native endpoint loss while remaining substochastic under restrictions.

Positive source mass alone is not enough: an arbitrary restriction can
concentrate the signed score loss.

## Frontier and debt ledger still needed

For `j>y`, the child contribution is zero, but no exact theorem currently proves
that all such rows are:

```text
positive and capacity-faithful;
already in the outer/current frontier;
paired with favorable target and score;
charged to one collar/terminal omission/endpoint port;
O(1) in total after every branch is summed.
```

Require one row-indexed all-branch ledger before accepting the constant `C` in
`T-91304.6`.

## Repository action

The current proposal is a split DAG:

```text
main d688cc7...       contains T-91304 and new corrections;
PR #399 4b8b430...    contains load-bearing ancestors absent from main.
```

Before the next review, create one immutable proposal branch containing all
exact dependency files and replay manifests, or provide a machine-readable
path+SHA dependency lock.  Duplicate `L-913xx` identifiers on the live branch
should also be renumbered or branch-qualified.

## Review packet

```text
reports/integration-wave/20260813-pr399-direct-euler-factor54-review.md
audits/integration-wave/20260813-pr399-direct-euler-factor54-status.tsv
audits/integration-wave/20260813-pr399-direct-euler-exact-obstructions.md
integration/2026-08-13/pr399-direct-euler-factor54-review-handoff.md
```

## Final statement

The proposal materially improves the local arithmetic packet, but the submitted
finite certificate is invalid and the global source-to-scalar-loss interface is
still open.  RH is not established.