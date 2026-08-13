# Independent review of PR #447 — corrected provenance-causal factor-54 closure

**Review verdict:** `UNPROVEN / GAP`  
**Mathematical type:** proposed complete theorem  
**Riemann Hypothesis:** **not established**  
**Review cutoff / final head recheck:** `2026-08-13T21:33:34Z`

## Frozen repository state

```text
repository:    gfreund123/riemann
proposal PR:   #447
proposal base: research/gpt56-pro/91355-causal-packet-budget
base SHA:      706445c01d4a5c9f852a4faf1329bd9858dc727a
proposal head: research/gpt56-pro/91661-corrected-provenance-closure
head SHA:      d44c45b3ececa878296914a49e49279b10a1f637
main observed: 9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
PR state:      open / draft / mergeable
```

No movement of the proposal head was observed between the substantive review and the final state check.

The principal reviewed blobs were:

```text
R-91654  409d63af63e249873d001858ee7fec944f0a7005
L-91661  9de33cccaa9728cf6749ed2592ee2bd932b0ad3a
L-91662  b5a4be7838f6f7d04e2664ffdc88e5eb89c54b41
L-91659  39834c1d35c3e443d11c2ac8349f36db5084bb05
T-91652  d99b86e37b32cd105ba2ee82f2052b78c3f2bd64
X-91651  c2ae9923dfd5a18e0bec24465a3f899e204973d6
```

## Executive verdict

PR #447 contains a substantial and mathematically useful correction layer. In particular, it correctly identifies and repairs the direct canonical-`P_61` normalization error, replaces the duplicated child accounting by an exact provenance-causal reset, obtains a genuinely subcritical recursive coefficient, and corrects the endpoint conclusion to the one-sided statement actually needed.

Those improvements do **not** yet prove RH. The first load-bearing unproved arrow is

\[
\boxed{\texttt{L-91659: native root current ledger}.}
\]

The root file defines the current datum as a coordinatewise complement and then asserts that a sum of Hall, outer B-spline, collar, mismatch, omission and endpoint-port rows is feasible in that complement. The exact componentwise inequalities proving this assertion are not supplied. Several cited imports either prove only conditional implications or explicitly retain the relevant routing/compatibility theorem as open.

Accordingly:

```text
new normalization firewall and causal envelope   SURVIVE
native root feasibility                          UNPROVED
full T-91652 composition                         UNPROVEN / GAP
Riemann Hypothesis                               UNPROVEN
```

This is a missing proof rather than an exact counterexample to the desired root theorem, so the proposal is not classified as false.

# I. What is verified

## 1. The canonical `P_61` native-capacity firewall is correct

`R-91654` derives

\[
C_{P,X}(q)-w_X(q)
=
\frac1{\sqrt q}
\sum_{\substack{2\le n\le X/q\\(n,P_{61})=1}}
\frac1{\sqrt n}\log\frac{X}{qn}.
\]

Every summand is nonnegative. The first integer greater than one coprime to `P_61` is `67`, and the exact first strict witness is

\[
C_{P,136}(2)-w_{136}(2)
=
\frac1{\sqrt{134}}\log\frac{68}{67}>0.
\]

Thus the globally nonnegative canonical finite-Euler row cannot be inserted unchanged into the native ordinary cone. This refutes only the native-capacity identification, not positivity of the canonical row itself.

**Classification:** `VERIFIED`, exact refutation.

## 2. The finite-Euler excess is exactly the rough-child reservoir

`L-91661` uses unique least-prime factorization to obtain

\[
H_P(Z)
=
\log Z+
\sum_{\substack{p\ge67\\p\le Z}}
 p^{-1/2}H_{\ge p}(Z/p),
\]

and hence, column by column,

\[
C_{P,X}(q)
=
w_X(q)+
\sum_{\substack{p\ge67\\pq\le X}}
 p^{-1/2}C_{\ge p,X/p}(q).
\]

This exactly identifies the normalization excess with the capacity owned by the actual rough children. Packing the full finite-Euler row and also retaining those children would double-spend the same capacity.

**Classification:** `VERIFIED`, unconditional exact theorem.

## 3. The provenance-causal coefficient reset is exact and subcritical

For

\[
r_i=p_i^{-1/2},\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad
\lambda_i=r_i s_{i-1},\qquad
\alpha_i=r_i\lambda_i,
\]

the displayed identity

\[
P_X
=
s_kP_X
+
\sum_i\lambda_i\bigl(P_X-r_iU_{p_i}P_{X/p_i}\bigr)
+
\sum_i\alpha_iU_{p_i}P_{X/p_i}
\]

is algebraically correct. Moreover,

\[
s_k+\sum_i\lambda_i=1
\]

and

