# Independent review of the PR #399 direct-Euler factor-54 RH proposal

Review date: 2026-08-13  
Review cutoff: `2026-08-13T07:40:41Z`  
Review base / current main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Displayed PR #399 head: `4b8b4306142e92d66bc27f7eda10f64a703ed3d8`  
PR #399 branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Review branch: `review/pr399-direct-euler-factor54`

## Executive verdict

\[
\boxed{
\begin{aligned}
R\text{-}91308,R\text{-}91309
&:\quad \mathbf{VERIFIED},\\
L\text{-}91346\text{ inherited-row theorem}
&:\quad \mathbf{VERIFIED\ WITH\ FIXES},\\
L\text{-}91351\text{ exact Euler identities}
&:\quad \mathbf{VERIFIED\ WITH\ FIXES},\\
L\text{-}91350.2
&:\quad \mathbf{FALSE},\\
X\text{-}91127\text{ as a complete certificate}
&:\quad \mathbf{FALSE},\\
T\text{-}91304
&:\quad \mathbf{UNPROVEN\ /\ GAP},\\
\mathrm{RH}
&:\quad \mathbf{UNPROVEN}.
\end{aligned}}
\]

The proposal contains important, durable local progress.  In particular, the
complete `P_79` one-prime Euler factor really does admit exact row, target, and
score splittings, and the inherited arithmetic residual row is supported by a
substantial exact/directed argument at its stated range.  The new work also
correctly refuses to infer arithmetic-row typing from a target-only Hall
residual.

The full composition does not pass review.  There are three independent
load-bearing failures:

1. the finite low-prefix Hall theorem `L-91350` uses an exact false formula that
   omits the parent support cutoff `d<=py`; its checker omits the corresponding
   parent activation cells, and its retained JSON is not the output of the
   checked-in script;
2. the hidden least-prime hazard branch is not the `p^(-1/2)`-scaled canonical
   child consumed by the direct Euler split; the pure reserve ray gives an exact
   target/score contradiction;
3. no theorem converts pointwise source/hazard weights into the scalar
   coefficients required by the signed endpoint-loss recurrence in `T-91302`,
   and the noninherited frontier/collar ledger is asserted rather than written.

Accordingly PR #399 at the frozen revisions does not establish the Riemann
Hypothesis.

## 1. Frozen repository reconstruction

The proposal is not contained in one commit.

The current main commit `d688cc7c...` contains:

```text
R-91308  old convex-minimum checker refutation
R-91309  Hall-residual row-typing refutation
L-91350  corrected low-prefix Hall claim
L-91351  direct Euler row/target/score splice
T-91304  proposed complete RH composition
O-91311  final proposed proof DAG
X-91127, X-91128, X-91129
```

The displayed PR #399 head `4b8b4306...` contains load-bearing ancestors that
are absent from main, including:

```text
L-91336  hidden least-prime hazard partition
L-91337  hidden target and score ledgers
R-91307  hazard canonical-return obstruction
L-91342  terminal P79 projection
L-91343  abstract positive-kernel branching
L-91344  finite Green row decomposition
L-91345  large-prefix reserve
L-91346  inherited-row positivity
T-91302  conditional branching consumer
X-91122, X-91124, X-91125
```

`O-91311` acknowledges this split.  No single frozen source commit therefore
contains the proposed theorem and all cited proof files.  Every conclusion in
this report is frozen to the two exact SHAs above.  Neither head moved during
the final drift census.

This split-DAG problem is not merely cosmetic.  Main cannot replay the proposal
from its own tree, while PR #399 does not contain the proposed final theorem.
Any later integration must first create one immutable proposal branch or a
manifest naming every exact path and SHA.

## 2. Strong local mathematics that survives

### 2.1 Exact Euler row split

For

\[
P=P_{79},\qquad p\ge83,\qquad 1\le y<83,
\qquad r=p^{-1/2},
\]

`L-91351` defines

\[
D_P(x;j)
=\sum_{d\mid P,\,d\le x/j}
\frac{\mu(d)}{\sqrt d}Q_{x/d}(j).
\]

Splitting the divisors of `Pp` into `d` and `pd` gives exactly

\[
\boxed{D_P(py;j)=rD_P(y;j)+D_{Pp}(py;j).}
\]

This is an equality, rowwise and before physical carry evaluation.  It is not a
continuum approximation and does not use the refuted completed two-state
cascade.

**Verdict:** `VERIFIED` as an unconditional finite algebraic identity.

### 2.2 Exact target and score splits

With

\[
F_{a,P}(x)=\sum_{d\mid P,\,d\le x}
\mu(d)\left(\frac{a\sqrt x}{d}-\frac1{\sqrt d}\right),
\]

\[
\mathfrak T_P=3F_{4/3,P},
\qquad
\mathfrak S_P=3F_{5/3,P},
\]

