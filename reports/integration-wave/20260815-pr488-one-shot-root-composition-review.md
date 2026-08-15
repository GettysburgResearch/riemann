# Independent review of PR #488 — one-shot factor-67 root composition

Review cutoff: `2026-08-15T12:26:19Z`  
Repository: `gfreund123/riemann`  
Main at review start: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Proposal PR: `#488`  
Frozen proposal head: `9acd381fa168db02a03646ab16851daebbf4d0fd`  
Proposal base PR: `#487`  
Proposal base SHA: `39d2cbc7cabf31ac1f8013f2f6d1785c86a4fdeb`  
Review branch: `review/pr488-one-shot-root-composition-20260815`

## Executive verdict

The reviewed packet contains two different mathematical layers which must be separated.

1. The **preferred one-shot route inherited from PR #487** constructs one nonnegative finite row, proves native ordinary/detail feasibility by a direct capacity comparison, defines the remaining detail slack by subtraction, and prices that slack directly by the positive `Y_4` dual. This is a coherent conditional route on its frozen endpoint-frame, Hall, quantizer, collar, mismatch, terminal and endpoint-consumer inputs.
2. The **new PR #488 recovery layer** claims something stronger: that all fourteen construction stages form a disjoint positive source telescope which itself derives the corrected native packet identity. That stronger source theorem is not proved. In particular, the finite/continuum mismatch and the collar/taper estimates are signed comparison data, not positive source-partition stages.

My claim-level conclusions are:

```text
L-91840 restriction-before-quadrature             VERIFIED
L-91841 first-owner restricted children           VERIFIED WITH FIXES
L-91842 six-class port aggregation                VERIFIED WITH FIXES / ABSTRACT
L-91843 fourteen-stage positive source ledger     UNPROVEN / GAP
L-91844 direct Y4 upper-bound accounting          VERIFIED WITH FIXES / CONDITIONAL
T-91840 complete RH composition                   UNPROVEN / GAP
X-91840 replay                                    EMPIRICAL ONLY
```

For the inherited one-shot spine:

```text
native row/ordinary/detail/score dictionary       VERIFIED
positive Y4 dual                                  VERIFIED
fixed-window Hall algebra                         VERIFIED WITH FROZEN DIRECTED INPUTS
rough first-owner partition                       VERIFIED
formal positive endpoint integration              VERIFIED WITH FIXES / CONDITIONAL
whole-cell support                                VERIFIED
single martingale quantizer                       VERIFIED WITH FIXES
all-column mismatch/collar arithmetic             VERIFIED WITH FIXES
terminal arithmetic                               VERIFIED WITH FIXES
Chebyshev thinning cost <12012                    VERIFIED
one-shot slack bound <61000                       VERIFIED CONDITIONAL ON PRODUCER
prime-square/Mellin-Landau endpoint implication   VERIFIED WITH FIXES / INHERITED
```

The proposal does **not** establish RH at the reviewed head. The first inherited load-bearing arrow which still requires a concrete proof object is

```text
native signed equality datum
    -> exact positive factor-67 endpoint-frame packet
       on which Hall, rough ownership, whole-cell integration,
       the one quantizer, and all finite comparisons act together.
```

`L-91674` is an abstract conditional intertwining theorem. `L-91754` names the desired concrete measure and operation order, but it does not derive the full source identity from the native finite datum in one displayed formula. PR #488's `L-91843` does not repair that: it introduces abstract stage packets and then assumes their positivity and source equalities.

The strongest correct conclusion is therefore:

```text
If the frozen common-parent endpoint-frame producer and its
all-column/terminal comparisons are reconstructed exactly,
then the PR #487 one-shot row has native deficit <61000,
and the frozen endpoint consumer implies RH.

PR #488 does not independently establish that antecedent.
```

RH remains unproved.

---

# I. Reconstructed shared mathematical spine

The conclusion-producing chain is not the recursive packet envelope from the earlier proposals. It is the following one-shot chain.

## 1. Exact native arithmetic datum

The full Möbius component row is

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]

The exact finite convolution gives

