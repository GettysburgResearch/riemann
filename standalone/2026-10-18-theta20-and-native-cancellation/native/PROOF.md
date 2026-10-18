# Complete native denominator cancellation and automatic balance removal

Status: **proposed unconditional component proofs; independent mathematical
review required. The remaining large-denominator energy and RH are OPEN.**

The new component is a bound on an entire sector of the signed native Newton
amplitude. It removes every reduced rational denominator up to a power cutoff,
including that denominator's contributions from ALL old-prefix products up to
Y^2. This differs from #988's cutoff on the products themselves. An exact
masked-Mobius factorization pays the complete denominator coefficients. On
the unconditionally cofinal native reciprocal crossings, both old balance
coordinates also disappear with a vanishing complete L2 error. A second
unconditional bound then removes ALL square reduced denominators, and more
generally a growing sector with small squarefree core, even when those
denominators range to Y^2. Its complete coherent energy is subpower for
any subpower core cutoff.

The rational modes, Möbius inversion, the masked reciprocal bound, harmonic
summation, Mellin transforms and the spacing argument are classical. No
worldwide priority, new prime number theorem, subconvexity bound, or new
zero-free fraction is claimed. No CT or character-family theorem is used.

## 1. Objects and main amplitude theorem

For an integer Y>=2 put

    b=Y+1, N=b^2-1,
    g_Y(n)=mu(n) 1_(n<=Y), z_Y=g_Y*g_Y,
    m(k)=sum_(n<=k)mu(n)/n, M_Y=m(Y), F_K=sum_(k<=K)m(k)^2,
    L_Y=sum_(n<=Y)mu(n)log(n)/n,
    B_Y=1+L_Y-(log Y+gamma/2)M_Y.

The convolution is Dirichlet convolution. No coefficient beyond Y is needed
to form z_Y. Define the COMPLETE reduced-denominator coefficient

    C_Y(q)=sum_(d<=Y^2, q|d) z_Y(d)/d.                    (1.1)

It includes d>k when used at an output k. It is not a product-truncated sum.
Let c_q(n)=sum_(a mod q,(a,q)=1) exp(2pi i an/q) be the integer Ramanujan
sum, and let Lambda(q)=log p if q is a positive prime power p^a, and zero
otherwise. For q>=2 and real x>0 set

    S_q(x)=sum_(n<=x)c_q(n)/n+Lambda(q).                  (1.2)

This is a real step function, constant on each integer cell [k,k+1).
Although S_q tends to zero, the centering Lambda(q) must remain.

Fix 1/2<rho<2/3, put alpha=2-3rho, and use the complete dyadic annuli

    X_j=2^j b<b^2, U_j=min(2X_j,b^2),
    I_j=[X_j,U_j), Q_j=floor(X_j^rho).

On every integer k in I_j define

    V_(Y,rho)(k)=-sum_(Q_j<q<=Y^2) C_Y(q)S_q(k),
    A_Y(k)=2M_Y B_Y+M_Y^2 log(Y^2/k),
    R(x)=H_floor(x)-log x-gamma, H_0=0.                 (1.3)

**Theorem 1 (complete low-denominator amplitude).** Uniformly in Y and in
the complete strict square step,

    ||m-A_Y+M_Y^2 R-V_(Y,rho)||_l2(b,...,N)^2
       <= E_(Y,rho),
    E_(Y,rho)=2048/(1-2^(-alpha))
                    b^(-alpha)(1+log b)^4.             (1.4)

The signs in (1.4) come from the exact identity in Section 3. Equivalently,
m=A_Y-M_Y^2 R+V plus a controlled low-denominator remainder.

Every product d<=Q_j contributes only to the removed denominator sector,
but the removed sector also contains all q<=Q_j modes of every d>Q_j.
Thus (1.4) retains fewer modes than a product cutoff at the same threshold.
No claim that the remaining coefficients have small total mass follows.

For rho=5/8 the error in squared norm is O(Y^(-1/8)log^4 Y). This controls
a component of the amplitude itself, not just its variation around means.

