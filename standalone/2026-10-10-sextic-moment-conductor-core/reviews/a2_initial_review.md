# Independent scoped review: A2 completion, interaction graph, and exact checker

Reviewer: the independent `moment_structure_attack` agent. Date: 2026-10-10.

## Verdict

**PASS at the stated arithmetic and conditional-transfer scope.** I found no mathematical defect in the frozen A2 five-label coefficient formula, forward completion, signed inverse, normalized norm transfer, or the all-scale envelope deduction. I also checked the complete interaction graph and its reflection calculation, and independently ran the frozen local checker with optimization enabled.

This verdict does not establish an analytic reflection theorem for the moving twists, the required completed mean square, the fourth moment, the generalized moment hierarchy, 17/24, or RH. These remain expressly outside the reviewed claims. There were no requested repairs to the reviewed files, and I did not edit the repository.

## 1. Exact reviewed objects

The following source bytes were frozen into scratch snapshots before the independent execution, and their hashes were checked again afterward. All three sources were unchanged during this review.

| Object | SHA-256 |
|---|---|
| `balanced_core_attack.md` | `615cde5ed5ff01a273b3b5d2882571c3810af395dfe8fbf51b17232de4b735c1` |
| `INTERACTION_GRAPH.md` | `46ac022dcbeee727689d1f2bc247ec22eae54850dd7e010ff2de35d42e1405c5` |
| `checks/check_local_structure.py` | `76cc2e5147175829804820a632fb4cd60a633c1510d784dd483294d1ad95970d` |

The full source paths, snapshot paths, byte counts and hashes are recorded in `moment_structure_independent_review_manifest.json`. The review applies to these byte identities. A later edit requires a review of the affected change; copying the same bytes into the proposed packet does not change the content verdict.

## 2. Primary-source check

