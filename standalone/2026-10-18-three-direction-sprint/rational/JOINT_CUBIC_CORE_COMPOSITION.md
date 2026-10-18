# Simultaneous row filtering, collision centering and dual-core removal

**PROPOSED source-qualified component theorem.** The final simultaneous
high-conductor, high-cubic-core signed form is OPEN. This note supplies
the composition argument; bounds for separately selected signed sectors
are not silently combined. The primary Poisson and quadratic/cubic sieve
inputs are pinned in `CUBIC_CORE_DUAL_SECTOR.md`. The full all-power
bilinear resource is `CUBIC_CORE_ALL_POWER_TRANSFER.md`.

Use the complete original inverse/plain source, profiles, sixth-free
physical rows and original zero extensions of those notes. Put L=DN,

    C0=D+N+L^(2/3),
    H0=D^(1/3)+N^(1/3)+L^(1/6),
    B(U,D,N,V)=U^(2/3)V^(2/3)
       +U^(3/4)C0^(1/4)V^(3/4)+U^(5/6)H0 V^(5/6).       (1)

All source parameters have their original common, fixed polynomial
seminorm/height cost. The extra norm phases introduced below never
enter those differentiated seminorms.

## 1. Exact separated restrictions on the original input pairs

The low-core bilinear argument is uniform when each original inverse
input and each original plain input is multiplied by an arbitrary
bounded coefficient, independently on the two sides of the opened
moment. To verify this, carry these coefficients through the exact
g,h decomposition. For a fixed component they become bounded functions
of g*a and g*h^2*b, respectively, hence bounded coefficients of a and
b separately. All local allocations preserve that separation. The
factorized Gauss projection then uses the cubic bilinear large sieve
with arbitrary bounded input vectors, and the quadratic mean uses
arbitrary bounded column vectors. Neither input theorem differentiates
or requires multiplicativity of these additional input coefficients.
No inverse-moment estimate for arbitrarily modified Mobius coefficients
is being imported here.

Consequently the ORIGINAL restrictions d1!=d2 and n1!=n2 can be retained
at constant total variation cost. Explicitly enumerate the finite
supported original d indices injectively by i_d in Z/J_d Z. Then

    1_(d1=d2)=J_d^(-1) sum_(l mod J_d)
                 exp(2*pi*i*l*i_d1/J_d)
                 exp(-2*pi*i*l*i_d2/J_d).              (2)

There is an identical formula for the original n indices. The signed
measure representing 1-delta has total variation at most two; their
product has total variation at most four. Equation (2) uses the
ORIGINAL inputs even after decomposing their powers. It does not
replace equality of d by equality of a or equality of product columns.
The equality formulas are finite exact identities, with no growing
Fourier-tail or smoothness cost. All original nonunit zeros remain.

## 2. A sharp primitive-pair-conductor cutoff costs logarithms

The primitive pair-conductor norm NC is a positive integer. For any
real Q>=1 put q=floor(Q). A smooth step which equals one below q+1/4
and zero above q+3/4 agrees EXACTLY with 1_(NC<=Q) at every possible
conductor norm. On a fixed component/local-pattern/gcd dyad the actual
conductor is

    NC=Lambda * Nx * Ny.                              (3)

After the finite coprimality projector, x=k*c1,y=k*c2, but the cutoff
still uses (3), including the factor (Nk)^2. It is not the primitive
conductor of an artificial extended pair.

Normalize x,y by their ORIGINAL lengths M1,M2. Their ratios lie in
fixed compact annuli. Let s=log(Nx/M1)+log(Ny/M2), multiply the smooth
step by a fixed compact cutoff equal to one on all these s, and call
the result F(s). If its transition meets that compact interval,
Lambda*M1*M2 is comparable to q+1. Thus

    ||F||_1+||F'||_1=O(1),
    ||F''||_1=O(1+q).

The elementary Fourier bounds therefore give

    |Fhat(t)| << min(1,1/|t|,(1+q)/|t|^2),
    integral |Fhat(t)|dt << log(2+q).                  (4)

If the transition misses the interval, use its constant value there
and a fixed compact cutoff, at bounded cost. The case q=0 is empty.
Inverting F inserts only the separated phases

    (Nx/M1)^(it) (Ny/M2)^(it).                         (5)

For any term before or after the k projector, these are bounded norm
phases on the two columns and factor further between each column's
original inverse/plain inputs. Apply the unchanged smooth Poisson
kernel separation AFTER extracting (5). Its fixed seminorms are not
those of the sharply varying step. The quadratic and cubic sieve
constants are uniform in all phases (5), so no polynomial t cost is
introduced. Fourier inversion is justified absolutely by (4).

This proves uniformity of (1), up to logarithms, with either sharp
restriction NC<=Q or NC>Q, and simultaneously with the original
both-different restriction from Section 1. Fixed bad-prime conductor
factors are included in Lambda. No approximate conductor cutoff or
unpaid endpoint remains.

## 3. Rebuild the physical Poisson kernel under the radical filter

Let tau be the fixed smooth step from `JOINT_CONDUCTOR_CENTERING.md`
and insert the ACTUAL row weight

    rho_hi(u)=tau(N(rad u)/Q0).                        (6)

This is a new physical kernel; the unfiltered sixth-power sieve proof
is not reused without modification. Uniquely write each original
sixth-free row as

    u=e*z,  e squarefree, z powerful with exponents in {2,3,4,5},
    (e,z)=1.                                         (7)

