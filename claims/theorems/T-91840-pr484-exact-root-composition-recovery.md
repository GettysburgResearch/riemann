# T-91840 — Recovered exact-root composition after the PR #484 audit

Claim ID: `T-91840`  
Status: **CANDIDATE-COMPLETE COMPOSITION PROPOSAL ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Base proposal: PR #487 at `39d2cbc7cabf31ac1f8013f2f6d1785c86a4fdeb`  
Review input: PR #484 at `aadf3541f9959e27a5e0eea890a13a8eb0467b01`  
New inputs: `L-91840--L-91844`, `O-91840`  
RH status: **unproved pending independent reconstruction**

## 1. Exact producer

For every integer `X>=10^12`, the exact measurable Hall integration and
whole-cell endpoint producer of PR #487, hardened by the sequential ownership
ledger `L-91843`, produces a finite coefficientwise nonnegative row `d_X` with

\[
\boxed{C_{d_X}(q)\le w_X(q),\qquad q\ge2,}
\tag{T-91840.1}
\]

and

\[
\boxed{
 \Omega_X=\Xi(d_X)+r_X,
 \qquad r_X\ge0.
}
\tag{T-91840.2}
\]

The equality and positivity are proved together from a source partition. They
are not obtained by defining `r_X` as an untyped remainder.

Every causal child is first-owner restricted by `L-91841` and remains an
internal colour of `d_X`. The exported recursive family is empty, so

\[
\boxed{\sum_b\beta_b=0<\frac18.}
\tag{T-91840.3}
\]

The auxiliary port is zero in the controlling route. `L-91842` gives the exact
one-owner aggregation theorem if a reviewer reconstructs the older portful
alternative.

## 2. Native deficit

By the exact radix-four dual,

\[
\Delta_X(d_X)
 =J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,r_X\rangle.
\tag{T-91840.4}
\]

`L-91844` gives

\[
\boxed{0\le\Delta_X(d_X)<61000.}
\tag{T-91840.5}
\]

No comparison between `J_Lambda(X)` and `4sqrt(X)` is used.

## 3. Endpoint composition

The frozen endpoint consumer gives

\[
F_\Lambda(X)\le\Delta_X(d_X)=o(\log^2X).
\tag{T-91840.6}
\]

The unconditional prime-square moat then forces eventual negativity of the
prime-only endpoint. The frozen Mellin pole audit and Landau one-sign theorem
exclude every zero to the right of the critical line; the functional equation
supplies the symmetric half.

Thus the packet proposes

\[
\boxed{\mathrm{RH}.}
\tag{T-91840.7}
\]

This is a proposal conclusion only. RH remains unproved until every frozen
analytic input and every composition interface is independently reconstructed.

## 4. PR #484 disposition

```text
fully corrected root packet identity             L-91843 / exact composition
complete common-port demand                      L-91842 / zero in preferred route
terminal/base/port exact Y4 cost                  L-91844 / no double charge
partial-cell ownership                            L-91840 / whole-cell specialization
first-owner global child operators                L-91841
RH-bearing benchmark bridge                       absent
endpoint/Mellin/Landau chain                      frozen exact-SHA review input
```

## 5. Immediate falsifiers

Reject at the first failure of:

```text
measurability or exactness of the root Hall kernel;
whole-cell support or restriction-before-quadrature typing;
first-owner disjointness;
one global labelled quantizer;
nonnegative all-column and terminal reserve;
port-free typing, or source-partitioned port shares if a port is used;
any line of the direct Y4 cost ledger;
prime-square moat or Mellin--Landau consumer;
any dependency SHA/path mismatch.
```

## 6. Exact boundary

```text
PR #484 producer objections                  addressed in one typed DAG
PR #487 one-shot SONTR/NRCT                  retained and composition-hardened
native deficit                               <61000 on frozen inputs
complete proposal                            yes, pending independent review
accepted proof of RH                         no
Riemann Hypothesis                           unproved pending review
```
