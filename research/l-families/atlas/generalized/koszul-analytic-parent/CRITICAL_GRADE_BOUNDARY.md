# The critical operator ideal and the native grade-cutoff boundary

Status: proposed third companion, preserving both earlier source packets.
Scope: nonexceptional finite Segre rank profiles from
[the mixed-rank theorem](MIXED_RANKS_AND_REGULARIZATION.md).
Operator-ideal statements hold for every unitary input. Grade-cutoff
boundary recovery below is asserted for identity input and its scalar
phase twists, not for every unitary tuple. No ordinary Fredholm determinant
is assigned to a non-trace-class operator, and no RH/GRH claim is made.

Write `R=lambda_1>1` for the largest reciprocal Hilbert root and `rho=1/R`.
Here R is a number, distinct from the source algebra in the earlier notes.
Let `epsilon_n=dim M_n`. The previous proof supplies more than its leading
asymptotic: for some `theta<1`,

    epsilon_n rho^n = 1/n + e_n,       e_n=O(theta^n).   (1.1)

Indeed the secondary-root error is at most
`(d-1)(lambda_2/R)^n/n` when d>1, and the proper-divisor error is at most
`d R^(-n/2)`. Finitely many early degrees do not affect this estimate.

## 1. Critical singular values, including their block oscillation

Fix real p>=1 and any unitary g, and put `|t|=rho^(1/p)`.
The compact operator K_g(t) is not in S_p. Let its singular values in
decreasing order, with multiplicity, be `s_1,s_2,...`, and set

    J_n = sum_(k=1)^n epsilon_k.

The nth source grade contributes epsilon_n copies of `s_j^p=R^(-n)`.

### Theorem KOSZUL.CRITICAL_SINGULAR_DISTRIBUTION

As j tends to infinity,

    s_j^p is comparable to 1/(j log j).                (1.2)

There is no pointwise equivalence with a single constant: precisely,

    liminf j log(j) s_j^p = log(R)/(R-1),
    limsup j log(j) s_j^p = R log(R)/(R-1).             (1.3)

Moreover, with gamma the Euler constant,

    sum_(j=1)^N s_j^p
      = log log N + gamma + sum_(n>=1)e_n
          - log log R + o(1).                         (1.4)

In particular the ratio to log log N tends to one, whereas the ratio
to log N tends to zero. These statements are independent of g and of
the phase of t.

#### Proof

Since epsilon_n~R^n/n, elementary comparison of successive differences,
or reverse summation of the geometric tail, gives

    J_n ~ [R/(R-1)] R^n/n.                            (1.5)

For completeness, compare J_n with `b_n=R^n/n`. The increment of b_n
is `b_n[1-n/(R(n-1))]`, whereas the increment of J_n is epsilon_n~b_n.
The ratio of these increments tends to R/(R-1). Summing bounds with an
arbitrary fixed small relative error, and then discarding finitely many
initial terms, proves (1.5).

On the block `J_(n-1)<j<=J_n`, `s_j^p=R^(-n)` and j log j increases.
Using (1.5) at the two block ends gives the two limits in (1.3).
All sufficiently large epsilon_n are positive, so both endpoints occur.
This proves the comparability and the genuine block oscillation.

At a block end, (1.1) gives

    sum_(j<=J_n) s_j^p = H_n + sum_(k<=n)e_k
                      = log n + gamma + sum_k e_k + o(1).

Meanwhile (1.5) implies `log log J_n=log n+log log R+o(1)`.
The additional partial-block contribution is at most
`epsilon_n R^(-n)=1/n+o(1/n)`, hence tends to zero; replacing a block
endpoint by any intermediate N also changes log log N by o(1).
This proves (1.4) for every N, not only a subsequence.

For clarity, define the Schatten--Lorentz sequence condition here by

    S_(p,q): sum_(j>=1) j^(q/p-1) s_j^q < infinity, 1<=q<infinity;
    S_(p,infinity): sup_j j^(1/p) s_j < infinity.

Equation (1.2) and the elementary integral test immediately give

    K_g(t) in S_(p,q)  iff  q>p,                       (1.6)

with infinity allowed on the right. It is even in the vanishing weak
class `j^(1/p)s_j -> 0`, while failing S_p. These are sequence estimates;
no existence theorem for singular traces is needed or claimed. In
particular the zero log-normalized average in (1.4) is not a nonzero
trace certificate in disguise.

## 2. The source grading supplies a conditional boundary product

For identity input define the finite grade cutoff

    D_N(t) = product_(1<=n<=N, n even) (1-t^n)^epsilon_n
               / product_(1<=n<=N, n odd) (1-t^n)^epsilon_n. (2.1)

Every factor is defined and nonzero for `|t|<1`; on the critical circle
`|t|=rho` the finite products are unambiguous. The cutoff includes whole
source grades in their intrinsic increasing order. It does not claim
reordering invariance or separate convergence of the even and odd
ordinary determinant factors.

### Theorem KOSZUL.ORDERED_CRITICAL_PRODUCT

On `|t|=rho`, away from t=-rho, D_N(t) converges to F_1(t). Convergence
is uniform on every closed arc avoiding -rho. At the excluded point,

    N D_N(-rho) -> exp(-gamma) rho F'_1(-rho) > 0.      (2.2)

Consequently D_N(-rho) tends to zero at exactly order 1/N. These are
limits of canonically ordered finite source products, not ordinary
trace-class Fredholm determinants at the boundary.

#### Proof

Put `t=rho z`. Each block has modulus strictly below one for |z|<=1,
so its logarithm is the power-series branch. Expand (2.1) to obtain

    log D_N(rho z)
      = sum_(n=1)^N (-1)^(n+1) z^n/n + B_N(z),         (2.3)

