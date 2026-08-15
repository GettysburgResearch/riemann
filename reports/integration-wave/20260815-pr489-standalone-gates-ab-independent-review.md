# Independent review of PR #489 at frozen head `0bb487c8a0782f601be0a3041743b357ad93726a`

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-15T12:16:53Z
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
proposal PR:      #489
proposal base:    research/gpt56-pro/91840-explicit-root-ledger-closure
base SHA:         9acd381fa168db02a03646ab16851daebbf4d0fd
proposal branch:  research/gpt56-pro/92880-standalone-gates-ab
reviewed head:    0bb487c8a0782f601be0a3041743b357ad93726a
review branch:    review/pr489-standalone-gates-ab-20260815
```

The conclusions below are frozen to the proposal head above. The review treats PR #489 as a distinct recursive/portful composition **over** the shared PR #488-era root-ledger spine. It is not counted as independent confirmation of the source-to-endpoint realization imported from that spine.

No heavy computation was rerun. I inspected the theorem files, direct dependencies, import manifest, lock, retained verifier, control data, and the relevant PR #488 and PR #482 review interfaces. Small exact algebraic checks were performed mentally or symbolically where needed; the large directed Hall, finite-realization, and endpoint computations were not repeated.

## Executive verdict

```text
mathematical type:  PROPOSED COMPLETE THEOREM
review verdict:     UNPROVEN / GAP
lifecycle:          retain as a conditional composition and review frontier
RH status:          UNPROVEN
```

PR #489 contains several correct and useful pieces:

1. one common target/score/row Hall-flow algebra;
2. the correct actual-target-mass normalization for grouped children;
3. a clean same-index vector and scalar slack cocycle;
4. a valid logarithmic-cost summation conditional on the physical root packet;
5. a transparent statement that the endpoint consumer is inherited.

No exact contradiction was found in those algebraic pieces. The proposal is therefore not classified `FALSE`.

The complete implication nevertheless does not pass independent reconstruction. Two load-bearing facts are still asserted or inherited rather than instantiated:

- the **actual post-correction common parent/current/full-child packet identity** is imported from the PR #488-era `L-91843` telescoping interface, whose theorem assumes exact positive stage decompositions rather than exhibiting all of them in PR #489;
- the **one-use Schur port** is not instantiated for the six actual correction classes. `L-92882` defines an aggregate scalar reserve/demand surrogate, but it does not provide the six concrete demand matrices, prove that they sum to the complete correction demand, or verify the classwise PSD dominations required by `L-91842`.

Even granting the entire PR #488 source-ledger spine as a frozen hypothesis, the second gap remains inside the new PR #489 work itself. Consequently `T-92880` is a conditional composition, not an independently reconstructed proof of RH.

## Relationship to PR #488

PR #489 is neither a mere duplicate nor an independent proof route.

Its genuinely new presentation layer is:

```text
L-92880  one target/score/row Hall-flow synthesis;
L-92881  actual-target-mass child normalization and public ledger wrapper;
L-92882  proposed one-use aggregate Schur-port wrapper;
L-92883  positive-reserve Y4 cost summation;
L-92884  same-index slack cocycle and endpoint composition;
T-92880  proposed complete Gates A/B implication.
```

The physical source-to-endpoint spine is shared. In particular:

```text
L-92881 -> L-91840, L-91841, L-91843;
L-92882 -> L-91842, L-91725, L-91320;
L-92883 -> L-91843, L-91844;
L-92884 -> L-92881, L-92883 and inherited positive-descendant/endpoint results.
```

`L-91843` is a sequential telescoping theorem. It says that if every stage has an exact positive decomposition

\[
P_{i-1}=P_i+R_i,
\]

then the full source, ordinary, and detail ledger telescopes. That formal implication is valuable, but it is not itself a construction of every concrete `R_i`. Accordingly, PR #489 may use it conjunctively as a frozen dependency, but it cannot count the resulting identity as independently re-derived evidence.

## Derived-versus-inherited map

| Claimed interface | What PR #489 genuinely derives | What remains inherited or asserted | Verdict |
|---|---|---|---|
| Single target/score/row Hall flow | Given a feasible no-upward flow and the frozen monotonicities, the target equality, score superordination, and positive row-bonus identity are derived correctly from the same flow | Existence of the deterministic Hall flow and the required profile monotonicities are imported from `L-91690`, `L-91682`, and related frozen inputs | `VERIFIED WITH FIXES` |
| Actual-target-mass children | The normalization \(\beta_b=M_b/M\) and the mass-weighted grouping are the correct quantities; Tonelli/additivity preserves the subcritical inequality | The actual fiberwise target contraction and the concrete grouped source fields are imported | `VERIFIED WITH FIXES` |
| Current/full-child source ledger | PR #489 writes a coherent public wrapper and correctly applies ordinary maps at `q` and `4q` before subtraction | The substantive post-correction source identity is inherited from `L-91840`, `L-91841`, and especially conditional telescoping theorem `L-91843` | `UNPROVEN / GAP` as a standalone claim; valid conditionally |
| All-column reserve | The later algebra consumes a nonnegative reserve consistently | Construction and all-column positivity of that reserve are imported from the PR #488-era realization and `L-91844` | `IMPORTED / CONDITIONAL` |
| One-use Schur port | Positive linear aggregation would be valid after classwise matrix domination | The six concrete correction-demand matrices and their classwise PSD bounds are not exhibited; `L-92882` replaces them with a declared aggregate scalar matrix | `UNPROVEN / GAP` |
| Positive-reserve `Y_4` cost | The numerical summation and logarithmic thinning term are correct conditional on the physical reserve | The base constant and port term are inherited; the latter depends on the unresolved port instantiation | `VERIFIED WITH FIXES` |
| Same-index slack cocycle | The vector identity and scalar pairing are exact consequences of a true source/capacity identity | The physical identity supplying the root reserve and children is not independently reconstructed | `VERIFIED WITH FIXES` / conditional |
| Endpoint consumer | The implication from an admissible row with native deficit `o(log^2 X)` to the frozen endpoint criterion is composed in the correct direction | `T-91313` and its dual/Landau inputs are imported and not reconstructed | `CONDITIONAL IMPLICATION` |

# Claim-by-claim reconstruction

## 1. `L-92880`: one common Hall flow

The theorem chooses one transport `t_x(o,e)` satisfying the target row and column constraints. It defines the positive residual by

\[
\nu_x(e)=1-\frac{\sum_o t_x(o,e)}{T_x(e)}.
\]

The target identity follows by conservation. If

\[
f_x(z)=\frac{S_x(z)}{T_x(z)}
\]

is decreasing along every allowed edge `e<=o`, then moving target mass downward cannot reduce the represented score. Likewise, if each target-normalized row profile is ordered in the required direction, then

\[
\text{signed row}
=
\text{positive residual row}
+
\text{positive Hall bonus row}.
\]

Those are exact algebraic consequences of one common flow; PR #489 does not mix separately chosen target, score, and row flows.

The qualification is scope. The theorem does not independently establish the Hall-flow existence or the profile inequalities. Those are frozen dependencies. Therefore the surviving statement is:

> On the imported finite Hall and monotonicity inputs, the same flow simultaneously gives target equality, score superordination, and component-row positivity.

This is useful route infrastructure and answers the common-source-flow concern, but it is not independent evidence for the imported directed inequalities.

## 2. `L-92881`: actual-target-mass child normalization

The theorem correctly avoids the old error of treating an unweighted coefficient sum as a target-mass contraction. For grouped child fields it uses

\[
\beta_b=\frac{M_b}{M},
\]

where `M_b` is actual child target mass and `M` is parent target mass. This is the right normalization for the hereditary consumer. Positive integration and grouping preserve the mass-weighted inequality once it holds fiberwise.

The theorem also preserves the essential order of operations:

1. restrict before quadrature;
2. retain complete provenance labels;
3. assign each rough atom to its first owner;
4. group full children by actual target mass;
5. form ordinary responses at `q` and `4q` separately;
6. only then form radix-four detail.

The formal order is correct.

The load-bearing identity, however, is written as an application of inherited theorems:

\[
P_{\rm ret}
=
P_{\rm cur}
+
\sum_b\beta_b U_b\widetilde P_b
+
P_{\rm omit}.
\]

`L-91843` proves that a chain of exact positive stage identities telescopes. It does not, inside PR #489, exhibit every actual stage residue after quantizer, mismatch, collar, omission, base, and port correction. Consequently `L-92881` is a faithful wrapper over the shared spine, not an independent construction of the concrete packet.

Two classifications are therefore needed:

```text
conjunctive reading with all PR #488 stage identities accepted:
    VERIFIED WITH FIXES / formal composition

