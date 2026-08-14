# L-91680 — Target-proportional causal projection is an exact source-faithful producer

Claim ID: `L-91680`  
Status: **PROVED EXACT ABSTRACT PRODUCER / DETERMINANT REDUCTION**  
Created: 2026-08-14  
Motivation: PR #456 refutes the branchwise no-upward Hall producer; PR #458 reduces the successor to a joint finite cone  
RH status: **unproved**

## 1. Purpose

The stopped-leaf Hall construction used a prescribed node order to remove the odd source from the even source.  The prefix inequalities required by that construction are false on an infinite family of leaves.  This note gives a different producer which:

```text
uses only the actual even source;
uses every source coefficient at most once;
preserves the signed target exactly;
requires no Hall graph or source ordering;
reduces every physical row/capacity condition to one full determinant;
exposes the exact native-score debt instead of hiding it.
```

It is an exact theorem, but the determinant and accumulated-debt inequalities for the actual `P_61` packet remain separate arithmetic obligations.

## 2. Typed positive source datum

Let `D` be a finite or countable labelled source space.  Let `E` and `O` be finite positive measures on `D`, representing the even and odd parts of one signed causal packet.

For each source point, retain one strictly positive target kernel `T`, one nonnegative declared-score kernel `S`, and a family of nonnegative physical kernels

\[
 R^\alpha,
 \qquad \alpha\in\mathcal A.
\]

The family may contain simultaneously:

```text
literal component-row coordinates;
ordinary physical responses;
radix-four detail responses;
shared endpoint-port usages;
any other additive nonnegative current coordinate.
```

Write

\[
 E_T=\int T\,dE,
 \qquad O_T=\int T\,dO,
\]

and similarly `E_S,O_S,E_\alpha,O_\alpha`.  Assume

\[
 0\le O_T<E_T.
 \tag{L-91680.1}
\]

The degenerate zero-target case is removed before applying the theorem.

## 3. Canonical target-proportional residual

Put

\[
 \theta=\frac{O_T}{E_T}\in[0,1)
 \tag{L-91680.2}
\]

and define the positive residual source

\[
 \boxed{
 \nu=(1-\theta)E.
 }
 \tag{L-91680.3}
\]

This is a literal submeasure of the original even source.  It introduces no synthetic source, copied atom, or post-hoc provenance label.

Its target is exactly the signed target:

\[
\begin{aligned}
 T(\nu)
 &=(1-\theta)E_T\\
 &=E_T-O_T.
\end{aligned}
 \tag{L-91680.4}
\]

Thus target equality is automatic, with no matching problem.

## 4. Exact physical determinant

For one physical coordinate `alpha`, the signed arithmetic value is

\[
 E_\alpha-O_\alpha,
\]

whereas the residual source uses

\[
 R^\alpha(\nu)=(1-\theta)E_\alpha.
\]

The unused row/capacity bonus is therefore

\[
\begin{aligned}
 B_\alpha
 &:=(E_\alpha-O_\alpha)-R^\alpha(\nu)\\
 &=\theta E_\alpha-O_\alpha\\
 &=\frac{O_TE_\alpha-E_TO_\alpha}{E_T}.
\end{aligned}
 \tag{L-91680.5}
\]

Consequently

\[
 \boxed{
 B_\alpha\ge0
 \iff
 O_TE_\alpha-E_TO_\alpha\ge0.
 }
 \tag{L-91680.6}
\]

If the determinant is nonnegative for every `alpha`, then

\[
 \boxed{
 E_\alpha-O_\alpha
 =R^\alpha(\nu)+B_\alpha,
 \qquad B_\alpha\ge0,
 }
 \tag{L-91680.7}
\]

simultaneously in every literal row and physical capacity coordinate.

This is the exact row-bonus orientation required by the joint cone of `L-91670` on PR #458.  It is a full-packet determinant, not a family of branchwise Hall-prefix inequalities.

## 5. Exact score comparison and debt

The residual declared score satisfies

