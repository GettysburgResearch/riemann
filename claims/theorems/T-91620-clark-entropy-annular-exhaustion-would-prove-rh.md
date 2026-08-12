# T-91620 — Clark-entropy annular exhaustion would prove RH

Claim ID: `T-91620`  
Status: **FULL CONDITIONAL RH PROPOSAL / SOURCE-ORDERED ENTROPY EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91620/L-91621`; `R-91620`; `T-91520`  
RH status: **unproved**

## 1. Fixed node and dyadic annuli

Fix

\[
 \eta=1,
 \qquad
 a_j=2^{-j-1}.
\]

For each dyadic annulus, the model crossed-zero output has logarithmic mass

\[
 \Lambda_j^{\rm ann}
 =-2\log|C_{a_j,a_{j-1}}(1)|
 \ge0.
\]

By `L-91520`,

\[
 \Lambda_{a_J}(1)
 =\sum_{j=1}^J\Lambda_j^{\rm ann},
\]

and RH is equivalent to the vanishing of every summand.

## 2. Clark-Entropy Annular Exhaustion (`CEAE_j`)

For each annulus construct explicitly a source-ordered multiplicative
factorization whose logarithmic ledger is

\[
 \boxed{
 \mathscr L_j^{\rm arith}
 =\mathscr L_j^{\rm crit}
  +\mathscr L_j^{\rm st}
  +\Lambda_j^{\rm ann}
  +\mathscr L_j^{\rm aux}.
 }
\]

The construction must satisfy:

1. `L_arith` is computed from declared positive arithmetic sources: the
   dyadic generalized-Jordan innovation, completed gamma/pole factor, one-Green
   vector, returned state, and any compact bridge used before norms.
2. `L_crit` and `L_st` are the logarithmic losses of the actual critical and
   deterministic stable model outputs at the same Cauchy node.
3. `Lambda_ann` is the canonical Blaschke log mass, not an arbitrary
   nonnegative scalar.
4. `L_aux>=0` is the log loss of a declared positive environment.
5. All quantities arise from one common factorization, so `R-91620` is not
   triggered.

Then prove exact exhaustion

\[
 \boxed{
 \mathscr L_j^{\rm arith}
 =\mathscr L_j^{\rm crit}
  +\mathscr L_j^{\rm st}.
 }
\]

It follows that

\[
 \Lambda_j^{\rm ann}=0,
 \qquad
 \mathscr L_j^{\rm aux}=0.
\]

## 3. Quantitative variant

A cofinal family of source-identified factorizations with error

\[
 0\le
 \mathscr L_j^{\rm arith}
 -\mathscr L_j^{\rm crit}
 -\mathscr L_j^{\rm st}
 \le\varepsilon_{j,n},
 \qquad
 \varepsilon_{j,n}\to0,
\]

also forces

\[
 \Lambda_j^{\rm ann}=0
\]

by `L-91621`.

Before the limit, the same theorem gives explicit finite depth-height zero
exclusions from the moat

\[
 \frac{4\eta\delta}
 {\left(\eta+\frac12\right)^2+Y^2}.
\]

## 4. Completion to RH

If `CEAE_j` holds for every `j`, then every dyadic annular factor is constant.
Hence there are no zeros in

\[
 \Re s>\frac12+a_J
\]

for any `J`.  Letting `J` tend to infinity and using functional-equation
symmetry proves RH.

## 5. Relation to the prime logarithmic route

Sibling `L-91610` proves that the safe prime Euler cascade has one additive
positive-real Clark generator.  Its local entropy losses are exact
resolvent-averaged Julia details.

Thus `CEAE` asks for a common factorization identifying:

```text
arithmetic Clark entropy production
    with
critical + stable entropy production
    plus
annular crossed-zero entropy and auxiliary entropy.
```

This is a more natural coordinate match than comparing Hilbert norms whose
multiplicative returned-state factors differ from generation to generation.

## 6. Exact boundary

```text
annular Clark entropy                         EXACT
quantitative zero moat                        EXACT
source provenance from scalar totals          NOT AUTOMATIC
CEAE source-ordered exact/cofinal exhaustion  OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVED
```
