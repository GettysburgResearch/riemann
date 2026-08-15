# L-91783 — Common-source Fubini preserves every native coordinate and one owner

Claim ID: `L-91783`  
Status: **PROVED EXACT FORMAL COMPOSITION THEOREM**  
Created: 2026-08-15  
Depends on: `L-91720`, `L-91671`, linear native response maps  
RH status: **unproved**

Let `E` be the labelled set of root source occurrences. For each `e in E`, let
`v_e` be one vector containing, in a single normalization,

```text
target; literal score; every component row;
every ordinary response; every boundary reserve;
one shared port coordinate.
```

Radix-four detail is not an independent branchwise observation: for the common
ordinary sum define

\[
 \Xi(q)=\Gamma(q)-2\Gamma(4q).
\tag{L-91783.1}
\]

Suppose the source occurrences are partitioned into disjoint leaves `E_v`, and
on each leaf one common coefficient `u_e in [0,1]` is used simultaneously in
every coordinate. Suppose also that every root correction has one declared
owner and that child, stop, correction and unused coefficients sum to the
original coefficient of each occurrence.

Then finite Tonelli/Fubini and linearity give one root identity

\[
 \sum_{e\in E}w_ev_e
 =D_{\rm current}+D_{\rm child}+D_{\rm stop}
  +D_{\rm correction}+R,
 \qquad R\ge0,
\tag{L-91783.2}
\]

in all listed coordinates. Applying (L-91783.1) only after the common ordinary
sum gives the same identity in every radix-four coordinate. In particular:

1. no source occurrence can be used by two leaves;
2. no row can select coefficients different from target or score;
3. the finite-Euler rough reservoir cannot be spent both as current and child;
4. a collar, mismatch, omission, taper, or port may be charged only by its one
   declared root owner.

This theorem closes the formal source-Fubini interchange. It does not export
the live finite source/channel coefficients or prove their local native
feasibility. That numerical/algebraic allocation remains the live ANRL gate.