the same divisor split gives

\[
\boxed{\mathfrak T_P(py)=r\mathfrak T_P(y)+\mathfrak T_{Pp}(py),}
\]

\[
\boxed{\mathfrak S_P(py)=r\mathfrak S_P(y)+\mathfrak S_{Pp}(py).}
\]

The first-moment difference is also exact:

\[
\boxed{
\mathfrak S_{Pp}(py)-\mathfrak T_{Pp}(py)
=\sqrt{py}\left[A_P(py)-\frac1pA_P(y)\right].
}
\]

The finite statement `A_P(y)<=1` for `1<=y<83` is checked by exact rational
arithmetic in `X-91128`; the large-prefix lower bound supplies
`A_P(py)>1/25`.  Conditional on those prefix results, the displayed surplus

\[
\frac{58}{2075}\sqrt{py}
\]

is correct.

**Verdict:** exact identities `VERIFIED`; numerical-prefix realization
`VERIFIED WITH FIXES` because the retained experiment is not hash-locked to a
complete replay manifest.

### 2.3 Inherited-row positivity

`L-91346` proves positivity only on the inherited range

\[
2\le j\le y<83.
\]

Its proof separates a positive Green bulk from a finite boundary functional,
uses exact rational inequalities for the final margins, and delegates two
large fixed-block scans to `X-91125`.  I inspected the checker, interval
operations, retained output scope, and analytic reduction.  I did not rerun the
`2^22` scan.

The checker is materially stronger than a floating-point sample: it uses exact
integer square-root enclosures, directed fixed-denominator logarithm intervals,
and exact rational final comparisons.  The theorem should nevertheless retain
its exact scope and an explicit proof-object hash before integration.

**Verdict:** `VERIFIED WITH FIXES`, surviving scope exactly
`p>=83`, `1<=y<83`, `2<=j<=y`.

### 2.4 Terminal `P_79` packet

`L-91342` constructs, on `1<=y<83`, a positive target-exact,
score-superordinate terminal representation and a nonnegative exact component
row.  The target-normalized row monotonicity is a finite directed statement.
It applies to the complete terminal packet at endpoint `y`; it does not state
that every pointwise restriction or hidden-hazard submeasure is a scalar copy
of that packet.

**Verdict:** `VERIFIED WITH FIXES` at terminal complete-packet scope.

### 2.5 Correct firewalls

`R-91308` correctly refutes the earlier use of an unconstrained global convex
minimum outside its activation cell.  `R-91309` correctly proves that a
Hall transport in target units does not automatically reproduce the arithmetic
row; the discrepancy is

\[
\sum_{o,e}t_{o,e}[\rho_j(e)-\rho_j(o)].
\]

These firewalls are valuable and must remain.

**Verdict:** both are `VERIFIED` `REFUTATION`s.

## 3. First fatal failure: the low-prefix Hall formula is false

`L-91350` defines the causal atom

\[
K_a(d;p,y)
=d^{-1/2}[a\sqrt{py/d}-3]\mathbf1_{d\le py}
-p^{-1/2}d^{-1/2}[a\sqrt{y/d}-3]\mathbf1_{d\le y}.
\]

It then writes the Hall margin using full prefixes `A_t,B_t` through `t+8`,
without the parent cutoff `d<=py`.  Its display `L-91350.2` is therefore not an
identity.

Take the exact admissible point

\[
t=79,\qquad p=83,\qquad y=1.
\]

The positive squarefree sources

\[
85=5\cdot17,
\quad86=2\cdot43,
\quad87=3\cdot29
\]

are included in the full positive prefix through `t+8=87`, but all exceed
`py=83`; their actual causal contributions are zero.  The right side of
`L-91350.2` includes instead the strictly positive quantity

\[
\sum_{e\in\{85,86,87\}}
\frac{a\sqrt{83/e}-3}{\sqrt e},
\qquad a\in\{4,5\}.
\]

Thus the equality is exactly false.

The checker has the same defect.  It partitions only at child activations and
at `y=t/83`; it omits the parent activation boundaries `y=d/p`.  Its `fixed`
and `active` formulas use the false full prefixes.  Consequently its 383,472
assertions are assertions about a different expression.

The retained `verification.json` is also not generated by the checked-in
script: the field names and reported minima do not match the script's output
schema, and the directory contains no `SHA256SUMS` binding script to result.

Precise disposition:

```text
L-91350.2                                      FALSE
X-91127 proves every actual Hall activation    FALSE
actual finite target Hall theorem              UNPROVEN / GAP
actual finite score Hall theorem               UNPROVEN / GAP
retained X-91127 JSON                           EMPIRICAL ONLY
```

