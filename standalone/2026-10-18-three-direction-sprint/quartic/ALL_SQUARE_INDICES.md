# All square indices in a quartic bilinear period

**PROPOSED late addendum, 18 October 2026.** This supplements the
three-direction research packet. It derives an arithmetic completion of
the known squarefree-square formula. It does not construct the required global period, prove a new
zero-free region, or assume nonvanishing of the first Fourier coefficient.

## 1. Normalizations and imported interfaces

Put F=Q(i), O=Z[i], lambda=1+i, and S={lambda}. An ideal prime to S is
represented once by its primary generator c=1 mod lambda^3. Write q=N(pi).
Use the quartic Gauss sum

    g(nu,c)=sum_(a mod c) (a/c)_4 exp(2 pi i Tr(nu a/c)),
    gtilde(nu,c)=g(nu,c)/sqrt(Nc).

The precise primary source is David--Dunn--Hamieh--Lin (DDHL),
*Quartic Gauss sums over primes and metaplectic theta functions*,
[arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2), 10 May 2025.
The imported identities used below are (3.2)--(3.11), meromorphic continuation
and the at-most-simple pole at z=5/4 in (4.1)--(4.2), and Suzuki's residue
identities (4.36), (4.38), in DDHL's stated sign convention. These are
classical inputs. The immutable repository starting point is
[PR #1005's quartic note](https://github.com/GettysburgResearch/riemann/blob/d3b3d19573b8dc47ac6e37abd108d54982e9e5f1/standalone/2026-10-18-amplified-boundary-and-global-attacks/field/PRINCIPAL_CORRELATIONS_AND_QUARTIC.md),
blob a2b9b84a6596cc6236b0f7d6705c357772b40db2. Suzuki's ORIGINAL
*The biquadratic theta series* (1983), Theorem 3, printed page 114,
in fact states the full fourth-power periodicity with no coprimality
restriction; see the
[primary scan](https://gdz.sub.uni-goettingen.de/content/PPN243919689_0340/1000/0/00000118.jpg).
This was visually checked independently of the narrower DDHL quotation.
Section 3 below is an independent reconstruction of this CLASSICAL
periodicity from the finite Gauss table and the weaker quoted interface,
not a claim to a new periodicity theorem. Section 4 combines these
classical identities into the Euler completion. No step repeatedly applies
a coprime statement where its coprimality hypothesis fails.

For beta in {1,beta1}, beta1=1+lambda^3=-1+2i modulo 4, define

    F_beta(z,nu)=sum_(c primary, c=beta mod 4) g(nu,c)/(Nc)^z,
    f(nu)=Res_(z=5/4) (F_1(z,nu),F_beta1(z,nu))^T,
    v0=f(1),             J=[[0,1],[-1,0]].

DDHL (4.38) says, for squarefree primary r,

    f(r^2)=conjugate(gtilde(1,r)) (Nr)^(-1/4) R(r) v0,
    R(r)=I if r=1 mod 4, and R(r)=J if r=beta1 mod 4.       (1)

No normalization v0=1, or even v0!=0, is imposed.

## 2. The exact Gauss-square codec and its limits

Set epsilon(c)=(-1/c)_4 c/|c|. On primary generators this is a multiplicative
unitary Hecke character; its finite conductor divides lambda^4 and its
angular type is 1. It is not a constant phase. The prime square formula,
quartic reciprocity and CRT give

    gtilde(1,c)^2=mu_F(c) epsilon(c)                         (2)

for EVERY primary c. For an inert prime the primary generator is pi=-p,
p=3 mod 4: gtilde(1,pi)=1, mu(pi)=-1 and epsilon(pi)=-1, so (2) still holds.
For a nonsquarefree c the Gauss sum with numerator 1 vanishes. For coprime
primary moduli the CRT factor has square 1, which proves multiplicativity
of the squared normalized sum including the zero cases.

For squarefree c and any numerator a, the exact extension is

    gtilde(a,c)^2=mu(c) epsilon(c) (a/c)_2,                 (3)

with the quadratic symbol extended by zero at shared primes. It does NOT
extend to all nonsquarefree moduli with a moving nonunit numerator. For
example g(pi,pi^2)=q g_2(pi), so gtilde(pi,pi^2)^2=q, whereas mu(pi^2)=0.
Such shared-prime branches must be retained in a putative unfolding.

## 3. Complete prime-power residue recurrence

**Claim.** If pi is a primary prime different from lambda, (pi,nu0)=1,
and j>=0, then

    f(pi^(4j) nu0)=f(nu0),
    f(pi^(4j+2) nu0)=f(pi^2 nu0).                          (4)

This includes both primary congruence classes, inert primes, and all j.

Here is the full two-ray calculation. Let eta(c)=(Nc-1)/4 modulo 2,
a_pi=(-1/pi)_4=(-1)^eta(pi), and define the finite operator

    (T_pi h)_beta=(-1)^(eta(pi)*eta(beta*pi^(-1)))
                      h_(beta*pi^(-1)).

Indices are primary classes modulo 4. Thus T_pi=I for eta(pi)=0,
T_pi=-J for eta(pi)=1, and T_pi^2=a_pi I.

For t=0,2 let H_t(z) be the two-ray vector

    sum_(c primary, (c,pi)=1) g(nu0,c) (pi/c)_4^(-t)/(Nc)^z.

The ray component is specified by the class of c. Put G=g(nu0,pi),

    A(z)=G q^(-z) T_pi,
    B(z)=q^2 a_pi conjugate(G) q^(-3z) T_pi.

Since |G|^2=q, these satisfy

    A(z)B(z)=B(z)A(z)=q^(3-4z) I.                       (5)

Splitting each modulus as pi^ell c with (pi,c)=1, the local table DDHL
(3.7) leaves, for numerator pi^(4j)nu0 or pi^(4j+2)nu0, exactly
ell=0,4,...,4j and the last exponent ell=4j+1 or 4j+3. The local terms
ell=4i contribute phi(pi^(4i))q^(-4iz); the last term is the fixed
quartic Gauss branch. CRT and reciprocity give, on the absolute initial
line and then meromorphically,

    F(z,pi^(4j)nu0)=Q_j(z)H_0(z)+r(z)^j A(z)H_2(z),
    F(z,pi^(4j+2)nu0)=Q_j(z)H_2(z)+r(z)^j B(z)H_0(z),   (6)

where r(z)=q^(4-4z) and

    Q_j(z)=1+(1-q^(-1)) sum_(i=1)^j r(z)^i.

For j=0 this is the system F(z,nu0)=H_0+A H_2 and
F(z,pi^2 nu0)=H_2+B H_0. Its determinant is a power of
1-q^(3-4z), nonzero at z0=5/4. Consequently H_0,H_2 are meromorphic
there with at most simple poles; let their residue vectors be h_0,h_2.
At z0, r=q^(-1) and AB=q^(-2)I.

The IMPORTED coprime identity f(pi^4 nu0)=f(nu0), applied only here
where (pi,nu0)=1, and the j=1 instance of (6) give

    A(z0)h_2=q^(-1)h_0.

Multiplying by B(z0) and using (5) yields B(z0)h_0=q^(-1)h_2.
Finally

    Q_j(z0)+q^(-j-1)=1+q^(-1).

Substitution in both equations (6) proves (4). This argument pays every
local prime power; it does not assume that a repeated pi remains coprime.

Every primary m has a unique decomposition m=d^2 r with r squarefree
primary, and (d,r) is UNRESTRICTED. Apply (4) prime by prime, extracting
the full valuation at the prime under consideration. It follows that

    f(m^2)=f(r^2).                                          (7)

Also d^2=1 mod 4 for every primary d, hence R(r)=R(m). Even a direct
ray correction therefore depends only on a fixed congruence class,
not on a growing squarefree-core computation.

## 4. Fixed bilinear cusp pairings and their Euler products

Let B be a symmetric 2-by-2 matrix satisfying J^T B J=kappa B,
where kappa is +1 or -1, and put Q_B(w)=w^T B w. The matrices I
and diag(1,-1) suffice: if v0!=0, their two values cannot both vanish.
The off-diagonal symmetric matrix is another kappa=-1 choice.
Define the finite ray character delta_kappa(m)=kappa^eta(m).
Equations (1), (2), (7) imply exactly

    Q_B(f(m^2))
      =mu(r) conjugate(epsilon(r)) delta_kappa(r)
                        (Nr)^(-1/2) Q_B(v0),   m=d^2 r.    (8)

Thus no m-dependent matrix is needed: a FIXED finite collection of
bilinear cusp pairings, with a fixed finite character, suffices.
For any fixed unitary Hecke character chi unramified outside S, absolute
convergence for Re(s)>1 and the independent d,r factorization give

    sum_(m primary, (m,S)=1) chi(m) (Nm)^(1/2-s) Q_B(f(m^2))
       =Q_B(v0) L_F^S(2s-1,chi^2)
                    /L_F^S(s,chi*conjugate(epsilon)*delta_kappa). (9)

For a character ramified at further primes, first enlarge S to include
all its conductor primes and restrict m, d and r to be prime to this
enlarged set. All L-functions in (9) have these same Euler deletions,
even when chi^2 has smaller primitive conductor. The target character
epsilon*delta_kappa below is already unramified outside the original S.

Indeed Nm=(Nd)^2 Nr; the d sum is L(2s-1,chi^2), while the squarefree
r sum is the reciprocal L-function. Shared primes between d and r
are allowed and are essential to this independent Euler factorization.
Choosing chi=epsilon*delta_kappa yields the complete target identity

    sum_m epsilon(m)delta_kappa(m)(Nm)^(1/2-s)Q_B(f(m^2))
       =Q_B(v0) L_F^S(2s-1,epsilon^2)/zeta_F^S(s).          (10)

Conjugating the whole coefficient identity instead gives the conjugate
character epsilon^(-2). Untwisted kappa=+1 gives
zeta_F^S(2s-1)/L_F^S(s,conjugate(epsilon)); it does NOT target ordinary
zeta. The angular compensation cannot be omitted.

This proves the arithmetic completion of the nonsquarefree square
indices. It does not assert that the Hecke character in the ROOT m
has already been implemented by an automorphic kernel in the Fourier
index nu=m^2. Its archimedean type and fixed local sections must match.
In particular, an ordinary Hecke twist in nu with integral angular
type k has angular type 2k on nu=nu_a m^2. The squared original
quartic coefficient has residual angular type -1 in m. Consequently
such an ordinary index twist cannot make this squarefree piece
principal, since 2k-1!=0. Finite characters do not change that
archimedean type. This only rules out that simple substitution; it
does not rule out a Weil or descent kernel whose original variable is m.

### 4a. A fixed nonzero squareclass exists without assuming v0!=0

The base v0=f(1) used in (9)--(10) need not be declared nonzero.
There is instead a fixed nonzero nu_a with v_a=f(nu_a)!=0, as follows.
Take the quartic Eisenstein residue theta_(i1), where i1 is the cusp 0
in DDHL. Use the DIRECT diagonal constant-term formula immediately
after DDHL (4.22), at its OWN cusp i1:

    Vol*phi_(i1,i1)(z,0,0)
      =2/(2^(4z-4)-1)*zeta_F^S(4z-4)/zeta_F^S(4z-3).

Its residue at z=5/4 is nonzero. The other fixed factors, including
K(0,z,0) and the cusp volume, are finite and nonzero there. Therefore
theta_(i1) is a nonzero automorphic function. This uses no symmetry
or transposition of the scattering matrix's two cusp indices.
If every nonzero Fourier coefficient of theta_(i1) vanished, DDHL
(4.34) would give theta_(i1)(z,y)=C y^(3/4) throughout H^3.
If C=0 this contradicts its nonzero residue at its own cusp.
If C!=0, use automorphy as follows.
But gamma=[[1,0],[lambda^4,1]] lies in Gamma_1(lambda^4) and has
quartic multiplier 1. At z=0 it changes y to

    y/(1+N(lambda^4)y^2),

contradicting that function's automorphy. Hence some nonzero Fourier
coefficient tau_(i1)(nu_a) is nonzero. By DDHL (4.35), v_a=f(nu_a)
is a nonzero two-component vector. This is an existence proof of a
fixed base index, not an effective computation of its smallest value.

Enlarge S to S_a=S union {prime ideals dividing nu_a}. This includes
lambda even if nu_a is lambda-divisible. Restrict m to be prime to S_a.
Section 3 applies with this base because every extracted prime is now
coprime to nu_a, and (4) pays every repeated valuation of m.
Let xi_a(m)=(nu_a/m)_2 be the quadratic Hecke character on this
prime-to-S_a support. The moving-numerator square identity (3) gives

    Q_B(f(nu_a m^2))
      =mu(r) conjugate(epsilon(r)) xi_a(r) delta_kappa(r)
                           (Nr)^(-1/2) Q_B(v_a), m=d^2 r.

Choose one of B=I or diag(1,-1) for which Q_B(v_a)!=0, and set
chi_a=epsilon*xi_a*delta_kappa. Because xi_a and delta_kappa are
quadratic, chi_a^2=epsilon^2 on the stated support. The complete
fixed-squareclass identity is therefore

    sum_(m primary, (m,S_a)=1)
       chi_a(m)(Nm)^(1/2-s) Q_B(f(nu_a m^2))
      =Q_B(v_a) L_F^(S_a)(2s-1,epsilon^2)/zeta_F^(S_a)(s),
      Re(s)>1.                                             (10a)

Thus a nonzero arithmetic coefficient object is available without an
unproved first-coefficient assumption. Its desired selector is one
fixed squareclass nu_a m^2, instead of the pure-square class m^2.
All additional target Euler factors are fixed factors 1-(Np)^(-s),
nonzero for Re(s)>0. The numerator, angular realization and global
squareclass-selector gates remain unchanged.

## 5. Actual radial Mellin variable and the ramified scope

DDHL (4.34) has nonzero Fourier modes

    c tau_i(nu) (Nnu)^(1/8) y K_(1/4)(pi |nu|y) e(nu z/lambda^4),
    c=2^(3/4)pi^(5/4)/Gamma(5/4).

DDHL (4.35) is tau=(1/Vol)diag(1,-1)f. The fixed diagonal change
of basis preserves the two pairing types above. Use Haar mass 1 on
the Fourier torus. The formal nonzero-mode Mellin integral against y^s
and hyperbolic radial measure y^(-3) dy is

    C(s) sum_(nu!=0) Q_B(tau(nu)) (Nnu)^(1/4-s/2),
    C(s)=c^2 pi^(-s) 2^(s-3)
           Gamma(s/2)^2 Gamma(s/2+1/4) Gamma(s/2-1/4)/Gamma(s), (11)

where the scalar Bessel integral converges for Re(s)>1/2. At nu=m^2,
the weight is EXACTLY (Nm)^(1/2-s), so the target variable in (10)
is s, not s+1/2. Formula (11) is a computation of a Fourier-mode
Mellin integral, not a claim that a noncuspidal global unfolding is
absolutely convergent or already regularized.
For the fixed-squareclass construction (10a), the additional radial
factor is exactly (Nnu_a)^(1/4-s/2), which is entire and nonzero.

The arithmetic sums here use primary m prime to lambda and the
corresponding plus-square unit class. Full torus expansions include
other unit classes and lambda-divisible indices. These are not silently
identified with (10). A fixed finite Fourier projection can select
indices coprime to lambda at a cusp; its global oldform/cusp terms
still belong in an actual adapter. We have NOT computed every ramified
coefficient. The target Euler correction is explicit:

    zeta_F^S(s)=(1-2^(-s))zeta_F(s).

It has no extra zero or pole for 0<Re(s)<1. This is sufficient for
ordinary-zeta zero transfer IF an estimate for the actual reciprocal
target is eventually proved, since zeta_F=zeta L(s,chi_-4).

## 6. What the period has not yet supplied

The Gaussian reflection z -> -z is induced by diag(i,-i). On the
DDHL congruence group it preserves the quartic multiplier, since the
extra factor (-1/a)_4 is 1 for a=1 mod 4. Therefore the product
theta_4(z,y)theta_4(-z,y) has quadratic multiplier; a compatible
quadratic Eisenstein can compensate its central weight. This is a
real opening, not a central-character no-go.

But torus orthogonality gives the signed diagonal over ALL indices:

    CT_z theta_4(z,y)theta_4(-z,y)=sum_nu A_nu(y)^2.

It does not select nu=m^2. The coefficients at non-square indices,
including the generally undetermined prime coefficients, remain.
Inserting an Eisenstein Fourier expansion without unfolding instead
adds the relation nu-eta+rho=0. A square-index projector is an exact
horospherical L2 contraction, but its Weyl/scattering transform is
not supplied by that fact. A two-torus expression with a quadratic
theta formally imposes two equal square indices; addition of the two
unipotent coordinates is not itself a homomorphism G x G -> G, so
a higher-rank/Jacobi kernel would need an actual construction.

There are also cusp constants proportional to y^(3/4). Their products
require cancellation or a full truncation/regularization argument;
one cannot simply assume a half-plane of naive absolute unfolding.

Finally (10) alone need not retain a pole at every zeta_F zero rho:
L(2rho-1,epsilon^2) might vanish there. A previously known Hecke
boundary beta only prevents this when Re(rho)>(1+beta)/2, which is
weaker. One must either prove the numerator is nonzero at the relevant
zeros, implement a justified deflation, or derive a different complete
period identity where its cancellation is legitimate.

For clarity, the quadratic Ramanujan constant-term calculation gives
the local ratio

    (1-chi(pi)^2 q^(1-2s))/(1-chi(pi)^2 q^(2-2s)),

and hence a scattering ratio L(2s-2,chi^2)/L(2s-1,chi^2). This does NOT
automatically divide (10) by its numerator. An Eisenstein series with
unipotent seed coefficient 1 unfolds with that seed normalization;
its Fourier denominator is already part of the same Eisenstein
series. Counting it again as an independent scalar would double-count
normalization. Dividing the entire series by an L-function is another
potentially singular operation unless the exact adapter justifies it.

The formal replica-deflation coefficients have square sum
sum_d (Nd)^(2-4sigma)<infinity for sigma>3/4. This does not prove a
bounded automorphic action: dilation ranges overlap at common square
multiples, and on a fixed Mellin component the dilations are coherent
scalar phases. A genuine operator Gram or dispersion estimate is
needed; square summability alone cannot yield reciprocal-L
holomorphy in a region where its zeros are unknown.

**Conclusion at proved scope.** The entire prime-to-lambda square-index
piece, with every repeated/shared prime retained, has the explicit
Euler completion (9)--(10). The remaining task is a square-selecting,
correctly normalized, regularized automorphic adapter and a complete
estimate. No new strip follows from this arithmetic identity alone.
