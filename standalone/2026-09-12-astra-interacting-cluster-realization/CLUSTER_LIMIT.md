# A whole-programme constraint: bounded lattice clusters lose their variance

Status: proposed analytic component theorem; independent review required.
This is a NECESSARY restriction on a specified Ising realization class, not
an RH proof or a no-go theorem for general weighted ferromagnets.

## 1. The statement and its precise scope

Consider any sequence of finite zero-field ferromagnets with J_ij>=0, observable
X_n=sum_i a_i sigma_i, a_i>=0, whose moments converge to the full theta moments
in PROOF.md. The variance is consequently bounded and converges to v>0.
The graph components are independent in the Gibbs law.

Fix positive integers K and B. Call a component C a (K,B)-lattice component
if it has at most K vertices and its observable weights can be written

    a_i = a_C b_i,   a_C>=0, b_i in {0,1,...,B} for i in C.

The b_i may vary between components and models. A zero observable component
has variance zero and is irrelevant. Couplings inside C are unrestricted
nonnegative finite numbers and may grow without bound along the sequence.

**Theorem ICR2 (escape of variance from bounded lattice components).**
For every FIXED K,B,

    sum_(C a (K,B)-lattice component) Var(X_(n,C)) -> 0.             (1)

In particular, if each component has a common observable weight (B=1), almost
all variance in any successful realizing sequence must lie in components of
unbounded size. One cannot finish by adding arbitrarily many independent
copies of uniformly bounded-size interacting clusters of this type.

This includes any collection of unequal-weight SINGLE spins and equal-weight
dimers, with arbitrary positive dimer couplings. It is stronger than a zero-
tripling restriction for independent signs. It does NOT include every bounded
cluster with arbitrary incommensurate weights. Growing integer weight ratios
also escape the specified K,B class. This scope limitation is essential.

## 2. Inputs: two classical theorems and elementary consequences

We import weighted Lee--Yang in the form stated in PROOF Section 6. In particular
for any component Y of variance V,

    E Y^4 <= 3 V^2,   E exp(hY)<=exp(V h^2/2), h real.              (2)

The zero-field pair correlations are nonnegative. A self-contained proof uses
exp(J sigma_i sigma_j)=cosh(J)[1+tanh(J)sigma_i sigma_j]: summing independent
signs leaves only parity-compatible terms, with nonnegative coefficients,
both in the partition denominator and in the pair-correlation numerator.
As a result, a nonzero (K,B)-component satisfies

    a_C^2 <= Var(X_C) <= (KB a_C)^2.                              (3)

The lower bound uses at least one b_i>=1 and includes all nonnegative covariance
terms; the upper bound follows from its support. We do not assume independent
spins within a component.

The only additional arithmetic input is the UNCONDITIONAL nonvanishing theorem
of Xiannan Li and Maksym Radziwill, *The Riemann-zeta function on vertical
arithmetic progressions*, arXiv:1208.2684, Theorem 4. For every alpha>0 and
beta real, a positive proportion (at least 1/3+o(1)) of integers l in [T,2T]
satisfy zeta(1/2+i(alpha*l+beta)) != 0. Only this consequence is needed:

    the real zeros of Xi do NOT contain any full infinite arithmetic
    progression with nonzero spacing.                             (4)

We do not reprove that analytic-number-theory theorem or invoke an unproved
linear-independence conjecture for zeta ordinates. No numeric zero is used.

## 3. No bounded lattice component can retain a positive variance

Assume otherwise. Pass to a subsequence with one chosen (K,B)-component Y_n
of variance at least epsilon>0. By (3), its SQUARED scales a_C^2 stay in a
compact subinterval of (0,infinity): bounded above by total variance and bounded
below by epsilon/(KB)^2. There are finitely many possible vertex counts and integer
weight patterns. Pass to fixed values of these and to a scale a>0.

Its finite probability vectors have a convergent subsequence, even if some
couplings tend to infinity. This gives a nondegenerate symmetric finite lattice
law Y, supported on integer multiples of a and with positive variance. Uniform
bounded support gives locally uniform convergence of its entire characteristic
functions. Lee--Yang and Hurwitz imply that chi_Y has only real zeros.

A nondegenerate finite lattice law has an exponential-polynomial characteristic
function of the form exp(i l0 a z) P(exp(i a z)), with P a polynomial having
nonzero constant and leading coefficients after removing a monomial. There
are at least two support points, so P has positive degree and at least one
nonzero root. Taking logarithms supplies zeros of chi_Y. Lee--Yang forces
those zeros to be real, so at least one gives the entire real progression

    z0 + 2pi j/a, j in Z.                                        (5)

A smaller spacing may occur; (5) alone suffices.

The sum R_n of all other components is independent of Y_n and has bounded
variance, hence is tight. On a further subsequence it converges weakly to R.
Characteristic functions give, for every real t,

    Xi(t)/Xi(0) = chi_Y(t) chi_R(t).