This exact contradiction does not prove the true Hall inequalities false.  A
correct checker must include parent and child support cells simultaneously.
Until then, the positivity claims `mathfrak T_(Pp)>0` and
`mathfrak S_(Pp)>0` used by `L-91351/T-91304` remain open on the finite
low-prefix region.

## 4. Second fatal interface: hazard branches are not canonical children

The proposal invokes the hidden least-prime hazard partition and then states
that every least-prime branch has one terminal canonical child with coefficient
`r=p^(-1/2)` plus a positive favorable residual.

That composition is false if interpreted branchwise.

On the canonical hidden pure-reserve state

\[
I(0,1)=(0,1,0,2)^T,
\]

the one-prime hazard scales the `X` mode by `r^2` and the `Y` mode by `r`.
The positive target and score ledgers are therefore

\[
T_{\rm haz}=2r,
\qquad
S_{\rm haz}=r^2.
\]

The asserted `r`-scaled canonical child has

\[
T_{\rm child}=2r,
\qquad
S_{\rm child}=r.
\]

Its target already exhausts the hazard target, but its score is larger by
`r-r^2>0`.  The remaining residual would have target zero and negative score.
It cannot be a positive score-superordinate current packet.

This is exactly the obstruction retained in `R-91307`.  The direct Euler split
repairs the **complete** one-prime `P_79` packet by regrouping terms.  No theorem
shows that an arbitrary pointwise hidden-hazard branch is that complete packet,
or identifies the regrouping that makes the two constructions commute.

Therefore the arrow

```text
hidden least-prime branch
  -> r times the complete canonical P79 child
     + positive favorable arithmetic residual
```

is `FALSE` as a literal branch statement and `UNPROVEN / GAP` as a proposed
regrouped statement.

A repair must define the grouping before the branch is normalized, prove its
positivity in target, score, and every component row, and show that it preserves
source-disjoint provenance.

## 5. Third open interface: pointwise mass is not scalar signed loss

`T-91304.1` supplies pointwise functions `theta_b(n)`.  Its recurrence later
uses scalars `theta_b`, but it does not define:

- the measure used to integrate `theta_b(n)`;
- the normalization of the resulting branch packet;
- an equality between that normalized packet and the native endpoint packet
  defining `mathfrak L_(X_b)`;
- where the direct Euler coefficient `r` enters the scalar coefficient.

Positive source mass, positive target mass, and signed endpoint loss are
different objects.  A branch restriction can concentrate on precisely the
source atoms where a packing loses score.  Thus a source-mass fraction
`theta` does not imply a loss bound `theta mathfrak L_Y`.

An exact two-atom example suffices.  Give two atoms equal source mass, pay the
first completely, and leave loss `H>0` on the second.  The complete packet loss
is `H`; the restriction to the second atom has mass fraction `1/2` but loss
`H`, not `H/2`.

This is not fixed merely by saying that the source map is linear.  Linearity
scales a packet under a common scalar; it does not make an arbitrary restriction
a scalar copy of the native packet.

There is also a sign issue.  The endpoint loss is signed, and endpoint weights
above one are allowed.  If the actual coefficient is `r theta_b`, replacing it
by `theta_b` is not a monotone relaxation when `mathfrak L_(X_b)<0`.

`T-91302` is an exact conditional consumer, but it explicitly assumes scalar
score-transfer coefficients, a capacity-faithful lift of arbitrary feasible
child packings, and the recurrence itself.  It does not derive those hypotheses
from hidden-source substochasticity.

**Verdict:** the recurrence `T-91304.6` is `UNPROVEN / GAP`.

## 6. Noninherited rows and one-use debt

`L-91346` proves positivity only for `2<=j<=y`.  For `j>y`, the child term
vanishes, but that algebraic fact alone does not establish that all such rows:

1. are nonnegative in the exact current arithmetic packet;
2. lie in an already certified outer/frontier capacity region;
3. receive target and score allocations of the required sign;
4. share one collar, terminal omission, and endpoint port without branchwise
   duplication;
5. contribute an absolute `O(1)` total debt after summing all branches.

`L-91351/T-91304` state that the rows are handled by the resident frontier but
do not provide one exact row-indexed ledger proving those five points.  The
statement `D_P(y;j)=0` for `j>y` proves only that nothing is inherited.

**Verdict:** current-generation frontier typing and bounded one-use debt are
`UNPROVEN / GAP`.

## 7. Exact reviewed proof DAG

The strongest correct DAG is:

```text
complete P79 one-prime divisor algebra
  -> exact row split
       D_P(py)=r D_P(y)+D_Pp(py)                    VERIFIED
  -> exact target/score splits                     VERIFIED
  -> inherited D_Pp row positive, 2<=j<=y          VERIFIED WITH FIXES
  -> terminal complete P79 child positive          VERIFIED WITH FIXES
  -> first-moment score-minus-target formula        VERIFIED WITH FIXES
  -> finite low-prefix target/score positivity      BROKEN: L-91350.2 FALSE
  -/-> complete positive current residual packet
```

