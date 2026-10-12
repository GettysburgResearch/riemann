# A literal Fourier-compact balanced sextic trace

Status: exact first-Poisson reduction and finite directed witness. The
quadratic trace correlations are cubic, but a signed mean estimate across
moving conductors remains unpaid. This document makes no asymptotic
generalized-moment or RH claim.

## F1. Source normalization and the face retained

Use K=Q(sqrt(-3)), O=Z[omega], omega=exp(2 pi i/3), and the literal source
additive character e(z)=exp(4 pi i Im(z)/sqrt(3)). Lebesgue measure is
normalized by c=2/sqrt(3), so O has covolume one. The Fourier transform is

    hat f(w)=c integral_C f(z)e(-zw) dx dy.

This is the normalization of the frozen OpenAI `qrh11-12.tex`, and of
PR914 `A2_COMPLETION.md`, SHA
`d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`,
commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`.

Let P be a set of 2k distinct primary prime ideals, with generators pi.
Set q=product_(p in P) pi. We retain the **prime-column** portion of the
literal Hermitian 2kth moment: each of its columns is one different prime
in P. All of these tuples lie on the fully coprime leading face. This is
a subface of the source's critical R_k; composite columns and the other
critical configurations remain present in the full R_k.

Write v_p=nu(p) W(Np/D). The Mobius signs contribute (-1)^(2k)=1.
For a subset A of P of size k, define

    chi_A(u)=product_(p in A) chi_p(u)
             product_(p notin A) conjugate(chi_p(u)),
    w_A=product_(p in A) v_p product_(p notin A) conjugate(v_p).

Every local character is the literal sextic residue character, extended
by zero at nonunits. Since all primes are distinct, chi_A is primitive
modulo q. It is not replaced by its cubic square. The source row sum is

    S_A(H)=sum_u Phi(Nu/H) chi_A(u).

Poisson summation, with the above normalization, gives exactly

    S_A(H)=H gamma(chi_A)/sqrt(Nq)
           sum_(h != 0) conjugate(chi_A(h)) Psi(H Nh/Nq),       (F1)

where Psi=hat Phi and gamma is the normalized Gauss sum using e(u/q).
The h=0 term vanishes because chi_A is primitive nonprincipal. The
ordered prime-column contribution is (k!)^2 sum_P sum_|A|=k w_A S_A(H).
There is no product-column diagonal in this face.

## F2. Exact reciprocity phases and balanced coefficient

For each p, let

    gamma_p=Np^(-1/2) sum_(a mod pi) chi_p(a)e(a/pi),
    sigma_p=chi_p(-1) in {+1,-1},
    a_p(h)=v_p gamma_p chi_p(q/pi) conjugate(chi_p(h)).

The factor chi_p(q/pi) is mandatory. CRT gives

    gamma(chi_A)=product_(p in A) gamma_p chi_p(q/pi)
                product_(p notin A)
                    sigma_p conjugate(gamma_p chi_p(q/pi)).   (F2)

Indeed the local CRT additive coefficient is the inverse of q/pi.
Changing that coefficient scales a Gauss sum by chi_p(q/pi). Also
gamma(conjugate chi_p)=chi_p(-1) conjugate(gamma_p).

Consequently the entire balanced Fourier coefficient is

    T_P(h)=[z^k] product_(p in P) (z a_p(h)+sigma_p conjugate(a_p(h))). (F3)

This formula retains both reciprocity and the local minus signs. It is
not a positive envelope. If h is divisible by any p in P, every monomial
vanishes. Equation (F1) becomes the concrete prime-face identity

    R_k,prime^Phi=(k!)^2 H sum_P (Nq)^(-1/2)
                   sum_(h != 0) Psi(H Nh/Nq) T_P(h).           (F4)

This identity is new bookkeeping of a specified source subface, not an
estimate for it. For general composite columns the column norm profile
does not factor independently prime by prime. One must retain the full
partition-dependent column weights; (F3) cannot be applied to those
weights by pretending they are multiplicative.

## F3. The free radial unit projection

Put zeta6=1+omega. In the literal residue field

    chi_p(zeta6)=zeta6^j_p, j_p=(Np-1)/6 modulo 6.

A radial Psi has the exact orbit projection

    T_P,0(h)=(1/6) sum_(epsilon in mu_6) T_P(epsilon h).

Its balanced allocation A survives precisely when

    sum_(p in A) j_p - sum_(p notin A) j_p =0 modulo 6.        (F5)

All other allocations are exactly zero after radial summation. This
removes a finite congruence class of prime configurations. It is not a
power saving in D. For surviving allocations chi_A(-1)=1; complementing
A therefore conjugates its whole Gauss-weighted term. Thus the complete
radial balanced sum is real. The source phases and zero extensions still
remain in every surviving term.

## F4. Quadratic correlations are exactly cubic

This is a useful smaller arithmetic module, with a strict limitation.
Let A_0 be the collection of neutral allocations in (F5). Write

    T_P,0(h)=sum_(A in A_0) c_A conjugate(chi_A(h)),
    c_A=w_A gamma(chi_A).

For A,B in A_0, the quotient character is

    chi_B(h) conjugate(chi_A(h))
      = product_(p in B\A) chi_p(h)^2
        product_(p in A\B) conjugate(chi_p(h)^2),             (F6)

with the literal additional nonunit mask at primes outside A triangle B.
For A!=B it is a nonprincipal primitive cubic character on the symmetric
difference. Its zero extension at the remaining primes is retained.
For any weight w(h), finite or absolutely summable, this gives the exact
identity

    sum_h w(h)|T_P,0(h)|^2
      = (sum_A |c_A|^2) sum_((h,q)=1) w(h)
        + sum_(A!=B) c_A conjugate(c_B)
          sum_h w(h) chi_B(h) conjugate(chi_A(h)).             (F7)

In particular, over a complete residue period modulo q,

    sum_(h mod q) T_P,0(h)=0,
    sum_(h mod q)|T_P,0(h)|^2
       = phi_K(q) |A_0| product_p |v_p|^2.                   (F8)

Local cubic orthogonality proves the second identity; the first uses
nonprincipality at every prime. Neither claim assumes random phases.

The cubic large-sieve/dispersion input could price the weighted quadratic
module (F7), provided it retains its moving coprimality masks, reciprocal
phases, actual norm window and conductor range. It does **not** price the
signed linear functional in (F4). Cauchy in h throws away the needed
linear cancellation. Cross-conductor products T_P conjugate(T_P') have
sextic characters at primes in only one conductor; (F6) is confined to a
fixed P. Therefore a cubic within-conductor estimate cannot be silently
used as a cross-conductor signed mean estimate.

## F5. A precise conditional prime-face contract

For primes in a fixed source norm range [ell D,u D], let v_p be the
actual fixed-character, fixed-profile source weights. Let Psi be the
actual radial compact Fourier transform of an admissible source Phi.
The following explicit signed trace input is sufficient for this
prime-column face at H=D^(1+theta):

    | sum_P (Nq)^(-1/2) sum_(h!=0)
          Psi(H Nh/Nq) T_P,0(h) | << D^(k+epsilon).           (OPEN-F9)

The constants must be uniform in D at fixed theta>0 and fixed profile
seminorms, including every moving conductor and source character zero.
Together with F4 this pays R_k,prime^Phi << H D^(k+epsilon).
This conditional module is explicitly unpaid. It is only the prime face;
it is not sufficient for the full generalized moment until the remaining
composite-column and coupled critical faces are also paid.

Unlike a positive energy substitute, OPEN-F9 retains the balanced local
trace, unit projection and reciprocity phase. Equations F6--F8 identify
the tractable cubic variance part and the additional interference that
must be estimated. There is no claim that the contract is already supplied
by the cited cubic first-moment paper or by PR912--917.

## F6. A positive radial Fourier-compact native test

Take a disk of radius R=1/4 in Fourier coordinates, divide its transform
by its value at zero, and square its absolute value. Explicitly

    Phi(x)=4 [2 J_1((pi/sqrt(3))*sqrt(x))
                  / ((pi/sqrt(3))*sqrt(x))]^2.                (F10)

The value at x=0 is 4 by continuity. Its Fourier transform is

    Psi(r^2)=4 sqrt(3)/(2 pi^2 R^4)
             [2R^2 acos(r/(2R))-(r/2)sqrt(4R^2-r^2)]         (F11)

for 0<=r<2R, and is zero for r>=2R. The factor 2/sqrt(3) in the
source transform is included in F11. This Psi is nonnegative and has
norm support x<=1/4.

For 0<=x<=1, the alternating Bessel series gives

    2J_1(y)/y >=1-y^2/8,
    Phi(x)>=4(1-pi^2/24)^2>1.

The series terms decrease for 0<=y<=pi/sqrt(3), so the lower bound is
valid. Thus this positive window majorizes the native ball Nu<=H.
Its spatial tail is O((1+|u|)^(-3)); its lattice sums are absolutely
convergent. Poisson can also be obtained as a limit of genuine Schwartz
source tests, as explained next. It is not the old compact **spatial**
cutoff from the 1176/456 witness.

## F7. A paid genuine Schwartz variant

Convolve the Fourier disk with any nonnegative radial C-infinity
probability mollifier of radius delta=10^-12. The new Fourier disk is
smooth compactly supported; its squared normalized transform Phi_delta
is nonnegative Schwartz. Its Fourier transform is Psi convolved with
the probability autocorrelation of that mollifier.

The disk-overlap area has radial derivative bounded by 2R. Therefore
the globally extended Psi is Lipschitz with constant

    4 sqrt(3)/(pi^2 R^3)<45.

Hence |Psi_delta-Psi|<=90 delta everywhere. Its norm support is
at most (1/2+2delta)^2. For |u|<=1, the normalized mollifier transform
has distance from 1 at most 4pi delta/sqrt(3). The strict lower bound
in F6 therefore still gives Phi_delta>=1 on [0,1].

For the finite native conductors below, Nq is odd. The checker proves

    max Nq (2delta+4delta^2)<1/4,

so the mollification introduces no additional dual lattice norm: the
old integer cutoff N(h)<Nq/160 remains the same. For X=Nq/160>=1,
the exact norm box gives at most 16X=Nq/10 lattice points. There are
at most six balanced allocations. The full native leading sum changes
by at most

    8640 delta sum_P sqrt(Nq) < .001.                        (F12)

This pays the replacement by an actual admissible smooth source test.
No uniform asymptotic source theorem for the nonsmooth limit is asserted.

## F8. Directed native experiment

The checker uses the same eight primary prime ideals as the old native
witness, over rational norms 7,13,19,31 and both conjugate prime ideals.
Set D=30, H=40 and take the actual prime coefficients v_p=1. A fixed
compact smooth W with these values at the four prime norms gives these
coefficients with trivial fixed nu. Mobius signs remain -1 at each prime
and cancel only because the face has four columns.

Every one of the 70 distinct four-prime sets, its six balanced
allocations, all dual lattice norms in the exact support, all six units,
and every primitive/nonunit character value are checked. Normalized
Gauss sums are independently evaluated over the actual residue fields
using e(a/pi), and CRT scaling is computed from actual Eisenstein products.
The directed result is a strictly positive leading contribution between
3916 and 3917. Positive and negative individual conductor contributions
both occur. Omitting the CRT phase or the local chi(-1) changes the
answer by more than one; these are required negative controls.

Consequently this specified prime-column subface is not killed by radial
unit projection, Fourier-compact support or the zero-frequency subtraction.
The actual smooth Schwartz variant still has a positive leading contribution
by F12. It can coexist with cancellation from other critical faces; this
is not a lower bound for the full R_2. The calculation does not prove or
disprove OPEN-F9, which is an asymptotic uniform estimate.
