# General unitary boundary recovery and a nonscalar symmetry gain

Status: proposed fourth companion; earlier frozen packets are unchanged.
Scope: the fixed canonical Koszul source operator of a nonexceptional
finite Segre rank profile, with unitary input automorphisms. Ordinary
Fredholm, regularized Fredholm, and ordered whole-grade products are kept
distinct. No arithmetic completion, priority, or RH/GRH claim is made.

The mixed-rank packet at `4499c6e44d425b6e43fbf004f2750123a9b20c31`
proves the source construction and regularization statements used below.
The critical packet at `f8b385d69c8b5eea13ef7f474a23835bf0dbbd2f`
proves identity/scalar boundary recovery. This note closes its stated
general-unitary boundary gap and provides an explicit nonscalar example
whose whole-grade convergence extends beyond the uniform trace-class disk.

## 1. The fixed operator and its finite grade cutoff

Let rho be the sharp trace-class radius of the source operator
`K_g(t)|M_n=t^n rho_n(g)`. For every unitary g, F_g is holomorphic on
|t|<1, nonzero on |t|<rho, and F_g(0)=1. The same operator has the
second regularized superdeterminant D_(2,g), holomorphic and nonzero on
|t|<sqrt(rho). Define the actual finite source product

    D_(N,g)(t) = product_(n<=N,n even) det(1-t^n rho_n(g))
                  / product_(n<=N,n odd) det(1-t^n rho_n(g)). (1.1)

Its canonical block logarithm is defined by the power-series logarithm of
each individual matrix block, valid for |t|<1. This is not necessarily
the principal logarithm of the entire finite product.

Write

    P_g(t)=sum_(n>=1) p_n(g)t^n,
    p_n(g)=(-1)^(n+1) tr(rho_n(g)).                    (1.2)

The source/PBW identity and the definition of det_2 give, near zero,

    P_g(t) = log F_g(t)-log D_(2,g)(t).                (1.3)

There is also an exact finite identity

    log D_(N,g)(t)
       = sum_(n=1)^N p_n(g)t^n + log D_(2,N,g)(t),     (1.4)

where D_(2,N,g) regularizes those same first N source grades. On every
closed disk strictly inside |t|<sqrt(rho), the final term in (1.4)
converges locally uniformly to log D_(2,g). Its tail is bounded by the
same absolutely summable j>=2 block-log series used in the second packet.

## 2. Boundary zeros determine the cutoff rate, without redefining the parent

### Theorem KOSZUL.UNITARY_BOUNDARY_RECOVERY

Fix a unitary input g. Let `rho<=s<sqrt(rho)` and suppose F_g has no
zeros in |t|<s. Let Z be its finite set of zeros on |t|=s, and let
m_tau be the multiplicity of a zero tau in Z. Then:

1. The canonical whole-grade logarithm and product converge locally
   uniformly to log F_g and F_g on |t|<s.
2. D_(N,g)(t) converges to F_g(t) on |t|=s away from Z, uniformly on
   closed arcs avoiding Z.
3. At each tau in Z,

       N^(m_tau) D_(N,g)(tau)
        -> exp(-m_tau gamma) (-tau)^(m_tau)
                        F_g^(m_tau)(tau)/m_tau!,       (2.1)

   a finite nonzero complex number.

The theorem always applies at s=rho. Thus it covers every unitary input
on the original critical circle, including an empty boundary zero set
and boundary zeros of arbitrary finite multiplicity. It does not replace
K_g by an operator fitted to those zeros.

#### Proof

The zeros of F_g are isolated because F_g(0)=1, and F_g is holomorphic on
a larger disk. There is therefore eta with `s<eta<sqrt(rho)` such that
the only zeros in |t|<eta are the finitely many members of Z. Set

    H_g(t) = F_g(t) / product_(tau in Z)(1-t/tau)^(m_tau).

This is holomorphic and nonzero on |t|<eta, and H_g(0)=1. Define there
the zero-at-origin logarithm

    V_g(t) = log H_g(t)-log D_(2,g)(t).

Equation (1.3) gives, as a Taylor identity,

    p_n(g) = [t^n]V_g(t) - sum_(tau in Z) m_tau/(n tau^n). (2.2)

Insert (2.2) into (1.4). The result is

    log D_(N,g)(t)
      = -sum_(tau in Z) m_tau sum_(n=1)^N (t/tau)^n/n
           + B_(N,g)(t),                              (2.3)

where B_(N,g) tends locally uniformly on |t|<eta to log H_g.
Indeed its two terms are the Taylor cutoff of V_g and the finite det_2
logarithm. The source dimensions give absolute convergence of the latter
on |t|<sqrt(rho), independently of this factorization.

For |t|<s the logarithmic sums converge normally. On |t|=s away from
Z, Dirichlet summation makes them converge uniformly on closed arcs
separated from Z; the relevant geometric partial sums are uniformly
bounded by `2/|1-t/tau|`. Exponentiation proves assertions 1 and 2.

