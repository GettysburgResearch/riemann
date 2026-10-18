# Independent principal coupled-line review

**PROPOSED internal component review, not repository acceptance.**

Reviewed the actual bytes of
`../theta/PRINCIPAL_COUPLED_LINE_AUDIT.md`, SHA256
`ee2e372efc0acf88e6e82574f652cc2bcd4a2d0f2261ad22c7b5c80d20fb3198`,
against the complete local table and physical Mellin weight in the pinned
original OpenAI source, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

No blocking error was found at the stated component scope. The following
were reconstructed independently, rather than inferred from a numerical
fit or from the source's existing convergence region.

1. With `s=x+w`, `DW=Q^(-s)`, direct multiplication gives
   `J_p-1=[D^2 W(1-W)+(1-DW)B]/(1-D)` after
   `J_p=(1-DW)H_p`. This removes the leading common coupling Euler term.
   In the stated cross-line region, `Re x+Re s>=1.50`,
   `2Re s>=1.98`, and the worst good-prime remainder is
   `Q^(4-6Re x-6Re z+2 max(-Re w,0))<=Q^(-1.08)`.
   Thus the continued product has a genuine strict normal-convergence
   margin across `Re(x+w)=1`.

2. The literal `j=1` row of the source gives
   `H_p=1+[R(1-Q^(-1))+Q^(-s)-Q^(1-s)V]/(1-R)`.
   Consequently `J_p=1+O(Q^(-1.10))` uniformly in every squarefree
   row, not merely `O(q_u^epsilon)`. In particular the dangerous
   `Q^(1-Re s)` term is damped by `V` when `j=1`. It is undamped
   only for valuations at least two. The resulting bound
   `J_u << q_u^epsilon rad_2(u)^((1-Re s)_+)`
   follows directly from all five ramified rows; since
   `rad_2(u)<=q_u^(1/2)`, its stated coarser version is valid.

3. The simultaneous dilation exponent is exactly `x+w-3/2`.
   Therefore the ideal-Mobius average with coefficients `(Na)^(-3/2)`
   multiplies by `1/zeta_E^S(x+w)`. The outer annular cutoff makes
   the physical sum finite at every fixed scale. At the principal
   extraction this multiplier is `1/zeta_E^S(x+1)`, which is
   holomorphic and nonzero in the required half-plane.
   The fixed Euler derivative multiplies instead by `x+w-1`, hence
   preserves the principal detector through its nonzero factor `x`.

4. On the exact complex line `w=1-x`, the primitive functional equation
   cancels the numerator/denominator ratio. Its root number is not
   discarded. The global identity
   `gamma_1(u)=mu(u) alpha(u)G(u) conjugate(gamma_2(u))`
   retains the squarefree Mobius sign. A fixed bad-place CRT correction
   supplies bounded finite-ray factors, not an extra Mobius sign.
   The coupling residue is thus a nuisance term, not a new target
   detector or an immediately admissible unweighted angular cubic mean.

5. The Cauchy projection cost and the absolute-residue geometry were
   checked algebraically. In particular the latter's constraint
   `5a+3b>5` forces the low-side comparison above `15/16`.
   Neither the pole removal nor the squarefree-row refinement alone
   bounds the remaining complete mixed inverse/plain family.

The review supports these exact reductions and the explicitly conditional
budgets. It does not validate a new zero-free boundary, the whole imported
OpenAI framework, or a full metaplectic spectral decomposition.

Final append reviewed: the theta note's final SHA256 is
`e3d69cd104d80deb21b9616612831f8be62580fd627eb373cbf1a500dbd33344`.
The only post-review addition is its equation (23) and the surrounding
critical-dyad budget. Independently, moving w left by d0 increases the
FE conductor bound by U^d0 and improves the physical factor by Y^(-d0);
thus (U/Y)^d0 is non-improving when l_y<=h. This matches the complete
old-source exponent derivative l_y-h already computed in this track.
No blocking issue is added by the final paragraph.
