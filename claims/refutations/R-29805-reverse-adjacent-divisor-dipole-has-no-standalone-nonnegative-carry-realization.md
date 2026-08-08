# R-29805 — A reverse adjacent divisor dipole has no standalone nonnegative carry realization

Claim ID: `R-29805`  
Title: The right-to-left source orientation in `L-29810` has a negative carry coordinate and therefore cannot be represented by any standalone nonnegative split flow  
Status: **EXACT LOCAL NO-GO THEOREM**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: atomized carry columns are nonnegative  
Scope: rules out only a standalone positive gadget; signed source-complete recombination remains open

## 1. Divisor-source coordinate

Let

\[
 d_n(q)=\mathbf1_{q\mid n},
 \qquad q\ge2.
\tag{R-29805.1}
\]

The right-to-left adjacent source orientation required by `L-29810` is

\[
 \boxed{d_{n+1}-d_n.}
\tag{R-29805.2}
\]

At the carry column `q=n`,

\[
 d_{n+1}(n)-d_n(n)=0-1=-1.
\tag{R-29805.3}
\]

## 2. Nonnegative carry flows cannot produce it

For every split edge `[N,j]`, the atomized carry column is

\[
 \chi_{N,j}(q)
 =\left\lfloor{N\over q}\right\rfloor
  -\left\lfloor{j\over q}\right\rfloor
  -\left\lfloor{N-j\over q}\right\rfloor
 \in\{0,1\}.
\tag{R-29805.4}
\]

Consequently every nonnegative split flow has nonnegative load in every carry
column.

Equation (R-29805.3) proves:

\[
 \boxed{
 d_{n+1}-d_n
 \text{ is not the carry-load vector of any nonnegative split flow}.}
\tag{R-29805.5}
\]

The conclusion is independent of the permitted parent size, balance reserve,
or number of edges. The negative `q=n` coordinate is an exact Farkas witness.

## 3. Relation to the Pascal sibling identity

The familiar sibling switch gives

\[
 \chi_{2n,n-1}-\chi_{2n,n}=d_n-d_{n+1}.
\tag{R-29805.6}
\]

This is the **forward** orientation. Its reverse is the difference

\[
 \chi_{2n,n}-\chi_{2n,n-1}=d_{n+1}-d_n,
\]

which necessarily uses a negative coefficient on one of the two edges when
viewed as a standalone change.

Thus the right-to-left half of the Hausdorff matching cannot be closed by
inventing a second local nonnegative central/sibling gadget.

## 4. Correct remaining theorem

A valid continuation must retain the reverse orientations until they are
combined with the complete positive source family. It must then prove either:

1. the negative `d_n` coordinates are paid by explicitly identified positive
   columns from neighboring jets/collars; or
2. the signed reverse switches have total capacity debt bounded by a
   polylogarithm after complete common-destination recombination.

The sparse adjacent-tree commutator

\[
 E_n=T_{n+1}-T_n,
 \qquad
 \partial E_n=e_{n+1}-e_n-e_1,
\]

from PR #272 is the canonical signed realization. Its negative capacity must be
charged in the same metric as the lower-flow odd leakage.

## 5. Disposition

```text
forward adjacent Pascal switch                    NONNEGATIVE / RETAINED
reverse adjacent dipole as standalone flow         IMPOSSIBLE
Hausdorff two-sided coefficient matching           RETAINED (`L-29810`)
source-complete signed reverse-debt estimate        OPEN
DCD / Cycle Debt                                    OPEN
Riemann Hypothesis                                  UNPROVEN
```
