# T-91720 — Target-Lorenz vector producer gives a fail-closed native-root resolution proposal

Claim ID: `T-91720`  
Status: **PROVED CONDITIONAL COMPOSITION / TWO EXPLICIT LIVE GATES**  
Created: 2026-08-14  
Normative new input: `L-91720`  
Retained inputs: `L-91362`, `L-91375`, `L-91377--L-91380`, `L-91682--L-91684`, `T-91312--T-91314`  
Cross-branch ledger input: abstract atomwise theorem `L-91671` on PR #454  
RH status: **unproved**

## 1. Purpose

The stopped-leaf no-upward Hall theorem is false and remains withdrawn. The
canonical `P_61` finite-Euler row also cannot be spent as current while its
rough reservoir is exported as children.

This proposal uses instead one common source submeasure at each actual causal
leaf. `L-91720` proves that the Target-Lorenz submeasure is the exact vector
optimizer and emits a dual obstruction if it fails.

## 2. Arithmetic Vector-Lorenz Theorem (`AVLT`)

The sole leafwise arithmetic sign required by this proposal is

\[
\boxed{
 \mathfrak L_j(p,y)
 =R_j(U_{p,y})-O_R^{(j)}(p,y)\ge0
}
\tag{T-91720.1}
\]

for

\[
 p\ge67,
 \qquad1\le y<67,
 \qquad2\le j\le66.
\]

Here `U_(p,y)` is the leftmost even target submeasure of exact target `O_T`.
The cutoff is one of the 185 even `P_61` divisors below 2000.

By `L-91720`, (T-91720.1) is not merely sufficient for the greedy ansatz. It is
necessary and sufficient for the entire exact-target common-source submeasure
cone, simultaneously in all 65 rows. If it fails, (L-91720.8) gives an exact
coordinate separator.

`AVLT` remains an arithmetic theorem to be certified. `L-91722` supplies the
stronger-to-prove but simpler sufficient gate

\[
 \mathscr R_jK_T(c)-\mathscr TK_R^{(j)}(c)\ge0,
\]

using the complete signed packet and one cutoff atom.

## 3. Leafwise common-source packet under `AVLT`

Assume `AVLT`. At each source-disjoint stopped leaf, let

\[
 \nu=E-U.
\]

Then, exactly,

\[
 T(\nu)=E_T-O_T,
\tag{T-91720.2}
\]

\[
 S(\nu)\ge E_S-O_S,
\tag{T-91720.3}
\]

and for every component row

\[
 E_R^{(j)}-O_R^{(j)}
 =R_j(\nu)+B_j,
 \qquad
 B_j=R_j(U)-O_R^{(j)}\ge0.
\tag{T-91720.4}
\]

The same source coefficient is used in target, score and every row. Applying
the positive resident ordinary and radix-four response maps to the nonnegative
row identity gives one simultaneous physical capacity ledger. No coordinate
chooses an independent complement.

## 4. Source-disjoint rough recursion

`L-91362` partitions the source tree into one finite forcing and actual rough
children labelled by their unique least rough prime. Every child endpoint is
at most `X/67`, and every source atom has one owner.

The causal coefficient budget supplies nonnegative child coefficients with

\[
 \rho:=\sum_b\alpha_b<\frac18.
\tag{T-91720.5}
\]

The same-index functor inserts each actual child once in literal row, ordinary
capacity, radix-four capacity and score coordinates.

Because (T-91720.4) is an equality before applying response maps, current and
recursive pieces spend one parent packet rather than separate coordinatewise
copies.

## 5. Live Atomwise Native-Root Ledger (`ANRL`)

The remaining root-level implementation gate is to export the finite live
source/channel matrix for

```text
outer producer;
Target-Lorenz finite forcing;
collar;
finite/continuum mismatch;
top omission and terminal taper;
one shared endpoint port;
recursive child;
stop/base packet;
weighted slack.
```

Every source occurrence must satisfy one coefficient partition, and every
local identity must use the native target/score/row/ordinary/detail/port
normalization.