At t=tau_0, the corresponding sum in (2.3) is `-m_tau0 H_N`. Every
other logarithmic sum has a convergent boundary value. Since
`H_N-log N -> gamma`, multiplying the product by N^(m_tau0) gives

    exp(-m_tau0 gamma) H_g(tau_0)
         product_(tau != tau_0)(1-tau_0/tau)^(m_tau).

The last two factors equal
`lim_(t->tau0) F_g(t)/(1-t/tau0)^(m_tau0)`.
Taylor expansion gives exactly the derivative in (2.1). The product is
nonzero by the definition of multiplicity. Complex logarithm continuations
may differ by multiples of 2 pi i, but their exponentials and the explicit
derivative formula are single valued. This proves the theorem.

This factorization is used to prove convergence and compute its rate.
The algebra, quadratic-dual modules, Hilbert operator, and cutoff in (1.1)
were already fixed before any zeros were identified.

## 3. A native involution improves whole-grade convergence

Let dim V=2, dim W=k>=3, and take the specific unitary input

    A=diag(1,-1) on V,       B=I_k on W.

For the same Segre source as before,

    h_n(A)=sum_(j=0)^n (-1)^j
           =1 if n is even, and 0 if n is odd,
    h_n(I_k)=binom(n+k-1,k-1).

Consequently its exact scalar series is the even part of the binomial
series, directly from the source coefficients:

    F_g(t) = [(1-t)^(-k)+(1+t)^(-k)]/2
           = E_k(t)/(1-t^2)^k,
    E_k(t) = [(1+t)^k+(1-t)^k]/2
           = sum_j binom(k,2j)t^(2j).                 (3.1)

There is no cancellation with the denominator: `E_k(1)=E_k(-1)=2^(k-1)`.
The finite zeros correspond to

    [(1+t)/(1-t)]^k = -1.

The change of variables is nonsingular away from t=1; the possible value
-1 of its ratio corresponds to infinity, not a missing finite zero.
All finite roots are simple. The pair closest to zero is

    tau_+ = i sigma,  tau_- = -i sigma,
    sigma = tan(alpha),       alpha=pi/(2k).           (3.2)

### Theorem KOSZUL.INVOLUTION_RADIUS_GAIN

For every integer k>=3,

    rho=1/(k-1) < sigma < sqrt(rho).                   (3.3)

The source Hilbert operator still has trace-class radius rho. However,
the canonical whole-grade logarithmic series converges absolutely and
locally uniformly on |t|<sigma, recovering F_g there. This is its exact
centered disk of absolute locally uniform block-log convergence.
On |t|=sigma, the ordered finite products recover F_g away from tau_+
and tau_-. At either of those points,

    N D_(N,g)(tau_+/-)
      -> exp(-gamma) k sin(alpha) cos(alpha)^(k+1).    (3.4)

This positive constant is `27 exp(-gamma)/32` for k=3. It is a rate
constant for the same finite source cutoff, not an ordinary Fredholm
determinant evaluated outside its trace-class disk.

#### Proof

For k>=3, `tan(alpha)>alpha=pi/(2k)>1/(k-1)` since pi>3 and
`3(k-1)>=2k`. Also `sin(alpha)^2<pi^2/(4k^2)<3/k^2<=1/k`, using
pi^2<12. Thus `tan(alpha)^2<1/(k-1)`, proving (3.3).

The zero description following (3.1) proves that there are no zeros
inside sigma, and the two boundary zeros are simple. The general theorem
therefore applies at s=sigma.

To check absolute block-log convergence, (1.3) shows that P_g is
holomorphic on |t|<sigma: F_g is zero-free there and D_(2,g) is zero-free
on the larger disk sqrt(rho). The first-order terms in each block log
are the coefficients of this normally convergent power series. All
j>=2 terms converge absolutely on |t|<sqrt(rho), by the operator estimate.
This proves absolute locally uniform block-log convergence inside sigma.
A larger centered disk of such convergence would produce a holomorphic
logarithm whose exponential equals F_g and is nonzero at tau_+ and tau_-,
contradicting their zeros. This establishes exactly the stated radius.
It does not assert failure of the exponentiated product at every individual
complex point outside that disk.

For the constant, (3.1) and (3.2) give

    E'_k(i tan alpha) = i k cos(alpha)^(-(k-2)),
    F'_g(i tan alpha) = i k cos(alpha)^(k+2).

Indeed `1 +/- i tan alpha = sec(alpha) exp(+/- i alpha)` and
`k alpha=pi/2`. Multiplication by `-i tan alpha` gives
`(-tau_+)F'_g(tau_+)=k sin(alpha)cos(alpha)^(k+1)`.
Conjugation gives the same positive value for tau_-. Formula (2.1)
with m=1 proves (3.4), including k=3.

## 4. The improvement is trace cancellation inside genuine source modules

The involution A is conjugate to -A. The latter differs by the central
scalar -1 on V, which acts on the degree-n parent M_n by (-1)^n.
Consequently

    tr(rho_n(g))=0 for every odd n.                    (4.1)

Let sigma be as above. After subtracting the two closest zero logarithms
from P_g in (1.3), the remainder is holomorphic on some disk of radius
eta>sigma. Equation (2.2) therefore gives, for any smaller fixed such eta,

    tr(rho_(2m)(g))
        = (-1)^m sigma^(-2m)/m + O(eta^(-2m)).          (4.2)