To justify the left limit from moment convergence, use the bounded-variance
Lee--Yang estimate (14) in PROOF.md and its complete Taylor-tail argument.
The passage is therefore not an arbitrary use of moment determinacy.
Equation (5) now makes Xi vanish on an entire arithmetic progression, contrary
to (4). We have proved

    max_(C a (K,B)-component) Var(X_(n,C)) -> 0.                  (6)

The maximum is zero if the indicated collection is empty.

## 4. The sum of their variances cannot hide in a Gaussian limit

Let S_n be the sum of all (K,B)-components and let t_n=Var(S_n), bounded by
the full variance. Pass to a subsequence with t_n->t. By (2),(6),

    sum_C E X_(n,C)^4
      <=3 [max_C Var(X_(n,C))] t_n -> 0.                         (7)

For each fixed real u, symmetry and Taylor's formula give

    chi_C(u)=1-u^2 Var(X_C)/2 + O(u^4 E X_C^4).

The maximal variance tends to zero, so all factors are positive and near one
for large n, and logarithms may be expanded at one. Summing their complete
remainders using (7) shows

    log chi_(S_n)(u) -> -t u^2/2.

Thus S_n converges to a centered Gaussian of variance t. The remainder R_n is
again tight and independent; a subsequential limit yields the convolution
factorization

    theta law = Normal(0,t) * law(R).                            (8)

This is a derived limit, not a Gaussian model substituted for the actual source.
The remainder is symmetric. All its exponential moments exist: the exponential
moment of the convolution (8) is finite and its Gaussian factor is positive.
Consequently for real h,

    M_theta(h) = exp(t h^2/2) E exp(hR) >= exp(t h^2/2).           (9)

But the ACTUAL theta law satisfies

    log M_theta(h) = O(|h| log(|h|+2)) = o(h^2), |h|->infinity.  (10)

For completeness (10) needs no RH. From the positive series (1), for t>=0,
phi(t)<=C exp(9t/2-pi exp(2t)), since the ratio of the full series to its
n=1 positive upper summand is bounded. Substitution u=exp(2t) bounds the
positive half of M_theta(h) by a constant times
Gamma((|h|+9/2)/2) pi^(-(|h|+9/2)/2). The negative half is the same bound by
evenness. The elementary factorial bound for this gamma integral gives (10):
for r>=1 take an integer k with r<=k<=r+1, split the integral at one and use
Gamma(r)<=1+k!, whose logarithm is O(r log(r+2)).

Equations (9),(10) imply t=0. Every convergent subsequence of the bounded
sequence t_n has limit zero, proving (1). This excludes a hidden Gaussian
variance reservoir as well as persistent finite lattice blocks. QED.

## 5. A weak-bridge version: connectedness alone is not enough

Suppose each graph can be partitioned into blocks of at most K vertices,
each with a common observable weight. Let eta_n be the SUM of all couplings
on edges joining different blocks. If eta_n->0, deleting those edges changes
the normalized Gibbs density by a factor between exp(-2eta_n) and exp(2eta_n).
Indeed the removed energy H_cut satisfies |H_cut|<=eta_n, and its partition
normalizer satisfies the same exponential bounds.

For any fixed even power, positivity gives

    |E_deleted X_n^(2r)-E_full X_n^(2r)|
       <=(exp(2eta_n)-1) E_full X_n^(2r) ->0.                    (11)

The moment on the right is bounded by the full variance via (14). Deleted
models would thus also realize all theta moments, while all their components
have at most K vertices and a common observable weight. Theorem ICR2 forces
their total variance to zero, contradicting its convergence to v>0.

**Corollary ICR3.** No such all-order realizing sequence can have eta_n->0
along an unbounded subsequence. In particular its minimal total connecting
coupling for these fixed-size homogeneous partitions has positive liminf
whenever such partitions exist at each n.

The assertion does not say that every edge must stay positive, supply a
numerical lower constant, or constrain partitions with growing block size.
It is also not the removable rank-one reserve in PR847, and not a spectral
mixing-time bound. The complete total bridge interaction is the quantity in
(11); many individually small bridges can have a large total.

## 6. What this suggests, and the unproved step

The new degree-fourteen model uses one real interaction, with a dimer variance
share of about 9.27%. Theorem ICR2 shows why repeatedly attaching bounded
lattice dimers cannot complete the programme: their aggregate variance must
ultimately move into larger correlated pieces (within that architecture).

A next construction should therefore enlarge the correlated component itself,
not merely increase the number of independent small components. Possibilities
include growing sparse blocks or unequal incommensurate internal weights.
These are research directions, not proved realizations. Nonnegative couplings,
lower-moment preservation, and actual reachability of the next theta target
must all be established. Neither the present seven-equation root nor the
necessary condition (1) proves an arbitrary-order extension or RH.