\[
 C_{c_X}(q)=w_X(q),
 \qquad
 \Xi_{c_X}(q)=\Omega_X(q),
 \qquad
 \mathcal H(c_X)=J_\Lambda(X).
\]

No positivity of `c_X` is asserted or needed at this stage.

**Disposition:** `L-91377` is **VERIFIED**.

## 2. Positive radix-four dual

For

\[
 Y_4(q)=\sum_{h=0}^{v_4(q)}2^h\Lambda(q/4^h),
\]

the exact recurrence

\[
 Y_4(q)-2\mathbf 1_{4\mid q}Y_4(q/4)=\Lambda(q)
\]

gives

\[
 \mathcal H(d)=\sum_qY_4(q)\Xi_d(q),
 \qquad
 J_\Lambda(X)=\sum_qY_4(q)\Omega_X(q).
\]

Thus every detail-feasible nonnegative row satisfies

\[
 J_\Lambda(X)-\mathcal H(d)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)]\ge0.
\]

**Disposition:** `L-91378` is **VERIFIED**.

## 3. Factor-67 fixed-window Hall

For `1<=x<67`, the finite `P_61` Hall theorem uses the positive target atoms

\[
 T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k}
\]

and target-normalized row profiles

\[
 \rho_j(k)=\frac{Q_{x/k}(j)}{4\sqrt{x/k}-3}.
\]

A no-upward transport gives a positive residual target and the exact row identity

\[
 \sum_eT_e\rho_j(e)-\sum_oT_o\rho_j(o)
 =\sum_er_e\rho_j(e)
 +\sum_{o,e}t_{o,e}[\rho_j(e)-\rho_j(o)].
\]

The second term is a nonnegative row bonus. Applying ordinary response at `q` and `4q` separately preserves this equality before the radix-four subtraction.

The directed compact checks and the algebraic Hall transparency are consistent with the previous independent reviews. I found no new counterexample.

**Disposition:** `L-91690` and the total-row part of `L-91692` are **VERIFIED WITH FIXES** at their finite-fiber scope. The exact endpoint-frame realization remains separate.

## 4. Rough-prime first ownership

The projections

\[
 R_j[m]=\mathbf1_{p_j\mid m}
 \prod_{h<j}\mathbf1_{p_h\nmid m}
\]

are disjoint and exhaustive on the rough monoid. They give a unique least-prime owner to every nontrivial rough monomial. This is exact support algebra.

**Disposition:** `L-91688` and the core of `L-91841` are **VERIFIED**.

## 5. Positive endpoint frame and whole-cell support

The intended outer endpoint measure is

\[
 d\mu_X(s)=\frac{2L(X/s)}s\,ds,
\]

restricted to

\[
 I_X=[K+2,X-W-2],
 \qquad K=\lfloor X/67\rfloor+1,
 \qquad W=10000.
\]

The endpoints are integral, so the continuumized adjacent endpoint cells are complete. The partial-cell theorem `L-91840` is mathematically correct and gives a useful general firewall, but the preferred PR #487 route is its immediate whole-cell specialization.

The exact signed-measure statement is:

\[
 \varepsilon_{A_X}(n)=\eta_X(A_X\cap[n,n+1)),
\]

\[
 E_{A_X}(m)-E_{A_X}(m+1)=\varepsilon_{A_X}(m),
\]

\[
 v_q(E_{A_X})=\sum_{j\ge1}\varepsilon_{A_X}(jq).
\]

Restriction must occur before quadrature. This portion is exact.

**Disposition:** `L-91840` is **VERIFIED**.

## 6. One global labelled quantizer

The martingale B-spline quantizer is positive and linear. It preserves the two parabolic endpoint modes in the bulk, has a width-three collar, and is score-favourable. If a labelled positive endpoint measure has already been constructed, one global quantizer may be applied while retaining labels, and the uncoloured physical row is the sum of its labelled components.

This is an exact formal property of the quantizer. The nontrivial input is that the measure to which it is applied is genuinely the common parent of the native arithmetic construction.

**Disposition:** `L-91110` and the formal part of `L-91674` are **VERIFIED WITH FIXES**. The latter is explicitly conditional on its endpoint-producer hypotheses.

