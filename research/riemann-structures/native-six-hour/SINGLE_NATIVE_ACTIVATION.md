# One final activation on cofinal eleven-prime sources

The exact arithmetic-shape atlas changes its support at eleven primes.
For r=11,13,15 the unique leading optimizer is the single central vertex.
All inactive inequalities are strict. This packet proves that sufficiently
tight actual prime clusters have that same exact minimizing vertex for the
full original kernel. Every source factor allocation and the physical
multiplier remain present.

This is a finite-arity theorem with cofinal actual-prime realizations.
It is not an all-arity classification, a growing principal-moment estimate,
or identification with the complete retained-gamma source.

## 1. Primitive source and independent finite calculation

Use the squarefree native source and cardinality separation of
HIGHER_NATIVE_CLUSTER_ATLAS.md at
755b27c2c9747f3db255238c59c2622dee6cad8b. For r primes and K their product,
a monotone source path has activation q in the simplex, and the coefficient
of factor allocation S is

    v_S = (-1)^r 2^(1-r) q(S),  q(S)=sum_(i in S) q_i.

It carries 1/sqrt(K) in the original Mellin measure. For arithmetic shape
x_i=i, i=0,...,r-1, put H(q)=q^T B q, with

    B_ij = sum_(k,S,T: |S|=|T|=k, i in S, j in T) |sum S-sum T|.       (1)

The discovery is frozen at39d689b7485a423a1e0323a755ffc6a68ee084ed.
It uses the complete incidence polynomials
u v^i product_(j!=i)(1+u v^j), followed by exact distance-prefix sums.
The final certificate independently enumerates EVERY subset for every
r=2,...,16, at most65536 subsets, groups equal subset sums, and rebuilds
every matrix entry by the cumulative-cut formula. Thus the higher arities
are not accepted solely because a recurrence and its own output agree.

Every reflection-group support is solved over the rationals. Reflection
invariance plus strict concavity from the singleton band implies that the
full optimizer is reflection invariant. Nevertheless the certificate checks
the KKT equations and inequalities in ALL original coordinates.

The exact results relevant here are:

| r | nonzero activation, zero-based index | smallest inactive Bq slack |
|---|---|---:|
|11|q_5=1|90|
|13|q_6=1|1858|
|15|q_7=1|22274|

For r=11 the entire slack vector is

    (6320,3856,2056,824,90,0,90,824,2056,3856,6320).

These are lambda-(Bq)_i, where lambda=(Bq)_m at the central index m.
At that vertex H has every inactive-minus-active gradient at most -2mu,
with mu from the table. Strict concavity proves uniqueness. This also
refutes the pre-run central-three hypothesis for every odd arity: its
failure at11 is retained in the original discovery, not removed by a
changed panel list.

For comparison, the held-out leading activations are
r=7: central (7/24,5/12,7/24);
r=9: central (3/16,5/8,3/16).
Every tested even r from8 through16 has central pair (1/2,1/2) and strict
inactive slacks. Those finite rows are certified but not extrapolated.

## 2. Stability estimate for the original kernel

Write C_r=binom(2r-2,r-1), A=144+64sqrt(2)>234, and
T_0=floor(r^2/4). Let actual primes obey

    log p_i = L + epsilon*i + e_i,
    |e_i| <= M epsilon^2,  M>0 fixed,                              (2)

with distinct cardinality bands separated as in the source theorem.
Their normalized shape x has ||x-(0,...,r-1)||_infinity<=eta=M epsilon.
Assume eta<=1/4 and put T=T_0+r/2. Then the largest same-cardinality
shape distance is at most T.

The exact source energy, after its positive physical scale is removed and
its constant band mass subtracted, is the maximization problem

    Phi(q)=H_x(q)+R(q),
    ||gradient R||_infinity <= 144 C_r T^2 epsilon/A,               (3)

provided 2epsilon T<=log2. This is the frozen original-kernel remainder,
not a replacement quadratic observation.

For two shapes at sup distance eta, each subset-sum distance in (1)
changes by at most2r eta. Each fixed i,j has W_k^2 terms in band k,
W_k=binom(r-1,k-1). Consequently

    |B_ij(x)-B_ij(x_0)| <= 2r C_r eta,
    ||gradient H_x(q)-gradient H_x0(q)||_infinity <=4r C_r eta.     (4)

At the fixed central vertex q=e_m, equations (3)--(4) bound the change
of any inactive-minus-active gradient by

    8r C_r M epsilon + 288 C_r T^2 epsilon/A.                     (5)

Thus all inactive gradients remain strictly negative whenever this is
less than2mu. No active-coordinate implicit-function argument is required:
there is only one active coordinate, and its mass is exactly one.

A completely explicit sufficient threshold is

    D = 4r C_r M + (144/234) C_r T^2,
    epsilon_0 = min(1/(4M), 1/(3T), mu/(2D)).                    (6)

For 0<epsilon<=epsilon_0, (5) is at most mu, while every original gap
was at most -2mu. Also2epsilon T<=2/3<log2 and eta<=1/4.
The complete KKT inequalities hold at the central vertex. The original
energy is strictly convex because its singleton band is a Gram form of
distinct exponentials in the nonzero absolutely continuous native measure.
Therefore its unique simplex minimizer is EXACTLY

    q=e_m,                                                       (7)

not merely e_m+O(epsilon). The finite checker records the rational bounds
in (6) for M=1; their general-M validity is the proof above.

## 3. Cofinal physical prime families and source realization

Choose epsilon_j decreasing to zero. For each fixed j, ordinary PNT gives
primes in every disjoint interval

    [X exp(epsilon_j*i), X exp(epsilon_j*i+M epsilon_j^2)]

once X is sufficiently large for that fixed j. Choose X successively
large enough for all intervals and cardinality separation. This is a
diagonal sequence of fixed-relative-interval PNT consequences, not a
uniform theorem for shrinking intervals. It supplies cofinal actual prime
tuples satisfying (2) and eventually (6), for each r=11,13,15.

The vertex q=e_m is an actual path: while the central coordinate remains
zero, move every other prime coordinate from zero to one; then activate
the central coordinate. All original local half-geodesic factors remain.
The final derivative measure is still2 ds. The factor coefficients become

    v_S = (-1)^r 2^(1-r) * 1_(m in S).

Zeros arise from the actual source path. They are not a rule deleting
unwanted source atoms after observation. For eleven primes all2048 factor
allocations are still accounted for, with1024 nonzero coefficients.

The endpoint product current is unchanged by this deformation. Its
ratio observation changes. The physical energy is O(1/K), and the gain
over uniform activation is O(epsilon/K), consistently with the earlier
source normalization. A single tuple's activation optimum need not assemble
into one globally optimal schedule for many products. The earlier63-pair
shared-schedule packet addresses a different finite question.

## 4. Evidence and boundaries

The artifact checks exact source matrices, every declared finite support,
full KKT slacks, rational thresholds and original physical constants.
It authenticates the primitive theorem and the frozen discovery producer
before executing any inherited source. Typed canonical JSON rejects
integer/Boolean/float aliases and nonfinite values.

The cofinal quantifier is proved above using the imported source remainder
and classical PNT. No high-arity actual prime search or ordinary numerical
quadrature is used to certify it. No assertion is made for r=17 or beyond.
