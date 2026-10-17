# Unconditional norm-fiber bounds for the actual Gaussian moments

Status: PROPOSED component mathematics, with complete written proofs below.
No unproved moment estimate, RH/GRH, quasi-RH theorem, or theta transformation
is a hypothesis. No independent referee or formal verification is claimed.
This is an unconditional *sector* theorem, not a bound for the whole moment.
The methods are classical Euler products, finite etale algebras, a positive
Laplace Tauberian argument, Gaussian integration, and a bounded-degree Schur
estimate. No general literature-priority claim is made.

## 1. Exact objects and the statement

Fix a number field F of degree d. Fix a finite set S of prime ideals,
containing the primes above 2 and 3, as in the source packets. Constants may
depend on F and S; none are asserted uniform in the discriminant.
Write

    F tensor_Q F = E_1 x ... x E_kappa.                         (1)

The E_j are number fields, repeated isomorphic factors included. Thus
kappa is a fixed positive integer. If F/Q is Galois, kappa=d. For a quadratic
field kappa=2; for Q, kappa=1. In general, if G acts on the embeddings of F
in its normal closure, kappa is the number of G-orbits on ordered pairs of
embeddings. This is NOT generally d: a non-Galois cubic has kappa=2.

Let w be any nonnegative measure of finite mass Z_w on rows u. Fix this SAME
measure at every column scale. At each prime ideal p outside S, put q=Np
and choose measurable phases |a_p(u)|,|b_p(u)|<=1. At every additional masked
prime set both phases to zero. For an integer m>=2 choose any ONE of the
following local coefficient families, with x a formal variable:

    native:       1-a_p x;
    coupled:      1-(1-1/q)a_p x-b_p q^(m/2-1)x^m;
    two-channel:  (1-a_p x)(1-b_p q^(m/2-1)x^m);
    geometric:    1-(1-1/q)a_p x/(1-b_p q^(m/2-1)x^m).       (2)

Let f_m(I,u) be their multiplicative ideal coefficients. Factors at S are 1.
The source at every scale is the literal Gaussian

    W_c(y)=(2 sqrt(pi))^(-1)y^(-c) exp[-(log y)^2/4],
    A_m(X,u)=sum_I f_m(I,u) W_c(NI/X),                       (3)

where c is any fixed real number (c=5/6 in the Dedekind application).
The phases and masks are unchanged as X varies. The geometric coefficients
have exponents 1,1+m,1+2m,..., as in #950; the other families are distinct.

Fix a positive integer k. The actual order-2k critical cumulative energy is

    E_2k(D;w)=integral_0^D integral |A_m(X,u)|^(2k) dw(u)
                                                   dX/X^(k+1). (4)

The theorem does NOT normalize by X^2 at every k. This energy is finite.
All positive and negative terms in its expansion are retained.

For every ordered k-tuple I=(I_1,...,I_k), put N=prod_i NI_i and

    b_k(I)=exp[-(1/4) sum_i (log NI_i-log N/k)^2],
    C_k(N,u)=sum_(prod_i NI_i=N) prod_i f_m(I_i,u) b_k(I).    (5)

The sum is over actual ideals, including distinct ideals of the same norm,
repeated ideals, common prime factors, and every original nonunit zero.
These C_k are not claimed multiplicative when k>1. Define

    beta=2c-1,
    gamma_ck=(sqrt(2pi k)/k)(2 sqrt(pi))^(-2k)exp(k beta^2/2),

    K_D,k(N,M)=gamma_ck/sqrt(NM) exp[-log(N/M)^2/(8k)]
       * Phi((k log D-(log N+log M)/2-k beta)/sqrt(k)),       (6)

where Phi is the standard normal distribution function.

### Theorem NF1: full product-norm block at all fixed orders

For D>=1, uniformly over every m>=2 and every allowed row/profile/mask,

    E_2k(D;w)=sum_(N,M>=1) K_D,k(N,M)
                          integral C_k(N,u)conj(C_k(M,u))dw(u), (7)

and its COMPLETE equal-product-norm block satisfies

    0 <= N_2k(D;w)
       :=sum_N K_D,k(N,N) integral |C_k(N,u)|^2dw(u)
       <= C_(F,S,c,k) Z_w (1+log D)^(kappa k^2).             (8)

