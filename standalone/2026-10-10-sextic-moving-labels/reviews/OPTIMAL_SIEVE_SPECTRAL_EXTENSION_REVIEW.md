# Independent review of the optimal-sieve spectral extension

**Reviewer:** moving-label adapter author, independently reviewing the descent author's spectral extension. This review does not concern a theorem authored by this reviewer.

**Frozen target:** *OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md*, SHA-256 **b0d3eee6d32ad7f69bfdd8ac5132c60139f322b1102086897ce0099defab8551**. The complete target was read, and its hash was checked again before this review was written. No target source was edited.

**Verdict:** **passes at its explicitly stated source-conditional scope.** The fixed-family comparison preserves common-prime zeros; the all-row decomposition retains the sixth-power repetition term; the three crossover computations yield the stated strict threshold \(4/7\); and the new canonical estimate transfers to the exact **squarefree-row** reflected series of PR #922 with all its cusp and ramified labels retained. The imported external large-sieve theorem and the inherited theta identities remain assumptions. This is not an independent proof of either external foundation.

## 1. Sources and exact scope

The following documents were read in full for this review.

| Document | Source or SHA-256 |
|---|---|
| Frozen target | b0d3eee6d32ad7f69bfdd8ac5132c60139f322b1102086897ce0099defab8551 |
| *ALL_ROW_SPECTRAL_MEAN.md* | ef597dfc793af976a92b731f01930fc199948e99d5ccf2fc3fe2c91ec5249a8b |
| PR #916, *continuation-integrated-window/OPTIMAL_SIEVE_AUDIT.md* | Commit f5c089e33ccce4eae4307d4f6475b9977485cb78; file 11c48419de8c34160a18343ceadefc9ff7646942d22ccfc1e52024dc3b66d25f |
| PR #922, *SECOND_REFLECTION_BOOTSTRAP.md* | Commit f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32; file e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0 |
| PR #922, *FULL_CUSP_DESCENT.md* | Same commit; file b025af8af1ac13d07a04fbc7de71401d2a47ef2c8df5a1e89a4edc4973482504 |

I also directly inspected the primary HTML of Alexandre de Faveri, [*Optimal large sieve for fixed order characters*, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1): Theorem 1.1 and Sections 2.3.4, 2.5.1 and 2.5.2. The imported statement has sixth-power-free row and column indices, arbitrary column coefficients, and fixed construction data. The source's conductor and residue-symbol conventions explicitly matter at shared primes. The Eisenstein field and an admissible fixed set of bad primes meet the field and class-group conditions used by the adapter. This review accepts that external theorem as an input; it checks its use here rather than attempting to reconstruct its proof.

The canonical Proposition R estimate and its theta foundation are inherited through the baseline note. The finite-cusp composition theorem is inherited through the pinned PR #922 documents. The review checks the new composition, uniformity, convergence and numerical deductions built on those inputs.

## 2. Fixed-family comparison and literal zeros

There are two logically separate operations in the target's Section 1: identify the repository symbols with a fixed admissible source family on sixth-power-free rows, and then reintroduce arbitrary sixth-power content. Their order is correct.

In the PID setting, the Kummer representative attached to a principal ideal and its fixed generator differ, modulo a sixth power, by an \(S\)-unit. The \(S\)-unit group modulo sixth powers is finite. Fixing that class moves only a fixed bounded phase into the column coefficients. The two fixed ray classes needed for reciprocity, and the finitely many element units, can likewise be partitioned before applying the operator. This is a comparison inside finitely many fixed families, not an appeal to uniformity in an arbitrary changing family construction.

For a sixth-power-free row, every occurring good-prime valuation is \(1,\ldots,5\). Its residue character is nontrivial at that prime. Consequently the primitive conductor retains that prime, and a column meeting the row has value zero in both conventions. This is the essential reason a comparison made only on unit values is sufficient here after checking the conductors. The argument would need repair if sixth-power primes had been included at this stage without their masks.

