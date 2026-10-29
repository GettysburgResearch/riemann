# A source-conditional dynamic contour for the unitary probe

**Status:** A reconstruction conditional on the specific source identities, fixed-type detector and bounds stated below. It is not an independent proof of Hu's local formulas, theta construction or detector, and it does not alone establish a zero-free region. Unlike a direct citation of OpenAI Lemma 10.3, its argument allows a family boundary below 7/8; it uses only that lemma's proof and the abstract trace-tail lemma.

## Inputs

Fix Hu's number field K, infinity-type orbit, unitary target ψ and finite unit sectors. Take positive fixed lₓ,lᵧ, a fixed finite slot system of total length ℓ≥0 and h=1−lₓ+ℓ>0. Let β be the supremum of zero real parts in the fixed buffered family, with β<1, and let e>0 be a sufficiently small fixed allowance. Assume:

1. Hu's general-scale physical identity (6.5), marked versions of (6.6), finite compensation (6.9), local factorizations (6.11)–(6.13), sector recombination and full ramified table hold with their stated masks. The same fixed bad set S and test functions are used on both sides. In particular the resulting quotient-free correction is the finite tuple sum of selected local factors times the product of unselected factors, before any division by an individual local H_p.
2. The [first-region calculation](../2026-10-29-unitary-first-euler-region/README.md) applies to those exact local factors. Its normal convergence and polynomial all-height majorant hold on every compact box in D₁(e₀): σ≥51/100, Re z≥17/50, Re w≥−1/100, σ+Re w≥1+e₀, e₀>0. The analogous absolute starting-line estimates hold. A fixed-field row of norm at most Z^D has conductor and deleted-factor radical at most a fixed power of Z.
3. For each finite nonprincipal row class with norm U=Z^d, d in a prescribed compact positive range, the fixed-type nested zero detector gives an endpoint a∈[51/100,β] and a buffered zero-free rectangle for the **actual** denominator presentation ψ·conjugate(χᵤ). On that rectangle its reciprocal and the finitely many deleted factors have U^ε times fixed polynomial height bounds. The buffer remains valid after allocating the original Mellin, prime-profile and any separating frequencies shares of one cumulative height allowance. On a global line Re s=β+20e, standard Hecke zero-free and strip bounds give a fixed polynomial bound in conductor and height. The numerator characters on the rows being moved are nonprincipal.
4. The external Mellin kernels and, where used as new trace coordinates, common separating densities satisfy the rapid-decay hypotheses of OpenAI Lemma 10.2. Internal coefficient measures controlled only in weighted L¹ remain integrated at their already fixed order, rather than being treated as trace coordinates. Arithmetic height exponents and profile orders are fixed before choosing the external tail order.

The field-local source claims in items 1–3 are not verified merely by the abstract contour lemma. Their use is explicit here.

## Conclusion

For a finite retained nonprincipal row dyad, a sufficiently small positive height exponent τ, and T₁=Z^τ, move the original quotient-free physical triple integral to

    Re z=17/50,  Re s=a+16e,  Re w=1/2−ϑ,
    0≤ϑ≤min{1/10,a−1/2},

where a and ϑ may depend on the row's finite detector/amplitude bin, and ϑ may be chosen after z is fixed. The contribution is the retained integral on those contours plus O_(ψ,N)(Z^B T₁^(−N)) for every fixed N. The finite B and internal polynomial height degree are independent of N. The row partition may vary measurably with the retained imaginary part of z; no additional z-contour shift is made afterward. All steps preserve the source zero masks and the exact common physical probe.

## Proof from the inputs

Start with a finite row dyad on the absolute lines in the physical identity. Move z to 17/50 with s,w on their right-hand lines, then move s to the global line β+20e. The scalar numerator is entire on these rows and ζ_K^S(6z) has no pole on the new z strip; the reciprocal is global on Re s>β. D₁ contains these paths after a fixed small margin. The source correction is kept as the full quotient-free holomorphic expression, and the global polynomial majorants and OpenAI Lemma 10.2 justify integrated and trace limits.

Discard the exterior of the fixed finite height box while s is still global. The global reciprocal, numerator, row-count and correction bounds give a fixed polynomial in Z and all heights, so the integrated tail is O_(ψ,N)(Z^B T₁^(−N)). The exponent B is fixed before N. For each fixed retained z, partition the finite row set by its detector and amplitude vector. These values are continuous functions of the retained variable z; deterministic rounding yields Borel classes, with the original masks unchanged. Within each class first move the retained s segment to a+16e while w remains on its right-hand line. The actual denominator argument stays in its stated buffered rectangle and the trace tails control the joins. No buffered s-axis is extended to all heights.

Next move w to its class-dependent line 1/2−ϑ. The row set is fixed during this move because the physical prime polynomials depend on z and the row, not on w. Since ϑ≤a−1/2,

    Re(s+w) ≥ (a+16e)+(1−a)=1+16e,
    Re w≥2/5,

so the entire path is in D₁ with a fixed margin. The numerator is entire for these rows and the denominator is independent of w. On each horizontal w-join the s integration remains inside its buffered interval; the numerator and full correction use global polynomial bounds there, and the domain-restricted trace estimate controls the join. The same single allowance covers every Mellin and prime-profile frequency. Fubini on the retained finite boxes and the uniform tail bounds give the stated result. □

The proof does not use β≥7/8. The usual floor bin, principal row, and outer row ranges must be treated separately. The selected main/error expansion and reflected numerator average are used only after this contour move; the contour proof does not divide by H_p at its zeros.

Sources: [Hu, arXiv:2610.00216v1](https://hexagonmath.org/2610.00216v1), (6.5)–(6.13) and Proposition 6.3; [OpenAI, quasi-Riemann preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Definition 10.1 and Lemmas 10.2–10.3; [Xu–Sang, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Appendix C.3.