standalone-public-ledger claim made by PR #489:
    UNPROVEN / GAP
```

## 3. `L-92882`: common Schur port

This is the first unresolved point that remains even if the complete PR #488 source ledger is granted.

The inherited `L-91842` lists six correction classes:

1. quantizer;
2. activation collar;
3. finite/continuum mismatch;
4. terminal omission;
5. fixed top/base correction;
6. endpoint gluing.

Its conclusion is a linearity theorem: if every actual correction demand `D_c` and reserve `P_c` satisfy

\[
0\preceq D_c\preceq P_c,
\]

then their sum has one owner and is covered by the aggregate reserve. `L-91842` expressly does not provide a new numerical Schur estimate.

`L-92882` instead introduces, branch by branch,

\[
D_b=\tau_bV_b I_2,
\qquad \tau_b\le\frac19,
\]

and calls this the complete branch correction demand. It then sums `D_b` and the branch reserves and invokes PSD linearity.

What is missing is an explicit adapter proving all of the following:

\[
D_b^{\rm actual}
=
D_{b,\rm quant}
+D_{b,\rm collar}
+D_{b,\rm mismatch}
+D_{b,\rm terminal}
+D_{b,\rm base}
+D_{b,\rm glue},
\]

\[
D_b^{\rm actual}\preceq \tau_bV_bI_2,
\]

and

\[
\tau_bV_bI_2\preceq P_b.
\]

The file does not list the six actual matrices, derive the first equality, or prove the middle domination. A scalar mass or trace bound cannot replace matrix order: for example, `diag(1,0)` and `diag(0,1)` have equal trace but neither dominates the other. The actual orientation of the correction demand is therefore proof-relevant.

The aggregate mass estimate below `70/3` does not close this matrix interface. It controls the size of a proposed port once the port has been physically justified; it does not show that the port absorbs the real correction demand.

**Verdict:** `UNPROVEN / GAP`.

This is the clearest first broken arrow inside the new PR #489 contribution itself.

## 4. `L-92883`: logarithmic native cost

The theorem decomposes the root cost into:

```text
square-root thinning                 < 4290 log X
finite/continuum mismatch + collar   < 392
activation collar/refinement         < 2
fixed top/base                        < C_base
one common port                       < 70/3
```

The arithmetic combination is sound and leads to

\[
\delta_X=\langle Y_4,r_X\rangle
\le C_{\rm base}+15124+4290\log X.
\]

This is the correct proof-relevant scale: `O(log X)=o(log^2 X)`. It does not revive the rejected `4\sqrt X-H(d_X)=O(1)` normalization.

The qualification is not that a numerical decimal for `C_base` is intrinsically necessary. An explicitly proved absolute constant would suffice. The problem is that the actual fixed base/top packet and the port demand remain imported, and the port term depends on `L-92882`. Thus the displayed bound is a valid conditional summation rather than a closed physical theorem.

**Verdict:** `VERIFIED WITH FIXES`, `CONDITIONAL IMPLICATION`.

## 5. `L-92884`: same-index vector and scalar cocycle

Given a true common-parent identity and feasible child rows, the assembled row

\[
d_X=d_X^{\rm cur}+\sum_b\beta_bU_bd_b
\]

has slack

\[
s_X=r_X+\sum_b\beta_bU_bs_b.
\]

Pairing with the nonnegative `Y_4` weights gives exactly

\[
\Delta_X
=
\delta_X+
\sum_b\beta_b\Delta_b.
\]

No sign reversal or extra child scaling was found. The same-index functor and actual target-mass coefficients are used consistently.

The positive-descendant theorem then supplies an absolute descendant contribution once the grouped child target mass is below one eighth of the root target mass. The stated root-mass arithmetic is compatible with this conclusion.

Again, the cocycle is downstream of the physical packet identity and port. It cannot establish those hypotheses.

**Verdict:** `VERIFIED WITH FIXES`, `CONDITIONAL IMPLICATION`.

## 6. `T-92880`: endpoint and RH

The final theorem applies the resident endpoint consumer after obtaining

\[
J_\Lambda(X)-\mathcal H(d_X)=O(\log X)=o(\log^2X).
\]

The orientation is the correct one-sided native deficit. The endpoint theorem `T-91313`, however, explicitly assumes the admissible row, complete dual inequality, and sub-log-squared deficit; it does not prove the producer hypotheses. PR #489 imports this consumer and does not independently reconstruct its finite dual and Mellin–Landau inputs.

Since the physical root packet and port are not yet established, the endpoint theorem is not reached.

**Verdict:** `UNPROVEN / GAP`, `PROPOSED COMPLETE THEOREM`.

# Disposition of PR #482's six-point resolution path

PR #482 ended with six concrete requirements. Their status at frozen PR #489 is as follows.

## 1. Construct the actual post-correction parent packet

**Disposition: `UNPROVEN / GAP`.**

`L-92881` names the packet and gives the correct operation order, but its substantive identity is inherited from `L-91843`. That theorem telescopes exact stage decompositions supplied as hypotheses. PR #489 does not exhibit one complete source-labelled formula or certificate for all actual quantizer, mismatch, knot, terminal, base, and port residues.

## 2. Prove the exact current/child identity at ordinary `q` and `4q` before forming detail

**Disposition: `VERIFIED CONDITIONALLY / INHERITED`.**

The order of linear operations is correct. Once the source identity is true, applying the ordinary map at `q` and `4q` separately and subtracting produces the exact detail identity. PR #489 does not commit the underlying physical packet independently, but it does not repeat the earlier sum-after-subtraction error.

## 3. Instantiate the full common-port correction demand

**Disposition: `UNPROVEN / GAP`.**

`L-92882` supplies aggregate notation and a scalar matrix budget, not the six actual demand matrices and classwise PSD comparisons required by `L-91842`. This is the first unresolved new theorem even on a fully accepted PR #488 spine.

## 4. Calculate an explicit terminal/base/port `Y_4`-cost constant

**Disposition: `PARTIAL / VERIFIED WITH FIXES`.**

The mismatch, collar, thinning, and proposed port arithmetic are explicit, and the final scale is correctly logarithmic. `C_base` remains an imported symbolic constant, and the port contribution is conditional on the missing matrix-demand adapter. A proved absolute `C_base` would be sufficient; the issue is that its source packet and bound are not reconstructed here.

## 5. Replace the toy cocycle replay with a ledger tied to the real packet formulas

**Disposition: `EMPIRICAL ONLY / NOT CLOSED`.**

`X-92880` checks rational coefficient arithmetic, sample partitions, declared hashes, required strings, and scalar constants. It does not generate the actual Hall flow, correction packets, source labels, ordinary responses at all `q` and `4q`, detail slack, six port matrices, or the real `Y_4` pairing. It is a useful regression test, not a proof-object replay of the physical root ledger.

## 6. Reconstruct the frozen endpoint-to-RH consumer

**Disposition: `CONDITIONAL / INHERITED / NOT RECONSTRUCTED`.**

`T-91313` is pinned and used in the correct direction. PR #489 does not independently reconstruct the finite dual, the strict endpoint threshold, or the Mellin–Landau implication. This is acceptable for a conjunctive proposal only after the producer is proved; it is not standalone verification.

# Replay and provenance audit

## Replay scope

The retained verifier authenticates, among other finite items:

- the numerical inequality `rho<1/8`;
- selected coefficient and target-mass arithmetic;
- the logarithmic-cost constant combination;
- root-mass and descendant-bound arithmetic;
- expected file hashes and marker strings.

It does not replay the load-bearing analytic/physical objects. In particular, it does not certify:

```text
one actual Hall transport on every root fiber;
the complete source-labelled post-correction packet;
ordinary responses for the real packet at all q and 4q;
the actual radix-four slack vector;
the six classwise Schur-port matrices;
classwise or aggregate PSD domination;
the actual Y4-weighted root reserve;
the endpoint dual and Mellin-Landau theorem.
```

The retained `PASS` line is therefore classified `EMPIRICAL ONLY` at the complete-proof scope.

## Manifest scope

The import manifest pins several important dependencies, including `L-91843` and `L-91844`. It does not list every direct load-bearing dependency named by the new theorem files. Missing direct entries include at least:

```text
L-91840
L-91841
L-91842
L-91725
L-91320
L-91674
```

Those files are present in the inherited branch history, so this is not a claim that the repository cannot resolve them. It is a claim that the advertised standalone import manifest is not a complete direct-dependency lock. The packet should either add them with exact blob identities or explicitly define the base commit as a conjunctive monolithic dependency and stop describing the manifest as complete standalone provenance.

**Verdict:** `VERIFIED WITH FIXES` as a partial provenance lock.

# Claim status table

| Claim | Mathematical type | Verdict | Surviving scope |
|---|---|---|---|
| `L-92880` | ROUTE INFRASTRUCTURE | `VERIFIED WITH FIXES` | One common-flow target/score/row algebra on frozen Hall and monotonicity inputs |
| `L-92881` | ROUTE INFRASTRUCTURE | `UNPROVEN / GAP` as standalone; conditional composition survives | Correct actual-target normalization and operation order; physical packet identity inherited |
| `L-92882` | ROUTE INFRASTRUCTURE | `UNPROVEN / GAP` | Positive aggregation is valid only after actual classwise port demands are proved |
| `L-92883` | CONDITIONAL IMPLICATION | `VERIFIED WITH FIXES` | Correct logarithmic cost summation conditional on real reserve/base/port packets |
| `L-92884` | CONDITIONAL IMPLICATION | `VERIFIED WITH FIXES` | Exact same-index vector/scalar cocycle after the root identity |
| `T-92880` | PROPOSED COMPLETE THEOREM | `UNPROVEN / GAP` | Conditional RH implication on all frozen producer and consumer hypotheses |
| `X-92880` | DISCOVERY / REGRESSION ONLY | `EMPIRICAL ONLY` | Finite scalar, schema, and provenance checks |
| import manifest and lock | ROUTE INFRASTRUCTURE | `VERIFIED WITH FIXES` | Partial lock; not a complete direct-dependency manifest |
| Riemann Hypothesis | — | `UNPROVEN` | No conclusion at the reviewed SHA |

# First open theorem

The shortest serious successor is not another abstract recurrence. It is a **Concrete Complete Root Correction and Port Instantiation Theorem**.

For the actual factor-67 parent, it should provide one immutable proof object containing:

1. every source-labelled retained/current/child/omitted packet after restriction and Hall;
2. the exact six correction packets for quantizer, activation collar, finite/continuum mismatch, terminal omission, fixed top/base correction, and endpoint gluing;
3. every stage identity `P_(i-1)=P_i+R_i` with all terms positive and one-use;
4. ordinary response vectors at `q` and `4q` before detail formation;
5. the resulting nonnegative all-column detail reserve;
6. the six concrete `2x2` Schur demand matrices `D_c` and reserve matrices `P_c`;
7. exact proofs `D_c <= P_c` in PSD order and the equality identifying their sum with the complete correction demand;
8. one physical common-port source realizing that aggregate demand;
9. an explicit proved absolute base/top/port native-cost bound;
10. a replay generated from those actual formulas rather than sample coefficient lists.

After that theorem, the actual-target-mass contraction and the verified scalar cocycle can legitimately feed the inherited endpoint consumer.

# Integration recommendation

Do not integrate `T-92880` as proof-level RH closure.

Retain the following as useful mathematics or architecture:

```text
one-common-flow target/score/row Hall algebra;
actual-target-mass child normalization;
ordinary-q and ordinary-4q before detail rule;
same-index vector and scalar slack cocycle;
logarithmic native-cost arithmetic;
explicit identification of the port-instantiation gate.
```

Mark the following as unresolved:

```text
actual post-correction packet construction;
complete six-class Schur-port demand and PSD domination;
fully explicit base/top/port native-cost theorem;
actual-packet replay;
independent endpoint-consumer reconstruction.
```

## Final verdict

\[
\boxed{\text{PR #489: UNPROVEN / GAP}}
\]

\[
\boxed{\text{RH remains unproved at }0bb487c8a0782f601be0a3041743b357ad93726a.}
\]