For arbitrary rows the target explicitly writes
\[
k=\epsilon z v^6 r,\qquad r\text{ sixth-power-free},
\]
where \(z\) is supported on the fixed bad set. There is no condition \((v,r)=1\). At a physical column outside that set,
\[
\chi_n(k)=\chi_n(\epsilon z)\,
\mathbf1_{(n,v)=1}\,\chi_n(r).
\]
Thus the lost conductor primes in \(v^6\) return as literal column masks. Even when \(v\) meets \(r\), this identity remains exact.

For fixed \(\epsilon,z,v\), the coefficients are fixed before the sieve is used. Summation over \(v\) gives the four weights
\[
(Nv)^{-6},\qquad 1,\qquad (Nv)^{-5},\qquad (Nv)^{-2},
\]
respectively. The second one is counted up to \((H/Nz)^{1/6}\). Therefore the resulting all-row bound is precisely
\[
H+H^{1/6}L+H^{5/6}L^{1/3}+H^{1/3}L^{5/6}.
\]
The target retains the \(H^{1/6}L\) term. Its positive height exponent also makes the remaining sum over bad-prime factors \(z\) a convergent fixed Euler product. No unproved removal of the generic sixth-power multiplicity has entered this spectral argument.

## 3. Completed blocks and the canonical analytic continuation

The target uses the same canonical series, auxiliary and zero-masked cube product as the baseline. In particular, a prime of the auxiliary \(d\) excludes physical columns; \(d\) is allowed to overlap \(k\). This does not say that the whole series \(G_{k,d}\) vanishes whenever \(k\) and \(d\) meet.

The literal cube expansion has coefficient \(c_k(b)/(Nb)\) multiplying a normalized raw block at length
\[
L_b=X/(Nb)^3.
\]
For a fixed \(b\), the exterior \(c_k(b)\) is a bounded row multiplier. The auxiliary and bad-prime masks are fixed column contractions. The raw block has bounded squared coefficient mass on its smooth dyadic support. The sieve therefore applies in the stated normalization.

The weighted Cauchy step is also compatible with the cube support. Its harmonic first factor and the height term produce only logarithms; every positive length exponent \(t\) uses a convergent sum
\[
\sum_b (Nb)^{-1-3t}.
\]
The indices \(n\) and \(b\) need not be coprime, and the target does not impose such a restriction. The fixed lower bound on every nonempty compact support block covers bounded values of \(L_b<1\); it does not require a new sieve at arbitrarily small length.

The analytic reconstruction uses the old reflected estimate
\[
H+H^2F/X
\]
as well as the new generic bound. For fixed \(H,F\), the weighted dyadic sum converges normally on compact subsets of \(\Re u>1/2\). In the same half-plane the cube parameter satisfies
\[
\Re(3u-1/2)>1.
\]
The cube product and its reciprocal are then absolutely bounded, uniformly in row and auxiliary exclusions. This proves the stated transfer between the exact completion and \(G_{k,d}\) without an additional reciprocal bound near a zero of a Hecke \(L\)-function.

## 4. The three thresholds and uniform strip estimate

For a generic monomial \(H^rX^t\), comparison with \(H^2F/X\) occurs at
\[
X_{r,t}=H^{(2-r)/(1+t)}F^{1/(1+t)}.
\]
After multiplying the square root by \(X^{1/2-a}\), the crossover contributes
\[
H^{1-a(2-r)/(1+t)}F^{1/2-a/(1+t)}.
\]

I recomputed all three cases.

| \((r,t)\) | Required height threshold for a square-root row norm |
|---|---|
| \((1/6,1)\) | \(a\ge 6/11\) |
| \((5/6,1/3)\) | \(a\ge 4/7\) |
| \((1/3,5/6)\) | \(a\ge 11/20\) |

The maximum is \(4/7\). Since \(t\le1\) in every case, the auxiliary factor is bounded by \(F^{(1-a)/2}\). Since \(r<1\), a lower-end contribution \(H^{r/2}\) is bounded by \(H^{1/2}\).

