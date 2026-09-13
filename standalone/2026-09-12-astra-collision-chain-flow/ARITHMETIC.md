# A matching logarithmic diagonal and a relative covariance target

2026-09-12. **Proposed component proof, requiring independent mathematical
review. The actual covariance upper bound and RH are not proved.**

This is an add-only continuation of XCC26, PR #848 at
`99101457b32b6f10f4eda88ca998048404b860ea`, rather than another change to the
underlying arithmetic source. The logarithmic lower bound below is the new
component. The short-source Newton identity is classical; Huxley–Watt,
arXiv:1807.05890, and its predecessors are credited. XCC26's common growth
exponent is an explicitly imported proposed result, not a numerical premise.

## 1. Literal source and the inherited exact identities

Write mu for the ordinary Möbius function and lambda(n)=(-1)^Omega(n). Put

    m(k)=sum_(n<=k) mu(n)/n,          F_Y=sum_(k<=Y) m(k)^2.

A crossing is an integer Y>=2 with mu(Y)!=0 and m(Y-1)m(Y)<=0. At a crossing,
|m(Y)|<=1/Y and, when m(Y)!=0, its sign is lambda(Y). Define

    c_n=mu(n) (n<=Y),       c_(2Y)=-2Y m(Y),       c_n=0 otherwise.

Then P_c(1)=sum c_n/n=0, |c_n|<=2, and EVERY coefficient has the form
c_n=lambda(n)b_n with b_n>=0. The latter includes the added coefficient,
since lambda(2Y)=-lambda(Y). Thus z=c*c also has exactly this sign pattern:

    z(d)=lambda(d) sum_(ab=d)b_a b_b.                         (1)

There is no cancellation inside one product fiber. Cross-product cancellation
remains a separate matter.

Let b=Y+1 and B=b^2-1. The identity

    mu-(2c-1*c*c)=mu*(delta-1*c)*(delta-1*c)

proves equality with mu at every integer <=B. The excluded boundary b^2 is
not silently included. With H_j=sum_(l<=j)1/l and H_0=0 define

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    Q(k)=sum_d z(d)K_d(k),           Y<k<=B.

Both separated terms cancel: sum z(d)/d=P_c(1)^2=0 and
sum z(d)log(d)/d=2 P_c(1) sum c_n log(n)/n=0. Hence Q can also be calculated
as the entirely rational sum sum z(d)H_floor(k/d)/d.

Set

    D_Y=sum_d z(d)^2 sum_(k=Y+1)^B K_d(k)^2,
    C_Y=sum_(d!=e) z(d)z(e) sum_(k=Y+1)^B K_d(k)K_e(k).

The covariance convention is ORDERED pairs d!=e. Thus sum Q(k)^2=D_Y+C_Y.
If t(k)=sum_(n<=k)c_n/n, then m(k)=2t(k)-Q(k) on this whole annulus and
sum t(k)^2=(Y-1)m(Y)^2<=1/Y. In particular,

    F_B <= F_Y+8/Y+2D_Y+2C_Y.                               (2)

XCC26 proves D_Y<=288 H_(4Y^2)^4. Its precise upper constant is inherited;
the lower proof below does not use a measured diagonal or fitted asymptotic.

## 2. A native product-fiber lower bound

**Theorem A1.** Define the positive convergent Euler product

    A4=product_p (1-1/p)^4 (1+4/p).

Along the unbounded set of crossings,

    liminf D_Y/(log Y)^4 >= A4/(81*15^4)>0.                  (3)

Together with the inherited upper bound, this gives D_Y asymptotic order
(log Y)^4. No effective first Y or optimal constant is claimed.

### 2.1 An injective family of actual signed products

Take four pairwise coprime squarefree positive integers g,h,r,s in

    Y^(1/3) < g,h,r,s <= Y^(2/5).

Put (a,b,c,d)=(gr,hs,gs,hr). All four lie below Y^(4/5), hence are in the
UNCHANGED Möbius prefix. Their products agree at n=ghrs, with

    Y^(4/3)<n<=Y^(8/5).

Their contribution to z(n)^2 is +1: they are squarefree and
mu(a)mu(b)mu(c)mu(d)=1. The parametrization is injective into the ORDERED
quadruples appearing in z(n)^2, since

    g=gcd(a,c), h=gcd(b,d), r=a/g, s=c/g.

Equation (1) ensures that additional terms, including any involving the late
coefficient, cannot subtract these contributions. Therefore

    sum_(Y^(4/3)<n<=Y^(8/5)) z(n)^2/n
       >= sum_(g,h,r,s in box; squarefree, pairwise coprime) 1/(ghrs). (4)

