# L-92933 — Physical root coupling plus actual terminal children has native deficit below `61744`

Claim ID: `L-92933`
Status: **CANDIDATE-COMPLETE DIRECT NATIVE-COST COMPOSITION ON FROZEN ESTIMATES — REVIEW REQUIRED**
Created: 2026-08-15
Primary inputs: `L-91853`; `L-92931`; `L-92932`; native dual `L-91378`
RH status: **unproved**

## 1. Restricting to the current marginal does not enlarge the root ledger

The PR #500 one-shot coupling is a positive labelled measure whose current and
actual-child classes are disjoint.  The fallback route restricts that measure to
the current labels before finite realization.  Common thinning and literal
omissions are positive operations, so their `Y_4` costs can only decrease under
this restriction.

The nonterminal and terminal comparison errors are signed labelled measures.
Restriction to the current label set does not increase total variation.  Since
the frozen bounds are obtained by pairing `Y_4>=0` against total-variation
majorants, the same numerical majorants remain valid for the exported-child
route.

Thus the `<60989` ledger is an upper bound both for the total one-shot coupling
and for its current-only restriction.

## 2. Root cost

The root physical coupling has four named cost classes:

```text
common square-root thinning             <12012
nonterminal signed comparison               <4
terminal signed comparison               <48972
positive omissions                          <1
port / large-X base                          0
----------------------------------------------
root total                                <60989
```

The signed comparison is paid by direct absolute `Y_4` pairing. It is not paid by positive source mass. No estimate of `J_Lambda(X)-4sqrt(X)` is used.

Thus

\[
 \delta_X^{\rm root}
 :=\langle Y_4,r_X\rangle<60989.
\tag{L-92933.1}
\]

## 3. Add the actual children once

By `L-92932`,

\[
 \sum_b\beta_b\Delta(\widetilde P_b)<\frac{6039}{8}.
\tag{L-92933.2}
\]

The exact benchmark/literal-score coordinates of the typed source identity give

\[
 J_\Lambda(X)-\mathcal H(d_X)
 =\delta_X^{\rm root}
  +\sum_b\beta_b\Delta(\widetilde P_b).
\tag{L-92933.3}
\]

Therefore

\[
\boxed{
 0\le J_\Lambda(X)-\mathcal H(d_X)
 <60989+\frac{6039}{8}
 =\frac{493951}{8}
 <61744.
}
\tag{L-92933.4}
\]

In particular this is `O(1)=o(log^2 X)`.

## 4. Why the bound is immune to the rough-lift separator

The root and child terms in (L-92933.3) descend from the native source-tree identity of `L-92931`. The complete rough lift `Theta_(P,X)` never appears. `R-92930` is retained as a fail-closed mutation: substituting the rough lift changes the `q=2` native coordinate and invalidates (L-92931.6).

## 5. Boundary

```text
root native cost                             <60989
actual terminal-child cost                   <6039/8
complete native deficit                      <61744
rough-lift substitution                      rejected at q=2
recursive tree                               absent
benchmark bridge                             absent
Riemann Hypothesis                           unproved
```
