# Independent review of the oscillating-overlap theorem

**Reviewer:** amplification subagent, independent of the author of the reviewed note.

**Reviewed object:** /workspace/scratch/5b23d9b20a3a/attack2_moment.md, SHA-256

271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397

The initial reading was at hash 6841efbefe80dd07f10fce7ae51a3eec9d861741b0a349a2d2bdd5d5907a8f74. After a concurrent author update, the reviewer reread Sections 2–5 at the hash above and confirmed that the reviewed mathematical statements and proofs remained as certified below.

**Review scope:** Sections 2–5, including the exact row decompositions, all nonunit zeros, designated-incidence and ordinary-gcd eligibility, ideal counts at bounded scales, the tail norm summation, and the equal-scale and rectangular cutoff algebra. Section 1's stated squarefree large sieves and the PR 913 all-row sextic bound are treated as the explicit analytic premises for this deduction. This review does not independently prove those external theorems. It does not certify the separately conditional Möbius-specific extension in Section 7.

**Verdict:** the arguments in Sections 2–5 are valid deductions from those stated premises. The fourth-moment gain is strict in the claimed range. No correction to the reviewed sections is required.

## 1. Cubic all-row theorem

The decomposition

\[
u=\varepsilon v^3ab^2
\]

is unique after a multiplicative choice of ideal generators and a unit representative. At each prime, write its valuation as \(3e+r\), \(r=0,1,2\). The ideals \(a,b\) are squarefree and coprime. The ideal \(v\) may intersect either one; the proof correctly permits this.

The local identity is exact even at nonunits:

\[
\chi_n(u)^2
=\chi_n(\varepsilon)^2
1_{(n,v)=1}\chi_n(a)^2\chi_n(b)^4.
\]

If a column prime meets \(v\), the left side and the displayed mask are zero. If it meets a remaining squarefree component, the corresponding character factor vanishes. A cubic power is therefore used as a mask, rather than as a constant-one character.

Separating the squarefree bad-prime parts of \(a,b\) requires only finitely many patterns. The unit and all frozen factors enter row-independent coefficients before the squarefree sieve is applied. In particular, the norm constant does not depend on the particular frozen ideal \(v\).

On a dyadic block put

\[
P=V^3AB^2,\qquad F=VAB,\qquad M=\max(A,B).
\]

There are \(O(F/M)\) frozen pairs. The coefficient norm for each pair is at most the original coefficient norm. The stated squarefree cubic sieve thus gives

\[
\left(F+\frac{FL}{M}
       +\frac{FL^{2/3}}{M^{1/3}}\right)\sum_n|z_n|^2
\]

up to the prescribed small power. Coprimality between the varying row and the frozen squarefree component is removed only from a nonnegative exterior square sum, which is legitimate.

I recomputed the optimization identities:

\[
\frac{(F/M)^3}{P}=\frac{A^2B}{M^3}\le1,
\qquad
\frac{(F/M^{1/3})^3}{P^2}
=\frac{A}{MV^3B}\le1.
\]

Also \(F\le P\). They hold for every \(V,A,B\ge1\), with no hidden ordering assumption except \(M=\max(A,B)\). Since \(P\ll_SH\), the resulting bracket is exactly

\[
H+H^{1/3}L+(HL)^{2/3}.
\]

Summing the \(O((1+\log H)^3)\) blocks and the finite labels only uses the allowed arbitrarily small loss.

The proof is valid at bounded scales: a nonempty dyadic component has lower endpoint at least one, and components of size one are allowed. The literal cube rows are retained.

## 2. Quadratic and principal orders

For \(m\equiv3\pmod6\), the decomposition

\[
u=\varepsilon v^2a
\]

has the same exact-mask property. With \(v\) frozen, the varying row length is \(O(H/Nv^2)\). The quadratic squarefree sieve gives two contributions whose sums are

\[
H\sum_v(Nv)^{-2}\ll H,
\qquad
L\,\#\{v:Nv\ll H^{1/2}\}\ll LH^{1/2}.
\]