Even after repairing that finite theorem, the global composition remains:

```text
hidden least-prime hazard source partition          VERIFIED
  -> branchwise r-scaled canonical child
     + positive favorable residual                  FALSE LITERALLY / REGROUPING OPEN
  -> scalar loss coefficients theta_b               UNPROVEN / GAP
  -> all-row one-use capacity/frontier ledger        UNPROVEN / GAP
  -> T-91302 conditional recurrence consumer         VERIFIED CONDITIONAL
  -> o(log^2 X) endpoint loss
  -> RH.
```

The first broken arrow in the submitted file order is the false finite identity
`L-91350.2`.  The first open global arrow after a hypothetical repair is the
hazard-branch-to-canonical-packet typing theorem.

## 8. Claim-level mathematical status

### Unconditional or finite structural results retained

```text
R-91308 old convex-minimum refutation              VERIFIED / REFUTATION
R-91309 Hall-row typing refutation                 VERIFIED / REFUTATION
L-91336 coordinatewise hidden hazard partition     VERIFIED / ROUTE INFRASTRUCTURE
L-91337 separate positive ledger partitions        VERIFIED WITH FIXES
L-91342 complete terminal P79 projection            VERIFIED WITH FIXES
L-91343 abstract positive-kernel branching          VERIFIED WITH FIXES
L-91345 large-prefix inequalities                   VERIFIED WITH FIXES
L-91346 inherited-row positivity                    VERIFIED WITH FIXES
L-91351 exact Euler row/target/score identities     VERIFIED WITH FIXES
T-91302 branching recurrence consumer               VERIFIED / CONDITIONAL IMPLICATION
```

### Failed or open load-bearing claims

```text
L-91350 exact low-prefix reduction                  FALSE
X-91127 complete exact replay                       FALSE AS CERTIFICATE
finite low-prefix residual positivity               UNPROVEN / GAP
hazard branch = r canonical child + positive rest   FALSE AS LITERAL COMPOSITION
regrouped branch typing                              UNPROVEN / GAP
source-mass fraction = endpoint-loss coefficient    UNPROVEN / GAP
noninherited frontier one-use ledger                 UNPROVEN / GAP
T-91304 complete RH proof                            UNPROVEN / GAP
Riemann Hypothesis                                   UNPROVEN
```

## 9. Retained experiments inspected but not rerun

I inspected source, retained outputs, and scope statements for:

```text
X-91122  terminal P79 target/score/row projection
X-91124  P79 prefix corridors
X-91125  P79 one-prime inherited-row splice
X-91127  corrected low-prefix Hall checker
X-91128  first-moment prefix check
X-91129  direct Euler composition demonstration
```

I did not rerun the `2^22` prefix/row scans or the 383,472-inequality campaign.
`X-91129` checks symbolic one-prime identities and a generic toy
substochastic tree; it does not certify the arithmetic branch typing, the
actual score recurrence, or the one-use physical frontier.

The decisive review findings require no heavy computation.  The
`L-91350.2` counterexample and the pure-reserve hazard obstruction are exact
finite algebra.

## 10. Integration actions

1. Mark `L-91350.2` and the current `X-91127` certificate claim **FALSE**.
2. Mark the true low-prefix Hall inequalities **UNPROVEN / GAP**, not false.
3. Quarantine `T-91304` from any proved-RH or complete-proof registry.
4. Retain the exact Euler identities and inherited-row theorem at their narrow
   scopes.
5. Replace `X-91127` with a checker whose cells include both
   `d<=y` and `d<=py` activations; regenerate the result from that exact script
   and add hashes/manifests.
6. Prove one explicit commuting branch diagram:

   ```text
   hidden colored branch measure
     -> scalar native terminal packet
        + positive target/score/row residual,
   ```

   or replace `T-91302` with a measure-valued consumer for restricted packets.
7. Write one rowwise frontier/collar/port ledger covering every `j>y` and prove
   total debt is absolute `O(1)` after all branches are summed.
8. Consolidate the proposal and all ancestors into one frozen branch or exact
   dependency manifest; do not integrate a split proof DAG.

## 11. Final conclusion

\[
\boxed{
\text{The corrected direct-Euler proposal contains substantial local progress,
 but it does not prove RH.}
}
\]

The low-prefix certificate is invalid by an exact support-cutoff counterexample,
and the global source-to-scalar-loss recurrence remains unproved even if that
finite certificate is repaired.  The first new theorem needed is a correctly
activated finite Hall certificate; the first remaining RH-sized global theorem
is an exact branch-packet homogeneity/regrouping theorem compatible with target,
score, every finite row, and one-use capacity.