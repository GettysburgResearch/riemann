# Exact-head independent review of PR #518 and PR #521

**Review type:** review-only; the two proposals are reconstructed independently  
**Review cutoff:** `2026-08-16T02:07:18Z`  
**Repository:** `gfreund123/riemann`  
**Main at review start:** `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
**Method:** exact-head genealogy, theorem-file reconstruction, lightweight exact arithmetic, small directed cell checks, and type/ownership auditing  
**Heavy computations rerun:** none  
**Riemann Hypothesis:** **unproved**

## Frozen targets

```text
PR #518
branch  research/gpt56-pro/92910-upstream-spine-reconstruction
head    3277b831b30f4783ed3b087df57e95b9f7dfd7b0
tree    72a88732a054c33b1e1fe5a751bd2c6442a13f8a
base    PR #494 at 1468ff62c7377f3f6cc1744ef6eafc3df3172d5c

PR #521
branch  research/gpt56-pro/94020-target-lorenz-live-marginal
head    b4a60a54b1d730a73ab1eb6bb571485dd40438d0
tree    da684b92762623b5a83ddfd7df9605784d69dab6
base    PR #508 at 4ae97dffd1f76ed3244b8f3028560ffa80663caf
```

The proposals are not treated as mutual confirmation. In particular, no positive verdict in the PR #521 section uses PR #518, and no positive verdict in the PR #518 section uses PR #521. The invalid PR #508 interval certificate is excluded completely from this review. Any PR #521 claim that imports it is classified only conditionally or as unproved.

---

# 1. Executive verdicts

```text
PR #518 local compact Hall/profile theorem:
CONDITIONAL PASS AT FROZEN DIRECTED-INPUT SCOPE

PR #518 whole-cell source/quantizer theorem L-92911:
FALSE

PR #518 end-to-end proposal T-92911:
REQUEST CHANGES / UNPROVEN

exact first broken arrow:
source-active fibre on a nominal integer cell
  -> source-exact and target-exact two-point endpoint quantization

PR #521 live source/owner registry:
VERIFIED WITH SCOPE FIXES

PR #521 preservation of the #514 q=2 obstruction:
VERIFIED

PR #521 JNTLC status:
OPEN, AS DECLARED

PR #521 end-to-end RH composition:
UNPROVEN / CONDITIONAL; NOT REACHED
```

The decisive PR #518 issue is not a numerical margin. It is a support discontinuity. The source set changes at points `s=X/k`, and these points generally lie strictly inside the retained integer cells used by `L-92911`. A two-point quantizer spanning such a point must either create a source occurrence at an inactive endpoint or lose positive target mass.

PR #521, by contrast, genuinely records the actual source/path marginal, retains the negative `q=2` child coordinate, and leaves the joint native Target-Lorenz coupling (`JNTLC`) open. It therefore addresses the type obstruction isolated in review PR #514 without claiming to solve it.

---

# 2. PR #518: Hall -> whole cells -> quantizer -> columns -> native cost -> endpoint

## 2.1 Reconstructed chain

```text
L-92910 compact factor-67 Hall/profile theorem
  -> L-92911 whole integer endpoint cells and two-point quantizer
  -> L-92912 adjacent-cell mismatch and all-column reserve
  -> L-92913 native Y4 cost <55000
  -> L-92914 prime-square quadratic moat
  -> T-92910 eventual prime-endpoint negativity and Mellin/Landau
  -> T-92911 proposed RH conclusion.