\[
\rho:=\sum_i\alpha_i
<67^{-1/2}<\frac18.
\]

The current certificate mass is therefore one, while the actual recursive children have strictly contracting total coefficient.

**Classification:** `VERIFIED`, unconditional coefficient theorem.

## 4. The abstract packet envelope is valid once its producer hypotheses hold

Given uniformly bounded current-generator debt, exact complete-datum child covariance and a valid root decomposition, positive homogeneity and subadditivity yield

\[
\Lambda(X)
\le C_*+\rho\Lambda(X/67),
\qquad \rho<\frac18,
\]

and therefore

\[
\Lambda(X)
\le\frac{C_*}{1-\rho}
<\frac{8C_*}{7}.
\]

The recurrence is not the disputed step. Its root producer hypothesis is.

**Classification:** `VERIFIED CONDITIONAL IMPLICATION`.

## 5. The one-sided endpoint correction is correct

If

\[
F_\Lambda(X)\le K,
\]

then

\[
\limsup_{X\to\infty}
\frac{F_\Lambda(X)}{\log^2X}
\le0.
\]

Since

\[
\frac{-1-\zeta(1/2)}4>0,
\]

this meets the resident strict endpoint threshold. No lower bound for `F_Lambda` and no conventional two-sided `O(1)` assertion are needed.

**Classification:** `VERIFIED WITH THE STATUS OF THE INHERITED ENDPOINT CONSUMER RETAINED`.

# II. The load-bearing gap in `L-91659`

`L-91659` defines

\[
\mathcal C_X
=
\mathcal N_X-\mathcal R_X,
\qquad
\mathcal R_X=R_X\widehat Z_X,
\]

so that

\[
\mathcal N_X=\mathcal C_X+R_X\widehat Z_X
\]

is tautologically an exact identity in the ambient vector space of endpoint data. It then proposes the current row

\[
d_X^{\rm cur}
=
d_X^{\rm edge}+d_X^{\rm outer}+d_X^{\rm port}
\]

and asserts

\[
d_X^{\rm cur}\in\mathcal F_X(\mathcal C_X).
\]

Defining a coordinatewise complement does not prove that the complement capacities are nonnegative, nor that the proposed row lies below them.

A valid proof must display, for every ordinary column `q`,

\[
\Gamma_X(d_X^{\rm cur})(q)
\le
w_X(q)-\Gamma_X(\mathcal R_X)(q),
\]

for every radix-four column `q`,

\[
\Xi_X(d_X^{\rm cur})(q)
\le
\Omega_X(q)-\Xi_X(\mathcal R_X)(q),
\]

and the analogous inequalities in every exact component-row and boundary-reserve coordinate.

The inequalities must be checked after summing all current contributions. Independent feasibility of several pieces against the full parent budget does not imply feasibility of their sum against the residual budget after the recursive certificate is removed.

The coordinate table in Section 5 of `L-91659` lists references and then says “consequently” that the capacities are nonnegative and the current row is feasible. No complete common-normalization calculation proving that consequence is present.

# III. Why the cited imports do not currently close the root theorem

## A. The Hall source typing is not yet the native root-capacity inequality

`L-91340` constructs a positive Hall representation that is exact in endpoint score and subordinate to the `W_Psi` target. `L-91341` lifts it to nonnegative exact finite component rows.

These are substantial results, but their conclusion-relevant kernels are

\[
W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
\qquad
W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\]

They do not by themselves prove the native ordinary and radix-four inequalities against

\[
w_X(q),\qquad\Omega_X(q).
\]

`L-91341` itself records the all-generation row/capacity assembly as open. The corrected causal reset repairs the duplication and coefficient recurrence, but it does not supply the missing root-level residual-capacity comparison.

## B. The literal butterfly route retains declared finite gates

`L-91659` describes `d_edge` as interval/butterfly rows. But `L-91321` explicitly states that it does not prove:

1. that the negative butterfly-center intensity is dominated by the resident baseline endpoint weights;
2. that the explicit positive upper-boundary atom fits in the remaining capacities.

There are therefore only two coherent repairs:

- use the literal butterfly realization and solve those two finite gates; or
- avoid the butterfly realization, use the direct nonnegative row from `L-91341`, and prove its complete native ordinary/detail/boundary feasibility explicitly.

The current root statement does neither.

## C. `L-90029` is a conditional telescope, not the missing antecedent

`L-90029` proves

\[
\text{detail feasibility}\Longrightarrow\text{ordinary feasibility}.
\]

It does not prove that the actual combined current row in `L-91659` satisfies detail feasibility. The root file supplies neither an explicit endpoint-weight vector for the full current sum nor a columnwise detail-slack certificate. Thus a valid implication is being cited without its hypothesis being established for the packet under review.

## D. The endpoint-port import changes small-prime normalization

