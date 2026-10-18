# The chosen full-RH route: primitive, zero-preserving determinant profiles

Status: **proposed complete identities and a precise unresolved arithmetic
estimate. RH is not proved.** The identities below audit and advance one
route: use integral determinants, but remove the arithmetic convolution that
can hide a prescribed zero before attempting a height bound. The lcm,
confluent-Vandermonde and Riesz-mean formulas are classical. No novelty is
claimed for those formulas or for the resulting RH criterion. The useful
connection here is the explicit accounting of what is lost and retained by
operations on the imported determinant, and its exact connection to #991's
fixed prime source. The improved real-character bound is proved separately
in RECTANGULAR_JETS.md; it is not an assumption in this note.

## 1. The full valuation profile can be recovered, but its inequality cannot

For a prime p and integer S>=1, extend the lower template from Lemma 2 to
real x>=1 by

    E_p(x,S)=2 sum_(h=1)^(S-1)(S-h)(x-ph)_+.

At integer x=R this equals (4) of RECTANGULAR_JETS.md, including endpoints.
Set E_p(x,0)=0. Its discrete second difference at S=h is exactly

    E_p(x,h+1)-2E_p(x,h)+E_p(x,h-1)=2(x-ph)_+.            (1)

Thus the underlying templates retain prime-resolved triangular profiles.
For a quadratic character chi, put

    F_S(x)=(1/(2x))sum_(chi(p)=-1) E_p(x,S)log p,
    H_S(s)=sum_(h=1)^(S-1)(S-h)h^(-s),
    P_-(s)=sum_(chi(p)=-1)log p p^(-s).

Finite summation and absolutely convergent integration give, for Re s>1,

    integral_1^infinity F_S(x)x^(-s-1)dx
                     =H_S(s)P_-(s)/[s(s+1)].             (2)

Indeed integral_(ph)^infinity (1-ph/x)x^(-s-1)dx
=(ph)^(-s)/[s(s+1)]. For S=2, H_2=1: the profile has no extra Mellin zero.

This is NOT an upper bound for a second difference of actual determinants.
If log det G_S>=L_S, its slack can be arbitrarily large at the middle index;
one cannot subtract three one-sided inequalities to bound Delta^2 L_S.
A valid continuation must estimate those slacks or a specific determinant
quotient. Formula (1) alone supplies neither estimate.

## 2. Inert primes can hide COMMON zeros

Let P_0(s)=sum_p log p p^(-s), P_chi(s)=sum_p chi(p)log p p^(-s),
and R_q(s)=sum_(p|q)log p p^(-s). Then exactly

    P_-=(P_0-P_chi-R_q)/2,
    P_+=(P_0+P_chi-R_q)/2.                                (3)

The prime-power tails in

    P_0=-zeta'/zeta-Q_0,  P_chi=-L'/L-Q_chi

converge normally for Re s>1/2: their terms have exponents k>=2.
At a nontrivial point rho with Re rho>1/2, let m_0 and m_chi be the zero
multiplicities of zeta and L, with zero meaning no zero. Then

    Res_rho P_-=(m_chi-m_0)/2,
    Res_rho P_+=-(m_chi+m_0)/2.                           (4)

A common zero of equal multiplicity disappears from the inert profile.
The split profile would retain it, but the imported Frobenius argument
specifically pays inert primes. This is a concrete failure of an automatic
extension from real exceptional characters to arbitrary zeta zeros. It
cannot be repaired by ignoring common zeros or postulating simplicity.
No actual common or off-line zero is asserted by this observation.

## 3. An all-prime integer determinant can also lose the zeros

Consider the rational Hermite evaluation matrix of the monomials
1,z,...,z^(NJ-1) at nodes 0,...,N-1, with ordinary derivatives j=0,...,J-1.
Confluent Vandermonde gives its determinant, up to orientation sign,

    V_(N,J)=(product_(j=0)^(J-1)j!)^N
                  product_(0<=a<b<N)(b-a)^(J^2).        (5)

