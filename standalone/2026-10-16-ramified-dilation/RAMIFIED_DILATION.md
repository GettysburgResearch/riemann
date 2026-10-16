# The shared-prime part of the joint dilation

Status: PROPOSED component mathematics, with the complete argument below.
No independent review, new native moment exponent, zero-free half-plane,
or RH proof. This is not an integrated result.

Scope: a fixed number field F containing mu_6, degree d_F, and a finite
set S of finite primes such that R=O_F[S^(-1)] is a PID. Include all primes
of norm below 7 in S. Fix the primitive additive and sextic multiplicative
characters described below. Ideal sums are over exterior integral ideals
(prime to S), with distinct conjugate primes kept distinct. For positive
unit rank, rows are the specified sixth-unit QUOTIENT, not a norm-only
ball of elements. The finite diagnostics use Eisenstein arithmetic only.

Sources: #950 at 5a6418b021a35c95bbc2c80775353ee33506faee, PRE_POISSON.md;
the pinned upstream actual probe and forward-row definitions listed in
SOURCES.md. The local Gauss calculation is classical and re-proved below.
The new object is its application to the actual simultaneous sixth-power
dilation and its exact raywise shared-prime energy budget.

## 1. Definitions and the elementary local calculation

For a nonzero allowed ideal s, write s=product p^e_p. Set Q=Ns. Choose a
primitive additive character of R/s. At each p choose a character chi_p of
EXACT order six of (R/p)^*, extended by zero at zero. The multiplicative
character on R/s is

    chi_s(x)=product_(p|s) chi_p(x mod p)^e_p,

and it is zero if x is not a unit modulo s, INCLUDING when e_p=0 modulo 6.
Define the normalized Gauss row

    g_s(m)=Q^(-1/2) sum_(x mod s) chi_s(x) psi_s(mx).

For s=1 use g_1=1. A different primitive additive character changes fixed
unit phases but none of the support conclusions below.

Call p|s ACTIVE when 6 does not divide e_p, and NEUTRAL when 6 divides e_p.
These terms classify the DENOMINATOR's Gauss character, not the moment
conductor/neutral radical of #944. Those are different objects.

### Lemma 1 (complete local support)

For a local modulus p^e with q=Np, put v=v_p(m). If v<e-1 the unnormalized
Gauss sum is zero. If v>=e-1, it equals

    q^(e-1) sum_(r in (R/p)^*) chi_p(r)^e psi_p(t r),   (1)

where t is m/p^(e-1) reduced modulo p, with a fixed unit in the additive
character absorbed into psi_p. Thus:

* when 6 does not divide e, the sum is supported EXACTLY on v=e-1;
  on that shell it is a nonzero Gauss constant times conj(chi_p(t)^e);
* when 6 divides e, its value is -q^(e-1) on v=e-1, and
  q^(e-1)(q-1) on v>=e.

Proof. Group units modulo p^e by their reduction r modulo p. The additive
sum over each lift fiber has q^(e-1) terms. It vanishes unless p^(e-1)
divides m; in that case it gives (1). For nontrivial chi_p^e, finite-group
orthogonality kills t=0. For t nonzero change variable r to t^(-1)r;
the remaining primitive finite-field Gauss sum is nonzero, since its
squared absolute value is q. This last identity follows by expanding the
square, setting r=a u, and using the additive sums q-1 at a=1 and -1
otherwise. For the trivial character, the sum over nonzero residues is
q-1 at t=0 and -1 otherwise. CRT multiplies these local expressions up to
fixed harmless unit phases. QED.

In particular

    g_s(m)!=0 ==> v_p(m)=e_p-1 for every active p|s.     (2)

No such equality is available at a neutral prime. Replacing its zero-
extended principal character by the constant function 1 is incorrect.

## 2. An exact common-row realization, before any inequality

### Rows and unit invariance

Let Gamma=(R^*)^6 act on nonzero elements of R, and let M be the quotient.
Write |m| for the positive integer exterior-ideal norm of a row class.
There are finitely many such classes with |m|<=T: a principal exterior
ideal has a finite number [R^*:(R^*)^6] of generator classes. Finiteness
of this index is the classical S-unit theorem, not a new result here.

Choose a generator delta_d of each exterior ideal d. The map

    [m] -> [delta_d^6 m]

is independent of the generator choice, injective, and its image is
exactly the rows whose exterior ideal is divisible by d^6. These maps
multiply correctly, even if the chosen generators do not. Norms multiply
by (Nd)^6. All later row sums are on M and exclude the zero element.

Use #950's actual coefficient

    h(d)=mu(rad d) eta(d) phi(rad d)/Nd,  |eta(p)|<=1,
    h(1)=1, h(p^j)=-(q-1) eta(p)^j/q^j  (j>=1).         (3)

