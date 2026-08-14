# Independent review of PR #451 — direct native-row response to PR #450

## Frozen review state

```text
Review cutoff:   2026-08-14T04:09:40Z
Repository:      gfreund123/riemann
Main at review:  9c7538559d7f56c2914b39aed5a1fb3fbf7ce131

Reviewed PR:     #451
Base branch:     research/gpt56-pro/91661-corrected-provenance-closure
Base SHA:        d44c45b3ececa878296914a49e49279b10a1f637
Head branch:     research/gpt56-pro/91663-direct-root-review-response
Head SHA:        f41797c91497dc462f549a127d8494bbe4ccde2f
State at review: open / draft / mergeable
```

No movement of the reviewed head was observed during the review or the final pre-deposit recheck.

## Executive verdict

\[
\boxed{\text{PR #451 is false as written.}}
\]

```text
mathematical type      proposed complete theorem
review verdict         false
first broken arrow     L-91621.12 -> L-91663.9
Riemann Hypothesis     unproved
```

The packet is materially easier to inspect than PR #447. Its new direct ordinary/detail replacement algebra is valuable, and it correctly accepts the central objection from PR #450. However, the Hall assertion used to manufacture the positive parent row has an explicit counterexample inside the proposal's own stopping-line domain.

The packet instructs reviewers to reject it upon the first failed Hall prefix. That falsifier fires at

\[
p=67,\qquad y=13,\qquad t=13.
\]

The exact refutation is deposited as `R-91656`, with a directed replay in `X-91664`.

# 1. Decisive Hall counterexample

## 1.1 Imported certificate scope

`L-91550` defines the no-upward Hall prefix

\[
\mathcal H_{\alpha,t}(x)
=
\alpha\sqrt{x}\,A_t-B_t,
\]

with

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

Its checker has

```python
WINDOW_RIGHT = 55
```

and certifies only the interval `1 <= x < 55`.

## 1.2 Actual parameter on a stopped leaf

`L-91621` permits

\[
p\ge67,\qquad1\le y<67,
\]

and writes the stopped parent row with component endpoints `py/d`. For the survival target, with `r=p^{-1/2}`, restoring the source coefficient gives

\[
\frac{\mu(d)}{\sqrt d}(1-r)
\left[
2(r+2)\sqrt{\frac{py}{d}}-(r+3)
\right].
\]

Therefore the signed prefix is a positive factor times

\[
\mathcal H_{\alpha_s,t}(py),
\qquad
\alpha_s=\frac{2(r+2)}{r+3}.
\]

The Hall parameter is the parent parameter `py`, not the terminal child parameter `y`.

## 1.3 Exact negative prefix

Take

\[
p=67,\qquad y=13,\qquad x=py=871,\qquad t=13.
\]

Then

\[
A_{13}=-\frac{2323}{30030}
\]

and directed rational square-root enclosures prove

\[
-2.140
<
\alpha_s\sqrt{871}\,A_{13}-B_{13}
<
-2.139.
\]

The omitted branch prefactor is positive, and the physical prefix is about

\[
-5.8638417096.
\]

Thus no no-upward survival-target transport exists on this allowed stopped leaf.

For fixed `y=13`,

\[
\alpha_s(p)\sqrt p
=
\frac{2u(1+2u)}{1+3u},
\qquad u=\sqrt p,
\]

has positive derivative. Since `A_13<0`, the prefix decreases with `p`. The counterexample therefore extends to every rough prime `p>=67`, producing arbitrarily large parent endpoints.

# 2. Consequence for the proof DAG

The failed Hall prefix invalidates the universal statement in `L-91621.12`. The positive residual-source and row-bonus identities derived from that transport are unavailable on the counterexample leaf. In particular, the universal positive parent identity

\[
R_{\rm parent}
=
R_{\rm pre}+R_s(c_s)+R_h(c_h)+B_s+B_h
\]

asserted in `L-91663.9` is not established and is false as a universal consequence of the imported Hall theorem.

The exact replacement

\[
d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}
\]

therefore lacks the positive Hall-produced parent row required by the composition. This breaks `L-91665` and `T-91653` before the recurrence can be invoked.

# 3. Mathematics that survives

## 3.1 Exact native response identities

For the positive component row `Q_Y`, the formulas

\[
\Gamma_Y(q)=q^{-1/2}H(Y/q)
\]

and

\[
\Xi_Y(q)
=
q^{-1/2}[H(Y/q)-H(Y/(4q))]
\]

are correct.

For

\[
c_X(j)=\sum_{k\le X}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j),
\]

Möbius convolution gives exactly

\[
\Gamma(c_X;q)=w_X(q),
\qquad
\Xi(c_X;q)=\Omega_X(q).
\]

**Review status:** `VERIFIED`.

## 3.2 Same-index child replacement

Assume one already has a genuine positive canonical parent row, its canonical child row, and a child-feasible replacement. Then

\[
\Gamma(R_{\rm parent}-R_{\rm ch}+d_{\rm ch})
\le
\Gamma(R_{\rm parent})
\]

and

\[
\Xi(R_{\rm parent}-R_{\rm ch}+d_{\rm ch})
\le
\Xi(R_{\rm parent})
\]

are exact.

**Review status:** `VERIFIED CONDITIONALLY`.

This is a real resolution of the algebraic residual-capacity objection in PR #450. It does not construct the positive parent decomposition.

## 3.3 Source provenance before Hall

The least-prime stopping-line decomposition remains a plausible exact source-disjoint identity. No source-duplication counterexample was found. The failure occurs when the signed stopped leaf is projected by the imported Hall theorem.

## 3.4 Corrected P61 constant

The correction