The first series converges by the elementary ideal count. No coprimality of \(v\) and \(a\) is required. This proves the advertised all-row quadratic bracket.

For \(6\mid m\), the equality

\[
\chi_n(u)^m=1_{(n,u)=1}
\]

is exact because \(m\) is positive. Cauchy–Schwarz with \(O(L)\) columns and \(O(H)\) rows gives \(HL\sum|z_n|^2\). The note correctly makes no oscillatory claim at order one.

## 3. Exact designated-incidence eligibility

Fix \(I\), \(|I|=m\ge2\), and let \(c=q_I\). Write \(n_i=ca_i\) for \(i\in I\), freezing these residual \(a_i\) and every \(n_j\) with \(j\notin I\).

The note's conditions are necessary and sufficient:

1. Every frozen ideal is squarefree and prime to the fixed bad set.
2. The varying \(c\) is squarefree, prime to that set, and coprime to every frozen ideal.
3. Every prime common to all \(a_i\), \(i\in I\), divides at least one of the frozen outside factors.

For sufficiency, primes of \(c\) occur exactly in the factors indexed by \(I\). Condition 3 prevents an additional prime with precisely that incidence pattern. Conversely, any tuple whose exact incidence ideal is \(c\) has these properties. There is no multiple counting. All eligibility conditions are independent of the row.

For an ordinary gcd of a subset, replace condition 3 by \(\gcd(a_i:i\in I)=1\), and require \(c\) to be coprime only to the residual \(a_i\). An outside factor may meet \(c\). This causes no problem: that outside factor has already been frozen, so its entire row dependence is a fixed bounded multiplier. The product identity is applied only within each original squarefree \(n_i=ca_i\).

This last distinction is important. The note states it correctly, and does not incorrectly use the exact-incidence coprimality with all outside factors for an ordinary subset gcd.

## 4. Frozen-tuple count and the master tail bound

On \(L\le Nc<2L\), support gives

\[
Na_i\le\beta_iD_i/L\quad(i\in I),\qquad
Nn_j\le\beta_jD_j\quad(j\notin I).
\]

The ideal count \(J(t)\ll_Kt\) holds for every positive \(t\): it is zero below one. Thus

\[
\#\{\text{frozen tuples}\}
\ll_{\mathbf W,k}\mathcal P L^{-m},
\qquad \mathcal P=\prod_iD_i.
\]

There is no fractional-cardinality assumption or floor issue here. A dyad with an upper support bound below one is empty. The note explicitly records the upper cutoff \(C\le\min_{i\in I}\beta_iD_i\) for any nonempty piece.

For a fixed tuple, the variable sum has form

\[
\eta(u)\sum_cz_c\chi_c(u)^m,
\]

where \(\eta\) is a bounded row multiplier, \(z_c\) contains the exact row-independent masks, and

\[
\sum_c|z_c|^2\ll_{\mathbf W,k}L.
\]

Neither the Möbius signs nor the smooth weights interfere with the arbitrary-coefficient sieve. The norm contraction by \(\eta(u)\), followed by Minkowski over the frozen tuples, yields the stated three norm terms

\[
\mathcal P\left(
\sqrt H\,L^{1/2-m}
+H^{1/(2r)}L^{1-m}
+H^{1/3}L^{5/6-m}\right)
\]

for \(r=3,6\), the first two for \(r=2\), and
\(\sqrt H\,\mathcal P L^{1-m}\) for \(r=1\).

All exponents of \(L\) are negative for \(m\ge2\). Thus the dyadic tail norms form convergent geometric sums beginning at \(C\). Squaring introduces only a fixed factor. I obtain exactly the master bounds (4.1)–(4.3).

The proof estimates a specified polynomial piece in row \(\ell^2\). It does not identify that piece as a positive sub-moment of the original \(|A_u|^{2k}\), and it does not use any such positivity. Its use of Minkowski is appropriate for this scope.

## 5. Recomputed general cutoff algebra

Divide the master squared bound by \(H\mathcal P\). For \(r=3,6\), the three ratios are

