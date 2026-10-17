# A native angular hull at radial parameter zero

Status: an unconditional source-specific obstruction, accompanying
NATIVE_ANGULAR_RAY_MOMENT.md. It proves actual native peaks at moving angular
characters while the radial parameter stays zero. It does not place a peak
at the fixed principal angular character. No estimate of the size of the
required angular integer is asserted.

Keep K=Q(omega), the fixed squarefree Q divisible by 6, its rationally
saturated excluded set S, and psi_l from the companion theorem.

## 1. Exact angular orbit limit

For every split rational prime p not dividing Q choose one of its two
prime ideals pfrak=(alpha_p). Its angular value is

    psi_1(pfrak)=(alpha_p/conjugate(alpha_p))^3.

For a finite collection of such primes, these values have no nontrivial
integer relation with product one. Indeed, taking the fractional ideal
of a proposed relation gives

    product_p (pfrak/conjugate(pfrak))^(3 n_p)=(1).

Unique ideal factorization forces every n_p=0. Thus the integer orbit
l -> (psi_1(pfrak)^l)_p is dense in the corresponding finite torus. One
elementary proof averages a smooth bump by its absolutely convergent
Fourier series: every nonconstant Fourier term is a geometric progression
with ratio different from one, whose Cesaro average tends to zero.
The limiting average is the positive torus integral of the bump.

Consequently there are arbitrarily large integers l approaching the value
-1 simultaneously at any finite list of split primes. The conjugate prime
ideal also approaches -1, since its angular value is the inverse. Inert
prime ideals are rational ideals and have angular value exactly +1 at
every integer l. A diagonal sequence l_j can therefore be chosen for which
every individual native ideal coefficient has the limit

    mu_K^S(I) psi_(l_j)(I) -> c_Q(I),
    c_Q(I)=mu_K(I)^2 1_((I,S)=1)
                       (-1)^(number of inert prime-ideal factors of I).

The inert signs remain in this formula. This is not a wholly unsigned
orbit limit.

## 2. An exact Euler quotient and an elementary positive-density estimate

For Re s>1, the full limit source has Euler series

    sum_I c_Q(I)(NI)^(-s)
      =product_(p split, p not dividing Q)(1+p^(-s))^2
         product_(p inert, p not dividing Q)(1-p^(-2s))
      = zeta_K^S(s) / zeta_Q^Q(2s)^2,                    (2.1)

where zeta_Q^Q(s)=zeta(s) product_(p|Q)(1-p^(-s)). The equality is local:
dividing by the split Euler factor of zeta_K contributes
(1-p^(-2s))^2, and the same factor results at an inert prime. Excluding
the ramified prime and imposing rational saturation are used here.

Write a_Q(d)=(mu^Q * mu^Q)(d), where mu^Q(d)=mu(d)1_((d,Q)=1).
Then |a_Q(d)|<=d_2(d), and coefficient convolution in (2.1) gives

    sum_(NI<=Y)c_Q(I)
       =sum_(d<=sqrt(Y)) a_Q(d) I_K^S(Y/d^2),

where I_K^S(u)=kappa_S u+O_Q(sqrt(u)), u>=1, and
kappa_S=Res_(s=1)zeta_K^S(s)>0. Using

    sum_(d<=Z)d_2(d)/d << log(3Z)^2,
    sum_(d>Z)d_2(d)/d^2 << log(3Z)/Z,

which follow directly from d_2(d)=sum_(ab=d)1 and elementary partial
summation, yields the unconditional arithmetic estimate

    sum_(NI<=Y)c_Q(I)=c_Q Y+O_Q(sqrt(Y)log(3Y)^2),          (2.2)
    c_Q=kappa_S / zeta_Q^Q(2)^2 > 0.

Here c_Q without an ideal argument denotes the constant, not the coefficient.
For the native exclusion Q=6 this constant is

    c_6=9sqrt(3)/(2pi^3).

There is no zero-free hypothesis, Tauberian assertion, or unproved prime
distribution estimate in (2.2).

## 3. Finite native peaks and the necessary angular width

For the original hard window (X/2,X], (2.2) gives

    sum_(X/2<NI<=X)c_Q(I)=c_Q X/2+O_Q(sqrt(X)log(3X)^2).

At each sufficiently large X this is at least c_Q X/4. The window is finite,
so the orbit approximation in Section 1 supplies an integer l_X for which

    Re A_(0,l_X)(X) >= c_Q X/8.                          (3.1)

The coefficients are the unchanged native Mobius coefficients. The radial
parameter is **exactly zero**, not a moving Kronecker center. The angular
center l_X may depend on X and may be extremely large.

Since p_R(0)>=1/(1+sqrt(2pi)R), keeping the single nonnegative term l=l_X
in the finite angular second moment proves

    M_R(X;0,l_X) >= c'_Q X^2/(1+R).                      (3.2)

For R>=1 this matches the X^2/R term in the companion theorem. A bound
M_R=O_Q(X) uniform in angular centers therefore requires R of order at
least X. The same argument yields the lower bound X^(2k)/(1+R) for each
fixed even moment 2k.

This sharpens the scope of the earlier moving-radial-center obstruction in
[PR #963, Section 6](https://github.com/GettysburgResearch/riemann/blob/c91fd9ddfb37668338d9aec22c0e29cfe741cf07/standalone/2026-10-17-archimedean-ideal-resolution/PROOF.md): the radial center can now be fixed
at zero, with the angular center carrying the resonant orbit instead.
It does not obstruct a theorem restricted to the fixed principal angular
character l=0. It does rule out converting the new angular-only mean into
a uniform pointwise theorem by discarding its averaging cost.
