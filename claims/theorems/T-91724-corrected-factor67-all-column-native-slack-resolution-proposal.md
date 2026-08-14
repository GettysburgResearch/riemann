# T-91724 — Corrected factor-67 all-column native-slack resolution proposal

Claim ID: `T-91724`  
Status: **CANDIDATE CORRECTED SONTR / NATIVE-SLACK / RH COMPOSITION ON FROZEN INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-15  
Frozen base: PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`  
Review input: PR #480 at `d6d9c051abb20a47f3ce7adb45de33bfc2b933b9`  
Additional inputs: `L-91378`, `L-91650`, `L-91658`, `L-91690`, `L-91723--L-91730`  
RH status: **unproved pending independent reconstruction**

## 1. Frozen review accepted

The corrected proof accepts every fatal objection in PR #480 against frozen PR
#476.  It does not use an `O(1)` equality-score recurrence, does not leave
`q<K` untreated, does not infer target contraction from coefficient mass alone,
and does not interpolate across activation knots.

## 2. Source-owned factor-67 packet

Put

\[
 K=\left\lfloor X/67\right\rfloor+1.
\]

The frozen factor-67 root theorem gives one target-exact positive Hall residual,
score superordination, simultaneous nonnegative row bonuses and unique rough
first ownership.  Apply the aggregate causal split while complete labels remain
present.  Its global coefficients satisfy

\[
 \boxed{\rho:=\sum_i\alpha_i<67^{-1/2}<\frac18.}
 \tag{T-91724.1}
\]

`L-91726` proves the actual weighted target statement

\[
 \boxed{
 \sum_i\alpha_i m(U_{p_i}P_{X/p_i})
 <\frac18m(P_X),
 }
 \tag{T-91724.2}
\]

fiberwise and after positive endpoint integration.  Complete placement labels
remain inside the child fields.

## 3. All physical columns, knots and port

PR #479 partitions adjacent carry cells by their actual owner and proves for all
`q>=2` an all-column square-root reserve after

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

Every nonterminal detail column has reserve at least

\[
 \frac{\Omega_X(q)}{\sqrt K+130},
\]

and the terminal annulus has margin `581X^-3/2`.  Activation-knot collars are
removed from an atomless positive endpoint measure before the split; positive
same-cell refinement is native-relative on the retained cells.  `L-91729`
chooses the refinement so that the final reserve satisfies

\[
 \boxed{
 \operatorname{Reserve}^{\rm final}
 >10152\|C\|\varepsilon_X.
 }
 \tag{T-91724.3}
\]

One uncolored common root port remains, and children carry zero port.

## 4. Exact packet-native capacity identity

Let `P_X` be the common positive realized parent packet before feasible child
rows are inserted.  `L-91730` applies the two ordinary maps before forming
detail and proves one nonnegative root slack `r_X` with

\[
 \boxed{
 \Omega_X=\Xi(c_X)+r_X+
 \int_Ba(b)U_b\Omega(P_b)\,d\nu(b).
 }
 \tag{T-91724.4}
\]

Each child owns its actual packet capacity once.  No native root capacity is
copied.

For arbitrary feasible child rows, `L-91727` gives

\[
 \boxed{
 s_X=r_X+
 \int_Ba(b)U_bs_b\,d\nu(b)
 }
 \tag{T-91724.5}
\]

and the exact native scalar cocycle

\[
 \boxed{
 \Delta_X:=J_\Lambda(X)-\mathcal H(d_X)
 =\delta_X+
 \int_Ba(b)\Delta_b\,d\nu(b),
 \quad \delta_X=\langle Y_4,r_X\rangle.
 }
 \tag{T-91724.6}
\]

## 5. Local native cost

`L-91728` uses the exact sparse support of `Y_4` and PR #479's all-column bound.
The all-column mismatch/collar and knot-refinement costs are `o(1)`.  The common
square-root thinning has native cost below `4290 log X`.  On the frozen
fixed-width/base/port inputs the remaining cost is `O(1)`.  Thus

\[
 \boxed{
 \delta_X\le A_0+4290\log(2X).
 }
 \tag{T-91724.7}
\]

This is the proof-relevant local scalar.  No estimate of
`4sqrt(X)-H(d_X)` occurs.

## 6. Subcritical native recurrence

Normalized same-index placement preserves the numerical native deficit.  From
(T-91724.1), (T-91724.6) and (T-91724.7),

\[
 D(X)\le A_0+4290\log(2X)+\rho D(X/67+1),
 \qquad \rho<\frac18.
 \tag{T-91724.8}
\]

Iteration yields

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =O(\log X)=o(\log^2X).
 }
 \tag{T-91724.9}
\]

The direct coefficient recurrence proves the native endpoint bound; the
weighted target theorem independently verifies the Hereditary Typed Reset
normalization.

## 7. Endpoint and safe-Xi consequences

The resident one-sided endpoint theorem consumes exactly (T-91724.9).  If the
frozen factor-67 Hall, all-column realization, fixed terminal/base/port and
endpoint-consumer inputs survive independent reconstruction, it gives the
proposed implication to RH.

Only after that conclusion, `L-92114` gives positive definiteness of every finite
safe-Xi Hankel pair.  It is a downstream corollary.

## 8. Immediate falsifiers

Reject at the first failure of:

```text
factor-67 target Hall or target-normalized row monotonicity;
one aggregate causal list with sum <1/8;
SHARP target nonexpansiveness L-91726;
all-column adjacent-cell ownership PR #479;
activation-knot relative refinement PR #479;
one uncolored common port;
packet-capacity identity L-91730;
fixed top/base/port native cost in L-91728;
same-index native-deficit covariance;
one-sided native endpoint orientation.
```

```text
PR #480 frozen review                         ACCEPTED
old equality-score recurrence                 REJECTED
small columns q<K                             REPAIRED
activation-knot refinement                    REPAIRED
actual weighted child target <1/8             PROVED
packet-native capacity/slack cocycle           PROVED
local native root cost O(log X)                PROPOSED COMPLETE / REVIEW
corrected native deficit O(log X)              CANDIDATE COMPLETE
endpoint implication                          FROZEN / RECONSTRUCT
safe-Xi Hankel positivity                     RH COROLLARY
Riemann Hypothesis                            UNPROVED PENDING REVIEW
```
