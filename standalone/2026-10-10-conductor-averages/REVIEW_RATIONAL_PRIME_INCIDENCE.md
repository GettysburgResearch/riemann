# Independent reconstruction of rational-prime incidence and its composition

**Reviewer:** the separate Möbius/scale research agent. This is an
independent AI-agent reconstruction, not human peer review or
proof-assistant certification. The reviewer authored the Gaussian
sampling note in this packet, but did not author either mathematical
object reviewed below.

**Primary reviewed object:** the complete
[RATIONAL_PRIME_INCIDENCE.md](RATIONAL_PRIME_INCIDENCE.md), 35,732 bytes,
SHA-256

    84b3aa3ba6ab0bdd05f70e2682f52d46697a335c8fa4f91cae77107de3b04d0e

**Companion independently checked for the composition:** the complete
[CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md), 24,307 bytes,
SHA-256

    74d9063bd36128d2b510a11d96dda8055539bd7c7a2f2d07f5cc3a105223ea61

These receipts bind file contents. A source-commit receipt must be
added after the mathematical source is frozen. In particular, a later
edit to either target is not covered merely by retaining its filename.

**Verdict:** the rational radical theorem, fixed rational-type count,
four-parameter accounting bounds, and rational singleton composition
are valid deductions at their explicitly stated dependencies and scope.
The reviewed companion's moving-background conductor mean, complete-row
adapter, all-order bound, and size-sensitive Corollary 4.3 also withstand
an independent reconstruction. The complete generalized moment and the
remaining signed upper bound are not established by these results.

The review found a local typographical error in the split-prime
formula: the two conductor indicators must be added in (1.7).
The reviewed content contains the repaired sum. The reviewer also
requested that the examples be compared with the specified positive
accounting branches, rather than described as outside every earlier
signed method. Both reviewed objects now state that distinction.

## 1. Exact source and review boundary

The following pinned sources were inspected for the identities,
earlier estimates, and comparisons used in this review:

- PR #914, commit
  0cc0428fedbbfc340044c7451b3d392c1da9a103,
  CONDUCTOR_SECTORS.md: the literal residual character and principal
  mask, smooth Poisson estimate, and earlier prime-ideal incidence.
- PR #925, frozen mathematical source
  5ad900ff27d34f1a8f94d28e19c47a3b37de6e39,
  SIGNED_CONDUCTOR_PROGRESS.md: the element-row subconvex adapters
  and the pointwise conductor accounting branches.
- PR #919, commit
  9b04a887e171b3104a66cf57296ce5b0b2920d78,
  SMALL_GCD_CONDUCTOR_REDUCTION.md: the actual signed remainder
  to which a new positively controlled region may be subtracted.
- PR #924, commit
  725b2d25ab47e57500049d93985560098c7ef3fa,
  CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md: the cross-gcd comparison.
- PR #926, commit
  086bf0560c0c2679a1fe41418f583d2c5ca743c3,
  [MOBIUS_OVERLAP_TAILS.md](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md),
  Sections 2, 5.1, and 6: the cubic axis cost, separately conditional
  common-gcd cutoff, and complete signed block selector.

