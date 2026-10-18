# Primitive positive determinants and short-conductor zero budgets

**PROPOSED component mathematics. RH remains unproved. NOT PUSHED.**

This is an add-only continuation of GettysburgResearch/riemann #993,
head `5569defd8d77f1f8f3586b326577aacb384ffb23`. The parent Green import and
its historical source qualifications are unchanged. This directory is new.

## Main advance: estimate the actual determinant's complete regularization

The parent prime-sensitive integer

    A_N=product_(p^j<=N) p^(N-p^j)

now has a single rational positive-definite matrix realization,
`det H_N(0)=A_N^2`, assembled from primitive Fourier subspaces of cycle
Laplacians. Every prime power and every complementary mode is retained.
At rational mass `t=1/N^2` the matrices remain positive and their condition
numbers grow at most quadratically.

For every N>=2 and 0<=c<=1, the proposed complete argument proves

    |(1/2)log det H_N(c^2/N^2)-log A_N-N^2 B(c)|
                                    <=c^2(1+log N)/24.

The infinite constant B(c) is explicit, with two absolutely convergent
representations and a certified truncation bound. This is a LOGARITHMIC
error for the same source, not a family average or a discarded exceptional
set. The proof uses exact divisor regrouping and an endpoint-aware
second-order Euler summation bound. First-order quadrature would lose O(N).

Read **POSITIVE_DETERMINANT.md**, Theorems 1--2. These are proposed complete
component proofs, not a fresh proof of the prime number theorem or RH.

## What is still missing

For any one fixed c in (0,1], the ONE-SIDED upper estimate

    (1/2)log det H_N(c^2/N^2)
       <=(N-1)^2/2+N^2 B(c)+O_epsilon(N^(3/2+epsilon))

for every epsilon>0 is sufficient for RH, by the complete Landau/Mellin
argument in Section 4. It is equivalent to RH, not a weaker condition
already established by the regularization theorem. **OPEN-PH is unproved.**
The raw coordinate Hadamard attempt still costs order N^3, not N^2.
The matrix eigenvalues are NOT the zeta zeros, and their positivity does
not close the unknown centered logarithmic height.

## A separate actual improvement in the inherited arithmetic method

**SHORT_CONDUCTOR.md** proves the explicit prime-bias estimate

    sum_(p<=R,chi(p)=-1)log p/p
       <=(1/2)log R+(1/4)log |d|+4log ceil(log(2R))+30

whenever `R>=16` and `R>=64 sqrt(q) ceil(log(2R))^2`. The previous displayed
range began at R>=q. Thus the same useful leading coefficients now reach
scales `R=q^(1/2+eta)` for each fixed eta>0 and sufficiently large q.
The inherited rank/Frobenius lemmas remain explicit dependencies.

A full Laplace/Hadamard transfer gives a positive budget for ALL nontrivial
zeros of a fixed primitive real character, not just a real zero. Its
consequences are conductor-scaled disks near s=1. They are not a new fixed
zero-free half-plane and do not replace the missing ordinary-zeta height.

## Reproduction and status

Run `python -B replay.py` in this directory. It verifies the exact byte
manifest, ordinary/optimized reports, and eight executed corrupted models.
The report contains **3,370 finite predicates**. Thirty complete determinant
regularization comparisons use rational enclosures, including their infinite
constant tails. No binary64 approximation controls acceptance.

Read SOURCES_AND_REVIEW.md and VALIDATION.md before interpreting the checks.
There is no external referee acceptance, separate-agent review, Lean proof,
remote CI, actual zeta-zero computation, or whole-repository validation.
Publication details and the precise failed push capability are in PUBLICATION.md.
