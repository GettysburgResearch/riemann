# Independent review of the balanced unitary inverse addendum

Reviewer: `/root/repo_routes_audit`. Date: 20 October 2026.

**Result:** No blocking gap found in the additional fixed-radial argument, subject to the explicitly imported source representation, finite local identities, sieve estimates, and inverse induction. This review concerns the new analytic transport and constant-term calculation; it does not certify the full external preprint.

## Exact scope and files

- Reviewed `BALANCED_UNITARY_INVERSE_ADDENDUM.md`, SHA-256 `590fef51aaf46e11c702099fd145444a58737f41d79607103c61f85c828d5e7c`.
- Its previously reviewed core is `ANGULAR_THETA_AND_INVERSE.md`, final SHA-256 `9ed89b4acf05c6fd35e7edbc0da0f0efa00a7b2b919b766846f01da0b003aa99`; the notation-only delta from the first core review is documented in `REVIEW_REPO_ROUTES.md`.
- Primary source: Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), PDF SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.

I read the complete radial draft, checked its Mellin formulas against source (5.2), (5.4) and the Bessel integral, and checked the representation statements against source Proposition 4.1, pp. 25--28, and Lemma 5.1, pp. 31--34. I then reread the final generalized-eigenspace and annihilating-polynomial argument in the packet version and verified its exact hash. This is mathematical review, not a claimed replay of the source's analytic proof by a local numerical checker.

## Checks that determine the conclusion

**Normalization and Mellin signs.** The ideal norm character has local weight \(|y|_v^{it}\), so subtracting the mean radial parameter gives the stated balanced vector. The direct sheet pairing uses \(L_S^{-1}\), yielding gamma arguments \(A+t-ig\) and \(B+t-ig\). The reflected pairing uses \(L_S\), yielding the opposite radial signs. Dividing by the direct transform at \(-t\) consequently gives exactly the displayed quotient. The local Bessel prefactor ratio is \((2/c)^{4t+4ig}\); its extra fixed factor is a unit phase, retained in the finite multiplier.

**No exponential or strip loss.** At \(t=\sigma+iT\), each paired gamma numerator and denominator has imaginary part \(T+g\) and its negative. Exponential Stirling factors cancel identically. The two gamma quotients at a place contribute the original power \(4\sigma\). Fixed translations of height change only constants, also for negative \(\sigma\). Numerator poles have real part at most \(-1/3\), and the source uses strict strips to its right. The direct Mellin product is nonzero. Newly inserted radial factors have modulus one in the absolute sheet bounds.

**The all-spherical case is handled.** When every theta angular degree is zero, the integer condition forces \(h=\pm1\), and nonresonance leaves a nonzero balanced radial vector. The real Jacquet exponents are the actual inducing exponents from Proposition 4.1 and Lemma 5.1, not inferred from a Whittaker asymptotic. Their finite generalized spectral support is unchanged by finite digit averages or a different vector in the same representation.

For a positive archimedean norm-one translation \(T_t\), choose \(t\) with the balanced radial phase nontrivial. Every weighted eigenvalue then has the form \(e^{A_j(t)-ig\cdot t}\ne1\), with \(A_j(t)\) real. The weighted constant term descends to the compact unit quotient by the global construction of \(L_S\); neither separate triviality of finite phases nor a product fundamental domain is assumed. Translation commutes with the unit and finite-class operations. If its finite translation span is annihilated by \(P(T_t)\), then \(P(1)\ne0\), and invariant integration gives

\[
 0=\int P(T_t)f=P(1)\int f.
\]

This proves the missing constant-term vanishing, including generalized eigenvectors. The supplementary CRT projection argument is compatible with the same descent. For one complex place there is no nonzero balanced radial vector, and the extra case correctly disappears.

**Coefficient and family scope.** Radial parameters stay in the fixed finite orbit \(\{h\gamma,-h\gamma\}\). The cube coefficient and the terminal row, tuple, and selected-prime factors retain their exact multiplicative separation. No radial character enters the periodic Kummer row matrices. The previously reviewed margin recursions and sixth-power amplification therefore use the same profile exponents and yield the stated preliminary \(11/12\) boundary, with constants allowed to depend on the fixed radial data.

The refined boundary still requires the separate balanced product-moment and continuation adapter. I authored `BALANCED_UNITARY_MOMENT_ADDENDUM.md` at SHA-256 `35448a3f2db447b3d493f39558b414594266ae2eb2bc2359d01193baaacf5636`; I do not present self-review of it as independent approval. The two resonant balanced types are excluded throughout, and no limiting argument in the radial parameters removes that exclusion.