I independently opened the [author-hosted Brubaker–Bump–Chinta–Friedberg–Hoffstein paper](https://chinta.ccny.cuny.edu/publ/wmd1.pdf). I checked its table (13), rigorous twisted multiplicativity (20), the statement directly following (20) that defines the prime-power coefficients by (13), and Theorem 2 / equation (25). Thus the A2 comparison is anchored to the rigorous coefficient definition, not only the paper's opening heuristic.

I also read the imported October 5 `paper2.tex` arithmetic definitions and `eq:crt-a` at the pinned OpenAI source. They give the exact unitary factor lambda and the squarefree Gauss multiplication law used by the draft.

The primary paper's stated continuation theorem has its own local-data space. The reviewed draft correctly leaves the moving conductor, infinity type, and quantitative mean-square adapters open. No larger analytic scope was inferred from the coefficient match.

## 3. A2 coefficient and five-label formula

### Claims checked: (1.1), (2.1)–(2.2), and Proposition 3.1

For coprime primary generators, squaring the stated sextic reciprocity sign removes it. The cubic interaction is therefore exact. In the rigorous A2 twisted product, all four cross-prime exponent coefficients become 2 modulo 3: the two negative edge exponents are also 2 modulo 3. This gives

\[
\kappa_{m_1m_2}(n_1n_2)^2
\]

as claimed in (3.3).

I independently checked the local normalization. The prime-square Gauss sum satisfies

\[
g_3(p,p^2)=q\,g_{\kappa_p^2}(1,p),
\quad
g_{\kappa_p}(1,p)g_{\kappa_p^2}(1,p)=q,
\]

using the same additive character and kappa_p(-1) = 1. The correction patterns (1,2) and (2,1) consequently have normalized magnitude sqrt(q), not one; pattern (2,2) has coefficient sqrt(q) lambda(p)^3 a_xi(p). These agree with (2.2).

The five nonunit support patterns give a unique assignment of every prime to a,b,c,d,e. The c,d labels have total exponent 3 and hence no cross-prime cubic interaction. The e label has total exponent 4, congruent to 1 modulo 3, so it interacts exactly like one squarefree Gauss factor. This proves the global formula

\[
\mathfrak a_\xi(acd^2e^2,bc^2de^2)
=\sqrt{N(cde)}\lambda(cde)^3a_\xi(abe).
\]

The proof uses twisted multiplication; it does not assume an ordinary Euler product for the completed series.

## 4. Forward completion and signed inverse

### Claims checked: Theorem 4.1, especially (4.5)–(4.7)

The total column ideal is ab e C^3. Its row symbol and auxiliary fourth power produce exactly the phases in Omega. In particular, chi_C(f)^12 retains the mask (C,f) = 1. The remaining cross phase between e and ab is precisely absorbed by updating the auxiliary ideal from f to ef.

The signed inverse is valid because the child mask q0 C prohibits a correction prime from appearing in two stages. For two disjoint correction triples, the only nontrivial composition check is the e_1,e_2 Gauss interaction. The auxiliary update supplies chi_{e_2}(e_1)^4, exactly the factor needed to replace a_xi(e_1)a_xi(e_2) by a_xi(e_1e_2). Every global correction set therefore has the same amplitude for every choice of its outer-stage subset. Summing the signs gives (1-1)^omega(C), as stated.

This argument remains valid when the row is divisible by a correction prime: the literal row phase is zero on both sides. Finiteness follows from the fixed compact factor rectangle, so no infinite rearrangement is involved.

**Essential domain boundary, correctly respected in the draft:** the new auxiliary ideal ef shares e with the new exclusion q0 C. The polynomial and energy definitions permit this overlap. A future analytic theorem which requires the auxiliary and exclusion ideals to be coprime would not satisfy the transfer hypothesis without a further adapter. This is not a present defect, but it must remain explicit when the norm transfer is used.

## 5. Normalization and the all-scale envelope

### Claims checked: Theorem 5.1 and Corollaries 5.2–5.3

The child scales give

\[
A'B'=AB/(Nc^3Nd^3Ne^4),\qquad
F'=FNe,\qquad
\Sigma'=\Sigma/(NC)^3.
\]

The injection f -> ef sends the original annulus into the stated child annulus. Enlarging the sum occurs only after taking a nonnegative square norm. Its exact normalized scalar cost is

\[
\sqrt{NC}\sqrt{\Sigma'/\Sigma}=1/(NC).
\]

The same cost applies to the inverse because its Möbius sign has modulus one. Summing three harmonic label factors gives the displayed logarithmic cube at the norm level, hence a sixth power in the energy.

For the all-scale envelope, the Hcal term has the same three harmonic factors. The Sigma' term instead has the absolutely summable weight (NC)^(-5/2). Squaring gives precisely

\[
M\{\mathcal H\log^6(2Z)+\Sigma\}.
\]

The fixed-auxiliary version has scalar cost 1/(Nc Nd Ne^(3/2)), so only c,d have harmonic sums. This normalization is also correct.

The corollary assumes an analytic estimate on a domain closed under all displayed child maps. The draft explicitly recognizes that a positive-gap condition alone is not closed: Hcal stays fixed while Sigma decreases. I found no circular use of the unknown all-scale bound.

## 6. Interaction graph

### Claims checked: Propositions 1.1, 2.1 and 3.1

Induction from the exact two-factor Gauss formula supplies an edge between every pair of axes. The displayed norm-7 and norm-13 prime generators are primary, have the claimed norms, and give a nontrivial inverse cubic symbol. Setting either axis to the unit ideal proves that this phase cannot be absorbed by independent nonzero axis weights.

The matrix C_k = 3I - 11^T has eigenvalue 3-k on the all-ones vector and eigenvalue 3 on its perpendicular space. Its reflections preserve the corresponding symmetric form. I independently checked the displayed three-axis product and nilpotent matrix. For higher k, the span of the first three coordinate vectors is invariant under the first three reflections, so the same infinite subgroup remains.

The manuscript correctly treats this as a statement about the proposed complete-graph reflection system. It does not infer the existence or continuation of a higher-rank Dirichlet series, or rule out a different representation.

## 7. Checker inspection and independent execution

I inspected the code before running the frozen snapshot with Python 3.12.14:

```text
python -O review_snapshot_check_local_structure.py \
  --output moment_structure_checker_review_result.json
```

The process exited 0 with `PASS`, and all **222,127** explicit predicates ran. Acceptance uses `require` and explicit exceptions, so `python -O` does not disable it.

I checked the two coordinate rings used in the program, the correspondence of its six roots, both split-prime residue maps, the inert-prime field arithmetic, squarefree ideal enumeration, the complete Eisenstein norm-ball bound, and the exact squared norm formula. The moment reconstruction uses an independent direct row evaluation and a Hermitian expansion grouped by prime-incidence counts. Its kernel key preserves a principal mask separately from an absent prime. The region decision squares the complexity inequality, so it is exact integer arithmetic rather than a floating-point comparison.

The five reconstructed moments were 444, 7,314, 33,534, 1,452 and 93,054 for the displayed parameter panels. All three regions were real under conjugation. The graph and finite-field checks also passed.

The result file SHA-256 is

```text
6fabde7e386feca8fdd143a2fff4a0a065cb5fe41d6cbe355aab31b30a457f92
```

This checker validates finite conductor, sign, mask, graph and literal moment bookkeeping. It does **not** numerically authenticate the smooth Poisson bound, the infinite tuple estimates, the A2 completion identities, or a higher-moment theorem. The A2 identities were reviewed mathematically above; their correctness is not being credited to a program that does not test them.

## 8. Final scope

No load-bearing defect was found in the exact objects listed in Section 1. The coefficient completion, inverse, and norm adapter are complete at their native arithmetic and conditional analytic scope. The moving-twist reflection, conductor-uniform estimates, high-complexity singleton cancellation, and full moment hierarchy remain open. This scoped approval must not be promoted to an approval of those missing claims.
