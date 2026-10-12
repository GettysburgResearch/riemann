# Independent review of the complete cusp support return

Reviewer: `/root/height_mechanisms`, 2026-10-10 UTC.
Result: **ACCEPT V1–V10 at the stated imported complete theta-automorphy and
source-compatible cusp-reduction scope.** This is a support filter, not a
complete moment bound or a strict contraction of the remaining branch.

Reviewed manuscript: `../literature/CUSP_VECTOR_SUPPORT_RETURN.md`, SHA-256
`5ba2e4cf7f5cf2cc64c71a9b567a156a8d5e90812115ab76eba0630148dc98d5`.
The exact primary source and derivative normalization are the ones bound in
[OPPOSITE_THETA_CROSS_REVIEW.md](OPPOSITE_THETA_CROSS_REVIEW.md).

1. Multiplying a full cusp coefficient by a bounded periodic function of
   `lambda^4 ell` is exactly the finite Fourier translate by `lambda^3 h/q`.
   The multiplier is defined at nonunits, and a possible constant mode is
   removed by the horizontal derivative. A premise `phi(0)=0` is unnecessary.
2. Every nonzero `chi_p^3` Fourier coefficient has a nonzero frequency, so
   every `k` prime is active. For a positive divisibility mask, each Fourier
   coefficient is exactly `1/Np`, including frequency zero; therefore its
   active good primes are an arbitrary `r|d`. The reduced denominator is
   `c20*k*r`, with a fixed finite family of `c20` from the fixed bad modulus.
3. The exact identity
   `G^(-1) H_u T(a/c)=[[delta-bu,1/c],[-c,0]]` follows from the determinant
   equation `a delta-b(ua+c)=1`. The inverse hyperbolic height therefore has
   denominator `Nc`, not the norm of the image-cusp denominator `ua+c`.
   The manuscript now explicitly chooses the second column by the source's
   congruence/CRT construction before invoking the three-cusp reduction.
   Primary-unit normalization has norm one and is retained in the phase.
   This clarification closes the arbitrary-Bezout-lift precision issue.
4. The opposite derivative at zero has the same inverted horizontal
   normalization as the earlier accepted packet. Its derivative of the
   inverted height is zero there, so constant modes do not enter the Mellin
   functional equation. The complete cusp coefficient support and its
   absolute convergence bounds are retained. No finite theta truncation is
   substituted for the full cusp vector.
5. The generic frequency Mellin normalization has no `27^s`. Its transform
   has scale `(2pi)^4`; composing it with the first primary-index transform
   of scale `(2pi)^4/27` yields exactly `V(27x)`. The full gamma quotient
   cancels. The intermediate Mellin line `-2/3` is above the first pole
   `-5/6`, with the same entire-series and vertical-decay justification as
   the accepted opposite-derivative argument.
6. The two-term Ramanujan expansion is exact before taking a norm. It unites
   the squarefree-divisibility and cube-divisibility alternatives, retaining
   their interference. After the second reflection the compact argument is
   `27 Nell' Nc10^2 N(a/r)^2/(B Nc20^2)`. Both moving `k` powers cancel.
   The full nonzero cusp frequency lattice has `Nell'>=1/81`; consequently
   every term with `Nh^2>C_V B`, `h=a/r`, vanishes individually. No uniform
   bound on the number or absolute mass of the finite translate terms is
   needed for this conclusion.
7. The all-negative allocation is covered at every cusp. The remaining
   support condition allows `h=1`, namely all positive-mask primes active.
   The manuscript correctly confines its explicit unit-modulus Gauss scalar
   to the standard cusp and makes no scalar assertion about all other cusps.
   The same-scale branch therefore remains an unpaid analytic interaction.

This audit does not rebuild Kubota/Patterson automorphy or approve an
unwritten estimate for the surviving reflected coefficients. Its conclusion
is the exact source-qualified support restriction and the named vanishing
components at full completion scope.

Final rebinding: the manuscript's status and review-summary-only update is
frozen at SHA-256 `caf970c667eef9686de24b2611b44768cc2b2e0fd833f143c43a0f46a341a183`.
Its mathematical argument is unchanged from the explicitly reviewed
`5ba2e4cf...` source above. Acceptance remains in force at this final hash.