\[
\begin{aligned}
 S(\nu)-(E_S-O_S)
 &=(1-\theta)E_S-E_S+O_S\\
 &=O_S-\theta E_S\\
 &=\frac{E_TO_S-O_TE_S}{E_T}.
\end{aligned}
 \tag{L-91680.8}
\]

Therefore score superordination holds exactly when

\[
 \boxed{
 E_TO_S-O_TE_S\ge0.
 }
 \tag{L-91680.9}
\]

Without that sign, the exact score debt is

\[
 \boxed{
 \mathfrak d_S(E,O)
 =\frac{[O_TE_S-E_TO_S]_+}{E_T}.
 }
 \tag{L-91680.10}
\]

There is no hidden constant and no appeal to target mass as a coefficient of an unrelated signed deficit.

The literal entropy of the nonnegative bonuses in (L-91680.7) may only improve the final physical score.  Equation (L-91680.10) is therefore a conservative declared-score debt.

## 6. Source-disjoint summation

Let `(E_v,O_v)` be a finite or countable family of mutually singular labelled stopped leaves.  Apply (L-91680.3) separately and put

\[
 \nu_{\rm glob}=\bigoplus_v\nu_v.
\]

Every original source atom has one owner.  Target equalities and physical decompositions add exactly:

\[
 T(\nu_{\rm glob})
 =\sum_v(E_{v,T}-O_{v,T}),
 \tag{L-91680.11}
\]

\[
 \sum_v(E_{v,\alpha}-O_{v,\alpha})
 =R^\alpha(\nu_{\rm glob})+
  \sum_vB_{v,\alpha}.
 \tag{L-91680.12}
\]

All right-hand terms are nonnegative under the determinant inequalities.  The total declared-score debt is bounded by the literal sum

\[
 \boxed{
 \mathfrak D_S
 \le\sum_v\mathfrak d_S(E_v,O_v).
 }
 \tag{L-91680.13}
\]

Thus a uniform proof requires an aggregate debt estimate, not merely a pointwise statement that each leaf debt is finite.

## 7. Relation to the post-Hall joint cone

The construction gives an explicit candidate vector in the joint finite cone of PR #458:

```text
allowed templates: the original even source atoms;
coefficient on each atom: the common factor 1-O_T/E_T;
target equality: exact;
row/capacity inequalities: full target-normalized determinants;
score inequality: exact determinant, or explicit debt (L-91680.10).
```

It therefore replaces the existential search for arbitrary template coefficients by one canonical source-faithful ray.  It does not prove that the actual determinants have the required signs.

## 8. Comparison with the Lorenz producer

The score-Lorenz producer of `L-91358` removes the leftmost even score submeasure and requires a monotone row-per-score profile.  The present producer is different:

```text
Lorenz projection:       score-normalized, order-sensitive;
target-proportional ray: target-normalized, order-free.
```

Either can close a leaf.  The target-proportional theorem is especially useful after the Hall refutation because it needs no global node order; its cost is the exact determinant/debt system above.

## 9. Firewall

The following inferences are invalid:

```text
branchwise Hall failure => target-proportional determinant failure;
separate row determinants => simultaneous source feasibility without one source ray;
pointwise finite score debt => bounded all-generation debt;
positive canonical P_61 row => current-only capacity ownership.
```

The theorem uses one source ray simultaneously in every coordinate and hence avoids the first three errors.  Rough-child ownership remains governed by the exact stopping-line partition.

## 10. Exact boundary

```text
target-proportional residual source              EXACT
one-use source provenance                         EXACT
signed target preservation                        EXACT
physical row/capacity determinant formula         EXACT
native-score determinant/debt formula             EXACT
source-disjoint global summation                  EXACT
actual P_61 full determinants                     OPEN / ARITHMETIC
aggregate score-debt bound                        OPEN / ARITHMETIC
post-Hall joint producer                          REDUCED TO THOSE GATES
Riemann Hypothesis                                UNPROVED
```
