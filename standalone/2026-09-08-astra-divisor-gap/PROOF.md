# ADG26: coercivity of the literal prime-power divisor form

Status: PROPOSED COMPONENT THEOREMS WITH COMPLETE PROOFS; independent review pending.
Date: 2026-09-08. Research contribution, not a Reviewer D acceptance.
RH and the cumulative prime-discrepancy upper bound remain unproved.

The earlier divisor-cusp packet proves a sum of squares and identifies its null
space. This packet proves a quantitative spectral gap. The proof is elementary:
it uses neither PNT nor RH nor zero verification nor random independent prime
phases. The finite/infinite domains and the inherited metric are explicit.
General graph Poincare/path comparison, Dirichlet forms, and Schur complements
are classical. No external novelty/priority or sharp-constant claim is made.

## 1. The theorem, including arbitrary exponent depth and cutoffs

Let S be a nonempty finite divisor-closed set of positive integers: if n is in S,
then every positive divisor of n is in S. Thus 1 is in S. Assume S is not {1}.
Let P>=2 bound all prime factors of every element of S. It need not bound the
integers themselves. Let H be any complex Hilbert space. Define

    Z_S = sum_(n in S) 1/n,
    E_S(f) = sum_(p prime, k>=1, j p^k in S)
                   (log p)/(j p^k) ||f(j p^k)-f(j)||_H^2,
    kappa(P) = 48[1+log(16 log P)].                        (1)

Every allowed prime-power edge is included once. All logarithms are natural.
The harmonic metric is sum ||f(n)||^2/n, NOT unweighted coefficient length.

**ADG26.T1 (anchored inequality).** For every such S, P and f,

    sum_(n in S) ||f(n)-f(1)||^2/n <= kappa(P) E_S(f).       (2)

In particular, with fbar=Z_S^(-1) sum f(n)/n,

    sum_(n in S) ||f(n)-fbar||^2/n <= kappa(P) E_S(f).       (3)

These estimates are uniform in |S|, the exponents of its prime factors, and the
shape of the divisor-closed cutoff. P is the largest allowed PRIME, not an
unknown zero parameter. Dependence on P is only O(1+log log P).
The case S={1} is vacuous, and can be assigned P=2.

For S={1,...,N}, set v_n=f(n)/sqrt(n), h_N=(1/sqrt(n))_(1<=n<=N),
Pi_N=I-h_N h_N^*/Z_S, and

    (C_N)_(i,j) = Lambda(q)/sqrt(q) if i=qj or j=qi, q>=2;
                   0 otherwise,
    M(x)=sum_(2<=q<=x) Lambda(q)/q,
    D_N=diag(log j+M(N/j)),  L_N=D_N-C_N.               (4)

Lambda is the ordinary von Mangoldt function. The diagonal of C_N is zero.
Then, in the ORIGINAL Euclidean v metric,

    kappa(P)^(-1) Pi_N <= L_N <= 2(log N+3) Pi_N,       (5)
    ker L_N = span{h_N}.

One may take P=N; the largest prime <=N gives the stronger bound. The upper
bound in (5) is not asserted for a time-varying physical source or for xi.
On h_N perpendicular the condition number is at most

    96(log N+3)[1+log(16 log P)].                       (6)

For Hilbert-valued v, the null space is ONE COPY OF H, not one scalar:
v_n=c/sqrt(n), c in H. The gap acts on its orthogonal complement.

## 2. Three elementary arithmetic estimates

We give the arithmetic facts in full so no explicit prime estimates have to be
imported. The inequalities 2/3<log2<3/4 follow from midpoint/trapezoid bounds
for the strictly convex function 1/t on [1,2]. Also e<3 follows from its series.

Write psi(x)=sum_(q<=x)Lambda(q). For integer r>=1, the valuation of the central
binomial coefficient gives

    psi(2r)-psi(r) <= log binom(2r,r) <= 2r log2.

Indeed a prime power in (r,2r] contributes 1 to its relevant floor difference,
and all other floor differences are nonnegative. Summing at dyadic endpoints
and then using monotonicity proves psi(x)<3x for all x>=1. Further,

    sum_(q<=x) Lambda(q) floor(x/q) = log(floor(x)!),

so floor(x/q)>=x/q-1 yields

    M(x) <= log x+3,                                  x>=1. (7)

Here the empty sum at x=1 is included. This also proves the diagonal bound in
(5). These arguments reproduce the earlier factorial bound, rather than
extending its conclusion to a new arithmetic population.

