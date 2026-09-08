# Exact growth of the mixed-sign debt: a finite-exception-sensitive RH criterion

Status: PROPOSED COMPLETE IDENTITIES AND GROWTH THEOREM; independent review
required. The source-side subexponential estimate is OPEN, so RH is unproved.
Scope: one fixed v>0, every Bernstein row, all actual invariant zeros with
multiplicity; no linear-independence or simple-zero hypothesis.
Dependencies: the parent's genus-zero product, sum |A|^-1<infinity and
conjugation symmetry; finite Bernstein polynomial algebra and Vandermonde.
What was run: exact finite rational/complex-rational fixtures, not asymptotic
numerics or a zero census. No external novelty claim.

## 1. A row of all mixed inequalities, without discarding cancellations

Fix v>0 and write kappa_A=v/(v+A), as in the parent. Define

    B_(n,k)(v)=binom(n,k) H_(k,n-k)(v),      0<=k<=n,
    V_n(v)=sum_(k=0)^n |B_(n,k)(v)|,
    E_n(v)=sum_(k=0)^n max(0,-B_(n,k)(v)).                   (1)

All entries are real. The letter E here denotes negative mass, not an
expectation or a zero error term. The binomial factors are essential.
Since sum_A |kappa_A|<infinity,

    B_(n,k)=sum_A kappa_A binom(n,k)kappa_A^k(1-kappa_A)^(n-k),
    sum_(k=0)^n B_(n,k)=p_1^*(v)>0,
    V_n=p_1^*+2E_n.                                        (2)

The Bernstein degree-elevation identity gives

    B_(n,k) = (n+1-k)/(n+1) B_(n+1,k)
                    +(k+1)/(n+1) B_(n+1,k+1).              (3)

The coefficients of this map are nonnegative and each input column sums to
one. Consequently

    V_(n+1)>=V_n,       E_(n+1)>=E_n.                       (4)

This monotonicity concerns TOTAL negative mass, not any single mixed entry.
A negative mixed entry can never disappear without its debt being transferred
to higher rows. This is exact finite algebra.

## 2. A generating polynomial and its sharp geometric growth rate

Put

    Q_n(z)=sum_(k=0)^n B_(n,k) z^k
          =sum_A kappa_A [1-kappa_A+kappa_A z]^n.            (5)

Let

    R(v)=sup_A (|kappa_A|+|1-kappa_A|)
        =sup_A (v+|A|)/|v+A|.                              (6)

The ratio in (6) tends to 1 as |A| tends to infinity. It equals 1 exactly
for positive real A, since Re A>0. Thus R(v)>=1, and any nonreal A forces
R(v)>1. In that case the supremum is a maximum attained at a finite set.

**Theorem ASTRA-TC2-08 (exact exponential rate).**

    lim_(n->infinity) V_n(v)^(1/n) = R(v).                  (7)

If RH fails, then also

    lim_(n->infinity) E_n(v)^(1/n) = R(v)>1.                 (8)

Proof of the upper bound. Expand each summand of (5) in powers of z and
apply the triangle inequality only after forming its finite coefficient row:

    V_n <= sum_A |kappa_A|(|1-kappa_A|+|kappa_A|)^n
         <= [sum_A |kappa_A|] R(v)^n.                       (9)

For the lower bound when R>1, choose A_* attaining R and a unit complex z_*
which aligns kappa_* z_* with 1-kappa_*. Then

    |1-kappa_*+kappa_* z_*|=R.

Since R>1, z_* is not 1. The affine map kappa -> 1-kappa+kappa z_* is
injective. After combining equal A's and retaining their integer
multiplicities, set mu_A=1-kappa_A+kappa_A z_*. These distinct numbers tend
to 1. Therefore exactly finitely many, say mu_1,...,mu_d, have modulus R,
and all remaining mu_A have modulus at most r<R. For 0<=ell<d,

    Q_(n+ell)(z_*)=sum_(j=1)^d w_j mu_j^n mu_j^ell+O(r^n),   (10)

where w_j is the nonzero multiplicity times kappa_j. The error is uniform
in this finite range, since sum |kappa_A|<infinity and the mu_A are bounded.
The d-by-d Vandermonde (mu_j^ell) is invertible. Thus, for some c>0 and all
sufficiently large n,

    max_(0<=ell<d) |Q_(n+ell)(z_*)| >= c R^n.                (11)

There is no assumed independence of the phases. The finite block of powers
and Vandermonde inversion prevents simultaneous cancellation.
Now |Q_l(z_*)|<=V_l, and V_l is nondecreasing by (4). Hence
V_(n+d-1)>=cR^n. This proves the lower limit in (7). Equation (2) yields (8).