\[
\mathcal P C^{1-2m},\qquad
\mathcal P H^{1/r-1}C^{2-2m},\qquad
\mathcal P H^{-1/3}C^{5/3-2m}.
\]

Making each at most one gives precisely

\[
C\ge
\max\left\{
1,\,
\mathcal P^{1/(2m-1)},\,
(\mathcal P/H^{1-1/r})^{1/(2m-2)},\,
(\mathcal P^3/H)^{1/(6m-5)}
\right\}.
\]

For \(r=2\), omit the last term and use \(1-1/r=1/2\). For \(r=1\), the condition is \(C^{2m-2}\ge\mathcal P\). These agree with (4.10)–(4.11).

Substituting \(\mathcal P=D^k\), \(H=D^h\), gives the exponent (4.12) without alteration:

\[
\max\left\{
0,\,
\frac{k}{2m-1},\,
\frac{k-h(1-1/r)}{2m-2},\,
\frac{3k-h}{6m-5}
\right\}.
\]

The compatibility with factor support is a genuine condition and is explicitly retained in the statement.

## 6. Fourth moment and the strict improvement

For \(k=m=2\), the gcd phase has order three, not six. Substitution gives

\[
\|T_{\ge C}\|_2^2
\ll(DH)^\epsilon D^4
\left(HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right).
\]

The exact formula obtained from \(n_1=ca,n_2=cb\), with squarefree pairwise-coprime \(a,b,c\), preserves the cubic factor \(\chi_c(u)^2\) in the varying sum. The proof does not replace it by its absolute value before applying the sieve.

The target \(HD^2\) therefore follows at

\[
C\ge\max\{1,D^{2/3},DH^{-1/3},(D^6/H)^{1/7}\}.
\]

When \(H=D^h\), \(1<h\le11/10\), the last term dominates. The two exact comparisons are

\[
\frac{6-h}{7}-\frac23=\frac{4-3h}{21}\ge0,
\qquad
\frac{6-h}{7}-\left(1-\frac h3\right)
=\frac{4h-3}{21}\ge0.
\]

The previously stated core cutoff is \(D^{(4-h)/4}\). Its exponent exceeds the new one by

\[
\frac{4-h}{4}-\frac{6-h}{7}
=\frac{4-3h}{28}
=\frac{1-3\theta}{28}>0
\]

for \(h=1+\theta\), \(0<\theta\le1/10\). The asymptotic thresholds as \(h\downarrow1\) are therefore \(D^{3/4}\) and \(D^{5/7}\). This is a strict enlargement of the controlled gcd tail.

## 7. Rectangular comparison

Writing \(P=XY\), the same calculation gives

\[
C\ge\max\{1,P^{1/3},P^{1/2}H^{-1/3},P^{3/7}H^{-1/7}\}.
\]

The last term dominates \(P^{1/3}\) exactly when \(H\le P^{2/3}\), and dominates \(P^{1/2}H^{-1/3}\) exactly when \(H\ge P^{3/8}\). It is strictly smaller than the previous cutoff \(P^{1/2}H^{-1/4}\) exactly when \(H<P^{2/3}\). Thus the stated interval

\[
P^{3/8}\le H<P^{2/3}
\]

is correct, including the strict upper endpoint for a strict improvement. The additional requirement \(C\le\min(\beta_1X,\beta_2Y)\) is necessary and is present. The theorem is not asserting usefulness for every anisotropic pair.

## 8. Limits of the certification

The classical analytic input is assumed in its exact form as written in Section 1. This review verifies the new algebraic and norm deductions from that input, including their all-row zero extensions. It does not independently authenticate the external large-sieve source or prove a new Möbius second moment.

The result controls the large-gcd polynomial tail. The complementary small-gcd piece remains unbounded at the desired diagonal fourth-moment scale. Consequently, the note's explicit refusal to claim the full fourth moment, the full hierarchy, or a new zero-free region is appropriate.

No mutation was made to the reviewed file. No numerical or formal proof claim is made by this review.
