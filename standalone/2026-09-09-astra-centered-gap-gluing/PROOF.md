# CGG26: a sharp centered bottleneck in the literal divisor graph

Date: 2026-09-09. Status: PROPOSED COMPLETE COMPONENT PROOFS; independent
mathematical review required. RH and the native coherent-work upper bound
remain UNPROVED. This is not a proposed full proof of RH.

The new result answers an explicit question left by #825, #826, #828 and #829:
can the centered divisor Poincare constant be bounded independently of the
prime alphabet on EVERY divisor-closed support? No. Two disjoint prime boxes,
joined at the actual integer 1, have a centered inverse gap of exact order
log log P. Each individual box has a uniform centered gap. Exactly one
additional slow direction is created by joining them. This is distinct from
the previously proved deterioration caused by GROUNDING a single box.

The individual-box spectral and root-capacity formulas are credited to the
parallel #828/#829 packets. Sections 2 and 5 reconstruct everything from those
formulas needed for the new all-scale result. Root gluing, variance decomposition
and min-max are classical methods; no general-method priority is claimed.

## 1. Original source, metric, and theorem

For a finite divisor-closed set S of positive integers, put

    ||f||_S^2 = sum_(n in S) |f(n)|^2/n,
    Z_S = sum_(n in S) 1/n,
    mean_S f = Z_S^(-1) sum_(n in S) f(n)/n,
    V_S(f) = ||f-mean_S f||_S^2,
    E_S(f) = sum_(p prime,k>=1,jp^k in S)
                 (log p)/(jp^k) |f(jp^k)-f(j)|^2.              (1.1)

Every allowed prime power is retained exactly once in E_S. The scalar centered
Poincare constant is C(S)=sup_(E_S(f)>0) V_S(f)/E_S(f). It is the inverse of
the first positive eigenvalue of this finite weighted graph, not an anchored
constant. The constant function is its only zero mode. All inequalities also
hold for complex Hilbert-valued f by summing scalar coordinates; each scalar
channel then becomes one copy of that Hilbert space.

For a finite nonempty prime alphabet A, let B(A) be all squarefree products of
primes in A, including 1. Define

    Z_A = product_(p in A)(1+1/p),
    nu_p = (1+1/p)log p,
    a_D = sum_(p in D)nu_p,   b_D = product_(p in D)1/p,
    G_A = sum_(empty != D subset A) b_D/a_D,
    H_A = sum_(empty != D subset A) b_D/a_D^2,
    g_A = min_(p in A) nu_p.                                  (1.2)

Now take DISJOINT alphabets A and B, and S=B(A) union B(B). Their intersection
is {1}; Z_S=Z_A+Z_B-1. This is an ordinary divisor-closed integer set. There
are no graph edges joining a nonroot A vertex to a nonroot B vertex: their
ratio cannot be an integer. Thus E_S=E_A+E_B in unnormalized harmonic metrics.
No edge of the prescribed support is dropped; no cross product is claimed to
belong to S. All vertices are squarefree, so no higher-power edge is allowed.

**CGG1 (quantitative centered gluing).** Put g=min(g_A,g_B). Then

    (Z_B-1)G_A/(Z_A+Z_B-1) + H_A/G_A <= C(S),                (1.3)

and the same bound with A,B interchanged. Also

    C(S) <= 1/g + (Z_B G_A+Z_A G_B)/(Z_A+Z_B).                (1.4)

These are finite all-coefficient theorems, not asymptotic approximations.
In addition, the explicit contrast ell(f)=mean_A f-mean_B f satisfies

    V_S(f) <= E_S(f)/g
               + [Z_A Z_B/(Z_A+Z_B)] |ell(f)|^2.             (1.5)

Consequently the entire mean-zero, zero-contrast subspace has gap at least g.
If 0=lambda_0<lambda_1<=lambda_2<=... is the full scalar spectrum, then

    lambda_2 >= g.                                         (1.6)

Repeated eigenvalues are included. No diagonalization is necessary to identify
the two explicit linear constraints (mean_S f=0 and ell(f)=0).

**CGG2 (sharp all-scale centered loss).** Fix an integer r>=1. For each real
y>=2 let A_y be all primes <=y. Let P_r(y) be the FIRST prime P>y for which

    product_(y<p<=P)(1+1/p) >= r Z_(A_y),                   (1.7)

