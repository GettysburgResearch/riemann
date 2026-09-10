# Direct completion attempt and the mixed-prime obstruction

Status: the proposed unconditional RH completion failed in this pass.
The exact entropy balance in PROOF.md is a component theorem, not an RH proof.
The arithmetic work W(X) has not been bounded at the required subpower scale.
No change to the historical proofs or reviewed status is made.

## 1. The attempted final inference

After the explicit O(log log X) nonlinear budget, the intended proof was:
show that the first-order prime-versus-continuum work is at most subpower,
then apply (3) and the parent's zero-detection theorem. I tried to obtain this
upper bound from bounded feedback and cancellation of successive prime
phases. The latter step is not justified by analytic mean identities.

The frequency variable y in this problem has the ONE-dimensional Cauchy law
mu(dy)=dy/[pi(1+y^2)]. It does not independently sample one phase per prime.
The following exact calculation locates the failure on the actual frequencies,
without inventing an alternative zeta function or hypothetical off-line zero.

## 2. Analytic prime moments agree; mixed moments do not

Let z_p(y)=exp(-iy log p). For any finite list of nonnegative integers k_p,

    integral product_p z_p(y)^k_p dmu(y)=product_p p^-k_p.   (1)

This agrees with a product of independent Poisson-circle laws having moments
E(z_p^k)=p^-|k|. Thus every finite analytic polynomial has the same mean under
the physical law and that independent product law. This explains why the
safe signed logarithmic mean is easy.

For arbitrary integer exponents k_p, however, write
m=product_(k_p>0)p^k_p and n=product_(k_p<0)p^(-k_p). Then

    E_physical product z_p^k_p =exp(-|log(m/n)|)
                               =min(m/n,n/m),
    E_independent product z_p^k_p=1/(mn).                 (2)

In the more general monomial Gram indexed by integers m,n, the two kernels are

    G_C(m,n)=min(m,n)/max(m,n),
    G_I(m,n)=gcd(m,n)^2/(mn).                            (3)

They agree when one index divides the other, but not in general. For the
actual primes 2 and 3,

    E cos(y log2)cos(y log3)=5/12,
    E cos(y log2) E cos(y log3)=1/6,
    Cov=1/4.                                            (4)

Both the physical and independent kernels are PSD, but their difference on
indices 2,3 is [[0,1/2],[1/2,0]], with eigenvalues +/-1/2. Consequently neither
one dominates the other with coefficient one. The nonlinear feedback
 tanh(U_(x-)) contains mixed/conjugate phase dependence. Identity (1) cannot
be used in place of (2) when estimating its work.

The continuum frequencies log x also cannot be replaced silently by extra
independent prime coordinates. This is another source-binding obligation,
not supplied by positivity of the Euler factors.

## 3. No dimension-free comparison rescues that argument

There is no constant C, independent of the finite integer packet, with
G_C<=C G_I in PSD order, and no such constant for the reverse inequality.
Here is a complete elementary proof, not an inference from a matrix scan.

For k>=2 take M=k^3 and n_j=M+j, j=1,...,k. For the normalized constant vector,

    <1,G_C 1>/k >= k M/(M+k) >= k/2.

For distinct indices, gcd(n_i,n_j)<=|i-j|<k, so

    <1,G_I 1>/k <=1+(k-1)k^2/M^2<2.

A uniform first comparison would force C>=k/4 for every k, impossible.
Every index uses only ordinary prime factors; this is an actual finite
prime-phase polynomial packet, not an unrelated kernel.

For the reverse comparison take M,M+1 and the normalized difference vector.
Its two energies are

    1/(M+1),          1-1/[M(M+1)].

Their ratio tends to infinity as M increases. This proves the second claim.
In particular, a product-measure L2 estimate does not transfer with a fixed
constant to the physical Cauchy measure (or conversely).

This theorem does NOT refute a source-specific estimate for the particular
feedback in PROOF.md. It rejects only the universal measure-comparison and
independent-phase steps tried here. Proving a bound on that restricted class
would be real new arithmetic work. The formulas connect this entropy attempt
to the repository's physical-measure/near-collision warnings at an exact
kernel level, not merely by analogy.

## 4. The bounded feedback is not an upper estimate for its work

Equation (18) in PROOF.md constructs a positive kernel with density between
zero and one. Its off-diagonal real parts may have either sign. Replacing
them by diagonal bounds yields at most O(sqrt X), as explicitly calculated
there. The convex remainder gives W(X)>=-O(log log X), not W(X)<=O(log log X).
Neither inequality may be reversed.

A generic martingale argument would need a proved conditional-centering law
for each new prime phase relative to the previous source. Equation (4)
refutes such centering for the actual Cauchy phases even after subtracting
their means. It does not prove that every more sophisticated arithmetic
martingale or transport construction is impossible.

I also considered the PNT discrepancy estimate supplied by the parent. It
remains E(X)<<1+sqrt(X)exp(-c sqrt(log X)), with unspecified positive constants.
By (3), it gives a classical-scale W upper bound. Its positive power of X
still fails the needed estimate. No finite verified height or numerical trend
changes that unbounded exponent.

## 5. What should be reviewed

Review the full-cutoff chain rule, the pre-jump convention, the complete
higher-prime-power bounds, the all-frequency initial estimate, and the exact
physical-versus-product phase calculation. The last requested theorem remains

    W(X)<=C_epsilon X^epsilon for every epsilon>0,

or a sufficient unbounded subsequence. It has NOT been proved. The original
critical source map still has no proved full-domain extension. There is no
unconditional RH conclusion in this packet.

An independent reviewer can validate the supplied component proofs; they are
not being asked to fill a missing central estimate. No external novelty or
priority claim is made for the convex identity, Poisson law, or Hardy criteria.
