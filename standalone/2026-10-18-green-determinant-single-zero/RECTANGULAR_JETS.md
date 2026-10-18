# Independent jets, balanced quadratic grids, and a sharper real-zero gap

Status: **PROPOSED complete component proofs, awaiting independent mathematical
review.** No fixed complex zero-free half-plane or RH proof is asserted.
The argument is a modification of the supplied Green determinant construction.
Its rank, divisibility and height calculations are proved below, rather than
adopted on the authority of the printed attribution. The classical Mertens,
Chebyshev, quadratic-character and Hadamard-product facts are the only
analytic/arithmetic background inputs. No quasi-RH, zero-density, mollifier
moment, or already-proved no-Siegel-zero conclusion is a premise.

## 1. Result and comparison with the supplied note

Let chi be a primitive nonprincipal real Dirichlet character of conductor q.
Write K=Q(sqrt(d)) for its quadratic field, with d squarefree, nonsquare and
D=|d|<=q. There are absolute constants C_0 and R_0 such that, for all real
R>=max(q,R_0),

    A_chi(R):=sum_(p<=R,chi(p)=-1) log(p)/p
       <= (1/2)log R+(1/4)log q+C_0(1+log log(3R)).       (T1)

The same proof gives log D in place of log q. In particular, for every fixed
integer C>=1 and sufficiently large q,

    A_chi(q^C)/log(q^C) <= 1/2+1/(4C)+o_C(1).             (T2)

The supplied note obtains 3/4 at sufficiently large fixed C. At C=12, (T2)
has leading coefficient 25/48; the o(1) remains and is not set to zero.
These coefficients describe a PRIME SUM, not a zeta zero's real part.

A consequence of (T1) and the classical logarithmic derivative is: for every
real zero beta in (0,1) of such a character, as q tends to infinity,

    (1-beta)log q >= 1-O(log log q/log q),                 (T3)

with an absolute implied constant. This is an asymptotic near-one real-zero
statement. It is not a numerically explicit constant for all conductors, and
is weaker as a zero exclusion than an independently established fixed strip.
No worldwide novelty or best-known-bound claim is made.

The new choices are to separate the incidence parameter from the jet depth,
and to balance the two quadratic grid directions against the discriminant.
Ordinary derivatives, not factorial-divided Hasse derivatives, are essential.

## 2. A rank lemma with independent jet depth

Let n points (z_i,w_i) in C^2 have distinct w_i. Suppose each nonzero
polynomial F satisfies #{i:F(z_i,w_i)=0}<=M deg F. Let R,S,J be positive
integers. Form the RS rows

    v_(r,s)=(partial_z^j(z^r w^s)(z_i,w_i))_(i<=n,0<=j<J),
    0<=r<R, 0<=s<S.

**Lemma 1.** These rows are independent if

    Jn > M(R+S)+2RS+(J-M)_+ S.                           (1)

Here t_+=max(t,0). This is a sufficient bound, not an optimal rank formula.

Proof. A dependence gives a nonzero F of separate degrees <R,<S with every
listed derivative zero. Factor F=F_0(w) product_l F_l(z,w), where positive
z-degree irreducibles are listed with multiplicity. Put d_l=deg_z F_l>0,
e_l=deg_w F_l, and e_0=deg F_0. The sums of d_l and e_l are at most R and
S-e_0 respectively. A specialization F_l(z,w_i) cannot be identically zero:
otherwise w-w_i divides this irreducible with positive z-degree.

The nonzero resultant Res_z(F_l,partial_z F_l) has degree at most 2d_l e_l.
At a specialized root of multiplicity mu, its order at w_i is at least
mu-1. For completeness, the (2d_l-1)-square Sylvester matrix specializes to
a map whose image polynomials are divisible by (z-z_i)^(mu-1). Its rank
falls by at least mu-1. A constant invertible row change then produces that
many rows divisible by w-w_i, proving the resultant-order bound. This also
handles degree drops at specialization; no fixed leading coefficient is
assumed. Characteristic zero ensures that the resultant is not identically
zero. Incidence and distinct w_i therefore give

    sum_i ord_(z=z_i) F_l(z,w_i) <= M(d_l+e_l)+2d_l e_l.

Remove at most e_0 points at which F_0 vanishes. At each remaining point F
has z-multiplicity at least J, so

    J(n-e_0) <= M(R+S-e_0)+2RS.

Thus Jn<=M(R+S)+2RS+(J-M)e_0, which is at most the right side of (1).
Contradiction. All estimates are valid also when e_0=0 or when the list of
positive-degree factors is empty. QED.

The supplied Lemma 3.1 is recovered when J=M. Allowing J>M is the actual
change; substituting it into the old lemma without this proof would be invalid.

## 3. Complete rectangular quadratic Gram matrix