If R=1, all A are positive real. Every B_(n,k) is nonnegative, so V_n=p_1^*
for all n. This also proves (7). The theorem is complete.

## 3. An asymptotic endpoint, not another finite positivity claim

The preceding theorem proves, at any ONE fixed v>0,

    RH <=> R(v)=1 <=> lim V_n^(1/n)=1
       <=> for every epsilon>0, V_n=O_epsilon(exp(epsilon n)). (12)

The last bound is the remaining SOURCE-SIDE target. It has not been proved.
It is equivalent to RH, not asserted easier. Its practical advantage over
checking every individual H is that it permits signed cancellation and uses
one norm on a whole row. Even a single finite off-line quartet forces
positive exponential growth, so density-zero exceptions are not diluted.

The asymptotic condition is also equivalent to the same bound for 1+E_n.
Under RH E_n=0 identically; under failure its positive rate is (8).

## 4. An exact Hardy-norm formulation directly from the heat source

On the unit circle use normalized arclength. Parseval and Cauchy--Schwarz give

    ||Q_n||_L2 <= V_n <= sqrt(n+1) ||Q_n||_L2.                (13)

Consequently the norm ||Q_n||_L2 has exactly the same exponential rate R(v).
The parent's integral for p_l^* gives, with the ordinary Laguerre convention,

    Q_n(z)=integral_0^infinity exp(-x) S(x/v)
                                      L_n((1-z)x) dx.       (14)

Indeed the coefficient of p_(j+1)^* in (5) is binom(n,j)(z-1)^j, and
p_(j+1)^*=integral exp(-x)S(x/v)x^j dx/j!. This is only a finite sum;
all required integrals converge. No infinite polynomial expansion is assumed.

Near w=0 the complete row-generating function is

    sum_(n>=0) Q_n(z) w^n
      = v/(1-w) * h( v(1-wz)/(1-w) ).                      (15)

One can prove this first on an absolutely convergent disk using (5), or
integrate the Laguerre generating function in (14). For a single A,

    kappa/[1-w(1-kappa+kappa z)]
       = v/[A(1-w)+v(1-wz)],

which proves (15) with all normalization factors explicit.

An RH proof along this continuation would establish

    || integral_0^infinity exp(-x) S(x/v)L_n((1-z)x) dx ||_L2(|z|=1)
                          = exp(o(n))                       (16)

for the literal arithmetic heat S and one fixed v. This estimate is OPEN.
Replacing S by a positive majorant, discarding Laguerre phase, or assuming
analyticity of (15) on the entire unit disk would put the answer into the
hypotheses. The source-dependent intermediate cancellation must be proved.

## 5. Verified height bounds the rate but does not make it equal to one

Suppose V_H holds. For any remaining off-line A associated with gamma>H,

    |A|-Re A=(Im A)^2/(|A|+Re A)<=1/2.

It follows that

    R(v)^2 <= 1+v/(v+H^2)^2.                               (17)

The bound applies to the supremum because critical A's give exactly 1.
It is extremely close to 1 for large H, but strictly above 1. No finite
verification can turn this particular upper bound into (12).

For a fixed A=r exp(i alpha), the individual ratio in (6) is maximized over
v>0 at v=r, with value sec(alpha/2). Its square is the transformed
invariant atom 4rA/(r+A)^2 at that matching scale. This identifies the
same geometry as PR #785's Widder resolvent; it is NOT an independent source
of positivity or an independent proof route.

## 6. The attempt at closing (16), and its honest outcome

The all-order small-time proof controls the range where the real Gaussian
saddle overwhelms horizontal phase. The late-time theorem controls the range
where the low verified zero dominates. Those results establish positive
mixed rows through 10^15, plus additional open-ended time regions.
They do not imply (16): when n and a hypothetical off-line atom are matched,
the Laguerre polynomial can isolate phase information that the positive
pointwise heat estimate does not constrain.

The tempting estimate obtained by taking absolute values in (5) is (9),
whose exponential rate is precisely R(v), NOT 1. Inequality (17) makes this
loss small, not subexponential at fixed v. Letting v vary with n would change
the one-scale moment problem and does not prove the fixed-v criterion.

Thus this pass neither assumes nor claims (16). A further proof must bring
in the actual theta lattice or the Euler product beyond strip confinement,
zero counting, and a finite verified prefix. The exact row-growth theorem
specifies how a finite exceptional zero would defeat the requested estimate,
without using a statistical or phase-independence assumption.
