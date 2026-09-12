# Frozen sources and reading boundaries

Date: 2026-09-12. Repository: `GettysburgResearch/riemann`.

## Native source used

PR #876, head `8002444ec4d4bd1c6f8fa073820bcc575cb218e1`:
`standalone/2026-09-12-beta-fixedpoint-homotopy/PROOF.md`, blob `bb82833e204abb8a69a7602642b3d0cb4e7b7024`.

The principal construction, source ordering, full positive response, Mellin normalization, endpoint argument, uniform zero-tail proof, and open collision sign were read via the connected GitHub tool. This packet retains its exact source, rederives the state-space estimates it needs, and adds the quantitative complex-parameter extension. Its positive response formula is explicitly attributed to #876. No predecessor checker was independently rerun.

## Related mathematical source sections read

PR #862, head `67d5d6a5f588642f4c451fe35d2369b5ddac9346`:
`standalone/2026-09-10-gamma-finite-defect/PROOF.md`, blob `738a6c1767fddcf4b8de408bc6b54b1a69ead47e`.
The source/convergence, weighted-defect limit, multiplicity distinction, Hankel-index argument and variance-flow obstruction were read. This concerns a DIFFERENT gamma approximation. None of its numerical claims or whole-plane cutoffs is imported into the new homotopy.

PR #869, head `6603f8b04f9a2d073123a328ac0298a498c93a96`:
`standalone/2026-09-12-three-route-completion/gamma/PROOF.md`, blob `202160d0310d2cc7d23af6574425c71d0a319ab3`.
The opening 155 lines, including the positive convolution path, its Bessel zero-safe anchor and beginning of the regularity argument, were read. Its PR description supplied the existing regularized Jensen/whole-tail strategy. The entire later analytic argument was NOT independently audited. This is motivation and method credit, not a numerical or analytic premise needed to prove the new weighted-space estimates.

Main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, tree `8bddd12122e8a772683c9ed0b37dbcb945036893`: README, STATUS, AGENTS and PROGRAMMES were read; the main ref/tree were freshly confirmed before publication. The active programme map informed the choice of a source-faithful zero-transport problem.

The current recent-PR search returned 35 updated descriptions, including #851, #864, #866-#875. In particular the permanent-window and unbounded-height tracking descriptions informed the decision not to mistake tracking to the actual xi divisor for confinement to the critical line. Those descriptions are reconnaissance, not an exhaustive audit or independent acceptance of their claims. No full historical ledger or whole-repository build was attempted.

## Classical inputs

- Biane, Pitman and Yor, *Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions*, arXiv:math/9912170. Abstract/metadata freshly read. The exact BPY normalization is taken from the displayed source derivation in #876; the complete external paper was not independently reviewed this pass.
- NIST DLMF 5.12, Euler beta integrals, particularly 5.12.1 and 5.12.3. Displayed formulas freshly read; used in the explicit contraction and Mellin bounds.
- NIST DLMF 5.9, gamma/digamma integral representations. Freshly consulted for the classical Binet remainder used in the inherited gamma endpoint argument.
- NIST DLMF 1.10, classical complex analysis. Freshly consulted. Banach contraction, local analytic roots, Jensen and the distributional identity `Lap log|f|=2pi sum mult(rho)delta_rho` are classical tools, not discoveries of this packet. The application to collisions is explained using contour power sums and finite monodromy in the proof.
- Konstantopoulos, Patie and Sarkar, arXiv:2211.16680v1, Theorem 23 and Section 4.1: freshly checked while considering whether the previously excluded complete-Bernstein route could be replaced by ordinary Bernstein membership. The general class does not imply real zeros. No theorem from this paper is used as a premise of BHF26.

No general novelty claim, independent analytic review, or formal verification is asserted.
