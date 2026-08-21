# Reconstructed mathematical spine for PR #488

Frozen proposal head: `9acd381fa168db02a03646ab16851daebbf4d0fd`

This file separates the shared factor-67 arithmetic method from PR #488's additional recovery claims.

## A. Shared native arithmetic

```text
full Möbius component row c_X
  |
  | L-91377: exact finite convolution
  v
ordinary response w_X
radix-four response Omega_X
literal score J_Lambda(X)

native detail target Omega_X
  |
  | L-91378: positive radix-four summation by parts
  v
J_Lambda(X)-H(d)
  = sum_q Y4(q)[Omega_X(q)-Xi_d(q)]
```

Status: **VERIFIED**.

## B. Fixed-window positive root entry

```text
root quotient 1<=x<67
  |
  | directed P61 target-Hall inequalities
  | target-normalized row monotonicity
  v
signed compact fibre
  = positive Hall residual
    + positive component-row bonus

rough source support
  |
  | least-prime first-owner projections
  v
one support owner per rough monomial
```

Status:

```text
finite Hall algebra          VERIFIED WITH FROZEN DIRECTED INPUTS
first-owner support          VERIFIED
```

## C. Exact common-parent endpoint frame

The intended concrete object is

\[
 d\mu_X(s)=\frac{2L(X/s)}s\,ds,
 \qquad
 K+2\le s\le X-W-2.
\]

The required arrow is:

```text
native signed finite datum
  + compact Hall fibres
  + rough first-owner labels
  + internal causal colours
        |
        v
one positive measurable common-parent endpoint packet
whose ideal ordinary/detail observations are the native datum
before the explicitly retained finite/continuum comparison.
```

`L-91674` proves that this arrow is compatible with positive integration and one quantizer **if the fibre identity and source interpretation are already available**. `L-91754` specifies the intended measure and operation order but does not give one source calculation deriving the common-parent packet from the native datum.

Status: **UNPROVEN / FIRST INHERITED PRODUCER GAP**.

## D. Whole-cell realization and one quantizer

Conditional on C:

```text
whole integer endpoint cells
  -> no partial-cell cutoff atom

positive endpoint packet
  -> one labelled martingale B-spline quantizer
  -> one finite nonnegative row d_X^0

retained adjacent mismatch + collar
  -> all-column absolute response bound

square-root thinning tau_K
  -> strict detail reserve for 2<=q<=X/4

fixed top omission
  -> strict terminal reserve for q>X/4

above retained support
  -> zero response by triangularity
```

Status: **VERIFIED WITH FIXES ON FROZEN ANALYTIC INPUTS**.

## E. Preferred one-shot specialization

```text
current and causal child colours
  remain internal labels of d_X

exported recursive family = empty
auxiliary matrix port      = absent

all-column comparison
  -> Xi(d_X)<=Omega_X

therefore
  r_X:=Omega_X-Xi(d_X)>=0
```

This route needs no recursive target-mass theorem and no source-derived port theorem. The child coefficient sum `<1/8` remains a provenance cross-check but is not used in the endpoint estimate.

Status: **VERIFIED CONDITIONAL ON C AND D**.

## F. Native one-shot slack price

```text
thinning                      <12012
nonterminal absolute errors   <4
terminal absolute errors      <48972
bottom/top omissions          <1
port/base                     0
----------------------------------
Y4-weighted root slack        <61000
```

The valid mathematical form is an upper bound obtained from positive duality and absolute-value estimates. PR #488's stronger claim that these are disjoint positive source-slack classes is not proved.

Status: **VERIFIED WITH FIXES / CONDITIONAL**.

## G. Endpoint consumer

```text
native slack <61000
  -> F_Lambda(X)<61000

prime-square source asymptotic
  -> A(X)=F_Lambda(X)-c log^2 X+o(log^2X)
  -> A(X)<0 eventually

prime endpoint Mellin transform
  retains every off-line zero pole

Landau one-sign theorem
  -> no off-line zero
  -> RH
```

Status: **INHERITED CONDITIONAL IMPLICATION; NO NEW CONTRADICTION FOUND**.

## H. PR #488 recovery layer

```text
L-91840 partial-cell restriction       VERIFIED
L-91841 first-owner child restriction  VERIFIED WITH FIXES
L-91842 port aggregation               ABSTRACT / NON-LOAD-BEARING
L-91843 positive fourteen-stage ledger UNPROVEN / GAP
L-91844 direct Y4 arithmetic           VERIFIED WITH FIXES
T-91840                                UNPROVEN / GAP
```

## First broken arrows

### Inherited

\[
 \boxed{
 \text{compact Hall/source fibres}
 \not\Rightarrow_{	ext{deposited proof}}
 \text{the concrete positive native common-parent endpoint packet}.
 }
\]

### PR #488-specific

\[
 \boxed{
 \text{signed finite-realization comparisons}
 \not\Rightarrow
 \text{positive source-partition stages}.
 }
\]

## Strongest honest conditional theorem

The current repository supports the following conditional implication:

> If the exact factor-67 common-parent endpoint packet asserted in `L-91754` is reconstructed on the frozen Hall/source inputs, and if the frozen all-column and terminal response comparisons hold for that same packet, then the one-shot row of PR #487 has native deficit below `61000`; the frozen endpoint consumer then implies RH.

Neither PR #487 nor PR #488 independently establishes the antecedent at the level required for an accepted proof.
