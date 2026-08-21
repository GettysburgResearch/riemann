# Frozen-head review of PR #455 — single-SHARP direct native-row factor-67 proposal

Review status: **REQUEST CHANGES / FINAL CONCLUSION DOES NOT SURVIVE**  
Repository: `gfreund123/riemann`  
Review cutoff: `2026-08-14T12:39:10Z`  
Reviewer branch: `review/pr455-single-sharp-hall-prefix-20260814`

## 1. Frozen target

```text
main SHA:                 9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
proposal PR:              #455
proposal base branch:     research/gpt56-pro/91663-direct-root-review-response
proposal base SHA:        f41797c91497dc462f549a127d8494bbe4ccde2f
proposal head branch:     research/gpt56-pro/91666-full-direct-row-closure
proposal head SHA:        1b502acbe511776178da3dc916e3cd3464cd5e77
normative content commit: c696d2a356eeacb3097d4ea6cc727b84548d7a03
manifest-v2 blob:         30b4a3d163de1e04972419bc91e5990a08089c56
handoff blob:             090cf5d086bf32fbd735ae325a859ebf7907f662
final-lock blob:          3aa11e1c1dde20401dd7e324a15696d5403ab3f4
review predecessor:       PR #457 / e136fcf42fbab1195fc193e64ce4039d1a1d416c
```

The proposal head and main were re-read at the cutoff and had not moved. Main is
not treated as the scientific state of the proposal.

## 2. Review method

I reconstructed the successor chain rather than relying on the PR summary. The
review covered `R-91659`, `L-91670`, `L-91671`, and `T-91656`, plus
the frozen dependencies governing:

```text
single-SHARP source recursion and row observation;
P_61 one-prime parent/child variables;
binary survival/hazard target, score, and row budgets;
target-Hall existence and Hall disintegration;
source-disjoint stopping-line assembly;
same-index child replacement;
fixed-67 score telescope;
finite/continuum mismatch and equality score.
```

I inspected the v2 manifest, final lock, hardening replay, and predecessor
review. The new falsifier was replayed with rational interval arithmetic in
`X-91672`. The expensive historical certificates were not rerun wholesale;
that is not decisive because the rejection uses one explicit necessary Hall
prefix with a large negative exact margin.

## 3. Executive verdict

The repair genuinely fixes the predecessor's factor-three error. It also
correctly separates the declared continuum score \(4\sqrt X\) from the literal
finite score \(P_\Lambda(X)\), and it supplies the exact finite-seed map to
\(c_X\).

The full proposal nevertheless fails at the next load-bearing interface. The
frozen Hall certificate is a bounded reset-window theorem, but the successor
applies it to stopped parent packets whose endpoint is \(x=py\). For the
admissible leaf

```text
p = 67
y = 13
x = py = 871
t = 13
```

the survival target's necessary no-upward Hall prefix is

\[
\mathcal H_{s,13}(871)<-2.1395<-2.
\]

Therefore the asserted Hall transport does not exist. In fact the same prefix
fails for every prime \(p\ge67\) at \(y=13\). This blocks the positive residual
sources, the positive complete parent row, the equality-deficit recurrence, and
the logarithmic native-loss conclusion.

**PR #455 is not a proof of RH.**

## 4. Finding 1 — P0: stopped-parent survival Hall is false as applied

### 4.1 Frozen target atom

With

\[
r=p^{-1/2},\qquad
\alpha_s=\frac{2(r+2)}{r+3},\qquad
g_s=(1-r)(r+3)>0,
\]

the survival target in `L-91556/L-91562` is

\[
T_s(x,n)
=g_s n^{-1/2}(\alpha_s\sqrt{x/n}-1)
=g_s w_{\alpha_s}(x,n).
\]

The preferred `P_61` packet in `O-91310/L-91560` has

\[
x=py,\qquad p\ge67,\qquad1\le y<67,
\]

with parent-index coefficients \(\mu(d)\) for \(d\mid P_{61}\). `L-91554`
fixes the incoming Hall coefficients at one.

### 4.2 Necessary prefix condition

A transport supported on `e<=o` must satisfy, for every odd threshold \(t\),

\[
\sum_{\substack{e\le t\\mu(e)=1}}T_s(x,e)
\ge
\sum_{\substack{o\le t\\mu(o)=-1}}T_s(x,o).
\]

After removing \(g_s>0\), the prefix is

\[
\mathcal H_{s,t}(x)=\alpha_s\sqrt x A_t-B_t,
\]

where

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

### 4.3 Exact counterexample and infinite family

Set \(p=67\), \(y=t=13\), and \(x=871\). All \(d\le13\) are active because

\[
p^{-1/2}\sqrt{x/d}=\sqrt{13/d}\ge1.
\]

Also

\[
A_{13}=-\frac{2323}{30030}.
\]

`X-91672` gives

\[
-2.139513718150116
<\alpha_s\sqrt{871}A_{13}-B_{13}
<-2.139513718150115.
\]

This is a necessary capacity inequality, so no Hall matching can repair its
wrong sign. Moreover \(A_{13}<0\), \(\alpha_s>4/3\), and
\(\sqrt{13p}\ge\sqrt{13\cdot67}\), while

\[
\frac43\sqrt{13\cdot67}A_{13}-B_{13}<-2.0799.
\]

Hence the failure holds for every prime \(p\ge67\), not only the smallest leaf.

### 4.4 Certificate-domain mismatch

`L-91550` certifies the relevant Hall corridors only on

\[
1\le x<55.
\]

The bounded child quotient is \(y\), but the controlled parent target and row
are evaluated at \(py/d\). Substituting \(y\) for \(py\) changes the target and
is not an identity in `L-91560`.

The abstract theorem `L-91545` survives. Its Hall-transport hypothesis fails
in this application.

