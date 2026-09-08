# DPG26: a quantitative inverse for the complete prime-power graph

Status: PROPOSED COMPONENT THEOREMS WITH COMPLETE PROOFS; independent review required.
Date: 2026-09-08. Author: Astra. RH and the sign of the complete Weil form remain unproved.

This packet supplies a positive estimate, not a new RH-equivalent assumption.
The graph in PR #790 already has an exact sum of squares and a known null vector.
We prove a quantitative lower bound away from that vector, on every finite
DIVISOR-CLOSED support. Inversion costs at most a logarithm of the integer cutoff,
and is uniform in all exponents when the number of distinct prime factors is fixed.
An explicit tree decoder attains the stated bound without a dense inverse.

Canonical-path comparison and weighted Poincare inequalities are classical.
The arithmetic point here is the least-prime-first tree: its descendant mass is
a finite Euler product, paid by the ORIGINAL log-prime edge weight. No priority
claim is made for the general method or for the one-coordinate diagonalization.
The proof below is self-contained; it uses no PNT, RH, zero table, statistical
independence hypothesis about primes, or unproved correlation estimate.

## 0. Objects, metric, and inherited identity

Let S be a nonempty finite set of positive integers, closed under divisors.
Then 1 belongs to S. Let P be the finite set of primes occurring in S and put

    H_S = sum_(n in S) 1/n,
    r_S = max_(n in S) omega(n),
    g_S(n) = 1/sqrt(n),
    Pi_S v(n) = [sum_(m in S) v(m)/sqrt(m)]/[H_S sqrt(n)].

Here omega counts DISTINCT prime factors, not prime factors with multiplicity.
Pi_S is the orthogonal projection onto g_S (tensored with the identity when
values lie in a complex Hilbert space V). All vector norms below are in the
ORIGINAL unweighted space ell2(S;V); no changing metric is hidden in a bound.
We sometimes write f(n)=sqrt(n)v(n), so ||v||^2=sum ||f(n)||^2/n.

Let Lambda(p^k)=log p for prime p and k>=1, with Lambda=0 otherwise. Define

    (C_S)_(i,j) = Lambda(n)/sqrt(n) if i=nj or j=ni, n>=2,
                  0 otherwise (including the diagonal),
    D_S(j,j) = log j + sum_(n>=2, nj in S) Lambda(n)/n,
    L_S = D_S-C_S.

The sum has every allowed prime power, not only prime edges. Both cross
orientations occur in C_S. Expanding the following squares gives exactly

    E_S(v) := <v,L_S v>
      = sum_(p prime,k>=1,j>=1 : p^k j in S)
            (log p)||v(p^k j)-p^(-k/2)v(j)||^2
      = sum_(p^k j in S) (log p)/(p^k j)||f(p^k j)-f(j)||^2.     (0.1)

The first diagonal equals log j because sum_(n|j)Lambda(n)=log j.
Divisor closure is used here to retain all downward endpoints. Equality in
(0.1) forces f constant, by repeated removal of prime factors. Thus

    ker L_S = Ran Pi_S.                                       (0.2)

These are the DC-1 source identity and nullspace from PR #790, reconstructed
here rather than assumed from a finite numerical test. Positivity of L_S is
not positivity of C_S and is not a determinant or spectrum identification with xi.

## 1. DPG26.1: the full quantitative bound

For p in P define the finite Euler mass

    Z_P(p) = product_(q in P, q<p) (1-1/q)^(-1),
    kappa_P = max_(p in P) Z_P(p)/(log p).

If S contains more than one integer, r_S>=1 and

    ||(I-Pi_S)v||^2 <= r_S kappa_P E_S(v) < 24 r_S E_S(v)
                       whenever E_S(v)>0.                    (1.1)

In particular, with non-strict Loewner inequalities,

    L_S >= [1/(24r_S)](I-Pi_S),
    ||L_S^dagger|| <= r_S kappa_P <= 24 r_S.                   (1.2)

