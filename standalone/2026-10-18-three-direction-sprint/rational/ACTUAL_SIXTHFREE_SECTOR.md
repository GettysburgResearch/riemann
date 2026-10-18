# Small conductors on the actual sixth-power-free row set

**PROPOSED.** This extends the small-conductor component of
`MIXED_CONDUCTOR_SECTOR.md` to the actual sixth-power-free rows, without
first adding all element rows. Root proposed the extension; this agent
independently reconstructed its kernel bound and pair summation.
The complete large-conductor correlation sum remains open.

Use exactly that file's complete coefficient c_A, support NA≈L=DN,
primitive conductor C(A,B), zero-only mask R(A,B), and fixed smooth
planar row majorant Phi. The only enlargement is from the original
physical compact box to the support of Phi; the sixth-power-free
indicator remains INSIDE the row kernel. Fixed S/unit/ray conditions
are retained with the same finite constants and masks as there.

Let

    K_sf(U;A,B)=sum_u 1_(u sixth-power-free)
            Phi(u/sqrt(U)) theta_C(u)1_((u,R)=1).      (1)

For C!=1 and NC<=U^2,

    |K_sf(U;A,B)|
         <<_epsilon L^epsilon U^(1/6)(NC)^(5/12).     (2)

For C=1 the bound is O(U). The implied constant in (2) may include
fixed profile/field/ray data. All changing common-prime masks retain
their displayed divisor cost, absorbed by L^epsilon because NA,NB≈L.

Indeed the exact identity

    1_(u sixth-power-free)=sum_(d^6|u) mu(d)

gives a sum at row scale `V=U/(Nd)^6` after u=d^6*v. A d meeting C or
R makes the original complete character zero, so that term is zero.
Otherwise `theta_C(d^6)=1`, and the v kernel has the SAME primitive
conductor C and the SAME zero-only mask R. Multiplication by d^6 can
rotate the planar profile; this preserves its uniform smooth bounds.
Thus each term costs at most

    C min(U/(Nd)^6, sqrt(NC)*tau(R)).                 (3)

The first estimate is the row count at scale V. If V is below a fixed
positive constant, compact annular support contains no nonzero lattice
row; throughout the nonempty range its count is O(V), with the constant
depending only on the fixed annulus. The second is precisely the full
masked primitive Poisson bound already proved in the preceding file.

Put `M=(U/sqrt(NC))^(1/6)>=1`. For Nd<=M, sum the second bound in
(3) over O(M) ideals. For Nd>M, sum the first bound and use
`sum_(Nd>M)(Nd)^(-6)<<M^(-5)`. Both contributions are at most

    C tau(R) U^(1/6)(NC)^(5/12),

which proves (2). No mean cancellation in mu(d), no removal of shared
primes, and no uniformity in a growing field is assumed.

For each fixed squarefree primitive C, the exact gcd/sixth-power
pair count in `MIXED_CONDUCTOR_SECTOR.md`, Section 3, gives

    sum_(A,B:C(A,B)=C) |c_A c_B|
          <<_epsilon L^epsilon (NC)^(-1/2+epsilon).   (4)

This follows from the same local product
`prod_(P|C) 2 sum_(j=1)^5 (NP)^(-j/2)`; it is not an assumption
of generic orthogonality. Combining (2), (4), and ideal counting yields,
for 1<=Q<=U^2,

    |T_sf,small(Q)|
       <<_epsilon (LQ)^epsilon
                    [U+U^(1/6)Q^(11/12)].             (5)

The principal C=1 pairs are included and paid by O(U L^epsilon).
At D=U,N=U^(1/2), Q=U, this is

    |T_sf,small(U)| <<_epsilon U^(13/12+epsilon).       (6)

It fits a hypothetical complete U^(6/5+epsilon) mixed budget. It does
not yet fit the stronger U^(1+epsilon) budget at that cutoff. If the
latter is required, the same argument pays conductors up to
`Q=U^(10/11)` with exponent one.

After expansion, the primitive-conductor sectors are signed. Formula
(5) bounds their actual sum absolutely; it does not authorize changing
the row set in each sector. The exact remaining task is the entire
correlation sum with `NC(A,B)>Q`, over the same actual sixth-power-free
rows and the same complete coefficient. Neither the all-row majorant
proof nor this extension estimates that remainder.