This is an actual arithmetic upper bound, not a hypothesis about an unknown
native moment. It is uniform in the auxiliary degree m, but the constants
and logarithmic exponent depend on fixed k. No useful growing-k estimate
is claimed. The logarithmic power in (8) is not claimed optimal for k>1.
The same upper bound holds for the sum of absolute values of ALL underlying
2k-tuple terms with equal product norms: repeat (5) with absolute source
coefficients. Thus arbitrary additional tuple selectors of modulus at most
one preserve this upper bound, although they do not preserve the identity
with the signed N_2k. This stronger absolute bound is denoted Nabs_2k below.

### Theorem NF1b: the same sector at the original FIXED column scale

Put

    Nfix_2k(X;w)=sum_N W_(c,k)(N/X^k)^2
                                integral |C_k(N,u)|^2 dw(u),

where W_(c,k) is the explicit Gaussian in (23). This is the complete
same-product-norm sector in the expansion of the ORIGINAL fixed-scale
moment integral |A_m(X,u)|^(2k)dw(u). For X>=1,

    Nfix_2k(X;w) <= C_(F,S,c,k) Z_w X^k
                                      (1+log X)^(kappa k^2). (8b)

The same bound holds for the sum of absolute underlying tuple terms.
Consequently it is O_epsilon(Z_w X^(k+epsilon)) at every fixed k. This is
not merely a scale-averaged estimate, and the row measure need not vary
with X. It is still ONLY the specified sector, not the whole moment.

### Corollary NF1c: the original compact-test column windows

Let W be any bounded complex function supported in (0,b], with b>0 fixed,
and set A_W(X,u)=sum_I f_m(I,u)W(NI/X). This includes the fixed smooth
annular tests and the hard window 1/2<NI/X<=1. Define

    C^W_k(N;X,u)=sum_(prod_i NI_i=N) prod_i[f_m(I_i,u)W(NI_i/X)].

Then for X>=1,

    sum_N integral |C^W_k(N;X,u)|^2dw(u)
      <= C_(F,S,b,k) ||W||_infinity^(2k) Z_w X^k
                                             (1+log X)^(kappa k^2). (8c)

The same estimate holds after replacing every underlying tuple coefficient
and test value by its absolute value. This is the complete equal-product-
rational-norm sector in the original compact-test order-2k moment. No
Gaussian conversion or scale averaging is needed. The bounded-degree graph
and subpower additive-gap conclusions in NF2 hold for this sector as well.
Only the selected sector is bounded; the full compact-test moment is not.

### Theorem NF2: sparse cross-norm blocks, including subpower norm gaps

Let G be any symmetric graph on the positive integers, without loops, whose
maximum number of neighbors is L<infinity. Keep ALL terms in (7) indexed by
G. Then even their sum of absolute values AFTER grouping by product norm is

    sum_((N,M) in G) K_D,k(N,M)
           |integral C_k(N,u)conj(C_k(M,u))dw(u)|
       <= L N_2k(D;w).                                    (9)

The identical graph bound holds at fixed scale with Nfix_2k on the right
and kernel W_(c,k)(N/X^k)W_(c,k)(M/X^k) on the left. Thus all underlying
tuple terms with |N-M|<=R(X)=X^o(1) have absolute size
O_epsilon(Z_w X^(k+epsilon)) at fixed scale, uniformly in m.

Edges are ordered in (9). In particular all terms with 0<|N-M|<=R cost at
most 2R times (8), for any nonnegative integer R. Together with the norm
block they cost at most (2R+1) times (8).

For any fixed k and R(D)=D^o(1), that entire selected contribution is
O_epsilon(Z_w D^epsilon), for each epsilon>0. This includes, for example,
R(D)=floor(exp(sqrt(log(2D)))). The gap is ADDITIVE IN THE PRODUCT RATIONAL
NORMS, not in each factor, not in log norm, and not in an ideal metric.
No terms outside that relation are controlled by (9). The same proof with
absolute source coefficients bounds the underlying absolute tuple sum by
L Nabs_2k. Thus a restricted tuple sector has the same logarithmic upper
bound, not necessarily L times the smaller signed norm-block N_2k.

### Theorem NF3: the logarithmic order is real, not an ideal-diagonal artifact

