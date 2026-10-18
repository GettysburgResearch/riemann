# A ramification-preserving quadratic average for ordinary Mobius

Status: PROPOSED complete elementary component arguments, not independently
refereed. No new zero-free boundary is established. The new estimates compare
actual arithmetic sources; the cancellation of the final signed mean is OPEN.
Classical quadratic characters, squarefree counting, Gauss sums and Dirichlet
convolution are used. No worldwide novelty or optimality claim is made.

## 1. Fixed exclusions, varying fields, and no loss at ramified primes

Put mu6(n)=mu(n) if gcd(n,6)=1, and zero otherwise. For d squarefree,
d=3 mod 4, let Delta=-d and chi_Delta be its primitive quadratic character.
Then K_Delta=Q(sqrt(Delta)) is an imaginary quadratic field. Only rational
2 and 3 are excluded, NOT every prime dividing the discriminant. Define

    a_Delta = mu6 * (mu6 chi_Delta),
    b_Delta(n) = mu6(n) product_(p|n)(1+chi_Delta(p)).       (1)

These are complete rational-norm coefficients. At an unexcluded split prime
the first coefficient of b is -2, at an inert prime it is zero, and at a
ramified prime it is -1. In particular chi(p)=0 is NOT replaced by a unit
value or by deletion of that prime. All nonsquarefree b(n) vanish.

Write zeta6 and L6 for the original functions with their factors at 2,3
removed. Initially in Re s>1,

    A_Delta(s)=1/[zeta6(s)L6(s,chi_Delta)],
    B_Delta(s)=product_(p>=5)[1-(1+chi_Delta(p))p^(-s)].    (2)

The quadratic Dedekind factorization identifies A with the reciprocal
of the incomplete zeta_K. This is the usual abelian factorization, not
a new analytic theorem.

### Theorem Q1 (uniform invertible primitive correction)

There are multiplicative coefficients v_Delta,w_Delta such that

    b_Delta=a_Delta*v_Delta,
    a_Delta=b_Delta*w_Delta,
    v_Delta*w_Delta=delta_1.                              (3)

For EVERY fixed sigma>1/2 their absolute Dirichlet norms are bounded
independently of Delta:

    sum |v_Delta(n)|n^(-sigma) <= C_V(sigma),
    sum |w_Delta(n)|n^(-sigma) <= C_W(sigma),              (4)

where the explicit finite constants are

    C_V=product_(p>=5)[1+p^(-2sigma)/(1-p^(-sigma))^2],
    C_W=product_(p>=5)[1+p^(-2sigma)/(1-2p^(-sigma))].      (5)

Proof. At a prime write x=p^(-s). At a split prime the exact local
series V=B/A and W=1/V are

    V=(1-2x)/(1-x)^2 =1-sum_(j>=2)(j-1)x^j,
    W=(1-x)^2/(1-2x) =1+sum_(j>=2)2^(j-2)x^j.

At an inert prime they are respectively 1/(1-x^2) and 1-x^2.
At a ramified or excluded prime they are BOTH 1. These identities
prove (3) as formal series with every prime power retained. Their local
absolute norms are dominated by (5). Since p>=5 and sigma>1/2,
2p^(-sigma)<1. Both products converge by comparison with sum p^(-2sigma).
This proves (4), and normal convergence gives holomorphic, nowhere-zero
V and 1/V in Re s>1/2. QED.

This strengthens the scope of the fixed-field primitive-core adapter
in #996: the kernels here are uniform over ALL these fields and ramified
primes remain in the source. The familiar split/inert factors themselves
are inherited/classical, not a new discovery.

Every nontrivial zero of ordinary zeta in Re s>1/2 is a pole of B_Delta
for EVERY Delta. A zero of the entire nonprincipal L-factor can only
increase the pole order. The correction V cannot cancel it. No conclusion
about the size of B or of its partial sums follows just from this fact.

The same kernels give no-loss transfers of partial-sum or uniformly
polynomial-phase power bounds at any exponent beta>1/2. In a convolution
sum the phase P(dm) has the same fixed degree; the cost is bounded by (4)
at beta plus any prescribed positive loss. Uniformity in Delta is retained.

## 2. A finite, polynomial-size field family

For real Q>=2^16 set

    D(Q)={d<=Q : d squarefree, d=3 mod 4}, N_Q=#D(Q).

### Lemma Q2 (count and a nonprincipal character average)

N_Q>=Q/8. For every odd squarefree r>1,

    |N_Q^(-1) sum_(d in D(Q)) chi_(-d)(r)|
       <=24 sqrt(r/Q),                                  (6)

and the stronger bound is

    <=24 r^(1/4) sqrt(1+log r)/sqrt Q.                    (7)

One can always take the minimum with the trivial bound 1.

Proof of the count. The progression 3 mod 4 contains at least Q/4-1
positive integers. Every nonsquarefree member is divisible by a^2 for
an odd a>=3. The number for one a is at most Q/(4a^2)+1. Using
sum_(a>=3) a^(-2)<=1/9+integral_3^infinity t^(-2)dt=4/9 gives

    N_Q >=5Q/36-sqrt Q-1 >=Q/8, Q>=2^16.

The last inequality follows on writing u=sqrt Q>=256; u^2/72-u-1>0
there and is increasing.

For the character bound expand mu(d)^2=sum_(a^2|d)mu(a).
Only odd a occur, and with d=a^2 b the progression becomes b=3 mod 4.
Terms with gcd(a,r)>1 vanish; in the others chi_(-a^2b)(r) is a
constant sign times the primitive nonprincipal Jacobi character (b/r).
The progression in b covers every residue mod r in a complete period,
since 4 is invertible mod r. Thus its sum over any initial segment is
bounded by min(r,Q/a^2). For any positive T,

    sum_(a>=1) min(T,Q/a^2) <=3 sqrt(QT)                 (8)

