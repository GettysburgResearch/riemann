# L-29815 — Scaled Pascal sibling intertwiner: withdrawn after a noncoprime-chain counterexample

Claim ID: `L-29815`  
Former title: The scaled Pascal sibling intertwines the common arithmetic destination  
Status: **WITHDRAWN / FALSE AS STATED**  
Authoring agent: `gpt56-02-r`  
Created and corrected: 2026-08-08  
Scope: exact disposition of an attempted source-to-carry tensorization; RH remains unproved

## 1. Former claim

The attempted lemma asserted that, for

\[
 c_{k,m}=[4km,2km],
 \qquad
 s_{k,m}=[4km,(2k-1)m],
\]

one had

\[
 \chi_{s_{k,m}}(d)-\chi_{c_{k,m}}(d)
 =\mathbf1_{d\mid2km}-\mathbf1_{d\mid(2k+1)m}
\tag{L-29815.old}
\]

for every carry base `d`.

This is false when the common arithmetic destination `m` is not coprime to the
relevant residue chain.

## 2. Exact counterexample

Take

\[
 k=1,
 \qquad m=2,
 \qquad d=3.
\]

Then

\[
 c_{1,2}=[8,4],
 \qquad
 s_{1,2}=[8,2].
\]

Their carry values are

\[
 \chi_{8,2}(3)
 =\left\lfloor{8\over3}\right\rfloor
  -\left\lfloor{2\over3}\right\rfloor
  -\left\lfloor{6\over3}\right\rfloor
 =0,
\]

\[
 \chi_{8,4}(3)
 =\left\lfloor{8\over3}\right\rfloor
  -2\left\lfloor{4\over3}\right\rfloor
 =0.
\]

Thus the left side of (L-29815.old) is zero.  The proposed divisor dipole is

\[
 \mathbf1_{3\mid4}-\mathbf1_{3\mid6}=0-1=-1.
\]

Hence

\[
 \boxed{0\ne-1.}
\tag{L-29815.1}
\]

This is a hypothesis-matching noncoprime-chain counterexample.

## 3. Why unscaled interpolation does not tensorize

For `m=1`, the familiar sibling identity

\[
 \chi_{4k,2k-1}(d)-\chi_{4k,2k}(d)
 =\mathbf1_{d\mid2k}-\mathbf1_{d\mid2k+1}
\]

is valid. Multiplying every parent and child by `m` changes the residue classes
modulo `d`; it is not a tensor operation on carry columns.

Therefore a coefficient-space pair at parity levels `2k,2k+1` cannot be bound
to the actual arithmetic destinations `2km,(2k+1)m` by simply scaling the
Pascal sibling.

The noncoprime residue chains must be emitted and recombined explicitly.

## 4. Consequences

The following conclusions from the former version are withdrawn:

- the asserted exact common-destination source-to-carry map;
- the destination-aware one-edge reverse-debt bound;
- the arithmetic source budget `B_M^ar` derived from that map;
- any claim that `L-29812` already supplies an exact DCD flow after multiplying
  by a common arithmetic destination.

The formal-index local results remain at their declared scopes:

- `L-29809` scalar interleaved Euler positivity;
- `L-29810` abstract Hausdorff matching;
- `L-29812` mode-separated formal source matching;
- `L-29813/L-29814` formal adjacent-tree capacity estimates.

They do not by themselves identify the actual carry-source image.

## 5. Correct remaining theorem

A valid source-binding theorem must retain the actual indices

\[
 2kq-1,
 \qquad
 (2k+1)q,
\]

or an exact duplicate-free expansion of their carry columns.  It must include:

1. every gcd/noncoprime residue chain;
2. the shift `-1` on the even leg;
3. every parity sibling and common destination;
4. a balanced split-flow realization or capacity-debt bound in the actual
   integer node coordinates;
5. the bottom and endpoint collars;
6. exact congruence with PR #272's dyadic commutator ledger.

No such theorem is proved here.

## 6. Disposition

```text
unscaled sibling identity                         RETAINED
scaled tensorized sibling identity                 FALSE
formal Hausdorff/parity coefficient matching       RETAINED AT FORMAL SCOPE
actual arithmetic source-to-carry binding          OPEN / RH-BEARING
DCD / Cycle Debt                                    OPEN
Riemann Hypothesis                                  UNPROVEN
```
