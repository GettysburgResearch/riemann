# L-92934 — Actual source-tree children may be internalized by one label-blind quantizer without creating a rough lift

Claim ID: `L-92934`
Status: **PROVED EXACT ONE-SHOT SPECIALIZATION OF THE NATIVE SOURCE IDENTITY**
Created: 2026-08-15
Primary inputs: `L-92931`; the coupling and label-blind Markov kernel of `L-91850/L-91852`
RH status: **unproved**

## 1. Native source identity before quantization

Retain the exact source-disjoint identity

\[
 P_X^{\rm nat}
 =P_X^{\rm cur,ideal}
 +\sum_b A_b
 +U_X^{\rm src}
\tag{L-92934.1}
\]

from `L-92931`.  Each `A_b` is an actual source-tree child with its channel,
least-prime and same-index labels.  The sum in (L-92934.1) is not the row-first
rough lift.

Let `Q_X` be the one physical Markov kernel of the PR #500 compiler.  Its domain
contains only the physical endpoint state; it does not contain a Hall, channel,
rough-owner, current or child label.

## 2. Internalization is linear label erasure

Apply `Q_X` after all positive physical placements.  Linearity gives

\[
\boxed{
 Q_X\left(P_X^{\rm cur,ideal}+\sum_bA_b\right)
 =Q_XP_X^{\rm cur,ideal}+
  \sum_bQ_XA_b.
}
\tag{L-92934.2}
\]

Thus “children remain internal colours” means only that the right side of
(L-92934.2) is stored as one output marginal.  It does not replace `A_b` by a
standard native packet or by a first-owner rough-lift reservoir slice.

The input marginal remains (L-92934.1), so every source occurrence has one
owner even after labels are hidden from the final row.

## 3. Native normalization and the `q=2` test

Apply ordinary response at `q` and `4q` to (L-92934.1) before forming detail.
The result is the native ideal response because (L-92934.1) is the observed
paired source-tree identity.  Consequently the signed comparison and unused
capacity give

\[
 \Omega_X=\Xi(d_X)+r_X,
 \qquad r_X\ge0,
\tag{L-92934.3}
\]

for the one-shot output after the frozen all-column comparison.

If (L-92934.1) is replaced by the full rough lift, `R-92930` changes the ideal
`q=2` response by at least `log(4)/sqrt(134)`.  Hence the `q=2` test verifies the
**input marginal**, not whether child labels are externally visible.

## 4. One-shot cost

The four named root classes of `L-91853` apply unchanged:

```text
thinning       <12012
nonterminal    <4
terminal       <48972
omissions      <1
-------------------
total          <60989.
```

No child is exported and no child terminalization cost is added.  Therefore,
on the frozen analytic estimates,

\[
\boxed{
 0\le J_\Lambda(X)-\mathcal H(d_X)<60989.
}
\tag{L-92934.4}

## 5. Relation to the fallback

If a reviewer prefers externally auditable child capacities, use `L-92932`:
export the same actual `A_b`, realize them once, and obtain the weaker but more
modular bound `<61744`.  The one-shot and terminal-child routes share the same
native source marginal and differ only in when the actual child labels are
erased.

```text
actual native source identity                 retained
one label-blind quantizer                     exact
internal child colours                        valid linear specialization
full rough-lift substitution                  forbidden
one-shot native deficit                       <60989 on frozen estimates
terminal-child fallback                       <61744
Riemann Hypothesis                            unproved
```