The proof correctly treats the interior values where the lower dyadic exponent \((1+t)/2-a\) changes sign. A bound by the crossover plus the lower endpoint, with a logarithmic factor, is uniform across that transition. There is no artificial pole in the strip constant there. The preliminary small powers and vertical smooth-test seminorms can be absorbed using the two strict strip margins.

The stated obstruction from \(X=H^{7/8}\), \(F=1\), is a valid comparison of the available upper-bound envelopes. It is explicitly not a lower bound for the actual canonical series and should not be read as such.

## 5. Exact transfer to the squarefree-row reflected series

The source identity in *SECOND_REFLECTION_BOOTSTRAP.md* has
\[
u=v-s,\quad a=\Re u,\quad \tau=\Re v,\quad t=1-s.
\]
Its conditioned divisor representation writes the relevant canonical \(Z_k\) as an absolute cube Euler factor times
\[
\sum_{\substack{d\ {\rm squarefree}\\(d,kS)=1}}
\frac{\widetilde a_k(d)h(d)}{(Nd)^u}\,G_{k,d}(u),
\]
with \(|\widetilde a_k(d)|\le1\) and
\[
|h(d)|\ll_\epsilon (Nd)^{-(1-\tau)+\epsilon}.
\]
The cube-character matching condition in the source is retained. The target does not replace that character by a generic independent family.

For each fixed \(d\), the restriction \((d,k)=1\) is a restriction of the row set, or equivalently a row contraction after extending \(\widetilde a_k(d)\) by zero. The new spectral bound is uniform for such subsets. It is consequently legitimate to apply it before Minkowski in \(d\), even though the allowed row subset moves with \(d\).

The resulting \(d\)-term norm is
\[
H^{1/2+\epsilon}
(Nd)^{-a-(1-\tau)+(1-a)/2+\epsilon}.
\]
The strict sufficient summability condition is exactly
\[
-a-(1-\tau)+(1-a)/2<-1
\quad\Longleftrightarrow\quad
\tau<(3a-1)/2.
\]
Choosing the preliminary epsilon smaller than the margin makes the ideal sum converge.

The condition \(a<1\) matters here. It gives
\[
(3a-1)/2<a,\qquad
\tau<1,\qquad
\Re t=1+a-\tau>1.
\]
Thus the proposed new mean region lies inside the exact source chamber with an absolute cube product. It is not a continuation of the source identity across an unchecked wall.

Finally, *FULL_CUSP_DESCENT.md* expresses the actual \(\mathcal Y_k\) as the prescribed complete cusp and finite-ray sum of these \(Z_k\)'s. Its coefficient mass is absolutely bounded in this region, including the full bad-prime and ramified labels. Row-dependent cusp coefficients are bounded multipliers; Minkowski controls their cross terms. No orthogonality or discarded cross-cusp cancellation is needed.

The corollary retains the source's squarefree row restriction. Although the canonical \(G_{k,d}\) theorem now permits all nonzero rows, the source identity for \(\mathcal Y_k\) has not thereby been proved for nonsquarefree rows. The target makes exactly this distinction.

## 6. Numerical consequences and retained limits

The optimization of the scalar exponent is correct:
\[
2a-\tau>(1+a)/2,\qquad
\inf(2a-\tau)=11/14.
\]
The old scalar infimum \(13/16\) exceeds this by \(3/112\). These numbers are spectral/Mellin exponents, not zero-free constants.

The non-improvement comparison is also correct. The factorwise energy is bounded by a constant times \(HD^{11/7}\) when \(H\le D^{4/7}\). The classical squarefree-row energy is bounded by the same candidate when \(H\ge D^{3/7}\). These overlapping ranges cover every \(H\ge1\). Even after a valid physical contour transfer, that candidate alone would not improve the older physical minimum.

The passing verdict therefore covers a new source-conditional all-row canonical spectral domain and an exact squarefree-row cusp-mean consequence. It does not establish the signed moving-auxiliary comparison, the original Möbius higher moment, a \(17/24\) zero-free boundary, the generalized moment hierarchy, or the Riemann hypothesis. No such assertion is needed for the proof that was reviewed.