\[
\prod_{q\le61}\left(1+\frac1q\right)
=
\frac{399441300081868800}{86204059532560853}
<
\frac{14}{3}
\]

is exact. The obsolete `9/2` bound fails at `P_61`.

The resident `L-91320` theorem nevertheless retains the colored-to-physical projection as open, so it should be classified as an abstract finite-block/matrix reserve rather than a complete physical port.

## 3.5 Corrected entropy bases

The packet correctly distinguishes

\[
E(67)-(5\sqrt{67}-3)
=
1.2764007195\ldots
\]

from

\[
E(67)-5(\sqrt{67}-1)
=
3.2764007195\ldots.
\]

The historical display was high by two.

# 4. Secondary gaps independent of the Hall refutation

## 4.1 L-91664 is only an index

The claim file contains no derivation of

\[
E(Y)-E(Y/67)
\ge
5(\sqrt Y-\sqrt{Y/67})
\qquad(Y\ge67).
\]

It points to the experiment directory. The retained replay checks the base value and an isolated derivative-control scalar, but does not traverse all activation cells or contain the promised global proof.

A targeted numerical scan found no counterexample, so the inequality appears repairable. At the reviewed SHA it remains a proof gap.

**Review status:** `UNPROVEN / GAP`.

## 4.2 Complete current/inner capacity partition is still missing

`L-91665` names the outer producer, quantization, collar, mismatch, safety factor, omission, terminal annulus, port, Hall row, and child, then declares their one-generation charge to be an absolute constant. It does not display one exact complete-data identity separating outer current capacity from the inner parent/child capacity in every ordinary, radix-four, and boundary coordinate.

A replacement theorem should exhibit a literal identity of the form

\[
c_X
=
R_X^{\rm outer,can}
+
R_X^{\rm inner,parent}
\]

and then prove simultaneous feasibility for

\[
d_X
=
d_X^{\rm outer}
+
R_X^{\rm inner,parent}
-
R_X^{\rm child}
+
d_X^{\rm child},
\]

with every mismatch, collar, omission, annulus, and port charged exactly once.

The normative lock itself lists this reconstruction as mandatory. Hence the old root-complement gap has not yet been replaced by a complete outer-plus-inner ledger.

# 5. Replay audit

The retained verdict

```text
PASS_DIRECT_ROOT_REVIEW_RESPONSE
610eaaced45259d77ccea4a59c10965d070ef1cc8e6b76a79ab1266312f39d6b
```

is a useful regression artifact, but its proof scope is narrower than the theorem:

```text
direct replacement      synthetic rational vectors
Möbius identity         finite divisor-sum replay to 1000
reset recurrence        sample constants 37 and 11
Hall/Fubini replay       randomized abstract leaves
actual Hall checker      only x < 55
outer/current ledger     not replayed
```

The new directed refutation checks the actual stopped-leaf parameter and returns

```text
PASS_PR451_STOPPED_LEAF_HALL_REFUTATION
```

with a strictly negative prefix.

# 6. Standalone-packet audit

The packet improves reviewability by importing frozen claims and scripts under `imports/t91653/` and recording many exact blob identities. It is not fully standalone:

1. The report advertised in the PR body, `reports/gpt56-pro/2026-08-14-pr450-adversarial-response-and-direct-reset.md`, is absent at the reviewed head.
2. The normative lock does not pin the new controlling blobs `L-91663`, `L-91664`, `L-91665`, `T-91653`, or the replay proof-object digest.
3. `L-91664` is not a reviewable theorem file.
4. Several imported claims retain open physical interfaces in their own status boundaries.

# 7. Claim-level disposition

| Claim | Review verdict | Surviving scope |
|---|---|---|
| `R-91655` acceptance of PR #450's `L-91659` objection | **VERIFIED** | Correct scope correction |
| `L-91663.1--.8` response formulas and Möbius collapse | **VERIFIED** | Exact native ordinary/detail identities |
| `L-91621.12` universal stopped-leaf Hall transport | **FALSE** | Counterexample `p=67,y=13,t=13` |
| `L-91663.9` universal Hall-produced positive parent identity | **FALSE** | Depends on failed Hall transport |
| `L-91663.10--.13` replacement algebra | **VERIFIED CONDITIONALLY** | Valid after a true positive parent/child decomposition |
| `L-91664` fixed-67 score inequality | **UNPROVEN / GAP** | Base value verified |
| corrected `P_61<14/3` normalization | **VERIFIED** | Abstract port reserve |
| physical `P_61` port placement | **UNPROVEN / GAP** | Color-to-physical projection open |
| `L-91665` factor-67 reset | **FALSE / GAP** | False Hall input; complete ledger absent |
| `T-91653` RH composition | **FALSE AS WRITTEN** | Direct response algebra survives |
| RH | **UNPROVEN** | No conclusion |

# 8. Integration recommendation

Do not integrate `T-91653`, `L-91665`, or the universal Hall part of `L-91621/L-91663` as proof-level material.

Retain separately:

```text
exact native response/Möbius theorem;
same-index direct replacement inequality;
corrected entropy constants;
P61 < 14/3 normalization;
least-prime source-disjoint decomposition;
R-91656 exact Hall-prefix refutation.
```

The current no-upward Hall producer cannot be repaired by extending its checker from `55` to `67`, because the true parameter `py` is unbounded and the threshold-13 prefix is genuinely negative. A successor needs a different producer: a joint survival-hazard transport, a genuinely contracted normalization, a controlled upward-edge theorem, or a direct non-Hall positivity proof for the stopped packet.

\[
\boxed{
\text{PR #451 does not prove RH; its universal stopped-leaf Hall closure is refuted.}
}
\]