Take k=1, one scalar row of weight one, a_p=1 outside S, and any fixed
profile |b_p|<=1. No extra row masks are used. Fix m. For each family in (2),
let B(N)=sum_(NI=N) f_m(I). Set A=F tensor_Q F and

    Z_A(s)=prod_(j=1)^kappa zeta_(E_j)(s),
    R_A=prod_j Res_(s=1) zeta_(E_j)(s)>0,
    D_p(s)=sum_(r>=0) |B(p^r)|^2 p^(-rs),
    H(1)=prod_p D_p(1)/Z_(A,p)(1).                         (10)

The product H(1) converges to a strictly positive real number. Then

    N_2(D) ~ [gamma_c1 R_A H(1)/kappa!](log D)^kappa.        (11)

Every rational prime, including ramified and excluded primes, occurs in
(10); their finite factors must not be silently omitted. The asymptotic is
for each fixed m and fixed b profile. It is NOT asserted uniform for moving
profiles or moving m. The upper estimate (8), in contrast, is uniform in m
and all rows. For the native source m and b do not matter.

Thus the original literal ideal diagonal of #952 can be O(log D) while the
full equal-rational-norm block is of order log^2 D over Q(omega), or log^4 D
over Q(zeta_12). Both remain subpower. This does not make the remaining
cross-norm block small.

More precisely, for every nontrivial number field (kappa>=2), the SIGNED
subtotal over distinct ideals of the same norm has the SAME positive main
term (11). Indeed the literal ideal diagonal is O_(F,c)(1+log D): using
(12), its squared ideal-coefficient count is <=A_F zeta_F(2) T, by the same
unique representation as (14), now with exponent m-2-m=-2. Gaussian
partial summation gives its logarithmic diagonal. Subtracting that smaller
quantity from (11) proves the assertion. Thus this is an unconditional
asymptotic for a genuine piece of the native/coupled signed covariance.

## 2. One uniform coefficient majorant for all four families

At an ideal prime use the nonnegative local series

    T_(m,q)(x)=(1+x)/(1-q^(m/2-1)x^m).                     (12)

It coefficientwise dominates the absolute values of every factor in (2),
including the two-channel shared-prime term and the full geometric series.
Let t_m(I) be its ideal coefficients and t_m(N)=sum_(NI=N)t_m(I). All are
nonnegative, and t_m(N) is multiplicative in the RATIONAL integer N.
Write t_m,k=t_m * ... * t_m (k rational Dirichlet convolutions). Equation (5)
and 0<b_k<=1 give

    |C_k(N,u)| <= t_m,k(N)                                (13)

uniformly in rows. No source coefficient has been replaced in an identity.

Every supported ideal in (12) is uniquely I=J D^m with J squarefree and D
unrestricted; J and D MAY share primes. Its coefficient is (ND)^(m/2-1).
Classical ideal counting I_F(T)<=A_F T therefore gives

    sum_(NI<=T)t_m(I)
      <= A_F T sum_D (ND)^(-m/2-1)
      <= A_F zeta_F(2) T,                                (14)

uniformly in m. Restrictions at S only reduce this bound. Partial summation
against |W_c'| shows sum_I t_m(I)|W_c(NI/X)|<=C_(F,c)X.
Consequently the absolute expansion of (4) is dominated by C Z_w X^(k-1)
on (0,D), which is integrable. This justifies its infinite expansions and
all norm-fiber regrouping at fixed D; no Gaussian tail is discarded.

## 3. The field tensor square pays every norm multiplicity

At a rational prime p unramified in F, let f_1,...,f_g be the residue degrees
of its prime ideals, and let g_1=#{i:f_i=1}. For finite fields,

    F_(p^a) tensor_(F_p) F_(p^b)
       = product_(1<=j<=gcd(a,b)) F_(p^lcm(a,b)).           (15)

One proof extends scalars to an algebraic closure: Frobenius acts on pairs
of cyclic sets of lengths a and b; each orbit has length lcm(a,b) and there
are gcd(a,b) orbits. This also proves the decomposition without choosing
noncanonical field embeddings. Hence, away from finitely many ramified
primes, the Euler factor of the etale algebra in (1) is

    Z_(A,p)(s)=prod_(i,j)
                (1-p^(-lcm(f_i,f_j)s))^(-gcd(f_i,f_j)).    (16)

In particular its coefficient of p^(-s) is g_1^2. The tensor algebra has
Q-dimension d^2, so uniformly for real s>=1 and p>=5,

    Z_(A,p)(s)^(k^2)=1+k^2 g_1^2 p^(-s)+O_(d,k)(p^(-2)). (17)

