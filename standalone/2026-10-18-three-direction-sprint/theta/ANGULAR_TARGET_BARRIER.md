# Why a fixed angular phase repair loses the principal cube signal

Status: **exact source-level obstruction for a specified linear probe
repair; no exclusion of all correlated probes.** The source and notation
are pinned in PRINCIPAL_COUPLED_LINE_AUDIT.md. This note tests the
tempting proposal to shift the coupled functional-equation Gauss vector
into an already estimated angular mode.

## 1. The same angular shift acts on the sixth-power completion

In the imported planar Poisson identity every surviving frequency has
the unique form H=u a^6, where u is sixth-power-free and a is primary.
Replace the radial physical Fourier profile by a single angular harmonic
chosen to produce a frequency harmonic of nonzero integer degree ell.
For the source's complex bilinear pairing e(xy), the physical harmonic
has degree -ell: rotating the integration variable by exp(it) shows that
the Fourier transform reverses that degree. A fixed quarter rotation in
the additive character only changes a scalar phase. The new frequency
multiplier is therefore

    alpha(H)^ell=alpha(u)^ell alpha(a)^(6ell).       (1)

The radial Hankel transform changes its scalar kernel, which does not
alter (1). All finite Gauss coefficients and their original zero masks
remain those of the same imported source.

Consequently the local sixth-power-completion variable changes from

    V=Q^(-6z)   to   V_ell=alpha(p)^(6ell)Q^(-6z).

The scalar completion factor is now

    L_F^S(6z,alpha^(6ell)),                         (2)

rather than zeta_F^S(6z). The remaining local factors are obtained from
the same exact polynomial tables with V replaced by V_ell. In the
principal extraction neighborhood x>7/8,w=1,z=1/6 their convergence
estimates are unchanged because |alpha(p)|=1. Thus no pole can be hidden
in that normally convergent correction to replace the missing pole of
(2).

For completeness, regularity of (2) at 6z=1 does not need a strong
automorphic import. Since alpha(a)^(6ell) is invariant under the six
units, its summatory function over ideals of norm at most T is one sixth
of the corresponding full lattice sum. The integral of
`(y/|y|)^(6ell)` over a disk is zero for ell!=0. Comparing lattice tiles
with this disk gives an O_ell(sqrt(T)+1) error: boundary tiles contribute
O(sqrt(T)), and the summed interior gradient error is bounded by
`C_ell integral_1^sqrt(T) r^(-1) r dr=O_ell(sqrt(T))`.
Partial summation therefore continues the ideal Dirichlet series
holomorphically to Re(6z)>1/2. Deleting the fixed primes S multiplies it
by finite entire factors. In particular (2) has no pole at z=1/6.

## 2. The proposed angular repair and the detector conflict

On squarefree u the actual complete Gauss identity is

    gamma_1(u)=mu(u)alpha(u)G(u)conjugate(gamma_2(u)). (3)

Conjugation converts the original vector to
`mu(u)bar alpha(u)bar G(u)gamma_2(u)`. The structured cubic theorem
available in the sibling source estimates the angular modes
`mu alpha^(+2)gamma_2` and `mu alpha^(-2)gamma_2`, with specified fixed
ray factors and row/column restrictions. Multiplying gamma_1 by
alpha(u) (ell=1) would, after whole-vector conjugation, place its angular
power at -2. This explains the attraction of that repair.

But exactly the same ell=1 probe changes the completion factor to
`L_F^S(6z,alpha^6)`, regular at z=1/6. It removes the scalar pole used to
produce the genuine principal target signal. The repaired vector is
therefore not another detector of the same original principal residue.

For a finite linear combination of fixed angular profiles, the
z=1/6 principal residue receives a contribution only from its ell=0
component. That component has the unchanged phase (3). Nonzero angular
components may still be useful auxiliary probes, but merely adding them
does not replace the phase of that principal residue by an allowed mode.
This statement concerns the same linear Poisson construction; nonlinear
correlated observables or arithmetic modifications of the completion
are outside its scope.

## 3. A formal scalar repair is not free in the native norm

One might try to multiply (2) by

    zeta_F^S(v)/L_F^S(v,alpha^(6ell)),    v=6z,       (4)

to put back the missing principal completion. This is an exact formal
Euler operation on the initial absolute lines. If its Dirichlet
coefficients are c(a), a z-only physical implementation is

    sum_a c(a)(Na)^(-3) I_ell((Na)^6 X,Y,Z).         (5)

Indeed `(Na)^(-3)` times the X dilation multiplies the Mellin weight
`X^(1/2-z)` by `(Na)^(-6z)`.

For the native size bound `|I(X,Y,Z)|<=C sqrt(max(X,Y))`, however, the
large-X terms in (5) have triangle cost proportional to |c(a)|, with no
remaining norm decay. This sum diverges even on powers of one good
nonreal prime p. Its Euler factor in (4) is

    [1-alpha(p)^(6ell)Q^(-v)]/[1-Q^(-v)],

so `c(p^k)=1-alpha(p)^(6ell)` for every k>=1. A nonreal Eisenstein prime
has alpha(p) of infinite order: a root of unity would lie on a unit ray,
whose Eisenstein integer norms are squares, whereas a split rational
prime has nonsquare norm. Choose such a p outside fixed S. Then these
coefficients are nonzero constants along all its powers.

Thus (5) has infinite absolute norm on the stated growth class. It does
not even converge termwise on the test trajectory `I(X,Y,Z)=sqrt(X)`,
because its p^k terms have a nonzero constant value. This is an
obstruction to deriving a bounded repair from that upper bound alone;
it is not a proof of divergence for the actual arithmetic probe.
A special signed estimate, a different physical source, or an additional
regularizing operation would have to be supplied and paid explicitly.

The source-level conclusion is precise: fixed angular shifting reaches
a better-estimated Gauss vector while discarding the original cube pole,
and the most direct scalar operation to restore that pole is not bounded
by the available native growth norm. No new zero-free conclusion is
drawn.