Its Gram determinant is V_(N,J)^2. This is a positive integer involving
ALL primes, not a character-selected set. After removing the explicit jet
factor, the underlying integer is

    B_N=product_(m=1)^(N-1)m^(N-m)=product_(k=1)^(N-1)k!.

Define the continuous log-volume profile

    B(x)=sum_(n<=x)(x-n)log n, so B(N)=log B_N.            (6)

Nevertheless its normalized Mellin transform is

    integral_1^infinity [B(x)/x]x^(-s-1)dx
                             =-zeta'(s)/[s(s+1)].        (7)

There is NO reciprocal zeta factor in (7). At a zero of zeta, the numerator
is still holomorphic; at a multiple zero it may vanish. Integral Gram
positivity and exact prime divisibility have not supplied a zero detector.
The reason is the identity log n=sum_(d|n)Lambda(d): an extra zeta factor
has canceled every logarithmic-derivative pole. This calibration prevents
mistaking determinant integrality itself for the missing RH mechanism.

## 4. Remove that convolution exactly, without discarding integrality

Define a signed dilation of the whole profile, not a truncation of primes:

    C(x)=sum_(m<=x)mu(m)m B(x/m).

Every sum is finite for fixed x. Regrouping the complete divisor fibers gives

    C(x)=sum_(k<=x)(x-k)sum_(m|k)mu(m)log(k/m)
        =sum_(k<=x)(x-k)Lambda(k).                        (8)

For integer N, the apparently signed quotient is actually a positive integer:

    A_N=product_(m<=N) product_(n<=N/m)n^(mu(m)(N-mn))
       =product_(p^j<=N)p^(N-p^j)
       =product_(r=1)^(N-1)lcm(1,...,r),
    log A_N=C(N).                                        (9)

The connection uses actual integer factorial determinants even at fractional
dilations. If K=floor(N/m), then exactly

    m B(N/m)=m log B_K+(N-mK)log(K!),
    A_N=product_(m<=N)[B_(floor(N/m))^m
                  (floor(N/m)!)^(N-m floor(N/m))]^(mu(m)). (9a)

Thus no nonintegral-size determinant is postulated. The equality includes
every prime power, the zero weight at p^j=N, and all shared divisors. Integrality follows either from the displayed prime
exponents or the lcm identity. The construction is not a claim that A_N is
a new number-theoretic object; it identifies the exact primitive part of
this determinant profile and what the desieving operation costs.

Let

    E(x)=C(x)-(x-1)^2/2, x>=1.                            (10)

