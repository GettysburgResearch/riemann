# Scoped independent review of the compact-height lemmas

Status: **ACCEPTED AT STATED PROPOSED SCOPE by the arithmetic-wave agent**;
this is an internal cross-review, not integration or an actual-xi source
certification.

Reviewed on October 10, 2026, from resident bytes:

| File | SHA-256 |
|---|---|
| `heights/DENOMINATOR_FRAME.md` | `3d21423e56268e660e4daddd70b26839f778260d7cd6d323cfc73212fad1ba58` |
| `heights/NEGATIVE_FEATURES.md` | `815ddf88401bd4dae4c363975f10d889f600013becdffb136037f1f958289b96` |

The declared conclusion is finite-order PSD on an entire compact positive
node interval, and PD for distinct nodes, conditional on the complete
source, selected critical-anchor existence, strip/height/counting inputs,
and the stated exact sufficient inequality. No all-order, cofinal,
unbounded-axis, or RH conclusion has been reviewed or inferred.

For the denominator frame, the exact feature scaling `2/S^2`, the placement
of the `R_j,1` coefficient metric, the Lagrange-evaluation inverse of the
even/odd polynomial blocks, and the trace bound (D4) are correct. The
Newton inverse consists of the coefficients of the prefix Newton
polynomials, giving (D5). Combining reciprocal-trace and inverse-Frobenius
bounds gives (D6). Arbitrarily close nodes do not introduce a lost
Vandermonde factor in this preconditioned inequality.

The normalized Leibniz and mixed divided-difference bounds (D7)--(D9)
correctly retain `beta=2S/H`; they do not require `H>=2S`. The error bound
is for the complete signed discrepancy from a positive shadow. Smaller
packets use principal restrictions, and repeated evaluation nodes use the
coefficient-summing pullback. Repeated evaluations are not confused with
derivative observations.

For the negative-feature improvement, I independently expanded the exact
quartet numerator with SymPy and obtained the two coefficient blocks
displayed in (N1). Completing the even and odd squares gives exactly the
two negative coefficients `4m h` and `4m h/c`; the positive terms are
actual PSD rank-one kernels. Four reciprocal pole factors give the weak
composition coefficient `binom(k+3,3)` in (N2). The derivative product rules
for the `Su` and `S^2u^2` prefactors give precisely (N3)--(N5).

The first negative term has norm bound
`16m a^2 S^2 V/b^6`; the second has bound
`16m a^2 S^4 W/(zeta b^8)`, where
`zeta=1-A^2/H^2`. Thus (N6) has the correct factors and height powers.
Partial summation of the complete count yields (N8), so the leading
negative-only tail is `H^-5`, while the prior absolute shadow tail was
`H^-3`. I independently checked the rational coefficients `951/25` and
`1772/49` in (N9). Positive-square convergence follows from the stated
`O(m/b^2)` and `O(m X^2/b^4)` bounds and the complete counting input.

No defect was found in these stated scopes. Application still requires
the actual sufficient inequality at the claimed packet size and range,
certified selected critical pairs, and binding to the imported finite-height
and all-height-counting sources. I did not reverify the high-height zero
computation or independently prove the external quasi-RH strip.

Earlier cross-review of `heights/PROOF.md` also checked the signed-shadow
second-difference constant, mixed derivative normalization, determinant
and trace bound, and the synthetic order-four obstruction. Exact arithmetic
reproduced its D0/D1 values, all fourteen positive proper principal minors,
and the negative full determinant. This earlier review did not certify an
actual xi counterexample.