Next, for y>=2 put

    B(y)=sum_(p<y) log p/(p-1).

Since sum_(p<y) log p/p <= M(y), and

    sum_(p<y) log p/[p(p-1)]
      <=sum_(n>=2) log n/[n(n-1)]
      <=sum_(r>=1) log(r+1)/r^2 <=3log2,

we have B(y)<=log y+3+3log2. The last sum is bounded by its first term plus the
integral: log(x+1)/x^2 is decreasing on [1,infinity), and its integral there is
2log2. For y>=16, 5log2>3 gives B(y)<3log y. For 5<=y<16 there are only the six
possible primes 2,3,5,7,11,13; log p/(p-1)<=log2, and 6log2<3log5. For 3<=y<5,
B(y)<=log2+(log3)/2<3log3; for 2<=y<3, B(y)<=log2. Thus in all cases

    B(y)<3log y.                                        (8)

Now set

    Z(y)=product_(p<y)(1-1/p)^(-1)
        =sum_(all prime factors of k < y) 1/k.

There are finitely many allowed primes, so this positive Euler sum converges.
Normalize its summands to a probability distribution. Its expected log k is
B(y). If B(y)>0, Markov's inequality gives probability at least 1/2 to
log k<=2B(y). Hence

    Z(y)/2 <= sum_(k<=exp(2B(y)))1/k <=1+2B(y),
    Z(y)<=2+4B(y)<16log y.                              (9)

At y=2, Z=1 and the same final bound holds directly. All exponents and the
whole smooth-number tail have been summed in (9); no finite smooth-number
enumeration is being substituted for it.

## 3. A prime-removal tree with a tunable weight

For n>1 let p(n) be its smallest prime factor and a(n) its full exponent there.
Let parent(n)=n/p(n)^a(n). This defines a rooted tree on S: divisor closure
keeps each parent in S. From the root to n, full prime-power blocks are added
in strictly DECREASING order of their prime bases. The depth is omega(n), the
number of DISTINCT prime factors, not Omega(n) counting multiplicity.

If v is a nonroot vertex with smallest prime p, every descendant is v*k with
all prime factors of k STRICTLY below p. In particular gcd(v,k)=1 and
omega(v*k)=omega(v)+omega(k). The height and additional restrictions from S
only remove descendants and therefore improve positive upper bounds.

Put Delta_v=f(v)-f(parent(v)). Fix any alpha>1. On the path to n,
weighted Cauchy--Schwarz for Hilbert vectors gives

    ||f(n)-f(1)||^2
      <=[sum_(v on path(n))alpha^omega(v)]
         [sum_(v on path(n))alpha^(-omega(v))||Delta_v||^2]
      <=alpha/(alpha-1) *alpha^omega(n)
         sum_(v on path(n))alpha^(-omega(v))||Delta_v||^2.  (10)

The second step is the geometric sum at successive depths 1,...,omega(n).
After summing with weight 1/n, positive finite Fubini and the descendant
factorization prove

    sum_(n in S)||f(n)-f(1)||^2/n
      <=alpha/(alpha-1) sum_(v in S, v>1) ||Delta_v||^2/v
                        product_(q<p(v))(1+alpha/(q-1)).  (11)

Each exponent of q in a descendant contributes alpha once, explaining the
factor 1+alpha/(q-1), not (1-alpha/q)^(-1). This distinction is essential.
Bernoulli's convexity inequality for alpha>=1 gives

    product_(q<p)(1+alpha/(q-1))
        <=[product_(q<p)(1-1/q)^(-1)]^alpha
        <(16log p)^alpha.                              (12)

Thus (11) is at most

    [16alpha/(alpha-1) * (16log P)^(alpha-1)]
       sum_(v in S,v>1) (log p(v))/v ||Delta_v||^2.       (13)

Every term in the last sum is one of the ORIGINAL prime-power edges in E_S.
No new edge, product-measure norm, or random prime sign has been introduced.

Choose

    alpha=1+1/log(16log P)>1.

The bracket in (13) is 16e[1+log(16log P)]<kappa(P). This proves (2).
The weighted mean minimizes the squared distance from a constant, proving (3).
This is the source of the log-log loss: an adjustable weight prevents the
number of prime-removal steps from becoming a factor log N.

## 4. The literal matrix and a stable rigidity estimate

Expanding the definition of E_S after f(n)=sqrt(n)v_n gives

    E_S(f)=sum_(p,k,jp^k in S) log p
                  ||v_(jp^k)-v_j/sqrt(p^k)||^2.         (14)