```

The first transition from the compact fibre theorem to the integer-cell quantizer fails.

## 2.2 `L-92910`: compact Hall/profile theorem

The finite Hall-prefix reduction is coherent. On each fixed activation cell in the fibre variable `x`, the source set is constant, the Hall coefficients are Borel, and target-normalized row monotonicity is the correct sufficient condition for a simultaneous target/score/row flow.

The large directed profile replay was not rerun. The theorem is therefore accepted only at the following scope:

```text
finite reduction and quantifiers                  VERIFIED
frozen directed inequalities                      IMPORTED / NOT RERUN
independent confirmation of every profile cell     NO
```

No contradiction was found inside `L-92910` itself.

## 2.3 Exact activation-knot counterexample to `L-92911`

`L-92911` retains

\[
 I_X=[K+2,X-W-2],
 \qquad K=\lfloor X/67\rfloor+1,
 \qquad W=10000,
\]

and asserts that integer endpoints make the retained region a union of complete cells with no activation collar. It then quantizes every `s in [n,n+1]` to `n,n+1`, preserving the constant and `s^{-1/2}` modes.

This does not account for source activations

\[
 s=\frac Xk.
\]

Take the exact admissible values

```text
X = 10^12
k = 3
K = 14925373135
n = floor(X/3) = 333333333333
X/3 = n + 1/3
s0 = n + 1/6.
```

The entire cell `[n,n+1]` lies in `I_X`. The source label `k=3` is active at `n` and at `s0`, because `3s0<X`, but inactive at `n+1`, because

\[
 3(n+1)=1000000000002>X.
\]

On its active side the SHARP target is the affine function of `s^{-1/2}`

\[
 \widetilde T_3(s)
 =\frac{4\sqrt{X/(3s)}-3}{\sqrt3}.
\]

The untruncated value at `n+1` is still strictly positive: this is equivalent to

\[
 16X>9\cdot3(n+1),
\]

which here reads

\[
 16000000000000>9000000000018.
\]

Let `q_n(s0),q_(n+1)(s0)` be the two weights of `L-92911`. Both are positive, and affine preservation gives

\[
 \widetilde T_3(s_0)
 =q_n\widetilde T_3(n)
  +q_{n+1}\widetilde T_3(n+1).
\]

A source-exact output must suppress the `n+1` term, since the label is inactive there. It therefore loses

\[
 q_{n+1}\widetilde T_3(n+1)>0.
\]

The lightweight directed evaluation gives

```text
q_(n+1)                         0.1666666666669791...
untruncated T_3(n+1)            0.5773502691873163...
missing target                  0.0962250448647331...
```

If the `n+1` target is retained instead, the construction creates an arithmetic source occurrence outside its causal support. Thus the quantizer cannot be both source exact and target exact.

The same issue applies to declared score and to further component-row activation knots. One-sided values at a knot are irrelevant to direct Lebesgue integration, but they are not irrelevant to a positive quantizer whose stencil crosses the knot.

This is also inconsistent with the inherited `L-91733` interface, which explicitly excluded activation-knot cells from the continuumized retained set. `L-92911` removes that exclusion without replacing it by a new boundary theorem.

### Exact verdict

```text
positive endpoint density                           survives
Borel Hall map                                      survives
cellwise two-point martingale algebra               survives on fixed-support cells
no activation collar                               FALSE
source-exact target-exact quantization on all cells FALSE
L-92911 overall                                    FALSE
```

## 2.4 `L-92912`: all-column estimate

The carry identity

\[
 v_q(E_X^I)=\sum_{jq\in I_X}\varepsilon_X(jq)
\]

is correct once the adjacent errors are correctly defined and bounded. The problem is the asserted bound

\[
 |\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}
\]

on every retained nominal unit cell.

Differentiating the finite sum is valid only on subcells with a constant active source set. On the counterexample cell above, the `k=3` term jumps at `X/3`. The proof contains no jump term, boundary atom, or activation-cell exclusion. The PR #518 verifier samples abstract reciprocal coordinates and calls frozen replays; it never instantiates a source label whose support terminates inside the quantizer cell.

Therefore:

```text
localized carry identity              VERIFIED
small-q summation after a valid bound VERIFIED
adjacent bound on all nominal cells   UNPROVEN / PROOF INVALID
all-column native feasibility         BLOCKED
```

## 2.5 `L-92913`: direct native cost

The numerical ledger is internally consistent:

\[
 6006+4+4452\cdot11+1=54983<55000.
\]

The Chebyshev/thinning constant also reconstructs:

\[
 (1-\tau_K)J_\Lambda(X)
 <1040(\log2)\sqrt{67}<6006.
\]

Zero port is legitimate for the declared operation list because no projective state completion or Schur complement is invoked.

But the quantity being priced must be the slack of an actual native-feasible row. Since `L-92911/L-92912` do not construct such a row, the theorem-level conclusion remains conditional.

```text
constant arithmetic      VERIFIED
port value zero          VERIFIED BY ABSENCE
native deficit <55000    UNPROVEN / PRODUCER BLOCKED
```

## 2.6 `L-92914`: prime-square drift

The local lower bound is exact:

\[
 C_\square
 =\int_0^1\{u^{-2}\}\,du
 \ge\int_{1/\sqrt2}^1(u^{-2}-1)du
 =\frac3{\sqrt2}-2>\frac1{10}.
\]

The higher-prime-power truncation, exceptional unit-interval estimate, PNT weighted Riemann sum, and Green transfer agree with the frozen `L-90020` argument. No heavy computation is involved.

**Verdict:** **VERIFIED WITH DEPENDENCIES** as an unconditional prime-square asymptotic. It does not repair the producer.

## 2.7 `T-92910`: finite dual and Mellin/Landau

Conditional on an actual row with bounded native deficit, ordinary feasibility gives

\[
 F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X),
\]

and the positive prime-square moat makes the prime-only endpoint eventually negative. The imported prime-endpoint Mellin symbol has no positive-real singularity and retains every off-line zero pole. The stated Landau one-sign argument is the correct formal consumer of eventual negativity.

This is a **CONDITIONAL IMPLICATION**. It cannot supply the missing row and is not the first broken arrow.

## 2.8 PR #518 claim-level verdicts

| Claim | Verdict | Mathematical type | Finding |
|---|---|---|---|
| `R-92910` | **VERIFIED** | REFUTATION / FIREWALL | Correctly retires recursive capacity and port shortcuts. |
| `L-92910` | **VERIFIED WITH DEPENDENCIES** | UNCONDITIONAL THEOREM | Finite Hall/profile reduction coherent; directed campaign not rerun. |
| `L-92911` | **FALSE** | PROPOSED PRODUCER THEOREM | Exact `X=10^12,k=3` activation-knot contradiction. |
| `L-92912` | **UNPROVEN / GAP** | PROPOSED ALL-COLUMN THEOREM | Derivative estimate omits source-activation jumps. |
| `L-92913` | **VERIFIED CONDITIONALLY** | CONDITIONAL NATIVE-COST LEMMA | Arithmetic valid; no row to price. |
| `L-92914` | **VERIFIED WITH DEPENDENCIES** | UNCONDITIONAL ASYMPTOTIC | Prime-square moat survives. |
| `T-92910` | **VERIFIED CONDITIONALLY** | CONDITIONAL IMPLICATION | Mellin/Landau consumer downstream of producer. |
| `T-92911` | **FALSE AS A COMPLETE COMPOSITION** | PROPOSED COMPLETE THEOREM | Stops at false `L-92911`. |
| `X-92910` | **EMPIRICAL / REGRESSION ONLY** | DISCOVERY / CHECKER | Does not test activation support. |

### PR #518 final verdict

\[
\boxed{\text{REQUEST CHANGES — first broken arrow is L-92911.}}
\]

---

# 3. PR #521: live Target-Lorenz registry and joint gate

This section does not use PR #508's interval certificate. The directed tail, AVLT positivity imported from that certificate, and the downstream all-column/endpoint locks receive no independent positive credit here.

## 3.1 `R-94020`: exact scope corrections

Both displayed counterexamples reconstruct:

1. At `(X,m,k)=(536,8,67)`, the literal finite endpoint coefficient is zero because `X=mk`, while the paired equality and SHARP target coefficients are `1/sqrt(67)`. The finite anchored occurrence is not atomwise a SHARP source atom.
2. The actual oriented child aggregate is the negative rough reservoir and has a strictly negative ordinary `q=2` coordinate.

The elementary bound

\[
 -\frac{\log4}{\sqrt{134}}<-\frac19
\]

is exact from `log 2>2/3` and `sqrt(134)<12`.

**Verdict:** **VERIFIED**.

## 3.2 `L-94020`: the live registry is genuine at its stated scope

The source theorem now supplies explicit formulas for:

```text
root x=X/s;
continuum paired equality colour masses;
literal finite endpoint occurrences;
P61 divisor;
ordered rough history;
least rough owner;
Möbius parity;
stopped-tree path coefficient.
```

The generated `X=536` registry is not a synthetic owner fixture. It contains all 327 squarefree source atoms. The `k=67` record has

```text
mu             -1
rough_history  [67]
first_owner    67
parity         odd
path           1/sqrt(67).
```

The finite endpoint file contains all 2473 occurrences `(m,k)` with `mk<=536` and records the exact `(m,k)=(8,67)` zero-boundary witness.

The replay is a deterministic instantiation of the formulas, not a proof of a positive physical compiler for every `X`. The general owner theorem itself follows from unique factorization and the exact stopping-line identity.

**Verdict:** **VERIFIED WITH SCOPE FIX** — exact source/owner registry, not physical feasibility.

## 3.3 `L-94021`: positive outer fibre

The 66-cell two-channel calculation was independently reproduced with rational square-root enclosures. It gives

```text
minimum E-channel lower bound  0.3186174007... on cell 32
minimum R-channel lower bound  0 at x=1
```

The result uses only the finite outer Möbius fibre and the identities

\[
 T=E+2R,
 \qquad S=2E+R.
\]

It does not use PR #508's interval certificate.

**Verdict:** **VERIFIED** at the two-channel outer-fibre scope.

## 3.4 `L-94022`: finite-forcing weights

The normalized causal identity is exact:

\[
 P_x
 =\sum_i\beta_i(P_x-r_iA_{p_i}P_{x/p_i})
 +\sum_i\gamma_iA_{p_i}P_{x/p_i},
\]

with

\[
 \sum_i\beta_i=1,
 \qquad
 \sum_i\gamma_i<67^{-1/2}<1/8.
\]

The generated `x=871` registry contains all 132 active terminal primes and does not clone the parent once per leaf.

The final positivity sentence invokes the complete directed AVLT inherited from PR #508. Under the review instruction excluding that invalid interval certificate, this positivity clause is not accepted.

```text
beta/gamma allocation                VERIFIED
nonduplication                       VERIFIED
complete causal-block positivity     UNPROVEN / EXCLUDED INPUT
native child cancellation            correctly not claimed
```

## 3.5 `L-94023` and `M-94020`: JNTLC remains open

`L-94023` correctly places the actual anchored marginal into one finite typed problem

\[
 A_Xz=b_X,
 \qquad G_Xz\ge0,
 \qquad z\ge0,
\]

with ordinary `q` and `4q` coordinates present before radix-four subtraction. It expressly permits finite-forcing/oriented-child cancellation inside a joint template and forbids exposing the negative child block as a positive branch.

This is an exact finite **problem schema**. The repository does not provide:

```text
a complete proved template family;
a feasible vector z for all large X;
or an exact separator for a proved-complete cone.
```

`M-94020` labels this missing theorem `JNTLC` and marks it OPEN. That status is preserved consistently in the replay, lock, theorem, report, and PR body.

**Verdict:**

```text
finite live-marginal reduction      VERIFIED AS ROUTE INFRASTRUCTURE
JNTLC feasibility                   OPEN / RH-BEARING
JNTLC template completeness         OPEN
```

This is the exact first unresolved arrow in PR #521.

## 3.6 `L-94024` and `T-94020`: conditional only

If JNTLC supplies one joint coefficient system and if the frozen analytic all-column and endpoint inputs are valid, then using the same coefficients at ordinary `q` and `4q`, forming detail afterward, and applying the native `Y4` dual is the right composition order.

This review does not import PR #508's invalid interval certificate. Consequently the claims that rely on its AVLT, all-column, or endpoint locks remain conditional even after JNTLC.

The important scientific point is that `T-94020` does not promote the conditional chain to an unconditional RH proof. It states that JNTLC is open and RH is unproved.

## 3.7 PR #521 claim-level verdicts

| Claim | Verdict | Mathematical type | Finding |
|---|---|---|---|
| `R-94020` | **VERIFIED** | REFUTATION | Finite/SHARP mismatch and negative `q=2` child coordinate exact. |
| `L-94020` | **VERIFIED WITH SCOPE FIX** | UNCONDITIONAL SOURCE THEOREM | Genuine live source/path/owner registry; not physical realization. |
| `L-94021` | **VERIFIED** | UNCONDITIONAL OUTER-FIBRE THEOREM | Independent 66-cell two-channel check passes. |
| `L-94022`, weight algebra | **VERIFIED** | ROUTE INFRASTRUCTURE | `beta/gamma` allocation exact and nonduplicating. |
| `L-94022`, AVLT positivity | **UNPROVEN / EXCLUDED** | PROPOSED PRODUCER INPUT | Depends on excluded PR #508 interval certificate. |
| `L-94023` | **VERIFIED WITH FIXES** | ROUTE INFRASTRUCTURE | Exact finite schema; not an instantiated complete matrix theorem. |
| `M-94020` | **VERIFIED AS OPEN** | OPEN PRODUCER SPECIFICATION | JNTLC honestly remains open. |
| `L-94024` | **CONDITIONAL ONLY** | CONDITIONAL IMPLICATION | Requires JNTLC and excluded analytic inputs. |
| `T-94020` | **VERIFIED WITH SCOPE FIX** | FRONTIER THEOREM | Correct open boundary; PR #508 certificate not credited. |
| `X-94020` | **VERIFIED AT REGISTRY SCOPE** | EXACT FINITE REPLAY | Deterministic files and local gates, not JNTLC. |

### PR #521 final verdict

\[
\boxed{
\text{Local live-registry repair passes; end-to-end closure remains OPEN at JNTLC.}
}
\]

No change is requested to the negative-coordinate firewall or to the OPEN status. The theorem and PR body should avoid treating the excluded PR #508 interval certificate as controlling evidence.

---

# 4. Separate proposed repair for PR #518

The repair is not to alter the endpoint of the false proof after the fact. It is a new producer gate:

```text
ACTIVATION-AWARE WHOLE-CELL COMPILER
```

A valid implementation must refine or remove every unit cell crossed by a nonzero source/profile activation knot, including at least

\[
 s=\frac Xk
\]

and the component-row knots generated by `Q_(X/(sk))(j)`. The safest proposed implementation is:

1. define the complete finite set of bad integer cells containing a typed activation knot;
2. keep those cells in a literal anchored finite ledger with one source owner;
3. apply the martingale quantizer only to good cells with constant active support;
4. prove exact target/score preservation on good cells;
5. construct and price the anchored activation-cell contribution separately;
6. rederive the adjacent mismatch, all-column estimate, terminal reserve, and native `Y4` cost;
7. retain zero port only if no new Schur mechanism is introduced.

This proposal is published separately as the `94030` activation-aware gate. Its status is **PROPOSED / OPEN**. It does not repair PR #518 retroactively and does not establish RH.

---

# 5. Computation boundary

No heavy computation was rerun. In particular, this review did not rerun:

```text
PR #518 profile/Hall directed campaigns;
PR #508's interval event campaign;
large endpoint scans;
large LP/Farkas searches;
Mellin contour computations.
```

Lightweight checks performed:

```text
exact X=10^12, k=3 activation-knot witness;
small reciprocal-mode quantizer arithmetic;
Möbius and owner registry through X=536;
2473 finite endpoint occurrence count;
66 outer two-channel cells with rational enclosures;
132 causal parent weights at x=871;
q=2 negative child-coordinate inequality;
named native-cost arithmetic.
```

Retained lightweight verdict:

```text
PASS_PR518_ACTIVATION_KNOT_AND_PR521_LIVE_REGISTRY_REVIEW
```

---

# 6. Final status

```text
PR #518 Hall/profile compact input               CONDITIONAL PASS
PR #518 whole-cell quantizer                     FALSE
PR #518 all-column/native-cost chain             BLOCKED
PR #518 Mellin/Landau consumer                   CONDITIONAL DOWNSTREAM
PR #518 complete proposal                        REQUEST CHANGES

PR #521 live source/path registry                VERIFIED
PR #521 negative q=2 child coordinate            VERIFIED
PR #521 outer two-channel fibre                  VERIFIED
PR #521 beta/gamma allocation                    VERIFIED
PR #521 AVLT/PR508 interval input                EXCLUDED / UNPROVEN
PR #521 JNTLC                                    OPEN
PR #521 native deficit and endpoint              CONDITIONAL / NOT REACHED

activation-aware 94030 repair                    PROPOSED / OPEN
Riemann Hypothesis                               UNPROVEN
```
