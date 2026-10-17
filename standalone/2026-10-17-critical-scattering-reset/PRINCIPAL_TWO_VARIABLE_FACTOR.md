# Keep the second Mellin variable: an exact principal-residue family

Status: proposed component algebra and analysis, with proof. No new zero-free
region is established. This treats the actual principal w-residue in the CT /
OpenAI Poisson identity, before its z=1/6 residue is taken. It does not repeat
the one-variable Euler stripping already developed in #948 and #950.

## 1. Exact primary-source identity

The input is equation `eq:Euler-good-exact` in OpenAI's
`build/sections/05-poisson.tex`, inspected at commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, blob
c8526f74b281d37fda034c17195c4bb5afd5f79b:

https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex

CT v2 Section 11 imports the same finite local calculation over its arbitrary
fixed field F containing mu_12. Write theta for CT's angular phase correction
and eta=theta^6. At an exterior prime of norm Q, for the principal row u=1 set

    r=Q^(-1), D=Q^(-xi), V=Q^(-6z),
    E=eta(p) Q^(4-6xi) V.

Setting w=1 in the source formula gives the following simplification. Its
first two summands combine to (1-rV)/((1-V)(1-r)); its E and D brackets both
contain (1-rV)/(1-V). Consequently

    F_(1,p)(xi,1,z)
      = (1-rV)[1-(1-r)D-rE]/[(1-V)(1-r)(1-E)],

and therefore its extracted local correction is EXACTLY

    H_(1,p)(xi,1,z)
      = (1-rV)[1-(1-r)D-rE]/[(1-D)(1-E)].               (1)

This is a local specialization of the meromorphic factorization: the global
w=1 pole is taken after extracting zeta_F^S(w). If R_S is its residue, the
global w-residue is R_S times

    P(xi,z)=zeta_F^S(6z) H_1(xi,1,z)/zeta_F^S(xi).     (2)

At z=1/6, (1) gives CT's quoted one-variable factor, since V=r. Shared-prime
issues do not arise for u=1; all the original S omissions remain.

## 2. Two-variable factorization and its actual divisors

Put

    J_p(xi,z)=[1-(1-r)D-rE]/(1-D),
    J(xi,z)=product_(p notin S) J_p(xi,z).

**Theorem 1.** The product J is holomorphic on

    Re xi>0,   Re(xi+z)>2/3.

It is nowhere zero on the subdomain

    Re xi>1/2,   Re(xi+z)>2/3,                         (3)

and J and its inverse are bounded on every subdomain of (3) with fixed positive
margins. In the original region of absolute convergence, and hence by
meromorphic continuation wherever the factors are defined,

    P(xi,z)
       = [zeta_F^S(6z)/zeta_F^S(6z+1)]
         [L_F^S(6xi+6z-4,eta)/zeta_F^S(xi)] J(xi,z). (4)

Proof. The elementary difference is

    J_p-1 = r(D-E)/(1-D).

For x=Re xi>0 and v=Re(xi+z)>2/3, on a fixed-margin subdomain,

    |J_p-1| <= C (Q^(-1-x)+Q^(3-6v)).                 (5)

Both prime-ideal series converge, which proves normal convergence. If x>1/2
and v>2/3, the numerator N=1-(1-r)D-rE satisfies

    |N-1| <= (1-r)Q^(-x)+Q^(3-6v)
             < (1-r)Q^(-1/2)+r < 1.

Thus every local numerator is nonzero; so are 1-D. Normal convergence and
the nonzero local factors prove nonvanishing and uniform bounds on fixed
margins, including an inverse bound. Finally multiply (1), using

    product(1-rV)=1/zeta_F^S(6z+1),
    product(1-E)^(-1)=L_F^S(6xi+6z-4,eta).

This proves (4). QED.

Equation (4) explicitly retains target zeros in xi, zeros of
zeta_F^S(6z+1), zeros of the angular numerator, and zeros of zeta_F^S(6z).
It also retains the zeta poles: z=1/6 supplies the principal pole through
zeta_F^S(6z), while the poles of zeta_F^S(xi) at xi=1 and of
zeta_F^S(6z+1) at z=0 supply zeros of the displayed reciprocals. A numerator
zero may cancel a target pole at an isolated intersection; it cannot cancel
an entire vertical target-pole divisor as z varies freely. These statements
refer to the nonvanishing domain (3); outside it zeros of J must also be
retained. No divisor is silently removed.

## 3. A fixed safe z already eliminates numerator cancellation

Fix any REAL z0>1/3. Define

    C_z0=zeta_F^S(6z0)/zeta_F^S(6z0+1),
    e_p=eta(p)Q^(4-6z0),
    G_(z0,p)(xi)
       = [1-(1-r)D-r e_p D^6]/[(1-D)(1-e_p D^6)].      (6)