`L-91316` is written for

\[
P_{53}=\prod_{p\le53}p
\]

and rough threshold `59`. Its quantitative port estimate uses

\[
\prod_{p\le53}\left(1+\frac1p\right)<\frac92.
\]

The corrected proposal uses `P_61` and rough threshold `67`. In that normalization,

\[
\prod_{p\le61}\left(1+\frac1p\right)
=
\frac{399441300081868800}{86204059532560853}
\approx4.6336715724
>
\frac92.
\]

This does not obstruct boundedness; it merely shows that the exact `P_53` theorem and its constants cannot be imported verbatim. A `P_61/67` adapter and a corresponding capacity placement are required. `L-91316` itself also retains “capacity-faithful conservative child routing” as open.

## E. The child functor cannot create the root source identity

`L-91658` correctly proves covariance and subadditivity after an exact source-disjoint datum identity has been supplied. It does not prove that the Hall residual, outer producer, common port and recursive certificate actually form such a source-disjoint identity in the native root datum. That missing identity and its coordinatewise feasibility are exactly the burden of `L-91659`.

# IV. Replay boundary

The retained `X-91651` result checks:

```text
reset coefficient algebra;
child cancellation;
recursive mass below 1/8;
geometric envelope arithmetic;
root mass-54 scalar arithmetic;
one-sided endpoint logic;
finite least-prime partition structure;
identifier shape and uniqueness.
```

It explicitly does not replay the Hall, B-spline, collar, finite/continuum mismatch, terminal omission or endpoint-port certificates. Those omitted objects are precisely the inputs needed to prove the disputed root feasibility statement.

Therefore

```text
PASS_CORRECTED_PROVENANCE_ENVELOPE_ALGEBRA
```

certifies the outer algebraic shell, not the native root theorem.

# V. Claim-level classifications

| Claim | Mathematical type | Review verdict | Surviving scope |
|---|---|---|---|
| `R-91654` | exact refutation | **VERIFIED** | direct canonical-`P_61` / native-ramp splice is invalid |
| `L-91661` | unconditional theorem | **VERIFIED** | exact least-prime rough-reservoir decomposition |
| causal reset in `T-91652` | unconditional theorem | **VERIFIED** | exact nonduplicating provenance identity |
| recursive mass `<1/8` | unconditional theorem | **VERIFIED** | genuine coefficient contraction |
| `L-91658` | route infrastructure | **VERIFIED WITH SCOPE** | valid after an exact source-disjoint datum identity is supplied |
| packet-envelope recurrence | conditional implication | **VERIFIED** | valid once producer and root hypotheses are proved |
| `L-91662` | conditional implication | **VERIFIED WITH SCOPE** | one-sided upper bound is sufficient under the resident endpoint theorem |
| `X-91651` | finite replay | **VERIFIED AS SCOPED** | algebraic shell only |
| `L-91659` | proposed complete root lemma | **UNPROVEN / GAP** | definitions and mass-54 arithmetic survive |
| `T-91652` | proposed complete RH theorem | **UNPROVEN / GAP** | conditional composition after root feasibility |
| Riemann Hypothesis | final conclusion | **UNPROVEN** | no promotion |

# VI. Exact theorem still required

The proposal has reduced the remaining burden to a concrete and potentially finite certificate. The theorem still needed is:

> **Native-root capacity theorem.** Construct an explicit nonnegative current row `d_X^cur` and an explicit source-disjoint recursive datum `R_X Z_X` such that every coordinate of `N_X-R_X Z_X` is nonnegative, `d_X^cur` uses no more than those residual capacities, and the current score deficit is bounded by one absolute constant.

A reviewable proof object should contain:

1. exact endpoint-row coefficients for all Hall/direct-row or butterfly, outer, collar, mismatch, omission and port pieces;
2. exact recursive source coefficients;
3. ordinary response vectors;
4. radix-four response vectors;
5. every boundary-port vector;
6. a componentwise residual-capacity comparison for the sum of all current pieces;
7. a `P_61/67`-normalized common-port calculation;
8. a one-use ledger proving no correction occurs in both current and recursive packets.

Only after this object is supplied does the verified causal reset imply a uniform packet envelope, and only then does the verified one-sided endpoint argument complete the implication to RH.

# Final assessment

PR #447 is a materially improved conditional architecture. It closes the normalization firewall, exact rough-reservoir identity, nonduplicating recursive coefficient ledger and one-sided endpoint orientation. It does not close the native-root feasibility theorem on which the asserted bounded deficit depends.

\[
\boxed{\text{PR #447: UNPROVEN / GAP}}
\]

\[
\boxed{\text{RH remains unproved at }d44c45b3ececa878296914a49e49279b10a1f637.}
\]
