# Claims, assumptions, and smallest failure points

Status: proposed mathematics on a research branch. No integrated result
is replaced, and RH remains unproved. The baseline is PR #1009 at
`7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0`.

| ID | Exact claim | Load-bearing assumptions / smallest failure point |
|---|---|---|
| BI26-CUBIC | For each fixed nonzero angular degree, the completed cubic row mean is \(R^{1+\epsilon}(1+|t|)^C\) on \(1/2<\sigma<3/4\); hence the bilinear form in average/ANGULAR_SELF_ABSORPTION.md is \(A^{1/2}B(AB)^\epsilon\). | DR's theta coefficients and reflection, the unconditional cubic large sieve, the exact eight-component Mellin closure (four profiles for each angular sign), and the finite-cutoff absorption. |
| BI26-ANGULAR-UNIFORM | The stronger explicit mean in type_i/ANGULAR_UNIFORMITY.md has angular/height factor \((1+|\ell|+|t|)^{2-4\delta+\epsilon}\); its smooth angular localization has error \(A^{1/2}B\Delta^{-1-\epsilon}(AB)^\epsilon\). | Uniform finite profile conversion and gamma quotient, an independently bounded initial supremum, and simultaneous row/angular absorption. This does not remove moving quadratic conductor costs. |
| BI26-HYBRID-ANGULAR | The three-term means H2 and H17 of type_i/HYBRID_ANGULAR_MEAN.md give the balanced smooth-sector exponent \((\sqrt{73}-1)/48\), with exact zero-mode subtraction. | The same theta and sieve inputs, uniform initial growth, and weighted divisor absorption. The enlarged middle row exponent needs its positive epsilon gap. This is a free-column Gauss form, not prime counting or a zero-free improvement. |
| BI26-HYBRID-RATIOS | The piecewise function g(a) in global/HYBRID_SECTOR_OPTIMIZATION.md is the optimal width exponent within the three displayed positive-displacement hybrid constraints. | Algebraic consequence of the reviewed hybrid means, with fixed length ratio and a positive width buffer. The normalization changes at displacement 1/6; no uniform a=0 endpoint is asserted. |
| BI26-CONDITIONAL-HYBRID | Under the actual-family common boundary, the minimum of CH5 in type_i/CONDITIONAL_HYBRID_SECTORS.md strictly improves g(a) for a>5/9. | Exact reflected hybrid mean, p>(2 beta+1)/6, uniform reciprocal for the actual cube factor, and exact zero-mode subtraction. This does not improve the assumed boundary. |
| BI26-DUAL | The full signed divisor resummation in type_i/DUAL_RESUMMATION.md restores the omitted cube Euler factors. | The literal natural zeros and the complete signed Ramanujan sum; first-power truncation is not licensed. |
| BI26-QUADRATIC | The closed quadratic/sextic pair has the mean and bilinear bounds Q4--Q13 of mixed/QUADRATIC_PAIR_ABSORPTION.md, with its explicit moving-conductor costs. | The primitive two-partner Fourier transform and conductor factor; dropping either changes the result. |
| BI26-OPPOSITE-CUBIC | The two-conductor cubic family in mixed/OPPOSITE_CUBIC_JOINT_MEAN.md satisfies OC4, with its explicit angular cost; at all conductor ratios it has natural-count size on Re s=2/3 and at equal lengths N yields the free-column N^(8/3+epsilon) consumer. | Positive cubic self-reflection, complete cube tails, de Faveri Proposition 8.1, and piecewise divisor closure for 0<delta<2/9. This is not the sextic detector family. |
| BI26-SPHERICAL | The same pair admits angular degree zero when its primitive squarefree quadratic conductor is nontrivial and prime to 6. | Componentwise annihilation of both Jacquet constants in every reflected partner; H=1 is excluded. |
| BI26-UNITARY | Every unitary Hecke character over every number field has no zero on \(\Re s>B_\flat\), with possible translated principal poles permitted. | Proposed fixed-type adapters from the preceding packet; new all-field spherical inverse terminal and physical auxiliary guard; Liu's complete inverse/product/direct/high arguments and continuous scalar certificates. This is a new source-dependent assembly, not a relabeling of the finite-order theorem. |
| BI26-UNIFORM | A common boundary beta for the actual unitary family implies conductor-uniform reciprocals, signed Mobius sums, and the signed dilation estimate (12). | Classical Hecke analytic continuation/functional equation and the explicitly stated common-family premise. The dilation estimate also requires both profile and Euler-derivative bounds. |
| BI26-SECTORS | Under the full-family premise, Eisenstein prime ideals satisfy the uniform arc estimate (4) in uniform/FULL_FAMILY_CONSEQUENCES.md; asymptotics hold for arc length at least \(x^{\beta-1+\delta}\). | Uniform logarithmic derivative derived from the common boundary, sharp Perron, and trigonometric arc approximation. The first angular harmonics must be included. |
| BI26-BARRIERS | The specified numerator hybrids and stated Type-I substitutions do not improve the supplied endpoint comparison. | Exact restricted-system algebra. These are not impossibility theorems for different analytic estimates. |
| BI26-TANGENT | The closing tangent scalar family is valid throughout the stated narrow kappa interval, with its continuous delta/x coverage and correct quartic endpoint branch. | Primitive formulas (14.3), (14.8), (14.10); exact polynomial identities, rational interval cover, and the readable completed-square argument. The analytic estimates and initial seven-eighths step remain source inputs. |
| BI26-SIGNED-GCD-TAIL | The unselected signed component in global/SIGNED_MOBIUS_GCD_TAIL.md has bound D^2 C^(-2) S^(beta-2), up to its stated subpowers and smooth seminorms. | Uniform Mobius cancellation for the actual finite-order cubic/ray family and norm translates, literal common-prime zeros, and the full shared smooth kernel. The short common-divisor sector is not bounded at the desired scale. |
| BI26-SIGNED-COMPLEMENT | The exact Euler product MC5 gives the smooth complementary-sum bound MC9 and the transformed-tail bound MC14. | Common zero-free half-plane for the actual angular and finite characters, nonzero angular order, full deleted Euler factors, and the prescribed Mobius coefficient. The full-divisor term remains. |
| BI26-CONDITIONAL-SECTORS | The free-column smooth discrepancy in type_i/CONDITIONAL_ANGULAR_SECTORS.md has width exponent xi_beta(a), improving a/4 for a>2/3. | Reflected uniform cubic mean and uniform reciprocals for the actual angular cube factors. The zero-angular term is subtracted exactly; this is not a prime-sector theorem. |

The unchanged endpoint is the root in (0.87488, 0.87489) of

\[
133488B^4-376596B^3+384534B^2-167541B+26231=0.
\]

The proposed full-family theorem extends the covered characters. It does
not lower the numerical finite-order or zeta boundary. The pure cubic
bilinear improvement is strict, but its free smooth variable and fixed
angular profile cannot be exchanged for a selected prime polynomial.

The source table, local Fourier identities, exponent identities and
negative controls have finite exact checkers. None of those checkers
certifies the upstream analytic theorems or their infinite quantifiers.
Any numerical probe is separately labeled exploration and is excluded
from the exact acceptance replay.
