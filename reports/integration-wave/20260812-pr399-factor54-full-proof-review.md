# Independent review of PR #399: factor-54 shadow-reset full proof proposal

## Review metadata

```text
review cutoff UTC:          2026-08-12T17:28:13Z
repository:                 gfreund123/riemann
base/main SHA:              b837c12199dd407116f604ce6c938039d1a76da4
quoted proposed-proof SHA:  4981bcd2ae05e5a4e41e2877cbf9b4e020081a69
live PR #399 head reviewed: 59b1d1773b0f1d98712d58b66f41202e5f221717
source branch:              research/gpt56-pro/91101-moment-neutral-shadow-transport
review branch:              review/pr399-factor54-full-proof
RH status:                  unproved and undisproved
```

The submitted summary froze `4981bcd2ae05e5a4e41e2877cbf9b4e020081a69` as the complete-proposal head. Before this review began, PR #399 had advanced ten commits to `59b1d1773b0f1d98712d58b66f41202e5f221717`. The drift is mathematically material: the descendant adds a common-Hilbert colligation (`L-91326`) and a positive four-state rough dilation (`L-91327`), and both new files explicitly leave the all-generation linear parity/endpoint/score projection open.

This report therefore distinguishes:

1. the full composition actually claimed at `4981bcd...`; and
2. the strongest corrected live frontier at `59b1d177...`.

No heavy experiment was rerun. The review inspected theorem files, refutations, retained exact-checker source, result scopes, and the branch genealogy. One new exact symbolic counterexample was derived independently and retained separately.

---

# Executive verdict

## Submitted full proposal at `4981bcd...`

\[
\boxed{\textbf{FALSE AS SUBMITTED}}
\]

The decisive failure is exact and load bearing. `L-91319` proves the valid one-factor identity

\[
(1,2)N_p=(1,2)M_p,
\]

but `L-91325` then states that the identity survives arbitrary products of the completed matrices. It does not. For two rough factors with

\[
r=p^{-1/2},\qquad s=q^{-1/2},
\]

the exact difference is

\[
\boxed{
(1,2)N(s)N(r)-(1,2)M(s)M(r)
=\bigl(0,12rs(1-r)(1-s)\bigr)\ne0.
}
\]

Thus the completed cascade does not preserve the claimed native SHARP/source mass. The positive source partition asserted in `L-91325.14` is not obtained, the abstract transport disintegration has no verified arithmetic partition to act on, and the coefficient-one recurrence `L-91325.18` does not follow.

The exact derivation is retained in:

```text
audits/integration-wave/20260812-pr399-exact-completed-cascade-counterexample.md
```

## Live corrected descendant at `59b1d177...`

\[
\boxed{\textbf{UNPROVEN / GAP}}
\]

The descendant does not defend the failed completed-matrix tensorization. Instead it supplies two legitimate replacements:

- a common quadratic Hilbert contraction and defect telescope (`L-91326`);
- a positive four-state parity semigroup with a linear total-variation telescope (`L-91327`).

Those are meaningful advances. They do not complete RH. `L-91326` explicitly leaves positive endpoint-row realization and the coefficient-one score/capacity ledger open. `L-91327` explicitly leaves the recursive parity-projection ledger and bounded all-generation score recurrence open.

## RH