Use integer grid points

    (z,w)=(x+y sqrt(d),x-y sqrt(d)), 0<=x<a, 0<=y<b.

Their second coordinates are distinct because sqrt(d) is irrational. The
invertible linear substitution into a polynomial and the rectangular
Schwartz-Zippel bound give incidence with M=max(a,b). One direct proof bounds
zeros on each nonidentically-zero horizontal slice by the degree in x;
identically-zero slices are bounded by the remaining y-degree. The total
is at most max(a,b) times total degree.

Take the rows from Lemma 1, with n=ab, and the coordinatewise trace pairing

    <alpha,beta>=Tr_(K/Q)(alpha conjugate(beta)).

For alpha=A+B sqrt(d) and beta=C+E sqrt(d), A,B,C,E real,
this is 2(AC+D BE), both for d>0 and d<0. Thus the Gram form is positive
on the real coefficient space. The rank lemma also gives independence of
the chosen-embedding rows over C, hence of the trace-expanded rows. Its
Gram determinant G is a POSITIVE RATIONAL INTEGER: every row coordinate
is in Z[sqrt(d)], and the trace pairing is integral on that order.
Maximality of the quadratic order is unnecessary.

Write H=a+b sqrt(D)>=1. Both field embeddings of each point have modulus
at most H. An ordinary derivative entry has size at most
R^(J-1) H^(r+s); derivatives of order j>r are simply zero. Hence Hadamard
gives the completely specified upper bound

    log det G <= RS log(2abJ)+2RS(J-1)log R
                         +RS(R+S-2)log H.                (2)

This retains the factor 2 from the trace and the actual column count abJ.

## 4. Divisibility for every derivative depth

For an odd prime p with chi(p)=-1 put

    h_(r,s)=min(floor(r/p),S-1-s),
    E_p(R,S)=2 sum_(r<R,s<S)h_(r,s).

**Lemma 2.** If the Gram determinant above is nonzero, then

                       v_p(det G)>=E_p(R,S)             (3)

for EVERY J>=1; J need not be smaller than p.

Proof. At every quadratic grid point psi=z^p-w is in p Z[sqrt(d)]. All
positive ORDINARY z-derivatives of psi have coefficients divisible by p,
including the p-th derivative p!. Derivatives above p vanish. Repeated
Leibniz differentiation of z^(r-ph) psi^h w^s therefore retains p^h.
The exact row transformation is

    vtilde_(r,s)=sum_(i=0)^h (-1)^i binom(h,i)v_(r-pi,s+i).

The indices remain in the original rectangle. In increasing r this is
unipotent triangular. Its Gram congruence preserves the determinant, and
factoring p^h out of each row and column proves (3). The p-adic row change
may be chosen separately for each p, since all calculations concern the
same unchanged integer determinant. QED.

This proof FAILS for Hasse derivatives: the p-th Hasse derivative of z^p-w
is 1, not a multiple of p. No factorial normalization is silently used.

Layer counting gives an exact formula for the VALUATION LOWER TEMPLATE:

    E_p(R,S)=2 sum_(h=1)^K (R-ph)(S-h),
    K=min(floor((R-1)/p),S-1).                           (4)

It is not asserted equal to the actual determinant valuation. In particular

    E_p=2[RS K-(R+pS)K(K+1)/2+pK(K+1)(2K+1)/6].         (5)

For every integer k>=0,

    sum_(s=0)^(S-1)min(k,S-1-s) >= Sk-k(k+1)/2.

Summing over r, using floor(r/p)>=r/p-1 and floor(r/p)<=r/p,
proves the convenient all-p inequality

    E_p/(SR^2) >= alpha/p-2/R-R/(3S p^2),
    alpha=1-1/R-1/(2S).                                  (6)

No asymptotic approximation to an individual floor is omitted from (6).

## 5. Balanced parameters and proof of T1

For integer R sufficiently large with R>=q, put

    B=ceil(log(2R)), S=floor(R/B), J=S,
    a=ceil(2 sqrt(R) D^(1/4)),
    b=ceil(2 sqrt(R) D^(-1/4)).                           (7)

All thresholds below are absolute. Since D<=R,

    4R<=ab<=9R,  M=a<=2R^(3/4)+1<=S,  S<=R/4,
    H<=6 sqrt(R) D^(1/4).                                (8)

The bounds follow by expanding the two ceiling products; for the last one,
a+b sqrt(D)<=4sqrt(R)D^(1/4)+1+sqrt(D), and the last two terms are
at most 2sqrt(R)D^(1/4). The comparison M<=S holds for all sufficiently
large R because R^(1/4)/log(2R) tends to infinity. This establishes ONE
absolute threshold uniformly for every D<=R, not a threshold depending on d.