The dagger denotes the Moore-Penrose inverse, zero on the stated nullspace.
No inverse on the null vector is claimed. For S={1}, the residual is zero and
(1.1) holds without dividing by r_S.

For S={1,...,N}, N>=2,

    ||L_N^dagger|| <=24 max_(n<=N)omega(n)
                   <=24 log N/log 2.                         (1.3)

More sharply r_S<=R(N):=max{r : (r+1)!<=N}; hence the inverse bound is
O(log N/log log N). This last asymptotic uses only the integral lower bound
for log(r!), not a theorem about prime distribution. The simpler explicit
bound in (1.3) suffices to show SUBPOWER inverse cost.

For every divisor-closed S using only primes {2,3,5}, however large its
prime exponents or number of vertices,

    L_S >=(1/6)(I-Pi_S).                                    (1.4)

Indeed Z_P(p) is no larger than 1,2,3 at p=2,3,5 respectively, while
log2>1/2, log3>1, log5>3/2. Thus kappa_P<2 and r_S<=3.
These elementary logarithm inequalities also have rational-series checks.

### 1.1 Least-prime-first paths

For a>1 let p(a) be its LEAST prime factor, e(a) its full valuation there,
and

    parent(a)=a/p(a)^e(a).

Keep precisely this one edge per nonroot vertex. Its conductance in f
coordinates is (log p(a))/a. It is an edge of (0.1), even when e(a)>1.
This tree stays in S because S is divisor closed. Each path to 1 has exactly
omega(n) edges: the entire power of the smallest remaining prime is removed
at each step.

For Hilbert-valued f, Cauchy-Schwarz along the path gives

    ||f(n)-f(1)||^2
       <= r_S sum_(a on path n->1, a>1)
                         ||f(a)-f(parent(a))||^2.            (1.5)

The nontrivial arithmetic step is the DESCENDANT description. If the path
from n passes through a, then

    n=a m, with every prime factor of m strictly less than p(a). (1.6)

Conversely (1.6) makes a a path vertex whenever am is in S. All exponents
of these smaller primes are allowed in the upper bound; no squarefree
restriction is imposed. Therefore

    sum_(n in S : a on path n->1) 1/n
      = (1/a) sum_(m : am in S, Pplus(m)<p(a)) 1/m
      <= Z_P(p(a))/a.                                       (1.7)

Sum (1.5) with weights 1/n, use (1.7), and compare each tree edge to its
ORIGINAL conductance:

    sum_(n in S)||f(n)-f(1)||^2/n
      <=r_S sum_(a>1) Z_P(p(a))/a ||f(a)-f(parent(a))||^2
      <=r_S kappa_P E_tree(f)
      <=r_S kappa_P E_S(v).                                 (1.8)

The weighted mean minimizes sum ||f-c||^2/n, so replacing f(1) by that mean
only decreases the left side. This proves (1.1), subject to kappa_P<=24,
which is proved next. Notice that (1.8) is stronger: it is an anchored
inequality using only |S|-1 selected original edges.

### 1.2 An elementary Euler-mass bound with every smooth number retained

We prove

    product_(q<p)(1-1/q)^(-1) <24 log p                      (1.9)

for every prime p. No Mertens product theorem is imported.

First Psi(x)=sum_(n<=x)Lambda(n)<3x and
M(x)=sum_(n<=x)Lambda(n)/n<=log x+3 for every x>=1.
For the first statement, prime valuations of the central binomial coefficient
give Psi(2k)-Psi(k)<=log binom(2k,k)<=2k log2. Dyadic summation and log2<3/4
give Psi(x)<3x. For the second use the EXACT factorial identity

    sum_(n<=x)Lambda(n)floor(x/n)=log(floor(x)!).

The bound floor(x/n)>=x/n-1 then gives x M(x)<=x log x+Psi(x).
This reconstructs the elementary bound used in the source packet.

