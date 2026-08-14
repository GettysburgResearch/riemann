# Independent review of PR #476 — factor-67 triple-closure proposal

## Frozen target

```text
repository:             gfreund123/riemann
proposal PR:            #476
proposal branch:        research/gpt56-pro/91692-triple-closure-proposal
reviewed proposal head: 9f16ce483954d4233b68ee09cb6bec47400aa3cc
proposal base SHA:      13ad1fdbf06edc931dc0c524327b701c5c8f86a3
review cutoff UTC:      2026-08-14T20:38:54Z
```

Live descendants observed before the cutoff include PRs #477, #478 and #479. They are relevant successors, but are not silently imported into this frozen verdict.

## Executive verdict

```text
review disposition: REQUEST CHANGES
T-91662 as an RH proof: REJECTED AS WRITTEN
Riemann Hypothesis: UNPROVEN
```

PR #476 contains a useful conditional Tonelli lemma, correct scalar reserve algebra, and a sound consequence of RH for finite safe-Xi Hankel packets. Its unconditional composition does not survive reconstruction. There are two independent fatal breaks before the endpoint consumer and two further normalization/stability gaps.

## Claim disposition

| Object | Verdict | Surviving scope |
|---|---|---|
| `L-91694`, Sections 1–3 | **VERIFIED CONDITIONAL** | Tonelli preserves an assumed fiberwise target-mass contraction |
| `L-91694`, Section 4 | **SCOPE FIX REQUIRED** | common scaling or restriction of the same positive measure before the split |
| `L-91694`, factor-67 application | **UNPROVEN / GAP** | needs the actual fiberwise weighted target-mass inequality |
| `L-91695`, reserve algebra | **VERIFIED FOR 0<delta<1/2** | exact strict leftover identity |
| `L-91695`, positive refinability | **UNPROVEN / GAP** | fixed native-capacity norm and bounded correction map remain open |
| `L-92114` | **VERIFIED CONDITIONAL ON RH** | every prescribed finite safe-Xi Hankel pair is positive definite |
| `X-91692` | **REGRESSION ONLY** | exact synthetic finite algebra |
| `T-91662`, Statement A | **REJECTED AS A PROOF** | local Hall/provenance inputs may survive separately |
| `T-91662`, Statement B | **CONDITIONAL / INCOMPLETE** | scalar algebra survives |
| `T-91662`, Statement C | **VERIFIED AS RH CONSEQUENCE** | no unconditional Xi conclusion |
| RH | **UNPROVEN** | endpoint implication not reached |

## 1. First fatal break: equality score is not native slack

The resident endpoint consumer uses

\[
\Delta_X(d_X)=J_\Lambda(X)-\mathcal H(d_X)
=\sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]\ge0.
\]

Every native-feasible row therefore satisfies

\[
\mathcal H(d_X)\le J_\Lambda(X).
\]

The frozen factor-67 spine used by `T-91662` instead asserts

\[
4\sqrt X-\mathcal H(d_X)=O(1).
\]

Under the proposal's own claimed RH conclusion, the smoothed explicit formula gives

