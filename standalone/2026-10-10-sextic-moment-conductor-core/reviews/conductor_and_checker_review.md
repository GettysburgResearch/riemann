# Independent review: conductor sectors, interaction graph, and finite checker

Reviewer: replica/extraction subagent, 2026-10-10.

## Frozen sources reviewed

| File | SHA-256 |
|---|---|
| CONDUCTOR_SECTORS.md | c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983 |
| INTERACTION_GRAPH.md | 46ac022dcbeee727689d1f2bc247ec22eae54850dd7e010ff2de35d42e1405c5 |
| checks/check_local_structure.py | 76cc2e5147175829804820a632fb4cd60a633c1510d784dd483294d1ad95970d |
| Reproduced checker JSON | 6fabde7e386feca8fdd143a2fff4a0a065cb5fe41d6cbe355aab31b30a457f92 |

All source paths are under the new 2026-10-10-sextic-moment-conductor-core packet. This review did not edit repository files. The reviewer also checked the imported October 5 equation labelled eq:crt-a, which states \(a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4\) for coprime squarefree inputs.

## Verdict

**PASS at the stated component scope.** No blocking error was found in these exact source bytes. The explicit nonprincipal restriction in Section 7 is necessary and is present. The note proves bounded contributions from the named portions of a smooth Hermitian expansion, and a larger no-singleton portion with either smooth or sharp rows. It does not prove the remaining signed moment estimate or any new zero-free boundary.

## Mathematical review

1. The residual conductor decomposition correctly retains the nonunit zero at a prime whose signed multiplicity is a multiple of six. Every local nontrivial character is primitive modulo that prime, so the stated primitive conductor is the squarefree product of nonzero residual classes.

2. The completion estimate is uniform in every positive scale. After Poisson summation, the zero Fourier frequency vanishes only for a nonprincipal primitive character. The primitive Gauss bound gives the factor \(T/\sqrt{Nf}\); the planar dual sum is \(O(Nf/T)\), including \(T/Nf<1\), yielding \(O(\sqrt{Nf})\). The radial smoothing assumption correctly removes rotations during the principal-mask inclusion-exclusion. No unjustified sharp-cutoff completion is used.

3. The tuple counts use only the finite incidence patterns and the inequality \(\prod_p(Np)^{m_p}\le(bD)^{2k}\). The allocation count is \(D^\epsilon\) for each fixed order, including the additional mask-divisor weight. The fixed-conductor factor \((Nf)^{-1/2}\) cancels the completion factor exactly.

4. The residual-type minimum loads \((1,2,3,2,1)\) are correct. The corresponding dyadic summation produces powers \(1,1/2,0,1/2,1\), in the ordering of the five residual classes. The refined actual-multiplicity cost \(G_m^{(3-m)/2}\) correctly has only singleton and double power losses, a logarithm at multiplicity three, and convergent sums thereafter.

5. In Theorem 7.1, both \(HD^{k+\epsilon}\sqrt L\) and \(D^{k+\epsilon}L\sqrt C\) apply to the same nonprincipal positive accounting quantity. The first uses only trivial row counting, so it also applies to sharp rows. The second requires completion and is stated only for the smooth majorant. Taking their minimum is legitimate. Principal tuples cannot be inserted into this estimate; they are explicitly routed to Section 8.

6. The no-singleton tuple count \(O(D^{k+\epsilon})\) follows from \(Nq\le(bD)^k\), independently of whether the residual character is principal. It is therefore a valid enlargement of the earlier diagonal count.

7. The Möbius identity \(\prod_i\mu(n_i)\prod_i\mu(m_i)=\mu(f_1f_3f_5)\) follows from \(r+s\equiv r-s\pmod2\). The qualifications on the remaining finite-order character phases are appropriate. Factoring this sign from a tuple coefficient does not make its completed row sum positive; the note does not use that invalid inference.

8. The controlled set and its complement are disjoint after the stated union convention. The complement is closed under left/right interchange, so its signed contribution is real. The full nonnegative smooth moment is bounded by the remainder plus the proved error. The requested sharp moment is dominated only after the full smooth moment has been formed, not after selecting a signed sector.

9. The all-pairs Gauss interaction follows by induction from the checked source multiplicativity formula. The two displayed prime generators have norms 7 and 13, are coprime and primary modulo 3, and give the nontrivial cubic edge claimed. The root-coordinate reflections preserve \(3I-\mathbf1\mathbf1^\mathsf T\), and the displayed nonzero nilpotent translation proves an infinite orbit from three axes onward. The graph note correctly does not infer a global multiple Dirichlet series or a new analytic moment estimate from this algebra.

## Checker review and reproduction

The reviewer read the full checker and ran it independently with ordinary Python and Python -O. Both executions passed all 222,127 explicit predicates; their output files are byte-identical to each other and to the packet's recorded JSON.

The finite-field routines consistently use \(a+b\omega\), with \(\omega^2+\omega+1=0\), while the exact output-root arithmetic uses the basis \(1,\zeta_6\), with \(\zeta_6^2=\zeta_6-1\). The listed unit maps connect these conventions correctly. Full multiplicativity was checked on every pair of elements in the five displayed residue fields, including the inert norm-25 field.

The norm-ball bounds contain every allowed Eisenstein element. Column recursion enumerates squarefree ideals, including products of the two distinct primes above a split rational prime. Local zero exponents are handled as absent factors, while nonempty principal residual factors retain their zero mask.

The reconstructed region predicate uses \((Ng_1)^2Ng_2\le H^2\), an exact integer version of \((Ng_1)\sqrt{Ng_2}\le H\). Every region is invariant under left/right exchange. The five complete sharp-row moments reproduce exactly as 444, 7314, 33534, 1452, and 93054.

These computations authenticate finite algebra and the specified small sharp-row experiments. They do not authenticate an asymptotic smooth completion estimate, the native Möbius cancellation in the remainder, any arbitrary order not covered by the written proof, a Hecke functional equation, or RH.

## Corrections and limitations

No source correction is required for the reviewed bytes. The original omission of a nonprincipal qualifier, mentioned in the parent review request, is repaired in the source actually reviewed.

This review does not cover A2_COMPLETION.md or the replica/extraction note written by this reviewer. Those require separate review to avoid self-approval.