For S={1,...,N}, its diagonal at n is

    sum_(p^k|n)log p +sum_(jp^k<=N, j=n)log p/p^k
       =log n+M(N/n),

and its off-diagonal is -C_N. This verifies (4) and fixes both cross orientations.
The vector h_N is in the kernel; equality of all prime edges forces it to be
the entire scalar kernel. The weighted variance in (3) equals ||Pi_N v||^2,
which proves the lower estimate in (5). From ||a-b||^2<=2||a||^2+2||b||^2,
L_N<=2D_N<=2(log N+3)I. Since L_N kills h_N, the upper bound is also valid
with Pi_N. This proves (5)-(6).

For any finite divisor-closed S the same conclusion holds with the exact
cutoff-dependent birth diagonal; its upper bound is 2(log max(S)+3).
Equivalently, if the COMPLETE arithmetic-edge error is at most epsilon^2,
there is one common c in H with

    sum_(n in S)||v_n-c/sqrt(n)||^2 <=kappa(P)epsilon^2.  (15)

Here c=Z_S^(-1)sum v_n/sqrt(n). This is a quantitative stability theorem for
the exact multiplicative relations, including all signed channel combinations.
The hypothesis is the total edge energy; small individual edges with no sum
bound are not sufficient. There is no assertion that the actual RH-facing
state has small edge energy.

## 5. Infinite fixed-prime reservoirs: depth is not a hidden dependency

Let S now be a countable divisor-closed set, all of whose prime factors are
at most a fixed finite P. It may have no bound on exponents. Its harmonic mass
Z_S is finite, bounded by product_(p<=P)(1-1/p)^(-1).
Define E_S by the nonnegative countable sum in (1), allowing infinity.

Applying (2) to S intersect [1,N] and passing monotonically to infinity gives
(2) for EVERY sequence f with finite entries, with extended values. If E_S(f)
is finite, this anchored bound puts f-f(1) in l2(S,1/n); finiteness of Z_S then
puts f itself in that space. Equation (3) follows. The SAME kappa(P) works
for every exponent-depth truncation and the full countable reservoir.

The graph form is closed: if f_j converges in l2 and the edge gradients are
Cauchy in their weighted l2 space, coordinate convergence identifies the
gradient limit with the gradient of f. The norm combining the two spaces is
therefore complete. It is densely defined since each finitely supported f
has finite energy (the prime set is finite and all geometric edge tails
converge). Normal contractions decrease each difference, so it is a Markov
form. Its associated nonnegative self-adjoint operator has gap at least
1/kappa(P) on the constants' orthogonal complement.

For clarity its Markov jump rates are exactly

    n -> n*p^k at rate (log p)/p^k when n*p^k is in S;
    n -> n/p^k at rate log p when p^k divides n.        (16)

Detailed balance holds with weight 1/n. The total birth rate is bounded by
sum_(p<=P)log p/(p-1). A finite interval has only finitely many births; between
births every death removes at least one prime factor. Hence explosion cannot
occur. The constant has zero energy, giving the conservative semigroup.
The spectral theorem yields, for mean-zero f,

    ||exp(-t A_S)f||_(l2(1/n)) <=exp(-t/kappa(P))||f||.  (17)

This is a genuine infinite arithmetic reservoir with a proved spectral gap.
It is NOT asserted to be the xi operator, nor to extend uniformly as P tends
to infinity. Only the displayed logarithmic dependence is claimed.

## 6. Scope of the improvement

The prior exact identity L_N>=0 had no quantitative inverse bound. Equations
(5) and (15) provide one for the full coefficient space, while Section 5
removes exponent-depth dependence entirely at fixed prime support. These
are unconditional theorems about the literal divisor source, not consequences
of RH or finite numerical spectra. Whether the gap is bounded below by a
positive absolute constant is NOT settled here; numerical scouting is not a
proof of that stronger assertion.

The remaining coherent channel cannot be thrown away. In particular
L_N-epsilon*h_N h_N^*/Z_S has the SAME positive restriction to h_N perpendicular
but a negative eigenvalue -epsilon. This is a finite algebraic control, not
an actual-xi counterexample. A map from the complete critical prime-discrepancy
or Weil form into these edges must account for its deterministic diagonal,
means, continuum and all other source terms. Such a global sign/upper-bound
map is NOT supplied here. APPLICATION.md gives the rigorous residual bound
that this gap DOES support, without pretending that those missing terms vanish.