For clarity, (1) follows because a finite separable algebra is etale and a
finite etale Q-algebra is a product of number fields. In the normal closure,
its factors correspond to orbits of the diagonal G-action on ordered pairs
of embeddings. When F is Galois its embedding action is regular, giving d
orbits. The diagonal and off-diagonal embedding pairs are separate orbits
for a nontrivial quadratic; a non-Galois cubic has the natural S3 action
and two orbits. These examples need no Chebotarev hypothesis or theorem.

### Lemma NF4: a uniform harmonic square bound

For L>=0,

    sum_(N<=exp L) t_m,k(N)^2/N
           <= C_(F,S,k)(1+L)^(kappa k^2),                 (18)

uniformly in all integers m>=2.

Proof. Put r=p^(-1/2). At the critical weight, one ideal factor in (12)
has TOTAL coefficient mass

    T_(m,p^f)(p^(-f/2))=(1+r^f)/(1-r^(2f))=(1-r^f)^(-1). (19)

The only rational-norm degree-one coefficient of the k-th product is k g_1.
Every other nonconstant coefficient has critical mass of formal r-degree
at least two: a geometric power contributes r^(2f) even when its norm degree
is mf. Thus the sum of critical masses at norm degrees >=2 is bounded by

    (1-r)^(-dk)-1-dk r <= B_(dk) r^2,
    B_n=n(n+1)2^(n+1),                                  (20)

for p>=5. To see the first bound, expand prod_i(1-r^f_i)^(-k)
coefficientwise; its r-linear coefficient is k g_1, and each coefficient
of degree >=2 is bounded by that of (1-r)^(-dk). Subtract the respective
constant and linear terms. The second bound is Taylor's theorem, since
r<=1/2 and the second derivative is n(n+1)(1-r)^(-n-2).

Squaring the nonnegative tail yields, uniformly for real s>=1,

    D^+_(m,k,p)(s):=sum_j t_m,k(p^j)^2 p^(-js)
       =1+k^2 g_1^2 p^(-s)+E_p(s),
    0<=E_p(s)<=B_(dk)^2 p^(-2).                           (21)

The finitely many ramified or excluded rational primes are harmless; their
critical factors are uniformly bounded by (1-p^(-1/2))^(-2dk). Exclusions
remove ideal factors, not conjugate identities. Equations (17)--(21) show

    sum_N t_m,k(N)^2 N^(-1-t)
       <= C_(F,S,k) Z_A(1+t)^(k^2)
       <= C'_(F,S,k) t^(-kappa k^2),  0<t<=1.              (22)

Here we use only the classical positive simple pole at 1 of each Dedekind
zeta function in (1). Its residue is positive. No zero-free half-plane is
used. The Euler products and nonnegative sums agree for t>0 by monotone
limits and the convergent local expansion. With t=1/(1+L), every N<=exp L
has N^t<=e. Equation (18) follows immediately. QED.

## 4. Proof of NF1 and NF2 for the actual higher moment

The exact square-completion identity

    sum_i(log NI_i-log X)^2
      =sum_i(log NI_i-log N/k)^2
                      +(log(N/X^k))^2/k

gives

    A_m(X,u)^k=sum_N C_k(N,u) W_(c,k)(N/X^k),
    W_(c,k)(y)=(2 sqrt(pi))^(-k)y^(-c)exp[-(log y)^2/(4k)]. (23)

Set Y=X^k. The energy measure transforms as

    dX/X^(k+1)=(1/k)dY/Y^2,                              (24)

not dY/Y and not dY/Y^(k+1). With a=log N, b=log M, x=log Y,
mu=(a+b)/2, the exponent in the pair integral is exactly

    beta x-c(a+b)-((x-a)^2+(x-b)^2)/(4k)
      =-(x-mu-k beta)^2/(2k)-mu+k beta^2/2-(a-b)^2/(8k).

This proves (6)--(7). Absolute Fubini was established in (14).
The kernel is a Gaussian Gram kernel, so

    0<K_D,k(N,M)<=sqrt(K_D,k(N,N)K_D,k(M,M)).              (25)

On its diagonal, use (13) and (18):

    N_2k <= gamma_ck Z_w sum_N [t_m,k(N)^2/N]
           Phi((k log D-log N-k beta)/sqrt(k)).            (26)

Let H(L) be the sum in (18), with H(L)=0 for L<0. If Z is a standard normal,
Tonelli identifies the sum in (26) with

    E_Z H(k log D-k beta-sqrt(k) Z).