Then

    P(xi,z0)=C_z0 G_z0(xi)/zeta_F^S(xi),
    G_z0=product G_(z0,p).                              (7)

**Theorem 2.** G_z0 is holomorphic and nowhere zero on

    Re xi>max(0,5/6-z0).                              (8)

Both it and its inverse are bounded on each closed half-plane strictly
inside (8). In particular they are bounded and nonzero on Re xi>=1/2 for
every fixed z0>1/3. The choices z0=1/2 and z0=7/8 give correction domains
Re xi>1/3 and Re xi>0, respectively. These are domains for a correction
factor, not zeta zero-free conclusions.

Proof. Write E=e_p D^6. Direct subtraction gives

    G_(z0,p)-1 = [rD+(1-r)E-DE]/[(1-D)(1-E)].           (9)

On (8), |E|=Q^(4-6z0-6x)<Q^(-1), and |D|<1. Thus the numerator in (6)
has nonconstant modulus at most (1-r)|D|+r|E|<1. All local factors are
holomorphic and nonzero. For any fixed closed half-plane in (8),

    |G_(z0,p)-1| <= C (Q^(-1-x)+Q^(4-6z0-6x)).        (10)

The exponents are strictly below -1. Normal convergence gives the theorem,
with the same argument applied to the inverse. QED.

This produces an especially simple noncancellation statement. For any
hypothetical target zero rho with Re rho>1/2, P(xi,z0) has a pole at xi=rho
of exactly its multiplicity. There is no possibility that the angular
numerator cancels it. Equivalently, a proof of joint holomorphy for the actual
principal-residue family near (rho,z0) would exclude that target zero.
Neither joint holomorphy nor the required growth bound has been proved here.

## 4. Actual ideal coefficients and a critical norm equivalence

Remove the nonzero scalar C_z0 and write

    D_z0(xi)=G_z0(xi)/zeta_F^S(xi)
            =sum_n a_z0(n) (Nn)^(-xi).

All ideal coefficients in this section are exterior to S, extended by zero
to ideals meeting S. In particular, write
mu_F^S(n)=mu_F(n) 1_((n,S)=1), the coefficients of 1/zeta_F^S(xi).

The exact local generating function is

    [1-(1-r)t-r e_p t^6]/[1-e_p t^6]
       =1+(1-r)sum_(j>=1)e_p^j t^(6j)
          -(1-r)sum_(j>=0)e_p^j t^(6j+1).             (11)

Thus

    a_z0(p)=-(1-1/Q),
    a_z0(p^(6j))=(1-1/Q) eta(p)^j Q^((4-6z0)j), j>=1,
    a_z0(p^(6j+1))=-(1-1/Q) eta(p)^j Q^((4-6z0)j), j>=1,

and every other positive local exponent has coefficient zero. At z0=1/2
the lift weight is Q^j; at z0=7/8 it is Q^(-5j/4). This differs from the
radical-preserving source of #950: powers 6j are present and their original
nonunit zero extensions must be retained when twists are introduced.

There are ideal kernels h_z0 and k_z0 such that

    a_z0 = mu_F^S * h_z0,       mu_F^S = a_z0 * k_z0,
    sum_n |h_z0(n)| (Nn)^(-1/2) < infinity,
    sum_n |k_z0(n)| (Nn)^(-1/2) < infinity.             (12)

Here the kernels are respectively the Dirichlet coefficients of G_z0 and
its inverse; the assertion is stronger than bounded analytic continuation.
To check it directly, put t=Q^(-1/2), E0=Q^(1-6z0)<Q^(-1). A positive
coefficient majorant for G_p-1 has mass at most

    [rt+(1-r)E0+tE0]/[(1-t)(1-E0)],

and one for G_p^(-1)-1 has mass at most

    [rt+(1-r)E0+tE0]/[1-(1-r)t-rE0].

Their denominators are uniformly positive for all Q>=2; their sums over
prime ideals converge, since the numerators are
O_z0(Q^(-3/2)+Q^(1-6z0)). Euler multiplication proves (12).

For any bounded compactly supported weight W, any completely multiplicative
row twist xi_u with modulus at most one and its literal original zeros, and
any fixed finite nonnegative row measure, define the two smoothed sums with
coefficients a_z0 and mu_F^S. Equations (12), literal ideal convolution, and
Minkowski give equivalent common-row, shorter-scale envelopes

    sup_(0<X<=D) X^(-1/2) ||A_z0(X)||_(Lp)
       <= C_z0 sup_(0<X<=D) X^(-1/2) ||M(X)||_(Lp),