## 7. All physical columns

For the retained whole-cell discrepancy, the adjacent estimate

\[
 |\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}
\]

gives, for every `q>=2`,

\[
 |v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\]

\[
 |\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\]

Adding the collar gives

\[
 |\mathcal D_4v_q(C_X-E_X^I)|
 <\frac{971}{4q\sqrt K}.
\]

With

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130},
\]

every nonterminal detail column retains strict reserve. The frozen top omission supplies the terminal margin.

I independently recomputed the decisive arithmetic constants. At `X=10^12`, the nonterminal `Y_4` cost bound is approximately `3.30669`, below the claimed value `4`; the thinning constant is below `12012`; and the terminal comparison constant is `4452*11=48972`.

**Disposition:** `L-91733`, the inherited collar arithmetic, and the terminal numerical synthesis are **VERIFIED WITH FIXES** on their stated analytic inputs.

## 8. Internal child colours and zero exported recursion

The one-shot implementation keeps the current and every causal child as labelled positive colours of the same final quantized row. The exported recursive family is empty. This makes the coefficient budget `<1/8` a provenance check rather than a recursive estimate used by the endpoint consumer.

This is mathematically legitimate if the common-parent identity has already been proved before labels are forgotten. It cannot itself prove that identity.

**Disposition:** the first-owner and causal algebra are **VERIFIED**; the one-shot use is **VERIFIED CONDITIONAL** on the common-parent producer.

## 9. Zero-port specialization

A route which uses only physical component rows, positive source restrictions, one scalar thinning, one quantizer, and comparison estimates need not introduce the older auxiliary Schur port. In that route the port coordinate is absent, not a hidden zero-cost capacity.

`L-91842` proves the abstract implication

\[
 0\preceq D_{c,s}\preceq P_{c,s}
 \quad\Longrightarrow\quad
 0\preceq\sum_{c,s}D_{c,s}\preceq\sum_{c,s}P_{c,s}.
\]

That statement is correct but conditional. It does not instantiate the six demands or their source shares. The preferred one-shot specialization simply declares all of them absent.

**Disposition:** `L-91842` is **VERIFIED WITH FIXES** as an abstract PSD lemma and is **NON-LOAD-BEARING** for the port-free route.

## 10. Native root slack

Once a nonnegative row `d_X` has actually been proved detail-feasible, the definition

\[
 r_X=\Omega_X-\Xi(d_X)
\]

is legitimate and gives `r_X>=0`. No source-level interpretation of `r_X` is required by the endpoint consumer.

The sparse-dual estimates give the following conservative upper bound:

```text
square-root thinning              <12012
nonterminal absolute comparison   <4
terminal absolute comparison      <48972
bottom/top omissions              <1
port and large-endpoint base       0
```

The sum is `60989<61000`.

The proof-relevant statement is an **upper bound** obtained by the triangle inequality and positive duality. It is not an exact decomposition of `r_X` into five disjoint positive slack packets.

**Disposition:** the numerical conclusion of `L-91756/L-91844` is **VERIFIED WITH FIXES**, conditional on the concrete producer and inherited comparison estimates.

## 11. Endpoint consumer

The one-sided finite dual gives

\[
 F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X).
\]

A uniform `<61000` bound is therefore stronger than the required `o(log^2X)` estimate. The unconditional prime-square occupancy asymptotic separates

\[
 A(X)=F_\Lambda(X)
 -\frac{-1-\zeta(1/2)}4\log^2X
 +o(\log^2X).
\]

Hence bounded `F_Lambda` forces eventual negativity of the prime endpoint. The Mellin symbol retains every off-line zero, and Landau's one-sign theorem then gives the proposed implication to RH.

I found no new contradiction in this logical consumer. The lock, however, does not transitively freeze its analytic dependencies: in particular the continuation and pole audit of `L-90004`, the PNT input to `L-90020`, and the contour/Landau details are not all enumerated by `t91840`.

**Disposition:** the endpoint implication is **VERIFIED WITH FIXES / CONDITIONAL** at theorem-composition scope and remains an inherited analytic reconstruction obligation.

