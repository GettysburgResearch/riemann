# Independent review of the quartic all-row estimate

23 October 2026. Reviewed file: `../two-hour-type-20261023/QUARTIC_ALL_ROW_SIEVE_AND_TAIL.md`, SHA256 `75368f2947be9c7f33877f13305faf7a3c7fe85d83e64019787d192b66eb906d`.

I independently read Q1--Q13 and the primary Blomer--Goldmakher--Louvel Theorem 1.3, https://arxiv.org/pdf/1112.1650, pp. 3--4 (PDF page 4). The latter has precisely the squarefree/squarefree bound used in Q1 for n=4. This receipt does not reprove that imported theorem or audit every inherited quartic Gauss convention.

No defect found in the following deductions:

* At fixed fourth-power part d, the disjoint squarefree triple (a,b,c) is uniquely determined by its good primitive conductor abc and local character digits 1,2,3. Fixed reciprocity classes introduce bounded multiplicity. The d factor is the literal common column mask, including shared primes.
* The complete primitive family can therefore bound the same dyad as the quartic sieve. In Q7, `min(MBC,(ABC)^2) <= (MBC)^(2/3)(ABC)^(2/3) <= (X_d M)^(2/3)`. Its extra M term is retained. Summing the unique d decomposition gives the stated `M X^(1/4)` term, rather than a squarefree-row estimate masquerading as an all-row estimate.
* The powerful-modulus expansion has only divisor-many supported branches at each nonzero physical row. Rowwise Cauchy therefore costs a subpower. The three required radical Euler masses have leading exponents 2, 3, and 13/4; their tails are respectively R^-1, R^-2, and R^-9/4. All local branches in the displayed table have the claimed or stronger decay.
* Substitution of K=D^2/H into the full cross-term Cauchy calculation gives exactly Q12. The third cutoff inequality is weaker than the first two for 0<alpha<=1. At alpha=14/15 the maximum is r=2/9. The additional tail square is smaller in this regime and is not omitted.

The improvement is a genuine upper bound for an exact omitted squarefree-sieve tail, subject to its stated analytic imports. It does not establish the separate full-vector row-scale premise or the centered low-divisor estimate in Section 4. Consequently this review supports no smaller zero-free boundary.