Here eta need not be a finite-order Hecke character. The Gauss row descends
to M, since changing m to u^6 m with u in R^* is an invertible change of
summation variable in the Gauss sum and chi_s(u^6)=1. Let B_m(Z) be ANY
complex family on M, Z>0. In the intended application it is the actual
forward theta row, not the native Mobius polynomial. Its sixth-unit
invariance is precisely the compatibility proved in the pinned upstream
ReflectionGaussianAndSixthUnitInvariance.lean; no invariance under a
nonunit sixth power is asserted.

For a bounded compactly supported norm test w:(0,infinity)->C set

    J_s(X,Z)=1/sqrt(QX) sum_(m in M)
                  w(|m|/(QX)) g_s(-m) B_m(Z).          (4)

If w is supported in [a,b], J_s(X,Z)=0 when bQX<1. Its theta/column
expansion may still be infinite; no truncation of that expansion is made.

### Compatibility with the actual norm-one integral

This version follows from the source probe by elementary unfolding,
under its original norm-one Haar/fundamental-domain data. More precisely,
let G1 be the norm-one S-local multiplicative group, D a fundamental
domain for Gamma, and ell_T a multiplicative radial section of norm T.
For compact W supported in the S-local units, the norm-fiber integral

    w(v)=integral_(t in G1) W(ell_v/t) dt

is a bounded compactly supported norm test. Haar normalization is fixed.
Then the source's expression

    integral_D sum_(alpha in R, alpha!=0)
        W(alpha/(t ell_T)) g_s(-alpha) B_alpha(Z) dt

is exactly sum_(m in M) w(|m|/T) g_s(-m) B_m(Z).
To prove this, split alpha into Gamma orbits, use the two invariances,
and unfold the translates of D to G1. Translate in G1 by
alpha/ell_|alpha| to identify the resulting fiber integral. Compact
support and the finite norm-class count justify the rearrangement.
A smaller fixed finite-index sixth-unit subgroup only changes the fixed
normalization/multiplicity; it does not change the dilation or exponent.
These are explicit source-data hypotheses, not a new construction of the
upstream theta representation or a new formal verification of ActualRecipe.

### Proposition 2 (literal row formula)

Set D_d=Nd and

    C_s(m;Z)=sum_(d^6 | (m)) h(d) D_d^3
                  g_s(-m/delta_d^6)
                  B_(m/delta_d^6)(Z/D_d^6).            (5)

C_s here is a TRANSFORMED GAUSS/THETA ROW. It is not the scalar geometric
Mobius source C of #950; the two are not identified by their Euler factors.
This is a finite divisor sum for every row m. Then

    sum_d h(d) J_s(X/D_d^6,Z/D_d^6)
       =1/sqrt(QX) sum_(m in M) w(|m|/(QX)) C_s(m;Z).  (6)

Proof. Only D_d^6<=bQX contributes on the left. In each summand replace
the old row n by m=delta_d^6 n. The prefactor becomes D_d^3/sqrt(QX),
and |m|=D_d^6|n| aligns the norm test. The old B index becomes
m/delta_d^6; it is NOT replaced by m. Every Gauss zero remains. This
proves (5)-(6) by finite rearrangement. QED.

The full three-scale probe additionally averages (4) over s with
Y^(-1) W1(Q/Y). It inherits (6) termwise, with Y FIXED. No change to the
outer denominator, the test, or the actual theta coefficients is made.
This refines the arithmetic operation in #950 after norm-one unfolding;
it is not a new theta transformation law.

## 3. Split the dilation into coprime and shared-prime parts

Every d has a unique factorization d=a b, with rad(a)|s and (b,s)=1.
Define the STILL SIGNED coprime-dilation row

    U_s(n;Z)=sum_(b^6 | (n), (b,s)=1) h(b) (Nb)^3
                   g_s(-n/delta_b^6)
                   B_(n/delta_b^6)(Z/(Nb)^6).          (7)

No estimate for (7) is assumed or proved at this point. This does not
replace h by its absolute value. Its actual B indices and scales remain.
Then the exact factorization of (5) is

    C_s(m;Z)=sum_(a^6 | (m), rad(a)|s) h(a)(Na)^3
                     U_s(m/delta_a^6;Z/(Na)^6).        (8)

At every active p|s, (b,s)=1 in (7) and Lemma 1 imply

    U_s(n;Z)!=0 ==> v_p(n)=e_p-1.                       (9)

Consequently the different a supported on active primes in (8) occupy
DISJOINT physical row shells:

    v_p(m)=e_p-1+6 v_p(a), for every active p|s.         (10)

