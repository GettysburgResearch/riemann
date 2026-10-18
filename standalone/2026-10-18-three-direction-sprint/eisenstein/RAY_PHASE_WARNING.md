# The Eisenstein finite phase must not be declared a Hecke character

Status: **exact finite obstruction for one specified ray architecture.**
It does not rule out the older Eisenstein construction or any correction
using a different generator convention, level or representation.

Let alpha be the primary generator of an exterior prime ideal of Q(omega),
q=Nalpha, and use the additive character exp(2pi i Tr(x/alpha)). Denote
the unnormalized sextic Gauss sums G_j and Jacobi sums J_ij. Exact finite
field Fourier identities give

    G_1 G_2=J_12 G_3,
    G_2^3=q J_22,
    J_12=conjugate(chi_6(4)) J_22.                       (1)

The prime fixtures in gauss_phase_check.py reconstruct these identities as
equalities in Z[omega,zeta_p]: arrays in powers of zeta_p represent every
actual finite field element, and equality is checked modulo
Phi_p=1+Z+...+Z^(p-1). This avoids floating approximation of the phases.
For the 42 prime ideals of norm <=193, J_22=-alpha exactly. The classical
quadratic Gauss evaluation identifies gamma_3=G_3/sqrt(q) as a power of i.

If one seeks a correction vartheta(P) making gamma_1(P)gamma_2(P)vartheta(P)=-1,
its ratio to the primary angular character conjugate(alpha)/sqrt(q) is

    eta(P)=conjugate(conjugate(chi_6(4)) gamma_3(P)).      (2)

Within those exact fixtures, eta depends consistently on alpha mod4 and
occupies all 12 invertible residue classes. Write eta=exp(2pi i k/12).
For alpha=-2-3omega, norm 7, its mod4 class is x=(2,1), and k=7. For
alpha=7+3omega, norm 37, the class is x^2=(3,3), and k=8. A character of
the ray unit group would require

    eta(x^2)=eta(x)^2,
    8=2*7 mod12,

which is false. In fact 54 of the 144 ordered class pairs violate
multiplicativity in this table. This is an exact counterexample to simply
calling this conductor-dividing-4 primary phase a finite ray character.
Finite consistency of the table on further primes would not repair its
multiplicativity defect.

This explains a concrete normalization risk in importing CT's mu_12
construction into Q(omega): CT's allowed-generator isotropy and its
Q=1 mod12 residue-field condition remove a quadratic multiplier defect.
Q(omega) has exterior norm-7 primes and does not satisfy that hypothesis.
The experiment does not prove that no larger-conductor correction exists,
nor that all older Eisenstein phase conventions behave this way.

ANGULAR_COEFFICIENTS.md deliberately permits a nonmultiplicative fixed
periodic eta, so its elementary lattice estimate is unaffected. Applying
that theorem to a complete native source still requires an actual global
coefficient identity, not just agreement with these prime-level phases.
LEGAL_FIELD.md supplies a separate ordinary-target construction in the
one genuinely CT-admissible field Q(zeta_12).