Also Abel summation, log(1+1/n)<=1/n, log2<3/4, and
sum_(n>=2)n^-2<=1/4+integral_2^infinity t^-2 dt=3/4 yield

    sum_(n>=2) log n/[n(n-1)]
      =log2+sum_(n>=2)log(1+1/n)/n <3/2.                    (1.10)

For p>=3 let Z be the Euler product on the left of (1.9). On integers
whose prime factors are <p, the weights 1/(n Z) form a probability measure.
Its mean logarithm is the finite, absolutely convergent sum

    B_p=sum_(q<p) log q/(q-1)
       <=M(p)+sum_(n>=2)log n/[n(n-1)]
       <log p+9/2.                                        (1.11)

Markov's inequality shows that at least half the mass lies at log n<=2B_p.
Since H_m<=1+log m, this implies

    Z/2 <= sum_(n<=exp(2B_p))1/n <=1+2B_p,
    Z <=2+4B_p <4log p+20 <24log p.                        (1.12)

The final strict inequality uses log p>=log3>1. For p=2 the product is 1,
so (1.9) is immediate. A product using only primes in P is no larger.
Thus kappa_P<24, and the theorem is proved.

### 1.3 Why the ordering is essential to THIS bound

Removing the greatest rather than least prime first gives a different tree.
The descendants of its edge 2->1 include 2m for all odd m<=N/2. Its harmonic
load divided by that edge's conductance is

    [sum_(m<=N/2, m odd)1/m]/log2 ~ (log N)/(2log2),

not a uniform Euler-mass constant. This does not refute a spectral gap for
that graph. It explains why the selected comparison tree is not arbitrary.
The finite checker reconstructs BOTH descendant counts as a direction test.

## 2. DPG26.2: a bounded, explicit source decoder

Let B_S v be the vector of all edge differences from (0.1), each multiplied
by sqrt(log p). Select its coordinates on the above tree. Given arbitrary
tree data y_a in V (a in S, a>1), define recursively

    F(1)=0,
    F(a)=F(parent(a))+sqrt(a/log p(a)) y_a.

Set c=H_S^(-1)sum_(a in S) F(a)/a and define

    (R_S y)(a)=(F(a)-c)/sqrt(a).                           (2.1)

Every tree data vector produces a function with those exact differences.
Apply (1.8) to that function to obtain

    ||R_S y|| <=sqrt(r_S kappa_P)||y|| <=sqrt(24r_S)||y||.   (2.2)

For an actual complete graph field,

    R_S (B_S v)|_tree = (I-Pi_S)v.                         (2.3)

Thus a complete-source observation which includes these tree edges has an
explicit left inverse modulo the single known harmonic mode. With additive
edge noise e, the recovered vector differs from (I-Pi_S)v by at most
sqrt(24r_S)||e||. There is NO requirement to invert an unstable selected
matrix of unrelated ratio rows.

This is not a claim that a previously compressed physical observation contains
these tree coordinates. Any application must identify that source adapter.
After factorizations and parent pointers are supplied, the scalar recursion
and weighted centering take O(|S|) arithmetic operations. This is not a bit
complexity bound or a bound on factorization cost.

### 2.1 The full Poisson solve also has a controlled iteration

For S contained in {1,...,N}, the same proof of M(x)<=log x+3 gives
D_S(j,j)<=log N+3. The inequality ||a-b||^2<=2||a||^2+2||b||^2 in
(0.1) shows L_S<=2D_S, hence

    spectrum(L_S restricted to g_S-perp)
         is contained in [1/(24r_S), 2(log N+3)].            (2.4)

Thus its nonzero condition number is at most 48r_S(log N+3).
Given b orthogonal to g_S, the unique solution u orthogonal to g_S of
L_S u=b satisfies ||u||<=24r_S||b||. The full-source Richardson iteration

    u_0=0,
    u_(m+1)=u_m+[b-L_S u_m]/[2(log N+3)]

