# Two independent conjugate frequencies in the fourth-slot collision factor

Status: proved exact finite-Euler bound and a proved local frequency estimate.
The optional bound at every frequency names an additional classical
reciprocal-zeta input explicitly. This does not bound the full independent
four-frequency source trace, the individual reciprocal factors, or R2.

## PF1. Literal factor and the enlarged plane

Use the source definitions and exact all-pair factorization P1--P4 of
`PRIME_SLOT_CANCELLATION.md`, frozen SHA-256
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
There are four labeled slots. At a prime p outside the fixed source set S
and moving exclusions uQ, write q=Np, a=eta_u(p), |a|=1.
Take the four frequencies

    s1=1/2+i t1, s2=1/2+i t2,
    s3=1/2-i t1, s4=1/2-i t2.

Let Delta=t1-t2. Both t1 and t2 are arbitrary. This is a two-dimensional
paired plane, rather than the one-dimensional common-frequency slice.
The individual source phases a are retained. At deleted primes all
variables are zero and the local collision factor is one.

Put x=1/q, u=exp(-i t1 log q), v=exp(-i t2 log q).
The absolute value of the **complete six reciprocal pair factors** is

    |1-a^2 u v x|^2 (1-x)^2 |1-u conjugate(v) x|^2.

Consequently, exactly and uniformly in the source character,

    |all pairs| <= (1-x^2)^2 |1-q^(-1-i Delta)|^2
                <= |1-q^(-1-i Delta)|^2.                  (PF1)

The first bound uses |1-a^2uvx|<=1+x. All six factors are present;
in particular the two cross self-pairs supply (1-x)^2.
The uniformly absolutely convergent degree-three remainder from P4
is bounded at all four real parts 1/2. Thus the exact finite collision
factor obeys

    |collision| <= C |L_(Y,SuQ)(1+i Delta,principal)|^(-2), (PF2)

where the partial principal Euler product includes precisely the primes
Np<=Y outside S,u,Q. This bound does not require a reciprocal bound for
the individual source L-functions at real part 1/2.

## PF2. An unconditional completed-zeta comparison

Let delta=1/log Y, Y>=3. For the fixed field K, Chebyshev's upper bound
pi_K(X)<=C_K X/log X gives, uniformly in every real Delta,

    |log |zeta_(K,Y)(1+i Delta)|
       -log |zeta_K(1+delta+i Delta)|| <= C_K.              (PF3)

This concerns absolute values; no branch of the logarithm is needed.
To prove it, compare the prime logarithm series. For Np<=Y, the
first-power change is bounded in absolute value by

    delta sum_(Np<=Y) log(Np)/Np = O_K(1).

For Np>Y, partial summation bounds the first powers by

    C_K integral_Y^infinity dx/(x^(1+delta) log x)
      = C_K integral_1^infinity exp(-v) dv/v = O_K(1).

All prime powers of degree at least two are absolutely summable, uniformly
in delta>=0 and Delta. This proves PF3. The field's prime-ideal Chebyshev
bound follows from the rational Chebyshev bound and degree-two splitting;
it is the same classical elementary input used in the frozen mask-density
proof. The complete zeta here is evaluated strictly inside its absolute
Euler half-plane Re(s)>1, so it has no zero there.

Deleting the fixed S costs a fixed constant. Deleting the moving uQ
costs at most the inverse principal-mask product

    product_(p|uQ) (1-1/Np)^(-1)
      <= C_K [1+log log(3N(uQ))].

The existing elementary Chebyshev/zeta-pole norm-budget proof in the
frozen P5 establishes this bound. Combining it with PF2--PF3 gives the
proved, phase-faithful estimate

    |collision| <= C [1+log log(3N(uQ))]^2
                      |zeta_K(1+1/logY+i Delta)|^(-2).    (PF4)

This is uniform in both paired frequencies and every finite cutoff.
It retains the entire finite Euler polynomial and all moving exclusions.

## PF3. A paid estimate near the frequency diagonal

The fixed-field zeta pole at 1 implies the existence of fixed positive
c0,C0 for which

    |1/zeta_K(s)| <= C0 |s-1|,  |s-1|<=c0, Re(s)>1.

This also follows directly from the fixed-field ideal count
A_K(X)=kappa_K X+O_K(sqrt X) by partial summation: after subtracting
kappa_K s/(s-1), the integral is holomorphic on Re(s)>1/2.
The pole residue kappa_K is positive. Therefore for sufficiently large
Y and |Delta|<=c0/2,

    |collision| <= C [1+log log(3N(uQ))]^2
                      [(logY)^(-2)+Delta^2].             (PF5)

For N(uQ)<=Y^c and |Delta|<=b/logY with fixed b, this pays
the same inverse-log-square saving as P10, uniformly in the common
central frequency (t1+t2)/2. For fixed small nonzero Delta it gives a
Y-independent bound, apart from the explicitly priced loglog mask cost.
This is an enlarged exact frequency region; it is not all four independent
frequencies of the source Mellin integral.

## PF4. Optional classical global-frequency corollary

If one imports the classical fixed-field reciprocal-zeta bound

    |1/zeta_K(sigma+i t)| <= C_K (1+|t|)^B,
    sigma>=1, sigma<=2,                                 (CLASSICAL-PF6)

with the reciprocal extended through the pole at t=0, then PF4 gives

    |collision| <= C (1+|Delta|)^(2B)
                         [1+log log(3N(uQ))]^2.          (PF7)

For this fixed K, CLASSICAL-PF6 follows from the classical zero-free
region and reciprocal estimates for zeta_Q and the fixed Dirichlet
L(s,chi_-3), since zeta_K is their product. This additional classical
theorem is named as an input here; its proof is not rebuilt in this packet.
Neither PF4 nor the near-diagonal estimate PF5 needs CLASSICAL-PF6.

The polynomial mask budget gives only (1+loglogY)^2 in PF7, compared
with the phase-erased positive log-power collision envelope. This saving
belongs to this paired plane and does not suppress the individual
finite inverse source factors.

## PF5. Why a diagonal-to-trace Cauchy step is unpaid

For one eligible source prime the finite coprime Euler polynomial is the
kernel

    K(x,y)=1-A(x)-conjugate(A(y)),

where A(x) is the sum of the two left slot variables. Its two-by-two
Hermitian determinant for two frequency vectors is exactly

    K(x,x)K(y,y)-|K(x,y)|^2=-|A(x)-A(y)|^2.              (PF8)

Even if both paired diagonal values are positive, this kernel is
indefinite whenever those sums differ. Dividing it by the exact single
reciprocal factors is a diagonal congruence and preserves its inertia.
Thus paired-plane estimates do not supply a local positive-kernel
Cauchy extension to independent left and right frequency vectors.

This is a statement about the local finite Euler kernel. It is not a
claim that the complete radial row trace is itself indefinite after
unit projection. The full moment is positive; the selected signed
critical remainder has a distinct, centered kernel. Its cross-frequency
and cross-conductor interference still requires an actual estimate.