Lemma 1 applies: its left side is at least 4RS, while, since J=S>=M,
its right side is MR+2RS+S^2<=3RS+S^2<4RS.
Dividing (2) by SR^2 and using (7)-(8),

    log det G/(SR^2)
       <= (1/2)log R+(1/4)log D+O(1).                    (9)

Indeed log(2abJ)/R=O(log R/R), 2(J-1)log R/R=O(1),
and ((S-2)/R)log H=O(1), uniformly D<=R. Notice that a large jet depth
costs only O(1) after normalization; setting J equal to the grid side in
the original construction hid this flexibility.

Let P=ceil(R/S), so P is of order log R. Sum (6) over inert odd primes
P<=p<=R and multiply by log p. The positive integer property, (3), and (9)
bound the sum of E_p log p by log det G. Chebyshev's theta(R)=O(R)
and partial summation give

    sum_(p>=P)log p/p^2=O(1/P).

The total error terms in (6) are consequently O(1). Since
alpha=1-O(1/S), dividing by alpha costs another O(log R/S)=O(1).
The omitted primes p<P have total logarithmic reciprocal mass O(log P)
by the elementary Mertens bound. Including p=2 costs only a constant.
We obtain (T1) with log D and error O(1+log log(3R)). Replacing D by q
weakens it as stated. For real R use floor(R); enlarging the absolute
threshold and constant pays the endpoint. This proves T1 and T2. QED.

No independence or density of inert primes has been assumed. Only positive
prime-power divisors of a fixed nonzero integer were used in the comparison.

## 6. Laplace transfer and the real-zero gap T3

Let ell=log q and take q large enough for the absolute threshold in T1.
For t in (0,1], define

    I_-(t)=sum_(chi(p)=-1)log p/p^(1+t).

Stieltjes integration of A_chi gives

    I_-(t)=t integral_0^infinity A_chi(exp y)exp(-ty)dy.   (10)

For y>=ell, T1 bounds the integrand cumulative function by
(1/2)y+(1/4)ell+C(1+log(2+y)). For y<ell use the elementary Mertens
bound A_chi(exp y)<=y+O(1). A single valid majorant on all y>=0 is

    (1/2)y+(1/4)ell+C(1+log(2+y))+(1/2)y 1_(y<ell).

Integrating and using concavity of log under the exponential probability
measure proves

    I_-(t)<=1/(2t)+ell/4
                      +O(t ell^2+1+log(2+1/t)).          (11)

For the ramified primes,

    sum_(p|q)log p/p=O(1+log(2+ell)).                     (12)

To see this, split at p=ell: Mertens pays the small primes, while the large
ones contribute at most ell^(-1) sum_(p|q)log p<=1.
The full prime sum at 1+t is 1/t+O(1), by the pole of -zeta'/zeta and the
absolutely bounded k>=2 prime-power contribution. The character's complete
prime-power contribution with k>=2 is likewise bounded absolutely. Since
chi(p)=1,-1,0,

    -L'/L(1+t,chi)
       >= -ell/2-O(t ell^2+log(2+1/t)+log(2+ell)).         (13)

This is an estimate for each real character separately. No family mean
or deletion of a possible exceptional character has occurred.

The classical Hadamard-product formula, used in Section 2 of the pinned
OpenAI original, says at real 1<s<=2

    -L'/L(s,chi)= (1/2)log(q/pi)
      +(1/2)Gamma'/Gamma((s+parity)/2)
      -sum_rho Re[1/(s-rho)].                            (14)

The real-part sum converges and its terms are nonnegative. Its gamma term
is bounded for both parities. At a hypothetical real zero beta, keeping
at least one copy in (14) yields

    -L'/L(1+t,chi)<=ell/2-1/(t+1-beta)+O(1).              (15)

Set t=ell^(-2). Combining (13)-(15) gives

    1/(ell^(-2)+1-beta)<=ell+O(log ell).

For all sufficiently large q the right side is positive. Inverting and
multiplying by ell proves

    (1-beta)ell>=1-O(log ell/ell),

which is T3. The existence of absolute constants follows from the displayed
uniform bounds. Their numerical values have NOT been computed here.
No statement about zeros at nonzero height follows from this last step.

## 7. What this proof does and does not improve

This is a stronger prime-bias estimate from the determinant construction,
and a stronger asymptotic coefficient than the original statement's
unspecified positive real-zero gap. It does not improve any separately
established fixed 7/8 or all-field strip. It needs no such theorem as input.

The classical product formula, resultants, Hadamard inequality and
Schwartz-Zippel estimate are credited rather than claimed invented. The
component contribution proposed here is the independent-jet rank budget,
the discriminant-balanced rectangle, and the complete quantitative transfer
through the small-prime and Laplace costs. Source authorship verification,
independent mathematical review, and formal proof checking are distinct
from the finite exact computations in verify.py.
