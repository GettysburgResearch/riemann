# Independent review of the double residual reduction

Review date: 2026-10-10. Reviewer: research agent /root/audit_formalization, distinct from the author /root/map_existing_riemann. This is an AI-agent mathematical review, not human peer review or Lean verification.

**Verdict: PASS at the stated source-conditional reduction scope.** The exact polynomial selection, sharp-to-smooth step, positive sector accounting, signed remainder, constants, and complementary incidence witnesses are valid. The result strictly narrows the remaining tuple domain at every fixed order \(k\ge3\); it supplies no estimate for that remaining signed sum and no new full-moment exponent.

## Bound objects

| Object | Bytes | SHA-256 |
| --- | ---: | --- |
| DOUBLE_RESIDUAL_REDUCTION.md | 10943 | a5f7c8da63cc1367ca0678030a28cc289f0a7350bdbc9dd6e0743cbf0a093324 |
| PR 914 CONDUCTOR_SECTORS.md at 0cc0428fedbbfc340044c7451b3d392c1da9a103 | 24272 | c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983 |
| PR 915 ANISOTROPIC_SINGLETON_CORES.md at 9959364671f89b86f3992ec5ed5e19f804eb607b | 8894 | 4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8 |

The new note was read in full. Both source files were read from their exact Git objects and their content hashes verified. The relevant PR 914 conductor, smooth-completion, counting, and selected-sector proofs were checked for the hypotheses used here. The PR 915 anisotropic theorem had also been independently reviewed in the preceding packet. Its underlying imported inverse second-moment theorem is retained as an analytic input, not independently rebuilt in this pass.

## 1. The polynomial selector is the one the input actually controls

The quantity \(Q\) depends only on the shared incidence ideals \(c_I\), \(|I|\ge2\). Fixing those ideals fixes every \(X_i\) and therefore \(Q\). The selection does not cut an arbitrary subset out of a singleton-core polynomial: it includes or excludes the entire block. This is precisely the form covered by PR 915's aggregate anisotropic bound. The literal coefficients, row characters, exclusions and incidence multiplicities are unchanged.

The bound is uniform for all \(Q_0\ge1\). No polynomial upper bound on \(Q_0\) is needed: an excessively large threshold merely includes every nonempty block and makes the displayed upper bound weaker. Constants may depend on the fixed order, tests, bad-prime set, character and input parameters, but not the selected threshold. For \(b=1\), the only additional analytic input is the inherited native second moment. Using \(b<1\) requires the separately stated pointwise estimate uniform in the moving row and smaller column scale.

The distinction between a one-sided singleton and a singleton of the full Hermitian tuple is correctly maintained. The latter, and the nonprincipal double product, determine the PR 914 complexity; they cannot be replaced by one side's incidence ideals.

## 2. Positivity is used at a legal point

The exact split is \(A^k=G+R\). The inequality \(|G+R|^2\le2|G|^2+2|R|^2\) is applied on the original sharp row set. Only the full nonnegative squared norm of \(R\) is then majorized by the fixed nonnegative smooth test. This avoids an unjustified comparison between a selected signed sharp-row sector and its smooth counterpart.

After expansion, both side tuples satisfy \(Q>Q_0\). PR 914's relevant theorems bound sums of absolute completed tuple contributions, not merely the absolute value of a total signed sector. Their bounds therefore survive these extra tuple restrictions. The union of the no-singleton region and the nonprincipal region with complexity at most \(H\) has total absolute contribution \(O(HD^{k+\epsilon})\); overlapping tuples are counted only once in the exact decomposition. Every principal tuple belongs to the no-singleton part.

The complement is exactly the new remainder in (2.3). Side exchange conjugates each summand and preserves both \(Q\) restrictions, the singleton condition and the complexity condition. The remainder is consequently real. The error in (2.7) is bounded in absolute value independently of \(Q_0\), regardless of its sign.

Writing that error as \(E\), with \(|E|\le C HD^{k+\epsilon}\), makes the asserted constant structure explicit:
\[
M_{\mathrm{sharp}}
\le 2C_1HD^{k+\epsilon}Q_0^{2b-1}
   +2C HD^{k+\epsilon}+2\max(0,\mathcal T).
\]
Thus the coefficient two on the positive part of the remainder is legitimate; only the controlled terms need an unspecified fixed constant. The smooth residual norm also implies \(\mathcal T\ge-C HD^{k+\epsilon}\). No lower-bound hypothesis on the signed remainder is hidden.

The possible zero row is retained only in the smooth norm and causes no problem. The original row sum is over nonzero elements. PR 914's elementary \(O(H)\) lattice bound uses \(H\ge1\), as guaranteed by the scales under consideration.

## 3. Exponent bookkeeping and witnesses

For a chosen subpower threshold \(Q_0(D)\), the factor \(Q_0^{2b-1}\) is absorbed by reallocating an arbitrarily small positive exponent. For \(Q_0=D^q\), the proved contribution has exactly the additional exponent \((2b-1)q\). The primitive residual conductor used in the restricted block statement is explicitly defined. The bound for each restricted singleton/double block is inherited unchanged as a subset of the same positive accounting sum. The new restrictions have not silently improved that bound's power.

The final wording correctly says that each remaining \(Q\) exceeds the chosen subpower cutoff. It does not assert that \(Q\) itself must cease to be subpower. Growing \(Q_0(D)\) is explicitly used for the strictness examples so that all bounded support-dependent values of \(Q\) are eventually removed; the proposition itself also permits bounded \(Q_0\).

For \((a,c,c)\) and \((a',c',c')\), with the four ideals mutually coprime and of norm comparable to \(D\), both one-sided values of \(Q\) are bounded. The full singleton norm is comparable to \(D^2\), the nonprincipal double norm to \(D^2\), and the complexity to \(D^3\). For \(k>3\), repeating \(c,c'\) another fixed number of times keeps \(Q\) bounded and the full singleton norm comparable to \(D^2\). The repeated residual classes may become principal, but this does not affect the singleton condition. The claimed strict removal therefore holds at every fixed \(k\ge3\) for \(0<\theta<1\).

For the converse witness \((pa,pb,c)\), \((qa,qb,c)\), the one-sided values are \(Q\asymp D^{2-2\eta}\), while every full-tuple prime occurs at least twice. Appending the same new ideal \(r\asymp D\), coprime to the original five ideals, on both sides extends this to higher orders: at \(k=4\), \(Q\asymp D^{3-2\eta}\); at \(k\ge5\), \(Q\asymp D^{2-2\eta}\), up to fixed support constants. The full tuple still has no singleton prime. Thus the conductor reduction controls patterns not removed by the one-sided subpower cutoff at every fixed \(k\ge3\).

These are feasible incidence configurations within a nontrivial test's fixed support annulus; they are not lower bounds for their signed sums. The fourth-moment qualification is also correct: its equal one-sided scales leave only a short balanced periphery, so the combination does not prove a new fourth-moment range.

## 4. Scope retained

The proof produces a new intersection of two unresolved domains and a sufficient signed estimate on that intersection. It does not estimate that signed quantity, eliminate its arithmetic correlations, or justify replacing it by an unsigned energy. The full moment hierarchy, a new zero-free boundary and RH remain unproved.

No numerical theorem test, finite-field replay or Lean build was needed or claimed for this composition. This review does not extend to the rest of PR 914, and it does not turn the separately audited signed first-Poisson diagonal identity into a bound for the new Hermitian remainder.