and the reverse inequality with another fixed constant, for every p>=1.
Shared prime factors are retained in the convolution. No coprimality is
inserted and no row measure is changed. Gaussian logarithmic weights also
work, with the following absolute-convergence check. Their fixed power tilts
satisfy |W(t)|<=C_B t^(-B) for every fixed B>0. The local formula (11) gives
|a_z0(n)|<=(Nn)^(1/3), and mu_F^S is bounded by one. Taking B=2 bounds either
convolution by a product of the kernel's convergent critical mass and the
convergent ideal series sum_m (Nm)^(-5/3), times a fixed multiple of X^2.
The same estimate makes the normalized sums tend to zero as X tends to zero;
on every finite interval of positive X, their absolute majorants are uniform.
Thus all shorter-scale envelopes at fixed D are finite before a new bound is
assumed, and Minkowski applies to the full convolution without deleting tails.

The free-z source therefore has exactly the same critical arithmetic
difficulty as the native reciprocal source. The significance is its direct
appearance before a residue in the automorphic Poisson calculation; its
analytic numerator is already harmless without a singular stripping operator.

## 5. Admissible profiles and the unproved automorphic step

The original weights have M(z)=integral W_hat_0(y)|y|_S^z d^x y. On fixed
admissible profiles, the double residue at w=1,z=1/6 contains only the scalar
M(1/6) W_hat_1(1). Changing those profiles or taking finite linear combinations
does not vary the arithmetic factor H(xi)/zeta_F^S(xi). Making that scalar
zero erases the detector. A norm twist of theta shifts its target and angular
factor together; it is not an independent numerator witness for a fixed zero.

For applying the projection at a specific z0, one must fix an admissible
profile for which M(z0)!=0; this is not asserted for an uninspected previously
fixed profile. Existence for any chosen z0 in (1/3,1) follows from the local
Tate identity stated and proved by citation in the primary source's weights
subsection. At one complex place, restrict to radial smooth functions on a
fixed open annulus. Up to nonzero constants, the additive integral and the
two required Fourier-Mellin pairings are the functionals with radial weights
r, r^(1-2z0), and r^(2/3), respectively. These three functions are linearly
independent on an open annulus. Hence on the kernel of the first functional,
the other two are nonzero linear functionals; avoid their two proper zero
hyperplanes. At the other places use nonnegative nonzero annular functions;
the same Tate identity has nonzero local factor for 0<z<1. Their positive
original Mellin integrals therefore keep both global pairings nonzero. This
constructs a fixed tensor profile with M(z0)!=0, M(1/6)!=0 and W_hat_0(0)=0.
The endpoint z0=1 is inappropriate for the
usual annular source: Fourier inversion gives the local additive integral of
W_hat_0 as W_0(0)=0, so M(1) is killed. The convenient z0=1/2 or 7/8 avoids it.

However, fixing a Mellin coordinate is not a contour estimate. To use (7), one
must retain the principal w-residue and prove a signed bound on its free-z
projection. Inverting the xi variable produces, apart from its fixed scalar,

    X^(1/2-z0) Z^(z0-1) sum_n a_z0(n) W_z0(Nn/Z),
    W_z0(t)=t^(z0-1) P_G(t),

because the original Gaussian factor is exp((xi+z0-1)^2), and the original
principal w-residue retains the physical-scale factor X^(1/2-z0). This
factor depends on the physical scales and cannot be absorbed into a fixed
scalar when X and Z are linked. After dividing out the explicit factor, the
critical target is

    sum_n a_z0(n) W_z0(Nn/Z) <<_epsilon Z^(1/2+epsilon),

or the corresponding signed vector/replica estimate with its genuine rows.
In the original principal-residue normalization this is the bound
O_epsilon(X^(1/2-z0) Z^(z0-1/2+epsilon)). In particular, for z0=1/2 the
prefactor in X disappears; for every other choice its scale dependence must
be retained when comparing a theta estimate with the desired bound.
The theta estimate in #959 bounds I at linked physical scales; it does not
bound this principal-residue projection. Mellin averaging in X and taking
the w=1 residue require cancellation and justified tails; exchanging those
operations with absolute values would silently assume the missing estimate.

Suitable place-by-place vanishing of the tensor factors of W_hat_0 near zero
can improve the analytic domain of M(z); a zero only at the joint origin does
not suffice for this claim. Equation (4) shows the next obstruction explicitly:
moving z left
encounters zeros of zeta_F^S(6z+1). A contour shift must keep their residues.
The two-variable family is thus a concrete alternative place to seek signed
automorphic cancellation, with numerator noncancellation settled; it is not
an exponent optimization or an already completed RH proof.
