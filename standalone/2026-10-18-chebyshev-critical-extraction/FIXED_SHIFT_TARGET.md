# One fixed positive-shift average, with no exceptional-member loophole

Status: PROPOSED complete analytic comparison and equivalence. The arithmetic
upper estimate OPEN-H below is NOT proved. No new zero-free bound is asserted.
The Gaussian prime-error/RH criterion is classical and already written in
#962 and #980. This note supplies the quantitative fixed-measure adapter for
the same exact translation family, rather than another family of characters.

## 1. The measure is fixed, not changed with scale or moment order

Use F,S,c,H,B(h,X),P(X) of PROOF.md. Put

 dnu_H(h)=dh/[pi sqrt(h(H-h))], 0<h<H,
 J_H(X)=integral_0^H |B(h,X)|^2 dnu_H(h),
 E_H(T)=integral_2^T J_H(X) dX/X^2,
 E_P(T)=integral_2^T |P(X)|^2 dX/X^2.                    (1)

nu_H is a probability measure. It contains no atom at the unknown endpoint
h=0. It is independent of X,T and every moment order. B extends continuously
to both endpoints, so the integrals in h exist for every finite X. All
integrands in E_H are nonnegative; no cancellation between different shifts
is presumed.

## 2. An exact polynomial reproducing kernel and its sharp norm

Let x=1-2h/H and K_m(x)=1+2 sum_(l=1)^(m-1)T_l(x). Chebyshev orthogonality
with respect to dx/[pi sqrt(1-x^2)] gives, for every polynomial f of degree<m,

 f(1)=integral_-1^1 K_m(x)f(x) dx/[pi sqrt(1-x^2)],
 integral_-1^1 |K_m(x)|^2 dx/[pi sqrt(1-x^2)]=2m-1.      (2)

The endpoint functional on this polynomial space therefore has norm
sqrt(2m-1), with equality at a multiple of K_m. This norm statement is
exact for the stated space, not a bound on the actual arithmetic source.

Define a second, continuous reconstruction

 C_m(X)=integral_0^H K_m(1-2h/H) B(h,X) dnu_H(h).         (3)

This is the endpoint value of the first m Chebyshev series terms of
h -> B(h,X). The coefficient decay in PROOF Lemma 3 gives

 |C_m(X)-P(X)| <= C X^(1+2H)(1+log X)^2 2^-m.           (4)

Thus for the SAME growing m_A(X) in PROOF (13),

 |C_(m_A(X))(X)-P(X)| <= C_A X^-A.                     (5)

No quadrature approximation to the integral (3) is being made in (4).
The discrete formula in PROOF is a different reconstruction with the same
accuracy order. Its exact sampling norm gives the parallel inequality

 |D_m(X)|^2 <= (2m-1) (1/m) sum_j |B(h_j,X)|^2.          (6)

This includes the averaging normalization 1/m. Omitting the factor 2m-1
would be false already on polynomials.

### Theorem B (a fixed-average energy comparison)

There are constants C_1,C_2 depending only on the fixed source data such that
for all T>=2,

                 E_P(T) <= C_1 log(3T) E_H(T)+C_2.      (7)

Proof. Take A=2 in (5). By Cauchy and (2),

 |P(X)|^2 <=2(2m_2(X)-1)J_H(X)+2 C_2'^2 X^-4.

The order m_2(X) is bounded by a fixed constant times log(3X). Integrate
against dX/X^2 and use positivity and log(3X)<=log(3T). The error integral
converges on [2,infinity). This proves (7). It uses the entire source and
fixed positive shift interval, not a compact-support truncation in ideals.

The logarithmic factor in (7) is harmless for a subpower criterion. Its
origin, the polynomial evaluation norm, has been paid explicitly rather
than quietly replaced by an order-independent bound.

## 3. The exact remaining target

The unproved statement is

       E_H(T) <<_(epsilon,F,S,c,H) T^epsilon
                     for EVERY epsilon>0.              (OPEN-H)

### Theorem C

For the fixed field F, OPEN-H is equivalent to the Riemann hypothesis for
zeta_F. No assertion is made that OPEN-H currently follows from an existing
large sieve or a character-family residual theorem.