and let B_y contain precisely these primes y<p<=P_r(y). Let
S_(y,r)=B(A_y) union B(B_y). The cutoff exists and is prescribed without zeros,
randomness, or optimizing the graph. Then

    log P_r(y) is comparable to (log y)^2,
    log log P_r(y) = 2 log log y+O_r(1),                    (1.8)

and the complete centered inverse gap obeys

    C(S_(y,r)) = [r/((1+r)zeta(2))] log log y+O_r(1)
               = [3r/((1+r)pi^2)] log log P_r(y)+O_r(1).    (1.9)

In particular, for r=1,

    lambda_1(S_(y,1)) ~ 2pi^2/[3 log log P_1(y)],
    lambda_2(S_(y,1)) >= (3/2)log 2.                        (1.10)

Thus the O(1+log log P) centered cost proved for all divisor-closed supports
in #825 has the correct ORDER on that class. Its numerical constant is not
shown optimal. There is no absolute centered gap on the whole class. This
result does NOT decide a constant gap for the special intervals {1,...,N}.
It does not retract the constant centered gaps on individual prime boxes.

## 2. Complete one-box reconstruction and an explicit trial vector

Under the probability weight 1/(Z_A n), a prime p is present with probability
1/(p+1). Its coordinate eigenfunction has values -1/sqrt(p) when absent and
sqrt(p) when present. Its eigenvalue is nu_p. This follows by substitution in
the two-state generator with birth rate (log p)/p and death rate log p.
Products chi_D of the coordinate functions are a complete orthonormal basis,
with eigenvalue a_D and |chi_D(1)|^2=b_D. The centered gap is g_A.

For mean-zero f, Cauchy--Schwarz in this basis gives

    |f(1)|^2 <= G_A E_A(f)/Z_A.                             (2.1)

Equality is attained by the root Green vector

    k_A(n)=sum_(D nonempty) chi_D(1)chi_D(n)/a_D.             (2.2)

This vector has mean zero, root value G_A, probability squared norm H_A, and
probability energy G_A. The rational-factor version of its numerator is

    chi_D(1)chi_D(n)
      =product_(p in D) [ -1 if p divides n, 1/p otherwise]. (2.3)

Hence the vector

    F_A(n)=1-k_A(n)/G_A                                    (2.4)

has root zero, mean one, probability variance H_A/G_A^2 and probability
energy 1/G_A. Extend it by zero throughout B(B). It is a well-defined function
on S because both root values are zero. Subtracting its global mean, if desired,
does not change its energy or centered variance. Its exact Rayleigh quotient is

    H_A/G_A + [(Z_B-1)/(Z_A+Z_B-1)]G_A.                     (2.5)

Indeed its global squared norm is Z_A(1+H_A/G_A^2), its weighted sum is Z_A,
and its energy is Z_A/G_A. This proves (1.3), with ALL vertices of the B box
contributing their exact mass to the centering even though its initial values
are zero. Formula (2.5) is not the anchored quotient of the A box.

The matrix formulation in Euclidean coordinates v_n=f(n)/sqrt(n) has the
original null vector (1/sqrt(n)). No Euclidean/harmonic norm is substituted.

## 3. Exact variance identity, upper bound, and the one slow channel

Subtract the common root value from f; this changes neither variance nor
energy. Write a=mean_A f and b=mean_B f after that subtraction, so f(1)=0.
Let V_A,V_B denote UNNORMALIZED within-box centered variances. Then exactly

    V_S(f)=V_A+V_B
       +[Z_A Z_B/(Z_A+Z_B)] |a-b|^2
       -|Z_A a+Z_B b|^2/[(Z_A+Z_B-1)(Z_A+Z_B)].             (3.1)

To verify, use sum_S |f|^2/n=V_A+Z_A|a|^2+V_B+Z_B|b|^2,
sum_S f/n=Z_Aa+Z_Bb, and Z_S=Z_A+Z_B-1. The shared root has weight ONE,
not zero and not two. The final term in (3.1) is nonpositive.

The individual centered inequalities give V_A+V_B<=E_S/g, proving (1.5).
The root contrast inequalities (2.1), applied to f-a and f-b, give

    |a|^2 <= G_A E_A/Z_A,   |b|^2 <= G_B E_B/Z_B.