This sign argument is source-specific. It is not a bound for an arbitrary
normalized vector with cancellations inside a product fiber.

### 2.2 The complete annulus contains enough positive kernel mass

For each such n choose ceil(n/8)<=k<=floor(n/4). For all sufficiently large Y,
this interval lies in [Y+1,B]. Since k<n,

    n K_n(k)=log n-H_k >= log(n/k)-1 >= log4-1>1/3.

Here H_k<=log k+1 and log4>4/3. For n>=72 the chosen integer interval has at
least n/9 members. Consequently

    sum_(k=Y+1)^B K_n(k)^2 >=1/(81n).                       (5)

The integer endpoint loss is explicitly paid. Equations (4)–(5) reduce (3)
to a weighted squarefree coprime counting statement, proved next.

### 2.3 The weighted four-variable asymptotic, with the whole Euler tail

For Re(s_i)>1 the generating function of pairwise coprime squarefree tuples is

    product_p (1+p^-s1+p^-s2+p^-s3+p^-s4)
       = zeta(s1)zeta(s2)zeta(s3)zeta(s4) G(s1,s2,s3,s4),

where the local factor of G is

    (1-x1)(1-x2)(1-x3)(1-x4)(1+x1+x2+x3+x4).

Every linear coefficient vanishes. The sum of the absolute coefficients after
weighting xi by 1/p is 1+O(p^-2), with a uniform constant. It follows that
G has a Dirichlet expansion with coefficients g(d1,d2,d3,d4) satisfying

    sum |g(d1,d2,d3,d4)|/(d1 d2 d3 d4)<infinity.            (6)

This uses only convergence of sum_p p^-2. It is not an appeal to PNT or a
probabilistic independence hypothesis.

Convolve these coefficients with four ordinary harmonic sums. For fixed d,

    (1/log Y) sum_(Y^a/d<n<=Y^b/d)1/n -> b-a,

and, uniformly in every positive integer d, the unnormalized sum is at most
1+(b-a)log Y. This bound also covers a lower endpoint below one. Dominated
convergence using (6) therefore gives

    sum_(Y^a<g,h,r,s<=Y^b; squarefree, pairwise coprime)1/(ghrs)
        ~ (b-a)^4 G(1,1,1,1)(log Y)^4.

G(1,1,1,1)=A4 and b-a=1/15. This proves (3). Positivity of A4 follows because
every Euler factor is positive and its logarithm is O(p^-2).

## 3. The resulting full-proof target is weaker than a nonpositive covariance

XCC26's proposed common-exponent theorem states

    lim_(Y->infinity) log(1+F_Y)/log(Y+1)=2Theta-1,

where Theta is the supremum of real parts of nontrivial zeta zeros. Its proof
uses a complete every-prefix zero witness and a classical zero-free-half-plane
Mertens bound. It permits Theta=1 and multiple zeros. We use that theorem at
its frozen source; it has not been formalized or independently accepted here.

**Conditional theorem A2.** Suppose a fixed finite K>=0 satisfies

    C_Y <= K D_Y                                             (OPEN-A)

on an unbounded sequence of ACTUAL crossings. Then, with the preceding
common-exponent theorem, RH follows.

Indeed (2) and the diagonal upper bound give F_B<=F_Y+O_K((log Y)^4). If
kappa=2Theta-1>0, the common-exponent theorem gives
F_B=Y^(2kappa+o(1)) and F_Y=Y^(kappa+o(1)), a contradiction along that same
sequence. Thus Theta=1/2; reflection is the usual final symmetry argument.

This does NOT prove OPEN-A. It shows that requiring C_Y<=0 is unnecessarily
strong for this consumer. A bounded positive multiple of the actual diagonal
would suffice. The new lower bound supplies its genuine scale but does not
bound the signed covariance from above.

## 4. What the exact finite computation covers

research_algebra.py checks 144 distinct coprime-squarefree parametrizations,
the local Euler polynomial, and EVERY native crossing Y<=17. It includes all
products in c*c, all cells through B, the collar, rational Newton identity,
and directed logarithmic diagonal/covariance values. These finite examples
are not evidence of an unbounded recurrence theorem by themselves. The old
countermodels explaining why generic sign coherence is insufficient remain
unchanged.

The exact remaining step is OPEN-A or another genuine native arithmetic gain.
No new bound on F_Y, on Theta, or on the prime counting error is claimed.