---

# II. Findings specific to PR #488

## 1. `L-91840` is a sound firewall

Restriction of a signed defect measure before cell quadrature is the correct operation. The theorem's carry and partition identities are exact. It also correctly notes that the preferred whole-cell construction makes the theorem unnecessary in the main path.

Verdict: **VERIFIED**.

## 2. `L-91841` correctly prevents duplicate rough ownership

The least-prime projections are disjoint and exhaustive. The theorem also gives a valid optional normalization by actual target mass if an exported recursive implementation is chosen.

Two wording corrections are needed:

1. the first-owner restriction must be part of every concrete child operator, not merely part of its label;
2. the one-shot specialization does not use the optional normalized child sum in the endpoint estimate.

Verdict: **VERIFIED WITH FIXES**.

## 3. `L-91842` is an assumption wrapper, not a complete port theorem

Its conclusion follows immediately from the hypotheses. What the old review requested was the construction of the actual complete demand and its available source-owned shares. `L-91842` assumes those objects and inequalities.

The preferred route may avoid the issue by genuinely using no port. Setting abstract variables to zero is not a proof that no inherited correction requires a port; that has to follow from the concrete operation list.

Verdict: **VERIFIED WITH FIXES** as route infrastructure; **UNPROVEN** as a claimed instantiation of the complete historical port demand.

## 4. `L-91843` does not prove the advertised source telescope

This is the first PR-#488-specific broken arrow.

The theorem postulates fourteen stages with disjoint positive packets

\[
 P^{(i)}=C_i+\sum_bP_{i,b}+U_i+\Sigma_i
\]

but it does not define these packets for the actual factor-67 construction or derive the stage equality from the frozen files.

More seriously, stage thirteen includes the finite/continuum mismatch and collar/taper/base **comparison**. The mismatch is introduced elsewhere as a signed defect measure. It is not a positive source packet. The proof may bound its physical response and pay that response from positive unused capacity, but that does not turn the signed comparison into another positive source-partition stage.

The top omission, bottom omission and scalar thinning are positive source restrictions. The quantization collar is the positive difference between a discrete and a continuum seed at its own scope. The finite/continuum mismatch remains signed. These operations cannot all be placed in one uniform positive-source telescope without an explicit Jordan decomposition and ownership theorem, which is absent.

Accordingly, the displayed source telescope does not derive

\[
 \Omega_X
 =\Xi(d_X^{\rm cur})+r_X+
  \sum_b\beta_bU_b^{(1)}\Omega(P_b).
\]

In the preferred one-shot route, that stronger identity is unnecessary: after proving the direct detail inequality one may define the nonnegative external slack by subtraction. But PR #488 claims to have answered PR #484 by a source-derived identity, and it has not.

Verdict: **UNPROVEN / GAP**.

## 5. `L-91844` proves a conservative bound, not an exact slack partition

The arithmetic sum

\[
 12012+4+48972+1=60989<61000
\]

is correct. The thinning estimate is unconditional, the sparse `Y_4` sums are elementary, and the inherited all-column/terminal estimates yield the claimed numerical upper bounds.

What is not proved is the statement that the root slack itself decomposes into disjoint nonnegative classes

\[
 r_X=r_X^{\rm thin}+r_X^{\rm nonterm}
     +r_X^{\rm term}+r_X^{\rm omit}.
\]

The error vectors can be signed. The valid proof uses absolute-value domination and the positive final slack, not an exact positive class decomposition.

Verdict: **VERIFIED WITH FIXES** at upper-bound scope.

## 6. `T-91840` remains conditional on the inherited producer

`T-91840` can be simplified:

```text
if PR #487 genuinely constructs the claimed all-column feasible row,
then its native deficit is <61000,
and the endpoint consumer yields RH.
```

The new `91840` lemmas do not independently prove PR #487's concrete common-parent antecedent. Therefore the full theorem remains a proposed conditional composition rather than an established proof.

Verdict: **UNPROVEN / GAP**.

## 7. `X-91840` is not a reconstruction of the arithmetic packet

The replay checks:

- a toy signed partial-cell measure;
- a three-prime finite first-owner box;
- arbitrary positive-semidefinite two-by-two matrices;
- a synthetic fourteen-stage atom partition;
- a synthetic current/child/slack vector;
- hard-coded cost constants.

It does not instantiate the actual Hall fibres, endpoint-frame measure, quantizer, finite/continuum defect, terminal packet or endpoint consumer. Its mutation tests are useful schema regressions, but they cannot validate `L-91843` or `T-91840`.

Verdict: **EMPIRICAL ONLY**.

## 8. Lock and publication hygiene

The requested head `9acd381f...` is real and was used throughout this review. The PR body still displays the pre-census head `57a9afee...`; it should be updated.

The `t91840` lock authenticates a selected list of imports. It is not a transitive proof lock. The base PR #487 lock supplies additional paths, but even read conjunctively the locks do not enumerate all analytic dependencies of the endpoint consumer.

Verdict: **VERIFIED WITH FIXES** as provenance infrastructure.

---

# III. Inherited-input findings

## A. Inputs which survive this pass

```text
L-91377 native row normalization               VERIFIED
L-91378 positive Y4 dual                       VERIFIED
L-91688 first-owner rough support              VERIFIED
L-91690 compact target Hall                    VERIFIED WITH FROZEN DIRECTED INPUTS
L-91110 positive quantizer algebra             VERIFIED WITH FIXES
L-91733 all-column retained-cell arithmetic    VERIFIED WITH FIXES
L-19885 sparse Y4 sums                         VERIFIED
L-19887 Chebyshev/native thinning bound        VERIFIED
L-90020 prime-square leading asymptotic        VERIFIED WITH FIXES
T-90011 bounded F_Lambda -> prime negativity   VERIFIED WITH FIXES
T-90008 eventual prime sign -> RH              VERIFIED WITH FIXES
```

## B. First inherited open producer interface

`L-91674` is deliberately formal. It begins with a measurable exact fibre identity in a product cone and proves that positive integration, response maps, child placement and one global quantizer commute.

The concrete proof still must identify, at exact normalization, the full native equality datum with the positive factor-67 endpoint-frame object to which those formal operations are applied, including:

1. the exact endpoint source measure;
2. the Hall residual and row bonus as one measurable physical packet;
3. the placement of all rough first-owner colours;
4. the bottom inner source represented by those colours rather than silently omitted;
5. the exact continuum seed generated before the finite mismatch is applied;
6. the equality of the resulting ideal ordinary/detail coordinates with the native target before comparison errors.

`L-91754` lists these operations and declares their outcome. It does not provide one source-level calculation deriving that outcome from `L-91377`, `L-91107`, `L-91690` and `L-91688`.

This is not a complaint that a theorem is merely long. It is the exact interface where the signed native finite row becomes a positive measurable common-parent object. The rest of the one-shot capacity proof consumes that object.

Disposition: **UNPROVEN / GAP**.

## C. Analytic finite-realization inputs

The collar, mismatch and terminal theorems have coherent formulas and constants. They remain proposed theorem files and were not all rerun from their retained directed artifacts in this pass.

The one-shot route uses them only as response comparisons, which is the correct type. They should not be promoted into source equalities.

Disposition: **VERIFIED WITH FIXES / FROZEN INPUTS**.

## D. Endpoint consumer

The implication

\[
 F_\Lambda(X)=o(\log^2X)\Longrightarrow RH
\]

has a coherent chain:

```text
positive prime-square source
 -> deterministic positive log-squared moat
 -> eventual negativity of the prime endpoint
 -> Mellin pole survival
 -> Landau one-sign contradiction for an off-line zero.
```

The proof is independent of the one-shot source construction. No new counterexample was found. A final accepted proof packet must transitively lock and reconstruct the prime-zeta continuation, PNT Riemann sum, contour bounds, real-endpoint interpolation and Landau hypotheses.

Disposition: **VERIFIED WITH FIXES / INHERITED ANALYTIC RECONSTRUCTION**.

---

# IV. Exact reviewed DAG and first broken arrows