The abstract sufficiency and Farkas alternative are already proved by
`L-91671` on PR #454. What remains is the live export and either:

\[
 Bx=b,\qquad Gx\le c,\qquad x\ge0,
\tag{T-91720.6}
\]

or one exact Farkas separator. This proposal calls the successful live
certificate `ANRL`.

## 6. Native-root consequence

Assume `AVLT` and `ANRL`. The current row and source-disjoint children then
satisfy the Native-Root Capacity Theorem `T-91314`:

\[
 C_{d_X^{\rm cur}}(q)
 +\sum_b\alpha_bC_{P_b}(q)
 \le w_X(q),
\tag{T-91720.7}
\]

\[
 \Xi_{d_X^{\rm cur}}(q)
 +\sum_b\alpha_b\Xi_{P_b}(q)
 \le\Omega_X(q),
\tag{T-91720.8}
\]

with every fixed correction and common port charged once.

The positive typed causal debt is bounded by twice exact target mass after
entry. Therefore the packet envelope obeys

\[
 \Lambda(X)
 \le C_{\rm fin}+2+\rho\Lambda(X/67+C_0),
 \qquad\rho<\frac18,
\tag{T-91720.9}
\]

where `C_fin` is the one-use finite correction cost supplied by `ANRL`. Hence

\[
 \Lambda(X)=O(1).
\tag{T-91720.10}
\]

A weaker one-use `O(log(3X))` current correction would still give
`Lambda(X)=O(log X)=o(log^2X)` and is sufficient.

## 7. Positive weighted-slack form

Using the exact radix-four dual,

\[
 J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)
  [\Omega_X(q)-\Xi_{d_X}(q)].
\tag{T-91720.11}
\]

Thus `ANRL` may certify either exact residual packing or a nonnegative slack
whose `Y_4`-weighted total is `o(log^2X)`. Exact zero slack is not required and,
by `L-91380`, would already force the full native Möbius row.

## 8. Endpoint conclusion

Under `AVLT` and `ANRL`, `T-91313` converts the resulting one-sided endpoint
deficit bound into the proposed RH conclusion through the retained finite dual
and Mellin--Landau consumer.

This section is a conditional implication. It does not promote either live gate
or RH.

## 9. Immediate falsifiers

Reject this proposal on the first occurrence of any of the following:

```text
one Target-Lorenz margin is negative;
a claimed common-source repair uses different source coefficients by row;
a boundary or common-port coordinate has two owners;
the canonical P_61 rough reservoir is spent current and recursively;
a child coefficient is scaled twice;
a source identity is used without its physical row/response realization;
the finite correction grows too quickly for o(log^2 X);
the endpoint inequality has the wrong one-sided orientation.
```

A negative margin is especially informative: `L-91720` turns it into a dual
separator for every exact-target even-source submeasure. It refutes this source
cone cleanly while leaving broader cones available.

## 10. Live genealogy scope

This theorem was authored from the PR #468/#467 stopped-leaf frontier. During
publication, PR #470 independently proved the same leftmost-basis optimality
for the live finite box LP and exposed an exact native-capacity separator for
the raw current-plus-child basis. PR #473 later proposed a distinct factor-67
root-Hall/SONTR realization.

Accordingly this theorem is a conditional **fallback route and dual audit**. It
must not be read as superseding the newer SONTR route, and it inherits the PR
#468 native-reservoir firewall: no finite-Euler rough capacity may be spent both
as current and as recursive child.

## 11. Exact boundary

```text
Target-Lorenz vector optimization and duality       PROVED / L-91720
common target/score source typing                    PROVED ON RETAINED INPUTS
complete causal profile order p>=67                  PROVED / L-91682
AVLT arithmetic row margins                          OPEN / EXPLICIT
abstract atomwise root-ledger alternative            PROVED / PR #454
ANRL live root source/channel allocation              OPEN / FINITE
subcritical consumer and positive Y_4 dual            PROVED CONDITIONAL
full implication after AVLT + ANRL                    PROVED CONDITIONAL
Riemann Hypothesis                                   UNPROVEN
```
