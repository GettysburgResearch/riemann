# Independent review of the advertised `T-91651` provenance-causal packet proposal

Review date: 2026-08-13  
Review cutoff: `2026-08-13T17:18:44Z`  
Current main: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
PR #399 head: `9deddaa92c1b709b052e0994bd9a6dc0bb307366`  
PR #439 head: `1546d866cdedb8a13b55b2deb154e47e0559e808`  
PR #424 head: `9f2ea36fd295efb117967edf8288f0e10d6fa716`  
Previous independent review PR #431 head: `78a622e32ef36e587099bb95cb791461b75d26bf`  
Review branch: `review/t91651-provenance-causal-packet-20260813`

## Executive verdict

\[
\boxed{
\begin{aligned}
\text{PR \#431 counterexample verification}
&:\quad \mathbf{VERIFIED},\\
\text{causal coefficient identity and }\sum\alpha_i<1/8
&:\quad \mathbf{VERIFIED},\\
\text{formal target/score/row causal positivity}
&:\quad \mathbf{VERIFIED\ WITH\ TYPING\ OBLIGATIONS},\\
\text{literal entropy tail above }67
&:\quad \mathbf{VERIFIED\ WITH\ A\ NUMERICAL\ CORRECTION},\\
\text{packet deficit homogeneity/subadditivity}
&:\quad \mathbf{VERIFIED\ ABSTRACTLY},\\
T\text{-}91651\text{ as an immutable repository theorem}
&:\quad \mathbf{ABSENT\ AT\ THE\ NAMED\ HEADS},\\
\text{concrete provenance packet producer}
&:\quad \mathbf{UNPROVEN\ /\ NOT\ DURABLY\ DEPOSITED},\\
\text{full packet-envelope-to-RH composition}
&:\quad \mathbf{UNPROVEN\ /\ GAP},\\
\mathrm{RH}
&:\quad \mathbf{UNPROVEN}.
\end{aligned}}
\]

The proposed repair is materially different from, and structurally better than,
historical `T-91304`.  It correctly abandons hidden-hazard observation and
source-fraction weighting of signed loss.  The identities behind the
provenance-labelled causal packet and the abstract packet-envelope consumer are
sound.

I found no exact algebraic counterexample to the central coefficient identity.
The proposal nevertheless cannot be classified as a complete proof at the
frozen repository state.  The advertised `R-91650`--`R-91652`,
`L-91650`--`L-91656`, `T-91650`, `T-91651`, `O-91650`, and the advertised
large-prime `L-91651` are not present on the current heads of PR #399 or PR
#439, nor on main.  No immutable dependency manifest identifies another exact
commit containing them.

More importantly, the summary passes from a labelled certificate algebra to a
native physical packet deficit without writing the required realization map,
benchmark, complete capacity/port vector, and root bridge.  Those are exactly
the producer hypotheses that the durable abstract consumer `T-91401` leaves
open.

Accordingly the present status is:

```text
serious repaired architecture                    YES
central causal coefficient contraction            EXACT
complete durable producer theorem                 NO
independently reviewable full proposal             NO
Riemann Hypothesis established                     NO
```

## 1. Frozen artifact census

### 1.1 Named deposit does not exist at the named PR heads

At the cutoff:

```text
PR #399  research/gpt56-pro/91101-moment-neutral-shadow-transport
         9deddaa92c1b709b052e0994bd9a6dc0bb307366

PR #439  research/gpt56-pro/91355-causal-packet-budget
         1546d866cdedb8a13b55b2deb154e47e0559e808
```

The theorem and lemma directories at both commits contain no `T-91651` and no
advertised `R-9165x/L-9165x/O-91650` packet.  Direct retrieval of

```text
claims/theorems/T-91651-provenance-causal-packet-factor54-resolution-proposal.md
```

returns `404` on both heads.  Code search, commit search, branch search, and a
recursive tree census likewise found no such file.  The only branch matching
`t91651` is this review branch.

PR #439 itself still states that literal physical packet typing is open, and a
later status comment says that complete terminal/collar/common-port typing
remains open.  Another PR #439 synthesis comment says that the finite Lorenz
determinant remains uncertified.  These durable statements are incompatible
with treating the agent summary as an already deposited complete theorem.

PR #424 does contain substantial later native-row work, including `L-91559` and
candidate composition `T-91561`, but it is a separate branch with a different
architecture and frozen inputs.  No exact manifest makes PR #424 part of the
advertised `T-91651` theorem.

### 1.2 Consequence of the missing deposit

This review distinguishes three objects:

1. the mathematical formulas stated in the user-supplied summary;
2. the closest durable supporting theorems currently in the repository;
3. the claimed complete theorem `T-91651`, which is absent.

The first two can be reviewed.  The third cannot receive `VERIFIED`, `FALSE`,
or even a stable line-by-line theorem classification until it exists at an
exact SHA.

## 2. Exact parts of the repair that survive review

### 2.1 The reviewer firewalls are correctly accepted

The summary correctly accepts all four failures found in PR #431:

```text
untruncated formal prefixes cannot replace causal prefixes;
hidden hazard coordinates cannot be observed as canonical children;
source mass does not multiply an arbitrary signed endpoint deficit;
a vanishing inherited child does not type the remaining frontier.
```

This is the right proof boundary.  Any repaired theorem must continue to cite
these as mandatory firewalls rather than describing `T-91304` as merely needing
notation changes.

### 2.2 Exact provenance coefficient identity

Let

\[
r_i=p_i^{-1/2},\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad
\lambda_i=r_i s_{i-1},\qquad
\alpha_i=r_i\lambda_i.
\]

Then

\[
s_k+\sum_i\lambda_i=1.
\]

For a base generator and causal difference

\[
\mathsf C_i
=\mathsf A_X-r_i\mathsf A_{X/p_i},
\]

the proposed identity

\[
\mathsf A_X
=s_k\mathsf A_X+
\sum_i\lambda_i\mathsf C_i+
\sum_i\alpha_i\mathsf A_{X/p_i}
\]

is exact after expansion, because

\[
-\lambda_i r_i+\alpha_i=0.
\]

Moreover

\[
\sum_i\alpha_i
=\sum_i r_i\lambda_i
\le r_1\sum_i\lambda_i
<67^{-1/2}<\frac18.
\]

This is the strongest clean advance in the proposal.  It is an actual
coefficient of an actual child term in an exact packet identity, not a hidden
ledger fraction and not an assumed multiplier of a signed loss.  The durable
`L-91355` proves the same algebraic budget at the current PR #439 head.

**Verdict:** `VERIFIED`.

### 2.3 Formal causal target and score positivity

For an active source quotient `u>=p`, with `r=p^{-1/2}`,

\[
T(u)=4\sqrt u-3,\qquad S(u)=5\sqrt u-3.
\]

Since

\[
r\sqrt{u/p}=r^2\sqrt u,
\]

the differences are

\[
T(u)-rT(u/p)
=4(1-r^2)\sqrt u-3(1-r)>0,
\]

\[
S(u)-rS(u/p)
=5(1-r^2)\sqrt u-3(1-r)>0,
\]

and

\[
[S-rS_{\rm child}]-[T-rT_{\rm child}]
=(1-r^2)\sqrt u>0.
\]

These signs are exact.

For any endpoint-monotone positive row family,

\[
Q_u-rQ_{u/p}
=[Q_u-Q_{u/p}]+(1-r)Q_{u/p}\ge0.
\]

The same inference is valid for ordinary and radix-four response vectors once
their native endpoint monotonicity is proved.  `L-91559` on PR #424 gives a
substantial exact identity-embedding theorem for the component-row ordinary and
radix-four targets.

**Verdict:** the displayed formulas are `VERIFIED`; the assertion that they
already form a complete typed packet, including every imported port and root
normalization, remains a producer obligation.

### 2.4 Literal component entropy tail

The literal component entropy is

\[
\mathcal E(u)
=\sum_{2\le m\le u}
\frac{\log m}{\sqrt m}\log\frac um.
\]

Put

\[
D(u)=\mathcal E(u)-(5\sqrt u-3).
\]

On `N<u<N+1`,

\[
D'(u)=\frac1u\sum_{m=2}^{N}
\frac{\log m}{\sqrt m}-\frac5{2\sqrt u}.
\]

The integral estimate used in the summary is ample for every `N>=67`, so
`D'(u)>0` above the base.  I independently evaluated the base expression:

\[
\mathcal E(67)=39.2031645789\ldots,
\]

\[
5\sqrt{67}-3=37.9267638594\ldots,
\]

and therefore

\[
\boxed{D(67)=1.2764007195\ldots>0.}
\]

The sign required by the proposed route is correct.

There is a repository correction to record: durable `L-91553` reports
`D(67)>3.2764`.  That number corresponds to subtracting `5sqrt(67)-5`, not the
stated `5sqrt(67)-3`.  The margin is misstated by exactly `2`, although the
load-bearing positivity survives.

For an active causal generator,

\[
D(u)-rD(u/p)
\]

is nonnegative when `u/p>=67`, because `D` is increasing and `0<r<1`; when
`u/p<67`, it is bounded below by an absolute finite-window constant.  Thus the
local literal-score debt mechanism is mathematically plausible and can be made
uniform.

**Verdict:** `VERIFIED WITH NUMERICAL CORRECTION`.

### 2.5 Actual packet deficits, not source fractions

For a fully typed physical packet `P`, let

\[
\Delta_X(P)=J_X(P)-
\sup_{d\in\mathcal F_X(P)}\mathcal S_X(d).
\]

If `J_X`, every capacity/port map, and score are linear, then

\[
\Delta_X(cP)=c\Delta_X(P),\qquad c\ge0,
\]

and Minkowski addition of feasible packings gives

\[
\Delta_X(P+Q)\le\Delta_X(P)+\Delta_X(Q).
\]

This is exact and is durably proved in `L-91406`.  The corresponding abstract
packet-envelope theorem `T-91401` is also correct: once a concrete reset
producer gives bounded local debt and substochastic child certificate mass,
the envelope recurrence follows without ever replacing a restricted packet by
a source-mass fraction of a preferred packet.

With the stronger child mass bound `rho<1/8`, the formal recurrence

\[
\Lambda(X)\le C+\rho\Lambda(X/67)
\]

indeed gives

\[
\Lambda(X)\le\frac C{1-\rho}<\frac{8C}{7}.
\]

**Verdict:** `VERIFIED ABSTRACTLY`; concrete packet typing remains required.

## 3. First load-bearing gap: certificate algebra versus physical packet equality

The summary defines a **free positive cone** generated by labelled
`mathsf A` and `mathsf C` atoms and retains provenance so physically dependent
images are not identified.  It then writes the causal decomposition as an exact
packet equality.

Those two statements require an explicit distinction.

In the free certificate cone, the coefficient vector on the left is not equal
to the coefficient vector on the right.  Indeed, the left certificate mass is
`1`, while the right certificate expression has current mass

\[
s_k+\sum_i\lambda_i=1
\]

plus recursive child mass `sum alpha_i>0`.

The equality holds only after applying a physical realization map that expands

\[
\mathsf C_i\mapsto
\mathsf A_X-r_i\mathsf A_{X/p_i}.
\]

A rigorous version should define:

```text
hat C_X       free provenance-labelled certificate cone;
R_X           linear realization into native physical packets;
m_hat         additive certificate mass;
Delta_hat(C)  := Delta_X(R_X C).
```

Then the reset is an `R_X`-identity or a production rule, not equality inside
the free cone.  Homogeneity/subadditivity apply to `Delta_hat` because `R_X` is
linear, while mass is computed on the chosen certificate representation.

Without this diagram, either:

1. the cone is free and the displayed equality is false in that cone; or
2. the cone is quotiented by physical equality and the proposed mass may depend
   on the chosen representation.

This is repairable, but it is not cosmetic: the envelope is defined using the
mass, while the deficit is defined using the physical realization.

**Verdict:** `NEEDS A FORMAL CERTIFICATE-REALIZATION THEOREM`.

## 4. Second load-bearing gap: no complete typed causal packet is deposited

Coordinatewise positivity of target, declared score, `Q`, ordinary response,
and radix-four response is necessary but is not by itself the complete input of
`L-91406/T-91401`.

For every generator, the producer must define linearly and at one exact SHA:

```text
benchmark J_X(P);
full ordinary and radix-four capacity vector;
all endpoint/collar/common-port capacities;
source and tail-prime provenance;
feasible packing cone F_X(P);
physical score functional;
endpoint-to-RH root comparison.
```

It must then prove that the realized causal difference is an admissible positive
typed packet in that system.  The summary leaves several of these as independent
review obligations, especially common endpoint ports and finite collars.

The closest durable theorem, `L-91355`, explicitly marks causal residual packet
typing as open.  PR #439's current body likewise says literal physical packet
typing is open.  PR #424's `L-91559` proves an important native row/detail
embedding, but it does not by itself instantiate the advertised provenance cone,
its mass, every port, and its root benchmark.

**Verdict:** `UNPROVEN / PRODUCER GAP`.

## 5. Third load-bearing gap: the claimed root mass bound is not a complete root ledger

The estimate

\[
m(P_{\rm root})\le54
\]

uses the residual Hall coefficients

\[
0\le\nu(e)=r_e/W_S(e)\le1
\]

on fewer than 55 root nodes.  This controls the coefficient mass of the residual
base atoms.  It does not automatically account for the complete root object,
which also contains or invokes:

```text
Hall transport-edge packets;
interval/butterfly lifts;
unused target capacity;
finite mismatch and B-spline collar;
terminal omission;
common endpoint ports and boundary charges.
```

The proposal may legitimately keep nonrecursive pieces outside recursive mass,
but then it must prove one exact root inequality

\[
\Delta_X(P_X^{\rm native})
\le C_{\rm root}+\Delta_X(P_{\rm root}^{\rm recursive})
\]

with `C_root=O(1)` and no duplicated target or port.  It must also prove the
native endpoint bridge

\[
F_\Lambda(X)
\le\Delta_X(P_X^{\rm native})+O(1)
\]

under the same normalization.

No deposited `T-91651` file supplies this full ledger.  The summary itself lists
the collar/common-port and endpoint-consumer checks as outstanding independent
obligations.

**Verdict:** `UNPROVEN / ROOT NORMALIZATION GAP`.

## 6. Cone closure and recursion scope

For the envelope supremum to be meaningful, every mass-one certificate in the
chosen cone must admit the asserted reset or a bounded terminal treatment.
A reasonable construction is:

```text
A generators: decompose by the causal identity;
C generators: retain entirely as current packets and pay bounded local debt;
tail children: re-enter only as A generators with advanced prime index.
```

This appears compatible with the summary and avoids reintroducing excluded
primes.  It should nevertheless be stated as a closure theorem.  In particular,
the reset must cover arbitrary positive sums, countable limits if used, all tail
indices, and endpoint ranges below the base.

**Verdict:** `PLAUSIBLE BUT NOT DURABLY STATED`.

## 7. Route B: large-prime Lorenz determinant

The advertised file

```text
L-91651-large-prime-lorenz-determinant-has-positive-leading-term.md
```

is absent from PR #439 at its current head.  The durable PR #439 synthesis says
that the finite determinant

\[
\mathfrak D_j(p,y)
=E_R^{(j)}O_S-E_SO_R^{(j)}
\]

remains open.

The asymptotic sign mechanism in the summary is credible:

```text
a_j<0;
V_eU_o-U_eV_o<0;
therefore the displayed leading coefficient is positive.
```

But a positive formal leading term is not yet a uniform theorem over
`1<=y<=67`, `2<=j<=66`.  A complete result requires:

1. a rigorously uniform Euler--Maclaurin remainder;
2. an explicit effective `P_0` valid for every row and child parameter;
3. a directed certificate for every prime/cell below `P_0` with both parent and
   child causal activation surfaces;
4. insertion of the resulting literal Lorenz packet into the same complete
   native capacity and root ledger.

The summary itself acknowledges that the finite determinant certificate remains
open.  Consequently Route B is valuable backup mathematics, not a completed RH
proof.

**Verdict:** `PROMISING ASYMPTOTIC ROUTE / FINITE LOAD-BEARING GATE OPEN`.

## 8. Strongest correct proof DAG at the cutoff

```text
PR #431 exact firewalls
  -> accepted and retained                                      VERIFIED

causal coefficient construction
  -> physical realization identity                             VERIFIED
  -> total recursive certificate mass <1/8                     VERIFIED

component endpoint monotonicity
  -> causal Q / ordinary / radix-four differences >=0          VERIFIED LOCALLY

literal component entropy
  -> D(67)=1.2764007195...>0                                   VERIFIED
  -> bounded causal local score debt                           VERIFIED IN PRINCIPLE

linear typed packet deficits
  -> homogeneity and subadditivity                             VERIFIED ABSTRACTLY
  -> abstract envelope contraction                             VERIFIED CONDITIONAL

missing arrows:
  free certificate -> completely typed native packet           OPEN
  all ports/collars -> one bounded current/root ledger          OPEN
  root Hall coefficients -> complete bounded root packet mass   OPEN
  native root deficit -> endpoint RH consumer                   OPEN / IMPORT AUDIT
  immutable T-91651 dependency graph                            ABSENT

therefore:
  Lambda(X)=O(1)                                                CONDITIONAL
  endpoint loss=o(log^2 X)                                     CONDITIONAL
  RH                                                            UNPROVEN
```

## 9. Exact disposition

```text
reviewer's four objections                            VERIFIED
historical T-91304                                    REJECTED
causal identity                                       VERIFIED
sum recursive coefficients <1/8                      VERIFIED
formal target/score causal surplus                    VERIFIED
component-row causal positivity                       VERIFIED FROM MONOTONICITY
ordinary/radix-four causal positivity                 VERIFIED WHERE L-91559 APPLIES
D(67)>0                                               VERIFIED; margin is 1.2764..., not 3.2764...
literal tail monotonicity                             VERIFIED
packet deficit homogeneity/subadditivity              VERIFIED ABSTRACTLY
certificate mass + physical realization compatibility NEEDS FORMALIZATION
complete native causal packet typing                  OPEN / NOT DEPOSITED
complete root mass and one-use debt                   OPEN / NOT DEPOSITED
T-91651 full composition                              ABSENT / UNREVIEWABLE AS A FILE
large-prime L-91651 Lorenz theorem                    ABSENT AT PR #439 HEAD
finite Lorenz determinant                             OPEN
Riemann Hypothesis                                    UNPROVEN
```

## 10. Required repair packet before another proof-level review

A reviewable proposal should be deposited on one immutable branch with:

1. the exact `T-91651` theorem and all `R/L/O/X-9165x` dependencies;
2. a machine-readable path/blob-SHA manifest;
3. an explicit certificate cone, realization map, mass, benchmark, capacities,
   ports, score, and deficit;
4. a theorem that every `A` and `C` generator is a complete admissible native
   packet;
5. one root Hall/collar/port identity with a complete mass/debt bound;
6. a frozen replay record and hashes for every finite certificate;
7. an exact root comparison to the endpoint-score RH consumer;
8. for Route B, an effective uniform remainder and finite determinant replay.

Once those exist, the central mathematical question is sharply isolated and
worth a fresh hostile reconstruction.  Until then, the advertised theorem is a
serious blueprint rather than a deposited proof.

## 11. Final conclusion

\[
\boxed{
\text{The provenance-causal idea successfully repairs the old scalar-loss architecture.}
}
\]

\[
\boxed{
\text{Its exact }<1/8\text{ coefficient contraction is genuine and valuable.}
}
\]

\[
\boxed{
\text{At the frozen repository state, however, }T\text{-}91651
\text{ is absent and the concrete producer/root interfaces remain unproved.}
}
\]

Therefore neither the advertised proposal nor the current repository state
establishes the Riemann Hypothesis.