Proof of sufficiency. Equation (7) transfers OPEN-H to E_P(T)=O_epsilon
(T^epsilon), by reducing the preliminary epsilon to absorb log(3T).
The exact Gaussian Mellin identity on Re s>1 is

 integral_0^infinity P(X)X^-s dX/X
  =exp[(s-c)^2] [-Z'(s)/Z(s)-1/(s-1)].                 (8)

For the prime sum, use the absolutely convergent prime-power series. For
the continuum, Fubini gives integral_1^infinity y^-s dy=1/(s-1). The
Mellin transform of W_c is exp[(s-c)^2]. All signs, finite-S omissions,
and the unit are the same as in PROOF (1)-(4).

At X approaching zero both terms of P are flat to every power, by the
full Gaussian. At infinity, Cauchy on [R,2R] gives

 integral_R^(2R) |P(X)| X^-sigma dX/X
       <= [integral_R^(2R)|P|^2 dX/X^2]^(1/2)
                          [integral_R^(2R)X^(-2sigma)dX]^(1/2)
       << R^(epsilon/2+1/2-sigma).                    (9)

For each compact in Re s>1/2 choose one epsilon smaller than twice its
real-part margin. Dyadic sums, with any fixed logarithmic derivatives,
converge normally. Thus (8) extends holomorphically throughout Re s>1/2.
At each zero rho of Z there, -Z'/Z has residue -m_rho, with m_rho>=1,
and the exponential factor never vanishes. The pole at one is canceled
by the rational term. Analytic uniqueness contradicts every such zero.
Finite-S Euler zeros have real part zero and play no role in this
half-plane. The functional equation gives field RH, including multiplicity.

Proof of necessity. This direction ASSUMES field RH. For any fixed small
eta>0 choose sigma=1/2+eta<3/4. The fixed-field reciprocal bound in this
zero-free half-plane is polynomial in vertical height. A proof uses an
analytic logarithm of the pole-removed zeta on a finite chain of fixed-width
zero-free disks to its Euler half-plane normalization, Borel--Caratheodory,
and classical polynomial strip growth. Constants depend on eta. This is
not a claimed bound on the critical boundary or on zeta derivatives at zeros.
Ordinary strip growth and Cauchy's formula also bound Z'(s+theta h)
polynomially for 0<=h<=H, 0<=theta<=1. Since sigma+H<1, the line contains
no numerator pole, even near height zero. There

 (1-Z(s+h)/Z(s))/h
       =-integral_0^1 Z'(s+theta h)/Z(s) dtheta         (10)

is uniform as h tends to zero. The exact Mellin transform of B is

 exp[(s-c)^2] [(1-Z(s+h)/Z(s))/h-k(h)/(s+h-1)].          (11)

It is jointly regular after the shifted-pole cancellation, also when h=0.
One can see the cancellation near s=1 explicitly by writing
A(s)=(s-1)Z(s), k(h)=kappa/A(1-h): the numerator after multiplication by
h(s+h-1) vanishes on BOTH h=0 and s+h-1=0, so it is divisible by their
product in the two independent local coordinates. This handles the
coalescing poles without an uncontrolled 1/h constant.

Move the original contour to the chosen sigma. Under RH there is no
uncanceled denominator pole in this movement. Fixed real-shift compactness,
(10), and the Gaussian exp[-(Im s)^2] justify horizontal limits and all
vertical integrals uniformly in 0<=h<=H. Hence

          sup_(0<=h<=H)|B(h,X)| <<_eta X^(1/2+eta), X>=2.

Integrating its square gives E_H(T)<<_eta 1+T^(2eta), since nu_H has mass
one. Choose eta below epsilon/2 to get OPEN-H. Arbitrary critical-zero
multiplicities are compatible with this subpower bound; an O(log T)
bound for E_H is NOT claimed to follow from RH. QED.

## 4. Averaging in h cannot hide a prescribed off-line zero

Here is a direct local check independent of polynomial approximation.
Suppose Z has a zero rho in the open critical strip, of multiplicity m,
and write Z(s)=(s-rho)^m g(s), g(rho)!=0. The coefficient of (s-rho)^(-m)
in the bracket in (11), as a function of h>0, is

                  v_rho(h)=-Z(rho+h)/[h g(rho)].        (12)

The continuum term is analytic at rho for the chosen small H: otherwise
rho=1-h would contradict the local nonvanishing of Z(1-h) used to choose H.
As h approaches zero, v_rho(h)=-h^(m-1)+O(h^m). It is therefore NOT
identically zero. On (0,H) its zeros are isolated. In particular,

                integral_0^H |v_rho(h)|^2 dnu_H(h)>0.   (13)

The integral is finite: its local behavior is O(h^(2m-2)) against an
h^-1/2 weight. A numerator zero can cancel the pole at one special h,
but cannot cancel (13). This is a quantitative positive pole-mass
statement for the fixed target, not a density assertion about many
unrelated Hecke functions.

The function v_rho and the local pole coefficient are regarded as
meromorphic/analytic germs; no value is assigned to a 0/0 expression at
s=rho. The proof does not presume a rightmost zero or simple zeros.

## 5. The attempted bridge from #986/#987, and its unresolved part

#986/#987 estimate L_a M_A-1 in a growing Hecke family. Their sums allow a
persistent exceptional member. They do NOT bound J_H(X), whose denominator
is the SAME fixed Z(s) at every h. The former family large sieve cannot
be applied to h as if h were a finite-order Hecke character index.

Taking absolute values in the complete source gives, at best from this
packet, J_H(X)<=C X^(2+4H)(1+log X)^4. Inserting this into (1) yields a
positive power of T, not OPEN-H. Thus the improved interpolation does
not establish the needed signed prime-versus-continuum estimate.

What changes: the previous moving-stencil target is replaced by one FIXED
positive measure with an explicit logarithmic extraction cost, and every
prescribed zero remains visible across almost all its shifts. What does
not change: a new arithmetic upper bound for that fixed mean is still
required. No bounded physical CT projection, low-powerful cancellation,
native all-order square-root estimate, or full RH resolution is claimed.

## 6. Remove even the endpoint: a fixed interval bounded away from zero

There is a second target that requires NO shifts tending to zero at all.
Let J=[H/2,H], let nu_J be uniform probability measure on J, and put

 E_J(T)=integral_2^T integral_J |B(h,X)|^2 dnu_J(h) dX/X^2. (14)

### Theorem D (Hilbert-valued fixed-interval criterion)

The statement E_J(T)<<_epsilon T^epsilon for every epsilon>0 is also
equivalent to field RH. It is denoted OPEN-J and remains UNPROVED.

Sufficiency has a direct proof, without Chebyshev extrapolation. Let
V=L^2(J,nu_J). Under the assumed energy bound, the V-valued Mellin
integral of B converges holomorphically for Re s>1/2. The Cauchy estimate
(9), with the V norm, proves normal convergence on compact subsets.
The X<2 part is entire after retaining its Gaussian flatness. On Re s>1,
this V-valued function is exactly (11), with h the V variable.

At a hypothetical zero rho the highest pole coefficient is the vector
exp[(rho-c)^2]v_rho(h). It has nonzero V norm by (12)-(13), now integrated
over J. To reduce to scalar uniqueness, pair with that fixed nonzero
coefficient vector in V. The scalar function would be both holomorphic
and have a pole with nonzero leading coefficient, a contradiction. This
pairing is used only in the proof by contradiction; it does NOT change
the fixed measure or arithmetic premise. Necessity follows from the same
RH-assuming uniform contour estimate in Theorem C. QED.

Theorem D is not a numerical comparison E_P<=C E_J with C independent of
T. Such a comparison is not asserted. The logarithmic comparison (7)
uses a DIFFERENT measure that reaches zero; (14) instead uses a direct
vector-valued holomorphy argument. These two assertions are not conflated.

### Theorem E (a quantitative fixed-member obstruction)

Let rho=1/2+delta+i gamma, delta>0, be a zero of Z of multiplicity m>=1.
Set

 C_rho^2=exp[2 Re((rho-c)^2)]
                integral_J |Z(rho+h)/(h g(rho))|^2 dnu_J(h)>0,
 q_m=((2m-1)/m)^(2m-1)/[2m (2m-2)!].

Then, WITHOUT assuming a rightmost zero, spacing, or simplicity,

 limsup_(T->infinity) E_J(T)/[T^(2delta)(log T)^(2m-2)]
                         >= (q_m/delta) C_rho^2 > 0.    (15)

For m=1, q_m=1/2. For m>1 this is a valid explicit lower constant, NOT
claimed sharp. It calibrates the exact fixed-interval energy, not a
truncated sum of formal zero modes.

Proof. Write x=log X, f(x)=e^(-x/2)B(h,e^x) as a V-valued function and
E(u)=integral_(log 2)^u ||f(x)||_V^2 dx=E_J(e^u). If the limsup in (15)
is infinite, there is nothing to prove. Otherwise let L be that finite
limsup. For any L'>L, eventually E(u)<=L'e^(2delta u)u^(2m-2).
This bound ensures that the V-valued Laplace integral is holomorphic for
Re z>delta, where it equals the meromorphic continuation of (11), modulo
an entire initial segment. Its pole at z0=delta+i gamma has leading
coefficient of V norm C_rho. Thus

 ||F(z0+epsilon)||_V^2 ~ C_rho^2 epsilon^(-2m)
                                            as epsilon ->0+.

For 0<a<1, Cauchy and Stieltjes integration by parts give

 ||F(z0+epsilon)||_V^2
 <= [integral exp(-2(delta+a epsilon)x) dE(x)]
                              [integral exp(-2(1-a)epsilon x) dx].

The fixed initial interval is negligible at the leading epsilon power.
Using the eventual upper bound and
integral_0^infinity e^(-2a epsilon x)x^(2m-2) dx
=(2m-2)!/(2a epsilon)^(2m-1), the limsup of epsilon^(2m)
times the right side is at most

             delta L' (2m-2)! /[(2a)^(2m-1)(1-a)].

Consequently L'>=C_rho^2 (2a)^(2m-1)(1-a)/[delta(2m-2)!].
Take a=(2m-1)/(2m) and L' down to L to obtain (15). Any zeros farther
right would have forced the energy limsup to be infinite; none were
silently assumed absent. QED.

The point of (14)-(15) is the absence of the persistent exceptional-MEMBER
loophole: the target L-function is fixed throughout this average. The missing
upper bound OPEN-J is still a full RH-strength arithmetic estimate. A positive
power of family size in #986 or #987 supplies no bound for it.
