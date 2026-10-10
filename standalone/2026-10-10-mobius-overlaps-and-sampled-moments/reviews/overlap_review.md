# Independent review of Signed residuals and two oscillating incidence axes

Reviewer: theta_closure, a nonauthor of the reviewed moment note.

Reviewed file: attack3_moments.md, titled Signed residuals and two oscillating incidence axes.

Exact reviewed SHA256:

980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04

**Verdict:** the native component deductions in Sections 3--7 are mathematically consistent under the explicitly stated analytic premises. I reconstructed the complete proof, including the designated-factor correction, sharp common-factor cutoff, critical mixed-sign correction, grouped cubic products, double-triangle thresholds, and embedding at every fixed higher order. No change to the frozen note is requested.

This verdict is conditional on the displayed classical all-row character-sieve interfaces and on the optional uniform inverse premises where used. It is not an independent proof of the imported 7/8 statement, the native inverse second moment, a full generalized moment theorem, or RH.

## 1. Source and quantifier checks

I read all 781 lines of the frozen note and checked its content hash. I also checked the locally pinned source manifest and the relevant earlier-selector statements. The quadratic companion currently has the exact hash cited in Section 5.2:

7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696.

The classical inputs needed by the new main examples are the all-row cubic and, for the common degree-three factor, quadratic sieve. Their primitive squarefree-column hypotheses, fixed ray/unit partitions and nonunit-zero convention remain explicit. The paper's all-row reduction is compatible with these: cubic rows split as a cube part times two coprime squarefree factors; quadratic rows split as a square part times one squarefree factor. In each case the excluded primes from the power part stay in the column vector. I accepted the cited squarefree large sieves as external inputs rather than claiming to reprove them.

The cancellation premise PW_b^sm is uniform in a fixed physical row range, all smaller column scales, and its stated exclusions, with a fixed finite test seminorm. These quantifiers are exactly what the Mellin and finite-convolution proofs use. A theorem only on a scale-linked diagonal or with uncontrolled conductor constants would not suffice.

The optional NM2 premise is stronger than a generic fixed-scale statement and is kept optional. Neither the new common-factor numerical example nor the grouped double-triangle numerical example uses NM2. The sharper quadratic common-factor example additionally needs the interval-test consequence of R_b. The note explicitly supplies this distinction rather than deriving sharp interval cancellation from a bare smooth-test estimate.

## 2. Designated-incidence algebra and its weighted correction

For a designated incidence set I of size m, I reconstructed the local possibilities directly from the original squarefree tuple. If the prime occurs in c=q_I, it occurs in no residual coordinate and has coefficient (-1)^m z_0. Otherwise the residual incidence may be any subset except exactly I. Thus the required local series is

\[
R-\varepsilon_m Z_I+\varepsilon_m z_0,
\qquad R=\prod_i(1-z_i),\quad \varepsilon_m=(-1)^m.
\]

Subtracting the independent factor \((1+\varepsilon_m z_0)R\) gives exactly

\[
\varepsilon_m\{z_0(1-R)-Z_I\}.
\]

Every nonconstant numerator term therefore either involves c and a residual axis or all m residual coordinates in I. The weighted majorant consequently starts with
\(q^{-\alpha-b}+q^{-mb}\), not a one-axis term. The strict hypotheses
\(\alpha+b>1\) and \(mb>1\) prove absolute convergence, including every fixed small prime. I checked that no condition such as \(1-k/\sqrt q>0\) has been inserted.

The global convolution shifts the c-scale by Nd_0 and the residual scales by Nd_i. The exterior factor
\(\eta_u(d_0)^m\prod_i\eta_u(d_i)\) is bounded by one and retains every zero. In particular, when 6 divides m the common-factor character is the principal mask at its modulus; it is not an everywhere-one factor.

The ordinary-subset-gcd variant correctly leaves the outside inverse factors independent. For a full common gcd, it requires that the residual common gcd be one; it does not accidentally impose pairwise coprimality.

## 3. Sharp common-factor tests and the tail theorem

The sharp c-dyad is not Mellin-inverted. On \(L\leq Nc<2L\), the original smooth weights are inverted in their smooth norm variables, producing the bounded c-test

\[
\mathbf1_{[1,2)}(t)t^{-i\sum s_i}.
\]

The classical sieve accepts this test without a differentiability assumption. The residual tests have finite seminorms polynomial in the Mellin variables, and the original smooth transforms decay rapidly enough to integrate those costs. Thus there is no unproved sharp inverse test in Theorem 4.1.

After applying the correction, the residual product is bounded by
\(\mathcal P^bL^{-mb}\). The three cubic/sextic common-factor row-norm weights are
\(L^{1/2},L,L^{5/6}\), yielding correction weights
\(\alpha=1/2,1,5/6\). Each satisfies Lemma 3.1 at b>1/2. The quadratic and principal-mask variants give exactly the stated two-term and one-term analogues.

Every resulting dyadic power is strictly decreasing because mb>1. Minkowski over the sharp tail is therefore a geometric sum. I independently recovered the three target conditions in (4.8), with denominators
\(2mb-1\), \(2mb-2\), and \(6mb-5\).

The fourth-moment specialization gives
\[
\frac35,\qquad 1-\frac{4h}{9},\qquad \frac{9-2h}{11}
\]
at b=7/8. The last is the largest on \(1<h\leq11/10\). The comparison with the earlier \((6-h)/7\) cutoff and the decrease \(3(1+h)/77\) are correct.

For m=3, the classical quadratic cutoff is
\[
\max\left\{\frac9{17},\frac{9-2h}{13}\right\}.
\]
The companion square-part interpolation gives the sharper term
\(H^{1/2}L^{1+b}\). Using it on the sharp c-test requires precisely the interval-test hypothesis identified in the note. Its new correction weight is \((1+b)/2\), and the resulting cutoff is
\[
\max\left\{\frac9{17},\frac{18-4h}{27}\right\}.
\]
The stated switch \(h\geq63/68\), and hence \(9/17\) on the displayed range, check exactly.

