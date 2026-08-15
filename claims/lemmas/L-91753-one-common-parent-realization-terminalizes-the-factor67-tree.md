# L-91753 — One common-parent realization terminalizes the factor-67 tree

Claim ID: `L-91753`  
Status: **PROVED EXACT ONE-SHOT ASSEMBLY ON THE FROZEN COMMON-PARENT INPUTS**  
Created: 2026-08-15  
Frozen inputs: `L-91377`, `L-91674`, `L-91688`, `L-91723--L-91725`, `L-91750`, `L-91752`  
RH status: **unproved**

## 1. The ideal total row

The full Möbius equality row `c_X` satisfies

\[
 C_{c_X}=w_X,
 \qquad
 \Xi_{c_X}=\Omega_X,
 \qquad
 \mathcal H(c_X)=J_\Lambda(X)
\tag{L-91753.1}
\]

exactly. It need not be coefficientwise nonnegative.

The factor-67 root Hall, row bonus and causal source partition produce a
positive labelled decomposition whose **total component row is still** `c_X`.
All ordinary responses are tested after the positive sum, and radix-four
equality is formed only after the ordinary equalities at `q` and `4q`.

## 2. The decomposition-blind realization

Let `mathfrak F_X` denote the complete common-parent realization:

```text
bottom/top/activation-collar restriction;
positive same-cell refinement;
one square-root thinning;
one global labelled quantizer;
one current-only finite correction and one uncolored port.
```

The frozen decomposition-blind theorem says that `mathfrak F_X` depends on the
total labelled endpoint measure, not on a choice of Hall or rough colour
presentation. Put

\[
 d_X=\mathfrak F_X(c_X).
\tag{L-91753.2}
\]

The positive source decomposition is retained inside the construction, so
`d_X` is a finite coefficientwise nonnegative physical row. PR #479 proves

\[
 C_{d_X}(q)\le w_X(q),
 \qquad
 \Xi_{d_X}(q)\le\Omega_X(q)
 \qquad(q\ge2).
\tag{L-91753.3}
\]

## 3. Why no hereditary child theorem is needed

The labelled equality of `L-91750` decomposes `d_X` internally as current
colours plus source-owned child colours. These are **components of the one final
row** (L-91753.2). They are not replaced by independently re-realized packets.

Consequently:

```text
no second Hall operation is applied;
no child is quantized a second time;
no collar, omission, finite correction or port is repeated;
no packet-capacity normalization is needed to insert a replacement row;
no recursive deficit is added.
```

The causal coefficient bound below `1/8` remains an exact provenance and
source-nonduplication certificate, but the endpoint score estimate is obtained
from the total physical row directly.

This is a distinct **assembly implementation** of the same factor-67 arithmetic
method. It bypasses, rather than assumes, the hereditary-reset gate identified
in PR #482.

## 4. Direct native deficit

By the exact native dual,

\[
 \boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,\Omega_X-\Xi(d_X)\rangle.
 }
\tag{L-91753.4}
\]

`L-91752` pairs every operation in `mathfrak F_X` directly against `Y_4` and
proves

\[
 \boxed{
 0\le J_\Lambda(X)-\mathcal H(d_X)
 \le A_0+4290\log(2X).
 }
\tag{L-91753.5}
\]

No equality-score recurrence, child-deficit recurrence, or estimate of
`J_Lambda-4sqrt(X)` occurs.

## 5. Relation to the recursive compiler

`L-91750/L-91751` still supply an exact recursive packet interpretation if a
reviewer wishes to reconstruct one. The one-shot theorem is stronger for the
endpoint conclusion because the already feasible common-parent row is never
discarded and reassembled.

Thus the live PR #481 material supports:

```text
one arithmetic method;
two downstream assembly implementations;
preferred implementation: one-shot total row;
optional implementation: recursive positive-packet reset.
```

## 6. Boundary

```text
full Möbius native row normalization             EXACT / L-91377
positive labelled root decomposition             FROZEN FACTOR-67 INPUT
common-parent realization decomposition-blind    EXACT ON FROZEN INPUT
all physical columns feasible                    PR #479 / FROZEN
child colours retained inside final row           EXACT
hereditary reset needed for endpoint bound        NO
native deficit direct O(log X)                    L-91752
Riemann Hypothesis                                UNPROVEN
```