Every row appears once. For fixed z, put X=U/Nz. The row profile in e
is the original fixed compact shape/ray profile, rotated by z, times

    tau(Ne*N(rad z)/Q0).

Its fixed-order Euler and angular derivatives are uniform in z,Q0:
on a transition the tau argument lies in [1,2], and otherwise tau is
constant. The fixed compact physical shape is only rotated and
rescaled. Its ray subdivision remains finite. Keep the outside
character value theta(z), including its literal zero at a ramified
prime, as a separated bounded column twist.

Expand squarefreeness of e EXACTLY by sum_(a^2|e)mu(a), and expand
the original zero-only mask, now including z, by its complete divisor
b. The new primitive Poisson prefactor and dual scale are

    P=U/[Lambda^(1/2) Nz (Na)^2 Nb sqrt(M1 M2)],
    H=M1 M2 Lambda Nz (Na)^2 Nb/U.                    (8)

All original coprimalities of a,z and the source columns remain. The
factors theta(a^2) and theta(z) give bounded separated coefficient
twists; no nonunit character value is inverted. Formula (8) replaces
the factor (Nd)^6 in the unfiltered proof by Nz*(Na)^2.

For every nonzero primitive dual frequency write h=j^3*v with v
cubefree. Apply the SAME unequal-length quadratic/projection hybrid
to j, including its full square replicas and all fixed bad-prime
frequency parts. The three resulting Poisson resources acquire the
following row-sieve factors, respectively:

    (Nz)^(-2/3) (Na)^(-4/3),
    (Nz)^(-3/4) (Na)^(-3/2),
    (Nz)^(-5/6) (Na)^(-5/3).                          (9)

Each a series converges over all ideals. Each z series converges over
all powerful ideals: its first possible prime term is p^(-2*s),
with s in {2/3,3/4,5/6}>1/2. Divisor losses from the additional z mask
are absorbed by choosing their prescribed subpower smaller than the
strict convergence margins. Thus EVERY physical powerful row part is
summed without a power loss. The remaining R,k,b,v resources and all
unequal-length cancellations are exactly those in the all-power proof.
The extra phases from Sections 1--2 do not change these positive
resource bounds.

The formal principal pair introduced by the coprimality extension
requires its own correction. For each z the nonzero-frequency smooth
lattice bound cancels the prefactor; there are O(sqrt(U/Nz)) available
squarefree sieve indices a, and the original column square mass is a
subpower. Summing all powerful z uses

    sum_(Nz<=CU,z powerful)(Nz)^(-1/2)<<_epsilon U^epsilon.

This gives O(U^(1/2+epsilon)), absorbed by the first term of (1).
The TRUE primitive-principal contribution remains separately O(U)
by the original complete coefficient-pair count; restricting rows by
(6) and input pairs by the both-different condition preserves that
absolute bound. Hence no formal principal replica is discarded.

We have therefore proved the following uniform scoped statement:

    |P_(rho_hi, both-different, NC>Q, Nv<=V)|
       <<_epsilon (UDNQVQ0)^epsilon B(U,D,N,V),        (10)

with the original common profile/height factors. The sharp opposite
conductor cutoff is also permitted. The sector in (10) is defined
using the exact row decomposition (7) and primitive Poisson (8).
Its frequency coordinates need not equal those in the unfiltered
sixth-power-sieve representation; the same representation is used
for BOTH selected and complementary terms here.

## 4. One exact complete simultaneous remaining form

At the synchronized corner D=U,N=sqrt(U), let E denote the complete
original positive mixed mean. Define C_open by the following exact
sequence on its original opened covariance:

* retain both original index inequalities d1!=d2,n1!=n2;
* insert rho_hi(u) from (6);
* retain the actual primitive pair conductor NC>Q1;
* use (7)--(8) and retain EVERY nonzero dual frequency whose cubefree
  core has Nv>V.

All original shared-prime masks, local classes, all-power components,
row sieve indices and Fourier tails are part of C_open. Conjugate
pairing makes it real. No positivity is claimed.

The original positive low-radical row estimate and the exact collision
strip centering in `JOINT_CONDUCTOR_CENTERING.md`, followed by (10),
give the single complete reduction

    E=C_open+O_epsilon(U^epsilon (1+T)^A *
        [U+U Q0/N+U^(1/2)Q1^(3/4)+B(U,D,N,V)]).        (11)

Using instead that note's exact low-row-count subtraction gives the
ALTERNATIVE reduction for the SAME C_open:

    E=C_open+O_epsilon(U^epsilon (1+T)^A *
        [U+U Q0/N+U^(1/6)Q1^(11/12)
                         +Q0 Q1^(1/2)+B(U,D,N,V)]).  (12)

For example either choice

    (Q0,Q1,V)=(U^(7/10),U^(9/10),U^(1/25)),
    (Q0,Q1,V)=(U^(51/80),U^(9/8),U^(1/25))

pays every displayed term in its corresponding reduction at
U^(6/5+epsilon). The last term of (1) reaches that exponent exactly;
the other two low-core terms have exponents 52/75 and 103/100.
This is one legally composed actual signed completion target, rather
than an inference from three unrelated paid sectors.

The upper bound C_open<<U^(6/5+epsilon) is OPEN, as is the corresponding
estimate on the full witness-length polygon. This note proves neither
a new full mixed mean nor a zero-free boundary.
