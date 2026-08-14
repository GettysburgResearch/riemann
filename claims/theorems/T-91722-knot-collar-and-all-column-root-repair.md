# T-91722 — Knot-collar refinement plus the all-column reserve repairs the finite root approximation

Claim ID: `T-91722`  
Status: **PROVED CONDITIONAL SUPPLEMENT / FULL FROZEN STACK STILL REQUIRES REVIEW**  
Created: 2026-08-14  
Primary new inputs: `L-91723`, `L-91724`  
Mass input: `L-91694`  
Frozen producer inputs: factor-67 root Hall, first-owner partition, common port, terminal omission and endpoint frame  
RH status: **unproved pending reconstruction**

## 1. Finite root realization clauses

Assume the frozen factor-67 ideal root packet has:

1. a positive source-owned root-Hall decomposition;
2. one current packet and source-disjoint children;
3. mass-weighted recursive target coefficient below `1/8`;
4. one common endpoint measure, quantizer and port;
5. the adjacent mismatch, collar and terminal bounds used by `L-91723`.

`L-91723` gives one source thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

and strict normalized detail reserve

\[
 r_K=\frac1{\sqrt K+130}
\]

in every nonterminal physical column, with bounded score cost.

## 2. Activation-knot approximation

`L-91724` removes an arbitrarily small positive collar around the finite
activation set and replaces the remaining complete typed fibers by a positive
cellwise barycentric refinement.

Choose the collar and mesh schedules so that:

\[
 \text{collar score loss}<X^{-2},
\]

\[
 \text{interpolation score loss}<X^{-2},
\]

and

\[
 10152\|C\|\epsilon_X<\frac{r_K}{2}.
\]

Then every nonterminal detail column retains

\[
 \boxed{
 s_X(q)>
 \frac{\Omega_X(q)}{2(\sqrt K+130)}>0.
 }
\tag{T-91722.1}
\]

Positive radix-four inversion gives ordinary feasibility.

## 3. Ownership and recursive mass

Both operations are performed before the current/child split is forgotten:

```text
discard the activation collar once;
push each retained endpoint mass to at most two same-cell mesh fibers;
apply one common Hall/quantizer/correction packet;
retain source and rough-owner labels;
group recursive children only after the positive sum.
```

Every barycentric pair has nonnegative coefficients summing to one.  The
discarded collar is never assigned to a child.  Therefore the exact
mass-weighted theorem `L-91694` still gives

\[
 \sum_b\alpha_b<\frac18.
\tag{T-91722.2}
\]

## 4. Endpoint deficit

The new knot-collar and interpolation costs are `o(1)`.  The square-root
thinning has score cost below `4290`.  Consequently, on the frozen producer
stack,

\[
 J_\Lambda(X)-\operatorname{Score}(d_X)
 \le4\log X+C_{\rm repaired}+o(1)
 =o(\log^2X).
\tag{T-91722.3}
\]

The exact positive `Y_4` dual identifies this with the native weighted detail
slack.

## 5. Conditional implication

After independent reconstruction of the frozen Hall, first-owner, common-port,
terminal and one-sided endpoint inputs, equations (T-91722.1)--(T-91722.3)
repair both finite-realization issues isolated in review:

```text
small physical columns q<K;
native-relative convergence at activation knots.
```

The resident subcritical consumer and endpoint theorem may then be applied.

This is a conditional proof supplement.  It does not independently certify
the imported stack and does not establish RH in this file.

## 6. Exact boundary

```text
small-column finite realization               repaired / L-91723
activation-knot native-relative refinement     repaired / L-91724
mass-weighted child coefficient <1/8           exact / L-91694
additional approximation score cost            o(1)
full frozen producer stack                      independent review required
SONTR / NRCT                                    conditional proposal
Riemann Hypothesis                              unproved
```