This remains true for arbitrary complex B, twists, and theta-column
common primes. It uses the Gauss row's actual zeros, not an independent
residue average or random model.

## 4. Exact energy identity for the active shared primes

Let Psi:[0,infinity)->[0,infinity) be bounded and compactly supported.
For 1<=p<infinity define the critical normalized row energy

    E_p[V](T,Z)=1/(T Z^(p/2)) sum_(m!=0) Psi(|m|/T)|V_m(Z)|^p,
    E^*_p[V](T,Z)=sup_(0<t<=1) E_p[V](tT,tZ).           (11)

T is the row NORM cap, equal to QX in (4), not X. These are suprema of
energies; no norm of a rowwise maximum is being used. The ratio Z/T stays
fixed on the ray. The supremum is allowed to be infinite.

Let A be the set of active denominator primes, and define

    (R_A U)_m(Z)=sum_(rad(a) subset A, a^6|(m))
                     h(a)(Na)^3 U_(m/delta_a^6)(Z/(Na)^6).

### Theorem 3 (all-p exact disjoint-shell identity)

If U has the support (9), then

    E_p[R_A U](T,Z)
       =sum_(rad(a) subset A) |h(a)|^p/(Na)^6
                              E_p[U](T/(Na)^6,Z/(Na)^6). (12)

The nonzero terms on the right are finite at each T. The SAME identity
with no Z normalization has coefficient |h(a)|^p (Na)^(3p-6).

Proof. Equation (10) means at most one summand contributes at any row m,
so the absolute p-th power separates exactly. Change m=delta_a^6 n.
Then |m|=(Na)^6 |n|. The factor (Na)^(3p) from the row coefficient is
cancelled by the change of Z^(p/2); the change in normalized row mass
leaves precisely (Na)^(-6). QED.

In particular the shared active-prime cost obeys

    E^*_p[R_A U] <= K_A,p E^*_p[U],
    K_A,p <= product_(p0 in A)
             [1+(Np0-1)^p/((Np0)^(p+6)-1)].            (13)

Do not conflate the moment parameter p with the prime p0. Equation (13)
is an equality for the coefficient mass when |eta(p0)|=1. Each factor is
at most 1+2(Np0)^(-6), for every real p>=1 and Np0>=7. Thus K_A,p is
bounded by ONE fixed constant, independent of s, T, Z, and p. Indeed
sum_(prime ideals) q^(-6) <=d_F sum_(n>=7)n^(-6)<infinity.
This is an energy-budget statement, not a bound for E^*_p[U].

## 5. Neutral primes: retain overlap, with a finite explicit budget

Let N be the neutral denominator primes and R_N the analogous operator.
Equation (8) says C=R_N R_A U. It does NOT say R_N is orthogonal.
For any row family V, Minkowski and the same change of variable give

    E^*_p[R_N V]^(1/p)
      <= L_N,p E^*_p[V]^(1/p),
    L_N,p <= product_(p0 in N)
             [1+(Np0-1)/((Np0)^(1+6/p)-1)].             (14)

For example, at a neutral p0, the rows of valuation e_p0+6 have nonzero
contributions from both a=1 and a=p0. An orthogonal formula there would
be false. The finite-prime mass (14) is valid for every fixed s and every
finite p. Bounds use |eta|<=1 and preserve complex phases in the operator.

### Theorem 4 (complete shared-prime removal)

For every s, all T,Z>0, and arbitrary actual row family B,

    E^*_p[C_s] <= K_A,p L_N,p^p E^*_p[U_s].              (15)

For EVERY fixed 1<=p<6, the factor in (15) is bounded uniformly over s.
In particular this holds at the SECOND AND FOURTH moments, with no
power or logarithm of s, T, or Z. At fourth order a deliberately coarse
uniform bound is exp(32 d_F), depending only on the fixed field degree.

Proof. Compose (13)-(14). If p<6, a neutral factor differs from 1 by
O_p(q^(-6/p)), a prime-summable sequence. For p=4 one may use the upper
bound 1+2q^(-3/2). Hence log of its fourth-power product is at most
8 sum q^(-3/2) <=8 d_F sum_(n>=7)n^(-3/2) <=16 d_F/sqrt(6).
The active product contributes at most 2 d_F sum_(n>=7)n^(-6).
Their sum is less than 32 d_F. All constants are explicit, though unoptimized.
QED.

For fixed p>=6, (15) still has no prescribed positive power loss: for
all epsilon>0 its coefficient factor is O_(p,epsilon)((Ns)^epsilon).
Indeed for large enough q each bounded local factor is at most q^epsilon;
the product of the finitely many smaller-prime factors is a constant and
Nrad(s)<=Ns. This does not assert a p-uniform cofinal error constant.