For the new conductor mean, the reviewer independently opened
[de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
dated 2 October 2026, and inspected Proposition 8.1, the fixed-ray
construction and Eisenstein example in Sections 2.3--2.5, and the
approximate-functional-equation argument in the proof of Theorem 1.2.
The unrestricted outer ideals, squarefree inner ideal, arbitrary
coefficient vector, reciprocity partition, and conductor normalization
agree with the companion's stated input.

This review does not certify the full external proof of that new
large-sieve proposition, or reprove the external subconvex inputs of
PR #925. They remain identified analytic dependencies. The elementary
rational radical theorem uses none of those external subconvex or
cubic-average inputs.

## 2. Reconstruction of the rational count

Fix the moment order and the original column support. For a tuple
of \(2k\) squarefree good ideals, the ordinary integer
\[
\mathscr N=\prod_iNn_i\prod_iNm_i\le(BD)^{2k}
\]
is the correct object for counting rational primes. At a split prime
there are two independent prime-ideal incidence subsets, but only one
ordinary rational prime parameter. Hence at most \(2^{4k}\) local
choices occur. At an inert prime there is one incidence subset and at
most \(2^{2k}\) choices. The assignments are allowed to put both
conjugate prime ideals in the same column.

For fixed rational radical \(\rho\), these choices determine the
tuple of ideals. The number is bounded by
\[
C_k^{\omega(\rho)}\ll_{k,\eta}\rho^\eta
\ll_{k,B,\epsilon}D^\epsilon.
\]
The last bound uses the original support, not an unjustified bound
on all integers appearing in an enlarged sum. Summing at most \(R\)
possible positive integers \(\rho\le R\) proves Theorem 2.1.
The bound is valid also when \(R\) exceeds the physical support:
only supported tuples require the small-power estimate.

Both the smooth and sharp row counts are \(O(H)\) for \(H\ge1\).
Therefore the entire sector \(\rho\le(BD)^k\) has positive absolute
accounting \(O(HD^{k+\epsilon})\). In the squarefull-total-norm
sector, \(\rho^2\le\mathscr N\); this proves the stated corollary,
including tuples with pairwise coprime column ideals. No estimate
for a character sum or a reciprocal \(L\)-function occurs here.

The local conductor formulas require the sum of the two split
indicators:
\[
\ell_p=m_{\mathfrak p}+m_{\overline{\mathfrak p}},
\qquad
j_p=\mathbf1_{e_{\mathfrak p}\ne0}
    +\mathbf1_{e_{\overline{\mathfrak p}}\ne0}.
\]
For an inert prime the two quantities are
\[
\ell_p=2m_{p\mathcal O_K},\qquad
j_p=2\mathbf1_{e_{p\mathcal O_K}\ne0}.
\]
In particular, one inert prime ideal occurring once has type
\((2,2)\), not \((1,1)\). A principal rational prime cannot have
\(\ell_p=1\).

These observations give the fixed-label inequality
\[
r_0^2\prod_{\ell,j}r_{\ell,j}^{\ell}
\le(BD)^{2k}.
\]
For fixed nonprincipal labels, put
\[
Z=(BD)^k\prod_{\ell,j}r_{\ell,j}^{-\ell/2}.
\]
If \(Z<1\), no tuple exists. Otherwise there are at most \(Z\)
possible positive integers \(r_0\), and the same local-assignment
bound applies for each. This yields Lemma 3.1 with its fractional
weight. There is no second count of the conjugate prime ideals;
this is the precise source of the rational-prime saving.

## 3. Reconstruction of the four block powers

For a row estimate of the form
\[
H^\tau(Nf)^\gamma D^\epsilon,
\]
the fixed rational labels have weight
\[
D^{k+\epsilon}H^\tau
\prod_{\ell,j}r_{\ell,j}^{j\gamma-\ell/2}.
\]
Counting ordinary integers in a dyadic interval adds one to each
retained exponent. For the four exceptional types, the resulting
powers are
\[
\frac12+\gamma,\qquad
\gamma,\qquad 2\gamma,\qquad
2\gamma-\frac12.
\]
This reproduces every entry of the reviewed table.

For the trivial row bound, all omitted types have
\(\ell\ge3\), so their weights sum absolutely. For completion,
\(\gamma=1/2\), the only omitted borderline types are
\((3,1)\) and \((4,2)\), each with weight exponent \(-1\).
Their physical cutoffs give logarithms that can be absorbed in
the prescribed positive loss. The \((3,2)\) label has a positive
completion exponent and is correctly kept as \(U^{1/2}\).

For \(\beta=103/512\), every omitted type has exponent at most
\[
2\beta-\frac32=-\frac{281}{256}<-1.
\]
The same argument for \(\gamma=1/6\) gives strict convergence of
the omitted sums. The nonprincipal condition is retained whenever
completion or subconvexity is used. The principal-mask divisor loss
is reassigned using \(NfNq_0\le(BD)^{2k}\), with the bad set fixed.

The four-label bounds consequently have the stated powers
\[
D^{k+\epsilon}\min\left\{
H L^{1/2}U^{-1/2},
L G^{1/2}T U^{1/2},
H^{1/2}L^{359/512}G^{103/512}T^{103/256}U^{-25/256}
\right\}.
\]
The prime-sensitive branch uses the largest prime-ideal norm
\(P(f)\). At an inert prime that norm is \(p^2\); replacing it
with \(p\) would be wrong. The balanced-divisor branch is used only
on the tuples satisfying its actual fixed-comparison divisor
condition.

Summing \(U\) is justified for the three negative exponents
\(-1/2,-25/256,-1/6\). It is not justified for the positive
completion exponent, and the note does not claim that sum.
The displayed diagonal regions follow by dyadic partition,
including the correct endpoint treatment for the negative
\(z\)-power. Only a fixed-order power of \(\log D\) is lost.

All these steps concern nonnegative accounting after the complete
row kernel has been retained. They therefore allow any further
tuple selector, including restrictions inherited from an earlier
signed remainder. No unsigned monotonicity of a signed sum is
being assumed.

## 4. Independent check of the cubic mean used in Section 8

The following checks also cover the companion's complete
source-dependent deduction, including its last Corollary 4.3.

### Moving conductor and common coefficients

For fixed background good conductor \(\mathfrak r\), disjointness
from squarefree coprime \(a,b\) makes the good conductor of the
product exactly \(\mathfrak r ab\). Its analytic conductor is
comparable to \(RNaNb(2+|t|)^2\), with bounded local possibilities
at the fixed bad primes. The finite bad set is not enlarged to
absorb \(R\).

The direct and dual approximate-functional-equation terms are
estimated separately. The dual root number remains a row
multiplier of modulus one; no separation of that root number
into factors depending on \(a,b\) is needed.

On a positive Mellin line, the real conductor multiplier costs an
arbitrarily small power, while its imaginary part has modulus one.
The Gaussian auxiliary factor gives an integrable Mellin kernel,
with polynomial dependence on the original height. The common
cutoff can therefore be taken as
\[
Y=(RAB)^{1/2+\delta}(2+|t|)^{C_\delta}.
\]
After separating that kernel, the good-index coefficient is
\(\psi(n)(Nn)^{-1/2-\delta-i\tau}\), independent of the varying
cubic labels. This is the load-bearing uniformity point: the
source's fixed-twist Theorem 1.2 is not invoked with an uncontrolled
moving constant.

Writing \(n=sqr^2\), with \(s\mid S^\infty\), \(q,r\) good and
\(q\) squarefree, introduces no coprimality requirement between
\(q,r\). Weighted Cauchy--Schwarz uses the convergent sum
\[
\sum_{s\mid S^\infty}\sum_r(N(sr^2))^{-1/2-\delta}<\infty.
\]
For fixed \(s,r\), their character values are bounded row
multipliers. At bad primes these values must be those of the
actual primitive product, including possible conductor
cancellation; the reviewed proof explicitly makes that correction.
At good primes the coefficient preserves the zeros of \(\psi(q)\).

After the fixed finite reciprocity partition, the coefficient norm
on a squarefree \(q\)-block is \(O_\delta(Q^{-2\delta})\).
The imported arbitrary-coefficient proposition applies. Its three
terms, after inserting \(Q\le Y\), give
\[
AB+M^{2/3}N^{1/3}(RAB)^{1/2}
  +M^{1/3}N^{2/3}(RAB)^{1/3}.
\]
Dividing by \(AB=MN\) gives
\[
1+R^{1/2}(M/N)^{1/6}+(R/M)^{1/3}.
\]
Both additional terms are at most \(R^{1/2}\) when \(R,M\ge1\)
and \(M\le N\). Small losses and logarithms are absorbed only
after imposing the physical norm ranges. The claimed uniform
dependence is thus the one obtained from the proposition.

### Unit correction, masks, and background counting

The radial complete row sum vanishes for a character nontrivial
on units. Otherwise its ideal Mellin representation has exactly
the factor six. The principal mask remains its exact finite Euler
polynomial before it is bounded by
\[
\prod_{p\mid q_0}(1+(Np)^{-1/2})
\ll_\eta(Nq_0)^\eta.
\]
The contour shift involves a nonprincipal \(L\)-function, never
its reciprocal. No zero-free premise is required.

A multiplicity-two nonprincipal prime has exponent \(2\) or \(4\),
so the varying labels form the cubic family \(ab^2\). After fixing
the background residual exponents and the finite ray classes of
\(a,b\), the discrepancy between physical symbols and that family
is fixed. The quotient of the total unit-trivial ideal character
by the cubic Hecke character has good conductor
\[
R=Ng_1\prod_{m\ge3}Ng_m
\]
and is independent of \(a,b\) within the class. The proof does not
assume that the uncorrected background element character is itself
unit-trivial. The source's finite class correction and class number
one justify the stated adapter.

The principal-mask count contributes
\[
D^k(Ng_1)^{-1/2}(Nab)^{-1}
\prod_{m\ge3}(Ng_m)^{-m/2}.
\]
All residual background exponents are frozen before applying the
mean. Their finite assignment count costs \(D^\epsilon\);
an \(a,b\)-dependent supremum is not inserted into the coefficient
vector. Cauchy--Schwarz on the conductor mean yields the first
mean \(ABR^{1/4}\), up to the stated losses, and its \(AB\)
cancels the weight \((Nab)^{-1}\).

The remaining background weight is consequently
\[
D^{k+\epsilon}H^{1/2}
(Ng_1)^{-1/4}\prod_{m\ge3}(Ng_m)^{-m/2+1/4}.
\]
The \(g_1\)-block sums to \(L^{3/4}\); every higher ideal sum
converges, already with exponent \(-5/4\) for \(m=3\).
This verifies the companion's all-order positive accounting
theorem and the exact fixed-background input used in rational
Section 8.

### The size-sensitive refinement

Retaining the sharper conductor mean before taking its square
root gives the three multipliers
\[
1,\qquad R^{1/4}(M/N)^{1/12},\qquad
R^{1/6}M^{-1/6}.
\]
Their singleton sums are respectively
\[
L^{1/2},\qquad L^{3/4}(M/N)^{1/12},\qquad
L^{2/3}M^{-1/6}.
\]
The three higher-multiplicity sums all converge, since none has
positive conductor exponent exceeding \(1/4\). This proves
the companion's (4.9). Comparing each term with \(H^{1/2}\)
and raising to powers \(2,12,6\) gives exactly
\[
L\le H,\qquad L^9M/N\le H^6,\qquad L^4\le H^3M.
\]
Dyadic partition of the actual cubic labels is legitimate and
produces only fixed factors and logarithms. These conditions
contain the earlier \(L\le H^{2/3}\) region, while allowing
additional compatible anisotropic ranges. No arbitrary proposed
norm configuration is claimed to be realizable.

## 5. Reconstruction of the rational singleton composition

The labels \(v(g_1),w(g_1)\) are determined by the singleton ideal
alone. They are not the full-tuple labels \(\lambda,t\). In
particular, a conjugate prime lying in a higher multiplicity
label does not move its singleton partner from \(v\) to \(w\).

Every squarefree singleton ideal satisfies
\[
Ng_1=v(g_1)w(g_1)^2,\qquad (v(g_1),w(g_1))=1.
\]
For fixed \(v,w\), there are at most \(2^{\omega(v)}\) ideals
\(g_1\). A split prime of \(v\) offers two choices; a prime of
\(w\) gives either the full conjugate pair or the unique inert
ideal. Thus the companion's singleton weight sums as
\[
\sum_{\substack{g_1:\ v(g_1)\sim V\\w(g_1)\sim W}}
(Ng_1)^{-1/4}
\ll D^\epsilon
\sum_{v\sim V}v^{-1/4}\sum_{w\sim W}w^{-1/2}
\ll D^\epsilon V^{3/4}W^{1/2}.
\]
The remaining higher-multiplicity ideal sums retain their strict
convergence margin. Rational-prime disjointness across the
different \(g_m\) is not assumed; any exclusions are dropped only
in the final positive majorant, after the cubic labels have
already been averaged with the correct fixed background.

This proves the stated bound and the complete diagonal region
\[
v(g_1)^3w(g_1)^2\le H^2.
\]
The unrefined cubic region is equivalently
\(v^3w^6\le H^2\), which is contained in the new one because
\(w\ge1\). The composition therefore gives a valid enlargement
of that positive controlled domain.

## 6. Exact comparisons and the remaining signed problem

The conjugate-pair example in Section 6 is compatible with pairwise
coprimality of all prime-ideal columns. Its total norm is
squarefull and its rational radical has scale \(D^k\). This is a
valid elementary improvement over treating every singleton ideal
as a separate ordinary norm parameter. The example only shows a
controlled sector and does not estimate its share of the full
moment.

For Section 7, I independently recalculated
\[
Ng_1:D^{2/5},\quad Ng_2:D^{7/5},\quad
\lambda:D^{8/25},\quad t:D^{1/25},\quad
\rho:D^{54/25}.
\]
At \(h=21/20\), the four excesses relative to \(HD^2\) are,
in the order of the table,
\[
\frac1{20},\qquad \frac{19}{512},\qquad
\frac1{100},\qquad-\frac{37}{12800}.
\]
The divisor-gap argument uses that \(c,d\) are actual prime
ideals. A divisor containing one has exponent at least \(7/10\);
a divisor avoiding both has exponent at most \(2/5\).
Neither is within a fixed factor of exponent \(3/5\), so the
balanced-divisor alternative is unavailable as stated.

For the composition example, each original column exponent is one.
The labels \(v,w\) have exponents \(3/5,1/10\), while
\(Ng_1\) has exponent \(4/5\). At the same height, the unrefined
cubic excess is \(3/40\), and the composed excess is \(-1/40\).
The separate rational completion and Wu excesses are \(3/20\)
and \(351/2560\). These are exact comparisons of upper-bound
formulas, not lower bounds on their underlying arithmetic sums.

An important comparison limit is now explicit. PR #926
Theorem 6.2, equations (6.6) and (6.8), already gives two-axis
bounds for complete smooth signed blocks with the source's
structured coefficients. With the elementary pointwise exponent
\(b=1\), its cubic cost is
\[
\mathcal Q_3(H,Q)=
\left[Q+H^{-2/3}Q^2+H^{-1/3}Q^{5/3}\right]^{1/2}.
\]
In the cubic companion's Section 5 example, selecting both
even axes gives cost exponent \(13/40\) on each axis, and the
remaining labels cost \(2/3+7/15\). Thus that source already
bounds the unselected complete signed block by
\(HD^{107/60+\epsilon}\).
For the rational composition example, the broader complete
signed block similarly has exponent
\[
\frac45+\frac35+\frac14+\frac14=\frac{19}{10}.
\]
Neither observation bounds the positive sum of individual
absolute tuple kernels, or its arbitrary selectors such as a
prescribed conjugate pairing. The new results are correctly
stated as improvements in that positive accounting problem.
They are not claimed to improve those earlier complete signed
block estimates.

Finally, the selected controlled union is invariant under
Hermitian-side interchange. Its complement therefore has a real
signed contribution. Removing the union costs
\(O(HD^{k+\epsilon})\) in absolute value and preserves the
stated remainder decomposition and lower bound. The principal
tuples cause no omission: their rational radical already lies
in the elementary controlled sector.

No upper bound for the surviving signed complement is supplied.
Top-scale split-prime singletons over distinct rational primes
still have radical and singleton norm of order \(D^{2k}\).
They remain outside the diagonal regions near \(H=D\).
Consequently this review approves the stated component deductions
at their explicit imported-input scope, without approving the
full \(2k\)-th moment, a sampled arithmetic hypothesis, a new
zero-free half-plane, or RH.