## 4. The mixed-sign correction and two-axis selection

For free incidence variables, let \(s_j=(-1)^{m_j}\). Their independent local product is \(\prod_j(1+s_jz_j)\), and the pairwise-disjoint numerator is \(1+\sum_js_jz_j\). With \(w_j=-s_jz_j\), the correction becomes

\[
\frac{1-\sum_jw_j}{\prod_j(1-w_j)}.
\]

A nonconstant monomial with support J has coefficient \(1-|J|\), up to the fixed sign substitution. Its absolute coefficient is therefore \(|1-|J||\), with every one-axis term zero. At a frozen-mask prime the absolute coefficients are one. This proves the exact mixed positive/inverse structure in Lemma 6.1, including prime powers in the correction.

At critical weights \(\alpha_j\geq1/2\), shifting all weights by a fixed \(\delta>0\) makes the unmasked error \(O(q^{-1-2\delta})\). The frozen-mask product is subpower in its actual norm, and returning to the original weights costs only the finite polynomial horizon raised to \(\delta\). This is a legitimate finite-horizon bound. It does not assert absolute convergence at a divergent critical endpoint.

The row Cauchy step uses exactly two selected axes, or later two selected products. The other free odd axes retain their signed inverse coefficients and use PW_b^sm. Frozen even axes are counted only after their bounded row factors and their common mask have been retained. Each monomial in a selected square-mean cost supplies a column weight at least 1/2, so the critical correction applies.

Choosing a minimum of costs at the original scales is valid: the proof then uses that selected analytic bound uniformly at every smaller scale. It does not require the same branch to remain the minimizing one after each shift.

## 5. Entire cubic products and grouped axes

I reconstructed Lemma 6.3 independently. For a product of j cubic columns with the same row exponent modulo six, freeze its exact shared-prime incidence labels. The residual singleton columns are pairwise coprime, so their product is squarefree and has scale

\[
P_{\mathbf c}=P\prod_{|I|\geq2}(Nc_I)^{-|I|}.
\]

The product-column coefficient energy is bounded by \(D^\epsilon P_{\mathbf c}\), by counting supported ordered tuples and their divisor-bounded representation multiplicity. Original coefficients need not be multiplicative: after freezing shared labels, their dependence on each residual column is still a bounded row-independent coefficient.

The exterior character at a shared prime has its literal zero even when its cubic exponent becomes principal. The all-row cubic sieve therefore gives the three row-norm terms with powers
\(P_{\mathbf c}^{1/2}\), \(P_{\mathbf c}\), \(P_{\mathbf c}^{5/6}\).
Minkowski assigns a multiplicity-m label weights \(m/2,m,5m/6\). Only m=2 in the first term is harmonic; its finite logarithm is harmless. Every other weight exceeds one. This proves the entire-product estimate without discarding its collisions.

In Corollary 6.4, the correction first makes the two cubic groups independent. Their internal collisions are then handled by Lemma 6.3. This order is sound: the original incidence variables remain pairwise coprime when the exact correction is reassembled, even though the independent products used in the estimate allow collisions. Every member of a group receives one of the admissible weights \(1/2,1,5/6\), so the critical correction still sums.

The requirement that each group have one common nonprincipal cubic exponent modulo six is essential and is correctly stated. Different finite column twists are harmless because the cubic sieve accepts them in its coefficient vectors.

## 6. Double triangles, comparisons, and higher-order embedding

The six same-side pair variables of size R give six singleton scales
\(X=D/R^2\). Two individual cubic axes give
\(HR^5X^{6b}\), with threshold \(r\geq9/22\) at b=7/8.

Grouping all three pairs on each side gives
\[
HX^{6b}\{R^3+H^{-2/3}R^6+H^{-1/3}R^5\}.
\]
I independently recovered the three thresholds
\[
\frac3{10},\qquad \frac12-\frac{4h}{27},
\qquad\frac{27-4h}{66},
\]
their crossing \(h=27/26\), and the value \(r=19/55\) at \(h=21/20\).

The comparisons use the same complete incidence configuration. The earlier two-singleton selector gives \(HR^6X^{1+4b}\), and the earlier full-subset selector requires \(r\geq1/2-h/12\). The differences \(3/880\) for the individual-pair improvement and \(59/880\) for the grouped improvement at h=21/20 are correct.

The conductor bookkeeping is also correct:
\[
Ng_1\sqrt{Ng_2}=X^6R^3=D^{6-9r}.
\]
For the displayed growing blocks, this is on the large-conductor side, and there is no triple or higher incidence and no cross-side shared prime. Hence this is a genuine additional signed sector, not a reclassification of the nontrivial common-triple tail.

The higher-order embedding freezes one principal matched cross pair for each extra unbarred/barred position. It costs \(D^{k-3}\) and preserves the additional row masks and free-axis exclusions. The same active six-position estimate then reaches \(HD^k\) for the specified portion of each fixed \(2k\)-th moment. This is correctly distinguished from full-moment coverage.

## 7. Computation and limits of this review

This was a mathematical reconstruction and source/hash inspection. I did not run a moment-data experiment or an independent moment checker for this review. My separately recorded replay of the theta diagnostic concerns a different theorem and supplies no analytic validation here.

The numerical fractions above were reconstructed from the displayed symbolic inequalities; no empirical estimates of sieve constants or L-functions were used. The fully singleton block and its signed large-conductor average remain unestimated beyond the stated earlier bounds. The frozen note preserves these limitations and does not implicitly assume the missing generalized hierarchy.
