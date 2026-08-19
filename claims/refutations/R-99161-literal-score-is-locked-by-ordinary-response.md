# R-99161 — Literal score is locked by the ordinary response and cannot be assigned independently

Claim ID: `R-99161`  
Status: **PROVED EXACT NORMALIZATION FIREWALL / BINDING APPLICATION REFUTATION**  
Created: 2026-08-19  
Depends on: the physical-row definitions used by PRs #513, #620 and #628  
RH status: **unproved**

## 1. Exact score lock

For every finite physical row `r`, let `C_r(q)` be its ordinary response. By
definition its literal score is

\[
\boxed{
\mathcal H(r)=\sum_{q\ge2}\Lambda(q)C_r(q).
}
\tag{R-99161.1}

Thus literal score is not an additional coordinate that may be normalized
independently of the ordinary response vector.

The native capacity is

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
\]

and therefore

\[
\boxed{
P_\Lambda(X)=\sum_q\Lambda(q)w_X(q).
}
\tag{R-99161.2}

Consequently, for every signed ordinary discrepancy `e_X(q)`,

\[
C_r(q)=w_X(q)-e_X(q)
\]

implies the exact identity

\[
\boxed{
\mathcal H(r)
=P_\Lambda(X)-\sum_q\Lambda(q)e_X(q).
}
\tag{R-99161.3}

No Hall, causal, Volterra, cubature or resolvent operation can change
(R-99161.3) while remaining an exact identity in the same physical row space.

## 2. The exact finite native row

The review-503-safe direct-row identity of PR #513 is

\[
d_X^0=c_X-\mathcal R E_X^I,
\]

with

\[
C_{d_X^0}(q)=w_X(q)-v_q(E_X^I).
\]

Therefore

\[
\boxed{
\mathcal H(d_X^0)
=P_\Lambda(X)-\sum_q\Lambda(q)v_q(E_X^I).
}
\tag{R-99161.4}

In particular, the exact finite Möbius row `c_X` satisfies

\[
\boxed{
C_{c_X}(q)=w_X(q),
\qquad
\mathcal H(c_X)=P_\Lambda(X).
}
\tag{R-99161.5}

This is the literal native normalization. A separate value `4sqrt(X)` can only
be a continuum or declared benchmark until an explicit physical-row defect is
inserted.

## 3. Detail domination also locks ordinary score

Put

\[
\Xi_r(q)=C_r(q)-2C_r(4q),
\qquad
\Omega_X(q)=w_X(q)-2w_X(4q).
\]

If one and the same row obeys

\[
\Xi_r(q)\le(1+\varepsilon_X)\Omega_X(q)
\qquad(q\ge2),
\]

then the positive finite radix-four inverse gives

\[
\boxed{
C_r(q)\le(1+\varepsilon_X)w_X(q)
}
\tag{R-99161.6}

and hence

\[
\boxed{
\mathcal H(r)
\le(1+\varepsilon_X)P_\Lambda(X).
}
\tag{R-99161.7}

For the PR #620 comparison,

\[
\varepsilon_X=23/\sqrt K,
\qquad K=\lfloor X/67\rfloor+1.
\]

Assume the endpoint consumer and the same-row claims. They imply RH. Under RH,

\[
P_\Lambda(X)=4\sqrt X-\kappa\log X+O(1),
\qquad \kappa>0,
\]

and `epsilon_X P_Lambda(X)=O(1)`. Thus (R-99161.7) becomes

\[
\mathcal H(r)
\le4\sqrt X-\kappa\log X+O(1),
\]

which contradicts the asserted same-row identity

\[
\mathcal H(r)=4\sqrt X.
\]

Therefore the exact equality-score assertion and the near-native all-column
assertion cannot both apply to one physical row.

## 4. Precise disposition of the candidate interfaces

The abstract nilpotent theorem of PR #628 remains valid. The failure is in its
application:

```text
continuum/declared equality score 4sqrt(X)
        was identified with
literal score of the finite near-native physical row.
```

That identification is not a consequence of Hall, causal splitting, direct
integration or Caratheodory compression. Those operations preserve the
physical row and hence preserve the score lock (R-99161.1).

The required repair is exactly the calibration-defect term of `T99160`:

\[
E_Xs_X=D_X+\mathfrak C_X,
\]

with

\[
\mathcal H(D_X)
=4\sqrt X-\mathcal H(\mathfrak C_X).
\]

The defect must be constructed from primitive finite/continuum and ownership
data. It cannot be supplied by voluntarily thinning a row after a stronger
same-row theorem has already been asserted.

```text
literal score / ordinary-response lock       PROVED EXACT
finite native row score = P_Lambda            PROVED EXACT
same-row detail domination -> score bound     PROVED EXACT
equality score 4sqrt(X) + near-native row      INCOMPATIBLE
abstract nilpotent resolvent                   RETAINED
primitive calibration defect SCDR99160         OPEN / CONCLUSION-PRODUCING
Riemann Hypothesis                             UNPROVEN
```
