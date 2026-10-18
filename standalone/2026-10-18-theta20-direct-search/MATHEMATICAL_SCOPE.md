# What the implementation evaluates, and what would still constitute a proof

This note documents classical finite identities implemented by the search.
It asserts no new moment-realization theorem.

## 1. Complete grouped Gibbs measure

A group of N_i spins with a common observable weight a_i has magnetization
m_i in {-N_i,-N_i+2,...,N_i}, with multiplicity binomial(N_i,(N_i+m_i)/2).
With constant pair coupling J_ij between groups and J_ii within a group, the
complete probability weight of the magnetization vector is proportional to

    product_i binomial(N_i,(N_i+m_i)/2)
      exp[sum_i J_ii(m_i^2-N_i)/2 + sum_(i<j) J_ij m_i m_j].

The identity follows from expanding (sum spins)^2 and counting assignments.
No spin configuration is discarded by this compression. Couplings are counted
once per unordered edge, not once per ordered pair.

For singleton visible groups and additional zero-observable-weight hidden spins,
summing each hidden spin exactly contributes

    2 cosh(sum_i W_hi sigma_i).

This is an exact conditional sum. It does not assert that a graph containing
negative couplings is ferromagnetic. The normalized joint law remains essential.

## 2. Optional independent Gaussian

Some searches use Y=sum_i a_i m_i+g Z with Z a standard independent Gaussian.
For every integer r>=0 its conditional raw moment is exactly

    E[(y+gZ)^r]
       = sum_(0<=j<=r/2) binomial(r,2j) y^(r-2j)
                           g^(2j) (2j)!/(2^j j!).

Eleven-node Gauss–Hermite quadrature is polynomial-exact through degree 21
when its nodes and weights are exact. Here their evaluation is binary64;
there is no claim of directed enclosure. Gaussian convolution changes the
ansatz. A finite-spin count does not include a Gaussian as another spin.

## 3. Correct normalized Jacobian

For any parameter lambda changing only the Gibbs energy E_lambda,

    d_lambda E[f(Y)] = Cov(f(Y), d_lambda E_lambda).

When lambda also changes Y, add E[f'(Y) d_lambda Y]. This is immediate by
differentiating both the finite numerator and its partition function. For
an edge parameter J_ij the energy derivative is sigma_i sigma_j. For a hidden
coupling W_hi after summing the hidden spin, it is

    sigma_i tanh(sum_j W_hj sigma_j).

The implementation retains the expectation subtraction in the covariance.
Tests compare these derivatives against exact rational small-graph identities
and numerical differences. These are checks of assembly, not of a global path.

## 4. Orthogonal moment coordinates

Let p_0=1 and p_1=x/a_1, with

    p_(j+1)(x)=(x p_j(x)-a_j p_(j-1)(x))/a_(j+1).

For a symmetric reference law, nonzero recurrence coefficients make matching
E p_(2j)(Y)=0, 1<=j<=10, equivalent to matching its moments 2,...,20, provided
the reference recurrence is exact. Our recurrence is numerical and therefore
only defines a search objective. The derivative recurrence is differentiated
as a polynomial identity, not estimated by a finite difference in the search.

A small norm of the ten coordinates does not bound raw moment 20 by the same
number, and does not give an exact lower-moment match. Accordingly none of our
objective values is compared with #988/#992's certified raw moment-20 excess.

## 5. The theorem-level gate was not crossed

To turn a numerical candidate into a degree-20 theorem would require:

1. complete directed enclosures for the original infinite theta moments;
2. a rational parameter box remaining inside the required positive class;
3. a validated existence argument, such as interval contraction, for all ten
   matching equations, with their full Jacobian and source error included.

No candidate in this packet passed those gates. A favorable local derivative,
a tangent LP, a lower unconstrained objective, or solver termination is not a
substitute. Nor does failure in these chosen graph families imply that another
ferromagnetic graph cannot match degree 20.

Even a valid degree-20 construction would remain finite. The cofinal moment
feasibility premise in #981/#992 requires control at unbounded matching orders;
this packet supplies no such premise and no signed critical arithmetic estimate.
