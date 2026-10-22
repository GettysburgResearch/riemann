# O-93021 - Fifth-strike proof DAG after the exact OPB separator

Claim ID: `O-93021`  
Status: **RESEARCH DAG / NO RH CLAIM**  
Created: 2026-08-16  
Frozen parent: PR #474 at `4f59985d9e453c1a1966c5476e1bfcaca3ce4b91`

## Executive disposition

The fifth strike tested the two advertised closing interfaces rather than
assuming them.

```text
zero OPB borrowing:
    FALSE at X=40 by an exact directed separator;

generic root-neutral positive fragmentation:
    FALSE at X=6 by an exact Farkas separator;

critical root-completed transverse producer:
    POSITIVE AT X=40 / ALL-SCALE OPEN AND FAIL-CLOSED;

scale-four source positivity:
    CLOSED EXACTLY;

scale-four atomwise physical capacity:
    CLOSED MODULO ONE PRINCIPAL CHANNEL;

aggregate transverse Q4 Gram:
    OPEN;

principal Q4 mean:
    OPEN / RH-BEARING;

Riemann Hypothesis:
    UNPROVED.
```

## Cycle-Debt DAG

```text
one-sided carry-discrepancy LP L-93017
    |
    +-- universal b2 root face R-93021
    |       |
    |       +-- exact rational primal/dual fixture
    |       +-- directed B_40 > 1/200
    |       +-- Mellin numerator 1-2^(-z-1/2)
    |
    +-- minimal bottom completion L-93021
            |
            +-- interior positive cone A_X^circ x = t_tilde
            +-- exact Farkas alternative
            +-- generic root-neutral no-go at X=6
            +-- exact positive critical fixture at X=40
            |
            +-- CRCTP [OPEN COFINALLY]
                    |
                    +-- all negative debt localized at bottom
                    +-- exact root scalar
                    +-- subpower root upper theorem [OPEN]
                    +-- RH consumer
```

The old possible shortcut

```text
high-scale witness -> lower-scale witness
```

is removed. The corrected producer theorem is a positive realization of one
specific root-completed critical target, not a source-free parity projection.

## Q4 DAG

```text
scale-four logarithmic derivative L-93019
    |
    +-- positive reciprocal G4 L-93022
    |       |
    |       +-- g4(n)=4^floor(v2(n)/2)>0
    |       +-- Lambda4>=0
    |       +-- Lambda+=(epsilon+2 delta2)*Lambda4>=0
    |       +-- c_circ=(epsilon-2 delta2)*Lambda+
    |
    +-- source-owned Haar fibres Z_(m,N)
            |
            +-- exact principal scalar kappa_(m,N)
            +-- mean-zero transverse fibre
            +-- atomwise norm <=144m
            |
            +-- aggregate transverse Gram [OPEN]
            +-- principal mean M_circ [OPEN]
            +-- Hardy boundary C_circ=o(N) [PNT / RETAINED]
            +-- Mellin consumer [T-93010/T-93011]
```

The positive source transfer is real, but a one-atom no-go proves that the
principal channel cannot be absorbed into a local source reserve.

## Cross-route synthesis target

The exact type match is now:

\[
\begin{array}{c|c}
\text{Cycle Debt}&\text{Q4}\\ \hline
\text{dyadic root face}&\text{principal endpoint mean}\\
\text{positive transverse carry cone}&
\text{positive-source transverse boundary Gram}
\end{array}
\]

A future cross-route theorem must provide:

1. a positive/capacity-faithful map between the two transverse objects;
2. a separate conservative identity coupling the root and mean principals;
3. the PNT Hardy boundary;
4. the zero-safe Mellin consumer.

It may not duplicate either principal channel into the transverse reserve.

## Review order

1. `R-93021`.
2. `X-93021`.
3. `L-93021`.
4. `L-93022`.
5. `X-93022`.
6. `R-93022`.
7. `L-93023`.
8. this DAG, the report, source lock, and content ledger.
9. prior PR #474 claims in their existing review order.

## Automatic rejection

Reject a claimed continuation upon any:

```text
use of mathfrak B_(2Y)=0;
dropping the b2 root face;
treating root neutrality as sufficient for a positive flow;
using a floating source equality instead of symbolic/directed coverage;
dropping the Hardy boundary term without C_circ=o(N);
calling Lambda+ positivity a bound for M_circ;
absorbing the constant fibre channel into a local reserve;
summing atomwise transverse capacities as though the fibres were orthogonal;
claiming RH from a finite LP trend.
```