Its Mellin transform is now zero-sensitive:

    integral_1^infinity [E(x)/x]x^(-s-1)dx
           =[-zeta'/zeta(s)-1/(s-1)]/[s(s+1)], Re s>1.    (11)

The continuum term is exact, since

    (1/2)[1/(s-1)-2/s+1/(s+1)]=1/[(s-1)s(s+1)].

At EVERY nontrivial zero rho of multiplicity m_rho, the continued right
side has residue

                     -m_rho/[rho(rho+1)] != 0.           (12)

Unlike the inert profile, this has a single fixed denominator and no
common-zero cancellation. Unlike the raw determinant, it has not lost the
reciprocal through convolution. Arbitrary multiplicities remain visible.

## 5. A complete fixed-source connection to #991

Specialize the field to Q and take no excluded primes. This is a literal
specialization of the prime observable, not a claim about all number fields.
Choose the logarithmic Gaussian

    W_c(u)=u^(-c)exp(-(log u)^2/4)/(2sqrt(pi)), u>0,

whose Mellin transform is exp((s-c)^2). Define the COMPLETE source

    P(X)=sum_n Lambda(n)W_c(n/X)-integral_1^infinity W_c(y/X)dy.

In distributions on [1,infinity), (8)-(10) give

    E''=sum_n Lambda(n)delta_n-1,
    E(1)=E'(1+)=0.

Two integrations by parts therefore give the exact identity

              P(X)=X^(-2) integral_1^infinity E(y)W_c''(y/X)dy. (13)

The tails and boundary terms are paid: E(y)=O(y^2 log(2y)) by the elementary
bound Lambda(n)<=log n, while every Gaussian derivative decays faster than
any power at both endpoints. The lower boundary terms vanish at 1. Nothing
has been replaced by only the leading large-X continuum.

The Mellin transform of (13) agrees with #991's fixed prime detector,
exp((s-c)^2)[-zeta'/zeta(s)-1/(s-1)]. This explains the connection to the
current repository without substituting a varying Hecke-family average.
The full source and all prime powers are unchanged.

## 6. The exact remaining arithmetic theorem, and what was attempted

The required estimate on these INTEGERS is

    |log A_N-(N-1)^2/2| <<_epsilon N^(3/2+epsilon)
              for EVERY epsilon>0 and every integer N>=2.     (OPEN-PD)

This is a classical Riesz-mean/lcm formulation with RH strength, not a weaker
statement that the source has already proved. The new determinant construction
has NOT proved OPEN-PD. It currently supplies one-sided prime-divisibility
information and a height estimate for a different, unsieved volume.

For clarity, here is the complete implication to RH. Between consecutive
integers C(x) is affine. Subtracting the quadratic continuum shows that E(x)
equals the linear interpolation of E(N),E(N+1) plus
(x-N)(N+1-x)/2, at most 1/8. Hence OPEN-PD controls every real x, not just
an integer subsequence. For every compact in Re s>1/2, choose epsilon
smaller than its real-part margin. The integral in (11), with any fixed
s derivatives, then converges normally and defines a holomorphic function
there. Its continuation cannot have the nonzero residues (12). The pole at
one is canceled explicitly; s=0,-1 lie outside this half-plane. The classical
functional equation therefore gives RH. No rightmost-zero or simplicity
assumption is used. Conversely RH and the classical bound
psi(x)-x=O(sqrt(x)log^2(2x)) give OPEN-PD by integration. Thus its difficulty
is stated exactly.

Equation (13) also transfers OPEN-PD to |P(X)|<<_epsilon X^(1/2+epsilon),
because integral_0^infinity u^(3/2+epsilon)|W_c''(u)|du is finite. This pays
the native prime-source step rather than merely renaming a reciprocal moment.

Three attempted shortcuts fail for proved reasons:

1. Taking finite differences of the Green determinant LOWER bounds does not
   bound their signed quotient. The unknown slacks remain.
2. Bounding every term in the desieving sum in absolute value destroys the
   Mobius cancellation that restores -zeta'/zeta. From the elementary
   B(y)<=y^2 log(2y) bound it gives only O(x^2 log^2(2x)), not OPEN-PD.
3. Inserting a vertical frequency only through separable unit-modulus row
   and column phases cannot improve a Gram determinant: for a complex
   evaluation matrix V, (VU)(VU)*=VV* when U is unitary, and a unitary row
   congruence preserves det(VV*). To encode a hypothetical imaginary part,
   a genuinely nonseparable deformation must pay its new arithmetic height
   and retain Frobenius divisibility. No such bound is supplied here.

The single next target is consequently a SIGNED HEIGHT ESTIMATE for the
primitive determinant quotient (9), or a Schur-complement realization that
bounds the SAME quotient at the error scale in OPEN-PD. The independent-jet
construction in RECTANGULAR_JETS.md shows that determinant geometry still
has quantitative flexibility; it does not establish that this flexibility
survives desieving. The lcm identity warns that an arbitrary positive-matrix
realization would simply encode a classical RH-strength problem.

This is the route chosen for its individual-zero sensitivity and different
arithmetic mechanism, not because it currently has a completed closure.
All component proofs and the failure points are exposed for adversarial review.
