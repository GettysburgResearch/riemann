# Independent source-normalization review of the paid triangle

**Reviewer:** the coherent-identity agent. **Verdict:** pass for the
specified common-shared-list, list-diagonal, rooted raw three-edge
class. The continuous theorem is an exact counting and normalization
result. The discrete theorem is a valid deduction conditional on the
explicitly imported source estimate (A.5). Neither theorem controls
the full HLC operator or the native inverse moment.

## 1. Reviewed objects and replay

| Object | SHA256 | Git blob |
|---|---|---|
| `CLOSED_TRIANGLE_WEIGHT.md` | `169112b8b41ede59ba23009e5b23d06184e19c03cad209d40940edf1568f7e37` | `999510900504d8ee0e3e318dc79a856f29e28bd4` |
| `check_closed_triangle_weight.py` | `3aed0d03eda009fbe93b2f17de320c89d7ce94b93f5487c843114d9e8d6a6d1b` | `9467a1a1766e945e43a66bfe9c3fcc61c39a0840` |

I read the complete note and checker and independently replayed the
checker under `python -O`. It passed. I separately consulted the
source PDF, SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`,
at p. 7 for V_i, pp. 15--16 for eta and psi_1, pp. 17--18 for
the original state measure, symmetrizer and raw kernel, pp. 22--24
for root coordinates, and pp. 47--51 for the exact statement and
final projective-line consequence of Lemma A.1. The source is
[Lü--Wang--Wu, arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242).

The scalar multiplicity and weighted gcd theorem came from my
`THREE_EDGE_INTEGER_BRIDGE.md`, so this is **not** an independent
review of that theorem's authorship. The HLC and middle-joint agents
review that scalar theorem separately. This review independently
checks the HLC author's source transfer, its original normalizers,
and its finite-residue consumer.

## 2. Original state and edge factors

The state measure is the constant
\(\sigma=\prod_iV_i^{-(J+1)}\), and an unordered complete
list has \(n_{\rm ord}=((J+1)!)^K\) orderings. The function one
on lists at the root has coordinate \(\sqrt{n_{\rm ord}\sigma}\)
in the corresponding orthonormal permutation-invariant basis.
For a contribution returning to the same unordered root lists,
the two endpoint coordinates multiply to
\(n_{\rm ord}\sigma\). Returning just the ordered trace would
give a different factor, and the note correctly avoids it.

For a prescribed legal unshared-prime replacement, the compatible
fraction of orderings is \((J+1)^{-K}\). Together with the literal
T_1 factor \(\prod_iV_i^{-1}\), three edges therefore give the
prefactor

\[
 ((J+1)!)^K(J+1)^{-3K}\prod_iV_i^{-(J+4)}.
\]

I also checked this directly in ordered states: the endpoint
symmetrizers act as the identity on the root vector, while the
two interior symmetrizers contribute their actual orbit averages.
For one group the resulting multiplicity is
\((J!)^3/((J+1)!)^2\), exactly the expression above after
multiplying by the original state and edge measures.

The chronological products are Db,Da,Dc,Db. The actual old-minus-new
determinants are \(D(b-a),D(a-c),D(c-b)\), and their sum is zero.
The scalar bridge note now displays this same tuple. Either cyclic
orientation gives the same positive gcd ratio needed by the bound.

## 3. One prime-line draw, not one draw per edge

A shared prime divides all three determinants. Primitive vertices
therefore have the same projective line modulo that prime, so its
active constraints are consistent and cost exactly 1/(p+1), once.
Each unshared product is active at one of the three distinct stages;
the returning product b is active at the identical initial and final
vertex and also costs only one line draw.

The original transition rules force a_i,b_i,c_i to be pairwise
distinct within each group. The groups themselves are disjoint.
Thus D,a,b,c are squarefree and pairwise coprime. Reducing the
appropriate determinant modulo an unshared prime shows that its
forced line is different at every inactive vertex. Its inactive
damping is therefore one. Other damping and good-state factors
are bounded by one and can be deleted in an absolute upper bound.

This proves precisely the active-union factor

\[
                \prod_{p\mid Dabc}(p+1)^{-1}\le(Dabc)^{-1}.
\]

The note obtains this weight on the actual legal prime labels before
enlarging to arbitrary integer products. That order is essential:
different integers can share prime factors, and then 1/(abc) would
count some original line probabilities more than once.

The raw kernel contributes d_0/D, with D in [d_0,2d_0); its
three factors are at most one. There is no extra 1/Y in the kernel.
The source eta is supported on [1,4], and psi_1 equals one on
[-4,4]. Hence the three raw differences lie inside the constant
part of psi_1 and the eta factors multiply to
\(\eta(a/Y)^2\eta(b/Y)^2\eta(c/Y)^2\), bounded by its
sixth supremum power. This checks the exact source attachment of
the scalar weighted theorem.

## 4. Multiplicity and shared-list cancellation

The closed congruence is h=1 modulo
\(q=|j_0|/\gcd(|j_0|,|j_2|)\). Integrating its **count**
over the global root, R=-2r, gives

\[
 \frac{255}{16}\,
        \frac{\gcd(|b-a|,|c-b|)}{|b-a|}.
\]

Using the probability of a union instead would lose candidate
multiplicity. The note retains it. Primitive and parity restrictions
are imposed before applying prime-line probabilities; the subsequent
integer count only enlarges that already weighted collection.

For fixed unshared products, the sum over unordered shared sets is
at most \(\prod_iV_i^J/J!\), because the source definition is
exactly \(V_i=\sum_{p\in\mathcal P_i}1/p\). Multiplying this
by the original orbit/edge prefactor gives

\[
                         (J+1)^{-2K}\prod_iV_i^{-4}.
\]

No returning-prime factor has been redrawn or canceled a second
time. Unique factorization and disjoint prime groups also mean
that a product a determines its selected prime in every group;
the enlargement to the numerical a,b,c sum introduces no omitted
factorization multiplicity.

The scalar gcd theorem therefore proves the continuous bound

\[
 T_{\rm tri}(s,t_0)
 \le765\|\eta\|_\infty^6(J+1)^{-2K}
       \left(\prod_iV_i^{-4}\right)
       \frac{(1+\log(3Y))^2}{Y}.
\]

Its first-position window and count are uniform in the other real
root coordinates. Integrating those coordinates over their full
ranges costs at most 15, with the separate source density
1/(3 zeta(2)). This is an actual paid restricted path family in the
continuous root-and-lines model.

## 5. Discrete-root transfer

The note states source (A.5) explicitly and uses it as an external
premise. I verified that its main term and discrepancy are copied
correctly: after prescribing one projective line at every prime of
the odd squarefree S, the normalized error is
\(O(S^5\min(d_0YM,N)^{-1/100})\). Its statement is uniform in
the three root intervals and in S. The note does not substitute the
paper's even-moment proposition for this odd three-edge count.

For fixed J,K and the stated polynomial bands, the used modulus
satisfies \(S=Dabc\le x^{(J+3)\beta}\). The number of label
families is at most \(x^{(J+3)\beta}\). The first window bounds
the possible h by \(O(x^{(J+1)\beta})\); each h determines at
most one second integer vertex. Every primitive retained candidate
has one prescribed line at each prime, so no extra sum over line
choices is needed.

After bounding the raw kernels by their fixed suprema and deleting
goodness and later position restrictions, the first-position event
for each candidate is one literal interval in r. The other root
coordinates use full rectangles. Thus (A.5) applies directly,
without a hidden boundary approximation. The proof of the continuous
bound applies to these enlarged main terms as well.

The total error exponent is consequently

\[
 (J+3)\beta+(J+1)\beta+5(J+3)\beta-\delta/100
                 =(7J+19)\beta-\delta/100.
\]

There is correctly no factor 1/(Dabc) attached to that discrepancy.
The lower bounds on V_i and fixed J,K keep the remaining original
state factors bounded. A nonempty product family has
\(Y\ge x^\alpha/4\), so the main bound is
\(O(x^{-\alpha+\epsilon})\).

The numerical example also checks exactly: for J=K=1,
\(\delta=1/4\), \(\alpha=1/80000\),
\(\beta=1/40000\), the discrepancy exponent is
\(-37/20000\). This gives the claimed restricted arithmetic
triangle bound conditional on source (A.5) and the stated band/V_i
hypotheses. It is not a verification of the paper's full proof or of
a polynomial redesign of all its other estimates.

## 6. Checker scope and outstanding work

The optimized replay passed 14,049 literal ordered triangle paths,
12 ordered/quotient normalization checks, 15 factorial cancellations,
720 shared-list exclusion sums, 3,050 direct prime-line averages,
560 primitive retained triangle paths, 24 complete-label and exact
multiplicity tests, 21 discrete-root budgets, the explicit polynomial
example, and six negative controls.

The principal remaining exclusions are substantive: two-edge
backtracks, changing-shared-list triangles, other return schedules,
the centered comparison kernels, arbitrary surrounding history and
the native inverse coefficient transfer. The note states these
boundaries. The restricted positive result and its conditional
arithmetic version are approved at precisely that scope.
