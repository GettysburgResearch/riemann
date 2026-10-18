# What a cofinal finite-model construction must allow to escape

Status: **PROPOSED elementary architecture obstructions.** These do not
obstruct any stated finite certificate or prove/disprove RH. They explain
why finite feasibility cannot be promoted to an unbounded-order construction
by freezing every convenient numerical constraint.

## 1. Bounded diameter and uniformly positive couplings force bounded support

Consider a zero-field ferromagnetic Ising TREE. Suppose every edge correlation
q_e=tanh J_e is at least q_0>0, the diameter is at most D, and

    Y=sum_i w_i sigma_i, w_i>=0, Var(Y)<=V.

On a tree the hub/edge-product parametrization gives exactly

    E sigma_i sigma_j=product_(e in path(i,j))q_e >=q_0^D.

Since E Y=0, including the diagonal and every cross term yields

    V>=E Y^2>=q_0^D (sum_i w_i)^2.

Consequently the entire observable has the uniform support bound

                     |Y|<=sqrt(V)q_0^(-D/2).             (1)

This remains true when some vertices have zero observable weight. A hub and
dimer tree has diameter at most four, regardless of its component count.

The actual original-theta density is strictly positive on every real
interval, and therefore has unbounded support. No uniformly bounded-support
sequence can match its moments at cofinal orders. Indeed if |Y_j|<=H, then
every fixed limiting even moment is at most H^(2r). If the target has positive
mass beyond some H'>H, its 2rth moment is at least p(H')^(2r), contradicting
that bound for sufficiently large r.

Thus any successful cofinal construction in this positive-weight tree
architecture must permit at least one of: edge correlations tending to zero,
diameter tending to infinity, or a growing variance normalization. With the
target variance fixed at one, the last option is unavailable. Each finite
model may of course retain strictly positive couplings. Uniform positivity
ACROSS the cofinal sequence is the extra constraint that fails.

The numerical lower edge bound 10^(-11) in the degree22 certificate is a
finite statement. This note does not impose it as an unbounded-order
requirement, and does not invalidate that certificate.

## 2. The original theta law has no nondegenerate Gaussian convolution factor

Let X have characteristic function xi(1/2+iz)/xi(1/2). Its real moment
generating function is

    M_X(t)=xi(1/2+t)/xi(1/2).

The classical completed-zeta formula and Stirling's formula give

    log M_X(t)=(t/2)log t+O(t)=o(t^2), t tends to +infinity.        (2)

This uses no zero-location hypothesis: for large positive real s, zeta(s)
is positive and tends to one, and Gamma(s/2) has its ordinary real Stirling
asymptotic.

Suppose X=G+Z in distribution, independently, where G is Gaussian of
variance v_G>0. The finiteness of M_X on the entire real line forces M_Z
finite there by independence and Tonelli. All variables have finite first
moments. Jensen's inequality and E G+E Z=0 imply

    M_X(t)=exp(t E G+v_G t^2/2) M_Z(t)
                              >=exp(v_G t^2/2), t real.

This contradicts (2). Hence v_G=0 in every Gaussian convolution factor.
The same statement holds after standardizing X by its positive variance.

## 3. A necessary condition on independent fair-spin padding

Suppose models are genuinely independent sums Y_N=S_N+Z_N, where

    S_N=a_N sum_(j=1)^(m_N) epsilon_j,
    a_N tends to zero, m_N a_N^2 tends to v_0>0,

the fair signs are independent, S_N is independent of Z_N, the models are
centered symmetric and Var(Y_N)=1. Suppose Y_N converges in distribution to
the standardized original-theta law.

Then S_N converges to a Gaussian of variance v_0, by its explicit product
characteristic function. Independence gives Var(Z_N)<=1, so the Z_N laws
are tight. Take a weakly convergent subsequence. Passing to the product
characteristic functions makes the theta target a convolution of that
Gaussian and the limiting Z law, contradicting Section2.

Therefore an infinitesimal independent fair-spin bulk cannot retain positive
variance in such a cofinal construction. Its variance must vanish, or the
architecture must retain an interaction that prevents this independent
Gaussian factorization.

The connected degree22 model is NOT an independent unconditional sum: its
components share a fair hub. No independent-sum obstruction is applied to
that law. Any argument that hub correlations disappear in a limiting design
must first prove the required approximation and independence; it cannot be
assumed because the finite hub correlation is numerically small.

These are design constraints for the next construction. They do not replace
the open task of obtaining a cofinal sequence of real-zero or strip-confined
models with actual original-theta moment convergence.
