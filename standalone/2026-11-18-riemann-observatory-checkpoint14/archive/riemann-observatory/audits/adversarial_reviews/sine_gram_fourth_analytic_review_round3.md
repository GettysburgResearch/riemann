# Independent analytic reconstruction of the mapped SG309–SG310 claims

Reviewer: analytic_frontier.17November2026. This is supporting review evidence for the existing SG309/SG310 records, not a new theorem ID or novelty claim. The m3/m4 computation and spanning-tree argument were independently reconstructed before reading the stored moment-existence draft; the already mapped draft was then read and checked to avoid duplicate claims.

## SG310: first four values

The full independent proof and exact graph-table program are proposals/independent_campaigns/sine_gram_fourth_moment_round3.md and experiments/code/sine_gram_fourth_exact.py, with observed output sine_gram_fourth_exact.json. All fifteen set partitions and every determinant permutation were accounted for. The exact m4 contributions by number of distinct point indices are1,127/60,2/15,0, summing to13/4. The all-distinct integral reduces to11/10−3I and the Fourier overlap/diamond volume givesI=11/30. The same method givesm3=2, with an all-distinct triangle cancellation.

The finite-window normalization is per expected unit length, not a random1/N_R normalization. The factorial-moment formula uses ordered distinct tuples and no extra1/l!. Anchoring one point produces the exact range-span factor in[0,1]. For m<=4, absolute integrability follows directly from Young/Hölder for the simple3/4cycles and factored double-edge stars, allowing determinant expansion and dominated convergence without formal delta distributions. The separate semantic_skeptic independently obtained the same partition formula and used another one-dimensional overlap-volume calculation, recorded in sine_gram_fourth_moment_semantic_round3.md.

These validate the model moments, not prime/zeta trace moments. No full-law or arithmetic inference is supplied by matching a few rational values alone.

## SG309: general existence mechanism

Read the complete stored proof in proposals/independent_campaigns/sine_gram_moment_existence_round4.md. Its graph step agrees with the independent reconstruction: every closed-word quotient is connected Eulerian after loops are removed. Thus every nonloop edge can appear in some spanning tree and can be omitted from another; uniform spanning-tree marginals lie strictly between0and1. Parallel edges must remain distinguished, which the proof does.

Weighted Hölder assigns exponent1/theta_e>1, precisely where absolute sinc powers are integrable. The tree change of variables has determinant1 and factors the integral; no false assertion that sinc itself isL1 is used. The one-vertex case is separate. Hadamard's determinant bound and the anchored range factor then justify dominated convergence for every fixed partition. There is no growing-m uniformity assumption, no ergodic theorem and no almost-sure IDS claim.

The combination with the previously established factorial bounds gives full expected-law convergence by tightness, uniform integrability and Hamburger determinacy. The no-zero-atom conclusion retains the separately inspected Paley–Wiener interpolation input and its proof boundary. The reviewer found no issue in this scope. No new source/error classification or independent re-audit of that external interpolation theorem is asserted.