where

    B_N(z) = sum_(n=1)^N (-1)^(n+1)e_n z^n
               +sum_(n=1)^N (-1)^(n+1)epsilon_n
                   sum_(m>=2) (rho z)^(nm)/m.          (2.4)

Choose eta>1 such that `eta theta<1` and `eta^2<R`.
The first sum in (2.4) then converges uniformly on smaller closed disks
inside |z|<eta by (1.1). The second is absolutely dominated there by
a constant times `sum_n epsilon_n (rho eta)^(2n)`, which converges
because `R(rho eta)^2=eta^2/R<1`. Thus B_N converges locally uniformly
to a holomorphic B on a disk containing the closed unit disk.

For |z|<1, the first sum in (2.3) tends to log(1+z), and ordinary
Fredholm recovery identifies

    F_1(rho z) = (1+z) exp(B(z)).                      (2.5)

By analytic continuation this identity holds on the common neighborhood
of the closed unit disk. On |z|=1 away from z=-1, the elementary
Dirichlet test gives convergence of the first sum to the continuation
of log(1+z), uniformly on closed arcs separated from -1: partial sums
of `(-z)^n` are bounded by `2/|1+z|`. Exponentiating (2.3) proves the
first assertion.

At z=-1, the first sum is exactly -H_N. Formula (2.3) therefore gives

    log(N D_N(-rho)) = log N - H_N + B_N(-1)
                       -> -gamma + B(-1).

Differentiating (2.5) at z=-1 gives `exp B(-1)=rho F'_1(-rho)`.
This number is positive: using the simple-root factorization from the
mixed-rank proof,

    rho F'_1(-rho)
      = product_(j>=2)(1-lambda_j/R)/(1+rho)^D > 0.    (2.6)

This proves (2.2), including its exact constant and sign.

For `(2,k)`, k>=3, rho=1/(k-1), and (2.6) is
`(1+rho)^(-(k+1))`. In particular the `(2,3)` constant in (2.2) is
`16 exp(-gamma)/81`. This is a consequence of the native grade cutoff;
it does not assign a trace to a divergent trace-class sum.

When each input matrix is scalar and their product phase is c, the action
on every degree-n parent is c^n. Replacing t by ct proves the same result
with the exceptional boundary point rotated to -rho/c. No such reduction
is asserted for nonscalar inputs.

## 3. Relation to the regularized determinant, and the remaining boundary

The second companion's det_p is holomorphic and nonzero at t=-rho for
every p>=2. Equation (2.2) is compatible with that fact: it uses a different,
explicitly ordered cutoff whose leading harmonic divergence retains the
scalar zero. The exact regularized counterterm accounts for the difference.

The source grading is essential to the statement. Arbitrary reorderings
of conditionally convergent factors are not covered. The full critical
boundary problem for general nonscalar unitary tuples remains open in
this packet. The operator is not trace class there, even when a scalar
grade-cutoff limit exists. Nothing here reaches the compactness boundary
|t|=1 or supplies arithmetic prime, conductor, or gamma-factor data.

## 4. Exact enclosures used by the companion replay

The finite controls use the rank strip `(2,q+1)` with integer q>=2,
rho=1/q. Its explicit Mobius formula gives, for n>1,

    |epsilon_n rho^n-1/n| <= q^(-floor(n/2)).

It also gives `epsilon_n<=3q^n`: for n>1 the stronger bound epsilon_n
<=q^n follows from (1.7) with d=1, while epsilon_1=2(q+1)<=3q.
Thus for N>=2 the omitted B-tail on |z|<=1 is bounded by

    delta_N = 2rho^(floor(N/2))/(1-rho)
                 +3rho^(N+1)/[2(1-rho)^2].            (4.1)

The first term bounds the sum of |e_n|, grouping even and odd indices.
For the second, bound the m>=2 logarithm tail by
`rho^(2n)/[2(1-rho)]` and sum `epsilon_n<=3q^n` over n>N.
In particular

    |log D_N(-rho)+H_N-log(rho F'_1(-rho))| <= delta_N.

For a unit complex z with `|1+z|>=1`, Dirichlet summation bounds the
omitted first term of (2.3) by `2/(N+1)`. Hence, if
`b=delta_N+2/(N+1)<1`,

    |D_N(rho z)/F_1(rho z)-1| <= b/(1-b).              (4.2)

Indeed the corresponding logarithm difference has modulus at most b,
and `|exp(w)-1|<=exp(|w|)-1<=b/(1-b)`. The exact Gaussian-rational
checks square both sides, avoiding uncertified square roots. The unit
phase z=-1 is excluded from (4.2) and belongs to the separate rate theorem.

For a positive rational x, range reduction writes x=2^k y with
1/2<=y<=2. With v=(y-1)/(y+1),

    log y = 2 sum_(j=0)^(L-1) v^(2j+1)/(2j+1) + error,
    |error| <= 2|v|^(2L+1)/[(2L+1)(1-v^2)].            (4.3)

The same formula at v=1/3 encloses log2. Combining intervals with the
integer k encloses log x, including k<0. Every outward grid rounding uses
integer floor or ceiling of an exact rational. For the block logarithms,
rounding occurs only after multiplying by epsilon_n; this avoids losing
precision through large multiplicities. These are rigorous rational
enclosures, not ordinary floating-point logarithms.

Finally `H_N-log(N+1)<=gamma<=H_N-log N`, by the integral comparison
for the defining harmonic limit. This also gives
`0<=H_N-log N-gamma<1/N`, which joins (4.1) to a finite enclosure for
the constant in (2.2). All finite controls use these proved tail bounds;
they do not infer convergence or the value of a limit by fitting data.