Another Cauchy--Schwarz inequality gives

    |a-b|^2 <= (G_A/Z_A+G_B/Z_B)(E_A+E_B).                 (3.2)

Combining with (3.1) proves (1.4). This bound does NOT pretend the two boxes
are independent after they share a root; the exact correction is in (3.1).

For (1.6), the constraints mean_S f=0 and ell(f)=0 are two independent linear
constraints when both alphabets are nonempty. On their common kernel, (1.5)
gives ||f||_S^2<=E_S/g. Min-max implies that at most two eigenvalues, counting
the zero eigenvalue, lie below g. Equivalently lambda_2>=g.

The contrast has explicit mean-zero Riesz vector

    r_S(n)=1_(n in B(A))/Z_A-1_(n in B(B))/Z_B.              (3.3)

Thus the orthogonal complement of span{1,r_S} has the rank-independent floor
g, at EVERY finite pair of boxes. These are two known vectors, not a guessed
collection of low eigenvectors. The full inverse still contains the slowly
varying scalar channel; discarding it changes the problem. For large y in
CGG2 there is exactly one positive eigenvalue below g, because (1.9) implies
lambda_1->0 and (1.6) excludes any second one.

## 4. Elementary Euler mass estimates and the prescribed second alphabet

We reconstruct enough arithmetic for (1.8). Put

    Z(x)=product_(p<=x)(1+1/p),
    Z_geom(x)=product_(p<=x)(1-1/p)^(-1).

Both finite products include the complete allowed exponent sum in the latter.
Elementary central-binomial valuations followed by dyadic summation give
psi(x)=sum_(p^k<=x)log p <=C x. The exact factorial identity

    sum_(d<=x)Lambda(d)floor(x/d)=log(floor(x)!)

gives sum_(d<=x)Lambda(d)/d<=log x+C. Therefore

    B(x)=sum_(p<=x)log p/(p-1)<=log x+C'

because sum_(n>=2)log n/[n(n-1)] converges. Normalize the harmonic mass of
x-smooth integers to a probability distribution. Its mean logarithm is B(x).
Markov puts at least half its mass below exp(2B(x)). The harmonic-sum bound
then gives Z_geom(x)<=2+4B(x)<=C''log x for x>=2. Thus Z(x)<=C''log x.

For the lower bound, the finite divisor identity mu(n)^2=sum_(d^2|n)mu(d)
and absolute convergence at s=2 give

    sum_(n<=x)mu(n)^2=x/zeta(2)+O(sqrt(x)),
    sum_(n<=x)mu(n)^2/n=(log x)/zeta(2)+O(1).                (4.1)

All squarefree n<=x occur in the prime box, so Z(x) is at least the second
sum. Consequently there exist absolute c,C>0 with

    c log x <= Z(x) <= C log x, x>=2,                     (4.2)

after adjusting c on a fixed initial interval. In particular Z(x)->infinity.
This also proves existence of the first prime in (1.7), without PNT, Bertrand's
postulate, a prime-location algorithm bound or a zero theorem.

At the first crossing P=P_r(y), the preceding product is smaller than r Z_A.
Therefore EXACTLY

    r Z_A <= Z_B < r Z_A(1+1/P).                           (4.3)

In particular Z_B/Z_A=r+O_r(1/y). Since A_y and B_y together are exactly the
primes through P, their masses multiply: Z(P)=Z_A Z_B. Equations (4.2)-(4.3)
then give log P comparable, with r-dependent constants, to (log y)^2. Taking
one more logarithm proves (1.8). Cardinality of the resulting box can be huge;
(1.7) defines a finite support, not a fast full-state enumeration.

## 5. The root capacity asymptotic, reconstructed and credited

For A_y consisting of all primes <=y, the exact root spectral formula yields

    G_(A_y)=integral_0^infinity
       [product_(p<=y)(1+p^-1 exp(-nu_p t))-1]dt.           (5.1)

This formula and the following asymptotic are the previously supplied common
#828/#829 component, not a new claim of this packet:

    G_(A_y)=(1/zeta(2))log log y+O(1).                      (5.2)

Here is a self-contained proof of what is used. For squarefree n, write
 a(n)=log n+b(n), b(n)=sum_(p|n)(log p)/p.