## 2. Literal masked reciprocal sums pay every complete coefficient

Write

    m_d(x)=sum_(n<=x,(n,d)=1)mu(n)/n,

with value zero for x<1. The classical bound is

                  |m_d(x)|<=1 for ALL d>=1, x>0.        (2.1)

Here is Tao's elementary prime-subsemigroup proof in this special case.
For integer x, let A count integers <=x coprime to d and let B count those
whose prime factors all divide d. Finite divisor inversion gives

    B=sum_(n<=x,(n,d)=1)mu(n)floor(x/n).

Since {x/n}<=1-1/n, it follows that

    |x m_d(x)|<=B+A-sum_(n<=x,(n,d)=1)1/n.

The two sets counted by A and B intersect only at 1, so A+B<=x+1. The
last harmonic sum is at least 1. This proves (2.1). For real x use its
integer part. This is Theorem 1.1 and equation (9) of Tao's
arXiv:0908.4323v5, not a new masked-Mobius estimate.

**Lemma 2 (exact complete coefficient factorization).** If q has a prime
cube factor, C_Y(q)=0. Otherwise uniquely write q=r^2 s, where r,s are
coprime squarefree integers. Then

    C_Y(r^2 s)=mu(s)/(r^2 s)
       sum_(u v w=s, u,v,w pairwise coprime)
         m_(r u w)(Y/(r u w)) m_(r v w)(Y/(r v w))/w.    (2.2)

All ordered triples occur; no coprimality between an old input and an
unrelated mask is added. In particular

    |q C_Y(q)|<=product_(p|s)(2+1/p),                    (2.3)
    sum_(q<=Q) q^2 |C_Y(q)|^2
                    <=32 Q (1+log Q)^3, Q>=1.          (2.4)

Proof of (2.2). Each nonzero g_Y input is squarefree, hence a product has
no prime cube. Put T(d)=sum_(a<=Y,d|a)mu(a)/a. For squarefree d,
T(d)=mu(d)m_d(Y/d)/d. A prime dividing r must divide both input indices.
For p|s use

    1_(p|ac)=1_(p|a)+1_(p|c)-1_(p|a)1_(p|c).

Multiplying these exact identities gives

    C_Y(r^2 s)=sum_(u v w=s)(-1)^omega(w) T(r u w)T(r v w).

The sign of each prefactor after substituting T is mu(s); its denominator
is r^2 s w. This proves (2.2). Terms with a mask above Y vanish by the
stated convention. Bound each m_d by (2.1); assigning each p|s to u,v,w
gives local total 2+1/p, proving (2.3).

For (2.4) let a(q) be the square of the bound in (2.3), with a(q)=0 on
non-cubefree q. Thus a(p)=(2+1/p)^2 and a(p^2)=1. Pointwise,

    a(q)<=d_4(q) product_(p|q)(1+h(p)),
    h(p)=1/p+1/(4p^2).

Expand the product as a nonnegative squarefree divisor sum and use
d_4(ab)<=d_4(a)d_4(b) and sum_(n<=x)d_4(n)<=x(1+log x)^3. The result is

    sum_(q<=Q)a(q)
       <=Q(1+log Q)^3 product_p(1+4/p^2+1/p^3).

The logarithm of this Euler product is at most
4 sum_(n>=2)n^-2+sum_(n>=2)n^-3<=13/4. Since log 2>2/3,
exp(13/4)<32. This proves (2.4), including its full infinite prime tail.

The proof also gives the stronger finite bound 32 Q H_floor(Q)^3.
Equation (2.2) is specific to the COMPLETE products in (1.1). A product
cutoff inside that sum destroys its rectangular factorization; (2.2)--(2.4)
are not silently asserted for those differently truncated coefficients.

## 3. Exact centered modes, including all above-output products

For 0<theta<1 define the classical centered harmonic tail

    Z_theta(k)=sum_(n<=k)e(n theta)/n+log(1-e(theta))
              =-sum_(n>k)e(n theta)/n, e(t)=exp(2pi i t).