Its bound is C_(F,S,c,k)(1+log D)^(kappa k^2), since every fixed absolute
normal moment is finite. This proves NF1, including the full Gaussian tail.

For NF1b, the exact normalized pointwise weight is

    X^(-k) W_(c,k)(N/X^k)^2
      =(2 sqrt(pi))^(-2k) exp(k beta^2/2)/N
           * exp[-(log N-k log X+k beta)^2/(2k)].

Use (13) and write the norm sum as a Gaussian integral against the
nonnegative harmonic counting measure in (18). On each unit interval
[j,j+1], that measure is at most C(2+j)^(kappa k^2). The supremum of the
Gaussian there decays quadratically in the distance from
k log X-k beta. Summing these intervals gives
C_(F,S,c,k)(1+log X)^(kappa k^2). This proves (8b). Replacing each source
coefficient by its absolute value proves the absolute-tuple variant.

For NF1c, all nonzero product norms obey N<=(bX)^k, and
|C^W_k(N;X,u)|<=||W||_infinity^k t_m,k(N). For T=(bX)^k>=1,

    sum_(N<=T) t_m,k(N)^2
      <= T sum_(N<=T) t_m,k(N)^2/N
      <= C T (1+log T)^(kappa k^2).

This proves (8c). If T<1 the source is zero. Apply the same argument to
absolute source and test coefficients for the absolute-tuple statement.
The constants can depend on the fixed upper support b; no control of a
varying test class beyond the displayed sup norm and support is needed.

For NF2 put v_N=sqrt(K_D,k(N,N)) ||C_k(N,.)||_(L2(w)). Cauchy in w and
(25) bound each summand by v_N v_M. Then

    sum_((N,M) in G) v_N v_M
       <= (1/2)sum_((N,M) in G)(v_N^2+v_M^2)
       <= L sum_N v_N^2.

The same argument with v_N=W_(c,k)(N/X^k)||C_k(N,.)||_2 proves the fixed-scale
version, since (8b) makes the squared sequence summable. For compact tests
use v_N=||C^W_k(N;X,.)||_2 and (8c); the norm set is finite. In the cumulative
version the series converge by (8); finite truncation followed by monotone limits
justifies the graph estimate. This proof takes absolute values only AFTER
the full ideal tuples have been grouped by their product norms. Arbitrary
subsets inside a norm fiber do not inherit its signed C_k. QED.

## 5. The exact logarithmic asymptotic at order two

For k=1 and the principal scalar profile, B(N) is multiplicative in N.
At a good unramified prime its first coefficient is -g_1 for native and
two-channel, and -(1-1/p)g_1 for coupled and geometric. Equation (20)
bounds all higher-degree critical absolute masses. Thus for every family,

    D_p(s)=1+g_1^2 p^(-s)+O_d(p^(-2)),  real s>=1,          (27)

uniformly in m and phases. The finite bad factors have positive constant
term one. Each D_p(1) is finite, and the quotient in (10) is positive and
1+O_d(p^(-2)) outside a finite set. Hence H(1) exists and is strictly positive.
For FIXED m and b, dominated convergence of logarithms gives

    F(1+t):=sum_N |B(N)|^2 N^(-1-t)
       ~ R_A H(1) t^(-kappa) as t decreases to zero.        (28)

No analytic continuation of F to the left of 1 is needed. The local series
are continuous down to 1 by their absolute critical bounds.

For completeness, the positive Tauberian step in this application can be
proved as follows; it is a version of the classical Karamata argument.
Let mu=sum_N |B(N)|^2/N delta_(log N), A0=R_A H(1), and write L_mu(t)=F(1+t).
Give x=t log N probability mass e^(-t log N)|B(N)|^2/[N L_mu(t)]. Its Laplace
moments at integers j>=0 tend to

    L_mu((j+1)t)/L_mu(t) -> (j+1)^(-kappa).

After z=e^(-x), these are ordinary moments on [0,1]. Polynomial approximation
therefore gives weak convergence to the pushforward of the Gamma(kappa,1)
law with density x^(kappa-1)e^(-x)/(kappa-1)!. The bounded function
exp(x) 1_(0<=x<=1) has just one discontinuity of zero limiting mass, so

    mu([0,1/t])/L_mu(t) ->
      integral_0^1 x^(kappa-1)/(kappa-1)! dx=1/kappa!.