Splitting the latter sum at log n and using the factorial estimate in Section 4
shows b(n)<=log log n+O(1). The summed difference between 1/[n a(n)] and
1/[n log n] is absolutely bounded, since
sum_(n>=3)(1+log log n)/[n(log n)^2] converges. All squarefree n<=y occur in
the defining sum for G. Partial summation of (4.1) gives the lower bound
G_(A_y)>=(1/zeta(2))log log y-O(1).

For the upper bound put F_y(t)=product_(p<=y)(1+p^-1 exp(-nu_p t)). Since
nu_p>=log p, positive absolute Euler products give

    1<=F_y(t)<=zeta(1+t)/zeta(2+2t), t>0.

Also F_y(t)<=Z(y)<=C log(y+1). Near t=0 the Euler comparison/integral test
zeta(1+t)=1/t+O(1) and the convergent derivative near 2 give
zeta(1+t)/zeta(2+2t)=1/[zeta(2)t]+O(1). Beyond t=1 its difference from 1
is O(2^-t). Integrate (5.1) separately over [0,1/log(y+1)],
[1/log(y+1),1], and [1,infinity). The first and last intervals have bounded
contribution and the middle interval supplies the upper side of (5.2).
No use of zeta off its real absolute-convergence interval is made.

For the B_y box every nonconstant eigenvalue is at least log y, and its
nonconstant root weights sum to Z_B-1. Thus the elementary finite bound

    G_(B_y) <= (Z_B-1)/log y                               (5.3)

is sufficient; no asymptotic for this second capacity is required.

## 6. Proof of the sharp CENTERED asymptotic

Use the weaker positive part of (1.3), then (4.3):

    C(S_(y,r)) >= [(Z_B-1)/(Z_A+Z_B-1)] G_A
                  = [r/(1+r)]G_A+O_r(G_A/Z_A+G_A/y).      (6.1)

The error tends to zero because Z_A is comparable to log y and G_A is
O(log log y). For the upper bound, g=g_A=(3/2)log2 and (1.4) gives

    C(S_(y,r)) <= 1/g
             +[Z_B/(Z_A+Z_B)]G_A
             +[Z_A/(Z_A+Z_B)]G_B.

The last term is at most Z_A/log y=O(1) by (5.3), and the middle coefficient
is r/(1+r)+O_r(1/y). Hence

    C(S_(y,r))=[r/(1+r)]G_A+O_r(1).                        (6.2)

Insert (5.2) and then (1.8) to obtain (1.9). Inverting a positive quantity
tending to infinity proves (1.10). For every fixed r this is an all-y
asymptotic, not a fitted finite spectrum. In particular no absolute centered
constant works for all divisor-closed sets, even if restricted to squarefree
sets and to the full literal graph on their supports.

The published #825 upper bound applies to these supports and to all other
finite divisor-closed supports with largest prime at most P:
 C(S)<=48[1+log(16log P)].
Together with (1.9) it establishes the sharp ORDER of that general centered
inequality. We do not independently re-prove the all-support upper theorem
here; this comparison explicitly imports that source-qualified component.
Neither the constant 48 nor the leading coefficient of the worst all-support
constant is determined optimally in this packet.

**CGG3 (worst-case centered order at EVERY large prime budget).** Let C_sf^*(P)
be the maximum of C(S) over squarefree divisor-closed supports with primes at
most P; let C_all^*(P) be the supremum when arbitrary finite exponent depths
are allowed. Then

    C_sf^*(P) and C_all^*(P) are both Theta(log log P).       (6.3)

In fact, for every fixed integer r>=1,

    C_sf^*(P) >= [3r/((1+r)pi^2)] log log P-O_r(1),          (6.4)

and therefore liminf C_sf^*(P)/log log P >=3/pi^2. This is a lower bound on
the possible leading constant, not an identification of that constant.

To fill the prime-budget gaps, take c,C from (4.2) and choose a fixed a>0
so small that r C^2 a^2<c. Put y=exp(a sqrt(log P)). For sufficiently large
P, y<P and r Z(y)^2<=r C^2 a^2 log P<c log P<=Z(P). Thus the first-crossing
cutoff P_r(y) is at most P. Apply (1.9) at this y and use
log log y=(1/2)log log P+log a. This proves (6.4). The #825 upper bound proves
(6.3). No assumption about gaps between consecutive actual primes is needed.