when T<=Q: split at sqrt(Q/T), bound the initial part by sqrt(QT),
and use sum_(a>L)a^(-2)<=2/L for L>=1. If T>Q use
sum a^(-2)<2 to obtain 2Q<=2sqrt(QT). This proves (8) in all cases.
Take T=r and divide by N_Q to prove (6).

For completeness the sharper incomplete character estimate needs no
hypothesis on zeros. Fourier inversion of a primitive character modulo
r uses Gauss coefficients of modulus sqrt r. Removing complete periods
and bounding each remaining geometric sum gives

    |sum_(j=0)^(H-1) (4j+3 / r)|
       <=r^(-1/2) sum_(a=1)^(r-1) 1/[2||a/r||]
       <=sqrt r H_floor(r/2) <=sqrt r(1+log r).

The symbol in this display is the Jacobi symbol. The geometric inequality
uses |1-exp(2pi i a/r)|>=4||a/r||. The primitive Gauss magnitude follows
by Fourier inversion and character orthogonality (or by the usual square
of the quadratic Gauss sum); primitivity holds for every odd squarefree r.
In (8) take T=sqrt r(1+log r), then divide by N_Q. This proves (7).
All a, including those above the splitting point, have been retained. QED.

## 3. The whole signed average recovers ordinary mu with an explicit error

### Theorem Q3 (uniform weighted finite-family comparison)

For every X>=1 and every complex array u_n with |u_n|<=1,

  |N_Q^(-1) sum_(d in D(Q)) sum_(n<=X) b_(-d)(n)u_n
                         -sum_(n<=X)mu6(n)u_n|
       <=48 X^(3/2)/sqrt Q,                              (9)

and also

       <=96 X^(5/4) sqrt(1+log X)/sqrt Q.                (10)

Proof. For squarefree n the exact expansion is

    product_(p|n)(1+chi(p))=sum_(r|n)chi(r).

Every r is squarefree; no assumption that chi(r) is nonzero is made.
The r=1 term is exactly mu6(n) in the family average. Apply (6) to all
remaining r and take absolute values only AFTER this exact cancellation.
The error is at most

    24 Q^(-1/2) sum_(n<=X) sum_(r|n,r>1)sqrt r
    <=24 X Q^(-1/2) sum_(r<=X)r^(-1/2)
    <=48 X^(3/2)/sqrt Q.

Using (7) instead and the bounds
sqrt(1+log r)<=sqrt(1+log X),
sum_(r<=X)r^(-3/4)<=4X^(1/4), proves (10). Removing squarefree and
coprimality constraints in these last POSITIVE upper sums is legitimate;
they have not been removed from the original observable. QED.

The error is uniform over all u_n, so it applies in particular to fixed
height norm phases or real polynomial phases. This is an actual arithmetic
approximation estimate, not a theorem that the final average is small.

### Consequence for a zeta-only route

Set u_n=1 and choose a candidate boundary theta>1/2. If Q=X^q with

    q>=5/2-2theta,

then (10) costs at most X^(theta) times a logarithm. Thus a bound of
order X^(theta+epsilon) for the SIGNED field average would imply the
same bound for the ordinary incomplete Mobius sum. Its Dirichlet series
is 1/zeta6; Abel summation then excludes every zeta zero to the right of
theta. No claim that the required mean estimate holds is made.

At theta=5/6 the required family scale is Q=X^(5/6), up to arbitrary
small slack. For RH the family scale is Q=X^(3/2), again with optional
positive slack. This criterion targets ORDINARY zeta; it does not require
square-root estimates for each quadratic field separately. The family size
moves with X. We use the coefficient comparison FIRST, not a Mellin
transform falsely treating this moving family as a fixed Dirichlet series.
Although every individual B_Delta retains a zeta pole, its residues could
cancel in a signed combination; no blanket pole-preservation theorem for
arbitrary combinations is asserted.

## 4. What the common-factor idea does NOT give for free

If F_d(s)=zeta(s)L(s,chi_d) and M_d is a finite mollifier, then at any
zeta zero rho the full mean of |F_d(rho)M_d(rho)-1|^2 is exactly 1.
Consequently a strict bound below 1 would indeed exclude that zero.
But a cofactor theorem for L alone does not prove this full-product bound.
The r=1 term in the proof of Q3 is the exact COMMON Mobius channel; it is
not an off-diagonal term that quadratic orthogonality can delete.

Nor may an exceptional set be thrown away without payment. Uniformly in d,

    |sum_(n<=X)b_(-d)(n)u_n| <=sum_(n<=X)2^omega(n)
                                  <=X(1+log X).

Deleting E members while retaining normalization N_Q therefore costs at
most (E/N_Q)X(1+log X). At theta=5/6,Q=X^(5/6), an exceptional fraction
Q^(-delta) would require delta>=1/5 merely to keep this deletion cost at
the intended power. Cofactor zero-density is not a bound on the common
source. The OPEN task is signed control of this full field mean.

## 5. Finite verification boundary

The checker reconstructs actual primitive quadratic characters for the
specified fundamental discriminants, including ramified local values. It
checks complete rational-integer convolution identities, fixed exclusions,
finite character means, and the average/product identity. These are not
L-value computations, infinite-field computations, or a proof of the open
cancellation estimate. See CHECKS.json for exact ranges and counts.