The logarithm is its radial Abel value. The second series converges by
Dirichlet's test. Conjugate fractions are paired, so all sums below are real.
The cyclotomic identity product_(a mod q, (a,q)=1)(1-e(a/q))=Phi_q(1)
shows that sum_a Z_(a/q)(k)=S_q(k); Phi_q(1)=p for a prime power q=p^a
and is 1 otherwise. The same identity follows by logarithmic Möbius
inversion of product_(a=1)^(d-1)(1-e(a/d))=d.

Finite Fourier inversion of 1_(d|n), followed by grouping reduced fractions,
gives for every positive integer k

    sum_(d<=Y^2) z_Y(d)R(k/d)/d
       =M_Y^2 R(k)+sum_(q=2)^(Y^2) C_Y(q)S_q(k).        (3.1)

Indeed sum_d z_Y(d)/d=M_Y^2, while the total centering is

    sum_(q>=2) C_Y(q)Lambda(q)
       =sum_d z_Y(d)log(d)/d=2M_Y L_Y.                 (3.2)

No d>k is deleted: its R(k/d) is -log(k/d)-gamma, and its reduced modes
are necessary for (3.1). The finite inverse identity is

    mu-(2g_Y-1*g_Y*g_Y)=mu*(delta-1*g_Y)*(delta-1*g_Y).

The last two factors vanish below b. Thus the Newton coefficients equal
mu(n) for EVERY n<b^2, and weighted summation gives

    m(k)=2M_Y-sum_d z_Y(d)H_floor(k/d)/d
        =A_Y(k)-M_Y^2 R(k)-sum_(q>=2)C_Y(q)S_q(k),
                                         b<=k<b^2.    (3.3)

At b^2 the first possible coefficient defect is mu(b)^2. The strict
endpoint cannot be enlarged by one in general. These source identities
are inherited from #905/#988 and are reproduced to fix the present source.

There is also a purely real finite formula useful for checking (3.1):

    S_q(x)=sum_(d|q)mu(q/d)R(x/d), q>=2.                (3.4)

It follows from c_q(n)=sum_(d|(q,n))d mu(q/d),
sum_(d|q)mu(q/d)=0, and sum_(d|q)mu(q/d)log d=Lambda(q).
The log x and gamma coefficients cancel EXACTLY in (3.4), which explains
why S_q is constant on complete integer cells.

## 4. Bound the entire small-denominator sector

**Lemma 3.** For integers 1<=Q<=K, uniformly in Y,

    sum_(K<=k<2K) |sum_(2<=q<=Q)C_Y(q)S_q(k)|^2
       <=64(1+log Q)^4 (Q/K+Q^3/K^2).                  (4.1)

The same bound applies after restricting to any subset of those output
cells. All same-frequency coincidences and all cross-denominator terms
remain in the sum before the norm.

First, an exact Abel expansion gives

    Z_theta(k)= e(k theta)/[(k+1)(1-e(-theta))]+E_theta(k),
    |E_theta(k)|<=2/[k^2 |1-e(theta)|^2].               (4.2)

To check the index, apply (1-r) to sum_(n>=k+1)r^n/n, |r|=1,r!=1.
The result is r^(k+1)/(k+1)-sum_(n>=k+2)r^n/[n(n-1)]. Summation by
parts bounds the latter by 2/[(k+1)(k+2)|1-r|]. This proves (4.2).

Write L=1+log Q and

    P(k)=sum_(q=2)^Q C_Y(q)
                     sum_(a mod q)^* e(ak/q)/(1-e(-a/q)).

The squared mass of its DISTINCT reduced-frequency coefficients is at most

    (1/4)sum_(q<=Q)q^2|C_Y(q)|^2<=8 Q L^3,             (4.3)

using |1-e(a/q)|>=4 min(a,q-a)/q and
sum_(a mod q)^* |1-e(a/q)|^-2<=q^2/4.

