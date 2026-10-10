# The Möbius sign is an exact translation of the complete sextic row law

Status: proposed elementary component theorem, pending independent review.
This attacks the generalized 2k-th moment program at its literal source.
It proves no new short-row upper bound or zero-free region. RH remains open.

The adjacent generalized-moment packets are pinned in
`/workspace/.riemann-research/moment-sources/inventory.json`: PR912 at
`6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`, PR914 at
`0cc0428fedbbfc340044c7451b3d392c1da9a103`, and PR917 at
`6b4723042b3d250024eef45cb1924f88f28e902c`. Their all-row and short-row
distinction, zero masks, and finite-order Hecke requirement are retained.
The argument below is a direct application of finite-field cyclicity and
ideal CRT; no external novelty is claimed for these standard facts.

## T-M1. Exact joint-law identity

Let P be a finite collection of prime ideals of the Eisenstein ring outside
the primes above 6. Put Q=product(P). For every p in P the residue field
has order Np congruent to one modulo six, and the literal sextic residue
character maps its multiplicative group onto mu6. Choose a nonzero residue
t_p with chi_p(t_p)=-1. Ideal CRT gives a class t modulo Q satisfying all
these conditions; it is a unit modulo Q.

For any squarefree ideal n supported on P, including the unit ideal,

    chi_n(t u)=mu_K(n) chi_n(u).                         (T-M1)

This identity includes nonunits: both sides are zero when u is divisible
by a prime of n. At a prime not dividing u it is ordinary multiplicativity.
Squarefreeness turns the product of local minus signs into mu_K(n).

Let arbitrary complex coefficients c_{j,n} be supported on these ideals.
For any finite collection of profiles define

    A_j(u)=sum_n mu_K(n)c_{j,n} chi_n(u),
    C_j(u)=sum_n c_{j,n} chi_n(u).

Then A_j(u)=C_j(tu) simultaneously for every j. Multiplication by t
permutes O_K/Q, so the entire joint distributions of (A_j) and (C_j) are
identical under uniform complete-residue averaging. In particular, for
every integer k>=1,

    average_(u mod Q) |A_j(u)|^(2k)
      =average_(u mod Q) |C_j(u)|^(2k).                    (T-M2)

This holds for arbitrary fixed coefficient characters nu and arbitrary
smooth or sharp finite profiles. It is an exact finite-source identity,
not an asymptotic claim or a random-character independence assumption.
It also retains every positive-multiple-of-six coprimality mask at high k.

## T-M2. Where the source-specific information actually lives

For a complete row norm ball let L_H(v) be the number of nonzero elements
u with Nu<=H in the residue class v modulo Q. The same substitution gives
the exact weighted transport identity

    sum_(0<Nu<=H)|A_j(u)|^(2k)
      =sum_(v mod Q)|C_j(v)|^(2k)L_H(t^(-1)v).             (T-M3)

The right side uses the original short lattice measure after an invertible
CRT multiplication. It cannot replace L_H(t^(-1)v) by its uniform mean.
Thus all complete local moments, even at unbounded orders, discard the
distinction between Möbius coefficients and positive coefficients.

This locates a concrete obligation for the current attack: estimate the
correlation between the actual translated short norm-ball measure and the
large values of the unsigned polynomial, preserving the specific t that
realizes all local Möbius signs. A bound depending only on complete-residue
moments cannot establish the desired short-row theorem. The positive-source
principal-replica obstruction in PR912 already shows why a generic bounded-
coefficient replacement is inadequate in the intended range H≈D.

Taking absolute values of the short-row discrepancy in (T-M3) also loses
the very information being sought. This is a mechanism diagnosis, not a
proof that its discrepancy is small.

## T-M3. A conditional lower bound on a coherent Möbius translator

The exact translation gives a further source-qualified deduction. Suppose
the full finite-order sextic twist family is zero-free to the right of a
fixed B<1 and has the uniform reciprocal/conductor bounds stated in PR912,
MELLIN_AND_SPIKES.md Section 5. Fix a nonzero nonnegative smooth profile W
and nu=1. Standard squarefree-ideal counting gives

    sum_(n squarefree,(n,S)=1) W(Nn/D) >= c_W D

for all sufficiently large D. If an element t_D has chi_p(t_D)=-1 at
every prime dividing an active ideal in that profile, then (T-M1) makes

    A_(t_D)(D;W)=sum_n W(Nn/D) >= c_W D.                    (T-M4)

For every fixed P>0, the stated uniform reciprocal and polynomial conductor
bounds instead give |A_u(D;W)|<=C_(P,epsilon)D^(B+epsilon) for all Nu<=D^P.
Choose epsilon<(1-B)/2. The two bounds are inconsistent for sufficiently
large D. Consequently the least norm of any such coherent t_D exceeds
D^P eventually, for every fixed P. The threshold may depend on P and W.

This deduction is conditional on precisely the uniform analytic inputs;
it does not prove them, yield an effective least-translator constant, or
bound less coherent rows of size D^(1/2+delta). Those partially coherent
rows are still relevant to the open fourth and higher moments.

## T-M4. Finite probes and a rejected cumulant shortcut

`check_mobius_translation.py` reconstructs the actual split-prime residue
characters at norms 7 and 13, a CRT translator, every local zero, several
simultaneous coefficient profiles, and complete even moments through order
sixteen. All checks use exact integer zeta6 coordinates.

The separate `probe_sextic_cumulants.py` computes the literal nu=1 source
over complete small norm balls, including split and inert prime ideals.
Its sharp band is D/2<Nn<=D, so it is a finite mechanism experiment rather
than the smooth all-scale theorem. It computes exact centered fourth
cumulants, comparing the signed source with the unsigned polynomial.
At D=128,256,512 and H=D, the signed fourth cumulant is strictly positive.
Thus the promising universal shortcut that this Möbius source has
nonpositive fourth cumulant is false even in small native finite samples.
Its failure is recorded before trying to use a Gaussian fourth-moment
comparison. A positive finite cumulant supplies no asymptotic obstruction
to the desired moment estimate.

The positive source and signed source can have very different short-ball
moments while having exactly the same complete-residue moments. Both facts
point to the signed, incomplete CRT/lattice correlation as the next place
to seek arithmetic cancellation.