uses EVERY prime-power edge and has the explicit error bound

    ||u_m-u|| <=24r_S||b||
          [1-1/(48r_S(log N+3))]^m.                        (2.5)

This follows by diagonalizing the finite self-adjoint L_S on the stated
orthogonal complement. It is not a new arithmetic cancellation assumption,
not an algorithmic claim about the full Weil form, and not a claim that a
finite numerical iteration here was run on arbitrarily large supports.

## 3. DPG26.3: exact prime-power spectra and rectangular source spectra

This section solves the graph, not just bounds it, on prime-exponent boxes.
It must NOT be substituted for a nonrectangular cutoff such as n<=N.

For S={1,p,...,p^m}, put q=1/p, write f(e)=p^(e/2)v(p^e), and omit log p
from the generator temporarily. In the weighted metric sum_(e=0)^m q^e|f(e)|^2,

    (L f)(e)=sum_(j<e)[f(e)-f(j)]
                     +sum_(j>e)q^(j-e)[f(e)-f(j)].          (3.1)

For 1<=j<=m, define A_j=sum_(l=1)^(m-j+1)q^l and the step vector

    u_j(e)=0 for e<j-1; -A_j for e=j-1; 1 for e>=j.         (3.2)

Its weighted mean is zero and its squared norm is
q^(j-1)A_j(1+A_j). Two such vectors are orthogonal: the earlier vector
is constant on the support of the later vector, whose weighted mean is zero.
Together with the constant vector they form an orthogonal basis.

Substitution in (3.1) gives the exact eigenvalues

    0 and (log p)[j+sum_(l=1)^(m-j+1)p^-l], 1<=j<=m.        (3.3)

For e<j-1 the sum vanishes by the weighted mean cancellation. At e=j-1
it equals -(j+A_j)A_j; above that level it equals j+A_j.
The eigenvalues strictly increase, since consecutive differences are
(log p)[1-p^(-(m-j+1))]>0.

For a rectangular source S={product_(p in P)p^e_p:0<=e_p<=m_p}, the graph
is a tensor sum of these one-prime operators. Tensor products of (3.2)
therefore give ALL eigenvectors and the spectrum is ALL sums of (3.3), with
multiplicities from coincidences retained. In particular its gap is exactly

    min_(p in P) (log p) sum_(l=0)^m_p p^-l.                 (3.4)

For example on {2^a3^b:0<=a<=2,0<=b<=1}, the prime-2 eigenvalues are
0,(7/4)log2,(5/2)log2, and the prime-3 eigenvalues are 0,(4/3)log3.
The six sums are the complete spectrum. No floating eigenvalue solve is
part of this assertion.

At infinite exponent on a FIXED finite prime set, the one-prime orthogonal
basis has A_j=q/(1-q); its positive eigenvalues are

    (log p)[j+1/(p-1)], j>=1.                              (3.5)

To justify the operator, in unweighted coordinates it is the diagonal
number operator plus a bounded symmetric Toeplitz operator: the off-diagonal
absolute row sum is at most 2sqrt(q)/(1-sqrt(q)). It is self-adjoint on the
number-operator domain and has compact resolvent. The vectors in (3.2), now
with infinite tails, belong to that domain. Completeness follows because a
vector orthogonal to all of them has equal successive coordinates in the
weighted representation and is therefore constant; orthogonality to the
constant then makes it zero. Tensoring finitely many factors is legitimate.
The gap is min_(p in P) p log p/(p-1), independent of all exponent horizons.

This is NOT an infinite all-prime operator at the critical harmonic weight.
For all primes the putative ground vector has divergent squared norm
sum_n1/n, and the unrenormalized birth diagonal diverges. We use (1.1)
for the finite growing-prime problem instead.

## 4. DPG26.4: a priced one-mode reduction for compatible perturbations