Distinct reduced fractions with denominators <=Q have circular spacing at
least Q^-2. Geometric summation bounds an off-diagonal Gram entry by
min(K,1/(2||theta-theta'||)). Ordering the fractions on both semicircles
from one chosen fraction and summing reciprocals gives the absolute row
bound K+2Q^2 L. Schur's inequality and (4.3) imply

    sum_(K<=k<2K)|P(k)/(k+1)|^2
       <=8 Q L^3/K+16 Q^3 L^4/K^2.                    (4.4)

The remainder after summing (4.2) has pointwise modulus at most

    (1/(2K^2))sum_(q<=Q)q^2|C_Y(q)|
       <=sqrt(8) Q^2 L^(3/2)/K^2,                     (4.5)

by Cauchy, (2.4), and sum_(q<=Q)q^2<=Q^3. Its squared norm on the K
cells is therefore <=8 Q^4 L^3/K^3. Applying (u+v)^2<=2u^2+2v^2 to
(4.4)--(4.5), and Q<=K, proves (4.1) with the displayed slack.

Apply (4.1) on each I_j with Q=Q_j. Since rho>1/2,
Q_j/X_j and Q_j^3/X_j^2 are both <=X_j^(-alpha).
Also 1+log X_j<=2(1+log b). Summing the complete dyadic geometric series
gives (1.4). A shortened final annulus is paid by its full positive dyadic
bound. The output never passes the strict endpoint b^2.

## 5. Both balance coordinates are automatically harmless at native crossings

Let

    Xcal={Y>=2: mu(Y)!=0 and m(Y-1)m(Y)<=0}.             (5.1)

These are the literal native reciprocal sign crossings, not a new source.
At each one, |M_Y|<=1/Y. The set is unbounded by the classical Landau
argument reproduced at the end of this section. No quantitative gap bound
between crossings is used or proved.

**Lemma 4.** For every Y>=1,

    B_Y=(gamma/2)M_Y+sum_(n<=Y)mu(n)R(Y/n)/n,
    |B_Y|<=1+(gamma/2)|M_Y|.                            (5.2)

Moreover B_Y tends to zero as Y tends to infinity, using only the ordinary
prime number theorem, not RH.

For the identity, finite divisor inversion gives

    1=sum_(n<=Y)mu(n)H_floor(Y/n)/n
      =(log Y+gamma)M_Y-L_Y+sum_(n<=Y)mu(n)R(Y/n)/n.

Rearrange to obtain (5.2). The elementary Euler remainder formula

    R(t)=psi(t)/t-integral_t^infinity psi(u)du/u^2,
    psi(t)=1/2-{t},

gives |R(t)|<=1/t for t>=1, including the right-hand value at integers.
It follows either by intervalwise integration by parts or by telescoping
the harmonic sums and their limiting constant. Thus the remainder sum
in (5.2) has absolute value <=Y^-1 sum_(n<=Y)|mu(n)|<=1.

For the limit, the classical PNT consequence m(x)=o(1) implies M(x)=o(x)
by partial summation. Fix 0<eta<1. The terms n<=eta Y in that remainder
sum have total absolute value <=eta. On eta Y<n<=Y it equals
Y^-1 sum mu(n) f(n/Y), with f(u)=R(1/u)/u. For fixed eta, this f has
bounded variation on [eta,1], including its finitely many jumps at 1/j.
Abel summation and M(x)=o(x) show that this part tends to zero. Take the
limsup and then eta down to zero. This proves B_Y=o(1), including all
small-n and large-n contributions. No convergence of an unbounded weighted
integral of m is assumed.

For the complete strict square-step balance vector one has, for Y>=2,

    ||A_Y||_2 <=sqrt(6)Y|M_Y B_Y|+sqrt(3)Y M_Y^2.       (5.3)

The first term uses b^2-b=Y^2+Y<=3Y^2/2. For the logarithmic term,

    sum_(k=b)^(b^2-1) log^2(Y^2/k)<=2Y^2+8/Y<=3Y^2.

Below Y^2, compare the decreasing positive summand with the integral from
Y to Y^2, and then extend that integral to (0,Y^2), where it equals 2Y^2.
Above Y^2 use log(k/Y^2)<=2/Y on its 2Y cells. Also

    ||M_Y^2 R||_2<=M_Y^2/sqrt(Y).                       (5.4)

Combining (1.4), (5.3) and (5.4) gives an all-Y, explicit root-norm error

    ||m-V_(Y,rho)||_2
       <=sqrt(E_(Y,rho))+sqrt(6)Y|M_YB_Y|
                       +sqrt(3)Y M_Y^2+M_Y^2/sqrt(Y). (5.5)

In particular on Xcal it is at most

    eta_Y=sqrt(E_(Y,rho))+sqrt(6)|B_Y|
                                  +sqrt(3)/Y+Y^(-5/2),
    eta_Y ->0.                                         (5.6)

Even without the PNT limit, (5.2)--(5.3) give ||A_Y||_2<4 at every crossing.
The stronger vanishing assertion in (5.6) pays the classical PNT input.

**Theorem 2 (nuisance-free complete amplitude on cofinal native cuts).**
For every fixed rho in (1/2,2/3), along the unbounded set Xcal,

    |sqrt(F_(b^2-1)-F_Y)-||V_(Y,rho)||_2|<=eta_Y ->0.    (5.7)

The same comparison holds after ANY orthogonal block-constant projection
of the complete square-step cells. Norms, rather than squared energies,
are compared: no mixed term with the large-denominator amplitude is erased.
For example the energy version costs
(1+epsilon)||V||^2+(1+epsilon^-1)eta_Y^2.

### Why Xcal is cofinal, without a crossing-spacing assumption

For Re z>0, partial summation gives

    integral_1^infinity m(x)x^(-z-1)dx=1/[z zeta(z+1)].

The right side is analytic at every real z>-1: its value at zero is
removable, the Euler product handles z>0, and the alternating eta series
gives zeta(z+1)<0 on -1<z<0. It has a genuine nonreal pole at rho-1 for
any nontrivial zeta zero rho; classical existence of such zeros suffices.
If m were eventually of one sign, change that sign if needed and remove
an initial compact interval. In log coordinates one obtains a nonnegative
Laplace density. Its finite convergence abscissa must be a REAL singularity
by Landau's elementary positivity argument: a Taylor expansion about a point
just to its right, evaluated to its left, has nonnegative integral terms,
so analyticity across the abscissa would force convergence farther left by
monotone convergence. This contradicts the definition of the abscissa.
The analytic real interval forces that abscissa to be <=-1, or minus
infinity, in which case the nonreal pole in Re z>-1 is impossible. Thus
m has both signs arbitrarily far out. Passing between them supplies the
weak crossings in (5.1). This is the argument of #848, reproduced with
the same quantifiers, not a new crossing-density theorem.

## 6. Pay every square denominator and a growing small-core sector

For cubefree q write q=r^2 s as in Lemma 2, and call s its squarefree
core. Put

    a(s)=product_(p|s)(2+1/p),
    beta(n)=product_(p|n)(1+p^(-1/2)), H_n=sum_(j<=n)1/j.

Denominators with a prime cube have coefficient zero. We keep q=1
outside this section; its M_Y^2 R mode has already been paid in Section 5.
All norms in this section are the full L2(0,infinity;dx) norm, unless
restricted explicitly. The coherent sums include EVERY denominator in the
stated sector, even those greater than the output and greater than Y.

**Theorem 3 (complete square and small-core sector).** Let omega_q(x)
be arbitrary measurable multipliers with |omega_q(x)|<=1. Uniformly in
Y>=2,

    ||sum_(2<=r<=Y, r squarefree)
             omega_(r^2)(x) C_Y(r^2) S_(r^2)(x)||_2
                  <=3 sqrt(3) H_Y.                    (6.1)

For every integer S>=1, uniformly in the same multipliers,

    ||sum_(2<=q<=Y^2, q cubefree, core(q)<=S)
                    omega_q(x) C_Y(q) S_q(x)||_2
                  <=12 H_Y sqrt(S) H_S^3.             (6.2)

Thus the complete squared norms are at most 27 H_Y^2 and
144 S H_Y^2 H_S^6, respectively. These are full amplitude bounds, not
sums of diagonal energies. No sign cancellation between different q is
assumed; the actual native masked sums pay their small coefficients.

First, |R(x)|<=1/x for x>=1. For 0<x<1, R(x)=-log x-gamma. Since
0<gamma<1,

    integral_0^infinity R(x)^2 dx
       <=(2-2gamma+gamma^2)+1<=3.                     (6.3)

Dilation in (3.4) and the triangle inequality give

    ||S_q||_2<=sqrt(3) sum_(d|q, mu(q/d)!=0) sqrt(d)
              =sqrt(3q) beta(q).                      (6.4)

Multiplication by omega_q contracts this norm. Lemma 2 gives the exact
special identity

    C_Y(r^2)=m_r(Y/r)^2/r^2>=0                         (6.5)

for squarefree r, hence |C_Y(r^2)|<=r^-2. Also

    sum_(r<=Y, r squarefree) beta(r)/r
      <=sum_(e<=Y, e squarefree) e^(-3/2) H_floor(Y/e)
      <=zeta(3/2)H_Y<=3H_Y.                           (6.6)

Indeed expand beta(r)=sum_(e|r)e^(-1/2) on squarefree r and discard the
remaining coprimality and squarefree conditions; all terms are positive.
The last constant follows from 1+integral_1^infinity t^(-3/2)dt=3.
Equations (6.4)--(6.6) and the L2 triangle inequality prove (6.1).
Including r=1 in the positive numerical upper bound does not insert a
q=1 mode into the amplitude.

For q=r^2 s, (2.3) and (6.4) instead give

    ||omega_q C_Y(q)S_q||_2
          <=sqrt(3) a(s) beta(s) beta(r)/(r sqrt(s)).  (6.7)

Here r,s are squarefree and coprime. Sum over r<=Y/sqrt(s), discard
coprimality, and apply (6.6); the result is bounded by
3sqrt(3)H_Y sum_(s<=S,s squarefree) a(s)beta(s)/sqrt(s).
For a prime p>=3,

    (2+1/p)(1+p^(-1/2))<=(7/3)(5/3)=35/9<4.

For p=2 the same expression is less than 9/2. Since a squarefree s has
at most one factor 2,

    a(s)beta(s)<=(9/8)d_4(s).

The elementary divisor bound sum_(s<=t)d_4(s)<=t H_floor(t)^3 and partial
summation give, for integer S>=1,

    sum_(s<=S)d_4(s)/sqrt(s)<=2sqrt(S)H_S^3.

Consequently the previous norm is at most
(27sqrt(3)/4)H_Y sqrt(S)H_S^3<12H_Y sqrt(S)H_S^3, which proves (6.2).
Every infinite tail in these estimates was paid by an explicit convergent
series or integral. No mean-value theorem for reciprocal Möbius twists is
being imported.

### Remove the paid sector coherently on the actual output annuli

For an integer S>=1 define, on k in I_j,

    Vrough_(Y,rho,S)(k)
       =-sum_(q>Q_j, q cubefree, core(q)>S) C_Y(q)S_q(k). (6.8)

Take omega_q(x) equal to the indicator of the union of precisely those
annuli I_j for which q>Q_j. These are measurable multipliers bounded by
one, even though their thresholds vary by annulus. Because all annular
endpoints are integers and each S_q is constant on every integer cell,
(6.2) implies

    ||V_(Y,rho)-Vrough_(Y,rho,S)||_l2(b,...,N)
                           <=12 H_Y sqrt(S) H_S^3.    (6.9)

There is no factor for the number of annuli: the theorem already bounds
the whole masked function in a single norm. When S=1 replace the right
side by 3sqrt(3)H_Y using (6.1). In particular at the native crossings,

    |sqrt(F_(b^2-1)-F_Y)-||Vrough_(Y,rho,S)||_2|
                <=eta_Y+12 H_Y sqrt(S) H_S^3.          (6.10)

The low-denominator, balance, square/core, and retained rough-core sectors
were combined by a ROOT-NORM inequality. Their cross terms have not been
deleted. The error in (6.10) is no longer claimed to vanish. For any fixed
integer-valued schedule S=S(Y)>=1 with log S=o(log Y), its squared size
is Y^o(1). The removed sector can therefore include squarefree cores
tending to infinity as any chosen power of log Y, or more generally at
any subpower rate. The large-denominator sector with a growing large
squarefree core remains to be bounded.

## 7. Exact multiplicative-frequency realization, with no cell interpolation

The retained amplitude has a useful expression in terms of the literal
old-prefix Dirichlet polynomial

    G_Y(s)=sum_(n<=Y)mu(n)n^-s.

For complex w define the Jordan polynomial

    J_w(q)=sum_(d|q)mu(q/d)d^w
          =q^w product_(p|q)(1-p^-w).

Put

    D_(Y,Q)(s)=sum_(Q<q<=Y^2) C_Y(q)J_(1-s)(q)
             =G_Y(s)^2-sum_(q<=Q) C_Y(q)J_(1-s)(q).     (7.1)

The equality follows by interchanging finite sums and using
sum_(q|d)J_(1-s)(q)=d^(1-s). It is an exact native signed polynomial,
not a substitution of G_Y by 1/zeta or an independent coefficient family.
In particular every original product d<=Q has zero contribution to (7.1).

For -1<Re z<0, the complete classical Mellin integral is

    integral_0^infinity R(x)x^(-z-1)dx=zeta(1+z)/z.     (7.2)

For Re z>0, harmonic summation on [1,infinity) gives
integral_1^infinity R(x)x^(-z-1)dx
=zeta(1+z)/z-1/z^2-gamma/z. The integral extends holomorphically to
Re z>-1 using |R(x)|<=1/x. On -1<Re z<0 the integral over (0,1) is
1/z^2+gamma/z, proving (7.2), including the two canceled terms.

Let f(u)=exp(u/2)R(exp u), with Fourier convention
fhat(t)=integral_R f(u)exp(-itu)du. Its exponential tails, with a linear
factor at minus infinity, put it in BOTH L1 and L2. Thus

    fhat(t)=zeta(1/2+it)/(-1/2+it).                     (7.3)

By (3.4), the Fourier transform of
exp(u/2) sum_(q>Q) C_Y(q)S_q(exp u) is exactly

    fhat(t)D_(Y,Q)(1/2+it).                            (7.4)

All operations up to this point involve finite sums of L2 translations.
Inversion and the infinite frequency norms are interpreted in L2; no
unproved absolute integrability in t is required.

For the annulus I_j put chi_j(u)=1_[log X_j,log U_j)(u). Its transform is

    chihat_j(t)=(X_j^(-it)-U_j^(-it))/(it),
    chihat_j(0)=log(U_j/X_j).

The transform of the actual retained amplitude on that annulus is

    W_j(t)=-(1/(2pi))integral_R chihat_j(t-v)
       zeta(1/2+iv)/(-1/2+iv) D_(Y,Q_j)(1/2+iv)dv.      (7.5)

For each t this integral is absolutely defined by L2 Cauchy--Schwarz.
It is the Fourier transform of the physical product chi_j times (7.4)'s
inverse transform, and belongs to L2. Multiplication by the annular window
has NOT been replaced by a sharp Mellin-frequency cutoff.

Since S_q(exp u) is constant on each integer cell, Plancherel gives EXACTLY

    ||V_(Y,rho)||_l2(b,...,N)^2
                     =(1/(2pi))sum_j integral_R |W_j(t)|^2dt. (7.6)

There is no integer-to-continuum error. The sum over j is a partition of the
same complete physical output, not an average over sources or arithmetic
characters. Every real frequency, every annulus, every Jordan term and its
centering are retained. Equations (5.7) and (7.6) give a quantitative
comparison between the native energy and a single specified signed
multiplicative-frequency object, with no remaining balance estimate at
the cofinal native crossings.

As a useful check on normalization, omitting BOTH masks and windows gives

    integral_0^infinity |sum_d z_Y(d)R(x/d)/d|^2 dx
       =(1/(2pi))integral_R
         |zeta(1/2+it)G_Y(1/2+it)^2/(-1/2+it)|^2dt.    (7.7)

This identity is valid for the uncompleted prefix because R itself has
both Mellin subtractions. It does not identify its output outside the
strict square step with native m, and (7.7) is not used to enlarge the
actual target (7.6).

For the stronger reduction of Section 6, define the exact rough-core
polynomial

    Drough_(Y,Q,S)(s)
       =sum_(q>Q, q cubefree, core(q)>S) C_Y(q)J_(1-s)(q). (7.8)

Replace D_(Y,Q_j) by Drough_(Y,Q_j,S) in (7.5), and call the result
Wrough_j. The identical argument gives

    ||Vrough_(Y,rho,S)||_2^2
             =(1/(2pi))sum_j integral_R |Wrough_j(t)|^2dt. (7.9)

Thus the square/core removal is performed inside each annulus's exact
finite polynomial, before taking its signed frequency amplitude and norm.
It is not an independent diagonal subtraction from (7.6). All cross terms
among the remaining modes and all physical window convolutions remain.

## 8. What remains, and the correct sparse-cutoff consumer

The new upper estimate is (4.1), for the COMPLETE small-denominator sector.
The new upper estimates (6.1)--(6.2) also pay every square denominator and
the full small-core sector, even at the largest denominator scales. None
of these estimates bounds the remaining large-denominator, large-core
norm with a subquadratic power of F_Y. The masked factorization does not
give the missing arithmetic cancellation estimate. There is no RH proof.

For orientation, #848 at its exact recorded source proves

    log(1+F_Y)/log(Y+1) -> kappa=2Theta-1,

where Theta is the supremum of the nontrivial-zero real parts. Its lower
bound holds at EVERY prefix; its upper bound is the generalized Littlewood
implication, with Theta=1 separately included. This source-qualified
consumer, not a claim about crossing gaps, says the following. Fix rho in
(1/2,2/3) and any integer-valued schedule S(Y)>=1 with log S=o(log Y).
An unbounded sequence of estimates

    ||Vrough_(Y,rho,S(Y))||_2^2
                  <=Y^o(1)(1+F_Y)^(2-delta),
    Y in Xcal, some fixed 0<delta<1,                     (OPEN)

would imply RH. Indeed (6.10), with the root-norm cross terms paid by
(a+b)^2<=2a^2+2b^2, gives

    F_(b^2-1)<=F_Y+Y^o(1)(1+F_Y)^(2-delta)+Y^o(1).

If kappa>0, the two sides have incompatible logarithmic exponents 2kappa
and at most (2-delta)kappa. The subpower square/core error contributes
exponent zero. The same statement follows from (5.7) with V in place of
Vrough, but (7.8)--(7.9) specify the smaller signed object now left open.
No interpolation across omitted scales occurs. The premise (OPEN) remains
unproved, and #848's infinite analytic arguments are a separate source
dependency from the finite checker here.

The completed work removes the balance issue on those cofinal native cuts,
replaces the product cutoff by a complete reduced-denominator cutoff, pays
its new full-product coefficients using literal native masked sums, and
pays every square denominator and a growing small-core sector in full
coherent norm, and gives an exact all-frequency realization of the
remaining object. It does not treat those reductions as the missing
signed large-denominator, large-core bound.