\[
\boxed{\textbf{The Riemann Hypothesis is not established by PR #399.}}
\]

---

# The proposed proof DAG

The claimed chain can be reconstructed as follows.

```text
A. arithmetic two-state source (L,R), Psi=L+2R
   |
   | finite factor-54 parity/Hall/component-row positivity
   v
B. positive local reset packets and contracted rough children
   |
   | signed rough Euler maps M_p
   v
C. entrywise-positive one-prime completions N_p
   |
   | claimed preservation of native source mass through rough cascades
   v
D. positive source partition mu_native=mu_0+sum_b mu_b
   |
   | common Markov-kernel target disintegration
   v
E. non-overlapping target shares nu_b
   |
   | B-spline quantization + affine real-column covariance
   v
F. one physical feasible endpoint vector at every column
   |
   | one global safety factor and one top omission
   v
G. coefficient-one score-loss recurrence
      L_X <= L_K + O(1), K<=c_0X+O(1)
   |
   | iteration
   v
H. L_X=O(log X)=o(log^2 X)
   |
   | PR #352 / T-91101 conditional consumer
   v
RH
```

The first false arrow is `C -> D`: the completed matrices do not preserve the native source functional through a multiprime cascade. Independent gaps also remain at `D -> E/F` and `F -> G`.

The live corrected descendant replaces `C -> D` by:

```text
positive four-state parity semigroup
  -> linear total-variation defect telescope
  -> [OPEN] explicit factor-54 parity projection into endpoint rows,
            residual contracted state, physical detail capacity,
            and bounded score debt
  -> coefficient-one recurrence
  -> RH conditionally
```

---

# Detailed claim review

## 1. `L-91108`: the scalar two-state identity

### Statement reviewed

\[
\Psi=L+2R.
\]

### Verdict

```text
mathematical type:  ROUTE INFRASTRUCTURE
review verdict:     VERIFIED at scalar-function scope
```

The algebraic identity follows directly from

\[
L=2\sqrt{x}B-A,\qquad R=\sqrt{x}B-A,
\qquad \Psi=4\sqrt{x}B-3A.
\]

The two positive renewal equations and finite reset-window positivity are separate claims. Nothing in the scalar identity alone identifies `L` and `R` with one and two copies, respectively, of the same factor-four endpoint probability law.

### Critical scope correction

`L-91325` defines

\[
\mathfrak B(L,R)=(L+2R)\mu_Y
\]

and calls this the exact native source-block measure. The equality `Psi=L+2R` proves an arithmetic scalar identity. It does not by itself prove the physical measure typing

```text
one unit of L = one copy of mu_Y,
two units of R = two copies of mu_Y,
```

at every branch, endpoint scale, parity state and Schur correction. That identification needs an explicit source map. It is not resident in `L-91108`.

Verdict on the stronger source-measure identification:

```text
UNPROVEN / GAP
```

---

## 2. `L-90028`: factor-four monotone transport

### Surviving statement

Given the factor-four source law `Y` and capped-Gamma target law `H`, the file proposes and explicitly constructs the stochastic-order relation

\[
Y\le_{\rm st}H
\]

and hence a positive Markov kernel `K(y,dh)` supported on `h>=y` carrying the source law to the target law.

### Verdict

```text
mathematical type:  ROUTE INFRASTRUCTURE
review verdict:     VERIFIED WITH FIXES at continuum-kernel scope
```

The tail formulas and one-dimensional quantile-coupling implication are coherent. The result supplies a positive continuum transport. It does not supply a finite packet realization or a branch partition. Its own proof boundary says those remain open.

The transport becomes useful for colors only after an exact positive source decomposition has been independently established.

---

## 3. `L-91110`: positive martingale B-spline quantization

### Surviving statements

The local nearest-neighbor state interpolation has:

- nonnegative weights;
- exact preservation of the two endpoint modes;
- exact inherited-bulk reproduction;
- a width-three moving collar;
- score majorization in the favorable direction.

### Verdict

```text
mathematical type:  ROUTE INFRASTRUCTURE
review verdict:     VERIFIED WITH FIXES at local quantization scope
```

The theorem is linear in the input endpoint measure, so an already valid positive measure partition remains a partition after quantization. This fact is conditional: the theorem does not construct the rough-color source partition that `L-91325` needs.

---

## 4. `L-91114/L-91115`: finite mismatch and integer terminal annulus

### Verdict

```text
interior adjacent mismatch identity and q^-3/2 bounds: VERIFIED WITH FIXES
integer-column terminal top-omission theorem:          VERIFIED WITH FIXES
rough recursive allocation:                            explicitly OPEN
```

The adjacent finite/continuum mismatch identity is correctly typed as a local quadrature error. The fixed top omission in `L-91115` is proved for **integer columns** `q`.

This distinction becomes important in `L-91324`, where the affine child is evaluated at the real column `Q/m`.

---

## 5. `L-91317`: positive support routing

### Surviving statements

For one rough factor, and for fully active finite Euler cubes:

- the paired interior is an exact positive dilation;
- the activation frontier is positive;
- least-prime labels give coefficient-one **support provenance**;
- rough support lands either in the already paid outer block or below the contracted endpoint.

### Verdict

```text
mathematical type:  ROUTE INFRASTRUCTURE
review verdict:     VERIFIED WITH FIXES
```

Least-prime labeling prevents one arithmetic source atom from being assigned to two least-prime branches. It does not allocate the auxiliary Schur port, completed-state correction, or physical target capacity among those branches. The file itself originally leaves projective cone conversion open.

---

## 6. `L-91318`: affine Pascal covariance and score amplification

### Surviving exact identities

For

\[
\Phi_m(n)=m(n+1)-1,
\]

and every real `q>0`,

\[
\overline\beta_{\Phi_m(n)}(mq)=\overline\beta_n(q).
\]

The target and radix-four detail have the matching `m^{-1/2}` covariance, and

\[
G_{m(n+1)-1}\ge mG_n.
\]

### Verdict

```text
real-column affine covariance:   VERIFIED
atomized matched-fiber identity: VERIFIED
entropy amplification:           VERIFIED
uncolored recursive allocation:  not proved here
```

The theorem is a correct positive functor for an already specified child row. It does not decide how much child source or target is assigned to each rough branch.

---

## 7. `L-91319`: one-factor positive completion

### One-factor result

For one rough prime `p`, the signed matrix `M_p` has an entrywise-positive completion `N_p`, and

\[
(1,2)N_p=(1,2)M_p.
\]

The endpoint score row `(2,1)` is improved.

### Verdict

```text
one-factor matrix algebra:                VERIFIED
one-factor SHARP preservation:            VERIFIED
one-factor score improvement:             VERIFIED
arbitrary completed-cascade preservation: FALSE
```

### Exact failure

For two factors `r=p^{-1/2}`, `s=q^{-1/2}`,

\[
(1,2)N(s)N(r)-(1,2)M(s)M(r)
=\bigl(0,12rs(1-r)(1-s)\bigr).
\]

The failure is structural. A left functional annihilating one correction need not annihilate that correction after another noncommuting state map has changed the left row.

This is the first exact contradiction in the submitted full proof.

---

## 8. `L-91320`: Schur-port domination

There are two distinct `L-91320` files on the same branch. The relevant one for the proposed source partition is:

```text
L-91320-absorbing-59-and-61-makes-the-schur-port-dominate-every-rough-state-correction.md
```

It proves a finite Boolean positivity certificate, a positive-semidefinite two-port matrix bound, and the scalar inequality `tau_p<1/9` for `p>=67`.

### Verdict

```text
finite Boolean and scalar inequalities: VERIFIED WITH FIXES
PSD Schur-port lower bound:              VERIFIED WITH FIXES
positive endpoint-row realization of
  every projective correction:           UNPROVEN / GAP
```

A PSD matrix inequality is not automatically a coefficientwise positive decomposition of endpoint measures or rows. The file says the correction is taken from each branch's own port, but does not write the required positive map from the Schur-port packet to the signed state correction in the native endpoint/carry coordinates.

This scope issue is confirmed by the live descendant `L-91326`, which explicitly states:

```text
linear positive endpoint realization of defects   OPEN
coefficient-one score/capacity ledger              OPEN / RH-BEARING
```

---

## 9. `L-91324`: fractional-column Green identity and continuous reset

There are also two distinct `L-91324` files. The new fractional-column file is:

```text
L-91324-fractional-column-green-identity-and-continuous-reset.md
```

### Exact fractional switching identity

For finite `F`,

\[
\overline v_q(F)
=\sum_{j\ge1}
\left[
F(k_j)-F(k_j+1)
+2\vartheta_j(A_F(k_j)-A_F(k_j+1))
\right]
\]

with `k_j=floor(jq)` and `vartheta_j={jq}`.

### Verdict

```text
fractional switching identity:       VERIFIED
q^-3/2 ordinary/detail estimates:    VERIFIED WITH FIXES
interior real-column safety factor:   VERIFIED WITH FIXES
unmatched affine-column covariance:   VERIFIED
continuous terminal top omission:     UNPROVEN / GAP in the submitted proof
```

### Terminal scope defect

Section 6 imports the top-omission lower bound from `L-91115` as though it were a real-column endpoint derivative theorem. `L-91115` states and proves its lower bound for **integer** columns.

The pointwise integer-column lower bound does not extend unchanged to arbitrary real columns. For `q=N+theta`, `s` just above `q`, and `theta` tending to zero, the scaled derivative of the fractional response can tend to zero, whereas the imported constant is `2-sqrt(2)>0`.

This does not by itself disprove the integrated real-column top-omission theorem; it shows that the proof currently cited for it is invalid. A separate integrated fractional-column lower bound may repair the gap. The exact checker `X-91112` verifies finite switching/covariance examples and arithmetic constants; it does not certify this analytic terminal lower bound.

This matters because a physical parent column `Q` evaluates a child at the potentially terminal real column `Q/m`.

---

## 10. `L-91325`: abstract disintegration versus arithmetic application

There are two distinct `L-91325` files. The full-proof claim is in:

```text
L-91325-monotone-transport-disintegration-forgets-rough-colors.md
```

### Abstract theorem

If a positive source measure already has a decomposition

\[
\mu=\mu_0+\sum_b\mu_b,
\]

then a positive Markov kernel produces

\[
\nu=\nu_0+\sum_b\nu_b.
\]

### Verdict

```text
abstract Markov-kernel disintegration: VERIFIED
linear scaling/quantization of an existing partition: VERIFIED
Riemann-specific positive source partition: FALSE / UNPROVEN
one-use target ledger in the submitted assembly: UNPROVEN / GAP
coefficient-one score recurrence: UNPROVEN / GAP
full RH composition: FALSE AS SUBMITTED
```

### Why abstract disintegration cannot close the proof

The disintegration lemma is linear bookkeeping. It does not prove its hypothesis. The load-bearing identity is the arithmetic source partition `L-91325.14`.

That partition is not produced by least-prime labels alone:

- least-prime labels partition arithmetic source atoms;
- the completed matrices add auxiliary state transfers;
- the Schur port must be allocated without duplication;
- the purported completed-cascade SHARP preservation is false.

The synthetic exact checker `X-91113` assumes a finite positive source partition as input and verifies that a Markov matrix preserves it. Its own scope statement says the Riemann application depends on the positive source partition. It therefore cannot certify `L-91325.14`.

---

## 11. `L-91325.18`: score recurrence

The proposed recurrence is

\[
\mathfrak L_X\le\mathfrak L_{K_X}+O(1).
\]

The cited ingredients establish several favorable local inequalities:

- quantization does not lower score;
- affine dilation amplifies a naturally scaled child score;
- local completion improves the one-step score row;
- the global safety factor and fixed omission have bounded local cost.

They do not write an exact global equality/inequality decomposing the parent target score, outer-packing score, all branch scores, Schur-port charge, and contracted residual score with coefficient one.

Because the source-mass partition fails, the branch weights needed for the score sum are not known to have total coefficient one. The recurrence is therefore not a consequence of the listed local observations.

Verdict:

```text
UNPROVEN / GAP
```

---

# Review of the four advertised load-bearing identifications

## Identification 1: `L+2R` is the exact native factor-four source-mass ledger

```text
scalar arithmetic identity Psi=L+2R:       VERIFIED
one-factor completed-state preservation:   VERIFIED
measure typing as copies of mu_Y:           UNPROVEN / GAP
multiprime completed-cascade preservation:  FALSE
```

The scalar identity is real. The source-measure interpretation needs an explicit typed map and fails for the submitted completed cascade.

## Identification 2: completed colors and Schur slack form a positive source partition

```text
least-prime arithmetic provenance:          VERIFIED WITH FIXES
one-scale positive state completion:         VERIFIED
branch-local PSD reserve estimate:           VERIFIED WITH FIXES
exact global positive source partition:      UNPROVEN / blocked by counterexample
```

The exact equality

\[
\mu^{\rm native}=\mu_0+\sum_b\mu_b
\]

is not present coefficientwise or measurewise. It is asserted after local statements whose interfaces do not imply it.

## Identification 3: monotone transport commutes with affine scale before quantization

```text
abstract product-measure transport:          VERIFIED
real-column affine response identity:        VERIFIED
linear quantization of a given partition:    VERIFIED
complete commuting finite diagram:           UNPROVEN / GAP
terminal real-column feasibility:             UNPROVEN / GAP
```

The continuum kernel can be reused at each logarithmic scale, but the proposed theorem does not supply the complete branch-scale/affine/quantization commutative diagram with all endpoint offsets, collars and target shares. The terminal real-column proof also imports an integer-only estimate.

## Identification 4: score recurrence has the correct direction and safety is spent once

```text
one global scalar multiplication commutes with a valid sum: VERIFIED
local score inequalities:                               VERIFIED WITH FIXES
coefficient-one global source/score decomposition:      UNPROVEN / GAP
recurrence L_X<=L_K+O(1):                               UNPROVEN / GAP
```

Applying a safety factor once would be correct after a genuine total-measure partition. It does not repair the absent partition or the false completed-cascade mass identity.

---

# Live descendant and corrected frontier

## `L-91326`: common Hilbert colligation

The common metric

\[
H=\begin{pmatrix}2&-3\\-3&5\end{pmatrix}
\]

satisfies

\[
M(A,B)^THM(A,B)\preceq H
\]

for every rough packet, and the multiprime quadratic defect telescopes exactly.

### Verdict

```text
common metric and defect algebra: VERIFIED
quadratic multiprime telescope:   VERIFIED
positive linear endpoint packets: OPEN
```

This is a valid quadratic stabilization. It does not imply coefficientwise endpoint positivity or a linear packing ledger.

## `L-91327`: positive four-state linear dilation

Writing

\[
X=X_+-X_-,\qquad Y=Y_+-Y_-,
\]

the diagonal positive four-state semigroup composes exactly, and total positive variation loss telescopes linearly.

### Verdict

```text
positive four-state semigroup:          VERIFIED
linear total-variation telescope:       VERIFIED
ordinary rough source provenance:       VERIFIED WITH FIXES
explicit recursive parity projection:   UNPROVEN / GAP
bounded all-generation score recurrence: UNPROVEN / GAP
```

The SHARP and score observations remain signed:

\[
\Psi=(4,-4,-3,3)z,
\qquad
2L+R=(5,-5,-3,3)z.
\]

A positive four-state cone does not make those functionals positive. The missing theorem is the exact all-generation application of the local parity shadow to the evolving four-state mass, with:

1. nonnegative endpoint rows;
2. full ordinary and radix-four capacity;
3. a nonnegative contracted residual state;
4. all boundary/port packets charged once;
5. bounded score debt.

That is the strongest honest live frontier.

---

# Exact current proof DAG after review

```text
Möbius arithmetic source
  -> exact two-state/four-state mode decomposition
  -> finite factor-54 small-prime Hall/component-row positivity
  -> exact rough support contraction by least prime
  -> positive four-state rough semigroup
  -> exact linear total-variation defect telescope
  -> [FIRST OPEN LOAD-BEARING ARROW]
     construct one recursive positive parity/endpoint projection satisfying:
       * exact source provenance,
       * ordinary and radix-four physical feasibility,
       * no port or target duplication,
       * one contracted residual state,
       * bounded coefficient-one score debt
  -> factor-54 recurrence
  -> O(log X) score loss
  -> conditional prime-endpoint consumer
  -> RH
```

The original shortcut through completed two-state matrices and target disintegration cannot be used.

---

# Claim-ID and provenance defect

At the reviewed head, the branch contains duplicate claim identifiers:

```text
L-91320  balanced-ray Hall/interval-seed theorem
L-91320  absorb-59/61 Schur-port theorem

L-91324  positive ordinary color-erasure functor
L-91324  fractional-column Green/continuous-reset theorem

L-91325  one-scale endpoint-port renewal
L-91325  transport-disintegration/full-composition theorem
```

Consequently a dependency such as

```text
L-91317/18/19/20/24/25
```

is not a uniquely resolvable proof DAG. Before integration, each claim must receive a unique identifier and every dependency line must use exact path plus exact SHA.

---

# Computation and replay boundary

No large experiment was rerun.

Inspected retained artifacts include:

```text
X-91112 fractional-column response
  - exact Fraction switching/covariance examples
  - constant arithmetic
  - does not prove analytic terminal real-column lower bound

X-91113 transport disintegration
  - exact finite Markov-matrix linearity
  - assumes a positive source partition
  - does not certify the Riemann source identification

X-91115 common rough Hilbert colligation
  - finite exact matrix identities
  - no positive endpoint realization

X-91116 positive four-state rough dilation
  - finite exact intertwining/telescope identities
  - no recursive parity/score assembly

R-91303 non-tensorization
  - exact negative distinct-prime scalar endpoint detail
```

The new review counterexample is analytic finite-dimensional algebra and does not depend on any retained numerical output.

---

# Recommended integration actions

1. **Do not merge or describe PR #399 as a proof of RH.**
2. Mark the sentence “the same identity survives arbitrary completed rough cascades” in the transport-disintegration `L-91325` **FALSE**.
3. Mark `L-91325.14`, `L-91325.17`, `L-91325.18` and the full composition `L-91325.19` **UNPROVEN / GAP**, with the full submitted proof classified **FALSE AS SUBMITTED** because it uses the exact false cascade identity.
4. Retain the abstract transport-disintegration lemma as **VERIFIED** at conditional measure-theoretic scope.
5. Retain the fractional switching identity and real-column affine covariance as **VERIFIED**, but demote the continuous terminal closure until a genuine fractional-column omission bound is proved.
6. Retain `L-91326/L-91327` as the corrected live infrastructure; make `L-91327` the new rough-state front door.
7. State the first open theorem as the explicit recursive four-state parity/endpoint/score projection, not “color forgetting” in the abstract.
8. Renumber duplicate `L-91320`, `L-91324`, and `L-91325` claims before canonical extraction.
9. Preserve `R-91303` and the new `REV-PR399-01` counterexample as mandatory tensorization firewalls.
10. Require any future full-proof claim to contain one written, typed, all-generation equality/inequality for source mass, endpoint rows, physical capacities, residual state and score—not a sequence of local favorable observations.

---

# Final status table

```text
fractional Pascal Green identity                    VERIFIED
real-column response estimates                      VERIFIED WITH FIXES
unmatched affine-column covariance                  VERIFIED
abstract target disintegration                      VERIFIED
linear quantization preserves an existing partition VERIFIED
one-factor positive rough completion                VERIFIED
one-factor SHARP preservation                       VERIFIED
completed-cascade SHARP preservation                FALSE
native rough source partition                       UNPROVEN / GAP
continuous terminal real-column closure             UNPROVEN / GAP
one-use physical target ledger in arithmetic stack  UNPROVEN / GAP
coefficient-one score recurrence                    UNPROVEN / GAP
4981bcd full proof proposal                          FALSE AS SUBMITTED
common-Hilbert live repair                           VERIFIED infrastructure
positive four-state live repair                      VERIFIED infrastructure
recursive four-state parity/score projection         OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