At p=6 the unrestricted product in (14) is at its harmonic endpoint; for
p>6 it is not prime-summable. Therefore that particular positive-majorant
proof does not give an all-s constant at those orders. This is a limitation
of (14), not an arithmetic lower bound for the actual theta sum.

### What the constant bound does not require

At p<6, even the FULL dilation has the elementary majorant

    E^*_p[R_all V]^(1/p)
       <= product_(all allowed p0)
            [1+(Np0-1)/((Np0)^(1+6/p)-1)] E^*_p[V]^(1/p). (16a)

This follows from the same change of variable and Minkowski, without
using a Gauss character at all. The Euler product converges because 6/p>1.
Thus the existence of a constant at second/fourth order alone is NOT
claimed as a new cancellation phenomenon. The additional arithmetic
content of (12) is the exact disjoint-shell identity, its all-p active
budget, and the separation of the actual common-prime and coprime terms.
The full signed coprime sum should not be bounded by (16a) when the aim
is an improvement over the already available source exponent.

These JOINT-RAY envelopes scale T and Z together. They are not the
SAME-HEIGHT native envelopes of #950/#951. No implication between those
norm contracts is asserted without an additional analytic argument.

## 6. A weaker, often useful unnormalized L2 version

Set E0[V](T,Z)=T^(-1) sum Psi(|m|/T)|V_m(Z)|^2, with the same ray supremum.
The exact active identity now has weight |h(a)|^2, without (Na)^(-6).
Consequently

    E0^*[C_s] <= [product_(active p0) 2q/(q+1)]
                     4^(# neutral p0) E0^*[U_s]
                <= C_epsilon (Ns)^epsilon E0^*[U_s].   (16)

This is the no-power common-prime statement WITHOUT hypothesizing that
E0 scales like Z. The stronger constant in Theorem 4 uses the explicitly
Z-normalized, raywise critical envelope; (16) and (15) must not be mixed.

More generally a ray inequality E0[U](tT,tZ)<=t^lambda B with lambda>-1/3
has active factors

    1+(q-1)^2/(q^(2+6lambda)-1)

and neutral root factors

    1+(q-1)/(q^(1+3lambda)-1).

This prices adverse off-curve growth instead of silently assuming it away.
At lambda=0 it gives (16). At lambda=-1/3 the infinite geometric budget
ceases to converge. All original finite sums still exist at that endpoint.

## 7. Sharpness and an attempted power saving

The exact active-prime budget cannot, for arbitrary compatible row families,
be replaced by a factor decaying as a power of T. This is a concrete limit
on the attempted estimate, not a claim that the actual theta family attains it.

Take the hard-ball test Psi=1_[0,1]. Fix one row m0 with active valuations
e_p-1, and let U be zero on all other rows, with

    U_m0(Z)=Z^(1/2+1/p).

Along T=Z>=|m0| the input critical ray envelope is exactly 1. The active
output energy is

    E_p[R_A U](T,T)
       =sum_(rad(a) subset A, (Na)^6 |m0|<=T)
                    |h(a)|^p/(Na)^6.                  (17)

It increases to the full coefficient mass in (13). Thus (13) is sharp
as an operator bound for this class of row families and this allowed
hard-ball norm test. In particular the a=1 term already equals 1, so no
uniform bound O(T^(-delta)) for delta>0 is possible here. The construction
can be multiplied by the inverse of the nonzero g_s(m0) to write it as a
Gauss row times an arbitrary B. It is NOT the actual theta B, nor an
arithmetic counterexample to RH.

This rules out finishing the argument by a universal improvement of this
shared-prime operator inequality. Any additional saving must use more
structure of the remaining coprime sum or of the actual theta coefficients.

## 8. What remains of the full proof

The new bound is a bound for an OPERATOR acting on an unknown source.
It does not establish the required critical energy of (7). Its hypotheses
require the SAME RAY of row and column scales, with s fixed. The old
fixed-curve theta estimate from #950/#951 does not automatically provide
that maximal estimate. A bound averaged in s at one common t also does
not automatically control a sum of s-dependent ray suprema.

The exact shared-prime adapter is supplied under the stated S-arithmetic
source data, including the sixth-unit quotient and Haar compatibility.
The remaining signed arithmetic is the coprime b-sum (7), together with
the full theta comparison residual in #950. Neither that sum, the scalar
Gaussian square-root target, nor I_k-D_k in #951 has been bounded at the
required power here. A local Lp operator budget is not a zero-free theorem.

Classical inputs have been re-proved where used. No claim of historical
priority is made. The intended advancement over #950 is the explicit
common-row kernel, its Gauss valuation split, and (12)-(16), rather than
another Euler numerator normalization.