### 4.5 Downstream impact

```text
L-91621: positive leafwise Hall output                    BLOCKED
L-91545 application: residual survival source            BLOCKED
L-91663: positive complete parent row                     BLOCKED
L-91671: one-use parent ownership and deficit recurrence  BLOCKED
T-91656: d_X and O(log X) native loss                     REJECTED
```

## 5. Finding 2 — P1: finite row margin is promoted beyond its certificate

`L-91670` says `L-91322` gives

\[
M_1>\frac1{20}
\]

at every activation-cell right endpoint. The cited checker covers only
\(2\le j\le N\le54\). At

\[
N=71,\qquad j=70,\qquad Y=72,
\]

`X-91672` proves

\[
0<M_1<0.049925670420019<\frac1{20}.
\]

Thus the promoted global numerical margin and the proof using it are false
outside the frozen window. This probe remains positive, so the review does not
claim a counterexample to global normalized-row monotonicity itself.

Any successor must prove row positivity on the actual domain of its Hall edges.

## 6. Finding 3 — P1: the hardening replay omits the decisive producer

The advertised replay

```text
PASS_SINGLE_SHARP_NORMALIZATION_HARDENING
```

correctly checks the factor-three diagnosis, one-copy atom algebra, finite-seed
Fubini, formal prime-log convolution, and coefficient-one deficit identity. Its
own scope says:

```text
expensive_hall_cells_replayed: false
outer_endpoint_certificate_replayed: false
```

Therefore its hash does not certify the Hall application rejected here.

## 7. Mathematics that survives

### 7.1 Single-SHARP normalization — verified exact

The historical two-channel coefficients sum to three. The successor instead
uses

\[
w_\Psi=3w_{4/3},\qquad
\mathcal H_{\Psi,j}(Y)=\frac{Q_Y(j)}{4\sqrt Y-3},
\]

and obtains exactly

\[
w_\Psi(X,n)\mathcal H_{\Psi,j}(X/n)
=n^{-1/2}Q_{X/n}(j).
\]

### 7.2 Finite equality seed to \(c_X\) — verified exact

Finite Fubini and linearity give

\[
b_X^\star(n)=\sum_{k\le X}\frac{\mu(k)}{\sqrt k}S_{X/k}(n),
\qquad
\mathcal R[b_X^\star](j)=c_X(j).
\]

The continuum seed remains distinct through

\[
b_X^\star=\overline b_X^\star+E_X,
\]

consistent with `R-91102`.

### 7.3 Score typing — verified

The successor does not identify

\[
P_\Lambda(X)=\mathcal S(c_X)
\quad\text{with}\quad
4\sqrt X.
\]

Its equality deficit and native benchmark loss are algebraically separated in
the correct order.

### 7.4 Same-index child replacement — verified conditionally

For an already-produced positive parent row and canonical child,

\[
d_X=R_X^{\rm par}-R_X^{\rm ch}+d_K
\]

is an exact simultaneous ordinary/detail capacity comparison. Finding 1 blocks
the production of the required positive \(R_X^{\rm par}\), not this conditional
identity.

### 7.5 Fixed-67 and endpoint-score inputs — no new objection

I found no new counterexample to the frozen fixed-67 entropy theorem, the
finite/continuum mismatch decomposition, or

\[
J_\Lambda(X)<4\sqrt X+4\log X.
\]

Their final use is blocked upstream.

### 7.6 Freeze — inspected v2 objects are consistent

The v2 manifest names the corrected content commit and the new single-SHARP
objects. The final lock is self-excluding and does not claim mathematical
validation. The predecessor's stale-manifest defect did not recur in the
inspected v2 objects.

## 8. Claim-status verdict

```text
PR #457 factor-three objection                         VERIFIED / ACCEPTED
R-91659                                                VERIFIED
single-SHARP local atom normalization                 VERIFIED EXACT
finite equality seed -> c_X                           VERIFIED EXACT
continuum/finite score distinction                    VERIFIED
same-index child replacement                          VERIFIED CONDITIONAL
fixed-67 theorem                                      SURVIVES THIS REVIEW
stopped-parent target Hall producer                   FALSE AS APPLIED
L-91670 global 1/20 row margin                        FALSE
positive complete parent row                          NOT ESTABLISHED
L-91671 equality-deficit recurrence                   BLOCKED
T-91656                                                REJECTED AS PROOF
Riemann Hypothesis                                    UNPROVEN
```

## 9. Minimal repair target

The exact single-SHARP normalization should be retained. The next producer gate
is:

> For every `p>=67`, every `1<=y<67`, and every active parent-index prefix
> of the `P_61` packet, construct a positive target/score/row decomposition at
> `x=py`; or replace the parent Hall step by a bounded-child construction with
> a proved exact ledger back to `Q_(py/d)`.

A successor must directly defeat the `y=13,t=13` family, prove normalized-row
positivity on its actual edge domain, and replay the complete producer rather
than only the atomwise normalization.

## 10. Review artifacts

```text
claims/refutations/R-91660-stopped-leaf-survival-hall-prefix-fails.md
experiments/X-91672-stopped-leaf-hall-prefix-counterexample/README.md
experiments/X-91672-stopped-leaf-hall-prefix-counterexample/verify.py
experiments/X-91672-stopped-leaf-hall-prefix-counterexample/results/verification.json
audits/integration-wave/20260814-pr455-single-sharp-claim-status.md
integration/2026-08-14/pr455-single-sharp-final-review-handoff.md
```

Replay verdict:

```text
PASS_PR455_STOPPED_LEAF_HALL_PREFIX_COUNTEREXAMPLE
d010a2ec2e1efa95efa98c237958a25166ae486381c6ace5d633d5f2016bace1
```

No proposal branch was modified and no theorem was integrated into main.