The error radius may depend on k. By contrast, the actual parent
dimensions satisfy

    dim M_(2m) ~ (k-1)^(2m)/(2m).

Their trace-to-dimension ratio therefore decays exponentially, since
rho/sigma<1. The gain in the whole-grade product arises from this
unitary character cancellation. It does not remove any Hilbert states,
alter their singular values, or improve the ordinary Schatten thresholds.

In particular the finite-grade determinant for an involution is computable
from the two genuine eigenspace multiplicities

    mult(+1 on M_n)=(epsilon_n+tr(rho_n(g)))/2,
    mult(-1 on M_n)=(epsilon_n-tr(rho_n(g)))/2.          (4.3)

These are nonnegative integers because the action is a genuine involution,
not because a scalar factorization happens to admit formal exponents.
The replay computes characters from native symmetric-power coefficients
and the source PBW/Adams identity, and independently checks degrees 1--3
against the actual frozen Lie quotient.

## 5. Scope left open

The theorem resolves whole-grade boundary recovery for general unitary
inputs on |t|=rho, and on any larger first-zero circle below sqrt(rho).
It does not classify which unitary tuples place zeros on the original
critical circle, nor determine every tuple's maximal possible ordered
product domain beyond the second-regularization region. Exceptional
pointwise product limits outside the stated analytic disk are not decided.

All source-freeze and operator distinctions remain in force. The results
do not identify an arithmetic prime-indexed object or prove its conductor,
archimedean completion, functional equation, or critical-line zeros.

## 6. Exact finite remainder bounds for the nonscalar `(2,3)` control

For k=3,

    F_g(t)=(1+3t^2)/(1-t^2)^3,
    P_g(t)=log(1+3t^2)+V(t),
    V(t)=-3log(1-t^2)-log D_(2,g)(t).                  (6.1)

The remainder V is holomorphic on |t|<1/sqrt(2), even though F_g has
already vanished at +/-i/sqrt(3). At r=2/3 it satisfies |V(t)|<=C, where
the following entirely rational bound is used by the replay:

    C = 12/5 + (3/2)[sum_(n=1)^64 epsilon_n(4/9)^n
                         +27(8/9)^65].               (6.2)

Indeed `3|log(1-t^2)|<=3r^2/(1-r^2)=12/5`. The absolute det_2
logarithm is bounded by `sum_n epsilon_n r^(2n)/[2(1-r)]`.
For n>64, the source bound epsilon_n<=3*2^n gives the last geometric
tail in (6.2). This is a proof-controlled finite truncation, not an
empirical supremum.

At tau=i/sqrt(3), the degree-N Taylor cutoff of log(1+3t^2) is exactly
`-H_floor(N/2)`. The Cauchy estimate from (6.2), together with
`|tau|/r=sqrt(3)/2<7/8`, bounds the omitted V Taylor terms by
`8C(7/8)^(N+1)`. The omitted det_2 grades are bounded by
`(45/4)(2/3)^(N+1)`: use |tau|<3/5 and sum
epsilon_n |tau|^(2n)<=3(2/3)^n. Therefore

    |log D_(N,g)(tau)+H_floor(N/2)-log(27/64)|
       <= 8C(7/8)^(N+1)+(45/4)(2/3)^(N+1).            (6.3)

This holds for odd and even N. It explains the factor two between the
regular part 27/64 and the cutoff constant 27 exp(-gamma)/32, since
`N exp(-H_floor(N/2)) -> 2 exp(-gamma)`.

For a real 0<t<1/sqrt(3), also take t<3/5 as in the bounded replay.
Put `a=3t^2`, `b=3t/2`, and m=floor(N/2). The analogous discrepancy
between log D_(N,g)(t) and log F_g(t) is at most

    a^(m+1)/[(m+1)(1-a)]
       + C b^(N+1)/(1-b)
       + 3(2t^2)^(N+1)/[2(1-t)(1-2t^2)].             (6.4)

These are respectively the scalar-root logarithm tail, the V Taylor
tail, and the det_2 grade tail. The stated domain makes every denominator
positive. The replay uses t=11/20, strictly beyond trace class, and an
independent held-out rational input.

Finally, actual finite involution determinants are evaluated as logarithms
with their eigenspace multiplicities (4.3). At t=tau, odd grades have
equal plus/minus dimensions and combine into
`(1-tau^(2n))^(epsilon_n/2)=(1+3^(-n))^(epsilon_n/2)`.
Even grades use `tau^n=(-1/3)^(n/2)` directly. Every block argument is
positive rational. The elementary log1p expansion has remainder

    |log(1+u)-sum_(j=1)^L (-1)^(j+1)u^j/j|
      <= |u|^(L+1)/[(L+1)(1-|u|)],       |u|<1.

Outward rational rounding occurs after multiplication by the source
multiplicity. Neither exponentially large state expansion nor exponentiation
by that multiplicity is needed. Equations (6.3)--(6.4), not numerical
curve fitting, supply the acceptance intervals.