\[
J_\Lambda(X)=4\sqrt X-\kappa_0\log X+O(1),
\qquad
\kappa_0=\frac{\zeta'}{\zeta}(1/2)>0.
\]

Hence native feasibility would force

\[
4\sqrt X-\mathcal H(d_X)
\ge \kappa_0\log X+O(1),
\]

contradicting the frozen `O(1)` line. Thus the bounded equality-deficit envelope cannot be the source of the claimed native `Y_4` slack.

A repair must work directly with an exact native slack-vector cocycle

\[
\Omega_X=\Xi(c_X)+r_X+\sum_b\alpha_bU_b\Omega_{Y_b},
\qquad r_X\ge0,
\]

and prove the literal root cost `\langle Y_4,r_X\rangle=O(\log X)` or better. PR #477 independently identifies this normalization firewall, but is not a dependency of frozen PR #476.

## 2. Second fatal break: physical columns 2<=q<K_X are uncovered

`L-91691` defines

\[
K_X=\lfloor X/67\rfloor+1.
\]

Its mismatch estimate is proved for `q>=K_X`; the relative detail estimate used by the safety thinning is proved only for `K_X<=q<=X/4`; and the terminal omission treats the upper annulus. This leaves

\[
2\le q<K_X
\]

without a mismatch/collar comparison.

An outer seed discrepancy at an index `n>=K_X` can still contribute to a smaller physical column through multiples `n=jq>=K_X`. Source ownership does not make that response vanish. The required repair splits the response into

```text
jq<K_X       exact inner/recursive owner
jq>=K_X      one current outer mismatch owner
```

and proves one comparison for every physical `q>=2`. PR #479 was created on top of the exact #476 head to address this range; it cannot be counted retroactively.

## 3. `L-91694`: correct abstract theorem, incomplete arithmetic application

The Tonelli argument is correct under its displayed premise

\[
\sum_i a_i(s)m(A_{s,i}Q_{s,i})
\le\rho m(P_s),
\qquad \rho<1/8.
\]

The cited causal result supplies only the unweighted coefficient statement

\[
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

The application still needs an actual child target-mass comparison in the factor-67 root-fiber normalization, for example `m(A_{s,i}Q_{s,i})<=m(P_s)`, or another exact weighted estimate. Children may be grouped only by labels that also fix the complete typed placement.

The statement about omission must also be narrowed: subcriticality is preserved by common scaling or by restricting the same positive measure before the current/child split, not merely because both parent and child masses decrease.

`X-91692` checks synthetic fiber ratios already assumed below `1/8`; it does not verify this arithmetic premise.

## 4. `L-91695`: algebra survives, analytic refinability remains open

For `0<delta_M<1/2`, with `sigma_M=1-2delta_M`, the identity

\[
2\delta_M-(1-2\delta_M)\delta_M
=\delta_M+2\delta_M^2>0
\]

is exact. The strict statement needs an explicit treatment of `delta_M=0`.

The substantive gap is the claimed uniform approximation in one native-capacity-normalized norm. Native capacities and active coordinates vary and may vanish at activation boundaries. The proposal does not yet prove:

- one fixed normalized space over the complete root window;
- relative interpolation bounds near vanishing capacities;
- realization of the interpolant by an admissible positive endpoint measure;
- boundedness of the complete mismatch/collar/terminal/port map in that same norm.

Thus Statement B is a conditional stability interface, not a closed root producer.

## 5. `L-92114` survives as an exact RH consequence

Under RH,

\[
\frac{\Xi_c'(\sqrt q)}{\sqrt q\,\Xi_c(\sqrt q)}
=2\sum_{\gamma>0}\frac1{q+\gamma^2}.
\]

The barycentric partial-fraction identity gives

\[
m_k=2\sum_{\gamma>0}
\frac{\gamma^{2k}}{\prod_i(q_i+\gamma^2)}.
\]

Therefore each required Hankel quadratic form is a positive sum of polynomial squares, and is strictly positive because a nonzero polynomial has finitely many roots while Xi has infinitely many positive zero ordinates. The matrix dimensions must be interpreted according to the parity cases in `L-92112`.

This theorem is downstream of RH and cannot repair Statement A.

## Replay boundary

The retained replay verifies only:

```text
weighted-average algebra for assumed subcritical toy fibers;
scalar reserve algebra for one rational control;
a finite positive Stieltjes pole model and exact LDL pivots;
five fail-closed mutations.
```

It does not replay the factor-67 arithmetic producer, all physical columns, native refinement, common port/collar/top omission, native slack cocycle, endpoint-to-RH chain, or actual Xi product before RH.

## Minimal repair order

1. close all physical ordinary/detail columns, including `2<=q<K_X`;
2. replace the equality-score recurrence by the exact native slack cocycle and literal root `Y_4` cost;
3. prove the actual fiberwise target-mass contraction before Tonelli and grouping;
4. export a positive capacity-relative refinement in one fixed norm and bound the correction operator;
5. reconstruct the one-sided endpoint consumer on that same packet;
6. append `L-92114` only after RH has been independently established.

## Final verdict

```text
L-91694 abstract Tonelli mechanism        SURVIVES WITH SCOPE FIXES
L-91695 strict reserve algebra             SURVIVES CONDITIONALLY
L-92114 RH -> finite Hankel PD             VERIFIED
factor-67 all-column native realization    NOT ESTABLISHED AT FROZEN HEAD
native Y4 slack recurrence                 NOT ESTABLISHED AT FROZEN HEAD
T-91662 complete composition               REJECTED AS WRITTEN
Riemann Hypothesis                         UNPROVEN
```
