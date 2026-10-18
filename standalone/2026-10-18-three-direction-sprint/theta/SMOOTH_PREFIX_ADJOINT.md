# Smooth row prefixes in the primitive adjoint contour

**Source-qualified interface lemma.** This closes only the distinction
between a fixed smooth annular row profile and a fixed smooth profile
nonzero at0 in the squarefree-row adjoint. It does not extend that
adjoint to nonsquarefree physical rows or estimate its contour remainder
more strongly.

Use the primitive series, fixed finite ray sectors, continuation and
polynomial vertical bounds of the pinned rStation paper10/v2,
Sections1--7. Let `h` be any fixed smooth function on `[0,infinity)`
with compact support there. It may be nonzero at0. For `Re s>0`,

    h_hat(s)=integral_0^infinity h(x)x^(s-1)dx

is holomorphic. On every closed vertical strip in that half-plane it
decays faster than every power of `1+|Im s|`. Indeed, with
`D=x*d/dx`, integration by parts N times gives

    h_hat(s)=(-s)^(-N) integral_0^infinity D^N h(x)x^(s-1)dx.

All boundary terms vanish for `Re s>0`. For `N>=1`, `D^N h(x)=O(x)`
at0, so the last integral has a fixed absolute bound on the strip.
Differentiating a fixed number of times in s only inserts integrable
powers of log x and gives the same conclusion. No annular cutoff or
truncation at a small positive argument has been introduced.

Consequently the literal identity (7.1) has Mellin representation

    U^(-1/2) sum_(z good squarefree)
       h(Nz/U) nu_[n](z) g6(nR,z)/sqrt(Nz)
      = (1/(2pi*i)) integral_(Re u=c)
           H_(nu_[n])(nR,u) h_hat(u-1/2) U^(u-1)du,

initially at any sufficiently large fixed c. The original row sum is
finite. The same Mellin shift to `Re u=1+eta`, `0<eta<1/6`, crosses
the same theta pole at `u=7/6`, and no profile pole. Throughout the
shift `Re(u-1/2)>0`. The residue is exactly

    U^(1/6) h_hat(2/3) rho_(prim,nu_[n])(nR).

The remaining integral is precisely paper10's contour integral with
`h_hat` in place of its annular transform. Its rapid vertical decay
allows the SAME primitive mean-square input and the SAME Minkowski
argument. Thus paper10's squared remainder bound

    sum_(n~X) |E_(U,R)(n)|^2
       <<_(epsilon,h) (UXNR)^epsilon X (NR)^(1/2)

extends to these fixed smooth prefixes. Every original ray sector and
nonunit Gauss zero remains. A possible Mellin pole at s=0 lies strictly
to the left of this argument; it contributes no new term.

For a frame application one may choose a fixed smooth nonnegative h
that majorizes the square root of the original bounded row weight.
This avoids dividing by a weight that becomes small at a boundary.
The unweighted character frame must still be proved separately. This
lemma supplies neither a full residue Type-I estimate nor a complete
mixed norm, and the squarefree physical-row restriction is unchanged.