This finite-dimensional consequence is sometimes useful when the graph is a
positive part of a larger source. It does not assert a bound for that larger
source without checking the stated hypothesis.

In scalar ell2(S), normalize g_S to unit length g, put Q=I-|g><g|, and let
K be ANY Hermitian perturbation. Let gamma=1/(24r_S). Suppose

    ||Q K Q||<=theta gamma, 0<=theta<1.                    (4.1)

The complement A=Q(L_S+K)Q is then >=(1-theta)gamma Q. Set
k00=<g,Kg> and b=QKg. Completion of squares gives

    L_S+K >=0 iff k00-<b,A^(-1)b> >=0,                    (4.2)
    0<=<b,A^(-1)b><=24r_S ||b||^2/(1-theta).               (4.3)

There is at most ONE negative eigenvalue. All coupling terms survive in
(4.2); positivity of A alone does not prove the scalar sign. For Hilbert-
valued graph vertices this is an operator on one copy of that Hilbert space,
not generally a scalar or a rank-one finite correction.

No perturbation K identifying the complete Weil form has been supplied in
this packet. Equations (4.1)-(4.3) are conditional application tools, whereas
(1.1)-(3.5) are unconditional graph/source theorems.

## 5. Concrete application to the existing cusp estimate

For S={1,...,N}, the complete cusp matrix from PR #790 now satisfies the
STRICTLY STRONGER source inequality

    <v,C_N v> <= sum_j [log j+M(N/j)]||v(j)||^2
                      -(1/(24r_N))||(I-Pi_N)v||^2.        (5.1)

Thus any non-harmonic coherent primitive profile has an explicitly paid
penalty. If G_j(s) are the zero-mean-window primitives in DC-3, applying
(5.1) in the Hilbert space L2(0,ell_N) keeps the entire original cusp form
and yields this additional nonnegative lower term after integration.
More explicitly, retaining DC-3's source estimates and its EXACT mean-zero
hypothesis in each interval, for N>=2 its conclusion strengthens to

    <f,T f> >= (3/2)[(log N+1/2) sum_j ||G_j||^2
                        +(1/(24r_N)) ||(I-Pi_N)G||^2].    (5.2)

The norm is in the same direct sum of primitive L2 spaces. To verify (5.2),
replace only the cusp inequality in DC-3's proof by (5.1), leaving its
local-diagonal and regular-cross estimates unchanged. This corollary uses
those specifically scoped source estimates as external-to-this-packet
inputs; the graph theorem itself does not need them and the checker does
not evaluate the full W kernel. No new independent acceptance of DC-3 is
implied by stating the conditional composition.

This does not control the window means or their coupling, and does not turn
those shrinking windows into a cofinal test family.

For a fixed-prime physical construction, (2.3) is a stable decoder ONLY if
its observation actually contains the displayed prime-power differences
with their native weights. A ratio/moment projection that drops those edges
requires its own source map; the theorem does not repair one by relabeling.

## 6. Limitations and the attempted stronger conclusion

A rank-independent gap for ALL cutoffs N was explored but is not proved here.
The available bound is 1/(24r_N), and no finite numerical panel promotes it
to a constant. The product-coordinate spectrum applies to rectangular boxes,
not to a knapsack cutoff: tensor independence is lost under n<=N.

Without divisor closure the theorem is false as written: S={1,6} has no
prime-power edge and hence zero energy for a nonconstant vector. The missing
divisors cannot be silently supplied in a supposedly unchanged source.

These results do not prove J(A)=0, complete the factorial source domain,
bound the full Mobius block gain, or prove RH. They remove a QUANTITATIVE
inverse/near-null-direction obstruction for the complete divisor graph.
The next legitimate application must retain its exact graph observations
or prove a norm-controlled source adapter, and separately bound any signed
perturbation. Neither of those missing source-specific assertions is assumed.