```text
full native Möbius row
  -> exact w_X, Omega_X, J_Lambda                  VERIFIED

positive Y4 dual
  -> native deficit = weighted detail slack        VERIFIED

fixed-window P61 Hall
  -> positive residual + positive row bonus         VERIFIED AT FIBRE SCOPE

rough first ownership
  -> one support owner per rough monomial           VERIFIED

fibre Hall packet
  -> concrete positive native endpoint-frame parent UNPROVEN / FIRST INHERITED GAP

whole-cell integration
  -> one positive parent measure                    CONDITIONAL ON PREVIOUS

one global quantizer
  -> nonnegative physical row                       VERIFIED CONDITIONAL

all-column and terminal comparisons
  -> Xi(d_X)<=Omega_X                               VERIFIED ON FROZEN INPUTS

one-shot complement
  -> r_X=Omega_X-Xi(d_X)>=0                         VERIFIED CONDITIONAL

Y4 absolute accounting
  -> <Y4,r_X><61000                                 VERIFIED CONDITIONAL

finite dual
  -> F_Lambda(X)<61000                              VERIFIED CONDITIONAL

prime-square moat + Mellin/Landau
  -> RH                                              INHERITED CONDITIONAL
```

The first PR-#488-specific broken arrow is:

\[
 \boxed{
 \text{signed comparison stages}
 \not\Longrightarrow
 \text{a fourteen-stage positive source telescope}.
 }
\]

The first inherited producer gap is:

\[
 \boxed{
 \text{compact Hall/source fibres}
 \not\Longrightarrow
 \text{the concrete full native common-parent endpoint packet}
 }
\]

from the currently deposited formulas alone.

---

# V. Required repair

A successful successor should avoid proving more than the endpoint consumer needs. It should deposit one exact concrete theorem with the following form.

For each sufficiently large integer `X`, define explicitly a positive endpoint measure `M_X`, a labelled quantizer `Q_X`, and a final finite row

\[
 d_X=Q_XM_X.
\]

Then prove directly:

\[
 d_X(j)\ge0,
\]

\[
 C_{d_X}(q)\le w_X(q),
 \qquad
 \Xi_{d_X}(q)\le\Omega_X(q)
 \quad(q\ge2),
\]

and

\[
 \sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]<61000.
\]

The theorem must give the exact expression for `M_X` in terms of the native source and must show, rather than assume, that:

- the Hall residual and row bonus are the physical fibre of this measure;
- every rough monomial has one retained owner;
- inner source is represented by internal colours rather than omitted;
- the whole-cell continuum object is the exact one compared with the finite native seed;
- the only adverse differences are precisely the stated mismatch, collar, terminal and omission terms.

No recursive child theorem, port theorem or positive source interpretation of the signed mismatch is needed in the one-shot route.

Once that single concrete producer is independently reconstructed, the existing `Y_4` accounting and endpoint consumer would give the proposed conclusion.

---

# VI. Computation boundary

I did not rerun the large directed Hall/profile campaigns, the full endpoint-cell scans, or any heavy formal build.

I inspected:

- the PR #488 theorem files and replay source;
- the base PR #487 one-shot theorem files;
- the exact native normalization and dual files;
- the compact Hall and first-owner inputs;
- the quantizer, mismatch, collar and terminal formulas;
- the Chebyshev/native-thinning proof;
- the sparse `Y_4` estimates;
- the prime-square and Mellin/Landau consumer files;
- the dependency locks and retained replay result.

I independently reconstructed the elementary numerical bounds used in the `<61000` ledger. The PR #488 replay was treated as a finite schema regression, not as a proof of the analytic packet.

---

# Final verdict

```text
shared native arithmetic spine                 substantial and coherent
one-shot capacity/slack strategy               mathematically viable conditionally
new PR #488 partial-cell/ownership firewalls   useful
new PR #488 source telescope                   unproved / overtyped
concrete native common-parent producer         still not independently established
T-91840                                        UNPROVEN / GAP
Riemann Hypothesis                             UNPROVEN
```

The proposal should remain open as a research draft and should not be integrated as a proof of RH.