## 7. Exact finite certificates without enumerating the large second box

An entirely elementary first instance is A={2}, B={3,5},
S={1,2,3,5,15}. Set f(2)=3 and f=0 at the other four vertices. Then

    Z_S=21/10,  sum f(n)/n=3/2,
    V_S(f)=24/7,  E_S(f)=(9/2)log2,
    V_S(f)/E_S(f)=16/[21log2]>2/[3log2].                    (7.0)

Both individual box inverse gaps are at most 2/[3log2], but their actual
five-vertex union already exceeds that value. This is a centered quotient;
subtracting the global mean 5/7 leaves energy and variance unchanged.
The unbounded failure of an absolute constant follows from Section 6, not
from this fixed example.

A finite rational trial can replace the real optimizer in (2.4). For each
p in A choose a specified positive rational l_p, put

    a_D^0=sum_(p in D)(1+1/p) l_p,
    G0=sum_(D nonempty)b_D/a_D^0,
    H0=sum_(D nonempty)b_D/(a_D^0)^2,
    K0(n)=sum_(D nonempty) product_(p in D)
                         [-1 if p|n,1/p otherwise]/a_D^0,
    F0(n)=1-K0(n)/G0 on B(A), and 0 on B(B).

This has EXACT root value zero and EXACT branch mean one. It is not claimed
to minimize the actual log-prime energy. Its probability variance in A is
H0/G0^2, while its actual probability energy is

    E0 = G0^(-2) sum_(D nonempty) b_D a_D/(a_D^0)^2.        (7.1)

The full centered Rayleigh quotient on S is exactly

    R0=[H0/G0^2+(Z_B-1)/(Z_A+Z_B-1)]/E0.                  (7.2)

Thus R0<=C(S). Only the A modes are enumerated. Every B vertex has F0=0;
its edges contribute exactly zero, but its full mass Z_B is included in the
global mean. The product representation is a proof of that compression,
not an empirical claim of complete large-state enumeration.

The checker uses the first-crossing alphabets for r=1 and y=2,3,5,7,11,13.
It freezes l_p to 32-bit dyadic lower approximations of log p, derives actual
log intervals from an 80-term reduced atanh sum with the full positive remainder,
and evaluates (7.1)-(7.2) with outward rational arithmetic. The largest alphabet
ends at 14549 and has 1698 B primes; its 2^1698 vertices are NOT enumerated.
All 63 nonconstant A modes at y=13 are included. The factorization identity,
root sharing, full mean and zero B energy certify the compressed calculation.

Small separate panels enumerate every vertex/edge, reconstruct the graph by
independent pair ratios, and check (3.1) and the product eigenbasis at exact
FORMAL rational rates. The latter are labeled algebra controls; they are not
certified actual logarithmic spectra. No asymptotic is inferred from the
six fixed Rayleigh quotients.

## 8. Exact boundary of the attempted RH composition

The user-facing objective was an unconditional full proof, not a graph-only
exercise. The current attempt did NOT produce it. The source-sensitive problem
in #829 remains the signed coherent work in

 J_N=sum_(k<N)M(k)^2/[k(k+1)]+M(N)^2/N
    =sum_(n<=N)mu(n)^2/n+2sum_(n<=N)mu(n)M(n-1)/n.

A subpower upper bound on an unbounded sequence would exclude any off-line
zeta zero by the source's exact-horizon Mellin detector. None of the gluing
inequalities proves that upper bound. In particular the field representing
J_N has a nonzero harmonic projection; the graph bounds complementary
fluctuations. A gap bound cannot be moved to a different metric or to the
annihilated coherent channel. The sharp Y/log Y norm-transfer loss in #803
also prohibits the coefficient-uniform shortcut tested in that branch.

CGG26 does settle a precise further question: even after global centering,
source support can create an unavoidable log-log inverse cost. Within the
constructed supports, it also supplies an explicit contrast whose removal
restores a constant gap. Future uses must retain or price that contrast.
The ordinary full interval supports, the unmodified signed Mobius estimate,
the full Weil form and J(A)=0 remain outside the new theorem.
