# BGSTB arXiv v1 full reading

PAPER-A006. All 13 pages of arXiv:2306.04799v1 were substantively read on 17 November 2026. This is Level 1 for the preprint. The first theorem's external estimates and the Tsang and Bourgain antecedents were followed through their uses. Their original proofs were outside this check. The Acta Arithmetica abstract and bibliographic record agree on the claimed outcomes. The journal text is subscriber-restricted and its treatment of the issues below is unverified. ArXiv records the only submission on 7 June 2023. The inspected PDF's internal date is 9 June 2023 and its SHA-256 is 133071c4d85c875fe9b1a7d4001f22d7174270ab8f1fa8e6cee6178d20276ee9. [Preprint](https://arxiv.org/abs/2306.04799v1) · [Journal record](https://doi.org/10.4064/aa230612-20-3)

## Whole-work reading map

- **§1, pp. 1–2.** The unconditional form factor uses the actual complex difference and the weight 4/(4−u²). Theorem 1 asserts reality, evenness and positivity for all real Fourier parameters, with the stated asymptotic uniform on [0,1]. Theorems 2 and 3 concern simple zeros under the thin-box and strong zero-density assumptions respectively. The latter requires uniform little-o control at its moving endpoint.
- **§2, pp. 2–6.** Reflection ρ ↦ 1−conj(ρ) rewrites the sum in conjugated squared-norm form. Lemma 1 subtracts Landau formulas at σ and 1−σ to recover a complex Cauchy kernel. Lemma 2 imports Riemann–von Mangoldt, and Lemma 3 identifies the finite-zero square by contour shift and a two-pole integral. Lemma 4 compares it with the infinite explicit-formula square on [0,T]. The cutoff Z = T log²T costs O(x). The endpoint terms cost O(x^(1−2η(Z)) log³T), bounded by O(T) using Vinogradov–Korobov and splitting at x = √T. Theorem 1 then uses the Goldston–Montgomery prime-side mean square. Its used range is 1 ≤ x ≤ T. The line above (2.19) prints 0 ≤ x ≤ T, although the formula contains x^−2 and log x.
- **§3, pp. 6–7.** Compactly supported L¹ tests have entire Fourier transforms. The text preceding (3.2) omits compact support or exponential integrability in its general assertion for g ∈ L¹. For example, g(α) = 1/(1+α²) diverges after multiplication by exp(2πα) on the positive half-line at z=i. Lemma 5 explicitly requires compact support and its applications use that hypothesis. Its Laplace peak has mass r(0). The Lipschitz estimate gives Oᵣ(log log T / log T) with the specified split, below the uniform Oᵣ((log T)^−1/2) remainder.
- **§§4–5, pp. 7–8.** The kernel has Fourier transform j(2πt) sech(2πt), with Fejér and Montgomery–Taylor choices for j. Tsang's property is positivity of the real part in the open unit strip. Lemma 5 is applied to r(α) = j(α) sech α, giving r̂(z) = 2πK(−2πz). The equality w(u)−1 = u²w(u)/4 cancels the apparent singularity and permits weight removal from the thin-strip pair sum at O(T) cost via the unit-window zero count. The complement S(T) keeps its weight.
- **§6, pp. 9–10.** Charge the larger of T^|2β−1| and T^|2β′−1| to its own zero. That outer zero lies outside the thin box. Reflection reduces to right-side zeros. The printed inner-sum estimate (6.4) and partial summation require separate scrutiny below.
- **§7, pp. 11–13.** Once S(T) is negligible, positivity bounds the diagonal by the thin-strip sum. A zero of multiplicity m contributes m² to the ordered diagonal. The inequality m·1_(m=1) ≥ m(2−m) gives (7.2). Independent 45-digit quadrature gives Fejér and Montgomery–Taylor constants 0.608612928507349859 and 0.617483788131941009. The last printed decimals differ slightly and the quoted 60.8% and 61.7% are retained. The final pages contain references and metadata. [Preprint](https://arxiv.org/pdf/2306.04799v1)

## Scope of the local issue in §6

Set L = log T and fix an outer height γ. Equation (6.4) bounds the sum of [1+L²(γ−γ′)²]^−1 over γ′ by an integral against the smooth main density. The cited estimate N(t+1)−N(t) ≪ log(t+2) allows ⌊cL⌋ ordinates inside [γ,γ+1/L], each contributing at least 1/2. This also respects a Riemann–von Mangoldt count with O(log T) error. Start with the floor of the smooth main term near a large height and move the ordinates of one unit interval into a subinterval of length 1/L. The count changes by O(L), and the moved ordinates can be distinct. For γ one of these ordinates, the sum grows like L. This is a counterexample to the inference from the cited estimates. Actual zeta zeros are outside the scope of the counterexample.

The valid bound from unit shells is O(L). Let a = 1/2+1/(2L) and let N≥(u,T) count β ≥ u and 0 < γ ≤ T. The exact partial summation identity is

    ∑_{β≥a} T^(2β−1) = e N≥(a,T) + 2L ∫_a^1 N≥(u,T) T^(2u−1) du.

The v1 display on p. 10 has the opposite sign on the integral and a different endpoint exponent. Under the stated uniform density premise and the supplied Bourgain range, the corrected expression gives o(TL). Together with O(L) for the inner sum this gives o(TL²), insufficient for the proposed S(T). This leaves a gap in this route to Theorem 3 from its stated premise. A bound ≪ ε(T) T^(2(1−u))/L uniformly over the whole range with ε(T) → 0 would suffice for this argument. The defect in (6.4) does not give a counterexample to Theorem 3. [Preprint, §6](https://arxiv.org/pdf/2306.04799v1)

## Thin-box repair using the stated external estimates

Theorem 2 has a separate repair with the valid O(L) bound. Write Y = T^(3/8). Every far pair is charged to an outer zero with |β−1/2| ≥ 1/(2L). By the thin-box hypothesis, this zero has γ ≤ Y. The part a ≤ β ≤ 4/5 costs at most T^(3/5) N(Y) ≪ T^(39/40)L. For β > 4/5, apply the paper's Bourgain input in its uniform range at height Y, using N(u,Y) ≪ Y^(2(1−u)). Put U = 1−η(Y), the Vinogradov–Korobov real-part bound. Correct partial summation bounds this part by

    O(T^(3/4) + L T exp[−(5/4)Lη(Y)]) = o(T).

Indeed T^(2u−1) Y^(2(1−u)) = T exp[−(5/4)L(1−u)], with u ≤ U, and Lη(Y) ≫ L^(1/3)(log L)^−1/3. The full outer sum is o(T). Applying the valid inner bound gives S(T) = o(TL), enough for §7 and Theorem 2. The repair uses the cited uniform Bourgain and Vinogradov–Korobov inputs. [Preprint, §§2, 6–7](https://arxiv.org/pdf/2306.04799v1)

## Explicit test dependence in Lemma 5

Write the uniform remainder in Theorem 1 as T^−2α E₁(α,T)+E₂(α,T), where |E₁| ≤ A and |E₂| ≤ B/√L on [0,1]. Suppose |r(α)−r(0)| ≤ Cα on [0,d], with 0 < d ≤ 1, and put R_d = ∫_d^1 |r(α)| dα. The absolute normalized remainder in (3.4) is at most

    (B/√L) ‖r‖₁ + C/(2L) + A(|r(0)|/L + C/(2L²))
      + exp(−2Ld) [2(L+A)R_d + |r(0)|].

For the Laplace peak, subtract the integral of r(0) against 2L exp(−2Lα) over [0,∞). On [0,d] use the Lipschitz bound. On [d,1] bound the r-tail by 2L exp(−2Ld) R_d. The subtracted constant tail is r(0) exp(−2Ld). For the E₁ term use the same split with |r(α)| ≤ |r(0)|+Cα near zero. Evenness supplies the L¹ bound for E₂. The dependence on the test is explicit and the numerical values of A, B and starting height are inherited from Theorem 1. [Preprint, §§2–3](https://arxiv.org/pdf/2306.04799v1)
