# Independent component review: principal correlations and quartic encoding

Reviewed on 2026-10-18 by the independent arithmetic agent.

**Reviewed file:** [PRINCIPAL_CORRELATIONS_AND_QUARTIC.md](../field/PRINCIPAL_CORRELATIONS_AND_QUARTIC.md).

**SHA256:** f67d4c44d512bdc87620cafb6e61a81b6d472917744ed72e929c1c9218b90774.

**Outcome:** no blocking mathematical or scientific-scope defect found in the
displayed component arguments. This is a review of the stated identities,
conditional algebra and their limits. It is not a verification of the imported
OpenAI analytic framework or a proof of the missing automorphic period.

## Checks

1. **Coupled Mellin residue.** The simultaneous dilation has total exponent
   $s+w-3/2$, so the proposed weighted integral inserts $(s+w-1)^{-1}$.
   I independently fetched the pinned resonant-jet source at commit
   edbc27b61208ccc7ee1fa99fa3f4e861f5a03452 and checked the stated factorization
   and convergence domain. Multiplication of the Laurent and Taylor expansions
   gives precisely (1.6), including both minus signs from differentiation at
   $s-\tau$ and the separate derivative of the test factor. The conductor
   contribution gives $(Y/Q_u)^\tau$. The note correctly retains fixed probe
   data, actual functional-equation partners, meromorphic interpretation at
   target zeros, and the need for a new complete contour estimate.

2. **Homogeneous probes.** Under the explicitly additional rank-one premise
   (2.2), the nuisance quadratic form is a positive multiple of
   $|\sum_j w_jY_j^{-1/3}|^2$. The principal coefficient has the same linear
   dependence. This is the claimed conditional obstruction. The note does
   not infer the cross kernel from a diagonal upper bound.

3. **Full quartic codec.** I checked DDHL's exact additive-character convention
   and equations (3.2), (3.5), (3.7)--(3.12) in
   [arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2).
   At a split primary prime the normalized square has the stated minus sign.
   At an inert prime the primary generator is $-p$: its angular factor is
   $-1$, while the Gauss sum and supplementary quartic sign give the same
   prime identity. The CRT multiplier has square one. Prime-power vanishing
   supplies every nonsquarefree modulus, and the unit modulus is included.
   Thus (3.1)--(3.3) retain all odd prime ideals, the ramified Euler correction,
   and the distinction between a signed square and a Hermitian norm.

4. **Square-index normalization and tensor.** DDHL (4.35) and (4.38) give
   the stated cusp sign and the real matrix
   $R=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ in the second
   primary residue class. Its lower-left minus sign uses $N(\beta_1)=5$.
   Conjugation followed by $R^{-1}$ leaves
   $\widetilde g_4(m)N(m)^{-1/4}\overline{v_0}$.
   The bilinear tensor contributes $N(m)^{-1/2}$, exactly canceled by the
   exterior $N(m)^{1/2}$ in (5.1). The remaining coefficient is
   $\mu_F(m)\overline{v_0}^{\otimes2}$. No unproved nonvanishing of $v_0$
   is used. The nonsquarefree warning agrees with DDHL (4.36).

5. **Scope of the period obstruction.** The central weights of the two-factor
   product are incompatible under the stated common-cover convention, while
   the extra genuine Eisenstein factor compensates them. Fourier constant
   terms impose the distinct index relations (4.2) and (4.3); neither
   automatically supplies (5.1). The completion, reflection, and denominator
   caution match DDHL (4.23)--(4.28). I also retrieved the body of
   [Friedberg--Ginzburg, arXiv:1403.3929v1](https://arxiv.org/pdf/1403.3929):
   its higher-rank construction assumes the indicated roots of unity and
   cuspidal input. The note preserves the possible compensated triple period
   and does not turn the absence of the present adapter into a general
   impossibility claim.

The final paragraph's wording change from the initially assigned hash
02733671681a33b855e532fefc7dfba8e4afbf26d222fb6d5bbff62fbdaa0778
to the reviewed hash above introduces no mathematical change.