Thus H_B(L):=sum_(N<=exp L)|B(N)|^2/N ~ A0 L^kappa/kappa!.
The polynomial upper bound (18) also holds for H_B. Finally the exact k=1
diagonal is

    gamma_c1 E_Z H_B(log D-beta-Z).

Dominated convergence after division by (log D)^kappa proves (11).
The dominator follows from (18) and the finite normal moments. QED.

## 6. Exact scope relative to the full problem

NF1 bounds all pairs of k-tuples with EQUAL PRODUCT RATIONAL NORM. It does
not merely select equal ideals, principal characters, sixth-power rows,
or tuples supported on a chosen finite prime set. For k>1, equality of
products of norms need not mean equality of ideal products or sextic charge.
All native masks remain. NF2 covers the stated sparse relations on these
complete fibers. This supplies actual unconditional estimates for a portion
of the covariance left in #952, with an all-order version for its Gaussian.

The total energy (4) can still be much larger: (7) includes pairs of product
norms outside every sparse graph considered here. A positive kernel does not
bound that dense signed part. For example over Q the allowed native profile
a_p=-1 has coefficients mu(n)^2 (with the fixed S exclusions). Elementary
squarefree counting gives A(X) of order X for the positive Gaussian, hence
E_2(D) of order D, despite NF1 giving an O(log D) norm block. This example
changes the source and is NOT a counterexample to its principal Mobius case.

No new zero-free exponent is asserted. The only exact asymptotic claimed
is (11) for fixed order two and its specified principal scalar profile.
The exponent kappa k^2 in (8) is a safe upper bound, not a claim of optimal
matching geometry. The FULL original fixed-scale compact-test moment contracts do
not follow from the compact-test sector estimate (8c) or the cumulative
normalization. The sector contract itself is proved directly in (8c).

## 7. This includes actual rough, nonprincipal native tuples

The newly bounded norm relation is not synonymous with the previously
bounded principal-character or smooth-singleton sectors. Over Q(omega),
take distinct conjugate prime ideals p and bar(p) above a split rational
prime ell outside S. For any k>=1 choose the k-tuples

    I=(p,...,p),       J=(p,...,p,bar(p)),

with k copies on each side and k-1 copies of p on the right. Every column
is a squarefree ideal of norm ell; both product rational norms are ell^k.
The net sextic charges are +1 at p and -1 at bar(p). Their quotient
character is nonprincipal by CRT (the two residue coordinates are
independent), and its conductor has norm ell^2. The original zero mask
contains BOTH primes. Unit phases cancel, since both prime norms are ell.
For k=1 both primes are singletons; for k>1 bar(p) remains a singleton.

Set the column scale D=ell. For large ell, this singleton is larger than
(log D)^2, so the smooth-singleton theorem does not cover it. At row height
H=D^h with h<2, its active conductor exceeds H and its neutral radical is
one. Thus the d=1 term survives the earlier conductor-divisor window;
low-radical exact annihilation does not apply. NF1 bounds the WHOLE
equal-product-norm sector containing this family, not just this example.
This comparison concerns the literal tuple algebra; it does not assert
dominance over all older sector estimates or a new estimate of the dense
unequal-norm remainder. Infinitely many split primes are classical, but
no prime-distribution theorem is needed in the proofs of NF1--NF3.

## 8. Classical credit and the scope of the addition

The permutation-character/double-coset exponent kappa is classical. During
the literature comparison, Durkan--Karak--Mahatab, arXiv:2606.27516v3,
Introduction equations defining Z_ij and Corollary 1.2, was found to state
this same invariant explicitly for Dedekind-zeta moment correlations.
Their main critical-line moment theorem assumes GRH; it is NOT used here.
The elementary Euler first-coefficient comparison on Re(s)>1 used above
requires no such assumption. The positive Tauberian step is also classical,
not a new Tauberian theorem.

The proposed contribution here is their source-compatible application to
ALL complete product-norm fibers of the actual Gaussian Mobius, coupled,
two-channel and radical-preserving geometric sources, with uniform m, the
full masks/tails, the exact higher-order scale measure, the scalar
asymptotic, and the bounded-gap sector. The external and repository
comparison is limited to the sources listed in SOURCES.md. This is not an
exhaustive novelty audit, and no claim of a first result in the literature
is made. It does not improve the published zero-free boundary.
