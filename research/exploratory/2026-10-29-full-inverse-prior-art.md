# Prior-art check: the averaged full-inverse obstruction

**Scope.** This note compares the conditional implication in [the full-inverse calculation](2026-10-29-cubic-full-inverse-mean/README.md) with sources found by targeted searches on 29 October 2026. It is not a comprehensive priority search, a verification of the full-inverse arithmetic estimate, or a claim of novelty. No cited paper below was found to state that precise implication.

## Classical analytic mechanism

Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut, [*On a Mertens-type conjecture for number fields*](https://arxiv.org/abs/2109.06665), Mathematical Proceedings of the Cambridge Philosophical Society 177 (2024), 481–523, study the ideal Möbius sum for a fixed number field K. In the [published full text](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/on-a-mertenstype-conjecture-for-number-fields/B01C7628DF4D57CAE8410901FD6A9321), Proposition 2.6 obtains two-sided Ω-results from nonreal zeros with real part beyond the real-zero obstruction. Propositions 2.7–2.8 treat further cases after subtracting explicit real-zero contributions, and Theorem 2.10 links bounded normalized ideal Möbius sums to RH and simple zeros. Their Dirichlet-series/Mellin connection is the base-field version of the familiar implication from square-root Möbius cancellation to zero-freeness. These results are for an **individual unsmoothed base-field Mertens function**; they do not state the squarefree cubic family average below. In particular the basic principle that a pole of 1/ζ_K prevents an appropriately strong bound is established mathematics and should not be presented as new.

## Cubic inverse-family precedent

Peng Gao and Liangyi Zhao, [*Ratios conjecture of cubic L-functions of prime moduli*](https://arxiv.org/abs/2311.08626), Indagationes Mathematicae 37 (2026), 1065–1083, [doi:10.1016/j.indag.2025.07.001](https://doi.org/10.1016/j.indag.2025.07.001), Theorem 1.3, prove under GRH an asymptotic negative first moment of **one individual cubic Hecke L-function** at 1/2+β, Re β>0, averaged over weighted prime primary moduli ϖ≡1 mod 9 in K=Q(ω). Their Theorem 1.1 concerns a single numerator/denominator ratio under GRH. Both are very close background for inverse-L family averages, but their averaged object and prime-only ordering differ from the proposed squarefree-row full inverse of ζ_L; the cited theorems do not furnish the displayed H_S product or its finite-length, second-moment implication. In particular, the fixed-prime ramification probability for prime rows tends to zero, unlike the squarefree row probability 1/(Np+1).

Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky, [*Non-vanishing for cubic Hecke L-functions*](https://arxiv.org/abs/2410.03048), study cubic residue characters indexed by squarefree q≡1 mod 9 over Q(ω), and establish a mollified second moment and nonvanishing results. This is a closer **squarefree family**, but the mollified quantity is an individual Hecke L-function with a chosen mollifier, not the entire reciprocal of ζ_K L(s,χ)L(s,barχ). Its second moment is therefore not an upper bound for the full inverse in the companion note.

For general background, Cho and Park, [*Low-lying zeros of cubic Dirichlet L-functions and the Ratios conjecture*](https://doi.org/10.1016/j.jmaa.2019.01.073), study a rational cubic Dirichlet family and compare a one-level density with the ratios prediction. This is neither the squarefree Eisenstein field-extension family nor an unconditional estimate of the proposed full inverse.

## What the calculation adds, conditional on its arithmetic input

At a fixed good prime p, write u=(Np)^(−s). The proposed squarefree family has asymptotic probabilities `P(p∤g)=Np/(Np+1)` and `E χ_g(p)=0`. Thus the local mean of the complete reciprocal Euler factor is

    (1−u) E[(1−χ_g(p)u)(1−barχ_g(p)u)]
      = (1−u)(1 + [Np/(Np+1)]u²).

This gives the local factor of H_S(s)/ζ_{K,S}(s); the second factor is holomorphic and nonzero in Re s>1/2 by absolute convergence. This local calculation is an elementary consequence of orthogonality and squarefree ramification density, not evidence of a priority claim. Passing from fixed primes to the moving-length average requires the uniform error in the companion note, which must be established independently of this literature comparison.

If that arithmetic estimate and its stated masks and sector hypotheses hold, a fixed test whose Mellin transform does not vanish at any off-critical zero turns a base zero β+iγ into a lower bound for the family mean along a sequence, and Cauchy–Schwarz yields the companion moment obstruction. The hypothesis is a bound for **one fixed full inverse** with all ε-losses, for all large X, at D=X^r with 0<r<1/2. It is not an assertion that such a bound holds. This is an RH-equivalence-style conditional obstruction for the chosen norm, not a new zero-free region. The full-inverse hypothesis is materially stronger than a moment bound for either isolated nonprincipal L-factor.

The search covered inverse cubic L-function and ratios papers, squarefree cubic mollified moments, and number-field Mertens Ω results. A directly identical result may exist under different terminology, or be implicit in an unexamined ratios calculation; no claim of first proof or novelty is justified by this search.
