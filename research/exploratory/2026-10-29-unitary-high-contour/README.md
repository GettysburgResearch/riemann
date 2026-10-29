# Conditional moderate-row estimate for the variable unitary probe

**Status:** This is an exponent-and-contour reduction, not a zero-free theorem. It combines source-conditional inputs already isolated in the companion notes. The conclusion is conditional on Hu's actual physical Mellin formula, its variable-scale contour and tail estimates, and the stated detector/moment matching; the recent analytic preprints have not been independently proved here. The scalar inequalities are those certified by Xu–Sang, not new numerical results.

## Conditional statement

Use the same compensated unitary Hecke probe, prime windows, target family and geometric notation as [the variable-low note](../2026-10-28-hu-variable-low/README.md). Take

    κ=3/4,  b=173/2000,  ℓ=10027/60000,
    B₀=11/12−ℓ/4=69991/80000,
    lᵧ=(1+b−ℓ)/2,  h=(1+b+3ℓ)/2,  z₀=17/50.

Let β be the common zero supremum for the buffered family used in the detector, and suppose B₀<β≤7/8. Fix ζ=10^(−7), dmin=1/100 and a sufficiently fine fixed slot mesh. Suppose all of the following source interfaces hold for this **same** probe and slot system:

1. The physical finite-row Mellin formula, original zero masks, retained-height contour moves, and integrated and trace-tail bounds in Hu §6.6 and Xu–Sang Appendix C.3 apply at these variable scales, with one cumulative buffered height allowance. In particular the original full correction is holomorphic throughout each move before selected factors are divided by unselected ones, and the amplitude partition is made at fixed z before shifting w.
2. The finite-row detector and count in [the witness-count note](../2026-10-29-hu-witness-count/README.md) apply to each retained nonfloor class; the relevant class cardinality is U^(R(δ,x)+ε) times a fixed height polynomial, and its original prime-slot amplitudes are the lower bounds used in the numerator moment. The detector floor uses the trivial row count.
3. Hu's paired fourth moment at κ=3/4, its finite-order zero-free premise, Kummer conductor identification and the physical slot matching hold with the stated mesh/profile quantifiers. Then [the amplified-numerator note](../2026-10-29-unitary-amplified-numerator/README.md) applies. The local selected-error bound and simultaneous conductor-deficit arithmetic in [the raised-line note](../2026-10-29-raised-line-error/README.md) also apply to every term of the full main/error expansion.

For a retained intermediate row dyad U=Z^d with dmin≤d≤h+ζ, the total nonprincipal contribution is, after the fixed normalization and for sufficiently small real losses,

    ≪ Z^(C_b(β)−ρ) (1+T₁)^A,
    C_b(s)=s−(4+b)/6,

for some ρ>0 independent of the target and of the finite row class. Here A and the implicit constant may depend on the fixed field, target and slot system, while the numerical saving and choice of mesh are independent of a later fixed target twist. The same bound holds after summing the logarithmically many intermediate dyads. This statement does not cover principal, small or distant rows, nor does it establish the trace-tail assumptions in item 1.

## Exponent calculation

On a nonfloor detector bin write a=(1+δ)/2, q=δx with 0≤x≤1/2, and let R=R₍₃⁄₄₎(δ,x) be the source count. Set K₀=(3R+1)/4 and L=ℓ/d. Choose the reflected numerator displacement

    ϑ=q min{L,1/(6κ)}      if 0<δ<1/8,
    ϑ=q/(6κ)               if 1/8≤δ≤3/4.

The second choice is permitted by the source inequality R≤(6κ−2q)L. Indeed on the retained range L>21/100 and the source crude estimate R≤1−2δ/3 give the displayed inequality with a fixed margin, exactly as in Xu–Sang (32). Both choices have 0≤ϑ<1/10 and ϑ≤a−1/2. The numerator average is U^(K₀−ϑ/2+ε); reflection and the whole error tuple cost U^(ϑ+ε). These are simultaneous, not separate savings reused for each error slot. The physical main slots contribute at most Z^(ℓq) on the class; dropping a main factor for an error slot never increases that exponent. All slots contribute their common centered factor Z^(ℓ(z₀−1/2)).

The outside Mellin factor, Poisson row weight U^(−z₀), and this row average give exponent relative to the low-side benchmark C_b(B₀):

    E(d;δ,x) = a−B₀−lᵧ(1/2+ϑ)+h(z₀−1/6)
                 −ℓ/2+ℓq+d(K₀+ϑ/2−z₀).                  (1)

If the s-line is raised by the customary fixed detector allowance, its cost is assigned to the small real losses. The high expression is compared with C_b(β), so β>B₀ only improves the relative exponent by β−B₀. Formula (1) is exactly Xu–Sang (27) with Hu's norm-scale variables; this equality uses the source physical Mellin prefactors, not just a numerical analogy.

At fixed δ,x, (1) is continuous and increasing in d with upper one-sided derivative at most 2; in the supply-limited branch ϑ=qℓ/d, the derivative is K₀−z₀+qℓlᵧ/d². Thus the extension from h to h+ζ costs at most 2ζ. At d=h and δ≥1/8, the expression becomes Xu–Sang (28). Their Appendix D.1 clears its positive denominator and proves E(h;δ,x)≤−10^(−6) on the full rectangle 0≤δ≤5/6, 0≤x≤1/2 by an exact positive-polynomial certificate. The continuation range δ≤3/4 lies inside it. Consequently these bins have a saving of at least 10^(−6)−2ζ=8·10^(−7) before small analytic losses.

For 0<δ<1/8, Xu–Sang (33) and their Appendix E bound the endpoint by less than −1/250, and the extension costs at most 2ζ. At the floor use the separate pointwise numerator contour, the trivial row count and the floor inequality in their Appendix E, which is less than −1/100 at h. In all cases choose the fixed mesh and the finite detector, coefficient, contour and normalization losses below a common fraction of the smallest of these margins. Finitely many bins and logarithmically many dyads then preserve a positive ρ. □

## Remaining analytic gate

The cited Hu statement of the high decomposition is printed at its original b=1/8, ℓ=1/6. Its proof says that the local formulas, finite height degrees, and OpenAI's contour construction transfer to the field-and-type setting, but an independent proof that each trace-tail and buffered height estimate is uniform at the variable scales has not been completed here. In particular, the s-axis must remain inside the detector's zero-free buffer on each w-join; one may not extend its reciprocal bound globally in height. The statement above deliberately assumes that precise interface. It therefore cannot yet be combined into an unconditional continuation argument.

Sources: [Hu, arXiv:2610.00216v1](https://hexagonmath.org/2610.00216v1), Proposition 6.3 and §§7–8; [Xu–Sang, arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Propositions 4.1, 5.1, 6.1, Appendices C–E.
